# -*- coding: utf-8 -*-
"""m22ma004_DL_Assign4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lQBJKQYgf-X0lPXdkE8_IpFGgIfjj2MN
"""



!pip install -q condacolab
import condacolab
condacolab.install()

!git clone https://github.com/BayesWatch/nas-without-training.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/nas-without-training

!conda env create -f /content/nas-without-training/env.yml

# !conda init bash
# !conda activate naswot2
# ??

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate naswot2
# cd /content/nas-without-training/src/nasbench-master
# python --version
# #?change setup.py file??
# pip install -e .

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate naswot2
# cd /content
# python --version
# git clone https://github.com/google-research/nasbench
#

#??change setup.py file

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate naswot2
# #change setup.py file
# cd /content/nasbench
# pip install -e .

from google.colab import drive
drive.mount('/content/mnt')

# %cd /content/nas-without-training
!unzip /content/mnt/MyDrive/DL_Assign/DL_Assignb4/data.zip

# %%bash
# source activate naswot2
# cd /content
# python --version
# git clone https://github.com/google-research/nasbench

# %%bash
# source activate naswot2
# #change setup.py file
# cd nasbench
# pip install -e .

# Commented out IPython magic to ensure Python compatibility.
# %cd /content
!mkdir /content/nas-without-training/nasbench   # create the directory
!mv /content/nasbench/nasbench/* /content/nas-without-training/nasbench   # move the files

# !cp -r /content/nasbench/nasbench /content/nas-without-training

# Commented out IPython magic to ensure Python compatibility.
# # !rm -r /content/nas-without-training/nasbench
# # !rm -r /content/nasbench
# 
# %%bash
# source activate naswot2
# python --version
# 
# python3.7 -m pip install yacs

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate naswot2
# python --version
# 
# pip install simplejson

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate naswot2
# cd /content/nas-without-training
# # python --version
# chmod +x scorehook.sh
# ./scorehook.sh



