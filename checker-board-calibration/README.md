# 📸 Implementing Tsai’s Calibration and DLT for 3D Computer Vision 
### Put picture here 
A complete computer vision pipeline for monocular 3D reconstruction, utilizing Direct Linear Transformation (DLT) and Tsai’s Algorithm to map 2D pixels to 3D world coordinates.

### Overview
This project implements a monocular 3D reconstruction pipeline. It utilizes **Direct Linear Transformation (DLT)** and **Tsai’s Calibration** method to estimate camera parameters and project virtual 3D objects into a 2D scene.

This project bridges the gap between 2D image processing and 3D geometric modeling. By analyzing checkerboard patterns, we estimate the camera’s internal geometry (Intrinsic) and its position in space (Extrinsic).

The pipeline enables the projection of virtual objects into a real-world scene with high mathematical precision, a foundational technique for Augmented Reality (AR) and robotics.

### Objectives
Extract intrinsic camera parameters (K) and extrinsic pose (R,T).

Implement Direct Linear Transformation (DLT) for projection matrix estimation.

Decompose the projection matrix M using RQ Factorization.

Verify accuracy by rendering a 3D wireframe cube onto a 2D image plane.

Correct common geometric errors in world-frame camera positioning.

### Methodology
1. Checkerboard Calibration
The system uses a 9×6 checkerboard grid to establish correspondences between:

2D Image Points (p): Detected using OpenCV's findChessboardCorners with sub-pixel refinement.

3D World Points (P): Defined on a planar grid where Z=0.

2. The DLT Algorithm
We solve for the 3×4 projection matrix M by constructing the Q matrix and applying Singular Value Decomposition (SVD) to solve the homogeneous linear system:

p≈MP
3. Parameter Decomposition
Using RQ Factorization, we decompose M into:

Intrinsic Matrix (K): Focal length, principal point, and skew.

Extrinsic Rotation (R): Orientation of the camera.

Extrinsic Translation (T): Position relative to the world origin.

### Key Geometric Correction
A critical aspect of this project is the accurate calculation of the Camera Center (C) in world coordinates. As identified during validation, the center is not simply −T, but is calculated as:

$$
 C=−R^TT 
$$

## Key Implementation Details
- **Calibration:** Decomposes the projection matrix $M$ into Intrinsic ($K$) and Extrinsic ($R, T$) parameters.
- **Correction:** Implements the camera center calculation $C = -R^T T$ for accurate world-space positioning.
- **Projection:** Maps 3D cube vertices in the world frame back to image pixels using the computed projection matrix.

### 📊 Results
​
### paste picture here 


### Visualization
The pipeline successfully projects a 3D wireframe cube (1×1 world units) onto the checkerboard, maintaining perspective consistency even when the board is at an angle.


### Future Work
Radial Distortion Correction: Implementing Brown-Conrady models to fix lens warping.

Multi-View Stereo: Reconstructing 3D points from two or more calibrated camera views.

Real-time AR: Porting the DLT logic to a live video stream for real-time object overlay.

### 👥 Authors
Isabella Opoku-Ware