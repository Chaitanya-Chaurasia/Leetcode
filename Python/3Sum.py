class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # our logic
        # fix one element, and use two pointer solution over the rest of the array
        # also, for every fixed element, there can be duplicates which we need to account for.
        # since the list is sorted, we can simply modify pointers to reduce or increase sum depending on what the sum of
        #  previous 2 elements are.

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                if threeSum > 0:
                    k -= 1
                else:
                    j += 1
                    # j - 1 will always exists because min(j - 1) is i and i exists.
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res


        # this is a very slow solution
        # faster solution- use hashmap
        # easy approach -  maintain three different hashmaps with counts of each element
        # one for positive, negative and zeroes
        # we can kind of hardcode some bits of this logic:
        # if one zero exists, check if -x and x exist.
        # if at least 3 zeroes exists, add 3 zeroes to result
        # else, for all pairs of positive integers, check if -ve complement exixts.
        # do same with negative integers.
        # since one value can occur multiple times, we can store positive and negative elements in a set.
        # not a set of 0s though, because we need the count

        # res = set()
        # neg, zero, pos = [], [], []
        # for i in nums:
        #     if i > 0:
        #         pos.append(i)
        #     elif i < 0:
        #         neg.append(i)
        #     else:
        #         zero.append(i)

        # Neg, Pos = set(neg), set(pos)

        # if zero:
        #     for i in Pos:
        #         if -i in Neg:
        #             res.add((-i, 0, i))

        # if len(zero) >= 3:
        #     res.add((0, 0, 0))

        # for i in range(len(pos)):
        #     for j in range(i + 1, len(pos)):
        #         if -(pos[i] + pos[j]) in neg:
        #             res.add(tuple(sorted([pos[i], pos[j],-(pos[i] + pos[j])])))

        # for i in range(len(neg)):
        #     for j in range(i + 1, len(neg)):
        #         if -(neg[i] + neg[j]) in pos:
        #             res.add(tuple(sorted([neg[i], neg[j],-(neg[i] + neg[j])])))
        # return list(res)
