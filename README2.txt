1. Obtain the pdb you will use as a target for binder design and place it in the BindCraft_template folder.
2. Update any relevant parameters is set_up_BindCraft.py (the variables to be updated are noted in the script)
     Any parameters not present in set_up_BindCraft.py can be directly edited in the BindCraft_template folder.
3. python set_up_BindCraft.py
This will produce folders for running BindCraft for every hotspot combination you have written in set_up_BindCraft.py. It will also produce a shell script to automatically submit these jobs.
4. sbatch launch_all.sh
Automatically submit all of the bindcraft jobs.

For more information about BindCraft, see the BindCraft GitHub.

written 6/17/26 by Sarah J
