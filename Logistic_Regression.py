import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = 0
        self.b = 0

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        n = len(X)

        for _ in range(self.epochs):
            z = self.w * X + self.b
            y_pred = self.sigmoid(z)

            dw = (1/n) * np.sum((y_pred - y) * X)
            db = (1/n) * np.sum(y_pred - y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X, threshold=0.5):
        z = self.w * X + self.b
        y_pred = self.sigmoid(z)
        return (y_pred >= threshold).astype(int)


# Example
X = np.array([1, 2, 3, 4])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)
print(model.predict(X))
