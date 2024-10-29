
import streamlit as st
from logics import crew_elig
from helper_functions import llm
import Insightify

from helper_functions.utility import check_password  


# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("Advisory")
st.subheader("Understanding HDB flat eligibility and housing loan options")
# st.sidebar.markdown(Insightify.md)
# topic = st.text_input("Please enter a detailed query about HDB flat eligibility and housing loan options. The more information you provide, the more accurate and helpful our response will be.")

topic = st.text_area("Please enter a detailed query about HDB flat eligibility and housing loan options. The more information you provide, the more accurate and helpful our response will be.",
value = "I am 38 years old, single, and a Singaporean. I plan to get an HDB flat. What is the maximum amount of subsidy and grants I can possibly receive from the government?" ) 

##prepare crew wit kb
@st.cache_resource
def load_crew():
    return crew_elig.gen_crew()

#load crew
if "crew" not in st.session_state.keys():  
    st.session_state.crew = load_crew()

#default answer
result = "I appreciate your understanding, but that question falls outside my area of expertise. My focus is on providing in-depth analysis of HDB flat eligibility and housing loan options tailored to your specific situation. If you have any questions related to that topic, please feel free to ask!"

#check for funny and irrelvant query
if st.button("Run"):
    with st.spinner('Loading...'):
        if llm.check_for_malicious_intent(topic) == "N":

            if  llm.check_query_relevancy (topic,"HDB flat eligibility and housing loan options" ) == "Y":

                result = st.session_state.crew.kickoff(inputs={"topic": topic})
     
        st.markdown(result)
