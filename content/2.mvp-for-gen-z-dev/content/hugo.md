---
title : Hugo
status: content
weight: 30
what  : static site generator and major paradigm shift on how to think about websites creation and deployment
task  : install hugo, create a website and publish it (ideally using AWS S3)
price : zero (hosting might have some costs)
image : 
---

[Hugo IO](https://gohugo.io) is a SWG (Static Website Generator that represents a very interesting twist on the development stack of a website (another popular Static Website Generator is [Jekyll](https://jekyllrb.com/) )

In addition to having a great environment to create content (and to maintain it), what hugo creates is a completely different paradigm shift on how to create and publish websites.

Basically an SWG pre-generates all possible web pages during the build stage .... and that's it! 

Once the build is finished (usually in less than a second), the entire content of the website is available in an local/CI folder, that can be easily deployed/copied/synced with any server or service that is able to host static files (for example AWS [S3](https://aws.amazon.com/s3))

In practice this means that you have a website running from vanilla web pages, with no backed and no moving parts. Not only this is massively secure (no server-side code to hack), this has amazing performance implications (i.e. the site is super fast, when compared with dynamically generated sites).

"Why no backend?" Well ... ask yourself the question: "Why do you need a database?" (i.e. What is the database actually doing, that you can't pre-generated all in one go?)

It is amazing how in any real-world scenarios a database is not actually needed!

That said, Hugo is actually using a very efficient and scalable database and cache: The file system :)

I really like the pattern of using the file system as a database, specially when combined with git for deployment, and GitHub for CMS (Content Management System)

Hugo also makes it really easy to create (and understand) an CD (Continuous Deployment) environment. Since it covers the key steps required: 

 - build the site 
 - edit the site
 - see changes
 - publish/sync the generated files (to a server/service serving static files)
 - (ideally you should also be writing tests, which I would do using: NodeJS, CoffeeScript, Mocha, Cheerio and WallabyJS)

Another key feature is the integration with [LiveReload](https://github.com/livereload/livereload-js) (which very important to experience in a practical/personal way). Assuming you have the editor and web browser side-by-side in your screen, Hugo+LiveReload creates an environment where you can see your content changes immediately reflected in the browser, in an quasi-real-time way (i.e as soon as the file is saved, the browser is reloaded and the new content in rendered)

Hugo is also a great case-study of how modern development techniques, technologies, and open source innovation create products/apis that are miles ahead of the competition, with killer features.

After using and developing all sorts of CMS (Content Management Systems), I have to say that it gives me a spectacular and highly-productive content creation/editing workflow. 

I use Hugo a lot these days, in all sort of internal and external sites, here are some examples:

 - The Open Security Summit 2018 website (https://open-security-summit.org/) is a highly complex data driven website (which will look like a database-powered site) that is entirely built on top of Hugo. All source code is available on [this GitHub repo](https://github.com/OpenSecuritySummit/oss2018) and the Hugo setup enabled 157 contributors to create 3575 commits
 - The Photobox Group Security Site (https://pbx-group-security.com/) is a simpler example of a fully working Hugo site in action
 - This book you are reading uses Hugo in two ways:
    1) locally hosted website with a number of extra pages that helps to improve my productivity when writing the book (for example: an hugo-based search, and print-friendly pages), 
    2) markdown generation for Leanpub publishing (which adds a couple extra features like the ability to create the MVP table from the content of its child pages)

### Simple example (MVP)

Here is simple example of my very first test of using Hugo where changes on the left are shown automagically on the right. I always start learning a new technology by creating the simplest possible version that works, i.e. an MVP.

![](images/hugo-simple-example.jpg)

### More advanced example (with graphs)

Here is a more advanced usage of Hugo, where we are using Hugo to create VisJs visualizations of Neo4J graphs populated from JIRA data

![](images/hugo-with-graphs.jpg)

### Do Static Site Generators scale?

Although I prefer Hugo to Jekyll, here are two amazing examples of using Jekyll at scale:

 - HealthCare.gov - see _[It's Called Jekyll, and It Works](https://developmentseed.org/blog/2013/10/24/its-called-jekyll/)_
 - Obama's fundraising website - see _[Meet the Obama campaign's $250 million fundraising platform](http://kylerush.net/blog/meet-the-obama-campaigns-250-million-fundraising-platform/)_
