import os
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompts import Ad_prompt
from dotenv import load_dotenv

load_dotenv()
# Use environment variable for API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = OpenAI(model="gpt-4o-mini", temperature=0.3, api_key=OPENAI_API_KEY)

prompt_template = Ad_prompt

prompt = PromptTemplate(template=prompt_template, input_variables=[
    "business_name", "business_info", "budget", "days", "country", "platforms", "additional_details"])

llm_chain = LLMChain(
    prompt=prompt,
    llm=llm
)

def main():
    print("Facebook Ads Recommendation System")

    try:
        business_name = input("Business Name: ")
        business_info = input("Business Info: ")
        budget = float(input("Budget (in dollars): "))
        days = int(input("Days to Run the Ad: "))
        country = input("Country (City): ")
        additional_details = input("Additional Details: ")
        
        platforms = "Facebook"

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
        
        print("Recommendations:")
        print(recommendations)
    except ValueError:
        print("Invalid input, please ensure all inputs are correctly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
