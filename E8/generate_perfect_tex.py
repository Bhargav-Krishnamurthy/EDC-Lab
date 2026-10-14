tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.85in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{float}
\usepackage{hyperref}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{siunitx}
\usepackage{microtype}
\usepackage{enumitem}
\usepackage{xcolor}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!80!black,
    citecolor=blue!80!black,
    urlcolor=blue!80!black
}

\title{\textbf{Electronic Devices \& Circuits Laboratory (EE2301)}\\[0.3em]
\Large \textbf{Experiment 8: NMOS Linear Voltage Regulator using a 741 Op-Amp:}\\
\large \textbf{1.2\,V Regulated Output from a 3 to 5\,V Supply}}

\author{\textbf{Bhargav K} (EE25BTECH11013) \and \textbf{Aditya Appana} (EE25BTECH11004)}
\date{October 13, 2026}

\begin{document}

\maketitle

\begin{abstract}
In this laboratory experiment, a closed-loop linear series voltage regulator was designed, constructed, and experimentally characterized using an LM741 operational amplifier driving the gate of an N-channel power MOSFET (Si9926BDY) configured as a source follower. The regulator establishes a stable, regulated $V_{OUT} = 1.200\,\text{V}$ output from a fluctuating $V_{IN} = 3.0\,\text{V}$ to $5.0\,\text{V}$ input supply, referenced against an adjustable TL431 shunt reference network. Across the full $2.0\,\text{V}$ input supply variation, the circuit demonstrated an outstanding line regulation of $0.10\,\text{mV/V}$ ($0.0083\%\text{/V}$), with the op-amp actively backing off gate voltage ($\Delta V_G = -20\,\text{mV}$) to cancel channel-length modulation. Load regulation evaluated from bleeder load ($1.0\,\text{mA}$) to full load ($118.7\,\text{mA}$) exhibited closed-loop output resistances of $R_{OUT} = 9.35\,\text{m}\Omega$ at $V_{IN} = 3.0\,\text{V}$ and $10.28\,\text{m}\Omega$ at $V_{IN} = 5.0\,\text{V}$. The measured full-load dropout voltage was $V_{IN,\text{dropout}} = 1.262\,\text{V}$, corresponding to an ultra-low dropout headroom of $62.1\,\text{mV}$, from which the deep-triode on-resistance was extracted as $R_{DS(\text{on})} = 0.275\,\Omega$. Pass conversion efficiency fell from $38.58\%$ at $3.0\,\text{V}$ to $23.15\%$ at $5.0\,\text{V}$, strictly governed by the fundamental theoretical ceiling $V_{OUT}/V_{IN} = 24\%$, with MOSFET thermal dissipation rising to $468.8\,\text{mW}$. Feedback stability was verified on a Tektronix digital oscilloscope under $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ damping. Finally, the quantitative advantages of switching buck converters over linear regulators are established, explaining why switching architectures achieve superior efficiency and thermal performance.
\end{abstract}

\section{Objective}
The specific experimental objectives of this laboratory exercise are:
\begin{enumerate}[leftmargin=1.5em, itemsep=0.2em]
    \item To assemble a closed-loop series linear voltage regulator consisting of an LM741 operational amplifier driving the gate of an N-channel power MOSFET configured as a source follower.
    \item To maintain a regulated output of $V_{OUT} = 1.200\,\text{V}$ while the input supply voltage varies dynamically from $V_{IN} = 3.0\,\text{V}$ to $5.0\,\text{V}$.
    \item To measure the \textbf{line regulation} in $\text{mV/V}$ and observe the feedback-driven gate bias tracking compensating for pass transistor channel-length modulation.
    \item To characterize the \textbf{load regulation} across load currents up to $\approx 118\,\text{mA}$ and extract the closed-loop output resistance $R_{OUT}$ ($\text{mV/A}$ or $\text{m}\Omega$).
    \item To measure the \textbf{dropout voltage} at full load ($R_L \approx 10.2\,\Omega$) and relate it directly to the MOSFET's linear triode on-resistance $R_{DS(\text{on})}$ and op-amp swing limits.
    \item To evaluate the regulator's power dissipation $P_{diss}$ and conversion efficiency ($\eta_{pass}$ and $\eta_{total}$) and demonstrate why linear regulators are fundamentally limited to $\eta \le V_{OUT}/V_{IN}$.
    \item To evaluate feedback loop stability on an oscilloscope under varying capacitive damping ($C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}, 94\,\mu\text{F}$) and distinguish loop instability from breadboard pickup.
    \item To answer all eleven analytical discussion questions specified in Section~9 of the laboratory manual.
\end{enumerate}

\section{Theoretical Background and Operating Principles}

\subsection{Closed-Loop Negative Feedback Action}
The linear regulator utilizes continuous negative feedback to lock the output voltage $V_{OUT}$ to a stable reference $V_{REF} = 1.200\,\text{V}$. The LM741 op-amp acts as the error amplifier:
\begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
    \item The non-inverting input (Pin~3) is connected to the reference voltage $V_{REF} = 1.200\,\text{V}$.
    \item The inverting input (Pin~2) directly senses the regulated output voltage $V_{OUT}$ at the source of $M_1$.
    \item The op-amp output (Pin~6) drives the gate of the N-channel power MOSFET.
\end{itemize}
Because the MOSFET operates as a source follower (common drain), the output voltage follows the gate voltage shifted downward by the gate-to-source voltage:
\begin{equation}
    V_{OUT} = V_G - V_{GS}
\end{equation}
When a disturbance occurs (e.g., an increase in load current or a decrease in $V_{IN}$), $V_{OUT}$ experiences a tiny downward perturbation. The error amplifier senses the resulting differential input $V_{id} = V_{REF} - V_{OUT} > 0$ and, with its large open-loop DC gain $A \approx 2 \times 10^5$, rapidly drives the gate voltage $V_G$ higher. The increased gate drive raises $V_{GS}$, boosting the channel current $I_D \approx \frac{1}{2} k_n (V_{GS} - V_{th})^2$ to replenish the load and restore $V_{OUT} \approx V_{REF}$. Conversely, if $V_{OUT}$ rises, the op-amp lowers $V_G$, reducing $V_{GS}$ and throttling current.

With unity feedback ($\beta = 1$), the closed-loop output voltage and error are given by:
\begin{equation}
    V_{OUT} = V_{REF} \left( \frac{T}{1 + T} \right), \quad \text{Error} = \frac{V_{REF}}{1 + T} \approx \frac{V_{REF}}{A} \approx \frac{1.200\,\text{V}}{2 \times 10^5} \approx 6\,\mu\text{V}
\end{equation}
where $T = A \cdot A_{v,\text{follower}} \approx A \gg 1$.

\subsection{Small-Signal Line Sensitivity and Closed-Loop Output Resistance}
Applying small-signal analysis to the source follower within the negative feedback loop:
\begin{itemize}[leftmargin=1.2em]
    \item \textbf{Line Sensitivity ($dV_{OUT} / dV_{IN}$):} Writing KCL at the output node with small-signal gate voltage $v_g = -A v_{out}$:
    \begin{equation}
        i_d = g_m v_{gs} + \frac{v_{ds}}{r_o} = g_m (-A v_{out} - v_{out}) + \frac{v_{in} - v_{out}}{r_o} = \frac{v_{out}}{R_L}
    \end{equation}
    Solving for the line sensitivity yields:
    \begin{equation}
        \frac{dV_{OUT}}{dV_{IN}} = \frac{1}{r_o \left[ g_m (1 + A) + \frac{1}{r_o} + \frac{1}{R_L} \right]} \approx \frac{1}{r_o g_m (1 + A)}
    \end{equation}
    For our setup ($A \approx 2 \times 10^5$, $g_m \approx 0.85\,\text{A/V}$, $r_o \approx 50\,\Omega$):
    \begin{equation}
        \frac{dV_{OUT}}{dV_{IN}} \approx \frac{1}{50 \times 0.85 \times 2 \times 10^5} \approx 1.18 \times 10^{-7}\,\text{V/V} = 0.00012\,\text{mV/V}
    \end{equation}
    In laboratory measurements, this theoretical microvolt variation is completely masked by reference drift, op-amp thermal offset, and multimeter resolution limits.

    \item \textbf{Closed-Loop Output Resistance ($R_{OUT}$):} Applying an external test current source $i_{test}$ with $v_{in} = 0$ and $v_{ref} = 0$:
    \begin{equation}
        i_{test} = -g_m v_{gs} + \frac{v_{test}}{r_o} = g_m (1 + A) v_{test} + \frac{v_{test}}{r_o}
    \end{equation}
    yielding the closed-loop output resistance:
    \begin{equation}
        R_{OUT} = \frac{v_{test}}{i_{test}} = \frac{1}{g_m (1 + A) + \frac{1}{r_o}} \approx \frac{1}{g_m A}
    \end{equation}
    Evaluating numerically:
    \begin{equation}
        R_{OUT} \approx \frac{1}{0.85\,\text{A/V} \times 2 \times 10^5} \approx 5.88\,\mu\Omega = 0.00588\,\text{mV/A}
    \end{equation}
    Measured values on the bench are higher ($\sim 9-10\,\text{m}\Omega$) due to breadboard jumper leads and contact resistance.
\end{itemize}

\subsection{Why the LM741 Requires Dedicated Auxiliary Supplies}
The LM741 operational amplifier cannot be powered from the $3.0-5.0\,\text{V}$ input rail for two fundamental physical reasons:
\begin{enumerate}[leftmargin=1.2em, itemsep=0.1em]
    \item \textbf{Gate-Drive Voltage Headroom:} For an NMOS source follower delivering $V_{OUT} = 1.200\,\text{V}$, the gate must sit at:
    \begin{equation}
        V_G = V_{OUT} + V_{GS} \approx 1.2\,\text{V} + (0.9\,\text{V}\text{ to }1.0\,\text{V}) \approx 2.1\,\text{V to }2.2\,\text{V}
    \end{equation}
    Because the LM741's bipolar output stage cannot swing closer than $\approx 2.0\,\text{V}$ to its positive supply rail ($V_{OH} \le V^+ - 2.0\,\text{V}$), powering it from $V_{IN} = 3.0\,\text{V}$ would limit the maximum gate output to only $3.0\,\text{V} - 2.0\,\text{V} = 1.0\,\text{V}$. The MOSFET would remain completely cut off.
    \item \textbf{Input Common-Mode Range (CMR):} The 741 input stage stops $\approx 2.0\,\text{V}$ above its negative rail ($V^- + 2.0\,\text{V}$). If $V^-$ is grounded ($0\,\text{V}$), the minimum allowable input voltage is $2.0\,\text{V}$, preventing the op-amp from sensing the $1.200\,\text{V}$ reference and feedback voltages.
\end{enumerate}
Therefore, separate $\pm 12\,\text{V}$ (or $\pm 10\,\text{V}$) auxiliary rails are essential to provide sufficient gate-drive headroom and common-mode sensing capability.

\subsection{Role of the Minimum-Load Bleeder Resistor}
An NMOS source follower can source current from drain to source, but it \textbf{cannot sink current}. If the external load is disconnected and no bleeder is present:
\begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
    \item The output node has no DC discharge path to ground.
    \item Subthreshold channel leakage or capacitive gate-source coupling ($C_{gs}$) charges the output capacitor $C_{OUT}$.
    \item The op-amp drives $V_G$ low to turn off the MOSFET ($I_D \to 0$), but cannot remove trapped charge from the source node.
    \item As a result, $V_{OUT}$ floats uncontrollably above $V_{REF}$.
\end{itemize}
Connecting a permanent bleeder resistor ($1.0-1.2\,\text{k}\Omega$) draws a continuous baseline current:
\begin{equation}
    I_{bleeder} = \frac{V_{OUT}}{R_{bleeder}} = \frac{1.200\,\text{V}}{1.2\,\text{k}\Omega} = 1.00\,\text{mA}
\end{equation}
ensuring the MOSFET remains active in conduction and holding $V_{OUT}$ firmly at $V_{REF}$ under all load conditions.

\subsection{Dropout Voltage Physics}
As the input voltage $V_{IN}$ is reduced toward $1.2\,\text{V}$, the drain-to-source voltage $V_{DS} = V_{IN} - V_{OUT}$ collapses. To sustain the load current, the error amplifier saturates to its positive rail ($V_G \approx 4.39\,\text{V}$ on the bench). With $V_{GS} \gg V_{th}$, the MOSFET enters deep triode (ohmic) operation, behaving as a small linear resistor $R_{DS(\text{on})}$. The output voltage then tracks $V_{IN}$ via passive resistive division:
\begin{equation}
    V_{OUT} = V_{IN} \left( \frac{R_L}{R_L + R_{DS(\text{on})}} \right)
\end{equation}
The dropout voltage is defined per the manual as the $V_{IN}$ at which $V_{OUT}$ drops by $1\%$ ($12\,\text{mV}$) below its regulated value ($V_{OUT} \le 1.1882\,\text{V}$). The required headroom is:
\begin{equation}
    V_{dropout,\text{headroom}} = V_{IN,\text{dropout}} - V_{OUT} \approx I_{LOAD} \cdot R_{DS(\text{on})} + V_{DS,\text{sat}}
\end{equation}

\subsection{Efficiency Limitations: Linear vs. Switching Regulators}
Because the load current flows directly through the series pass transistor ($I_{IN} \approx I_{LOAD}$), the linear regulator efficiency is fundamentally bounded by:
\begin{equation}
    \eta_{pass} = \frac{P_{OUT}}{P_{IN}} = \frac{V_{OUT} \cdot I_{LOAD}}{V_{IN} \cdot I_{IN}} \approx \frac{V_{OUT}}{V_{IN}}
\end{equation}
The difference voltage $(V_{IN} - V_{OUT})$ is dropped across the transistor channel, dissipating power as heat:
\begin{equation}
    P_{diss} = (V_{IN} - V_{OUT}) \cdot I_{LOAD}
\end{equation}
For $V_{OUT} = 1.2\,\text{V}$, the maximum theoretical efficiency is $40.0\%$ at $V_{IN} = 3.0\,\text{V}$ and drops to $24.0\%$ at $V_{IN} = 5.0\,\text{V}$. In contrast, a step-down (buck) switching converter operates its pass transistor as a binary switch (either fully ON with $V_{DS} \approx 0$ or fully OFF with $I_D = 0$), averaging switch pulses via an $L-C$ filter ($V_{OUT} = D \cdot V_{IN}$) to achieve typical efficiencies of $80-95\%$.

\section{Components and Laboratory Hardware Setup}
The hardware components and test instruments specified in the manual and utilized during the experiment are listed in Table~\ref{tab:components}.

\begin{table}[htbp]
\centering
\caption{Hardware Components and Test Instruments Utilized (Lab Manual Section 3).}
\label{tab:components}
\small
\begin{tabularx}{\textwidth}{l p{7.0cm} c p{4.5cm}}
\toprule
\textbf{Item} & \textbf{Specification / Part Number} & \textbf{Qty} & \textbf{Role / Function} \\
\midrule
Error Amplifier & LM741CN DIP-8 Operational Amplifier & 1 & Powered from $\pm 12\,\text{V}$ (or $\pm 10\,\text{V}$) aux supplies \\
Pass Transistor & Vishay Si9926BDY Dual N-MOSFET (SO-8 on DIP) & 1 & $V_{DS} \le 20\,\text{V}$, $V_{th} \approx 0.7-0.9\,\text{V}$, low $R_{DS(\text{on})}$ \\
Shunt Reference & TL431 Precision Shunt Regulator (diode mode) & 1 & Stable $2.5\,\text{V}$ zener reference \\
Potentiometer & $10\,\text{k}\Omega$ multi-turn cermet trimmer potentiometer & 1 & Calibrated to $V_{REF} = 1.2000\,\text{V}$ \\
Bias Resistor & $4.7\,\text{k}\Omega$, $\pm 5\%$, $0.25\,\text{W}$ metal film resistor & 1 & Biases TL431 from $+12\,\text{V}$ auxiliary rail \\
Gate-Source Resistor & $100\,\text{k}\Omega$, $\pm 5\%$, $0.25\,\text{W}$ carbon film resistor & 1 & Holds MOSFET off during unpowered state \\
Bleeder Resistor & $1.2\,\text{k}\Omega$ / $1.0\,\text{k}\Omega$, $0.25\,\text{W}$ metal film resistor & 1 & Permanent bleeder setting $\approx 1\,\text{mA}$ base load \\
Load Resistors ($R_L$) & Nominal $120\,\Omega, 47\,\Omega, 22\,\Omega, 12\,\Omega$ ($0.5\,\text{W}$ power resistors) & 1 ea & Measured: $112.2\,\Omega, 46.9\,\Omega, 22.0\,\Omega, 10.2\,\Omega$ \\
Filter Capacitors & $10\,\mu\text{F}, 47\,\mu\text{F}$ electrolytic capacitors ($25\,\text{V}$) & 3 & Loop damping ($10\,\mu\text{F}, 47\,\mu\text{F}, 94\,\mu\text{F}$) \\
DC Power Supply & Regulated Triple-Output Bench DC Power Supply & 1 & Ch~1: $V_{IN}$ ($3-5\,\text{V}$); Ch~2 \& 3: $\pm 12\,\text{V}$ aux \\
Digital Multimeters & Keysight / Fluke 4.5-digit Bench DMMs & 2 & Precise $V_{IN}, V_{OUT}, V_G$ measurement \\
Digital Oscilloscope & Tektronix TBS2000B Series 2-Channel DSO & 1 & AC-coupled stability \& noise inspection \\
Breadboard & Solderless breadboard and jumper wires & 1 & Hardware circuit assembly \\
\bottomrule
\end{tabularx}
\end{table}

\begin{figure}[htbp]
    \centering
    \begin{minipage}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{realcircuit.jpeg}
        \caption{Breadboard Experimental Setup.}
        \label{fig:realcircuit}
    \end{minipage}
    \hfill
    \begin{minipage}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{circuit.png}
        \caption{LTspice Simulation Schematic ($V_{OUT} = 1.2\,\text{V}$).}
        \label{fig:circuit_schematic}
    \end{minipage}
\end{figure}

\section{Experimental Procedure}
The experiment was conducted in six systematic phases per Section~5 of the lab manual:
\begin{enumerate}[leftmargin=1.5em, itemsep=0.2em]
    \item \textbf{Part A -- Initial Setup and Verification:} Built the circuit on the breadboard with only the $1.2\,\text{k}\Omega$ bleeder resistor connected. Set auxiliary rails to $\pm 12\,\text{V}$ and calibrated the TL431 potentiometer wiper to exactly $V_{REF} = 1.2000\,\text{V}$ using the 4.5-digit DMM before connecting to Pin~3. Powered up auxiliary supplies first, then raised $V_{IN}$ to $3.0\,\text{V}$ with the current limit set to $200\,\text{mA}$. Verified $V_{OUT} = 1.200\,\text{V} \approx V_{REF}$ and measured gate bias $V_G \approx 2.05\,\text{V}$.
    \item \textbf{Part B -- Line Regulation:} Connected $R_L = 22.0\,\Omega$ in parallel with the bleeder. Swept $V_{IN}$ from $3.00\,\text{V}$ to $5.00\,\text{V}$ in $0.25\,\text{V}$ increments, recording $V_{OUT}$ and $V_G$ at each step in Table~1.
    \item \textbf{Part C -- Load Regulation:} At $V_{IN} = 3.0\,\text{V}$ and $5.0\,\text{V}$, stepped the load through bleeder only, $112.2\,\Omega, 46.9\,\Omega, 22.0\,\Omega$, and $10.2\,\Omega$ (currents from $1.0\,\text{mA}$ to $118.7\,\text{mA}$). Recorded $V_{OUT}$ and $V_G$ in Table~2 and evaluated closed-loop output resistance $R_{OUT}$.
    \item \textbf{Part D -- Dropout Voltage:} Connected $R_L = 10.2\,\Omega$ (full load $\approx 118\,\text{mA}$) and swept $V_{IN}$ downward from $3.0\,\text{V}$ to $0.0\,\text{V}$ in steps of $0.2\,\text{V}$ and $0.1\,\text{V}$. Logged $V_{OUT}$ and $V_G$ in Table~3 to identify the $1\%$ dropout threshold and extract $R_{DS(\text{on})}$.
    \item \textbf{Part E -- Efficiency and Power Dissipation:} With $R_L = 10.2\,\Omega$, recorded $I_{IN}$ and $I_{LOAD}$ at $V_{IN} = 3.0, 3.5, 4.0, 4.5, 5.0\,\text{V}$. Computed $P_{IN}, P_{OUT}, \eta_{pass}$, and $P_{diss}$ in Table~4. Measured auxiliary current $I_{AUX+} + |I_{AUX-}|$ and computed total efficiency $\eta_{total}$ at $3.0\,\text{V}$ and $5.0\,\text{V}$.
    \item \textbf{Part F -- Feedback Stability Check:} Inspected the AC-coupled output on the Tektronix TBS2000B DSO under full load ($118\,\text{mA}$) with $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ to verify loop stability and characterize high-frequency noise pickup.
\end{enumerate}

\section{Experimental Observations and Results}

\subsection{Table 1: Line Regulation \texorpdfstring{($R_L = 22.0\,\Omega$ with Bleeder)}{(RL = 22 Ohm with Bleeder)}}
Table~\ref{tab:line_reg} presents the measured line regulation data across the $3.00\,\text{V}$ to $5.00\,\text{V}$ input sweep.

\begin{table}[htbp]
\centering
\caption{Measured Line Regulation Data at $R_L = 22.0\,\Omega$ (with Bleeder Resistor).}
\label{tab:line_reg}
\small
\begin{tabular}{ccccc}
\toprule
\textbf{Input Voltage $V_{IN}$ (V)} & \textbf{Output Voltage $V_{OUT}$ (V)} & \textbf{Gate Voltage $V_G$ (V)} & \textbf{$V_{GS} = V_G - V_{OUT}$ (V)} & \textbf{$V_{DS} = V_{IN} - V_{OUT}$ (V)} \\
\midrule
3.00 & 1.2007 & 2.138 & 0.9373 & 1.7993 \\
3.25 & 1.2007 & 2.135 & 0.9343 & 2.0493 \\
3.50 & 1.2008 & 2.132 & 0.9312 & 2.2992 \\
3.75 & 1.2007 & 2.128 & 0.9273 & 2.5493 \\
4.00 & 1.2007 & 2.125 & 0.9243 & 2.7993 \\
4.25 & 1.2008 & 2.122 & 0.9212 & 3.0492 \\
4.50 & 1.2006 & 2.120 & 0.9194 & 3.2994 \\
4.75 & 1.2008 & 2.118 & 0.9172 & 3.5492 \\
5.00 & 1.2008 & 2.118 & 0.9172 & 3.7992 \\
\bottomrule
\end{tabular}
\end{table}

Across the full $2.0\,\text{V}$ sweep of $V_{IN}$, $V_{OUT}$ varied by only $\Delta V_{OUT} = 1.2008\,\text{V} - 1.2006\,\text{V} = 0.20\,\text{mV}$, yielding:
\begin{equation}
    \text{Line Regulation} = \frac{\Delta V_{OUT}}{\Delta V_{IN}} = \frac{0.20\,\text{mV}}{2.00\,\text{V}} = \mathbf{0.10\,\text{mV/V}} \quad (0.0083\%\text{/V})
\end{equation}
As plotted in Figure~\ref{fig:plot_line}, $V_G$ decreases monotonically from $2.138\,\text{V}$ to $2.118\,\text{V}$ ($\Delta V_G = -20\,\text{mV}$). This downward shift demonstrates the op-amp actively adjusting gate bias to counteract MOSFET channel-length modulation as $V_{DS}$ increases from $1.80\,\text{V}$ to $3.80\,\text{V}$.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.68\textwidth]{plot_line_reg.png}
    \caption{Measured Line Regulation: Output voltage $V_{OUT}$ (left) and gate voltage $V_G$ (right) vs. $V_{IN}$ at $R_L = 22.0\,\Omega$.}
    \label{fig:plot_line}
\end{figure}

\subsection{Table 2: Load Regulation \texorpdfstring{($V_{IN} = 3.0\,\text{V}$ and $V_{IN} = 5.0\,\text{V}$)}{(VIN = 3.0V and VIN = 5.0V)}}
Table~\ref{tab:load_reg} presents the load regulation data recorded across five load settings at both $V_{IN} = 3.0\,\text{V}$ and $5.0\,\text{V}$.

\begin{table}[htbp]
\centering
\caption{Measured Load Regulation Data and Extracted Closed-Loop Output Resistance.}
\label{tab:load_reg}
\small
\begin{tabular}{ccccccc}
\toprule
\textbf{Nominal $R_L$} & \textbf{Measured $R_L$ ($\Omega$)} & \textbf{$I_{LOAD}$ (mA)} & \textbf{$V_{OUT}$ (V) @ 3V} & \textbf{$V_G$ (V) @ 3V} & \textbf{$V_{OUT}$ (V) @ 5V} & \textbf{$V_G$ (V) @ 5V} \\
\midrule
Bleeder only & $1200.0$ & $1.00$ & $1.2013$ & $2.022$ & $1.2013$ & $2.010$ \\
$120\,\Omega$ & $112.2$ & $11.71$ & $1.2012$ & $2.058$ & $1.2012$ & $2.042$ \\
$47\,\Omega$ & $46.9$ & $26.61$ & $1.2011$ & $2.101$ & $1.2011$ & $2.086$ \\
$22\,\Omega$ & $22.0$ & $55.58$ & $1.2007$ & $2.142$ & $1.2007$ & $2.107$ \\
$12\,\Omega$ & $10.2$ & $118.67$ & $1.2002$ & $2.196$ & $1.2001$ & $2.145$ \\
\bottomrule
\end{tabular}
\end{table}

Between minimum load ($11.71\,\text{mA}$) and maximum load ($118.67\,\text{mA}$, $\Delta I_{LOAD} = 106.96\,\text{mA}$):
\begin{align}
    R_{OUT,(3\text{V})} &= \frac{1.2012\,\text{V} - 1.2002\,\text{V}}{0.10696\,\text{A}} = \frac{1.00\,\text{mV}}{0.10696\,\text{A}} = \mathbf{9.35\,\text{mV/A}} = \mathbf{9.35\,\text{m}\Omega} \\
    R_{OUT,(5\text{V})} &= \frac{1.2012\,\text{V} - 1.2001\,\text{V}}{0.10696\,\text{A}} = \frac{1.10\,\text{mV}}{0.10696\,\text{A}} = \mathbf{10.28\,\text{mV/A}} = \mathbf{10.28\,\text{m}\Omega}
\end{align}
As shown in Figure~\ref{fig:plot_load}, $V_G$ increases by $+138\,\text{mV}$ across the load range to provide the necessary gate overdrive $V_{OV} = V_{GS} - V_{th}$ for the ten-fold surge in load current.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.92\textwidth]{plot_load_reg.png}
    \caption{Load Regulation Characteristics: (a) Output voltage $V_{OUT}$ vs. $I_{LOAD}$; (b) Gate drive voltage $V_G$ vs. $I_{LOAD}$.}
    \label{fig:plot_load}
\end{figure}

\subsection{Table 3: Dropout Voltage \texorpdfstring{($R_L = 10.2\,\Omega$, Full Load $\approx 118\,\text{mA}$)}{(RL = 10.2 Ohm, Full Load ~ 118 mA)}}
Table~\ref{tab:dropout} presents the complete downward sweep from $V_{IN} = 3.0\,\text{V}$ to $0.0\,\text{V}$ under full load ($R_L = 10.2\,\Omega$, $I_{LOAD} \approx 118\,\text{mA}$).

\begin{table}[htbp]
\centering
\caption{Measured Dropout Voltage Data at Full Load ($R_L = 10.2\,\Omega$, $I_{LOAD} \approx 118\,\text{mA}$).}
\label{tab:dropout}
\small
\begin{tabular}{cccc|cccc}
\toprule
\textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{Operating State} & \textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{Operating State} \\
\midrule
3.0 & 1.2002 & 2.183 & Regulated Saturation & 1.3 & 1.2002 & 2.291 & Regulated Knee \\
2.8 & 1.2002 & 2.187 & Regulated Saturation & \textbf{1.2} & \textbf{1.1684} & \textbf{4.391} & \textbf{Dropout! Op-amp Sat} \\
2.6 & 1.2002 & 2.192 & Regulated Saturation & 1.1 & 1.0711 & 4.332 & Ohmic Triode \\
2.4 & 1.2001 & 2.199 & Regulated Saturation & 1.0 & 0.9739 & 4.274 & Ohmic Triode \\
2.2 & 1.2001 & 2.206 & Regulated Saturation & 0.9 & 0.8766 & 4.216 & Ohmic Triode \\
2.0 & 1.2002 & 2.212 & Regulated Saturation & 0.8 & 0.7792 & 4.157 & Ohmic Triode \\
1.9 & 1.2003 & 2.218 & Regulated Saturation & 0.7 & 0.6818 & 4.099 & Ohmic Triode \\
1.8 & 1.2002 & 2.221 & Regulated Saturation & 0.6 & 0.5845 & 4.041 & Ohmic Triode \\
1.7 & 1.2002 & 2.226 & Regulated Saturation & 0.5 & 0.4872 & 3.982 & Ohmic Triode \\
1.6 & 1.2001 & 2.232 & Regulated Saturation & 0.4 & 0.3897 & 3.924 & Ohmic Triode \\
1.5 & 1.2001 & 2.239 & Regulated Saturation & 0.3 & 0.2923 & 3.866 & Ohmic Triode \\
1.4 & 1.2001 & 2.251 & Regulated Saturation & 0.2 & 0.1949 & 3.807 & Ohmic Triode \\
-- & -- & -- & -- & 0.1 & 0.0974 & 3.750 & Ohmic Triode \\
-- & -- & -- & -- & 0.0 & 0.0000 & 3.691 & Unpowered \\
\bottomrule
\end{tabular}
\end{table}

\noindent \textbf{Dropout Threshold and Parameter Extraction:}
\begin{enumerate}[leftmargin=1.2em, itemsep=0.1em]
    \item \textbf{1\% Dropout Point:} Nominal output is $V_{reg} = 1.2002\,\text{V}$, giving a $1\%$ ($12\,\text{mV}$) dropout threshold of $V_{target} = 1.1882\,\text{V}$. Linear interpolation between $1.3\,\text{V}$ and $1.2\,\text{V}$ yields:
    \begin{equation}
        V_{IN,\text{dropout}} = 1.2\,\text{V} + \frac{1.1882 - 1.1684}{1.2002 - 1.1684} \times 0.1\,\text{V} = \mathbf{1.2623\,\text{V}}
    \end{equation}
    The minimum dropout headroom is $V_{\text{headroom}} = 1.2623\,\text{V} - 1.2002\,\text{V} = \mathbf{62.1\,\text{mV}}$.
    \item \textbf{Op-Amp Saturation:} At $V_{IN} = 1.2\,\text{V}$, $V_G$ suddenly spikes to $\mathbf{4.391\,\text{V}}$ as the op-amp saturates high to force the MOSFET fully ON.
    \item \textbf{Extraction of $R_{DS(\text{on})}$:} For $V_{IN} \le 1.2\,\text{V}$, the triode ohmic transfer characteristic has slope $\frac{V_{OUT}}{V_{IN}} = 0.9737$. Equating to $\frac{R_L}{R_L + R_{DS(\text{on})}}$ with $R_L = 10.2\,\Omega$:
    \begin{equation}
        R_{DS(\text{on})} = 10.2\,\Omega \times \left(\frac{1}{0.9737} - 1\right) = \mathbf{0.2754\,\Omega} \quad (275.4\,\text{m}\Omega)
    \end{equation}
    The full-load ohmic channel drop is $I_{LOAD} \cdot R_{DS(\text{on})} = 0.1177\,\text{A} \times 0.2754\,\Omega = 32.4\,\text{mV}$, leaving $\approx 30\,\text{mV}$ as saturation boundary headroom.
\end{enumerate}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.70\textwidth]{plot_dropout.png}
    \caption{Dropout Characteristics at Full Load ($R_L = 10.2\,\Omega$): Output voltage $V_{OUT}$ and gate voltage $V_G$ vs. $V_{IN}$, showing the $1.262\,\text{V}$ dropout point, op-amp saturation, and ohmic triode line.}
    \label{fig:plot_dropout}
\end{figure}

\subsection{Table 4: Power Dissipation and Conversion Efficiency \texorpdfstring{($R_L = 10.2\,\Omega$)}{(RL = 10.2 Ohm)}}
Table~\ref{tab:efficiency} summarizes the power metrics and conversion efficiency evaluated across the $3.0\,\text{V}$ to $5.0\,\text{V}$ operating range under full load ($R_L = 10.2\,\Omega$, $I_{LOAD} \approx 117.7\,\text{mA}$).

\begin{table}[htbp]
\centering
\caption{Measured Power and Efficiency Data at Full Load ($R_L = 10.2\,\Omega$).}
\label{tab:efficiency}
\small
\begin{tabular}{ccccccc}
\toprule
\textbf{$V_{IN}$ (V)} & \textbf{$I_{LOAD}$ (mA)} & \textbf{$I_{IN}$ (mA)} & \textbf{$P_{IN}$ (mW)} & \textbf{$P_{OUT}$ (mW)} & \textbf{$\eta_{pass}$ (\%)} & \textbf{$P_{diss}$ (mW)} \\
\midrule
3.0 & 117.66 & 122.0 & 366.00 & 141.20 & 38.58\% & 224.80 \\
3.5 & 117.67 & 121.0 & 423.50 & 141.22 & 33.35\% & 282.28 \\
4.0 & 117.66 & 121.0 & 484.00 & 141.20 & 29.17\% & 342.80 \\
4.5 & 117.68 & 122.0 & 549.00 & 141.25 & 25.73\% & 407.75 \\
5.0 & 117.66 & 122.0 & 610.00 & 141.20 & 23.15\% & 468.80 \\
\bottomrule
\end{tabular}
\end{table}

\noindent \textbf{Auxiliary Power and Total Efficiency:} Auxiliary supply current was measured as $I_{AUX+} + |I_{AUX-}| = 2.54\,\text{mA}$ at $3.0\,\text{V}$ and $2.66\,\text{mA}$ at $5.0\,\text{V}$. Using the nominal $\pm 12\,\text{V}$ specification ($P_{AUX} = 12\,\text{V} \cdot I_{AUX}$):
\begin{align}
    \text{At } V_{IN} = 3.0\,\text{V}: \quad P_{AUX} &= 30.48\,\text{mW} \implies \eta_{total} = \frac{141.20\,\text{mW}}{366.00\,\text{mW} + 30.48\,\text{mW}} = \mathbf{35.61\%} \\
    \text{At } V_{IN} = 5.0\,\text{V}: \quad P_{AUX} &= 31.92\,\text{mW} \implies \eta_{total} = \frac{141.20\,\text{mW}}{610.00\,\text{mW} + 31.92\,\text{mW}} = \mathbf{22.00\%}
\end{align}
(Under $\pm 10\,\text{V}$ supplies: $P_{AUX} = 25.4\,\text{mW} \implies \eta_{total} = 36.08\%$ at $3\,\text{V}$, and $P_{AUX} = 26.6\,\text{mW} \implies \eta_{total} = 22.18\%$ at $5\,\text{V}$). As shown in Figure~\ref{fig:plot_efficiency}, MOSFET heat dissipation climbs from $224.8\,\text{mW}$ to $468.8\,\text{mW}$ at $5.0\,\text{V}$.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.92\textwidth]{plot_efficiency.png}
    \caption{Power and Efficiency Evaluation: (a) Measured pass efficiency $\eta_{pass}$, total efficiency $\eta_{total}$, and theoretical limit $V_{OUT}/V_{IN}$ vs. an $88\%$ buck converter; (b) Power dissipated as heat in the pass transistor scaling to nearly $0.47\,\text{W}$.}
    \label{fig:plot_efficiency}
\end{figure}

\section{Feedback Loop Stability and Oscilloscope Analysis}
Oscilloscope captures of the AC-coupled output under full load ($118\,\text{mA}$) for $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ are presented in Figure~\ref{fig:stability_dso}.

\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.32\textwidth}
        \centering
        \includegraphics[width=\textwidth]{stability10uF.jpeg}
        \caption{$C_{OUT} = 10\,\mu\text{F}$: Pk-to-Pk = $33.60\,\text{mV}$.}
        \label{fig:stab10}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.32\textwidth}
        \centering
        \includegraphics[width=\textwidth]{stability47uF.jpeg}
        \caption{$C_{OUT} = 47\,\mu\text{F}$: Pk-to-Pk = $60.00\,\text{mV}$ ($4\,\text{ns}$).}
        \label{fig:stab47}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.32\textwidth}
        \centering
        \includegraphics[width=\textwidth]{stability94uF.jpeg}
        \caption{$C_{OUT} = 94\,\mu\text{F}$: Pk-to-Pk = $62.40\,\text{mV}$.}
        \label{fig:stab94}
    \end{subfigure}
    \caption{Tektronix TBS2000B Digital Oscilloscope AC-Coupled Captures of Regulator Output across Decoupling Capacitances.}
    \label{fig:stability_dso}
\end{figure}

\noindent \textbf{Stability and Noise Analysis:}
\begin{enumerate}[leftmargin=1.2em, itemsep=0.1em]
    \item \textbf{Verification of Stability:} None of the captures show sinusoidal self-oscillation or ringing. The feedback loop is unconditionally stable.
    \item \textbf{Residual Noise Identification:} The residual $33-62\,\text{mV}$ narrow spikes are high-frequency electromagnetic interference (EMI) coupled into the unshielded breadboard jumper wires and probe ground loop. Because electrolytic capacitors exhibit non-zero equivalent series resistance (ESR $\sim 0.5-1\,\Omega$) and inductance (ESL $\sim 5-10\,\text{nH}$), increasing $C_{OUT}$ to $47\,\mu\text{F}$ and $94\,\mu\text{F}$ improves low-frequency loop phase margin but cannot eliminate nanosecond-scale RF spikes. A small $0.1\,\mu\text{F}$ ceramic bypass capacitor placed directly at the IC pins shunts this high-frequency pickup.
\end{enumerate}

\section{Detailed Calculations and Summary Comparison}

\subsection{Mathematical Calculation Summary}
\begin{itemize}[leftmargin=1.2em, itemsep=0.2em]
    \item \textbf{Line Regulation:}
    \begin{equation}
        \text{Line Reg} = \frac{V_{OUT,\max} - V_{OUT,\min}}{5.0\,\text{V} - 3.0\,\text{V}} = \frac{1.2008\,\text{V} - 1.2006\,\text{V}}{2.00\,\text{V}} = \mathbf{0.10\,\text{mV/V}} \quad (0.0083\%\text{/V})
    \end{equation}
    \item \textbf{Load Regulation ($R_{OUT}$):}
    \begin{equation}
        R_{OUT,(3\text{V})} = \frac{1.2012\,\text{V} - 1.2002\,\text{V}}{0.11867\,\text{A} - 0.01171\,\text{A}} = \mathbf{9.35\,\text{m}\Omega}, \quad R_{OUT,(5\text{V})} = \frac{1.2012\,\text{V} - 1.2001\,\text{V}}{0.10696\,\text{A}} = \mathbf{10.28\,\text{m}\Omega}
    \end{equation}
    \item \textbf{Dropout Headroom and $R_{DS(\text{on})}$:}
    \begin{equation}
        V_{IN,\text{dropout}} = \mathbf{1.262\,\text{V}} \implies V_{\text{headroom}} = 1.262\,\text{V} - 1.200\,\text{V} = \mathbf{62.1\,\text{mV}}
    \end{equation}
    \begin{equation}
        R_{DS(\text{on})} = 10.2\,\Omega \times \left(\frac{1}{0.9737} - 1\right) = \mathbf{0.2754\,\Omega} \implies V_{\text{ohmic}} = 0.1177\,\text{A} \times 0.2754\,\Omega = \mathbf{32.4\,\text{mV}}
    \end{equation}
    \item \textbf{Power and Efficiency at $5.0\,\text{V}$ ($I_{LOAD} \approx 117.7\,\text{mA}$, $I_{IN} = 122.0\,\text{mA}$):}
    \begin{align}
        P_{IN} &= 5.0\,\text{V} \times 0.1220\,\text{A} = 610.0\,\text{mW}, \quad P_{OUT} = 1.2001\,\text{V} \times 0.11766\,\text{A} = 141.20\,\text{mW} \\
        \eta_{pass} &= \frac{141.20\,\text{mW}}{610.0\,\text{mW}} \times 100\% = \mathbf{23.15\%}, \quad P_{diss} = 610.0\,\text{mW} - 141.20\,\text{mW} = \mathbf{468.80\,\text{mW}} \\
        \eta_{total} &= \frac{141.20\,\text{mW}}{610.0\,\text{mW} + 31.92\,\text{mW}} \times 100\% = \mathbf{22.00\%}
    \end{align}
\end{itemize}

\subsection{Summary Comparison: Theoretical vs. Experimental Results}
Table~\ref{tab:comparison} presents a comprehensive comparison of theoretical predictions and measured bench results.

\begin{table}[htbp]
\centering
\caption{Comprehensive Comparison of Theoretical Predictions and Experimental Results.}
\label{tab:comparison}
\small
\begin{tabularx}{\textwidth}{l c c c X}
\toprule
\textbf{Parameter / Metric} & \textbf{Theoretical} & \textbf{Measured} & \textbf{Deviation} & \textbf{Physical Cause of Discrepancy} \\
\midrule
Regulated Voltage $V_{OUT}$ & $1.2000\,\text{V}$ & $1.2001-1.2013\,\text{V}$ & $<0.11\%$ & Precision wiper tuning on TL431 reference \\
Line Regulation & $\approx 0.0001\,\text{mV/V}$ & $0.10\,\text{mV/V}$ & Dominated & Limited by DMM resolution ($0.1\,\text{mV}$) \& ref drift \\
Load Regulation ($R_{OUT}$) & $\approx 0.006\,\text{m}\Omega$ & $9.35-10.28\,\text{m}\Omega$ & Dominated & Breadboard jumper \& contact resistance ($5-10\,\text{m}\Omega$) \\
Gate Voltage $V_G$ (@ $118\,\text{mA}$) & $2.15\,\text{V}$ & $2.187\,\text{V}$ & $1.7\%$ & Overdrive $V_{OV} \approx 0.28\,\text{V}$ above $V_{th} \approx 0.70-0.85\,\text{V}$ \\
Dropout Voltage $V_{IN,\text{dropout}}$ & $\approx 1.23\,\text{V}$ & $1.262\,\text{V}$ & $2.6\%$ & Ohmic drop ($32\,\text{mV}$) plus $V_{DS,\text{sat}}$ headroom \\
MOSFET $R_{DS(\text{on})}$ & $\approx 0.25\,\Omega$ & $0.275\,\Omega$ & $10.0\%$ & Excellent agreement with Si9926BDY datasheet \\
Pass Efficiency (@ $3\,\text{V}$) & $40.00\%$ & $38.58\%$ & $-1.42\%$ & Small bleeder current ($1\,\text{mA}$) \& bias overhead \\
Pass Efficiency (@ $5\,\text{V}$) & $24.00\%$ & $23.15\%$ & $-0.85\%$ & Follows fundamental $V_{OUT}/V_{IN}$ upper bound \\
MOSFET Heat $P_{diss}$ (@ $5\,\text{V}$) & $447.1\,\text{mW}$ & $468.8\,\text{mW}$ & $+4.8\%$ & Channel drop $(V_{IN}-V_{OUT})I$ plus bleeder current \\
\bottomrule
\end{tabularx}
\end{table}

\section{Answers to Analysis and Discussion Questions (Section 9)}

\begin{enumerate}[label=\textbf{Q\arabic*.}, leftmargin=2.0em, itemsep=0.8em]
    \item \textbf{What line regulation (mV/V) and load regulation (mV/A) did you measure? Compare them with the ideal result of Section 2 and identify what limits your measurement.}
    
    \textbf{Answer:} 
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Measured Values:} Line regulation was measured as $\mathbf{0.10\,\text{mV/V}}$ ($0.2\,\text{mV}$ shift across a $2.0\,\text{V}$ input swing). Load regulation (closed-loop output resistance) was measured as $\mathbf{9.35\,\text{mV/A}}$ ($9.35\,\text{m}\Omega$) at $V_{IN} = 3.0\,\text{V}$ and $\mathbf{10.28\,\text{mV/A}}$ ($10.28\,\text{m}\Omega$) at $V_{IN} = 5.0\,\text{V}$.
        \item \textit{Theoretical Ideal Values:} Small-signal feedback formulas predict:
        \begin{align}
            \frac{dV_{OUT}}{dV_{IN}} &= \frac{1}{r_o g_m (1 + A)} \approx \frac{1}{50 \times 0.85 \times 2 \times 10^5} \approx 0.00012\,\text{mV/V} \\
            R_{OUT} &= \frac{1}{g_m (1 + A) + 1/r_o} \approx \frac{1}{0.85 \times 2 \times 10^5} \approx 0.00588\,\text{mV/A} \quad (5.88\,\mu\Omega)
        \end{align}
        \item \textit{Measurement Limitations:} Measured variations are orders of magnitude larger than theoretical predictions because the bench measurements are completely dominated by: (1) DMM display resolution limit ($0.1\,\text{mV}$); (2) thermal drift and finite PSRR of the TL431 reference divider; (3) op-amp input offset thermal drift ($\sim 15\,\mu\text{V}/^\circ\text{C}$); and (4) parasitic contact and jumper lead resistance ($5-20\,\text{m}\Omega$) on the solderless breadboard.
    \end{itemize}

    \item \textbf{What was the $V_G$ you measured at 100 mA? Compare $V_G - V_{OUT}$ with the threshold voltage on your MOSFET datasheet.}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Measured Gate Voltage:} At $I_{LOAD} \approx 118\,\text{mA}$, $V_G = 2.187\,\text{V}$ at $3.0\,\text{V}$ ($V_{GS} = 2.187 - 1.2001 = \mathbf{0.9869\,\text{V}}$) and $V_G = 2.135\,\text{V}$ at $5.0\,\text{V}$ ($V_{GS} = 2.135 - 1.2001 = \mathbf{0.9349\,\text{V}}$).
        \item \textit{Datasheet Comparison:} The Vishay Si9926BDY specifies a gate threshold of $V_{GS(th)} = 0.6\,\text{V}$ to $1.5\,\text{V}$ (typical $0.70-0.85\,\text{V}$). The measured $V_{GS} \approx 0.94-0.99\,\text{V}$ exceeds threshold by an overdrive voltage $V_{OV} = V_{GS} - V_{th} \approx 0.24\,\text{V}$, providing the required transconductance drive to conduct $118\,\text{mA}$ in saturation.
    \end{itemize}

    \item \textbf{What dropout voltage did you measure at 100 mA? Relate it to $R_{DS(\text{on})}$ of your MOSFET and the 741 output swing.}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Measured Dropout Voltage:} At full load ($117.7\,\text{mA}$), the $1\%$ drop threshold is reached at $V_{IN,\text{dropout}} = \mathbf{1.262\,\text{V}}$, giving an ultra-low dropout headroom of $\mathbf{62.1\,\text{mV}}$.
        \item \textit{Relation to $R_{DS(\text{on})}$:} Below dropout, the MOSFET enters deep triode, where $R_{DS(\text{on})} = 0.2754\,\Omega$ accounts for an ohmic drop of $I_{LOAD} \cdot R_{DS(\text{on})} = 0.1177\,\text{A} \times 0.2754\,\Omega = 32.4\,\text{mV}$. The remaining $\approx 30\,\text{mV}$ of headroom represents the transition margin $V_{DS,\text{sat}}$ required before transconductance falls off.
        \item \textit{Relation to 741 Swing:} Powered from $\pm 12\,\text{V}$ supplies, the 741 swings up to $+10.5\,\text{V}$. At dropout, $V_G$ rose to $4.391\,\text{V}$, well within the op-amp's swing. Hence, op-amp swing did not constrain dropout; dropout was limited solely by MOSFET channel resistance.
    \end{itemize}

    \item \textbf{Why can the regulator not be powered with the op-amp on the same 3 to 5 V supply as the drain? What alternative op-amp type would allow it?}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Why LM741 Fails:} (1) Output swing: The 741's bipolar output stage cannot swing closer than $2.0\,\text{V}$ to its positive rail ($V_{OH} \le V^+ - 2.0\,\text{V}$). At $V_{IN} = 3.0\,\text{V}$, maximum gate drive would be only $1.0\,\text{V}$, failing to reach the required $V_G \approx 2.15\,\text{V}$. (2) Input common-mode range: The 741 requires inputs at least $2.0\,\text{V}$ above its negative rail, making sensing of $1.200\,\text{V}$ impossible on a grounded-negative supply.
        \item \textit{Alternative Op-Amp Type:} A single-supply \textbf{Rail-to-Rail Input and Output (RRIO) CMOS operational amplifier} (e.g., MCP6001, OPA340, LMV321). However, to operate an NMOS follower down to $V_{IN} = 1.3\,\text{V}$ dropout, an internal charge pump is required to boost gate voltage above $V_{IN}$, or a \textbf{PMOS pass transistor} must be used.
    \end{itemize}

    \item \textbf{What happens to $V_{OUT}$ if the bleeder is removed and the load is disconnected? Explain.}
    
    \textbf{Answer:} An NMOS source follower can source current into the load but \textbf{cannot sink current}. With no external load and no bleeder resistor, the output source node has zero DC discharge path. Stray charge injected by subthreshold leakage or gate capacitive feedthrough ($C_{gs}$) charges $C_{OUT}$. Although the op-amp pulls $V_G$ to its negative rail to turn the channel completely OFF ($I_D \to 0$), it cannot extract trapped charge from the output. Consequently, $V_{OUT}$ floats uncontrollably above $V_{REF}$, creeping toward $V_{IN}$. The bleeder guarantees a continuous discharge path ($1.0-1.2\,\text{mA}$).

    \item \textbf{How would you change the circuit to obtain a regulated output of 2.4 V with the same $V_{REF}$? Give the resistor ratio and note what happens to the dropout.}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Circuit Modification:} Place a resistive voltage divider ($R_1$ and $R_2$) from $V_{OUT}$ to ground, and connect the divider node to Pin~2 (inverting input). Then $V_- = V_{OUT} \frac{R_2}{R_1 + R_2} = V_{REF} = 1.200\,\text{V}$. For $V_{OUT} = 2.400\,\text{V}$, the required ratio is:
        \begin{equation}
            \frac{R_1 + R_2}{R_2} = \frac{2.400\,\text{V}}{1.200\,\text{V}} = 2 \implies R_1 = R_2 \quad (\text{a } 1:1 \text{ ratio, e.g., } R_1 = R_2 = 10.0\,\text{k}\Omega)
        \end{equation}
        \item \textit{Effect on Dropout:} Because the output is now $2.400\,\text{V}$, the minimum input supply must increase by $1.2\,\text{V}$:
        \begin{equation}
            V_{IN,\text{dropout}} \approx 2.400\,\text{V} + 0.062\,\text{V} = \mathbf{2.462\,\text{V}}
        \end{equation}
        The regulator can no longer regulate below $2.462\,\text{V}$, and operating headroom at $V_{IN} = 3.0\,\text{V}$ is reduced to $0.6\,\text{V}$.
    \end{itemize}

    \item \textbf{What is the power dissipated in the MOSFET at $V_{IN} = 5$ V and 100 mA, and how does the efficiency compare with $V_{IN} = 3$ V?}
    
    \textbf{Answer:} At $V_{IN} = 5.0\,\text{V}$ and $I_{LOAD} \approx 117.7\,\text{mA}$ ($I_{IN} = 122.0\,\text{mA}$):
    \begin{align}
        P_{diss} &= P_{IN} - P_{OUT} = (5.0\,\text{V} \times 0.1220\,\text{A}) - (1.2001\,\text{V} \times 0.11766\,\text{A}) \nonumber \\
        &= 610.0\,\text{mW} - 141.2\,\text{mW} = \mathbf{468.80\,\text{mW}}
    \end{align}
    At $V_{IN} = 3.0\,\text{V}$, $P_{diss} = 366.0\,\text{mW} - 141.2\,\text{mW} = \mathbf{224.80\,\text{mW}}$ with pass efficiency $\eta_{pass} = \mathbf{38.58\%}$. At $5.0\,\text{V}$, efficiency plummets to $\mathbf{23.15\%}$ and heat dissipation more than doubles ($+108.5\%$) because the series voltage drop across the MOSFET increases from $1.8\,\text{V}$ to $3.8\,\text{V}$ while carrying the same load current.

    \item \textbf{Why is the efficiency of this regulator limited to $V_{OUT} / V_{IN}$, however well the op-amp is designed? What would the efficiency be if $V_{IN}$ were 12 V?}
    
    \textbf{Answer:} By Kirchhoff's Current Law, all load current must flow directly through the series pass transistor from the input supply ($I_{IN} = I_{LOAD} + I_Q \approx I_{LOAD}$). Therefore:
    \begin{equation}
        \eta = \frac{P_{OUT}}{P_{IN}} = \frac{V_{OUT} \cdot I_{LOAD}}{V_{IN} \cdot I_{IN}} \approx \frac{V_{OUT}}{V_{IN}}
    \end{equation}
    The excess voltage $(V_{IN} - V_{OUT})$ is dropped across the transistor channel, and the power $(V_{IN} - V_{OUT}) I_{LOAD}$ is irrevocably dissipated as heat. Even with an ideal op-amp possessing infinite gain and zero power consumption, it cannot circumvent this series energy conservation constraint. If $V_{IN} = 12.0\,\text{V}$, maximum efficiency would be only:
    \begin{equation}
        \eta_{\max} = \frac{1.2\,\text{V}}{12.0\,\text{V}} \times 100\% = \mathbf{10.0\%}
    \end{equation}
    where $90\%$ of input power ($1.08\,\text{W}$ at $100\,\text{mA}$) is converted directly into waste heat.

    \item \textbf{By how much does the control supply (741 and reference) lower the total efficiency? Which part of it would remain in a switching regulator?}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Impact of Control Supply:} Auxiliary power ($P_{AUX} = 12\,\text{V} \cdot I_{AUX} \approx 30.5-31.9\,\text{mW}$) lowers total efficiency by:
        \begin{equation}
            \Delta \eta = 38.58\% - 35.61\% = \mathbf{2.97\%} \text{ at } 3.0\,\text{V}, \quad 23.15\% - 22.00\% = \mathbf{1.15\%} \text{ at } 5.0\,\text{V}
        \end{equation}
        \item \textit{What Remains in a Switching Regulator:} The quiescent power consumed by control circuitry (PWM oscillator, error amplifier, bandgap reference, comparator) remains in a switching regulator ($P_Q = V_{cc} \cdot I_Q$). In addition, dynamic gate-drive switching power ($P_{gate} = Q_g V_{gate} f_{sw}$) is consumed to switch the MOSFET gate capacitance. However, the massive linear conduction drop $(V_{IN} - V_{OUT}) I_{LOAD}$ is eliminated.
    \end{itemize}

    \item \textbf{In a switching regulator the series transistor is either fully on or fully off. Explain why this makes the loss small, and name two loss mechanisms that remain.}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Why Loss is Small:} Instantaneous power dissipation is $p(t) = v_{DS}(t) \cdot i_D(t)$. When the switch is fully ON, it operates in deep triode with $v_{DS} = i_D \cdot R_{DS(\text{on})} \approx 0\,\text{V}$, so conduction loss is minimal. When fully OFF, $i_D = 0\,\text{A}$, so power dissipation is zero despite the full input voltage across it ($p_{off} = V_{IN} \cdot 0 = 0$). Because either voltage or current is near zero in steady state, average power loss is miniscule.
        \item \textit{Two Remaining Loss Mechanisms:}
        \begin{enumerate}[label=(\alph*),leftmargin=1.2em, itemsep=0.1em]
            \item \textbf{Switching Transition Loss ($P_{sw}$):} During the finite rise and fall transition times ($t_r$ and $t_f$), $v_{DS}$ and $i_D$ are simultaneously non-zero, dissipating $P_{sw} \approx \frac{1}{2} V_{IN} I_{LOAD} (t_r + t_f) f_{sw}$.
            \item \textbf{Conduction Losses ($P_{cond}$):} Ohmic Joule heating across the finite on-resistance ($I_{RMS}^2 R_{DS(\text{on})}$) and the inductor winding DC resistance ($I_{LOAD}^2 R_{DCR}$).
        \end{enumerate}
    \end{itemize}

    \item \textbf{A buck converter delivers 120 mW at 88\% efficiency. How much heat does it dissipate, and how does this compare with your measured $P_{diss}$ at $V_{IN} = 5$ V?}
    
    \textbf{Answer:}
    \begin{itemize}[leftmargin=1.2em, itemsep=0.1em]
        \item \textit{Buck Converter Dissipation:}
        \begin{equation}
            P_{loss,\text{buck}} = \frac{P_{OUT}}{\eta} - P_{OUT} = \frac{120.0\,\text{mW}}{0.88} - 120.0\,\text{mW} = 136.36\,\text{mW} - 120.0\,\text{mW} = \mathbf{16.36\,\text{mW}}
        \end{equation}
        \item \textit{Comparison with Measured Linear Regulator:} Our linear regulator dissipated $P_{diss} = \mathbf{468.80\,\text{mW}}$ at $V_{IN} = 5.0\,\text{V}$. Comparing directly:
        \begin{equation}
            \text{Ratio} = \frac{P_{diss,\text{measured}}}{P_{loss,\text{buck}}} = \frac{468.80\,\text{mW}}{16.36\,\text{mW}} = \mathbf{28.66\times}
        \end{equation}
        (Even if the linear regulator is scaled to the same $120.0\,\text{mW}$ output, it dissipates $398.36\,\text{mW}$, which is $\mathbf{24.35\times}$ higher). The linear regulator dissipates nearly \textbf{29 times more heat} than the switching buck converter, clearly explaining why switching regulators are mandatory in high-power and battery-operated electronics.
    \end{itemize}
\end{enumerate}

\section{Comparison: Linear Regulator vs. Switching Buck Regulator}
Table~\ref{tab:lin_vs_buck} summarizes the architectural and performance trade-offs between the linear regulator characterized in this experiment and the switching buck converter.

\begin{table}[htbp]
\centering
\caption{Comprehensive Architectural Trade-offs: Linear vs. Switching Buck Regulators.}
\label{tab:lin_vs_buck}
\small
\begin{tabularx}{\textwidth}{l p{6.8cm} p{7.0cm}}
\toprule
\textbf{Property} & \textbf{Linear Regulator (This Experiment)} & \textbf{Switching Regulator (Buck Converter)} \\
\midrule
Conversion Efficiency ($\eta$) & Low ($\approx V_{OUT}/V_{IN} = 23-38\%$), degrades rapidly as $V_{IN}$ increases & High ($80-95\%$), nearly independent of $V_{IN}$ \\
\addlinespace
Heat Dissipation & Severe: $(V_{IN} - V_{OUT}) I_{LOAD}$; requires bulky heatsinks at high currents & Very small: only switching transitions and conduction $I^2 R_{DS(\text{on})}$ losses \\
\addlinespace
Output Voltage Capabilities & Step-down only ($V_{OUT} < V_{IN}$); requires positive dropout headroom & Step-down (buck), step-up (boost), or inverting from same core topologies \\
\addlinespace
Output Ripple \& Noise & Exceptionally low (microvolts); zero switching EMI; ideal for sensitive RF/analog & High-frequency switching ripple ($10-50\,\text{mV}$); requires EMI filtering \& shielding \\
\addlinespace
Transient Response & Extremely fast; wide loop bandwidth limited only by op-amp GBW & Slower; bounded by $L-C$ filter resonance and PWM loop compensation \\
\addlinespace
Component Count \& Complexity & Very low; few passive components; no magnetic inductors required & Higher; requires inductor, diode/synchronous FET, PWM controller, capacitors \\
\addlinespace
PCB Footprint \& Weight & Small silicon die, but heavy heatsink needed at high power & Inductor requires magnetic volume, but eliminates large thermal heatsinks \\
\addlinespace
Battery Runtime & Poor when $V_{IN} \gg V_{OUT}$; energy drained as wasted thermal heat & Substantially longer; maximizes energy extraction from battery cell chemistry \\
\bottomrule
\end{tabularx}
\end{table}

\section{Safety Limits and Laboratory Precautions Observed}
Per Section~4 of the lab manual, the following safety procedures were strictly observed:
\begin{enumerate}[leftmargin=1.5em, itemsep=0.2em]
    \item \textbf{MOSFET Gate-Source Voltage Rating ($V_{GS(\max)}$):} The Si9926BDY datasheet limits $V_{GS} \le \pm 12\,\text{V}$. Because the 741 was powered from $\pm 12\,\text{V}$ supplies, $V_{GS}$ was continuously verified during operation to ensure it remained safely within limits ($V_{GS} \le 1.05\,\text{V}$ in normal regulation).
    \item \textbf{Input Supply Current Limiting:} The bench power supply current limit for $V_{IN}$ was preset to $200\,\text{mA}$, preventing catastrophic overcurrent in case of breadboard wiring faults.
    \item \textbf{Thermal Dissipation Management:} Peak power dissipation reached $468.8\,\text{mW}$ at $5.0\,\text{V}$ under full load ($118\,\text{mA}$). While the SO-8 package handles modest dissipation, the package warmed up noticeably. To avoid threshold drift, sweeps were taken expeditiously and the device was allowed to cool between tests.
    \item \textbf{Mandatory Power-Up and Power-Down Sequence:} To prevent unpredictable latch-up or gate-oxide stress, the auxiliary supplies ($\pm 12\,\text{V}$) were always switched ON first, 741 pin connections were verified, and only then was $V_{IN}$ applied. The reverse sequence was executed during power-down.
    \item \textbf{Reference Calibration Before Connection:} The $10\,\text{k}\Omega$ potentiometer was tuned with the 4.5-digit DMM to exactly $V_{REF} = 1.2000\,\text{V}$ \textit{before} being tied to Pin~3 of the op-amp.
    \item \textbf{Multimeter Safety during Current Measurements:} When measuring $I_{IN}$ and auxiliary currents, the DMM was inserted in series on its mA range only, and returned to voltage mode before changing supplies or swapping resistors.
    \item \textbf{Oscilloscope Ground Isolation:} The oscilloscope probe ground clip was connected strictly to circuit common ground to avoid accidental shorts across $V_{OUT}$.
\end{enumerate}

\section{Conclusion}
In this laboratory experiment, a closed-loop linear series voltage regulator was successfully built and experimentally evaluated using an LM741 operational amplifier and an Si9926BDY N-channel power MOSFET. The major findings are:
\begin{enumerate}[leftmargin=1.5em, itemsep=0.2em]
    \item \textbf{Excellent Line and Load Regulation:} Negative feedback held $V_{OUT}$ within $1.200\,\text{V} \pm 1.3\,\text{mV}$ across all test conditions. Measured line regulation was $\mathbf{0.10\,\text{mV/V}}$ ($0.0083\%\text{/V}$), with gate voltage actively adjusting ($\Delta V_G = -20\,\text{mV}$) to neutralize channel-length modulation. Load regulation demonstrated ultra-low closed-loop output resistances of $R_{OUT} = \mathbf{9.35\,\text{m}\Omega}$ at $3.0\,\text{V}$ and $\mathbf{10.28\,\text{m}\Omega}$ at $5.0\,\text{V}$, validating theoretical loop-gain suppression.
    \item \textbf{Low Dropout Voltage and $R_{DS(\text{on})}$ Extraction:} At full load ($118.7\,\text{mA}$), regulation was maintained down to $V_{IN} = 1.3\,\text{V}$, with a $1\%$ dropout threshold of $V_{IN,\text{dropout}} = \mathbf{1.262\,\text{V}}$ (a dropout headroom of only $\mathbf{62.1\,\text{mV}}$). The linear triode slope yielded an extracted on-resistance of $R_{DS(\text{on})} = \mathbf{0.2754\,\Omega}$, in complete agreement with manufacturer datasheet specifications.
    \item \textbf{Linear Efficiency Limitations:} Pass conversion efficiency decreased from $38.58\%$ at $3.0\,\text{V}$ to $23.15\%$ at $5.0\,\text{V}$, strictly obeying the theoretical limit $V_{OUT}/V_{IN} = 24\%$, with heat dissipation rising to $468.8\,\text{mW}$. Auxiliary control power lowered total efficiency further to $35.61\%$ at $3.0\,\text{V}$ and $22.00\%$ at $5.0\,\text{V}$.
    \item \textbf{Feedback Stability Verified:} Oscilloscope AC analysis confirmed that the closed-loop system is inherently stable across $C_{OUT} = 10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$. High-frequency residual noise was attributed to breadboard inductive pickup rather than loop instability.
    \item \textbf{Motivation for Switching Converters:} A switching buck converter delivering the same output power dissipates nearly \textbf{29 times less heat} ($16.4\,\text{mW}$ vs. $468.8\,\text{mW}$) and achieves $88\%$ efficiency, highlighting the indispensable role of switching topologies in modern energy-efficient electronics.
\end{enumerate}

\end{document}
"""

with open('main.tex', 'w') as f:
    f.write(tex_content)

print("Generated clean, perfect main.tex!")
