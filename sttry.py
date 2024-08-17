import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompts import Ad_prompt

# Initialize the OpenAI model with specified parameters
OPENAI_API_KEY = 'API KEY'

llm = OpenAI(model="gpt-4o-mini", temperature=0.2, api_key=OPENAI_API_KEY)

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

# Function to evaluate inputs and outputs to suggest changes and budget
def evaluate_and_recommend_changes(user_inputs, output):
    evaluation_prompt_template = """
    Given the following input and output:
    
    Input:
    Business Name: {business_name}
    Business Info: {business_info}
    Budget: {budget}
    Days: {days}
    Country: {country}
    Platforms: {platforms}
    Additional Details: {additional_details}
    
    Output:
    {output}
    
    Please suggest any changes to the input that would improve the ad campaign, and recommend an appropriate budget and dont stick for a single budget recommend budget from you side for the best results.
    """
    
    evaluation_prompt = PromptTemplate(
        template=evaluation_prompt_template,
        input_variables=[
            "business_name", "business_info", "budget", "days", "country", "platforms", "additional_details", "output"]
    )
    
    evaluation_chain = LLMChain(
        prompt=evaluation_prompt,
        llm=llm
    )
    
    evaluation_inputs = {
        "business_name": user_inputs["business_name"],
        "business_info": user_inputs["business_info"],
        "budget": user_inputs["budget"],
        "days": user_inputs["days"],
        "country": user_inputs["country"],
        "platforms": user_inputs["platforms"],
        "additional_details": user_inputs["additional_details"],
        "output": output
    }
    
    recommendations = evaluation_chain.run(evaluation_inputs)
    
    return recommendations

# Streamlit app
def main():
    st.title("Facebook Ads Recommendation System")

    # Gather user inputs
    business_name = st.text_input("Business Name")
    business_info = st.text_area("Business Info")
    budget = st.number_input("Budget (in dollars)", min_value=0.0, step=0.01)
    days = st.number_input("Days to Run the Ad", min_value=1, step=1)
    country = st.text_input("Country (City)")
    additional_details = st.text_area("Additional Details")
    
    # Fixed platform value
    platforms = "Facebook"

    if st.button("Generate Recommendations"):
        if not business_name or not business_info or not country:
            st.error("Please fill in all required fields (Business Name, Business Info, Country).")
        else:
            user_inputs = {
                "business_name": business_name,
                "business_info": business_info,
                "budget": f"${budget:.2f}",
                "days": str(days),
                "country": country,
                "platforms": platforms,
                "additional_details": additional_details
            }

            recommendations = llm_chain.run(user_inputs)
            
            st.subheader("Initial Recommendations:")
            st.write(recommendations)
            
            evaluation = evaluate_and_recommend_changes(user_inputs, recommendations)
            
            st.subheader("Evaluation and Suggested Changes:")
            st.write(evaluation)

if __name__ == "__main__":
    main()
