import nibabel as nib
import matplotlib.pyplot as plt

img = nib.load("BraTS20_Training_003/BraTS20_Training_003_flair.nii")

data = img.get_fdata()

slice = data[:, :, data.shape[2]//2]

plt.imshow(slice, cmap="gray")
plt.title("Brain MRI")
plt.axis("off")
plt.show()