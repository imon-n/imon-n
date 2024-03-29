import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Define the 

t = np.arange(0, 10.01, 0.01)

# Define the input signal (in this case, a ramp)
u = t

# Prompt the user to enter the numerator and denominator
num_str = input('Enter the numerator of the transfer function: ')
den_str = input('Enter the denominator of the transfer function: ')

# Convert the input strings to numerical arrays
num = list(map(float, num_str.split()))
den = list(map(float, den_str.split()))

# Create the transfer function
sys = signal.TransferFunction(num, den)

print(sys)
# Display the transfer function
print('Transfer Function:')
print(sys)

# Simulate the response to the input signal
time, y, _ = signal.lsim(sys, u, t)

# Plot the response
plt.plot(time, y)
plt.title('System Response to Ramp Input')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()