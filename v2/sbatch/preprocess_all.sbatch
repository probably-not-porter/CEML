#!/bin/sh
#SBATCH --job-name CEML_preprocess_ALL
#SBATCH --nodes=1 
#SBATCH -c 1
#SBATCH -t 24:00:00
#SBATCH -o "CEML_preprocess_ALL.out"

DATA_DIR="../../images/dogs_cats_parent/dogs_cats"

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

srun python3 ../process_images.py -i $DATA_DIR --pre
