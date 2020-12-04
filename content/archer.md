+++
date = "2017-01-27T22:16:26-07:00"
title = "Archer"
parent = "toolset"
+++

<h1><span style="font-variant: small-caps;"><b>Archer</b></span></h1>

---

## Description

<img src="../img/archer_logo.svg" width="25%" alt="Archer Logo" title="Archer" align="right" style="margin-left: 20px; margin-right: 20px;"/>

<span style="font-variant: small-caps;"><b>Archer</b></span> is a data race detector for OpenMP programs.

<span style="font-variant: small-caps;"><b>Archer</b></span> combines static and dynamic techniques to identify data races in large OpenMP applications, leading to low runtime and memory overheads, while still offering high accuracy and precision. It builds on an open-source tools infrastructure including LLVM, ThreadSanitizer, and OMPT to provide portability.

---

## Software

<span style="font-variant: small-caps;"><b>Archer</b></span> is an open-source tool and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/archer" target="_blank">GitHub <i class="fa fa-github"></i></a>.

---

## Quick Start

### Install latest LLVM binary package

The dynamic analysis of <span style="font-variant: small-caps;"><b>Archer</b></span> is part of LLVM starting with LLVM release 10.0. 
New features and fixes are upstreamed to LLVM, so always check out the latest version of LLVM.

LLVM is available at <a class="smooth-link" title="LLVM Downloads" href="https://releases.llvm.org/download.html" target="_blank">the LLVM Download Page</a>.

Alternatively install using Spack:

```console
$ git clone https://github.com/LLNL/spack
$ spack/bin/spack install llvm+clang
```

### Spack Installation: Recommended for users curious about the static analysis

<span style="font-variant: small-caps;"><b>Archer</b></span> maintains an up-to-date package in the Spack develop branch, which builds all dependencies and <span style="font-variant: small-caps;"><b>Archer</b></span> itself.
This version of <span style="font-variant: small-caps;"><b>Archer</b></span> includes the static analysis, but latest features of the dynamic anaylsis might be missing.
To install via Spack run:

```console
$ git clone https://github.com/LLNL/spack
$ spack/bin/spack install archer
```

If you already have Spack, you can omit the first line.

### Manual Installation: Recommended for developers and contributors

Please refer to the instructions in the
<a class="smooth-link" title="README" href="https://github.com/PRUNERS/archer/blob/master/README.md" target="_blank">README.md</a>. 
