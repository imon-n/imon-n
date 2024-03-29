import numpy as np
from scipy.signal import TransferFunction

num = np.array(input('Enter the numerator of the transfer function: ').split(), dtype=float)
den = np.array(input('Enter the denominator of the transfer function: ').split(), dtype=float)

# Find zeros and poles using NumPy's roots function
zeros = np.roots(num)
poles = np.roots(den)

# Display zeros and poles
print('Zeros:', zeros)
print('Poles:', poles)
