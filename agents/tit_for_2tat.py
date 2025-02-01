from outcomes import Outcome


def play(opponent_past_moves: list[Outcome], my_past_moves: list[Outcome]) -> Outcome:
    if (len(opponent_past_moves) > 1
        and opponent_past_moves[-1] == Outcome.defect
        and opponent_past_moves[-2] == Outcome.defect):
        return Outcome.defect
    else:
        return Outcome.cooperate