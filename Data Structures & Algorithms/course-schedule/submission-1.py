class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        NEW, VISITING, DONE = 0, 1, 2
        state = [NEW] * numCourses

        for start in range(numCourses):
            if state[start] != NEW:
                continue
            state[start] = VISITING
            stack = [(start, iter(prereqs[start]))]
            while stack:
                course, pres = stack[-1]
                pre = next(pres, None)
                if pre is None:
                    state[course] = DONE
                    stack.pop()
                elif state[pre] == VISITING:
                    return False
                elif state[pre] == NEW:
                    state[pre] = VISITING
                    stack.append((pre, iter(prereqs[pre])))
        return True