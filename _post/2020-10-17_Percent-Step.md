---
blog_heading: Percent Steps
blog_subheading: 
blog_author: David Lutton
blog_publish_date: 2020/10/17
---

# Purpose
Calculate a array of frequencies for use in RF immunity tests  

# Presumptions
Start is not below 100Hz at 1% step

# Where
Applied in EN 61000-4-3 and EN 61000-4-6

# How
Calculates the number of points needed to have <= percent_step in logspace   
Use [geomspace](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html) to produce array of frequencies, limited to integers with int64

Where geomspace returns numbers spaced evenly on a log scale (a geometric progression).



# Example
\begin{gather*}
\begin{aligned}
\mathrm{decade} &= \log_{10} \left( \frac{ \mathrm{stop Hz} }{ \mathrm{start Hz} } \right) \\&= \log_{10} \left( \frac{ 230000000.0 }{ 150000.0 } \right) \\&= 3.186  \\
\\[10pt]
\mathrm{factor} &= \frac{ \mathrm{percent}_{step} }{ 100 } + 1 \\&= \frac{ 1 }{ 100 } + 1 \\&= 1.01  \\
\\[10pt]
\mathrm{points} &= \left \lceil \frac{ \mathrm{decade} }{ \log_{10} \left( factor \right) } \right \rceil \\&=  \left \lceil \frac{ 3.186 }{ \log_{10} \left( 1.01 \right) } \right \rceil \\&= 738  \\
\end{aligned}
\end{gather*}
## Compact form
\begin{gather*}
\begin{aligned}
\mathrm{points} &= \left \lceil \frac{ \log_{10} \left( \frac{ \mathrm{stop Hz} }{ \mathrm{start Hz} } \right) }{ \log_{10} \left( \frac{ \mathrm{percent}_{step} }{ 100 } + 1 \right) } \right \rceil \\&= \left \lceil \frac{ \log_{10} \left( \frac{ 230000000.0 }{ 150000.0 } \right) }{ \log_{10} \left( \frac{ 1 }{ 100 } + 1 \right) } \right \rceil \\&= 738  \\
\end{aligned}
\end{gather*}

# Python
``` python
from numpy import log10, geomspace, int64, ceil

def percent_increment(start, stop, percent_step):
    decade = log10(stop/start)

    ratio = percent_step / 100 + 1

    points = ceil(decade / log10(ratio))
    
    # points = int(ceil( log10(stop/start) / log10(percent_step / 100 + 1)))
    
    # print(f'{decade = }')
    # print(f'{ratio = }')
    # print(f'{points = }')
    return geomspace(start, stop, int(points), dtype=int64, endpoint=True)

start, stop, percent = 150e3, 230e6, 1
percent_increment(start, stop, percent)
# start, stop, percent = 80e6, 1e9, 1
# start, stop, percent = 1e9, 6e9, 1

'''
array([   
   150000,    151500,    153015,    154546,    156092,    157653,
   159230,    160823,    162431,    164056,    165697,    167354,
   169028,    170719,    172427,    174151,    175893,    177653,
   179430,    181224,    183037,    184868,    186717,    188585,
   190471,    192376,    194300,    196244,    198207,    200189,

172336450, 174060241, 175801274, 177559721, 179335758, 181129559,
182941303, 184771169, 186619338, 188485993, 190371319, 192275503,
194198734, 196141202, 198103099, 200084620, 202085961, 204107321,
206148899, 208210898, 210293523, 212396978, 214521473, 216667219,
218834427, 221023313, 223234093, 225466986, 227722214, 230000000
])
'''
```