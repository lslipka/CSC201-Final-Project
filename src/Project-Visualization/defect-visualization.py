import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

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

# Begin Y max [train]

plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTrain, x='ymax', bins=30, kde=True, color='orange')


plt.title('Y Max Plot, Train Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin y min [train]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTrain, x='ymin', bins=30, kde=True, color='orange')


plt.title('Y Min Plot, Train Data')


plt.xlabel('Y min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin X max [train]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTrain, x='xmax', bins=30, kde=True, color='orange')


plt.title('X Max Plot, Train Data')


plt.xlabel('X max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin X min [train]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTrain, x='xmin', bins=30, kde=True, color='orange')


plt.title('X Min Plot, Train Data')


plt.xlabel('X min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin class [train]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTrain, x='class', bins=30, kde=True, color='orange')


plt.title('Class Plot, Train Data')


plt.xlabel('Class')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


## End Train

## Begin Valid

# Begin Y max [valid]

plt.figure(figsize=(10, 8))

sns.histplot(data=annotationValid, x='ymax', bins=30, kde=True, color='green')


plt.title('Y Max Plot, Validation Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin y min [valid]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationValid, x='ymin', bins=30, kde=True, color='green')


plt.title('Y Min Plot, Validation Data')


plt.xlabel('Y min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin X max [valid]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationValid, x='xmax', bins=30, kde=True, color='green')


plt.title('X Max Plot, Validation Data')


plt.xlabel('X max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin X min [valid]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationValid, x='xmin', bins=30, kde=True, color='green')


plt.title('X Min Plot, Validation Data')


plt.xlabel('X min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin class [valid]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationValid, x='class', bins=30, kde=True, color='green')


plt.title('Class Plot, Validation Data')


plt.xlabel('Class')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


## End Valid

## Begin Test

# Begin Y max [test]

plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='ymax', bins=30, kde=True, color='red')


plt.title('Y Max Plot, Test Data')


plt.xlabel('Y max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin y min [test]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='ymin', bins=30, kde=True, color='red')


plt.title('Y Min Plot, Test Data')


plt.xlabel('Y min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()

# Begin X max [test]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='xmax', bins=30, kde=True, color='red')


plt.title('X Max Plot, Test Data')


plt.xlabel('X max')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin X min [test]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='xmin', bins=30, kde=True, color='red')


plt.title('X Min Plot, Test Data')


plt.xlabel('X min')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


# Begin class [test]


plt.figure(figsize=(10, 8))

sns.histplot(data=annotationTest, x='class', bins=30, kde=True, color='red')


plt.title('Class Plot, Test Data')


plt.xlabel('Class')
plt.ylabel('Frequency')


plt.grid(False)


plt.tight_layout()


## End Test

## Source: https://stackoverflow.com/questions/26368876/saving-all-open-matplotlib-figures-in-one-file-at-once 

def multipage(filename, figs=None, dpi=200):
    pp = PdfPages(filename)
    if figs is None:
        figs = [plt.figure(n) for n in plt.get_fignums()]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

multipage("C:\\Users\\lukas\\Files\\Dev\\CSC201\\src\\assets\\CSC201-Visualization.pdf")

def individualImages():
    figs = plt.get_fignums()
    for fig in figs:
        plt.figure(fig)
        plt.savefig(f'C:\\Users\\lukas\\Files\\Dev\\CSC201\\src\\assets\\image{fig}.png', format='png')

individualImages()

## Call at the end
plt.show()