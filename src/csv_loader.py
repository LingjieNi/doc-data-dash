import pandas as pd
import numpy as np
from pathlib import Path

from dataclasses import dataclass


class CSV:
    """Class for CSV file
    """
    loc: Path
    def load_csv(loc:Path):
        """read csv file

        :param loc: location of file
        :type loc: Path
        :return: csv file in pandas dataframe
        :rtype: pd.Dataframe

        Usage:
        
        .. doctest::

            >>> print("load csv")
        
        """
        return pd.read_csv(loc)


@dataclass
class Benchmark:
    """benchmark about

    With :class:`CSV`

    .. note::

        With :class:`CSV`
        time
    """
    id : str
    

if __name__ == "__main__":
    print("test doc data dash")