This project focuses on predicting spindle torque (Nm) based on rotational speed (RPM) using Machine Learning. A Linear Regression algorithm is implemented using Python to identify the relationship between spindle rotational speed and torque.

The project uses a predictive maintenance dataset to train and test the model and predict torque values for new rotational speeds.
- Understand the relationship between rotational speed and torque.
- Apply Linear Regression for torque prediction.
- Evaluate model performance using statistical metrics.
- Explore Machine Learning applications in Mechanical Engineering and Predictive Maintenance.
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Linear Regression
Dataset Name: predictive_maintenance.csv

The dataset contains machine operating parameters, including:
- Rotational speed [rpm]
- Torque [Nm]
Missing values in the required columns are removed during data preprocessing.
1. Data Loading: Import the dataset using Pandas.
2. Data Preprocessing: Remove missing values from the rotational speed and torque columns.
3. Feature Selection: Select rotational speed as the input feature (X) and torque as the target variable (y).
4. Data Splitting: Divide the dataset into 80% training data and 20% testing data.
5. Model Training: Train the Linear Regression model using Scikit-learn.
6. Model Evaluation: Evaluate performance using R² Score and Mean Absolute Error (MAE).
7. Prediction: Predict spindle torque at a new rotational speed of 1800 RPM.
8. Visualization: Plot actual test values and the regression line using Matplotlib.
- R² Score: Measures how well the model explains the variation in torque.
- Mean Absolute Error (MAE): Measures the average absolute difference between actual and predicted torque values.
- Slope (m): Represents the change in predicted torque for a unit increase in rotational speed.
- Intercept (c): Represents the predicted torque when rotational speed is zero.
```
Spindle-Torque-Prediction-ML/
│
├── predictive_maintenance.csv
├── spindle_torque_prediction.py
└── README.md
```
Step 1: Clone the repository.
```
git clone <your-repository-url>
```
Step 2: Install the required libraries.
```
pip install pandas matplotlib scikit-learn
```
Step 3: Ensure the dataset predictive_maintenance.csv is available in the project folder.

Step 4: Run the Python program.
```
python spindle_torque_prediction.py
```
The program displays:
- Dataset row and column count.
- R² Score.
- Mean Absolute Error.
- Regression slope and intercept.
- Predicted torque at 1800 RPM.
- Graph showing actual torque values and the regression line.
- Spindle performance analysis.
- Machine condition monitoring.
- Predictive maintenance.
- Manufacturing process analysis.
- Data-driven machine performance prediction.
This project demonstrates how Machine Learning techniques can be applied to Mechanical Engineering problems. Linear Regression provides a basic approach to understanding the relationship between spindle rotational speed and torque and predicting torque values from the given dataset.
