
import streamlit as st

md = """
**📦 Deliverables**

**Web Application:**

    A fully functional, deployed web application accessible via a URL, demonstrating all required features and the two specified use cases.
    The suggested platform for deploying the web application is Streamlit Community Cloud.
    It is recommended to password protect the application.

**Documentation (As Pages within the Streamlit App):**

    In addition to the webpages that include the required features and functionality, your Streamlit app MUST contain the following two additional pages:

*“About Us” Page:*
    
    A detailed page outlining the project scope, objectives, data sources, and features.

*“Methodology” Page:*
    
    A comprehensive explanation of the data flows and implementation details.
    
    A flowchart illustrating the process flow for each of the use cases in the application. For example, if the application has two main use cases: a) chat with information and b) intelligent search, each of these use cases should have its own flowchart.
    Refer to the sample hereLinks to an external site. for the samples of the flowcharts and methodology (Slide 13, 14, and 15).

OPTIONAL: editable templateLinks to an external site. (this is .pptx of the sample for your usage/reference; you don't need to submit this file) 🆕 
Source Code (Upon Request):
Well-documented Python code for the web application, including all scripts related to data processing, LLM integration, and UI components.
"""


st.markdown(md)