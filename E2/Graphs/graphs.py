import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Plot 1: Common Emitter Output (image_578b68.png / image_578b30.png)
# ---------------------------------------------------------
vce_out = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10]
ic_20_out = [0.031, 6.825, 6.93, 7.005, 7.155, 7.158, 7.385, 7.583, 7.921]
ic_60_out = [0.031, 16.17, 19.015, 20.132, 20.732, 21.691, 23.07, 24.97, None]
ic_80_out = [0.029, 19.391, 23.11, 25.531, 26.58, 28.39, 30.14, 32.15, None]
ic_100_out = [0.0026, 22.4, 26.301, 29.56, 31.75, 34.5, 37.01, 40.57, None]

plt.figure(figsize=(8, 6))
plt.plot(vce_out, ic_20_out, marker='o', label='IB = 20 µA')
plt.plot(vce_out, ic_60_out, marker='s', label='IB = 60 µA')
plt.plot(vce_out, ic_80_out, marker='^', label='IB = 80 µA')
plt.plot(vce_out, ic_100_out, marker='d', label='IB = 100 µA')
plt.title('Common Emitter Output Characteristics')
plt.xlabel('VCE (V)')
plt.ylabel('IC (mA)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("emitter_output_characteristics.png")

# ---------------------------------------------------------
# Plot 2: Common Emitter Input (image_578b89.png)
# ---------------------------------------------------------
vbe_in = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.42, 0.44, 0.46, 0.48, 
          0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7]

ib_vce_1 = [0]*16 + [0.0001, 0.0004, 0.0008, 0.0012, 0.0019, 0.0029, 0.0041, 0.0056]
ib_vce_5 = [0]*16 + [0.0003, 0.0004, 0.0007, 0.0011, 0.0019, 0.003, 0.0044, 0.0057]
ib_vce_10 = [0]*15 + [0.0001, 0.0002, 0.0003, 0.0008, 0.0012, 0.002, 0.0034, 0.0047, 0.0063]

plt.figure(figsize=(8, 6))
plt.plot(vbe_in, ib_vce_1, marker='o', label='VCE = 1 V')
plt.plot(vbe_in, ib_vce_5, marker='s', label='VCE = 5 V')
plt.plot(vbe_in, ib_vce_10, marker='^', label='VCE = 10 V')
plt.title('Common Emitter Input Characteristics')
plt.xlabel('VBE (V)')
plt.ylabel('IB (mA)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("emitter_input_characteristics.png")

# ---------------------------------------------------------
# Plot 3: Common Collector Output (image_578ba8.png)
# ---------------------------------------------------------
# Data extracted from the table
V_EC = [0.0, 0.5, 1.0, 1.5, 2.0, 4.0, 6.0, 8.0]

# Emitter currents (I_E) in mA for different base currents (I_B)
I_E_20uA = [0.0016, 6.21, 6.24, 6.3, 6.35, 6.47, 6.65, 6.78]
I_E_60uA = [0.05, 16.01, 18.30, 18.60, 18.90, 19.65, 21.09, 21.9]
I_E_100uA = [0.09, 21.50, 24.62, 26.55, 27.35, 28.81, 30.4, 31.9]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each series with a line and markers
plt.plot(V_EC, I_E_20uA, marker='o', linestyle='-', label=r'$I_B = 20\mu A$')
plt.plot(V_EC, I_E_60uA, marker='s', linestyle='-', label=r'$I_B = 60\mu A$')
plt.plot(V_EC, I_E_100uA, marker='^', linestyle='-', label=r'$I_B = 100\mu A$')

# Labeling and titles
plt.title('CC Output Characteristics', fontsize=14, pad=15)
plt.xlabel(r'$V_{EC}$ (V)', fontsize=12)
plt.ylabel(r'$I_E$ (mA)', fontsize=12)

# Grid and Legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Base Current', fontsize=10, title_fontsize=11)

# Set axes limits starting from 0 for better visualization
plt.xlim(left=0)
plt.ylim(bottom=0)

# Display the plot
plt.tight_layout()
plt.savefig("collector_output_characteristics.png")

# ---------------------------------------------------------
# Plot 4: Common Collector Input (image_578e51.png)
# ---------------------------------------------------------
# Data extracted from the table

# Data extracted from the table
# V_EC = 1V Data
V_BC_1V = [0.593, 0.518, 0.418, 0.407, 0.39, 0.385, 0.382, 0.373, 0.374]
I_B_1V = [0, 0.1, 0.7, 1, 1.9, 2.2, 2.6, 3.9, 6]

# V_EC = 5V Data
V_BC_5V = [4.47, 4.44, 4.42, 4.40, 4.38, 4.36, 4.34, 4.32, 4.30]
I_B_5V = [0, 0.1, 0.5, 1, 2, 4.6, 9.7, 23, 61]

# V_EC = 10V Data
V_BC_10V = [9.42, 9.41, 9.40, 9.38, 9.36, 9.34]
I_B_10V = [0.0000, 0.4, 1, 2.0, 5.0, 13.4]

# Create the plot with a much wider figure size to stretch the curves out
plt.figure(figsize=(16, 6))

# Plot each series
plt.plot(V_BC_1V, I_B_1V, marker='o', linestyle='-', label=r'$V_{EC} = 1V$')
plt.plot(V_BC_5V, I_B_5V, marker='s', linestyle='-', label=r'$V_{EC} = 5V$')
plt.plot(V_BC_10V, I_B_10V, marker='^', linestyle='-', label=r'$V_{EC} = 10V$')

# Labeling and titles
plt.title('CC Input Characteristics', fontsize=14, pad=15)
plt.xlabel(r'$V_{BC}$ (V)', fontsize=12)
plt.ylabel(r'$I_B$ ($\mu$A)', fontsize=12)

# Create more divisions on the X-axis (ticks every 0.5V instead of auto-spacing)
plt.xticks(np.arange(0, 10.5, 0.5))

# Grid and Legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Emitter-Collector Voltage', fontsize=10, title_fontsize=11)

# Display the plot
plt.tight_layout()
plt.savefig("collector_input_characteristics.png")


# Data extracted from "image_5aab1c.png" (Common Base Input)
veb = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.42, 0.44, 0.46, 
       0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7]

ie_vcb_0 = [0.0007, 0.0606, 0.1207, 0.1816, 0.2417, 0.3026, 0.3625, 0.4227, 
            0.4835, 0.5077, 0.5316, 0.5562, 0.5801, 0.6044, 0.6287, 0.6528, 
            0.6768, 0.7009, 0.7252, 0.7495, 0.7734, 0.7977, 0.8219, 0.8456]

ie_vcb_5 = [0.0008, 0.0606, 0.1207, 0.1816, 0.2417, 0.3026, 0.3625, 0.4227, 
            0.4835, 0.5077, 0.5316, 0.5562, 0.5801, 0.6045, 0.6288, 0.6526, 
            0.6769, 0.7011, 0.7255, 0.7491, 0.7735, 0.7976, 0.822, 0.8454]

ie_vcb_10 = [0.0008, 0.0606, 0.1207, 0.1816, 0.2417, 0.3026, 0.3625, 0.4227, 
             0.4835, 0.5077, 0.5316, 0.5562, 0.5801, 0.6045, 0.6288, 0.6526, 
             0.6769, 0.7011, 0.7255, 0.7491, 0.7735, 0.7976, 0.822, 0.8454]

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(veb, ie_vcb_0, marker='o', linestyle='-', label='VCB = 0 V')
plt.plot(veb, ie_vcb_5, marker='s', linestyle='--', label='VCB = 5 V')
plt.plot(veb, ie_vcb_10, marker='^', linestyle=':', label='VCB = 10 V')

# Add labels and title
plt.title('Common Base Input Characteristics')
plt.xlabel('VEB (V)')
plt.ylabel('IE (mA)')

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("common_base_input_characteristics.png")


# Data extracted from "image_5c9144.png" (Common Base Output)
vcb = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# IC values for different IE levels
ic_ie_2 = [2.01] * len(vcb)
ic_ie_6 = [6.01] * len(vcb)
ic_ie_10 = [10.01] * len(vcb)

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(vcb, ic_ie_2, marker='o', linestyle='-', label='IE = 2 mA')
plt.plot(vcb, ic_ie_6, marker='s', linestyle='-', label='IE = 6 mA')
plt.plot(vcb, ic_ie_10, marker='^', linestyle='-', label='IE = 10 mA')

# Add labels and title
plt.title('Common Base Output Characteristics')
plt.xlabel('VCB (V)')
plt.ylabel('IC (mA)')

# Set y-axis limits to give some space around the straight lines
plt.ylim(0, 12)

# Add grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.tight_layout()
plt.savefig("common_base_output_characteristics.png")