from outcomes import Outcome
import random

def play(opponent_past_moves: list[Outcome], my_past_moves: list[Outcome]) -> Outcome:
    return random.choice([Outcome.cooperate, Outcome.defect])