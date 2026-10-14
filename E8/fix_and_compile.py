import re

with open('main.tex', 'r') as f:
    content = f.read()

# 1. Fix unescaped %
content = content.replace('delivers 120 mW at 88% efficiency', r'delivers 120 mW at 88\% efficiency')

# 2. Fix hyperref math in titles with \texorpdfstring
content = content.replace(r'\subsection{Table 1: Line Regulation ($R_L = 22.0\,\Omega$ with Bleeder)}',
                          r'\subsection{Table 1: Line Regulation \texorpdfstring{($R_L = 22.0\,\Omega$ with Bleeder)}{(RL = 22 Ohm with Bleeder)}}')

content = content.replace(r'\subsection{Table 2: Load Regulation ($V_{IN} = 3.0\,\text{V}$ and $V_{IN} = 5.0\,\text{V}$)}',
                          r'\subsection{Table 2: Load Regulation \texorpdfstring{($V_{IN} = 3.0\,\text{V}$ and $V_{IN} = 5.0\,\text{V}$)}{(VIN = 3.0V and VIN = 5.0V)}}')

content = content.replace(r'\subsection{Table 3: Dropout Voltage ($R_L = 10.2\,\Omega$, Full Load $\approx 118\,\text{mA}$)}',
                          r'\subsection{Table 3: Dropout Voltage \texorpdfstring{($R_L = 10.2\,\Omega$, Full Load $\approx 118\,\text{mA}$)}{(RL = 10.2 Ohm, Full Load ~ 118 mA)}}')

content = content.replace(r'\subsection{Table 4: Power Dissipation and Conversion Efficiency ($R_L = 10.2\,\Omega$)}',
                          r'\subsection{Table 4: Power Dissipation and Conversion Efficiency \texorpdfstring{($R_L = 10.2\,\Omega$)}{(RL = 10.2 Ohm)}}')

content = content.replace(r'\subsection{Dropout Voltage and $R_{DS(\text{on})}$ Derivation}',
                          r'\subsection{Dropout Voltage and \texorpdfstring{$R_{DS(\text{on})}$}{RDS(on)} Derivation}')

# 3. Break long equations that had overfull hboxes
old_eq1 = r"""\begin{equation}
        \frac{R_L}{R_L + R_{DS(\text{on})}} = 0.9737 \implies R_{DS(\text{on})} = R_L \left(\frac{1}{0.9737} - 1\right) = 10.2\,\Omega \times 0.02701 = \mathbf{0.2754\,\Omega} \quad (275.4\,\text{m}\Omega)
    \end{equation}"""

new_eq1 = r"""\begin{align}
        \frac{R_L}{R_L + R_{DS(\text{on})}} &= 0.9737 \nonumber \\
        \implies R_{DS(\text{on})} &= R_L \left(\frac{1}{0.9737} - 1\right) = 10.2\,\Omega \times 0.02701 = \mathbf{0.2754\,\Omega} \quad (275.4\,\text{m}\Omega)
    \end{align}"""
content = content.replace(old_eq1, new_eq1)

old_eq2 = r"""\begin{equation}
        P_{diss} = P_{IN} - P_{OUT} = (5.0\,\text{V} \times 0.1220\,\text{A}) - (1.2001\,\text{V} \times 0.11766\,\text{A}) = 610.0\,\text{mW} - 141.2\,\text{mW} = \mathbf{468.80\,\text{mW}}
    \end{equation}"""

new_eq2 = r"""\begin{align}
        P_{diss} &= P_{IN} - P_{OUT} = (5.0\,\text{V} \times 0.1220\,\text{A}) - (1.2001\,\text{V} \times 0.11766\,\text{A}) \nonumber \\
        &= 610.0\,\text{mW} - 141.2\,\text{mW} = \mathbf{468.80\,\text{mW}}
    \end{align}"""
content = content.replace(old_eq2, new_eq2)

with open('main.tex', 'w') as f:
    f.write(content)

print('Updated main.tex cleanly!')
