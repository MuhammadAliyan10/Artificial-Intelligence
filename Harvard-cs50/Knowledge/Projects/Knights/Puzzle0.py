from Logic import *

knight = Symbol('AKnight')
knave = Symbol('AKnave')
characters = [knight, knave]


knowledge0 = And(Or(knight, knave), Not(And(knight, knave)))
S = And(knight, knave)
knowledge0.add(And(Implication(knight, S), Implication(knave, Not(S))))


print("Puzzle 0:")
for character in characters:
    if modelCheck(knowledge0, character):
        print(f"{character} is True")
    elif modelCheck(knowledge0, Not(character)):
        print(f"{character} is False")