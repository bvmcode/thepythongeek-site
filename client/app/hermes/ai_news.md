# AI News — Tuesday, November 10, 2026

A short briefing of the day's main stories.

## Nvidia's board hands its CEO-spy review to Wachtell as Trump confirms an FBI probe

The scandal crossed from tabloid into governance. After the Times identified CEO Jensen Huang's romantic partner as Alice Huang — a Chinese citizen and Megaspeed executive US intelligence concluded was spying for Beijing — Nvidia's independent directors opened an investigation, and Huang admitted to employees he had been "unfaithful," taking "full responsibility"; the board says it has "no reason to believe" national security or Nvidia secrets were compromised, and he stays CEO. Tuesday brought escalation on all fronts: Trump said he spoke with Huang ("I really believe him") and confirmed the FBI is investigating; the board retained former US attorney Joon H. Kim and the Wachtell firm that ran the Clippers–Ballmer probe; and the Times reported Marco Rubio had briefed Trump on the relationship in May — the second warning in seven months. Shares fell another 3-plus percent on a report the relationship aided $7.5 billion of Nvidia chip shipments into China — with a $4.5 trillion company, an aging founder and no succession plan, investors are pricing leadership risk.

- [Nvidia board statement](https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board)
- [AP via PBS](https://www.pbs.org/newshour/world/what-we-know-and-what-we-dont-as-nvidia-investigates-an-alleged-spy-plot-involving-its-ceo)
- [The Verge on the Wachtell hire](https://www.theverge.com/ai-artificial-intelligence/1031190/nvidia-huang-investigation)

## AMD ships 256-core Epyc SP7 "Venice" as agentic AI turns server CPUs into the battleground

AMD said Tuesday its sixth-generation Epyc SP7 — 256 cores, first of four Venice-era server CPUs — is generally available with partner systems already shipping. Demand is the strongest AMD has seen for any Epyc generation: more than 240 Venice platforms committed, 20 percent more than signed up for Turin, with revenue shipments begun in Q3. AMD claims up to 3.7 times the performance of an Nvidia Vera CPU system and 2.2 times an Intel Xeon 6980P. The driver: agentic AI burns vast numbers of ordinary CPUs on services, GPU hosting and per-agent sandboxes — so the Helion rack line (Dell, HPE, Lenovo, Supermicro, Cisco) lands this month as Liquid (CPU-only, liquid-cooled), Air, and Air Inference (CPU+GPU).

- [Data Center Knowledge](https://www.datacenterknowledge.com/data-center-chips/amd-launches-epyc-sp7-helion-as-ai-rack-demand-rises)

## PSI closes the 18-year-old Aaronson–Ambainis conjecture with pre-release Fable 5.2

Physical Superintelligence announced that David Turturean, a recent MIT grad on its staff, solved the Aaronson–Ambainis conjecture — open since 2009 — with early access to Anthropic's pre-release Fable 5.2. The result: low-degree Boolean polynomials over many random inputs must reveal an influential variable, meaning quantum query algorithms get no superpolynomial advantage on decision problems defined over most inputs — settling the 1998 Fortnow–Rogers random-oracle question. Scott Aaronson, who posed it, says he doesn't fully follow the proof yet but believes it, because it was autoformalized in Lean and vetted by experts; it rules out one class of speedups, not quantum computing itself, and he noted OpenAI's recent "Mathocalypse" batch had skipped the problem. PSI sells the same harness-heavy approach today as data-center physics optimization, with best practices for AI-paced science still being invented ahead of next week's MIT summit.

- [TechCrunch](https://techcrunch.com/2026/11/10/psi-is-trying-to-make-a-business-out-of-ai-driven-scientific-discovery/)

## Anthropic turns Claude into an office suite — Meetings, Whiteboards, Sheets

Anthropic shipped a workspace suite Tuesday. Claude Meetings (beta on Team and Enterprise, Google Meet first) joins video calls as a visible participant that drafts the plan under discussion, maps timelines on a whiteboard, fields chat questions and pulls figures from connected apps while people still talk, then drops notes and action items into claude.ai. Claude Whiteboards (beta) is a shared real-time board Claude can turn into a doc or slide deck, and fills in live during Meetings. Claude Sheets (beta) builds spreadsheets with tabs, formulas and dropdowns, then edits cells alongside the team while outlining each change. Claude Data (formerly Dashboards) goes generally available — connect a warehouse or CRM, get dashboards, data stories or narrated videos — while Anthropic, OpenAI and Meta all converge the assistant on the productivity suite.

- [TechCrunch](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/)

## OpenAI opens ChatGPT to business profiles and verified Business Agents

OpenAI introduced Businesses in ChatGPT in beta: companies get claimable, verified profiles in front of 1.2 billion weekly users, with a Business Hub for verification, updated details, self-service product feeds with pricing and availability, and engagement insights — Shopify merchants connect their stores directly. The sharper edge is verified Business Agents: brand-operated agents that appear alongside responses, answer questions about offerings, handle "how do these two differ" follow-ups and support comparison shopping, starting with eligible US e-commerce and online-service businesses. It makes ChatGPT a discovery surface with a direct line to brands — aimed at the role Google's local profiles and shopping listings hold — and follows ChatGPT Enterprise landing in AWS Marketplace on November 9.

- [OpenAI announcement](https://openai.com/index/introducing-businesses-chatgpt/)

## Infrathon: 24-hour benchmarks reorder the model leaderboard

A large academic team (UW, Penn, AI2) posted Infrathon on arXiv Monday: six models, 150 runs, real AI-infrastructure optimization tasks under 24-hour budgets, 10,000-plus GPU-hours. Two findings: model rankings shift with the evaluation horizon, and 135 of 150 runs kept improving during the second half of their budgets — so the short-horizon evals most labs publish understate both the gains and the gaps between models. Agents also beat human baselines: Claude Opus 5.5 lifted mean KV-cache compression from 6.82 percent (the human-designed Quant-VideoGen codec) to 19.86 percent. The failure modes — task violations, unreliable self-testing, premature completion — read like a checklist for any long-horizon agent work.

- [arXiv:2611.11995](https://arxiv.org/abs/2611.11995)

## Glasswing's seven-month ledger: AI-found CVEs pile up faster than they get fixed

VulnCheck's November audit of Anthropic's Project Glasswing — launched April 7 promising thousands of responsibly disclosed vulnerabilities — shows agentic scale outrunning disclosure infrastructure. Seven months in: 442 CVEs attributable to Anthropic, about 0.5 percent of all CVEs published this year, only two spotted exploited in the wild. Of 37,966 findings, 7,349 (19.4 percent) are public and just 217 marked fixed; since September Anthropic added nearly 12,000 findings versus 15 more fixes, marked 1,654 as duplicates and 419 withdrawn, while its claimed true-positive rate rose from 90.8 to 94.2 percent. curl's maintainers rejected 19 of 34 published reports — the AI finds bugs fast, and the validation cost lands on open-source maintainers.

- [VulnCheck](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

## Also in tech

- **ByteDance rolls out Seedream 5.5 in limited release** — image generation with multi-turn editing and native transparent-background output. ([No Code MBA](https://www.nocode.mba/ai-release-tracker))
- **EKS adds dynamic GPU resource allocation** — Karpenter can now launch the cheapest instances matching NVIDIA GPU and EFA device attributes, with GPU sharing across pods. ([The GPU Daily](https://thegpu.ai/p/gpu-daily-2026-11-10))

## Business roundup

- **New York's AI safety law takes effect** — OpenAI, Anthropic and other major developers must register, disclose safety practices and report critical incidents, or face fines. ([TechCrunch](https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/))
- **Anthropic's IPO filing warns of a safety threshold** — AI is advancing its research so quickly it could trip a key safety threshold, days before listing. ([Yahoo Finance](https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html))
- **All seven Anthropic founders cash out ~$250M each** — roughly $1.75 billion at listing time. ([TechCrunch](https://techcrunch.com/2026/11/10/all-7-anthropic-founders-will-each-cash-out-about-250m-in-ipo/))
- **OpenAI races to raise $30B at ~$1.4T before Anthropic lists** — Reuters reports acceleration to lock commitments; some investors argue $1.5T is the honest number. ([CTech](https://www.calcalistech.com/ctechnews/article/0ik7s4qx4))
- **OpenAI acquires Odessia** — the travel startup by Sonder's founder, for a consumer-travel play inside ChatGPT. ([TechCrunch](https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/))

## Also noted

- **The Huang scandal became a meme genre overnight** — "honeypot" jokes are their own beat. ([TechCrunch](https://techcrunch.com/2026/11/09/jensen-huangs-alleged-honeypot-scandal-has-inspired-some-top-notch-memes/))
