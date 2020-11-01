---
blog_heading: Distance Change Correction dB
blog_subheading: 
blog_author: David Lutton
blog_publish_date: 2020/10/14
---

# Purpose
Apply a correction for distance change  
# Presumptions
All distances are in far field for the frequiencies being considered
# Where
Applied in CISPR 16-1-4 for sVSWR calibration
# Product
Is dB loss/gain for distance change  
Loss for increasing distance  
Gain for reducing distance

# Python
``` python
from numpy import log10

distance_measurement = 340  # cm
distance_reference = 300  # cm
x = 20 * log10(distance_measurement / distance_reference)
# dB loss/gain for distance change
```

# Example
\begin{gather*}
\begin{aligned}
\mathrm{distance}_{measurement} &= 340 \; 
\\[10pt]
\mathrm{distance}_{reference} &= 300 \; 
\\[10pt]
x &= 20 \cdot \log_{10} \left( \frac{ \mathrm{distance}_{measurement} }{ \mathrm{distance}_{reference} } \right) \\&= 20 \cdot \log_{10} \left( \frac{ 340 }{ 300 } \right) \\&= 1.087 \; \;\textrm{(dB loss/gain for distance change)}\\
\end{aligned}
\end{gather*}
