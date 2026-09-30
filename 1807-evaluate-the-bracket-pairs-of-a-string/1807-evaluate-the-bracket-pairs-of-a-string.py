class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        i = 0
        result = []

        for key , value in knowledge:
            d[key] = value
        
        while i < len(s):
            if s[i] == "(":
                key = ""
                i += 1

                while s[i] != ")":
                    key += s[i]
                    i += 1

                if key in d:
                    result.append(d[key])
                    i += 1
                else :
                    result.append("?")
                    i += 1

            else :
                result.append(s[i])
                i += 1
        
        return "".join(result)
        