from io import BytesIO
import pandas as pd


def normalize_cols(df0):
    dfx = df0.copy()
    col_use = [x.lower() for x in dfx.columns]
    col_mapping = dict(zip(dfx.columns, col_use))
    dfx = dfx.rename(columns = col_mapping)
    return dfx

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data