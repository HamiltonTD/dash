import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region== 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Dashboard"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(
                    children="🥑",
                    className="header-emoji"
                       ),
                html.H1(
                    children="Avocado Analytics",
                    className="header-title",
                ),
                html.P(
                    children="Analyzing avocado prices",
                    className="header-description"
                ),
            ],
            className="header"
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.2f}"
                                    "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
        ),
    ],
)
                
                
if __name__ == "__main__":
    app.run_server(debug=True)

