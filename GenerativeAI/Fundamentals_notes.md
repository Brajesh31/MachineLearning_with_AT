# Generative AI Fundamentals Notes

These notes summarize introductory concepts. Platform capabilities, product names, model availability, licenses, and legal requirements change, so verify current details against primary documentation before using them for decisions.

## 1. AI's future impact

- AI automation may displace some tasks and roles.
- AI can also improve efficiency and productivity when deployed responsibly.
- Over-reliance on AI can hide errors and weaken human skills if outputs are not reviewed.
- Privacy, security, accountability, and transparency remain important concerns.

## 2. Databricks Lakehouse AI concepts

- Model Serving is used to deploy models for inference.
- Lakehouse Monitoring supports monitoring data and model quality over time.
- MLflow provides tools for experiment tracking and model evaluation. Product capabilities and names can evolve, so consult current Databricks and MLflow documentation.

## 3. Competitive advantage for AI businesses

Organizations may gain an advantage by using proprietary, high-quality data responsibly. Data access alone is not enough. Governance, relevance, quality, privacy, and execution also matter.

## 4. LLM input chunks

Tokens are units used to represent text for language models. A token may be a word, part of a word, punctuation, or another text unit. Tokenization depends on the model's tokenizer.

## 5. Security: prompt injection

Prompt injection is an attempt to manipulate a model by placing instructions in user input, retrieved content, documents, or other data. Treat untrusted content as data, enforce permissions outside the model, and validate actions before execution.

## 6. Relationship between AI fields

Artificial intelligence is the broad field. Machine learning is one approach within AI. Deep learning is a family of machine-learning methods based on multi-layer neural networks. Generative AI describes systems that create content and can use different underlying model approaches.

## 7. Fine-tuning

Fine-tuning means continuing the training of a pre-trained model on a task-specific dataset. It is different from prompt engineering and retrieval-augmented generation. It requires careful data preparation and evaluation.

## 8. Legal and responsible-use risks

Generative AI can be misused to produce fraud, impersonation, harmful content, or malicious code. Organizations remain responsible for how they deploy systems and handle personal or protected data. Applicable obligations depend on jurisdiction and context.

## 9. Governance and monitoring

Data and AI governance can include access controls, cataloging, lineage, auditability, and policy enforcement. Monitoring can help identify data quality issues, model drift, latency, and operational failures.

## 10. Open-source and open-weight model licensing

Do not assume that a model is unrestricted because its weights or code are publicly available. Commercial use, redistribution, acceptable-use rules, and attribution requirements depend on the exact model license and version. Review the license directly before use.
