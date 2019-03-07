# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:11:37 2019

@author: papaj
"""

import numpy as np
import machup.MU as MU
import matplotlib.pyplot as plt


baseline = MU.MachUp("BaselineGlider.json")

atmos_state = {"V_mag":22.7,
              "rho":0.0020628,
              "alpha":0,
              "beta":0}

baseline.create_stl("baseline.stl")

FM = baseline.solve(aero_state=atmos_state)
print(FM)

derivs = baseline.derivatives(aero_state=atmos_state)
for key in derivs:
    print(key,derivs[key])
