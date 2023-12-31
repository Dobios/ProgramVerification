from solution import solve_jigsaw

def create_jigsaws(groups):
  jigsaws = [ [] for i in range(len(groups)) ]
  for row in range(9):
    for col in range(9):
      jigsaws[groups[row][col]].append((row, col))
  return jigsaws

# test cases for Task 3
if __name__ == "__main__":
  GRID_F = (
    (0,0,5,0,1,0,0,0,4),
    (0,0,0,0,0,0,0,0,0),
    (0,0,3,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,1),
    (0,0,0,7,0,0,0,1,0),
    (0,0,2,0,0,0,4,0,0),
    (0,0,0,0,7,0,0,8,0),
    (0,6,0,0,0,3,9,0,0),
    (0,0,0,3,2,0,0,0,0),
  )
  GRID_F_JIGSAWS = create_jigsaws((
    (0,0,0,0,0,0,1,2,2),
    (3,3,3,3,0,1,1,2,2),
    (4,3,3,0,0,1,1,1,2),
    (4,4,3,5,5,1,5,1,2),
    (4,4,3,3,5,5,5,1,2),
    (4,4,6,7,5,7,5,2,2),
    (4,4,6,7,7,7,5,8,8),
    (6,6,6,7,7,7,8,8,8),
    (6,6,6,6,7,8,8,8,8),
  ))
  GRID_F_SOLUTION = (
    (7,3,5,9,1,2,8,6,4),
    (2,1,8,5,4,6,3,7,9),
    (1,4,3,8,6,7,2,9,5),
    (3,8,6,2,9,4,7,5,1),
    (4,5,9,7,3,8,6,1,2),
    (6,7,2,1,5,9,4,3,8),
    (9,2,4,6,7,5,1,8,3),
    (5,6,1,4,8,3,9,2,7),
    (8,9,7,3,2,1,5,4,6),
  )
  print("GRID_F solved?", solve_jigsaw(GRID_F, GRID_F_JIGSAWS) == GRID_F_SOLUTION)

  GRID_G = (
    (8,0,0,9,0,4,0,2,0),
    (0,0,0,0,2,0,0,0,0),
    (0,0,0,0,0,0,1,3,0),
    (0,0,6,0,0,1,0,0,0),
    (0,9,0,0,0,8,0,0,0),
    (4,0,5,0,0,0,3,0,0),
    (0,0,0,2,0,0,0,0,6),
    (0,0,1,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
  )
  GRID_G_JIGSAWS = create_jigsaws((
    (0,0,0,0,1,2,2,2,2),
    (3,0,0,0,1,2,2,4,2),
    (3,0,0,1,1,1,2,4,4),
    (3,3,3,1,1,1,2,4,4),
    (3,3,5,1,6,6,6,4,4),
    (3,3,5,6,6,6,6,7,4),
    (8,8,5,5,5,6,7,7,4),
    (8,8,8,8,5,6,7,7,7),
    (8,8,8,5,5,5,7,7,7),
  ))
  GRID_G_SOLUTION = (
    (8,1,3,9,7,4,6,2,5),
    (7,6,4,5,2,3,8,1,9),
    (5,7,2,6,4,9,1,3,8),
    (2,3,6,8,5,1,7,9,4),
    (1,9,7,3,6,8,4,5,2),
    (4,8,5,1,9,2,3,6,7),
    (3,4,9,2,1,7,5,8,6),
    (6,2,1,7,8,5,9,4,3),
    (9,5,8,4,3,6,2,7,1),
  )
  print("GRID_G solved?", solve_jigsaw(GRID_G, GRID_G_JIGSAWS) == GRID_G_SOLUTION)
