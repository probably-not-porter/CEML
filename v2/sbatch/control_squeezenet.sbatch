#!/bin/sh
#SBATCH --job-name CEML_control_model_squeezenet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 72:00:00
#SBATCH -o "CEML_control_model_squeezenet.out"
#SBATCH --chdir=/code/CEML/v2

DATA_DIR="../images/dogs_cats_parent/dogs_cats"
CYCLES=20

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "squeezenet1_0 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "squeezenet1_0" --cycles $CYCLES

echo $(date)
echo "squeezenet1_1 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "squeezenet1_1" --cycles $CYCLES
