# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:11:37 2019

@author: papaj
"""

import numpy as np
import machup.MU as MU
import matplotlib.pyplot as plt


baseline = MU.MachUp("BaselineDesign.json")

atmos_state = {"V_mag":10,
              "rho":0.0023769,
              "alpha": 0,
              "beta":0}

