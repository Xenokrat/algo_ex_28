def MassVote(n: int, votes: list[int]) -> str:
    current_winner = 0
    another_winner = False
    total_votes = 0
    winner_index = None

    for ind, vote in enumerate(votes):
        if vote == current_winner:
            another_winner = True

        elif vote > current_winner:
            current_winner = vote
            another_winner = False
            winner_index = ind + 1

        total_votes += vote

    majority = current_winner > total_votes / 2

    if another_winner:
        return 'no winner'
    elif majority:
        return f'majority winner {winner_index}'
    else:
        return f'minority winner {winner_index}'
