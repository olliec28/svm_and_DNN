import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the multiclass CSV file of channel state information
df_train = pd.read_csv('ol_ler_sit_stand_comb.csv')

# Perform pre-processing on the data
X_train = df_train.drop(columns=['activity'])
y_train = df_train['activity']

# Create a pipeline with StandardScaler and SVM
svm_pipeline = make_pipeline(StandardScaler(), SVC(decision_function_shape='ovr'))

# Train the SVM model on the pre-processed data
svm_pipeline.fit(X_train, y_train)

# Load the preprocessed CSV file for prediction
df_test = pd.read_csv('ol_sitting.csv')

# Perform pre-processing on the test data
X_test = df_test.drop(columns=['activity'])

# Use the trained SVM model to predict the target variable
y_pred = svm_pipeline.predict(X_test)

# Convert the predicted target variable to a string and save to a CSV file
df_pred = pd.DataFrame({'activity': y_pred.astype(str)})
df_pred.to_csv('predicted_data.csv', index=False)
