#!/bin/sh
#SBATCH --job-name CEML_control_model_resnet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 500:00:00
#SBATCH -o "CEML_control_model_resnet.out"

DATA_DIR="../../images/xray_parent/xray"

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "RESNET18 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "resnet18" --cycles 100

echo $(date)
echo "RESNET34 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "resnet34" --cycles 100

echo $(date)
echo "RESNET50 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "resnet50" --cycles 100

echo $(date)
echo "RESNET101 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "resnet101" --cycles 100

echo $(date)
echo "RESNET152 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "resnet152" --cycles 100
