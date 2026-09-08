class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position[i]: starting position in miles of i'th car
        # speed[i]: speed of i'th car miles/hour
        # target: position in miles of destination

        # car fleet: cars moving together
        # How many car fleets reach target?

        # If a car behind was going faster than car in front
        # it will form a fleet with the one ahead

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p,s in pairs:
            stack.append((target-p)/s) # time taken to reach target
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)