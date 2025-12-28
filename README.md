#**LiveDoc Sentinel**

An Agentic AI System for Continuously Evolving Knowledge

##**Overview**

LiveDoc Sentinel is an agentic AI system designed to operate over continuously changing
documents without relying on static knowledge snapshots.
Traditional Retrieval-Augmented Generation (RAG) systems assume that knowledge is updated
periodically through batch re-indexing. In fast-moving environments such as developer
tooling, this assumption breaks down. Documentation changes, issues are created or closed,
and APIs evolve daily. AI systems built on static pipelines quickly fall out of sync with
reality.
LiveDoc Sentinel demonstrates how streaming-first data ingestion and agentic reasoning
can be combined to build AI assistants that remain accurate, explainable, and trustworthy
over time.

##**Problem Statement**

Most AI assistants used in developer workflows rely on static RAG pipelines. These systems
fail when knowledge changes, because:
Documentation updates are not reflected immediately
AI answers silently rely on outdated information
Re-embedding and re-indexing entire corpora is slow and operationally expensive
Users cannot tell when or why an answer has changed
In practice, this leads to loss of trust. Developers stop relying on AI assistants when
they produce answers that ignore recent changes or fail during critical moments such as
debugging or API migration.
The core problem is not retrieval quality alone — it is the inability of AI systems to
observe, understand, and adapt to change as it happens.

##**Design Goals**

LiveDoc Sentinel is built around the following principles:
Live Knowledge, Not Snapshots
The system must reason over the latest state of documents at all times.
Incremental Updates
Small changes should trigger small updates, not full reprocessing.
Explainability Over Blind Accuracy
Users should be able to understand why an answer exists and what changed.
Agentic Adaptation
The system should not only retrieve information, but reason about its relevance and
impact.

##**Solution Summary**

LiveDoc Sentinel uses Pathway’s streaming engine to treat documents as live data streams
rather than static files.
As documents are added, edited, or removed:
Changes are detected automatically
Only affected content is reprocessed
Embeddings and semantic indexes are updated incrementally
The agent reasons over the updated knowledge base within seconds
This enables an AI co-pilot that adapts continuously without manual refresh cycles.

##**System Architecture**
<img width="749" height="302" alt="image" src="https://github.com/user-attachments/assets/a193267e-f034-4b5b-b822-797cc8fd94b7" />

##**Demonstrating “Live” Behavior**

The system explicitly demonstrates real-time adaptation:
1.A user queries the agent about existing documentation
2.A document is modified (e.g., bug report update or documentation edit)
3.Pathway detects the change and updates only affected embeddings
4.The agent’s response changes accordingly
5.The user can observe what changed and why
This behavior cannot be replicated with traditional static RAG pipelines.

##**Agent Behavior & Reasoning**

The agent follows a structured reasoning loop:
1.Observe
Detects updates in the knowledge base.

2.Assess Relevance
Determines whether the change affects current or recent queries.

3.Plan
Decides whether to retrieve, summarize, or defer based on confidence.

4.Act
Produces responses grounded in the latest data.

5.Validate
Handles missing context, conflicting information, or uncertainty.

The agent is designed to avoid overconfidence and prefers traceable answers over
speculative ones.

##**Failure Awareness & Limitations**

LiveDoc Sentinel is not designed to be infallible. Known challenges include:
High-frequency updates causing noisy signals
Ambiguous document changes with unclear impact
Latency trade-offs between ingestion and reasoning depth
Rather than hiding these limitations, the system is designed to surface uncertainty and
prioritize correctness over immediacy when required.

##**Future Scope: Baby Dragon Hatchling (BDH)**

The architecture anticipates integration with Pathway’s Baby Dragon Hatchling (BDH)
model once available.
BDH integration would enable:
1.Long-horizon reasoning over document evolution
2.Persistent agent memory across sessions
3.More deterministic planning under continuous updates
4.Reduced inference cost for always-on agents
The reasoning layer is intentionally modular to allow seamless replacement when BDH is
released.

##**Applicability Beyond Developer Tools**

While demonstrated in the Developer Tools domain, the same architecture applies to any
context where knowledge evolves continuously:
Financial filings and earnings reports
Medical literature and clinical guidelines
Compliance and regulatory monitoring
The core contribution is not domain-specific, but architectural.

##**Conclusion**

LiveDoc Sentinel demonstrates a shift from static AI assistants to adaptive,
streaming-aware agents.
By combining Pathway’s real-time data processing with agentic reasoning, the system shows
how AI can remain trustworthy in environments where knowledge never stands still.


