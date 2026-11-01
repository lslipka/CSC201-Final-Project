import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background') ## Accessibility

pd.set_option('display.max_columns', None)
pd.set_option('display.width',1000)

annotationTest =  pd.read_csv("C:\\Users\\lukas\\Files\\Dev\\CSC201\\Data\\Test\\_annotations.csv")
annotationTest.info() #no null values


plt.figure(figsize=(6, 4))

sns.histplot(data=annotationTest, x='ymax', bins=30, kde=True, color='red')


plt.title('Ymax Plot')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


plt.show()
plt.close()
