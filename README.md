````markdown
# Iris Dataset Analysis with Pandas & Matplotlib

## 📌 Overview
This project analyzes the famous **Iris dataset** using Python libraries such as **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.  
It covers:
- Loading and exploring the dataset  
- Performing basic descriptive statistics  
- Creating visualizations  
- Highlighting key observations  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Noela6344/iris_analysis.git
   cd iris_analysis
````

2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Run the script:

   ```bash
   python iris_analysis.py
   ```

---

## 📊 Features

* **Data Loading**: Loads Iris dataset from `sklearn.datasets` into a DataFrame.
* **Exploration**: Displays first rows, dataset info, missing values, and summary statistics.
* **Analysis**: Calculates mean, median, standard deviation, and group statistics by species.
* **Visualizations**: Saves the following plots:

  * `line_chart.png` → Sepal length by sample index
  * `bar_chart.png` → Average petal length by species
  * `histogram.png` → Sepal length distribution
  * `scatter_plot.png` → Sepal vs Petal length by species
* **Findings**:

  * Setosa has the smallest petals, Virginica the largest.
  * Sepal length and petal length are positively correlated.
  * Sepal length is mostly between 5–7 cm.
  * Scatter plot shows Setosa clearly separated from others.

---

## 📂 Project Structure

```
iris_analysis/
│-- iris_analysis.py
│-- line_chart.png
│-- bar_chart.png
│-- histogram.png
│-- scatter_plot.png
│-- README.md
```

---

## 🛠️ Requirements

* Python 3.8+
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn

Install all at once:

```bash
pip install -r requirements.txt
```

---

