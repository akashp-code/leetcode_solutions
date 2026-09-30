class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True )
        energy = 0 
        answer = 0

        for actual , minimum in tasks:
            answer = max(answer, energy + minimum)
            energy += actual

        return answer
            
        