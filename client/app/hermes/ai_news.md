# AI News — Saturday, November 21, 2026

A short briefing of the day's main stories.

## The Lean and Mathlib communities certify the Claude-assisted Riemann proof

One day after Anthropic mathematician Levent Alpöge released a Riemann Hypothesis proof as a 17-million-line Lean library, the Lean and Mathlib communities issued a joint statement — endorsed by the Lean FRO and the Mathlib Initiative — certifying that "both the statement and the proof are correct." All 175,187 modules compile on stock Lean 4.33.1 with zero errors, Mathlib files are byte-identical to the official cache, the five headline theorems depend only on the three standard axioms, a Mathlib-only challenge file matched Alpöge's proved theorems via two independent statement-comparison tools, and the ~61.5GB exported proof was accepted by the Lean kernel, the Rust kernel nanoda and con-leche — checkers carrying a formal proof they cannot accept a false theorem — on an inert export malicious code couldn't touch, with every check logged by Andrew Sutherland at MIT. Terence Tao's first read: the argument uses the full power of modern Langlands and arithmetic geometry, and digesting it will take time, so the $1M Clay prize stays put. Same-day twist: Stanford's Ravi Vakil posted a competing human-written Generalized-RH draft by postdoc Alessandro Masullo — "all human, with no AI," not yet machine-checked. Scope: RH plus Dirichlet GRH only, and the formal object at that.

- [Lean and Mathlib communities, the joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- [Andrew Sutherland, MIT verification files](https://math.mit.edu/~drew/grh/)
- [Alpöge's announcement](https://alpo.ge/remark.pdf)

## OpenAI explains the outage that failed three-quarters of ChatGPT

OpenAI's same-day post-mortem (Nov 21) covers the 1:48–5:21 PT incident that peaked at a 75% request-failure rate on ChatGPT. Scheduled maintenance on a PostgresDB backing the Primary API service failed both read replicas at once — and they were load-bearing, handling user and service-to-service authentication stack-wide — so every dependent request path died while replica lag grew unboundedly; revivals and out-of-region replacements failed, and two brand-new replicas in the same region recovered it. Already shipped: a moratorium on similar maintenance, config changes to cut connection churn, a flag shifting traffic off replicas by percentage, and a verified failure hypothesis by routing 100% of queries to the primary. Promised: pre-maintenance reviews, hot-standby capacity, replica-lag recovery automation, and a full-stack redundancy review.

- [OpenAI status, the write-up](https://status.openai.com/incidents/01JMYB602A6H2E04Y1497J434X/write-up)

## OpenAI details its anti-distillation defenses — with numbers

A Nov 20 post explains how OpenAI detects and disrupts "adversarial distillation" — rebuilding frontier capability from unauthorized outputs, minus the safeguards. In adaptive black-box red-teaming, attack success rates for extracting protected reasoning fell from 54.0% on GPT-6 Astra to 0.2% on GPT-6.2 Astra for earlier-turn reasoning, and 22.9%→0.9% for the current turn. Weekly enforcement against distillation campaigns has ranged from thousands to tens of thousands of accounts; the post says it briefed Congress in February on DeepSeek distillation attempts and attributed a September campaign to people associated with Moonshot AI. GPT-6.2 now ties reasoning to its origin conversation, and the usage policies effective Nov 20 bar using OpenAI outputs to prepare or score training data for rival models.

- [OpenAI, Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation)

## Two million canary prompts expose a leaky AI supply chain

Dragos' HD Moore sent ~2M prompts from July through November carrying unique URLs and canary credentials, then watched where they surfaced: evidence at least three AI providers were compromised and their prompts siphoned, inference-marketplace resellers logging and misusing customer prompts, and providers ignoring Zero Data Retention flags — the baited AWS keys saw tens of thousands of AWS API calls. Ars Technica's follow-up (Nov 21): OpenRouter emailed customers that a third party may have read prompts sent to MiniMax models, directly or via resellers AtlasCloud, Novita and StreamLake, with planted URLs accessed 40–130 hours after submission; OpenRouter pulled the "Zero Data Retention" label from those endpoints while investigating. Structural lesson: prompts are encrypted in transit but decrypted and logged at every router hop.

- [Dragos, Three breaches, endless leaks](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)
- [Ars Technica, the canary research](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/)

## Signal starts blocking the OS-level AI agents that read your screen

A Nov 20 post from Signal president Meredith Whittaker argues agents with on-screen awareness undermine app-level privacy: E2EE protects messages in transit, but an assistant reading your screen sees exactly what you do, outside Signal's control. An iOS 27 toggle blocks Siri's scanning and in-app screenshots and hides Signal from the App Switcher; Android auto-enables screen security when an AI assistant's screen access is detected; on macOS the app says it can't reliably prevent it. The post names Google's Gemini Intelligence and Apple's Siri AI directly, follows Reuters' report that Meta's Muse agent read Signal messages via notification and accessibility permissions, and asks Apple, Google and Microsoft for a documented app-level opt-out from agent data access.

- [Signal, Protecting your privacy](https://signal.org/blog/protecting-your-privacy/)

## Oracle: the OpenAI buildout is fully funded, and Abilene is nearly done

Oracle's Nov 20 statement answers the week's core fear — whether the money behind the compute build-out exists: "Oracle has secured all the funding we need to fulfill our contract with OpenAI." The final capital raise earlier this month made it, by its own claim, "the first hyperscaler fully funded for this investment cycle," with vendor financing in place and further vendor talks "just additional options." Execution detail: the Abilene, Texas campus — where "Astra-6" was trained — is nearly complete; the next gigawatt campus in Shackelford County is fully permitted; NVIDIA Vera Rubin rack handovers are "on track for the coming weeks." Guidance: positive free cash flow in the second half of FY2028, over $30B in FY2029, self-funded growth from there — and the stock, down 8.48% in Friday's rout, rebounded after hours.

- [Oracle statement](https://www.oracle.com/news/announcement/oracle-statement-2026-11-20/)

## Also in tech

- **Harness adapters** — Hugging Face shows a small LoRA trained for a specific harness lifts frozen Qwen3.8-27B from 39% to 55% on Terminal-Bench 2.1 at ~half the tokens, validated across the pi, OpenCode and Hermes Agent harnesses. [HF](https://huggingface.co/blog/harness-adapters-at-scale)
- **MedChemBench** — OpenAI's medicinal-chemistry benchmark: 99 problems from 117 papers/patents, 761 molecular structures; GPT-6.2 Astra takes 84.5% of available credit at xhigh vs 83.3% (GPT-6 Astra), 58.2% (GPT-5.6 Sol). [OpenAI](https://openai.com/index/introducing-medchembench/)
- **LangChain's "knowledge factory"** — Harrison Chase's Nov 21 piece: the missing layer for enterprise agents isn't context but maintained knowledge of how your company works. [LangChain](https://www.langchain.com/blog/knowledge-factory)

## Business roundup

- **Nvidia slipped below Alphabet in market value** — first swap in over two years (~$3.44T vs $3.41T), ~$2.3T off its October peak. [Reuters](https://www.reuters.com/business/retail-consumer/nvidias-share-slide-knocks-it-below-alphabet-valuation-2026-11-20/)
- **The Nasdaq erased all its 2026 gains** — Friday's 5.28% plunge capped the worst week since March 2020 and cooled Anthropic's second trading day. [The Guardian](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)
- **Trump threatens a "tremendous tax" on AI data centers built outside the US.** [The Verge](https://www.theverge.com/policy/1038892/trump-foreign-data-centers-tax)
- **The BIS remote-access rule keeps closing chip routes** — TSMC and Samsung suspended some China-linked orders at 16nm-and-below pending US licences; Nikkei reports the rules now reach consumer SoCs. [AI Weekly](https://aiweekly.co/alerts/tsmc-pauses-shipments-as-new-us-chip-rules-hit-beyond-ai)
- **Amazon nears a ~$7.5B Decart acquisition** — nearly double its $4B May valuation, for the chip-switching software and Lucy/Oasis world-model maker. [Crypto Briefing](https://cryptobriefing.com/amazon-nears-deal-ai-startup-decart/)
- **SoftBank's Son explored a $1 trillion SK Hynix buyout** — he sought Wall Street financing before SoftBank said the idea is off the table. [Reuters](https://www.reuters.com/world/asia-pacific/softbanks-son-explored-1-trillion-buyout-sk-hynix-information-reports-2026-11-21/)
- **UN talks punt on "killer robots"** — the CCW conference gave countries two years to propose rules, binding or optional, after the US pushed for nonbinding guidelines. [NPR](https://www.npr.org/2026/11/21/nx-s1-6047916/killer-robots-un-drones)

## Also noted

- **A frontier-pause pitch and its rebuttal** — Dan Hendrycks backed an indefinite pause on frontier training at a DealBook panel; Max Hodak countered enforcement would take a surveillance state. [The Next Web](https://thenextweb.com/news/dealbook-agi-panel-hendrycks-pause-frontier-ai-hodak-surveillance)
- **Provenance metadata is rare in the wild** — of 31,734 images through Uravation's AI-image checker since September, 5.8% carried C2PA data and 87.3% had no record of AI, a camera or editing software. [ASCII.jp](https://ascii.jp/elem/000/004/453/4453835/)
