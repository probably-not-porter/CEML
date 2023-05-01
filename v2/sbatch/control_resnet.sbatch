#!/bin/sh
#SBATCH --job-name CEML_control_model_resnet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 500:00:00
#SBATCH -o "CEML_control_model_resnet.out"

cd ..
echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "RESNET18 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "resnet18" --cycles 100

echo $(date)
echo "RESNET34 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "resnet34" --cycles 100

echo $(date)
echo "RESNET50 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "resnet50" --cycles 100

echo $(date)
echo "RESNET101 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "resnet101" --cycles 100

echo $(date)
echo "RESNET152 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "resnet152" --cycles 100
