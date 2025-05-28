import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_stacked_upright_pyramid(levels, colors, title="Pyramid", filename="pyramid.png", show_text=True):
    """
    Draws a clean, upright stacked pyramid with optional text.
    
    Args:
        levels (list): Labels for each level (from top to bottom).
        colors (list): Colors for each level.
        title (str): Title of the pyramid.
        filename (str): Output filename.
        show_text (bool): Whether to show text labels.
    """
    if len(levels) != len(colors):
        raise ValueError("levels and colors must be the same length")

    n = len(levels)
    fig, ax = plt.subplots(figsize=(6, n))
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(0, n)
    ax.axis('off')

    for i, (label, color) in enumerate(zip(reversed(levels), reversed(colors))):
        bottom_width = 1 - i * (1 / n)
        top_width = 1 - (i + 1) * (1 / n)
        y_bottom = i
        y_top = i + 1

        points = [
            [-bottom_width, y_bottom],
            [bottom_width, y_bottom],
            [top_width, y_top],
            [-top_width, y_top]
        ]
        # No border line
        trapezoid = Polygon(points, closed=True, facecolor=color, edgecolor=None, linewidth=0)
        ax.add_patch(trapezoid)

        if show_text:
            ax.text(
                0, (y_bottom + y_top) / 2, label,
                ha='center', va='center', fontsize=11, weight='bold',
                color='white' if i < n // 2 else 'black'
            )

    if title:
        plt.title(title, fontsize=14, weight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

# Example usage
levels = [
    "Level 4: Groundbreaking Scientific Contribution",
    "Level 3: Novel Scientific Contribution",
    "Level 2: SOTA Achievement",
    "Level 1: Baseline Improvement",
    "Level 0: Reproduction"
]
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#1abc9c']

draw_stacked_upright_pyramid(
    levels,
    colors,
    title="AI Research Agent Levels",
    filename="clean_pyramid.png",
    show_text=False  # Toggle this for minimal or labeled version
)
