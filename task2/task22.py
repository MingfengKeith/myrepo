from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

data=load_iris()
feature_names=data.feature_names
target_names=data.target_names
x=data.data
group=data.target

color_code={0:"darkblue",1:"red",2:"lightgreen"}
fig,axis =plt.subplots(nrows=4,ncols=4,figsize=(16,16))
for i in range(0,4):
    for j in range(0,4):
        if i!=j:
            axis[i,j].set_xlabel(feature_names[j])
            axis[i,j].set_ylabel(feature_names[i])
            for g in np.unique(group):
                index=np.where(group == g)
                axis[i,j].scatter(x[:,j][index], x[:,i][index], c = color_code[g], s = 50, label = data.target_names[g], edgecolors = 'black')
                handles, labels = axis[i,j].get_legend_handles_labels()
fig.legend(handles, labels, loc = "center right")

for dia in range(0,4):
    axis[dia,dia].hist(x[:,dia], bins = 20, color = "darkblue")

fig.suptitle("Pair plot of the Iris Dataset, colored by class label", size = 32)
fig.savefig("task22.png")
