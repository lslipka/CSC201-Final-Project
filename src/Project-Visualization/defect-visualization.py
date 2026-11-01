import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background') ## Accessibility

pd.set_option('display.max_columns', None)
pd.set_option('display.width',1000)

## Orange = Train
## Red = Test
## Green = Valid


## Begin CSV Block

annotationTrain = pd.read_csv("C:\\Users\\lukas\\Files\\Dev\\CSC201\\Data\\Train\\_annotations.csv")
annotationTrain.info() #no null values

annotationTest =  pd.read_csv("C:\\Users\\lukas\\Files\\Dev\\CSC201\\Data\\Test\\_annotations.csv")
annotationTest.info() #no null values

annotationValid = pd.read_csv("C:\\Users\\lukas\\Files\\Dev\\CSC201\\Data\\Valid\\_annotations.csv")
annotationValid.info() #no null values

## End CSV Block

## Begin Train

plt.figure(figsize=(6, 4))

sns.histplot(data=annotationTrain, x='ymax', bins=30, kde=True, color='orange')


plt.title('Y Max Plot, Test Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


## End Train


## Begin Test

# Y max [test] plot

plt.figure(figsize=(6, 4))

sns.histplot(data=annotationTest, x='ymax', bins=30, kde=True, color='red')


plt.title('Y Max Plot, Test Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Y min [test] plot

plt.figure(figsize=(6, 4))

sns.histplot(data=annotationTest, x='ymin', bins=30, kde=True, color='red')


plt.title('Y Min Plot, Test Data')


plt.xlabel('Y min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Y max [test] plot

plt.figure(figsize=(6, 4))

sns.histplot(data=annotationTest, x='ymax', bins=30, kde=True, color='red')


plt.title('Y Max Plot, Test Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# class [test] plot

plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='class', bins=30, kde=True, color='red')


plt.title('Class Plot, Test Data')


plt.xlabel('Class')
plt.ylabel('Frequency')


plt.grid(False)


## End Test





## Call at the end
plt.show()