+++
date = "2017-01-27T22:16:37-07:00"
title = "FLiT"
parent = "toolset"
+++

<h1>FLiT</h1>

---

## Description

Floating-point Litmus Tests is a test infrastructure for detecting varibility in floating-point code caused by variations in compiler code generation, hardware and execution environments.

FLiT works by building many versions of the test suite, using multiple C++ compilers, floating-point related settings (i.e. flags) and optimization levels. These tests are then executed on target platforms, where a representative 'score' is collected into a database, along with the other parameters relevant to the execution, such as host, compiler configuration and compiler vendor. In addition to the user-configured test output, we collect counts of each assembly opcode executed (currently, this works with Intel architectures only, using their PIN dynamic binary instrumentation tool).

After executing the suite and collecting the data, it is easy to see how results may diverge using only different compiler settings, etc. Also, the developer is able to understand how to configure their build environment for their target architecture(s) such that they can expect consistent floating-point computations.

It consists of the following components:

* a test infrastructure in the form of c++ code, where additional tests are easily added
* a dynamic make system to generate diverse executables
* an execution disbursement system
* a SQL database for collecting results
* a collection of queries to help the user understand results
* some data analysis tools, utilizing machine intelligence (such as k-means clustering).

---

## Software

FLiT is an open-source tool and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/FLiT"><u>GitHub</u> <i class="fa fa-github"></i></a>.