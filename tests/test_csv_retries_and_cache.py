from unittest import mock

import pytest

from leetnotes import csv_source, repo


class _FakeResponse:
    def __init__(self, payload: bytes = b"col1\n"):
        self.status = 200
        self.headers = mock.Mock()
        self.headers.get_content_charset.return_value = "utf-8"
        self._payload = payload

    def read(self) -> bytes:
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def test_fetch_csv_retries_then_succeeds(monkeypatch):
    failures = [TimeoutError("first"), TimeoutError("second")]
    responses = [*failures, _FakeResponse()]

    urlopen = mock.MagicMock(side_effect=responses)
    sleeps: list[float] = []

    monkeypatch.setattr(csv_source.urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(csv_source.time, "sleep", lambda delay: sleeps.append(delay))

    data, charset = csv_source.fetch_csv("http://example.com/data.csv", max_attempts=3, backoff_factor=2)

    assert data == b"col1\n"
    assert charset == "utf-8"
    assert urlopen.call_count == 3
    assert sleeps == [1.0, 2.0]


def test_fetch_csv_gives_up_after_max_attempts(monkeypatch):
    urlopen = mock.MagicMock(side_effect=TimeoutError("network down"))
    sleeps: list[float] = []

    monkeypatch.setattr(csv_source.urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(csv_source.time, "sleep", lambda delay: sleeps.append(delay))

    with pytest.raises(RuntimeError) as excinfo:
        csv_source.fetch_csv("http://example.com/data.csv", max_attempts=4, backoff_factor=3)

    assert "Failed to download" in str(excinfo.value)
    assert urlopen.call_count == 4  # initial try + 3 retries
    assert sleeps == [1.0, 3.0, 9.0]


def test_write_bytes_if_changed(tmp_path):
    target = tmp_path / "artifact.bin"

    repo.write_bytes_if_changed(target, b"abc")
    first_mtime = target.stat().st_mtime_ns
    repo.write_bytes_if_changed(target, b"abc")
    assert target.stat().st_mtime_ns == first_mtime  # unchanged when content matches

    repo.write_bytes_if_changed(target, b"abcd")
    stats = target.stat()
    assert target.read_bytes() == b"abcd"
    assert stats.st_size == 4
    assert stats.st_mtime_ns >= first_mtime
