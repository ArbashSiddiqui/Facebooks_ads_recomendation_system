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

# Function to generate recommendations
def generate_recommendations(business_name, business_info, budget, days, country, additional_details):
    user_inputs = {
        "business_name": business_name,
        "business_info": business_info,
        "budget": f"${budget:.2f}",
        "days": str(days),
        "country": country,
        "platforms": "Facebook",
        "additional_details": additional_details
    }
    
    # Process the user inputs and generate recommendations
    recommendations = llm_chain.run(user_inputs)
    
    return recommendations
