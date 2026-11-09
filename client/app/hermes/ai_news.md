# AI News — Sunday, November 8, 2026

A short briefing of the day's main stories.

## Claude Code's "don't ask again" archives plaintext secrets — 2,539 now sit on public GitHub

Ask Claude Code to check a database and the proposed command carries whatever secret it needs; pick "Yes, and don't ask again," and it saves that literal command — password and all — to `.claude/settings.local.json`, a file nothing in the repo marks private. Apiiro's scan (collected Nov 1–3; reporting broke Nov 7) found 104,185 public copies across 103,617 repos; 1,122 hold a real secret — 379 database passwords, 43 SSH logins, 42 repo/npm tokens, 23 AWS keys across 63 organizations — and one notified company confirmed a live key. Counting history, shared settings files and agent logs, 2,539 secrets hit 1,994 repos. Anthropic's guard — the user's global git excludes — lives on one machine and misses committed files; half sat on default branches 217+ days. Fix: rotate first, untrack with `git rm --cached`, move secrets into `$VAR`s, approve patterns over literals.

- [Apiiro research](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)
- [The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

## Alibaba's Co-Design Bench: agents fully finish one change request in four

Built from real coding sessions — change requests users actually had to rephrase or roll back — Co-Design Bench leaves the best of ten models, GPT-6 Astra, fully completing just 26.4 percent while hitting about 70 percent of requirements on average; older benchmarks score that model class above 99. One AI judge tests the app in a browser; a second re-checks every pass for hardcoded mock-ups. Scores sag when a task mixes three or four kinds of change, and compute doesn't rescue it: GLM-5.2 burns nearly six times Astra's tokens and still scores worse. The harness matters as much as the model — Qwen3.8-27B scored 75 or 56 percent on large overhauls depending only on which harness ran it — so pair model and environment when you buy.

- [Paper (arXiv)](https://arxiv.org/abs/2610.35138)
- [The Decoder](https://the-decoder.com/ai-coding-agents-still-need-human-cleanup-on-nearly-three-out-of-four-tasks-in-a-real-world-test/)

## Vals' CyberOffense: agents break corporate networks — open models close to a tenth the cost

Vals AI hands each agent a solo Kali box and one public web address; everything after is unsupervised attack on a simulated corporate network. OpenAI's restricted GPT-6 Sol (Daybreak) posted the best aggregate, 80.8 percent of objectives — but open-weight DeepSeek V4.1 Flash reached 72.8 percent at roughly $3 per run against $22. In Lighthouse, Daybreak took the first company's admin, stole passwords and entered a second company — 27 of 31 objectives in under three hours; DeepSeek got 21 at a tenth the cost. Most models went nowhere until past 100 million tokens, so short tests understate open-weight potential; UK AISI put the open/closed gap at 4–7 months, with runs at $1.19 vs $85 for Opus 4.5.

- [Vals AI: CyberOffense](https://www.vals.ai/benchmarks/cyber_offense)
- [The Decoder](https://the-decoder.com/the-gap-between-open-and-closed-ai-models-in-cyber-capabilities-keeps-shrinking/)

## Nous strips Chinese state propaganda from Qwen3.8-27B with 53 million tokens

Nous Research fine-tuned Alibaba's 27B open-weight model into Arete-27B and reports the propaganda rate fell from 22 percent to under one, capabilities intact, on just 53 million tokens of fine-tuning over 803 prompts. The finding: the political layer is "applied late, it is applied thin" — a patch, not something baked into the weights. Model and data are public. The corollary: residual Chinese-flavored bias showed up even in Nvidia's Nemotron line — corpora carry politics you didn't choose.

- [Nous Research](https://nousresearch.com/arete)
- [The Decoder](https://the-decoder.com/state-propaganda-in-some-chinese-ai-models-is-only-a-thin-layer-that-fine-tuning-can-strip-away/)

## Inside China's answer to Stargate: an 800MW campus built in a year at $3M per MW

SemiAnalysis toured Envision Group's Galaxy campus in Ulanqab, Inner Mongolia — planned for 800MW, the size of Stargate Abilene's core, built-to-suit for two internet giants. The first 120MW phase went up in under twelve months at about one-fifth of US construction cost (under $3M per MW), full campus due end-2027, plus 22 projects and 30,000 workers nearby. Envision plans to cover over 60 percent of early-phase power with 420MW of dedicated wind; a 5MW pilot hall runs solid-state transformers taking 10kV AC straight to 800V DC at the rack. Power runs ~$0.055/kWh, 25GW announced region-wide — while US sites fight anti-datacenter politics.

- [SemiAnalysis](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner)

## Also in tech

- **Google marks agent-to-agent communication stable** — ADK 2.14.0 graduates the A2A protocol, execution environments, evaluation and core runtime to stable; claims 23 percent faster multi-turn runs. ([PyPI](https://pypi.org/project/google-adk/2.14.0/))
- **AI auditors flood reviewers with false alarms** — a study by Anthropic Institute's Andy Hall (the Decoder, Nov 7) finds GPT-5 catches ~98 percent of reward hacking at a 5 percent false-alarm rate, but 99 percent detection makes the best model flag 15 percent of clean logs; newer models audit no better. ([Free Systems](https://freesystems.substack.com/p/were-using-ai-to-audit-ai))

## Business roundup

- **Nvidia's board probes CEO Jensen Huang** — he admitted Sunday an affair with a Megaspeed executive whom US intelligence called an MSS recruit targeting him; the board sees no evidence secrets were compromised. ([TechCrunch](https://techcrunch.com/2026/11/08/nvidia-says-its-investigating-ceo-jensen-huangs-relationship-with-possible-chinese-spy/), [Nvidia](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors))
- **Anthropic pushes a pre-Thanksgiving IPO** — targeting $80–100B at a $1.25–1.75T valuation (optimists wanted ~$2T); buyers now weigh $1.1–1.3T. ([Decoder/FT](https://the-decoder.com/anthropic-pushes-ahead-with-pre-thanksgiving-ipo-despite-tech-selloff-accepts-lower-valuation/))
- **OpenAI's first $11B close lands at $1.25T** — below the $30B at $1.4T it sought in September; CFO Sarah Friar confirmed the price; could reach ~$20B. ([TechCrunch](https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/))
- **Anthropic buys $3.4B of gas generators** — the late-September deal takes over 1.7GW of Caterpillar-ordered capacity, plus engineering and installation. ([CNBC/FT](https://www.cnbc.com/2026/11/08/anthropic-generator-deal-ai-data-centers.html))
- **The chip shortage is back, says Microchip** — AI buyers "took over the whole factory" at test houses; its data-center segment grew 55.7 percent as shares fell 10 percent. ([247wallst](https://247wallst.com/investing/2026/11/07/the-chip-shortage-is-back-and-microchip-says-ai-customers-are-crowding-everyone-out/))
- **Schools adopt AI in place of hiring teachers** — Stanford's SCALE Initiative calls learning-gains evidence "extremely limited"; NYC bans K-8 classroom use. ([Truthout](https://truthout.org/articles/ai-companies-are-preying-on-under-resourced-schools-students-say))

## Also noted

- **Tencent's AI chief: models near "mastering biology"** — Yao Shunyu says cyber and bio abilities near a harm threshold; open weights multiply the risk. ([SCMP](https://www.scmp.com/tech/big-tech/article/3373697/ai-will-soon-master-biology-unleashing-new-safety-risks-tencent-ai-chief-warns))
- **A 284B DeepSeek model on a 64GB CPU-only box** — llama-modchip claims DeepSeek-V4-Flash in under 59GiB RAM at 9.1–14.7 tok/s, no GPU (self-benchmarked). ([GitHub](https://github.com/synchopate/llama-modchip))
- **"Agent memory needs its OpenTelemetry moment"** — LoreKit pitches a shared four-layer memory spec under the Linux Foundation's Agentic AI Foundation. ([LoreKit](https://www.lorekit.io/blog/open-agent-memory-format))
