from random_data import RandomData
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

if __name__ == '__main__':

    # Create some random data
    num = 500
    data1 = RandomData(num).create_data()
    data2 = RandomData(num).create_data()

    # Get some colors for the data
    colors = RandomData(num).color_labels()

    # Construct the colormap
    current_palette = sns.color_palette("muted", n_colors=5)
    cmap = ListedColormap(sns.color_palette(current_palette).as_hex())

    # Create a scatter plot
    plt.title("Cool Random Plot")
    plt.scatter(data1, data2, c=colors, cmap=cmap)

    # Add a color bar
    plt.colorbar()

    # Show/save the plot
    # plt.show()
    plt.savefig('random_plot.png')

    print("Plot created!")
