# Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions.

import printing_functions_T1 as pft

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pft.print_models(unprinted_designs, completed_models)
pft.show_completed_models(completed_models)