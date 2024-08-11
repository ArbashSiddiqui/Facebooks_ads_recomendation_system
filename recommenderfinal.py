import os
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from d import demographics_str, interests_str, behaviors_str
from prompts import Ad_prompt

# Load environment variables
load_dotenv()
# Use environment variable for API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = OpenAI(model="gpt-4o-mini", temperature=0.3, api_key=OPENAI_API_KEY)

# Prompt template
prompt_template = Ad_prompt

prompt = PromptTemplate(
    template=prompt_template, 
    input_variables=[
        "business_name", "project_decription", "budget", "days", 
        "country", "platforms", "additional_details", 
        "demographics_str", "interests_str", "behaviors_str"
    ]
)

llm_chain = prompt | llm 


def main():
    print("Facebook Ads Recommendation System")

    try:
        business_name = input("Business Name: ")
        project_decription = input("Project description: ")
        budget = float(input("Budget (in dollars): "))
        days = int(input("Days to Run the Ad: "))
        country = input("Country (City): ")
        additional_details = input("Additional Details: ")
        
        platforms = "Facebook"

        user_inputs = {
            "business_name": business_name,
            "project_decription": project_decription,
            "budget": f"${budget:.2f}",
            "days": str(days),
            "country": country,
            "platforms": platforms,
            "additional_details": additional_details,
            "demographics_str": demographics_str,
            "interests_str": interests_str,
            "behaviors_str": behaviors_str
        }
        
        recommendations = llm_chain.invoke(user_inputs)
        
        # Parse the output
        output_text = recommendations.content
        
        # Initialize empty strings for each dictionary
        interests_output = ""
        demographics_output = ""
        behaviors_output = ""
        
        # Split the output into sections
        sections = output_text.split("\n\n")
        
        # Extract relevant sections into the corresponding variables
        for section in sections:
            if "Interests" in section:
                interests_output = section
            elif "Demographics" in section:
                demographics_output = section
            elif "Behaviors" in section:
                behaviors_output = section
        
        # Display each section separately
        print("Interests:")
        print(interests_output)
        
        print("\nDemographics:")
        print(demographics_output)
        
        print("\nBehaviors:")
        print(behaviors_output)
        
        
        # Return each section separately
        return interests_output, demographics_output, behaviors_output , recommendations
        
    except ValueError:
        print("Invalid input, please ensure all inputs are correctly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    interests, demographics, behaviors, recommendations = main()
