# How to Think Like a Computer Scientist & "Functional" : Learning with Python 3.10.0+

The renowned book "How to Think Like a Computer Scientist: Learning with Python 3, 3rd edition" was published on Feb. 2020 under GNU open source license.
From the first edition of this book on 2002, it has enlightened many future and now present developers, but, it has some shortages as well.
 1. The grammar used in this book is mostly Python 3.5~3.8.
 2. Only a little advanced concepts such as Iterators, Generators and Decorators.
 3. Lack of debugging chapter.

## Motivation
Though Python has been OOP language from its birth, it has gradually embraced functional programming techniques. At last, Python
 version 3.10.0 on December, 2021 has introduced a structural pattern matching, **Match Case**, which OOP developers are not so accustomed to.
If this book is complemented its current shortages, it may be one of best books for students learning Python Programming.
From December 2021, I started to revise this book to use it as a text book of a course named **Python and Functional Programming** mainly for Korean students from K5 to K12, elementary to high school students, and expect it to be used from March, 2022.
At first, the intended readers were Korean students, but, as revised and newly added chapters of this book is being written in English, not only Koreans, but anyone can enjoy the book.

## Intension

Our intention is to revise the book is to:
 1. Replace the grammar used in the book to those of Python 3.10.0+
 2. Write functional version of sample codes and exercises in the book by using new 3.10 grammar and functional libraries such as **functools**.
 3. Introduce **static typing** and explain memory architecture such as **stack and heap**.
 4. Explain some advanced concept such as Generators.
 5. Explain debugging and more detailed algorithm theory

## Readers
We assume the readers of our revised book have either (1) studied our **EMC** course made by **Team Jupeter(팀 주피터)**. , **Scratch coding** for elementary students, or (2) some learning experience on Python or other programming languages like JavaScript so on.
 Typical readers are:
 1. K4 ~ K12 students, age from 10 to 18.
 2. have learned or are learning EMC courses
 3. have some English skills.

## Youtube
This book version has accompanying lecture videos on Youtube in Korean(한국어). Not only Korean readers, but others also can freely watch the playlist using Youtube translation.
The Youtube playlist has about 200 episodes, each running time being 10 more or less minutes. For convenience, the playlist is divided into 4.

 1. Part 1: Episode 001~049 | Chapter 1 ~ 4
 2. Part 2: Episode 050~099 | Chapter 5 ~ 8
 3. Part 3: Episode 100~149 | Chapter 9 ~ 15
 4. Part 4: Episode 150~200 | Chapter 16 ~ 20 - those are newly added in this book version.

## Further Learnings

This book and accompanying lectures, titled as **Python and Functional Programming**, is a part of a larger learning courses provided by Team Jupeter(all lecture videos are in **Korean**), consist of about 7,000 Youtube video clips/episodes:
All lectures are freely available via Youtube.
 - Elementary(K1~K6) Course:
	 - EMC | Basic - Learning Scratch Coding
	 - EMC | Intermediate - Learning Scratch Coding
	 - EMC | Advanced - Learning App Inventor
 - Middle School(K7~K9):
	 - Python and Functional Programming
	 - Gleam Programming Language
 - High School(K7~K9):
	 - JS/TS Web Development - HTML, CSS, JavaScript/TypeScript, React.js, Vue.js, Svelte, Angular and Cycle.js
	 - Rust & System Programming | Intermediate
	 - Python & Data Science
	 - Elixir & Phoenix Web Development | Basic
 - College
	 - Rust & System Programming | Advanced
	 - Elixir & Phoenix Web Development | Advanced
	 - Python & Machine Learning

```mermaid
A[EMC] --> B[Python & FP]
B --> C[JS/TS Web Development] --> D[Elixir & Phoenix]
B --> E[Python & DS]--> F[Python & DS]--> G[Python & DS]--> H[Python & ML]
B --> I[Gleam] --> J[Rust | Intermediate]--> K[Rust | Advanced]
```

**Team Jupeter[팀 주피터]**