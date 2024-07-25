


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(frames, labels, test_size=0.2, random_state=42)
cnn_model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)








