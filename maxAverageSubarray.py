class solution:

  def findMaxAverage(self, nums: List[int], k: int) -> float:
          n = len(nums)
          s = sum(nums[:k])
          answer = s
          for i in range(k, n):
              s += nums[i]
              s -= nums[i-k]
              answer = max(answer, s)
          return answer/k
