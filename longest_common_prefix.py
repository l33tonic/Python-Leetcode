class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest_str = strs[0]
        for i in strs[1:]:
            if len(i) < len(shortest_str):
                shortest_str = i

        longest_prefix = ""
        for i in range(1, len(shortest_str) + 1):
            test_prefix = shortest_str[:i]
            for j in strs:
                if j[:i] != test_prefix:
                    break
            else:
                longest_prefix = test_prefix
                continue
            break

        return longest_prefix

