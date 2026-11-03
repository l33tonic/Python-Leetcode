class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest_str = strs[0]
        for i in strs:
            if len(i) < len(shortest_str):
                shortest_str = i

        longest_prefix = ""
        for i in range(len(shortest_str)):
            next_char = shortest_str[i]
            for j in strs:
                if j[i] != next_char:
                    break
            else:
                longest_prefix += next_char
                continue
            break

        return longest_prefix

