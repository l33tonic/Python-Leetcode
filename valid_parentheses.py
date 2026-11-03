class Solution(object):
    def isValid(self, s):
        matches = {'{': '}', '(': ')', '[': ']'}
        close_order = []
        valid = True

        if s == "" or s[-1] in matches:
            return False

        for char in s:
            if char in matches:
                close_order.append(matches[char])
            else:
                if not close_order:
                    valid = False
                    break

                if close_order[-1] == char:
                    close_order.pop()
                else:
                    valid = False
                    break

        if close_order:
            valid = False

        return valid
