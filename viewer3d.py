import plotly.graph_objects as go
import nibabel as nib
import numpy as np

# Load MRI
img = nib.load("BraTS20_Training_003/BraTS20_Training_003_flair.nii")
data = img.get_fdata()

# Load tumor segmentation
mask = nib.load("BraTS20_Training_003/BraTS20_Training_003_seg.nii")
mask_data = mask.get_fdata()

# Downsample (important for speed)
data = data[::4, ::4, ::4]
mask_data = mask_data[::4, ::4, ::4]

# Normalize MRI
data = (data - data.min()) / (data.max() - data.min())

# Grid
x, y, z = np.mgrid[
    0:data.shape[0],
    0:data.shape[1],
    0:data.shape[2]
]

# Brain volume
brain = go.Volume(
    x=x.flatten(),
    y=y.flatten(),
    z=z.flatten(),
    value=data.flatten(),
    opacity=0.1,
    surface_count=10,
    colorscale="Gray",
    showscale=False
)

# Tumor surface
tumor = go.Isosurface(
    x=x.flatten(),
    y=y.flatten(),
    z=z.flatten(),
    value=mask_data.flatten(),
    isomin=1,
    isomax=4,
    opacity=0.6,
    surface_count=3,
    colorscale="Reds",
    name="Tumor"
)

fig = go.Figure(data=[brain, tumor])

fig.update_layout(title="3D Brain MRI with Tumor")
fig.write_html("static/brain3d.html")
fig.show()