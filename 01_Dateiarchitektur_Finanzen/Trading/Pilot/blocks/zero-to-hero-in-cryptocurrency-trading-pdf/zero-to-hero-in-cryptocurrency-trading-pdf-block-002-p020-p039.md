# Zero to Hero in Cryptocurrency Trading.pdf — pages 20–39

--- page 20 ---

During that time, I was following an influencer’s account (@EmperorBTC) and he posted a trading technique that I
found interesting. I coded his strategy in Pine Script so that I could check its historical success and get alerts as to
when I should enter and exit trades, and I shared the code with him. Next, I found myself added to a private group
with other successful traders who were trading at another level. Together with these traders and with EmperorBTC’s
guidance, we were learning at an accelerated pace and developing great strategies that were beating the market.
I was linking those strategies to bots and automating them, dreaming about owning a Tesla and yachting when the 2021
crash happened.
Suddenly, my money-making strategies were unprofitable. Everything that worked during the bull market was still
beating Bitcoin, but Bitcoin was also beating itself.
So, I left my dreams for another day and went back to the drawing board. My learning switched from Exocharts and
volume profile techniques to developing strategies that could work for both markets. I learned about algorithmic
trading, the pandas framework, statistics, and how to better evaluate trading strategies considering drawdowns,
market crashes, and other (not-so-rare) events.
Since then, I have immersed myself in the world of statistics and developed smaller timescale strategies that run on 5-
minute candles (a term I will explain in Chapter 2) and provide a smaller but consistent profit through a higher number
of trades. That is the place where I found I can best use my analytical mind to identify opportunities to beat the
market.
And here I am now, giving you a shorter path to arrive at this place of evidence-based trading—a place from which
you can identify, test, and automate profitable strategies.
Overview of the book’s structure
I am an avid reader. My Goodreads account features over 100 books read per year. That is one every three days,
including audiobooks. I mostly read fiction now, but I have read my fair share of personal development books and a
whole bunch of trading books. What I found out during my page-turning adventures is that most trading books fail in
two respects:
They aren’t clear enough. Basically, they jump from concept to concept, making it hard for you to follow, or they immerse you in stories and
don’t provide enough useful content.
They don’t provide a step-by-step guide to arrive, together with the author, at the finish line. What they do instead is superficially present
concepts, tease you, and promote other programs at the end of the book.
Regarding the second point, I actually know a trading book that is delivered for free (minus a shipping and handling fee
that actually includes the book’s price) and teases the reader with methods of success that they can access by paying
for a high-ticket program.
However, throughout this book, I aim to provide you with content that is easy to follow and helps you increase your
knowledge in cryptocurrency trading (or fill in the gaps if you’ve traded before) and, step by step, chapter by chapter,
get you to a point where you can develop a successful strategy and automate it.
I’ve organized the chapters sequentially, but feel free to skim anything that you already know. Note that I recommend
skimming, not skipping. Make sure that you fully understand the sections that you’re skimming so that you don’t miss
--- page 21 ---

important information that you’ll need later on.
All the chapters contain detailed explanations of the methods presented, diagrams and screenshots that illustrate the
points made there, and exercises that I recommend you do so that you can evaluate yourself and build your confidence
in the method.
Do those exercises! They are important, not only from a psychological point but also to identify areas you’re not sure
about or concepts you haven’t fully grasped.
I will also provide some templates you can use when trading. I will refer to them in the book when we arrive at the
appropriate sections so that you can jump there and use them.
Aaaaand, of course, GitHub. Together with Packt Publishing, we provide a GitHub link to a repository where you can
download all the materials presented in the book, ordered by chapters. Here, you will also find high resolution versions
of the images shown in the book, in case you want to zoom in on them. Feel free to access this resource at
https://github.com/PacktPublishing/Zero-to-Hero-in-Cryptocurrency-Trading.
Note that I will also be providing links to a lot of useful content inside the book. Some of them are harder to type,
especially if you’re not reading the e-book version, but you’ll find all of them aggregated in a file in the GitHub
repository for you to point and click.
Market myths
There’s a lot of information on the internet regarding how to trade successfully. Yet with all of this information, most
people using it fail miserably. A few, though, have incredible success and come to like, comment, and share the videos
that helped them succeed. Some might even think that the information works, but they just don’t know how to apply it.
They too like, comment, and share, mostly because they like the speaker, not because the content actually works.
In this section, we’re going to take a closer look at some common market myths and recommendations newbies get
from other people, mostly on social media. Next, I’m going to debunk those myths and help you get a critical way of
looking at the market—a way that helps you discern random advice from true and tested information.
I will find a successful strategy on YouTube
Here’s a screenshot of what a simple search for a trading strategy shows on YouTube. This is what most people who
are interested in trading get when they first look for advice:
--- page 22 ---

Figure 1.1 – Searching “trading strategy high w in rate”
Most of my coaching clients ask me to check one strategy or another that they have found while browsing YouTube. It
is either a well-known influencer or a strategy that looks good on screen and that, every time, fails in practice. To
prevent that, I tell everyone that I am not looking at a strategy unless it comes with clear instructions and at least 100
trades in a spreadsheet.
I will make money paying for trading signals
Here’s another screenshot of what a newbie might look for. The classical get-rich-quick scheme. Over million results
later, we see this:
--- page 23 ---

Figure 1.2 – Searching “trading signals crypto”
Trading signals are “triggers for action.” After an algorithm (or a human) decides it is the time to enter (or exit) an
asset, it sends (or they send) a message to a private group that you subscribe to, where you receive that message and
can enter (or exit) a trade.
This can be worse than paying for a winning strategy. When you pay for a strategy, you can test it, understand it,
figure out whether it works, and adapt it to the market. With signals, the only thing you can do is record them in a
spreadsheet and check their profitability over an extended period (a period during which you are paying for the signal).
--- page 24 ---

Would you trust an estate agent you do not know telling you to buy an apartment? Would you buy it? Even if they are
well intentioned and not doing it (only) for the money, even if they are right most of the time, you are still buying only
one apartment and might just be unlucky. Also, you are not learning what to look for when buying an apartment; that
knowledge is kept secret from you, and you are just told that this is a good apartment.
I will run a successful trading bot
I still remember a phone call from my best friend from high school, enthusiastically telling me that some crypto bots
can help me make money. What I need to do is invest in them, and they will trade in my place and give me the profits.
He sounded like he’d found the golden goose.
One thing he did not take into consideration was that this was all happening during the bull run. The bot could have just
held Bitcoin and it would have made a profit.
And yes—some of those trading bots worked during the bull run, just as in specific market conditions, there are
strategies and trading signals that work. But they worked because everyone was investing during that time, and even
holding Bitcoin without trading was increasing your assets compared to the dollar. But when you traded, you were
actually losing money if you were comparing your portfolio to Bitcoin because Bitcoin was growing faster.
It is not a bad idea to run a trading bot if you know what you are doing. But the bots that most providers offer run
based on strategies that if you really test them... do not work!
Yep—you will learn later that exponential moving average (EMA) intersection (or any other strategy for that
matter) works in theory, and it also works when you plot entries and exits on the chart, but when you crunch the
numbers, it does not. That is because the indicator is “repainting” the chart (it’s redrawing the lines after the fact) and
discounting the lower timeframes. It also does not take fees and slippage into consideration, which can add up quite
quickly when trading.
But let’s not get into the details just yet. Just promise me you will not pay for crypto bots until you have at least read
the whole book. By the end of it, you will not need to pay for any bots, you’ll be able to build your own.
I will successfully invest in copy-trading platforms
I am not against copying good investors or traders. On these platforms, you can use filters to find out how profitable
(and risky) the traders were during the past years and figure out the ones that made money during both the bull and the
bear markets. Then, calculate all the fees that you would incur while doing this (platform fees, traders fees), and see
whether you would still be in profit. If so, sure—why not?
The problem is that most of these platforms do not show how the trader performed compared to Bitcoin . It’s not
particularly relevant if they made profits in dollars ($) during a bull run because you could simply hold Bitcoin and
achieve the same result. Next, they do not provide proper statistics, and, for that matter, they do not show how much
you would have made minus taxes and fees if you had invested in a particular trader. Also, do the traders have enough
of a history? Did they run into the last two bear markets, or have they just recently made an account and have bigger
short-term profits just because they risk more? Would you really trust the platform with your money?
--- page 25 ---

Just to name a situation where the charts looked good but the logic was flawed: copy traders were investing only in the
Terra stablecoin, which had a 10% staking yield. They were beating the dollar by 10% and the charts looked amazing.
However, the portfolio was not diversified, and when the ecosystem collapsed, all the traders, copy traders, investors,
and other involved parties lost their money. If you were to check current traders on the platform, you would see that
they are not successful traders (their total results are poor). However, if you had looked at them before the Terra
crash, they would have been at the top, and you would have probably invested in them. Here’s a link to what happened
to Terra: https://www.forbes.com/sites/qai/2022/09/20/what-really-happened-to-luna-crypto.
And why do these strategies, signals, and bots fail?
In this section, I will bust the myths we went through in the previous sections. However, since I will be providing
examples that might not be that clear to understand if you are new to trading, feel free to skim through this part and
come back to it after reading Chapter 3 and Chapter 4.
Reason #1 – A high win rate does not mean a high profit
From the following options, which would you choose?
A. A 75%-win-rate strategy where you win $1 75% of the time and lose $10 25% of the time
B. A 20%-win-rate strategy where you win $10 20% of the time and you lose $1 80% of the time
“Market-mathics” would say that with option A, over a long time, you would win $1 for trades out of and lose $10 on a
fourth one. That means -$1,750, a big loss for a 75%-win-rate strategy over 1,000 trades. For option B, you would win
$10 for trade out of five and lose $1 for the rest. That means a $1,200 profit for a 20% win rate strategy over 1,000
trades.
If you don’t believe my calculations, you can always ask ChatGPT:
--- page 26 ---
--- page 27 ---

Figure 1.3 – ChatGPT’s math w orks
But note that I have said, “over a long time.” If you toss a coin, there’s a 50-50 chance to get heads or tails. When
tossing, you can get heads four, five, and even six times in a row. So, even though you would choose option B for
higher profitability, you might not be as profitable as option A in the first few trades.
Reason #2 – Community and echo chambers
When a famous influencer posts a strategy on YouTube, you will see a lot of positive reactions. You will read about
how some people had quite a successful run with that strategy and how grateful they are, and, right next to them, how
other people want to better understand it and need additional explanations.
Now, imagine a bell curve. Or better yet, look at it:
Figure 1.4 – A bell curve
Imagine a strategy that is profitable. Even though most people applying the strategy will turn a profit, statistics show us
that a small percentage of people will not profit (and another smaller percentage will profit a lot).
That is all reasonable, right?
--- page 28 ---

Well, imagine an influencer posts a trading strategy without testing it. Even though most people will not profit, the bell
curve shows us that, even then, a small percentage will still profit (yes—even with an unprofitable strategy).
OK—but then, wouldn’t the number of comments saying that the strategy does not work overflow the comments
saying that it does?
Well, not quite. Because you are on an influencer’s platform and their following already believes in them. Welcome
to... the echo chambers!
An echo chamber refers to situations in which beliefs are amplified or reinforced by communication and
repetition inside a closed system and insulated from rebuttal. By participating in an echo chamber, people are
able to seek out information that reinforces their existing views without encountering opposing views,
potentially resulting in an unintended exercise in confirmation bias. Echo chambers may increase social and
political polarization and extremism. On social media, it is thought that echo chambers limit exposure to diverse
perspectives, and favor and reinforce presupposed narratives and ideologies. (Echo chamber (media). (2023,
August 29). On Wikipedia: https://en.wikipedia.org/wiki/Echo_chamber_(media)).
An influencer runs their own echo chamber where the community will support them (and believe in them) even though
they might be wrong.
When people are writing about the technique’s success, the vast majority for which the technique did not work will
think that it is their fault and that they do not know how to use it and will either skip to the next video or ask for more
details on how to use that technique.
Basically, the echo chamber will echo the influencer’s beliefs and propagate a feeling of success on the platform (and
yes—some people will have success using that trading technique).
Reason #3 – The strategy was not tested properly
To check whether a strategy provides an advantage over the market, that strategy needs to be tested correctly. But
what does “correctly” actually mean? Here are a few questions you can ask yourself before you apply the strategy:
Did the trader test it over 30 trades? 100? 10,000?
Was it tested during the bull market? During a bear market?
Was it backward tested over a sufficient period? Did it take into consideration tokens that were unlisted from the exchange or tokens that were
dumped? Market switching direction? New tokens listings? Does it need new tokens to age in the market before trading?
Was it forward tested? Was it paper traded? Was it tested live? For how long?
Does it work on all token pairs or only on large-cap/mid-cap/small-cap/blockchains/volatile assets and so on?
Does it take into consideration lower timeframes, intra-candle movement, repainting, slippage, fees, and drawdown?
Can somebody else reproduce the results by following the exact same steps?
Was it tested automatically or manually?
Is it well defined or is it discretionary? Can it be coded into clear rules? Is the risk mentioned? Or the drawdown?
If it will be traded manually (for example, discretionary strategies), does it mention the time availability needed for those results?
Were delays such as market delays, API delays, overfitting, and underfitting taken into consideration?
Was it detrended or is it biased toward a market direction?
Does it work in the current market? Does it work in crypto?
--- page 29 ---

And the list goes on...
In Chapter 5, we will talk more about what you must watch out for when testing a strategy and how to do that, but for
now, understand that there is more to testing a strategy than looking for 5 minutes over a chart and pinpointing places
to successfully trade it.
Reason #4 – Past performance is no guarantee for future results
Even if the strategy was tested successfully and it works, markets change, and past performance cannot
guarantee future results. Do not expect your strategy to work until the dawn of crypto. Understand the necessity of
fine-tuning it from time to time and even changing it in favor of other strategies better suited to the markets you will
find yourself in.
Reason #5 – The outcome of any single trade has a random outcome
No matter how successful a trade is, you cannot take into account all the factors that go into that particular trade. By
random, I do not mean 50-50 randomness; even a trade that has a 99% success rate will, over time, fail in 1 out of 100
situations. So, any one single trade that you take can be that trade that has a 1% chance of failing.
Extrapolate this into a situation where an influencer is showing how a strategy is successfully applied in five
consecutive situations. That is irrelevant statistically, but it sure looks good in a video.
Reason #6 – Cognitive biases
According to Wikipedia, “A cognitive bias is a systematic pattern of deviation from norm or rationality in
judgment. Individuals create their own “subjective reality” from their perception of the input. An individual’s
construction of reality, not the objective input, may dictate their behavior in the world. Thus, cognitive biases
may sometimes lead to perceptual distortion, inaccurate judgment, illogical interpretation, or what is broadly
called irrationality.”
And here’s a list of biases, on the same page: https://en.wikipedia.org/wiki/Cognitive_bias#List_of_biases.
Here are some biases that can affect an influencer, you, or any trader, for that matter:
Confirmation bias (https://en.wikipedia.org/wiki/Confirmation_bias) is the tendency to search for, interpret, favor, and recall information in a
way that confirms or supports one’s prior beliefs or values. “Look at how I correctly predicted the market. This indicator also proves my view.”
Attribution bias (https://en.wikipedia.org/wiki/Attribution_bias) is a cognitive bias that refers to systematic errors made when people evaluate
or try to find reasons for their own and others’ behaviors. “I succeeded in that particular trade because of my technique, not because of random
market movements.”
Illusion of control (https://en.wikipedia.org/wiki/Illusion_of_control) is the tendency for people to overestimate their ability to control events.
“My small modification to this indicator is what makes the strategy work (not the small sample size where I overfitted).”
The overconfidence effect (https://en.wikipedia.org/wiki/Overconfidence_effect) is a well-established bias in which a person’s subjective
confidence in their judgments is reliably greater than the objective accuracy of those judgments, especially when confidence is relatively high.
“After 10 trades, I can tell you that the strategy works correctly!”
Optimism bias (or the optimistic bias) (https://en.wikipedia.org/wiki/Optimism_bias) is a cognitive bias that causes someone to believe that
they are less likely to experience a negative event. “I won’t test this strategy over a larger time range because I know it will work; my first trades
were pretty successful.”
Selection bias (https://en.wikipedia.org/wiki/Selection_bias) is the bias introduced by the selection of individuals, groups, or data for analysis in
such a way that proper randomization is not achieved, thereby failing to ensure that the sample obtained is representative of the population
intended to be analyzed. “My strategy works because I have tested it well, not because I tested it in a favorable market.”
--- page 30 ---

Hindsight bias (https://en.wikipedia.org/wiki/Hindsight_bias), also known as the knew-it-all-along phenomenon or creeping
determinism, is the common tendency for people to perceive past events as having been more predictable than they actually were. People
often believe that after an event has occurred, they would have predicted or perhaps even known with a high degree of certainty what the
outcome of the event would have been before the event occurred. “You can see how many times we can apply the strategy on the chart. Look
here, here, and here.”
Illusory correlation (https://en.wikipedia.org/wiki/Illusory_correlation) is the phenomenon of perceiving a relationship between variables
(typically people, events, or behaviors) even when no such relationship exists. “Bitcoin always goes down before the halving, so the next time it
goes down, it will be because of this.”
The representativeness heuristic (https://en.wikipedia.org/wiki/Representativeness_heuristic) is used when making judgments about the
probability of an event under uncertainty. We use heuristics to create shortcuts in our decision-making, but when something is more
representative to a group, it doesn’t mean it is also more likely to happen. “When these two indicators show buy, the price goes up. You can see
this happening here, here, and here. So, these are correlated.”
Insensitivity to sample size (https://en.wikipedia.org/wiki/Insensitivity_to_sample_size) is a cognitive bias that occurs when people judge the
probability of obtaining a sample statistic without respect to the sample size. “Based on the last 50 trades, I can assure you this strategy works.”
Random reinforcement (https://www.investopedia.com/articles/trading/09/random-reinforcement-why-most-traders-fail.asp) occurs when a
trader misattributes a random outcome to their own skill or lack of skill. The market sometimes rewards bad players too and, statistically, some
bad traders get rewarded more than others, giving them the illusion that they are skilled. “I’m a successful trader because I have good trading
skills, not because I was lucky.”
All these biases are hard to detect because they come naturally to us in our day-to-day lives. So, imagine how easy it
is to fall for one of these biases (and there are more). Developing a strategy is not that simple, and even good
strategies have a lot of conditions when they do not work.
What I want to say here is that we, as human beings, will fall into these traps. And it is all right—we do not have to
solve all our problems to trade successfully. Still, if we want to shake the hand of success, we will need to work on the
psychological factors that prevent us from being successful, as well as on the technical factors. And we should stop,
while reading this book at least, following influencers and instantly believing what they say about trading techniques,
even (and especially) if they have a large following. Before believing in something, understand what is behind it, check
the assumptions, verify the results yourself, and then, if everything checks, believe in it. This is how you become
profitable.
Don’t take extreme examples of success, such as Bill Gates and Steve Jobs. They were very successful, but their
success also contained an element of luck, maybe even an extreme version of it. Instead, think of the moderately
successful people. That’s your realistic target. Venture capital (VC) companies lose a lot in the majority of their
investments, but they recuperate everything and come out on profit from their top 3-4% investments. Also, take into
account the element of time. Disney created a lot of cartoons before it had their success with Snow White and the
Seven Dwarfs. And consider the element of personalization. You can get some information when searching the
internet for the symptoms of your particular medical condition, but when you go to an expert, the treatment is tailored
to you.
Summary
In this chapter, I have told you my story and presented you with the book’s structure.
Then, we went right into market myths and the reasons people believe in them. We finished with cognitive biases and
how they can impact your trading, and now, we are ready to jump right into the basics.
--- page 31 ---

My goal for this chapter was for you to understand the myths that losing traders believe in and to understand why getrich-quick schemes don’t work.
The next chapter is great for new traders who will get a grasp on what happens psychologically when they trade, what
mistakes they usually make, and why people lose money. Then, we are going to talk about how to read a chart and
who are the market participants trading that chart.
Exercises
1. “A father and son were involved in a car accident in which the father was killed and the son was seriously injured. The father was pronounced
dead at the scene of the accident and his body was taken to a local morgue. The son was taken by ambulance to a nearby hospital and was
immediately wheeled into an emergency operating room. A surgeon was called. Upon arrival and seeing the patient, the attending surgeon
exclaimed, “Oh my God, it’s my son! Can you explain this?” (Story adapted from the Father/Son activity found in Pendry, Driscoll, and Field
(2007).)
2. Try to remember how many times you were afraid of being wrong. Now, imagine that you’re presenting a trading technique. Would you make sure
that you are presenting it in the best light possible? Would you choose a chart where you have 10 successes and 2 failures or a chart where you
have 7 failures and 3 successes? Some people would say they would present both, but when you have hundreds of thousands of people following
you, the title of your video refers to a successful strategy, and you can only present one of the charts; which would you choose?
3. Do you remember any “I told you so” instances happening after breakups? Maybe those people have not “told you so” before, just after. What
about situations where your favorite football team plays against another good team? Before the game, you are asking yourself, “Will they win?”
After the game, you are telling yourself, “I knew they’d win!”
Explanations follow next.
Answers to the exercises
1. The surgeon is the boy’s mother. Most readers miss this answer and try to elaborate complex stories regarding paternity and priesthood. This is
related to stereotyping.
2. This is related to confirmation bias. You are presenting the information in a way that confirms your beliefs.
3. This point is related to hindsight bias. It is easy for us to think we know the answer to a situation that has already passed, but we can’t actually
predict the outcome when the situation is in the future.
--- page 32 ---

2
Understanding the Basics
In this chapter, you’re going to take a risk assessment questionnaire so that you can better understand yourself and be
able to handle the emotions you’ll encounter when trading. Next, I’m going to share with you a candlestick story so
that you’ll take your first steps in studying a chart on various timeframes. After that, I’m going to share with you how
different market participants trade so that you can better understand the market environment and why suddenly one of
them buys a token, even if all the indicators show it should be sold. Finally, you’ll learn about the three types of
markets and what makes them different.
My goal for this chapter is for you to get to know your risk level and to find out more about the entities that trade
alongside you.
Here are the topics we’re going to talk about:
A trader’s psychology
Understanding risks
Cryptocurrencies as an asset class
A candlestick story
Timeframes
Market participants
Types of markets
A trader’s psychology
In this section, you’ll complete a risk assessment questionnaire and learn about the three types of traders to determine
which category you fall into. Based on your responses, you’ll gain insight into potential risks you may encounter while
trading and how to address them.
Risk assessment questionnaire
Answer questions 1 to 10 by choosing the answer that’s most related to your current situation (or what you’re most
likely to do in the situation provided). Ignore what you think you’ve learned after reading the question (what you
should do) and focus on what you would do:
1. How would you be characterized by your best friend?
A. Gambler
B. Willing to take some risks
C. Cautious
2. Choose your prize:
--- page 33 ---

A. $1,000 cash
B. 50% chance of winning $5,000
C. 10% chance of winning $15,000
3. The price declines by 50%. What’s the percentage it needs to increase to arrive at the same level as before?
A. 50%
B. 75%
C. 100%
4. What win rate do you need to break even (getting $0 in profit) for trades with a risk-reward ratio of 4:1 (for every trade you risk $1 to win $4)?
A. 20%
B. 25%
C. 33%
5. What does risk mean for you?
A. Prejudice
B. Thrill
C. Possibility
6. What would you do with $1,000?
A. Invest all of it in a fast-growing crypto asset
B. Invest 25% of it in a fast-growing asset, 25% in a stable asset, 25% in a risky asset, and keep 25% for other opportunities
C. Keep it in cash for better opportunities
7. If you had $10,000 to invest for 10 years, which option would you choose?
A. Low risk, low return
B. Medium risk, medium return
C. High risk, high return
8. When the market goes down, what would you do?
A. Do nothing
B. Double down
C. Sell riskier assets and buy safer ones
9. If you left $1,000 in a deposit with a 2% interest rate per year and inflation was 2% per year, after 1 year, how much would you be able to buy
with the money in the account (without taxes)?
A. More than today
B. Less than today
C. Exactly as much as today
10. When making a trade with a strategy that has an 80% win rate, if you’re at a minus of 10%, what would you do?
--- page 34 ---

A. Consider exiting the trade
B. Double down—the strategy has a high win rate
C. Set a stop-loss lower, just in case it falls even further
Here are the scores for the answers to these questions:
Figure 2.1 – Scoring table for the answ ers to the questionnaire
For question 8*, it’s logic versus psychology. Doing nothing is what a low-risk investor would do, even though
financially speaking, selling riskier assets and buying safer ones is what a low-risk investor should do. In my test, I’m
biased toward psychological accuracy.
The gambler (score < 17)
What is life without a touch of risk?
--- page 35 ---

You are a gambler at your core, and you actually know it. When you trade, your emotions run high, and you’re there,
into the trade, living every high of it and dreading every low. When you win, you win. You smile and you think of all the
future earnings that you’ll receive. And when you lose, you sure lose. You’ve already doubled down, and every loss
hurts.
In my coaching business, I have a lot of gamblers who come and want me to teach them how to win when trading.
When they see the work it takes, they ask for the best strategy or daily signals. And when I show them what’s the
work behind creating and managing such a strategy, they have a choice to make. Either slow down hard or risk losing
money before actual learning occurs.
The best advice I have for the gambler is to better understand their counterpart, the cautious trader. I invite you to do
swing trading that is not micromanaged, to set trades that enter at a certain price and that exit at specific prices, be it
at a loss or a win. Before each trade, you need to have a hypothesis (reasons for entering the trade and for exiting the
trade at your chosen levels). Then, after the trade has run its course, you need to revisit your hypothesis and update it
with the result.
In time, this will help the gambler in you create a distance between your emotions and the trades you are taking so that
you can follow a strategy to its success.
And to also have a release for those emotions, you can either use another account or just mark your trades as
#spontaneous and do those trades with a lower amount of money.
The cautious trader (score > 23)
I want to protect my money before I win anything.
You value your hard-earned money, and you know you’re not here for the easy win. Maybe you’ve already started
studying the classics of investment literature; if not, you’re surely planning to and you are ready to put that money into
some fruitful investments. You are a bit scared of losing them, especially in the cryptocurrency world where you’ve
heard that there are big fluctuations, but you’re here to stay and to ride those waves for the win.
I don’t have a lot of cautious traders as clients, but when I do, I identify them instantly. From the first few minutes,
they are telling me what’s important to them (variations of not losing money), and they are also making sure my
credentials are intact (How much did you win? What types of strategies do you use? What’s the success rate of
your clients?). They are trying to make sure that they’ve made the correct choice.
My top advice for (fellow) cautious traders is to dedicate money to losses. Not to risk, but to lose. Trading is an
emotional game, and when you switch from paper trading to money-based trading, a lot of emotions will circle around
you, waiting for that chink in your armor. In paper trading, it’s easy to start a trade and then wait for it to finish. In real
trading, you’re enticed to always watch the charts and to make sure that your trade is working... So, what happens if
the price starts falling? Should you exit early or wait for it to touch the price you’ve set as a stop-loss?
Here, the cautious trader’s brain freezes. There are too many variables, and they can look at reasons for the trade to
end in profit, but they can also find reasons that the trade will fail.
In order to overcome all of those emotions, they need to accept risk as part of their trading career and learn to manage
it rationally and predictably.
The balanced trader (score between 18 and 23)
--- page 36 ---

Winning is a slow and steady process.
You have lived a life full of experiences. You know that winning involves risk, and you’re ready to put some money
where your desires are. Yet you have a financial reserve that you will not touch, and that is there just in case you
realize trading is not for you. You’re willing to give it all but also to analyze your results after a time and to decide if
this is for you or not.
I have quite a few balanced traders as clients, and they are the easiest to work with. That’s because I can put the
psychologist in me to sleep and focus on the mechanics of trading with them. Some catch the mechanics pretty quickly,
some a bit later, and most of them leave when they have a few techniques that they can trade and when they
understand that trading is like chess—easy to learn, hard to master. Sometimes, they come back when they need a
technique automated or when they have some really advanced questions.
My advice for the balanced trader is to continue what you are doing. If you’ve got this score, your emotions won’t
impede your trading that much, and you will be able to grasp the concepts and learn at the pace needed to keep your
motivation and start getting results. And after you’ve got the results, everything else is just scaling.
Some final thoughts on risk assessment
Every type of person can fit in the trading space, but some have more challenges than others. Maybe a cautious trader
progresses slower, but they also lose less money. During this time, the gambler might get some early wins, enough to
push their motivation to learn the difference between trading and gambling. But they might also get enough early losses
to make them leave the markets for good. And in all this time, the balanced trader progresses slowly and steadily, still
wondering how all those people win so much. Each personality has its own set of questions and emotions that help or
impede them when trading and its own battles on the money battlefield. All you can do is prepare yourself to the best
of your abilities and then live your life as you want to live it.
We’ve identified what type of trader you are, and next, I’m going to show you who the other market participants are
and how they behave in specific market types.
But first, let’s start with an answer to the following question: What exactly are currencies?
Cryptocurrencies as an asset class
A cryptocurrency is a digital currency, secured by a cryptographic algorithm that prevents double-spending and
counterfeiting. Most of today’s currencies work on computer networks independent of central authorities such as
governments or banks, eliminating the need for traditional middlemen and facilitating true ownership of funds and quick
(almost instantaneous) transactions.
Even though they are named cryptocurrencies, they are not considered to be currencies in the traditional sense (though
they are classified as commodities, securities, or even currencies). They are usually viewed as a distinct asset class
and are theoretically immune to government financial manipulation.
By asset class, we are referring to the ability of the asset to hold value and have true use cases. The first
cryptocurrency, Bitcoin, defined in a white paper that was published on October 31, 2008, has already proven its valueholding potential; its returns for the last 10 years have been positive, even with its high volatility. Its main use case can
--- page 37 ---

be considered fast and cheap transfers (through the Lightning Network) that work between any parties having a
Bitcoin wallet, 24/7.
In this section, you will hear a candlestick story, followed by an overview of the different timeframes that traders use.
We will also discuss the various market participants and how their trading affects the market, creating different types
of markets, each with its own unique characteristics and trading style.
A candlestick story
Hey Siri, play “The Candlelight Story” by Tony Chen.
The God of Markets, Munehisa Honma, is said to be the creator of candlestick charts. He was a rice merchant from
Sakata, Japan, who traded the Dojima Rice Market in Osaka, during the Edo shogunate. Stories are told about when
he created a personal postal service (men spread every 6 kilometers over 600 kilometers) to get the market prices in
time. In 1755, he wrote the first book on market psychology, San-en Kinsen Hiroku, or The Fountain of Gold – The
Three Monkey Record of Money, in which he talks about traders’ emotions and how they influence prices.
In 1991, the candlestick appeared in the Western world in a book called Japanese Candlestick Charting Techniques,
written by Steve Nison, who says that, according to his research, it is unlikely that Honma used candlestick charts.
So, the initial story might actually be the first trading urban legend in Japan.
But what is a candlestick chart?
Well... let’s first start with a candle...stick!
--- page 38 ---

Figure 2.2 – A candlestick
A candlestick chart is a financial chart that shows the price movements of securities, derivates, or (crypto)currencies.
It is also called a Japanese candlestick chart or a K-line chart. Each candlestick there represents four essential pieces
of information: the price at opening time, the price at closing time, and the lowest and highest price of that timeframe.
They are usually colored white or green for rising prices (Close > Open) and black or red for falling prices (Open >
Close).
NOTE
All images in this book are in grayscale, so there may be a slight adjustment period when you view the colored candles on TradingView.
So, with just one look, you can see if the price is rising or falling, by how much, and even what were the highest and
lowest points it traded during that timeframe.
Here’s how it looks on a chart:
--- page 39 ---

Figure 2.3 – A candlestick chart
This chart is also called an open-high-low-close (OHLC) chart (because you can see these values for each candle
on the chart). To make it easier, we’re going to use the short forms for Open, High, Low, and Close (O, H, L, and
C).
Here, you can see how the white candles (or green candles) show rising prices (C > O, meaning that the close price is
greater than the open price; basically, it closes “higher”) and the black candles (or red candles) show falling prices (O
> C).
Each candle on this chart represents 1 hour of price movement, and we’ll find out in the next section what exactly
these timeframes are.
Timeframes
We know what a candlestick is and what a candlestick chart looks like, and now it’s time to understand how to
represent price movements over large (or small) periods. Have a look at the graph shown in Figure 2.4:
