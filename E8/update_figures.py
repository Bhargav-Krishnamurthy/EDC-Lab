with open('main.tex', 'r') as f:
    text = f.read()

old_fig = r"""\begin{figure}[htbp]
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
\end{figure}"""

new_fig = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.92\textwidth]{circuit.png}
    \caption{LTspice Simulation Schematic of the Closed-Loop NMOS Linear Voltage Regulator ($V_{OUT} = 1.2\,\text{V}$).}
    \label{fig:circuit_schematic}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.48\textwidth]{realcircuit.jpeg}
    \caption{Breadboard Experimental Setup.}
    \label{fig:realcircuit}
\end{figure}"""

text = text.replace(old_fig, new_fig)

with open('main.tex', 'w') as f:
    f.write(text)

print("Updated figure placement and size!")
