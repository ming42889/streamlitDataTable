import streamlit as st
import pandas as pd
from datetime import datetime

def getDataFrame():
    if "dataFrame" not in st.session_state:
         st.session_state.dataFrame = pd.DataFrame()
    return st.session_state.dataFrame

def addOrUpdateTable(code):
    df = st.session_state.dataFrame
    if code in df.index:
        df.loc[code,"count"] = df.loc[code,"count"]+1
    else:
        new_row = pd.DataFrame([{"code":code,"count":1,"date": datetime.now()}])
        new_row.set_index('code', inplace=True) 
        df = pd.concat([df, new_row])
        st.session_state.dataFrame = df
    
def drawTable() :
    df = getDataFrame()
    if (len(df) > 0):
        edited_df = st.data_editor(df,disabled=["code"])
        st.session_state.dataFrame = edited_df

# def convert_for_download():
#     df = getDataFrame()
#     return df.to_csv().encode("utf-8")

# st.download_button(
#     label="Download CSV",
#     data=convert_for_download(),
#     file_name="data.csv",
#     mime="text/csv",
#     icon=":material/download:",
# )

# Accept user input
if prompt := st.chat_input("What is up?"):
    print(prompt)
    code =prompt.strip()
    addOrUpdateTable(code)


drawTable()