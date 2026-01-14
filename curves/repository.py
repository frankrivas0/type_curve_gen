import numpy as np
import pandas as pd

'''
Module for retrieving pre-computed curves from CSV files.
'''
# think i dont need a module here, just a function.

class CurveRepository:
    def __init__(self, csv_path):
        self.pre_computed_curves = pd.read_csv(csv_path)

    def get(self, **params):
        """
        Retrieve analytical curve for a single model DB.
        """
        # Check that parameters exist
        for key in params:
            if key not in self.pre_computed_curves.columns:
                raise KeyError(f"Parameter '{key}' not found in model")

        mask = self.pre_computed_curves[list(params)].eq(pd.Series(params)).all(axis=1)
        curve = self.pre_computed_curves.loc[mask, ['tD', 'pD', 'dD']]

        if curve.empty:
            return None

        return curve