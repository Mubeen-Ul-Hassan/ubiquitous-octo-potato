# Boyer-Moore Majority ALGORITHM:
# (1) --> Create variables to store number and it's votes.
# (2) -->  Loop through each number:
#         a. If votes are 0, set the current number as the candidate and start voting (vote = 1).
#         b. If the current number matches the candidate, increase votes.
#         c. Otherwise, decrease votes. If votes reach 0, forget the current candidate and start fresh.
# (3) -->After the loop, check if the candidate still has a majority (half the votes).
#        a. If yes, return the candidate.
#        b. Otherwise, there's no majority, so return None.
# This algorithm cleverly tracks a potential majority candidate while automatically handling "disqualified" candidates that lose all their votes. It then verifies if the final candidate truly has the majority.

class Solution:
    def majority_element(self, nums):
        candidate = None
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            vote += (1 if num == candidate else -1)

        majority_vote = 0
        for num in nums:
            majority_vote += (1 if num == candidate else 0)

        return candidate if majority_vote == len(nums)/2 else None