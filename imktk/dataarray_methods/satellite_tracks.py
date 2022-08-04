#!/usr/bin/env python
# coding: utf-8
"""
Interpolation routine to satellite tracks

This script helps calculating interpolations along satellite tracks.
"""
import xarray as xr


def main(dataarray):
    """Interpolation routine to satellite tracks

    This script helps calculating interpolations along satellite tracks.

    Arguments
    =========
    dataarray: <Description>
    argument1: <Description>
    ...
    argumentX: <Description>

    Returns
    =======
    dataarray: <Description>
    """
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"

    # add data processing code here

    return dataarray
