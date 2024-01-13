import micrograd as mg

# Generate some synthetic data
np.random.seed(42)
X = mg.tensor(np.random.rand(100, 1))
y = 3 * X + 2 + 0.1 * mg.randn(100, 1)

# Define a simple linear regression model
class LinearRegressionModel:
    def __init__(self, in_features, out_features):
        self.W = mg.Parameter(mg.randn(in_features, out_features))
        self.b = mg.Parameter(mg.randn(out_features))

    def __call__(self, x):
        return x @ self.W + self.b

# Mean Squared Error (MSE) loss
def mse_loss(pred, target):
    return mg.mean((pred - target) ** 2)

# Train the model using gradient descent
def train(model, inputs, targets, epochs=100, learning_rate=0.01):
    for epoch in range(epochs):
        pred = model(inputs)
        loss = mse_loss(pred, targets)
        loss.backward()

        # Gradient descent update
        for param in model.parameters():
            param.data -= learning_rate * param.grad

        model.zero_grad()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.data}")

# Instantiate the model and train it
model = LinearRegressionModel(1, 1)
train(model, X, y)

# Print the learned parameters
print("Learned parameters:")
print("W:", model.W.data.item())
print("b:", model.b.data.item())
