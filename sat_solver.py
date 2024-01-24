# importing system module for reading files
import sys

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


def isClauseSat(clause, assign):
    for var in clause:
      # checks if bit that represents var is 1 or 0
      varAsssign = (assign >> (abs(var) - 1)) % 2
      # if the var is positive and the assign is true
      if varAsssign == 1 and var > 0:
        return True
      # if the var is negative and the assign is false
      if varAsssign == 0 and var < 0:
        return True
    return False


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
def naive_solve(cnf, num_vars, num_clauses):
  rounds = 2 ** num_vars
  for i in range(rounds):
    flag = True
    for clause in cnf:
      if not isClauseSat(clause, i):
        flag = False
        break
    if flag:
      printNaiveSolution(i, num_vars)
      return
  print("unsat")


def isNotClauseSat(m, clause):
  for var in clause:
    # checks if there isn't any assign for var in m
    if var not in m and -var not in m:
      return False
    else:
      # checks if var satisfy clause, hence it is not satisfy notClause
      if var in m:
        return False
  return True



def isFail(config):
  # checks if there aren't any deduction in m or if there is guess in d
  if len(config.get("m")) == 0 or len(config.get("d")) != 0:
    return False
  for clause in config.get("f"):
    # checks if m satisfy notClause
    if isNotClauseSat(config.get("m"), clause):
      return True
  return False


def varNotInM(var, m):
  # checks if there is assign for var in m
  if -var not in m and var not in m:
    return True
  return False


def varSatisfyClause(var, m):
  if var in m:
    return True

def findUPCandidate(clause, m):
  candidate = 0
  for var in clause:
    # checks if var is first that can be candidate
    if varNotInM(var, m) and candidate == 0:
      candidate = var
      continue
    # checks if var can be candidate but not the first
    if varNotInM(var, m) and candidate != 0:
      return 0
    # checks if there is var that satisfy clause
    if varSatisfyClause(var, m):
      return 0
  return candidate



def tryUP(config):
  for clause in config.get("f"):
    # checks if there is candidate for UP in this clause
    candidate = findUPCandidate(clause, config.get("m"))
    if candidate != 0:
      config.get("m").append(candidate)
      return True
  return False



def success(config, num_vars):
  # checks if there are assigns for all the vars
  if len(config.get("m")) != num_vars:
    return False
  # checks that m satisfy all the clauses
  for clause in config.get("f"):
    flag = False
    for var in clause:
      if varSatisfyClause(var, config.get("m")):
        flag = True
        break
    if not flag:
      return False
  return True



def backTrackNeeded(config):
  # checks if there is any clause in f that m satisfy notClause
  for clause in config.get("f"):
    if isNotClauseSat(config.get("m"), clause):
      return True
  return False



def doBackTrack(config):
  # get the last guess
  pivot = config.get("d")[-1]
  # remove the last guess from d
  config.get("d").remove(pivot)
  # get the index of the guess in m
  pivotIndex = config.get("m").index(pivot)
  # remove all the variables from the guess until the end of m
  del config.get("m")[pivotIndex:]
  # append the opposite of the guess to m
  config.get("m").append(-pivot)



def decide(config, num_vars):
  for i in range(num_vars):
    # checks if there isn't assign for var number i+1
    if varNotInM(i+1, config.get("m")):
      # guess assign for var and adds it to d and m
      config.get("d").append(i+1)
      config.get("m").append(i + 1)
      return


def printDpllSolution(m, num_vars):
  print("sat")
  for i in range(num_vars):
    if (i+1) in m:
      print(str(i+1) + ": true")
    else:
      print(str(i+1) + ": false")




# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def dpll_solve(cnf, num_vars):
  config = {"m": [], "f": cnf, "d": []}
  flag = False
  while(True):
    if success(config, num_vars):
      flag = True
      break
    if isFail(config):
      flag = False
      break
    if backTrackNeeded(config):
      doBackTrack(config)
      continue
    if tryUP(config):
      continue
    decide(config, num_vars)

  if flag:
    printDpllSolution(config.get("m"), num_vars)
  else:
    print("unsat")


######################################################################

# get path to cnf file from the command line
#path = sys.argv[1]
path = "C:/ar2/a.cnf"


# get algorithm from the command line
# algorithm = sys.argv[2]
algorithm = "dpll"

# make sure that algorithm is either "naive" or "dpll"
assert(algorithm in ["naive", "dpll"])

# parse the file
cnf, num_vars, num_clauses = parse_dimacs_path(path)


# check satisfiability based on the chosen algorithm
# and print the result
if algorithm == "dpll":
  naive_solve(cnf, num_vars, num_clauses)
else:
  dpll_solve(cnf, num_vars)