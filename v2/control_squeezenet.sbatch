#!/bin/sh
#SBATCH --job-name CEML_control_model_squeezenet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 24:00:00
#SBATCH -o "CEML_control_model_squeezenet.out"


echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "squeezenet1_0 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "squeezenet1_0" --cycles 10

echo $(date)
echo "squeezenet1_1 MODEL"
srun python3 create_model.py --input "../images/xray_parent/xray" --model "squeezenet1_1" --cycles 10
