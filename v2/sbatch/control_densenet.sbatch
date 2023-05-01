#!/bin/sh
#SBATCH --job-name CEML_control_model_densenet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 500:00:00
#SBATCH -o "CEML_control_model_densenet.out"

DATA_DIR="../../images/xray_parent/xray"

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "densenet121 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet121" --cycles 100

echo $(date)
echo "densenet169 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet169" --cycles 100

echo $(date)
echo "densenet201 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet201" --cycles 100

echo $(date)
echo "densenet161 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet161" --cycles 100



