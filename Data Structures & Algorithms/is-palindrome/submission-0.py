class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join([char for char in s if char.isalnum()]) 
        cleaned_text.replace(" ", "")
        cleaned_text = cleaned_text.lower()

        reverse = cleaned_text[::-1]
        return cleaned_text == reverse