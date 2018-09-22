---
title: Assembly and Bytecode
status: content
weight: 20
---

Assembly code is a representation of what the machine code that the CPUs actually execute. It is the lowest level of abstraction that you can program.

The moment I fallen in love with programming was when (as a teenager) I executed the POKE assembly command in my ZX Spectrum, which changed a pixel on my TV screen. That was such a magical moment because I had direct control over what was happening inside the computer and screen.

[PEEK and POKE](https://en.wikipedia.org/wiki/PEEK_and_POKE) were [BASIC](https://en.wikipedia.org/wiki/BASIC) commands that allow direct memory access and manipulation (PEEK reads and POKE writes). What I was doing was to write directly to the memory location that was used to control the screen (i.e. each byte in that memory address represented a small section of the screen).

A while later I started learning how to go deeper and explored writing assembly code. In those 'pre internet' days there was very little information around and with only one book available, I actually remember manually translated assembly code into binary by hand (I didn't started with an assembler compiler). Eventually I got an assembler and did many experiments in the ZX Spectrum, the [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500) and the x86 PCs (which when compared with the Amiga's Motorola 68000 microprocessor had a much more complex memory layout).

In fact my first 'security hacks' were based around memory and disk manipulations written in assembly. They were designed to manipulate and change the behavior of the games I was playing (I think there was some cool way to get more money in SimCity)

Looking back, what I can see is that when I was writing assembly language, what I was doing was learning (in a very efficient way) about: computer architecture, memory layout, systems design, programming and much more. For example learning about hardware interrupts, TSR (Terminate and Stay Resident), and Kernel vs User-land memory, did wonders for my understanding of computer science.

These days you are more likely to code in Python, Java or .Net than assembly. But if you look under the hood, these languages are compiled into [bytecode](https://en.wikipedia.org/wiki/Bytecode) which is a normalized version of assembly. 

For example here is what `print("Hello, World!")` looks like in [python's bytecode](https://opensource.com/article/18/4/introduction-python-bytecode)

    0 LOAD_NAME                0 (print)
    2 LOAD_CONST               0 ('Hello, World!')
    4 CALL_FUNCTION            1    

Python (as with .Net and Java) is a [stack-based virtual machine](https://en.wikipedia.org/wiki/Stack_machine) which is provides a translation layer between the language and the CPU specific machine code

### Decompiling code

Bytecode is the reason why .Net and Java can be easily decompiled from an .dll or .class file. 

In .Net this can be quite spectacular since tools like [ILSpy](https://github.com/icsharpcode/ILSpy) allow the easy decompilation of non-obfuscated .Net assembly (including the ones from the Microsoft .Net Framework).

For viewing C++ and other compiled code, two great tools on windows are [ollydbg](http://www.ollydbg.de) and [Ida Pro](https://www.hex-rays.com/products/ida/)

