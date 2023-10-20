#!/bin/sh
#SBATCH --job-name CEML_sobely_sobelx_original_densenet
#SBATCH --nodes=1
#SBATCH -c 3
#SBATCH -t 72:00:00
#SBATCH -o "CEML_sobely_sobelx_original_densenet.out"
#SBATCH --chdir=/code/CEML/v2

DATA_DIR="../images/dogs_cats_parent/dogs_cats-sobel_x-sobel_y-composit"
CYCLES=20

echo "queue is `echo $SLURM_JOB_PARTITION`"
echo "running on `echo $SLURM_JOB_NODELIST`"
echo "work directory is `echo $SLURM_SUBMIT_DIR`"

echo $(date)
echo "CREATE COMPOSITE"
srun python3 process_images.py -i "../images/dogs_cats_parent/dogs_cats" --sobel_x --sobel_y --original

echo $(date)
echo "densenet121 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet121" --cycles $CYCLES

echo $(date)
echo "densenet169 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet169" --cycles $CYCLES

echo $(date)
echo "densenet201 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet201" --cycles $CYCLES

echo $(date)
echo "densenet161 MODEL"
srun python3 create_model.py --input $DATA_DIR --model "densenet161" --cycles $CYCLES



