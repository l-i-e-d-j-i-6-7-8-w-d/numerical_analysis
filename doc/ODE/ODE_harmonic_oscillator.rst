
Ordinary Differential Equations : Practical work on the harmonic oscillator
===========================================================================

In this example, you will simulate an harmonic oscillator and compare
the numerical solution to the closed form one.

Theory
------

Read about the theory of harmonic oscillators on
`Wikipedia <https://en.wikipedia.org/wiki/Harmonic_oscillator>`__

Mechanical oscillator
~~~~~~~~~~~~~~~~~~~~~

The case of the one dimensional mechanical oscillator leads to the
following equation:

.. math::


   m \ddot x + \mu \dot x + k x = m \ddot x_d

Where:

-  :math:`x` is the position,
-  :math:`\dot x` and :math:`\ddot x` are respectively the speed and
   acceleration,
-  :math:`m` is the mass,
-  :math:`\mu` the
-  :math:`k` the stiffness,
-  and :math:`\ddot x_d` the driving acceleration which is null if the
   oscillator is free.

Canonical equation
~~~~~~~~~~~~~~~~~~

Most 1D oscilators follow the same canonical equation:

.. math::


   \ddot x + 2 \zeta \omega_0 \dot x + \omega_0^2 x = \ddot x_d

Where:

-  :math:`\omega_0` is the undamped pulsation,
-  :math:`\zeta` is damping ratio,
-  :math:`\ddot x_d` is the imposed acceleration.

In the case of the mechanical oscillator:

.. math::


   \omega_0 = \sqrt{\dfrac{k}{m}}

.. math::


   \zeta = \dfrac{\mu}{2\sqrt{mk}} 

 Undampened oscillator
~~~~~~~~~~~~~~~~~~~~~~

First, you will focus on the case of an undamped free oscillator
(:math:`\zeta = 0`, :math:`\ddot x_d = 0`) with the following initial
conditions:

.. math::


   \left \lbrace
   \begin{split}
   x(t = 0) = 1 \\
   \dot x(t = 0) = 0
   \end{split}\right.

The closed form solution is:

.. math::


   x(t) = a\cos \omega_0 t

.. code:: python

    # Setup
    %matplotlib inline
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import odeint
    
    # Setup
    f0     = 1.
    omega0 = 2. * np.pi * f0
    a      = 1.

Part 1: theoretical solution
----------------------------

Plot the closed form solution of the undamped free oscillator for 5
periods.

Steps:

1. Create an array :math:`t` reprenting time,
2. Create a function :math:`x_{th}` representing the amplitude of the
   closed form solution,
3. Plot :math:`x_{th}` vs :math:`t`.

.. code:: python

    # Complete here
    #t = 
    #xth = 
    


Part 2: Numerical solution with Euler integrator
------------------------------------------------

Solve the problem introduced in question 1 with the Euler integrator.

Steps:

1. Rewrite the canonical equation as a system of first order ODEs
   depending of the variable :math:`X = [x, \dot x]`,
2. Code the derivative function :math:`f(X,t) = \dot X`,
3. Define initial conditions :math:`X_0`,
4. Solve the problem.
5. Plot the position :math:`x` along and compare it with the theoretical
   solution.


Part 3: Energies an errors
--------------------------

Calculate and plot the kinetic energy :math:`E_c`, the potential energy
:math:`E_p` and the total energy :math:`E_t = E_c + E_p`, comment the
result.

Steps:

1. Calculate :math:`E_c`,
2. Calculate :math:`E_p`,
3. Calculate :math:`E_t`,
4. Plot the evolution of the 3 energies. You can use *plt.fill\_between*
   instead of *plt.plot*,
5. Use the results to define a relative error estimator base on
   energies.


Part 4: Numerical solution convergence
--------------------------------------

Plot the effect of the number time steps :math:`n_t` on the error
:math:`e`.

Steps:

1. Create an array containing the different number of time steps from
   100 to 100000,
2. Loop over this array and calculate the the error for each
   configuration,
3. Plot the error as a function of :math:`n_t`.


Part 5: integrator benchmark
----------------------------

Rewrite the code of part 4 in order to compare the RK4 and ODEint
solvers with the Euler solver. Comment the efficiency of each solver.


Part 6: Error *vs.* time
------------------------

Modify the code of part 5 in order to measure the computing time of each
method in each case. Plot the error *vs.* the computing time.
