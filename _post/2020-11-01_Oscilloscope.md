---
blog_heading: Oscilloscope
blog_subheading:
blog_author: David Lutton
blog_publish_date: 2020/11/01
---
``` Python
import matplotlib.pyplot as plt
import numpy as np

size, aspect = 10, 2
plt.rcParams['figure.figsize'] = [aspect * size, size]
```
# One Cycle
``` Python
time = np.linspace(np.pi*-.4, np.pi*2.4, 360)
amplitude = np.sin(time)

plt.plot(time * 180 / np.pi , amplitude)
plt.xlabel('Angle [deg]')
plt.ylabel('sin(x)')

# plt.axis('tight')
# plt.annotate(text='Vpk', xy=(1.46,1.02))
# plt.annotate(text='Vrms = Vpk * 0.707', xy=(1.1,0.707+.02))
# plt.annotate(text='Vav = Vpk * 0.637', xy=(1.1,0.637+.02))
# plt.annotate(text='Vpkpk or Vpp', xy=(-1.46,1.02))
plt.axvspan(0,360, alpha=0.2)

plt.yticks([-1,-0.707,-0.637,0,0.637,0.707,1])
plt.xticks([0, 90,180,270,360])
plt.grid(axis='both')
# plt.savefig('One_Cycle.svg')
plt.show()
```
![One Cycle](/image/Osciliscope/One_Cycle.svg)  

# AC Signal
``` Python
time = np.arange(0, np.pi*2.0, 0.1)
time = np.linspace(-np.pi, np.pi, 360)
amplitude = np.sin(time)
plt.plot(time, amplitude)

plt.title('AC Signal')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')

plt.annotate(text='Vpk', xy=(1.46,1.02))
plt.annotate(text='Vrms = Vpk * 0.707', xy=(1.1,0.707+.02))
plt.annotate(text='Vav = Vpk * 0.637', xy=(1.1,0.637+.02))
# plt.annotate(text='Vpkpk or Vpp', xy=(-1.46,1.02))

plt.yticks([-1,-0.707,-0.637,0,0.637,0.707,1])
plt.grid(axis='y')
# plt.savefig('AC_Signal.svg')
plt.show()
```
![AC Signal](/image/Osciliscope/AC_Signal.svg)  

# Rise Time 10% to 90%

``` Python
time = np.arange(-1, 11, 0.1)
amplitude = np.concatenate([np.zeros(10), np.arange(0, 10, 0.1), np.ones(10)*10])

plt.plot(time, amplitude)
plt.title('10% to 90% Rise Time')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# plt.annotate(text='Pk', xy=(np.pi/2,1+.02))
plt.annotate("",xy=(9,1), xytext=(1,1),xycoords="data",
             arrowprops={"arrowstyle" : "-", "linestyle" : "--", "linewidth" : 1.5})
plt.annotate("",xy=(9,9), xytext=(9,1),xycoords="data",
             arrowprops={"arrowstyle" : "-", "linestyle" : "--", "linewidth" : 1.5})
plt.annotate("<-- 10/90% Rise Time -->",xy=(4, 0.5),xycoords="data", fontsize=15)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.xlim(-0.5, 10.5)

plt.grid(axis='both')
# plt.savefig('Rise_Time.svg')
plt.show()
```
![Rise Time](/image/Osciliscope/Rise_Time.svg)



# Square Wave
``` Python
time = np.arange(-5, 25, 0.1)
amplitude = np.concatenate([np.ones(50), np.zeros(100), np.ones(100), np.zeros(50)]) - 0.5

plt.plot(time, amplitude)
plt.annotate(text='Vpk', xy=(14.5,.47))
plt.annotate(text='Vpkpk or Vpp', xy=(3,.0))
# plt.savefig('Square_Wave.svg')
plt.show()
```
![Square Wave](/image/Osciliscope/Square_Wave.svg)

# AC Signals with DC offset and Phase offset
``` Python
time = np.linspace(np.pi*-.4, np.pi*4.4, 360)
amplitude = np.sin(time)

plt.plot(time * 180 / np.pi+0  , amplitude)
plt.plot(time * 180 / np.pi+10 , amplitude*1.4+.3)
plt.plot(time * 180 / np.pi-33 , amplitude*1.2)
plt.plot(time * 180 / np.pi+40 , amplitude*1.2-.9)

plt.title('AC Signals with DC offset and Phase offset')
plt.xlabel('Angle [deg]')
plt.ylabel('sin(x)')

plt.xticks(np.linspace(0,720, 9))
plt.xlim(0,720)
plt.grid(axis='both')
# plt.savefig('Offset.svg')
plt.show()
```
![AC Signals with DC offset and Phase offset](/image/Osciliscope/Offset.svg)

# Data
``` Python
from numpy import arange, array

points = 11
xincr = 1
xzero = -1

ydata = array([0,1,0,-1,0,1,0,-1,0,1,0])
yoffs = 0
ymult = 10
yzero = -5

x = arange(points) * xincr + xzero
y = ((ydata - yoffs) * ymult) + yzero
```
\begin{gather*}
\begin{aligned}
\mathrm{points} &= 11 \; 
\\[1pt]
\mathrm{xincr} &= 1 \; 
\\[1pt]
\mathrm{xzero} &= -1 \; 
\\[1pt]
\mathrm{ydata} &= [0,\ 1,\ 0,\ -1,\ 0,\ 1,\ 0,\ -1,\ 0,\ 1,\ 0] \; 
\\[1pt]
\mathrm{yoffs} &= 0 \; 
\\[1pt]
\mathrm{ymult} &= 10 \; 
\\[1pt]
\mathrm{yzero} &= -5 \; 
\\[10pt]
x &= \operatorname{arange} \left( \mathrm{points} \right) \cdot \mathrm{xincr} + \mathrm{xzero} \\&= \operatorname{arange} \left( 11 \right) \cdot 1 + -1 \\&= [-1,\ 0,\ 1,\ 2,\ 3,\ 4,\ 5,\ 6,\ 7,\ 8,\ 9]
\\[1pt]
y &= \left( \mathrm{ydata} - \mathrm{yoffs} \right) \cdot \mathrm{ymult} + \mathrm{yzero} \\&= \left( [0,\ 1,\ 0,\ -1,\ 0,\ 1,\ 0,\ -1,\ 0,\ 1,\ 0] - 0 \right) \cdot 10 + -5 \\&= [-5,\ 5,\ -5,\ -15,\ -5,\ 5,\ -5,\ -15,\ -5,\ 5,\ -5]  \\
\end{aligned}
\end{gather*}