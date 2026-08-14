<div align="center">

<img src="./assets/hero.svg" alt="ZAEX. AI Engineering Lead, Commerce Intelligence. Enterprise data turned into answers you can trace. Eng Lead (AI) at OJCommerce. Retrieval: BM25 plus kNN, RRF fused. Grounding: span-level citations. Output: schema-validated. Background: 300M+ player-visit systems." />

</div>

Ask what a product costs. Get an answer with a source. Sounds simple.

Now make it true across an enterprise data lake, where the ERP, the vendor feed and the marketplace listing all describe the same product differently, and two of them are a day stale.

That is the problem I work on.

**Lead - Software Engineering (AI) at OJCommerce.**

---

## What I actually build

Most AI answers are confident. Very few are checkable.

I build the part that makes them checkable. Retrieval that knows the ERP record outranks a scraped description. Fusion that knows the newer feed supersedes the row it replaced. A citation guard that reads the finished answer, finds the claim, and blocks it when the cited record does not actually say that.

The model is the easy part. The evidence is the whole job.

---

## System architecture

<div align="center">

<img src="./assets/retrieval-architecture.svg" alt="Context lake retrieval lifecycle, summarised in the header as data lake, retrieval, decision, trace. Stage 1, Acquire: sources (catalog, orders, pricing, vendors, docs, content) flow into ingestion (connectors, scheduling, change detection), then parse and normalize (sections, tables, attributes, identifiers), then context metadata (domain, source system, freshness, version). Stage 2, Index: chunking and metadata strategy applied before write, feeding a sparse index (BM25 lexical matching on OpenSearch for SKUs, brand names and exact part numbers) and a dense index (embeddings and kNN vector search for paraphrase and concept-level recall). Stage 3, Retrieve: query understanding (intent, expansion, category and freshness scope), then hybrid retrieval (sparse and dense in parallel with metadata pre-filtering), then fusion (reciprocal rank fusion, source-of-truth weighting), then rerank (cross-encoder and LLM, precision at low k). Stage 4, Reason and decide: grounded reasoning (RAG over ranked evidence, citation-bound generation), then structured decision (classification, ranking signals, confidence and abstention), then provenance record (span-level citations, versions, trace id, immutable event log). Offline evaluation feeds back into retrieval, fusion and rerank tuning. Stage 5, across every stage: evaluation, observability, guardrails, versioning, confidence, human review." />

</div>

`sources → ingestion → parse & normalize → context metadata → sparse + dense indexes → query understanding → hybrid retrieval → RRF fusion → rerank → grounded reasoning → structured decision → provenance record`

---

## Why this is not just semantic search

**Not all sources are equal.** The ERP record and a scraped description are both text. Only one of them settles a dispute.

**"What is the price" is an incomplete question.** The complete one ends with "as at when".

**Right product, wrong version, still wrong.** A newer feed supersedes an older one. Retrieval has to know the timestamp, not just the topic.

**Sources disagree, and that is normal.** Averaging two conflicting records gives you an answer that is true nowhere. Surface the conflict instead.

**A citation is not a link.** It is a span of text that contains the claim. Anything looser is decoration.

**Sometimes the right answer is "not enough evidence".** Thin retrieval should lower confidence, not raise word count.

---

## Failure modes and the controls that stop them

<div align="center">

<img src="./assets/engineering-console.svg" alt="Enterprise retrieval failure modes mapped to engineering controls. Stale catalog data served as current is prevented by freshness windows and change-data capture. Source systems disagreeing on one product is prevented by source-of-truth precedence during fusion. A cited source that does not support the claim is prevented by span-level grounding verification. High confidence on thin evidence is prevented by coverage-aware scoring and abstention. Prose output breaking downstream systems is prevented by schema-validated structured output. Silent regression after a config change is prevented by offline evaluation gates before deploy. The two columns are headed what goes wrong and what prevents it. Footer: an answer is only as good as the evidence it can show and the ranking it can justify." />

</div>

---

## How I work

**Retrieval before generation.** When the answer is wrong, the evidence was usually wrong first.

**Evidence before confidence.** A score with no passages behind it is a guess with better formatting.

**Evaluation before deployment.** Blind the judge, run the set, compare, then ship.

**Structure over prose.** If a machine reads it next, hand it a schema, not a paragraph.

**Provenance by default.** Sources, versions, trace id. Every answer, every time.

**Escalate, do not decide.** When the stakes are real, the system's job is to put evidence in front of a human.

---

## Capabilities

| Domain | Detail |
| :--- | :--- |
| **Retrieval** | BM25 · kNN vector search · reciprocal rank fusion · query expansion · metadata and freshness filtering · cross-encoder and LLM reranking |
| **Reasoning** | RAG orchestration · multi-agent deliberation · planner and researcher agents · structured generation · tool calling · citation guards |
| **Data** | Data lake ingestion · catalog and document parsing · ETL · chunking and metadata strategy · lineage · PostgreSQL · OpenSearch |
| **Reliability** | Blinded LLM evaluation harnesses · guardrails · provenance · immutable event logs · distributed tracing · PII redaction |
| **Delivery** | Python · FastAPI · SSE streaming · async pipelines · Docker |
| **Scale** | Real-time systems · concurrent state · event-driven architecture · low-latency engineering · Luau |

<div align="center">

![Python](https://img.shields.io/badge/Python-22D3EE?style=flat-square&logo=python&logoColor=22D3EE&labelColor=0B1020)
&nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-A78BFA?style=flat-square&logo=fastapi&logoColor=A78BFA&labelColor=0B1020)
&nbsp;
![OpenSearch](https://img.shields.io/badge/OpenSearch-F0B429?style=flat-square&logo=opensearch&logoColor=F0B429&labelColor=0B1020)
&nbsp;
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-34D399?style=flat-square&logo=postgresql&logoColor=34D399&labelColor=0B1020)
&nbsp;
![Docker](https://img.shields.io/badge/Docker-22D3EE?style=flat-square&logo=docker&logoColor=22D3EE&labelColor=0B1020)

</div>

---

## Games

I build games. That is not a line on a timeline, it is the thing that taught me systems.

Roblox experiences with more than **300 million player visits**. Authoritative servers. Real-time multiplayer state. Distributed events. Economies that break the instant one number is wrong.

Here is the problem every multiplayer game has to solve. The server sends state a few times a second. Move a character to each position as it arrives and the motion is unwatchable. So you hold a buffer, interpolate between the positions, and accept that you are always rendering slightly in the past.

<div align="center">

<img src="./assets/realtime-systems.svg" alt="Animated netcode diagram. A fixed-timestep server tick strip pulses across the top. The middle lane shows an entity snapping between the eight discrete positions the server sent. The bottom lane shows the same entity interpolated into continuous motion, trailing the raw snapshots by exactly one tick. Caption: one tick of buffer buys smooth motion, choosing what to trade is the job. Concepts: authoritative server, client prediction, lag compensation, deterministic state, event ordering." />

</div>

The gold square is the truth. The green square is a lie, one tick stale, and it is the one players want. Every real-time system is a negotiation like that.

None of this stopped being useful. A desynced game state and an ungrounded product answer fail in exactly the same way: quietly, confidently, and only in front of the person who checks.

**M.Sc. Computer Games Technology**, University of London. Luau, real-time state, ML-driven mechanics, economy design.

---

## What I am working on now

- Evaluation harnesses that catch a retrieval regression before it reaches anyone
- Reranking that weighs source authority and freshness, not just similarity
- Confidence that means something, and abstention that triggers when it should
- Provenance that survives multi-step reasoning instead of dissolving in it
- Safety boundaries for agents that call tools inside live commerce workflows

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
