from outcomes import Outcome
import random

def play(opponent_past_moves: list[Outcome], my_past_moves: list[Outcome]) -> Outcome:
    rand = random.random()
    if rand <= 0.8:
        return Outcome.defect
    else:
        return Outcome.cooperate