class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        
        for char in magazine:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char in ransomNote:
            if counts.get(char, 0) == 0:
                return False
            counts[char] -= 1

        return True

#решение с импользованием Counter
#class Solution:
#    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#       return Counter(ransomNote) <= Counter(magazine)return
#       mag_count = Counter(magazine)