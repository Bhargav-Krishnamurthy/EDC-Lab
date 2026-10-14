with open('main.tex', 'r') as f:
    text = f.read()

# 1. Fix Table tab:components
old_comp = r"""\begin{tabularx}{\textwidth}{l p{7.0cm} c p{4.5cm}}"""
new_comp = r"""\begin{tabularx}{\textwidth}{l p{5.5cm} c X}"""
text = text.replace(old_comp, new_comp)

# 2. Fix Table tab:line_reg headers
old_line_tab = r"""\begin{tabular}{ccccc}
\toprule
\textbf{Input Voltage $V_{IN}$ (V)} & \textbf{Output Voltage $V_{OUT}$ (V)} & \textbf{Gate Voltage $V_G$ (V)} & \textbf{$V_{GS} = V_G - V_{OUT}$ (V)} & \textbf{$V_{DS} = V_{IN} - V_{OUT}$ (V)} \\"""

new_line_tab = r"""\begin{tabular}{ccccc}
\toprule
\textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{$V_{GS} = V_G - V_{OUT}$ (V)} & \textbf{$V_{DS} = V_{IN} - V_{OUT}$ (V)} \\"""
text = text.replace(old_line_tab, new_line_tab)

# 3. Fix Table tab:load_reg headers
old_load_tab = r"""\begin{tabular}{ccccccc}
\toprule
\textbf{Nominal $R_L$} & \textbf{Measured $R_L$ ($\Omega$)} & \textbf{$I_{LOAD}$ (mA)} & \textbf{$V_{OUT}$ (V) @ 3V} & \textbf{$V_G$ (V) @ 3V} & \textbf{$V_{OUT}$ (V) @ 5V} & \textbf{$V_G$ (V) @ 5V} \\"""

new_load_tab = r"""\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{ccccccc}
\toprule
\textbf{$R_L$ (nom)} & \textbf{$R_L$ ($\Omega$)} & \textbf{$I_{LOAD}$ (mA)} & \textbf{$V_{OUT}$ (3V)} & \textbf{$V_G$ (3V)} & \textbf{$V_{OUT}$ (5V)} & \textbf{$V_G$ (5V)} \\"""
text = text.replace(old_load_tab, new_load_tab)

# 4. Fix Table tab:dropout headers and colsep
old_drop_tab = r"""\begin{tabular}{cccc|cccc}
\toprule
\textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{Operating State} & \textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{Operating State} \\"""

new_drop_tab = r"""\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{cccc|cccc}
\toprule
\textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{State} & \textbf{$V_{IN}$ (V)} & \textbf{$V_{OUT}$ (V)} & \textbf{$V_G$ (V)} & \textbf{State} \\"""
text = text.replace(old_drop_tab, new_drop_tab)

# 5. Fix Table tab:lin_vs_buck
old_comp_tab = r"""\begin{tabularx}{\textwidth}{l p{6.8cm} p{7.0cm}}"""
new_comp_tab = r"""\begin{tabularx}{\textwidth}{l X X}"""
text = text.replace(old_comp_tab, new_comp_tab)

# 6. Fix line 417 equation: R_{OUT,(3\text{V})} = ...; R_{OUT,(5\text{V})} = ...
old_rout_eq = r"""\begin{equation}
        R_{OUT,(3\text{V})} = \frac{1.2012\,\text{V} - 1.2002\,\text{V}}{0.11867\,\text{A} - 0.01171\,\text{A}} = \mathbf{9.35\,\text{m}\Omega}, \quad R_{OUT,(5\text{V})} = \frac{1.2012\,\text{V} - 1.2001\,\text{V}}{0.10696\,\text{A}} = \mathbf{10.28\,\text{m}\Omega}
    \end{equation}"""

new_rout_eq = r"""\begin{align}
        R_{OUT,(3\text{V})} &= \frac{1.2012\,\text{V} - 1.2002\,\text{V}}{0.11867\,\text{A} - 0.01171\,\text{A}} = \frac{1.00\,\text{mV}}{0.10696\,\text{A}} = \mathbf{9.35\,\text{m}\Omega} \\
        R_{OUT,(5\text{V})} &= \frac{1.2012\,\text{V} - 1.2001\,\text{V}}{0.10696\,\text{A}} = \frac{1.10\,\text{mV}}{0.10696\,\text{A}} = \mathbf{10.28\,\text{m}\Omega}
    \end{align}"""
text = text.replace(old_rout_eq, new_rout_eq)

with open('main.tex', 'w') as f:
    f.write(text)

print("Applied table fixes!")
