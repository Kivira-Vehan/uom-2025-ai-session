**Machine Learning Lifecycle**

Machine Learning Lifecycle is a structured process for developing, deploying, and maintaining ML models, ensuring accuracy, reliability, and scalability.

By following this lifecycle, we can:
-Define objectives, scope, and success criteria for clear project direction.
-Collect diverse, sufficient datasets from reliable sources.
-Clean and preprocess data, handling issues like missing values and outliers.
-Analyze data using statistics and visualizations to uncover insights.
-Engineer features and select relevant attributes for better model performance.
-Train models, compare options, and select the best one.
-Evaluate on unseen data, optimize, and measure performance.
-Deploy models into production and monitor for drift, retraining as needed.


### Data Processing

#### Data Cleaning
-Raw Daat: initial data collected from various sources. Log files, audio/video, image, text file, etc
-Goal: make that raw data accurate, consistant, free of errors, and usuable for analysis.

##### How to clean data
1.Remove duplications
2.Remove unwanted observations
3.Handdle missing values
4.Manage outliers

##### Data Formatting
-Converting your input data into standard formats or structures that can be easily processed by machine learning algorithms.
-In our case, we go through scaling, normalization, encoding categorical variables (One Hot Encoding), etc.

1.Min Max Scaling
    -Rescales features to a fixed range, usually 0 to 1.
    -Formula: X_scaled = (X - X_min) / (X_max - X_min)

2.Standardization (Z-score Normalization)
    -Centers the feature by subtracting the mean and scaling to unit variance.
    -Formula: X_standardized = (X - μ) / σ
