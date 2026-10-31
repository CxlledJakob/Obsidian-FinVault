# Wyckoff 2.0_ Structures, Volume Profile and Order Flow (Trading and Investing Course_ Advanced Te...{Rubén Villahermosa}{94095402} libgen.li.pdf — pages 153–172

--- page 153 ---

That is, the price may never visit that level and therefore we
would not enter the market. As long as they are not executed,
they can be removed at any time.
❖ Stop. A passive order that is executed at a specific price. When
the price reaches it, it becomes a market order and is therefore
executed at the best available price (Best BID/ASK).
❖ Stop-Limit. Combines the features of Limit and Stop orders.
Once a certain price level is reached (Stop orders function), an
order is generated at a specific level (Limit orders function).
Operationally, it works exactly the same as Limit orders.
Based on the four types of orders we have just seen, the following
is the full spectrum of basic orders available depending on the intention
and what it is used for:
❖ Buy Market. Aggressive order at the current price. It is used to:
Enter the market on buy.
Close a sell position (either at a profit or loss).
❖ Buy Stop. Pending order above the current price. It is used to:
Enter the market on buy.
Close a sell position (by Stop Loss).
❖ Buy Limit. Pending order below the current price. It is used for:
Enter the market on buy.
Close a sell position (by Take Profit).
❖ Buy Stop Limit. Pending order below the price after reaching a
--- page 154 ---

level. It is used to:
Enter the market to buy.
Close a sell position (by Take Profit).
❖ Sell Market. Aggressive order at the current price. It is used to:
Enter the market on sell.
Close a buy position (either in profit or loss).
❖ Sell Stop. Pending order below the current price. It is used to:
Enter the market on sell.
Close a buy position (by Stop Loss).
❖ Sell Limit. Pending order above the current price. It is used to:
Enter the market on sell.
Close a buy position (by Take Profit).
❖ Sell Stop Limit. Pending order above the price after reaching a
level. It is used to:
Enter the market to sell.
Close a buy position (by Take Profit).
4.3.1 ADVANCED FEATURES
--- page 155 ---

There are certain advanced instructions that can be applied,
depending on the broker, to orders to enter and exit the market:
One-Cancels-Other (OCO). Entering two orders to the market
with one of them being cancelled when the other is executed.
Order-Sends-Order (OSO). Instruction to execute secondary
orders when the initial one is executed.
Market-To-Limit (MTL). Execution of a market order that
includes an instruction to place a limit order at the same price with the
remainder of the position if it is not fully executed.
Market-If-Touched (MIT). Execution of a market order that
includes an instruction to place a limit order at the same price with the
remainder of the position if it is not fully executed.
Limit-If-Touched (LIT). Conditional order to trade with a pending
order (Limit) when a specific level is reached. It is used to buy above the
current price and to sell below the current price.
Good-Til-Cancelled (GTC). It includes a temporary execution
period which is usually the duration of the session. If at that point the
order has not been executed, it will be cancelled.
Good-Til-Date (GTD). The order remains active until a specific
date.
Immediate-Or-Cancel (IOC). Instruction to execute the order
immediately. If any portion of the order remains unfilled, that portion is
cancelled.
Fill-Or-Kill (FOK). It does not allow partial execution. When the
price is reached, it either enters the market with full volume or is
--- page 156 ---

cancelled.
All-Or-None (AON). Similar to the FOK orders with the difference
that in case the price reaches it and it is not executed because it cannot
cover all its volume, it remains active until it obtains all the counterpart or
it is cancelled by the trader.
At-The-Opening (ATO). Instruction to execute an order at the
opening of the session. If this is not possible, it is cancelled.
At-The-Close (ATC). Instruction to execute an order at the close of
the session.
--- page 157 ---

4.4 TOOLS FOR VOLUME ANALYSIS
Thanks to certain tools that analyze the flow of orders we can see all the
interaction between buyers and sellers who participate in the market in
different ways.
We will mainly distinguish them by the type of orders they deal
with as not all these tools are based on the same data:
❖ Analysis of pending orders: Order Book, also called Depth of
Market (DOM).
❖ Analysis of executed orders: Time & Sales and Footprint.
We will point out their most important characteristics in order to
provide the reader with a basic knowledge of the peculiarities of each one.
4.4.1 ORDER BOOK
Identifies all pending orders for execution (liquidity) that are
located in the BID and ASK columns; as we already know, the BID
--- page 158 ---

represents pending buy orders and the ASK represents pending sell
orders.
As these types of software only have Level II of depth, most
markets can only show ten levels of liquidity above and below the current
price. This is relevant because beyond those ten levels there will still be
liquidity located, but it is only visible to those who have Level III of depth
(mainly liquidity providers).
The analysis of the order book presents some problems. One of
them is that the visible liquidity is never the liquidity that is actually
located in those levels. The liquidity that can be seen in the order book
comes only from limit orders. By their very nature, market orders cannot
--- page 159 ---

be seen anywhere, since they are born from an initiative and are executed
instantaneously. On the other hand, Stop orders, as they become a market
order when their price is reached, are not displayed in the Order Book
either.
In addition to this, as we have seen in the advanced features of
some orders, there are certain instructions that are not displayed in the
Order Book either, so that in reality we would be analyzing a not very
high percentage of the total orders pending execution.
Another major problem with the analysis of the order book or any
other tool based on this liquidity data is that these orders that are pending
execution can be removed by whoever placed them there at any time
before they are executed. Due to this peculiarity different forms of
manipulation carried out by algorithms emerged:
SPOOFING
This is the placement of huge amounts of contracts in the BID and
ASKS columns (limit orders) without the intention of actually executing
them. The aim is to give the impression of an "insurmountable barrier"
and cause the price to move to the opposite side. They are false orders
because when the price is about to reach its level, they are cancelled and
are not executed.
It is an interesting concept that highlights the value of the ability of
limit orders with respect to price movement. As we have mentioned, limit
orders by themselves and by their very nature do not have the ability to
move the market, but using this form of manipulative activity we see how
--- page 160 ---

the price can move influenced by them at certain times. Not directly based
on their execution, but indirectly based on their influence.
Imagine that you normally see limit orders of around 50 contracts
per price level. What will the other participants think if you suddenly see
500 contracts? Well, most logically they will see that this is a too high
price to pay for the price to cross that level and most likely cause a lack of
interest to go against such orders. And of course, this will result in a move
in the opposite direction of the huge order. Manipulation by large traders
to drive the price in the direction they want.
ICEBERG ORDERS
This is the splitting of a large limit order into smaller portions. The
motivation for this type of action has to do with wanting to hide the actual
size of the original order.
Mainly used by institutional traders who want to execute a huge
number of contracts in a given price range and who use algorithms
programmed with this technology to be able to do so passively and
without turning the price against them. It is important to note that there is
only one source behind such an order, just one large trader, not a
collection of them.
It is very visual to take the example of a real Iceberg. On the
surface what you see is a seemingly normal amount of contracts, but what
you don't know is that this order is simply a part of a much, much larger
one. And when this small part is filled by the market the large order
quickly replenishes it.
--- page 161 ---

This is the clearest example of what a takeover would look like.
There may be many aggressive buyers pushing the ASK and all those Buy
Markets are crossing the Sell Limits of an Iceberg order which do not
allow the price to move up. We will say that a takeover of these purchases
is taking place.
4.4.2 TAPE
Thanks to Time & Sales we can see in real time all the crossing of
orders already executed. The analysis of the tape becomes very complex
due to the speed at which the current markets move (mainly futures
markets).
--- page 162 ---

Depending on the software we can access different types of
information. It usually includes at least the columns with the time of
execution, the price level and the number of contracts.
It can certainly be useful for the identification of large volumes
executed in a single order, known as "big trade". More modern versions
also allow the grouping of orders executed in blocks, pointing to the same
trader as the origin of different transactions spaced in time.
A positive point of the Tape with respect to the Order Book is that
the tape represents the past, the orders already executed and therefore is
--- page 163 ---

not susceptible to manipulation.
Operating solely by analyzing the tape is not within everyone's
reach since it requires enormous experience as well as a great capacity for
concentration due to the speed at which it moves.
4.4.3 FOOTPRINT
When most people refer to Order Flow they are actually referring to
this section of the order flow, the use of Footprint. Order Flow is a general
term that, as the name suggests, is concerned with order flow.
The Footprint charts the data provided by the tape (orders already
executed) and represents them in a much more visual way. It would be
like putting a magnifying glass inside the candlesticks and observing the
number of contracts executed at each price level..
The advantage of analyzing the Footprint is that it allows us to
--- page 164 ---

quantify in maximum detail the interaction between buyers and sellers.
Observing the balance and imbalance between participants as well as
being able to identify in which column more volume is being traded can
certainly be useful at certain times.
There are different types of footprint charting based on:
❖ The nature of the data: it can be set up with time, range, volume
and rotation candlesticks.
❖ The representation protocol: Profile, Delta, Imbalance,
Histogram, Ladder or BID/ASK.
It is a very configurable tool that generally includes multiple
functionalities although it basically analyzes the orders executed by price
levels with the objective of looking for imbalances, takeovers, initiatives,
unfinished auctions, clusters, big trades etc.
Once you know in depth how the order crossing is executed, you
will come to the conclusion that its analysis is very subjective and that
trading based on this tool without taking into account anything else is not
advisable.
4.4.2 DELTA
A more specific and popular tool in the world of Order Flow
analysis is the Delta. The delta is an indicator that simply measures the
difference between the volume traded on the BID and the volume traded
on the ASK in a given period of time. If the difference is positive the delta
--- page 165 ---

will be positive and vice versa if it is negative. In addition, the difference
between deltas can also be visualized since the indicators will normally
show them with different sizes.
There is a common misconception that all volume traded on the
ASK "are buys" and all volume crossed on the BID "are sells", although
in reality with that statement they mean that they are directional in origin;
that is, they have an intention to add pressure towards one of the sides. If
this were so, why do we sometimes see bearish moves with positive deltas
and bullish moves with negative deltas? Believe me it's not that simple. If
it were, we would have found the Holy Grail. Again it has to do with the
crossover mechanism.

For the time being, let's keep in mind that it is visually observed on
a horizontal axis with value 0 and that depending on the column where the
transactions are executed, it will be displayed positively or negatively on
the axis. This representation would be for the example of the normal Delta
since there is another variant, the accumulated, where it is charted
continuously without taking into account the horizontal axis.
The delta is updated at each executed order and therefore gives rise
to the possibility that, as with the price, wicks are represented at its
extremes. If we observe a delta with a wick in its lower part, what it
means is that at a certain moment of its development the difference in
favor of the BID was extraordinarily large, and that at a certain point it
has begun to negotiate much more actively in the ASK column,
generating that reversal that leaves its mark in the form of a wick.
--- page 166 ---

As it happens in general terms with the analysis of the footprint,
although its interpretation is not as basic as I have explained above, it can
provide us with certain usefulness at certain specific moments.
--- page 167 ---

4.5 THE ORDER FLOW PROBLEM
As a basis, we must be clear about a series of ideas that will help us to
understand the rest of the content:
1. A purchase is matched to a sale and vice versa.
2. An aggressive order is matched with a passive order.
3. In the columns of the BID and the ASK only the aggressiveness
is reflected.
Considering the different types of orders, it is now necessary to
understand what mechanism is used to match orders between participants
and in which column this execution is reflected.
--- page 168 ---

❖ Stop orders become Market orders when they are filled.
❖ Stop Limit orders become Limit orders when the price set by
the Stop order is reached.
When the trader executes a Buy Market order, the order processing
mechanism kicks in and goes to the Order Book to find the first Sell Limit
order located in the ASK column to match this buy.
The same happens when a Sell Market order is executed. The
processing mechanism directs that order to the most immediate price level
of the BID column to find the counterpart in the Buy Limit orders that are
pending to be matched there.
With limit orders the process is the same. A participant leaves his
order pending execution in one of the two columns and it will stay there
until an aggressive trader arrives who needs to match his order.
--- page 169 ---

This is essentially what happens over and over again at high speed.
Regardless of the type of order used to enter the market, the end result
will always be that an aggressive order will cross with a passive one:
And the column on which those order crossovers will be displayed
will depend on the order that initiated it. Therefore:
❖ Buy Market crosses with Sell Limit and is displayed in the ASK
column, since the order that initiated the transaction is the
aggressive buy.
❖ Sell Market intersects with Buy Limit and is shown in the BID
column since the initiation comes from the aggressive sell side.

Now let's do a reasoning exercise using as an example a trader who
enters the market with a short position (sell). This trader has different
ways to exit this position:
--- page 170 ---

❖ Through a manual exit, either in loss or in profit by executing a
buy Market order (and it would appear in the ASK).
❖ By executing the stop loss (stop loss), whose order will be a buy
stop (and would appear in the ASK).
❖ By executing the take profit, whose order is a buy limit (and
would appear in the BID).

Similarly, a trader who enters the market with a long position (buy)
can leave it through three options:
--- page 171 ---

❖ Through a manual exit, either at a loss or at a profit by
executing a sell market order (and would appear in the BID).
❖ By executing the stop loss, whose order will be a sell stop (and
would appear in the BID).
❖ By executing the take profit, whose order will be a sell limit
(and would appear in the ASK).

The point of this example is that the same action, such as closing a
position, can be shown in different columns (BID and ASK) depending on
the type of order used for it.
Understanding this information is of tremendous importance
because many analyses of order crossing are erroneous because they start
from wrong premises.
The first conclusion should therefore be that not everything that
appears executed in the ASK column is buying with the intention of
--- page 172 ---

adding buying pressure to the market and not everything that appears in
the BID column is selling with the intention of adding selling pressure.
Herein lies the problem when analyzing order flow in any of its variants.
These programs based on the order crossing mechanism are set up
to always reflect aggressiveness, the problem is that it is not possible to
distinguish what intention is behind the executed orders.
When we see a cross executed in the ASK it will always be a Buy
Market with Sell Limit order; while when we see a cross executed in the
BID it will be a Sell Market with Buy Limit order, but what we will not
know is the origin/intention behind such a cross order:
The main source of error when dealing with order flow analysis
comes because there is the belief that everything executed in the ASK has
a buy initiative origin and everything executed in the BID has a sell
initiative origin, but as we have just seen, nothing could be further from
the truth. This type of software makes a reduction to the execution of
aggressive orders with passive, but they cannot know what the
origin/intention of those orders is.
What would happen if there is a crossing of orders of a Stop Loss
