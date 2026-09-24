class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        suo = 0
        sue = 0

        for i in range(1, n + 1):
            suo += 2 * i - 1
            sue += 2 * i

        while sue != 0:
            suo, sue = sue, suo % sue
        return suo
