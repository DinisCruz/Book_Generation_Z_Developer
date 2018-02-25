---
title : Docker
status: content
weight : 20
---

As a developer it is critical that you understand how docker works and how it became so successful and widely used.

The first time I saw and used docker, I was massively impressed by its simplicity and its potential to change how not only applications are deployed, but how applications are developed and sandboxed.

To understand Docker and its power, the first concept to master is how docker is a _"process that exposes a multi-layered file system as an fully isolated OS"_

It is easy to see Docker as just a faster VM environment or a faster Vagrant (which is a way to programmatically create VMs). I've seen companies that because they had automated VM deployments to such an extent (i.e. they become really good at automating the creation and deployment of multi-gigabyte VMs) they dismissed Docker as just another IT fad.

The problem is that Docker is much more than just a faster VM. Btw, by fast, I mean super-fast. normal VMs book in minutes, Docker can give you a fully working Ubuntu box with Node installed in sub second start time.

Docker starts in second(s) because it is just a process. The magic sauce is created by:

1. a number of linux kernel technologies that are able create a sandboxed environment for that process (for files and network access)
2. a layered (i.e. docker images) file system, where each layer contains a diff with the previous layer.This is a powerful graph db, where each file location is dynamically calculated when you are inside the docker image.

From a security poing of view, Docker has massive advantages. Finally it is possible to run 3rd party code in isolated (i.e. sandboxed) environments, where any malicious code running inside those docker containers, would not have access to the current host user's data. This is actually the future of desktop and server-side apps. where easy external (or even missing critical) service/code is executed inside containers.


--

**Topics to cover and ideas**


 - _What is happening is that each layer is immutable, and when a file is changed inside docker it is either a) lost when the docker image stops or b) saved a new docker image_
    - rewrite paragraph (above) that tries to explain how docker file system works and how new images are created)

 - why docker image development environment is so powerful and fast (explain the concept of images commits)
    - if you don't understand git and virtual file systems you will struggle to understand git

**Kubernetes**

 - what problem it solves
    - k8s architecutre
    - the power of coding your server environment (just a higher level of programming abstraction layers)
 - AWS Elactic container service
 - Digital Ocean Docker droplet
 - explain Kubernetes (how it come from Google's Borg)
    - this container's capability was why google grew so fast and innovated so much in the last decade
 - Docker Compose and Swarm

**Couple examples of Docker in action**

- add some technical examples of how to use docker (and how easy it is)

**Testing Docker**
    - repeatable bash scritps
    - testing of docker images and builds is still a very imature space (no good tools, IDEs and Test Runners). I played with BATS but it wasn't very good
            - we need TDD for docker development
            - big comptetitive advantage in the market place if you understand these concepts


**where to focus**

- a very good research area is the visualisation and mapping or docker environment



**references**
 - [Containerization](https://vimeo.com/49392667) - by MAYA Design
  - [Containerization: The Most Influential Invention That You've Never Heard Of](https://www.youtube.com/watch?v=F-ZskaqBshs)

  - [Trillions](https://vimeo.com/7395079) - video from MAYA Design
  - [Trillions: Thriving in the Emerging Information Ecology](https://www.amazon.co.uk/Trillions-Thriving-Emerging-Information-Ecology/dp/1118176073)