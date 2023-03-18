# Python Performance Test From 3.5 To 3.11

[中文](README-CHS.md)


- [Python Performance Test From 3.5 To 3.11](#python-performance-test-from-35-to-311)
  - [Dependencies](#dependencies)
  - [Benchmark Test Task (K-mers)](#benchmark-test-task-k-mers)
    - [Background](#background)
    - [Task Description](#task-description)
  - [Quick Start](#quick-start)
  - [Run the C++ version of Task](#run-the-c-version-of-task)
  - [Create the Figures](#create-the-figures)
  - [Original Post:](#original-post)

Use Docker to test the performance of different versions of Python and compare it to C++ on the same task.

<p align="center"> 
<img src="assets/3_extrapolated.png" width="90%" height="45%" >
</p> 

## Dependencies
- Python environment
- Docker

## Benchmark Test Task (K-mers)

### Background

[DNA K-mers](https://en.wikipedia.org/wiki/K-mer) In bioinformatics, k-mers are substrings of length `k` contained within a biological sequence. Primarily used within the context of computational genomics and sequence analysis.

Genome assembly algorithm DNA K-mers. The idea behind this algorithm is simple, DNA is a long string of sequences called nucleotides. 

In DNA, there are 4 nucleotides represented by the letters A, C, G and T. Humans (or more accurately Homo sapiens) have 3 billion nucleotide pairs. For example, a small portion of human DNA might be:

```
ACTAGGGATCATGAAGATAATGTTGGTGTTTGTATGGTTTTCAGACAATT 
```

### Task Description

In this example, if one wanted to select any 4 consecutive nucleotides (i.e. letters) from this string, it would be a k-mer of length 4 ( We call it 4-mer). 

Here are some examples of 4-mers derived from the examples. 

```
ACTA, CTAG, TAGG, AGGG, GGGA
``` 

For this repo, let's generate all possible `13-mers`. Mathematically, this is a permutation problem. Therefore, we have $4^{13} (=67108864)$ possible 13-mers. 

I use a simple algorithm to generate results in C++ and Python. 

Let's see how different Python versions compare to C++.


## Quick Start

Test the performance of different versions of Python and compare it to C++ on the same task.

```bash
python run_main_test.py
```

## Run the C++ version of Task
- [C++ Performance Test](k_mer_in_C/README.md)


## Create the Figures
- [Matplot with XKCD theame ](notebookds/plotting_results.ipynb)



## Original Post:  

- [Python 3.11 性能测评超 3.10 约 25%，这能说明什么？ - 春阳CYang的回答 - 知乎](
https://www.zhihu.com/question/538399507/answer/2700334978)