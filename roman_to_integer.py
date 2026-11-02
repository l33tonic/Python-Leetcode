class Solution(object):
    def romanToInt(self, s):
        conv_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = conv_dict[s[0]]

        for i in range(1, len(s)):
            num = conv_dict[s[i]]
            prev_num = conv_dict[s[i-1]]

            total += num

            if prev_num < num:
                total -= 2 * prev_num

        return total
