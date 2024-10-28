import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import Insightify

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()



# md = """
# project scope, objectives, data sources, and features.
# """

# st.markdown(md)
st.title("About Us")
st.sidebar.markdown(Insightify.md)
# st.set_page_config(
#         page_title="About Us",  
#     )

pdf_file = "pages/US.pdf"
  
with open(pdf_file,"rb") as f:
     pdf_viewer(input=pdf_file,
                   width=900)

