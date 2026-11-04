# AI News — Tuesday, November 3, 2026

A short briefing of the day's main stories.

## Google tells K-12 schools to switch AI on or lose Search

In a Tuesday education update, Google said access to Gemini, Gemini Notebook, Gemini in Classroom, and Google Search will be "entirely off" for K-12 student accounts unless administrators explicitly turn them on, and that schools which disable the Gemini features lose Search too: there is no toggle that keeps one without the other. "Search and AI are deeply integrated," Google's education VP Chris Phillips told The New York Times, which reports the choice arrives in early 2027. Former FTC chair Lina Khan called it "using its search monopoly to coerce schools into adopting AI"; NYC and LA, the nation's two biggest districts, already have temporary AI bans in elementary and middle schools — and the ultimatum lands after October Senate pressure over the August default-on Gemini rollout in Classroom.

- [The Verge](https://www.theverge.com/tech/1025411/google-turn-off-search-ai-features)
- [AP](https://apnews.com/article/ai-schools-classroom-students-google-7ba4219e505db1c11d672f6eefe7155a)

## Election Day: the chatbot war rooms face chatbot errors

OpenAI and Anthropic both staffed dedicated election "war rooms" for Tuesday's midterms — a first for both — monitoring for misuse and ready to respond to misleading voting information, Semafor reports. Their products remain part of the problem: WIRED's Election-Day piece cites Forum AI research finding almost 40 percent of mainstream chatbots' election answers contained at least one factual error — Gemini gave November 3 as the Pennsylvania mail-ballot deadline; the real date was October 27 — while NewsGuard found chatbots cite "pink slime" partisan sites in half of candidate-and-policy queries, ChatGPT the worst above 70 percent and Grok the best at 30 percent. The war rooms can catch incidents; the answers themselves are the risk.

- [WIRED](https://www.wired.com/story/heres-why-you-shouldnt-use-ai-to-vote/)
- [Semafor](https://www.semafor.com/article/11/02/2026/election-war-rooms-enter-the-ai-age)

## Anthropic's amended IPO filing: a $17B quarter, $895B of compute, and an RSI warning

Monday's revised S-1/A, a week after the original and ahead of a Nasdaq debut expected this month under ticker ANT, shows quarterly revenue of $17 billion (up from $11.5 billion) against a $23.3 billion quarterly net loss, nine-month revenue up 13-fold to $33.2 billion, and a nine-month loss of $104 billion including a $94 billion accounting charge from financing agreements. Anthropic disclosed $895.4 billion of committed AI compute and infrastructure spend, $70 billion of it due within 12 months; TechCrunch's read has compute absorbing 58 percent of quarterly revenue (up from 48 percent), revenue per compute-dollar down from a peak above 2x to 1.72x, and a $10 billion quarterly compute bill whose $5 billion of short-term commitments cost "significantly more" than multi-year terms — the price of chasing demand through providers like SpaceX, at $1.25 billion a month. The risk factors add a quieter disclosure: Anthropic "may imminently meet" its Responsible Scaling Policy's definition of "dramatically accelerated progress attributable to AI" — recursive self-improvement — with no current model past that threshold and a promise to keep Claude from building "successive generations of frontier models without meaningful human supervision." AI building AI is now formally an SEC-disclosed risk.

- [AP](https://apnews.com/article/anthropic-ipo-revenue-ai-claude-0cbd1a649a4cce904be59af8f6b30179)
- [TechCrunch](https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/)

## Anthropic publishes FlashProve: cryptographic proof of which model answered

Anthropic released research Tuesday on FlashProve, an open-source design for "provable inference": labs would publish a cryptographic fingerprint of each model release, without revealing weights, so anyone can verify locally that an output really came from the model claimed — the way an email signature proves a sender. It targets live trust gaps, from silently swapping in cheaper models to claims that a library "was scanned for vulnerabilities by a frontier cybersecurity model," and migration trackers flagged xAI just this week for quietly redirecting a retired image model's traffic to a cheaper model's lowest-quality output. Anthropic shipped a specification and working code on GitHub, and stages it as research with no deployment planned yet.

- [TechCrunch](https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/)
- [Anthropic](https://www.anthropic.com/research/provable-inference)

## Goldman Sachs pulls Claude Code and GitHub from traders and bankers

Internal guidance updated in October and seen by Bloomberg restricts coding agents — Anthropic's Claude Code and Microsoft's GitHub — to Goldman's engineers, ending months in which traders and bankers used them to follow client trading flows, simulate market shifts, and draft documents. "Strats," the hybrid quant-engineer-trader group, keep access; the move unwinds CIO Marco Argenti's spring push for non-engineer vibe-coding with engineer review. Spokesperson Nick Carcaterra called it the end of the experiment: after weighing "productivity and risk management," "we put them in the hands of those who are best suited to leverage them for the long term." The bet: the limiting factor on agents at work is not capability but the number of people who can audit what they produce.

- [Quartz](https://qz.com/goldman-sachs-restricts-ai-coding-tools-traders-bankers-110226)

## Beijing speeds toward a national AI law as its regulator flags AI concentration

At a Tuesday briefing on the 15th Five-Year Plan, NDRC deputy director-general Wang Ruomeng said China will accelerate a basic national AI law, set safety standards and ethics guidelines across the AI life cycle, and push developers to disclose safety risks and report incidents on their own initiative — rules that, under Bloomberg's reading, reach DeepSeek, Moonshot AI, and Alibaba. The package adds AI job titles like model trainer to China's occupations list and includes a US-China AI incident channel agreed in September. At Hong Kong's Global Financial Leaders' Investment Summit, financial-regulator vice head Xiao Yuanqi warned that global AI investment has become "overly concentrated," crowding out traditional industries by raising borrowing costs and credit risks. Disclosure, self-reporting, and prudential rules for the frontier, all in one motion.

- [Reuters](https://www.reuters.com/business/finance/ai-investment-is-becoming-overly-concentrated-chinese-official-says-2026-11-03/)
- [After Update (LinkedIn)](https://www.linkedin.com/pulse/after-update-issue-30-november-3-2026-john-kump-d49gc)

## Also noted

- **Data centers are filling the power gap with old jet engines.** Grid hook-ups for 100 megawatts take about seven years in Northern Virginia, so AI builders are burning converted jet engines from retired aircraft: xAI has eight at Colossus 2, Crusoe ordered 13 rebuilt ProEnergy units for Abilene, and a jet-powered site can run in 24 months. ([TechCrunch](https://techcrunch.com/2026/11/03/data-centers-are-turning-to-old-jet-engines-as-the-wait-for-power-grows/))
- **A deepfake "nudify" network hid in the app stores all year.** WIRED traced 400-plus apps — pet-portrait generators, language tutors, workout coaches — that could silently load interfaces for explicit deepfakes of uploaded photos, run by a Hong Kong-registered entity and spread through Meta ads; 27 Play Store apps found in September had 350,000-plus downloads, many rated for all ages. ([WIRED](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/))
- **Zalando unveiled its first AI shopping agent as margins slipped.** The in-app agent lets customers buy from other retailers, with AI-assisted checkout planned for 2027 and only a Westwing pilot live today; Q3 gross margin fell to 38.7 percent against 39.9 expected, and JPMorgan flagged "structural risk from agentic commerce development." ([Reuters](https://www.rte.ie/news/business/2026/1103/1597792-zalando-launches-ai-shopping-agent-as-margins-squeezed/))
- **The AI trade wobbled from Seoul to New York.** Korea's KOSPI closed down 3.59 percent (Samsung and SK Hynix off 4–5 percent) as brokerages flagged big-tech bond issuance and "Anthropic's financial burden," while the S&P 500 rose 0.4 percent to 7,568.92 on an Nvidia-led AI rebound even as Apple sank on memory-cost margin warnings. ([fnnews](https://fnnews.com/news/202611031557188079), [AP](https://apnews.com/article/wall-street-stocks-dow-nasdaq-95ac47c160dba546cbbdf72c10010e2c))