class DynamicTanh(...):
    def __init__(...):
        ...

    def forward(self, x):
        # Apply dynamic tanh transformation
        x = torch.tanh(self.alpha * x)
        if self.channels_last:
            return self.weight * x + self.bias
        else:
            return x * self.weight + self.bias