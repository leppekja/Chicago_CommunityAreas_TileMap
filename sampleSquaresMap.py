import altair as alt
import pandas as pd

def create_squares():
    return pd.read_csv("Chicago_Community_Areas_As_Squares.csv")

def plot_sample_variable(squares):
    return alt.Chart(squares, title="Sample Tile Map of Chicago's 77 Community Areas").mark_square(size=1500).encode(
                x=alt.X('x', axis=None),
                y=alt.Y('y', axis=None),
                color='POP_2020:Q',
                tooltip=["Name","GEOID", "POP_2020"]
            ).configure_view(width=450, height=600, strokeWidth=0).configure_axis(
                grid=False
            )

if __name__ == "__main__":
    squares = create_squares()
    chart = plot_sample_variable(squares)
    chart.save('chart.html', embed_options={'renderer':'svg'})

