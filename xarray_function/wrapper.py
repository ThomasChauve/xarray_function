import xarray as xr
import numpy as np
import scipy

def kde(x1,x2,**kwargs):
    '''
    Wrapper for teh function scipy.stats,gaussian_kde
    '''
    
    x=np.ndarray.flatten(np.array(x1))
    y=np.ndarray.flatten(np.array(x2))
    
    return scipy.stats.gaussian_kde(np.vstack([x, y]))