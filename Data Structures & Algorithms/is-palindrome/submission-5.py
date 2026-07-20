class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = "".join(c.lower() for c in s if c.isalnum())
        return z == z[::-1]

        