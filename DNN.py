import pandas as pd
import tensorflow as tf

# Load preprocessed training CSV file
train_df = pd.read_csv('ol_ler_sit_stand_comb.csv')

# Load test CSV file for prediction
test_df = pd.read_csv('ol_standing.csv')

# Map label values to integer values
label_map = {label: i for i, label in enumerate(set(train_df['activity']))}
train_df['activity'] = train_df['activity'].map(label_map)
test_df['activity'] = test_df['activity'].map(label_map)

# Split training data into features and labels
X_train = train_df.drop('activity', axis=1).values
y_train = train_df['activity'].values

# Split test data into features and labels
X_test = test_df.drop('activity', axis=1).values
y_test = test_df['activity'].values

# Define number of classes
num_classes = len(set(y_train))

# Define model architecture with dropout and softmax output
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(100, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          activity_regularizer=tf.keras.regularizers.l1(0.01)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(100, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          activity_regularizer=tf.keras.regularizers.l1(0.01)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Define optimizer with Stochastic Gradient Descent
optimizer = tf.keras.optimizers.SGD(learning_rate=1e-5)

# Compile model
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=15, batch_size=32, validation_split=0.2)

# Predict on test data and convert label integers back to original string labels
y_pred = model.predict(X_test)
pred_labels = [list(label_map.keys())[list(label_map.values()).index(pred)] for pred in y_pred.argmax(axis=1)]

# Create dataframe of predicted labels and write to CSV file
pred_df = pd.DataFrame({'predicted_activity': pred_labels})
pred_df.to_csv('predicted_labels_olstand.csv', index=False)
