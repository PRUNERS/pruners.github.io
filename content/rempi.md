+++
date = "2017-01-27T22:16:40-07:00"
title = "ReMPI"
parent = "toolset"
+++

<h1>ReMPI</h1>

---
## Description

<img src="../img/rempi_logo.png" width="40%" alt="ReMPI Logo" title="ReMPI" align="right" style="margin-left: 20px; margin-right: 20px;"/>

ReMPI is a highly scalable scalable record-and-replay tool for MPI applications.
ReMPI records the order of MPI message matching in one run and can deterministically
replay it during subsequent runs. One of the supported modes uses Clock Delta
Compression (CDC) for extreme scale support. CDC can reduce the record size down
to a bare minimum, which then help scale ReMPI by keeping the record to node-local
storage.

---
## Software

ReMPI is open-source software and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/ReMPI"><u>GitHub</u></a> <i class="fa fa-github"></i>.

---
## Quick Start

### 1. Spack: Recommended for curious users

<b>ReMPI</b> maintains an up-to-date package in the Spack develop branch, which builds all dependencies and <b>ReMPI</b> itself from the current head of the master branch:

```console
$ git clone https://github.com/LLNL/spack
$ spack/bin/spack install rempi
```

If you already have Spack, you can omit the first line.


### 2. Manual: Recommended for developers and contributors

Please refer to the instructions in <a class="smooth-link" title="README" href="https://github.com/PRUNERS/ReMPI/blob/master/README.md" target="_blank">README.md</a>.


