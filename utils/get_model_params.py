import streamlit as st
from interpolation.interpolation import HomogeneousInfiniteInterpolator, DualPorosityInterpolator, HomogeneousBoundedInterpolator
from utils.model_descriptions import descriptions

MODEL_SPECS = {
    'Homogeneous_infinite': {
        'interpolator': HomogeneousInfiniteInterpolator,
        'curve_path': 'data/homogeneous_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)'},
        'model_description': descriptions['Homogeneous_infinite']
    },
    'Homogeneous_Closed_Circular': {
        'interpolator': HomogeneousBoundedInterpolator,
        'curve_path': 'data/closed_circle_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)', 'rb': 'Dimensionless Reservoir Radius (reD)'},
        'model_description': descriptions['Homogeneous_Closed_Circular']
    },
    'Homogeneous_Constant_Pressure_Circular': {
        'interpolator': HomogeneousBoundedInterpolator,
        'curve_path': 'data/constant_pressure_circle_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)', 'rb': 'Dimensionless Reservoir Radius (reD)'},
        'model_description': descriptions['Homogeneous_Constant_Pressure_Circular']
    },
    'Dual_porosity_PSS': {
        'interpolator': DualPorosityInterpolator,
        'curve_path': 'data/dual_porosity_pss_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)',
                   'omega': 'Storativity Coefficient (ω)', 'lam': 'Interporosity Flow Coefficient (λ)'},
        'model_description': descriptions['Dual_porosity_PSS']
    },
    'Dual_porosity_transient_sphere': {
        'interpolator': DualPorosityInterpolator,
        'curve_path': 'data/dual_porosity_transient_sphere_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)',
                   'omega': 'Storativity Coefficient (ω)', 'lam': 'Interporosity Flow Coefficient (λ)'},
        'model_description': descriptions['Dual_porosity_sphere']
    },
    'Dual_porosity_transient_slab': {
        'interpolator': DualPorosityInterpolator,
        'curve_path': 'data/dual_porosity_transient_slab_type_curves.csv',
        'params': {'CD': 'Dimensionless Wellbore Storage Coefficient (CD)', 's': 'Skin Factor (s)',
                   'omega': 'Storativity Coefficient (ω)', 'lam': 'Interporosity Flow Coefficient (λ)'},
        'model_description': descriptions['Dual_porosity_slab']
    }

}


@st.cache_data
def get_model_params(model, df):
    spec = MODEL_SPECS[model]

    params = {}
    for param, label in spec['params'].items():
        params[param] = {
            'Name': label,
            'min': float(df[param].min()),
            'max': float(df[param].max()),
        }

    return params