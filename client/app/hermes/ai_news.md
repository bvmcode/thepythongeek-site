# AI News — Sunday, November 22, 2026

A short briefing of the day's main stories.

## OpenAI publishes its pretraining loss curve — and proposes limits with a number on them

OpenAI chief scientist Jakub Pachocki published the company's internal log-perplexity curve on Nov 22: GPT-3.5 at ~0.99 enabled fluent conversation, GPT-4 at ~0.91 made chain-of-thought worth eliciting, recent models below 0.8 are where serious cybersecurity and math ability emerged, and at ~0.76 the model began resolving open problems "one after another in a single Slack thread." Since progress mostly works by harnessing a compressor, he argues perplexity stays informative while benchmarks saturate — so labs should expose pretraining numbers and commit to common limits, thresholds untouchable until a monitorability milestone (a CoT-monitor successor, say) exists. The ~0.68–0.7 window should bring capabilities nobody has named: "we may not be testing for them today." Days after Amodei's pacing essay, the first attempt to put a number under it.

- [OpenAI, Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/)

## The canary fallout lands: OpenRouter off-boards three providers — and an agent leaked the key

OpenRouter's Nov 22 post turns the Dragos canary findings into consequences: no breach of OpenRouter itself, but three providers — Novita, Phala and Together — off-boarded, 125 endpoints stripped of Zero Data Retention eligibility (some as precaution), customers notified, and removed endpoints must earn the ZDR label back with assurances. Behind it sits Together AI's notice: while engineers developed xorl, a public repo of its distributed-training framework, an AI coding agent committed a credential that unlocked a private Hugging Face repo of authorized prompt samples from the serverless service — requests to MiniMax M3, GLM-5.2 and Kimi K2.6, mostly June 24 and July 4, 8 and 14. Scanning caught the key and the commit was reverted, but in the window an unauthorized party downloaded the samples, then searched them for other services' credentials and tested those found — five were Dragos canaries. Together, forensics and law enforcement involved, has "no reason to believe" the data leaked further and understands it was deleted. The old leak story had a tired human and a rushed commit; this one was committed by software.

- [OpenRouter, the enforcement post](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)
- [Together AI, the security notice](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)

## Meta's Muse egress gate fell to patience — and a CSA note turns the chain into lessons

The Cloud Security Alliance's weekend note dissects the NebuSec chain (disclosed Nov 20, fully patched by Meta before publication) that broke Meta's Muse agent in three stages, none needing prompt injection. Muse's bundled Chromium ran a stale patch level with the IPC sandbox disabled for PDF export, so one parser bug — worth about $500 on the exploit market — turned "save page as PDF" into a 0.5-click RCE inside the agent container. The theft was policy-compliant: Sentinel, the egress gate and permission authority, treats bodiless GET/HEAD/OPTIONS as silent reads, screened against hex/Base64 decoding, entropy thresholds and per-domain volume budgets — rules that tell a patient attacker exactly what passes; NebuSec moved conversation history and stored memories out without an approval prompt. Sentinel's hook rides the container's cgroup, so the last stage left it behind: the shared VM kernel had hardening disabled, automated exploits won >99.9% of runs, and VM root reached the volume, credential store and Sentinel itself. The CSA's lesson: container-scoped enforcement and silent reads — the two assumptions that broke — are common design choices elsewhere; use VM-level egress enforcement, deny-by-default destinations, and red-team the classifier.

- [CSA, Breaking the agent's egress gate](https://labs.cloudsecurityalliance.org/research/csa-research-note-meta-muse-sentinel-bypass-agent-egress-202/)
- [NebuSec, Inside Meta Muse](https://nebusec.ai/research/inside-meta-muse/)

## Frostbite: a CPU designed end to end by AI agent swarms — pre-silicon, 4.59x claimed

Architect Labs' writeup (Nov 18, caught by mainstream hardware press Nov 22) claims a general-purpose CPU whose compiler, ISA, microarchitecture, RTL, verification and final GDS were iterated entirely by its agent swarms from "zero architectural priors." The substrate is Lafont's 1990 interaction nets: a program is a graph of rewritable nodes, every value used exactly once, active pairs never overlapping — work runs in any order with no shared mutable state, so parallelism is a property of the program, not something out-of-order windows and coherence protocols spend silicon rediscovering. Claims, all pre-silicon: 7 nm timing closed at 800 MHz (500 MHz in GDS); a 0.792 mm² quad versus an unnamed "silicon-proven" dual-issue in-order core (0.895 mm²) withheld "for legal reasons"; a 4.59x geometric-mean performance-per-watt and 8.77x per area across 25 workloads, split 6.02x on the ten tuned targets and 3.83x on the fifteen held back. Nothing has touched silicon and the baseline is microcontroller-class — but the economics point stands: an architecture that sat in papers for 35 years reached a finished layout because agents did the exploring.

- [Architect Labs, the technical writeup](https://architectlabs.com/blog/frostbite)
- [Hardware Busters, the fine print](https://hwbusters.com/news/frostbite-cpu-was-designed-end-to-end-by-ai-agents-and-architect-labs-claims-4-59x-the-perf-w-of-an-in-order-core/)

## Pandex puts 2.8 million European legal documents behind one MCP server

Pandex, launched Nov 22, starts from the view that in law the substrate, not the model, is the bottleneck — agents need exact official text, versioning, a citation graph, and an honest answer about missing sources. It serves EU legislation plus the highest courts of France, Germany, the Netherlands, the UK, Austria, Switzerland and Luxembourg (and the ECHR): 2.8 million documents — 2.4 million court decisions, 421,000 acts and codes — with 37 million citations linked to the passage each points at, pulled from the institutions themselves. The MCP server exposes six read-only tools (search, get_document, get_outline, get_citations, get_changes, list_sources) and plugs into Claude Code, claude.ai, Cursor, Copilot, Windsurf, Zed and Gemini; 50 requests a day need no key, 1,000 on a free one. Trust comes from point-in-time law — what a statute said on a date — and a public coverage register of 41 institutions, 33 complete with gaps named (the Cour de cassation partial, government dumps two months stale). Spain, Italy, Ireland and Belgium are next.

- [Pandex, the MCP server and API](https://github.com/pandex-io/pandex-mcp)
- [The Tesseract Press, on the launch](https://thetesserapress.com/articles/pandex-official-european-law-for-ai-agents-over-mcp)

## SWE-CoWork: agents ace the tests, then finish fewer than 1 in 10 office assignments

The Decoder's Nov 22 writeup covers SWE-CoWork: 101 assignments across 101 real repositories in 11 languages, staged inside a simulated engineering organization where 26 colleagues hold distinct, bounded pieces of the requirement — agents start from a brief handoff, recover requirements scattered across people and records, reconcile conflicting evidence, and get graded by private executable tests. The gap between passing tests and delivering work is stark: the two leading models satisfy roughly 63% of fail-to-pass tests but fully complete fewer than 8% of assignments. Handing GPT-6 Astra and peers complete requirements upfront lifts fail-to-pass ~16 points while complete-task success stays unchanged — coding isn't the bottleneck, the delivery process is. The trajectory analysis is blunt: Claude Opus 5.5 routes 93% of first clarifying questions to the accountable colleague yet walks off with only 64% of colleague-held requirements, deferred questions go unfollowed, and 31% of self-reported-complete requirements fail their tests. Sustained requirement tracking — through implementation, verification and handoff — is where autonomous software engineering breaks.

- [The Decoder, the writeup](https://www.the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/)
- [SWE-CoWork, the paper](https://arxiv.org/abs/2611.20218)

## Also in tech

- **Neuralink flies GTA VI on imagined finger taps** — a trial participant plays the Nov 19 title via an implant mapped by JoypadOS to a PS5 controller (ring-finger tap = punch, hand slide = pitch); no latency figures yet. [Hardware Busters](https://hwbusters.com/news/neuralink-gta-vi-demo-has-a-trial-participant-flying-planes-by-imagining-finger-taps/)
- **Sarvam's 105B API switches to new open weights** — Sarvam-105B-1711 (Apache-2.0, 65 GB NVFP4 build) serves the same endpoints with no code changes; Flash-Lite quality for under a fifth of the price, Sarvam says. [Changelog](https://docs.sarvam.ai/changelog/2026/11/22), [blog](https://sarvam.ai/blogs/sarvam-105b-1711)

## Business roundup

- **Bessent won't rule out Huang's return to Nvidia** — "I said they should go to the outside, but he's on the outside now," the Treasury secretary told Face the Nation Nov 22, after Trump backed reinstatement; Nvidia owes Treasury export-control answers by Nov 25. [Yahoo/Motley Fool](https://finance.yahoo.com/markets/stocks/articles/u-treasury-secretary-scott-bessent-210804381.html)
- **AI-server prices climb mid-contract** — Dell, HPE, Lenovo and Supermicro raising Nvidia-server prices up to 45% months after signing, passing on memory costs. [FT](https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f)
- **The AI-search drag reaches Apple** — Google -18% since search-ad growth slowed to 12% (from 17%) on AI-feature pressure; Apple Services cooled to 10%, partly the 36% Safari ad share Google pays. [The Information](https://www.theinformation.com/articles/apple-got-caught-google-search-ads-slowdown)
- **Studios move to compel Midjourney's v8 source code** — Disney, Universal and Warner Bros.' Nov 21 motion demands the full v8 source and its "torch aesthetic-redux" component. [MLQ](https://mlq.ai/news/disney-universal-and-warner-bros-ask-the-court-to-make-midjourney-comply-on-its-v8-source-code/)
- **The WSJ profile revives an old Amodei aside** — at OpenAI he reportedly floated immersive video games for "the political strife caused by AI-induced joblessness." [The Verge](https://www.theverge.com/ai-artificial-intelligence/1039745/dario-amodei-video-games-ai-joblessness)
- **South Korea's education chief resigns over an AI-cheating scandal** — stepped down Sunday over AI-assisted cheating ahead of the entrance-exam fallout. [AFP](https://www.afp.com/en/south-korea-education-chief-resigns-amid-ai-cheating-scandal)

## Also noted

- **Binding of Isaac: Repentance Plus pulls its AI music** — Suno metadata found in a GTA-spoof daily-run section; review-bomb first, removal after. [The Verge](https://www.theverge.com/games/1039770/binding-of-isaac-ai-music)
- **Dragos: AI is compressing OT attack planning** — AI speeds attack preparation on industrial targets, but model output still needs human review before acting. [ExplainX](https://explainx.ai/blog/ai-cyber-threat-operational-technology-dragos-robert-lee-november-2026)
