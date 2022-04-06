# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:25:47 2022

@author: jahop_fz60h0
"""

import streamlit as st
import base64

st.subheader("")
def show_pdf(file_path):
    with open(file_path,"rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("CV.pdf")
