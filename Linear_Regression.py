import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = 0
        self.b = 0

    def fit(self, X, y):
        n = len(X)

        for _ in range(self.epochs):
            y_pred = self.w * X + self.b

            dw = (1/n) * np.sum((y_pred - y) * X)
            db = (1/n) * np.sum(y_pred - y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):
        return self.w * X + self.b


# Example
X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)
print(model.predict(X))
