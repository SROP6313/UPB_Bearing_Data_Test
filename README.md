# UPB_Bearing_Data_Test

## Introduction
Test and analyze the Bearing Fault open dataset in [Paderborn University Bearing DataCenter](https://mb.uni-paderborn.de/en/kat/main-research/datacenter/bearing-datacenter).

## Environment Setup
### Method 1: Use Anaconda .yml file
```bash
conda env create -f UPB_py36.yml
```
### Method 2: Use PyPI requirements file
```bash
conda create -n UPB_py36 python==3.6.5
pip install -r requirements_py365.txt
conda install ipykernel
```
### Method 3: Refer to the Self-LSTM original author's website 
[Deep ConvLSTM with self-attention for human activity decoding using wearable sensors](https://github.com/isukrit/encodingHumanActivity)
