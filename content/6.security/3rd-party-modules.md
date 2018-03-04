---
title : 3rd-party-modules
status: draft
---

...

**Topics to cover and ideas**

 - package management systems (https://en.wikipedia.org/wiki/List_of_software_package_management_systems)
 - massive problem for quality and securtiy
    - add examples of npm changes that broke tons of apps
        - https://medium.freecodecamp.org/npm-package-hijacking-from-the-hijackers-perspective-af0c48ab9922
    - add story about nmp module hack (simulated)
 - this applies to both open source and proprietary code
    - at least with open source we have the ability to see that is inside the code (at least we have a change to detect and even fix (if we are paying attention))
        - and eventually as a community we will be able to add (or paid for) enough eyeballs to review it (namely the dependencies we use)
        - we can leverage the community's trust in packages (just like AVs today) and be able to quickly propagate information about bad packages
            - https://snyk.io/ is a really good commercial service in this space

 - Bitcoin mining
    - injection in 3rd party javascript library (to which read out webpages for blind or partially sighted people) hit tons of websites in the uk https://www.theregister.co.uk/2018/02/11/browsealoud_compromised_coinhive/
    - Bitcoin mining via module injection is going to dramatically change the security of 3rd party modules, since there is now a business model for attacking 3rd party modules (up until now the options to monetise those libraries was not very easy). Just to be clear, the reason more 3rd party libraries (used my millions of applications) have not been compromised is not because they were developed and deployed securely, it was just that the malicious attackers did not a good business model to exploit it (now they do)
    - there is even an interesting question if it is ok for popular open source libraries to mine bitcoins from their users.
        - for example what if JQuery did this and it took 0.1% of the user's CPU (or %1% of the QA servers) and used these funds to support the develpment of the next version (and pay for example for dedicated developers or security reviews)
        - this could solve the problem of how to fund the development of popular open source frameworks
        - maybe the browsers or servers could even support this natively (with 5% or 10% of CPU allocated for 3rd party services bitcoin mining)
        - Add story behind the developers that were thinking of doing this using the sleep function



