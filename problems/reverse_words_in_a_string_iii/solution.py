class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(" ")
        l2 = [] 
        for i in ls:
            sw = "".join(list(reversed(i)))
            es ="".join(sw)
            l2.append(es)
        return " ".join(l2)