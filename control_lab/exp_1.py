import numpy as np
from scipy.signal import zpk2tf, TransferFunction

# User input for zeros, poles, and gain
z = np.array(input('Enter zeroes: ').split(), dtype=float)
p = np.array(input('Enter poles: ').split(), dtype=float)
k = float(input('Enter gain: '))

# Convert zeros, poles, and gain to transfer function coefficients
numerator, denominator = zpk2tf(z, p, k)

# Display the numerator and denominator
print('Numerator Coefficients:', numerator)
print('Denominator Coefficients:', denominator)



