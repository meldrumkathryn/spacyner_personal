# -------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import spacy
from spacy import displacy
import scispacy
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# Page setup
st.set_page_config(page_title="Inclusion\Exclusion Criteria", page_icon = '🧠', layout="wide")
st.title("Inclusion\Exclusion Criteria Search")

# NCT Dummy
sheet_id = "1o0WD5Cym4Xe1-ltIM-NDmHDnk85IoEdRROY-EGuJpYQ"
sheet_name = "nct_dummy"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/Capstone/main/streamlit_files/entities.csv', dtype=str).fillna("")
# df_entities = df['Entity Type'].unique()
# df_entities = pd.read_csv('https://github.com/meldrumkathryn/Capstone/blob/main/entities.csv', dtype=str)
df_entities = df['Entities'].unique()

# Example Real Trial Sheet
df3 = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/clinicaltrials.gov_NER/main/streamlit_files/api_pull_data_small.csv', dtype=str).fillna('')
# df3.columns = df3.iloc[0]
# df3 = df3[1:]

# Entities
df6 = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/Capstone/main/streamlit_files/entities.csv')

# Entity Spans
# ent_spans1 = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/Capstone/main/streamlit_files/ents_spans_small.csv')
# ent_spans1 = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/Capstone/main/streamlit_files/ents_spans_small.csv')
ent_spans1 = pd.read_csv('https://raw.githubusercontent.com/meldrumkathryn/clinicaltrials.gov_NER/main/streamlit_files/ents_spans_small.csv')

# api_pull
# df5 = pd.read_csv('api_pull_data.csv')
# df5 = df.head()

# AgGrid
gb = GridOptionsBuilder.from_dataframe(df3)
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()
gridoptions = gb.build()

# -------------------------------------------------------------------------------------------
# Testing playground
# st.write(condition)
# st.write(ent_spans1[option])
# -------------------------------------------------------------------------------------------

entities = df6['Entities']
# st.write(df5)
# Corpus Selection Form
with st.form("my_form1"):
   corpus = st.radio(
     "Choose a corpus",
     ('Chia'))

   # Every form must have a submit button.
   submitted1 = st.form_submit_button("Choose")

# Search Entities Form
with st.form("my_form2"):
  if corpus == 'Chia':
    st.write('Entities for Chia')
#   elif corpus == 'EBM NLP':
#     st.write('Entities for EBM NLP')

  if submitted1:
    if corpus == 'Chia':
      st.write('[Chia, a large annotated corpus of clinical trial eligibility criteria](https://www.nature.com/articles/s41597-020-00620-0)')
      st.write(df6)
#     elif corpus == 'EBM NLP':
#       st.write('[EBM NLP, A Corpus with Multi-Level Annotations of Patients, Interventions and Outcomes to Support Language Processing for Medical Literature](https://www.nature.com/articles/s41597-020-00620-0)')
    else:
      st.write("Please select a corpus.")

  st.write('Search entities')
  if corpus == 'Chia':
   option = st.selectbox('Entity name', entities)  
  elif corpus == 'EBM NLP':
   option = st.selectbox('Entity name', entities)
  else:
   st.write('Choose an entity')

  submitted2 = st.form_submit_button("Submit")

# Display trials filtered by entity -- do after getting trials with inc/exc already labeled
# Logic here should filter on entities that inc/exc criteria contain

# Search Spans Form
with st.form("my_form3"):
  if df6['Entities'].str.contains(option).any():
    option8 = st.selectbox('Spans', ent_spans1[option])
  submitted3 = st.form_submit_button("Submit")

# Create dataframe from selection
filter_on_spans = df3[df3['Spans'].str.contains(option8)]

# Display Trials and Displacy
# if submitted3:
  # Display Trials
  # st.subheader('Trials')
  # gd = GridOptionsBuilder.from_dataframe(filter_on_spans)
  # gd.configure_pagination(enabled=True)
  # gd.configure_selection(selection_mode='single', use_checkbox=True)
  # gridoptions = gd.build()
  # ag = AgGrid(filter_on_spans, 
  #             gridOptions=gridoptions,
  #             height=200, 
  #             use_checkbox=True)

  # Display selected rows    
  # v = ag['selected_rows']
  # if v:
  #   st.write('Selected rows')
  #   st.dataframe(v)
  # v = ag['selected_rows']
  # st.write(v)

# Displacy - test for any
  # st.header('Visualizing Entities')
  # nlp = spacy.load('C:/Users/nikit/UVAMSDS/app/app/model-last')
  # # To Do: Change text input to be selected trials from aggrid
  # # df_head = df3.head()
  # text_inc = str(df3['InclusionCriteria'][0])
  # text_exc = str(df3['ExclusionCriteria'][0])
  # doc = nlp(text_inc)
  # doc2 = nlp(text_exc)
  # ent_html = displacy.render(doc, style='ent', jupyter=False)
  # ent_html2 = displacy.render(doc2, style='ent', jupyter=False)
  # st.subheader('Inclusion Criteria')
  # st.markdown(ent_html, unsafe_allow_html=True)
  # st.subheader('Exclusion Criteria')
  # st.markdown(ent_html2, unsafe_allow_html=True)


# --------------------------------------------------------------------------------------------------------
# Testing area for ag-grid
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd
import streamlit as st

@st.cache_data
def convert_df(test_df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return test_df.to_csv(index=False).encode('utf-8')


test_df = pd.DataFrame(filter_on_spans)

gb = GridOptionsBuilder.from_dataframe(test_df)
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="single", use_checkbox=True)
gb.configure_side_bar()
gridoptions = gb.build()

response = AgGrid(
    test_df,
    height=200,
    gridOptions=gridoptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
    header_checkbox_selection_filtered_only=True,
    use_checkbox=True)

# st.write(type(response))
# st.write(response.keys())

# Store selected
v = response['selected_rows']
if v:
    dfs = pd.DataFrame(v)
    csv = convert_df(dfs)

    # Displacy - test for any
    st.header('Visualizing Entities')
    nlp = spacy.load('https://github.com/meldrumkathryn/clinicaltrials.gov_NER/tree/main/app/app/model-last/model-last')
    # To Do: Change text input to be selected trials from aggrid
    # df_head = df3.head()
    # text_inc = str(df3['InclusionCriteria'][0])
    # text_exc = str(df3['ExclusionCriteria'][0])
    text_inc = str(v)
    text_exc = str(v)
    doc = nlp(text_inc)
    doc2 = nlp(text_exc)
    ent_html = displacy.render(doc, style='ent', jupyter=False)
    ent_html2 = displacy.render(doc2, style='ent', jupyter=False)
    st.subheader('Inclusion Criteria')
    st.markdown(ent_html, unsafe_allow_html=True)
    st.subheader('Exclusion Criteria')
    st.markdown(ent_html2, unsafe_allow_html=True)

    
