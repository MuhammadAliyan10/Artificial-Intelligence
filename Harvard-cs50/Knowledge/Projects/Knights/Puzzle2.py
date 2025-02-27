from Logic import *

AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")
BKnight = Symbol("BKnight")
BKnave = Symbol("BKnave")
characters = [AKnight, AKnave, BKnight, BKnave]


knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
)
S_A = Or(And(AKnight, BKnight), And(AKnave, BKnave))
knowledge2.add(Implication(AKnight, S_A))
knowledge2.add(Implication(AKnave, Not(S_A)))
S_B = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2.add(Implication(BKnight, S_B))
knowledge2.add(Implication(BKnave, Not(S_B)))


print("Puzzle 2:")
for character in characters:
    if modelCheck(knowledge2, character):
        print(f"{character} is True")
    elif modelCheck(knowledge2, Not(character)):
        print(f"{character} is False")
