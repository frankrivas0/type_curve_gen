import streamlit as st
from utils.get_model_params import MODEL_SPECS, get_model_params
from utils.pta_plots import plot_pta_combined
from service import PTACurveService
from numpy import logspace, log10

app_title = 'Type Curve Generator'

st.set_page_config(page_title=app_title, page_icon=":chart_with_upwards_trend:", layout='wide')
tD = logspace(-2, 9, 100)

st.sidebar.markdown("## Set model and parameters")


select_model = st.sidebar.selectbox('Choose a model to start', list(MODEL_SPECS.keys()), format_func=lambda x: x.replace("_", " "))

@st.cache_data(max_entries=5)
def model_creation_wrapper(model, tD, inter_method='linear'):
    return PTACurveService(model, tD, inter_method)

model_creation = model_creation_wrapper(select_model, tD, inter_method='linear')

st.markdown(MODEL_SPECS[select_model]['model_description'], unsafe_allow_html=True)
st.sidebar.text("Use the sliders to change the model parameters.")
param_specs = get_model_params(select_model, model_creation.repo.pre_computed_curves)

# SIDEBAR FOR PARAMETER SELECTION
# Create a slider for each parameter. Log scale for all except 's'.
params = {}
for p, cfg in param_specs.items():
    if p == 's':
        params[p] = st.sidebar.slider(
            cfg['Name'],
            min_value=cfg['min'],
            max_value=cfg['max'],
            value=cfg['min'],
            step=0.5
        )
    else:
        params[p] = st.sidebar.slider(
            cfg['Name'],
            min_value=log10(cfg['min']),
            max_value=log10(cfg['max']),
            value=log10(cfg['min']),
            format = "10^%.2f",
            step=0.1
        )

# Convert back from log scale except 's'.
for p in params.keys():
    if p != 's':
        params[p] = 10**params[p]
        

# GENERATE RESULTS GIVEN THE MODEL AND PARAMETERS
table, curve_source = model_creation.get_curve(**params)

# LOG-LOG PLOT tD vs pD, dD
st.plotly_chart(plot_pta_combined(table, curve_source), use_container_width=True, theme=None)
