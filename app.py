import gradio as gr
import pandas as pd
from validate_email_address import validate_email
from utils import enrich_data, score_lead

def process_leads(file):
    df = pd.read_csv(file.name)
    results = []
    for _, row in df.iterrows():
        email = row.get("email", "")
        domain = row.get("domain", "")
        is_valid = validate_email(email, verify=True)
        enrichment = enrich_data(domain)
        score = score_lead({
            "email_verified": is_valid,
            "LinkedIn": enrichment.get("LinkedIn"),
            "Size": enrichment.get("Size")
        })
        result = {
            "email": email,
            "domain": domain,
            "valid": is_valid,
            **enrichment,
            "lead_score": score
        }
        results.append(result)
    result_df = pd.DataFrame(results)
    return result_df

iface = gr.Interface(
    fn=process_leads,
    inputs=gr.File(label="Upload CSV with 'email' and 'domain' columns"),
    outputs=gr.Dataframe(),
    title="LeadIQ - Smart Lead Validator & Enricher",
    description="Validates, enriches, and scores leads in a single step. Powered by Gradio + Hugging Face."
)

if __name__ == "__main__":
    iface.launch()
