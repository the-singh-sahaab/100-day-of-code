class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = ''
        for word in words:
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    break
            else:
                ans += word
        return len(ans)