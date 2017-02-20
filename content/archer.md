+++
date = "2017-01-27T22:16:26-07:00"
title = "Archer"
parent = "toolset"
+++

<h1><span style="font-variant: small-caps;">Archer</span></h1>

---

### Description

<img src="../img/archer_logo.svg" width="25%" alt="Archer Logo" title="Archer" align="right" style="margin-left: 20px; margin-right: 20px;"/>

<span style="font-variant: small-caps;"><b>Archer</b></span> is a data race detector for OpenMP programs.

<span style="font-variant: small-caps;">Archer</span> combines static and dynamic techniques to identify data races in large OpenMP applications, leading to low runtime and memory overheads, while still offering high accuracy and precision. It builds on open-source tools infrastructure such as LLVM, ThreadSanitizer, and OMPT to provide portability.

---

### Software

<span style="font-variant: small-caps;">Archer</span> is an open-source tool and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/archer"><u>GitHub</u> <i class="fa fa-github"></i></a>.

---

### Quick Start

* **Spack: Recommended for curious users**

	<span style="font-variant: small-caps;"><b>Archer</b></span> maintains an up-to-date package in the Spack develop branch, which builds all dependencies and <span style="font-variant: small-caps;"><b>Archer</b></span> itself from the current head of the master branch:

	```console
	$ git clone https://github.com/LLNL/spack
	$ spack/bin/spack install archer
	```

	If you already have Spack, you can omit the first line.


* **Manual: Recommended for developers and contributors**

	Please refer to the instructions in <a class="smooth-link" title="README" href="https://github.com/PRUNERS/archer/blob/master/README.md" target="_blank">README.md</a>. 
