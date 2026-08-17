import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title('Probability of Successful Transmission')
    plt.xlabel('Num. Of Nodes')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    p = 0.7
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y = [(i * p * ((1 - p) ** (i - 1))) for i in x]
    print(y)
    draw_graph(x, y)