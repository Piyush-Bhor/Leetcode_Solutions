class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r_votes, d_votes = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                r_votes.append(i)
            else:
                d_votes.append(i)

        while r_votes and d_votes:
            
            r_vote = r_votes.popleft()
            d_vote = d_votes.popleft()

            if r_vote < d_vote:
                r_votes.append(r_vote + len(senate))
            else:
                d_votes.append(d_vote + len(senate))
            
        return "Radiant" if r_votes else "Dire"