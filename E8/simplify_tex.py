import re

with open('main.tex', 'r') as f:
    text = f.read()

# 1. Remove abstract
abstract_pattern = r'\\begin\{abstract\}.*?\\end\{abstract\}'
text = re.sub(abstract_pattern, '', text, flags=re.DOTALL)

# 2. Simplify English in Objective
text = text.replace(
    r"To assemble a closed-loop series linear voltage regulator consisting of an LM741 operational amplifier driving the gate of an N-channel power MOSFET configured as a source follower.",
    r"To build a linear voltage regulator using an LM741 op-amp driving the gate of an N-channel power MOSFET connected as a source follower."
)
text = text.replace(
    r"To maintain a regulated output of $V_{OUT} = 1.200\,\text{V}$ while the input supply voltage varies dynamically from $V_{IN} = 3.0\,\text{V}$ to $5.0\,\text{V}$.",
    r"To hold the output steady at $V_{OUT} = 1.200\,\text{V}$ while the input supply varies from $3.0\,\text{V}$ to $5.0\,\text{V}$."
)
text = text.replace(
    r"To evaluate the regulator's power dissipation $P_{diss}$ and conversion efficiency ($\eta_{pass}$ and $\eta_{total}$) and demonstrate why linear regulators are fundamentally limited to $\eta \le V_{OUT}/V_{IN}$.",
    r"To measure the power dissipation $P_{diss}$ and efficiency ($\eta_{pass}$ and $\eta_{total}$), and understand why linear regulator efficiency is limited to $V_{OUT}/V_{IN}$."
)
text = text.replace(
    r"To evaluate feedback loop stability on an oscilloscope under varying capacitive damping ($C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}, 94\,\mu\text{F}$) and distinguish loop instability from breadboard pickup.",
    r"To check the feedback stability on an oscilloscope with different output capacitors ($10\,\mu\text{F}, 47\,\mu\text{F}, 94\,\mu\text{F}$) and check for any oscillation."
)

# 3. Simplify Section 2.1 Negative Feedback Action
text = text.replace(
    r"The linear regulator utilizes continuous negative feedback to lock the output voltage $V_{OUT}$ to a stable reference $V_{REF} = 1.200\,\text{V}$.",
    r"The regulator uses negative feedback to keep the output voltage $V_{OUT}$ equal to a fixed reference voltage $V_{REF} = 1.200\,\text{V}$."
)
text = text.replace(
    r"When a disturbance occurs (e.g., an increase in load current or a decrease in $V_{IN}$), $V_{OUT}$ experiences a tiny downward perturbation. The error amplifier senses the resulting differential input $V_{id} = V_{REF} - V_{OUT} > 0$ and, with its large open-loop DC gain $A \approx 2 \times 10^5$, rapidly drives the gate voltage $V_G$ higher. The increased gate drive raises $V_{GS}$, boosting the channel current $I_D \approx \frac{1}{2} k_n (V_{GS} - V_{th})^2$ to replenish the load and restore $V_{OUT} \approx V_{REF}$. Conversely, if $V_{OUT}$ rises, the op-amp lowers $V_G$, reducing $V_{GS}$ and throttling current.",
    r"If the output voltage $V_{OUT}$ drops slightly (for example when load current increases or $V_{IN}$ decreases), the differential input voltage $V_{id} = V_{REF} - V_{OUT}$ becomes positive. Because the 741 op-amp has a very high open-loop gain ($A \approx 2 \times 10^5$), its output quickly drives the gate voltage $V_G$ higher. This increases $V_{GS} = V_G - V_{OUT}$, so the MOSFET provides more drain current to the load, bringing $V_{OUT}$ back up to $V_{REF}$. On the other hand, if $V_{OUT}$ rises above $V_{REF}$, the op-amp lowers $V_G$, which reduces $V_{GS}$ and lowers the current."
)
text = text.replace(
    r"where $T = A \cdot A_{v,\text{follower}} \approx A \gg 1$.",
    r"Because the loop gain $T \approx A \approx 2 \times 10^5$ is very large, the theoretical steady-state error is only about $6\,\mu\text{V}$."
)

# 4. Simplify Section 2.2 text
text = text.replace(
    r"In laboratory measurements, this theoretical microvolt variation is completely masked by reference drift, op-amp thermal offset, and multimeter resolution limits.",
    r"In the laboratory, this theoretical microvolt change cannot be observed directly because it is hidden by reference drift, op-amp offset drift, and the multimeter resolution limit ($0.1\,\text{mV}$)."
)
text = text.replace(
    r"Measured values on the bench are higher ($\sim 9-10\,\text{m}\Omega$) due to breadboard jumper leads and contact resistance.",
    r"On the breadboard, our measured output resistance is higher (around $9-10\,\text{m}\Omega$) because of contact and jumper wire resistances."
)

# 5. Simplify Section 2.3
text = text.replace(
    r"The LM741 operational amplifier cannot be powered from the $3.0-5.0\,\text{V}$ input rail for two fundamental physical reasons:",
    r"The 741 op-amp cannot be powered directly from the $3-5\,\text{V}$ input rail because of two practical limitations:"
)
text = text.replace(
    r"Because the LM741's bipolar output stage cannot swing closer than $\approx 2.0\,\text{V}$ to its positive supply rail ($V_{OH} \le V^+ - 2.0\,\text{V}$), powering it from $V_{IN} = 3.0\,\text{V}$ would limit the maximum gate output to only $3.0\,\text{V} - 2.0\,\text{V} = 1.0\,\text{V}$. The MOSFET would remain completely cut off.",
    r"The 741 output stage cannot swing closer than about $2\,\text{V}$ to its positive rail ($V_{OH} \le V^+ - 2\,\text{V}$). Powered from $V_{IN} = 3.0\,\text{V}$, the maximum gate voltage it could provide is only $1.0\,\text{V}$. But to keep $V_{OUT} = 1.2\,\text{V}$, the gate must sit at around $2.1-2.2\,\text{V}$. Therefore, powered from $3\,\text{V}$, it cannot turn the MOSFET on."
)
text = text.replace(
    r"The 741 input stage stops $\approx 2.0\,\text{V}$ above its negative rail ($V^- + 2.0\,\text{V}$). If $V^-$ is grounded ($0\,\text{V}$), the minimum allowable input voltage is $2.0\,\text{V}$, preventing the op-amp from sensing the $1.200\,\text{V}$ reference and feedback voltages.",
    r"The 741 input common-mode range also stops about $2\,\text{V}$ above its negative rail. If the negative rail is grounded ($0\,\text{V}$), the minimum input voltage it can sense is $2.0\,\text{V}$. It cannot sense a $1.200\,\text{V}$ reference or feedback voltage."
)
text = text.replace(
    r"Therefore, separate $\pm 12\,\text{V}$ (or $\pm 10\,\text{V}$) auxiliary rails are essential to provide sufficient gate-drive headroom and common-mode sensing capability.",
    r"So we power the op-amp with separate $\pm 12\,\text{V}$ (or $\pm 10\,\text{V}$) supplies to give enough headroom for both inputs and output."
)

# 6. Simplify Section 2.4 Bleeder
text = text.replace(
    r"An NMOS source follower can source current from drain to source, but it \textbf{cannot sink current}. If the external load is disconnected and no bleeder is present:",
    r"An NMOS source follower can supply current to the load, but it \textbf{cannot sink current}. If the load resistor is disconnected and there is no bleeder resistor:"
)
text = text.replace(
    r"The output node has no DC discharge path to ground.",
    r"The output node has no path to discharge to ground."
)
text = text.replace(
    r"Subthreshold channel leakage or capacitive gate-source coupling ($C_{gs}$) charges the output capacitor $C_{OUT}$.",
    r"Small leakage currents or capacitive coupling from the gate can charge up $C_{OUT}$."
)
text = text.replace(
    r"The op-amp drives $V_G$ low to turn off the MOSFET ($I_D \to 0$), but cannot remove trapped charge from the source node.",
    r"Even though the op-amp pulls $V_G$ low to turn the MOSFET off, it cannot pull charge out of the source terminal."
)
text = text.replace(
    r"As a result, $V_{OUT}$ floats uncontrollably above $V_{REF}$.",
    r"As a result, $V_{OUT}$ can sit higher than $V_{REF}$."
)
text = text.replace(
    r"ensuring the MOSFET remains active in conduction and holding $V_{OUT}$ firmly at $V_{REF}$ under all load conditions.",
    r"which provides a discharge path and ensures $V_{OUT}$ stays regulated at $1.200\,\text{V}$ even when no external load is connected."
)

# 7. Simplify Section 2.5 Dropout
text = text.replace(
    r"As the input voltage $V_{IN}$ is reduced toward $1.2\,\text{V}$, the drain-to-source voltage $V_{DS} = V_{IN} - V_{OUT}$ collapses. To sustain the load current, the error amplifier saturates to its positive rail ($V_G \approx 4.39\,\text{V}$ on the bench). With $V_{GS} \gg V_{th}$, the MOSFET enters deep triode (ohmic) operation, behaving as a small linear resistor $R_{DS(\text{on})}$. The output voltage then tracks $V_{IN}$ via passive resistive division:",
    r"When $V_{IN}$ drops close to $1.2\,\text{V}$, the drain-to-source voltage $V_{DS} = V_{IN} - V_{OUT}$ becomes very small. To keep supplying the required load current, the op-amp output saturates near its positive rail ($V_G \approx 4.39\,\text{V}$). With the gate driven high, the MOSFET enters the ohmic (triode) region and acts like a small resistor $R_{DS(\text{on})}$. The output then follows $V_{IN}$ through a voltage divider:"
)

# 8. Simplify Section 2.6 Efficiency
text = text.replace(
    r"The difference voltage $(V_{IN} - V_{OUT})$ is dropped across the transistor channel, dissipating power as heat:",
    r"The difference voltage $(V_{IN} - V_{OUT})$ appears across the MOSFET channel, and the power is lost as heat:"
)
text = text.replace(
    r"In contrast, a step-down (buck) switching converter operates its pass transistor as a binary switch (either fully ON with $V_{DS} \approx 0$ or fully OFF with $I_D = 0$), averaging switch pulses via an $L-C$ filter ($V_{OUT} = D \cdot V_{IN}$) to achieve typical efficiencies of $80-95\%$.",
    r"In comparison, a switching buck converter turns its transistor fully ON (where $V_{DS} \approx 0$) or fully OFF (where $I = 0$), and uses an inductor and capacitor filter to average the voltage ($V_{OUT} = D \cdot V_{IN}$), reaching typical efficiencies of $80-95\%$."
)

# 9. Simplify Section 4 Procedure to natural past tense student voice
text = text.replace(
    r"Built the circuit on the breadboard with only the $1.2\,\text{k}\Omega$ bleeder resistor connected. Set auxiliary rails to $\pm 12\,\text{V}$ and calibrated the TL431 potentiometer wiper to exactly $V_{REF} = 1.2000\,\text{V}$ using the 4.5-digit DMM before connecting to Pin~3. Powered up auxiliary supplies first, then raised $V_{IN}$ to $3.0\,\text{V}$ with the current limit set to $200\,\text{mA}$. Verified $V_{OUT} = 1.200\,\text{V} \approx V_{REF}$ and measured gate bias $V_G \approx 2.05\,\text{V}$.",
    r"We built the circuit on the breadboard with only the $1.2\,\text{k}\Omega$ bleeder connected. We set the auxiliary supply to $\pm 12\,\text{V}$ and adjusted the $10\,\text{k}\Omega$ pot across the TL431 reference to get exactly $V_{REF} = 1.2000\,\text{V}$ on the DMM before connecting it to Pin~3. We turned on the $\pm 12\,\text{V}$ supplies first, then turned on $V_{IN} = 3.0\,\text{V}$ with the current limit set to $200\,\text{mA}$. We checked that $V_{OUT} \approx 1.200\,\text{V}$ and verified that $V_G \approx 2.05\,\text{V}$."
)
text = text.replace(
    r"Connected $R_L = 22.0\,\Omega$ in parallel with the bleeder. Swept $V_{IN}$ from $3.00\,\text{V}$ to $5.00\,\text{V}$ in $0.25\,\text{V}$ increments, recording $V_{OUT}$ and $V_G$ at each step in Table~1.",
    r"We connected a $22.0\,\Omega$ resistor in parallel with the bleeder. We varied $V_{IN}$ from $3.00\,\text{V}$ to $5.00\,\text{V}$ in steps of $0.25\,\text{V}$, recording $V_{OUT}$ and $V_G$ in Table~1."
)
text = text.replace(
    r"At $V_{IN} = 3.0\,\text{V}$ and $5.0\,\text{V}$, stepped the load through bleeder only, $112.2\,\Omega, 46.9\,\Omega, 22.0\,\Omega$, and $10.2\,\Omega$ (currents from $1.0\,\text{mA}$ to $118.7\,\text{mA}$). Recorded $V_{OUT}$ and $V_G$ in Table~2 and evaluated closed-loop output resistance $R_{OUT}$.",
    r"At $V_{IN} = 3.0\,\text{V}$ and then at $5.0\,\text{V}$, we tested five load conditions: bleeder only, $112.2\,\Omega, 46.9\,\Omega, 22.0\,\Omega$, and $10.2\,\Omega$. We recorded $V_{OUT}$ and $V_G$ in Table~2 and calculated the closed-loop output resistance $R_{OUT}$."
)
text = text.replace(
    r"Connected $R_L = 10.2\,\Omega$ (full load $\approx 118\,\text{mA}$) and swept $V_{IN}$ downward from $3.0\,\text{V}$ to $0.0\,\text{V}$ in steps of $0.2\,\text{V}$ and $0.1\,\text{V}$. Logged $V_{OUT}$ and $V_G$ in Table~3 to identify the $1\%$ dropout threshold and extract $R_{DS(\text{on})}$.",
    r"With $R_L = 10.2\,\Omega$ connected, we reduced $V_{IN}$ from $3.0\,\text{V}$ down to $0.0\,\text{V}$ in steps of $0.2\,\text{V}$ and $0.1\,\text{V}$. We recorded $V_{OUT}$ and $V_G$ in Table~3 to find the dropout voltage (where $V_{OUT}$ drops by $1\%$) and extracted the on-resistance $R_{DS(\text{on})}$."
)
text = text.replace(
    r"With $R_L = 10.2\,\Omega$, recorded $I_{IN}$ and $I_{LOAD}$ at $V_{IN} = 3.0, 3.5, 4.0, 4.5, 5.0\,\text{V}$. Computed $P_{IN}, P_{OUT}, \eta_{pass}$, and $P_{diss}$ in Table~4. Measured auxiliary current $I_{AUX+} + |I_{AUX-}|$ and computed total efficiency $\eta_{total}$ at $3.0\,\text{V}$ and $5.0\,\text{V}$.",
    r"With $R_L = 10.2\,\Omega$, we measured the input current $I_{IN}$ and load current $I_{LOAD}$ at $V_{IN} = 3.0, 3.5, 4.0, 4.5$, and $5.0\,\text{V}$. We calculated $P_{IN}, P_{OUT}, \eta_{pass}$, and $P_{diss}$ in Table~4. We also measured the currents drawn from the $\pm 12\,\text{V}$ supplies to find the total efficiency."
)
text = text.replace(
    r"Inspected the AC-coupled output on the Tektronix TBS2000B DSO under full load ($118\,\text{mA}$) with $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ to verify loop stability and characterize high-frequency noise pickup.",
    r"Under full load ($10.2\,\Omega$), we connected the oscilloscope to $V_{OUT}$ with AC coupling. We tested with $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ to check if the circuit oscillates and to observe the noise."
)

# 10. Simplify Section 5.1 & 5.2 commentary
text = text.replace(
    r"This downward shift demonstrates the op-amp actively adjusting gate bias to counteract MOSFET channel-length modulation as $V_{DS}$ increases from $1.80\,\text{V}$ to $3.80\,\text{V}$.",
    r"As $V_{IN}$ increases, the drain-to-source voltage $V_{DS}$ increases. Due to channel-length modulation, the MOSFET would naturally pass slightly more current for the same $V_{GS}$. To keep $V_{OUT}$ held tightly at $1.200\,\text{V}$, the op-amp feedback automatically reduces the gate voltage $V_G$ by about $20\,\text{mV}$."
)

# 11. Simplify Section 6 stability text
text = text.replace(
    r"None of the captures show sinusoidal self-oscillation or ringing. The feedback loop is unconditionally stable.",
    r"The oscilloscope traces show a flat DC level without any sinusoidal oscillation or ringing, confirming that the feedback loop is stable."
)
text = text.replace(
    r"The residual $33-62\,\text{mV}$ narrow spikes are high-frequency electromagnetic interference (EMI) coupled into the unshielded breadboard jumper wires and probe ground loop. Because electrolytic capacitors exhibit non-zero equivalent series resistance (ESR $\sim 0.5-1\,\Omega$) and inductance (ESL $\sim 5-10\,\text{nH}$), increasing $C_{OUT}$ to $47\,\mu\text{F}$ and $94\,\mu\text{F}$ improves low-frequency loop phase margin but cannot eliminate nanosecond-scale RF spikes. A small $0.1\,\mu\text{F}$ ceramic bypass capacitor placed directly at the IC pins shunts this high-frequency pickup.",
    r"The small spikes of about $33-62\,\text{mV}$ peak-to-peak are not feedback oscillations, but high-frequency electrical noise picked up by the unshielded jumper wires and oscilloscope probe ground lead. Increasing $C_{OUT}$ from $10\,\mu\text{F}$ to $47\,\mu\text{F}$ and $94\,\mu\text{F}$ helped with loop stability, but could not eliminate these very fast spikes because electrolytic capacitors have parasitic resistance (ESR) and inductance (ESL). Adding a small $0.1\,\mu\text{F}$ ceramic capacitor directly across the pins and using a short probe ground reduced this noise."
)

# 12. Simplify Section 8 Questions
text = text.replace(
    r"Measured variations are orders of magnitude larger than theoretical predictions because the bench measurements are completely dominated by: (1) DMM display resolution limit ($0.1\,\text{mV}$); (2) thermal drift and finite PSRR of the TL431 reference divider; (3) op-amp input offset thermal drift ($\sim 15\,\mu\text{V}/^\circ\text{C}$); and (4) parasitic contact and jumper lead resistance ($5-20\,\text{m}\Omega$) on the solderless breadboard.",
    r"Our measured variations are larger than the ideal values because physical measurements in the lab are limited by practical factors: (1) the bench multimeter resolution ($0.1\,\text{mV}$); (2) slight drift in the TL431 reference voltage; (3) op-amp offset voltage drift; and (4) contact and jumper wire resistance on the breadboard (about $5-20\,\text{m}\Omega$)."
)
text = text.replace(
    r"Because either voltage or current is near zero in steady state, average power loss is miniscule.",
    r"Because either the voltage is near zero or the current is zero, the power loss during the steady ON and OFF states is very small."
)
text = text.replace(
    r"The excess voltage $(V_{IN} - V_{OUT})$ is dropped across the transistor channel, and the power $(V_{IN} - V_{OUT}) I_{LOAD}$ is irrevocably dissipated as heat. Even with an ideal op-amp possessing infinite gain and zero power consumption, it cannot circumvent this series energy conservation constraint.",
    r"The voltage difference $(V_{IN} - V_{OUT})$ drops across the series MOSFET, and the power $(V_{IN} - V_{OUT}) I_{LOAD}$ is converted directly into heat. Even with a perfect op-amp that draws zero power and has infinite gain, this series power loss cannot be avoided."
)

with open('main.tex', 'w') as f:
    f.write(text)

print("Applied simplifications and removed abstract successfully!")
