# What is a neural network?

A neural network is a machine-learning model made of connected computational units, often called neurons, arranged in layers. The structure is loosely inspired by biological nervous systems, but artificial neurons are mathematical functions rather than realistic brain cells.

## Basic structure

- **Input layer:** receives the input features.
- **Hidden layers:** transform information using learned weights, biases, and activation functions.
- **Output layer:** produces a prediction, score, or generated representation.

## How learning works

During training, a model makes predictions and compares them with target values using a loss function. An optimization algorithm updates the model parameters, commonly using gradients computed by backpropagation. Repeated training can reduce the loss on the training data, but does not guarantee good performance on new data.

## Common applications

Neural networks are used in image recognition, speech processing, language modeling, recommendation systems, forecasting, and many other tasks.

## Important cautions

A neural network is not automatically accurate, unbiased, explainable, or safe. Evaluation should use data representative of the intended use, with checks for overfitting, data leakage, fairness, robustness, and privacy.
