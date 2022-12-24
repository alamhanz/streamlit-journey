from collections import namedtuple
from locale import normalize
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import noto

def upload_file1():
    st.session_state['file1_excel'] = 'not ready'

def sheet_file1():
    st.session_state['file1'] = 'not ready'

"""
# Welcome to Nop-Exist!
You can upload 2 excel then choose the sheet. After that choose one columns which exist from those two excels.
This app will provide dataframe where value of the columns in table A is not exist in table B.
"""

## First File Upload
if 'file1_excel' not in st.session_state:
    st.session_state['file1_excel'] = 'not ready'
    st.session_state['file1_path'] = 'not exist'
    st.session_state['file1'] = 'not ready'

if st.session_state['file1_excel'] == 'not ready':
    default_text = 'Type Here'
    uploaded_file1 = st.file_uploader("Choose file A", key = 123)
    converter_rules = {'NOP' : str,'nop':str, 'Nop':str,'NOp':str,'NoP':str}

    st.write(st.session_state['file1_excel'])
    if uploaded_file1:

        # upload excel file 1
        Excel1 = pd.ExcelFile(uploaded_file1)
        sheet_names1 = Excel1.sheet_names
        st.session_state['file1_excel'] = 'ready'
        st.session_state['file_path'] = uploaded_file1

st.write(st.session_state['file1_path'])
st.write(st.session_state['file1_excel'])
if (st.session_state['file1_excel'] == 'ready') & (st.session_state['file1'] == 'not ready'):
    # select sheet
    sheet_options = st.selectbox('which sheet are you using?',
            sheet_names1, key = 'file1', on_change = sheet_file1)

    if sheet_options:
        st.write('You selected:', sheet_options)

        # get the df and normalize the colname
        df1 = Excel1.parse(sheet_name=sheet_options,
                                converters = converter_rules)
        df1 = noto.normalize_cols(df1)
        st.write(df1.shape)
        st.write(df1)
        st.session_state['file1'] = 'ready'





# ## Second File Upload
# uploaded_file2 = st.file_uploader("Choose file B", key = 122)
# if uploaded_file2 is not None:

#     # upload excel file 1
#     Excel2 = pd.ExcelFile(uploaded_file2)
#     sheet_names2 = Excel2.sheet_names

#     # select sheet
#     sheet_options = st.selectbox('which sheet are you using?',
#             sheet_names2, key = 132)

#     if sheet_options:
#         st.write('You selected:', sheet_options)

#         # get the df and normalize the colname
#         df2 = Excel2.parse(sheet_name=sheet_options,converters = converter_rules)
#         df2 = noto.normalize_cols(df2)
#         st.write(df2.shape)
#         st.write(df2)


# if uploaded_file1 is not None and uploaded_file2 is not None:
#     col_in_both = set(df1.columns) & set(df2.columns)
#     st.write('--'*10)
#     st.write('the column options to compare :')
#     st.write(col_in_both)
#     col_compare = st.text_input("Type the column name :", default_text)

#     if col_compare != default_text:
#         # try:
#         val1 = set(df1[col_compare].unique())
#         val2 = set(df2[col_compare].unique())
#         res_val = val1-val2

#         st.write(len(val1))
#         st.write(len(val2))

#         str_res = 'nop minimum res : '+str(len(res_val))+' rows'

#         st.write(str_res)

#         df_results = df1[df1[col_compare].isin(res_val)]

#         df_xlsx = noto.to_excel(df_results)
#         st.download_button(label='📥 Download The Result',
#                                         data=df_xlsx ,
#                                         file_name= 'nop_result.xlsx')

#         # except:
#         #     st.write('Error. Check The Column Name')

    