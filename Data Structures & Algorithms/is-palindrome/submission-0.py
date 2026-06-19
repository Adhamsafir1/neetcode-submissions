class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            asc1 = ord(s[i])
            asc2 = ord(s[j])

            if 97 <= asc1 <= 122:
                asc1 -= 32

            if 97 <= asc2 <= 122:
                asc2 -= 32

         
            if not (65 <= asc1 <= 90 or 48 <= asc1 <= 57):
                i += 1
                continue

            if not (65 <= asc2 <= 90 or 48 <= asc2 <= 57):
                j -= 1
                continue

            if asc1 != asc2:
                return False

            i += 1
            j -= 1

        return True