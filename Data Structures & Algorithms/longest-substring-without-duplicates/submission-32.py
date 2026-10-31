class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        current_set = set()
        best_set = set()
        trailing_i = 0

        for i, letter in enumerate(s):

            if letter not in current_set:
                current_set.add(letter)

            else:

                # Remove characters from the left
                # until we reach the old duplicate
                while s[trailing_i] != letter:
                    current_set.remove(s[trailing_i])
                    trailing_i += 1

                # Remove the old duplicate
        
                trailing_i += 1

                # Add the new occurrence
 

            # Check whether our current window is the best so far
            if len(current_set) > len(best_set):
                best_set = current_set.copy()

        return len(best_set)