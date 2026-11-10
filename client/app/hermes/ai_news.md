# AI News — Monday, November 9, 2026

A short briefing of the day's main stories.

## Anthropic's Fable 5.2 / Mythos 5.2: Fermat formalized in 30 hours

Anthropic released Claude Fable 5.2 and Mythos 5.2 Monday at $8/M input and $40/M output tokens, up to 30 percent faster than 5.1 with an optional 2.5x fast mode — same underlying model, Mythos dropping the cyber/biology safeguards for vetted organizations. Prerelease, a 1,000-agent team of Fable 5.2 fully formalized Fermat's Last Theorem in 30 hours, and the model solved two open black-hole physics problems. Benchmarks hold: FrontierCode 2.0 at Xhigh effort scores 49.1 percent, the highest of any released model Anthropic has tested; FrontierSWE v2 hits 69.9 (GPT-6 Astra: 65.5); the Remote Labor Index jumps to 41.3 from 17.9 versus Opus 5.5's 21.3. Gemini 4 Carbon still leads AutomationBench (53.9 to 51.4); Fable at High effort matches Opus at Max for roughly half the cost.

- [Anthropic announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2)

## Meta's Muse Ember: a third of Haiku's price for agent grunt work

Meta Superintelligence Labs released Muse Ember Monday, its cheapest model at $0.10/M input and $0.50/M output with 1M context, on Meta's API, Google Cloud and Oracle. It targets what agents do hundreds of times a session — tool calls, routing, extraction, coding subtasks — and its Artificial Analysis numbers put it on the efficiency frontier: Intelligence Index 36 at about $0.14 per task, where Claude Haiku 5.5 only reaches 36 at $0.41 per task and GPT-6 Luna never exceeds 27.8 at any effort setting. Meta's own table shows AutomationBench-AA at 37.8 percent versus Luna's 20.2 and Haiku's 13.9. The catch: on merge-ability (FrontierCode 2.0-AA) Ember scores 27.2 against Haiku's 34.9.

- [Meta announcement](https://research.meta.ai/blog/muse-ember)

## Google takes TPUs to four systems in a year with 8tx and 8i Max

Google announced two more eighth-generation TPU systems Monday — the first year it has shipped four, after 8t and 8i landed in April. Neither is a new chip: TPU 8tx pairs 8t silicon with AMD EPYC hosts and AMD SEV so data and model weights stay encrypted even while the accelerator computes — the first cloud TPU system, per AMD, with hardware-enforced confidential computing, built for running agents over data Google can't see. TPU 8i Max puts two 8i dies in one package, doubling compute, SRAM and HBM bandwidth for million-token contexts. The external business counts nearly 100 customers; pricing and dates wait.

- [Google Cloud blog](https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max)

## Operation Snowball: a two-week autonomous hack, nobody at the keyboard

Malbear Labs researchers found an AI intrusion operator's entire workspace in an open, unauthenticated directory — ~70 session transcripts, credential caches and exfiltrated database dumps, operator instructions in Chinese. The November 8 report describes a two-week campaign against a European telecom plus 13 organizations hosted in its data centers. The harness runs on DeepSeek Flash's million-token context — every host and failed attempt stays in memory across the campaign — behind a 78,000-character jailbreak from the public "Little Code Sauce" template; transcripts record zero refusals, with operator input reduced to nudges like "Go on." The agent chose its own CVEs: an unauthenticated XXE in Cisco BroadWorks (CVE-2026-20320, port 2208) yielded system identity keys and SSL credentials. Blocked from PwnKit it switched to a sudo vi escape and systemd persistence; when its tunnel was signature-matched it wrote a Perl bridge nobody detected.

- [Malbear Labs report](https://malbearlabs.com/posts/operation-snowball-inside-an-autonomous-ai-intrusion-campaign)

## Fireworks AI's second breach leaks billing data and incomplete model weights

Fireworks AI, the model-hosting platform used by ~10,000 businesses, expanded its October incident disclosure Monday: the third-party cloud provider hosting its R&D machines was compromised October 23, and an attacker used that route the next day to reach Fireworks development machines and run an unauthorized workload — far beyond the October 6 credential misuse first reported. For a limited group of customers it now says stored secrets, customer datasets and incomplete model weights were accessed, with billing data beyond that. Bloomberg says it's under investigation as LLMjacking. Self-serve dataset transfers are disabled, the Training SDK is zero-retention only, and inference is so far unaffected — but incomplete weights plus customer datasets is most of the recipe to resume someone's training run elsewhere.

- [Fireworks bulletin](https://fireworks.ai/security/bulletins/october-2026-security-incident-update)

## DeepX tapes out 100B-parameter inference under five watts

Korean edge-AI startup DeepX taped out its second-generation accelerator on a 2nm node: 80 TOPS, memory bandwidth tripled to 150 GB/s, and the same sub-5W budget as the DX-M1 — enough, it says, for 20-to-100-billion-parameter MoE models at 10–30 tokens per second. The memory play: 18 months with Samsung lets its LPDDR5x-PIM chips run the bandwidth-bound GEMV operations in the memory itself, lifting Llama3.1-8B throughput 6.7x at 2.7x power, with the DX-M3 slated for official LPDDR6 PIM. DX-Newton libraries drop in for Nvidia's Isaac robotics stack, and the DX-M1 is already in mass production at Hyundai's robotics lab. The thesis: 100B-parameter models on devices could cut AI data-center traffic by more than 80 percent.

- [EE Times](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/)

## Also in tech

- **Google quietly routes your Drive files and Gmail to human reviewers** — an October 16 edit to Google's 2023 promise plus updated docs confirm connected-app content can reach human annotation; demos show casual chat autonomously pulling unredacted PII. ([GitHub receipts](https://github.com/thisisme6598/gemini_files/))
- **NVIDIA deepens Korea's sovereign-AI buildout** — NVLink Fusion for Korean NPU/XPU makers, Dynamo for four Korean model builders, and a new SK Telecom × Rebellions collaboration. ([NVIDIA blog](https://blogs.nvidia.com/blog/korea-sovereign-ai-collaboration/))

## Business roundup

- **Nvidia's spy scandal reaches the DOJ** — NYT: Commerce's Megaspeed probe was transferred to the Justice Department after Nvidia intervened; Huang owes an answer by November 11 on the House's November 18 briefing. ([AI Weekly](https://aiweekly.co/alerts/nvidia-lawyers-email-preceded-megaspeed-probe-shift-to-doj))
- **Anthropic sets IPO dates despite pushback** — investor meetings this week, trading targeted November 19–20 after buyers balked at ~$1.5T. ([RuntimeWire](https://runtimewire.com/article/anthropic-pushes-ahead-november-ipo-valuation-pushback))
- **EU's Digital Fairness Act draft lands Wednesday** — users may switch off chatbots simulating personal relationships; fines up to 6 percent of revenue. ([AI Weekly](https://aiweekly.co/alerts/eu-draft-digital-fairness-act-targets-ai-companion-bots-6-fines))
- **SpaceX files a $24B Starbase AI campus** — super-compute facility plus a 748MW gas plant to skip grid interconnect; vote December 9. ([Crypto Briefing](https://cryptobriefing.com/spacex-24-billion-ai-supercomputer-starbase/))
- **Disney picks Adobe's Firefly Foundry** — brand-safe models trained on Disney characters for parks, cruise line and ESPN. ([The Decoder](https://the-decoder.com/disney-bets-on-adobes-firefly-to-create-brand-safe-ai-models-for-its-entertainment-empire))
- **Apple's new CEO wants an agentic Siri by 2027** — Gurman: Ternus pressed Federighi to accelerate; Siri chief Mike Rockwell may step down. ([TNW](https://thenextweb.com/news/ternus-federighi-agentic-siri-apple-ai-bloomberg))

## Also noted

- **OpenAI sells a $200 Game Boy-style Codex handheld** — builds playable ROMs from prompts. ([RuntimeWire](https://runtimewire.com/article/openai-sells-200-codex-chromatic-handheld-that-turns-prompts-into-game-boy-games))
- **Tencent's upcoming open-weight Hy4 filters hacking knowledge out of its training data** — an approach that reportedly survives abliteration. ([The Decoder](https://the-decoder.com/tencents-ai-chief-says-ai-bioweapons-are-coming-but-closing-off-models-isnt-the-answer/))
