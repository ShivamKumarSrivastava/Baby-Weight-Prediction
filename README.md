# Baby-Weight-Prediction

# 👶 Baby Weight Prediction(OUNCES) - Flask App

This project is a **machine learning web application** that predicts the weight of a baby at birth based on various maternal factors such as:

- Mother's weight (pounds)
- Height (inches)
- Age
- Smoking status (0 - non smoker ) (1 - smoker)
- Other medical indicators

The backend is powered by a **trained regression model** using `scikit-learn`, with a `Flask` API that exposes a `/predict` endpoint for real-time predictions.

---

## 🛠️ Technologies Used

| Component      | Description                                      |
|----------------|--------------------------------------------------|
| Python         | Base programming language                        |
| Pandas         | Data loading, cleaning, and preprocessing        |
| Matplotlib     | Visualization and EDA                            |
| scikit-learn   | Model training, evaluation, and preprocessing    |
| Pickle         | Model serialization and deserialization          |
| Flask          | Web framework for building the REST API          |

---

## 🧠 ML Model

- A **regression model** (e.g., Linear Regression, Lasso, Ridge) trained on a dataset of maternal and baby health features.
- The model is saved using `pickle` and loaded during API inference.

---

## 📊 Features

- Maternal weight
- Maternal height
- Age of the mother
- Smoking status (binary)
- gestational weeks, etc.

---


