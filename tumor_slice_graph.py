import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the MRI file
file_path = os.path.join(base_dir, "BraTS20_Training_004_t2.nii")

# Check if file exists
if not os.path.exists(file_path):
    print("Error: File not found ->", file_path)
    exit()

# Load MRI file
img = nib.load(file_path)
data = img.get_fdata()

# Total number of slices in MRI
num_slices = data.shape[2]

slice_index = []
ground_truth_area = []
prediction_area = []

for i in range(num_slices):

    slice_data = data[:, :, i]

    # Ground truth tumor pixels
    tumor_pixels = np.sum(slice_data > 0)
    ground_truth_area.append(int(tumor_pixels))

    # Simulated prediction values
    predicted_pixels = tumor_pixels * np.random.uniform(0.8, 1.2)
    prediction_area.append(int(predicted_pixels))

    slice_index.append(i)

# Plot graph
plt.figure(figsize=(10,5))

plt.plot(slice_index, ground_truth_area, label="Ground Truth", color="blue")
plt.plot(slice_index, prediction_area, label="Prediction", color="red")

plt.title("Tumor Area per MRI Slice")
plt.xlabel("Slice Index")
plt.ylabel("Tumor Area (pixels)")

plt.legend()
plt.grid(True)

plt.show()