""" IO Module for different reading methods
"""
import xarray as xr
import tempfile
import glob
import os


def mean_merge_files_with_data_dump(fl, output, chunksize=100, keep_attrs=True, parallel=True, dim="lon", keep_dims=True):
    if fl is None or not fl:
        print("No files.")
        return
    xr.set_options(keep_attrs=keep_attrs)

    with tempfile.TemporaryDirectory() as tmpdirname:
        print(f"created temporary directory: {tmpdirname}")

        # processing each chunk
        for i in range(0, len(fl), chunksize):
            subset = fl[i : i + chunksize]
            data = xr.open_mfdataset(subset, parallel=parallel).mean(dim=dim, keepdims=keep_dims)
            tfilename = os.path.join(tmpdirname, f"temporary_{i}.nc")
            data.to_netcdf(tfilename)
            print(f"Saved chunk {i}:{i+chunksize} to {tfilename}")
        print("Done processing chunks")

        # merging all temporary chunks
        tfiles = os.path.join(tmpdirname, "temporary_*.nc")
        merged_ds = xr.open_mfdataset(tfiles)
        merged_ds.to_netcdf(output)
        print(f"Saved all files to {output}")


def main():
    ws = "/hkfs/work/workspace/scratch/mu5263-esmart/v0/"
    fl = sorted(glob.glob(ws + "atm_esmart_atm_3d_reg_pl_*.nc"))
    output = "merged.nc"
    mean_merge_files_with_data_dump(fl=fl, output=output)


if __name__ == "__main__":
    main()
