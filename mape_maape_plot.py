import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mape_maape.csv")

fig, ax = plt.subplots(figsize=(15, 8))
ax = sns.lineplot(data=df, x=df.index, y="MAPE", marker= "o", label="MAPE")
ax1 = sns.lineplot(data=df, x=df.index, y="MAAPE", marker= "o", label="MAAPE")
my_xticks = df.residue.tolist()
plt.xticks(df.index, my_xticks)
plt.xlabel("Residue (y_real - y_pred)")
plt.ylabel("Metrics (%)")

# zip joins x and y coordinates in pairs
for x,y in zip(df.index,df["MAPE"]):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y+4), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
# zip joins x and y coordinates in pairs
for x,y in zip(df.index,df["MAAPE"]):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
     
plt.show()
