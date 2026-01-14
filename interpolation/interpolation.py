import numpy as np
from abc import ABC, abstractmethod
from scipy.interpolate import RegularGridInterpolator

class Interpolator(ABC):
    def __init__(self, df_raw, tD, method='linear'):
        self.df_raw = df_raw.copy()
        self.tD = tD
        self.method = method
        self.param_keys = self.df_raw.columns.drop(['tD', 'pD', 'dD']).to_list()
        self.interpolator = self.build_interpolator()

    def build_interpolator(self):
        curve = self.build_interpolator_features()  # THIS IS THE MODIFIED DATAFRAME WITH NEW FEATURES BUT SAME COLUMN NAMES
        unique_values = []
        shape = []
        for param_key in self.param_keys:
            val = curve[param_key].unique()
            unique_values.append(val) # [np.array[cd, cd, ...], np.array[s, s, ...], ...]
            shape.append(len(val)) # [shape CD, shape s, ..., shape tD]
                
        shape.append(len(self.tD))   
        # pD_values[i, j, .., k] is the curve corresponding to the values CD[i], s[j], ..., param[k]
        pD_values = np.log10(curve['pD'].to_numpy().reshape(tuple(shape)))
        interpolator = RegularGridInterpolator(tuple(unique_values), pD_values, method=self.method)
        return interpolator

    @abstractmethod
    def build_interpolator_features(self):
        raise NotImplementedError
    
    @abstractmethod
    def modify_params(self, **params):
        raise NotImplementedError

    def interpolate_curve(self, **params):
        mod_params_sorted = self.modify_params(**params)
        pD = self.interpolator(tuple(mod_params_sorted.values()))
        return 10**pD

class HomogeneousInfiniteInterpolator(Interpolator):
    def __init__(self, df_raw, tD, method='linear'):
        super().__init__(df_raw, tD, method)

    def build_interpolator_features(self):
        curve = self.df_raw.copy()
        curve['CD'] = np.log10(curve['CD'])
        return curve
    
    def modify_params(self, **params):
        params['CD'] = np.log10(params['CD'])
        mod_params_sorted = {key: params[key] for key in self.param_keys}
        return mod_params_sorted

class HomogeneousBoundedInterpolator(Interpolator):
    def __init__(self, df_raw, tD, method='linear'):
        super().__init__(df_raw, tD, method)

    def build_interpolator_features(self):
        curve = self.df_raw.copy()
        curve['CD'] = np.log10(curve['CD'])
        curve['rb'] = np.log10(curve['rb'])
        return curve
    
    def modify_params(self, **params):
        params['CD'] = np.log10(params['CD'])
        params['rb'] = np.log10(params['rb'])
        mod_params_sorted = {key: params[key] for key in self.param_keys}
        return mod_params_sorted

class DualPorosityInterpolator(Interpolator):
    def __init__(self, df_raw, tD, method='linear'):
        super().__init__(df_raw, tD, method)

    def build_interpolator_features(self):
        curve = self.df_raw.copy()
        curve['CD'] = np.log10(curve['CD'])
        #curve['omega'] = np.log10(curve['omega'])
        curve['lam'] = np.log10(curve['lam'])
        return curve
    
    def modify_params(self, **params):
        params['CD'] = np.log10(params['CD'])
        #params['omega'] = np.log10(params['omega'])
        params['lam'] = np.log10(params['lam'])
        mod_params_sorted = {key: params[key] for key in self.param_keys}
        return mod_params_sorted
        
        

