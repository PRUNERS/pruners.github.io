### Description
Reproducibility is highly desirable for parallel applications, but as they are run on increasingly large and heterogeneous platforms, reproducibility of numerical results or code behaviors is becoming less and less obtainable. The same code can produce different results or occasional failures such as a crash on different systems or even across different runs on the same hardware. PRUNER is a research and development project that aims at innovating scalable techniques to aid applications to obtain the reproducibility. Specifically, our strategy is to accomplish this by developing a multilevel analysis and control toolset called the PRUNING toolset, which combines static and dynamic analysis techniques to detect, control and eliminate targeted sources of non-determinism, as introduced through parallel programming libraries and APIs.￼

### Software Toolset
* Archer – Low-overhead OpenMP data-race detector ([GitHub](https://github.com/PRUNER/archer))
* ReMPI – Highly scalable, storage-efficient record and replay tool for MPI

### Contributors
**LLNL**
  * Dong H. Ahn (Lead)
  * Chris Chambreau
  * Ignacio Laguna
  * Gregory L. Lee
  * Kento Sato (Postdoc)
  * Martin Schulz

**University of Utah - Formal Method Group**
  * Simone Atzeni (PhD student, @simoatze)
  * Prof. Ganesh Gopalakrishnan (Advisor)
  * Prof. Zvonimir Rakamaric (Co-Advisor)

### Publications
* Atzeni, S., G. Gopalakrishnan, Z. Rakamaric, D. H. Ahn, I. Laguna, M. Schulz, G. L. Lee, J. Protze, and M. S. Müller. 2016. “ARCHER: Effectively Spotting Data Races in Large Openmp Applications.” In _2016 Ieee International Parallel and Distributed Processing Symposium (IPDPS)_, 53–62. doi:[10.1109/IPDPS.2016.68](https://doi.org/10.1109/IPDPS.2016.68)
* Protze, Joachim, Simone Atzeni, Dong H. Ahn, Martin Schulz, Ganesh Gopalakrishnan, Matthias S. Müller, Ignacio Laguna, Zvonimir Rakamarić, and Greg L. Lee. 2014. “Towards Providing Low-Overhead Data Race Detection for Large Openmp Applications.” In <em>Proceedings of the 2014 Llvm Compiler Infrastructure in Hpc</em>, 40–47. LLVM-Hpc ’14. Piscataway, NJ, USA: IEEE Press. doi:[10.1109/LLVM-HPC.2014.7](https://doi.org/10.1109/LLVM-HPC.2014.7)
* Sato, Kento, Dong H. Ahn, Ignacio Laguna, Gregory L. Lee, and Martin Schulz. 2015. “Clock Delta Compression for Scalable Order-Replay of Non-Deterministic Parallel Applications.” In <em>Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis</em>, 62:1–62:12. SC ’15. New York, NY, USA: ACM. doi:[10.1145/2807591.2807642](https://doi.org/10.1145/2807591.2807642)

### News Coverage
* [“Pruning” Sources of Nondeterminism in Large-Scale Applications](http://computation.llnl.gov/newsroom/pruning-sources-nondeterminism-large-scale-applications), News Highlights in LLNL Computation and Bits and Bytes, June 2015
* [Supercomputing Tools Speed Simulations](https://str.llnl.gov/july-2014/ahn), Research Highlights in LLNL Science and Technology Review (S&TR), July 2014

### Support
For any question or problem please contact [Simone Atzeni](mailto:simone@cs.utah.edu?subject=[PRUNER] Info).
