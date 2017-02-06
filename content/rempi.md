+++
date = "2017-01-27T22:16:40-07:00"
title = "ReMPI"
parent = "toolset"
+++

## Description

ReMPI is a highly scalable scalable record-and-replay tool for MPI applications.
ReMPI records the order of MPI message matching in one run and can deterministically
replay it during subsequent runs. One of the supported modes uses Clock Delta
Compression (CDC) for extreme scale support. CDC can reduce the record size down
to a bare minimum, which then help scale ReMPI by keeping the record to node-local
storage.

## Software

ReMPI is open-source software and can be obtained on <a class="smooth-link" title="GitHub" href="https://github.com/PRUNERS/ReMPI">GitHub <i class="fa fa-github"></i>.


