class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Brute Force: Check every single number of the array with other numbers in the array. 
        Time - O(n^2); Space - O(1)

        Sorting: Sort all elements so that similar elements end up next to each other.
        Time - O(nlogn); Space - O(1)

        HashSet: Check if the value exists in the hash set. Reduces time complexity but increases space complexity because of hash.
        Time - O(n); Space - O(n)
        """

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False