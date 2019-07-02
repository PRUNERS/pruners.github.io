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
Compression (CDC) for running at extreme-scale. CDC can reduce the record size down
to the bare minimum, which allows ReMPI to keep record data on node-local
storage, and drastically improve scalability versus writing to a shared file system.

---
## Software

ReMPI is open-source software and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/ReMPI" target="_blank"><u>GitHub</u></a> <i class="fa fa-github"></i>.

---
## Quick Start

### Installation

1. **Spack: Recommended for curious users**

<b>ReMPI</b> maintains an up-to-date package in the Spack develop branch, which builds all dependencies and <b>ReMPI</b> itself. To install via Spack run:

```console
$ git clone https://github.com/LLNL/spack
$ spack/bin/spack install rempi
```

If you already have Spack, you can omit the first line.


2. **Manual: Recommended for developers and contributors**

Please refer to the installation instructions in <a class="smooth-link" title="README" href="https://github.com/PRUNERS/ReMPI/blob/master/README.md" target="_blank">README.md</a>.

---
## Reference
- Kento Sato, Dong H. Ahn, Ignacio Laguna, Gregory L. Lee and Martin Schulz, "Clock Delta Compression for Scalable Order-Replay of Non-Deterministic Parallel Applications", In Proceedings of the International Conference on High Performance Computing, Networking, Storage and Analysis 2015 (SC15), Austin, USA, Nov, 2015.
