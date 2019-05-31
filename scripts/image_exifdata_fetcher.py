#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
image_exifdata_fetcher
"""


import os as _os
import click as _click

import app.image_exifdata_fetcher as _app


def validate(ctx, param, value):
    """
    Validation of input file
    """
    if param.name == "path":
        if not _os.path.isfile(value):
            print("File {value} not found".format(value=value))
            ctx.exit()
        elif not _os.access(value, _os.R_OK):
            print("Permission denied for {value}".format(value=value))
            ctx.exit()
    elif param.name == "outfile":
        if not value.endswith(".kml"):
            print(
                "{value} is not allowed. Default is set: {param}".format(
                    value=value,
                    param=param.default,
                ),
            )
            value = param.default

    return value


@_click.command()
@_click.option("--path", "-p", required=True, callback=validate)
@_click.option("--outfile", "-o", required=True, default="data/exif_data.kml", callback=validate)
def cli(path, outfile):
    """
    Client
    """
    print(path)
    print(outfile)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
