---
title: Chaos Engineering
status: draft
---


**Topics to cover and ideas**

 - Great concept (from 2017)
 - Security has been doing this for ages
 - Add references to site and best posts
 - focus on resilient systems
 - need to understand and visualize what is going on
    - a massive problem with micro-services (and any services/monolith) based application is vibility into what is going on (and even just getting good graphs is the first step, just ask anybody who has deployed AppDynamics)
 - integrate this concept with the SRE's 'Error Budget'
 - expand on the concept of 'Steady state' (and write tests for it)
    - how we want tests to replicate it

(from Miles)
- **Chaos Engineering is Experimentation and Testing** : In part of the definition of chaos engineering it is useful to state that the technique is made up of experimentation, to explore and discover weaknesses, and testing, to validate that a known weakness is in fact overcome.
- **Chaos Engineering and Resilience Engineering** - People practicing Chaos Engineering are part of the Resilience Engineering capability of an organisation. Chaos Engineering is a key discipline for learning and validating a system's robustness in the face of turbulent conditions, and it provides a pre-emptive motivation to learn and improve as part of the overall sociotechnical system's resiliency.
- **Make sure to reference the Principles of Chaos** - For me, this is the authoritative definition for Chaos Engineering: http://principlesofchaos.org/ I'd also argue any sufficiently complex system, distributed or not, can gain from pre-emptively exploring and discovering sociotechnical system weaknesses.
- **Game Days and Automated Chaos Experiments part of a Chaos Engineers toolbox** - Game Days are manually executed chaos experiments. Automated Chaos Experiments and Tests are where you'd like to execute your experiments and tests continuously (Continuous Chaos) and so automation enables that without distracting everyone from their other valuable work.
- **Chaos Engineering and the overall Software Development Lifecycle** - Chaos experimentation can begin even before anything has arrived in production by exploring the potential for system weaknesses in a solution, mentally or actually running Game Day experiments. It is a great architecture, design and organisational exploration technique to find weaknesses early.
- **Continuous Chaos (Engineering)** - Chaos experimentation and testing is often executed as frequently as possible as the turbulent conditions of the target (production) system are often sufficiently dynamic that weaknesses can surface and be discovered by a chaos experiment at any time. This also informs the relationship between CI/CD and continuous chaos. While there is value in adding chaos testing and experimentation into the CI/CD pipeline, "delivery" is only one cause of conditions that you might want to trigger chaos experiments to explore. Traffic changes, infrastructure failure, platform conditions; the system is under the stress of transient turbulent conditions between releases and so often it is desirable to execute chaos on an entirely different cadence to delivery, often more frequently, to explore these interim conditions as well.
- **Chaos Engineering and Observability** - Chaos Engineering frequently encourages better system observability, and takes advantage of that greater observability, so the two techniques are mutual forcing-factors for improvement.


**references**:

 - [The Language of Chaos Experiments in Chaos Toolkit](https://medium.com/chaos-toolkit/the-language-of-chaos-experiments-in-chaos-toolkit-bd55a5c04057)
 - https://github.com/chaostoolkit , http://chaostoolkit.org/ , http://chaostoolkit.org/faq/
 - http://www.oreilly.com/webops-perf/free/chaos-engineering.csp book
 - [Chaos Engineering: Why the Label Matters](https://medium.com/russmiles/chaos-engineering-why-the-label-matters-35ddbb974fa5)
 - [Chaos Engineering for the Business](https://medium.com/russmiles/chaos-engineering-for-the-business-17b723f26361) introduces great concept "Limited scope, continuous, disaster recovery"
 - [Are you ready for Chaos Engineering?](https://medium.com/russmiles/are-you-ready-for-chaos-engineering-59b859091281)
 - [Chaos engineering paradigm](https://www.codibly.com/2017/05/chaos-engineering-paradigm/)
 - https://github.com/Netflix/chaosmonkey
 - [From resilient to antifragile - Chaos Engineering Primer DevSecCon](https://www.slideshare.net/sbodiu/from-resilient-to-antifragile-chaos-engineering-primer-devseccon)