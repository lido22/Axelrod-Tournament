from outcomes import Outcome


def play(opponent_past_moves: list[Outcome], my_past_moves: list[Outcome]) -> Outcome:
    return opponent_past_moves[-1] if len(opponent_past_moves) > 0 else Outcome.cooperate
