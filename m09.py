
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


# STEP 1: Load the dataset
df = pd.read_csv("predictive_maintenance.csv")

print("Rows and columns:", df.shape)


# STEP 2: Clean the data
df = df.dropna(
    subset=["Rotational speed [rpm]", "Torque [Nm]"]
)


# STEP 3: Select input (X) and output (y)
X = df[["Rotational speed [rpm]"]]
y = df["Torque [Nm]"]


# STEP 4: Split the dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# STEP 5: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)


# STEP 6: Test the model
y_pred = model.predict(X_test)

print("R2 Score:", round(r2_score(y_test, y_pred), 3))

print(
    "Average Error:",
    round(mean_absolute_error(y_test, y_pred), 2),
    "Nm"
)

print("Slope (m):", round(model.coef_[0], 4))
print("Intercept (c):", round(model.intercept_, 2))


# STEP 7: Predict torque for a new rotational speed
new = pd.DataFrame({
    "Rotational speed [rpm]": [1800]
})

predicted_torque = model.predict(new)[0]

print(
    "Predicted torque at 1800 rpm:",
    round(predicted_torque, 2),
    "Nm"
)


# STEP 8: Plot the regression graph
line_x = pd.DataFrame({
    "Rotational speed [rpm]": sorted(
        X["Rotational speed [rpm]"]
    )
})

plt.scatter(
    X_test["Rotational speed [rpm]"],
    y_test,
    s=12,
    alpha=0.6,
    label="Actual (test data)"
)

plt.plot(
    line_x["Rotational speed [rpm]"],
    model.predict(line_x),
    color="red",
    label="Regression line"
)

plt.xlabel("Rotational speed (rpm)")
plt.ylabel("Torque (Nm)")
plt.title("Spindle Torque from Rotational Speed")

plt.legend()
plt.grid(True)
plt.show()
