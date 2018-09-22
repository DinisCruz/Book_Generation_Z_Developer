---
title: Slack and ChatOps
status: content
what  : Communication and decision making platform
task  : Create Slack Workspace and write a Slack bot integration
price : free
---

It is easy to underestimate [Slack](https://slack.com/)'s capabilities, not realise that Slack is a massive agent for change, and that Slack's empowered workflows will play a  big  part in your future as a developer. 

Initially Slack might look like just an evolution of instant messaging tools like: [Skype](https://en.wikipedia.org/wiki/Skype), [MSN Messenger](https://en.wikipedia.org/wiki/Windows_Live_Messenger), [SMS](https://en.wikipedia.org/wiki/SMS), [ICQ](https://en.wikipedia.org/wiki/ICQ), [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) or [Smoke Signals](https://en.wikipedia.org/wiki/Smoke_signal). 

The reason why Slack in a relative short period (5 years) gained such adoption and traction, is because its features enable organizations and communities to not only to change how they communicate, but how they behave. Namely how they understand what is going on and how they respond to events.

Effective Communication and alignment are not only key competitive advantages of successful organizations, but are usually the reason they succeed or fail (see ["Aligning vectors"](https://www.linkedin.com/pulse/what-elon-musk-taught-me-growing-business-dharmesh-shah/) presentation for more details). 

Slack provides an Asynchronous data/information exchange environment that can be at the epicenter of the multiple actors involved in the organization ecosystem: humans, bots, servers, applications, services and events.

The potential for change is enormous, although at the moment, most companies are only taking advantage of about 10% of Slack's capabilities. In most organizations Slack is at the _'replacing email'_ stage, which quickly is followed by the _'too many channels'_ and _'how do find what is going on without having to read a gigantic slack thread'_ phases (which can have diminishing returns)

The important question for you is: _"Are you going to take an active and proactive role in making Slack work for an organization?"_. I can guarantee you that if you have hands on experience in the ideas and techniques described in this chapter, you have just increased your competitive advantage and employability.

### Why was Slack successful?

Slack's success is a great case study of the power of marginal gains, where a large number of 1% improvements created an spectacular platform (for another great example 1% marginal gains the see the British' cycle success on _[How 1% Performance Improvements Led to Olympic Gold](https://hbr.org/2015/10/how-1-performance-improvements-led-to-olympic-gold)_ where they talk about the power of marginal gains, based on 3 areas: strategy, human performance and continuous improvement).

Here are some of the features that Slack added that (in aggregation) made a massive difference:

 - **Copy and Paste of images** - this 'simple' feature massively improves the user's workflow and ability to communicate (It still amazes me how companies don't realise that there is a massive usability difference between copy and pasting an image and having to upload an image). If I remember correctly this was one of the reasons I started to like Slack
 - **Effective use of Emojis** - not only for emotions (happy/sad/angry/laughing face) but for actions/decisions (yes/no, ok, 'read document', 'need more details')
 - **Great desktop application** - with seamless integration with web and mobile (the desktop app is built of top of [Electron](https://electronjs.org/))
 - **Effective search and shortcuts**
 - **Drag and drop of documents** - with ability to preview them in slack (for example pdfs)
 - **Auto previews of links dropped** - like web pages, twitter links, videos
 - **Buttons and forms to drive actions** - which allow the expansion/improvement of Slack's UI by 3rd party apps/services
 - **3rd party integrations** and **Native support for Bots**
 - **Smooth and regular deployment of new features** (audio and voice conferencing, single channel users, message reminders, message threads)
 - **Scalable backend with very few outages**
 - **Application Security** and **Security usability**

All of the above combined (can) create a super productive environment. Your task is to be a 'Slack master' and lead the revolution :)

The big lesson here is that: 

1. high focus on where you add value, speed of delivery and adaptability of the direction of travel 

beats 

2. a highly defined strategy 

For a great example of changing directions, if you check out [Slack's history](https://en.wikipedia.org/wiki/Slack_(software)) you will see that Slack actually started as an internal tool created by the company _Tiny Speck_ while they were working on the [Glitch](https://en.wikipedia.org/wiki/Glitch_(video_game)) game

### Learn how to use Slack

As with every tool, you need to spend time in learning how to use it in order to be effective. It is very important to  initially not be overwhelmed by the large number of channels and messages that you will get. 

Fun fact, when things get quite heavy, sometimes we call it _'Slack Tennis'_ since there is so much stuff bouncing around in multiple channels that it fells like you are playing Tennis inside Slack.

Some practical tips:

 - remove most  Slack notifications 
 - mute chatty channels that don't provide important information for your day to day activities
 - do to not be afraid to leave a channel, since if you are needed, it is easy for others to bring you in with a mention of your name
 - consume Slack under your terms, not when a message arrives and you receive a dopamine kick
 
 Think of Slack as asynchronous communications, where there is a gap of time between when:
 
 1. a message is sent
 2. a message is received  
 3. a message is processed (with our without a reply)

 As with just about everything, the challenges are one of People, Process and Technology:
 
 - **People**  - you and and who/what you are communicating with
 - **Process**  - how Slack is used (conversions, workflows, human behaviors, response's protocols/expectations, new users on-boarding, documentation)
 - **Technology**  - Slack and its integrations

 The good news is that you have direct control over these three, and there is nothing stopping you from learning. 
 
 This is why your understanding and use of Slack is a major sign of your own values and skills. 
 
 There is no cost in learning and using slack in the ways I describe in this chapter. 
 
 If you don't learn how to effectively use Slack, what is that telling about your drive, priorities, energy, desire to learn and ability to effectively use new technologies. Basically your competitive advantages in the marketplace is directly related to how you use Slack.

### ChatOps

Let's go up a gear and start looking at what makes Slack so powerful. I'm talking about Bot Integration.

Bots are basically applications (ideally setup in a serverless pipeline) that react or generate events. For example we could have a bot that:

1. receives a notification from an live server (an CPU Spike, new deployment, or an particular user action) or from an 3rd party service (like email, twitter or CI pipeline)
2. processes and (optionally) transforms it
3. sends a follow-up slack message to a particular channel (based on a pre-defined set of rules)
4. gets response from user (simple acknowledgement or action)
5. reacts to that response

The concept that clearly explains this workflow is the '_ChatOps_' idea, which was initially shared in the amazing '[Chatops At GitHub](https://speakerdeck.com/jnewland/chatops-at-github) presentation (see video [here](https://www.youtube.com/watch?v=NST3u-GjjFw)) 

One of the definitions of ChatOps is  _"a collaboration model that connects people, tools, process, and automation into a transparent workflow"_ that creates a  _Culture of Automation, Measurement and Sharing_ (CAMS). This basically means that ChatOps is at the epicenter of information and decisions flows.

A real world example is when you (as a developer) use Slack as a communication medium for what is going on (in your live servers, test's execution or even build). But even more interesting, not only you can get data into Slack, you can issue back commands and influence what is going on. 

### Getting started 

The best way to learn is by doing it. 

Your first step is to [create a Slack workspace](https://slack.com/create) so that you have a playground for your ideas. There is [no cost](https://slack.com/pricing) to create new Slack Workspace, so what are you waiting for? 

Make sure you invite your friends and colleagues to participate, so that you have a wide set of scenarios to play with.

To get you going here are a couple scenarios: 
  
  - write code that sends messages to a slack channel (simple HTTP POST requests with your Slack API key)
  - follow GitHub's footsteps and deploy and customize [Hubot](https://hubot.github.com/). [Errbot](http://errbot.io/) is a Python alternative, and Slack's tutorial shows an integration using [Botkit](https://api.slack.com/tutorials/easy-peasy-bots)
  - write bot integrations with services like [Zapier](https://zapier.com/) or [IFTTT](https://ifttt.com/). See Zapier's _[How to Build Your Own Slack Bot in 5 minutes](https://zapier.com/blog/how-to-build-chat-bot/)_ guide
  - write a serverless Slack integration using AWS API Gateway and Lambda functions
  - write a Slack integration that automates one area of your life (maybe something to do with a task you do every day) 

### Join the OWASP Slack Community

OWASP (Open Web Application Security Project) is an very friendly open source community that has migrated a large part of its digital interactions to Slack (see [OWASP chapter](https://github.com/DinisCruz/Book_Generation_Z_Developer/blob/master/content/2.mvp-for-gen-z-dev/content/owasp.md) for more details).

I strongly advise you to join the Owasp Slack using the http://owaspslack.com/ registration form. 

Not only you will see examples of these integrations in real-world scenarios, in that workspace you will find a multiple Slack experts, who will be more than happy to help you. You can also find multiple opportunities (in OWASP project or chapters) to put your Slack integration skills in action.

When you join in, drop me a message saying Hi. I should be easy to find :)


### Talking to yourself via Slack

As I mention in the [Talking to yourself digitally](https://github.com/DinisCruz/Book_Generation_Z_Developer/blob/master/content/4.life-patterns/content/talking-to-yourself.md) chapter, the practice of capturing your thoughts and workflows is super important.

Slack is a great medium to do this, since it massively improves the workflow that we we usually have when using Word docs (or services like [Evernote](https://evernote.com/)) to capture notes about what we are doing. 

Here is the workflow I usually use:

 1. in Slack describe what I am going to try next
 2. do it
 3. take screenshot of the latest change
 4. in Slack paste the screenshot
 5. go back to 1.

This workflow is really powerful, because what you are doing is capturing how you are thinking about the problem you are solving (including all the tangents that you tried and didn't work). And yes, very often, you will find that it is only you that (initially): asks questions, provides answers, learn from failures and celebrates successes.

One way to keep sanity is to remember that this information will be super useful one day to your _'future self'_, and that you now have the raw data / screenshots for a great blog post. This will help others to understand the steps you took, the challenges you had, the solutions that didn't work, the solutions that did work, and how to arrived at the final result/conclusion. 

This is also how you scale your knowledge and avoid having to answer the same question twice (specially when you create a blog post which makes it really easy to find that content)

A simpler version of this pattern is when you:

1. ask a question in Slack
2. find the answer
3. reply to your own message with the solution

### Use Slack when debugging code (as a log collector)

When you have a bug in your code that you don't understand the root cause, a common practice is to use a [Debugger](https://en.wikipedia.org/wiki/Debugger), which will provide features like breakpoints and code stepping.

This just about works when you have direct access to the execution environment and you are looking at simple applications. 

But as soon as you start working on distributed systems with lots of moving parts (for example with multiple web services and serverless functions), you stop having the ability to realy understand what is going on (namely the exact sequence of events and what the data looks like in those intermediate states) 

Slack gives you an environment to receive logs/messages from those internal execution flow and states. To make this scale, you should create helper APIs that make it easy to send and receive data from Slack.

As simple example, here is a Python method that I wrote to help me understand and debug AWS Lambda function's execution:

```
send_to_slack('there are {0} missing ips'.format(len(missing)))

    ...(do something)...

send_to_slack('resolving {0} missing ips'.format(len(missing)))

   ...(do something)...

send_to_slack('resolved {0} ipdata ips'.format(len(ipdatas)))
```


 


 