# Real-Time Depth Estimation with MiDaS 📸

## 📄 Project Overview

  This real-time depth estimation system processes live video feeds, generating depth maps using MiDaS with PyTorch and OpenCV. It’s suitable for applications like robotics, AR/VR, and          autonomous systems, showcasing the power of AI in visualizing spatial depth.

## ✨ Features

 - Real-Time Processing: Converts live video frames into depth maps with minimal latency.
 - Depth Visualization: Generates high-quality depth maps for various applications.
 - Easy Integration: Compatible with any real-time video feed, customizable for different use cases.

## ⚙️ Setup

Clone the repository and install dependencies:

bash

    pip install torch opencv-python
Download MiDaS model weights and save them in <code>models/</code>.

## 🚀 Usage

Start the depth estimation system:

bash

    python depth_estimation.py

## 🎥 Output

Generated depth maps will be displayed live. Screenshots are saved in the <code>output/</code> directory.


this repo contains an midascv.py file which  helps to identify the real time moment of the person or an individual and plot its graph simultaneously in real time.
