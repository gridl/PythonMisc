from bokeh.io import output_file, show
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

import pandas as pd

def plotthis():
    map_options = GMapOptions(lat=67.97, lng=-97.73, map_type="roadmap", zoom=2)

    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Runners IOS"
    )

    df = pd.read_csv("runners.csv")
    df = df.dropna()
    df = df.head(500)
    source = ColumnDataSource( data=dict(lat=df["start_latitude"],lon=df["start_longitude"],))


    #source = ColumnDataSource( data=dict(lat=[30.29, 30.20, 30.29],lon=[-97.70, -97.74, -97.78],))

    circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
    plot.add_glyph(source, circle)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    output_file("gmap_plot.html")
    show(plot)

def testimpala():
    from impala.dbapi import connect
    import os
    import pandas as pd
    import numpy as np
    pd.set_option('display.max_columns', 500)
    conn = connect(host="10.184.193.2", port=21050, auth_mechanism="GSSAPI")
    # %time pd.read_sql("show databases",conn)
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_style('whitegrid')


if __name__ == "__main__":
    plotthis()
    #testimpala()