---
title : Backup your life
status: content
---

Backing up your code (and ideas) is one of the most important patterns that you must master. Your current approach to backups will depend on how much have you lost, and how painful it was.

The reality is that sometime and somewhere in the future, you will lose some of your data (and ideas).

This could be something as simple as a lost laptop, or some data that was deleted by accident, or even an ransomware attack that encrypted all the files in your devices or servers. If you don't have a good strategy and habits for how you do your backups, it is just a matter of time before you have a catastrophic event.

Trust me, there are few things in life more soul destroying and demotivating, than having to re-create something again (that you were happy with and you had spent a lot of time creating). Even worse when you are not able to recreate it, which in a business environment can easily lead to you being fired for lack of due-diligence or negligence.

The solution is to think about where you classify and store your data (and ideas), so that you can come up with strategies that work in your day-to-day activities.

I'm going to provide a number of examples of how I do it, which hopefully will give you some ideas:

- **Secrets Minimisation** - From a security point of view, the less secrets you have the better (and the easier it is to backup the rest). This is where the more you embrace the idea to publish as much of your data (and ideas) as possible, the easier it is to use web based services as your backup medium.
- **Passwords** - A clearly important piece of data not to lose or disclose. My strategy is to pick formulas that I can remember and to use 2FA authentication (like SMS) as much as possible (which dramatically reduce the importance of passwords)
- **Future Self** - Part of my drive to share, is to think that one day in the future, my future self will need it. This is also why I like to Open Source as much as as possible, since it makes sure that as I move jobs, I don't have to start from scratch (for example what happened with me and the O2 Platform research or the Maturity Model tool I developed recently)
- **Git** - Git is not just a version control which you use when you want to commit to the main repo. I've seen developers that code for days before doing a commit. This is missing a massive trick. Not only during those periods between commits there is a high risk of data loss, the developer is also missing the opportunity to go back to a version created a couple hours ago (which was better than the current one). Basically there is only so much Ctrl-Z can help you. Note that you should be using git to store as much data (and ideas) as possible, since this workflow is not just for source code (another reason why I like to use markdown for content and DOT for graphs)
- **Autosave and Commits** - When using git as a data store, I always enable auto-save on the IDEs so that I never have unsaved text in memory. I then use git commits (and git staging) to really understand what has been changed (and to double check those changes before committing to the target branch). This is very empowering and liberating, since I don't really worry about losing anything
- **GitHub** - I push as much code (and ideas) on GitHub as possible. For example I have repos (some private) that act like document storage and (literally) backups. My expectation is that GitHub's backup strategy is sound and better than mine.
- **DropBox and GDocs** - Same thing for DropBox and Google Docs. I use them to store data and rely (as most companies do) on their security and backups (very important to have 2FA on these accounts and to pay for the commercial versions, which provide features like version control and much more storage)
- **Twitter** - I use twitter as my personal search engine, and use it to store all sort of links and ideas that I might be interested in the future
- **Google** - A great site effect of putting your data (and ideas) online on a public and hyperlinked location (for example on a blog or slideshare), is that Google (and [Web Archive](https://web.archive.org/) project) will eventually index it (and keep a copy for ever). I actually have used these service's caches to recover ideas that I published ages ago, on a platform or site that has since disappeared!
- **Simulate disaster** - Ask yourself, if you lost your laptop now, how painful it would be? For example at this very moment, the only thing I would lose if my laptop disappeared (or was stolen) would be the text in this chapter (and in about 30m, I wouldn't lose anything, since I will have committed this text into Git and GitHub)
- **External Drives** - For large files and VM (not really much these days) I also have a number of external drives in my house that hold it (although some of the most interesting research VMs, like the ones I was using when developing the O2 Platform, have been moved to dropbox)

 Finally, you probably noticed that every time I mentioned code I also added a note about 'ideas'. The reason is that you also need to backup your ideas so that your future self has access to them. The reality is that you will forget about those ideas and the connections that got you there. The only way to make sure they are not lost forever is to publish them into an hyperlinked medium.

 You basically need to backup your life!

 Please make sure that when (not if) some of your devices lose (or encrypt) your creations, you have a quick and efficient way to recover them.