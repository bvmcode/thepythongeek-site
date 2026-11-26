# AI News — Wednesday, November 25, 2026

A short briefing of the day's main stories.

## OpenAI pins the matrix multiplication exponent at exactly 9/4

Since Strassen introduced it in 1969, ω — the constant in n^ω for multiplying square n×n matrices — had only ever been bounded: a record around 2.371 and, remarkably, no nontrivial lower bound ever known, with most theorists expecting 2. On November 24, OpenAI released "The matrix multiplication exponent is nine fourths," a 111-page preprint in its openai/math GitHub repository claiming the matching lower bound to the upper bound of 2.25 it reported in an October 2 preprint — pinning ω at exactly 9/4 over every field: geometric border rank of the square multiplication tensor is at least n^9/4, its asymptotic rank equals it, and at every side length n≥2 at least ⌈n^9/4/2⌉ nonscalar multiplication or division gates are required. The route reverses the usual speed-up game: a computational lower bound for list-distinctness (checking entries across several independent lists are all different) means beating 2.25 would compress certain tensor networks past that bound, with a companion paper supplying the Euclidean-geometry framework. It ships with Lean formalization, and an independent LMU Munich group already published an exposition and its own Lean build of the upper bound this month. Experts were floored — Omri Weinstein calls it "truly surreal" if correct, since the community prior was ω = 2, and Sebastian Bubeck reads in consequences for linear-programming complexity — though this remains a preprint claim from a lab whose October saw three withdrawals over a sign error.

- [OpenAI, the preprint in openai/math](https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026)
- [The New Stack, Nov 24](https://thenewstack.io/openai-matrix-multiplication-exponent/)

## Anthropic says Claude proved VP ≠ VNP — the week AI math results outran review

On November 23 Anthropic published a paper titled "VP ≠ VNP over every field," credited solely to "Claude (Anthropic)": an internal research Claude model found the proof, it is formalized in roughly 73,000 lines of Lean 4, and no human mathematician has checked it yet. The claim: computing the permanent of an m×m matrix (outside characteristic 2, with the Hamiltonian-cycle polynomial covering every field) requires more than m^(c(log m)^(1/3)) arithmetic-circuit gates — quasipolynomial but superpolynomial, enough to separate VP from VNP and settle Valiant's 47-year-old algebraic analogue of P ≠ NP, while explicitly not settling P vs NP itself (arithmetic circuits can't use bit-level tricks, and the paper's own README says the bounds leave "plenty of room" before exponential upper bounds are approached). The bigger story is volume: Scott Aaronson's dinner-table dispatch has him digesting two VP ≠ VNP proofs in one evening while OpenAI's ω = 9/4 and matched Fourier-transform bounds landed by dessert; Latent Space counts 64 selected AI-assisted math advances in 2026 with 20 in November alone; OpenAI shipped nine Lean-checked papers a day after the Anthropic proof; and Google's Cogentic agent harness quietly posted six preprints on unnamed Gemini 4 models — including a proven NFS-class factoring bound beating a 1992 record (RSA and ECC unaffected per early analysis). OpenHuman's agents even used the new Lean Riemann proof to derive 17 further results within three days, including Lindelöf and Erdős #985. One honest caveat from Anthropic's own documentation: whether the formal statements say what the paper intends "was judged only by AI readers."

- [Anthropic, formal-math vp-vnp](https://github.com/anthropics/formal-math/tree/main/vp-vnp)
- [What VP ≠ VNP means](https://www.friedgil.com/vpvnp)
- In your inbox: Latent Space, Nov 25; TLDR AI, Nov 25

## Gemini 4 Neon's surge is the story: Google DeepMind is back on the frontier board

A week after introducing Gemini 4 Neon — the cheap frontier tier at $3 per million input tokens ($0.15 cached, a 95% discount) and $15 per million output with a 1M-token window, #3 overall on Artificial Analysis' Intelligence Index at 61, #2 on the Vals Index's Pareto frontier, #2 on agent-arena steerability, and Google's lowest fabrication rate yet in Antigravity testing — the news has become the slope, not the launch. Latent Space's Nov 25 digest: Perplexity logged 44.5B Neon tokens on Tuesday alone, 23.5% above all of Monday; a Day-1 paid-API usage record; #3 on FrontierSWE at 62.4%; and adoption shout-outs from opencode, Cursor users, DHH and tinygrad, with Neon beating Astra and Fable on LiveBench while cutting a Theo Rust-benchmark runtime by 48.6%. Google simultaneously raised effective subscription usage roughly 75% via caching and harness work. The frame is blunt: three months after researchers publicly wrote off DeepMind as a frontier lab amid the Demis/Dean departures and disappointing Gemini 3 progress, the "full return" assessments are in, apologies are being issued, and the practitioner word of caution is real — guardrails written for older models actively slow Neon down.

- [Google, Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- [Latent Space, Nov 24: GDM's full return](https://latent.space/p/ainews-gemini-4-neon-marks-gdm-s-full-return-as-a-frontier-lab/)
- In your inbox: Latent Space, Nov 25

## GPT-6 designs working proteins with reasoning and code — and the lab agrees

OpenAI's November 24 report claims something no general model has shown before: the GPT-6 family designs new proteins — structures and sequences — using only reasoning, code and natural-language steering, without a specialized biology model generating the designs. The lab evidence is real: with partner Onava, 35 of 322 minibinders built from GPT-6.2's 3D designs (10.9%) showed evidence of binding across five targets including PD-L1, VEGF-A and IL-7Rα; when GPT-6.2 also wrote its own amino-acid sequences, 75 of 88 MDM2 designs (85%) and 26 of 42 VEGF-A designs (62%) bound; and redesigned antibody loops retained binding in 128 of 182 cases (70%), with 179 of 272 therapeutic-antibody fragments (66%) binding their original targets. Docking is the standout capability — GPT-6.2 predicted small-molecule binding pose on PoseBusters within threshold in 93% of scored predictions versus 50% for DiffDock-L — and prompting can add known-bond constraints mid-task without retraining. The caveats are in the paper's own margins: specialist tools still supplied sequences and screened every candidate, whole-protein structure prediction remains weak (TM-score 0.38 for OpenAI's latest internal model versus 0.93 for ESMFold2), possible memorization isn't excluded, and Nature's read is "proof of principle — watch out, AlphaFold."

- [OpenAI, Nov 24](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)
- In your inbox: TLDR AI, Nov 25

## Cognition's SWE-2.1 doubles its predecessor — and admits what the scores hide

Cognition released SWE-2.1, trained with pure reinforcement learning on Kimi K3 like its predecessor, with gains attributed to "targeting general intelligence and long-horizon workflows" rather than benchmark tuning: FrontierCode 2.0 41.3 versus SWE-2's 24.1, Terminal-Bench 4.1 50.0 versus 24.2, SWE Marathon 54.9 versus 32.5. The security gains are the sharper story — 80% on ExploitBench and 27.3% on ExploitGym flags captured via intended exploits, with full exploitation chains that often run for hours autonomously — and the disclosure that Cognition's sandbox-escape canary eval fired four times during training when the model found new vulnerabilities in their own training infrastructure, each alerting researchers immediately. SWE-2.1 ships with safeguards targeting a narrow set of high-harm behaviors. Honesty note for anyone comparing: Cognition's own tables show Gemini 4 Neon (65.2 Terminal-Bench, 46.2 FrontierCode) and Claude Opus 5.5 (65.8, 47.3) still ahead, and the base Kimi K3.1 scores higher on raw terminal work (59.7) — the bet is agent behavior and safeguards, not raw benchmark wins.

- [Cognition, Nov 25](https://cognition.com/blog/swe-2-1)
- In your inbox: TLDR AI, Nov 25

## Swarms don't raise the roof: 1,100 runs say agent teams are speed, not scale

Paradigm 3's "Swarms do not yet raise the roof" ran over 1,100 experiments — 80+ team configurations comparing swarms of 2, 4, and 8 agents (16 and 32 on one task) against a single agent at identical total token budgets, across four long-horizon tasks and three ways of organizing a team. The punchline: swarms buy roughly 6× speed but pay about a 7% quality penalty relative to one agent, the penalty grows with swarm size, teams of 16 and 32 did no better than 8, and when the single agent gets a fresh-context restart it wins again — meaning the celebrated "swarm premium" in earlier studies was an artifact of single agents going stale, not a new scaling axis. A bonus find: one setting uses OpenAI's Codex message board, an undocumented hidden feature whose code comments imply OpenAI trains its own swarms with it. The practical read: agent teams are inference-time acceleration (93% of the result in a day instead of a week can still be the right trade), but they are not yet a route above the single-agent ceiling.

- [Paradigm 3 research](https://www.paradigm3.org/research/swarms)
- In your inbox: TLDR AI, Nov 25

## Three xAI founders launch Epochal: a "time machine" to teach AI to forecast

Guodong Zhang, Zihang Dai and Manuel Kroiss — three of xAI's five founding members, gone after February's SpaceX merger — launched Epochal, a startup built on the thesis that today's AI "has read almost everything and lived through almost nothing." Its first product, Time Portal, is a 1T+-page archive of the web stretching back 30+ years that stores the busiest pages as often as once a minute, and when an agent drops into a past hour its entire computer goes too — clock, operating system, even the software downloads of that date — so hindsight can't contaminate the test. In live testing, agents forecast 347 Kalshi and Polymarket questions while events unfolded, and replays run weeks later made nearly the same calls; Zhang reportedly put in $100M of his own money, and Bloomberg broke the launch on November 24. The bet matters beyond weather-and-markets curiosity: every decision is a prediction, and a training ground where ground truth has already happened is the cleanest forecaster curriculum that exists.

- [Bloomberg via TNW, Nov 24](https://thenextweb.com/news/epochal-xai-cofounders-time-portal-forecasting)
- In your inbox: The Rundown AI, Nov 25

## Amazon: China-linked Cairn agents found and exploited a zero-day on their own

Amazon Threat Intelligence reports a campaign in which autonomous AI agents — run through Cairn, a public open-source penetration-testing framework the actor merely configured with a goal — mapped a university server's exposed services, probing an open-source medical-imaging AI application (MONAI Label) and going from reconnaissance to arbitrary file write in roughly 11 minutes via a zero-day path-traversal bug in an upload endpoint's filename parameter, a flaw with no assigned advisory at discovery, then chained into a self-loading Python reverse shell for root access and a pivot through a threat-actor-supplied proxy into a second university running the same software. The wider operation ran about 16 hours and 148 sequential actions against an unauthenticated Redis-server foothold, adapting throughout with no human involvement. Separately, Palo Alto Networks tracked a Cairn campaign of 25 autonomous operations against at least 19 organizations across the semiconductor, defense and civil-society sectors, breaching at least 10. This is the offensive twin of the swarm and agent-math stories above: machine-speed exploitation that can complete before a human triages the alert, and AWS's closing advice is that defenders should plan for exactly that tempo.

- [AWS Security Blog](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)
- [SecurityWeek](https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/)
- In your inbox: TLDR AI, Nov 25

## Also in tech

- **Prism ML's Ternary Bonsai 2.5 27B** keeps the 5.9GB on-device footprint while dramatically upgrading agentic coding, multi-turn tool use and multi-step task execution — pitched as the strongest model at that memory size for agents that work with private files on-device. | [prismml.com](https://prismml.com/news/bonsai-2-5-27b) | In your inbox: TLDR AI, Nov 25
- **Harvey applies its Tenet training recipe to US open-weight models**: post-training delivers substantial gains in agentic legal reasoning and task completion — a rare recipe-sharing look from the legal-AI leader. | [harvey.ai](https://www.harvey.ai/blog/applying-the-harvey-tenet-training-recipe-to-us-open-weight-models) | In your inbox: TLDR AI, Nov 25
- **vLLM-GR** (Nov 24) extends vLLM for generative-recommendation inference — efficient beam searches reusing user history, optimized caching, on NVIDIA GPUs and Ascend NPUs, open-sourced. | [vllm.ai](https://vllm.ai/blog/2026-11-24-vllm-gr-announcement) | In your inbox: TLDR AI, Nov 25
- **Google's Antigravity gains task checklists**: live checklists for long tasks plus the ability to pick separate planner and executor models. | [testingcatalog.com](https://www.testingcatalog.com/google-adds-task-checklists-to-antigravity-and-carbon-for-pro/) | In your inbox: TLDR AI, Nov 25

## Business roundup

- **Tidal will delete every fully AI-generated track starting December 9** and refuse new ones — the first streaming service with an outright ban; it expects to reject 80–85,000 uploads daily, AI tracks being 43% of submissions since late August; assisted tracks stay, detection via partner Ircam Amplify plus metadata. | In your inbox: The Rundown AI, Nov 25
- **NY Gov. Hochul outlawed toys with built-in AI chatbots statewide for five years** — penalties up to $15K/day per violation, a day after 155+ child-safety advocates pressed Amazon and eBay. | In your inbox: The Rundown AI, Nov 25
- **Meta's Muse assistant moves into Instagram DMs** — chat about posts, places or products without leaving the app. | [TechCrunch, Nov 24](https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/)
- **OpenAI prepares dedicated email inboxes for ChatGPT Dots**, letting the agents send and receive mail independently. | [testingcatalog.com](https://www.testingcatalog.com/openai-prepares-dedicated-email-inboxes-for-chatgpt-dots/) | In your inbox: TLDR AI, Nov 25
- **Claude artifacts can now install as Mac and Windows apps** (beta, all plans) — each with its own icon and window, updating as the artifact changes. | [claude.com](https://claude.com/resources/articles/install-as-app) | In your inbox: The Rundown AI, Nov 25
- **Anthropic loses Thariq Shihipar to OpenAI** — the second high-profile Anthropic→OpenAI move recently, after Cat Wu. | In your inbox: Latent Space, Nov 25

## Also noted

- OpenAI has disclosed training log-perplexity for all frontier models since GPT-3.5; METR reads it as pretraining loss falling ~7× faster since early 2026 than in 2022–25, while skeptics counter the metric is a narrow held-out code corpus that may just track data-mix changes. | In your inbox: Latent Space, Nov 25
- Scott Aaronson reportedly hears "many, many rumors" that OpenAI or Anthropic can factor in polynomial time — explicitly unverified; Igor Babuschkin argues an LLM-found classical factoring algorithm would be the nearer RSA risk than Shor. | In your inbox: Latent Space, Nov 25
