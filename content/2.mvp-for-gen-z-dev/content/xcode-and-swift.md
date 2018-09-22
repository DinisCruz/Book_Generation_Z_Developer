---
title : Xcode and Swift
status: content
weight: 42
what  : Development environment to create iPhone of Mac applications
task  : Install Xcode and create your first Mac Application
price : Xcode requires a Mac (bought or rented)
---

If don't have a Mac computer you can ignore this chapter (or use [MacinCloud](https://www.macincloud.com) to rent one). 

With a Mac there is nothing stopping you from being hours away from your first Mac or iPhone application.

[Xcode](https://en.wikipedia.org/wiki/Xcode) is Apple's main development environment, and you can download it for free from the Apple store. Xcode contains everything you need you develop an Mac or iPhone application, namely an IDE, an Debugger and an execution Simulator (iOS, iPad and MacBooks)

[Swift](https://developer.apple.com/swift/) is the modern Open Source language developed by Apple that I highly recommend that you use. Swift dramatically simplifies the creation of applications for macOS, iOS, watchOS and tvOS.

Creating your own application is a major milestone in your programming career. You should do it even if you don't want to become an mobile developer. Not only you will learn a large number of key concepts, you will also gain an understanding of how relatively easy it is to go from an idea in your head into a deployed application.

### First application

To kickstart your development and experiments, start with step-by-step tutorials like the _[Hello World! Build Your First App in Swift](https://www.appcoda.com/learnswift/build-your-first-app.html)_ which will guide you through the code and technologies required to make it happen.

After building your first application, your next objective is to think of an use-case that will help you to do something better in your life. This is an **App for you** and the only thing that matters is that it is useful enough that you use it regularly. 

One of the key reasons why it is important at this stage that this application is only used by you (or a couple of your friends) is because that way, you can use the Xcode simulators to execute it (i.e. you don't have to release it to the AppStore). 

By using the application everyday, you will get direct feedback from what works, what doesn't what and what need improvement. Initially, try to release a new version at least once a week (or once a day). It is important to create a process for this release (ideally with as much automation as possible).

Make sure you release your application under an Open Source license like Apache 2.0 and that you share it on a GitHub repository. This will allow you to expand your user base and gain more users.

### Write tests and create a CI pipeline

Other key workflows that you need to adopt is writing tests and executing them in a CI (Continuous Integration) environment.

See [Writing Test Classes and Methods](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/04-writing_tests.html) for an integration on how to write tests in Swift. 

Once you have a number of tests written, it is time to start looking at cloud/SaaS based build solutions. [Travis](https://docs.travis-ci.com/user/languages/objective-c/) is one of my favorites, but also check out [BuddyBuild](https://www.buddybuild.com/), [AWS Device Farm](https://aws.amazon.com/device-farm/), [BrowserStack](https://www.browserstack.com/ios-testing) or [SauceLabs](https://saucelabs.com/resources/articles/ios-app-testing).

### Experiment with Machine Learning

Apple has released _Core ML 2_ which is [described in Apple's site]((https://developer.apple.com/machine-learning/)) as an _'machine learning framework used across Apple products, including Siri, Camera, and QuickType. Core ML 2 delivers blazingly fast performance with easy integration of machine learning models, enabling you to build apps with intelligent features using just a few lines of code'_.

This means that you can easily add features like _Vision_ or _Natural Language_ to your application. If you do this, make sure to write blog posts about your experiments, since I'm sure any potential employer would be very interested in reading them.

### Publish to AppStore

If you want to take this up a level, you should try to get your application published in the AppStore. This will have some costs, but they will be worth it for the learnings that you will get. 

This would also be highly impressive for any potential employer, since it will show that you were able to meet Apple's quality bar.