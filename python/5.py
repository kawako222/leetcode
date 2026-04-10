class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandirCentro(s, i, i)
            len2 = self.expandirCentro(s, i, i + 1)

            mayor = max(len1, len2)

            if mayor > end - start:
                 start = i - (mayor - 1) // 2
                 end = i + mayor // 2 
                 
        return s[start:end+1]

    def expandirCentro(self, s: str, izquierda: int, derecha: int) -> int:
        while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
            izquierda -= 1
            derecha += 1

        return derecha - izquierda - 1
