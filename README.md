# 🍽️ Naïve Bayes Review Sentiment Classification

<p align="center">
  <strong>Turning Customer Reviews into Meaningful Insights with Machine Learning</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/NLP-8A2BE2?style=for-the-badge" alt="NLP"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
</p>

## 📌 Project Overview

**Naïve Bayes Review Sentiment Classification** is a Natural Language Processing (NLP) and Machine Learning project that classifies customer reviews into **Positive** and **Negative** sentiments.

The project processes raw review text, converts words into numerical features, trains Naïve Bayes classifiers, and evaluates their performance. A Streamlit web application allows users to enter a new review and receive a predicted sentiment.

### 🎯 Project Objectives

- Explore and understand a customer review dataset.
- Clean and preprocess textual data.
- Convert text into numerical features using Bag of Words and TF-IDF.
- Train a Bernoulli Naïve Bayes classifier.
- Compare model performance using classification metrics.
- Predict sentiment for new customer reviews.
- Build and deploy an interactive Streamlit application.

## ✨ Key Features

- 🧹 **Text Preprocessing:** Lowercasing, punctuation and number removal, stopword removal, and lemmatization.
- 🔢 **Text Vectorization:** Binary Bag of Words and TF-IDF.
- 🧠 **Machine Learning:** Bernoulli Naïve Bayes and Multinomial Naïve Bayes.
- 📊 **Model Evaluation:** Accuracy, precision, recall, F1 score, and confusion matrix.
- 💬 **Sentiment Prediction:** Classifies new reviews as positive or negative.
- 🌐 **Interactive Web App:** A Streamlit interface for entering reviews and viewing predictions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Jupyter Notebook | Data exploration and model development |
| Pandas & NumPy | Data handling and processing |
| NLTK | Text preprocessing and lemmatization |
| Scikit-learn | Feature extraction, model training and evaluation |
| Matplotlib & Seaborn | Data visualization |
| Joblib | Saving and loading trained models |
| Streamlit | Interactive web application |
| Git & GitHub | Version control and project hosting |

## 📂 Project Workflow

```text
Customer Reviews Dataset
          |
          ▼
   Data Exploration
          |
          ▼
  Text Preprocessing
          |
          ▼
  Feature Extraction
   ┌──────┴───────┐
   ▼              ▼
Bag of Words    TF-IDF
   |              |
   ▼              ▼
BernoulliNB   MultinomialNB
   |              |
   └──────┬───────┘
          ▼
   Model Evaluation
          |
          ▼
 Sentiment Prediction
          |
          ▼
   Streamlit Web App
```

## 🔬 Machine Learning Models

### 1. Bernoulli Naïve Bayes

BernoulliNB is trained using binary Bag of Words features, representing whether a word is present or absent in a review.

### 2. Multinomial Naïve Bayes

MultinomialNB is trained using TF-IDF features as an additional model for comparison.

Both models are evaluated to understand their performance on the review classification task.

## 🧹 Text Preprocessing

The review text goes through the following steps:

1. Convert text to lowercase.
2. Remove numbers, punctuation, and special characters.
3. Remove unnecessary extra spaces.
4. Remove English stopwords while preserving important negation words such as `not`, `no`, and `nor`.
5. Apply lemmatization to reduce words to their base forms.

**Example:**

| Original Review | Example Cleaned Text |
|---|---|
| The food was fantastic! | food fantastic |
| The service was not good. | service not good |
| I loved the restaurant. | loved restaurant |

## 📊 Model Evaluation

The dataset is split into training and testing sets using an **80:20 ratio**.

The following metrics are used to evaluate the models:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted positive reviews that are actually positive.
- **Recall:** Proportion of actual positive reviews correctly identified.
- **F1 Score:** Harmonic mean of precision and recall.
- **Confusion Matrix:** Displays correct and incorrect predictions by class.

Actual evaluation results should be added here after running the notebook.

| Model | Feature Extraction | Accuracy |
|---|---|---|
| Bernoulli Naïve Bayes | Binary Bag of Words | Add measured result |
| Multinomial Naïve Bayes | TF-IDF | Add measured result |

## 💬 Sample Predictions

| Customer Review | Expected Sentiment |
|---|---|
| "The food was fantastic!" | Positive |
| "Worst service ever." | Negative |
| "The staff was friendly and helpful." | Positive |
| "The food was not good." | Negative |

*These are illustrative examples. Actual predictions depend on the trained model.*

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.10 or a compatible Python version
- Jupyter Notebook
- Visual Studio Code (optional)
- Git (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/Bidyashreepanda/Naive_Bayes_Project.git
```

### 2. Navigate to the Project Folder

```bash
cd Naive_Bayes_Project
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If the requirements file does not contain all the necessary packages, install them with:

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn nltk joblib streamlit
```

### 5. Run the Jupyter Notebook

Start Jupyter:

```bash
python -m pip install notebook
python -m notebook
```

Open the project notebook and run the cells in order to load the dataset, preprocess the reviews, train the model, evaluate its performance, and save the model.

### 6. Run the Streamlit Application

Ensure that `app.py` and the trained `sentiment_model.pkl` file are in the project directory.

Run:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the application.

> **Note:** The Streamlit application requires a previously trained and saved model. If `sentiment_model.pkl` is missing, train the model in the notebook and save the model and vectorizer before launching the app.

## 🌐 Streamlit Deployment

The application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

1. Push the required application files to GitHub.
2. Sign in to Streamlit Community Cloud using GitHub.
3. Create a new app and select this repository.
4. Select the correct branch and `app.py` as the entry point.
5. Deploy the application and test the public URL.

Ensure that the repository contains the required dependencies and model artifacts, and that the application can load them successfully.

**Live Demo:** Add your deployed Streamlit URL here once deployment is successful.

## 📁 Suggested Project Structure

```text
Naive_Bayes_Project/
│
├── app.py
├── requirements.txt
├── README.md
├── sentiment_model.pkl
├── Reviews_data.csv
└── Naive_Bayes_Review_Classification.ipynb
```

*The filenames above are suggested. Adjust them to match the actual files in your repository.*

## 🧠 Key Learnings

Through this project, I practiced:

- Exploratory Data Analysis (EDA).
- Text cleaning and preprocessing.
- Natural Language Processing fundamentals.
- Bag of Words and TF-IDF vectorization.
- Naïve Bayes classification.
- Model evaluation and comparison.
- Saving and loading machine learning models.
- Building and deploying a Streamlit application.

## 🔮 Future Improvements

- Compare additional classification algorithms such as Logistic Regression and Support Vector Machines.
- Improve preprocessing and handle negation, emojis, and spelling variations.
- Tune model hyperparameters.
- Add interactive charts and sentiment distribution analysis.
- Improve the application's interface and user experience.
- Evaluate the model on additional review datasets.

## 👩‍💻 Author

**Bidyashree Panda**

- GitHub: [@Bidyashreepanda](https://github.com/Bidyashreepanda)
- LinkedIn: [Bidyashree Panda](https://www.linkedin.com/in/bidyashree-panda/)

## ⭐ Support

If you find this project useful for learning Natural Language Processing and Machine Learning, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  <strong>Built with Python, Machine Learning, and NLP ❤️</strong>
</p>
