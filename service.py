from pandas import DataFrame
from curves.repository import CurveRepository
from processing.smoothing import smooth_pD
from utils.get_model_params import MODEL_SPECS
from processing.bourdet_derivative import bourdet_derivative

'''
Module for retrieving PTA curves using analytical, interpolation, or ML methods.
'''

class PTACurveService:
    # Class variable to hold repositories for different model types
    _repos = {}

    def __init__(self, model_type, tD, inter_method = 'linear'):
        # Load model specifications. It includes curve path, parameters, and model info.
        self.spec = MODEL_SPECS[model_type]

        if model_type not in self._repos:
            self._repos[model_type] = CurveRepository(self.spec['curve_path'])

        # Assign the repository for the instance.
        self.repo = self._repos[model_type]
        self.tD = tD
        # Build interpolator
        self.interpolator = self.spec['interpolator'](self.repo.pre_computed_curves, self.tD, method=inter_method)
        

    def get_curve(self, **params):
        # First, try to get the analytical curve from the repository
        curve = self.repo.get(**params)
        if curve is not None:
            return curve, "analytical"
        
        # If not found, decide whether to use interpolation or ML model
        # check if params are between data in the curve
        check = [False if (params[key]<self.repo.pre_computed_curves[key].min() or 
                          params[key]>self.repo.pre_computed_curves[key].max()) 
                          else True 
                          for key in params.keys()]
        if all(check): # CAN USE INTERPOLATION
            pD = self.interpolator.interpolate_curve(**params)
            method = 'Interpolation'
        else: # USE ML MODEL
            raise NotImplementedError("ML model not implemented yet")
        
        # Smooth and compute derivative
        pD_smooth = smooth_pD(pD)
        dD = bourdet_derivative(self.tD, pD_smooth)

        curve = DataFrame({
            'tD': self.tD,
            'pD': pD_smooth,
            'dD': dD
        })
        return curve, method