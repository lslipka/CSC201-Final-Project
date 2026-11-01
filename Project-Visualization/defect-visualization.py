import numpy as np
import pandas as pd
import matplotlib as plt

#plt.style.use('dark_background') ## Accessibility

pd.set_option('display.max_columns', None)
pd.set_option('display.width',1000)

annotationTest =  pd.read_csv("C:\\Users\\lukas\\Files\\Dev\\CSC201\\Data\\Test\\_annotations.csv")
annotationTest.info()

