lyap-fractal
============

The Lyapunov Fractal is an interesting mathematical object linked deeply with notions of Chaos. This program implements the version found on the wikipedia page: en.wikipedia.org/wiki/Lyapunov_fractal.

This program is written in Python and uses matplotlib to generate plots. So far it is fairly simple, using SQLite to store data and in later stages will use Cython to store the relevant mathematical equations in order to reduce calculation time. I am also considering playing with a third dimension as well as using other chaotic mathematical functions so long as it is relatively simple to approximate the derivative df_n+1/df_n. See the wikipedia page for more details.
