import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompts import Ad_prompt

# Initialize the OpenAI model with specified parameters
OPENAI_API_KEY = 'API_KEY'

llm = OpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

# Define the prompt template for gathering user inputs and generating recommendations
prompt_template = Ad_prompt

# Create a LangChain prompt template using the defined prompt
prompt = PromptTemplate(template=prompt_template, input_variables=[
    "business_name", "business_info", "budget", "days", "country", "platforms", "additional_details"])

# Create an LLMChain with the prompt and the OpenAI model
llm_chain = LLMChain(
    prompt=prompt,
    llm=llm
)

# Streamlit app
def main():
    st.title("Facebook Ads Recommendation System")

    # Gather user inputs
    business_name = st.text_input("Business Name")
    business_info = st.text_area("Business Info")
    budget = st.number_input("Budget (in dollars)", min_value=0.0, format="%.2f", step=1.0)
    days = st.number_input("Days to Run the Ad", min_value=1, step=1)
    country = st.text_input("Country (City)")
    additional_details = st.text_area("Additional Details")
    
    # Fixed platform value
    platforms = "Facebook"

    # Generate recommendations when the user submits the form
    if st.button("Get Recommendations"):
        user_inputs = {
            "business_name": business_name,
            "business_info": business_info,
            "budget": f"${budget:.2f}",
            "days": str(days),
            "country": country,
            "platforms": platforms,
            "additional_details": additional_details
        }
        
        # Process the user inputs and generate recommendations
        recommendations = llm_chain.run(user_inputs)
        
        # Display the recommendations
        st.subheader("Recommendations")
        st.markdown(recommendations)

if __name__ == "__main__":
    main()
