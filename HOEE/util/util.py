import numpy as np
import astropy.units as u

def sep_to_lamD(sep, D, lam):
    """
    Convert a separation in arcseconds to lambda / D units.

    Parameters
    ----------
    sep : float or astropy.units.Quantity
        Separation (assumed mas).
    diam : float or astropy.units.Quantity
        Diameter of the telescope (assumed m).
    lam : float or astropy.units.Quantity
        Wavelength (assumed nm).

    Returns
    -------
    float
        Separation in lambda / D units.
    """

    if not isinstance(sep, u.Quantity):
        sep = sep * u.mas
    
    if not isinstance(D, u.Quantity):
        D = D * u.m
    
    if not isinstance(lam, u.Quantity):
        lam = lam * u.nm

    # Convert separation from milliarcseconds to radians
    sep_rad = sep.to(u.rad).value

    # Calculate lambda / D
    lam_D = lam / D

    # Convert separation to lambda / D units
    sep_lam_D = sep_rad / lam_D.decompose().value

    return sep_lam_D

def lamD_to_sep(lamD, D, lam):
    """
    Convert a separation in lambda / D units to mas.

    Parameters
    ----------
    lamD : float
        Separation in lambda / D units.
    diam : float or astropy.units.Quantity
        Diameter of the telescope (assumed m).
    lam : float or astropy.units.Quantity
        Wavelength (assumed nm).

    Returns
    -------
    astropy.units.Quantity
        Separation in mas.
    """

    if not isinstance(D, u.Quantity):
        D = D * u.m
    
    if not isinstance(lam, u.Quantity):
        lam = lam * u.nm

    # Calculate lambda / D
    lam_D = lam / D

    # Convert separation from lambda / D units to radians
    sep_rad = lamD * lam_D.decompose().value

    # Convert separation from radians to arcseconds
    sep_arcsec = (sep_rad * u.rad).to(u.mas)

    return sep_arcsec.value