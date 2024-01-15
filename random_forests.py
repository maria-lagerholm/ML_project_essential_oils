import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import learning_curve


HYPERPARAMETERS = {'warm_start': False, 'n_estimators': 50, 'min_weight_fraction_leaf': 0.0, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_leaf_nodes': 2, 'max_features': 'sqrt', 'max_depth': 12, 'criterion': 'entropy', 'ccp_alpha': 0.01, 'bootstrap': False}

# Function to calculate TNR (True Negative Rate)
def true_negative_rate(cm):
    tn, fp, _, _ = cm.ravel()
    return tn / (tn + fp) if (tn + fp) != 0 else 0

# Function to calculate and append metrics
def calculate_metrics(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    metrics = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'F1 Score': f1_score(y_true, y_pred),
        'True Positive Rate': recall_score(y_true, y_pred),
        'True Negative Rate': true_negative_rate(cm)
    }
    return metrics


# Function to plot learning curve
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

# Function to plot confusion matrix
def plot_confusion_matrix(cm, classes, title='Confusion Matrix'):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title(title)
    plt.show()
    




# Load the dataset
data = pd.read_csv('aggregated_plants.csv')

# Define the feature set and target variable
features = data[[col for col in data.columns if col.startswith('Bit_')]]
target = data['Candida albicans']







# Initialize StratifiedKFold
skf = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)

# Initialize an empty DataFrame for metrics
metrics_list = []

# Define class labels for the confusion matrix
class_labels = ['Class 0', 'Class 1']



best_model = None
best_score = 0
best_cm = None
best_test_set = None


# Perform cross-validation
for fold, (train_index, test_index) in enumerate(skf.split(features, target), start=1):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = target.iloc[train_index], target.iloc[test_index]

    # Initialize and train the RandomForestClassifier
    model = RandomForestClassifier(**HYPERPARAMETERS, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    # Calculate metrics for training and test sets
    train_metrics = calculate_metrics(y_train, train_predictions)
    test_metrics = calculate_metrics(y_test, test_predictions)

    # Record metrics for each fold
    metrics_list.append({
        'Fold': fold,
        'Dataset': 'Train',
        **train_metrics
    })

    metrics_list.append({
        'Fold': fold,
        'Dataset': 'Test',
        **test_metrics
    })


    # Evaluate the model (using F1 score or another metric)
    test_f1 = f1_score(y_test, test_predictions)

    # If this model is the best so far, store it and its confusion matrix
    if test_f1 > best_score:
        best_model = model
        best_score = test_f1
        best_cm = confusion_matrix(y_test, test_predictions)
        best_test_set = (y_test, test_predictions)
# Plot confusion matrix for the best model
if best_model is not None:
    plot_confusion_matrix(best_cm, classes=class_labels, title='Best Model - Test Set Confusion Matrix')

# Create a DataFrame from the list of metrics
metrics_df = pd.DataFrame(metrics_list)

# Reformat DataFrame for better readability
metrics_df = metrics_df.round(2)  # Round to two decimal places for readability



# Create DataFrames for average train and test metrics
average_train_metrics_df = pd.DataFrame([average_train_metrics_all_folds], columns=metrics_df.columns)
average_train_metrics_df['Fold'] = 'Average (All Folds)'
average_train_metrics_df['Dataset'] = 'Train'

average_test_metrics_df = pd.DataFrame([average_test_metrics_all_folds], columns=metrics_df.columns)
average_test_metrics_df['Fold'] = 'Average (All Folds)'
average_test_metrics_df['Dataset'] = 'Test'

# Concatenate the DataFrames to add average metrics
metrics_df = pd.concat([metrics_df, average_train_metrics_df, average_test_metrics_df])



# Save the metrics to a CSV file
metrics_df.to_csv('classification_metrics_output.csv', index=False)

# Display the DataFrame with average rows for all folds
print(metrics_df)


# Plot learning curve for the best model
title = "Learning Curves (Best model of CV=5, Random Forest)"
plot_learning_curve(best_model, title, X, y, cv=skf, n_jobs=-1)
plt.show()
