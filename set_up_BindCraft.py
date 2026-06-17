import os
import shutil
import json

####### Adjust these variables as desired ##########

source_folder = "../BindCraft_template"  #path to the template bindcraft folder. This will be copied and edits will be made with the inputs below
dest_name_start = "260617_BindCraft_Acp" #The hotspot numbers will be added to the end of the folder name

hotspots = ["57","53","61","66","68","56","69"]   #A list containing strings of each of the hotspot conditions. For example: ["30,22","12"] would set up two BindCraft folders, one using hotspots 30 and 22, the other using the hotspot 12

binder_name_start = "260617_ACP"  #The hotspots will be added after the name
starting_pdb = "ACP_9D27.pdb"
chains = "A"
lengths = [40,90]
number_of_final_designs = 100

#change if needed
partition = "gpu-all" 
memory = "42gb"

######################################################

sh_files = []

for hotspot in hotspots:
    hotspot_name = hotspot.replace(",","_")
    destination = dest_name_start + "_" + hotspot_name
    binder_name = binder_name_start + hotspot_name
    dest = shutil.copytree(source_folder,destination)
    sh_files.append(dest + "/bindcraft.slurm")
    print(dest) #optional
    with open(dest + "/bindcraft.slurm","r") as f:
        lines = f.readlines()
        newlines = lines
        index = 0
        for line in lines:
            if "#SBATCH --partition" in line:
                newlines[index] = f"#SBATCH --partition={partition}\n"
            elif "#SBATCH --mem" in line:
                newlines[index] = f"#SBATCH --mem {memory}\n"
            elif "SETTINGS=" in line and ")" not in line:
                newlines[index] = f'SETTINGS="'+ dest + '/design.json"\n'
            elif "FILTERS=" in line and ")" not in line:
                newlines[index] = f'FILTERS="'+dest+ '/default_filters.json"\n'
            elif "ADVANCED=" in line and ")" not in line:
                newlines[index] = f'ADVANCED="'+dest+ '/default_4stage_multimer.json"\n'
            index += 1
    with open(dest + "/bindcraft.slurm","w") as f:
        f.writelines(newlines)

    with open(dest + "/design.json") as f:
        data = json.load(f)
        data["design_path"] = dest + "/Outputs"
        data["binder_name"] = binder_name
        data["starting_pdb"] = dest + "/" + starting_pdb
        data["chains"] = chains
        data["lengths"] = lengths
        data["number_of_final_designs"] = number_of_final_designs
        data["target_hotspot_residues"] = hotspot
    with open(dest + "/design.json","w") as f:
        json.dump(data,f,indent=2)


with open("launch_all.sh","w") as f:
    f.write('''#!/bin/bash
#SBATCH -J launch_all
#SBATCH --partition=cpu
#SBATCH -c 1
#SBATCH --mem=8g
#SBATCH -t 24:00:00

''')
    for sh in sh_files:
        f.write("sbatch " + sh + "\n")


