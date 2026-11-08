# AI News — Saturday, November 7, 2026

A short briefing of the day's main stories.

## An 18-year-old quantum conjecture, proved by AI

Aaronson–Ambainis asked whether quantum machines win exponentially on random inputs — one of the field's central open problems since 2008, reduced to polynomials: a varying low-degree polynomial must have an influential bit. On November 6, Physical Superintelligence announced that an internal research system, running instances of a non-public Anthropic model, had a complete proof on day three of a run, with the Lean checker accepting every step, then improved the bound twice more. Caveats: it limits input reads, not total compute; Lean-verified, not journal-reviewed; the Anthropic model unnamed. But the pattern is METR's AI-R&D acceleration thesis, demonstrated.

- [PSI](https://psi.inc/research/aaronson-ambainis/)

## DeepMind's AI-found attacks on legacy 1024-bit RSA

DeepMind announced November 6 that AI models, working under human direction, found two weaknesses in legacy 1024-bit RSA — the retired key size (today's 2048-bit keys are unaffected). One: signature forgery, via an algorithm claimed to beat the previous best attack by ~1,600x when the attacker controls only part of the signed data. Two: related-moduli batch factoring made ~30x cheaper per additional key. DeepMind researchers did the work with cryptographers Heninger and Thomé — the numbers are DeepMind's claims, unverified. But the shape is proven: a UCSD/Inria paper (IACR ePrint 2026/2131) forged a real 1024-bit signature through an HSM's black-box API — 1,380 core-years, 232 oracle queries — and reads RSA's signing-oracle security 15–30 bits below factoring estimates.

- [Crypto Briefing](https://cryptobriefing.com/google-deepmind-ai-rsa-1024-bit-weaknesses/)

## Grok API's default text watermarking turns on today

As of today, seven Grok API models — grok-4.7 through 4.3 plus the 4.20 variants — return statistically watermarked text by default across Responses and Chat Completions. The mark steers token choices during generation, so copied strings look ordinary; the only visible signal is an `x-watermark: true` response header. xAI posted the policy October 31 and is blunt about why: EU AI Act compliance. Opt-out is deliberately friction-heavy — team admins only, per model, a confirmed legal exception and sole responsibility; changes propagate in five minutes and are audit-logged. Consumer surfaces are untouched, so API users carry the weight: log that header now.

- [xAI developer docs](https://docs.x.ai/developers/advanced-api-usage/watermarking)

## Raw lab imagery still defeats AI: two new benchmarks agree

Two lab-work benchmarks landed the same day, agreeing. OpenAI's BioBasicsBench (with biotech Ligo, Nov 6) is 100 tasks built from raw bench evidence: gels, cytometry files, FASTQs, technique videos. At top effort, GPT-6 Astra averaged 66.7 percent on ~4,700 output tokens per task versus GPT-5.6 Sol's 43.8 on ~9,100. Given a mislabeled control plate, Sol trusted it; Astra read the rim label and rejected it. Artificial Analysis' VIALS-AA launched the same day on Handshake AI's 161-task science-image benchmark, on pass^3: Gemini 4 Carbon (high) 64, GPT-6 Astra (max) 63, Claude Opus 5.5 61 — while open-weights Kimi K3.1 Pro solves about three-quarters of tasks at least once and only 45 percent every time. Paper-figure benchmarks saturate; raw bench reality doesn't.

- [OpenAI: BioBasicsBench](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/)
- [Artificial Analysis: VIALS-AA](https://artificialanalysis.ai/articles/vials-aa)

## How Claude should remember — and Anthropic's "dreaming"

Anthropic's engineering post "The components of agent memory" (Nov 6) defines memory narrowly — knowledge Claude keeps between sessions as text it can reread later, excluding weight updates and compaction. Measured on CL-Bench, each question starting fresh with only the memory folder persisting, Opus 5.5 rose from 0.655 to 0.838 mean reward. "Dreaming" is the mechanism: an offline pass that rereads transcripts, corrects bad notes, builds wikis, and curates what loads next. In Pokémon Red: one Sonnet 3.7 run wrote 413 files and earned one badge; Fable 5 kept ~10 files, mostly strategy, and earned four; Opus 5.5 finished the game on a small goals folder. And the traveling rule: "tell Claude what memory is for, not how to use it" — dictation makes strong models worse.

- [Anthropic Research](https://www.anthropic.com/research/components-of-agent-memory)

## Wonder-trained models roll out to every Muse and Meta AI user

Meta announced November 6 that Muse and Meta AI switch to "specialized" versions of their models, trained with learnings from Muse Wonder — the October 12 frontier family. Active Memory separates temporary from permanent facts and catches staleness: 2.4x less forgetting, critical context correct in 90 percent of tasks, Personal Superintelligence Index up 38→47 percent. Active Focus trains on hard bottlenecks to persist, recover or find alternatives — 67 percent better where surprises arise. No model card; self-reported numbers, not a documented release. The direction: frontier behavior pushed into the default assistant, not a bigger model shipped outward.

- [Meta AI Research](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai)

## Also in tech

- **NVIDIA opens four Cosmos 3 world models** — post-trained 16B Cosmos 3 Nano checkpoints (OpenMDW 1.1): Transfer-Auto, Sim-Auto, Sim-Bimanual — open driving/robotics data generation; NVIDIA says policy-learning support "remains to be measured." ([Hugging Face](https://huggingface.co/collections/nvidia/cosmos3))
- **OpenAI deputizes Hacktron** — partners the AI-security startup to jointly attack its own systems, third-party seams first, with Daybreak Red model access. ([Hacktron](https://www.hacktron.ai/blog/openai-partnership))
- **Terminal-Bench 2.1** — a Stanford/Cornell audit (arXiv, Nov 5) found ~30 percent of Terminal-Bench 2.0's 89 tasks defective; repairs moved 19 re-run agents' scores up to ~12 points and ranks by three while order held. ([arXiv](https://arxiv.org/abs/2611.08417))

## Business roundup

- **Microsoft winds down its Oracle deal** — won't renew the 2023 Oracle rental for AI-powered Bing (Bloomberg, Nov 6); $80B+ in external AI-cloud contracts are under review. ([Santage](https://santageai.com/news/2026/11/07/microsoft-oracle-older-nvidia-gpus))
- **OpenAI presses on post-midterms** — voters backed limits in 40 of 41 ballot questions; CFO Sarah Friar told CNBC investment continues; its compact now pledges full grid-cost payment, financial assurances and an NDA ban for public officials. ([CNBC](https://www.cnbc.com/2026/11/06/open-ai-data-centers-election.html))
- **Agent-security M&A** — Palo Alto Networks reportedly negotiating ~$500M for Clutch and separate talks for Beacon — its seventh acquisition of 2026. ([Calcalist](https://www.calcalistech.com/ctechnews/article/4sjcl3ooj))
- **Packaging is the next chip bottleneck**: advanced-packaging demand exceeds capacity; Yole sees its revenue passing traditional in 2026 on ~$28B capex, AMD $10B+ into Taiwan packaging. ([Euronext/Reuters](https://live.euronext.com/en/financial-news/ai-boom-turns-chip-packaging-next-battleground-semiconductors))
- **Physicl raises $10M** — to close robotics' sim-to-real gap. ([AI Daybook](https://sguys99.github.io/global-ai-news/en/article/1404))
- **UK banks: AI gains real but narrow** — KPMG: over half have an AI use case with measurable results, but gains stay "concentrated in specific functions." ([HotMinute](https://hotminute.co.uk/2026/11/07/uk-banks-invest-in-hiring-as-benefits-from-ai-remain-elusive/))

## Also noted

- **A law professor's cautionary tale** — U Chicago's William Baude asked Claude to renumber pages; during lunch it deleted his syllabus and a year of lecture notes, admitted it deleted the files through its own carelessness, and only a Dropbox copy saved them. ([AI Brief](https://dailyaibrief.com/news/claude-deletes-law-professor-lecture-notes-syllabus-ko0Q7RCk))
