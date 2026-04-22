import numpy as np
import scipy.linalg as linalg

def calibrate_camera_tsai(p, P):
    """
    p : pixel coordinates (3 x n)
    P : world coordinates (4 x n)
    Returns: K (Intrinsic), R (Rotation), T (Translation), M (Projection Matrix)
    """
    n = p.shape[1]
    p_uv = p[0:2,:] / p[2,:]

    # Build Q matrix for DLT
    Q = np.empty((0, 12))
    for i in range(n):
        Qi_0 = np.array([[1, 0, -p_uv[0,i]], [0, 1, -p_uv[1,i]]])
        Qi = np.kron(Qi_0, P[:,i].T)
        Q = np.append(Q, Qi, axis=0)

    # SVD to find Projection Matrix M
    _, _, VT = linalg.svd(Q)
    M = VT.T[:, -1].reshape(3, 4)

    # RQ Factorization for K and R
    K, R = linalg.rq(M[:, 0:3])
    
    # Sign correction to ensure positive focal length
    T_sign = np.diag(np.sign(np.diag(K)))
    K = K @ T_sign
    R = T_sign @ R
    
    # Normalize K and find T
    T = linalg.inv(K) @ M[:, 3].reshape(3, 1)
    K = K / K[2,2]
    
    return K, R, T, M

def get_corrected_camera_center(R, T):
    """
    Calculates the camera center in world coordinates.
    Formula: C = -R.T @ T
    """
    return -R.T @ T