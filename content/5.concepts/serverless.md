---
title: Serverless
---

...

---

**Topics to cover and ideas**

 - latest industry fad, but important development
 - important to understand why is it gaining momentum
 - important to understand the limitations
 - another example of the failure of Techops to innovate
 - the path to 'Serverless'
 - How AWS Lambda changed the paradigm
    - big example of how it can work in enterprise enviroments
    - lots of powerful side applications (for example creating AWS WAF rules)
        - Writing AWS WAF rules is a skill that would get you hired! (for example dynamically blocking IPs)
 - serverless doesn't mean 'no servers'
    - of course that there is a server, just that the app abstraction goes up another level (it lots of cases it is an function)
    - this will be successfully because it is massively cost effective (story of the crazy cost reductions and performance gains from moving to a lambda based architecture)
    - when you look at how much process and memory (in aggregate) is actually used in by apps in dev, qa and production, you will see that the amount of waste and over-provisioning is huge (i.e. resources not used)
    - once we add more scalable and dynamic micro-services architectures and applications that are able to 'self-degragade' their features based on load (and other factors like security), we will have a very powerful, resilient, available and secure application environment.
    - mention kubeless
