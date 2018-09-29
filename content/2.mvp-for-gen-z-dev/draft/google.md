---
title: Google and GDD
status: draft
---

As a developer one of the most important skills you need to learn is how to GDD.

GDD stands for is Google Driven Development, and it how every professional developer codes these days. Google's search engine is so powerful and effective, that when coding (and learning), Google's Search Engine can point to the correct answers much better than somebody else.

#### But how does Google do it?

Google's search magic is created by the PageRank algorithm which is how Google decides the order for the results. One of the first major innovations of this algorithm was to use the number of links that point to particular page as an indicator of the page relevance. The other major innovation was the feedback loop between what the users are clicking and the position of that link in the page. This means that every time you click on a link in Google you are voting on your best answer and teaching Google's PageRank algorithm. To see this in action, note how when you copy the link of an Google Search result, the link is not to the page you want to see. The link is to an google service that will capture and store your choice. It is the capture of this data that allows Google to provide custom search results to each user (yes, when you search for a particular topic, you will get different results than somebody else)
 
The clever part of Google Business model is that it found a way for their product (which is the users) to actually 'work' for Google. Remember that for Google you (the entity doing the search) are not the client. You are the product. Google doesn't view you as a customer. You are the 'goods' that Google sells to their real customers. 


### Who are Google customers?

In most cases they are the companies that buy access to Google users to sell Advertisement. This is why Google wants to know more and more about what you (the user) is doing online, since that is what allows Google's clients to sell more and more targeted Ads.

[Google Adwords](https://en.wikipedia.org/wiki/AdWords) is the tech stack and workflows that allows just about anybody to buy (and bid for) an Ad on a particular keyword, which is the highest income stream for Google (with $94 Billion in revenue in 2017). 


### Do know how to use Google's Search Engine

how much do you really know how to use it? How much do you know about why and how Google was so successful? How much  

Have you [learned how to search using Google](https://support.google.com/websearch/answer/134479?hl=en&ref_topic=3081620). Google is a tool and you need to spend time learning how to use it and become a master at how to access and query the wealth of information that Google stores.

A great place to start is the [Advanced Search](https://www.google.com/advanced_search) page and this great list of [Google Search Operators](https://ahrefs.com/blog/google-advanced-search-operators/)

Next steps is to look into [Google Dorks](https://en.wikipedia.org/wiki/Google_hacking) which is a Google Hacking technique that searches for sensitive data exposed by Google's Crawlers. To get an and idea of what is possible check out the [Google Hacking Database](https://www.exploit-db.com/google-hacking-database/) which has sections like: Sensitive Directories, Files Containing Passwords, Sensitive Online Shopping Info , Network or Vulnerability Data and much more. I always find that the best way to learn a technology is using the techniques and patterns used to exploit it (because security tends to go deeper into what is 'really' possible, not just how it is supposed to be used). In this case, the Google Hacking Database will give you tons of examples of WTF how is this exposed to the internet, and more interesting, will make you ask the question, 'How did that work?' (which is the best way to learn)




### Google's history and scale

Google is one of the best Software engineering companies in the world, and one of the first companies to do 'Internet Scale' really well. 

Google is also massive on open source with highly successful [hundreds of projects](https://opensource.google.com/) projects like Android or Kubernetes. Google also hired some of the best Open Source developers to work on internal projects related to their passion, for example the [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) Python founder and lead developer worked at Google ..... TCB

Google's profits from the Search Engine were able to fund so many different areas and companies that in 2015 the founders of Google created the [Alphabet](https://en.wikipedia.org/wiki/Alphabet_Inc.) parent company. This is a really cleaver move since it should make each division (from self-driving cars, to drone deliveries) more accountable and focused.


---

**Topics to cover and ideas**
 
 - angular JS and Kubernetes, Chrome, Android
 - 
 - do you know how to use google?
    - show examples of powerful google searches
    - google docks (and finding vulns and credentials via google)
 - google's history 
    - clean UI
    - redirected traffic from other engines
 - why google won
 - what makes google algorithm work
 - How google tests software
 - SRE (book). lots of great concepts (like error Budgets)
 - show how google tracks all clicks (why you can't just copy an google's url)

 - Google move to graphs (see what happens when you search for a movie)
 - Google driven Development
 - show Google hacks (normal and security related)
 - Highlight the fact that google shows different searches to different people and different geographical regions
- Google Cloud (missed opportunity), google Borg

- mention Docker chapter , and rewrite 
   - Kubernetes (sometimes also called K8) was actually developed by Google and was inspired by [Google's Borg](https://ai.google/research/pubs/pub43438). The Borg is one of the key reasons why Google was able to scale massively in its web search and in services like GMail. Everything at Google is a container and as early as 2014 Google claimed to start [two billion](https://www.theregister.co.uk/2014/05/23/google_containerization_two_billion/) [containers per week](https://cloud.google.com/containers/)
- explain pagerank    
- explain adworks
- Gmail and GMaps history
- 20% to work on research projects
- Google approach to management and people management ('Work Rules' book). See [Not A Happy Accident: How Google Deliberately Designs Workplace Satisfaction](https://www.fastcompany.com/3007268/not-happy-accident-how-google-deliberately-designs-workplace-satisfaction)
- Google's [Chief Decision Officer](https://www.fastcompany.com/90203073/why-google-defined-a-new-discipline-to-help-humans-make-decisions) and the field of Decision Intelligence Engineering

- task: programmatically detect changes in google's behavior. Once you have a script that is able to use Google.com to search for results, you need to capture the responses (namely title and links) into an json file, and then compare it
- mention Alphabet
- explain how Google Links works (how they capture the link that you clicked)
- How Google Analytics works (gs.js)
- mention the idea that users should be paid for the work they give for free
- you are the product not the customer (Google sells access to you). 

