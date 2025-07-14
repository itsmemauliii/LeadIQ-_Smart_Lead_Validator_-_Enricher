def enrich_data(domain):
    # Mock enrichment logic
    return {
        "Industry": "SaaS",
        "Size": "51-200",
        "LinkedIn": f"https://linkedin.com/company/{domain.split('.')[0]}"
    }

def score_lead(data):
    score = 0
    if data["email_verified"]: score += 1
    if data["LinkedIn"]: score += 1
    if data["Size"] != "Unknown": score += 1
    return score
