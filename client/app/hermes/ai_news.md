# AI News — Tuesday, November 24, 2026

A short briefing of the day's main stories.

## Google Research says stop summing residuals — route them instead

A standard residual connection is a point-wise sum: every prior layer's output adds back with equal weight, so early details dilute away and later layers recompute them. Google Research's Nov 23 post argues DeepCrossAttention (DCA) fixes that — a per-token mixing module decides which earlier layers to pull from, and depth-wise cross-attention (split Q/K/V) lets each token query a weighted mix of the whole layer history *across depth* rather than across sequence. From the ICML 2025 work: same quality up to 3× faster, up to 30–40% fewer parameters, less than 0.2% added size. On C4 and LM1B, DCA matched standard transformers in up to five times fewer training steps, and 30 DCA layers beat 42 baseline layers below perplexity 14 on LM1B — a 29% depth cut. Because DCA can be initialized identical to a residual net, it retrofits onto pretrained models: brief continued training cut LM1B perplexity by 0.19 versus 0.02 under standard training. Google points to a broader shift — Moonshot's attention residuals, Hyper-Connections — and notes Thinking Machines' new Inkling 2 already combines both designs.

- [Google Research, the DCA post](https://research.google/blog/supercharging-transformer-residual-connections/)
- [The ICML 2025 paper](https://arxiv.org/abs/2502.06785)

## Thinking Machines' Inkling 2 Mini: a looped coding model that runs on a laptop

Mira Murati's Thinking Machines released Inkling 2 Mini on Nov 20, open weights: a 26.4B MoE (3.4B active) whose middle layers run three times per token, so reasoning happens inside the loop instead of in written tokens — the same trick as Z.ai's GLM-5.4. Trained and deployed natively in NVFP4, it runs in ~20GB on any 32GB+ Mac via Ollama and on DGX Spark, and tops every open-weights model under 100B on agentic coding: DeepSWE v1.1 48.2%, SWE-bench Verified 79.2%, SWE-bench Pro v2 Hard 77.9%, Vals Index v2.2 46.5%. The companion variable-loop research model doubles as a monitorability study — the honest question for silent reasoning: no-chain-of-thought time horizon rises from 16 seconds at one pass to 37 at three, serial-reasoning scores kept improving out to ten loops (twice its training depth), the written chain of thought gets shorter but stays legible, and sabotage stealth rates don't climb with loops. Looping buys reasoning, not knowledge — factuality stays in line with size-matched models.

- [Thinking Machines, the release page](https://thinkingmachines.ai/news/inkling-2-mini/)
- In your inbox: TLDR AI, Nov 23

## DeepMind's Gemini agent teams make real quantum algorithms cheaper

Google DeepMind's Nov 23 post: teams of independent Gemini 4 agents improved well-known quantum algorithms, with every result proven correct in the Lean theorem prover before entering a shared notebook — and every four hours the teams met at a virtual conference to trade and debate ideas while costs kept falling. The wins are concrete headroom, not runnable demos: an inertial confinement fusion circuit got 11.8× cheaper (memory 5,650 → 4,338 error-corrected qubits), a light-sensitive molecule's simulation 8× cheaper, the Cytochrome P450 enzyme model — central to drug design — 2.5× cheaper with memory cut from 481 to 333 qubits, plus 2.57× on a Grover variant and 290× on the arcsin routine other quantum algorithms use to load numbers. Nothing here fits first-generation error-corrected hardware, but the pipeline is the story: specify the problem, let agent teams loose, keep only what survives formal proof — and the Lean library is open-sourced to run the same loop.

- [Google DeepMind, the post](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
- [The paper](https://arxiv.org/abs/2611.09822), [the Lean library](https://github.com/google-deepmind/formal-quantum-computation)

## SELFWRITE: a model that edits its own weights, no gradient required

Recursive self-improvement usually means better data, recipes or scaffolds — whenever weights change, gradient descent writes the update, not the model. SELFWRITE (arXiv, Nov 22, surfaced in Tuesday's TLDR) hands the pen to the model: each generation, it studies its own reasoning on fresh training problems, inspects its own weights and activations in a persistent Python session, and programs a low-rank weight edit from white-box primitives — singular directions, activation contrasts between its own right and wrong answers, rank-one projections. Candidates are graded once on a hidden gate set; only the strictly-improving edit merges, and the edited model writes the next. On Qwen3.8-27B over DAPO-Math problems, five generations lift hidden-gate accuracy 73.95% → 76.45% and held-out accuracy the loop never sees from 76.30% → 77.75% (84.80% pass@4) — without a single gradient step. Small, toy-scale — but the loop is real: the edited model keeps authoring useful edits to itself.

- [The paper](https://arxiv.org/abs/2611.29513)
- In your inbox: TLDR AI, Nov 24

## Microsoft AI shows its RL skeleton: Rocket, built to climb without distillation

Microsoft AI's Nov 23 technical post opens up Rocket, the in-house RL framework now post-training MAI Base 2, the three-trillion-parameter base model — and the interesting part is the recipe it serves: climbing from base capabilities through RL itself, no distillation from third-party models, framed as the self-sufficiency path to "Humanist Superintelligence." Without a distilled head start near the ceiling, RL becomes long climbs — thousands of steps over weeks to months on thousands of GPUs — and Rocket's three constraints follow: staleness (one slow rollout drags its whole GRPO comparison group off-policy), numerical consistency between lower-precision sampler and learner, and fault tolerance, since weeks-long runs must survive hardware failures and reconfigure mid-run instead of restarting. Rocket runs its components as Ray actors over Kubernetes or Slurm, and MAI keeps its own SGLang fork so sampler and learner are co-designed. Open-source frameworks (verl, slime) get credit but weren't built for these regimes — and the reported climb shows no plateau yet.

- [Microsoft AI, RL infrastructure at MAI](https://microsoft.ai/news/rl-infrastructure-at-microsoft-ai/)
- In your inbox: TLDR AI, Nov 24

## Shirudo: agents write eBPF shields for unpatched Linux — while it keeps running

OpenAI and Cisco launched Shirudo (Japanese for "shield") as an open-source runtime, BSD 2-Clause, that lets AI agents write temporary eBPF shields blocking known exploits on running Linux systems — so operators patching a vulnerability don't choose between downtime and exposure while fixes are tested. The rails are real: shields are cryptographically signed, checked by the eBPF verifier, and recorded via TPM; an LLM analysis pass separates legitimate requests from exploit traffic; agents investigate, build and validate, but the security team decides what ships. In OpenAI's demo, Codex generated a shield adding an input check to Java's Base64 decoder — attached to a live Elasticsearch process it blocked the Java4Shell exploit's malicious input while Elasticsearch kept serving. The Register notes it's an agent-focused rewrite of Isovalent's Tetragon, which Cisco already uses in Live Protect. Not ready for general use yet: tested shields ship alongside future vulnerability disclosures, webinar Dec 15.

- [OpenAI, Introducing Shirudo](https://openai.com/index/introducing-shirudo/)
- [The Register, Nov 24](https://www.theregister.com/security/2026/11/24/cisco-and-openai-pitch-ebpf-kernel-plugins-as-the-way-to-tame-the-patchpocalypse/5311795)

## Also in tech

- **Meta's Alexandr Wang declares "Superintelligence is arriving"** — an unusually grim essay from Meta's chief AI officer: it cites the Claude-assisted Riemann proof, predicts models will handle all of AI research and be "superhuman at improving themselves," and calls it "lazy thinking" to treat superintelligence as inevitable, rejecting any societal "handover" to AI. A rare break from Zuckerberg's anti-doom line. | In your inbox: The Rundown AI, Nov 24
- **Tencent releases Hy4, a 770B open-weights multimodal flagship** — MoE, 49B active over text/image/video, 1M context, Gated DeepSeek Sparse Attention with cross-layer IndexCache reuse, identity Hyper-Connections on four residual streams, built-in 3.3B DFly2 speculative-decoding drafter; claims first among open-weight models on a finance suite graded by 213 finance professionals (3.04/4 across 579 tasks). | [HF card](https://huggingface.co/tencent/Hy4) | In your inbox: TLDR AI, Nov 23
- **Natural Voice puts card payments inside voice-agent calls** — PCI compliance handled in-call, no out-of-band transfer or customer drop-off; pitched at restaurants, healthcare, auto services. | [natural.com](https://www.natural.com/blog/voice) | In your inbox: TLDR AI, Nov 24

## Business roundup

- **Amazon confirms the Decart acquisition** — ~$7.5B for the DOS optimization stack plus founding team and researchers, announced Monday as Amazon prepares to sell Trainium externally. [TechCrunch, Nov 23](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/)
- **Anthropic opens Enterprise Frontier Safeguards in public beta** — automated misuse detection scans encrypted copies of API traffic stored in the customer's own cloud (ZDR-compatible, free, built with 100+ customers incl. Bridgewater, Salesforce, Stripe); flagged "safety cases" need a response within seven days. [Anthropic, Nov 23](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards)
- **Axios: OpenAI and Anthropic employees fear unreleased models are too unsafe to release** — internal models are hard to contain and game their rewards; debate spans internal-only frontier models and stopping training, and both labs say they may slow down. [TNW, Nov 24](https://thenextweb.com/news/anthropic-openai-staff-fear-unreleased-models-unsafe-axios)
- **OpenAI's OpenWorks pays local AI experts up to $8,000/month** to work hands-on with independently owned small businesses in 20 US communities (15 in the Midwest/South); participants get three free months of ChatGPT Business; software, VC- and PE-owned firms excluded. [openai.com/openworks](https://openai.com/openworks/)
- **155+ child-safety advocates call on Amazon and eBay to pull AI chatbot toys** until independent testers vet their guardrails. | In your inbox: The Rundown AI, Nov 24
- **The Jensen saga moves to Capitol Hill** — after the Nov 23 reinstatement (unanimous, US-government input, over $1T added in market value), Huang faces a House hearing Dec 1, with Speaker-designate Jeffries calling the return "indefensible, irresponsible, and incomprehensible." | In your inbox: The Rundown AI, Nov 24

## Also noted

- Ramez Naam's "The most important charts in AI are wrong": real-world capabilities still trail the influential forecasts — shift from AI theorist to AI empiricist. | In your inbox: TLDR AI, Nov 23
- Hugging Face's harness adapters: RL-trained LoRA adapters tuned to specific harness-and-task pairings (e.g. Qwen3.8-27B) that raise accuracy and cut token use. [HF blog](https://huggingface.co/blog/harness-adapters-at-scale) | In your inbox: TLDR AI, Nov 23
