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

*#**Key Novelty**

Unlike traditional RAG systems that treat documents as static corpora, LiveDoc Sentinel treats documentation as a continuously evolving data stream. The system combines streaming ingestion, incremental semantic indexing, and agentic reasoning to maintain alignment with real-world knowledge in near real time—without manual reprocessing cycles.

##**Problem Statement**

Modern AI assistants rely heavily on Retrieval-Augmented Generation (RAG) to answer
questions over documents, codebases, and knowledge bases. However, traditional RAG
pipelines are fundamentally static.
In real-world environments—especially in developer workflows—documentation, codebases,
and APIs change continuously. Every update requires expensive re-embedding, re-indexing,
and redeployment, which means AI systems inevitably operate on stale or outdated
knowledge.
For developers, this leads to:
•	Incorrect answers after recent code changes
•	Missed breaking changes in evolving APIs
•	Manual effort to keep AI tools in sync with repositories
•	Reduced trust in AI assistants for real-time decision-making
Existing solutions accept this staleness as a trade-off, relying on batch updates and
human oversight. This limits AI systems to reactive, snapshot-based behavior, rather
than continuous understanding.
What is missing is an AI system that can:
•	Observe knowledge as it evolves
•	Update its understanding instantly
•	Reason over changes, not just static content
•	Act autonomously without manual refresh cycles
Without live knowledge adaptation, AI assistants cannot function as reliable co-pilots
in fast-moving, real-world workflows.

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

LiveDoc Sentinel is designed with a modular reasoning layer that can evolve as more capable
reasoning models become available. In particular, the system architecture anticipates
integration with Pathway’s Baby Dragon Hatchling (BDH) model once officially released.

Potential future enhancements include:

1.Long-horizon reasoning over document evolution
While the current agent reasons over the latest document state, BDH could enable reasoning
across historical change sequences, allowing the agent to understand how and why
knowledge has evolved over time.

2.Persistent and deterministic agent memory
BDH may allow the agent to maintain structured memory across sessions, reducing reliance on
ad-hoc context windows while avoiding memory drift and hallucinations.

3.More stable planning under continuous updates
Streaming data introduces frequent state changes. BDH’s design could support more
deterministic planning and decision-making in environments where knowledge updates are
ongoing.

4.Cost-efficient always-on reasoning
As a lighter-weight reasoning model, BDH could serve as a default reasoning layer for
continuously running agents, escalating to larger models only when deeper analysis is
required.

The current system cleanly separates ingestion, indexing, and reasoning, allowing the
reasoning component to be upgraded without architectural changes when BDH becomes available.

##**Applicability Beyond Developer Tools**

The architecture generalizes because it operates on change events, not domain-specific semantics.

##**Conclusion**

LiveDoc Sentinel demonstrates a shift from static AI assistants to adaptive,
streaming-aware agents.
By combining Pathway’s real-time data processing with agentic reasoning, the system shows
how AI can remain trustworthy in environments where knowledge never stands still.





