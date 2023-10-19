class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        h = sentence.split()
        for i in range(len(h)):
            if h[i][0] == "$" and h[i].count("$") == 1 and len(h[i])>1 and h[i][1:].isdigit()==True:
                num = format(int(h[i][1:])-(int(h[i][1:]) *(discount/100)), ".2f")
                h[i] = f"${num}"
        return " ".join(h)

        