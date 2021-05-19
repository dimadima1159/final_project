    if ((np.abs(y0 - Y4) <= radius and (np.abs(x0 - X0) <= radius or np.abs(x0 - X1) <= radius)) 
    if ((np.abs(y0 - Y3) <= radius and (np.abs(x0 - X1) <= radius or np.abs(x0 - X2) <= radius))
    if ((np.abs(y0 - Y2) <= radius and (np.abs(x0 - X2) <= radius or np.abs(x0 - X3) <= radius))     
    if ((np.abs(y0 - Y1) <= radius and (np.abs(x0 - X3) <= radius or np.abs(x0 - X4) <= radius))
    if ((np.abs(y0 - Y0) <= radius and (np.abs(x0 - X4) <= radius or np.abs(x0 - X5) <= radius)): 
       vy0 = -vy0
        vx0 = -vx0
    if np.abs(x0 - X0) <= radius or np.abs(x0 - X5) <= radius:
        vx0 = -vx0
    if np.abs(y0 - Y0) <= radius or np.abs(y0 - Y5) <= radius:
        vy0 = -vy0
    s0 = x0, y0, vx0, vy0
