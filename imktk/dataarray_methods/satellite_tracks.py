#!/usr/bin/env python
# coding: utf-8
"""
Interpolation routine to satellite tracks

This script helps calculating interpolations along satellite tracks.

Usage:

    ```python
    import imktk

    da = imktk.tutorial.open_dataset("sat")
    dims = dict(lat = [1.1,2.4], lon = [.21,.35])
    da.imktk.satellite_tracks(**dims)
    ```
"""
import xarray as xr


def main(dataarray, name=None, method="linear", **dims):
    """Interpolation routine to satellite tracks

    This script helps calculating interpolations along satellite tracks.

    Arguments
    =========
    dataarray: xr.DataArray to be mapped on the Satellite tracks
    name: Name of satellite
    method: Interpolation method to be used
    dims: Dictionary of coord and list of values

    Returns
    =======
    result: xr.DataArray of interpolated values to satellite track
    """
    # check if first argument is a dataarray
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"

    # check if dims dictionary fits to the dataarray, based on ...
    msg = f"Some dim keys of {dims.keys()} not found in {list(dataarray.coords)}"
    # ... all keys are valid coordinate dimensions
    assert all([x in dataarray.coords for x in dims.keys()]), msg
    # ... satellite tracks are lists
    assert all([isinstance(x, list) for x in dims.values()]), "Dimension values are not lists"
    # ... all satellite tracks are the same length
    lengths = [len(x) for x in dims.values()]
    assert all([x == lengths[0] for x in lengths]), "Not all dims are of same length"

    if not name:
        name = "satellite"
    criteria = {k: xr.DataArray(v, dims=name) for k, v in dims.items()}

    return dataarray.interp(**criteria, method=method)
