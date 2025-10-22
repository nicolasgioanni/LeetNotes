class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            courseToPrereq[course].append(prereq)

        path = set()

        def dfs(course):
            if course in path:
                return False
            elif not courseToPrereq[course]:
                return True
            else:
                path.add(course)

                for prereq in courseToPrereq[course]:
                    if not dfs(prereq): return False
                path.remove(course)
                courseToPrereq[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
