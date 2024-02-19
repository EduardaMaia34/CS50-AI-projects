from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, AKnight), 
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    And(Not(And(AKnave, BKnave)), Not(And(AKnight, BKnight))),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnave, BKnight),
    Not(And(AKnave, BKnave)),
    Not(And(AKnight, BKnight)),
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(BKnight, And(BKnight, AKnave)),
    Implication(AKnave, And(AKnave, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    #if Bknight
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
        #if A is Knave, then he's telling the truth, so he is not a knave
        #if A is a Knight, and is telling the truth based on what B said, then he is a Knave
        Implication(AKnave, Not(AKnave)),
        Implication(AKnight, AKnave)
    )),
    #if Bknave
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
        #if A is Knigh then he would really be a Knight, because A couldn't be a Knave since that's what B said and B is lying (B is knave in this case)
        #if A is Knave then he wouldn't be a Knave because then B would be telling the truth making it a Knight (which is not the case)
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnave))
    )),

    #if Cknight
    Implication(CKnight, AKnight),
    #if Cknave
    Implication(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
