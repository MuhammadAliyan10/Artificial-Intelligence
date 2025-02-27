from Logic import *

AKnight = Symbol('AKnight')
AKnave = Symbol('AKnave')
BKnight = Symbol('BKnight')
BKnave = Symbol('BKnave')
CKnight = Symbol('CKnight')
CKnave = Symbol('CKnave')
ASaidKnave = Symbol("ASaidKnave") 
characters = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]

knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), 
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),  
    Or(CKnight, CKnave), Not(And(CKnight, CKnave))  
)
knowledge3.add(Or(
    And(ASaidKnave, Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))),
    And(Not(ASaidKnave), Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))
))
knowledge3.add(Implication(BKnight, ASaidKnave)) 
knowledge3.add(Implication(BKnave, Not(ASaidKnave)))
knowledge3.add(Implication(BKnight, CKnave))   
knowledge3.add(Implication(BKnave, Not(CKnave)))

knowledge3.add(Implication(CKnight, AKnight))   
knowledge3.add(Implication(CKnave, Not(AKnight)))


print("Puzzle 3:")
for character in characters:
    if modelCheck(knowledge3, character):
        print(f"{character} is True")
    elif modelCheck(knowledge3, Not(character)):
        print(f"{character} is False")