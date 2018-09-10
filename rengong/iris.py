# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import *

np.random.seed(123)

iris=pd.read_csv("C:\\Users\\jc\\Downloads\\iris.csv",header=None)
print iris.shape
print iris.head()