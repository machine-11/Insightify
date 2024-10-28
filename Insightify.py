import streamlit as st

from helper_functions.utility import check_password  



# Check if the password is correct.  
if not check_password():  
    st.stop()


st.set_page_config(
        page_title="Insightify",  
    )

md = """
**IMPORTANT NOTICE:**

This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.

"""

st.markdown(md)


# st.sidebar("""IMPORTANT NOTICE:
# This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

# Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

# Always consult with qualified professionals for accurate and personalized advice.""")