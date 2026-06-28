from app.rag.retriever import retrieve_documents

from app.agents.summary_agent import summarize_claim
from app.agents.coverage_agent import check_coverage
from app.agents.missing_docs_agent import find_missing_documents
from app.agents.fraud_agent import detect_fraud
from app.agents.recommendation_agent import recommend_claim


def analyze_claim(question: str):
    """
    Main workflow that coordinates all AI agents.
    """

    # Retrieve relevant document chunks from FAISS
    documents = retrieve_documents(
        question=question,
        k=5
    )

    # Build context
    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    # Run all agents
    summary = summarize_claim(context)

    coverage = check_coverage(
        context=context,
        question=question
    )

    missing_documents = find_missing_documents(context)

    fraud = detect_fraud(context)

    recommendation = recommend_claim(
        context=context,
        coverage=coverage,
        fraud=fraud,
        missing_documents=missing_documents
    )

    # Final combined response
    return {
        "claim_summary": summary,
        "coverage": coverage,
        "missing_documents": missing_documents,
        "fraud": fraud,
        "recommendation": recommendation
    }