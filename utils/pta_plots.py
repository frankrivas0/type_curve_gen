import plotly.graph_objects as go

def plot_pta_combined(df, curve_source):
    fig = go.Figure()

    # Pressure curve
    fig.add_trace(
        go.Scatter(
            x=df["tD"],
            y=df["pD"],
            mode="lines",
            name="pD",
            line=dict(color="green", width=2)
        )
    )

    # Bourdet derivative
    fig.add_trace(
        go.Scatter(
            x=df["tD"],
            y=df["dD"],
            mode="lines",
            name="Bourdet",
            line=dict(color="red", width=2, dash="dash")
        )
    )

    fig.update_layout(
        # Axes
        xaxis=dict(
            title="t<sub>D</sub>",
            type="log",
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=0.5,
            zeroline=False,
            ticks="inside",
            tickwidth=1,
            ticklen=6,
            minor=dict(
                ticks="inside",
                ticklen=4,
                showgrid=True
            ),
            exponentformat = "power"
        ),
        yaxis=dict(
            title="p<sub>D</sub> and dp<sub>D</sub>/d ln t",
            type="log",
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=0.5,
            zeroline=False,
            ticks="inside",
            tickwidth=1,
            ticklen=6,
            minor=dict(
                ticks="inside",
                ticklen=4,
                showgrid=True
            ),
            exponentformat = "power"
        ),

        # Layout
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Times New Roman, serif",
            size=13,
            color="black"
        ),
        height=600,

        legend=dict(
            title=dict(
                text=f'Curve source: {curve_source}'
            ),
            orientation="h",
            y=1.05,
            x=0.5,
            xanchor="center",
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(l=80, r=80, t=40, b=60)
    )

    return fig