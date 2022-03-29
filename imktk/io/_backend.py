"""
Backend module to extend xarray with custom readers as described
[here](https://xarray.pydata.org/en/stable/internals/how-to-add-new-backend.html)

This module enables a new backend for xarray which can be used via

``` python
xr.open_dataset(filename_or_obj, engine='imktk', mode='reader')
```

where `reader` defines the function to be used.
This could also be automated using
[`guess_can_open`](https://xarray.pydata.org/en/stable/internals/how-to-add-new-backend.html#guess-can-open) but that is for later.
"""
from xarray.backends import BackendEntrypoint
from ._reader import READERS


class ImktkBackendEntrypoint(BackendEntrypoint):
    open_dataset_parameters = ["filename_or_obj", "drop_variables", "mode"]

    def open_dataset(self, filename_or_obj, mode, *, drop_variables=None):
        print(f"Using imktk reader in mode {mode} on {filename_or_obj}")
        return READERS[mode.lower()](filename_or_obj, drop_variables=drop_variables)
