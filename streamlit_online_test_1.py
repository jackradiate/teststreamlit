import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import duckdb
from colorama import Fore, Back, Style
from icecream import ic
import openpyxl # used either to convert files to excel or in the streamlit download button
import os
from pathlib import Path
import math
from plotly.tools import mpl_to_plotly

st.write("## Test of Streamlit Online Deployment")
st.write("### From Wikipedia: ")
st.write("Transcontinental Gas Pipe Line (Transco) is a natural gas pipeline which brings gas from the Gulf coast of Texas, Louisiana, Mississippi, and Alabama, through Georgia, South Carolina, North Carolina, Virginia, Maryland, and Pennsylvania to deliver gas to the New Jersey and New York City area. It is owned by the Williams Companies. Its FERC code is 29.")

st.write('<p style = "color:green;">That\'s the end of this test website!',unsafe_allow_html=True)

image_url = "https://cdn-icons-png.flaticon.com/512/9139/9139910.png"
st.image(image_url)