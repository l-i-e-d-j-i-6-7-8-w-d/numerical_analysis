
Tutorial: The simple pendulum
=============================

Introduction
------------

This tutorial aims at modelling and solving the yet classical but not so
simple problem of the pendulum. A representiation is given bellow
(source: `Wikipedia <https://en.wikipedia.org/wiki/Pendulum>`__).

.. figure:: https://upload.wikimedia.org/wikipedia/commons/f/fa/PenduloTmg.gif
   :alt: Simple pendulum

   The simple pendulum

On a mechanical point of view, the mass :math:`m` is supposed to be
concentrated at the lower end of the rigid arm. The length of the arm is
noted :math:`l`. The angle between the arm and the vertical direction is
noted :math:`\theta`. A simple modelling using dynamics leads to:

.. math::


   \Gamma = \vec P + \vec T

Where:

-  :math:`\vec \Gamma` is the acceleration of the mass,
-  :math:`\vec P` if the weight of the mass,
-  :math:`\vec T` if the reaction force of the arm.

A projection of this equation along the direction perpendicular to the
arm gives a more simple equation:

.. math::


   \ddot \theta = \dfrac{g}{l} \sin \theta

This equation is a second order, non linear ODE. The closed form
solution is only known when the equation is linearized by assuming that
:math:`\theta` is small enough to write that
:math:`\sin \theta \approx \theta`. In this tutorial, we will solve this
problem with a numerical approach that does not require such
simplification.

.. code:: python

    # Setup
    %matplotlib nbagg
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.integrate import odeint


 Numerical values
~~~~~~~~~~~~~~~~~

.. code:: python

    l = 1.   # m
    g = 9.81 # m/s**2

Part 1: Reformulation of the problem
------------------------------------

-  This problem can be reformulated to match the standard formulation
   :math:`\dot X = f(X, t)`:

.. math::


   X = \begin{bmatrix} \theta \\ \dot \theta \end{bmatrix}
   = \begin{bmatrix} x_0 \\ x_1 \end{bmatrix}

.. math::


   \dot X = \begin{bmatrix} x_1 \\ -\dfrac{g}{l} \sin x_0 \end{bmatrix} = f(X, t) 

-  Write the function :math:`f` in Python:

.. code:: python

    def f(X, t):
        """
        The derivative function
        """
        # To be completed
        return

Part 3: Numerical solution
--------------------------

Solve the problem with Euler, RK4 and ODEint integrators and compare the
results. First assume that the pendulum is released with no speed
(:math:`\dot \theta = 0 ^o/s`) at :math:`\theta = 10 ^o`. The time
discretization will be as follows:

-  duration: 10 s,
-  time step: 0.01 s.

.. code:: python

    def Euler(func, X0, t):
        """
        Euler integrator.
        """
        dt = t[1] - t[0]
        nt = len(t)
        X  = np.zeros([nt, len(X0)])
        X[0] = X0
        for i in range(nt-1):
            X[i+1] = X[i] + func(X[i], t[i]) * dt
        return X
    
    def RK4(func, X0, t):
        """
        Runge and Kutta 4 integrator.
        """
        dt = t[1] - t[0]
        nt = len(t)
        X  = np.zeros([nt, len(X0)])
        X[0] = X0
        for i in range(nt-1):
            k1 = func(X[i], t[i])
            k2 = func(X[i] + dt/2. * k1, t[i] + dt/2.)
            k3 = func(X[i] + dt/2. * k2, t[i] + dt/2.)
            k4 = func(X[i] + dt    * k3, t[i] + dt)
            X[i+1] = X[i] + dt / 6. * (k1 + 2. * k2 + 2. * k3 + k4)
        return X
    
    # ODEint is preloaded.


.. code:: python

    # Define the time vector t and the initial conditions X0

Part 4: Energies an errors
--------------------------

Calculate and plot the kinetic energy :math:`E_c`, the potential energy
:math:`E_p` and the total energy :math:`E_t = E_c + E_p` for all 3
cases, plot it and comment.

