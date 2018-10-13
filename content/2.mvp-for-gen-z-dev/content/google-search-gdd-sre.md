---
title: Google Search, GDD and SRE
status: content
weight: 40
what  : Search engine and development workflows
task  : Write scripts to automate and analyse Google search results
price : 0
image : 
---

As a developer one of the most important skills you need to learn is how to GDD.

GDD stands for is Google Driven Development, and it is how every professional developer codes these days. Google's search engine is so powerful and effective that when coding (and learning), Google's Search Engine can point to the correct answers much better (and generally much quicker) than anyone or anything else.

#### Why is Google Search so good?

Google's search magic is created by the [WebGraph](https://en.wikipedia.org/wiki/Webgraph) inspired [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm, which decides the order in which the search results appear. One of the first major innovations of this algorithm was to use the number of links to a particular page as an indicator of the page's relevance. The other major innovation was introducing a feedback loop between what the users were clicking on the search results page and the resulting position of the link on the page. This means that every time you click on a link in Google, you are effectively voting with your answer and teaching Google's PageRank algorithm. To see this in action, notice when you copy the link of a Google Search result, the link is not to the page you want to see. The link is to a google service that will capture and store your choice. It is the capture of this data that allows Google to benefit from [network effects](https://en.wikipedia.org/wiki/Network_effect) and provide custom search results to each user. Yes, when you search for a particular topic you will get different results from somebody else. 

Here is a challenge for you: _"how can you prove that google shows different results for different users and in different geographical locations?"_. To answer this question effectively and factually you'll need to programmatically detect changes in google's behavior. To do this, using a Cloud environment, write an api/tool (or set of serverless functions) that:
  - is able to use Google.com to search for results from multiple IPs and geographical regions (in an pure anonymous way, and in ways that Google search engine can track each one of you 'test users')
  - captures the responses, namely the order in which the link's titles appear (my preference is to use services like S3 as a data store, for the raw data and any transformations done into JSON files)
  - visualizes and compares the results (my preference is to use ELK and Neo4J as visualization and analysis engines)
  - presents the data in easy to consume ways (my preference is to use Hugo to create a site that allows the easy navigation of the 'story you want to tell')

Also very interesting is the [evolution](https://medium.com/s/story/what-google-teaches-us-2613711712de) of Google's Search technology into a Knowledge Graph (which has been [happening since 2010](https://mashable.com/2012/02/13/google-knowledge-graph-change-search/)). The real power in Google's search engine is the gigantic and hyperlinked graph (powered by machine learning) that is able to understand the meaning and intent of the queries made.

#### For Google Search, you are the product
 
The clever part of Google Search business model is their turning of the product (i.e. the users doing the searches) into actual 'workers' for Google. Remember that for Google you are not the client. Google's primary focus and center of gravity is not you.

[Google Adwords](https://en.wikipedia.org/wiki/AdWords) is the system that allows everybody to buy (and bid for) the placement of Ads on a particular Google search keyword. Adwords is by far the highest income stream for Google, with $94 Billion in revenue in 2017 [*reference needed*]. A key problem with Ad based services that are seemingly 'free' (but generate billions for the owners of the network) is the reality that you (the user) are the product. You are the 'goods' that Google sells to their real customers (the companies buying the ads). 

This is why Google's business model is at odds with privacy. From Google's (and Facebook, Twitter, LinkedIn, etc..) point of view, the less Privacy you have the more they know about you and the more valuable an asset you become (an asset that they will sell to the highest bidder). 

My view is that this business model is reaching its peak. Two major changes will happen in this space in the short to medium term: the move to make the user the real customer and the move to reward users that add value to networks.

Let's analyse these trends in more detail.

1. User as the real customer - Once the balance of power shifts back toward the user and the protection of user data (with Privacy elevated to a Human right and something companies want to provide for their employees), the protection and anonymization of user's data will be an area with massive growth. And in ways that make the process of sharing and using personal data more secure, efficient and even more profitable. 

2. Network that rewards its contributing users - Jaron Lanier in _[You are not a Gadget](https://www.amazon.co.uk/You-Are-Not-Gadget-Manifesto/dp/0141049111)_ defends the idea that creators of digital value should be paid for their contributions (in micro-payments). If you look at the income generated by Google and other community/Ad driven companies, you can see that the rewards and financial reurns for the value created by the product (i.e. the users) is today very one sided with notable exceptions such as [YouTubers](https://en.wikipedia.org/wiki/YouTuber) and [Medium Writers](https://medium.com/words-for-life/a-100-transparent-look-at-my-first-medium-paycheck-197b69483b44)).

You would be very wise in researching and learning about these paradigm shifts, namely: how will they impact development practices and the code you write.

### Do know how to use Google's Search Engine?

How much do you really know about searching Google for text (images, ideas, videos, books) in the most efficient, effective and productive way? 

Have you spent time to [learn how to search using Google](https://support.google.com/websearch/answer/134479?hl=en&ref_topic=3081620)? Google is just another tool. You need to spend time learning how to use it and become a master at how to access and query the wealth of information that it stores.

A great place to start is the [Advanced Search](https://www.google.com/advanced_search) page and this great list of [Google Search Operators](https://ahrefs.com/blog/google-advanced-search-operators/).

Once you've done that, take a look at [Google Dorks](https://en.wikipedia.org/wiki/Google_hacking) which is a Google Hacking technique that searches for sensitive data exposed by Google's Crawlers. To get an idea of what is possible check out the [Google Hacking Database](https://www.exploit-db.com/google-hacking-database/) which has sections like: Sensitive Directories, Files Containing Passwords, Sensitive Online Shopping Info, Network or Vulnerability Data and much more. You will be surprised, amazed and horrified by what you will discover.

I always find that the best way to learn a technology is using the techniques and patterns used to exploit it; because security tends to go deeper into what is 'really possible' and not just how it is 'supposed to be used'. In this case, the Google Hacking Database will give you tons of examples of "WTF! how is this data exposed to the internet"? More interesting and relevant to your quest into becoming a better developer, this data will make you ask the questions: _'How did that search query work?'_ and _'How did Google Crawlers found that data?'_ (which is the best way to learn)

### Google's history and scale

Google is one of the best Software engineering companies in the world, and one of the first companies to do _'Internet Scale'_ really well. 

Google is also massive in open source with highly successful [hundreds of projects](https://opensource.google.com/) projects like Angular JS, Android or Kubernetes. Google hires some of the best Open Source developers to work on internal projects related to their passion. For example [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), Python's founder and lead developer, worked at Google. By the way, being hired to work on Open Source projects is a very common practice for companies that actively use a particular technology or language. This is a great way to get a dream job: write an Open Source tool/package and get hired by a company that uses it.

Google's profits from the Search Engine are so high that it was able to fund a large number of ideas and industries. It got so big that in 2015 the founders of Google created [Alphabet](https://en.wikipedia.org/wiki/Alphabet_Inc.) as Google parent company. This is a really clever move since it will make each susequent division (from self-driving cars, to drone deliveries) more accountable and focused.

### Learn from Google's focus on engineering and SRE

Part of the reason Google has gained massive amounts of market share is due to its ability to experiment and then execute at scale. Google allows employees to spend 20% of their time on ideas they are passionate about, which sounds crazy at first, but there is [solid data](https://www.inc.com/bryan-adams/12-ways-to-encourage-more-free-thinking-and-innovation-into-any-business.html) to suggest this practice is highly effective at empowering developers to create new products and services. For example Google services like AdSense, Gmail, Google Maps, Google News or Google Talk were initially developed under the 20% research time initiative. 

Also, Google sets the bar incredibly high for quality and engineering. Two good books that explore their practices are the [How Google Tests Software](https://www.amazon.co.uk/Google-Tests-Software-James-Whittaker/dp/0321803027) and the [Site Reliability Engineering](https://www.amazon.co.uk/Site-Reliability-Engineering-Betsy-Beyer/dp/149192912X).

The [SRE (Site Reliability Engineering)](https://landing.google.com/sre/) is an amazing concept that you as a developer really should spend time learning and understanding (especially how SREs behave). At Google, the SRE teams are the ones that deploy and maintain applications. There are many lessons that we can learn from Google's experience of deploying things at scale. For example I really like the SRE idea of spending 50% 'doing X' and 50% improving the process + tools required to do 'X'more effectively. ['Error Budgets'](https://landing.google.com/sre/book/chapters/embracing-risk.html) are another SRE concept which can make a massive difference in how applications are developed and tested. The SRE idea of 'Error Budget' is that each application or service needs to provides a clear and objective metric of how unreliable that service is allowed to be within a set period of time.

Google also puts a lot of effort in understanding workers interaction from a scientific prspective and how to create hi-performing teams. See ['Work Rules'](https://www.amazon.co.uk/Work-Rules-Insights-Inside-Transform-ebook/dp/B00NLHJKBE) book,  _[Not A Happy Accident: How Google Deliberately Designs Workplace Satisfaction](https://www.fastcompany.com/3007268/not-happy-accident-how-google-deliberately-designs-workplace-satisfaction)_ and [Why Google defined a new discipline to help humans make decisions](https://www.fastcompany.com/90203073/why-google-defined-a-new-discipline-to-help-humans-make-decisions) (which introduces the role of _Chief Decision Officer_ and the field of _Decision Intelligence Engineering_)