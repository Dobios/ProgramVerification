from z3 import *

ROWS = 9
COLS = 9

# ========================================
# ================ TASK 1 ================
# ========================================

# Input:
#   - "puzzle" is a 9-tuple of 9-tuples of digits (0-9). 0 means empty, i.e. a
#     square that is NOT pre-filled. "puzzle[row][col]" refers to the square in
#     row "row", column "col" (counting from the top starting at 0).
#
# Output:
#   - A 9-tuple of 9-tuples of digits (1-9).
def solve(puzzle):
  s = Solver()

  # matrix of Int variables X[row][col]
  X = [ [ Int("square_%s_%s" % (row, col)) for col in range(COLS) ] for row in range(ROWS) ]

  # constraint: pre-filled squares
  for row in range(ROWS):
    for col in range(COLS):
      if puzzle[row][col] != 0:
        s.add(X[row][col] == puzzle[row][col])

  # constraint: each cell contains a digit between 1 and 9
  # --- ADD YOUR SOLUTION HERE ---
  for row in range(ROWS):
    for col in range(COLS):
      s.add(And(1 <= X[row][col], X[row][col] <= 9))

  # constraint: each row contains every digit at most once
  # --- ADD YOUR SOLUTION HERE ---
  for row in range(ROWS):
    s.add(Distinct(X[row]))

  # constraint: each column contains every digit at most once
  # --- ADD YOUR SOLUTION HERE ---
  Y = [[X[j][i] for j in range(ROWS)] for i in range(COLS)]
  for col in range(COLS):
    s.add(Distinct(Y[col]))

  # constraint: each 3 x 3 square contains every digit at most once
  # --- ADD YOUR SOLUTION HERE ---
  for i in range(3):
    for j in range(3):
      Z = [X[i * 3 + y][j * 3 + x] for y in range(3) for x in range(3)]
      s.add(Distinct(Z))

  # can Z3 find a solution for the given constraints?
  if s.check() == sat:
    # if so, fetch the model
    m = s.model()
    # and check what the variables are set to in that model
    solution = [ [ m.evaluate(X[row][col]) for col in range(COLS) ] for row in range(ROWS) ]
    # then print the solved grid!
    #print_matrix(solution)
    return tuple([ tuple(solution[row]) for row in range(ROWS) ])
  else:
    print("no solution!")
    return None

# ========================================
# ================ TASK 2 ================
# ========================================

# Input:
#   - Same as for Task 1.
#
# Output:
#   - A list of 9-tuples of 9-tuples of digits (1-9).
def solve_all(puzzle):
  # --- ADD YOUR SOLUTION HERE ---
  pass

# ========================================
# ================ TASK 3 ================
# ========================================

# Input:
#   - "puzzle" is the same as for Task 1.
#   - "jigsaws" is a list of jigsaw pieces. Each jigsaw piece is a list of
#     coordinate tuples "(row, col)" representing which coordinates belong
#     to that jigsaw piece.
#
# Output:
#   - A 9-tuple of 9-tuples of digits (1-9).
def solve_jigsaw(puzzle, jigsaws):
  # --- ADD YOUR SOLUTION HERE ---
  pass
