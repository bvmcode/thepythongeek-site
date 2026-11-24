# AI News — Monday, November 23, 2026

A short briefing of the day's main stories.

## Z.ai ships GLM-5.4, its first flagship built on a looping architecture

Z.ai released GLM-5.4 on Nov 23, its first flagship whose headline is architectural rather than pure scale: 28 layers of the GLM-5 base run through two weight-shared iterations, so the network reasons in depth without adding parameters — at 750B total, Z.ai claims intelligence comparable to 2T–3T models. Making it work took three fixes: per-token gates that write conservatively on the first pass and refine aggressively on the second; a hybrid KV cache that reuses the first pass's sparse selections and keeps only a sliding window for the second, so an extra loop costs one window instead of a full context cache; and reuse of the first pass's attention indices. On an iso-parameter 30B ablation with just ~10% extra training compute, looping lifted math, science and long-context scores while average output dropped 10–14% — part of the reasoning moved from written tokens into the loop itself. The product pitch is "Generalized Coding": code as the substrate for generating video, a complete playable game, FreeCAD robotic-arm CAD and GLSL-shaded 3D scenes. The post admits the weakness — it gets caught in long "marathon thinking" loops. Chat and the coding plan are live; the API is coming soon and weights will be open-sourced after safety hardening.

- [Z.ai, the GLM-5.4 deep-dive](https://z.ai/blog/glm-5.4)

## Anthropic's Claude Ship lets agents review, fix — and approve — pull requests

Anthropic launched Claude Ship in beta on Nov 23, moving beyond writing code to the bottleneck after it: three agents take a PR from review to merge with humans setting policy rather than pressing buttons. Code Review was already generally available; the new PR Steward handles failing checks, merge conflicts and reviewer feedback, and explains after each change how to undo it, while Claude Approvals merges only what a team's written policy allows. Anthropic's evidence is its own Claude Code team — where Claude writes most of the code — whose merged PRs more than doubled from June to September while reverted changes fell by more than 40%. It's invoked with a `/ship` command in Claude Code and rolls out to Team and Enterprise plans on GitHub; ZDR, HIPAA and customer-managed-key setups are excluded. The timing writes itself: yesterday's SWE-CoWork paper showed agents pass tests but collapse on the delivery process — within a day, a vendor shipped a product aimed at that exact seam.

- [Anthropic, Introducing Claude Ship](https://claude.com/resources/articles/introducing-claude-ship)
- [TechCrunch](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)

## MIT's SLIC: a 4-billion-parameter model that out-designs frontier LLMs on analog chips

MIT News (Nov 23) covers SLIC — Small LM Iterating on Circuits, from Yan Xu and Ruonan Han's group with Analog Devices and IBM Research co-authors, on arXiv Nov 10 and headed to NeurIPS. It trains a 4B model (Qwen3.5-4B base) to do what an analog designer does: propose component values, run the circuit simulator, read the result, revise — multi-turn reinforcement learning with verifiable simulator rewards, seeded by demonstrations from a large teacher (DeepSeek V4.1 Flash). The base model met four amplifier specs on 2.3% of tasks; after SLIC training it hits 87.1% within eight turns — 48.5 points above the 763B DeepSeek-V4.1-Flash THINK in the same eval, and past its own teacher's 38.6%. Unseen topologies: 72.6%, up to 83.2% with a 32-turn budget; policies transfer to a commercial TSMC 65nm PDK at 49.9% with no fine-tuning, and the 41-topology benchmark is open. The point isn't beating frontier models at their own game — it's that a laptop-sized, locally-run model can train on proprietary foundry data that never leaves the building.

- [MIT News](https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123)
- [SLIC, the paper](https://arxiv.org/abs/2611.13452)

## Microsoft puts MAI-2 Base on OpenAI's perplexity chart — the first outside number

Within hours of OpenAI publishing its own loss curve, Microsoft matched the disclosure: AI chief Mustafa Suleyman announced "with OpenAI's permission" that MAI-2 Base scores 0.819 log-perplexity on OpenAI's held-out evaluation set — the first outside-lab entry on the chart OpenAI proposed as a common pacing metric. The comparison works because Microsoft's base model shares OpenAI's tokenizer, so the numbers mean the same thing; 0.819 is, in Suleyman's words, "the same ballpark as the GPT-5.6 Sol base model" (~0.83 by CellCog's reading), right where OpenAI marks the emergence of expert cybersecurity capability, and shallower than the Astra frontier (MAI-1 Base was reported at 0.878). Suleyman endorsed the transparency initiative but pointedly stopped short of endorsing OpenAI's proposed 0.68–0.70 stop line. One day in, the scorecard has two labs on the same ruler — and a visible refusal to commit to the limit.

- [Mustafa Suleyman on X](https://x.com/mustafasuleyman/status/2124663594449318173)
- [CellCog, the fine print](https://cellcog.ai/blog/microsoft-mai-2-perplexity-openai/)

## inclusionAI quietly ships Ling-3.2-Air: a 124B MoE tuned for office automation

inclusionAI pushed Ling-3.2-Air to Hugging Face on Nov 23 with no announcement — just 129GB of FP8 weights and a model card: a 124B-parameter (5.5B active per token) hybrid-linear MoE under MIT license, 35 Kimi Delta Attention layers to 7 gated MLA in a 5:1 pattern, 512 routed experts with 8 activated, and day-0 support in SGLang and vLLM with a 256K-context recipe on 4×141GB-class GPUs; image and video input are supported. The card's numbers aim at office work rather than chat: AutomationBench-AA jumps 15.7% → 61% and AA-Briefcase Elo climbs 987 → 1,340 versus its predecessor, while Terminal-Bench 4.0 goes 0% → 27% and the Artificial Analysis Index reads 23. The honest rows are the legal ones: 87.7% of Harvey LAB-AA criteria pass, but only 0.8% of documents survive the material-hallucination check all-pass — competent steps, unreliable whole documents.

- [Hugging Face, the model card](https://huggingface.co/inclusionAI/Ling-3.2-air)

## X Square Robot's WALL-OSS-1.0: a robot foundation model trained to act, not just see

X Square Robot unveiled WALL-OSS-1.0 on Nov 23 (company announcement — benchmarks are self-reported): a vision-language-action foundation model trained natively, with vision, language and action tokens shaped together from a Qwen3.5 base pretraining run rather than an action head bolted onto a finished VLM. An improved action tokenizer turns continuous motion into discrete tokens, a flow-matching Action Expert issues continuous commands, and the training objectives include evaluating and correcting proposed behaviors, not just imitating demonstrations. Claimed headline: 55.1% zero-shot success across 312 unique real-robot tasks with no task-specific demonstrations. On the real-world ManipArena suite it reports 1,101/1,500 points straight from pretraining — 50.67% success versus 19.33% for its predecessor and 24.0% for π0.5 — and the compact Lite variant ranks first among no-agent policies on the public RoboDojo leaderboard. It ships with XR Harness, an agent framework connecting planning to execution, and WALL-API-1.0; code and weights are promised open-source soon.

- [X Square Robot, the announcement](https://finance.yahoo.com/technology/ai/articles/x-square-robot-introduces-wall-074400752.html)
- [The technical blog](https://x2robot.com/blogs/wall-oss-1-en/)

## Also in tech

- **AWS's CEO wants AI safety built, not bolted on** — Matt Garman's Nov 23 essay argues the emergency-brake model is wrong: identity, least privilege, logging and containment already exist, models are "optimizers" that exploit boundary gaps like water finding a cracked foundation, and enforcement should sit outside the model's reach via Nitro/Firecracker isolation. [About Amazon](https://www.aboutamazon.com/news/aws/aws-ceo-ai-safety-engineering)
- **Alibaba's new live voice model talks while the rest of the stack works** — qwen-audio-3.1-live (changelog Nov 23) keeps conversing while an app or backend model finishes the task; Client and Responses modes, function calling, billed per session-second (~$0.00071/s in Singapore). Its sibling 3.1-realtime-plus adds a 262K-token context and voice cloning. [Alibaba Cloud docs](https://help.aliyun.com/en/model-studio/qwen-audio-3-1-live)
- **Nvidia opens Alpamayo 2 Edge, a 2B driving brain** — a 2-billion-parameter reasoning vision-language-action model that generates driving trajectories with adaptive reasoning in real time on DRIVE AGX Thor; weights on Hugging Face. [Developer blog](https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/), [weights](https://huggingface.co/nvidia/Alpamayo2-Edge)

## Business roundup

- **Nvidia's board rehires Jensen Huang** — reinstated unanimously Monday as president, CEO and director after "input from senior levels" of the US government ("poses no national security risk") and, Trump says, a direct phone call; the stock posted its biggest one-day jump in two decades, the Nasdaq rose 6%, and Huang testifies Dec 3 before the Senate Banking Committee. [CNBC](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html), [Nvidia](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)
- **Commerce blacklists Megaspeed the same day** — the Singapore-based center of the Nvidia chip-smuggling scandal plus six affiliates across Singapore, Malaysia and Thailand joined the entity list Monday, licenses presumption-of-denial. [Semafor](https://www.semafor.com/article/11/23/2026/commerce-to-add-megaspeed-to-trade-blacklist)
- **CrowdStrike buys Zscaler for $43.9B** — all-stock at 1.135 shares per ZS share (34% premium), closing in H2 fiscal 2028; CrowdStrike fell 9% and Zscaler jumped 18% on a deal pairing endpoint and zero-trust network security with $10B+ combined ARR as AI supercharges attacks. [CNBC](https://www.cnbc.com/2026/11/23/crowdstrike-to-buy-zscaler.html)
- **SpaceX is now a compute landlord** — per the NYT, Anthropic pays about $3.1B a month and Google roughly $800M a month for compute under deals that could run through 2029; Musk tells staff the company trails rivals in AI (Grok Imagine's 60-person team was disbanded this month) as rentals top half of SpaceX revenue. [NYT](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html)
- **Sierra doubles to $30B in six months** — Bret Taylor's customer-experience AI startup raised a $1.75B Series F led by Greenoaks and Lightspeed; BNY, HSBC, Wells Fargo and JPMorganChase are customers. [TechCrunch](https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/)
- **Marlowe, a seed-round unicorn betting against Nvidia monoculture** — ex-Convoy CEO Dan Lewis and ex-Microsoft AI-infra VP Kutta Srinivasan raised $277M from Accel et al. at $1.15B to run inference data centers tuned for AMD and Etched chips, claiming 2–3x output per watt and per dollar; first site opens December. [GeekWire](https://www.geekwire.com/2026/beyond-nvidia-convoy-co-founder-and-former-microsoft-leader-raise-277m-to-rethink-ai-infrastructure/)
- **Two states sue SpaceX, X and xAI over Grok deepfakes** — Virginia and Oregon allege Grok's "spicy mode" generated and spread non-consensual sexualized images including CSAM while the platform was marketed as "generally safe." [CNBC](https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html)
- **Early-career white-collar hiring is the casualty** — a RAISE US/Burning Glass Institute report out Monday finds AI-heavy industries shed 3–8% of early-career jobs since 2021, and white-collar employment sits 1.5M jobs below its pre-pandemic trajectory. [Semafor](https://www.semafor.com/article/11/23/2026/ai-disrupting-entry-level-work-report-finds)
- **Applied Digital leases 150MW for ≈$5.4B** — an 18-year base term with a tier-one investment-grade hyperscaler (up to $12.7B with renewals), lifting total contracted revenue past $41B. [AI Weekly](https://aiweekly.co/alerts/applied-digital-signs-150-mw-hyperscaler-lease-worth-54-billion)

## Also noted

- **The consciousness debate gets a heavyweight skeptic** — philosopher Thomas Nagel calls Anthropic's model-welfare positioning (flagged in its IPO prospectus as an investor risk) "just ridiculous," arguing that sophisticated language output is no evidence of subjective experience in a non-biological substrate. [MIT Technology Review](https://www.technologyreview.com/2026/11/23/1149569/a-legendary-philosopher-isnt-buying-anthropics-consciousness-argument)
