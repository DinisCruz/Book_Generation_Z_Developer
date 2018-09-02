---
title: TDD (Test-Driven Development)
status : draft
weight : 20
---


**Topics to cover and ideas**

 - the most coverage you get, the more changes you are happy to make, the better the code is because you have the confidence to make the hundreds of small changes that the only way to create a high quality and scalable application
 - be a craftsman
 - explain history
 - key challenges
 - why the TDD community created dogma and lost the plot
 - if you don't have 100% code coverage, what are those bits of code not covered by tests? (what happens if that code changes)
 - everything should be tested
    - history of a site that went down for hours because of a one char (pipe) change in a nginx config file


 ** bugs as features**

  - replicate bugs first (before trying to fix them)
  - link my slideshare presentation on this topic


### BDD (Behaviour-Driven Development)

**Topics to cover and ideas**

 - what is it
 - great evolution
 - where is works
    - when it works well it is amazing
 - great connection with business
 - can create bit white elaphants (like like Selenium)
    - requires quite a lot of discipline and investment to keep up to date

 - explain Gherkin language

 ### FDD (Feedback-Driven Development)

 **Topics to cover and ideas**

 - real-time feedback in IDE (REPLs)
    - this is key to learn
    - run code as you lift your fingers or press save
 - show screenshot of my typical dev environment
 - wallabyjs
    - great example of what this UI needs to be
    - incredible how it has not be copied into all IDEs (as far as I can tell only NCrunch has the same features)
 - all code changes (except refactoring) should require a test change
    - see http://pitest.org/
    - see chaos engineering
 - every developer does tests all time
    - the question is how repeatable, scalable, mesuable those tests are
    - and how much context switching occurs

 - the FDD applies to much more than just coding (see chapter on "Inventing on Principle") it is also related to how we learn

  - Power of Feedback loops