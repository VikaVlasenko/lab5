import matplotlib.pyplot as plt
from algorithms import sutherland_cohen
import sys

def load_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        segments = []
        for i in range(1, n + 1):
            x1, y1, x2, y2 = map(int, lines[i].strip().split())
            segments.append(((x1, y1), (x2, y2)))
        xmin, ymin, xmax, ymax = map(int, lines[n + 1].strip().split())
    return segments, (xmin, ymin, xmax, ymax)

def main():
    if len(sys.argv) != 2:
        
        print("Использование: python main.py <путь_к_файлу>")
        return

    file_path = sys.argv[1]
    segments, window = load_file(file_path)

    fig, ax = plt.subplots()
    ax.grid(True)
    ax.set_aspect('equal')

    ax.plot([window[0], window[2], window[2], window[0], window[0]], [window[1], window[1], window[3], window[3], window[1]], 'b-')
    for segment in segments:
        ax.plot([segment[0][0], segment[1][0]], [segment[0][1], segment[1][1]], 'r-')

    clipped_segments = []
    for segment in segments:
        clipped_segment = sutherland_cohen(segment, window)
        if clipped_segment:
            clipped_segments.append(clipped_segment)

    for segment in clipped_segments:
        ax.plot([segment[0][0], segment[1][0]], [segment[0][1], segment[1][1]], 'g-')

    plt.show()

if __name__ == "__main__":
    main()