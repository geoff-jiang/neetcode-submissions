class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        # {}

        hand.sort()

        # 12233445
        # {
        #     1: 0 
        #     2: 1
        #     3: 1
        #     4: 1
        #     5: 1
        # }
        for i in hand:
            if i in counter and counter[i] > 0:
                counter[i] -= 1
                for j in range(1, groupSize):
                    if counter[j + i] > 0:
                        counter[j + i] -= 1
                    else:
                        return False
        return True




