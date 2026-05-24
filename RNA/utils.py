def  parsePDB(file_name):
    with open (pdb_name, 'r') as file :
        line = file.readline()  
        while line [0.6].strip() != 'TER' : 
            if line[0:7].strip() == 'ATOM':
                x= line[30:38].strip()
                print(x)
            line = file.readline()  



    RNA= 'RNA found in '  + file_name
    return RNA

def generate_dot_bracket(model) :
    print('Dot-bracket notation of the ' + model)

  