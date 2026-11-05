# AI News — Wednesday, November 4, 2026

A short briefing of the day's main stories.

## Tencent's Hy4 gets eyes and hands — full weights still "coming days"

Tencent released the full Hy4 on November 4, its 770-billion-parameter mixture-of-experts flagship from the August preview, adding vision and computer use for the first time: reading images and charts, plus driving a computer through both CLI and GUI, with dedicated training on Blender and CAD for long multi-step workflows. It is live via API on Tencent Cloud and OpenRouter at preview pricing, about $0.90 and $2.70 per million input and output tokens. Tencent reports hallucination down from 12.95 to 7.2 percent, and a blind eval with 213 financial professionals over 579 real tasks ranks it the best open-source model, ahead of DeepSeek-V4.1-Flash-1017, Kimi K3.1 Pro and GLM-5.3. The company also says Hy4 is "advancing into the next stage of Recursive Self-Improvement," its Hyra 2.0 harness using Hy4 to optimize pre-training infrastructure for smaller same-architecture models. The rankings are Tencent's own, and Hugging Face still hosts only the preview — full weights are promised "in the coming days."

- [Tencent](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)

## Kimi K3.1 Pro's 2.8T open weights arrive on schedule

Moonshot promised open weights for Kimi K3.1 Pro by November 4 and hit the date, publishing a checkpoint with a legible spec sheet: a natively multimodal agentic model at 2.8 trillion total and 104 billion active parameters, a 1,048,576-token context window, and a 401-million-parameter MoonViT-V2 vision encoder, shipped as MXFP4 weights with MXFP8 activations straight from quantization-aware training. Self-reported max-effort scores put it at Terminal-Bench 4.0 of 65.7 — one point under Claude Opus 5.5's 66.4 — plus DeepSWE 75.5 and GPQA-Diamond 94.2. All reproducible locally if the custom (non-MIT) Kimi license permits. A 2.8T MXFP4 model being a small-node download rather than a two-rack install is the real headline.

- [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- [Kimi blog](https://www.kimi.ai/blog/kimi-k3-1-pro)

## Ai2's StateBench: frontier models fall to 13 percent on long state tracking

Ai2 released StateBench, a benchmark for long-context state tracking with four difficulty tiers grounded in Krohn–Rhodes algebra — immutable assignment, reassignment, self-referential updates, and assignment by reference (the cup-swap problem). Gemini 3.8 Flash, Claude Opus 5.5, and GPT-6 Sol and Luna handle the easy tiers, then collapse to 13 percent accuracy or worse on the longest general-finite inputs. The architecture result is the news: 275-million-parameter models trained from scratch with Gated DeltaNet or hybrid layers generalized almost perfectly to 64,000 assignments — 250 times their training length — while transformers, even trained directly on the task, never learned the hardest level. Long-running agents live on this gap.

- [Ai2](https://allenai.org/blog/statebench)

## Two papers redraw the agent-inference stack

Subconscious researchers measured speculative decoding on long-horizon agents and found numerical noise grows inside verification windows — which thinking tokens the draft happens to get accepted changes the target model's output distribution after about 30 steps, drifting agentic accuracy in random directions (arXiv 2611.05345). Their fix inverts the usual goal: train the draft model to be deliberately rejected at critical reasoning points so decision tokens are encoded by the target model at full precision; tuning 0.06 percent of hosted parameters on DeepSeek-V4.1-Flash-1017 raises agentic coding success without touching target weights. The companion NVIDIA paper (arXiv 2611.05306) argues long context is oversold: later tokens can cost up to 7x more to generate, yet frequent compaction keeps accuracy roughly level on long-horizon tasks, with "semantic state space models" holding a compact natural-language state instead of a giant window. Both land the same week two releases headline million-token contexts.

- [HF Papers](https://huggingface.co/papers/2611.05345)
- [arXiv](https://arxiv.org/abs/2611.05306)

## Claude found Xen's host-takeover hypervisor bugs

Xen advisory XSA-523 (November 3) discloses two grant-copy flaws (CVE-2026-102703/704) letting a malicious guest read and write any other VM's memory, including dom0 — in XCP-ng's words, "a single compromised guest can break out of its isolation and take over the whole host." Every release from 4.6 onward is affected; patches are out. The credit makes this a first: "Anthropic identified these flaws using its Claude AI model," validated by Ada Logics' Stephan Lipp and independently reported by CodeAnt's security team, with the patch commit ending "Assisted-by: Claude." The flaw sits in a performance cache that wrongly reuses validation between grant-copy batches — tedious invariant bookkeeping, exactly where machine review pays off, at the bottom of the cloud's trust stack.

- [Xen advisory](https://xenbits.xen.org/xsa/advisory-523.html)
- [The Hacker News](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html)

## Chip earnings: Arm's data-center royalties doubled; Qualcomm's AI ramp is supply-starved

Arm's fiscal Q2 (ended September 30, reported November 4) set a record $1.44 billion revenue, up 27 percent, with royalties at $670 million — data-center royalties doubling year over year — and a first-ever quarter shipping more than 10 billion Arm-based chips. Arm says server share at the top hyperscalers went from 15 percent in 2024 to over half in 2025, headed past 60 percent by year-end, with its own AGI CPU due to ship first silicon in Q4 FYE27. Qualcomm's same-day fiscal Q4 beat on revenue ($10.44 billion) and EPS ($2.17), but handset chips fell 26 percent to $5.14 billion as memory costs squeeze phones, while the data-center ramp to a $5 billion fiscal-2027 target ($650 million this quarter) is gated by supply, per CEO Cristiano Amon: "We don't have a demand issue; it's a supply issue." Light guidance cut the stock about 7 percent after hours. AI compute is where silicon money now accrues; the constraint is manufacturing, not appetite.

- [Arm](https://newsroom.arm.com/news/arm-q2-fye27-results)
- [CNBC](https://www.cnbc.com/2026/11/04/qualcomm-qcom-earnings-report-q4-2026.html)

## Also in tech

- **Ripple-65B Preview** — a 65B dense model from new lab Ricursive Intelligence claims US open-weight SOTA on agentic coding (80.52 TerminalBench 2.1) at a claimed $32M all-in cost, a tenth of the prior leader; self-reported, not independently verified. ([Ricursive](https://www.ricursive.com/ripple))
- **Xpeng GroundingPI** — a 4B-parameter, perception-first model scored 73.68 across 34 perception benchmarks versus 71.54 for GPT-6 Astra, in Xpeng's own evaluation; weights on GitHub. ([CnEVPost](https://cnevpost.com/2026/11/04/xpeng-unveils-groundingpi-pre-trained-model/))

## Business roundup

- **AMD** — data-center revenue jumped 97 percent to $8.5 billion, its "largest and most profitable quarter in history." ([The Verge](https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc))
- **AMD bought Taalas** — a ~$2.9 billion cash-and-stock deal ($1.4 billion contingent) for the Toronto AI inference-chip startup. ([The Globe and Mail](https://www.theglobeandmail.com/business/article-amd-to-pay-29-billion-for-ai-chip-firm-taalas/))
- **Meta and OpenAI bought the coding-agent layer** — Meta acquired Conductor for parallel coding-agent orchestration; OpenAI announced it will acquire code-storage startup Pierre Computer. ([Axios](https://www.axios.com/2026/11/04/meta-acquires-ai-coding-startup-conductor))
- **Sequoia** — raised $10 billion while closing its Arc accelerator, sunsetting its Scouts program, and closing its London office. ([TechCrunch](https://techcrunch.com/2026/11/04/sequoia-hits-rewind-undoing-20-years-of-expansion/))
- **TeraWulf–Anthropic–Google** — Google will credit-backstop Anthropic's ~$19 billion of lease commitments at a Kentucky campus, binding Anthropic to Google-approved TPUs. ([Unite.AI](https://www.unite.ai/terawulf-lines-up-google-backstop-for-anthropics-kentucky-ai-campus/))
- **Ohio** — voters approved data-center restrictions in 14 cities across 21 midterm ballot measures. ([Fortune](https://fortune.com/2026/11/04/ohio-data-center-ballot-measures-midterm-elections/))
- **EU–Gemini** — a CJEU adviser found Gemini can infringe publishers by circumventing paywalls or reproducing distinctive expression recognizably enough to substitute. ([PPC Land](https://ppc.land/googles-gemini-can-infringe-press-rights-in-2-ways-eu-court-adviser-says/))
- **Apple** — the new 10-K flags autonomous AI agents acting on systems they aren't authorized to touch as a business risk. ([CNBC](https://www.cnbc.com/2026/11/03/apple-warns-of-ai-agents-behave-in-unintended-or-unpredictable-ways.html))
- **ChatGPT** — 1.2 billion weekly users, up 200 million in two months; search-style queries now equal ~20 percent of Google's search volume, per OpenAI's internal analysis. ([Big Technology](https://www.bigtechnology.com/p/openai-chatgpt-search-is-about-20))

## Also noted

- **RTX Spark laptops run Linux at about a third of Windows speed** — MindStudio measured GPT-OSS-120B at 65.4 tok/s on Windows versus 13.9 on Linux, blaming an encrypted power table only the Windows driver stack can decrypt. ([MindStudio](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop))
- **"Prompt adware" hides in a Codex jailbreak bundle** — Check Point dissects a package that injects a persistent ad for an LLM gateway into Codex's global identity file. ([Check Point](https://research.checkpoint.com/2026/free-the-model-sell-the-gateway-prompt-adware-hidden-in-jailbreak-bundles/))
- **World of Warcraft: Forever is drowning in AI addon clones** — the ecosystem went from ~200 developers to 10,000, roughly 1,000 abusive AI copycats, forcing Warcraft Logs to rework its API. ([404 Media](https://www.404media.co/world-of-warcraft-forever-is-already-overrun-with-ai-slop/))
