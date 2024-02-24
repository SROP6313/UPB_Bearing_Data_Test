import scipy.io
import pandas as pd
import numpy as np
import os
import glob

# Directory containing the .mat files
mat_files_dir = 'KI17'  # 這裡改為想要處理的資料夾
mat_files = glob.glob(os.path.join(mat_files_dir, '*.mat'))
file_len = len(mat_files)
file_index = 0

for mat_file in mat_files:
    # Extract base filename without extension for folder creation
    base_name = os.path.splitext(os.path.basename(mat_file))[0]
    newpath = os.path.join(mat_files_dir, base_name)
    
    # Create a directory for the current file's CSVs if it doesn't exist
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    # Load the .mat file
    mat_data = scipy.io.loadmat(mat_file)
    
    # Update the 'data_key' as per actual structure inside your .mat files
    data_key = base_name
    
    # 機械參數(軸承徑向力，負載力矩，速度)，取樣頻率 4KHz (16,002筆)
    mat_data_force = mat_data[data_key][0, 0]['Y']['Data'][0, 0]
    mat_data_speed = mat_data[data_key][0, 0]['Y']['Data'][0, 3]
    mat_data_torque = mat_data[data_key][0, 0]['Y']['Data'][0, 5]
    mat_data_ME_parameter_name = ['force', 'speed', 'torque']
    
    mat_data_concat = np.vstack((mat_data_force, mat_data_speed, mat_data_torque)).T
    mat_data_concat = np.vstack((mat_data_ME_parameter_name, mat_data_concat))
    df = pd.DataFrame(mat_data_concat)
    df.to_csv(os.path.join(newpath, f'{base_name}_ME_parameter.csv'), header=False, index=False)
    
    # 馬達電流、振動，取樣頻率 64KHz (256,002筆)
    mat_data_phase_current_1 = mat_data[data_key][0, 0]['Y']['Data'][0, 1]
    mat_data_phase_current_2 = mat_data[data_key][0, 0]['Y']['Data'][0, 2]
    mat_data_vibration_1 = mat_data[data_key][0, 0]['Y']['Data'][0, 6]
    mat_data_current_vib_name = ['phase_current_1', 'phase_current_2', 'vibration_1']

    mat_data_concat = np.vstack((mat_data_phase_current_1, mat_data_phase_current_2, mat_data_vibration_1)).T
    mat_data_concat = np.vstack((mat_data_current_vib_name, mat_data_concat))
    df = pd.DataFrame(mat_data_concat)
    df.to_csv(os.path.join(newpath, f'{base_name}_current_vib.csv'), header=False, index=False)

    # 溫度，取樣頻率 1Hz (5筆)
    mat_data_temp = mat_data[data_key][0, 0]['Y']['Data'][0, 4]
    mat_data_temp_name = ['temp_2_bearing_module']

    mat_data_temp = mat_data_temp.T
    mat_data_concat = np.vstack((mat_data_temp_name, mat_data_temp))
    df = pd.DataFrame(mat_data_concat)
    df.to_csv(os.path.join(newpath, f'{base_name}_temp.csv'), header=False, index=False)

    file_index += 1
    print("{} convert complete! ({}/{})".format(base_name, file_index, file_len))
