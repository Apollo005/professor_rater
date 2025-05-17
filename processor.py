# Establish imports
import pandas as pd 

# Read the file
file = pd.read_json("professors.json")

# EECS Professors - 
compsci_profs = file[file["department"] == "Computer Science"]
electric_profs = file[file["department"] == "Electrical Engineering"]
eecs_profs = file[file["department"] == "Electrical Engineering & Computer Science"]

# Mathematics -
math_profs = file[file["department"] == "Mathematics"]

# English + English Lit - 
engl_profs = file[file["department"] == "English"]
lit_profs = file[file["department"] == "English Language & Literature"]

# Chemistry -
chem_profs = file[file["department"] == "Chemistry"]
