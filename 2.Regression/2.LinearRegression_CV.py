#!/usr/bin/python
# -*- coding:utf-8 -*-

#广告预测案例 ,交叉验证 ； lasso ，ridge ；GridSearchCV

import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pprint import pprint