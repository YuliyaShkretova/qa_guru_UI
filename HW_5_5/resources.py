from pathlib import Path

import HW_5_5
import basic_test
import form_fill_in


def image(file_name):
    return str(
        Path(HW_5_5.__file__).parent.joinpath(file_name).absolute()
    )


