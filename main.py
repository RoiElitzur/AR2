import sys

# from pysmt.shortcuts import Implies, Solver, And, Or, Not, BOOL, Symbol, TRUE ,FALSE
# solver = Solver(name="z3")

number_of_psukiot = 0
number_of_vars = 0
symbols = {}
all_psukiot = []
def symbol_exist(var_number):
    symbol_number = abs(var_number)
    result = symbols.get(symbol_number, 0)
    if not result:
        # symbols[symbol_number] = Symbol(symbol_number)
        symbol_number[symbol_number] = symbol_number
    if var_number < 0:
        ##return    Not(symbols[symbol_number])
        symbols[symbol_number]*-1
    return symbols[symbol_number]



def build_psukiot(psukiot):
    for psukit in psukiot:
        for var in psukit:
            current_psukit = []
            var_symbol = symbol_exist(var)
            current_psukit.append(var_symbol)

        # solver.add_assertion(And(current_psukit))




def open_and_parsing_file(file_path):
    psukiot = []
    try:
        with open(file_path,'r') as file:
            flag = True
            for line in file:
                line = line.split()
                if flag == True:
                    number_of_vars = int(line[2])
                    number_of_psukiot = int(line[3])
                    flag = False
                else:
                    psukit = [int(element) for element in line]
                    psukit.pop()
                    psukiot.append(psukit)
        return psukiot


    except:
        print("path is not valid")



# def print_victory():
#     print("There is an installation plan:")
#     model = solver.get_model()
#     for symbol_name, symbol in symbols.items():
#         if model.get_value(symbol) == TRUE():
#             print(symbol_name)



if __name__ == '__main__':
    psukiot = open_and_parsing_file(sys.argv[1])
    build_psukiot(psukiot)


    # if solver.solve():
    #     print_victory()
    # else:
    #     print("There is no installation plan")

