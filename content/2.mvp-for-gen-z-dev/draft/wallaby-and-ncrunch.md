---
title: Wallaby and NCrunch
status: draft
what  : Unit Testing execution tool that will change how you code
task  : Install the evaluation version are give it a good test drive
price : Free eval for 30 days, $100 USD for personal license
---

[WallabyJS](https://wallabyjs.com/) is a an _Integrated Continuous Testing Tool for JavaScript_ that represents the best TDD (Test Driven Development) environment that I've seen, because it allows the creation of a highly productive and efficient development workflow. [NCrunch](https://www.ncrunch.net/) is very similar for .NET and all the concepts bellow apply (my experience is that wallaby is a bit faster). Unfortunately there isn't an equivalent for the other languages (some IDEs do have the ability to automatically execute tests, but they only have subset of the features I describe below and the development experience is not the same)

WallabyJS is an extension to the most popular IDEs (WebStorm, IntelliJ IDEA, PhpStorm, Rider, RubyMine, PyCharm, Visual Studio , Atom Text Editor, Sublime Text) that enables the execution of Unit Tests immediately. The loop from detection to 'test execution completion', usually takes less than 1 sec, which give it a feel of real-time test execution.

The proof of a good piece of technology is when it dramatically improves the productivity of its users by changing how they behave and operate (while making them awesome). WallabyJS and NCrunch are such technologies and you as a developer need to understand why.

### All developers test their code

One key concept that I always try to make to developers is that they are already testing their code changes. For example when developers make a change in a particular web page or back-end service, they will fire up a browser or PostMan and click a number of times until their reach the location where the change they made can be seen in action.

The problem is that in most cases the ways they test their changes: 
 
 - Are highly inefficient
 - Can take many seconds or event minutes to test one change
 - Are non repeatable
 - Are limited in their scope (i.e. not testing most/all real-world moving parts affected by the changes)
 - Tends to focus on a very narrow set of use-cases
 - Loses the history of the multiple test scenario tested
 - Makes the developer switch context in their mind
 - Does not show the code coverage (in the IDE) of the changes made

The reality is that developing using workflows that don't have the capabilities enabled by WallabyJS is highly expensive, inefficient, unproductive, slow, and frustrating for everybody involved (namely the developers who pay the price of that inefficiency every time they code)

### Key WallabyJS features

As with everything, the key is in the People, Process and Technology ecosystem. WallabyJS is a _Technology_ that allows a massive paradigm shift in the _People_ involved, that leads to massive changes in the _Process_ of developing applications.

Here are the key features that WallabyJS has, and that I wished every IDE had by default:

 - **Automatic execution of tests** - as soon as you make a change to the code (or save it), the tests runs automatically (WallabyJS is so fast, that some tests actually execute in between your key stokes)
 - **Execution of only affected tests** - part of making the automatic execution of tests scale is the ability to only execute the tests that where changed. The ability to detect this also means that there is no need to keep configuring the test runner
 - **Execution of only tests affeced by code changes** - this feature answers the question _"what is the impact of the code change I just made"_. Using code coverage, it is possible to know the tests that are currently able to hit the lines that where changed (and then only execute those). This is such a simple concept, but makes a massive difference, since the alternative is to run all tests or to try to manually find the tests that can be executed.
 - **Code coverage in the IDE after execution** - Another feature highly underestimated is the power of seeing in the IDE the status of the test's execution. Not only this clearly shows the areas of the code that are currently not being reached, the way WallabyJS (and NCrunch) do it is very cleaver, since they show the paths of pass and fail (i.e. you see in green the lines that were executed by passing tests, and in red the lines affected by failed tests). This allows for really powerful workflows, including a massive reduction of the need to 'debug' code using a 'debugger' (i.e. in many projects that I was involved in, after a while, we realized that me and development team stopped using the debugger when coding! Wallaby or NCrunch gave us enough visibility to understand where the bug was (this allowed us to not have to deal with all the inefficient of having to maintain a salad of breakpoints and hundreds of 'Step Into' or 'Step Over' clicks)
- **Feedback of values in IDE** - A nice little feature of WallabyJS is that it has a number of ways to get feedback from the tests being executed. This goes from simple `console.log` outputs to  expressions and even variable transformations, that are showed directly in the IDE and in context.
- **Crazy fast execution** - The speed of execution of WallabyJS cannot be overestimated, in fact I thought that NCrunch was fast, but after using WallabyJS for a while, NCrunch felt really slow, and using normal test runners just kills my brain. We have quite a lot of data on how page speed affects users experience (see _[Why Performance Maters](https://developers.google.com/web/fundamentals/performance/why-performance-matters/)_) and it is the same for test execution and the developer's brain. When tests execute automatically and in less than a second, there is a flow and effectiveness that occurs, which dramatically improves productivity and focus.

### Aim for 100% code coverage

My view of code coverage is that if you make a change in the code and a test didn't break, you are making random changes (where you don't really understand the side effects of your changes). 

Even when you are doing refactoring, you should break a number of tests until you arrive back a test passing state. 

This means that you need to aim for 100% code coverage since that means that all of your code is covered by tests. I know that this high-code-coverage percentage can be gamed, and there are many horror stories on companies that abused this metric (which always are indicators of bigger problems within the development culture and management). 

If fact, what you want is much more than code coverage. What you want is to make sure that the tests that are executed,  correctly represent your understanding of what the code changed is doing. 

This means that the question is not _"When I made this change, did a test break?"_  but it should be instead _"When I made this change, did the tests that failed represent my understanding of the change I made"_. 

The bottom line is that if you make changes to parts of your code that are not reflected in tests, then how do you know that your changes/fixes worked as expected?

The only way to achieve this level of code coverage is to expose the developer to real-time code-coverage in the IDE (i.e. the developer is able to see exactly what lines and code have coverage, and even more interesting, which ones have been affected by the code changes)

### Wallaby represents the real TDD

One of the unfortunate side-effects of the horror stories of high code coverage exercises (namely the ones that created massive white-elephants that were completely usable and very expensive to maintain), is the allergic reaction that TDD (Test Driven Development) can sometimes have today.

What ended up happening is that everybody agrees that TDD is very important, that TDD is should be used by all developers, that TDD is an important hiring and candidate selection process, but when we look at where TDD is actually used we tend to see that it happens on low level 'pure' Unit Tests, and code coverages of 80%+ are seen as a success. 

Part of the problem is how TDD got into the bad idea that to do TDD is to: 

1. Start with a passing state
2. Write a failed test with the smallest possible feature
3. make code change that makes that test pass
4. back to 1 until the function does what it is supposed to do

The problem is that this is only useful and relevant in a couple of the TDD scenarios.

The way I do TDD is 

1. Start with a passing state
2. Make one of more changes (in the code or test)
3. Fix the code or tests so that we are back into the passing state
4. Back to 1 until the function does what it is supposed to do

Although the 1st and last steps are the same, the middle bit is very important. I like to view it as _I'm pair programming with myself_, where I loop back and forward from code and tests. What matters is that the code changes are made in the location that matters at that moment in time. Also important is that I use this workflow for everything, from tests that affect a stand alone function (traditional called an _Unit Test_) to tests that require quite a bit of code to be executed in order to really test the changes (traditionally called _Integration Tests_). For me a _Test_ is the confirmation that a particular behavior exists in a particular target (which can be a function, an web service, an website, an CI pipeline, an Docker container, an Cloud setup, etc..)

A good sign that TDD has lost is mojo is how the concept of code coverage and its actually coverage are mapped to the team's deliverables or OKRs (Objectives and Key Results).

I keep trying to find a better name for the workflow that WallabyJs enables, but TDD still feels like the correct terms, since when I code using Wallaby I am really doing Test Driven Development. 

FDD (Feedback Driven Development) is a close alternately, but TDD is still the one I like the most 


### Test code is as important as production code

I will argue that focusing on the quality of your test code is as important as focusing on the quality of the code that you run in production.

Why? because the more effective and productive your test code and test environment is, the better your production code will be. But the opposite is not true (i.e. the better your production code is, the better your test code is).

If your team doesn't not have the same amount of care and craftsmanship with test code as they have with production code (including testing the CI pipeline), then you will never achieve the speeds and quality of development that are required.

Part of the problem seems to be the horror stories of big and cumbersome test environments that actually slowed teams down (a couple minutes code changes required hours of test changes). This is a symptom of badly engineered test environments and lack of time spending on improving the test infrastructure and effectiveness.

As a developer, your test environment (and executing workflow) is one of the most important capabilities that you need to work on (and improve). Just like successful athletes pay a massive amount of energy and focus in their supporting equipment, you as a developer need to make sure that the code that helps you to write good production code, is as effective and robust as possible.

### You have to try it to believe it

As with everything, the best way to learn is to experience it, so download one of the Open Source editors (like Atom or VS Code), install the Evaluation version of WallabyJS and give it a good test drive.

Try it in some of the apps that you are coding, or write something new. What is important is that you experience the power of the real-time test execution.

A good place for you to start is with using WallabyJS to understand how an API works. One of my patterns when learning how to use a new API is to write tests that invoke its capabilities. Not only this allows me to gain a much better understanding of how they work, the tests I leave behind represent my understanding of that API and more importantly how I expect that API to behave (this is very important to pick you future bugs caused by modifications in APIs behaviors caused by upgrades or security fixes)

When learning how to use WallabyJS you are exploring the concept Bret Victor mentions in his [Inventing on principle](https://vimeo.com/36579366) presentation which is the 'The need for inventors to be close to what they create and have quick feedback'


### Why is wallabyJS more widely used 

For me, once I saw and exprienced NCrunch and then WallabyJS I knew that I would never be able to code in .Net or Javascript with those tools. 

But the question that really puzzles me is why its adoption is still quite low. Why aren't more developers using it and why aren't they demanding the IDE developers to add those features. This is one of the reasons why IDE support for these workflows is so low, there isn't enough market pressure.

First I think there is a general lack of investment in tools for developers, where in some companies that is seen as a cost, instead of a investment.

But event in companies what are ok with spending on developers tools (and wallaby costs $100 per named developer or $240 for a company license) I still don't see developers asking for those licenses?

My only logical explanation is the natural resistance to change, an lack of understanding of the power of these kind of testing environments/workflows and a lack of time to make WallabyJS work in the current application. 

Usually the argument is that _'It sounds good but we are too busy to improve the test environment'_, which is a self fulfilling tragedy since until the test environment is improved, everybody is always going to be busy and reactive.

As a new developer, this blind spot is a massive opportunity for you. If you are able to make these paradigm changes and behave in a real TDD (Test Driven Development way)

### We need an Wallaby for the Cloud

The tragedy of the lack of focus in making technology easy to test (in an WallabyJS-like workflow) is that we are not adding those capabilities to the new tech stacks

For example who is writing tests for their 'Infrastructure as Code' scripts? How do we know that this code (for example used to setup an cloud environment) is actually working as expected?

For example who is writing tests for Serverless functions, for example Lambdas? I don't mean tests that run locally, I mean tests that actually run on the Serverless environment?

What is really nice about making the paradigm shifts mentioned in the chapter, is that your brain will refuse to program any other way. So when recently I had to write some Lambda functions in Python, after realising that the maturity of the Lambda TDD environment was really low, I spend a bit of time creating an environment where using the AWS `boto3`'s API (which wraps most AWS capabilites in easy to use Python functions) I was able to create an environment in PyCharm where I could execute lambdas (written locally) in AWS  in less than 1 sec. Since PyCharm has a feature to auto execute the last test after a couple seconds of a code change, I was able to create an workflow where 2 seconds after making a code change, the affected Lambda was executed in AWS (with execution times under 1 second). Ok it is not as smooth as wallabyJS and I don't get code coverage, but it is much better than anything else I saw (from the tools that created local simulated AWS Lambda environments in Docker, to tools like Serverless that used CloudFormation to deploy the Lambdas and took almost 1 minute to run)

### The problem of switching context

Part of the reason WallabyJS-Driven-Development makes such a difference, is because it prevents your brain from doing Context Switching.

Our brains are not very good at switching context, which is why even a couple seconds interruption can be so damaging. 

When we program, what we are doing is creating in our brains a whole set of model models about the problem/issue we are addressing. This is why sometimes we can be super productive, and other times, we just can't make it work. This is key in programing since the impact of bad/inefficient code can be enormous. Sometimes it's much better not to code, than to write code that will cause so many side-effects at later stage, that those code changes actually had a negative value (i.e. like when somebody is trying to help, but they are actually 'anti-help').

This is also why it is very important to have un-interrupted periods of time for coding (ideally blocks of 2 or 4 hours), since it takes a while to build these mental models and gain speed.

When we code in an non WallabyJS-Driven-Development environnement, what happens is that we are forced to switch context every time we want to test the code changes. Even if that is a couple seconds where  mouse clicks or keyboard inputs, the compound effect of that interruption is enormous. This is way worse when the time that it takes to test the code changes is more than 10 seconds or even minutes (the impact of productivity is enormous)

With WallabyJS-Driven-Development environnement what happens is that you get into a groove, and you get just about 100% focus on the code changes that you are doing, and start to use the visual feedback that you get as part of your development. You need to experience this to understand but, when you get this right, this is what being the 'coding zone' really feels like, and the productivity that you achieve is really something incredible.

One question I'm asked quite a lot is _How can I code and learn so fast_. The answer is in how I code and the time I spend in creating productive environments that allow me to code in the 'Zone'.

As a developer if you can behave like this, you will have a massive competitive advantage in the marketplace and when applying for new jobs. It is very common these days to ask job applicants to write some tests during an job interview. When I review those applications, the first thing I look at is the test workflow and environment that they create.



### One to watch: LightTable 

As a final idea, If I was you, I would spend some time with the experimental LightTable Open Source IDE (ideally even becoming a contributor)

I need to give this tool a better test drive since it has implemented a number of the features presented in Bret Victor's "Inventing in Principle", namely the real time feedback of code changes and showing the values in the IDE. 

One area I would like to see more example is how LightTable can be to applied to testing, which is a good area for you to focus your research on :)

