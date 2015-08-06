title: Just a simple bar plot
tags: python, dataviz
date:  2015-08-06

Couple of days ago I stumbled upon a table in one literature review ;-) and asked myself: "How can these data be presented better?". So I sat and wrote a little Python code that produces a neat bar chart using powers of `matplotlib` and to some extent `pandas`. Think of this post as a cookbook page with a recipy assembled from a handful of Stack Overflow answers and `matplotlib` documentation.

<!-- PELICAN_END_SUMMARY -->

Here is the original table, though written in Markdown, not in LaTeX.

The data consists of estimates of ozone burden in Tg and its production in Tg per year with the corresponding references. The idea was to present the data on a single figure, hence I decided to plot a series of bar pairs. In other words, each study will correspond to a pair of bars, one plotted along one axis and the other - along another axis.

|Burden, Tg | Production, Tg yr–1 | Reference |
|:---------:|:-------------------:|:---------:|
| Modelling Studies                            |
|37+-23     |4877+-853            |Young et al. (2013) |
|323        |-	                  |Archibald et al. (2011)  |
|330        |4876                 |Kawase et al. (2011)  |
|312        |4289                 |Huijnen et al. (2010)  |
|334        |3826                 |Zeng et al. (2010)  |
|324        |4870                 |Wild and Palmer (2008)  |
|314        |-	                  |Zeng et al. (2008)  |
|319        |4487                 |Wu et al. (2007) |
|372        |5042                 |Horowitz (2006)  |
|349        |4384                 |Liao et al. (2006) |
|344+-39    |5110+-606            |Stevenson et al. (2006) |
|314+-33    |4465+-514            |Wild (2007) |
|Observational Studies |
|333        | -	                  |Fortuin and Kelder (1998) |
|327        | -	                  |Logan (1999) |
|325        | -	                  |Ziemke et al. (2011) |
|319–351    | -	                  |Osterman et al. (2008) |

It can be seen that the table is not very expressive in presenting data. Let's try to convert it to a diagram that hopefully will be more eloquent.

{% notebook O3_Budget_Studies.ipynb cells[:] %}
