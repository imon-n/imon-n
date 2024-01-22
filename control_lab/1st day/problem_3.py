import control as ctrl
import matplotlib.pyplot as plt

# Prompt the user to enter the numerator and denominator
num_str = input('Enter the numerator of the transfer function: ')
den_str = input('Enter the denominator of the transfer function: ')

# Convert the input strings to numerical arrays
num = list(map(float, num_str.split()))
den = list(map(float, den_str.split()))

# Create the transfer function
sys = ctrl.TransferFunction(num, den)

# Display the transfer function
print('Transfer Function:')
print(sys)

# Plot the step response
time, response = ctrl.step_response(sys)
plt.plot(time, response)
plt.title('Step Response')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
