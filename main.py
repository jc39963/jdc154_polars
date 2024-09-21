"""Code to look at Netflix Movie and Show rating trends"""

import polars as pl
import matplotlib.pyplot as plt


def generate_summary_stats(filename):
    """Generate summary stats of data"""
    data = pl.read_csv(filename)
    return data["release_year"].describe()


def clean_ratings(data):
    """Cleans up rating column of data"""
    data = data.filter(pl.col("rating") != "74 min")
    data = data.filter(pl.col("rating") != "84 min")
    data = data.filter(pl.col("rating") != "66 min")
    return data


def years_and_ratings(data):
    """Looks at the number of films released per rating"""
    return data.group_by("rating").agg([pl.mean("release_year")])


def years_ratings_trends(data):
    """Looks at number of films released per year with each rating"""
    return (
        data.group_by(["release_year", "rating"])
        .agg(pl.len().alias("count"))
        .pivot(index="release_year", on="rating", values="count")
        .fill_null(0)
    )


def plot_trends(data, category):
    """Plots the number of films released per year with each rating"""
    release_years = data["release_year"].to_numpy()
    ratings = data.columns[1:]  # Skip the first column ('release_year')

    # Convert Polars DataFrame to numpy array (counts of each rating)
    cat_numpy = data.drop("release_year").to_numpy()

    # Plotting the stacked bar chart
    axis = plt.subplots(figsize=(10, 6))[1]
    bottom = None  # To stack the bars

    # Loop through each rating and plot stacked bars
    for i, rating in enumerate(ratings):
        counts = cat_numpy[:, i]  # Get the count for each rating
        axis.bar(release_years, counts, bottom=bottom, label=rating)
        if bottom is None:
            bottom = counts  # Initialize bottom with the first bar
        else:
            bottom += counts  # Stack bars

    # Add labels and title
    axis.set_xlabel("Year")
    axis.set_ylabel("Count")
    axis.set_title(f"{category} Ratings over the Years")
    axis.legend(title="Rating")
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = pl.read_csv("netflix_titles.csv")
    movies = df.filter(pl.col("type") == "Movie")
    shows = df.filter(pl.col("type") == "TV Show")
    generate_summary_stats("netflix_titles.csv")
    clean_ratings(df)
    print("Ratings types:", df["rating"].value_counts())
    movie_years_and_ratings = years_and_ratings(movies)
    print("Movie years and ratings:", movie_years_and_ratings)
    shows_years_and_ratings = years_and_ratings(shows)
    print("Shows years and ratings:", shows_years_and_ratings)
    movie_trends = years_ratings_trends(movies)
    shows_trends = years_ratings_trends(shows)
    plot_trends(movie_trends, "Movie")
    plot_trends(shows_trends, "Shows")
