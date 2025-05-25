#This project uses pandas and matplotlib to visualize wine review data, focusing on the points and price columns from PE04_winereview.csvS
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("PE04_winereview.csv")

# Part 1: Bar chart of 'points'**
points_count = df['points'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
points_count.plot(kind='bar', color='skyblue')
plt.title("Wine Review Score")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("plot_part1_score.png")  # Save the image
plt.show()
##Comments: Part 1: Bar chart of points using value_counts() → plot_part1_score.png

# Part 2a: Histogram of 'points' (bin=10)**
plt.figure(figsize=(8, 5))
plt.hist(df['points'], bins=10, color='cornflowerblue', edgecolor='black')
plt.title("Wine Score Histogram (Bin Size 10)")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plot_part2a_hist_bin10.png")
plt.show()
#comments:a) Histograms of points
#Bin size 10 → plot_part2a_hist_bin10.png


# Part 2b: Histogram of 'points' (bin=3)**
plt.figure(figsize=(8, 5))
bins_3 = range(int(df['points'].min()), int(df['points'].max()) + 3, 3)
plt.hist(df['points'], bins=bins_3, color='royalblue', edgecolor='black')
plt.title("Wine Score Histogram (Bin Size 3)")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plot_part2b_hist_bin3.png")
plt.show()
##Comments: Bin size 3 → plot_part2b_hist_bin3.png


# Part 3: Histogram of 'price' (bin=5)**
clean_price = df['price'].dropna()  # Remove missing values
bins_5 = range(0, int(clean_price.max()) + 5, 5)

plt.figure(figsize=(8, 5))
plt.hist(clean_price, bins=bins_5, color='mediumseagreen', edgecolor='black')
plt.title("Wine Price Histogram (Bin Size 5)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plot_part3_price_bin5.png")
plt.show()
#Comments:Part 3:Histogram of price (after removing missing values) with bin size 5 → plot_part3_price_bin5.png