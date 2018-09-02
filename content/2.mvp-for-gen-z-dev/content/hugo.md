---
title   : Hugo
status  : content
weight  : 30
---

[Hugo IO](https://gohugo.io) is a Static Website Generator (SWG) and represents a very interesting twist on the development stack of a website (another popular Static Website Generator is [Jekyll](https://jekyllrb.com/) )

In addition to having a great environment to create content (and to maintain it), what hugo represents is a completely different paradigm shift on how to create and publish websites.

Basically what SWG (Static Website Generators) do, is to pre-create all possible web pages during a build stage, and to place them all in a single folder that can be easily deployed to any server or service that is able to host static files (for example AWS [S3](https://aws.amazon.com/s3))

In practice this means that you can have a website running from valina web pages, with no backend and no moving parts. Not only this is massively secure (no server-side code to hack), this has amazing performance implications (i.e. the site is super fast, when compared with dynamically generated sites).

Ask yourself the question: "Why do you need a database?"

It is amazing how in tons of cases a database is not actually needed (specialy when it is possible to pre-generate all pages programmatically).

In fact Hugo is using a very efficient and scalable database and cache: The file system :)

I really like the pattern of using the file system as a database, specially when combined with git for deployment.

Hugo is also a great case-study of how modern development techniques, technologies, and open source innovation create products/apis that are miles ahead of the competition (with killer features)

I use Hugo a lot these days, in all sort of internal and external sites, and after using (and developing) all sorts of CMS (Content Management Systems), I have to say that it provides me a spectacular and highly-productive content creation/editing workflow.

This book for example has a companion websites that is created using Hugo, and I've created a number of extra pages that help to improve my productivity (for example search and print pages)
