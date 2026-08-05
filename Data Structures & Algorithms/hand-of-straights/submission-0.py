class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        buckets = [(0, 0)] * (len(hand) // groupSize)

        for card in hand:
            card_used = False
            for i in range(len(buckets)):
                if not buckets[i][1] or (buckets[i][1] < groupSize and buckets[i][0] == (card - 1)):
                    buckets[i] = (card, buckets[i][1] + 1) 
                    card_used = True
                    print(buckets)
                    break
            if not card_used:
                return False
        return True
                
                

                


        