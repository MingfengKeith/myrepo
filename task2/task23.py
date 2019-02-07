import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import dataset
data=pd.read_csv('mpg.csv',index_col=0)
group=np.asarray(data['drv'])
color_code={"f": 'goldenrod',"4":'black',"r":'skyblue'}
displacement = np.asarray(data['displ'])
fuel_economy = np.asarray(data['cty'])

#18.1
fig, axis = plt.subplots(nrows = 2, ncols = 2, figsize = (16, 16))
for g in np.unique(group):
    index = np.where(group == g)
    axis[0][0].scatter(displacement[index], fuel_economy[index], c = color_code[g], s = 50, label = g)
axis[0][0].set_xlabel("displacement (I)")
axis[0][0].set_ylabel("fuel economy (mpg)")
axis[0][0].set_title ("Figure 18.1: City fuel economy versus engine displacement")
Legend = axis[0][0].legend()
Legend.get_texts()[0].set_text('4WD')
Legend.get_texts()[1].set_text('FWD')
Legend.get_texts()[2].set_text('RWD')
Legend.set_title("drive train")

#18.2
for g in np.unique(group):
    index = np.where(group == g)
    axis[0][1].scatter(displacement[index], fuel_economy[index], c = color_code[g], s = 50, label = g, alpha = 0.5)
axis[0][1].set_xlabel("displacement (I)")
axis[0][1].set_ylabel("fuel economy (mpg)")
axis[0][1].set_title ("Figure 18.2: City fuel economy versus engine displacement")
Legend = axis[0][1].legend()
Legend.get_texts()[0].set_text('4WD')
Legend.get_texts()[1].set_text('FWD')
Legend.get_texts()[2].set_text('RWD')
Legend.set_title("drive train")

#18.3
x_3 = displacement + (np.random.rand(len(displacement)) * 0.1)
y_3 = fuel_economy + (np.random.rand(len(fuel_economy)) * 0.1)
for g in np.unique(group):
    index = np.where(group == g)
    axis[1][0].scatter(x_3[index], y_3[index], c = color_code[g], s = 50, label = g, alpha = 0.5)
axis[1][0].set_xlabel("displacement (I)")
axis[1][0].set_ylabel("fuel economy (mpg)")
axis[1][0].set_title ("Figure 18.3: City fuel economy versus engine displacement")
Legend = axis[1][0].legend()
Legend.get_texts()[0].set_text('4WD')
Legend.get_texts()[1].set_text('FWD')
Legend.get_texts()[2].set_text('RWD')
Legend.set_title("drive train")

#18.4
x_3 = displacement + (np.random.rand(len(displacement)) * 2)
y_3 = fuel_economy + (np.random.rand(len(fuel_economy)) * 2)
for g in np.unique(group):
    index = np.where(group == g)
    axis[1][1].scatter(x_3[index], y_3[index], c = color_code[g], s = 50, label = g, alpha = 0.5)
axis[1][1].set_xlabel("displacement (I)")
axis[1][1].set_ylabel("fuel economy (mpg)")
axis[1][1].set_title ("Figure 18.4: City fuel economy versus engine displacement")
Legend = axis[1][1].legend()
Legend.get_texts()[0].set_text('4WD')
Legend.get_texts()[1].set_text('FWD')
Legend.get_texts()[2].set_text('RWD')
Legend.set_title("drive train")

#save image
fig.savefig("task23.png")
plt.show()
