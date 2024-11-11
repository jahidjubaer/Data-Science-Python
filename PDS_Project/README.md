# MBTI Personality Prediction Model

## Project Overview

This project aims to predict an individual's **Myers-Briggs Type Indicator (MBTI)** personality type based on their text data, such as social media posts or written content. The model utilizes natural language processing (NLP) techniques and machine learning algorithms to classify text into 16 distinct MBTI personality types.

## Dataset

The project utilizes the "**Myers-Briggs Personality Type**" dataset, which contains a collection of personality types and their corresponding text data. This dataset is publicly available.

## Methodology

### 1. Data Preprocessing:
- **Removing URLs and special characters** from the text data.
- **Converting text to lowercase** for uniformity and consistency.

### 2. Feature Extraction:
- **TF-IDF (Term Frequency-Inverse Document Frequency):** This method is used to convert the text into numerical representations.
- **Truncated SVD (Singular Value Decomposition):** Dimensionality reduction is performed using Truncated SVD, selecting the top 100 features to improve model efficiency and accuracy.

### 3. Model Training:
- **ExtraTreesClassifier** with 100 estimators is used for classification.
- The model is trained on **80%** of the dataset, and **20%** is reserved for testing.

### 4. Evaluation:
- The model’s performance is evaluated using metrics like accuracy score and classification report.
- **Confusion matrix** visualization is used to display model predictions and evaluate classification results.

## Usage

To use the model for prediction, follow these steps:

### 1. **Input:**
   Provide a text sample as input to the `predict_personality` function.

### 2. **Preprocessing:**
   The function preprocesses the text, removing URLs, special characters, and converting it to lowercase for uniformity.

### 3. **Prediction:**
   The model predicts the MBTI personality type based on the processed text.

### 4. **Output:**
   The function will display:
   - The predicted MBTI type.
   - Detailed personality characteristics associated with each letter of the MBTI type.

---

## Example

You can test the model with a sample input. Here's an example of how to use it:

### Input: 

```python
# write your prompt 
sample_text = "I enjoy spending time alone, reflecting on my thoughts and ideas."
predicted_type = predict_personality(sample_text)

# Output
print("Predicted MBTI Type:", predicted_type)
```

### Output
```yaml
Predicted MBTI Type: INTP
Personality Characteristics:
- Introversion: Focused on inner thoughts and ideas rather than external stimulation.
- Intuition: Prefers abstract concepts and future possibilities.
- Thinking: Makes decisions based on logic and objective analysis.
- Perceiving: Prefers flexibility, spontaneity, and adaptability.
```

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request. We encourage collaboration and appreciate any feedback.

