# Ad_prompt="""
# # You are a recommendation system for Facebook Ads Management. Based on the following input details, provide the best recommendations for running a Facebook ad:

# # 1. Business Name: {business_name}
# # 2. Business Info: {business_info}
# # 3. Budget: {budget}
# # 4. Days to Run the Ad: {days}
# # 5. Country (City): {country}
# # 6. Platforms: {platforms}
# # 7. Additional Details: {additional_details}


# # Recommendations:
# # 1. Interests (from Facebook's predefined behaviors that facebook provides while creating ads)
# # 2. Behaviors (from Facebook's predefined behaviors that facebook provides while creating ads.)
# # 3. Demographics (from Facebook's predefined demographics)
# #         demographics should include the income level for example: top 10,20 or less or more percent of audiences as per the product price range.
# #         it must also include the professions to be targeted , areas and what kind of demographics would be best fit for product.
# #         also focus on relation, life events , Work where and if necessary.

# # 4. Optimal Days to Run the Ad (keep in mind the location)
# # 5. Best Hours to Run the Ad
# # 6. Type of Ad (only recommend the best ad type for the user's campaign)
# # 7. Calculate maximum estimated Reach and Impressions per day as per Facebook predefined, and also give total reach.
# # 8. Other Helpful Suggestions
# # Note: Recommendations should be tailored based on the r egion specified (e.g., country or city).
# # """
Ad_prompt="""
# You are a recommendation system for Facebook Ads Management. Based on the following input details, provide the best recommendations for running a Facebook ad:

# 1. Business Name: {business_name}
# 2. Project description: {project_decription}
# 3. Budget: {budget}
# 4. Days to Run the Ad: {days}
# 5. Country (City): {country}
# 6. Platforms: {platforms}
# 7. Additional Details: {additional_details}
# 8. Demographics_str: {demographics_str}
# 9. Interests_str: {interests_str}
# 10. Behaviors_str: {behaviors_str}



# Recommendations:
# 1. Interests (interests - given in input)
# 2. Behaviors (Behaviours - given in input)
# 3. Demographics (demographics - given in input)
# 4. Optimal Days to Run the Ad (keep in mind the location)
# 5. Best Hours to Run the Ad
# 6. Type of Ad (only recommend the best ad type for the user's campaign)
# 7. Calculate maximum estimated Reach (estiamted 10k - 30k as per facbook for 5$ perday) and Impressions per day as per Facebook predefined, and also give total reach.
# 8. Other Helpful Suggestions
# Note: Recommendations should be tailored based on the region specified (e.g., country or city).

the recommendations for interests , behaviors and demographics should be in a proper format:
for the relevant options selected by engine as a recommendation the output should be like :
name (recommended key:value against the name):
"""

# eval_prompt="""
# Given the following input details for a business's ad campaign:

# - Business Name: {business_name}
# - Business Info: {business_info}
# - Current Budget: {budget}
# - Campaign Duration (Days): {days}
# - Target Country: {country}
# - Advertising Platforms: {platforms}
# - Additional Details: {additional_details}

# and the ad campaign's expected output:

# - Expected Campaign Results: {output}

# Please review the input and suggest any modifications to enhance the effectiveness of the ad campaign.
# Additionally, provide a range of budget options that could potentially yield better results, explaining the benefits of each suggested budget.
# If available, please provide details on previous ad campaign performances and any specific goals (e.g., increase brand awareness, drive sales) for this campaign.
# Please provide insights into potential long-term strategies that could be beneficial following the initial ad campaign period.




