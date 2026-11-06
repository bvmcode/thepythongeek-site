# AI News — Thursday, November 5, 2026

A short briefing of the day's main stories.

## OpenAI ships GPT‑6 Cyber — and aims it at the Linux kernel

OpenAI released GPT‑6 Cyber, built to find, validate and exploit vulnerabilities — rated Critical, up from High, under its own Preparedness Framework. ExploitGym: 48.5 percent vs 32.1 for GPT‑5.6 Cyber. A new black-box web-pentest eval: 40.3 percent recall vs Astra's 32 — and Cyber completed 95 percent of remote-exploit tasks Astra refused entirely. Access stays gated to approved Daybreak Red accounts, with scope-keeping holding at 99.93 percent on honeypot tests. The companion "A thousand fewer paths to root" report runs it through an autonomous Linux pipeline: 2,308 candidate findings → 1,724 dynamically reproduced bugs → 948 local privilege-escalation exploits plus drafted patches, for ~$1.2M of API credit, plus 81 high-severity Firefox flaws (Mozilla fixes shipped). Counters: the 948 counts patches not bugs, ~24 OpenAI-linked commits reached mainline, and the bounty math assumes payouts those programs don't offer.

- [GPT‑6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/)
- [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/)
- [The counters](https://sxz.io/openai-thousand-fewer-paths-to-root-948-patches-24-mainline-commits-bounty-math)

## Google ties Search to AI in schools, then hits the backlash

Google announced November 3: Gemini and Search go off by default in K‑12 Classroom accounts — and schools rejecting AI entirely also lose Search, because "search and AI are deeply integrated," VP Chris Phillips told the Times. Sanders called it extortion; Lina Khan, "an unregulated monopolist controlling an essential service." Google retreated within hours — per-product controls — but executives still call Search and AI inseparable, and districts allowing AI get two flavors of AI-augmented search from early 2027. Bundling an essential utility to push AI adoption is either a product decision or a legal exhibit.

- [TechCrunch](https://techcrunch.com/2026/11/04/google-faces-backlash-for-plan-that-would-turn-off-search-for-schools-that-restrict-ai/)
- [NYT](https://nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html)

## Cognition's SWE‑2 Flash: mid-training turns Inkling‑Small into a coder

Cognition shipped SWE‑2 Flash, a 276B-total/12B-active MoE built on Thinking Machines' Inkling-Small, and the recipe is the story: a first-ever mid-training stage (a few trillion tokens, three stages) before RL lifts Terminal-Bench 4.0 from 0.9 to 20.0 percent and FrontierCode 2.0 from 3.2 to 24.0 — though SWE‑2 still wins Terminal-Bench 4.0 (27.3) and DeepSWE (73.0 vs 60.1). It runs ~200 tok/s at a fifth of SWE‑2's price, free through November. The "best American open-weight coder" claim holds — Chinese open coders rate far higher (DeepSeek V4.1 Flash 1017: 42.3 on TB4.0). Weights stay gated (ExploitBench 11.3→34.8 explains why).

- [Cognition](https://cognition.ai/blog/swe-2-flash)

## Images 2.6: GIFs from a prompt, on 4 billion images a week

OpenAI's Images 2.6 shipped November 4 across ChatGPT, Codex and the API: animated GIFs from a prompt or photo with speed control (0.5–2x) and per-frame editing, 50 percent faster generation, and two API models — Flare (a low-quality image in six seconds) and Sunburst (higher fidelity, better edit consistency). Developers get image markup, SVG export, a "complexity" planning dial, and saved reference images for consistent characters. Users now generate 4 billion images a week — up from 3 billion in September.

- [OpenAI](https://openai.com/index/introducing-images-2-6/)

## Axiom machine-checks all 7,500 pages of algebraic geometry

Axiom released a Lean formalization of the entire Stacks Project — roughly 7,500 pages, ~16 million lines of machine-checked Lean covering the foundations of modern algebraic geometry, the largest formalized-math library ever built, assembled by AI-agent swarms proving thousands of theorems in parallel. Permanent Stacks tags link every Lean declaration back to the canonical text. If AI generates mathematics faster than humans can read, formal verification is the receipt.

- [Axiom](https://axiommath.ai/research/the-stacks-project-formalized/)

## Baidu publishes ERNIE 5.5 Flash Base — deliberately raw

Baidu put ERNIE-5.5-Flash-Base on Hugging Face: a 280B MoE (14B active) pre-trained on 33.5 trillion tokens and shipped with nothing after it — no fine-tuning, no post-training — in FP8 and BF16 as a clean fine-tuning starting point. Training context is 128K; Baidu's self-run comparisons claim wins on 24 of 30 base-model benchmarks (MMLU‑Pro 78.4 vs DeepSeek-V4-Flash-Base's 69.2) but a loss on HELMET-Rerank (56.2 vs 60.0). A post-trained version follows.

- [The Decoder](https://the-decoder.com/baidu-releases-ernie-5-5-flash-base-with-280-billion-parameters-as-an-open-source-foundation-model/)

## Also in tech

- **Ant's Ling-3.1-flash open weights** — a MoE tuned for rapid UI/code prototyping (React Native screens, SVG, web 3D), 1M context. ([Source](https://www.thenextgentechinsider.com/pulse/ant-ling-releases-ling-31-flash-open-source-moe-model-for-rapid-prototyping))
- **Pangram Image 1.0** — AI-image and video detection, heatmaps locate where AI content sits inside real photos, robust to edits/compression/low-res; Chrome extension plus API. ([Pangram](https://www.pangram.com/blog/introducing-pangram-image-1-0))
- **Anthropic open-sources FlashProve** — with EPFL/MIT/StarkWare: cryptographic proof a given model produced a given output, ~110 proved tokens/sec on an H100 at 72–94x vLLM's cost; tested on Llama 4 Maverick, weights withheld. ([Help Net Security](https://www.helpnetsecurity.com/2026/11/04/anthropic-flashprove-provable-inference/))

## Business roundup

- **The AI trade cracked** — Nasdaq fell 5.2 percent Thursday, ~$3T erased, worst day since April 2025; Nvidia down ~8–9 percent, AMD 17, Micron 17, Sandisk 22. ([Fortune](https://fortune.com/2026/11/05/tech-stocks-are-suffering-the-biggest-selloff-since-covid-as-investors-see-premature-end-to-ai-datacenter-boom))
- **Voters pulled the plug** — data-center opponents won 37 of 38 decided ballot contests (Redbud); Ohio restricted in 14+ municipalities, Piqua (Meta's planned $1B, 1.4GW campus) recalled its mayor and two commissioners, and Texas elected Gina Hinojosa on a buildout-moratorium platform. ([Fortune](https://fortune.com/2026/11/04/voters-pull-the-plug-on-big-techs-data-center-boom/))
- **OpenAI's data-center peace offering** — no NDAs on negotiations, pay full power and grid-upgrade bills, publish per-facility water and electricity use, community input first, low-water cooling; it wants the pledges made binding rules. ([Bloomberg via Fortune](https://fortune.com/2026/11/05/openais-dots-are-coming-up-against-the-price-of-privacy-and-the-price-of-compute))
- **Menlo Ventures: $177B** — enterprise AI spend hit $177B in the year to September; agents are 80 percent of usage, AI labs capture 69 cents of every dollar, Anthropic leads a two-horse race. ([Menlo](https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/))
- **Tenspresso** — three months old, 15 people, ex-Google-TPU founders, in talks for ≥$50M at ~$500M weeks after a $20M Striker round. ([Bloomberg via BigGo](https://finance.biggo.com/news/7b02489b-ab9e-4fb8-a448-3d2e4b2b8dab))
- **Isomorphic Labs** — DeepMind's drug-discovery spinout in talks for ~$5B at ~$50B, five months after a $2.1B round. ([Bloomberg via Yahoo](https://uk.finance.yahoo.com/news/isomorphic-labs-talks-5-billion-225144910.html))

## Also noted

- **Uber quantified agentic commerce: 4 rides** — Uber says third-party AI agents booked four trips and ~500 Eats orders in the busiest Halloween week. ([TechCrunch](https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/))
