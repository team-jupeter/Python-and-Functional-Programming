



# How to Think Like a Computer Scientist & "Functional" : Learning with Python 3.10.0+



The renowned book "How to Think Like a Computer Scientist: Learning with Python 3, 3rd edition" was published on April, 2020, under GNU open source license.

From the first edition of this book on 2002, it has enlightened many future and now present developers, but, it has a few shortages from the prospect of year 2022, at least for me. For example,

1. The grammar used in this book is mostly Python 3.5~3.8, at the time of writing the Python version is 3.10.0 which has a few significant changes.

2. Rather short of advanced concepts such as Iterators, Generators and Decorators.

3. Rather short of debugging techniques.

4. Rather short of memory architecture such as stack and heap.

5. Without static typing, which is just great both for commentary and debugging.



## Motivation

Though Python has been OOP language from its birth, it has gradually embraced functional programming techniques. At last, Python

version 3.10.0 on October, 2021 has included a structural pattern matching, **Match Case**, which OOP developers are not accustomed to.

This book is great at present, but if complemented its current shortages, it may be even more valuable for students learning Python Programming and current Python developers without functional programming experiences.

From December 1, 2021, I started to revise this book to use it as a text book of a course named **Python and Functional Programming** mainly for Korean students from K5 to K12, that is elementary to high school students, and expect it to be used from March, 2022.

At first, the intended readers were Korean students, but, as revised and newly added chapters of this book is being written in English, not only Koreans, but anyone can enjoy the book.



## Intension

As a member of Team Jupeter, my intention to revise the book is to:

1. Replace the grammar used in the book to those of Python 3.10.0+

2. Write functional version of sample codes and exercises in the book by using new Python 3.10.0 grammars and functional libraries such as **functools**.

3. Introduce **static typing** and explain memory architecture such as **stack and heap**.

4. Explain some advanced concept such as Generators.

5. Explain debugging and more detailed algorithm theory

6. Add static typing on code samples.



## Revision Process

Beside source codes of the book here, the text of each chapter is stored and edited in Google Docs. Readers can see the on-going process in real time. The revision work is expected to complete March, 2022.

-  ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) The text of the original book is colored black, and the newly added parts are differently colored like;

```diff

- text in red

+ text in green

! text in orange

# text in gray

@@ text in purple (and bold)@@

```

## Table of Contents

The order of Chapter 1 to 15 are same to the original book with some added source codes and text. Chapter 16~20 are to be newly added.

0. [Preface](https://docs.google.com/document/d/1suTMd9zY1mHZCKgfvue9tsEkqtFgtTFM-yDp_rO4UrI/edit?usp=sharing)

1. Chapter 1 | [The way of the program](https://docs.google.com/document/d/1emx2sd2ZX4Qlsp3fhBODX7fYnlH2sI9DL3NZ0TKZSeI/edit?usp=sharing)

2. Chapter 2 | [Variables, expressions and statement](https://docs.google.com/document/d/1_dPJyauAckGjqjZDZ5iTmcGuoX88Q01NJl9d0mMbME0/edit?usp=sharing)

3. Chapter 3 | [Program Flow](https://docs.google.com/document/d/1hSnjCfZKRAvUQMGxibBXUAtqvA61jxvU_PK-SvDDVpM/edit?usp=sharing)

4. Chapter 4 | [Functions](https://docs.google.com/document/d/1stNB0pfuyAPrWryxUx-w6p5UOCVyxEIwF8bcWTykGnA/edit?usp=sharing)

5. Chapter 5 | [Data Types](https://docs.google.com/document/d/1kmjh2COtgQZD5UNvllZ8zwJP6pV38WZLBFzSWQBmA-E/edit?usp=sharing)

6. Chapter 6 | [Numpy](https://docs.google.com/document/d/1KwoEFb50hxaBvRoUZYzbKyVIC_r4wTZ293W9oSNxOxY/edit?usp=sharing)

7. Chapter 7 | [Files](https://docs.google.com/document/d/1qUlvYm3TuPC12tkhHvpFMMbqKIBOucctuqw6pn4WrVw/edit?usp=sharing)

8. Chapter 8 | [Modules](https://docs.google.com/document/d/1897ymL0zzgyZfZx20cFTolsuDhdPuqu_HUPlUH-kfF8/edit?usp=sharing)

9. Chapter 9 | [More datatypes](https://docs.google.com/document/d/1GKYOVSezNl_g2wDqM59YqNrkoM_tHbsjLwVHkrPXwZA/edit?usp=sharing)

10. Chapter 10 | [Recursion](https://docs.google.com/document/d/1-hqMFwDRnxqkgcABHtkTNY-bxRn3V51I-9eGBjiwqA0/edit?usp=sharing)

11. Chapter 11 | [Classes and Objects](https://docs.google.com/document/d/1xHFg8OK3QauMfxcVuQvgTzgGhRtTHJh41CABPLYa52Q/edit?usp=sharing)

12. Chapter 12 | [Exceptions](https://docs.google.com/document/d/1SKSv2S71zQt1kEAG7_MT7xQ626Zd-k96pzUgWPexxYM/edit?usp=sharing)

13. Chapter 13 | [Fitting](https://docs.google.com/document/d/1PTGY7x6dCgCB6LL2ike_GsuAvjqqrFRr_OTL_BJYTcE/edit?usp=sharing)

14. Chapter 14 | [PyGame](https://docs.google.com/document/d/1ev5mql4LqmRUtX-pCqTZKsyyx8GGrtWZeidvpGnl3N8/edit?usp=sharing)

15. Chapter 15 | [Plotting data with matplotlib](https://docs.google.com/document/d/15EGu5DokeJIHryUkR06UGzYuSlLG8h_vUrblQNe_ZB0/edit?usp=sharing)

16. Chapter 16 | Iterators, Generators and Decorators

17. Chapter 17 | Debugging

18. Chapter 18 | functools library

19. Chapter 19 | Coding Projects | Part 1

20. Chapter 20 | Coding Projects | Part 2

21. Appendix | Git




## Readers

We assume the readers of our revised book have either (1) studied the **EMC** course made by **Team Jupeter(팀 주피터)**, **Scratch coding** for elementary students, or (2) some learning experience on programming languages like JavaScript.

Expected readers are:

1. K4 ~ K12 students, age from 10 to 18.

2. have learned or are learning basic coding courses such as EMC of Team Jupeter

3. have some English skills.

4. current Python users without functional programming experiences.



## Youtube

This being-revised book has accompanying lecture videos on Youtube in Korean(한국어) narration. However, not only Korean students, but also those not Korean speakers can freely watch the lectures using Youtube caption and auto translation.

The Youtube playlist has about 200 episodes, of which each running time being about 10 minutes. For convenience, the playlist is divided into 4.



1.  [Part 1](https://www.youtube.com/watch?v=XyjbAeIj4oA&list=PLlSZlNj22M7RjeCn-sYRHkns9j_gtc2tf): Episode 001~049 | Chapter 1 ~ 4

2. Part 2: Episode 050~099 | Chapter 5 ~ 8

3. Part 3: Episode 100~149 | Chapter 9 ~ 15

4. Part 4: Episode 150~200 | Chapter 16 ~ 20 - those are to-be newly added in this book version in January 2022.



See the playlists of this book.

See [full playlists](https://www.youtube.com/channel/UCxnsWjMKyb6px5lDiqInDHA/playlists) of Team Jupeter.



## Further Learnings



This revised book and accompanying lectures, titled as **Python and Functional Programming**, is a part of a larger learning courses provided by Team Jupeter(all lectures are in **Korean** narration), consist of about 7,000 Youtube video clips/episodes:

All lectures are freely available via Youtube. Some of them are;

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