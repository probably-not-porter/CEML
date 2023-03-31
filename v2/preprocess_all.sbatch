#!/bin/sh
#SBATCH --job-name CEML_preprocess_ALL
#SBATCH --nodes=1 
#SBATCH -c 4 # ask for four cores
#SBATCH --mail-type=BEGIN,END,FAIL 
#SBATCH --mail-user=pelibby16@earlham.edu

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

module purge
module load modules
module load python/3.9

srun python process_images.py -i "../images/xray_parent/xray" --pre
