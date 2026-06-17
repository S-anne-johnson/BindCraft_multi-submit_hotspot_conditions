1. Obtain the pdb you will use as a target for binder design and place it in this folder.
2. Update design path in design.json for where you want designs and statistics to be desposited. Updated the other parameters in design.json as well.
3. Update any relevant parameters in default_filters.json and default_4stage_multimer.json for the purposes of your binder design task.
4. In bindcraft.slurm, make SETTINGS, FILTERS, and ADVANCED equal to the paths to design.json, default_filters.json and default_4stage_multimer.json.
5. sbatch bindscraft.slurm

Note that due to the memory required (usually more than 32 GB), it may be best to run these jobs on the gpu-6000ada and avoid the gpu-a4000 which have less memory.

written 10/29/25 by Sarah J
