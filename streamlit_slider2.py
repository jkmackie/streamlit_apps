#!/usr/bin/env python
# coding: utf-8

import streamlit as st

x = st.slider('Select a value')
st.write(x, 'half is', x/2)


