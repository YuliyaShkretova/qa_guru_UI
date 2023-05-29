
from pathlib import Path
import resource


def image(file_name):
    return str(
        Path(resource.__file__).parent.joinpath(file_name).absolute()
    )


