class Solution:
    def gcd(a, b):
        while b != 0:
                a, b = b, a % b
        return a

    def lcm(a,b):
        return abs(a,b) // gcd(a,b)

    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            lc = 1
            for j in range(i, len(nums)):
                lc = lcm(lc, nums[j])

                if lc == k:
                    count += 1
                if lc > k:
                    break

        return count
