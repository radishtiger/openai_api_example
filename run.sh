#!/bin/bash
#SBATCH --job-name=openai_api_tutorial
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --time=0-00:10:00
#SBATCH --output=%A_out.log   
#SBATCH --error=%A_err.log
#SBATCH --mem=6400MB
#SBATCH --cpus-per-task=1

source ~/data/.bashrc
source ~/data/miniconda3/etc/profile.d/conda.sh

conda activate openai_api

srun python api_call.py