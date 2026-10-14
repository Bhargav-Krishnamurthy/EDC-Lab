import os
os.environ['MPLCONFIGDIR'] = '/tmp'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set font and style for publication / B.Tech lab report
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['grid.color'] = '#dddddd'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.7

# -------------------------------------------------------------
# 1. Line Regulation Plot
# -------------------------------------------------------------
vin_line = np.array([3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 4.50, 4.75, 5.00])
vout_line = np.array([1.2007, 1.2007, 1.2008, 1.2007, 1.2007, 1.2008, 1.2006, 1.2008, 1.2008])
vg_line = np.array([2.138, 2.135, 2.132, 2.128, 2.125, 2.122, 2.120, 2.118, 2.118])

fig, ax1 = plt.subplots(figsize=(7, 4.5), dpi=300)

color_vout = '#1f77b4'
color_vg = '#d62728'

ax1.set_xlabel(r'Input Voltage $V_{IN}$ (V)', fontsize=11, fontweight='bold')
ax1.set_ylabel(r'Regulated Output $V_{OUT}$ (V)', color=color_vout, fontsize=11, fontweight='bold')
line1 = ax1.plot(vin_line, vout_line, marker='s', markersize=6, color=color_vout, linewidth=1.8, label=r'$V_{OUT}$ (Output Voltage)')
ax1.tick_params(axis='y', labelcolor=color_vout)
ax1.set_ylim(1.2000, 1.2015)
ax1.grid(True)

ax2 = ax1.twinx()
ax2.set_ylabel(r'Gate Voltage $V_G$ (V)', color=color_vg, fontsize=11, fontweight='bold')
line2 = ax2.plot(vin_line, vg_line, marker='o', markersize=6, color=color_vg, linewidth=1.8, linestyle='--', label=r'$V_G$ (Op-Amp Output)')
ax2.tick_params(axis='y', labelcolor=color_vg)
ax2.set_ylim(2.110, 2.145)

# Annotate line regulation
ax1.annotate(r'Line Reg = $\frac{\Delta V_{OUT}}{\Delta V_{IN}} = 0.10$ mV/V',
             xy=(4.0, 1.2007), xytext=(3.4, 1.2012),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
             fontsize=9.5, bbox=dict(boxstyle="round,pad=0.3", fc="#eef4ff", ec="#1f77b4", lw=1))

# Title and combined legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower left', framealpha=0.9)
plt.title(r'Line Regulation: Output & Gate Voltage vs. Input Supply ($R_L = 22\ \Omega$)', fontsize=11.5, pad=12, fontweight='bold')

plt.tight_layout()
plt.savefig('plot_line_reg.png', dpi=300)
plt.close()
print('Generated plot_line_reg.png')

# -------------------------------------------------------------
# 2. Load Regulation Plot
# -------------------------------------------------------------
iload = np.array([11.71, 26.61, 55.58, 118.67])
vout_3v = np.array([1.2012, 1.2011, 1.2007, 1.2002])
vout_5v = np.array([1.2012, 1.2011, 1.2007, 1.2001])
vg_3v = np.array([2.058, 2.101, 2.142, 2.196])
vg_5v = np.array([2.042, 2.086, 2.107, 2.145])

fig, (ax_v, ax_g) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Output voltage vs load current
ax_v.plot(iload, vout_3v, marker='o', color='#1f77b4', linewidth=1.8, label=r'$V_{IN} = 3.0$ V ($R_{OUT} = 9.35$ m$\Omega$)')
ax_v.plot(iload, vout_5v, marker='^', color='#2ca02c', linewidth=1.8, linestyle='--', label=r'$V_{IN} = 5.0$ V ($R_{OUT} = 10.28$ m$\Omega$)')
ax_v.set_xlabel(r'Load Current $I_{LOAD}$ (mA)', fontsize=10.5, fontweight='bold')
ax_v.set_ylabel(r'Output Voltage $V_{OUT}$ (V)', fontsize=10.5, fontweight='bold')
ax_v.set_ylim(1.1998, 1.2016)
ax_v.set_title(r'(a) Closed-Loop Output Voltage vs. $I_{LOAD}$', fontsize=11, fontweight='bold')
ax_v.grid(True)
ax_v.legend(loc='lower left', framealpha=0.9, fontsize=9)

# Gate voltage vs load current
ax_g.plot(iload, vg_3v, marker='s', color='#d62728', linewidth=1.8, label=r'$V_G$ at $V_{IN} = 3.0$ V')
ax_g.plot(iload, vg_5v, marker='d', color='#9467bd', linewidth=1.8, linestyle='--', label=r'$V_G$ at $V_{IN} = 5.0$ V')
ax_g.set_xlabel(r'Load Current $I_{LOAD}$ (mA)', fontsize=10.5, fontweight='bold')
ax_g.set_ylabel(r'Gate Drive Voltage $V_G$ (V)', fontsize=10.5, fontweight='bold')
ax_g.set_ylim(2.02, 2.22)
ax_g.set_title(r'(b) Gate Voltage Drive vs. $I_{LOAD}$', fontsize=11, fontweight='bold')
ax_g.grid(True)
ax_g.legend(loc='lower right', framealpha=0.9, fontsize=9)

plt.tight_layout()
plt.savefig('plot_load_reg.png', dpi=300)
plt.close()
print('Generated plot_load_reg.png')

# -------------------------------------------------------------
# 3. Dropout Characteristic Plot
# -------------------------------------------------------------
vin_drop = np.array([3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0])
vout_drop = np.array([1.2002, 1.2002, 1.2002, 1.2001, 1.2001, 1.2002, 1.2003, 1.2002, 1.2002, 1.2001, 1.2001, 1.2001, 1.2002, 1.1684, 1.0711, 0.9739, 0.8766, 0.7792, 0.6818, 0.5845, 0.4872, 0.38966, 0.2923, 0.1949, 0.0974, 0.0])
vg_drop = np.array([2.183, 2.187, 2.192, 2.199, 2.206, 2.212, 2.218, 2.221, 2.226, 2.232, 2.239, 2.251, 2.291, 4.391, 4.332, 4.274, 4.216, 4.157, 4.099, 4.041, 3.982, 3.924, 3.866, 3.807, 3.75, 3.691])

fig, ax1 = plt.subplots(figsize=(7.5, 4.8), dpi=300)

ax1.plot(vin_drop, vout_drop, marker='o', markersize=4.5, color='#1f77b4', linewidth=2, label=r'$V_{OUT}$ (Output Voltage)')
ax1.axhline(1.2002, color='#555555', linestyle=':', label='Regulated Target (1.200 V)')
ax1.axhline(1.1882, color='#e377c2', linestyle='--', label='1% Dropout Threshold (1.188 V)')

# Mark Dropout point
ax1.plot(1.262, 1.1882, marker='*', markersize=14, color='#d62728', zorder=5)
ax1.annotate(r'Dropout Threshold' + '\n' + r'$V_{IN,drop} = 1.262$ V' + '\n' + r'Headroom = $62$ mV',
             xy=(1.262, 1.1882), xytext=(1.5, 0.7),
             arrowprops=dict(facecolor='#d62728', shrink=0.08, width=1.2, headwidth=6),
             fontsize=9.5, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fff2f2", ec="#d62728", lw=1))

# Annotate Ohmic slope
ax1.annotate(r'Ohmic Triode Region' + '\n' + r'$V_{OUT} = 0.9737 V_{IN}$' + '\n' + r'$R_{DS(on)} = 0.275\ \Omega$',
             xy=(0.6, 0.5845), xytext=(0.08, 0.85),
             arrowprops=dict(facecolor='#1f77b4', shrink=0.08, width=1, headwidth=5),
             fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="#eef4ff", ec="#1f77b4", lw=1))

ax1.set_xlabel(r'Input Voltage $V_{IN}$ (V)', fontsize=11, fontweight='bold')
ax1.set_ylabel(r'Regulated Output $V_{OUT}$ (V)', color='#1f77b4', fontsize=11, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_ylim(-0.05, 1.35)
ax1.set_xlim(-0.1, 3.1)
ax1.grid(True)

# Secondary axis for Vg
ax2 = ax1.twinx()
ax2.plot(vin_drop, vg_drop, marker='x', markersize=4.5, color='#ff7f0e', linewidth=1.6, linestyle='-.', label=r'$V_G$ (Gate Voltage)')
ax2.set_ylabel(r'Gate Voltage $V_G$ (V)', color='#ff7f0e', fontsize=11, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#ff7f0e')
ax2.set_ylim(1.5, 5.0)

# Op-amp saturation annotation
ax2.annotate(r'Op-Amp Saturation' + '\n' + r'$V_G$ Spikes to $\sim 4.39$ V',
             xy=(1.2, 4.391), xytext=(0.35, 4.45),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.08, width=1, headwidth=5),
             fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="#fff9e6", ec="#ff7f0e", lw=1))

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', framealpha=0.9, fontsize=8.5)

plt.title(r'Dropout Characteristic and Op-Amp Saturation at Heavy Load ($R_L = 10.2\ \Omega$)', fontsize=11, pad=12, fontweight='bold')
plt.tight_layout()
plt.savefig('plot_dropout.png', dpi=300)
plt.close()
print('Generated plot_dropout.png')

# -------------------------------------------------------------
# 4. Efficiency and Power Dissipation Plot
# -------------------------------------------------------------
vin_eff = np.array([3.0, 3.5, 4.0, 4.5, 5.0])
eta_pass = np.array([38.58, 33.35, 29.17, 25.73, 23.15])
eta_tot_12v = np.array([35.61, 31.02, 27.42, 24.36, 22.00])
eta_ideal = 1.2 / vin_eff * 100
pdiss_linear = np.array([224.80, 282.28, 342.80, 407.75, 468.80])
pdiss_buck = np.full_like(vin_eff, 19.25)

fig, (ax_e, ax_p) = plt.subplots(1, 2, figsize=(11.5, 4.6), dpi=300)

# Efficiency comparison
ax_e.plot(vin_eff, eta_pass, marker='o', color='#1f77b4', linewidth=1.8, label=r'Measured Pass-Only $\eta$')
ax_e.plot(vin_eff, eta_tot_12v, marker='s', color='#9467bd', linewidth=1.8, linestyle='--', label=r'Measured Total $\eta$ (incl. Aux)')
ax_e.plot(vin_eff, eta_ideal, color='#2ca02c', linewidth=1.6, linestyle=':', label=r'Theoretical Limit ($V_{OUT}/V_{IN}$)')
ax_e.axhline(88.0, color='#d62728', linestyle='-.', linewidth=1.5, label='Buck Regulator Benchmark (88%)')

ax_e.set_xlabel(r'Input Supply $V_{IN}$ (V)', fontsize=10.5, fontweight='bold')
ax_e.set_ylabel(r'Efficiency $\eta$ (%)', fontsize=10.5, fontweight='bold')
ax_e.set_ylim(15, 95)
ax_e.set_title(r'(a) Regulator Efficiency vs. $V_{IN}$', fontsize=11, fontweight='bold')
ax_e.grid(True)
ax_e.legend(loc='upper right', framealpha=0.9, fontsize=8.5)

# Power dissipation comparison
ax_p.plot(vin_eff, pdiss_linear, marker='o', color='#d62728', linewidth=2, label=r'Linear Pass Transistor ($P_{diss}$)')
ax_p.plot(vin_eff, pdiss_buck, marker='^', color='#2ca02c', linewidth=2, linestyle='--', label=r'Buck Converter Loss ($P_{loss} \approx 19.3$ mW)')
ax_p.fill_between(vin_eff, pdiss_buck, pdiss_linear, color='#ffebee', alpha=0.6, label='Excess Wasted Power')

ax_p.set_xlabel(r'Input Supply $V_{IN}$ (V)', fontsize=10.5, fontweight='bold')
ax_p.set_ylabel(r'Heat Dissipated $P_{diss}$ (mW)', fontsize=10.5, fontweight='bold')
ax_p.set_ylim(0, 520)
ax_p.set_title(r'(b) Power Dissipated as Heat ($I_{LOAD} \approx 118$ mA)', fontsize=11, fontweight='bold')
ax_p.grid(True)
ax_p.legend(loc='upper left', framealpha=0.9, fontsize=8.5)

plt.tight_layout()
plt.savefig('plot_efficiency.png', dpi=300)
plt.close()
print('Generated plot_efficiency.png')
