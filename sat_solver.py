# importing system module for reading files
import sys

# in what follows, a *formula* is a collection of clauses,
# a clause is a collection of literals,
# and a literal is a non-zero integer.


symbols = {}
all_psukiot = []



def parse_dimacs_path(file_path):
  psukiot = []
  num_clauses = 0
  num_vars = 0
  try:
    with open(file_path, 'r') as file:
      flag = True
      for line in file:
        line = line.split()
        if flag == True:
          num_vars = int(line[2])
          num_clauses = int(line[3])
          flag = False
        else:
          psukit = [int(element) for element in line]
          psukit.pop()
          psukiot.append(psukit)
    return psukiot, num_vars, num_clauses


  except:
    print("path is not valid")






# input path:  a path to a cnf file
# output: the formula represented by the file,
#         the number of variables,
#         and the number of clauses
# def parse_dimacs_path(path):
#   psukiot = open_and_parsing_file(path)
#   print(psukiot)
#   return [], 0, 0



def isClauseSat(clause, assign):
    for var in clause:
      varAsssign = (assign >> (abs(var) - 1)) % 2
      if varAsssign == 1 and var > 0:
        return True
      if varAsssign == 0 and var < 0:
        return True
    return False



# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def naive_solve(cnf, num_vars, num_clauses):
  rounds = 2 ** num_vars
  for i in range(rounds):
    flag = True
    for clause in cnf:
      if not isClauseSat(clause, i):
        flag = False
        break
    if flag:
      return i
  return -1



def printNaiveSolution(assign, num_vars):
  print("sat")
  for i in range(num_vars):
    varAssign = (assign >> i) % 2
    if varAssign == 1:
      print(str(i + 1) + ": true")
    else:
      print(str(i + 1) + ": false")





# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def dpll_solve(cnf, n_vars, n_clauses):
  return True


######################################################################

# get path to cnf file from the command line
#path = sys.argv[1]
path = "C:/ar2/a.cnf"


# get algorithm from the command line
#algorithm = sys.argv[2]
algorithm = "naive"

# make sure that algorithm is either "naive" or "dpll"
assert(algorithm in ["naive", "dpll"])

# parse the file
cnf, num_vars, num_clauses = parse_dimacs_path(path)


# check satisfiability based on the chosen algorithm
# and print the result
if algorithm == "naive":
  result = naive_solve(cnf, num_vars, num_clauses)
  if result == -1:
    print("unsat")
  else:
    printNaiveSolution(result, num_vars)
  #print("sat" if naive_solve(cnf, num_vars, num_clauses) else "unsat")
else:
  print("sat" if dpll_solve(cnf, num_vars, num_clauses) else "unsat")