import matplotlib.pyplot as plt

# Data extracted from the provided Common Mode table
V_gg = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 
        2.1, 2.2, 2.3, 2.4, 2.5, 2.6]

V_out1 = [9.15, 8.82, 8.53, 8.2, 7.98, 7.85, 7.76, 7.66, 7.58, 7.5, 7.43, 
          7.36, 7.3, 7.23, 7.16, 7.1, 7.08, 7.0, 6.93]

V_out2 = [8.985, 8.62, 8.27, 7.9, 7.646, 7.51, 7.393, 7.3, 7.21, 7.133, 7.054, 
          6.974, 6.9, 6.84, 6.77, 6.72, 6.65, 6.59, 6.54]

I_net = [11, 15.2, 19.2, 23.22, 26.38, 27.94, 29.26, 30.43, 31.48, 32.46, 33.38, 
         34.25, 35.1, 35.9, 36.7, 37.46, 37.23, 38.98, 39.704]

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot V_out1 and V_out2 on the primary y-axis
line1, = ax1.plot(V_gg, V_out1, marker='o', linestyle='-', color='b', label='Vout1')
line2, = ax1.plot(V_gg, V_out2, marker='s', linestyle='-', color='r', label='Vout2')
ax1.set_xlabel('Common Mode Input Voltage Vgg (V)')
ax1.set_ylabel('Output Voltage (V)', color='k')
ax1.tick_params(axis='y', labelcolor='k')
ax1.grid(True)

# Create a secondary y-axis for I_net
ax2 = ax1.twinx()
line3, = ax2.plot(V_gg, I_net, marker='^', linestyle='--', color='g', label='I_net (mA)')
ax2.set_ylabel('Net Current I_net (mA)', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# --- Mark ICMR Limits ---
lower_icmr = 0.9  # Current begins collapsing below this point
upper_icmr = 2.6  # Safe active region extends through the end of the swept data

# Add vertical lines for the limits
line4 = ax1.axvline(x=lower_icmr, color='purple', linestyle=':', linewidth=2, label='Lower ICMR Limit (\u22480.9V)')
line5 = ax1.axvline(x=upper_icmr, color='purple', linestyle=':', linewidth=2, label='Upper ICMR Data Bound')

# Shade the valid ICMR region
patch = ax1.axvspan(lower_icmr, upper_icmr, color='purple', alpha=0.1, label='ICMR Region')

# Combine legends from both axes and the ICMR markers
handles = [line1, line2, line3, line4, patch]
labels = [h.get_label() for h in handles]
ax1.legend(handles, labels, loc='center right', bbox_to_anchor=(1.0, 0.6))

# Add title and layout adjustments
plt.title('Common Mode Transfer Characteristics with ICMR Limits')
fig.tight_layout()

# Display the plot
plt.savefig('Common_Mode_Transfer_Characteristics_with_ICMR_Limits.png', dpi=300)