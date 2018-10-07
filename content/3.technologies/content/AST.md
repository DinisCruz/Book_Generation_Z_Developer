---
title : AST (Abstract Syntax Tree)
status: content
weight: 40
---

[AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (Abstract Syntax Tree) is a graph representation of source code primarly used by compilers to read code and generate the target binaries.

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

![](https://raw.githubusercontent.com/DinisCruz/Book_Generation_Z_Developer/master/static/images/800px-Abstract_syntax_tree_for_Euclidean_algorithm.svg.png)


The transformation from source code to an AST, is a very common pattern when processing any type of structured data. The typical workflow is based on _"Creating a parser that converts raw data into an graph-based format, that can then be consumed by an rendering engine"_. 

This is basically the process of converting raw data into in strongly typed in-memory objects that can be manipulated programmatically.

Here is a another example from the really cool online tool [astexplorer.net](https://astexplorer.net/):

![](https://user-images.githubusercontent.com/656739/46580312-4c212080-ca1a-11e8-8426-26335bd7d9d9.png)

Note how in the image above the [DOT](https://github.com/DinisCruz/Book_Generation_Z_Developer/blob/master/content/2.mvp-for-gen-z-dev/content/dot-language.md) language raw text was converted into a object tree (which can also be consumed/saved as a json file).

As a developer if you are able to _'see code or raw data as a graph'_, you will have made an amazing paradigm shift which will help you tremendously across your carer.

For example I have used ASTs and custom parsers to:

 - write tests that check for what is actually happening in the code (easy when you have access to an object model of the code)
 - consume log data which normal 'regex' based parsers struggled to understand
 - perform static analysis on code written in custom languages
 - transform data dumps into in-memory objects (than can then be easily transformed and filtered)
 - create transformed files with slices of multiple source code files (which I called MethodStreams and CodeStreams) - See example below for what this looks like in practice
 - perform custom code refactoring (for example to automatically fix security issues in code) - See example below for what this looks like in practice
 

 ### Refactoring and write code from AST

 When building a parser for a particular data source, a key milestone is the round-trip capability, of being able to go from the AST, back to the original text (with no data loss). 
 
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

1. write a 'standard document/wiki-page' that defines that requirement, and make sure that all developers read it, understand it, and more importantly, follow it 
2. manually check if that standard/requirement was correctly implemented (on Pull Requests code reviews)
3. try to use automation with 'regex' based tools (commercial or open source), and realise that it is really hard to get good results from it
4. fallback on manual QA tests (and Security reviews) to pick up any blind-spots

But, when you have the capability to write tests that check for this requirement, here is what happens:

1. write tests that consume the code's AST to be able to very explicitly check if the standard/requirement was correctly implemented/coded 
2. via comments in the test file, the documentation can be generated from the test code (i.e. no extra step required to create documentation for this standard/requirement)
2. run those tests as part of the local build and as part of the main CI pipeline
3. by having a failed test, the developers will know ASAP once an issue has been discovered, and can fix it very quickly

This is a perfect example of how to scale architecture and security requirements, in a way that is embedded within the Software Development Lifecycle.

### We need ASTs for legacy and cloud environments 

The more your get into ASTs, the more you realise that they are abstractions layers between different layers or dimensions. More importantly they allow the manipulation of a particular layer's data in a programmatic way. 

But when you look at the current legacy and cloud environments (the part that we call 'Infrastructure as code'), what you will see are large parts of that ecosystems that today don't have AST parsers to convert their reality into programable objects.

This is a great area of research, where you would focus on creating DSLs (Domain Specific Languages) for either legacy systems or for cloud applications (pick one since each will have complete different sets of source materials). One example of the kind DSL we need is an language to describe and codify the behaviour of Lambda functions (namely the resources they need to execute, and what is the expected behaviour of the Lambda function)

### MethodStreams

One of the most powerful examples of AST manipulation I've seen, is the MethodStreams feature that I added to the [O2 Platform](http://o2platform.com). 

With this feature I was able to programmatically create a file based on the call tree of a particular method. This file contained all the source code relevant to that original method (generated from multiple files), and made a massive difference when doing code reviews.

To understand why I did this, let's start with the problem I had.

Back in 2010 I was doing a code review of an .Net application that had a million lines of code. But I was only looking at the WebServices methods, which only covered a small part of that codebase (which made sense since those were the methods exposed to the internet). I knew how to find those internet exposed methods, but in order to understand how they worked, I had to look at hundreds of files, which were the files that contained code in the execution path of those methods.

Since in the O2 Platform I already had a very strong C# parser and code refactoring support (implemented for the REPL feature), I was able to quickly write a new module that:
 
1. starting on web service method X
2. calculated all methods called from that method X
3. calculated all methods called by 2. (recursively)
4. capture the AST objects from all the methods identified by the previous steps
5. created a new file with all the objects from 4.

This new file was amazing, since it contained ONLY the code that I need to read during my security review.

But it got event better, since in this situation, I was able to add the validation RegExs (applied to all WebServices methods) to the top of the file, and add the source code of the relevant Stored Procedures at the bottom of the file.

Some of the generated files had 3k+ lines of code, which was a massive simplification of the 20+ files that contained them (which had probably 50k+ lines of code).

Here is a good example of me being able to do a better job, by having access to a wide set of capabilities and techniques (in this case the ability to programmatically manipulate source code)

This type of AST manipulation is an area of research that I highly recommend for you to focus on (which will also give you a massive toolkit for your day to day coding activities). Btw, If you go down this path, also check out the O2 Platform's **CodeStreams** which are an evolution of the **MethodStreams** technology. CodeStreams will give you a stream of all all variables that are touched by a particular source variable (what in static analysis is called _[Taint flow analysis](http://www.rroij.com/open-access/taint-flow-analysis-for-the-detection-of-bufferoverflow-attacks-.php)_ and _[Taint Checking](https://en.wikipedia.org/wiki/Taint_checking)_)

### Fixing code in real time (or at compilation time)

Another really cool example of the power of AST manipulation is the PoC I wrote in 2011 on _[Fixing/Encoding .NET code in real time (in this case Response.Write)](https://o2platform.wordpress.com/2011/11/07/fixingencoding-net-code-in-real-time-in-this-case-response-write/)_, where I show how to programmatically add a security fix to a vulnerable by design method.

Here is what the UI looked like, where the code on the left, was transformed programmatically to the code on the right (by adding the extra ```AntiXSS.HtmlEncode``` wrapper method)

![](https://user-images.githubusercontent.com/656739/46583057-a933cb00-ca48-11e8-8525-122acf63bf81.png)

Here is the source code that does the transformation and code fix (note the round-trip of code):

![image](https://user-images.githubusercontent.com/656739/46583215-fc0e8200-ca4a-11e8-94b6-c7d3a59e6d9d.png)

In 2018, the way to implement this workflow in a developer friendly way, is to automatically create a Pull Request with those extra changes.


