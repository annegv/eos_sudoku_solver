import matplotlib.pyplot as plt

# Read the loss values from the log file
losses = []
with open("training_loss_log.txt", "r") as f:
    for line in f:
        # Extract the number after 'Loss:'
        parts = line.strip().split("Loss:")
        if len(parts) == 2:
            loss_value = float(parts[1])
            losses.append(loss_value)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(losses, label='Training Loss')
plt.xlabel("Iteration (Batch)")
plt.ylabel("Loss")
plt.title("Training Loss Over Iterations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("training_loss_plot.png", dpi=300)