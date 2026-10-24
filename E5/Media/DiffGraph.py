import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the provided Differential Mode table
V_gg1 = [1.7, 1.73, 1.76, 1.79, 1.82, 1.85, 1.88, 1.91, 1.94, 1.97, 2.0, 
         2.03, 2.06, 2.09, 2.12, 2.15, 2.18, 2.21, 2.24, 2.27, 2.3, 
         2.33, 2.36, 2.39, 2.42, 2.45, 2.48, 2.51, 2.54]

V_out1 = [9.99, 9.99, 9.99, 9.99, 9.99, 9.99, 9.98, 9.97, 9.94, 9.89, 9.8, 
          9.65, 9.42, 9.1, 8.66, 8.15, 7.57, 6.97, 6.39, 5.87, 5.41, 
          5.08, 4.824, 4.648, 4.53, 4.45, 4.394, 4.382, 4.37]

V_out2 = [3.46, 3.474, 3.47, 3.473, 3.473, 3.478, 3.485, 3.5, 3.531, 3.588, 3.69, 
          3.87, 4.14, 4.526, 5.039, 5.642, 6.32, 7.02, 7.71, 8.33, 8.85, 
          9.25, 9.54, 9.73, 9.83, 9.89, 9.92, 9.9, 9.88]

I_net = [36.08, 36.06, 36.06, 36.05, 36.04, 36.05, 36.05, 36.05, 36.06, 36.06, 36.08, 
         36.12, 36.18, 36.25, 36.34, 36.45, 36.58, 36.71, 36.85, 36.98, 37.14, 
         37.3, 37.48, 37.66, 37.88, 38.09, 38.3, 38.53, 38.75]

# --- Theoretical tanh curve calculations ---
# Convert lists to numpy array for vector operations
V_gg1_arr = np.array(V_gg1)

# Generate a smooth array of x-values for the theoretical curves
V_gg1_smooth = np.linspace(min(V_gg1_arr), max(V_gg1_arr), 200)
V_id_smooth = V_gg1_smooth - 2.2  # Vgg2 is constant at 2.2V

# Parameters from Section 10 of the Lab Manual
ISS_theo = 80.0       # mA
n_theo = 1.5          # Slope factor
VT = 0.02585          # Thermal voltage in V (25.85 mV)
RD = 130.0            # Drain resistor in ohms
VDD = 12.0            # Supply voltage

# Calculate theoretical delta ID and branch currents
delta_ID_theo = ISS_theo * np.tanh(V_id_smooth / (2 * n_theo * VT))
ID1_theo = (ISS_theo + delta_ID_theo) / 2
ID2_theo = (ISS_theo - delta_ID_theo) / 2

# Calculate theoretical output voltages
V_out1_theo = VDD - (ID1_theo * RD / 1000.0)
V_out2_theo = VDD - (ID2_theo * RD / 1000.0)
# -------------------------------------------

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot experimental V_out1 and V_out2 as discrete markers
ax1.plot(V_gg1, V_out1, marker='o', linestyle='none', color='b', label='Measured Vout1')
ax1.plot(V_gg1, V_out2, marker='s', linestyle='none', color='r', label='Measured Vout2')

# Overlay the theoretical tanh curves as solid lines
ax1.plot(V_gg1_smooth, V_out1_theo, linestyle='-', color='cyan', linewidth=2, label='Theoretical Vout1 (tanh)')
ax1.plot(V_gg1_smooth, V_out2_theo, linestyle='-', color='magenta', linewidth=2, label='Theoretical Vout2 (tanh)')

ax1.set_xlabel('Vgg1 (V) [with Vgg2 constant at 2.2V]')
ax1.set_ylabel('Output Voltage (V)', color='k')
ax1.tick_params(axis='y', labelcolor='k')
ax1.grid(True)

# Create a secondary y-axis for I_net
ax2 = ax1.twinx()
ax2.plot(V_gg1, I_net, marker='^', linestyle=':', color='g', label='Measured I_net (mA)')
ax2.set_ylabel('Net Current I_net (mA)', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Combine legends from both axes and position them so they don't block the data
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='center right')

# Add title and layout adjustments
plt.title('Differential Mode Transfer Characteristics with Theoretical tanh Overlay')
fig.tight_layout()

# Save the plot
plt.savefig('Differential_Mode_Transfer_Characteristics.png', dpi=300)