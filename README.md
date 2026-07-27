<div align="center">

<img src="./assets/hero.svg" alt="ZAEX — AI Systems Engineer, Regulatory Intelligence. Hybrid retrieval and grounded reasoning for high-stakes compliance decisions. AI Engineer at AskSolique. Retrieval: BM25 plus dense hybrid. Grounding: span-level citations. Output: schema-validated. Background: 300M+ player-visit systems." />

</div>

I build search and reasoning systems for regulatory work — the kind where an answer is worthless unless you can show which source it came from, which version of that source was in force, and why it outranked the alternatives.

Currently **AI Engineer at AskSolique**, working on retrieval and reasoning for tax and compliance.

---

## Current work

Regulatory corpora are fragmented, versioned, jurisdiction-bound, and routinely self-contradictory. The hard part is not generation — it is everything around it: deciding what evidence reaches the model, proving it was the right evidence, and recording the decision so it survives review months later.

My work sits across the whole path: ingestion and normalization, chunking and metadata strategy, sparse and dense indexing, query understanding, hybrid retrieval and fusion, reranking, grounded reasoning, structured decisions, and the provenance record that ties the answer back to its sources.

---

## System architecture

<div align="center">

<img src="./assets/regulatory-intelligence-architecture.svg" alt="Regulatory intelligence lifecycle. Stage 1, Acquire: sources (statutes, rulings, guidance, filings) flow into ingestion (connectors, scheduling, change detection), then parse and normalize (sections, tables, citations, references), then regulatory metadata (jurisdiction, authority, effective dates, version). Stage 2, Index: chunking and metadata strategy applied before write, feeding a sparse index (BM25 lexical matching on Elasticsearch for statute numbers, defined terms and exact phrases) and a dense index (embedding pipeline on Qdrant for paraphrase and concept-level recall). Stage 3, Retrieve: query understanding (intent, expansion, jurisdiction and date scope), then hybrid retrieval (sparse and dense in parallel with metadata pre-filtering), then fusion (rank merge, dedup, authority weighting), then rerank (cross-encoder and LLM, precision at low k). Stage 4, Reason and decide: grounded reasoning (RAG over ranked evidence, citation-bound generation), then structured decision (classification, risk scoring, confidence and abstention), then provenance record (span-level citations, versions, trace id, immutable audit log). Offline evaluation feeds back into retrieval, fusion and rerank tuning. Stage 5, across every stage: evaluation, observability, guardrails, versioning, confidence, human review." />

</div>

`sources → ingestion → parse & normalize → regulatory metadata → sparse + dense indexes → query understanding → hybrid retrieval → fusion → rerank → grounded reasoning → structured decision → provenance record`

---

## Why regulatory retrieval is not generic semantic search

- **Authority is ranked, not flat.** A statute, a binding ruling, and an explanatory note are not interchangeable evidence, and fusion has to know the difference.
- **Time is a filter, not a field.** "What is the rule" is an incomplete question without "as at when".
- **Versions supersede.** Retrieving the right document at the wrong revision is still a wrong answer.
- **Conflict is the normal case.** Sources disagree. The system should surface the disagreement, not quietly average it away.
- **Citations bind to spans.** A document-level reference is a pointer, not evidence.
- **Abstention beats a confident guess.** Where retrieval coverage is thin, saying so is the correct output.

---

## Failure modes and the controls that prevent them

<div align="center">

<img src="./assets/engineering-console.svg" alt="Regulatory retrieval failure modes mapped to engineering controls. Superseded rule retrieved as current is prevented by effective-date and version-aware filtering. Conflicting authorities ranked equally is prevented by source-authority weighting during fusion. Citation does not support the claim is prevented by span-level grounding verification. High confidence on thin evidence is prevented by coverage-aware scoring and abstention. Prose output breaking downstream systems is prevented by schema-validated structured output. Silent regression after a config change is prevented by offline evaluation gates before deploy." />

</div>

---

## Engineering principles

**Retrieval before generation.** Most problems blamed on the model are evidence problems.

**Evidence before confidence.** A score is meaningless without the passages standing behind it.

**Evaluation before deployment.** Retrieval changes ship behind offline gates, not intuition.

**Structure over prose.** Typed, validated output wherever another system consumes the result.

**Provenance by default.** Every answer carries its sources, their versions, and a trace id.

**Human review where consequences are material.** Automation should escalate, not quietly decide.

---

## Capabilities

| Domain | Detail |
| :--- | :--- |
| **Retrieval** | BM25 · dense vectors · hybrid fusion · query expansion · metadata filtering · cross-encoder and LLM reranking |
| **Reasoning** | RAG orchestration · structured generation · tool execution · confidence scoring · output validation |
| **Data** | Regulatory parsing · ETL · chunking and metadata strategy · lineage · PostgreSQL · Elasticsearch · Qdrant |
| **Reliability** | Retrieval evaluation · guardrails · provenance · audit trails · observability · governance |
| **Scale** | Real-time systems · concurrent state · event-driven architecture · low-latency engineering · Luau |

<div align="center">

![Python](https://img.shields.io/badge/Python-22D3EE?style=flat-square&logo=python&logoColor=22D3EE&labelColor=0B1020)
&nbsp;
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-A78BFA?style=flat-square&logo=elasticsearch&logoColor=A78BFA&labelColor=0B1020)
&nbsp;
![Qdrant](https://img.shields.io/badge/Qdrant-F0B429?style=flat-square&logo=qdrant&logoColor=F0B429&labelColor=0B1020)
&nbsp;
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-34D399?style=flat-square&logo=postgresql&logoColor=34D399&labelColor=0B1020)
&nbsp;
![Docker](https://img.shields.io/badge/Docker-22D3EE?style=flat-square&logo=docker&logoColor=22D3EE&labelColor=0B1020)

</div>

---

## Where the scale instinct came from

Before compliance systems, I built game systems on Roblox used across experiences with more than **300 million player visits** — real-time multiplayer state, distributed event handling, economy design and balancing, and ML-driven mechanics running under hard latency budgets.

That turned out to be good preparation for this. Both jobs are correctness under load with nowhere to hand-wave: a desynced game state and an unsupported compliance answer are the same class of failure — a system that looked fine right up until somebody checked.

**M.Sc. Computer Games Technology**, University of London.

---

## Current focus

- Retrieval evaluation harnesses that catch regressions before they reach production
- Reranking that respects source authority and recency, not just semantic similarity
- Calibrated confidence and principled abstention
- Provenance that stays intact through multi-step reasoning
- Safety boundaries for agentic tool use inside regulated workflows

---

## GitHub

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=daezoxx&bg_color=0B1020&color=E6EDF3&title_color=22D3EE&line=22D3EE&point=A78BFA&area_color=22D3EE&area=true&hide_border=true&radius=8&custom_title=Contribution%20Activity" alt="Contribution activity graph for GitHub user daezoxx over the past year." />

<br /><br />

<img src="./assets/streak.svg" alt="GitHub contribution streak for daezoxx: current streak, longest streak, and total contributions." />

</div>

---

## Contact

<div align="center">

[![Email](https://img.shields.io/badge/Email-dhanu%40dhanu.dev-22D3EE?style=flat-square&logo=maildotru&logoColor=22D3EE&labelColor=0B1020)](mailto:dhanu@dhanu.dev)
&nbsp;
[![Website](https://img.shields.io/badge/Website-dhanu.dev-A78BFA?style=flat-square&logo=firefoxbrowser&logoColor=A78BFA&labelColor=0B1020)](https://dhanu.dev/)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-progamedev-34D399?style=flat-square&logo=linkedin&logoColor=34D399&labelColor=0B1020)](https://linkedin.com/in/progamedev)

</div>
