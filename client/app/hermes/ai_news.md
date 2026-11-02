# AI News — Monday, November 2, 2026

A short briefing of the day's main stories.

## Best model still fails most real expert work, new benchmark finds

SemiAnalysis released GDPx, a benchmark of long agentic tasks in eleven fields chosen for economic stakes — chip design, cybersecurity, biology, finance, law, quant trading, materials science, alignment, and software engineering — built with specialist vendors in each field. Claude Opus 5.5 leads at 12.0%, with Gemini 4 Carbon at 10.9% and GPT-6 Astra at 9.6%. Nearly every model scored zero on the finance and legal tasks. The firm found safety classifiers now measurably depress scores: Meta's Muse Wonder was the strongest cybersecurity model partly because it refuses less. The takeaway is a floor reading on where frontier agents actually are.

- [SemiAnalysis](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities)

## Anthropic reports $17 billion in quarterly revenue ahead of its IPO

Anthropic amended its S-1 with full third-quarter results: roughly $17 billion in Q3 revenue, about twelve times a year earlier, against a $23.29 billion net loss driven mainly by accounting charges on notes and derivatives, not cash burn. Nine-month revenue reached $33.24 billion, with purchase commitments and leases of about $895.4 billion, substantially all for compute. The Wall Street Journal separately reported that institutional investors are pushing the mid-November Nasdaq listing toward a $1.5–1.6 trillion valuation, down from $2 trillion previously floated.

- [The Decoder](https://the-decoder.com/anthropic-grows-revenue-twelvefold-but-posts-23-billion-loss/)

## Marvell to buy Lumentum for $115 billion in stock, its AI-connectivity bet

Marvell confirmed an all-stock acquisition of optical-component maker Lumentum at an implied enterprise value of $115 billion — about $1,132 per Lumentum share, a 23.9% premium to the October 28 close — the largest public technology acquisition ever. Marvell shareholders will own 67% of the combined company, and the deal targets a close in early 2028. The logic: optical links between AI chips have become the constrained piece of the data-center buildout. Lumentum CEO Michael Hurlston said the combination could help meet rising demand for connections between AI components, and called the opportunity enormous.

- [CNBC](https://www.cnbc.com/2026/11/02/marvell-lumentum-ai-deal.html)

## The New York Times and other publishers sue the Brave browser

The New York Times and three other newspapers sued Brave, alleging the browser company copied their articles and supplied the content to AI companies without permission. The lawsuits also challenge a Brave feature that bypasses paywalls, along with the company's ad practices. The suits open a new front over who profits from published writing: this time the target is the browser layer that funnels the web's content into AI products wholesale.

- [TechCrunch](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/)

## On the eve of the midterms, chatbots fail almost 40 percent of election answers

A study by Forum AI, which evaluates AI models, found that almost 40 percent of answers from eight chatbots to US election questions contained at least one factual error, AFP reported ahead of the November 3 vote. Logistics questions failed more often than candidate questions: Google's Gemini 3.6 Flash gave the wrong deadline to request a mail-in ballot in Pennsylvania, a week too late to be useful, and Claude credited a North Carolina congressman with another person's résumé. NewsGuard separately found Google's AI Overview, Gemini, and Copilot repeating a smear of a Texas Senate candidate that fact-checkers had already debunked.

- [AFP via Arab News](https://www.arabnews.pk/world/spewing-us-election-falsehoods-ai-chatbots-face-scrutiny-3005766)

## MIT shows GPT-6 Astra editing a neural network's weights directly

MIT CSAIL researchers published "Sparks of Weight-Space Programming," showing frontier models can natively read and write raw network weights with no gradient descent. GPT-6 Astra could infer what small networks were trained on from the raw numbers alone, write from scratch game-playing networks that beat networks trained with PPO for 100 million steps, and — asked to fix looping failures in Qwen3.5-0.8B's math answers, a flaw Qwen's own model card warns about — it edited 0.016% of the weights directly. MATH-500 rose from 7.9% to 48.1% and instruction-following tripled. The edit mostly stopped repetition: an interpretability result, not a leap in math skill.

- [Research blog](https://rikiyat.github.io/blog/weight-space-programming/)

## OpenAI signs four Abu Dhabi deals spanning government, energy, and investment

OpenAI signed four agreements in Abu Dhabi with the government, the state investor Mubadala, and Inception42, a subsidiary of G42, after Altman met Crown Prince Khaled bin Mohamed. The most concrete is a "machine-readable government" project that turns policies and regulations into a form AI can check applications against, with a food-imports pilot already running on models served from inside the UAE and officials keeping final decisions. The others cover investment analysis with Mubadala, a five-year Frontier-platform rollout by Inception42, and deployment of frontier models across ADNOC operations with G42. No contract values were disclosed; the deals land as OpenAI seeks UAE backing for a round near $20 billion.

- [CNBC](https://www.cnbc.com/2026/11/02/openai-abu-dhabi-ai-deals.html)
- [Reuters](https://www.reuters.com/business/energy/abu-dhabis-adnoc-g42-sign-deal-with-openai-sam-altman-travels-uae-2026-11-02/)

## Oracle files a $20 billion stock-and-bond sale as AI spend leans on debt

Oracle filed plans to raise $20 billion — $10 billion in shares and $10 billion in bonds — to fund its AI infrastructure buildout, and its stock fell 8.8% Monday as investors weighed the plan against the company's existing debt. Bloomberg separately reported that Meta is sounding out an investment-grade bond offering of at least $20 billion, after a quarter of negative free cash flow and $135–145 billion in planned data-center capex. Both test how much leverage the debt market will extend.

- [CNBC](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html)

## Also noted

- **Anthropic puts a near-term self-improvement warning in its filing.** The same S-1 cautions that "using AI to help build more capable AI could also pose a considerable safety risk," pointing to its Responsible Scaling Policy and what it calls recursive self-improvement; no current model has reached the threshold. ([TechCrunch](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/))
- **Meituan ships LongCat-2.5.** A natively multimodal mixture-of-experts model with 1.6 trillion total parameters, about 48 billion active per token, a 1-million-token context window, built for agentic coding and GUI work. ([TechNode](https://technode.com/2026/11/02/meituan-launches-longcat-2-5-multimodal-ai-model-for-extended-coding-tasks/))
- **Grok Bot gets throttled.** Usage limits fell for some users weeks after Elon Musk called it his fastest-growing product; Musk said its cost of serving was "unsustainably high relative to revenue," giving no figure or fix. ([The Decoder](https://the-decoder.com/spacexsi-apparently-cuts-grok-bot-quotas-weeks-after-musk-called-it-his-fastest-growing-product/))
- **Squarespace cuts 19% of staff.** About 300 employees, framed as simplification for growth phases, as AI website builders — its own Blueprint AI and Forma among them — reshape the market. ([TechCrunch](https://techcrunch.com/2026/11/02/web-host-squarespace-lays-off-19-of-its-employees))
- **South Korea's October exports hit a record $115.3 billion.** Chip exports jumped 259% to $56.4 billion on AI demand, with US-bound shipments nearly tripling as buyers pay for high-bandwidth memory. ([AI Pro Playbook](https://aiproplaybook.com/top-ai-stories/2026-11-02))