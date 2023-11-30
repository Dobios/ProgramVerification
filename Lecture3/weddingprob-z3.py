from z3 import *

# 9 variables, one for each state
Ax = Bools('al ar am')
Bx = Bools('bl br bm')
Cx = Bools('cl cr cm')

S = Solver()

# Alice can't sit next to Charlie
S.add(
    And(
        Implies(Or(Ax[0], Ax[1]), Not(Cx[2])),
        Implies(Ax[2], Not(Or(Cx[0], Cx[1])))
    )
)

# Alice can't sit on the left
S.add(Not(Ax[0]))

# Bob doesn't sit to the right of Charlie
S.add(And(Implies(Cx[0], Not(Bx[2])), Implies(Cx[2], Not(Bx[1]))))

# Each person gets a chair
S.add(
    And(
        Or(Cx[1], Or(Cx[0], Cx[2])),
        And(
            Or(Ax[1], Or(Ax[0], Ax[2])),
            Or(Bx[1], Or(Bx[0], Bx[2]))
        )
    )
)

S.add(
    And(
        Not(And(Ax[0], Bx[0])),
        And(
            Not(And(Ax[0], Cx[0])),
            And(
                Not(And(Ax[1], Bx[1])),
                And(
                    Not(And(Ax[1], Cx[1])),
                    And(
                        Not(And(Ax[2], Bx[2])),
                        And(
                            Not(And(Ax[2], Cx[2])),
                            And(
                                Not(And(Bx[0], Cx[0])),
                                And(
                                    Not(And(Bx[1], Cx[1])),
                                    Not(And(Bx[2], Cx[2]))
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

S.add(
    And(
        Not(And(Ax[0], Ax[1])),
        And(
            Not(And(Ax[0], Ax[2])),
            And(
                Not(And(Ax[1], Ax[2])),
                And(
                    Not(And(Bx[0], Bx[1])),
                    And(
                        Not(And(Bx[0], Bx[2])),
                        And(
                            Not(And(Bx[1], Bx[2])),
                            And(
                                Not(And(Cx[0], Cx[1])),
                                And(
                                    Not(And(Cx[0], Cx[2])),
                                    Not(And(Cx[1], Cx[2]))
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

print(S.check())
