import matplotlib.pyplot as plt

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
vec_out = [0, 0.5, 1, 1.5, 2, 4, 6, 8]
ie_20_out = [0.0001, 0.0653, 0.068, 0.0704, 0.0725, 0.082, 0.096, 0.499]
ie_60_out = [0.0001, 0.2245, 0.2326, 0.2396, 0.2463, 0.2743, 0.3261, 0.5947]
# Note: The last value (1324) seems to be an anomalous outlier in the original image, kept as printed.
ie_100_out = [0.0001, 0.4187, 0.426, 0.4512, 0.4631, 0.4867, 0.6158, 1.324]

plt.figure(figsize=(8, 6))
plt.plot(vec_out, ie_20_out, marker='o', label='IB = 20 µA')
plt.plot(vec_out, ie_60_out, marker='s', label='IB = 60 µA')
plt.plot(vec_out, ie_100_out, marker='^', label='IB = 100 µA')
plt.title('Common Collector Output Characteristics')
plt.xlabel('VEC (V)')
plt.ylabel('IE (mA)')
# Setting log scale for Y-axis due to the massive spike at the end of IB=100µA
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("collector_output_characteristics.png")

# ---------------------------------------------------------
# Plot 4: Common Collector Input (image_578e51.png)
# ---------------------------------------------------------
vbc_in = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
ib_vec_1 = [0, 0.0014, 0.0023, 0.1041, 0.1642, 0.2234, 0.2825, 0.3426, 0.4014, 
            0.4607, 0.5201, 0.5799, 0.6207, 0.6866, 0.7422, 0.7915, 0.877]
ib_vec_5 = [0, 0.0017, 0.0503, 0.1085, 0.1682, 0.2285, 0.2888, 0.35, 0.4107, 
            0.4717, 0.5297, 0.5884, 0.6495, 0.7097, 0.7315, 0.789, 0.867]
ib_vec_10 = [0, 0.0007, 0.06, 0.1222, 0.1845, 0.2462, 0.3076, 0.3694, 0.4309, 
             0.4915, 0.5417, 0.6016, 0.673, 0.7085, 0.7949, 0.8558, 0.9171]

plt.figure(figsize=(8, 6))
plt.plot(vbc_in, ib_vec_1, marker='o', label='VEC = 1 V')
plt.plot(vbc_in, ib_vec_5, marker='s', label='VEC = 5 V')
plt.plot(vbc_in, ib_vec_10, marker='^', label='VEC = 10 V')
plt.title('Common Collector Input Characteristics')
plt.xlabel('VBC (V)')
plt.ylabel('IB (µA)')
plt.grid(True)
plt.legend()
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