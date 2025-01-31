from outcomes import Outcome


def play(opponent_past_moves: list[Outcome], my_past_moves: list[Outcome]) -> Outcome:
    return Outcome.cooperate
