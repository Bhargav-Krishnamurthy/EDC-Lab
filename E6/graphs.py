import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# 1. EXPERIMENTAL DATA EXTRACTION
# ==============================================================================

# --- UNITY GAIN CONFIGURATION ---
# Input Amplitude = 100 mV peak (200 mV peak-to-peak reference)
# Combined low-frequency sweep and high-frequency sweep data
ug_frequency = np.array([
    # Low frequency sweep (1 Hz to 9.5 Hz)
    1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5,
    # Main sweep (10 Hz to 76,000 Hz)
    10, 20, 50, 500, 1000, 2000, 3000, 5000, 6000, 7000, 8000, 8200, 8400, 8600, 8800, 9000,
    9200, 9400, 9600, 9800, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000,
    19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000,
    31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000,
    43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000, 52000, 54000, 56000, 58000,
    60000, 62000, 64000, 66000, 68000, 70000, 72000, 74000, 76000
])

ug_vout_pp = np.array([
    # Low frequency Vout (mV peak-to-peak)
    172, 180, 188, 188, 196, 196, 204, 204, 204, 208, 212, 216, 220, 220, 220, 220, 224, 228, 228, 228, 228, 228, 228, 228, 228, 228,
    # Main sweep Vout (mV peak-to-peak)
    224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 220, 220, 220, 216, 216,
    216, 216, 216, 216, 216, 212, 212, 212, 208, 208, 204, 204, 200, 200, 196, 192,
    192, 188, 184, 184, 180, 176, 176, 172, 168, 168, 164, 164, 160, 156, 156, 152,
    152, 148, 144, 144, 140, 140, 136, 136, 132, 132, 128, 128, 124, 120, 120, 116,
    112, 108, 108, 104, 100, 96, 96, 92, 92, 88
])

# --- TEN GAIN CONFIGURATION ---
# Input Peak-to-Peak Amplitude = 40 mV
tg_frequency = np.array([1, 5, 7, 9, 10, 15, 50, 100, 200, 500, 700, 1000, 1200, 1500, 1700, 2000, 5000])
tg_vout_pp = np.array([312, 352, 396, 396, 388, 336, 288, 252, 296, 240, 224, 225, 240, 240, 224, 208, 176])


# ==============================================================================
# 2. GAIN CALCULATIONS
# ==============================================================================

# Unity Gain: Input amplitude = 100 mV peak (200 mV peak-to-peak)
ug_vin_pp = 200.0  # mV
ug_gain_linear = ug_vout_pp / ug_vin_pp
ug_gain_db = 20 * np.log10(ug_gain_linear)

# Ten Gain: Input peak-to-peak amplitude = 40 mV
tg_vin_pp = 40.0  # mV
tg_gain_linear = tg_vout_pp / tg_vin_pp
tg_gain_db = 20 * np.log10(tg_gain_linear)


# ==============================================================================
# 3. GRAPH 1: UNITY GAIN FREQUENCY RESPONSE
# ==============================================================================

fig1, ax1 = plt.subplots(figsize=(9, 5.5))

ax1.semilogx(ug_frequency, ug_gain_db, 'o-', color='#1f77b4', linewidth=2, markersize=4, label='Measured Gain (dB)')

# Reference Lines & Annotations
midband_ug = np.max(ug_gain_db)
ax1.axhline(y=midband_ug, color='red', linestyle='--', alpha=0.7, label=f'Midband Gain ({midband_ug:.2f} dB)')
ax1.axhline(y=midband_ug - 3.0, color='green', linestyle=':', alpha=0.8, label=f'-3 dB Level ({midband_ug - 3.0:.2f} dB)')

# Theoretical fc reference (15.9 Hz)
ax1.axvline(x=15.9, color='purple', linestyle='-.', alpha=0.6, label='Theoretical $f_c$ = 15.9 Hz')

ax1.set_title('Experiment 5: Unity Gain Frequency Response', fontsize=13, fontweight='bold', pad=12)
ax1.set_xlabel('Frequency (Hz)', fontsize=11)
ax1.set_ylabel('Gain $A_v$ (dB)', fontsize=11)
ax1.grid(True, which="both", linestyle='--', alpha=0.5)
ax1.legend(loc='lower left', frameon=True)

plt.tight_layout()
plt.savefig('unity_gain_frequency_response.png', dpi=300)


# ==============================================================================
# 4. GRAPH 2: TEN GAIN FREQUENCY RESPONSE
# ==============================================================================

fig2, ax2 = plt.subplots(figsize=(9, 5.5))

ax2.semilogx(tg_frequency, tg_gain_db, 's-', color='#ff7f0e', linewidth=2, markersize=5, label='Measured Gain (dB)')

# Reference Lines & Annotations
midband_tg = np.max(tg_gain_db)
ax2.axhline(y=midband_tg, color='red', linestyle='--', alpha=0.7, label=f'Midband Gain ({midband_tg:.2f} dB)')
ax2.axhline(y=midband_tg - 3.0, color='green', linestyle=':', alpha=0.8, label=f'-3 dB Level ({midband_tg - 3.0:.2f} dB)')

# Theoretical fc reference (15.9 Hz)
ax2.axvline(x=15.9, color='purple', linestyle='-.', alpha=0.6, label='Theoretical $f_c$ = 15.9 Hz')

ax2.set_title('Experiment 5: Gain-of-10 Frequency Response', fontsize=13, fontweight='bold', pad=12)
ax2.set_xlabel('Frequency (Hz)', fontsize=11)
ax2.set_ylabel('Gain $A_v$ (dB)', fontsize=11)
ax2.grid(True, which="both", linestyle='--', alpha=0.5)
ax2.legend(loc='lower left', frameon=True)

plt.tight_layout()
plt.savefig('ten_gain_frequency_response.png', dpi=300)

# Display plots
plt.show()