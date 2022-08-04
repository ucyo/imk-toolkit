#!/usr/bin/env python
# coding: utf-8
"""
Interpolation routine to satellite tracks

This script helps calculating interpolations along satellite tracks.
"""
import xarray as xr


def main(dataarray, lat, lon, name=None):
    """Interpolation routine to satellite tracks

    This script helps calculating interpolations along satellite tracks.

    Arguments
    =========
    dataarray: xr.DataArray to be mapped on the Satellite tracks
    lat: List of latitude values
    lon: List of longitude values
    name: Name of satellite

    Returns
    =======
    result: xr.DataArray of interpolated values to satellite track
    """
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    assert isinstance(lat, list), "Latitude is not a list"
    assert isinstance(lon, list), "Longitude is not a list"
    assert len(lon) == len(lat), f"Longitude and Latitute lists are not of same length {len(lon)} != {len(lat)}"
    assert "lat" in dataarray.data_coords, f"Lat(itute) not found in {dataarray.data_coords}"
    assert "lon" in dataarray.data_coords, f"Lon(gitude) not found in {dataarray.data_coords}"

    if not name:
        name = "satellite"
    lon = xr.DataArray(lon, dims=name)
    lat = xr.DataArray(lat, dims=name)

    return dataarray.sel(lon=lon, lat=lat)
