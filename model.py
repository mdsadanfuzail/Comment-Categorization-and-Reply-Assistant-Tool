import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from response_templates import RESPONSE_TEMPLATES
from text_preprocess import preprocess_text


def train_model(df):
    # Preprocess comments
    df['processed_comment'] = df['comment'].apply(preprocess_text)
    
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SVC(kernel='linear', probability=True))
    ])
    
    model.fit(df['processed_comment'], df['category'])
    return model

def predict_and_visualize(comments, model):
    if isinstance(comments, str):
        comments = [comments]
    elif isinstance(comments, list):
        comments = [c.strip() for c in comments if c.strip()]

    # Preprocess
    processed_comments = [preprocess_text(c) for c in comments]
    
    predictions = model.predict(processed_comments)
    probabilities = model.predict_proba(processed_comments)

    results = []
    for comment, pred in zip(comments, predictions):
        response = RESPONSE_TEMPLATES.get(pred, "Thank you for your feedback.")
        results.append({
            'Comment': comment,
            'Category': pred,
            'Suggested Response': response
        })

    # Plot distribution
    categories = model.classes_
    pred_counts = [predictions.tolist().count(cat) for cat in categories]

    fig, ax = plt.subplots()
    ax.bar(categories, pred_counts)
    ax.set_title('Comment Category Distribution')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    return pd.DataFrame(results), fig

