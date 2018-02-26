---
title: Git
---

**Topics to cover and ideas**

 - git history: "Here is how it all started..."
    - what git means in the UK and in the US
 - "the opposite of SVN"
 - why is it called git
 - TED talk about 'git for the rest of us'
 - explain git architecture
    - graph and tree based
    - how every commit is connected to all commits (hashed together)
    - very similar to blockchain
    - the distributed nature of git
 - invented to scale
    - linux is one of the most complex and large software development project (and community) in the world
 - Git (version control) all your documents
 - Use Git as your backup
    - get a version of your code or document from a couple hours (or days) ago
 - write code that consumes Git Native objects
 - learn about git hooks namely the post commit ones
 - learn what is inside the .git folder
 - collaborate with your colleages (at school or work) using git (and GitHub/GitLab)
 - why forks and branching are so easy and fast in git (just a pointer)
 - graph based structure/database
 - in git the files don't exist on disk (the paths are dynamically generated based on the git graph)
        - "Git is fundamentally a content-addressable filesystem with a VCS user interface written on top of it" (https://git-scm.com/book/en/v1/Git-Internals)
    - this is why branching is so fast (no need to copy files to the file system)
    - best way to learn this is to clone a repo with lots of files and versions, and just checkout different branches (each with a different file structure). What is impressive in this example is how we can see major directories changing in seconds in front of us (i.e. with each branch checkout)
 - explain why git cannot store empty folders
 - by now (2018) we should have git based file systems
 - git is also great for site deployment
    - explain pattern of having a special web method that listen for github webhooks and triggers a pull (updating the site in seconds)
    - git deployment also works great for binaries (for example we one setup an git deployment workflow for .Net binaries). Upgrades and rollbacks become a simple fact of doing a git checkout
 - use Git everyday
