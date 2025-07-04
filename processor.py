# Establish imports
import pandas as pd 

# Read the file
file = pd.read_json("professors.json")

# EECS Professors - 
eecs_profs = file[
    (file["department"] == "Computer Science") |
    (file["department"] == "Electrical Engineering") |
    (file["department"] == "Electrical Engineering & Computer Science")
]


# Mathematics -
math_profs = file[file["department"] == "Mathematics"]

# English + English Lit - 
engl_profs = file[
    (file["department"] == "English") |
    (file["department"] == "English Language & Literature")
]

# Chemistry -
chem_profs = file[file["department"] == "Chemistry"]

# Statistics -
stats_profs = file[file["department"] == "Statistics"]

# Business -
business_profs = file[(file["department"] == "Business") 
|  (file["department"] == "Business Administration") |
(file["department"] == "Business Economics") | (file["department"] == "Business Operations")]

# Biology -
bio_profs = file[file["department"] == "Biology"]

# Economics -
econ_profs = file[file["department"] == "Economics"]

# Mechanical -
mech_profs = file[file["department"] == "Mechanical Engineering"]

# Information Science -
infosci_profs = file[file["department"] == "Information Science"]

# Polisci -
polisci_profs = file[file["department"] == "Political Science"]

# Psychology -
psych_profs = file[file["department"] == "Psychology"]

# Art & Design -
art_profs = file[(file["department"] == "Art") | (file["department"] == "Graphic Arts")
| (file["department"] == "Dramatic Arts") ]

# Communications  -
comms_profs = file[(file["department"] == "Communication") | 
(file["department"] == "Communication Studies") ]

# Environment -
environ_profs = file[(file["department"] == "Environment") |
(file["department"] == "Environmental Science") | (file["department"] == "Environmental Studies")]

# Economics -
nursing_profs = file[file["department"] == "Nursing"]

# IOE -
ioe_profs = file[file["department"] == "Industrial Engineering"]

# History -
history_profs = file[file["department"] == "History"]

# Music -
music_profs = file[(file["department"] == "Music") | (file["department"] == "Music Education")
| (file["department"] == "Music Performance") ] 

# Physics -
physics_profs = file[file["department"] == "Physics"]


# 0 profs scraped

# Aerospace -
# aero_profs = file[file["department"] == "Aerospace Engineering"]

# Biomedical Engineering -
# bio_eng_profs = file[file["department"] == "Biomedical Engineering"]

# Sports -
# sports_profs = file[file["department"] == "Sports Management"]

dept_dict = {
    "eecs_profs": eecs_profs,
    "math_profs": math_profs,
    "engl_profs": engl_profs,
    "chem_profs": chem_profs,
    "stats_profs": stats_profs,
    "business_profs": business_profs,
    "bio_profs": bio_profs,
    "econ_profs": econ_profs,
    "mech_profs": mech_profs,
    "infosci_profs": infosci_profs,
    "polisci_profs": polisci_profs,
    "psych_profs": psych_profs,
    "art_profs": art_profs,
    "comms_profs": comms_profs,
    "environ_profs": environ_profs,
    "nursing_profs": nursing_profs,
    "ioe_profs": ioe_profs,
    "history_profs": history_profs,
    "music_profs": music_profs,
    "physics_profs": physics_profs
}

# Department average stats
def prof_stats(metric):
    stats = []
    for name, df in dept_dict.items():
        avg = df[metric].mean()
        stats.append({"department": name, f"{metric}": avg})
    return pd.DataFrame(stats)

avg_ratings = prof_stats('avg_rating')
avg_ratings = avg_ratings.sort_values(by='department')
avg_ratings.to_csv("rmp_avg_rating.csv", index=False)

avg_difficulty = prof_stats('avg_difficulty')
avg_difficulty = avg_difficulty.sort_values(by='department')
avg_difficulty.to_csv("rmp_avg_difficulty.csv", index=False)

avg_take_again = prof_stats('would_take_again_percent')
avg_take_again = avg_take_again.sort_values(by='department')
avg_take_again.to_csv("rmp_avg_take_again.csv", index=False)

# change to sum()
total_ratings = prof_stats('num_ratings')
total_ratings = total_ratings.sort_values(by='department')
total_ratings.to_csv("rmp_total_ratings.csv", index=False)

# Profs per dept sample
num_profs = []
for dept_name, df in dept_dict.items():
    num_profs.append({
        "department": dept_name,
        "num_professors": df.shape[0]  # number of rows
    })

num_profs = pd.DataFrame(num_profs).sort_values(by='department')
num_profs.to_csv("rmp_num_profs.csv", index=False)

# Language Department analysis
