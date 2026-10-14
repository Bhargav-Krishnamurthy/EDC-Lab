with open('main.tex', 'r') as f:
    text = f.read()

# 1. Table 3: set \footnotesize and \tabcolsep{3pt}
old_t3 = r"""\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{cccc|cccc}"""

new_t3 = r"""\setlength{\tabcolsep}{3.2pt}
\footnotesize
\begin{tabular}{cccc|cccc}"""
text = text.replace(old_t3, new_t3)

# 2. Conduction loss line
old_cond = r"""\textbf{Conduction Losses ($P_{cond}$):} Ohmic Joule heating across the finite on-resistance ($I_{RMS}^2 R_{DS(\text{on})}$)"""
new_cond = r"""\textbf{Conduction Losses ($P_{cond}$):} Ohmic dissipation across on-resistance ($I_{RMS}^2 R_{DS(\text{on})}$)"""
text = text.replace(old_cond, new_cond)

# 3. Comparison line
old_comp_line = r"""\textit{Comparison with Measured Linear Regulator:} Our linear regulator dissipated $P_{diss} = \mathbf{468.80\,\text{mW}}$ at $V_{IN} = 5.0\,\text{V}$."""
new_comp_line = r"""\textit{Comparison with Linear Regulator:} Our measured linear regulator dissipated $P_{diss} = \mathbf{468.80\,\text{mW}}$ at $V_{IN} = 5.0\,\text{V}$."""
text = text.replace(old_comp_line, new_comp_line)

with open('main.tex', 'w') as f:
    f.write(text)

print("Applied final hbox fixes!")
