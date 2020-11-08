''' 
Useful function to adjust data from the oscilloscope Rigol DS2000A

INPUTs:
    - data_file: .csv to read
    - ncols: number of columns to extract from the file
    - errs: consider also errors in the amplitude as 1% of the read value. False by default.

RETURNS:
    -> Array of columns with a quantity in each column. Time is the firt column.
'''

import numpy as np
from libphysics import *

def dataFix(data_file, errs=False):

    filetoread = os.path.join(data_file)
    
    # Assuming to find "dt" and "t_offset" in the second row, 3rd and 4th columns
    with open(filetoread, 'r') as f:
        lines = f.readlines()
        ncols = len(lines[2].split(',')) - 1 # -1 because of the extra "," at the end of the line in the csv
        line = lines[1]
        row = line.split(",")
        t_offset = float(row[ncols])
        dt = float(row[ncols+1])
    
    # Assuming time in the 1st column and assuming data starting from 3rd row
    data = readCSV(data_file, skiprows=2, cols=range(ncols))
    data = numpify(data)
    data = np.transpose(data)
    # Fix time values
    t = data[:,0]
    t = t_offset + t*dt
    data[:,0] = t
    # If errs flag is True adds uncertainties to data matrix
    if errs:
        dV = np.zeros((t.shape[0], ncols-1))
        for col in range(ncols-1):
            dV[:,col] = data[:,1+col] / 100 
        data = np.concatenate((data, dV), axis=1)
    return np.transpose(data)
