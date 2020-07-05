# 860. 柠檬水找零
class Solution:
    def lemonadeChange(self, bills) -> bool:
        five = ten = 0
        for money in bills:
            if money == 5:
                five += 1
            elif money == 10:
                five -= 1
                ten += 1
            else:
                if ten == 0:
                    five -= 3
                else:
                    ten -= 1
                    five -= 1
            if five < 0 or ten < 0:
                return False
        return True

