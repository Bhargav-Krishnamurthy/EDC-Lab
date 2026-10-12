import os
os.environ['MPLCONFIGDIR'] = '/tmp'
import numpy as np
import matplotlib.pyplot as plt

# Set styling for clean, professional, human-looking engineering lab plots
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.0

# -------------------------------------------------------------
# 1. DC Transfer Characteristic: Vout vs Vin and Tail Current
# -------------------------------------------------------------
vin = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5])
vout = np.array([0.184, 0.660, 1.158, 1.653, 2.150, 2.645, 3.139, 3.633, 4.126, 4.622, 5.115, 5.607, 6.090, 6.580, 7.060, 7.550])
ics = np.array([18.45, 29.47, 34.30, 38.241, 41.90, 45.48, 49.146, 52.988, 57.062, 61.45, 66.19, 71.313, 77.10, 83.803, 91.48, 101.45])

fig, ax1 = plt.subplots(figsize=(7, 5))

color = '#1f77b4'
ax1.set_xlabel(r'Input Voltage $V_{in}$ (V)')
ax1.set_ylabel(r'Output Voltage $V_{out}$ (V)', color=color)
line1 = ax1.plot(vin, vout, marker='o', markersize=5, linestyle='-', color=color, label=r'$V_{out}$ vs $V_{in}$')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6)

# Highlight linear range vs thermal region
ax1.axvspan(1.5, 3.5, color='green', alpha=0.08, label='Linear Operating Region')

# Twin axis for tail current to illustrate thermal runaway
ax2 = ax1.twinx()
color2 = '#d62728'
ax2.set_ylabel(r'Tail Current $I_{cs}$ (mA)', color=color2)
line2 = ax2.plot(vin, ics, marker='s', markersize=4, linestyle='--', color=color2, label=r'Mirror Current $I_{cs}$')
ax2.tick_params(axis='y', labelcolor=color2)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', framealpha=0.9)

plt.title('DC Transfer Characteristic & Tail Mirror Current')
fig.tight_layout()
plt.savefig('dc_transfer.png', dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. AC Frequency Response: Bode Plot
# -------------------------------------------------------------
freq = np.array([6, 8, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000])
vout_ac = np.array([192, 192, 192, 194, 194, 194, 196, 196, 198, 200, 200]) # mV pk-pk
vin_ac = 200.0 # mV pk-pk
gain_linear = vout_ac / vin_ac
gain_db = 20 * np.log10(gain_linear)

fig, ax = plt.subplots(figsize=(7, 4.8))
ax.semilogx(freq, gain_db, marker='s', markersize=6, linestyle='-', color='#d62728', label='Measured Gain (dB)')
ax.set_title('Frequency Response: Small-Signal Voltage Gain')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Voltage Gain (dB)')
ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.set_ylim([-0.5, 0.1])

# Annotate mid-band region
ax.axhline(0, color='gray', linestyle=':', alpha=0.7)
ax.annotate(r'$A_v \approx 0.98$ (-0.18 dB) @ 1 kHz', xy=(1000, -0.175), xytext=(1200, -0.32),
            arrowprops=dict(facecolor='black', shrink=0.08, width=0.8, headwidth=5),
            fontsize=9.5)
ax.legend(loc='lower right')
fig.tight_layout()
plt.savefig('bode_plot.png', dpi=300)
plt.close()

# -------------------------------------------------------------
# 3. Output Resistance Loading Effect
# -------------------------------------------------------------
RL = np.array([10.2, 47.0, 112.0])
vout_loaded = np.array([174.0, 188.0, 192.0])
vout_unloaded = 196.0
ratio_measured = vout_loaded / vout_unloaded

RL_theory = np.linspace(2, 130, 200)
Rout_10V = 1.18  # Adjusted theory for 10V supply (Iref ≈ 33 mA, gm ≈ 0.85 A/V)
Rout_12V = 0.96  # Manual nominal at 12V supply (Iref ≈ 40.4 mA, gm ≈ 1.04 A/V)
ratio_10V = RL_theory / (RL_theory + Rout_10V)
ratio_12V = RL_theory / (RL_theory + Rout_12V)

fig, ax = plt.subplots(figsize=(7, 4.8))
ax.plot(RL_theory, ratio_10V, linestyle='-', color='#1f77b4', linewidth=1.8, label=r'10V Theory ($R_{out} = 1.18\ \Omega$, bench supply)')
ax.plot(RL_theory, ratio_12V, linestyle=':', color='#7f7f7f', linewidth=1.5, label=r'12V Manual Spec ($R_{out} = 0.96\ \Omega$)')
ax.plot(RL, ratio_measured, marker='o', markersize=7, linestyle='None', color='#2ca02c', label='Measured Data Points')

for r, rat in zip(RL, ratio_measured):
    ax.annotate(f'({r:.1f} $\Omega$, {rat:.3f})', xy=(r, rat), xytext=(r + 3, rat - 0.025),
                fontsize=9)

ax.set_title(r'Output Loading Effect: $V_{out,loaded} / V_{out,unloaded}$ vs $R_L$')
ax.set_xlabel(r'Load Resistance $R_L\ (\Omega)$')
ax.set_ylabel(r'Normalized Voltage Ratio $V_{out,loaded} / V_{out,unloaded}$')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='lower right', framealpha=0.9)
ax.set_ylim([0.80, 1.02])
fig.tight_layout()
plt.savefig('loading_effect.png', dpi=300)
plt.close()

print('All 3 plots successfully generated.')
