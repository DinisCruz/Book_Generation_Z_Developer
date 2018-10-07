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

The conversion from source code to an AST is a very common pattern when processing structured data: _"Create parser that converts raw data into an graphical representation that can then be consumed by an rendering engine"_. Which is basically the process of converting raw data into in strongly typed in-memory objects that can be manipulated programmatically.

Here is a another example from the really cool online tool [](https://astexplorer.net/):

![](https://user-images.githubusercontent.com/656739/46580312-4c212080-ca1a-11e8-8426-26335bd7d9d9.png)

Note how in the image above the [DOT](https://github.com/DinisCruz/Book_Generation_Z_Developer/blob/master/content/2.mvp-for-gen-z-dev/content/dot-language.md) language raw text was converted into a object tree (which can also be consumed/saved as a json file).

As a developer if you are able to 'see code or raw data as a graph' you will have made an amazing paradigm shift which will help you tremendously across your carer.

For example I have used ASTs and custom parsers to:

 - write tests that check for what is actually happening in the code (easy when you have access to an object model of the code)
 - consume log data which normal 'regex' based parsers struggled to understand
 - perform static analysis on code written in custom languages
 - transform data dumps into in-memory objects (than can then be easily transformed and filtered)
 - perform custom code refactoring (for example to automatically fix security issues in code)
 - create transformed files with slices of multiple source code files (which I called MethodStreams)

 ### Refactoring and write code from AST

 When building a parser for a particular data source, a key milestone is the round-trip capability of being able to go from the AST back to the original text (with no data loss). 
 
 This is exactly how [code refactoring](https://en.wikipedia.org/wiki/Code_refactoring) in IDEs works (for example when you rename a variable and all instances of that variable are renamed).

 Here is how this round-trip works:
 
 1. start with _file A_ (i.e. the source code)
 2. create the AST of _file A_
 3. create _file B_ as transformation from the AST
 4. _file A_ is equal to _file B_ (byte by byte)

When this is possible, it becomes easy to change code programmatically, since we will be manipulating strongly typed objects without worrying about the creation of syntactic correct source code (which is now a transformation from the AST).

### Writing tests using ASTs objects

Once you start to see your source code (or data that you consume) as _'only an AST parser away from being objects you can manipulate'_, a whole word of opportunities and capabilities will open up for you. 

A good example is how to detect a particular pattern in the source code that you want to make sure occurs in a large number of files, lets say for example that you want to: _"make sure that a particular Authorization (or data validation) method is called on every exposed web services method"_?

This is not a trivial problem, since unless you are able to programmatically write a test that checks for this call, your only options are:

1. write a 'standard' that documents that requirement and make sure that all developers read it 
2. manually check if the requirement was correctly executed
3. try to check it with 'regex' based tools, and realise that it is really hard to get good results from it
4. rely of QA tests (or Security reviews) to pick up any inconsistencies

But, when you have the capability to write tests that check for this requirement, here is what happens:

1. write tests with requirement with the 'standard' being documented via the test's comments (that can be parsed and showed in multiple formats)
2. run those tests as part of the local (or CI) build
3. by having a failed test, the developers will know ASAP once an issue has been discovered, and can fix it



---

**Topics to cover and ideas**

 - source code is not the best medium to consume code
    - explain how O2Platform's Method Streams work and how they are a lot more effective
    - what you want to see is all the code relevant to the path you are looking at
 - we also need the equivalent of AST and static complilation for all the 'coding' that exists in all the cloud environments and between services (i.e. we need a DSL)
    - for example for AWS lambdas and how they behave

