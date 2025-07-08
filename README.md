# Comment Categorization & Reply Assistant Tool

## Problem Statement

This tool categorizes user comments  into one of eight categories: Praise, Support, Constructive Criticism, Hate, Threat, Emotional, Spam, or Question. It uses NLP to analyze comments and suggests appropriate response templates to help teams engage efficiently.

## Technologies Used

- **Python**: Core programming language
- **scikit-learn**: For SVM classifier and TF-IDF vectorization
- **NLTK**: For text preprocessing (tokenization, lemmatization, stopword removal)
- **Gradio**: For the web-based UI
- **pandas**: For dataset handling
- **matplotlib/seaborn**: For visualization

## Directory Structure

```
project/
├── data/                            
│   ├── comments_dataset.csv                      
│   ├── test.csv
├── app.py                   
├── data_loader.py           
├── model.py                 
├── response_templates.py      
├── text_preprocess.py
├── ui.py
├── README.md            
└── requirements.txt      
```

## How to Run

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**:

   ```bash
   python app.py
   ```

4. Open the Gradio interface URL (usually `http://127.0.0.1:7860`) in your browser.

5. Enter One or more comment in the text box (seperated by lines) to get its category, a suggested response, and a bar chart of category distribution.

6. You can also upload csv file containing the comments under the column name as "comment"

## Example Results

- Input: "Amazing work! Loved the animation."
  - Output: Category: Praise, Response: Thank you for the kind words!
- Input: "This is trash, quit now."
  - Output: Category: Hate, Response: We’re sorry you feel this way. Let us know how we can improve.

## Notes

- The dataset is manually created using AI with set of 500+ comments.
- The Gradio UI runs locally.

## Output Images

### Screenshot 1 (Single input)
![Screenshot 1](https://github.com/mdsadanfuzail/Comment-Categorization-and-Reply-Assistant-Tool/blob/main/output_images/Screenshot%201.png)

### Screenshot 2 (CSV file input)
![Screenshot 2](https://github.com/mdsadanfuzail/Comment-Categorization-and-Reply-Assistant-Tool/blob/main/output_images/Screenshot%202.png)