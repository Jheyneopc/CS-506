from sklearn import  datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
#-----------------------------------------------------------------------------------------------------------------------
# Problem 2: The data contains 4 different features namely sepal length, sepal width, petal length, and petal width
# It is important to recognize which feature set(s) performs the best. Choose the best combination based on your
# experiment. You will have 10 different combinations possible (e.g. {SL, SW, PL, PW, (SL,SW), (SL, PL)...(SL, SW, PL, PW)} 
# You will show different performance after based on the best training parameters from Problem #1.
# This may show that the more number of features doesn't end up with better accuracy necessarily. 
# You will have the performance results per 10 combinations and plot the results on a graph for each classifier.
# with your analysis in words.
# Refer to the topic in the "curse of dimensionality"
# Resource : https://en.wikipedia.org/wiki/Curse_of_dimensionality
#-----------------------------------------------------------------------------------------------------------------------

x=iris.data   # data that contains 4 features of 150 samples. 
y=iris.target # labels with ground truth information

# split the data into split% training and (100-split)% testing
split = 0.9

#-----------------------------------------------------------------------------------------
# Problem 3: Once you decide the best feature set(s) from the Problem #2, it is important to recognize 
# how the size of training set versus testing set (or ratio between sets) would influence the
# overall representative performance. You will have the performance results per 10%, 20% ... 90% and plot
# the results on a graph for each classifier with your analysis in words.
#-----------------------------------------------------------------------------------------
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=split)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#-----------------------------------------------------------------------------------------
# Problem 1: Write a program such that different training variables
# such as "mxdepth" for DecisionTreeClassifier and "k" for KNN classifier 
# can have consecutive values being experimented. For example, rewrite the
# following code so that mxdepth starts from 1 to 10 or k goes from 1 to 10
# You will need to plot the accuracy per varying these parameters of each classifier 
# with your analysis in words
#-----------------------------------------------------------------------------------------
# Resource:
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
# A decision tree classifier. Training parameter is mxdepth
mxdepth = 1
classifier1 = DecisionTreeClassifier(max_depth=mxdepth)
classifier1.fit(x_train,y_train)
predictions=classifier1.predict(x_test)
print(f"DTC ({mxdepth}) = %0.2f accuracy" % accuracy_score(y_test,predictions))

# Resource:
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# Finds the K-neighbors of a point. Returns indices of and distances to the neighbors of each point.
# Training parameter is k
k = 1
classifier2 = KNeighborsClassifier(n_neighbors=k)
classifier2.fit(x_train,y_train)
predictions=classifier2.predict(x_test)
print(f"KNN ({k}) = %0.2f accuracy" % accuracy_score(y_test,predictions))


#Problems Resulution below: 

# PE07- Iris Dataset Analysis with Visualizations

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import itertools

# Load Iris data
iris = datasets.load_iris()
x = iris.data
y = iris.target

# --------------------------------------------------------------------------------------------------------
# Problem 1 – Varying Parameters

print("DTC (1) = %.2f accuracy" % accuracy_score(y, DecisionTreeClassifier(max_depth=1).fit(x, y).predict(x)))
print("KNN (1) = %.2f accuracy" % accuracy_score(y, KNeighborsClassifier(n_neighbors=1).fit(x, y).predict(x)))

# Use consistent training/testing split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

print("\nDecision Tree Classifier results (varying max_depth):")
dt_scores = []
for depth in range(1, 11):
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(x_train, y_train)
    acc = accuracy_score(y_test, model.predict(x_test))
    dt_scores.append(acc)
    print(f"max_depth = {depth} -> Accuracy = {acc:.2f}")

print("\nK-Nearest Neighbors results (varying k):")
knn_scores = []
for k in range(1, 11):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    acc = accuracy_score(y_test, model.predict(x_test))
    knn_scores.append(acc)
    print(f"k = {k} -> Accuracy = {acc:.2f}")

# Plot Problem 1 results
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), dt_scores, marker='o')
plt.title("Decision Tree Accuracy by max_depth")
plt.xlabel("max_depth")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), knn_scores, marker='s', color='green')
plt.title("KNN Accuracy by k")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# Problem 2 – Feature Combinations

features = [0, 1, 2, 3]
combinations = []
for r in range(1, 5):
    combinations.extend(itertools.combinations(features, r))

feature_labels = []
combo_scores = []

print("\nKNN classifier results using different feature combinations:")
for combo in combinations:
    x_subset = x[:, combo]
    x_train, x_test, y_train, y_test = train_test_split(x_subset, y, test_size=0.1, random_state=42)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    acc = accuracy_score(y_test, model.predict(x_test))
    feature_labels.append(str(combo))
    combo_scores.append(acc)
    print(f"Features {combo} -> Accuracy = {acc:.2f}")

# Plot Problem 2 results
plt.figure(figsize=(10, 6))
plt.barh(feature_labels, combo_scores, color='skyblue')
plt.title("KNN Accuracy by Feature Combination")
plt.xlabel("Accuracy")
plt.ylabel("Feature Combination")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------------------------------
# Problem 3 – Training Size Effect

train_sizes = []
accuracies = []

print("\nDecision Tree Classifier results with varying training sizes:")
for percent in range(1, 10):
    train_size = percent / 10
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_size, random_state=42)
    model = DecisionTreeClassifier(max_depth=3)
    model.fit(x_train, y_train)
    acc = accuracy_score(y_test, model.predict(x_test))
    train_sizes.append(int(train_size * 100))
    accuracies.append(acc)
    print(f"Training Size = {int(train_size * 100)}% -> Accuracy = {acc:.2f}")

# Plot Problem 3 results
plt.figure(figsize=(8, 5))
plt.plot(train_sizes, accuracies, marker='^', color='orange')
plt.title("Decision Tree Accuracy by Training Set Size")
plt.xlabel("Training Set Size (%)")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()
