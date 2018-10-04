---
title  : Docker
status : content
weight : 20
what   : Containerization technology that is super fast at applications or micro-services execution
task   : Install Docker and try the ubuntu, apache, elk and gogs images 
price  : free
image  : images/logo_docker.png
---

As a developer it is critical that you understand how Docker works and how it became so successful and widely used. Docker is one of those revolutions that occur regularly in the IT industry. The right product comes at the right time and meets a number of very specific pain points that developers have.

From a practical point of view, Docker means it is very easy for you to try and use a wide variety of applications and environments. For example you can start a local, fully working instance, of the [ELK Stack](https://www.elastic.co/elk-stack) (Elastic search + Logstash + Kibana) in Docker, simply by running the `sudo docker pull sebp/elk` command (without installing anything on your host machine)

The first time I saw and used dDocker, I was massively impressed by its simplicity and its potential to change how not only applications are deployed, but how applications are developed.

To understand Docker and its power, the first concept to master is how docker is a _"process that exposes a multi-layered file system as an fully isolated OS"_

It is easy to see Docker as just a faster VM environment or a faster Vagrant (which is a way to programmatically create VMs). I've seen companies dismiss Docker as just another IT fad because they had automated VM deployments to such an extent (i.e. they become really good at automating the creation and deployment of multi-gigabyte VMs).

The problem is that Docker is much more than just a faster VM, and By fast, I mean super-fast. Normal VMs boot in minutes, Docker can give you a fully working Ubuntu box with Node installed in sub second start time (just run `docker run -it node bash` and when inside the docker container run `node -e 'console.log(20+22)'`).

Docker starts in second(s) because it is just a process. The magic sauce is created by:

1. A number of Linux kernel technologies that are able create a sandboxed environment for that process (for files and network access and other key parts of the OS)
2. A layered file system, where each layer contains a diff with the previous layer. This is a powerful graph db, where each file location is dynamically calculated when you are inside the Docker image. Basically what is happening is that each layer is immutable, and when a file is changed inside Docker it is either a) saved as new Docker image or b) lost when the Docker image stops. An final 'docker image' is just a collection of multiple images, all stacked up, one of top of the other. 
 

### Kubernetes

Once you want to:

1. Use multiple Docker images in parallel (for example an image for the web server, an image for file system and an image with a database) or 

2. Start multiple images at the same time (for example a web server behind an load balancer) 

you will need to start looking at what is called orchestration technologies.

The Docker team has published a light version of orchestration called [Docker Compose](https://docs.docker.com/compose/) and [Docker Swarm](https://docs.docker.com/engine/swarm/), but what is widely used in the production is [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)

Kubernetes (sometimes also called K8) was actually developed by Google and was inspired by [Google's Borg](https://ai.google/research/pubs/pub43438). The Borg is one of the key reasons why Google was able to scale massively in its web search and in services like GMail. Everything at Google is a container and as early as 2014 Google claimed to start [two billion](https://www.theregister.co.uk/2014/05/23/google_containerization_two_billion/) [containers per week](https://cloud.google.com/containers/)

The problem that Kubernetes solves is the codification of an application environment, plus its deployment strategy and its scalably requirements. 

This is very powerful, since it allows you to basically say: _"I want x number of pods (i.e. web servers and database) to always be available, and if they stop, make sure they are restarted (and configured accordingly)"_

It's important to understand this because you need to evolve from: creating environments by clicking on a lot of of things, to: codifying your server environment (which is just a higher level of programming abstraction layer). 

Note that you also get a similar workflow with tools like [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 

One easy way to give Kubernetes a test drive is to use [AWS EKS](https://aws.amazon.com/eks/)

### Security advantages

From a security point of view, Docker has massive advantages. 

The first is an explicit mapping of what needs to be installed and what resources (for example ports) need to be made available.

Docker also makes possible to safely run 3rd party code in isolated (i.e. sandboxed) environments, where any malicious code running inside those docker containers, would not have access to the current host user's data. This is actually the future of desktop and server-side apps where easy external (or even missing critical) service/code is executed inside containers.

### Testing and visualizing Docker

One area where we are still quite immature, as an industry, is the testing of Docker images and Kubernetes setups.

There aren't good tools, IDEs and Test Runners for Docker and kubernetes. Basically we need a TDD workflow for Docker development!

If I were you, this is definitely an area I would focus my research, whilst blogging about your efforts. 

Another great research area is the visualization and mapping of kubernetes environment (i.e. who is speaking to who, and how is that traffic authentication and authorized)

You would have big competitive advantage in the market place if you understood these concepts and had practical experience solving them.

### It all stated with physical containers

For a great introduction to Containers see MAYA Design's [Containerization](https://vimeo.com/49392667) animation, and the Wendover Productions' [Containerization: The Most Influential Invention That You've Never Heard Of](https://www.youtube.com/watch?v=F-ZskaqBshs) video

To see what is coming next see MAYA Design's [Trillions](https://vimeo.com/7395079) - video and the [Trillions: Thriving in the Emerging Information Ecology](https://www.amazon.co.uk/Trillions-Thriving-Emerging-Information-Ecology/dp/1118176073) book
