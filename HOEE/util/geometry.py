import numpy as np

def area_hexagon(D):
    """
    Computes the collecting area of a hexagon.

    Parameters
    ----------
    D : float
        Diameter of the circumscribed circle [m]
        or equivalently, the distance between opposite vertices of the hexagon [m]

    Returns
    -------
    A_collect : float
        Collecting area of the hexagonal aperture [m^2]
    """
    A_collect = (3 * np.sqrt(3) / 2) * (D/2)**2
    return A_collect