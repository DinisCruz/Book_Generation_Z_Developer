---
title : Jira
status: content
weight: 20
what  : Web based issue tracking system (can be used as Graph Database)
task  : Create an free account at atlassian.com and try it out
price : 0 to you
image : images/logo-creative-commons.png
---

[Jira](https://www.atlassian.com/software/jira) is a web application that is widely used by development, engineering and technical teams to manage their day to day tasks and activities.

There is massive worldwide adoption by all types of companies, and we (at Photobox Group Security) use Jira extensively in our day-to-day. We use it for example to manage: vulnerabilities, risks, task management, incident handling, OKRs (Objectives and Key Results) management, asset register, threat modeling, data journeys and even to create a pseudo org chart for the stakeholders of risks. 

To make this work we are very advanced users of Jira, where we create tons of custom Workflows and even write custom applications that consume Jira's APIs.

We basically use Jira as a graph database and [Confluence](https://www.atlassian.com/software/confluence) as a way to display the information stored in JIRA. See the [Creating a Graph Based Security Organization](https://www.slideshare.net/DinisCruz/creating-a-graph-based-security-organisation-devseccon-keynote-81345667) presentation for more ideas on how we do this.

The key point I want to make here is: in order to make the tools that we use in the enterprise work, they need to be customized and extended. 

Being able to write these customizations and understanding at a much deeper level what is possible with these tools is a massive competitive advantage, when compared to 'normal' or 'power' users. Customizing and extending tools should not be seen as an exception, it should be the rule. 

The reason this scales is due to the compound effect (i.e. increased returns) of the features implemented. The changes/features we make today, will make us more productive tomorrow, which will help us to make more changes, which make us even more productive.

In fact as a developer, if you are able to write custom JIRA workflows that are usable by your team, that will be another competitive advantage for you, and it will make you highly employable today.

### Reality is the complex one

It is important to note that once the complexities and interconnections of reality start to be mapped in Jira, it can be very overwhelming. 

For example we use Jira heavily in our incident handling process, where we can easily create 100+ issues during an incident, with each issue being a relevant question or action to be answered or executed during the incident. It is easy to look at that setup and think that it is too complex and a massive bureaucracy. But in reality that combination of issues (of type: Incident, Task, Vulnerability and Epics) is an accurate representation of the complex reality and massive amount of information that is created during an incident. The alternatives are completely unmanageable and unreadable email, slack threads or word docs). 

All the work comes together via powerful up-to-date Confluence pages (which we convert to PDFs and distribute via slack/email) to answer the key questions of: 'What has happened?', 'What are the facts?', 'What are the hypothesis we are exploring?', 'What is happening now?' and 'What are the next steps?'. This is how we keep everybody involved in sync, and how we provide regular management updates.

The other big advantage of this setup is that it allows us to do very effective post-incident analysis and to create playbooks with predefined tasks to be executed when a similar incident occurs in the future. Basically our playbooks are not a word document with tasks and actions, our playbooks are a lists of Jira Tasks that are used to populate the incident set of tasks.

For more ideas about this topic see the [SecDevOps Risk Workflow](https://leanpub.com/secdevops/) book that I'm also writing and the [SecDevOps Risk Workflow - v0.6](https://www.slideshare.net/DinisCruz/secdevops-risk-workflow-v06) presentation .


### Use Jira in your life

Create Jira projects for your life activities, with Epics to track group of tasks.

Create a Kanban board for your personal tasks and Epics.

Create custom workflows and learn how to manage Jira. This will give you tons of confidence when using Jira in the real world or when intervening.

And since Atlassian has evaluation version for their cloud version of Jira, there isn't any cost to try this. You have no excuse for not using Jira before, at a level more advanced than most corporate users and the developers interviewing you.

### What makes Jira so powerful

Although Jira has tons of really annoying features and bugs, its feature set is very powerful. With finely tuned process and customizations it will make the difference on your productivity and will change how you work.

Here are some of Jira's really powerful features:
 
 - **Issues** - that can be easily linked to each other (i.e. nodes and edges)
 - **Links** - which can be named, and allow the creation of named edges, for example 'RISK-111 is-created-by VULN-222'
 - **Workflows** - state machine environment where the issue's status can be visually mapped and powerful buttons be created, for example for status transitions like 'Accept Risk'
 - **Activity logging** - ability to log every change and status transition
 - **Labels** - ability to apply all sorts of loosely created labels/tags to issues (we use this to help managing specific workflows, for example by adding the 'Needs_Risk_Mapping' label to an issue)
 - **Components** - ability to map issues to components which map directly into business' areas or applications
 - **Kanban boards** - powerful way to view the current tasks and what status they are
 - **Dashboards** - ability to create all sorts of diagrams and tables from Jira data (although we tend to use Confluence for data visualization)

### Its all about People, Process and Technology

In order to create a successful Jira environment, the 'Technology' part, we have to start with the 'People' part (in this case you). It is the mindset of the individual user that helps to kickstart these workflows.

The 'Process' of how things work is the other key element. I found it's very hard for participants to really 'get' these processes and to really understand at a deeper level how the hyperlinked graph-based architecture works. By nature there will be a lot of changes, not only of past workflows, but of existing workflows. Change is the only constant.

Ironically this means that Jira is not key to make this work. 

I have built similar systems using GitHub.

Although GitHub doesn't have some of the most advanced features of Jira (like workflows), the fact that GitHub has native Markdown support, that all content is managed using git and that it is super fast, makes it also an effective graph database.

With the right People and Process, lots of Technologies can be used to make this work. As long as they can be used a Graph Database with every piece of data being available in an hyperlinkable way
