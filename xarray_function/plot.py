import xarray as xr
import numpy as np
import scipy
import xarray_function.wrapper as xrw
import matplotlib.pyplot as plt

def plotKDE(x1,x2,xmin=np.nan,xmax=np.nan,ymin=np.nan,ymax=np.nan,nb=100j,figsize=[10,7],**kwargs):
    
    if np.isnan(xmin):
        xmin=float(np.min(x1))
    if np.isnan(xmax):
        xmax=float(np.max(x1))
    if np.isnan(ymin):
        ymin=float(np.min(x2))
    if np.isnan(ymax):
        ymax=float(np.max(x2))
    
    kde=xrw.kde(x1,x2)
    
    X, Y = np.mgrid[xmin:xmax:nb, ymin:ymax:nb]
    positions = np.vstack([X.ravel(), Y.ravel()])
    Z = np.reshape(kde(positions).T, X.shape)
    
    fig, ax = plt.subplots()
    fig=ax.imshow(np.rot90(Z),extent=[xmin, xmax, ymin, ymax],**kwargs)
    ax.set_aspect(xmax/ymax)
    plt.xlabel(x1.name)
    plt.ylabel(x2.name)
    plt.colorbar(fig)
    
    return fig, ax