import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:\\Users\\MEHWISH\\Downloads\\retail_sales_dataset.csv")
print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.isnull().sum())
  
          # Discriptive statistics
print(df.describe())

           #Tme series analysis

df["Date"]=pd.to_datetime(df["Date"])
   # set date as index
df.set_index("Date",inplace=True)
print(df.head())
      # Analyze sales over time series technique
print("Daily Sales :\n")
daily_sales=df["Total Amount"].resample("D").sum()
print(daily_sales.head(10))
print("Monthly Sales :\n")
monthly_sales=df["Total Amount"].resample("ME").sum()
print(monthly_sales.head(10))
print("Yearly Sales :\n")
yearly_sales=df["Total Amount"].resample("YE").sum()
print(yearly_sales.head(10))

        # customer demographics
print(df.groupby(["Gender","Age","Product Category"])["Quantity"].sum())
  
# Purchaising behavior
# frequency means how many time it visits, Monetary means how many amount it spend
FM=df.groupby("Customer ID").agg(Frequency=("Transaction ID","count"),Monetary=("Total Amount",sum)).reset_index()
print(FM.head(10))


# visatulation
# Bar plot
sales=df.groupby("Product Category")["Total Amount"].sum().sort_values()
plt.figure(figsize=(10,5))
plt.bar(sales.index,sales.values,width=0.4,color="teal")
plt.xlabel("Product Category")
plt.ylabel("Total sales")
plt.title("Total sales by product categort")
plt.show()

# Line plot
monthly_sales=df["Total Amount"].resample("ME").sum()
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index,monthly_sales.values,marker="o",linestyle="-",color="navy")
plt.title("Monthly sales Trend")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.grid(True)
plt.show()

numerical_cols=["Age","Quantity","Price per Unit","Total Amount"]
corr_matrics=df[numerical_cols].corr()

# Heatmap
plt.figure(figsize=(10,5))
sns.heatmap(corr_matrics,annot=True,fmt=".2f",cmap="RdBu",linewidths=.5)
plt.title("Correlation over numericals features")
plt.show()