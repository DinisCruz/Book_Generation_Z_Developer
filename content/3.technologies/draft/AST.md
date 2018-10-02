---
title : AST (Abstract Syntax Tree)
status: draft
weight: 100
---

[AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (Abstract Syntax Tree) is a graph representation of source code used by compilers to understand what is going on.

For example, the AST of this code sample:
```
while b ≠ 0
    if a > b
       a := a − b
    else
        b := b − a
    return a
```
Will look like this:

![](images/800px-Abstract_syntax_tree_for_Euclidean_algorithm.svg.png)



---

**Topics to cover and ideas**

 - Why is so important
 - How they work
    - object model of source code
    - amazing paradigm shift when one can 'see code as a graph'
 - Using AST to write tests
 - Powerful AST abstractions (specially when added the code refactoring mappings)
 - how code refactoring works
 - source code is not the best medium to consume code
    - explain how O2Platform's Method Streams work and how they are a lot more effective
    - what you want to see is all the code relevant to the path you are looking at
 - we also need the equivalent of AST and static complilation for all the 'coding' that exists in all the cloud environments and between services (i.e. we need a DSL)
    - for example for AWS lambdas and how they behave

