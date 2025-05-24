PE07
Overview
This project explores the Iris dataset using three classic machine learning techniques:
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Feature selection and data split experiments

It is divided into 3 main problems, with visualizations and performance comparisons.

Problem 1 – Parameter Variation
I experimented with different values for:
- `max_depth` in Decision Tree
- `k` in KNN

 Both models reached perfect accuracy at certain settings, but Decision Tree showed signs of overfitting when depth increased.

Two accuracy plots were generated:  
- Accuracy by `max_depth` (Decision Tree)  
- Accuracy by `k` (KNN)

---

#Problem 2 – Feature Combination Analysis
Using different combinations of the 4 Iris features (sepal/petal length/width), we tested how the feature set affects accuracy.

Key insights:
- Petal width alone performed very well.
- More features didn’t always mean better performance.
- Some two-feature combinations performed as well as all four.

A horizontal bar chart displays KNN accuracy by feature combination.

---

Problem 3 – Training Size Impact
We tested model accuracy using different training sizes: 10% to 90%.

Findings:
- Accuracy improves as training size increases.
- Around 70%-90% training data was enough to reach 100% accuracy with Decision Tree.

A line chart visualizes accuracy growth with training size.
