PE05

Task Overview:
 PE05 - Image Enhancement with PIL
 In this exercise, I used the Python Pillow (PIL) library to apply a series of image filters and enhancement techniques.
 The goal was to improve the quality of a dark image (PE05-input.jpg) using filters like histogram equalization, unsharp masking, and contrast enhancement.
 Tools Used:- Pillow (PIL) - For image processing- Matplotlib - For displaying images
 Steps Performed:
 1. Original Image Displayed
   - Observed 2 people in the image.
 2. Histogram Equalization
   - Improved brightness and contrast.
   - Now, 4 tree trunks are clearly visible along the left sidewalk.
 3. Unsharp Mask
   - Applied to enhance edge clarity.
   - Helped reveal 2 windows on the second floor of building 1 (label 1).
 4. Contrast Boost
   - Made the image more readable.
   - Helped identify about 3 windows on building 2 (label 2).
 Final Output:
 The enhanced image was saved as PE05-output.jpg and visually analyzed to answer the following questions:
 Observations:- People in image: 2- Trees visible: 4 trunks- Windows on 2nd floor (building 1): 2
- Windows on building 2: about 3

PE04 - Wine Review Data Visualization

Description
This project uses the dataset `PE04_winereview.csv` to visualize key columns (`points` and `price`) using Python libraries pandas and matplotlib. The goal is to understand the frequency distribution of wine scores and prices.

Tools Used
- Python
- pandas
- matplotlib

Part 1: Bar Chart of Wine Scores
- Used `value_counts()` to count wine review scores from the `points` column.
- Displayed results in a bar chart.
- Output: `plot_part1_score.png`
  
Part 2: Histogram of Wine Scores
- Created two histograms using the `points` column:
  - Bin size 10 → `plot_part2a_hist_bin10.png`
  - Bin size 3  → `plot_part2b_hist_bin3.png`

Part 3: Histogram of Wine Prices
- Dropped missing values (`NaN`) from the `price` column.
- Created histogram using bin size 5.
- Output: `plot_part3_price_bin5.png`

How to Run
1. Open terminal and navigate to the `PE04` folder.
2. Run the script:

bash
python pe04_wine_plots.py



COMMENTS FOR PE03

In this project, Python was used to scrape and organize data from a website. Using libraries like requests and BeautifulSoup, the titles and links from the Hacker News page were extracted and saved to a text file.
This task helps in understanding web scraping, and HTML parsing, as well as automating repetitive tasks with Python.
