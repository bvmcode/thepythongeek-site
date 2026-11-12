# AI News — Wednesday, November 11, 2026

A short briefing of the day's main stories.

## Gemini 4 Carbon goes wide, with a clock on its $2 pricing

Two weeks after opening it to cybersecurity defenders via Fairwind, Google made Gemini 4 Carbon available Wednesday UTC to all paying developers and enterprises and to AI Ultra subscribers in Antigravity, the Gemini app and AI Mode — introductory $2 per million input tokens and $10 output (Argon's entry price) until November 30, then $4/$20. Carbon is Google's ceiling-breaker, spending more tokens than Argon on exploration and verification for long-horizon agentic work, complex multi-step coding and open-ended research. Benchmarks: #1 on CursorBench 4.0, Perplexity's WANDR and Zapier's AutomationBench at over 2x lower cost per task than the next best external model, #2 on the new Multimodal Knowledge Agent benchmark at over 6x lower. Antigravity's /swarm preview turns one prompt into a tracked agent team — Carbon on architecture and auditing, lighter models on parallel workspaces, adversarial verifiers checking every change.

- [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)

## Gemini Decision 1: a model that answers instead of writing text

Google also shipped a new API shape Wednesday UTC: the Decisions API and Gemini Decision 1, which scores up to 1,000 typed questions against one shared multimodal input (text, images, audio, video, PDFs — up to 256K tokens) in a single forward pass, no token-by-token generation, no prose parsing. Three question types return calibrated probabilities with confidence scores — yes/no, multiple choice (2–255 options), rubric scoring — so code branches, routes and grades directly and falls back to a human on low confidence. Median latency is 50–100 ms, nearly flat from 1 to 100 questions, at $0.10 per million input tokens with zero output billed — nearly 5x cheaper than Gemini 3.5 Flash-Lite for this workload, with OpenRouter, LangChain and LiteLLM integrations live and Google-internal use routing Notebook queries and guarding Search's MCP tools. For classification and routing pipelines, it's a different primitive than a chat model.

- [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

## AlphaGenome 2 predicts how DNA reads out — cell type by cell type

DeepMind's new genome model answers what the first AlphaGenome blurred: not what a variant does on average, but what it does in this cell. AlphaGenome 2 conditions on cell type or state and was trained on more than 107 million single-cell profiles across 68 tissues from human and mouse samples. On TenK10K, covering 28 immune cell types, it identified 30 percent of causal variants per DeepMind, nearly double the 16 percent of the original model fine-tuned on single-cell data, and it scores unseen cell states from a snapshot of gene activity without retraining — variants hiding in tissue-level averages stop hiding. Inputs approach a million DNA letters; free via the AlphaGenome API for non-commercial research.

- [DeepMind blog](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)

## DeepMind's agents formally verified the code behind Signal — 6.5 million lines of Lean

Formal verification of a deployed crypto implementation has cost teams person-decades; DeepMind's new AlphaProof Code framework did Signal's in about four weeks with five researchers. The targets were real AArch64 machine-code artifacts of libsignal v0.105.4, proving one-to-one session security both symbolically and computationally. Gemini 4 Carbon prover agents generated about 6.5 million lines of machine-checked Lean on roughly 26,000 lines of trusted specification; humans reviewed about 1 percent of the codebase because Lean's kernel checks the rest. Two previously fixed libsignal bugs were reintroduced, and the machine-checked proofs flagged them. DeepMind calls it the first formal verification of a widely deployed protocol implementation at this depth and is open-sourcing the artifacts; the proofs establish the code meets the specs, assuming the cryptography itself is perfect.

- [DeepMind blog](https://deepmind.google/blog/introducing-alphaproof-code/)

## Baidu's ERNIE 5.5 Flash Preview: 280B total / 14B active, 1M context, Apache 2.0 soon

Baidu posted ERNIE 5.5 Flash Preview Wednesday UTC — the first post-trained model on its ERNIE 5.5 Flash Base: 280 billion total parameters, 14 billion active, a 1 million-token context, API live on Qianfan and free on OpenRouter, Apache 2.0 weights "soon." The demos are odd-job-agentic: a complete Unreal Engine 5.8 wuxia game written in C++ in one 11-hour session — the text-only model converts playtest complaints like a hovering character into code test cases because it can't see the screen — plus ~100 mobile mini-games from design docs, Blender-built scenes through the Python API (an airport, a full Hōryū-ji temple), FreeCAD models, and end-to-end science videos.

- [Baidu ERNIE release](https://ernie.baidu.com/release/ernie-5-5-flash-preview/)

## MiniMax open-weights an image model that edits and generates from one checkpoint

MiniMax published MiniMax-H3-Image Wednesday UTC — open weights, one checkpoint (a 33.1B-parameter DiT, 68.65 GB in BF16) that generates bare and edits when handed references, up to 16 of them. It's CFG-distilled — six fixed sampling steps at guidance 1, nothing to tune, no negative prompt — and emits native ~16-megapixel images (4096×4096 up to 6272×2688) with no upscaler. It derives from the H3 video model and shares that model's Qwen3-VL text encoder; MiniMax claims 4K images in under 10 seconds and API pricing at 50–70 percent of comparable services. ComfyUI supports it natively and it serves through SGLang on one GPU; the license is a community agreement, not a fully open license.

- [Hugging Face model card](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)

## Google open-sources XSE, the C++ server that took Python out of 6M-QPS inference

Google open-sourced XSE (XLA Serving Engine) Wednesday UTC under OpenXLA: a C++ serving runtime that removes the Python interpreter from the inference path. Models are authored in JAX, packaged with weights into a StableHLO "XLA SavedModel," and compiled to native code for the target hardware at serve time. Internally XSE handles more than 6 million queries per second across YouTube Shorts, Google Ads, Search and parts of Gemini Omni, and short-request tests showed 2–5x the throughput of its best optimized Python servers at a quarter of the memory. The target is the high-QPS task-model tier — classifiers, retrieval, moderation — rather than conversational LLMs; a PyTorch path arrives via TorchTPU.

- [Google open-source blog](https://opensource.googleblog.com/2026/11/supercharging-xla-inference-xla-serving-engine.html)

## Nvidia's board is reportedly preparing to oust Jensen Huang

Wednesday evening the Nvidia scandal escalated hard. Hours after the Times reported Huang had an affair with an Nvidia executive who reports to him — separate from the affair with Alice Huang, the US-intelligence-linked Megaspeed executive he admitted to Sunday — the Journal reported the board is preparing to remove the only CEO the 33-year-old company has known, meeting to decide his future as soon as Wednesday. Shares fell more than 8 percent after hours to $159.51; market value had already shed over $450 billion since the probe was announced November 8. The governance math is blunt: ~60 direct reports, no designated successor, no board chair — with "stay, with less" the likelier outcome if the board blinks.

- [CNN Business](https://edition.cnn.com/2026/11/11/investing/nvidia-stock-jensen-huang)
- [TechCrunch](https://techcrunch.com/2026/11/11/nvidias-stock-drops-as-board-reportedly-preps-to-oust-ceo-jensen-huang)

## Also in tech

- **Tether's QVAC BotPsy-0.8B** — open-weight on-device 0.8B agent model that doubles its Qwen3.5-0.8B-Think base on tool-use tests (τ-bench 23.2→51.5) and beats models up to 2.5x its size. ([Tether](https://tether.io/news/tethers-800m-ai-agent-beats-models-2-5x-its-size-on-everyday-phone-tasks/))
- **Fish Audio's Live 3 is full-duplex** — the voice model keeps listening while it speaks, with learned backchannels and company-reported latency as low as 186 ms; a platform ships alongside for action-taking voice agents. ([Fish Audio](https://fish.audio/))
- **Fireworks AI's breach got worse** — a November 9 update to the October intrusion says billing data and subsets of customer model weights and datasets were reached, after the first bulletin ruled those out. ([The Register](https://www.theregister.com/cyber-crime/2026/11/10/fireworks-ai-gets-burned-twice-as-customer-data-exposure-widens/5308722))

## Business roundup

- **OpenAI's Q3 revenue crossed $10 billion** — up ~50 percent sequentially to a ~$50B run rate with a $10.9B adjusted operating loss and ~100M paying ChatGPT subscribers; Anthropic booked $17B the same quarter, with a small operating profit before its IPO. ([WSJ](https://www.wsj.com/business/earnings/openai-continues-to-suffer-heavy-losses-as-revenue-rises-to-10-billion-d2a96bbb), [AI Chat Daily](https://aichatdaily.com/ai-business/openai-quarterly-revenue-tops-10b-operating-loss-widens))
- **Anthropic's IPO is oversubscribed multiple times** — roadshow opened Tuesday at $70–78, ~$1.4T target, $ANT pricing November 18, Nasdaq trading November 19. ([Quartz](https://qz.com/anthropic-ipo-oversubscribed-roadshow-demand-111126))
- **TSMC puts up to $1B into Anthropic and OpenAI** — $500M in Anthropic common at the IPO price, $500M in OpenAI preferred, plus a $500M strategic-investment vehicle. ([Focus Taiwan](https://focustaiwan.tw/business/202611110009))
- **CoreWeave's "breakout quarter" snapped the selloff** — Q3 revenue $3.66B (+168 percent), guidance raised to $13–13.3B, backlog $132.5B, ~$9B of prepayments expected in three months; the stock jumped 25 percent with AI infra. ([CNBC](https://cnbc.com/2026/11/11/coreweave-crwv-outlook-earnings-ai.html))
- **ChinaTalk finds US data vendors selling ~$500M to Chinese labs** — nine firms including Mercor, Surge AI, Turing and AfterQuery sold training data and RL environments, some of the same products sold to OpenAI and Anthropic, largely outside export controls. ([ChinaTalk](https://www.chinatalk.media/p/the-us-is-selling-rl-environments))
- **United Airlines blocks agentic bookings** — third-party AI agents may browse but can't buy, over credential-exposure, fraud and federal-rule risks; CEO Scott Kirby: "I don't want to create another middleman." ([Bloomberg via Seattle Times](https://www.seattletimes.com/business/united-blocks-ai-agents-from-booking-flights-ahead-of-holidays))

## Also noted

- **A blacklisted Chinese university bought H200s anyway** — procurement records show military-linked Northwestern Polytechnical bought two Nvidia H200s (874,700 yuan) through a reseller in October and rented A100 and A800 servers this year. ([Quartz/Reuters](https://qz.com/military-linked-university-nvidia-h200-chips-blacklist-111126))
- **Gemini's voice mode lands on Apple CarPlay** — global iOS rollout, in-car chats syncing to the iPhone's Gemini history. ([Quartz](https://qz.com/google-gemini-voice-ai-apple-carplay-111126))
