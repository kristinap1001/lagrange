# Lagrange Points Calculator
Calculate &amp; plot Lagrange points of 2-body system\
Usage: `lagrange.py m1 m2 d`\
The program will print the coordinates of Lagrange points to the console and open the MatPlotLib figure.

# Gravitational Potential and Acceleration Equations
The following equations were used to find the gravitational potential and acceleration for a two-body system. Masses are in solar masses and distances are in astronomical units, making $G=1$. The origin is defined at the system's center of mass with both masses along the x axis, so $x_{1} = -\frac{m_{2}}{m}d$ and $x_{2} = \frac{m_{1}}{m}d$, with d being the distance between the masses and $m=m_{1}+m_{2}$. Thus, $\mathbf{r_{1}}=(x_{1},0)$ and $\mathbf{r_{2}}=(x_{2},0)$. $\Omega^2$ is the angular velocity squared, or $\frac{m}{d^3}$.
Equation for gravitational potential:
```math
    \Phi = -\frac{m_{1}}{|\mathbf{r}-\mathbf{r_{1}}|} 
    - \frac{m_{2}}{|\mathbf{r}-\mathbf{r_{2}}|} 
    - \frac{1}{2}\Omega^2r^2
```
Equation for gravitational acceleration:
```math
    g = -\nabla\Phi = -\frac{m_{1}}{|\mathbf{r}-\mathbf{r_{1}}|^3}(\mathbf{r}-\mathbf{r_{1}}) 
    - \frac{m_{2}}{|\mathbf{r}-\mathbf{r_{2}}|^3}(\mathbf{r}-\mathbf{r_{2}}) 
    + \Omega^2\mathbf{r}
```
The x and y components of the gravitational acceleration are, respectively,
```math
    g_{x} = -\frac{m_{1}}{((x-x_{1})^2+y^2)^\frac{3}{2}}(x-x_{1}) 
    - \frac{m_{2}}{((x-x_{2})^2+y^2)^\frac{3}{2}}(x-x_{2}) 
    + \Omega^2x
```
```math
    g_{y} = -\frac{m_{1}}{((x-x_{1})^2+y^2)^\frac{3}{2}}y 
    - \frac{m_{2}}{((x-x_{2})^2+y^2)^\frac{3}{2}}y
    + \Omega^2y
```
I used MatPlotLib to graph these equations in my Python program. When graphing the acceleration vectors, I divided their components by the magnitude to the 0.6 power to keep the graph clean and readable. Additionally, the contour lines for the gravitational potential are graphed on a logarithmic scale.

# Lagrange Points Calculation
To find the Lagrange points, I used a simple bisection root finding function with a tolerance of $10^{-4}$. L1, L2, and L3 are roots of $g_{x}$ (eq. 3) within the brackets $[x_{1}+0.01,x_{2}-0.01]$, $[x_{2}+0.01,2d]$, and $[-2d,x_{1}-0.01]$, respectively, along the x axis. L4 and L5 are roots of $g_{y}$ (eq. 4) along the $\frac{x1+x2}{2}$ axis within the brackets $[0.01,2d]$ and $[-2d,-0.01]$, respectively. I adjusted some of the bracket bounds by 0.01 to avoid the algorithm dividing by zero or wrongly placing L4 and L5 on the x axis. The locations of the points are shown as red dots on the figures below.

![Case1_Figure-50](https://github.com/user-attachments/assets/0590de0e-ddee-4962-96f0-6b72198253d4)
![Case2_Figure-50](https://github.com/user-attachments/assets/dd8fc5cc-6722-4b0f-bf90-5e7a29b47e5a)\
_Examples with_ ($m_{1}=3 M_{solar}, m_{2}=1 M_{solar}, d=1$ AU) _and_ ($m_{1}=100 M_{solar}, m_{2}=1 M_{solar}, d=1$ AU)

# James Webb Space Telescope
![JWST_Figure_Full-50](https://github.com/user-attachments/assets/680a60a3-8926-4d42-b1b2-d6201218ad2b)
![JWST_Figure_Zoom-50](https://github.com/user-attachments/assets/d3f6aab0-a59f-4664-99b4-7e23a4cc8c79)\
_Example of Earth-Sun system, with zoomed-in figure (right) showing JWST's approximate location at L2_

In order for the JWST to shield the light from the Sun, Earth, and Moon, the best location is at L2 of the Sun-Earth system. To model this system, $m_{1}=1$, $m_{2}=\frac{M_{earth}}{M_{solar}}=$ 3.0027e-6, and $d=1$. The location of L2 given by the program is (1.0101,0). This means that JWST should be orbiting the Earth at a distance of 0.0101 AU.
