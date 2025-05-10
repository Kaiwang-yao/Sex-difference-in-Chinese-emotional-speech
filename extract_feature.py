import os
import numpy as np
import csv
# 'IS09_emotion': 384,
# "eGeMAPS": 88,

# Generate the command to be executed in the CMD terminal
def excuteCMD(ExcuteFile, Config, Audio, Output):
    cmd = ExcuteFile + " -C " + Config + " -I " + Audio + " -csvoutput " + Output
    print(cmd)
    return cmd

# Convert a .csv file to a list
def CsvToList(nameFront):
    with open(nameFront) as f:
        f_csv = csv.reader(f)


        header = next(f_csv)  # Extract the header (first row)
        l = []
        for row in f_csv:
            print("Original row:\n", row)
            l = row[0].split(';')[2:]  # Split by ';' and discard the first two elements to get features
            print("After removing first two elements and converting to list:\n", l)
            float_l = list(map(float, l))  # Convert all string elements to float
            print("Converted strings to floats:\n", float_l)
            print(len(l))
    os.remove(nameFront)  # Delete the file after reading
    return float_l

# Feature extraction
def ExtractFea():
    pathExcuteFile = r"F:\AI\SER\opensmile\bin\SMILExtract.exe"   #
    # pathConfig = r"F:\AI\SER\opensmile\config\is09-13\IS09_emotion.conf"
    pathConfig = r"F:\AI\SER\opensmile\config\egemaps\v01a\eGeMAPSv01a.conf"
    pathAudioRoot = r"F:\corpus\test\1"  # Folder containing wav files
    file_path = r"F:\corpus\test\2"  # Temporary folder to store csv features (create this manually)
    for wav in os.listdir(pathAudioRoot):  # Traverse all files in the folder
        pathAudio = os.path.join(pathAudioRoot, wav)
        print(pathAudio)
        csv_filedir = os.path.join(file_path, wav[0:-4]) + '.csv'  # Path to save extracted CSV features
        print("Save path:", csv_filedir)
        os.system(excuteCMD(pathExcuteFile, pathConfig, pathAudio, csv_filedir))
        l = CsvToList(csv_filedir)
        print(l)
    return 0

if __name__ == "__main__":
    ExtractFea()
