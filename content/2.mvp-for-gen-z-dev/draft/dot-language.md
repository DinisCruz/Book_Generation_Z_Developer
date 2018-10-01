---
title : Dot Language
status: draft
---

As a new developer joining the market, one of the real-world patterns that will surprise you the most is the lack of up-to-date documentation and diagrams about how the applications, services and even code behave (and even when they exists, they are usually out-of-date and not used on day-to-day decisions and coding). When you take a step back and think about this, you should realise that it is insane. What we do when developing software is to create large interconnected and complex structures without accurate maps and a solid understanding of what already exists and we are supposed to be building.

This doesn't happen because developers, architects or managers don't understand or value good up-to-date documentation. In fact they are usually the first ones to complain about these gaps. The problem is that most patterns and technologies used to create these diagrams are highly inefficient, time-consuming, complex and isolated.

[DOT](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) is a text based representation of graphs which is a key part of the solution.

With DOT you describe the graph/diagram in text which is then transformed (by tools like [Graphwiz](http://www.graphviz.org/) or [vis.js](http://visjs.org/network_examples.html)) into a diagram.

Here is an example of DOT Language:

``` 
digraph G {
     size="2";     
     a [label="Foo"];     
     b [shape=box];     
     a -> b -> c [color=blue]
     b -> d [style=dotted];  
}
 ```

 Which looks like this when rendered (try this online at https://dreampuf.github.io/GraphvizOnline/)

 ![](https://user-images.githubusercontent.com/656739/46248785-ed561880-c415-11e8-8f07-6f5c83b4b03b.png)

What you have here is 'Diagrams as code' which is a major paradigm shift that very few developers and professionals have been able to make. 

As you will see below, text-based representation of reality using diagrams is an area that still needs a lot of innovation and usage, I strongly recommend you to get your head around who to use DOT language for diagraming since that will give you a strong competitive advantage (specially if you are able to automate some/all of its creation)


#### Why we need diagrams

One of the key challenges that exist when working in a team with multiple stake-holders and areas of expertise, is the alignment of what are the objectives and what will be delivered. Don't underestimate how hard this is. Without a graphical representation of the plan and reality it is very hard to have that alignment

Diagrams provide an [lingua franca](https://en.wikipedia.org/wiki/Lingua_franca) where it becomes much easier to syncronise expectations and make sure that every stake holder understands the diagram's reality and action plan

Actually, what we really need are [Maps](https://medium.com/wardleymaps), but if we can start with Graphs that would be a great start

### Version control graphs using Git

A key advantage of storing diagram data in a text format is that you are then able to use git to stored it and sites like GitHub to edit it.

The benefits are tremendous since now you are able to start treating your diagrams as you do your code, namely code/diagram reviews, branches for new features (to be merged when code is merged/live), use tags to mark releases/sprints, easily collaborate between multiple team members, and being able to do a diff between versions (i.e. see what changed between versions)

### Diff graphs and animate evolution

Your brain is really good at understanding patterns, but due to the highly efficient and hyperlinked way our brains works, what we think we remember from a diagram reviewed a couple days (or weeks) ago sometimes is not even a good representation of reality. This becomes a major problem when reviewing the diagrams for a 2nd, 3rd or nth time, since unless we are presented with 'what changed' since the last review, our brains really struggle to understand the meaning of those changes.

One of the nice side effects of storing diagram data in a text based format, is that diffing versions becomes possible (i.e. it is possible to create text and graphical representations of those changes). 

Diffing Diagrams (and making it as easy and smooth process), is is another area that we need quite a bit of innovation and a good area for you to become a player.

#### Why Visio doesn't scale

But why not use [Visio](https://en.wikipedia.org/wiki/Microsoft_Visio), or one of its online/offline variations?

Visio diagrams are today the industry standard for creating detailed technical and workflow diagrams, and the reality is that Visio diagrams can look really good (specially if its creator has good design sense and good taste).

The irony is that Visio's main features are actually its main drawbacks. Due to the fact that Visio allows the creation of very detailed diagrams means that it is:

 - **very time consuming** - it is normal to take hours (if not days) to create an detailed diagrams 
 - **created from somebody's interpretation of reality** - the author of the Visio diagram will have a massive impact on the design, taxonomies, conventions and depth of detail, which means that it's personal bias and agenda will be reflected in the diagram
 - **a work of art** - yes some diagrams look really beautiful, but the point of a diagram is to help with data communication,   understanding and collaboration. The point should be to empower decisions, not to look good
 - **not created from dynamic data** - all elements in the Visio diagram are manually added, which means that once the original data/scenario/architecture changes, the diagram will be out-of-data
 - **layout is pixel based** - which means that moving anything can become really hard because the actually location of a particular element is 'hard-coded' to a particular location in the page (i.e. its pixel). This is one of the reasons why changes are so hard, since it is easy to hit clashes between elements, when moving/adding new elements
 - **locked to a particular design convention** - due to the fact that the design is hard-coded and the creator of the Visio diagram has enormous scope for applying its creative interpretation to the diagram's data, what ever convention the author used, becomes the one that everybody has to use. This becomes a massive issue when it is required to see the diagram's data from differnt points of view or different levels of abstraction 
 - **very easy to mix abstraction layers** - another common problem with Visio is the used of multiple abstractions in the same diagram (for example mixing network flows, with application flows, with user journey flows). This tends to be an side effect of not being able to reuse part of the diagram in new diagrams for example focused on a particular use-case or user-journey.
 - **stored in binary or xml format (very hard to diff)** - not only these files are hard/impossible to diff, some of the file formats are proprietary (i.e. not open) and sometimes on online services the data is not even available.
 - **mixes data and design in same file** - to effectively diff data it is key to store the data and the design in different files. Not only this will make the version diffing possible, it allows the creation of standard design templates (which will create a consistency of design, making it easier to consume)
 - **very hard to update** - once a diagram grows to a particular size, simple changes, can required considerate time (and big changes even more). This creates situations where the diagram authors become 'alergic' to making changes (since they might not have the time required to make the changes)
 - **not an accurate representation of reality** - due to the fact that these diagrams are hard to update, even in the unlikely situation that the diagrams were accurate on day 0 (i.e. when they were completed for the first time), due to the natural rate of change in development and systems, it is inevitable that the diagrams will start to go out of date. Them, unless they are significant efforts put in maintaining those diagrams, they stop being sources of truth (and valuable for teams)
 - **not used everyday (by developers, architects or managers)** - usually the reason for all the properties listed above, is the simple fact that the diagrams created are not part of the multiple day-to-day conversations and decisions that occur between the multiple players
 - **they are usually not maps** - finally the worse part of 99% of the diagrams out there is that that are not Maps. Although diagrams tend to be visual, have context (i.e. specific to purpose / perspective) and are mode of components , they miss the key [mapping properties](http://wardleypedia.org/mediawiki/index.php/Wardley_Mapping) of: anchor, position (relative to anchor) and consistency of movement.

#### Not being able to control the layout is a feature

When you stat using text based diagraming tools (like DOT) one of the behaviors that will drive you crazy is the fact that you can't control the diagram layout (in the same way you do in Visio). Text based diagrams are dynamically rendered based on a set of predefined strategies. This means that the exact location of components will vary with most changes (note that some engines allow the fixation of components, which allows the creation of anchors and special areas).

This limitation is actually the best feature of text base diagrams. It is only when you stop caring about the exact layout that you realise that it doesn't really matter, since as long as you understand the diagram's context, they are easy to read and consume.

The other positive site effect of this lack of control, is the fact that changes (big or small) are easy to make, which means that it is easy to keep the diagrams up-to-date.

#### Automatic generation of graphs for code

So what is the solution to make diagrams scale so that they are:

 - a correct representation of reality
 - easy to create and maintain
 - able to provide multiple views from the same data
 - able to separate code and data 
 - easy to diff (between versions)

The solution is to auto-generate the diagrams (from source-code, config files, data-analysis, logs, or other data sources). Only then will we have something that can be maintained and correctly represents reality.

But doesn't this mean that we need a way to parse the (for example) config files, understand its structure and find a way to create information from it?

Yes

And what is wrong with being able to do that ?

What is crazy is to make decisions based on shadows of reality (or even worse, what somebody thinks reality is)

#### Infrastructure as Code 

One of the good things of codifying the infrastructure (vs clicking on things or running a bunch of scripts), is that it provides the opportunity to use the config/recipe files to generate diagrams that represent what they create.

A good example is the visualization of the relationships between multiple running Docker containers. In docker based environments, when this visualization of running containers is not available (in quasi real-time), eventually it becomes really hard to understand what is really going on, and system failures caused by cascading set of events start to become a common occurrence.

#### Use Threat Models as a way to create diagrams

[Threat Models](https://en.wikipedia.org/wiki/Threat_model) are a technique used by application security professionals to map out the security implications of a particular design. There are multiple schools of though on how to do threat models, I like the simple one where we create a set of architecture/flow diagrams and map a number of threads to it: Authentication, Authorization, Data Validation, Secrets Management, Resilience and Privacy. To scale the creation of the Threat Models needs to be done by Security Champions (which are usually developers embedded in a particular team)

The trick here is to use Threat Models as a way to create diagrams that not only represent reality, but are kept up-to-date (by the Security Champion)

And why do teams find the time to do Threat Models, when they struggle to get management/business-buy-in for doing documentation?

Because doing documentation feels like a 'low/medium priority' task (when compared with the latest feature requested by the business), which is easy to keep pushing to one of the 'next sprints'. This is a typical technical debt problem, where the real impact of not doing something will only happen in the future (usually when the ones making the current decisions are not there any more)

But NOT doing a Threat Model, means that that team (namely the business and technical owners) have taken an active step to 'Not understand the security implications of the current design or latest set of changes'_. This is a much higher risk and one that if you have a mature risk based workflow, will create a set of vulnerabilities and risks for those technical and management owners to accept.

#### The crazy idea that in Agile you don't need documentation

_To go fast go alone ... To go far go in a team .... To go fast and far, you need a team and real-time understanding/visualization of what is being created/executed_

One of the very dangerous ideas that started to happen in Agile teams that were able to deploy fast to production, was the idea that _you don't need to document and diagrams things_ (since that will just slow things down).

This is a crazy idea and very short-sighted!

The quality of the test code and ability to create diagrams from what actually exists, are critical factors in creating highly productive, effective and rewarding environments.


#### People, Process and Technology

The biggest challenge in adopting (for example) DOT Language is are the _People_ and _Process_ part. Although there still are some limitations in the _Technology_ part (DOT diagrams needs to have better support for icons, and better control of the positioning/anchor of key components), what I find is the hardest part is for the _People_ to do the paradigm shifts mentioned in this chapter. Once they do, the _Processes_ will evolve around the existing tech stack (for example the one I use is: DOT Language, Git, GitHub, Vis.js and  Hugo)

#### Evolution of Diagrams into Maps

What is very frustrating is that in most development teams, we are still at the _'Why do we need up-to-date diagrams?' phase. 

Where the question that should be asked is _'How can we make our diagrams every better and more valuable?'

And the answer is Maps, which are diagrams with the following properties

- are visual
- have context (i.e. specific to purpose / perspective) 
- are mode of components
- have at least one anchor
- have a position (relative to anchor) 
- have a consistency of movement

For a great introduction to this kind of maps see [Wardley Mapping](http://wardleypedia.org/mediawiki/index.php/Wardley_Mapping), which was created by Simon Wardley who is writing a [book about it at the Medium Platorm](https://medium.com/wardleymaps)

#### Explore Vis.js Javascript engine

If you are looking for a great javascript-based DOT language visualization engine, then _[vis.js network](http://visjs.org/docs/network/)_ is the one I recommend you spend a lot of time learning and customizing (see my [neovis fork](https://github.com/pbx-gs/neovis.js) for an example of what those customization can look like)

#### Mermaid and WebSequenceDiagrams.com

Another good example of diagram as code is the open source [Mermaid](https://mermaidjs.github.io/) tool, which is designed to help with chart generation.

Here is what a Sequence Diagram code looks like in Mermaid 

```
sequenceDiagram
    participant Alice
    participant Bob
    Alice->John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
```

Which looks like this when rendered:

![](https://user-images.githubusercontent.com/656739/46255423-a22f1a80-c494-11e8-8eb3-5c9c992e162c.png)

An alternative is the propriatary https://www.websequencediagrams.com service, which more feature rich that mermaid and has a nicer design (the free version is already very usable and practical):

```
title Authentication Sequence

Alice->Bob: Authentication Request
note right of Bob: Bob thinks about it
Bob->Alice: Authentication Response
```

Will look like this

![](https://user-images.githubusercontent.com/656739/46255585-abb98200-c496-11e8-93a7-7ac3abeaf535.png)


The [Diagram in R](http://rich-iannone.github.io/DiagrammeR/index.html) integration page contains a great video of DOT in action:

![](https://user-images.githubusercontent.com/656739/46255638-41551180-c497-11e8-88b8-26ab35aacedf.png)

Btw, if you have not learned how to code in [R](https://en.wikipedia.org/wiki/R_(programming_language)), you definitely should, since it is a great way to manipulate and visualise data. 
