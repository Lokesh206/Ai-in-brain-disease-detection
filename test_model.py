import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

img = nib.load("BraTS20_Training_003/BraTS20_Training_003_flair.nii")
data = img.get_fdata()

mask = nib.load("BraTS20_Training_003/BraTS20_Training_003_seg.nii")
mask_data = mask.get_fdata()

slice_index = data.shape[2] // 2

mri_slice = data[:, :, slice_index]
mask_slice = mask_data[:, :, slice_index]

plt.imshow(mri_slice, cmap="gray")
plt.imshow(mask_slice, cmap="jet", alpha=0.5)

plt.title("MRI with Tumor Highlight")
plt.axis("off")

plt.savefig("static/result.png")
plt.close()