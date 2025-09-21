print("script started")
# Assignment: Analyzing Data with Pandas & Matplotlib
# Student: Your Name
# -----------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    sns.set(style="whitegrid")  # nicer plots
    
    # ------------------------------
    # Task 1: Load and Explore Dataset
    # ------------------------------
    try:
        from sklearn.datasets import load_iris
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        print("✅ Dataset loaded successfully (Iris dataset).")
    except Exception as e:
        print("❌ Could not load dataset:", e)
        return

    # Show first few rows
    print("\n--- First 5 rows ---")
    print(df.head())

    # Show structure and missing values
    print("\n--- Dataset Info ---")
    print(df.info())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # ------------------------------
    # Task 2: Basic Data Analysis
    # ------------------------------
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # Mean, median, std
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print("\nMeans:\n", df[numeric_cols].mean())
    print("\nMedians:\n", df[numeric_cols].median())
    print("\nStandard Deviations:\n", df[numeric_cols].std())

    # Group by species
    grouped_means = df.groupby('species')[numeric_cols].mean()
    print("\n--- Mean values grouped by species ---")
    print(grouped_means)

    # ------------------------------
    # Task 3: Data Visualizations
    # ------------------------------

    # Line chart
    plt.figure(figsize=(9,5))
    for sp in df['species'].unique():
        subset = df[df['species'] == sp]
        plt.plot(subset.index, subset['sepal length (cm)'], label=sp)
    plt.title("Line Chart: Sepal Length by Sample Index")
    plt.xlabel("Sample Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.savefig("line_chart.png")
    plt.close()

    # Bar chart
    avg_petal_length = df.groupby('species')['petal length (cm)'].mean().sort_values()
    avg_petal_length.plot(kind='bar', color=['skyblue','orange','green'])
    plt.title("Bar Chart: Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.savefig("bar_chart.png")
    plt.close()

    # Histogram
    plt.hist(df['sepal length (cm)'], bins=12, color="purple", edgecolor="black")
    plt.title("Histogram: Sepal Length Distribution")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.close()

    # Scatter plot
    sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", s=60)
    plt.title("Scatter Plot: Sepal vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.savefig("scatter_plot.png")
    plt.close()

    print("\n✅ Visualizations saved as:")
    print("line_chart.png, bar_chart.png, histogram.png, scatter_plot.png")

    # ------------------------------
    # Findings / Observations
    # ------------------------------
    print("\n--- Observations ---")
    print("1. Setosa species has the smallest petal size, Virginica the largest.")
    print("2. Sepal length and petal length are positively correlated.")
    print("3. Histogram shows sepal length is mostly between 5-7 cm.")
    print("4. Scatter plot reveals clear separation of Setosa from the other species.")

if __name__ == "__main__":
    main()
