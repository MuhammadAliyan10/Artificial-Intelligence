from Logic import *

AKnight = Symbol('AKnight')
AKnave = Symbol('AKnave')
BKnight = Symbol('BKnight')
BKnave = Symbol('BKnave')
characters = [AKnight, AKnave,BKnight,BKnave]


knowledge1 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)),Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
S = And(AKnave, BKnave)
knowledge1.add(Implication(AKnight, S))
knowledge1.add(Implication(AKnave, Not(S)))



print("Puzzle 1:")
for character in characters:
    if modelCheck(knowledge1, character):
        print(f"{character} is True")
    elif modelCheck(knowledge1, Not(character)):
        print(f"{character} is False")