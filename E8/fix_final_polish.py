with open('main.tex', 'r') as f:
    text = f.read()

# Fix line 46 overfull hbox
old_obj7 = r"7. To check the feedback stability on an oscilloscope with different output capacitors ($10\,\mu\text{F}, 47\,\mu\text{F}, 94\,\mu\text{F}$) and check for any oscillation."
new_obj7 = r"7. To check feedback loop stability on an oscilloscope using $10\,\mu\text{F}, 47\,\mu\text{F}$, and $94\,\mu\text{F}$ output capacitors to verify that the loop does not oscillate."
text = text.replace(old_obj7, new_obj7)

# Fix floating table 7 splitting Section 10
# Insert \clearpage right before Section 10 so Table 7 is printed before Section 10 begins!
old_sec10 = r"\section{Safety Limits and Laboratory Precautions Observed}"
new_sec10 = r"\clearpage" + "\n" + r"\section{Safety Limits and Laboratory Precautions Observed}"
text = text.replace(old_sec10, new_sec10)

with open('main.tex', 'w') as f:
    f.write(text)

print("Applied final polish!")
