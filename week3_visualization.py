import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Put blinkit_sales_cleaned.csv in this folder.
df = pd.read_csv("blinkit_sales_cleaned.csv")

# Bar chart
plt.figure(figsize=(10,6))
df.groupby("Item_Type")["Item_Outlet_Sales"].sum().sort_values().plot(kind="barh")
plt.title("Total Sales by Item Type")
plt.xlabel("Total Item Outlet Sales")
plt.ylabel("Item Type")
plt.tight_layout()
plt.savefig("charts/01_total_sales_by_item_type.png", dpi=180)
plt.show()

# Line chart
year_sales = df.groupby("Outlet_Establishment_Year")["Item_Outlet_Sales"].sum().sort_index()
plt.figure(figsize=(9,5))
year_sales.plot(marker="o")
plt.title("Sales by Outlet Establishment Year")
plt.xlabel("Outlet Establishment Year")
plt.ylabel("Total Sales")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("charts/02_sales_by_establishment_year.png", dpi=180)
plt.show()

# Scatter plot
plt.figure(figsize=(9,6))
plt.scatter(df["Item_MRP"], df["Item_Outlet_Sales"], alpha=0.25)
plt.title("Item MRP vs Item Outlet Sales")
plt.xlabel("Item MRP")
plt.ylabel("Item Outlet Sales")
plt.tight_layout()
plt.savefig("charts/03_mrp_vs_sales_scatter.png", dpi=180)
plt.show()

# Heatmap
num_cols=["Item_Weight","Item_Visibility","Item_MRP",
          "Outlet_Establishment_Year","Item_Outlet_Sales"]
corr=df[num_cols].corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/04_correlation_heatmap.png", dpi=180)
plt.show()

print("Week 3 visualization completed.")
