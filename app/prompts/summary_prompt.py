SUMMARY_PROMPT = """
You are an expert Healthcare Claims AI.

Using ONLY the provided context, extract the following information.

Return valid JSON.

Fields:

patient_name
hospital_name
diagnosis
treatment
claim_amount
admission_date
discharge_date
summary

If a field is missing, return null.

Context:

{context}
"""