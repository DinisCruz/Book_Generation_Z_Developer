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

One of the key challenges that exist when working in a team with multiple stake-holders and areas of expertise, is the alignment of what are the objectives and what will be delivered. Don't underestimate how hard this is. Without a graphical representation of the plan and reality it is very hard to have that aligment

(Add image of situation were each person has a different understanding of the objective)

Actually, what we really need is Maps, but if we can start with Graphs that would be a great start



#### People, Process and Technology

....

#### Automatic generation of graphs for code

The reason why graph generation from text is so imporatnt

#### Infrastucture as Code 

### Version control graphs using Git

### Diff graphs and animate evolution

#### Why Visio doesn't scale

the fact that you can't control the diagram layout (in the same way you do in Visio) is actually a major feature

#### Why diagrams are so important

#### Evolution of Diagrams into Maps

#### Use Javascript engines 

vis.js is a great way to visualise DOT graphs

lots of innovation in this space (see for example the changes I have been working on in vis.js)


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
