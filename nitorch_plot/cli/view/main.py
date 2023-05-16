from nitorch_plot import ImageViewer
import matplotlib.pyplot as plt


def view(files):
    """Interactive viewer for volumetric images.

    Parameters
    ----------
    files : list[str]
        Inputs images.

    """
    if plt is None:
        raise ImportError('Matplotlib not available')

    ImageViewer(files)
    plt.show(block=True)
