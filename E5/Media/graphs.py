import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# 1. Common-Mode Transfer Characteristic (Req 1)
# ---------------------------------------------------------
V_cm = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 
                 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
V_D1 = np.array([9.15, 8.82, 8.53, 8.2, 7.98, 7.85, 7.76, 7.66, 7.58, 7.5, 
                 7.43, 7.36, 7.3, 7.23, 7.16, 7.1, 7.08, 7.0, 6.93])
V_D2 = np.array([8.985, 8.62, 8.27, 7.9, 7.646, 7.51, 7.393, 7.3, 7.21, 7.133, 
                 7.054, 6.974, 6.9, 6.84, 6.77, 6.72, 6.65, 6.59, 6.54])

plt.figure(figsize=(9, 6))
plt.plot(V_cm, V_D1, marker='o', linestyle='-', color='b', label='VD1')
plt.plot(V_cm, V_D2, marker='s', linestyle='-', color='r', label='VD2')

# Marking ICMR Limits
lower_icmr = 0.9
upper_icmr = 2.6
plt.axvline(x=lower_icmr, color='purple', linestyle=':', linewidth=2, label='Lower ICMR Limit (~0.9V)')
plt.axvline(x=upper_icmr, color='purple', linestyle=':', linewidth=2, label='Upper ICMR Data Bound')
plt.axvspan(lower_icmr, upper_icmr, color='purple', alpha=0.1, label='ICMR Region')

plt.title('Common-Mode Transfer Characteristic (VD1, VD2 vs Vcm)')
plt.xlabel('Common Mode Input Voltage Vcm (V)')
plt.ylabel('Drain Voltage (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('common_mode_icmr.png')
plt.close()

# ---------------------------------------------------------
# Differential Mode Data Processing
# ---------------------------------------------------------
V_gg1 = np.array([1.7, 1.73, 1.76, 1.79, 1.82, 1.85, 1.88, 1.91, 1.94, 1.97, 2.0, 
                  2.03, 2.06, 2.09, 2.12, 2.15, 2.18, 2.21, 2.24, 2.27, 2.3, 
                  2.33, 2.36, 2.39, 2.42, 2.45, 2.48, 2.51, 2.54])

V_out1_diff = np.array([9.99, 9.99, 9.99, 9.99, 9.99, 9.99, 9.98, 9.97, 9.94, 9.89, 9.8, 
                        9.65, 9.42, 9.1, 8.66, 8.15, 7.57, 6.97, 6.39, 5.87, 5.41, 
                        5.08, 4.824, 4.648, 4.53, 4.45, 4.394, 4.382, 4.37])

V_out2_diff = np.array([3.46, 3.474, 3.47, 3.473, 3.473, 3.478, 3.485, 3.5, 3.531, 3.588, 3.69, 
                        3.87, 4.14, 4.526, 5.039, 5.642, 6.32, 7.02, 7.71, 8.33, 8.85, 
                        9.25, 9.54, 9.73, 9.83, 9.89, 9.92, 9.9, 9.88])

# Calculate Vid (V_in+ - V_in-) in mV, assuming V_gg2 is constant at 2.2V
V_id = (V_gg1 - 2.2) * 1000

# Compute ID1 and ID2 in mA (VDD = 12V, RD = 130 ohms)
V_DD = 12.0
R_D = 130.0
I_D1 = (V_DD - V_out1_diff) / R_D * 1000
I_D2 = (V_DD - V_out2_diff) / R_D * 1000
delta_ID = I_D1 - I_D2

# Theoretical Data from Section 10
V_id_theo = np.array([-300, -200, -150, -100, -50, -25, 0, 25, 50, 100, 150, 200, 300])
delta_ID_theo = np.array([-79.93, -79.09, -76.73, -68.72, -45.45, -24.93, 0.00, 
                          24.93, 45.45, 68.72, 76.73, 79.09, 79.93])

# ---------------------------------------------------------
# 2. Linear Delta ID vs Vid with Theoretical Overlay (Req 2 & 4)
# ---------------------------------------------------------
plt.figure(figsize=(9, 6))
plt.plot(V_id, delta_ID, marker='o', linestyle='-', color='b', label='Measured $\Delta I_D$')
plt.plot(V_id_theo, delta_ID_theo, marker='s', linestyle='--', color='r', label='Theoretical $\Delta I_D$ (tanh)')

plt.title('Differential-Mode Transfer Characteristic (Linear Overlay)')
plt.xlabel('Differential Input Voltage Vid (mV)')
plt.ylabel('$\Delta I_D$ (mA)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('differential_linear_overlay.png')
plt.close()

# ---------------------------------------------------------
# 3. Semi-log plot of |Delta ID| vs Vid (Req 3)
# ---------------------------------------------------------
# Mask to filter out V_id exactly at 0 (to avoid log scale issues if delta_ID drops exactly to 0)
pos_mask = V_id > 0
neg_mask = V_id < 0

plt.figure(figsize=(9, 6))
plt.semilogy(V_id[pos_mask], np.abs(delta_ID[pos_mask]), marker='o', linestyle='-', color='g', label='Vid > 0')
plt.semilogy(V_id[neg_mask], np.abs(delta_ID[neg_mask]), marker='^', linestyle='-', color='m', label='Vid < 0')

plt.title('Weak-Inversion Test: $|\Delta I_D|$ vs Vid (Semi-log Axes)')
plt.xlabel('Differential Input Voltage Vid (mV)')
plt.ylabel('$|\Delta I_D|$ (mA) - Log Scale')
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.savefig('differential_semilog.png')
plt.close()