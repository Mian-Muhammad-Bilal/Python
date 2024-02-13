import numpy as np

data = np.array([
    # [FREE,$,LENGTH,URGENT]
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0],
    [200, 10, 50, 1, 1],
    [1, 0, 15, 1110, 200],
    [30, 200, 205, 0, 10],
    [0, 30, 10, 1, 0]
])

weights = np.array([0.5, -0.2, 0.1, 0.3])
bias = 0.1
learning_rate = 0.5
itrations = 9

split_index = int(0.8 * len(data))
train_data, test_data = data[:split_index], data[split_index:]


def predict(features, weights, bias):
    # Calculate the weighted sum of inputs (x)
    activation = np.dot(features, weights) + bias

    # Output 1 if positive, -1 if negative
    return 1 if activation > 0 else 0  # Change from -1 to 0 for non-binary labels


def update_weights(features, label, weights, bias, learning_rate):
    # Update weights and bias for one itration
    prediction = predict(features, weights, bias)
    error = label - prediction

    weights += learning_rate * error * features
    bias += learning_rate * error

    return weights, bias


def train_perceptron(train_data, weights, bias, learning_rate, epochs):
    for epoch in range(epochs):
        for row in train_data:
            features = row[:-1]  # Exclude the label from features
            label = row[-1]

            weights, bias = update_weights(
                features, label, weights, bias, learning_rate)

    print(f"Itration {epoch + 1}: Weights = {weights}, Bias = {bias}")

    return weights, bias


def test_perceptron(test_data, weights, bias):
    correct_predictions = 0

    for row in test_data:
        features = row[:-1]
        label = row[-1]

        prediction = predict(features, weights, bias)

        if prediction == label:
            correct_predictions += 1

    return correct_predictions / len(test_data) * 100


weights, bias = train_perceptron(
    train_data, weights, bias, learning_rate, itrations)

accuracy = test_perceptron(test_data, weights, bias)
print(f"Accuracy: {accuracy:.2f}%")
