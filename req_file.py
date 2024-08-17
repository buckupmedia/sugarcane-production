import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
df = pd.read_csv("List of Countries by Sugarcane Production.csv")
df.head()

#DATA CLEANING 

df = pd.read_csv("List of Countries by Sugarcane Production.csv")
df["Production (Tons)"]= df["Production (Tons)"].str.replace(".", "")
df["Production per Person (Kg)"]= df["Production per Person (Kg)"].str.replace(".", "").str.replace(",",".")
df["Acreage (Hectare)"]= df["Acreage (Hectare)"].str.replace(".", "")
df["Yield (Kg / Hectare)"]= df["Yield (Kg / Hectare)"].str.replace(".", "").str.replace(",", ".")
df.rename(columns = {"Production (Tons)" : "Production(Tons)"}, inplace = True)
df.rename(columns = {"Production per Person (Kg)" : "Production_per_person(Kg)"}, inplace = True)
df.rename(columns = {"Acreage (Hectare)" : "Acreage(Hectare)"}, inplace = True)
df.rename(columns = {" 	Yield (Kg / Hectare)" : "Yield (Kg / Hectare)"}, inplace = True)
df.head()

#checking for the null values in the dataset
df.isnull().sum()
df[df["Acreage(Hectare)"].isnull()]
#since there is null value in this particular row for both Acreage(Hectare) and Yield (Kg / Hectare) so we will delete it 
#dropping the null values and reseting the index 
df = df.dropna().reset_index()
df=df.drop(["index", "Unnamed: 0"], axis = 1)


#Converting the datatype of numeric values
df["Production(Tons)"]= df["Production(Tons)"].astype("float")
df["Production_per_person(Kg)"]= df["Production_per_person(Kg)"].astype("float")
df["Acreage(Hectare)"]= df["Acreage(Hectare)"].astype("float")
df["Yield (Kg / Hectare)"]= df["Yield (Kg / Hectare)"].astype("float")

#DATATYPES OF THE COLUMNS
df.dtypes

df.head()

df.nunique()

#continent wise production of sugarcane
df["Continent"].value_counts()

#bar graph for the above statement
colors = ["silver", "blue", "green","yellow", "purple", "orange"]
df["Continent"].value_counts().plot(kind= "bar", color = colors)
plt.title("CONTINENT WISE SUGARCANE PRODUCTION", color = "red", fontdict ={'fontsize': 16})

plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.distplot(df["Production(Tons)"])
plt.subplot(2,2,2)
sns.distplot(df["Production_per_person(Kg)"])
plt.subplot(2,2,3)
sns.distplot(df["Acreage(Hectare)"])
plt.subplot(2,2,4)
sns.distplot(df["Yield (Kg / Hectare)"])


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.subplot(2,2,2)
sns.boxplot(df["Production_per_person(Kg)"])
plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.subplot(2,2,4)
sns.boxplot(df["Yield (Kg / Hectare)"])



#We will create a new database that will have only country and production(ton) column

df_new = df[["Country","Production(Tons)"]].set_index("Country")

#We will create a new column that will give us percentage wise production of each country
df_new["Production(Tons)_percentage"]= df_new["Production(Tons)"] *100 / df_new["Production(Tons)"].sum()

#Top 5 Countries with max sugarcane production
df_new.head()


#Lets plot a pie chart for the above data for all the countries
df_new["Production(Tons)_percentage"].plot(kind = "pie", autopct = "%.2f")
plt.title("Sugar cane production of all the countries")

#15 top producer of sugar cane
df_new["Production(Tons)_percentage"].head(15).plot(kind = "pie", autopct = "%.2f")
plt.title("Sugar cane production in top 15 countries")

#15 top producer of sugar cane bar graph
colors = ["orange", "blue", "green", "red", "purple", "brown", "pink", "yellow", "cyan", "magenta"]
df_new["Production(Tons)_percentage"].head(15).plot(kind = "bar", color= colors)
plt.title("Sugar cane production in top 15 countries" ,  color = "red")
plt.xlabel("PRODUCTION IN TONS", color = "red")
plt.ylabel("COUNTRIES",  color = "red")

#10 top COUNTRIES WITH MAX LAND
df_new1 = df[["Country","Acreage(Hectare)"]].set_index("Country")
df_acre = df_new1.sort_values("Acreage(Hectare)", ascending = False)
colors = ["orange", "blue", "green", "red", "purple", "brown", "pink", "yellow", "cyan", "magenta"]
df_acre["Acreage(Hectare)"].head(10).plot(kind = "bar", color = colors)
plt.title("AREA WISE LAND DISTRIBUTION" ,  color = "red")
plt.ylabel("ACREAGE", color = "red")
plt.xlabel("COUNTRIES",  color = "red")

#10 top highest yield countries
df_new2 = df[["Country","Yield (Kg / Hectare)"]].set_index("Country")
df_acre1 = df_new2.sort_values("Yield (Kg / Hectare)", ascending = False)
colors = ["orange", "blue", "green", "red", "purple", "brown", "pink", "yellow", "cyan", "magenta"]
df_acre1["Yield (Kg / Hectare)"].head(10).plot(kind = "bar", color = colors)
plt.title("HIGHEST YIELD COUNTRIES" ,  color = "red")
plt.ylabel("Yield (Kg / Hectare)", color = "red")
plt.xlabel("COUNTRIES",  color = "red")

df_new_ = df[["Country", "Production_per_person(Kg)"]].set_index("Country")

df_new_.sort_values("Production_per_person(Kg)", ascending = False, inplace = True)
df_new_.head(10).plot(kind = "bar")
plt.xlabel("COUNTRY", color = "red")
plt.ylabel("Production per person in KG", color = "red")
plt.title("Countries with highest production per person", color = "red")


#Create a seprate database with only numeric values
df1 = df[["Production(Tons)", "Production_per_person(Kg)","Acreage(Hectare)", "Yield (Kg / Hectare)"]]
df1.corr()

#MORE THE VALUE CLOSER TO 1 MORE IT IS DEPENDENT ON EACH OTHER

#Creating a heatmap to find the correlation 
sns.heatmap(df1.corr(), cmap = "Greens",annot= True, linewidths=11)


sns.scatterplot(data = df , x= "Acreage(Hectare)", y = "Production(Tons)")

sns.scatterplot(data = df , x= "Yield (Kg / Hectare)", y = "Production(Tons)")

#Creating a new dataset that is according to the continents
df_Continent= df.groupby("Continent").sum()
#sorting the production in ascending order
df_Continent=df_Continent.sort_values("Production(Tons)", ascending =False)
#creating a bar graph now 
df_Continent["Production(Tons)"].plot(kind = "bar", color = colors)
plt.xlabel("Continents", color = "red")
plt.ylabel("Production(Tons)", color= "red")
plt.title("Production of Sugarcane Continents wise", color = "red")
plt.show()

df1= df.groupby("Continent").sum()
df1["Production(Tons)"].plot(kind = "pie", autopct = "%.2f")


