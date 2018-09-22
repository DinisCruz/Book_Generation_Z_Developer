---
title: Slack and ChatOps
status: draft
---

Initially [Slack](https://slack.com/) feels like an evolution of instant messaging tools like Skype, MSN Messenger, SMS, ICQ, IRC or Smoke Signals. But the reason why Slack in a relative short period (5 years) as gained such adoption and traction, is because its features enable organizations and communities to not only to change how they communicate, but how they behave, namely how they understand what is going on and how they respond to events.

Effective Communication and alignment are not only key competitive advantages of successful organizations, but are usally the reason they success of fail. Slack provides an Asynchronous data/information exchange environment that can be at the epicenter of the multiple actors involved in the organization ecosystem: humans, bots, servers, applications, services and events.

The potential for change is enormous, and at the moment, most companies are only taking advantage of about 10% of Slack's capabilities. In most organizations Slack is at the _'replacing email'_ stage, which quickly is followed by the _'too many channels'_ and _'how do find what is going on without having to read a gigantic slack thread'_ phases (which can have diminishing returns)

The important question for you is: _"Are you going to take an active and proactive role in this change?"_. I can guarantee you that if you have hands on experience in the ideas and techniques described in this chapter, you have just increased your competitive advantage and employability.

### Why was Slack successful

Slack's success is a great case study of the power of marginal gains, where a large number of 1% improvements created an spectacular platform (for another great example 1% marginal gains the see the British' cycle success on '[How 1% Performance Improvements Led to Olympic Gold](https://hbr.org/2015/10/how-1-performance-improvements-led-to-olympic-gold)' where they talk about the power of marginal gains, based on 3 areas: strategy, human performance and continuous improvement).

Here are some of the features that Slack added that (in aggregation) made a massive difference:

 - Copy and Paste of images - massively improves workflow and ability to communicate (It still amazes me how companies don't realise that there is a massive usability difference between copy and pasting an image and having to upload an image)
 - Effective use of Emojis - not only for emotions (happy/sad/angry/laughing face) but for actions/decisions (yes/no, ok, 'read document', 'need more details')
 - great desktop application - with seamless integration with web and mobile (the desktop app is built of top of [Electron](https://electronjs.org/))
 - effective search and shortcuts
 - drag and drop of documents with with ability to preview them in slack (for example pdfs)
 - auto previews of links dropped (like web pages, twitter links, videos)
 - buttons and forms to drive actions (which allow the expansion/improvement of Slack's UI)
 - 3rd party integrations 
 - Native support for Bots
 - Smooth and regular deployment of new features (audio and voice conferencing, single channel users, message reminders, message threads, )

All of the above combined (can) create a super productive environment. Your task is to be at that end of the spectrum and be a 'Slack master'

The big lesson here is that a high focus on where you add value, speed of delivery and adaptability of the direction of travel beats a highly defined strategy (if you check out [Slack's history](https://en.wikipedia.org/wiki/Slack_(software)) you will see that Slack actually started as an internal tool created by Tiny Speck while they were working on the [Glitch](https://en.wikipedia.org/wiki/Glitch_(video_game)) game)

### Learn how to use Slack

As with every tool, you need to spend time in learning how to use it in order to be effective, and very importantly, not to be innitially overwhelmed by the large number of channels and messages that you will get. 

When things get quite heavy, sometimes we call it 'Slack Tennis' since there is so much stuff bouncing around in multiple channels.

Some practical tips:

 - remove most  Slack notifications 
 - mute chatty channels that don't provide important information for your day to day activities
 - do to not be afraid to leave a channel, since if you are needed, it is easy for others to bring you in with a mention of your name
 - consume Slack under your terms, not when a message arrives and you receive a dopamine kick
 
 Think of Slack as Async communication, where there is a gap of time between when a message is sent, a message is received and even when a message is processed

 As with everything the challenges is:
 
 - People (you and your network)
 - Process (how Slack is used) 
 - Technology (Slack and its integrations)

 The good news is that you have direct control over these three, and there is nothing stopping you. This is why your understanding and use of Slack is a major sign of your own values and skills. There is no cost in learning and using slack in the ways I describe in this chapter. And if you don't, what is that telling me about your drive, energy, desire to learn and ability to effectively use new technologies. Basically your competitive advantages in the marketplace is directly related to how you use Slack.

### ChatOps

Let's go up a gear and start looking at what makes Slack so powerful: Bot Integration

Bots are basically applications (ideally setup in a serverless pipeline) that react to events. For example a bot that receives notifications from an server (or 3rd party service) and sends a slack message to a particular channel (based on a pre-defined set of rules)

The concept that clearly explains this workflow is the '_ChatOps_' idea, which was initially shared in the amazing '[Chatops At GitHub](https://speakerdeck.com/jnewland/chatops-at-github) presentation (see video [here](https://www.youtube.com/watch?v=NST3u-GjjFw)) 

One of the definitions of ChatOps is  _"a collaboration model that connects people, tools, process, and automation into a transparent workflow"_ that creates a  'Culture of Automation, Measurement and Sharing (CAMS). This basically means that ChatOps is at the epicenter of information and decisions flows.

A real world example is when you (as a developer) use Slack as a communication medium for what is going on (in your live servers, test's execution or even build). But even more interesting, not only you can get data into Slack, you can issue back commands and influence what is going on. 

The best way to learn is by doing it. Here are some ideas:
- Write code that sends messages to a slack channel (really easy since it is only an HTTP post request)
- follow of GitHub's footsteps and deploy and customize [Hubot](https://hubot.github.com/) ([Errbot](http://errbot.io/) is a Python alternative)
- write integrations with api integrations services like [Zapier](https://zapier.com/) or [IFTTT](https://ifttt.com/)
- 

### Talking to yourself via Slack

### Use Slack as a debugger



### Security considerations
 - now a critical part of business
 - data protection and encryption
 - adopt snapchat security paradigms
 - better understanding (and logging) of who is seeing what (important for security incident handling) and ability to integrate with other authentication solutions (like OAuth)
    - ability to send access to logs to an AWS S3 bucket would be great
 - More granular control for bot access (in fact a mature API to manage access keys would be great)
 - More granularity in the pricing model (specially for some security features)
 





**Topics to cover and ideas**

- built of top of Electron
- example of the right technology at the right time
 - Slack bots
    - power of bots to automate workflows    
    - 
 - Why slack won
 - Integrations using Zapier or ITTT and AWS Lambda with API Gateway
 - Copy and paste of images
 - there are large numbers of Slack communities that you can join, for example OWASP the Open Security Summit one
 