# Celebal Internship Assignments

This repository contains weekly assignments completed as part of my Data Science Internship at **Celebal Technologies**.

---

## Week 1: Pattern Generator
**Task**: Create different triangle patterns using `*`  
- Lower Triangular Pattern  
- Upper Triangular Pattern  
- Center-Aligned Pyramid

File: `assignment_1.py`

---

## Week 2: Singly Linked List using OOP
**Task**: Implement a singly linked list using OOP in Python with:
- `Node` and `LinkedList` classes
- Append nodes, print the list
- Delete the nth node with exception handling

File: `assignment_2.py`

---

## Week 3: Data Visualization  
**Task**: Visualize the Netflix Movies & TV Shows dataset using matplotlib/seaborn.  
File: `assignment_3.ipynb`

---

## Week 4: In-depth Exploratory Data Analysis (Titanic Dataset)
**Task**: Conduct a detailed EDA covering:
- Missing value detection
- Outlier identification
- Distributions & relationships between features

**Visualizations**:  
- Heatmap of missing values  
- Histograms and box plots for key numerical features  
- Correlation heatmap  

Files:  
- `titanic.csv` (raw dataset)  
- `assignment_4.ipynb` (notebook with code, charts, and insights)

---

### Week 5 – House Price Prediction (📈 Current Task)  
**Task**: Build a preprocessing and feature-engineering pipeline for the Kaggle “House Prices – Advanced Regression Techniques” dataset, including:  
- Missing-value imputation  
- Outlier removal & skewness correction  
- Engineered features: total square footage, bathrooms, binary flags  
- Preprocessing pipeline with scaling and one-hot encoding  
**File** (added):    
- `assignment_5.ipynb` 

---

### Week 6 – Model Evaluation & Hyperparameter Tuning 

**Task**: Train multiple classification models and identify the best one through systematic evaluation and hyperparameter optimization.

- Implement **RandomForest**, **SVM**, and **GradientBoosting** classifiers.
- Use **GridSearchCV** (and optionally **RandomizedSearchCV**) for tuning key hyperparameters like `n_estimators`, `max_depth`, `C`, `kernel`, `learning_rate`, etc.
- Evaluate models via **accuracy**, **precision**, **recall**, **F1-score**, and **classification report**.
- Compile a comparison table to select the top-performing model.

**Resources**:
- KDnuggets guide on hyperparameter tuning with GridSearchCV & RandomizedSearchCV :contentReference[oaicite:1]{index=1}

**File**:
- `assignment_6.py` – Full script:
  - Loads dataset (e.g. Wine dataset)
  - Splits data (train/test)
  - Defines models & hyperparameter grids
  - Runs GridSearchCV (and RandomizedSearchCV for SVM)
  - Evaluates and prints classification reports
  - Summarizes results in a DataFrame

---

## Week 7: Deploying Machine Learning Model using Streamlit  
**Task**: Build an interactive web app using Streamlit to serve a trained machine learning model.  
- Train and save a `RandomForestClassifier` on the Iris dataset  
- Create a user-friendly Streamlit interface with sliders  
- Load the model and show real-time predictions  
- Add clear UI and feedback for predicted class  

📄 **Files**:  
- `model_trainer(week-7).py` – trains and saves the model  
- `app(week-7).py` – Streamlit app  
- `requirements(week-7).txt` – dependencies for setup  

---  


More weekly tasks will be added as the internship progresses.
