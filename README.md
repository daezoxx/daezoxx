<div align="center">

<img src="./assets/hero.svg" alt="ZAEX. AI Systems Engineer, Regulatory Intelligence. Tax and compliance answers that survive an audit. AI Engineer at AskSolique. Retrieval: BM25 plus kNN, RRF fused. Grounding: span-level citations. Output: schema-validated. Background: 300M+ player-visit systems." />

</div>

Ask a tax question. Get an answer with a citation. Sounds simple.

Now make it true for Indian tax law, where the statute was amended in 2017, three benches disagree, and the circular that settles it landed last March.

That is the problem I work on.

**AI Engineer at AskSolique.**

---

## What I actually build

Most AI answers are confident. Very few are checkable.

I build the part that makes them checkable. Retrieval that knows a Supreme Court judgment outranks a practitioner's note. Fusion that knows the amendment replaced the rule it amended. A citation guard that reads the finished answer, finds the claim, and blocks it when the cited source does not actually say that.

The model is the easy part. The evidence is the whole job.

---

## System architecture

<div align="center">

<img src="./assets/regulatory-intelligence-architecture.svg" alt="Regulatory intelligence lifecycle. Stage 1, Acquire: sources (statutes, rulings, guidance, filings) flow into ingestion (connectors, scheduling, change detection), then parse and normalize (sections, tables, citations, references), then regulatory metadata (jurisdiction, authority, effective dates, version). Stage 2, Index: chunking and metadata strategy applied before write, feeding a sparse index (BM25 lexical matching on OpenSearch for statute numbers, defined terms and exact phrases) and a dense index (embeddings and kNN vector search for paraphrase and concept-level recall). Stage 3, Retrieve: query understanding (intent, expansion, jurisdiction and date scope), then hybrid retrieval (sparse and dense in parallel with metadata pre-filtering), then fusion (reciprocal rank fusion, dedup, authority weighting), then rerank (cross-encoder and LLM, precision at low k). Stage 4, Reason and decide: grounded reasoning (RAG over ranked evidence, citation-bound generation), then structured decision (classification, risk scoring, confidence and abstention), then provenance record (span-level citations, versions, trace id, immutable audit log). Offline evaluation feeds back into retrieval, fusion and rerank tuning. Stage 5, across every stage: evaluation, observability, guardrails, versioning, confidence, human review." />

</div>

`sources → ingestion → parse & normalize → regulatory metadata → sparse + dense indexes → query understanding → hybrid retrieval → RRF fusion → rerank → grounded reasoning → structured decision → provenance record`

---

## Why this is not just semantic search

**Not all sources are equal.** A Supreme Court judgment and a practitioner's note are both text. Only one of them ends an argument.

**"What is the rule" is an incomplete question.** The complete one ends with "as at when".

**Right document, wrong version, still wrong.** Amendments supersede. Retrieval has to know the date, not just the topic.

**Sources disagree, and that is normal.** Averaging two conflicting authorities gives you an answer that is true nowhere. Surface the conflict instead.

**A citation is not a link.** It is a span of text that contains the claim. Anything looser is decoration.

**Sometimes the right answer is "not enough evidence".** Thin retrieval should lower confidence, not raise word count.

---

## Failure modes and the controls that stop them

<div align="center">

<img src="./assets/engineering-console.svg" alt="Regulatory retrieval failure modes mapped to engineering controls. Superseded rule retrieved as current is prevented by effective-date and version-aware filtering. Conflicting authorities ranked equally is prevented by source-authority weighting during fusion. Citation does not support the claim is prevented by span-level grounding verification. High confidence on thin evidence is prevented by coverage-aware scoring and abstention. Prose output breaking downstream systems is prevented by schema-validated structured output. Silent regression after a config change is prevented by offline evaluation gates before deploy." />

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
| **Retrieval** | BM25 · kNN vector search · reciprocal rank fusion · query expansion · metadata and date filtering · cross-encoder and LLM reranking |
| **Reasoning** | RAG orchestration · multi-agent deliberation · planner and researcher agents · structured generation · tool calling · citation guards |
| **Data** | Regulatory parsing · ETL · chunking and metadata strategy · lineage · PostgreSQL · OpenSearch |
| **Reliability** | Blinded LLM evaluation harnesses · guardrails · provenance · audit trails · distributed tracing · PII redaction |
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

## Where the instinct came from

Before tax law, I built games.

Roblox systems across experiences with more than **300 million player visits**. Real-time multiplayer state. Distributed events. Economies that break the instant one number is wrong.

People assume that was a different career. It was the same one. A desynced game state and an unsupported tax answer fail in exactly the same way: quietly, confidently, and only in front of the person who checks.

**M.Sc. Computer Games Technology**, University of London.

---

## What I am working on now

- Evaluation harnesses that catch a retrieval regression before it reaches anyone
- Reranking that weighs authority and recency, not just similarity
- Confidence that means something, and abstention that triggers when it should
- Provenance that survives multi-step reasoning instead of dissolving in it
- Safety boundaries for agents that call tools inside regulated workflows

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
