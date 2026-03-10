import matplotlib.pyplot as plt

# Epoch numbers
epochs = [1,2,3,4,5]

# Training accuracy
train_acc = [0.60,0.72,0.81,0.88,0.93]

# Validation accuracy
val_acc = [0.58,0.70,0.78,0.84,0.90]

plt.plot(epochs, train_acc, label="Training Accuracy")
plt.plot(epochs, val_acc, label="Validation Accuracy")

plt.title("Brain Tumor Detection Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.legend()   # shows labels
plt.grid()

plt.show()