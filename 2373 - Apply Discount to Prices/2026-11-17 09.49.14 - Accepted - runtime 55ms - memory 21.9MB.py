class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        result = []
        
        for w in words:
            
            if w.startswith("$") and w[1:].isdigit():
                price = int(w[1:])
                new_price = price * (1 - discount / 100)
                result.append(f"${new_price:.2f}")
            else:
                result.append(w)
        
        return " ".join(result)