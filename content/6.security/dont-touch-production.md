---
title : Don't touch production
status: draft
---

...

**Topics to cover and ideas**

 - requiring access to production systems (to debug an issue or even worse, to make deployment changes) represents a failure at multiple levels
    - deployment workflow
    - logging and visualization of what is going on in the servers (and live environment)
    - ability to quickly push changes (or revert recent deployments/changes)
    - QA and test environments (that don't match production)
 - it is very important that there is an air-gap between the development workflow and the deployment/production workflow
 - having access to production systems introduces massive security risks and makes massive assets the devices uses to access that data (imagine for example that the developer's laptop had some malware which provided remote access to a malicious agent)
 - it is a sign of maturity when issues can be debugged and resolved without the developers (and security professionals) requiring access to production systems
 - same concept for having access to production data. We once had an incident where some S3 keys where compromised (S3 keys allow access to data in AWS), which belonged to an BI (Business Intelligence) team that was working on some business analysis. Upon investigation we found that that key allowed access to highly sensitive data which the BI team did not actually needed for their analysis. This is why teams (and individuals) need to be allergic to being given access to data and systems (the more you have access to, the more responsibility you have, and the more damaging a compromise of your system will be)
 - this is also related to the concept of 'Infrastructure as Code' where everything in the deployment/production environments is 'scripted' (i.e. code). 
    - 'code' in this case needs to be managed correctly (with version control, change management, code reviews, testing, etc...)
    - related to the DevOps movement
