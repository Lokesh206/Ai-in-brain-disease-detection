🧠 2D Medical Scan Analysis to 3D Reconstruction

A research-based project that analyzes 2D medical scan slices (MRI, CT, and other imaging modalities) and reconstructs them into a 3D anatomical model.
The system also identifies potential infection or abnormal regions and highlights them using a unique spatial detection method.

📌 Overview
Medical imaging data is usually stored as multiple 2D slices. Understanding the spatial relationship between these slices can be difficult.

This project creates a pipeline that:

Processes 2D medical scan slices
Performs image preprocessing and segmentation
Reconstructs the slices into a 3D volumetric model
Detects infected or abnormal regions
Marks the infection using a unique 3D localization technique
The goal is to help visualize medical data in 3D space for easier analysis.

🚀 Features
📂 Supports multiple scan types

MRI
CT Scan
Other 2D medical image slices
🧹 Image Preprocessing

Noise reduction
Contrast enhancement
Normalization
🧠 Infection Detection

AI/ML-based anomaly detection
Tissue segmentation
Pattern recognition
🏗 3D Reconstruction

Converts stacked 2D slices into volumetric 3D data
Surface / voxel rendering
🎯 Unique Infection Localization

Voxel anomaly detection
Spatial clustering of infected tissue
3D coordinate tagging of infection regions
🖥 3D Visualization

Interactive model rotation
Infection heatmap
Slice-by-slice inspection
🏗 System Architecture
2D Medical Scans (MRI / CT Slices)
          │
          ▼
   Image Preprocessing
 (Noise removal, filtering)
          │
          ▼
      Segmentation
 (Separating tissue regions)
          │
          ▼
   Infection Detection
 (AI / anomaly detection)
          │
          ▼
     3D Reconstruction
 (Stacking slices → volume)
          │
          ▼
  Infection Localization
 (Voxel clustering + tagging)
          │
          ▼
   Interactive 3D Visualization
🧪 Tech Stack
Category	Tools
Language	Python
Image Processing	OpenCV, scikit-image
Medical Imaging	NiBabel, SimpleITK
Machine Learning	PyTorch / TensorFlow
3D Visualization	VTK, PyVista
Data Visualization	Matplotlib, Plotly
📂 Project Structure
medical-3d-reconstruction
│
├── data
│   ├── raw_scans
│   └── processed_scans
│
├── preprocessing
│   ├── preprocess.py
│   └── noise_removal.py
│
├── segmentation
│   └── tissue_segmentation.py
│
├── detection
│   └── infection_detection_model.py
│
├── reconstruction
│   └── build_3d_model.py
│
├── visualization
│   └── render_3d.py
│
├── models
│
├── notebooks
│
└── README.md
⚙ Installation
Clone the repository:

git clone https://github.com/yourusername/medical-3d-reconstruction.git
cd medical-3d-reconstruction
Install dependencies:

pip install -r requirements.txt
▶ Usage
1️⃣ Place scan slices in:

data/raw_scans/
Example:

slice_001.png
slice_002.png
slice_003.png
2️⃣ Run preprocessing

python preprocessing/preprocess.py
3️⃣ Detect infection regions

python detection/infection_detection_model.py
4️⃣ Generate 3D model

python reconstruction/build_3d_model.py
5️⃣ Visualize results

python visualization/render_3d.py
🎯 Unique Infection Detection Method
This project uses a 3-stage approach:

1️⃣ Intensity Anomaly Detection
Detect abnormal tissue regions based on pixel intensity variation.

2️⃣ Spatial Voxel Clustering
Groups nearby abnormal voxels into clusters representing possible infection zones.

3️⃣ 3D Coordinate Tagging
Each infection cluster is tagged with 3D spatial coordinates and highlighted in the reconstructed model.

This allows precise identification of infection areas in 3D space.

📊 Future Improvements
3D CNN based infection detection
U-Net segmentation model
Real-time rendering
Web-based visualization dashboard
Integration with medical dataset
