class Solution:
        def lemondeChange(self,bills):
            five = ten = 0
            for bill in bills:
                if bill == 5:
                    five += 1
                elif bill == 10:
                    # 如果付款10块，没有5块钱，就直接返回false
                    if not five:
                        return False
                    five -= 1
                    ten += 1
                else:
                    #手上有10块和5块
                    if ten and five:
                        ten -= 1
                        five -=1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False
            return True
