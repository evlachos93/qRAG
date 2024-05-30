
# Quantum Information Processing with Superconducting Circuits: a Review

**G. Wendin**

Department of Microtechnology and Nanoscience - MC2,
Chalmers University of Technology,
SE-41296 Gothenburg, Sweden

# **Abstract.**
During the last ten years, superconducting circuits have passed from being
interesting physical devices to becoming contenders for near-future useful and scalable
quantum information processing (QIP). Advanced quantum simulation experiments
have been shown with up to nine qubits, while a demonstration of Quantum
Supremacy with fifty qubits is anticipated in just a few years. Quantum Supremacy
means that the quantum system can no longer be simulated by the most powerful
classical supercomputers. Integrated classical-quantum computing systems are already
emerging that can be used for software development and experimentation, even via web
interfaces.
Therefore, the time is ripe for describing some of the recent development of superconducting devices, systems and applications. As such, the discussion of superconducting qubits and circuits is limited to devices that are proven useful for current or near
future applications. Consequently, the centre of interest is the practical applications
of QIP, such as computation and simulation in Physics and Chemistry.

Keywords: superconducting circuits, microwave resonators, Josephson junctions,
qubits, quantum computing, simulation, quantum control, quantum error correction,
superposition, entanglement


-----

# **Contents**

**1** **Introduction** **6**

**2** **Easy and hard problems** **8**
2.1 Computational complexity . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.2 Hard problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.3 Quantum speedup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

2.4 Quantum Supremacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

**3** **Superconducting circuits and systems** **12**
3.1 The DiVincenzo criteria (DV1-DV7) . . . . . . . . . . . . . . . . . . . . 12

3.2 Josephson quantum circuits . . . . . . . . . . . . . . . . . . . . . . . . . 12

3.3 Qubits (DV1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

3.3.1 Phase qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

3.3.2 rf-SQUID flux qubit . . . . . . . . . . . . . . . . . . . . . . . . . 16

3.3.3 Three-JJ flux qubit . . . . . . . . . . . . . . . . . . . . . . . . . 16

3.3.4 Fluxonium qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

3.3.5 C-shunt flux qubit . . . . . . . . . . . . . . . . . . . . . . . . . . 17

3.3.6 2D Transmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . 17

3.3.7 3D Transmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3.3.8 Xmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3.3.9 Gatemon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3.3.10 Andreev level qubit . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3.3.11 Majorana qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3.4 Initialisation (DV2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3.5 Universal gate operation (DV3) . . . . . . . . . . . . . . . . . . . . . . . 19

3.6 Readout (DV4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3.7 Coherence times (DV5) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3.8 Algorithms, protocols and software . . . . . . . . . . . . . . . . . . . . . 21

**4** **Transmon quantum circuits** **22**
4.1 Transmon cQED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

4.2 Weak, strong, ultra-strong and deep-strong coupling . . . . . . . . . . . . 23

4.3 Multi-qubit Transmon Hamiltonians . . . . . . . . . . . . . . . . . . . . . 24

4.3.1 Capacitive coupling . . . . . . . . . . . . . . . . . . . . . . . . . . 24

4.3.2 Resonator coupling . . . . . . . . . . . . . . . . . . . . . . . . . . 25

4.3.3 Josephson junction coupling . . . . . . . . . . . . . . . . . . . . . 25

4.3.4 Tunable coupling . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

**5** **Hybrid circuits and systems** **26**
5.1 Quantum interfaces for qubit interconversion (DV6) . . . . . . . . . . . . 26

5.1.1 Transmon-spin-cQED . . . . . . . . . . . . . . . . . . . . . . . . . 27


-----


5.1.2 Transmon-micromechanical oscillator-cQED . . . . . . . . . . . . 27

5.1.3 Transmon-SAW . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

5.1.4 Transmon-HBAR . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

5.2 Quantum interfaces to flying qubits (DV7) . . . . . . . . . . . . . . . . . 28

5.2.1 Microwave-optical conversion: optomechanics . . . . . . . . . . . 29

5.2.2 Microwave-optical conversion: micromechanics . . . . . . . . . . . 30

5.2.3 Microwave-optical conversion: cavity optomagnonics . . . . . . . . 30

5.2.4 Microwave-optical conversion: SAW . . . . . . . . . . . . . . . . . 31

**Quantum gates** **32**
6.1 Quantum state time evolution . . . . . . . . . . . . . . . . . . . . . . . . 32

6.2 Gate operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

6.3 1q rotation gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

6.4 2q resonance gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

6.4.1 iSWAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

6.4.2 CPHASE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

6.4.3 CNOT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

6.4.4 Controlled rotation . . . . . . . . . . . . . . . . . . . . . . . . . . 37

6.4.5 2q time evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

6.5 2q gates induced by microwave driving . . . . . . . . . . . . . . . . . . . 37

6.5.1 Driving qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

6.5.2 Driving a tunable bus . . . . . . . . . . . . . . . . . . . . . . . . 38

6.6 Gate synthesis and universal sets of gates . . . . . . . . . . . . . . . . . . 40

**Quantum state preparation and characterisation** **41**
7.1 Quantum state characterisation . . . . . . . . . . . . . . . . . . . . . . . 41

7.2 Quantum Supremacy characterisation . . . . . . . . . . . . . . . . . . . . 42

7.3 Multi-qubit state preparation . . . . . . . . . . . . . . . . . . . . . . . . 42

7.3.1 Bell states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

7.3.2 GHZ states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

7.3.3 W-states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

7.3.4 Generating Bell states by parity measurement . . . . . . . . . . . 44

7.4 Teleportation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

7.4.1 Teleportation of states . . . . . . . . . . . . . . . . . . . . . . . . 45

7.4.2 Teleportation of entanglement . . . . . . . . . . . . . . . . . . . . 46

7.5 Distillation of entanglement . . . . . . . . . . . . . . . . . . . . . . . . . 46

**Quantum state protection** **49**
8.1 Quantum control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

8.2 Feedforward control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

8.3 Feedback control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

8.3.1 Digital feedback control . . . . . . . . . . . . . . . . . . . . . . . 49

8.3.2 Analogue feedback control . . . . . . . . . . . . . . . . . . . . . . 50


-----


8.3.3 Measurement and back-action . . . . . . . . . . . . . . . . . . . . 50

8.4 Quantum networks and machine learning . . . . . . . . . . . . . . . . . . 50

8.5 Error correction codes and stabilisers . . . . . . . . . . . . . . . . . . . . 51

8.6 Three qubit code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

8.7 Surface codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

8.7.1 Basic concepts and models . . . . . . . . . . . . . . . . . . . . . . 54

8.7.2 4-qubit parity measurements on a surface code plaquette . . . . . 55

8.7.3 17-qubit design for the surface code . . . . . . . . . . . . . . . . . 55

8.7.4 Multi 2-qubit parity measurements on a surface code 1D chain . . 56

8.8 Architecture and error correction in 3D cQED . . . . . . . . . . . . . . . 57

8.8.1 cQED 3D architecture . . . . . . . . . . . . . . . . . . . . . . . . 57

8.8.2 Engineering cat-states . . . . . . . . . . . . . . . . . . . . . . . . 57

8.8.3 Engineering QEC . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

8.8.4 Gates and operations . . . . . . . . . . . . . . . . . . . . . . . . . 58

**9** **Quantum simulation of many-body systems** **59**
9.1 Basics of quantum simulation . . . . . . . . . . . . . . . . . . . . . . . . 59

9.2 Trotterisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

9.3 Phase estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

9.4 Digital quantum simulation of the quantum Rabi model . . . . . . . . . . 61

9.5 Digital quantum simulation of spin models . . . . . . . . . . . . . . . . . 62

9.5.1 Two-spin Ising and Heisenberg models . . . . . . . . . . . . . . . 62

9.5.2 Digitized adiabatic four-spin transverse Ising model . . . . . . . . 64

9.6 Digital quantum simulation of fermionic models . . . . . . . . . . . . . . 65

9.7 Analogue/adiabatic quantum simulation . . . . . . . . . . . . . . . . . . 67

9.8 Digital-analogue quantum simulation . . . . . . . . . . . . . . . . . . . . 67

**10 Toward quantum chemistry simulation** **69**
10.1 Hamiltonian ground-state energy estimation . . . . . . . . . . . . . . . . 69

10.1.1 Quantum energy estimation . . . . . . . . . . . . . . . . . . . . . 70

10.1.2 Quantum variational eigensolver . . . . . . . . . . . . . . . . . . . 70

10.1.3 H-H ground-state energy curve . . . . . . . . . . . . . . . . . . . 71

10.1.4 He-H + ground-state energy curve . . . . . . . . . . . . . . . . . . 72

10.1.5 Ground-state energy curves for H 2 , LiH and BeH 2 . . . . . . . . . 73

10.2 Toward large-scale simulations . . . . . . . . . . . . . . . . . . . . . . . . 73

10.2.1 From high-level language to hardware instructions . . . . . . . . . 73

10.2.2 Quantum computer emulation . . . . . . . . . . . . . . . . . . . . 74

10.2.3 Electronic structure calculations - molecules . . . . . . . . . . . . 74

10.2.4 Electronic structure of strongly correlated materials . . . . . . . . 75

**11 Adiabatic quantum optimisation** **76**
11.1 Adiabatic quantum algorithms . . . . . . . . . . . . . . . . . . . . . . . . 76

11.2 Quantum annealing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77


-----


**12 Perspectives** **79**
12.1 Looking back . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

12.2 Looking around . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

12.3 Looking ahead . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81


-----

# **1. Introduction**

Quantum Computing is the art of controlling the time evolution of highly complex,
entangled quantum states in physical hardware registers for computation and simulation.
Quantum Supremacy is a recent term for an old ambition - to prove and demonstrate
that quantum computers can outperform conventional classical computers [1].
Since the 1980s, quantum computer science has been way ahead of experiment,
driving the development of quantum information processing (QIP) at abstract and
formal levels. This situation may now be changing, due to recent experimental advances
to scale up and operate highly coherent and operational qubit platforms. In particular,
one can expect superconducting quantum hardware systems with 50 qubits or more
during the next few years.
The near-term goal is to operate a physical quantum device that a classical
computer cannot simulate [2], therefore demonstrating Quantum Supremacy. For
QIP to be of interest one often requests killer applications, outperforming classical
supercomputers on real-world applications like factorisation and code breaking [3].
However, this is not a realistic way to look upon the power of QIP. During the
last seventy years, classical information processing has progressed via continuous
development and improvement of more or less efficient algorithms to solve specific tasks,
in tune with the development of increasingly powerful hardware. The same will certainly
apply also to QIP, the really useful applications arriving along the way.
There is, in fact, already a clear short-term QIP perspective, recognising the
importance of quantum technologies (QT) and quantum engineering for driving the
present and near-future development [4]. This is necessary for developing large scale
devices to achieve the long-term goals of useful quantum computing. To this end,
investigations of quantum device physics have been essential for the present efforts to
scale up of multi-qubit platforms. The work on improving coherence has demonstrated
that qubits are extremely sensitive to a variety of noise sources. The requirement of
making measurements without destroying the coherence has led to the development of
a range of quantum limited superconducting amplifiers. As a result, advanced quantum
sensors and quantum measurement may give rise to a new quantum technology: a
qubit at the tip of a scanning probe, greatly enhancing the sensitivity of magnetic
measurements [57].
The potential of superconducting circuits for QIP has been recognised for more
than twenty years [810]. The first experimental realisation of the simplest qubit,
a Josephson-junction (JJ) based Cooper-pair Box (CPB) in the charge regime, was
demonstrated in 1999 [11]. Originally, the coherence time was very short, just a
few nanoseconds, but it took only another few years to demonstrate a number of
useful qubit concepts: the flux qubit [1214], the quantronium CPB [15], and the
phase qubit [16]. The next important step was to embed qubits in a superconducting
microwave resonator, introducing circuit quantum electrodynamics (cQED) [1722].
The subsequent experiments using a 2D superconducting coplanar microwave resonator


-----



[23,24] demonstrated groundbreaking progress:

(i) Microwave qubit control, strong qubit-resonator coupling and dispersive readout

[23];


(ii) Coupling of CPB qubits and swapping excitations, in practice implementing a
universal __ _iSWAP_ gate [24].

A basis for potentially scalable multi-qubit systems with useful long coherence times
- the transmon version of the CPB - was published in 2007 [25]. Moreover, in 2011
the invention of a transmon embedded in a 3D-cavity increased coherence times toward
100 __ s [26]. At present there is intense development of both 2D and 3D multi-qubit
circuits with long-lived qubits and resonators, capable of performing a large number of
high-fidelity quantum gates with control and readout operations.
The purpose of this review is to provide a snapshot of current progress, and to
outline some expectations for the future. We will focus on hardware and protocols
actually implemented on current superconducting devices, with discussion of the most
promising development to scale up superconducting circuits and systems. In fact,
superconducting quantum circuits are now being scaled up experimentally to systems
with several tens of qubits, to address real issues of quantum computing and simulation

[2741].
The aim is here to present a self-contained discussion for a broad QIP readership. To
this end, time evolution and the construction and implementation of 1q and 2q gates in
superconducting devices are treated in considerable detail to make recent experimental
work more easily accessible. On the other hand, the more general discussion of theory,
as well as much of the experimental work, only touches the surface and is covered by
references to recent work. Reviews and analyses of the QIP field are provided by [4253].
For a comprehensive treatise on QIP we refer to Nielsen and Chuang [54]. Extensive
technical discussions of a broad range of superconducting circuits and qubits can be
found in [5560].
The present review also tries to look beyond the experimental state of the art, to
anticipate what will be coming up in the near future in the way of applications. There
is so much theoretical experience that waits to be implemented on superconducting
platforms. The ambition is to outline opportunities for addressing real-world problems
in Physics, Chemistry and Materials Science.


-----

# **2. Easy and hard problems**

Why are quantum computers and quantum simulators of such great interest? Quantum
computers are certainly able to solve some problems much faster than classical
computers. However, this does not say much about solving computational problems
that are hard for classical computers. Hard problems are not only a question of whether
they take long time - the question is whether they can be solved at all with finite
resources.
The map of computational complexity in Fig. 1 classifies the hardness of
computational (decision) problems. Quantum computation belongs to class BQP
(bounded-error quantum polynomial time). Figure 1 shows that the BQP only
encompasses a rather limited space, basically not solving really hard problems. One
may then ask what is the relation between problems of practical interest and really
hard mathematical problems - what is the usefulness of quantum computing, and which
problems are hard even for quantum computers?

![G_Wendin_Review_of_superconducting_circuits.pdf-7-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-7-0.png)

Figure 1: Computational complexity is defined by Turing machines (TM) providing digital
models of computing [1, 62, 63]: deterministic TM (DTM); quantum TM (QTM); classical
non-deterministic TM (NTM). Tractable problems are defined by polynomial time execution
and define complexity classes: P denotes problems that are efficiently solvable with a classical
computer; P is a subset of NP, the problems efficiently checkable by a classical computer. QMA
denotes the problems efficiently checkable by a quantum computer. NP-hard problems are the
problems at least as hard as any NP problem, and QMA-hard problems are the problems
at least as hard as any QMA problem. For a nice tutorial on how to classify combinatorial
problems, including games, see [61].


-----


_2.1. Computational complexity_

Computational complexity [1, 6264] is defined in terms of different kinds of Turing
machines (TM) providing digital models of computing. A universal TM (UTM) can
simulate any other TM (including quantum computers) and defines what is computable
in principle, without caring about time and memory. Problems that can be solved
by a deterministic TM (DTM) in polynomial time belong to class P (Fig. 1), and are
considered to be easy, or at least tractable. A DTM is a model for ordinary classical
computers - a finite state machine (FSM) reading and writing from a finite tape.
A probabilistic TM (PTM) makes random choices of the state of the FSM upon
reading from the tape, and traverses all the states in a random sequence. This defines the
class BPP (bounded-error probabilistic polynomial time). A PTM may be more powerful
then a DTM since it avoids getting stuck away from the solution. Nevertheless, a PTM
can be simulated by a DTM with only polynomial overhead, so the relation BPP=P is
believed to be true.
A quantum TM (QTM) is a model for a quantum computer with a quantum
processor and quantum tape (quantum memory). Problems that can be solved by a
QTM in polynomial time belong to class BQP (Fig. 1). There, outside P (P __ BQP),
we find problems like Shors algorithm [3] where a QTM provides exponential speedup.
Nevertheless, Fig. 1 shows that BQP is a limited region of the complexity map, not
including a large part of the NP-class containing many hard problems for a classical
computer. It is unknown whether these are hard for a quantum computer. The class
NP (non-deterministic polynomial) is defined by a non-deterministic TM (NTM), able
to provide an answer that can be verified by a DTM in polynomial time. The NTM is not
a real computer but rather works as an oracle, providing an answer. A subclass of NP
is the MA (Merlin-Arthur) class where the all-mighty Merlin provides the answer which
the classical Arthur can verify in polynomial time. Some of these problems are beyond
a quantum computer to calculate, but it might be used to verify solutions in polynomial
time. This is the large quantum Merlin-Arthur (QMA) complexity class shown in Fig. 1.
When not even a quantum computer can verify a solution in polynomial time, then that
problem belongs to the NP-hard complexity class, where even a quantum computer is
of no use.

_2.2. Hard problems_

Can a physical processes exist while being too hard to compute? Or does Nature actually
not solve really hard instances of hard problems? Perhaps the results of Evolution are
based on optimisation and compromises?
There is a long-standing notion that unconventional adaptive analogue computers
can provide solutions to NP-hard problems that take exponential resources (time and/or
memory) for classical digital machines to solve [6571]. The key question therefore is:
can unconventional computing provide solutions to NP-complete problems? The answer
is in principle given by the Strong Church Thesis: Any finite analogue computer can be


-----


simulated _efficiently_ by a digital computer. This is due to the time required by the digital
computer to simulate the analogue computer being This is due to the time required by
the digital computer to simulate the analogue computer being bounded by a polynomial
function of the resources used by the analogue machine [72]. This suggests that physical
systems (both digital and analogue) cannot provide solutions to NP-complete problems.
NP-completeness is a worst case analysis, where at least one case requires exponential,
rather than polynomial, resources in the form of time or memory.
Given the idea that Nature is physical and does not solve NP-hard problems

[61, 7375], where does this place quantum computing? In principle, in a better
position than classical computing, to compute the properties of physical quantum
systems. Tractable problems for quantum computers (BQP) are in principle hard for
classical computers (P). In 1982 Feynman [76] introduced the concept of simulating
one quantum system by another, emulating quantum physics by tailored quantum
systems describing model quantum Hamiltonians (analogue quantum computers). The
subsequent development went mostly in the direction of gate circuit models [77], but two
decades later the analogue/adiabatic approach was formally established as an equivalent
universal approach [7882]. Nevertheless, also for quantum computers the class of
tractable problems (BQP) is limited. There are many problems described by quantum
Hamiltonians that are hard for quantum computers, residing in QMA, or worse (QMAhard, or NP-hard) [8394]. Although, the many-body problem is tractable for quantum
spin chains [95, 96]. When quantum mechanics is not involved, e.g. in combinatorial
problems, quantum computers may not have any advantage [61].

_2.3. Quantum speedup_


Quantum speedup is by definition connected with non-classical correlations [97, 98].
_Entanglement_ is a fundamental manifestation of quantum superposition and nonclassical correlations for pure states [99]. An elementary example of classical behaviour
is provided by a tensor product of independent superpositions of two 2-level systems,
__ 1 = __ 1 2 ( 0 + 1 ) and __ 2 = __ 1 2 ( 0 + 1 ). The tensor product of _N_ (= 2) states
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __


__ 1 = __ 1 2 ( 0 + 1 ) and __ 2 = __ 1 2 ( 0 + 1 ). The tensor product of _N_ (= 2) states
_|_ __ __ = __ 1 _|_ __ __ 2 _|_ = __ __ 1 2 ( 0 _|_ + __ 1 ) __ 1 2 _|_ ( __ 0 + _|_ __ 1 ) = 1 2 ( 00 + 01 + 10 + 11 ) contains

_|_ __ _|_ _|_ __ _|_ __ _|_ __ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __



( 0 + 1 ) and __ 2 =
2

_|_ __ _|_ __ _|_ __



( 0 + 1 ) = 1
2 2

_|_ __ _|_ __


__ = __ 1 __ 2 = __ 1 2 ( 0 + 1 ) __ 1 2 ( 0 + 1 ) = 1 2 ( 00 + 01 + 10 + 11 ) contains
_|_ 2 _N_ __ (= 4) superposed configurations: this is the basis for creating exponentially large _|_ _|_ __ _|_ __ _|_ __ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

superpositions with only a linear amount of physical resources (qubits).
Highly entangled states are created by finite numbers of superpositions. In
the present 2-qubit case, a maximally entangled state is the 2-qubit Bell state,



( 0 + 1 )
2

_|_ __ _|_ __ __


__ 1 2 ( 00 + 11 ): it is not possible to assign a single state vector to any of the two

_|_ __ _|_ __
subsystems, only to the total system. Entanglement allows us to construct maximally
entangled superpositions with only a linear amount of physical resources, e.g. a large
cat state: __ 1 2 ( 0 _......_ 00 + 1 _....._ 11 ), entangling _N_ 2-level systems. This is what allows

_|_ __ _|_ __
us to perform non-classical tasks and provide speedup [97, 98]. Interestingly, just to
characterise the entanglement can be a hard problem for a classical computer, because
several entanglement measures are NP-hard to compute [100]. There is a large number


__ 1 2 ( 00 + 11 ): it is not possible to assign a single state vector to any of the two

_|_ __ _|_ __
subsystems, only to the total system. Entanglement allows us to construct maximally
entangled superpositions with only a linear amount of physical resources, e.g. a large
cat state: 1 ( 0 _......_ 00 + 1 _....._ 11 ), entangling _N_ 2-level systems. This is what allows


10


-----


of measures of entanglement, e.g. concurrence; entropy of entanglement (bipartite);
entanglement of formation; negativity; quantum discord [98,100106]. Quantum discord
is defined as the difference between two classically equivalent measures of information

[107], and indicates the presence of correlations due to noncommutativity of quantum
operators. For pure states it equals the entropy of entanglement [102]. Quantum discord
determines the interferometric power of quantum states [104]. It provides a fundamental
concept for computation with mixed quantum states in open systems, separable and
lacking entanglement but still providing useful non-classical correlations.
Quantum speedup is achieved by definition if a quantum calculation is successful,
as discussed by Dewes et al. [108] in the case of Grover search with a transmon 2-qubit
system. It is then related to the expected known success probabilities of the classical
and quantum systems. In general, however, speedup of a computation is an asymptotic
scaling property [109]. Nevertheless, in practice there are so many different aspects
involving setting up and solving different instances of various classes of problems that
the time to solution (TTS) may be the most relevant measure [110].
Polynomial or exponential speedup has not been much discussed in connection with
digital QC because the systems are still small (5-10 qubits), and the limited coherence
time does not allow very long calculations. In contrast, defining and detecting quantum
speedup is presently a hot issue when assessing the performance of the D-Wave quantum
annealing machines [109112].

_2.4. Quantum Supremacy_

Quantum Supremacy is a recent term for the old ambition of proving that
quantum computers can outperform conventional classical computers [1]. A simple
implementation of Quantum supremacy is to create a physical quantum device that
cannot be simulated by existing classical computers with available memory in any
reasonable time. Currently, such a device would be a 50 qubit processor. It could
model a large molecule that cannot be simulated by a classical computer. It would
be an artificial physical piece of quantum matter that can be characterised by various
quantum benchmarking methods in a limited time, but cannot be simulated by classical
computers of today. And by scaling up by a small number of qubits it will not be
simulatable even by next generation classical computers. A recent example of this given
by Boixo et al. [2], discussing how to characterise Quantum Supremacy in near-term
circuits and systems with superconducting devices.

11


-----

# **3. Superconducting circuits and systems**

The last twenty years have witnessed a dramatic development of coherent nano- and
microsystems. When the DiVincenzo criteria were first formulated during 1996-2000

[113, 114] there were essentially no useful solid-state qubit devices around. Certainly
there were a number of quantum devices: Josephson junctions (JJ), Cooper pair
boxes (CPB), semiconductor quantum dots, implanted spins, etc. However, there
was no technology for building coherent systems that could be kept isolated from the
environment and controlled at will from the outside. These problems were addressed
through a steady technological development during the subsequent ten years, and
the most recent development is now resulting in practical approaches toward scalable
systems.

_3.1. The DiVincenzo criteria (DV1-DV7)_

The seven DiVincenzo criteria [114] formulate necessary conditions for gate-driven
(digital) QIP:
1. Qubits: fabrication of registers with several (many) qubits (DV1).
2. Initialisation: the qubit register must be possible to initialise to a known state (DV2).
3. Universal gate operations: high fidelity single and 2-qubit gate operations must be
available (DV3).
4. Readout: the state of the qubit register must be possible to read out, typically via
readout of individual qubits (DV4).
5. Long coherence times: a large number of single and 2-qubit gate operations must be
performed within the coherence time of the qubit register, _T_ 2 (DV5).
6. Quantum interfaces for qubit interconversion: qubit interfaces must be possible for
storage and on-chip communication between qubit registers (DV6).
7. Quantum interfaces to flying qubits for optical communication: qubit-photon
interfaces must be available for long-distance transfer of entanglement and quantum
information (DV7).

_3.2. Josephson quantum circuits_

The recent systematic development of reliable transmon-based JJ-cQED circuits is now
forming a basis for serious upscaling to 50 qubits in the near future, to develop system
control, benchmarking, error correction and quantum simulation schemes.
The qubits are based on the superconducting non-linear oscillator circuit shown in
Fig. 2 (for an in-depth discussion, see Girvin [57]). The Hamiltonian of the harmonic
oscillator LC circuit alone is given by


 2
 2 __
_H_ = _E_ _C_  _n_ + _E_ _L_ _,_ (1)

2

where  _n_ is the induced charge on the capacitor measured in units of 2e (Cooper pair),

 
and __ is the phase difference over the inductor. The charge  _n_ and phase __ operators

12


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-12-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-12-0.png)

Figure 2: Basic equivalent circuit for all Josephson junction (JJ) based qubits. _C_ represents
a shunt capacitance and _L_ a shunt inductance. _C_ _J_ is the intrinsic capacitance of the JJ.
_E_ _C_ = (2 _e_ ) 2 _/_ 2 _C_ , _E_ _L_ =  _h_ 2 _/_ (4 _e_ 2 _L_ ) and _E_ _J_ 0 =  _h_ 2 _/_ (4 _e_ 2 _L_ _J_ 0 ). The Josephson inductance _L_ _J_ 0 is
defined in the text. _n_ _g_ is the charge on the island induced by capacitive coupling to a voltage
source (not shown), and __ _e_ is the phase across the JJ controlled by an external flux .




do not commute, [ _,_  _n_ ] = _i_ , which means that their expectation values cannot be
measured simultaneously. _E_ _C_ = (2 _e_ ) 2 _/_ 2 _C_ (charging energy of one 2e Cooper pair),
_E_ _L_ =  _h_ 2 _/_ (4 _e_ 2 _L_ ), and the distance between the energy levels of the harmonic oscillator
is given by  _h_ =  _h/_ __ _LC_ = __ 2 _E_ _L_ _E_ _C_ .

For a superconducting high-Q oscillator the energy levels are narrow and
equidistant. However, in order to serve as a qubit, the oscillator must be anharmonic
so that a specific pair of levels can be addressed. Adding the Josephson junction (JJ),
the Hamiltonian of the LCJ circuit becomes




 2  ( __ __ _e_ )
_H_ = _E_ _C_ ( _n_ _n_ _g_ ) _E_ _J_ 0 cos( __ ) + _E_ _L_ __
__ __ 2


(2)


where _n_ _g_ is the voltage-induced charge on the capacitor C (qubit island), and __ _e_ is the
flux-induced phase across the JJ. The Josephson energy _E_ _J_ 0 is given by _E_ _J_ 0 = 2  _h_ _e_ _I_ 0 in

terms of the critical current _I_ 0 of the junction [55]. Typically, the JJ is of SIS type
(superconductor-insulator-superconductor) with fixed critical current.
In order to introduce the Josephson nonlinear inductance, one starts from the
fundamental Josephson relation


where _n_ _g_ is the voltage-induced charge on the capacitor C (qubit island), and __ _e_ is the
flux-induced phase across the JJ. The Josephson energy _E_ _J_ 0 is given by _E_ _J_ 0 =  _h_ _I_ 0 in


_I_ _J_ = _I_ 0 sin __ (3)

Combined with Lenz law:

_V_ = _V_ = _d_  _/dt_ =  0 _/_ 2 _ d/dt,_  0 = _h/_ 2 _e_ (4)

one finds that

_V_ =  0 _/_ 2 __ ( _I_ 0 cos __ ) __ 1 _dI_ _J_ _/dt._ (5)

Defining _dI_ _J_ _/dt_ = _V/L_ _J_ , one finally obtains the Josephson inductance _L_ _J_ 0 :

_L_ _J_ =  0 _/_ 2 __ ( _I_ 0 cos __ ) __ 1 = _L_ _J_ 0 (cos __ ) __ 1 (6)

This defines the Josephson inductance _L_ _J_ 0 of the isolated JJ circuit element in Fig. 2,
and allows us to express the Josephson energy as _E_ _J_ 0 =  _h_ 2 _/_ (4 _e_ 2 _L_ _J_ 0 ).

13


-----


In order to describe the energy-level structure of the quantum LCJ circuit in Fig.
2 one introduces  _n_ = _i_ _h_  __ to get a Schr odinger equation for the circuit wave function

__

__

__ in the phase variable __ :



[ _E_ _C_ ( _i_ _h_  __ _n_ _g_ ) 2 + _U_ ( __ )] __ = _E _ (7)
__ __ __


( __ __ _e_ ) 2
_U_ ( __ ) = _E_ _J_ 0 cos( __ ) + _E_ _L_ __
__ 2


(8)


![G_Wendin_Review_of_superconducting_circuits.pdf-13-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-13-0.png)

Figure 3: Level spectrum (band structure) of the Cooper pair box (CPB) as a function of the
offset charge _n_ _g_ for different ratios _E_ _J_ 0 _/E_ _C_ [25]: (a) charge qubit [23]; (b) Quantronium [15];
(d) Transmon [25]. Historically, the CPB evolved from the original charge qubit (1999) [11]
via the quantronium (2002) [15, 203, 206] and CPB-cQED (2004) [21, 23], to the transmon
(2007) [25] and the Xmon (2013) [149, 150]. The charge dispersion decreases exponentially
with _E_ _J_ 0 _/E_ _C_ , while the anharmonicity only decreases algebraically with a slow power law in
_E_ _J_ 0 _/E_ _C_ [25,203] - this makes it possible to individually address selected transitions even for
quite large ratios of _E_ _J_ 0 _/E_ _C_ . Figure adapted from [25].

With respect to Eq. 8 and Fig. 2 there are two distinct cases:
(1) _E_ _L_ =0 ( _L_ ) : _U_ ( __ ) becomes a pure cosine periodic potential, and the wave
function has the form __ __ = __ ( _, n_ _g_ ) _e_ _in_ _g_ __ , where __ ( _, n_ _g_ ) is a Mathieu function. The
energy levels form bands _E_ ( _n_ _g_ ) in the momentum direction [22, 25]. The dispersion
of these band depends on the ratio _E_ _J_ 0 _/E_ _C_ , as shown in Fig. 3. Of special interest is
that a large capacitance _C_ results in flat low-lying bands, making the circuit insensitive
to charge fluctuations (as well as to charge control via a DC gate voltage) [25].

14


-----


(2) _E_ _L_ __ _E_ _J_ 0 : _U_ ( __ ) is no longer periodic, but described by a parabola modulated
by sinusoidal function. The shape of the potential toward the bottom of the parabola,
and the associated qubit level structure, depend on the _E_ _L_ _/E_ _J_ 0 ratio and on the external
flux __ _e_ . This makes it possible to design a wide variety of qubits by tuning the circuit
parameters in Fig. 2.

_3.3. Qubits (DV1)_

We will now briefly discuss the qubit families listed in Table 1 and shown in Fig. 4. In
reality, all qubits are multi-level systems. However, since they are most often treated
as quantum bits (binary logic), we will refer to them as qubits even if additional levels
are used for gate operations. The qubits can be defined in terms of different values of
the circuit parameters through the _E_ _J_ 0 _/E_ _C_ and _E_ _L_ _/E_ _J_ 0 ratios, characterising a number
of charge and flux types of devices.

Table 1: Main types of Josephson junction (JJ) based qubit circuits.


_C_ _C_ _J_ _L_ _L_ _J_ 0 _E_ _L_ _/E_ _J_ 0 _E_ _J_ 0 _/E_ _C_ Z
fF fF pH pH 
2. Phase qubit [115] 1. Phase qubit [16] 0 800 __ 6000 0 720 3300 __ 16 80 0.11 0.005 __ __ 10 10 4 6 __ __ 15 1.5
3. rf-SQUID [12] 0 40 238 101 0.43 2000 48
4. Flux qubit [125] 0 3 1200 600 0.5 10 450
5. Fluxonium [137] 0.15 __ 0 3300 150 0.045 1 1400
6. C-shunt [140] 7. Charge qubit [11] 8. Quantronium [15] 9. Transmon [25,26] 10. Xmon [149] 11. Gatemon [153] 50 0.68 2.8 15-40 100 100 __ __ __ __ __ __ 0 0 0 0 0 0 __ __ __ __ __ 15000 808 1.1 10 __ __ __ 4500 10 10 10 3 4 4 4 0 0 0 0 0 0.3 1.27 10-50 22-28 17-32 0.018 25 __ __ __ __ 1300 480 10 250 500 500 4


Charging energy of one Cooper pair (2e): _E_ _C_ = (2 _e_ ) 2 _/_ 2 _C_
Inductive energy: _E_ _L_ =  _h_ 2 _/_ (4 _e_ 2 _L_ )
Josephson energy: _E_ _J_ 0 =  _h_ 2 _/_ (4 _e_ 2 _L_ _J_ 0 )
Resistance quantum: _R_ _Q_ =  _h/_ (2 _e_ ) 2 __ 1 _._ 027059 _k_ 
Impedance: _Z_ _L_ _J_ 0 _/C_ = _R_ _Q_ __ 2 _/_ _E_ _J_ 0 _/E_ _C_
__
 


_L_ _J_ 0 _/C_ = _R_ _Q_


2 _/_


_E_ _J_ 0 _/E_ _C_


_3.3.1. Phase qubit_ The phase qubit is formed by the two lowest levels in the potential
wells formed by a current-biased Josephson junction. In practice, current bias is achieved
by flux-biasing an rf-SQUID ( __ _e_ knob) (Fig. 2), placing the qubit in an anharmonic
potential well on the slope of the parabola.

15


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-15-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-15-0.png)

Figure 4: Graphic presentation of data from Table 1: 1. Phase qubit [16]; 2. Phase qubit

[115]; 3. rf-SQUID [12]; 4. Flux qubit [125]; 5. Fluxonium [137]; 6. C-shunt [140]; 7. Charge
qubit [11]; 8. Quantronium [15]; 9. Transmon [25,26]; 10. Xmon [149]; 11. Gatemon [153].

The original phase qubit [16] was built on a large-area junction with large selfcapacitance _C_ _J_ (Table 1). However, the large area of the junction oxide gave rise to
many defects, trapping two-level fluctuators (TLS) that severely limited the coherence
time. An improved phase qubit [115] was created by separating the device into a smallarea (low _C_ _J_ ) JJ with the same critical current (and thus the same _E_ _J_ 0 , _J_ 0 ), and a large
shunt capacitance _C_ with a dielectric with much fewer defects. This phase qubit was
the first one to be used for advanced and groundbreaking QIP applications with up to
four qubits [116121]. However, the coherence time has stayed rather short ( _<_ 1 _s_ );
therefore, phase-qubit technology cannot be scaled up at the present time. See [22,55]
for detailed discussions.

_3.3.2. rf-SQUID flux qubit_ The rf-SQUID flux qubit [12, 122] is a persistent-current
qubit obtained by setting the biasing flux to  0 _/_ 2 so that the Josephson part creates
two potential wells separated by a barrier at the bottom of the parabola. This defines
two low-lying bonding-antibonding qubit levels describing superpositions of left- and
right-rotating supercurrents: _|_ _L_ _ |_ _R_ __ . Since the inductive SQUID loop is large, this
flux qubit is sensitive to flux noise, and the relaxation and coherence times are quite
short, __ 20 _ns_ [122], probably due to two-level fluctuators in the Nb/AlOx/Nb trilayer
junction [122]. The D-Wave Systems flux qubit is of this type [123,124].

_3.3.3. Three-JJ flux qubit_ The three-JJ flux qubit [13,14,125] consists of an rf-SQUID
where the inductor _L_ has been replaced by two JJs to provide large inductance with
a small SQUID ring. Since the added JJs also create an oscillating cosine potential,
with the right parameters there appears a periodic potential with a double well at the
bottom of each major well, defining two low-lying bonding-antibonding qubit levels.
Tuning the flux bias with the __ _e_ knob makes it possible to vary the relative energies of

16


-----


the wells. Since the 3-JJ potential is periodic, it is associated with a band structure.
The three-JJ flux qubit has always been a major candidate for scaled-up multiqubit systems, but the coherence time has not improved much, which has so far limited
applications to cases making use of the SQUID properties and strong flux coupling

[126128] for applications to microwave technology [129, 130], analog computing [131],
and metamaterials [132134]. A recent experiment has demonstrated somewhat longer
coherence time of a flux qubit in a 3D cavity [135]. Also, see the C-shunt flux qubit
below.

_3.3.4. Fluxonium qubit_ The fluxonium [136, 137] consists of a small JJ shunted by a
very large inductance provided by a long array of large JJs. The resulting effective
capacitance is very small (see Table 1). This looks similar to the 3-JJ flux qubit in the
sense that the two large JJs are replaced by a large JJ array. Approximately, the large
array creates a wider parabola accommodating several potential wells. An important
thing is that the capacitance C is so small that the there are practically no charge
fluctuations (similar to the CPB charge qubit). The relaxation time _T_ 1 1 _ms_ at 1/2
__
flux quantum bias is due to suppression of coupling to quasiparticles [137].

_3.3.5. C-shunt flux qubit_ The C-shunt flux qubit [138,139] is usually viewed as a 3-JJ
flux qubit shunted by a large capacitance. Viewed from another angle, it can be also
be viewed as a transmon shunted by the effective large inductance of the two large flux
qubits of the 3-JJ flux qubit. The effect is to flatten the bottom of the wells of the
transmon cosine potential, making them quartic rather than quadratic. There is then
no longer any double-well structure like in the flux qubit, but still strong anharmonicity
(in contrast to the transmon)
Experimentally, presently the C-shunt flux qubit shows great promise [140], with
broad frequency tunability, strong anharmonicity, high reproducibility, and coherence
times in excess of 40 __ s at its flux-insensitive point.

_3.3.6. 2D Transmon qubit_ The transmon [25] is a development of the CPB toward a
circuit with low sensitivity to charge noise, and therefore much longer coherence times.
This is achieved by radically flattening the bands in the charge direction by increasing
the _E_ _J_ 0 _/E_ _C_ ratio (Fig. 3d). It should be noted that the transmon is really a flat-band
multilevel system (qudit), and the higher levels are often used for implemetation of 2qubit gates. Since the influence of the charge offset _n_ _g_ will vanish (the situation in Fig.
3d), it follows that the energy levels can no longer be tuned statically by the charge
gate - it can only be used for microwave excitation to drive transitions between energy
levels. The driving is differential - the transmon is floating (not grounded). Tuning of
the frequency of the transmon by varying the Josephson energy _E_ _J_ 0 can be achieved
by replacing the JJ by a 2-JJ SQUID (which then also increases the sensitivity to flux
noise).

17


-----


The 2D transmon is now established as a central component of several scalable
platforms [28,31,34], with applications to a wide range of QIP problems.

_3.3.7. 3D Transmon qubit_ In the 3D transmon [26], the JJ qubit is coupled to the 3D
cavity through a broadband planar dipole antenna. Experiments with 3D devices and
architectures are presently demonstrating important progress along two different lines:
(i) like in 2D, a digital qubit approach with 1q and 2q gate operations controlled by
microwave driving [141]; (ii) a continuous-variable approach where the 3D cavities carry
the information in multi-photon cat-states, and the transmon qubits mainly serve for
creating and controlling the states of the cavities [142148].

_3.3.8. Xmon qubit_ The Xmon [32,3537,149,150] is a transmon-type qubit developed
for architectures with 2D arrays of nearest-neighbour capacitively coupled qubits. The
large shunt capacitance _C_ (see Table 1) has the shape of a cross and is grounded via
the JJ-SQUID, allowing tunability of the qubit frequency.
The Xmon is established as a component for a major scalable platform. Circuits
and systems with up to 9 Xmon qubits [35, 37] are presently being investigated with
applications to a wide range of QIP problems.
A variation is the gmon with direct tunable coupling between qubits [151].

_3.3.9. Gatemon qubit_ The gatemon [152, 153] is a new type of transmon-like device,
a semiconductor nanowire-based superconducting qubit. The gatemon is of weak-link
SNS type (superconductor-normal-metal-superconductor), and the Josephson energy
is controlled by an electrostatic gate that depletes carriers in a semiconducting weak
link region, i.e. controls the critical current _I_ _c_ like in a superconducting transistor.
There is strong coupling to an on-chip microwave cavity, and coherent qubit control via
gate voltage pulses. Experiments with a two-qubit gatemon circuit has demonstrated
coherent capacitive coupling, swap operations and a two-qubit controlled-phase gate

[153].

_3.3.10._ The Andreev level qubit (ALQ) [154, 155] is a spindegenerate, single-channel, SNS-type Josephson junction in an rf-SQUID loop. _Andreev level qubit_ The
ALQ can be strongly coupled to a coplanar resonator [156]. Adding coupling to a spin
degree of freedom in the junction makes it possible to manipulate the Andreev bound
states (ABS) with a magnetic field [157,158].
Recently there has been significant experimental progress toward detecting and
manipulating ABSs in atomic contacts (break junction point contacts) [159, 160] and
hybrid semiconductor-superconductor (Sm-S) nanostructures [161, 162]. The device
is typically an InAs nanowire (NW) between epitaxially grown superconducting Al
electrodes (S). The resulting S-NW-S Josephson junction [162] is in fact a single-channel
version of the gatemon [153]. The ALQ is potentially long-lived, but so far the coherence
times are short - the ALQ remains a device for fundamental research.

18


-----


_3.3.11. Majorana qubit_ The ultimate system for quantum computing might be devices
based on topological protection of information. One such system could be Majorana
bound states (MBS) in Sm-S nanostructures that produce ABS at the interface between
the normal NW semiconductor (Sm) and the superconductor (S) [163167]. By applying
an axial magnetic field along the S-NW device, one can make the ABSs move to
zero energy with increasing magnetic field and form mid gap states [161, 167]. If
the states remain at zero energy in a long junction, a topological phase forms with
MBSs at the endpoints of the nanowire [167]. The first experimental signatures of
MBS in superconductor-semiconductor nanowires [164] have been confirmed [161,167],
and extended to superconductor-atomic chain platforms [168]. A major issue is how
to manipulate topologically protected qubits to allow universal quantum computation

[169,170].

_3.4. Initialisation (DV2)_

Qubit lifetimes are now so long that one cannot depend on natural relaxation time
_T_ 1 for initialization to the ground state. For fast initialisation on demand, qubits can
be temporarily connected to strongly dissipative circuits, or to measurement devices

[171175].

_3.5. Universal gate operation (DV3)_

Universal high fidelity single- and two-qubit operations (Clifford + T gates; see Sect. 6.6)
have been achieved for all major types of superconducting qubits. The shortest time
needed for basic 1- and 2-qubit quantum operation is a few nanoseconds. Entangling
gates with 99.4% fidelity have recently been demonstrated experimentally [32]. However,
it should be noted that high-fidelity gates may require carefully shaped control pulses
with typically 10-40 __ s duration.

_3.6. Readout (DV4)_

There are now well-established efficient methods for single-shot readout of individual
qubits, typically performed via dispersive readout of a resonator circuit coupled to
the qubit. A strong measurement collapses the system to a specific state, and
then repeated non-destructive measurements will give the same result. Single-shot
measurements require extremely sensitive quantum-limited amplifiers, and it is the
recent development of such amplifiers that has made single-shot readout of individual
qubits possible [48,171186].

_3.7. Coherence times (DV5)_

JJ-qubits are manufactured and therefore sensitive to imperfections. Nevertheless, there
has been a remarkable improvement of the coherence times of both qubits and resonators

19


-----


during the last five years [48, 150, 187, 188]. Table 2 indicates the present state of the
art.

Table 2: The DiVincenzo criteria [114] and the status of the main types of
superconducting JJ-based qubits (March 2017). The figures in the table refer to the best
published results, but may have limited significance - the coherence times in operational
multi-qubit circuits are often considerably lower.

2D Tmon 3D Tmon Xmon Fluxm C-shunt Flux Gatemon

[25] [26] [149] [137] [139,140] [13] [153]


DV1, #q 5 [34,204] 4 [141] 9 [32,37] 1 2 [140] 4 [205] 2
DV2 _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_
DV3 _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_
t 1 _q_ ( _ns_ ) 10-20 30-40 10-20 5-10 5-10 30
n _op,_ 1 _q_ _>_ 10 3 _>_ 10 3 _>_ 10 3 __ 10 3 10 3 10
__ __ __ __


F 1 _q_ 0.999 _>_ 0 _._ 999 0.9995 _>_ 0 _._ 99
__ __ __ __
t 2 _q_ ( _ns_ ) 10-40 450 5-30 50
n _op,_ 2 _q_ 10 3 __ 10 2 10 3 __ __ __ 10 2
__ __ __ __ __ __ __


F 2 _q_ _>_ 0.99 0.96-0.98 0.9945 0.91
__ __ __
DV4 _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_
DV5 _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_ _Y es_
_T_ 1 ( _s_ ) 40 100 50 1000 55 20 [135] 5.3
__
_T_ 2 __ ( _s_ ) 40 _>_ 140 20 _>_ 10 40 3.7
_T_ 2 _echo_ ( _s_ ) __ 40 _>_ 140 85 __ 9.5
__ __ __ __


- The number of qubits ( ) refers to operational circuits with all qubits connected. _DV_ 1 _,_ # _q_
- _t_ 1 _q_ and _t_ 2 _q_ are gate times for 1q- and 2q-gates.
- _n_ _op,_ 1 _q_ and _n_ _op,_ 2 _q_ are the number of 1q- and 2q-gate operations in the coherence time.
- _F_ 1 _q_ and _F_ 2 _q_ are average fidelities of 1q- and 2q-gates, measured e.g. via randomised
benchmarking (Sect. 7.1).
- _T_ 1 is the qubit energy relaxation time.
- _T_ 2 __ is the qubit coherence time measured in a Ramsey experiment.
- _T_ 2 _echo_ is the qubit coherence time measured in a spin-echo (refocusing) experiment.
- Table entries marked with a hyphen (-) indicate present lack of data.
- Note that average gate fidelities F 1 _q_ and F 2 _q_ do not necessarily correspond to
thresholds for error correction [207].
- The t 2 _q_ gate time for the 3D Tmon refers to a resonator-induced phase gate.

20


-----


_3.8. Algorithms, protocols and software_

A number of central quantum algorithms and protocols have been performed
experimentally with multi-qubit circuits and platforms built from the main types of
superconducting JJ-based qubits (see e.g. [36, 37, 108, 120, 189193]), demonstrating
proofs of principle and allowing several transmon-type systems to be scaled up.
In practice, a quantum computer (QC) is always embedded in a classical computer
(CC), surrounded by several classical shells of hardware (HW) and software (SW)

[31,194,195]. Quantum computation and quantum simulation then involve a number of
steps:

(i) CC control and readout HW (shaped microwave pulses, bias voltages, bias fluxes).

(ii) CC control and readout SW for the HW (machine language; optimal control).

(iii) CC subroutines implementing gates (gate libraries).

(iv) High-level CC optimal control of quantum operations.

(v) CC subroutines implementing quantum gate sequences (for benchmarking, QFT,
time evolution, etc.).

(vi) High-level CC programming, compilation, and simulation of quantum algorithms
and circuits [196199].

(vii) High-level CC programs solving problems [200,201]

The only truly quantum part is step (v), explicitly performing quantum gates
on quantum HW and quantum states. This is where quantum speedup can be
achieved, in principle. Since the quantum gates have to be implemented by classical
SW, it is necessary that the needed number of gates to describe a quantum circuit
scales polynominally in the size of problem. For the Clifford gates there are efficient
(polynomial) representations. However, to describe an arbitrary, universal quantum
circuit needs T-gates and may take exponential resources [202].
If the quantum gates are executed in SW on representations of quantum states on
a classical machine, then the quantum computer is emulated by the classical machine.
Then to execute the gates scales exponentially, which means that a classical computer
can only simulate a small quantum system. The present limit is around 50 qubits [2,202]
- beyond that is the realm of Quantum Supremacy [2] .

21


-----

# **4. Transmon quantum circuits**

The present development of quantum information processing with scalable Josephson
Junction circuits and systems goes in the direction of coupling transmon-type qubits
with quantum oscillators, for operation, readout and memory. In this section we will
therefore focus on the transmon, and describe the components in some detail. For an
in-depth discussion, the reader is referred to the original article by Koch _et al._ [25].

_4.1. Transmon cQED_

A generic compact circuit model for the device is shown in Fig. 5a, and a hardware
implementation is shown schematically in Fig. 5b.

![G_Wendin_Review_of_superconducting_circuits.pdf-21-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-21-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-21-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-21-1.png)

Figure 5: Transmon-cQED: (a) Equivalent circuit (see text); (b) Physical device. The 2-JJ
SQUID is located at the centre of a large interdigitated shunt capacitor ( _C_ _B_ ), and the entire
transmon is capacitively coupled to a coplanar waveguide (CPW) resonator ( _L_ _r_ _C_ _r_ ). The
transmon is not grounded - it is floating and driven differentially. Adapted from [25].

The transmon circuit in Fig. 5a consists of a number of fundamental components:
- A Cooper pair box (CPB) with one or two Josephson junctions (JJ) sitting in a closed
circuit with a large shunting capacitance _C_ _B_ (anharmonic oscillator). The excitation
energy of the two-level systems is __ = _E_ 1 _E_ 0
__
- A resonator circuit _L_ _r_ _C_ _r_ (harmonic oscillator) with frequency __ = 1 _/_ __ _L_ _r_ _C_ _r_ .
- A capacitance _C_ _g_ coupling the transmon and the resonator with coupling constant _g_ .
- A drive circuit (right) flux-coupled to the SQUID-type JJ circuit for tuning the qubit
energy.
- A microwave drive circuit (left) capacitively coupled to the CPW for qubit operation.
- There is no explicit readout oscillator included in Fig. 5a, but the _L_ _r_ _C_ _r_ bus resonator
can serve to illustrate a readout device..
Treating the transmon as an approximate two-level system with linear coupling to
a single-mode oscillator, the transmon-cQED Hamiltonian takes the form



1
   
_H_ = _H_ _q_ + _H_ _qr_ + _H_ _r_ =
__ 2



1 _ _ _z_ + _g _ _x_ ( _a_ + _a_ + ) +  _h_ ( _a_ + _a_ + 1

2 2



) (9)
2


where __ is the qubit excitation energy, _g_ is the qubit-oscillator coupling, and __ is the
oscillator frequency.

22


-----


Introducing the raising and lowering operators __ = ( __ _x_ _i _ _y_ ) _/_
__
__
2, the qubitresonator coupling term  _H_ _qr_
is split into two terms, Jaynes-Cummings (JC) and antiJaynes-Cummings (AJC):

_H_  _qr_ = _H_  _qr_ _JC_ +  _H_ _qr_ _AJC_ = _g_ ( __ + _a_ + __ __ _a_ + ) + _g_ ( __ + _a_ + + __ __ _a_ ) (10)

This Hamiltonian describes the canonical quantum Rabi model (QRM) [208210].
Equations (9,10) are completely general, applicable to any qubit-oscillator system. Only
keeping the Jaynes-Cummings (JC) terms corresponds to performing the rotating-wave
approximation (RWA).

_4.2. Weak, strong, ultra-strong and deep-strong coupling_

There are five basic energy scales that determine the qubit-oscillator coupling strength:
_g, , _ , plus the oscillator decay rate __ (resonance line width) and the qubit decay rate
__ (transition line width) .
One typically distinguishes between four cases of qubit-oscillator coupling:
(i) _Weak coupling_ : _g_ __ _, , , _ ; RWA valid for __ __ __ __ __ .
(ii) _Strong coupling_ : _, _ __ _g_ __ _, _ ; RWA valid; vacuum Rabi oscillations.  _AJC_
(iii) _Ultra-strong coupling (USC)_ : _g/_ __ 1; RWA breaks down; _H_ counter-rotating
term important.

 _AJC_
(iv) essential; qubitoscillator compound system. _Deep-strong coupling (DSC)_ : _g/_ __ 1; RWA not valid at all; _H_
In the two cases of _weak_ and _strong coupling_ , one performs the rotating-wave

 _JC_
approximation (RWA) and only keeps the first _H_ _qr_ term, which gives the canonical
Jaynes-Cummings model [208,211,212],


_H_ 1 _ _ _z_ + _g_ ( __ + _a_ + __ __ _a_ + ) +  _h_ ( _a_ + _a_ ) (11)
__ 2

describing dipole coupling of a two-level system to an oscillator. In the non-resonant
case, diagonalising the Jaynes-Cummings Hamiltonian to second order by a unitary
transformation gives [21,25,212]



1
_H_ =
__ 2



1 2

( __ + _g_
2 



2 _g_

) __ _z_ + ( _h_ +
 



__ _z_ ) _a_ + _a_ (12)



where = __ __ _h_  __ _g_ is the so-called detuning. The result implies that (i) the qubit
transition energy __ is Stark shifted (renormalized) by the coupling to the oscillator, and
(ii) the oscillator energy  _h_ is shifted by the qubit in different directions depending
on the state of the qubit. This condition allows discriminating the two qubit states in
dispersive readout measurement [21,23].
The _strong coupling_ situation [17,18,21] was demonstrated experimentally already
in 2004 with superconducting CPB-cQED [23] by direct physical coupling of the CPB
and the 2D resonator. The _ultra-strong coupling_ case [209,213] is more difficult to achieve
by direct statical physical coupling of a transmon qubit and a resonator, and but has
recently been achieved experimentally using flux qubit cQED [126128]. On the other

23


-----


hand, it is possible to simulate the QRM in the USC and DSC regimes by external timedependent driving of the oscillator in analogue [213,214] or digital [215217] quantum
simulation schemes.

_4.3. Multi-qubit Transmon Hamiltonians_

In the following we will focus on transmon multi-qubit systems, and then the
Hamiltonian takes the general form (omitting the harmonic oscillator term):

   
_H_ = _H_ _q_ + _H_ _qr_ + _H_ _qq_



1
=
__ 2


__ _i_ __ _zi_ +


_g_ _i_ __ _xi_ ( _a_ + _a_ + ) + 1


__ _,ij_ __ _i_ __ _j_ (13)
_i,j_ ; __




For simplicity, in Eq. 13 the qubit-resonator term _H_ _qr_ is considered only to refer to
readout and bus operations, leaving indirect qubit-qubit interaction via the resonator


to be included in _H_ _qq_ via the coupling constant __ _,ij_ .

![G_Wendin_Review_of_superconducting_circuits.pdf-23-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-23-0.png)

Figure 6: Two coupled transmon qubits flux-tunable energies _E_ 10 _,_ 1 _, E_ 10 _,_ 2 . (a) Generic
coupling scheme; (b) Capacitive coupling, _C_ _c_ ; (c) Resonator coupling; (d) Inductive coupling
with tunable JJ [151]; (e) Transmon-bus coupling [220].

_4.3.1._ _Capacitive coupling_ This case (Fig. 6b) is described by an Ising-type model
Hamiltonian with direct capacitive ( _C_ _c_ ) qubit-qubit charge coupling. For the transmon

[55],


_H_ = __


_i_ =1 _,_ 2


__ _i_

__ _zi_ + __ 12 __ _x_ 1 __ _x_ 2 (14)
2



1
__ 12 =


_E_ 10 _,_ 1 _E_ 10 _,_ 2


__ _E_ _C_ 1 _E_ _C_ 2 1

=
_E_ _Cc_ 2


_C_ _c_ 1 _C_ _c_
_E_ 10 _,_ 1 _E_ 10 _,_ 2 _E_ 10
__ _C_ 1 _C_ 2 __ 2 _C_


_C_ _c_ 1
_E_ 10 _,_ 1 _E_ 10 _,_ 2
__ _C_ 1 _C_ 2 __ 2


(15)


24


-----


where the approximate result for __ 12 refers to identical qubits in resonance. In the RWA
one finally obtains the Jaynes-Cummings Hamiltonian


_H_ = __


_i_ =1 _,_


__ 2 _i_ __ _zi_ + __ 12 ( __ 1 + __ 2 __ + __ 1 __ __ 2 + ) (16)


_4.3.2. Resonator coupling_ In this case (Fig. 6c) the coupling is primarily indirect, via
virtual excitation (polarisation) of the detuned bus resonator. Diagonalisation of the
Hamiltonian gives the usual second-order qubit-qubit coupling [21,24,55]:


_H_ = __


_i_ =1 _,_


__ _i_

__ _zi_ + __ 12 __ _x_ 1 __ _x_ 2 (17)
2



1
__ 12 =



1

_g_ 1 _g_ 2 ( 1
2 


+ 1
 1 


) _g_ 1 _g_ 2
 2 __


(18)


Here  1 = __ 1 __ _h_  and  2 = __ 2 __ _h_  are the detunings of the qubits, and _g_ 1 _g_ 2 __  1 _,_  2 .
Finally, in the RWA one again obtains the Jaynes-Cummings Hamiltonian


_H_ = __


_i_ =1 _,_ 2


__ _i_ 1 _g_

__ _zi_ + _g_
2 


( __ 1 + __ 2 __ + __ 1 __ __ 2 + ) (19)


_4.3.3. Josephson junction coupling_ The transmon qubits can also be coupled via a
Josephson junction circuit [55], as illustrated in Fig. 6d. A case of direct JJ-coupling
(omitting the coupling capacitors in Fig. 6d) has recently been treated theoretically
and implemented experimentally by Martinis and coworkers [151, 218]. To a good
approximation, the Hamiltonian is given by


_H_ = __


_i_ =1 _,_ 2


__ _i_

__ _zi_ + __ 12 __ _y_ 1 __ _y_ 2 (20)
2



1
__ 12
__ 2



1 _L_

_E_ 10
2 _L_


_L_ _J_


2 _L_ _c_ + _L_ _Jc_ _/_ cos __ _c_


(21)


where the approximate result for __ 12 refers to identical qubits in resonance, and the
RWA Hamiltonian is again given by Eq. 16. By varying the flux in the coupling
loop, the Josephson inductance can be varied between zero and strong coupling,
0 2 __ 12 2 __ 110 _MHz_ [151].
__ __

_4.3.4. Tunable coupling_ Tunable qubit-qubit coupling can be achieved in a number of
ways, for example (i) by tuning two qubits directly into resonance with each other; (ii)
by tuning the qubits (sequentially) into resonance with the resonator; (iii) by tuning
the resonator sequentially and adiabatically into resonance with the qubits [219]; (iv) by
driving the qubits with microwave radiation and coupling via sidebands; (v) by driving
the qubit coupler with microwave radiation (e.g. [220]); (vi) by flux-tunable inductive
(transformer) coupling [221]. In particular, for JJ-coupling, the qubit-qubit coupling
can be made tunable by current-biasing the coupling JJ [218,222,223].

25


-----

# **5. Hybrid circuits and systems**

In this section we will discuss the status of the DiVincenzo criteria DV6 and DV7 listed
in Sect. 3.1.
Even if a QIP system in principle can consist of a single large coherent register
of qubits, practical systems will most likely be built as hybrid systems with different
types of specialized quantum components: qubits, resonators, buses, memory, interfaces.
The relatively short coherence time of JJ-qubits ( _s_ ) compared to spin qubits ( _ms_ )
and trapped ions ( ) has promoted visions of architectures with fast short-lived JJqubit processors coupled to long-lived memories and microwave-optical interfaces, as _s_
illustrated in Fig. 7.

![G_Wendin_Review_of_superconducting_circuits.pdf-25-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-25-0.png)

Figure 7: A conceptual view of a transmon hybrid system with peripherals serving as
long-term memory and communication devices.

There are numerous demonstrations of coherent transfer between JJ-qubits and
microwave resonators (both lumped circuits and microwave cavities, and mechanical
resonators), as well as between JJ-qubits and spin ensembles. In principle, qubits
coupled to microwave resonators (q-cQED) is already a hybrid technology. An
interesting aspect is that the development of long-lived transmon qubits and high-Q
2D and 3D resonators has changed the playground, and it is no longer clear what other
kind of hybrid memory devices are needed for short-term quantum memory. Even for
long-term memory, the issue is not clear: with emerging quantum error correction (QEC)
techniques it may be possible to dynamically refresh JJ-cQED systems and prolong
coherence times at will. To achieve long-term static quantum memory, spin ensembles
are still likely candidates, but much development remains.
The current situation for hybrid systems is described in three excellent review and
research articles [224226]. Here we will only briefly mention a few general aspects in
order to connect to the DiVincenzo criteria DV6 and DV7, and to refer to some of the
most recent work.

_5.1. Quantum interfaces for qubit interconversion (DV6)_

The name of the game is to achieve strong coupling between elementary excitations
(e.g. photons, phonons, spin waves, electrons) of two or more different components

26


-----


so that the mixing leads to pronounced sideband structures. This can then be used
for entangling different types of excitations for information storage or conversion from
localised to flying qubits.

_5.1.1._ _Transmon-spin-cQED_ Experimentally, strong coupling between an ensemble
of electronic spins and a superconducting resonator (Fig. 7) has been demonstrated
spectroscopically, using NV centres in diamond crystal [227229] and _Er_ 3+ spins doped
in a _Y_ 2 _SiO_ 5 [230].
Moreover, storage of a microwave field into multi-mode collective excitations of a
spin ensemble has recently been achieved [231,232]. This involved the active reset of the
nitrogen-vacancy spins into their ground state by optical pumping and their refocusing
by Hahn-echo sequences. This made it possible to store multiple microwave pulses at
the picowatt level and to retrieve them after up to 35 _s_ , a three orders of magnitude
improvement compared to previous experiments [232].
The ultimate purpose is to connect qubits to the superconducting resonator bus,
and to use the spin ensemble as a long-lived memory. Such experiments have been
performed, entangling a transmon with a NV spin ensemble [233] via a frequency-tunable
superconducting resonator acting as a quantum bus, storing and retrieving the state of
the qubit. Although these results constitute a proof of the concept of spin-ensemblebased quantum memory for superconducting qubits, the life-time, coherence and fidelity
of spin ensembles are still far from what is needed. Similar results were also achieved
by directly coupling a flux qubit to an ensemble of NV centers without a resonator
bus [234].
Finally, strong coupling between a transmon qubit and magnon modes in a
ferromagnetic sphere has recently been achieved [235, 236], demonstrating magnonvacuum-induced Rabi splitting, as well as tunable magnon-qubit coupling utilising
a parametric drive. The approach provides efficient means for quantum control
and measurement of the magnon excitations and opens a new discipline of quantum
magnonics.

_5.1.2. Transmon-micromechanical oscillator-cQED_ Mechanical oscillators (Fig. 7) can
be designed to have resonance frequencies in the microwave _GHz_ range and achieve
strong coupling to superconducting qubits. Mechanical resonators therefore provide a
new type of quantum mode - localised phonons. However, for this to be useful for
quantum information processing one must be able to cool the mechanical oscillator
to its ground state, to be able to create and control single phonons [237, 238]. It is
then possible to induce Rabi oscillations between the transmon and the oscillator by
microwave driving via motional sidebands, resulting in periodic entanglement of the
qubit and the micromechanical oscillator [239].

_5.1.3. Transmon-SAW_ Surface acoustic waves (SAW) are propagating modes of surface
vibrations - sound waves. Recently, propagating SAW phonons on the surface of a

27


-----


piezoelectric crystal have been coupled to a transmon in the quantum regime (Fig. 8),
reproducing findings from quantum optics with sound taking over the role of light [240].
The results highlight the similarities between phonons and photons but also point to
new opportunities arising from the unique features of quantum mechanical sound. The
low propagation speed of phonons should enable new dynamic schemes for processing
quantum information, and the short wavelength allows regimes of atomic physics to be
explored that cannot be reached in photonic systems [241].
The SAW-approach can be extended [242] to embedding a transmon qubit in a
Fabry-Perot SAW cavity, piezoelectrically coupled to the acoustic field. This then
realises a SAW version of cQED: circuit quantum acoustodynamics (cQAD) [243].

![G_Wendin_Review_of_superconducting_circuits.pdf-27-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-27-0.png)

Figure 8: Propagating surface acoustic wave (SAW) phonons coupled to an artificial atom.
Semi-classical circuit model for the qubit. The interdigital transducer (IDT) converts electrical
signals to SAWs and vice versa. Adapted from [240].

_5.1.4. Transmon-HBAR_ The recent development of bulk acoustic resonators [237,244]
has made possible the experimental demonstration [245] of a high frequency, high-Q,
bulk acoustic wave resonator (high-overtone bulk acoustic resonator) (HBAR) that is
strongly coupled to a superconducting transmon qubit using piezoelectric transduction.
The system was used to demonstrate basic quantum swap operations on the coupled
qubit-phonon system. The _T_ 1 relaxation time of the qubit was found to be 6 _s_ .
Moreover, _T_ 1 and _T_ 2 for the lowest phonon level in the resonator was found to be 17 _s_
and 27 _s_ resp. The analogy to 3D cQED is obvious, but the thickness of the device
is only about 0.5 mm, so it looks more 2D than 3D. It is expected [245] that fairly
straightforward improvements will make cavity quantum acoustodynamics (cQAD) a
novel resource for building scalable hybrid quantum systems.

_5.2. Quantum interfaces to flying qubits (DV7)_

The principle is that of good old radio technology: from the transmitter side, one
achieves low-frequency ( __ ) modulation of a strong high-frequency () carrier (pump)
beam by controlling the amplitude, frequency or phase of the carrier. The modulation is
achieved by mixing the signals in a non-linear device, creating sidebands  __ __ around
the carrier frequency.

28


-----


In the present case, the mixers are different types of electro-optomechanical
oscillators that influence the conditions for transmitting or reflecting the optical carrier
beam. Typically three different oscillators are coupled in series, as illustrated in Fig. 7:
a microwave resonator ( __ _r_ ), a micro/nanomechanical oscillator ( __ _m_ ), and an optical
cavity ( _c_ ), with coupling energies _g_ _rm_ and _g_ _mc_ , resulting in the following standard
Hamiltonian:


 + 1
_H_ =  _h_ _r_ ( _a_ _a_ +



1 ) +  _h_ _m_ ( _b_ + _b_ + 1

2 2



1 ) +  _h_  _c_ ( _c_ + _c_ + 1

2 2



) (22)
2


+ _g_ _rm_ ( _a_ + _a_ + )( _b_ + _b_ + ) + _g_ _mc_ _c_ + _c_ ( _b_ + _b_ + )

The mechanical oscillator changes the frequency of the optical cavity. This is the same
principle as readout: the phase of the reflected carrier carries information about the
state of the reflecting device. Here the phase of the reflected optical beam maps the
state of the mechanical oscillator. Tuning the laser frequency so that  _c_  __ ,
__ __
either sideband is now in resonance with the optical cavity. If the resonance linewidth of
the optical cavity is smaller than __ , then the sideband is resolved and will show a strong
resonance. Adding a (transmon) qubit coupled to the microwave resonator (Fig. 7) one
then has a chain of coupled devices that, if coherent, can entangle the localised qubit
with the optical beam and the flying photon qubits.
To create this entanglement is clearly a _major challenge_ , and coherent coupling
has so far only been achieved to varying degrees between various components. We will
now briefly describe a few technical approaches to the central oscillator components:
piezoelectric optomechanical oscillator [246], micromechanical membrane oscillator

[247250], collective spin (magnon) oscillator [235,236,251253], and SAW [243].

![G_Wendin_Review_of_superconducting_circuits.pdf-28-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-28-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-28-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-28-1.png)

Figure 9: Layout and operation of microwave-to-optical converter using a piezoelectric
optomechanical oscillator. Adapted from [246].

_5.2.1. Microwave-optical conversion: optomechanics_ This approach (Fig. 9) is based
on the established optomechanical devices for modulating light [224], and has been
investigated experimentally [246]. A beam of piezoelectrical material is patterned to
contain a nanophotonic (1D) crystal, localizing light in a region of enhanced vibrational
amplitude.

29


-----


_5.2.2. Microwave-optical conversion: micromechanics_ This approach (Fig. 10) is based
on the well-known technique of modulating reflected light, e.g. to determine the
position of the tip of an AFM probe. The radiation pressure (light intensity) exerts
a ponderomotive force on the membrane (Fig. 10), coupling the mechanical oscillator
and the optical cavity [248]. There are proof-of-concept experimental results showing
coherent bi-directional efficient conversion of _GHz_ microwave photons and _THz_ optical
photons [247]. Moreover, this technique was recently used for demonstrating optical
detection of radiowaves [249].

![G_Wendin_Review_of_superconducting_circuits.pdf-29-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-29-0.png)

Figure 10: Layout and operation of microwave-optical interface using an oscillating
micromechanical membrane [247]. Microwave-to-optical conversion is achieved by pumping
at optical frequency with detuning so as to amplify the sidebands at  __ __ inside the
optical cavity resonance line. Optical-to-microwave conversion is achieved by pumping at MW
frequency __ _p_ with detuning so as to amplify the sidebands at __ _p_ __ __ inside the MW resonator
resonance line. Adapted from [247]

_5.2.3. Microwave-optical conversion: cavity optomagnonics_ The Nakamura group has
been investigating the coupling of microwave photons to collective spin excitations magnons - in a macroscopic sphere of ferromagnetic insulator [235,236,251253]. They
recently demonstrated strong coupling between single magnons in a magnetostatic
mode in the sphere and a microwave cavity mode [251, 252], including bidirectional
conversion [253].

![G_Wendin_Review_of_superconducting_circuits.pdf-29-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-29-1.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-29-2.png](G_Wendin_Review_of_superconducting_circuits.pdf-29-2.png)

Figure 11: Layout and operation of microwave-to-optical converter using an SAW travelling
wave. Adapted from [243].

30


-----


_5.2.4._ _Microwave-optical conversion: SAW_ Shumeiko [243] has presented a theory
for a reversible quantum transducer (Fig. 11) connecting superconducting qubits and
optical photons using acoustic waves in piezoelectrics. The approach employs stimulated
Brillouin scattering for phonon-photon conversion, and the piezoelectric effect for
coupling of phonons to qubits. It is shown that full and faithful quantum conversion is
feasible with state-of-the-art integrated acousto-optics.

31


-----

# **6. Quantum gates**

_6.1. Quantum state time evolution_

In quantum information processing (QIP) one maps classical data on the Hilbert space
of a given quantum circuit, studies the resulting time evolution of the quantum system,
performs readout measurements of quantum registers, and analyses the classical output.
At this level there is no difference between quantum computing (QC) and quantum
simulation (QS).


_Time-evolution operator_ The time evolution of a many-body system can be described
by the Schr odinger equation for the state vector _|_ __ ( _t_ ) __ ,



__
_i_ _h_ 



__ ( _t_ ) =  _H_ ( _t_ ) __ ( _t_ ) _._ (23)
_t_ _|_ __ _|_ __




in terms of the time-evolution operator _U_ ( _t, t_ 0 )




__ ( _t_ ) = _U_ ( _t, t_ 0 ) __ ( _t_ 0 ) _._ (24)
_|_ __ _|_ __


determined by the time-dependent many-body Hamiltonian _H_ ( _t_ ) of the system

  
_H_ ( _t_ ) = _H_ _syst_ + _H_ _ctrl_ ( _t_ ) (25)

describing the intrinsic system and the applied control operations. Gates are the results
of applying specific control pulses to selected parts of a physical circuit. This affects the
various terms in the Hamiltonian by making them time-dependent.

 
For simplicity, _H_ _syst_ can be regarded as time-independent, and _H_ _ctrl_ ( _t_ ) taken to
describe DC and microwave drives controlling the parameters of the total Hamiltonian.
This involves e.g. tuning of qubits and resonators for coupling and readout, or setting


up and evolving the Hamiltonian. In addition, _H_ _ctrl_ ( _t_ ) can introduce new driving terms
with different symmetries. In general, the perturbing noise from the environment can
be regarded as additional time dependence of the control parameters.
For the transmon, the system Hamiltonian takes the form in the RWA (same
notation as in Sect. 4.3):



1

_H_ _syst_ =
__ 2


__ _i_ __ _zi_ +
_i_


_g_ _i_ ( __ _i_ + _a_ + __ _i_ __ _a_ + ) +  _h a_ + _a_ (26)


+ 1


__ _,ij_ ( __ _i_ + __ _j_ __ + __ _i_ __ __ _j_ + ) (27)
_i,j_ ; __


and the control term can be written as



_H_ _ctrl_ ( _t_ ) =



1
_f_ _i_ ( _t_ ) __ _i_ +
_i_ ; __ 2


_h_ _,ij_ ( _t_ ) __ _i_ __ _j_ + _k_ ( _t_ ) _a_ + _a_ (28)
_i,j_ ; __




The time dependent _H_ _ctrl_ ( _t_ ) allows switching on and off or modulating the various terms


in _H_ _syst_ , as well as introducing pulse shapes for optimal control. In Eq. (28), the first
term provides general types of single-qubit gates, the second term describes qubit-qubit
coupling explicitly introduced by external driving, and the third term tuning of the

32


-----


frequency of the oscillator. Moreover, in Eq. (28), the first term allows tuning of the
qubit energies in and out of resonance with the oscillator, making it possible to switch on
and off the qubit-oscillator coupling as well as creating oscillator-mediated qubit-qubit
coupling. In the same way, the third term makes it possible to tune the oscillator itself
in and out of resonance with the qubits.


The solution of Schr odinger equation for _U_ ( _t, t_ 0 ) may be written as


_t_
_U_  ( _t, t_ 0 ) = _U_  ( _t_ 0 _, t_ 0 ) + _H_  ( _t_ __ ) _U_  ( _t_ __ _, t_ 0 ) _dt_ __ (29)

_t_ 0




and in terms of the time-ordering operator _T_ :


_t_

_t_




_U_  ( _t, t_ 0 ) = _T e_  __


_t_ _t_ 0 _H_  ( _t_ __ ) _dt_ __ _,_ (30)


describing the time evolution of the entire many-particle state in the interval [ _t_ 0 _, t_ ].

_U_ ( _t, t_ 0 ) in Eq. 30 is the basis for describing all kinds of quantum information processing,
from the gate model for quantum computing to adiabatic quantum simulation. If the
total Hamiltonian commutes with itself at different times, the time ordering can be
omitted,


_t_

_t_





_i_
_U_  ( _t, t_ 0 ) = _e_ __ 


_t_ 0 _H_  ( _t_ __ ) _dt_ __ _._ (31)


This describes the time-evolution controlled by a homogeneous time-dependent potential
or electromagnetic field, e.g. dc or ac pulses with finite rise times, or more or
less complicated pulse shapes, but having no space-dependence. Moreover, if the
Hamiltonian is constant in the interval [ _t_ 0 _, t_ ], then the evolution operator takes the
simple form


_U_  ( _t, t_ 0 ) = _e_ __ _h_  _i_ _H_  ( _t_ __ _t_ 0 ) _,_ (32)


_h_  _i_ _H_  ( _t_ __ _t_ 0 ) _,_ (32)


describing stepwise time-evolution.
Computation is achieved by sequentially turning on and off 1q and 2q gates, in
parallel on different groups of qubits, inducing effective _N_ -qubit gates.

_6.2. Gate operations_

The time-development will depend on how many terms are switched on in the
Hamiltonian during a given time interval. In the ideal case all terms are switched
off except for those selected for the specific computational step. A single qubit gate
operation then involves turning on a particular term in the Hamiltonian for a specific
qubit, while a two-qubit gate involves turning on an interaction term between two
specific qubits. In principle one can perform direct _N_ -qubit gate operations by turning
on interactions among all _N_ qubits.

_6.3. 1q rotation gates_


1q gates are associated with the time-dependent 1q term of the control Hamiltonian:

_H_ _ctrl_ ( _t_ ) = _i_ ; __ _f_ _i_ ( _t_ ) __ _i_ . Expanding the state vector __ ( _t_ ) in a computational 1q basis,

_|_ __



33


-----


one obtains for a given single qubit,


_|_ __ ( _t_ ) __ =



_i_
_|_ _k_ __ _k_ _|_ _e_ __ 


_t_

_t_




__ _f_ __ ( _t_ __ ) _dt_ __ __ __ _|_ _m_ __ (33)


_a_


For a general control Hamiltonian the __ __ -operators do not commute, and the exponential
cannot be factorised in terms of products of __ _x_ , __ _y_ and __ _z_ terms. To get a product we
must apply the operators sequentially, acting in different time slots. In that case, for a
given __ __ -operator we get


_|_ __ ( _t_ ) __ =


_a_ _m_


_|_ _k_ __ _k_ _|_ _e_ __ __ ( _t_ ) __ __ _|_ _m_ __ (34)


where __ = __ ( _t_ ) =  _h_ _i_ _t_ _t_ 0 _f_ __ ( _t_ __ ) _dt_ __ .

Expanding the exponential,  calculating the _k_ __ __ _m_ matrix elements, and
__ _|_ _|_ __
resumming, one obtains the time evolution in terms of rotation operators _R_ __ ( __ ):


_|_ __ ( _t_ ) __ =


_a_ _m_


_k_ _k_ _R_ __ ( __ ) _km_ _m_ (35)
_|_ __ _|_ _|_ __


where


_R_ _x_ ( __ ) =

_R_ _y_ ( __ ) =

_R_ _z_ ( __ ) =


_cos_ ( _/_ 2) __ _i sin_ ( _/_ 2)
__ _i sin_ ( _/_ 2) _cos_ ( _/_ 2)

_cos_ ( _/_ 2) __ _sin_ ( _/_ 2)
_sin_ ( _/_ 2) _cos_ ( _/_ 2) 

exp( __ _i/_ 2) 0
0 exp( _i/_ 2) 


(36)

(37)

(38)


describing single qubit rotations around the x-, y-, and z-axes.

_6.4. 2q resonance gates_




_6.4.1. iSWAP_ The 2q iSWAP gate can be implemented by using _H_ _ctrl_ for tuning the
energy of one of the qubits onto resonance with the other qubit, thereby effectively

 
turning on the _H_ 12 qubit-qubit interaction in _H_ _syst_ .
Expanding the state vector _|_ __ ( _t_ ) __ in a computational 2q basis, one obtains


_|_ __ ( _t_ ) __ =


_a_ _mn_
_m,n_


_k,l_ _|_ _kl_ __ _kl_ _|_ _e_ __ _i_  _H_ 12 _t_ _|_ _mn_ __ (39)


If the qubits are on resonance ( __ 1 = __ 2 ), then the matrix elements of the 2-qubit
interaction part of the time evolution operator take the form


_kl_ _H_  12 _mn_ = __ _kl_ __ 1 + __ 2 __ + __ 1 __ __ 2 + _mn_ (40)
__ _|_ _|_ __ __ _|_ _|_ __

= __ ( __ _k,m_ 1 __ _l,n_ +1 + __ _k,m_ +1 __ _l,n_ 1 )
__ __

Expanding the exponential function, introducing the matrix elements and resumming
yields


_U_  ( _t_ ) = __ _kl_ _|_ _e_ __ _h_  _i_ _H_  12 _t_ _|_ _mn_ __ = __ _kl_ _|_ _iSWAP_ _|_ _mn_ __ _,_ (41)

34


-----


_cos_ ( _t_ ) __ _i sin_ ( _t_
__ _i sin_ ( _t_ ) _cos_ ( _t_ )


_iSWAP_ =



_,_ (42)






referred to as the iSWAP gate.
Creating an excited _|_ 01 __ state from _|_ 00 __ by a __ pulse, the iSWAP gate describes how
the system oscillates between the _|_ 01 __ and _|_ 10 __ states. The __ _iSWAP_ gate is obtained


the system oscillates between the _|_ 01 __ and _|_ 10 __ states. The _iSWAP_ gate is obtained

by choosing _t_ = _/_ 2,


1 __ _i_
__ _i_ 1


_iSWAP_ =



_,_ (43)






putting the system in a Bell-state type of superposition _|_ __ __ =



( 01 + _i_ 10 ).
2

_|_ __ _|_ __


_6.4.2. CPHASE_ The CPHASE gate can be implemented by making use of the spectral
repulsion from the third level _|_ 2 __ of the transmon, as shown in Fig. 12. One first uses
two-colour __ -pulses to drive both qubits from _|_ 0 __ to _|_ 1 __ , inducing a _|_ 00 _|_ 11 __ transition
(point I). Then tuning one of the qubits rapidly into (near) resonance with the other
one, staying at the crossing of the _|_ 11 __ and _|_ 02 __ levels for a certain time (point II),
produces an interaction-dependent shift __ of the _|_ 11 __ level relative to _|_ 01 + 10 __ . This
induces an iSWAP gate between _|_ 11 __ and _|_ 02 __ .

![G_Wendin_Review_of_superconducting_circuits.pdf-34-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-34-0.png)

Figure 12: Energy level spectra explaining the CPHASE two-transmon resonance gate. The
frequencies of the transmons are controlled by voltages _V_ _L_ and _V_ _R_ applied to CPWs controlling
the flux in the transmon 2-JJ loops (Fig. 6). Keeping _V_ _L_ constant and varying _V_ _R_ produces
the energy level dispersion. The CPHASE gate is produced by moving from point (I) to the
curve crossing point (II), staying for a prescribed time ( _|_ 11 _|_ 02 __ ), and then moving back to
(I). The frequency shift __ = _f_ 10 + _f_ 01 __ _f_ 11 (Fig. 12b) makes the phase of the _|_ 11 __ level evolve
more slowly that of _|_ 01 + 10 __ , producing a controlled phase gate. Adapted from [189].

To see this, one expands the state vector in an extended computational basis:


_|_ __ (0) __ =


_a_ _mn_ _mn_
_m,n_ _|_ __

35


-----


= _a_ 00 00 + _a_ 01 01 + _a_ 10 10 + _a_ 20 20 + _a_ 11 11 + _a_ 02 02 (44)
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __


and calculates the matrix elements __ _kl_ _|_ _H_ _|_ _mn_ __ (like in Sect. 6.4.1). The resulting energy
level spectra in Fig. 12 show an avoided level crossing and a frequency shift __ of the _|_ 11 __
level due to repulsion from the _|_ 02 __ level, as shown in detail in Fig. 12b.
In this representation the evolution operator is diagonal, with the result that


_e_ __ 01 0 0
0 _e_ __ 10 0
0 0 _e_ __ 11 ( _t_


_U_ ( _t_ ) =


(45)


with



 __ 1
__ 01 = 01 _H_ 01 _t_ =
__ _|_ _|_ __ __ 2



1 __ 2

_t_ ; __ 10 = 10  _H_ 10 _t_ =
2 __ _|_ _|_ __ __ 2



_t_ (46)
2



__ 1 + __ 2


__ 11 ( _t_ ) = 11 _H_ 11 _t_ =
__ _|_ _|_ __ __ 2


_t_
_t_ + _h_

0





__ ( _t_ )) _dt_ (47)
0


In the experiment, the 11-02 splitting is determined by the time-dependent bias tuning
voltage _V_ _R_ ( _t_ ) in Fig. 12. If __ 1 = __ 2 (point II), then


After time t such that



__
__ 01 = __ 10 = __



__ _t_

_t_ ; __ 11 ( _t_ ) = _ t_ + _h_
2 __ 0




__ ( _V_ _R_ ( _t_ )) _dt_ (48)
0



__
__ 01 = __ 10 = __



_t_ = 2 __ (49)
2


then the 11 state has rotated twice, and the phase is given by 4 __ + _h_ 0 _t_ __ ( _V_ _R_ ( _t_ )) _dt_
__

1 0 0 0 


_t_

; __ 11 ( _t_ ) = _h_

0

 







_U_ ( _t_ ) =



__ ( _V_ _R_ ( _t_ )) _dt_ (50)
0


_e_ _i_ 11 ( _t_


At this point, the excursion of the bias voltage will decide the integrated strength needed
for achieving __ 11 ( _t_ ) = __ , providing the CPHASE gate (Fig. 13a):


_CPHASE_ = _CZ_ = _Ctrl R_ _z_ ( __ ) =


(51)

0



1 



__




_6.4.3._ _CNOT_ The CNOT gate can be expressed in terms of CPHASE and two
Hadamard gates, as commonly implemented in transmon circuits (Fig. 13b):


_CNOT_ = _CX_ = _Ctrl R_ _y_ ( __ ) =


(52)


The first H-gate changes from the z- to the x-basis, and the second H-gate transforms
back.

36


-----


_6.4.4. Controlled rotation_
CPHASE is a special example of the general controlled Zrotation - Ctrl-Z( __ ) - gate in Eq. (51) and Fig. 13c, allowing one to control time evolution
and (Fig. 13d) to map states to ancillas for phase estimation,


_6.4.5. 2q time evolution_ We now have the tools to describe the time evolution operator
corresponding to 2-qubit interaction terms. The parts of the Hamiltonian with __ _z_ __ _z_

__ __
products, _U_ = _exp_ [ _i_ 2 __ _z_ __ _z_ ] can be implemented by a quantum circuit of the form
__ __


products, _U_ = _exp_ [ _i_ 2 __ __ _z_ __ _z_ ] can be implemented by a quantum circuit of the form
__ __ __

shown in Fig. 13e [54]. Operators like _exp_ [ _i_ 2 __ _x_ __ _x_ ] and _exp_ [ _i_ __ 2 __ _z_ __ _x_ ] can be
__ __ __ __


2 __ __ _x_ __ _x_ ] and _exp_ [ _i_ __

__ __



__ 2 __ _z_ __ _x_ ] can be

__


![G_Wendin_Review_of_superconducting_circuits.pdf-36-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-36-0.png)

Figure 13: Circuits for implementation of (a) CPHASE; (b) CNOT; (c) Ctrl-Z( __ ), __ arbitrary;
(d) basic circuit for phase estimation using an ancilla (top qubit); (e) the _U_ = _exp_ [ _i_ 2 __ __ _z_ __ _z_
__ __

operator; (f) a controlled version of (e) for controlled time evolution and phase estimation (top
qubit).


Figure 13: Circuits for implementation of (a) CPHASE; (b) CNOT; (c) Ctrl-Z( __ ), __ arbitrary;
(d) basic circuit for phase estimation using an ancilla (top qubit); (e) the _U_ = _exp_ [ _i_ 2 __ __ _z_ __ _z_
__ __


generated by adding a number of 1q-rotation gates. Moreover, Fig. 13f represents a
controlled version of Fig. 13e for controlled time evolution and phase estimation.

_6.5. 2q gates induced by microwave driving_

The flux-tunability of transmons make them sensitive to flux noise, resulting in
decoherence. One approach is therefore to use fixed-frequency transmon qubits,
replacing the frequency-tuning squid by a single JJ. This is also an important design
for arrays of 3D transmon qubits where direct access for tuning individual qubits may
be difficult or impossible.
The generic approach for coupling non-linear oscillators is to use electromagnetic
driving fields to induce parametric coupling with tunable strength by creating a
spectrum of sidebands bridging frequency gaps. In this way it is possible to entangle
superconducting qubits with different frequencies using (i) fixed linear couplings, (ii)
only microwave control signals, and (iii) tunable effective interaction strengths. Recently
these methods have been applied experimentally through a variety of schemes based on

37


-----


two different principles: (i) driving qubits, and (ii) driving coupling resonators, e.g. a
tunable bus.

_6.5.1. Driving qubits_

_Cross resonance (CR) 2q gates_ The CR scheme [254258] exploits already present
nonlinearities to achieve tunable coupling, circumventing the need for nonlinear coupling
elements. The CR two-qubit gate scheme irradiates one of the qubits at the transition
frequency of the other qubit. In the presence of this cross-resonant microwave drive,
an effective coupling emerges between the two qubits whose strength increases linearly
with the ratio (drive amplitude)/(difference frequency).
The CR-coupling of two qubits, Q1 and Q2, can be understood in the dressed state
picture of quantum optics [254, 255]. Under CR driving, the central transition at the
irradiation frequency of the driven dressed Q1 system is matched to the bare transition
of the undriven Q2. One thus creates a resonance between the central feature of the
Mollow triplet on Q1 and the bare transition of Q2. The tunability of the effective
coupling strength _G_ results from the evolution of the dressed Q1 eigenstates as the field
amplitude _F_ is adjusted [254,255]:


_H_ _eff_ = _g_ ( _F_ ) __ _z_ 1 __ _x_ 2 _,_ (53)

which is related to the CNOT gate by one additional local _/_ 2 rotation of each qubit.
In addition to the CR scheme, one approach is to create a microwave-activated
conditional-phase gate (MAP) [259] based on driving the _|_ 03 __ and _|_ 12 __ transmon states
into resonance. A general problem with driving qubits is that the couplings may depend
sensitively on the qubit level structure. For transmon qubits the CR scheme is limited
by the weak anharmonicity of the transmon, and the MAP scheme employs specific
higher excited states of the transmon. These schemes may therefore be challenging to
scale up to many qubits.

_6.5.2. Driving a tunable bus_ Attaching a SQUID to the end of a coplanar wave-guide
resonator (CPW) makes it possible to vary the boundary condition (effective length)
and create a flux-tunable resonator [260,261] and to couple qubits [262,263]. In [262],
fixed-frequency qubits with different frequencies were coupled by successively bringing
each qubit quasi-statically in and out of resonance with the tunable CPW, effectively
creating multi-qubit gates. In [260,263], the CPW was rapidly tuned (chirped) to create
interference and beating of microwave emission, which in principle could dynamically
couple qubits [263]. Alternatively, one can drive the resonator at high frequency to create
sideband structure and dynamic parametric coupling between qubits. This is presently
at the focus of extensive and promising research [141,220,264266], potentially providing
multi-qubit gate architectures for scaled-up systems. A recent proposal is based on the
_Dynamical Casimir Effect_ [266]: A SQUID is then connected to the midpoint of a CPW
resonator that is connected to transmon qubits at both ends, varying the coupling

38


-----


between the two halves by flux tuning. Driving the SQUID at microwave frequencies
emits pair of photons that can entangle the qubits [266].

_Resonator-induced phase gate (RIP)_ In the resonator-induced phase gate (RIP) scheme

[141,220,264] fixed-frequency transmons are statically coupled to the same bus resonator
driven at the difference frequency of two qubits.
In a two 2D-transmon setup [220], parametrically oscillating a flux-tunable bus
qubit (similar to a combination of the qubit-qubit couplings in Figs. 6b,c) at the
qubit-qubit detuning enables a __ + __ + __ __ + resonant exchange (XX+YY) interaction.
__ __
The interaction is said to implement a 183 _ns_ two-qubit iSWAP gate between qubits
separated in frequency by 854 _MHz_ with a measured average fidelity of 0.98 from
interleaved randomized benchmarking. This gate may be an enabling technology for
surface code circuits and for analog quantum simulation [220].
In a 3D-transmon-cQED setup with four superconducting qubits [141], RIP gates
are experimentally implemented between pairs of qubits, demonstrating high-fidelity CZ
gates between all possible pairs of qubits. The qubits are arranged within a wide range
of frequency detunings, up to as large as 1.8 _GHz_ . This setup was used to generate a
four-qubit Greenberger-Horne-Zeilinger (GHZ) type of state [141].

_Mlmer-Srensen (MS) 2q gate_ In ion traps, the qubits (ions) are naturally coupled
by collective vibrational modes generating a sideband structure [267]. The MlmerSorensen (MS) gate [268270] is a single-step 2-qubit entangling gate _|_ 00 _|_ 11 __ driven
by 2-tone 2-photon excitation assisted by collective (vibrational) modes, providing
resonant intermediate states with sideband structure. It looks like Rabi driving of a
single qubit, coupling the 0 _,_ 1 _ph_ and 1 _,_ 0 _ph_ levels, 0 _,_ 1 _ph_ 1 _,_ 0 _ph_ _ _ _x_ 1
_|_ __ _|_ __ _|_ _ |_ __ __
extended to resonant 2-photon direct driving of two qubits, coupling the _|_ 00 _,_ 2 _ph_ __
and _|_ 11 _,_ 0 _ph_ __ levels, _|_ 00 _,_ 2 _ph_ _ |_ 11 _,_ 0 _ph_ __ giving rise to an effective 2-qubit interaction
_ _ _x_ 1 __ _x_ 2 .

_Multiqubit gates_ can be implemented in several ways: (i) sequentially, by series of
1q and 2q gates to yield CCNOT (Toffoli) or CCZ [120, 271, 272]; (ii) by a singleshot optimised pulse sequence [273, 274]; or (iii) by single-shot collective excitation
via bus dynamics. The state of the art of (iii) is currently defined by an ion-trap
experiment entangling 14 qubits via a Mlmer-Srensen (MS) gate [267]. The MS gate
can be generalised to direct Rabi-like driving of N qubits, coupling the _|_ 0 _..._ 00 _, Nph_ __ and
_|_ 1 _..._ 11 _,_ 0 _ph_ __ levels, leading to an effective N-qubit interaction _ _ _x_ 1 __ _x_ 2 _....... _ _xN_ . There
is a recent proposal for implementing MS gates in transmon-cQED [265] by driving a
SQUID to create sideband structure, as discussed above, and simultaneously driving the
qubits with two microwave tones. Also, there are recent proposals how to implement
controlled multi-qubit gates by multi-tone microwave driving of the bus, the control
qubit, and the target qubits, in cQED [275278].

39


-----


Finally we mention two very different recent approaches to gate construction and
time evolution: a genetic algorithm (GA) approach to decomposing the time evolution
operator in a series of high-fidelity gates adapted to the system under study [279]; and a
supervised-learning approach to tuning a 4-spin circuit to performing a 3q-Toffoli gate
in a feed-forward style without external control [280].

_6.6. Gate synthesis and universal sets of gates_

An important problem in quantum computing is how to decompose an arbitrary unitary
operation in a sequence of standard elementary gates from a gate library [281]. The
Clifford stabiliser group can be generated by three elementary gates: two single-qubit
gates, the Hadamard gate H, and the S-gate (phase gate),



1
_H_ =


_S_ =


(54)


__ 1


and a two-qubit gate, e.g. CNOT (Eq. (52)) or CPHASE (Eq. (51)). This constitutes a
standard set of Clifford gates _{_ _H, S, CNOT_ _}_ . Adding a non-Clifford gate, such as the
T gate:


_T_ =


_e_ _/_ 4


(55)


forms a universal set _{_ _H, S, CNOT, T_ _}_ , and makes it possible to generate all quantum
circuits, i.e. in principle to perform universal, but not necessarily efficient (poly-time),
quantum computing.
Any quantum circuit of operations can be described by a sequence of gates from
this finite universal set. For the specific case of single qubit unitaries the Solovay-Kitaev
theorem [282] guarantees that this can be done efficiently, involving only a polynomial
number of gates. For a general quantum circuit, it may take an exponential number of
gates to synthesise the operation. Recently Bravyi and Gosset [202] presented a new
algorithm for classical simulation of quantum circuits over the universal Clifford + T
gate set which is polynomial in the number of qubits and the number of Clifford gates but
exponential in the number of T gates. However, the exponential scaling was sufficiently
mild that it was possible to use the algorithm to simulate classically a medium-sized
quantum circuit dominated by Clifford gates, namely a hidden-shift quantum algorithm
with 40 qubits, a few hundred Clifford gates, and nearly 50 T gates [202].

40


-----

# **7. Quantum state preparation and characterisation**

_7.1. Quantum state characterisation_

Quantum state characterisation and quantum computing are two sides of the same coin.
Both involve application of long series of gates. The difference lies in the purpose of the
protocol: characterisation of a quantum state, or solution of a computational problem.
Tomography is all about visualisation of quantum states and processes, which means
measurement and presentation of large quantities of quantum information.
In the general case, the N-qubit density matrix is defined by (2 _N_ ) 2 matrix elements,
requiring 2 2 _N_ __ 1 independent measurements for characterization, based on an ensemble
of replicas of the state in question. In the 2-qubit case, 15 matrix elements have to be
determined via a set of 15 measurements at different angles. In solid-stated devices
the integrated detectors cannot be rotated. Therefore, measurements are typically
performed by rotation gates applied to the various qubits before measurement. The
data are then used to calculate the elements of the density matrix. The discussion is
of course not limited to two-level systems: the transmon is a multi-level system and a
single qutrit 3-level density matrix was investigated in [283].
For large-scale quantum circuits and systems to be trustworthy, it is all-important
to be able to verify the functionality and performance at various levels by appropriate
measurements and data analysis. Full characterisation via quantum state tomography
(QST) and quantum process tomography (QPT) [284287] scales exponentially with the
number of qubits - an NP-hard problem - and is only possible for small systems. For
up to three qubits, QST and QPT are well-established tools for characterising quantum
states, gates and processes, as demonstrated by a large number of recent applications
involving superconducting circuits (see e.g. [272,288290]).
For larger systems, however, full QPT becomes impractical, and methods have to
be developed for reducing the information needed, e.g. via _randomised benchmarking_
(RB) (a randomised QPT procedure, applying a random sequence of gates) [291293],
compressed sensing QPT (CSQPT) (exploiting sparsity of matrices) [294298], and
adaptive Bayesian quantum tomography [299301]
The rapid scaling up of transmon systems will make reduced-information methods
indispensable, and there has already been a number of recent applications of RB and
twirling protocols [302307] and CSQPT [298] to superconducting circuits. While
standard QPT provides information about a single gate, RB gives a measure of the
accumulated error over a long sequence of gates. Standard QPT is limited by errors in
state preparation, measurement and one-qubit gates and suffers from inefficient scaling
with number of qubits. RB yields estimates of the computationally relevant errors
without relying on accurate state preparation and measurement. Since it involves long
sequences of randomly chosen gates, it also verifies that error behaviour is stable when
used in long computations. _Interleaved_ RB (IRB) is a scalable protocol for estimating
the average error of individual quantum computational gates. IRB involves sequentially
mixing Clifford and Pauli gates. The technique takes into account both state preparation

41


-----


and measurement errors and is scalable in the number of qubits [32,308310]. _Twirling_
provides useful partial information of a quantum channel by averaging the channel
under the action of a set of unitaries [311, 312], pre-multiplying the input state by
an operation, running the original process, post-multiplying by the inverse operation,
and finally averaging over a set of operations. Randomly applying the Pauli operators
with uniform probability to any density operator - Pauli twirling - gives the maximally
mixed state. Twirling is often a part of the abovementioned RB protocols to introduce
averaging.

_7.2. Quantum Supremacy characterisation_

In just a few years, quantum computers without error correction are expected to be
able to approximately sample the output of random quantum circuits that state-of-theart classical computers cannot simulate [313]. In this spirit, Boixo et al. [2] study the
computational task of sampling from the output distribution of pseudo-random quantum
circuits composed from a universal gate set, a typical benchmarking problem, and
introduce the concept of Cross Entropy (CE) to characterise Quantum Supremacy. The
Shannon entropy _S_ ( _A_ ) = _a_ _P_ ( _A_ _a_ ) _lnP_ ( _A_ _a_ ) is a measure of the inherent uncertainty
__
of a single random variable _A_  . The Cross Entropy _CE_ ( _A_ ; _B_ ) = _x_ _P_ ( _A_ _x_ ) _lnP_ ( _B_ _x_ ) is
__
a _measure of inaccuracy_ [314] and gives the average number of bits needed to identify 
events that occur with probability _P_ ( _A_ _x_ ), if a coding scheme is used that is optimal for
the probability distribution _P_ ( _B_ _x_ ) [315].
Boixo et al. [2] consider a 7 x 6 qubit 2D lattice with gate depth 25, close to
the limit of present classical computers (7 x 7 qubits). They show how to estimate
the cross entropy between the sampled output distribution _P_ ( _A_ ) of an experimental
implementation of a random quantum circuit providing quantum chaos, and the ideal
output distribution _P_ ( _B_ ) simulated by a supercomputer, and argue that the cross
entropy is closely related to the circuit fidelity. If the experimental quantum device
achieves a cross entropy surpassing the performance of the state-of-the-art classical
competition, this will be a first demonstration of Quantum Supremacy [2,315] .
A crucial aspect of a near-term Quantum Supremacy proposal is that the
computational task can only be performed classically through direct simulations with
cost that is exponential in the number of qubits. Quantum Supremacy can be claimed
if the theoretical estimates are in good agreement with the experimental extrapolations.

_7.3. Multi-qubit state preparation_


_7.3.1._ _Bell states_ Bell state preparation and characterisation represent pioneering
experiments [116, 189]. By now these experiments are routine, and focus is rather
on multi-qubit entangled states for QEC and QIP.
For the double-excitation Bell state __ = __ 1 2 ( 00 + 11 ), the density matrix is
_|_ __ _|_ __ _|_ __

42


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-42-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-42-0.png)

Figure 14: Bell states. The Hadamard gate creates superposition states _|_ 0 _|_ 0 __ + _|_ 1 __
and _|_ 1 _|_ 0 _|_ 1 __ , which allows the CNOT gate to create 2q-superposition Bell states: (a)



( 00 + 11 ); (b)
2

_|_ __ _|_ __



( 01 + 10 ).
2

_|_ __ _|_ __


given by



1
__  = ( 00 + 11 )( 00 + 11 ) = 1

2 _|_ __ _|_ __ __ _|_ __ _|_ 2


(56)


Figure 15 shows characterisation of maximally entangled GHZ-type states with five
capacitively coupled Xmon qubits [32] via quantum state tomography (QST). The Bell

![G_Wendin_Review_of_superconducting_circuits.pdf-42-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-42-1.png)

Figure 15: Quantum state tomography (QST) and generation of GHZ type of states. Top row:
Real part of the density matrix for the N = 2 Bell state and the N = 3, 4 and 5 GHZ states,
measured by quantum state tomography. Ideal density matrix elements are transparent, with
value 0.5 at the four corners. Bottom row: Algorithm used to construct the states. Adapted
from [32].


state density matrix is experimentally demonstrated in the leftmost panel of Fig. 15,
showing the characteristic four corner pillars. (Note that Song et al. [40] recently
published tomographic results for a 10-qubit GHZ state).
For the single-excitation Bell state __ = __ 1 2 ( 01 + 10 ), the density matrix is given
_|_ __ _|_ __ _|_ __

43


-----


by



1
__  = ( 01 + 10 )( 01 + 10 ) = 1

2 _|_ __ _|_ __ __ _|_ __ _|_ 2


(57)


spanning a different part of Hilbert space than the double-excitation Bell state.


_7.3.2. GHZ states_ For the triple-excitation GHZ state __ = __ 1 2 ( 000 + 111 ), the
_|_ __ _|_ __ _|_ __

density matrix is given by



1
__  = ( 000 + 111 )( 000 + 111 ) (58)

2 _|_ __ _|_ __ __ _|_ __ _|_

corresponding to the corner pillars in the second panel in Fig. 15.


_7.3.3. W-states_ For the 3-qubit single-excitation Werner W-state, _|_ __ __ =


_7.3.3. W-states_ For the 3-qubit single-excitation Werner W-state, __ = __ 1 3 ( 001 +
_|_ __ _|_ __

_|_ 010 __ + _|_ 100 __ ), the density matrix is given by



1
__  =



( 001 + 010 + 100 )( 001 + 010 + 100 ) (59)
3 _|_ __ _|_ __ _|_ __ __ _|_ __ _|_ __ _|_


The form of the density matrix is illustrated by the experimental results shown in
Fig. 16 [316] (cf. the N=3 GHZ state in Fig. 15).

![G_Wendin_Review_of_superconducting_circuits.pdf-43-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-43-0.png)

Figure 16: Tomography of the W-state [316]. Left: Real part of the density matrix. Right:
Pauli set from quantum process tomography. Adapted from [316].

_7.3.4._ _Generating Bell states by parity measurement_ Measurement provides an
important way to prepare quantum states. Figure 17 shows a way to prepare entangled
states by parity measurement [33]. The Hadamard gates generate the two-qubit product
state _|_ 00 __ + _|_ 01 __ + _|_ 10 __ + _|_ 11 __ . Adding the ancilla, the three-qubit state becomes
_|_ 000 __ + _|_ 010 __ + _|_ 100 __ + _|_ 110 __ . After applying the CNOT gates, the state (at the dashed
line) is given by _|_ 000 __ + _|_ 011 __ + _|_ 101 __ + _|_ 110 __ = [ _|_ 00 __ + _|_ 11 __ ] _|_ 0 __ +[ _|_ 01 __ + _|_ 10 __ ] _|_ 1 __ , representing
a sum of Bell pairs with opposite parities. Measurement of the state (parity) of the
ancilla collapses the state into one of the Bell states. The entanglement process can be
made deterministic by feedback control, inducing a bit flip on demand if the unwanted
parity is detected, as demonstrated by Saira _et al._ [33].

44


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-44-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-44-0.png)

Figure 17: Entanglement by parity measurement. The state at the dashed line is given by

[ _|_ 00 __ + _|_ 11 __ ] _|_ 0 __ + [ _|_ 01 __ + _|_ 10 __ ] _|_ 1 __ . Projective measurement of the ancilla collapses the state into
one of the Bell states [33]. The information about the state of the ancilla can be used for
deterministic entanglement.

_7.4. Teleportation_

![G_Wendin_Review_of_superconducting_circuits.pdf-44-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-44-1.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-44-2.png](G_Wendin_Review_of_superconducting_circuits.pdf-44-2.png)

Figure 18: Quantum circuits for teleportation. Left: (a) Generic standard circuit. (b)
The first application with superconducting 2D transmon-cQED and FPGA control of readout
and feedforward gates [190]. Right: The hardware circuit used in the experiment. Adapted
from [190].

_7.4.1._ Teleportation is a fundamental QIPC protocol it allows quantum states to be reconstructed in distant places given a coherent _Teleportation of states_
quantum communication channel and additional classical channels for sending control
information. Teleportation is a fundamental milestone that has to be passed by any
competitive technology [317,318].
The successful demonstration of teleportation with a transmon circuit (Fig. 18) [190]
therefore represents a very important step for superconducting circuits, even though
it only involved transfer over a distance of a millimeter between two qubits on
the same chip, limited by the length of the microwave bus resonator. It remains to
perform communication between distant qubits (cf. Ref. [319]), requiring long microwave
transmission links, or optical links made possible by MW-optical interfaces.

45


-----


_7.4.2. Teleportation of entanglement_ This is an extension of the teleportation protocol
- called entanglement swapping - entangling two independent qubits that never
interacted in the past [320,321]. The quantum circuit is shown in Fig. 19.

![G_Wendin_Review_of_superconducting_circuits.pdf-45-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-45-0.png)

Figure 19: Entanglement swapping. The protocol first creates two independent entangled
pairs, applying CNOT gates to (Q1,Q2) and (Q3,Q4), and then further applies a CNOT gate
to entangle Q2 and Q3. This results in a special 4-qubit entangled state, and projective
measurement of Q2 and Q3 provides classical information how to create an entangled pair
(Q1,Q4) at a distant location, given that the states of qubits Q1 and Q4 are available.

As a simple example, consider the input state _|_ 0000 __ . The two first Hadamard and
CNOT gates then create a product of two Bell states at (a): ( _|_ 00 __ + _|_ 11 __ )( _|_ 00 __ + _|_ 11 __ ) =
_|_ 0000 __ + _|_ 0011 __ + _|_ 1100 __ + _|_ 1111 __ . Applying a CNOT gate to Q2, Q3 and a Hadamard
gate to Q2 results in (b): ( _|_ 0000 __ + _|_ 1001 __ ) + ( _|_ 0011 __ + _|_ 1010 __ ) + ( _|_ 0100 _|_ 1101 __ ) +
( _|_ 0111 _|_ 1110 __ ). Performing a Bell measurement of Q2 and Q3 then projects the state
with probability 0 _._ 25 to one of the following entangled (Q1,Q4) Bell pairs:


00 _|_ 00 __ + _|_ 11 __ (60)


01 _|_ 01 __ + _|_ 10 __ (61)


10 _|_ 00 _|_ 11 __ (62)


11 _|_ 01 _|_ 10 __ (63)


The measurement entangles the remaining coherent qubits, and the classical 2-bit
information tells exactly what Bell state was created. This at the core of a repeater
protocol. Heinsoo _et al._ [192] have implemented the circuit in Fig. 19 with a 4-transmon
circuit (similar to Fig. 18), measuring Q2, Q3 and identifying the four Bell states via
quantum state tomography of Q1, Q4.

_7.5. Distillation of entanglement_

The purpose of entanglement distillation is to extract a maximally entangled state from
a collection of less entangled states. This can be used as an entanglement resource, e.g.
for repeaters in quantum communication [322]. The distillation concept applies to both
pure and mixed states.

46


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-46-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-46-0.png)

Figure 20: Distillation of entanglement of two partially entangled pairs, __ 12 _in_ and __ 34 _in_ . The
4-qubit state at (a) is a product of two independent pairs. In contrast, the 4-qubit state __ 1234
at (b) is not factorisable at all, in general. Measurement of Q3,Q4 projects out a 2-qubit state,
with two different outcomes: (Q3,Q4) = (0,0) __ 12 _out_ 1 and (Q3,Q4) = (1,1) __ 12 _out_ 2 . Both
__ __
represent superpositions of Bell states. The instance of identical input pairs is very special,
(0,0) producing a state with low concurrence _C_ 1 _< C_ _in_ , and (1,1) producing a Bell state state
with _C_ 2 = 1.


A general two-qubit state can be written as __ = _a_ 0 00 + _a_ 1 01 + _a_ 2 10 + _a_ 3 11 . A
_|_ __ _|_ __ _|_ __ _|_ __
measure of entanglement is the Concurrence: _C_ = 2 _a_ 0 _a_ 3 _a_ 1 _a_ 2 . For a product state,
_|_ __ _|_
_C_ = 0, which can be achieved in a number of ways. For a Bell state, on the other hand,
_C_ = 1.
An example of a distillation quantum circuit is shown in Fig. 20. Two partially
entangled and independent pairs of input states __ 12 and __ 34 :
__ 12 _in_ = [cos( __ 12 __ ) 00 + sin( __ 12 __ ) 11 ]; _C_ = sin( __ 12 __ ) (64)

4 _|_ __ 4 _|_ __ 2

  _in_  __ __ __
 __ 34 = [cos( __ 34 ) 00 + sin( __ 34 ) 11 ]; _C_ = sin( __ 34 ) (65)



) 00 + sin( __ 12
4 _|_ __



) 11 ]; _C_ = sin( __ 12
4 _|_ __


2 ) (64)


__ 34 _in_ = [cos( __ 34





) 00 + sin( __ 34
4 _|_ __



) 11 ]; _C_ = sin( __ 34
4 _|_ __


2 ) (65)


are entangled by two CNOT gates, creating a 4-qubit entangled state __ 1234 at (b).
Introducing __ 12 + __ 34 = 2 __ and __ 12 __ __ 34 =  __ one obtains



__
__ 1234 = [cos( __
_|_ __



__ 4 ) + cos( __


2 )] _|_ 0000 __ + [sin( __


2 ) __ sin( __


4 )] _|_ 0011 __



__
+[sin( __



__ 2 ) + sin( __


4 )] _|_ 1111 __ + [cos( __


4 ) __ cos( __


2 )] _|_ 1100 __ (66)


Performing a Bell measurement of Q3 and Q4 results in (0,0) or (1,1) outcomes
with equal probability, and projects the 4q-qubit state to one of two different entangled
2-qubit (Q1,Q2) Bell pairs (not normalised):


(0 _,_ 0) __ 12 _out_ 1
__

__
= [cos(  __





__
= [cos( __



__ 4 ) + cos( __


2 )] _|_ 00 __ + [cos( __


4 ) __ cos( __


2 )] _|_ 11 __ (67)


_C_ 1 = _|_ [cos 2 ( __ __



__ 2

4 ) __ cos ( __


2 )] _/_ [cos 2 ( __



2
4 ) + cos ( __


2 )] (68)


(1 _,_ 1) __ 12 _out_ 2
__




47


-----



__
= [sin( __



__ 2 ) __ sin( __


4 )] _|_ 00 __ + [sin( __


2 ) + sin( __


4 )] _|_ 11 __ (69)


_C_ 2 = _|_ [sin 2 ( __ __



__ 2

2 ) __ sin ( __


4 )] _/_ [sin 2 ( __



2
2 ) + sin ( __


4 )] _|_ (70)


In the case of identical input states ( __ = 0), investigated experimentally by
Oppliger _et al._ [193],


_C_ 1 = _|_ sin 2 ( __ __



__ 2 ) _/_ [1 + cos 2 ( __


2 )] _|_ (71)


_C_ 2 = 1 _,_ __ __ = 0 (72)


Of the two resulting entangled pairs, the (0,0) outcome produces a less entangled __ 12 _out_ 1
output state than the input __ 12 state, while the (1,1) outcome produces a fully entangled
__ 12 _out_ 2 Bell state with probability _P_ _S_ = 0 _._ 5 sin 2 ( __ __ 2 ), as demonstrated experimentally

[193].
If the input states are not identical ( __ __ = 0), there is a new dimension, and one
must evaluate the concurrence as a functions of __ 1 and __ 2 , _C_ ( __ 1 _, _ 2 ).

48


-----

# **8. Quantum state protection**

_8.1. Quantum control_

_Quantum optimal control_ [323] is essentially a question of controlling qubit driving
and time evolution via pulse shaping. The quantum system to be controlled is modeled

 
by unperturbed and control Hamiltonians _H_ and _H_ _ci_ with _u_ _i_ ( _t_ ) the control fields (e.g.
microwave driving fields) to be shaped:


 
_H_ := _H_ +




_u_ _i_ ( _t_ ) _H_ _ci_ (73)


Pulse shaping [324326] can be used to reduce single-qubit gate errors arising from the
weak anharmonicity of transmon superconducting qubits [283,327329].
Motzoi et al. [330] developed optimal control methods for rapidly time-varying
Hamiltonians, in the form of a numerical method to find optimal control pulses that
account for the separation of timescales between the variation of the input control fields
and the applied Hamiltonian. The simulation of the quantum evolution is accurate on
the timescale of the fast variation in the applied Hamiltonian.
Egger and Wilhelm [331] have recently developed adaptive hybrid optimal quantum
control for imprecisely characterized systems (Ad-HOC). The method combines openand closed-loop optimal control by first performing a gradient search towards a nearoptimal control pulse and then an experimental fidelity estimation with a gradientfree method. For typical settings in solid-state quantum information processing, AdHOC enhances gate fidelities by an order of magnitude, making optimal control theory
applicable and useful.

_8.2. Feedforward control_

Feedforward control means reading out information from a qubit, or group of qubits,
and sending the classical information at a later time (forward) to a device that
controls another group of (distant) qubits. Teleportation is a typical example of strong
(projective) measurement and digital feedforward control (Fig. 18) [190].

_8.3. Feedback control_

Feedback control differs from feedforward control in that the measured classical control
information is fed back to the same group of qubits via a classical feedback loop (of
course still forward in time).

_8.3.1. Digital feedback control_ involves strong (projective) measurement on the device
to be controlled, classical processing using fast electronics (FPGA), and finally communication of classical signals back to the device to operate digital quantum gates [332],
e.g. to reset a qubit [171,333], or to create deterministic entanglement by parity measurement and feedback [334].

49


-----


_8.3.2. Analogue feedback control_ involves weak (non-projective) measurement on the
device to be controlled, classical processing using fast electronics (FPGA), and finally
communication of classical signals back to the device to counteract the disturbance, e.g.
in order to stabilise Rabi oscillations [335337] or quantum trajectories [338344].

_8.3.3._ _Measurement and back-action_ is a continuous process with speed controlled
by the interaction strength between the system and the measurement device. This
means that the collapse of the wave function, i.e. the separation into distinguishable
projections, has a time scale, from weak (slow) to strong (fast) measurement [345,346].
There is a connection between information gain and back action, and the effects of back
action can be undone under the right circumstances [347350].
Groen _et al._ [350] performed a two-step indirect measurement of a transmon
qubit with tunable measurement strength by partially entangling the qubit with an
ancilla qubit (weak measurement), followed by a projective ancilla measurement using
a dedicated resonator (strong, projective measurement). This revealed the back-action
of the measurement on the qubit as a function of qubit-ancilla interaction strength and
ancilla measurement basis. Nonclassical weak values were observed upon conditioning
ancilla measurements on the outcome of a projective measurement of the qubit.
Monitoring a quantum state by weak measurements also makes it possible
to uncollapse quantum states and achieve decoherence suppression by quantum
measurement reversal [351354]

_8.4. Quantum networks and machine learning_

Artificial intelligence (AI) and machine learning (ML) represent frontlines in classical
computer science. Quantum machine learning (QML) [355] is now of great and
increasing interest in QIP [274, 355361], in addition to classical ML optimisation
processes of quantum hardware [280] and software [199, 362]. Machine learning is an
adaptive dynamical data-driven process where a computer code is modified by training learning how to provide an optimal solution to a given task according to certain criteria.
The main processes are: supervised learning, unsupervised learning, and reinforcement
learning. In all cases, the program code is modified in response to the training.
In _supervised learning_ , the machine adapts in response to sets of already classified
(labeled) training data and feedback. In _unsupervised learning_ , the machine develops the
ability to classify unlabeled data without feedback, grouping data into different clusters
(without necessarily understanding what the clusters represent). In _reinforcement_
_learning_ the machine selects a series of actions depending on feedback (reward) from
the environment. To achieve an optimal transition from a given initial state to a desired
final state the system needs feedback. Typically, the teacher only responds by telling the
machine that its behaviour was inappropriate in terms of the distance in an appropriate
fitness measure. The machine can be a piece of real hardware (e.g. a neural net
with adjustable synaptic weights), or it can be an adaptive dynamical program, or a

50


-----


combination of both.
The topic is of central importance because AI and QML (or even classical ML) might
provide optimal solutions to the single most important issue in quantum computing
and simulation - how to design a time evolution operator that evolves a system from
A to B in an efficient manner, i.e. in polynomial time as a function of the size of
the input? Effectively this might mean to avoid expressing the evolution operator
in series of 1q and 2q gates, or even multi-qubit gates, and instead find efficient
paths through the high-dimensional Hilbert space from the initial to the final state
of, e.g., a large molecule. Carleo and Troyer [362] recently showed that systematic
reinforcement machine learning with a variational representation of the wave function
based on artificial neural networks (restricted Boltzmann machine, RBM) can reduce
the complexity to a tractable computational form for some interacting quantum spins
models in one and two dimensions.
This then puts focus on machine learning for optimal control and searching for
optimal paths in complex energy landscapes. Recently, a quantum algorithm for solving
a system of linear equations _Ax_ = _b_ (HHL) [363, 364] has attracted great interest and
been used for constructing algorithms for both supervised and unsupervised machine
learning [365367], e.g. to classify data or to identify patterns in large data sets (Big
Data). This type of work is touching some core questions regarding speedup of quantum
algorithms: the HHL algorithm in itself can achieve quantum speedup when allowed
to work on suitably conditioned quantum data, but this does not necessarily admit
exponential speedup of finding solutions to given real-world problems - there are a
number of caveats [368].
Finally, Las Heras et al. [279] have used a genetic algorithm (GA) to synthesize
high-fidelity 2q gates by adding ancillas to increase the fidelity and optimise the resource
requirements of digital quantum simulation protocols, while adapting naturally to the
experimental constraints. Moreover, Zhang and Kim [369,370] devised machine learning
for a neural network to analyse topological phase transitions.

_8.5. Error correction codes and stabilisers_

Quantum error correction (QEC) presents one of the greatest experimental challenges.
QEC is quite well developed theoretically, but experimentally it is just at the beginning.
In this section we will describe a few simple examples of experimental applications,
including pieces of the surface code on the way to the complete scheme [2831,35].
An error in a single qubit cannot be corrected - if an error changes the state of
the qubit, a measurement of that state says nothing about the original state - the
information is lost. Expanding the space of a qubit changes this situation because the
information about the error can be stored for later correction - this is essentially the
same as discussed earlier in terms of feedback undoing measurement back action.
Expanding the space means coding a qubit __ _|_ 0 __ + __ _|_ 1 __ by representing it as a
cluster of qubits - a logical qubit. For a given code, there are operators that commute

51


-----


with the code operators and have the same eigenstates - these are called stabilisers (see
e.g. [371]). A measurement of a stabiliser operator then results in an eigenstate of the
logical qubit, with no knowledge of the individual qubits.
A common measure of the size of the error is the Hamming distance, stating how
many bits differ between the correct and corrupted codewords. Classically the simplest
form of error correction is redundancy at a level corresponding to the Hamming distance.
If one expands 0 and 1 into bit-string code words 00 and 11 with distinct parity +1,
defined by the bit sum modulo 2 checked by XOR gates, then a bit-flip error will lead
to 01 or 10, and can be detected as a parity change to -1. Parity checks represent
fundamental steps in both classical and quantum error detection schemes.

![G_Wendin_Review_of_superconducting_circuits.pdf-51-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-51-0.png)

Figure 21: Quantum circuit for checking the ZZ (bit-flip) and XX (phase-flip) parities of a
2-qubit state _|_ __ __ . Since ZZ and XX commute, bit-flip and phase-flip parities can be checked
independently. The Hadamard gates switch to the _|_ + __ X-basis

In the quantum version in Fig. 21, the qubit _|_ __ __ = __ _|_ 0 __ + __ _|_ 1 __ is coded as
__ _|_ 00 __ + __ _|_ 11 __ . One then adds a third and a fourth qubit for checking and storing
the ZZ and XX parities of the codeword. The parity checks are then performed via
CNOT (XOR) gates between each of the ancillas and the two qubits.
As a specific example, consider checking for bit-flips with the ZZ ( __ _z_ 1 __ _z_ 2 ) operator in
the _|_ 0 __ _,_ _|_ 1 __ basis. The qubits+ancilla state is then ( __ _|_ 00 __ + __ _|_ 11 __ ) _|_ 0 __ = __ _|_ 000 __ + __ _|_ 110 __ . If
there is no bit flip, one obtains: _CNOT_ 23 _CNOT_ 13 ( __ 000 + __ 110 ) = ( __ 00 + __ 11 ) 0 ,
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __
where the ancilla stays in state _|_ 0 __ , with parity +1. If there is a bit flip, leading
to __ 01 + __ 10 , the parity check results in: _CNOT_ 23 _CNOT_ 13 ( __ 010 + __ 100 ) =
_|_ __ _|_ __ _|_ __ _|_ __
( __ _|_ 01 __ + __ _|_ 10 __ ) _|_ 1 __ , where the ancilla changes to state _|_ 1 __ , with parity -1.
As another specific example, consider checking for phase-flips with the XX ( __ _x_ 1 __ _x_ 2 )
operator in the _|_ + __ _,_ _|_ basis. Phase-flips are sign changes of the code word, __ _|_ 00 __
__ _|_ 11 __ , and look like bit-flips along the X-axis, corresponding to _|_ + _|_ . The
qubits+ancilla state is then ( __ _|_ 00 __ + __ _|_ 11 __ ) _|_ + __ = __ _|_ 00+ __ + __ _|_ 11+ __ . If there is no phase
flip, one obtains: _CNOT_ 42 _CNOT_ 41 ( __ 00+ + __ 11+ ) = ( __ 00 + __ 11 ) + , where the
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __
ancilla stays in state _|_ + __ , with parity +1. If there is a phase flip, leading to __ _|_ 00 __ __ _|_ 11 __ ,
the parity check results in: _CNOT_ 42 _CNOT_ 41 ( __ 00+ __ 11+ ) = ( __ 00 __ 11 ) ,
_|_ __ _|_ __ _|_ __ _|_ __ _|_
where the ancilla changes to state _|_ , with parity -1.
Since ZZ and XX commute, [ _ZZ, XX_ ] = 0, bit-flip and phase-flip parities can
be checked (and corrected) independently and the ZZ and XX parity eigenvalues

52


-----


characterise the state, (ZZ,XX): (+,+), (+,-), (-,+) and (-,-).

_8.6. Three qubit code_

To obtain a correctable code, classically the simplest case is to make use of redundancy
via code words with three bits: 000 and 111, in which case a bit flip can be corrected by
a majority vote: 010 __ 000, etc. Quantum mechanically the corresponding protected
logic qubit becomes:

_|_ __ __ = __ _|_ 0 __ + __ _|_ 1 __ __ _|_ 000 __ + __ _|_ 111 __ (74)

Experimental implementation of this coding has been done in ion traps [372374], NV
centra [375] and transmon circuits [34,271]
A systematic scheme to correct bit flips in any of the three qubits requires separate
ancillas for syndrome measurement, storage and correction, as illustrated in Fig. 22.
This involves precisely the bit-flip ZZ parity-check procedure described in Fig. 21.

![G_Wendin_Review_of_superconducting_circuits.pdf-52-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-52-0.png)

Figure 22: Standard bit-flip QEC with two ancillas for detecting and storing the error
syndrome, and correcting the error. In this way the code words are not perturbed by
measurement and recoding is not needed. The figure illustrates explicit error detection followed
by feedforward control using e.g. FPGA electronics. The correction can also be implemented
via Toffoli gates. In the case of phase flips one uses Hadamard gates to transform phase flips
into bit flips, checks the parity, and then transforms back.

 
Defining _U_ 1 = _CNOT_ _q_ 1 _,a_ 1 _CNOT_ _q_ 2 _,a_ 1 and _U_ 2 = _CNOT_ _q_ 2 _a_ 2 _CNOT_ _q_ 3 _a_ 2 , we want to

 
calculate _U_ 2 _U_ 1 ( __ 000 + __ 111 ) 00 , and characterise the effects of bit flips via the ancilla
_|_ __ _|_ __ _|_ __
syndrome.
Zero bit-flip error:

 
_U_ 2 _U_ 1 ( __ 000 + __ 111 ) 00 = ( __ 000 + __ 111 ) 00 (75)
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

On measuring (00), do nothing.
Bit-flip error in qubit 1:

 
_U_ 2 _U_ 1 ( __ 100 + __ 011 ) 00 = ( __ 100 + __ 011 ) 10 (76)
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

On measuring (10), X-flip qubit 1.

53


-----


Bit-flip error in qubit 2:

 
_U_ 2 _U_ 1 ( __ 010 + __ 101 ) 00 = ( __ 010 + __ 101 ) 11 (77)
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

On measuring (11), X-flip qubit 2.
Bit-flip error in qubit 3:

 
_U_ 2 _U_ 1 ( __ 001 + __ 110 ) 00 = ( __ 001 + __ 110 ) 01 (78)
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

On measuring (01), X-flip qubit 3.
There are typically three ways to apply the correction:
1. By feed-forward application of X gates via fast electronics, flipping the faulty qubit;
2. By automatic correction via a set of Toffoli (CCNOT, controlled X) gates with
suitable truth tables, flipping the faulty qubit. This corrects and restores the original
coded qubit - there is then no need for re-coding, only the ancillas have to be reset.
3. To store the errors in classical memory, and correct at the end.
A single round of QEC for 3 qubits was implemented by Reed et al. [271] in a 3
transmon qubit circuit without ancillas, correcting for single bit- or phase-flips using
a Toffoli gate. Recently the scheme in Fig. 22 was implemented by Riste et al. [34],
detecting bit-flip errors in a logical qubit using stabiliser measurements. The experiment
uses 3 qubits for encoding, 2 ancilla qubits for the syndrome, and fast feed-forward
control for correction (Fig. 22).
Moreover, using their 9-qubit 1D chain, Kelly et al. [35] recently implemented the
3q repetition code with 3 QEC cycles, and extended the work to a 5q code. This work
represents first steps toward the 2D-surface code, and will be discussed in some detail
below.
Fast electronics makes it possible to perform qubit calibration during repetitive
error detection [376]. Moreover, one does not have to apply corrections when errors are
detected - it is enough to store the information about errors in classical memory and
correct at the end [377,378].

_8.7. Surface codes_

The surface (toric) QEC code was invented by Kitaev [379,380] and is now at the focus
of intense development and experimental implementations [2931,377,378,381384].

_8.7.1._ _Basic concepts and models_ The surface code is connected with a specific
geometrical arrangement (architecture) of qubits (Fig. 23): 4 data qubits (D) at the
corners of a square with a syndrome ancilla qubit (S) at the centre. The central task
is to perform 4-qubit parity measurements on the data qubits (D) using ZZZZ and
XXXX stabiliser operators and to register the measured (classical) ancilla syndrome (S)
eigenvalue, showing whether there has been a bit-flip _|_ 0 _|_ 1 __ or a phase-flip _|_ + _|_
in the 4q data cluster.

54


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-54-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-54-0.png)

Figure 23: (a) Surface code 4 x 4 qubit array layout. (b) Basic 5 qubit plaquette with 4 data
qubits (D) and a central ancilla (syndrome, S) qubit for measuring ZZZZ (bit-flip) parities.
(c) Basic 5 qubit plaquette with 4 data qubits (D) and a central ancilla (syndrome, S) qubit
for measuring XXXX (phase-flip) parities. Note the measuring order D1-D2-D3-D4 forming
an S-like trace.

_8.7.2. 4-qubit parity measurements on a surface code plaquette_ IBM has performed
4-qubit parity measurements that demonstrate the detection of arbitrary single-qubit
quantum errors on an effective 4-qubit plaquette (Fig. 23b,c) designed for the surface
code using all-microwave control [29, 30]. In particular, the qubit-qubit couplings are
dynamically driven via the CR technique, and the pulse schemes include echo sequences
to remove non-ideal-gate errors. Gates were characterised by randomised benchmarking
(RB) and correct ZZZZ and XXXX parity assignments were obtained with 0.75-0.80
probability.

_8.7.3. 17-qubit design for the surface code_ TU Delft is presently developing and testing
a scalable architecture [31] for executing the error-correction cycle of a monolithic
surface-code fabric (Surface-17 [382]), composed of fast-flux-tunable transmon qubits
with nearest-neighbor coupling. The scheme combines four key concepts [31]: (i)
an eight-qubit unit cell as the basis for repetition of quantum hardware and control
signals (cutting out a section in Fig. 23a); (ii) pipelining of X- and Z-type stabiliser
measurements (Fig. 23b,c); (iii) a fixed set of three frequencies for single-qubit control;
and (iv) a fixed set of eight detuning sequences implementing the needed controlledphase gates. The design couples nearest-neighbour data and ancilla transmons in a
planar cQED architecture via bus resonators. The eight-qubit unit cell can be repeated
in 2D using vertical interconnects for all input and output signals from the control
layers. Each transmon will have a dedicated flux line allowing control of its transition
frequency on nanosecond timescales, a dedicated microwave-drive line, and a dedicated

55


-----


dispersively-coupled resonator for readout.

_8.7.4. Multi 2-qubit parity measurements on a surface code 1D chain_ Martinis group
has performed a set of surface-code type of experiments on a linear 1D chain with
9 qubits [35, 376] (Fig. 24), tracking errors as they occur by repeatedly performing
projective quantum non-demolition parity measurements. This is a first step toward
the 2D surface code scheme (Fig. 23), measuring ZZ (bit-flip) parities (Figs. 21, 22).
The first experiment [35] used 5 qubits (Fig. 24a) with 3 data qubits and 2
measurement ancillas to implement the 3q repetition code (same circuit as in Fig. 22).
The repetition code algorithm uses repeated entangling and measurement operations to
detect bit-flips using the ZZ parity. The initial state can be reproduced by removing
physical errors in software based on qubit measurements during the execution the
repetition code.

![G_Wendin_Review_of_superconducting_circuits.pdf-55-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-55-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-55-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-55-1.png)

Figure 24: (a) Left: 3q repetition code __ _|_ 000 __ + __ _|_ 111 __ : algorithm (same circuit as in Fig. 22.
(b) Right: 5q repetition code __ _|_ 00000 __ + __ _|_ 11111 __ : error propagation and identification.
Adapted from [35].

Figure 24b shows a 9 qubit quantum circuit with 5 data qubits and 4 measurement
ancillas, for three cycles of the repetition code, with examples of errors [35]. Errors
propagate horizontally in time, and vertically through entangling gates. Different errors
lead to different detection patterns: an error on a measurement qubit is detected in two
subsequent rounds. Data qubit errors are detected on neighbouring measurement qubits
in the same or next cycle. Data errors after the last round are detected by constructing
the final set of ZZ eigenvalues from the data qubit measurements.
To study the ability to preserve quantum states, the data qubits were initialised
into a GHZ state, and two rounds of the repetition code were applied. The result shows
that the one-dimensional repetition code algorithm allows for preserving the quantum
state in the case of no errors, and correcting bit-flip errors otherwise, purely through
error detection and classical post-processing. This is similar to the full surface code,
avoiding the need for dynamic feedback with quantum gates.
Relative to a single physical qubit, the failure rate in retrieving an input state was
reduced by a factor of 2.7 when using five qubits, and by a factor of 8.5 when using all
nine qubits after eight cycles. Moreover, the preservation of the GHZ state was verified

56


-----


tomographically.

_8.8. Architecture and error correction in 3D cQED_

Recent experimental results for the 3D transmon approach show great promise, and 3D
architectures are in the process of being scaled up.

_8.8.1. cQED 3D architecture_ Architectures based on 2D resonator networks coupled
by JJs have been proposed and developed by Houck _et al._ [430]. However, the superior
coherence times of 3D resonators have recently been exploited by the Yale group to
design a 3D architecture [142, 143] which encodes quantum information in the Hilbert
space of a 3D array of 3D superconducting cavities and employs the Josephson junction
only to perform operations on states of the cavities. The approach promises to be
hardware efficient since there is only one dominant error mechanism - single photon
loss of the cavity - while the room in Hilbert space is large enough to accommodate
particularly easy-to-correct sub-manifolds. The idea [143] is to control the qubit-cavity
components well enough that they may serve as logical qubits in an architecture based
on multilayer microwave integrated quantum circuit (MMIQC) technology. (MMIC is
already a well-established classical microwave technology).

_8.8.2. Engineering cat-states_ Specially engineered interaction with the environment
can become a resource for the generation and protection of coherent superpositions
of multiple, stable, steady states. Leghtas _et al._ [144] have confined the state of a
superconducting resonator to the quantum manifold spanned by two coherent states
of opposite phases and have observed a Schr odinger cat state spontaneously squeeze
out of vacuum before decaying into a classical mixture. This experiment points toward
robustly encoding quantum information in multi-dimensional steady-state manifolds.
Moreover, Wang _et al._ [145] have realized a two-mode cat state of electromagnetic
fields in two microwave cavities bridged by a superconducting artificial atom, which can
also be viewed as an entangled pair of single-cavity cat states. The work presents full
quantum state tomography of this complex cat state over a Hilbert space exceeding
100 dimensions via quantum nondemolition measurements of the joint photon number
parity. This paves the way for logical operations between redundantly encoded qubits
for fault-tolerant quantum computation and communication.

_8.8.3. Engineering QEC_ The break-even point of QEC is when the lifetime of a qubit
exceeds the lifetime of the constituents of the system. Yale [146] has demonstrated a
QEC system that reaches the break-even point by suppressing the natural errors due to
energy loss for a qubit logically encoded in superpositions of Schr odinger-cat states of
a superconducting resonator. Ofek _et al._ [146] implement a full QEC protocol by using
real-time feedback to (i) encode, (ii) monitor naturally occurring errors, (iii) decode and
(iv) correct. As measured by full quantum process tomography without post-selection,

57


-----


the corrected qubit lifetime is 320 _s_ , which is longer than the lifetime of any of the
parts of the system.

_8.8.4._ _Gates and operations_ Heeres _et al._ [148] recently demonstrated high-fidelity
implementation of a universal set of gates on a qubit encoded into an oscillator using
the cat code, targeting the creation and manipulation of a logical qubit encoded in
an even-parity four-component cat subspace. Using optimal control techniques, they
created a universal set of gates on this logical qubit, including X and Y rotations by __
and _/_ 2, as well as Hadamard and T gates. This includes the creation of encoding and
decoding pulses to transfer bits of quantum information between the transmon subspace
and the encoded cat subspace.
A major step nevertheless remains - to perform entangling gate operations on two
logical qubits to achieve a universal set of gates for quantum computing. As discussed
in Sect. 7.4.2, entangling two remote quantum systems that never interact directly
is an essential building block in quantum information science - it forms a basis for
modular architectures of quantum computing. For protocols relying on using traveling
single-photon states as flying qubits, needed for the 3D architecture considered by
Yale, efficiently detecting single photons is challenging because of the low energy of
microwave quanta. Entangling distant qubits by photon detection is a well-established
technique in quantum optics. Narla _et al._ [147] now report the realisation of a robust
form of concurrent remote entanglement based on a novel microwave photon detector
implemented in their cQED platform. This may open the way for a modular 3Darchitecture of QIP with superconducting qubits.

58


-----

# **9. Quantum simulation of many-body systems**

Quantum systems need quantum systems for efficient simulation [76]. Simulation of
a large quantum system, say a molecule of medical interest, may be intractable on a
classical digital computer due to lack of time and memory, but tractable on quantum
computers and simulators in order to achieve necessary accuracy.
Ordinary classical digital computers are basically used for number crunching:
encoding and running algorithms that process numbers for various purposes, like
numerically solving equations, performing search, classifying data, and optimising
approximate solutions. Classical digital computers are based on networks of logic
gates and memory. The concept of digital quantum computation (QC) and simulation
(QS) is similar: it involves circuit models with quantum gates to input, process and
output digital quantum information [50,53,54,385391]. Both digital QC and QS map
mathematical problems onto a quantum representation (Hilbert space), devise sequences
of gate operations, and use superposition and entanglement to compute and to achieve
speedup.
In contrast, analogue QC and QS are not based on quantum gates, but on direct
construction of the physical system Hamiltonian in hardware (HW). There are a number
of ways to emulate interesting quantum Hamiltonians in quantum HW. In adiabatic QC
(AQC) [78, 79] one adiabatically follows the development of the ground state when a
perturbation is slowly switched on, switching from an initial model Hamiltonian to a
final one, implementing the transition to the desired interacting many-body system.
Finally, quantum annealing (QA) [392] is related to AQC in that one emulates a
Hamiltonian in hardware. The difference is that one heats up and then cools the system,
following its path toward the ground state via classical thermal and quantum tunneling
transitions.

_9.1. Basics of quantum simulation_

Basically, a quantum simulator solves the time-dependent Schr odinger equation (TDSE)


for a system described by a Hamiltonian _H_ ,



__
_i_ _h_  __ ( _t_ ) =  _H_ ( _t_ ) __ ( _t_ ) (79)

_t_ _|_ __ _|_ __


via propagation of an initial state __ ( _t_ 0 ) using the time-evolution operator
_|_ __


__ ( _t_ ) = _U_  ( _t, t_ 0 ) __ ( _t_ 0 ) = _T e_  __
_|_ __ _|_ __


_t_




_t_ 0 _H_  ( _t_ __ ) _dt_ __ __ ( _t_ 0 ) _._ (80)
_|_ __


The initial state __ ( _t_ 0 ) represents an essential part of the problem. It can be a
_|_ __
computational basis state or a superposition of configurations. If the configuration
is not an eigenstate, the state will then evolve in time through state space and reflect
the dynamics of the system Hamiltonian, and the Fourier spectrum will provide the
energies of the eigenstates. A systematic way to construct the initial state __ ( _t_ 0 ) is
_|_ __
to start from a reference state __ _ref_ and add states representing excitations from the
_|_ __


59


-----


reference state:


__ ( _t_ 0 ) = _a_ _ref_ __ _ref_ + (81)
_|_ __ _|_ __

+ _a_ _ni_ _c_ + _p_ _c_ _q_ __ _ref_ + _a_ _mnji_ _c_ + _p_ _c_ + _q_ _c_ _r_ _c_ _s_ __ _ref_ + _...._

_|_ __ _|_ __

Relation (81) represents a configuration interaction (CI) state including single   _a_ _ni_ _c_ + _p_ _c_ _q_
and double _a_ _mnji_ _c_ + _p_ _c_ + _q_ _c_ _r_ _c_ _s_ excitations, typically adding many-particle correlation effects
to a mean-field initial state; formal inclusion of all possible excitations defines the full CI
(FCI) state. Simple approximations for __ ( _t_ 0 )
could be a product state, or a HartreeFock determinant. Advanced approximations can be constructed via coupled-cluster _|_ __
(CC) [393] or matrix product (MPS) [394] reference states. Also note the very recent
work by Carleo and Troyer [362].
For a nice review and hands-on discussion of all the steps needed for simulating
the time evolution of a _H_ 2 molecule and extracting the ground state energy, see Whitfield
_et al._ [389].

_9.2. Trotterisation_

There are many different approaches that can be used to compute _e_ __ _i_  _Ht_ _|_ __ (0) __ , and
many of them rely on Trotter decompositions involving discretisation of the time
evolution [386,388,389].
Let us for simplicity consider a time-independent Hamiltonian, and set _t_ 0 = 0. (In
the following we also set  _h_ = 1, with energy measured in units of frequency).

_|_ __ ( _t_ ) __ = _U_  ( _t,_ 0) _|_ __ (0) __ = _e_ __ _i_  _Ht_ _|_ __ (0) __ _,_ (82)

where


_H_ =


_H_ _i_ (83)
_i_ =1 _,k_


Trotterisation (Lie-Trotter-Suzuki formula)



_i_  _Ht_ _i_ ( _H_  1 + _H_  2 + _....._ + _H_  _k_ ) _t/m_ _m_
_e_ __ [ _e_ __ ]
__ _i_  _H_ 1 _t/m_ _i_ _H_  2 _t/m_ _i_ _H_  _k_ _t/m_ _m_

__ [ _e_ __ _e_ __ _.... e_ __ ] (84)

makes it possible to express the time evolution operator as a sequence of operations of


the individual terms _H_ _i_ of the Hamiltonian. These operations can be gate operations
in a quantum circuit model, or the application of classical control fields in an analog
quantum system, or combinations thereof. In practice one uses higher order Trotter
formulas to minimize the errors [388,395].

_9.3. Phase estimation_

The time evolution methods solve dynamical simulation problems, and do not directly
solve the ground-state energy estimation problem. The phase estimation algorithm
(PEA) (see e.g. [54,387389,396]) provides the connection needed to relate the eigenvalue
estimation problem to the dynamical simulation problem. The left part of Fig. 25a

60


-----



 _i_  _Ht_
describes the propagation of the quantum state _U_ _|_ __ __ = _e_ __ _|_ __ __ in smaller and smaller
steps (longer and longer times) to achieve the required accuracy. The phase information
from the time evolution is stored in the ancillas, and the energy spectrum is finally
analysed by an inverse quantum Fourier transform (QFT) (right part of Fig. 25a).

![G_Wendin_Review_of_superconducting_circuits.pdf-60-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-60-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-60-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-60-1.png)

Figure 25: (a) The Phase Estimation Algorithm (PEA). (b) The kth iteration of the iterative
PEA (IPEA). The feedback angle _k_ depends on the previously measured bits [396].

The multi-qubit state _|_ __ __ itself in Fig. 25a can be efficiently implemented by a


polynomial number of gates (Sect. 6.6), because the _U_ -operators consist of exponentials
of polynomial numbers of Pauli operators in the Hamiltonian (cf. Fig. 13e). Calculation
of the energy via the PEA is however not necessarily scaling polynomially: it employs
Cntrl- _R_ _z_ ( __ gates (cf. Fig. 13f), and the number depends on the accuracy required. For
a large molecule, requiring many qubits and chemical precision, the number of gates will
be very large, requiring long coherence times. This will be further discussed in Sect. 10.
The PEA in Fig. 25a requires as many ancillas as significant bits in the result. To
save on the number of ancilla qubits, the PEA can be implemented through an iterative
process using only a single ancilla qubit and classical feedback [389,396], as illustrated
in (Fig. 25b).

_9.4. Digital quantum simulation of the quantum Rabi model_

Langford _et al._ [216] have performed a digital quantum simulation of the quantum Rabi
model (QRM, Eqs. (9),(10)) in the ultra-strong (USC, DSC) regime. Building on the
proposal in [215], they perform a digital simulation of the QRM for arbitrarily large
coupling strength using a physical qubit(transmon)-resonator circuit in the moderatecoupling regime ( _g/ <_ 10 __ 3 ). The name of the game is to simulate a system
where the effective resonator frequency __ _eff_ can be made so small that _g/_ _eff_ __ 1,
representing the USC/DSC regimes. This was achieved by transforming the Hamiltonian
to rotating frames and simulating the effects of the JC and AJC co- and counter-rotating
interactions in the qubit-resonator Hamiltonian using up to 90 second-order Trotter
steps [216]. The work demonstrates the expected Schr odinger-cat-like entanglement
and build-up of large photon numbers and population revivals characteristic of deep
USC. Furthermore, it opens the door to exploring extreme USC regimes, quantum phase
transitions and many-body effects in the Dicke model [217].

61


-----


_9.5. Digital quantum simulation of spin models_

In digital quantum simulation (DQS) one induces the time evolution of a qubit register
in the quantum circuit model by applying a sequence of qubit gates according to a
specific protocol. DQS has previously been implemented in an ion trap to perform
universal digital quantum simulation of spin models [397], and now also on a transmon
platforms [36,191,398] to simulate the dynamics of small spin systems.

_9.5.1. Two-spin Ising and Heisenberg models_ For a two-spin system, the canonical spin
models are:

(i) The Ising model:


_H_ _I_ = _J_ 1 _z_ __ 2 _z_ + _B_ __ _iz_ (85)


(ii) The transverse field Ising model (TIM):


_H_ _TIM_ = _J_ 1 _x_ __ 2 _x_ + _B_ __ _iz_ (86)


(iii) The XY model:


_H_ _XY_ = _J_ ( __ 1 _x_ __ 2 _x_ + __ 1 _y_ __ 2 _y_ ) + _B_ __ _iz_ (87)


(iv) The XYZ anisotropic Heisenberg model:


_H_ _XY Z_ = _J_ _x_ __ 1 _x_ __ 2 _x_ + _J_ _y_ __ 1 _y_ __ 2 _y_ + _J_ _z_ __ 1 _z_ __ 1 _z_ + _B_ __ _iz_ (88)


The XY interaction 1 2 ( __ 1 _x_ __ 2 _x_ + __ 1 _y_ __ 2 _y_ ) = __ 1+ __ 2 __ + __ 1 __ __ 2+ is naturally implemented


via the _iSWAP_ gate _U_ _XY_ ( _t_ ) (Eq. (41)), tuning the qubits in and out of resonance, and
can be used to construct a digital decomposition of the model-specific evolution and to
extract its full dynamics.
Salath e _et al._ [191] performed digital quantum simulation of the XY and
isotropic Heisenberg XYZ spin models with a four-transmon-qubit circuit quantum
electrodynamics setup, using two qubits to represent the two spins. The isotropic model
Hamiltonian can be written as



1
  
_H_ _XY Z_ = (  _H_ _XY_ + _H_ _XZ_ + _H_ _Y Z_ ) (89)

2

and since the three terms commute, the time evolution operator takes the form of a

   
simple product: _U_ _XY Z_ = _U_ _XY_ _U_ _XZ_ _U_ _Y Z_ .
Moreover, rotating the computational basis,

   
_U_ _XY Z_ = _U_ _XY_ _U_ _XZ_ _U_ _Y Z_ (90)

  
= _U_ _XY_ _R_ _y_ ( __ _/_ 2) _U_ _XY_ _R_ _y_ ( _/_ 2) _R_ _x_ ( __ _/_ 2) _U_ _XY_ _R_ _x_ ( _/_ 2) (91)



1
_R_ _x_ ( _/_ 2) =


1 __ _i_
__ _i_ 1



1
_R_ _y_ ( _/_ 2) =


__ 1


(92)


makes it possible to apply the XZ and YZ interactions via the XY interaction.
The procedure is shown in Fig. 26a,b, displaying the circuit diagrams to digitally


simulate (a) the XY interaction acting on the qubits Q1 and Q2 by applying _U_ _XY_ ( _t_ )


62


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-62-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-62-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-62-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-62-1.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-62-2.png](G_Wendin_Review_of_superconducting_circuits.pdf-62-2.png)



Figure 26: (a) Two-spin XY model: Circuit diagram implementing the _U_ _XY_ ( _t_ ) gate
for a certain time _t_ = __ . (b) Two-spin Heisenberg (XYZ) model: Circuit diagram


implementing the _U_ _XY Z_ ( _t_ ) gate (Eq. 90) for a certain time _t_ = __ . (c) Time evolution

_U_ _XY_ ( _t_ ) of the two-spin XY model: Experimentally determined coordinates of the Bloch
vectors. Red (Q1) and blue (Q2) points are compared to the ideal paths shown as
dashed lines in the XY model. (d) describes the same thing for the Heisenberg (XYZ)
model. Adapted from [191].


for a time __ ; and (b) the two-spin Heisenberg (XYZ) interaction by applying _U_ _XY_ ( _t_ )
for time __ . Fig. 26c presents the time-development of the spin dynamics under the XY
interaction for a characteristic initial two-qubit state _|_ __ (0) __ = _|_ 0 __ ( _|_ 0 __ + _|_ 1 __ ) _/_ 2 in which
the spins point in the + **z** and + **x** directions. Since this is not an eigenstate of the
Hamiltonian, the spins start to rotate due to the XY-interaction. Fig. 26d presents the
result of simulating the full Heisenberg model.
Salath e _et al._ [191] also performed digital quantum simulation of the transverse Ising
model (TIM), Eq.(86). Here the XY and Z parts of the Hamiltonian do not commute,
which means that one must implement a split-operator procedure (trotterisation), as
shown in Fig. 27, splitting the evolution over time __ into _n_ slices. In each Trotter time
slice of length _/n_ , the _R_ _x_ ( __ ) rotation operators change the sign of the second term in
__
the XY interaction, adding up to the XX interaction, and _R_ _z_ ( _/n_
) implements the Zpart of the Hamiltonian. The simulation uses n=3 Trotter slices and demonstrates [191]
that after three iterations, the z-components of the spins oscillate as expected.
The approach uses only Clifford gates and is universal and efficient, employing only
resources that are polynomial in the number of spins (Sect. 6.6). An idea of the future
challenges can be obtained from a recent investigation of how to simulate the transverse
Ising model (TIM) on a quantum computer including error correction with the surface
code [399].

63


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-63-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-63-0.png)

Figure 27: Protocol to decompose and simulate Ising XY spin dynamics in a homogeneous
transverse magnetic field. Adapted from [191].

_9.5.2. Digitized adiabatic four-spin transverse Ising model_ An experiment with a 9qubit superconducting circuit was recently carried out by Barends _et al._ [37]. They
probed the adiabatic evolutions, and quantified the success of the algorithm for random
spin problems, approximating the solutions to both frustrated Ising problems and
problems with more complex interactions. The approach is compatible with small-scale
systems as well as future error-corrected quantum computers.
The digital quantum simulation (DQS) involved the following two Hamiltonians:



_H_ _I_ = __ _B_ _x,I_


__ _ix_ (93)


describing noninteracting spins in an external field in the x-direction, and



_H_ _P_ = __


( _B_ _iz_ __ _iz_ + _B_ _ix_ __ _ix_ ) __


( _J_ _zz_ _i,i_ +1 __ _iz_ __ _i_ +1 _z_ + _J_ _xx_ _i,i_ +1 __ _ix_ __ _i_ +1 _x_ ) (94)


describing a range of Ising-type spin Hamiltonians. For the analogue quantum
simulation (AQS) part, these were combined:

  
_H_ ( _s_ ) = (1 __ _s_ ) _H_ _I_ + _s_ _H_ _P_ (95)

to allow one to perform DQS for a series of Hamiltonians from non-interacting spins
(s=0) to a range of interacting spin models (s=1), and to follow the evolution of the
density matrix. Figure 28 shows an application where a four qubit system is stepwise
evolved from an initial Hamiltonian _H_ _I_ , where all spins are aligned along the x-axis, to a
problem Hamiltonian _H_ _P_ with equal ferromagnetic couplings between adjacent qubits,
described by a 4-qubit GHZ state.
Barends _et al._ [37] also investigated digital evolutions of random stoquastic and
non-stoquastic problems. Quantum stochastic calculus concerns generalisation of the
Langevin equation to quantum systems. Because of the relation to stochastic processes
one has adopted the term stoquastic to refer to quantum Hamiltonians where all
off-diagonal matrix elements in the standard basis are real and non-positive [400].
Stoquastic Hamiltonians are very common in physics. Among spin-1/2 models, the wellstudied ferromagnetic Heisenberg models and the quantum transverse Ising model [79]
are stoquastic. Another example is a Heisenberg antiferromagnet on a cubic lattice.
Barends _et al._ chose to investigate a stoquastic frustrated Ising Hamiltonian having
random local X and Z fields, and random zz couplings. Non-stoquastic problems

64


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-64-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-64-0.png)

Figure 28: Quantum state tomography of the digital evolution into a GHZ state. A four qubit
system is adiabatically evolved from an initial Hamiltonian where all spins are aligned along
the X axis to a problem Hamiltonian with equal ferromagnetic couplings between adjacent
qubits. The displayed five step algorithm is 2.1 _s_ long. Implementations of zz coupling and
local X-fields are highlighted. Adapted from [37].

have additional random xx couplings. The results show that the system can find the
ground states of both stoquastic and non-stoquastic Hamiltonians with comparable
performance.

_9.6. Digital quantum simulation of fermionic models_

Computational physics, chemistry and materials science deal with the structure and
dynamics of electronic systems: atoms, molecules, solids, liquids, soft matter, etc. To
describe theses systems one needs the full machinery of quantum many-body theory
involving fermionic and bosonic particles and excitations. So far a we have been
working with 2-level (spin) systems coupled to bosonic modes. However, to describe
electronic systems, the fermionic anti-commutation rules have to be built in. One
way to do this was invented a long time ago in the form of the Jordan-Wigner (JW)
transformation [401]. One then works in the occupation-number representation and
keeps track of parity under permutations via the the anti-commutation rules of a set
of auxiliary Pauli __ operators embedded in the fermionic creation and annihilation
operators. In this way the number of __ operators scales as _O_ ( _n_ ), i.e. as the number of
qubits.
Bravyi and Kitaev [402] derived an alternative (BK) transformation, using the

65


-----


qubits for storing parities rather than occupation numbers. This scheme also maps the
fermionic operators on products of Pauli __ operators. One advantage, however, is that
the number of __ operators scales as _O_ (log _n_ ), which will be important for simulation of
large systems that require large numbers of qubits.
These methods have been developed theoretically and simulated classically over
the last 15 years [389, 403408], but never explored experimentally, until now. The
first experimental applications ever, with superconducting circuits, have recently been
published, implementing digital simulation of the Fermi-Hubbard model [36] and the
ground state binding curve of the hydrogen molecule, _H_ 2 [38] (see further Sect. 10.1.4).
For illustration of the approach to an elementary fermonic many-body system,
consider a closed-shell atom or molecule. The general second-quantised Hamiltonian is
given by:


_H_ =


_pq_ _h_ _pq_ _c_ + _p_ _c_ _q_ + 1 2


_h_ _pqrs_ _c_ + _p_ _c_ + _q_ _c_ _r_ _c_ _s_ (96)
_pqrs_


where the first term describes the single-particle kinetic and potential energies, and
the second term the 2-body Coulomb interaction. The indices refer to the set of basis
orbitals (fermionic modes) used to expand the Hamiltonian.
The simplest possible case is the ground state of a 2-electron system with a minimal
basis of 2 states: a _He_ atom with 1 _s_ __ 1 _s_ __ , or a _H_ 2 molecule with 1 __ __ 1 __ __ . The
Hartree Hamiltonian is then given by:

 + + + +
_H_ = _h_ 1 _c_ 1 _c_ 1 + _h_ 2 _c_ 2 _c_ 2 + _V_ 12 _c_ 1 _c_ 1 _c_ 2 _c_ 2 (97)

where the Hartree term can be written as _V_ 12 _n_ 1 _n_ 2 , on the form of a Hubbard onsite
__ __
interaction (here is only one site).
The JW transformation becomes


_c_ + 1 = _I_ __ + (98)

__


_c_ + 2 = __ + __ _z_ (99)

__


_c_ 1 = _I_ __ __ __ (100)


_c_ 2 = __ __ __ __ _z_ (101)


Worked out in detail, one obtains [389]


_c_ + 1 _c_ 1 = 1 2 ( _I_ __ __ _z_ 1 ) (102)


_c_ + 2 _c_ 2 = 1 2 ( _I_ __ __ _z_ 2 __ _z_ 1 ) (103)


_c_ + 1 _c_ 1 _c_ + 2 _c_ 2 = 1 4 ( _I_ __ __ _z_ 1 __ __ _z_ 2 __ _z_ 1 + __ _z_ 2 ) (104)

The Hamiltonian then finally becomes [389]:


_H_ = _h_ __ _h/_ 2 ( __ _z_ 1 + __ _z_ 2 __ _z_ 1 ) + _V/_ 4 (1 __ __ _z_ 1 + __ _z_ 2 __ __ _z_ 2 __ _z_ 1 ) (105)


The evolution operator corresponding to the parts of the Hamiltonian with __ _z_ __

 __ __
products, _U_ = _exp_ [ _i_ 2 __ _z_ __ _z_ ] can be implemented by a quantum circuit of the form
__ __


products, _U_ = _exp_ [ _i_ 2 __ __ _z_ __ _z_ ] can be implemented by a quantum circuit of the form
__ __

shown in Fig. 13e.


66


-----


At the next level, the simplest possible case is still the ground state of a 2-electron
_He_ atom, but now with a slightly extended basis of 4 states, 1: 1 _s_ __ , 2: 1 _s_ __ , 3: 2 _s_ __
and 4: 2 _s_ __ . At this level one can begin to investigate effects of correlation on the
ground state energy. Taking into account that in the ground state only states 1 and 2
are occupied, the Hamiltonian can be written as:

  
_H_ = _H_ 1 + _H_ 2 (106)

 + +
_H_ 1 = _h_ 11 _c_ 1 _c_ 1 + _h_ 22 _c_ 2 _c_ 2 (107)

 + + + + + +
_H_ 2 = _h_ 1221 _c_ 1 _c_ 2 _c_ 2 _c_ 1 + _h_ 1243 ( _c_ 1 _c_ 2 _c_ 4 _c_ 3 + _c_ 3 _c_ 4 _c_ 2 _c_ 1 ) (108)

The interaction term can be rewritten as

 + + + + + +
_H_ 2 = _V_ 12 _c_ 1 _c_ 1 _c_ 2 _c_ 2 + _V_ 1324 ( _c_ 1 _c_ 3 _c_ 2 _c_ 4 + _c_ 3 _c_ 1 _c_ 4 _c_ 2 ) (109)


emphasizing the physical meaning of the terms: the first term describes the direct
Coulomb interaction describes the (radial) correlation energy generated by interacting virtual (1 and (1 _s_ __ ) __ 1 (2 _s_ __ ) electron-hole pair excitations [409]. _V_ 12 between the 1 _s_ __ and 1 _s_ __ electrons, while the second term _s_ __ ) __ 1 (2 _s_ __ )
The correlation term involves all four states, and therefore all four qubits. The
result of applying the JW transformation then leads to the appearance of an interaction
Hamiltonian of the form __ __ __ __ __ __ __ __ . A detailed analysis [389] shows that only the
__ __ __
terms __ _x_ __ _x_ __ _y_ __ _y_ , __ _y_ __ _y_ __ _x_ __ _x_ , __ _y_ __ _x_ __ _x_ __ _y_ , __ _x_ __ _y_ __ _y_ __ _x_ need to be considered. These can be

 __
generated by an evolution operator of the form _U_ = _exp_ [ _i_ 2 __ _z_ __ _z_ __ _z_ __ _z_ ] together
__ __ __ __

with suitable qubit rotations changing the computational basis (see Table A3 in [389]).
This method - the full approach with trotterisation and phase estimation - was
recently applied by OMalley _et al._ [38] to the calculation the _H_ 2 binding energy curve,
as discussed in Sect. 10

_9.7. Analogue/adiabatic quantum simulation_

In analogue quantum simulation (AQS) one induces the time evolution of a qubit register
by application of a sequence of time-dependent external fields and internal interactions

[50,410]. AQS has so far been implemented experimentally in ion traps [411413], ultracold atoms in optical lattices [414418] and photonics circuits [419429], to perform
simulation of various physical models involving spins, bosons and fermions.
With the advent of useful and powerful JJ-based qubit circuits, there is a
recent surge of proposals involving superconducting qubits [133, 215, 430442] as well
experimental results [118,119,214,443449] for superconducting circuits.

_9.8. Digital-analogue quantum simulation_

By digital-analogue quantum simulation we denote methods that control the time
evolution (operator) by both (i) applying circuit-based digital gates (DQS) and (ii)
evolving the Hamiltonian parameters in time (AQS). If the time scales are widely

67


-----


separated, e.g. the analogue evolution being adiabatic, the calculation becomes a
number of complete DQS calculations for a series of adiabatic Hamiltonian time steps.
Recently a fermionic 4-mode problem was performed experimentally with a
superconducting system by Barends _et al._ [36], implementing a scheme of Las Heras _et_
_al._ [408]. The experiment involved time evolutions with constant interactions, with up to
four fermionic modes encoded in four qubits, using the Jordan-Wigner transformation.
The time evolution involved over 300 single-qubit and two-qubit gates, reaching global
fidelities limited by gate errors in an intuitive error model. Barends _et al._ [36] also
introduced time-dependence in the model Hamiltonian, by slowly ramping the hopping
interaction from zero to the strength of the on-site fermion-fermion interaction, switching
the system from localised to itinerant fermions, observing elements of a dynamic phase
transition. The experiment, as well as that in [37], therefore may present a step on the
path to creating an analogue-digital quantum simulator using discrete fermionic modes
combined with discrete or continuous bosonic modes [450].
In the general case with no separation of time scales, the combined evolution needs
to be implemented via the full evolution operator with a time-dependent Hamiltonian.
In the end combinations of analogue and digital simulation schemes may be the most
powerful ones, driving or inducing selected terms in the Hamiltonian that allow sets of
gates not possible in the undriven physical system.

68


-----

# **10. Toward quantum chemistry simulation**

Quantum chemistry is traditionally a testing ground for classical high-performance
computing (HPC) [451] and is currently at the focus of investigations of various advanced
approximation methods in many-body physics [452454]. The simulation of quantum
chemistry is one of the most anticipated applications of quantum computing, but the
scaling of known upper bounds on the complexity of these algorithms is very demanding.
Hamiltonian problems with 2-body interactions have been shown to be QMA-hard [81],
which means that it is fundamentally impossible to calculate the exact ground state
electron structure of large molecules [83,8589]. This implies that the quantum chemical
problem of ground state energy search is non-polynomial (actually exponential) in time
with respect to the system size. Consequently, like in the classical case, also quantum
simulation of molecular electronic structure must build on advanced approximation
schemes in order for full configuration interaction (FCI) to be tractable in high-accuracy
calculations already for fairly small molecules.
Quantum simulation methods are now the targets of an emerging field of quantum
HPC both theoretically [38,196,198201,388,389,395,406,455471] and experimentally

[38, 456, 467, 470, 472, 473]. Even if the number of gates only scales polynomially,
the required number may still be prohibitive to reach chemical accuracy in nearfuture applications. However, applying the intuition of classical quantum chemistry
to QS may reduce the computational complexity. A natural way forward is to make
use of state-of-the-art classical approximate treatments of FCI and apply these to
quantum algorithms [38, 395]. Also, it is very important to have realistic ideas of the
computational effort needed for specific molecules, to be able to address cases that are
tractable with present resources. Fortunately, the recent development has been quite
dramatic [458]. Combined with the rapid development of superconducting multi-qubit
systems, it now seems possible to go beyond toy models and implement larger-scale
calculations on real hardware systems [38,395,456].

_10.1. Hamiltonian ground-state energy estimation_

The quantum phase estimation algorithm PEA efficiently finds the eigenvalue of a given
eigenvector but requires fully coherent evolution. For large systems requiring many
qubits and gate operations, the coherence time may eventually become too short. To
alleviate this problem, Peruzzo et al. [456] introduced an alternative to the PEA that
significantly reduces the requirements for coherent evolution. They have developed
a reconfigurable quantum processing unit, which efficiently calculates the expectation
value of a Hamiltonian, providing an exponential speedup over exact diagonalisation,
the only known exact method of solution to the problem on a traditional computer. The
calculation is mainly classical but uses a quantum subroutine for exponential speedup of
the critical step of quantum energy estimation. The power of the approach derives from
the fact that quantum hardware can store a global quantum state with exponentially
fewer resources than required by classical hardware, and as a result the QMA-hard

69


-----


N-representability problem (constraining the two-electron reduced density matrix to
represent an N-electron density matrix) [474] does not arise.

_10.1.1. Quantum energy estimation_ The quantum energy estimation (QEE) algorithm

  
computes the expectation value _<_ _H >_ = __ __ _|_ _H_ _|_ __ __ of a given Hamiltonian _H_ with
respect to a given state _|_ __ __ [456].
As discussed in Sect. 9, after JW or BK transformations [457] the second quantized
Hamiltonian for electronic physical systems can be written in terms of Pauli operators
as


_H_ =


_h_ _i_ __ _i_ +
_i_


_h_ _i,j_ __ _i_ __ _j_ + _...._ (110)
_i,j_


with expectation value:




_<_ _H >_ =


_h_ _i_ _< _ _i_ _>_ +
_i_


_h_ _i,j_ _< _ _i_ __ _j_ _>_ + _...._ (111)
_i,j_


The coefficients are determined using a classical quantum chemistry package.
The expectation value of a tensor product _< _ _i_ __ _j_ __ _k_ _..... >_ of an arbitrary number
of Pauli operators can be estimated by local measurement of each qubit [54], independent
measurements that can be performed in parallel. The advantage of this approach [456]
is then that the coherence time to make a single measurement after preparing the state
is _O_ (1). The disadvantage relative to the PEA is that the scaling in the total number
of operations as a function of the desired precision is quadratically worse [456]. The
scaling will also reflect the number of state preparation repetitions required, whereas in
PEA the number of state preparation steps is constant.
In the end, however, the QEE dramatically reduces the coherence time requirement,
while maintaining an exponential advantage over the classical case by adding only a
polynomial number of repetitions with respect to QPE [456].

_10.1.2. Quantum variational eigensolver_ The quantum variational eigensolver (QVE)

[456] is based on the Ritz variational principle, finding the minimum of the expectation
value of the Hamiltonian under variation of the trial state function: (i) prepare the trial


state _|_ __ __ ; (ii) compute the Rayleigh-Ritz quotient _< H_ _i_ _>_ = __ __ _|_ _H_ _i_ _|_ __ __ _/_ __ __ _||_ __ __ of all the
terms in the Hamiltonian using the QEE as a subroutine; (iii) calculate _i_ _< H_ _i_ _>_ ; (iv)
compare the resulting energy with the previous runs and feed back new parameters for 
the trial state. Note that the only step that is quantum is step (iii) - the other steps
are prepared using a classical computer.
The issue now concerns state preparation. One example of a quantum state
parameterised by a polynomial number of parameters for which there is no known
efficient classical implementation is the unitary coupled cluster ansatz (UCC) [393,456]

__ = _e_ _T_ __ _T_ __ __ _ref_ (112)
_|_ __ _|_ __

70


-----


where __ _ref_ is some reference state, usually the Hartree Fock ground state, and T is
_|_ __
the cluster operator for an N electron system, defined by operators

_T_ = _T_ 1 + _T_ 2 + _T_ 3 + _...._ + _T_ _N_ (113)

producing 1 _,_ 2 _,_ 3 _, ...., N_ electron-hole pairs from the N-electron reference state. Explicity
for _T_ 1 and _T_ 2 :


_T_ 1 =

_T_ 2 =


_t_ _pq_ _c_ + _p_ _c_ _q_ (114)
_pq_



_t_ _pqrs_ _c_ + _p_ _c_ + _q_ _c_ _r_ _c_ _s_ (115)
_pqrs_




The series in Eqs. (114),(115) generate in principle all possible configurations for FCI,
producing all possible ground and excited state correlations.
In real molecules, often a limited number of these correlations produce the bulk of
the interaction energy due to the Coulomb repulsion. The problem is that to achieve
the accuracy needed for describing realistic molecular chemical energy surfaces and
accurately predicting chemical reaction paths, a large number of small correlations are
needed to build up to the final accurate result. This is QMA-hard, i.e. intractable
for both classical and quantum computers. It therefore becomes a question of useful
approximations. Again, note here the recent work by Carleo and Troyer [362].
In the case of the two-electron _H_ 2 and _He_ - _H_ + molecules, _N_ = 2. The cluster
operators are then limited to _T_ 1 and _T_ 2 in Eq. (112) and it is possible to apply the full
machinery with suitable approximations and to obtain chemical accuracy.

_10.1.3._ _H-H ground-state energy curve_ We will now describe an experimental
application of the QVE to the problem of the ground-state energy curve of the hydrogen
molecule [38].
For a 2-electron system, the Hamiltonian reduces to



_H_ =


_h_ _i_ ( _R_ ) __ _i_ +
_i_


_h_ _i,j_ ( _R_ ) __ _i_ __ _j_ (116)
_i,j_


or equivalently


_H_ = _g_ 0 **1** + _g_ 1 _Z_ 0 + _g_ 2 _Z_ 1 + _g_ 3 _Z_ 0 _Z_ 1 + _g_ 4 _X_ 0 _X_ 1 + _g_ 5 _Y_ 0 _Y_ 1 (117)

where the set of parameters _g_ _i_ = _g_ _i_ ( _R_ ) depends on the _H_ - _H_ distance and is obtained
from the expectation values of the Hamiltonian terms evaluated on a classical computer
using the basis (reference) states.
We discussed quantum state preparation in general in Sect. 9, and the coupledcluster approach above. In the QVE, the state _|_ __ ( __ ) __ is parameterised by the action of

 
a quantum circuit _U_ ( __ ) on an initial state __ _ref_ , i.e. __ ( __ ) = _U_ ( __ ) __ _ref_ . Even if __ ( __ )
_|_ __ _|_ __ _|_ __ _|_ __


is a simple product state and _U_ ( __ ) is a very shallow circuit, __ _ref_ can contain complex
_|_ __
many-body correlations and span an exponential number of standard basis states.
The unitary coupled cluster approach states that the ground state of Eq. (112) can
be expressed as

__ ( __ ) = _U_  ( __ ) __ _HF_ = _e_ __ _iX_ 0 _Y_ 1 01 (118)
_|_ __ _|_ __ _|_ __

71


-----


where _|_ 01 __ is the Hartree-Fock (mean-field) state of molecular hydrogen in the
representation of Eq. (112). The gate model circuit that performs this unitary mapping
is shown in the software section of Fig. (29).

![G_Wendin_Review_of_superconducting_circuits.pdf-71-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-71-0.png)

Figure 29: Schematic of the application of the quantum variational eigensolver (QVE) to
the _H_ 2 ground state energy. The hardware part (top panel) shows two Xmon transmon
qubits and microwave pulse sequences to perform single-qubit rotations (thick lines), dc
pulses for two-qubit entangling gates (dashed lines), and microwave spectroscopy tones for
qubit measurements (thin lines). The software quantum circuit diagram (bottom panel)
shows preparation of the Hartree-Fock state, followed by application of the unitary coupled
cluster ansatz (UCC) in Eqs. (112),(115) and efficient partial tomography (R _t_ ) to measure the
expectation values in Eq. (118). Finally, the total energy is computed via the QEE protocol
according to Eq. (118) and provided to a classical optimiser that suggests new parameters __
for the time evolution operator _U_  ( __ ) (right panel). Adapted from [38].

The total bonding energy curve in Fig. (30) demonstrates chemical accuracy (better
than 10 __ 3 hartree), which is a very important result. In contrast, the calculation using
the full canonical protocol of trotterisation plus quantum phase estimation (PEA) turns
out much less accurate, amply demonstrating that the fully quantum approach is very
demanding on coherence time.

_10.1.4._ _He-H_ + _ground-state energy curve_ The QVE was originally applied to the
al. [456] . Recently, Wang et al. [473] applied the IPEA to the helium-hydride cation _He_ __ _H_ + problem on a 2-qubit photonic processor by Peruzzo et _He_ __ _H_ + problem using
a solid-state quantum register realised in a nitrogen-vacancy centre (NVC) in diamond,
reporting an energy uncertainty (relative to the model basis) of the order of 10 __ 14

hartree, 10 orders of magnitude below the desired chemical precision. However, this
remarkable precision only refers to the 13 iterations of the IPEA itself. The fundamental
propagation of the quantum state using the time evolution operator was done on a
classical computer. In a fully quantum approach trotterisation will be necessary to
create the state, which will put high demands on precision and coherence time. With

72


-----


![G_Wendin_Review_of_superconducting_circuits.pdf-72-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-72-0.png)

Figure 30: Total energy curve of molecular hydrogen as determined by both QVE and PEA.
The QVE approach shows dissociation energy error of (8 __ 5) __ 10 __ 4 hartree (error bars on
QVE data are smaller than markers). The PEA approach shows dissociation energy error of
(1 __ 1) __ 10 __ 2 hartree. Adapted from [38].

present hardware systems, this will drastically reduce the accuracy, as is clear from the
experimental results for _H_ 2 in Fig. 30 [38].

_10.1.5._ _Ground-state energy curves for H_ 2 _, LiH and BeH_ 2 The IBM group has
recently demonstrated [41] the experimental optimisation of up to six-qubit Hamiltonian
problems with over a hundred Pauli terms, determining the ground state energy curves
of H 2 , LiH and BeH 2 . Instead of the UCC, they use trial states parameterised by
quantum gates that are tailored to the available physical devices. This hardware-efficient
approach [41] does not rely on the accurate implementation of specific two-qubit gates - it
can be used with any time-evolution operator that generates sufficient entanglement. In
the present experiments, two-qubit cross-resonance (CR) gates were used as components
of the entanglers. This is in contrast to UCC trial states that require high-fidelity
quantum gates approximating a unitary operator designed to describe a theoretical
ansatz.

_10.2. Toward large-scale simulations_

_10.2.1._ _From high-level language to hardware instructions_ In order to assess the
computational capability of even a small quantum systems for producing total-energy
surfaces with chemical accuracy, it is necessary to develop simulation SW all the way
from high-level language programs down to HW-specific instructions. H aner et al. [198]
have recently developed a SW methodology for compiling quantum programs that
goes beyond the simulators that have been developed so far. The approach involves
an embedded domain-specific language by representing quantum types and operations

73


-----


through types and functions existing in a classical host language, underlining the roles
of quantum computers as special purpose accelerators for existing classical codes. In
the near term, a quantum SW architecture will allow the control of small-scale quantum
devices and enable the testing, design, and development of components on both the HW
and SW sides [198].

_10.2.2. Quantum computer emulation_ H aner et al. [199] have introduced the concept
of a quantum computer emulator as a component of a SW framework for quantum
computing. A QC emulator is an interface (HW or SW) that makes the user believe
that he/she is operating a quantum computer even if the calculations are performed
classically. This can enable a significant performance advantage by avoiding simulating
essentially classical boolean logic by quantum gate operations. H aner et al. [199] describe
various optimisation approaches and present benchmarking results, establishing the
superiority of quantum computer emulators in terms of performance. The results
show [199] that emulating quantum programs allows one to test and debug large
quantum circuits at a cost that is substantially reduced when compared to the simulation
approaches which have been taken so far. The advantage is already substantial for
operations such as the quantum Fourier transforms, and grows to many orders of
magnitude for arithmetic operations, since emulation avoids simulating ancilla qubits
(needed for reversible arithmetic) at an exponential cost. Emulation will thus be
a crucial tool for testing, debugging and evaluating the performance of quantum
algorithms involving arithmetic operations.

_10.2.3. Electronic structure calculations - molecules_ To describe the function of an
enzyme from first principles is a computationally hard problem. While at present a
quantitative understanding of chemical processes involving complex open-shell species
remains beyond the capability of classical computer simulations, the work of Reiher et
al. [201] shows that quantum computers used as accelerators to classical computers could
be used to elucidate this mechanism using a manageable amount of memory and time.
In this context a quantum computer would be used to obtain, validate, or correct the
energies of intermediates and transition states and thus give accurate activation energies
for various transitions. In particular, Reiher et al. [201] show how a quantum computer
can be employed to elucidate reaction mechanisms in complex chemical systems, using
the open problem of biological nitrogen fixation in nitrogenase as an example. Detailed
resource estimates show that, even when taking into account the substantial overhead of
quantum error correction, and the need to compile into discrete gate sets, the necessary
computations can be performed in reasonable time on small quantum computers. This
demonstrates that quantum computers will realistically be able to tackle important
problems in chemistry that are both scientifically and economically significant.
However, the required quantum computing resources are comparable to that needed
for Shors factoring algorithm for interesting numbers, both in terms of number of gates
and physical qubits [201]. The complexity of these simulations is thus typical of that

74


-----


required for other targets for quantum computing, requiring robust qubits with long
coherence time.

_10.2.4. Electronic structure of strongly correlated materials_ Using a hybrid quantumclassical algorithm that incorporates the power of a small quantum computer into a
framework of classical embedding algorithms [200,475], the electronic structure of complex correlated materials can be efficiently tackled using a quantum computer. The
quantum computer solves a small effective quantum impurity problem that is selfconsistently determined via a feedback loop between the quantum and classical computation. Use of a quantum computer enables much larger and more accurate simulations
than with any known classical algorithm. This will allow many open questions in quantum materials to be resolved once small quantum computers with around one hundred
long-lived (logical) qubits become available.

75


-----

# **11. Adiabatic quantum optimisation**

It is not known to what extent coherence and entanglement are essential for AQC.
(Except, since AQC has been shown to be equivalent to DQC [80], one would perhaps
expect that coherence and entanglement are needed also for AQC to provide optimum
processing speed).

_11.1. Adiabatic quantum algorithms_

Adiabatic quantum optimisation (AQO) is an adiabatic form of analogue quantum
computing/simulation [7881, 92, 476478]. AQO is in principle universal [80] and
equivalent to the digital circuit model. AQO refers to zero temperature. In AQO one


considers the time evolution _|_ __ ( _t_ ) __ = _U_ ( _t,_ 0) _|_ __ (0) __ with a time-dependent Hamiltonian
of the form:

  
_H_ ( _t_ ) = [1 __ _s_ ( _t_ )] _H_ 0 + _s_ ( _t_ ) _H_ _T_ (119)

_s_ ( _t_ ) is a scalar function of time running from 0 to 1, controlling the adiabatic switching.
The starting Hamiltonian _H_ 0 is given on a simple form, and the target Hamiltonian _H_ _T_
is designed to encode the problem under consideration, often defined by an Ising type of
Hamiltonian. One then searches for an optimal path on the ground state energy surface
toward a global energy minimum representing a final solution __ ( _t_ _f_ ) described by the
_|_ __
target Hamiltonian _H_ _T_ (Fig. 31).


![G_Wendin_Review_of_superconducting_circuits.pdf-75-0.png](G_Wendin_Review_of_superconducting_circuits.pdf-75-0.png)

![G_Wendin_Review_of_superconducting_circuits.pdf-75-1.png](G_Wendin_Review_of_superconducting_circuits.pdf-75-1.png)

Figure 31: Quantum adiabatic optimisation (AQO) and quantum annealing (QA). _H_  ( _t_ ) =
_A_ ( _t_ ) _H_  0 + _B_ ( _t_ ) _H_  _T_ . Spin-glass (Ising) type of cost function defining the energy landscape
_H_ _T_ = _ij_ _a_ _ij_ _x_ _i_ _x_ _j_ + _i_ _b_ _i_ _x_ _i_ . Adapted from [111]

 

The philosophy behind AQO is that a wide range of problems in science can be
formulated as Ising models (see e.g. Refs. [361, 479485]), and therefore AQO could
be a practical way to proceed toward addressing hard spin-glass type of problems with
quantum computing. The vision is that gate-driven DQS will need extensive error
correction and is, at best, a distant option, while AQO may be able to shorten that long
path. However, there is seldom any free lunch - in the end calibration and embedding
issues may limit the real power of AQO.

76


-----


_11.2. Quantum annealing_

In Quantum Annealing (QA) the temperature of a system is lowered during the timeevolution of the Hamiltonian until the system gets trapped in an energy minimum,
preferably a global minimum, but more typically a local one [109,124,392,486,487].
Quantum annealing can be looked upon in typically two ways:
(i) As an extension of classical Simulated Annealing (SA) by including quantum
tunneling in addition to thermal hopping over the barriers (Fig. 11.2) [476,488] .
(ii) As a version of Adiabatic QC/QS applied to real systems influenced by noise and
imperfections [477] .
Traditionally, SA and QA have been performed with software running on classical
machines, solving both classical and quantum problems, e.g. using quantum Monte
Carlo (QMC), including descriptions of quantum tunneling [488]. Recently, however,
the D-Wave machines (DW1-108 qubits; DW2-504 qubits; D-Wave 2X-1152 qubits) have
been used to perform annealing in hardware. The mission is to perform QA (actually
AQO), and the goal has been to gain decisive speedup over classical machines because
the hardware is intended to function as quantum circuits and to be able to profit from
coherence and entanglement.
The D-Wave Systems machines are built top-down - scaling up is based on flux
qubits and circuits with short coherence time [123, 124, 486]. The technology is based
on classical Nb RSFQ circuits combined with Nb rf-SQUID qubits, and forms the basis
of the current D-Wave processors. The architecture is based on a cross-bar network
of communication buses allowing (limited) coupling of distant qubits. The qubits are
operated by varying the dc-bias, changing the qubit energies and qubit-qubit couplings.
As a result, the coherence and entanglement properties have to be investigated by
performing various types of experiments on the machines and their components: Physics
experiments on the hardware [123, 489], and benchmarking of the performance by
running a range of QA schemes [109,111,392,487,490496].
During the last three years, the topic has rapidly evolved, and by now a certain
common understanding and consensus has been reached. Based on the discussion in
some recent papers [111,112,497506], the situation can be summed up in the following
way:



__ The behaviour of the D-Wave machines is consistent with quantum annealing.



__ No scaling advantage (quantum speedup) has so far been seen [503,505,506].



__ QA is efficient in quickly finding good solutions as long as barriers are narrow, but
ultimately gets stuck once broad barriers are encountered



__ The Google D-Wave 2X results showing million-times speedup [111] are for native
instances that perfectly fit the hardware graph of the device [112].

__ For generic problems that do not map well onto the hardware of a QA, performance
will suffer significantly [112,503,505,506].

77


-----



__ Even more efficient classical optimisation algorithms exist for these problems
(mentioned in [111]), which outperform the current D-Wave 2X device for most
problem instances [498,500,501]. However, the race is on [505,506].

__ With improved engineering, especially faster annealing and readout, the time to
perform a quantum annealing run can be reduced by a factor 100x over the current
generation QA devices [112].

__ However, misspecification of the cost function due to calibration inaccuracies is a
challenge that may hamper the performance of analogue QA devices [112].

__ Another challenge is the embedding of problems into the native hardware
architecture with limited connectivity.



__ There is the open question of quantum speedup in analogue QA [503,504].

__ QA error correction has been demonstrated and may pave a path toward large scale
noise-protected AQO devices [495,496].

__ Typically, classically computationally hard problems also seem to be hard problems
for QA devices [503].

__ Improved machine calibration, noise reduction, optimisation of the QA schedule,
larger system sizes and tailored spin-glass problems may be needed for
demonstrating quantum speedup. However what is hard may not be easy to
judge [505,506].

__ It remains to see what the newest D-Wave 2000Q system can do with 2000 qubits.

78


-----

# **12. Perspectives**

_12.1. Looking back_

Once upon a time, in 2010, there was a major European flagship project proposing
to marry QIPC to classical high-performance computing (HPC). The effort failed (like
earlier the Swedish flagship Wasa, 1628), for a number of good reasons: (i) The HPC
people had essentially no knowledge of what QIPC might be good for, and the QIPC
side had no really convincing arguments; (ii) There was no clear and convincing focus
on scalable quantum hardware and software; (iii) Solid-state circuits were still at an
embryonic level, demonstrating some limited basic QIP functionality only at the 2-3
qubit level.
Since then, there has been dramatic progress in the way of superconducting devices
and systems. It is now possible to build a variety of superconducting Josephson junction
multi-qubit platforms able to seriously address proof-of-principles quantum simulations
of significant interest for future Materials Science and Chemistry, as well as smallerscale Physics problems (e.g. quantum magnetism) where classical computers already
now cannot provide solutions. Moreover, D-Wave Systems now operates 2000 qubit
systems for quantum annealing. One can expect these systems to develop toward better
coherence. This means that there will be a range of systems and problems that can be
investigated from both bottom-up and top-down points of view.
Fortunately this message has now reached the European Union - a Quantum
Technologies flagship will be launched in January 2019.

_12.2. Looking around_

The focus of the present review has so far been on superconducting devices and hybrid
systems. It is now time to broaden the scope a bit and discuss the wider perspective
including a number of emerging solid-state quantum technologies.

_Spins implanted in semiconductors_ Originally, the solid-state approach to quantum
computers was a silicon-based nuclear spin quantum computer [507]. This line of
research has been very active ever since, with extensive efforts on technology for
implanting spin impurities in semiconductors, in particular silicon. Presently there
is great progress at the 1- and 2-qubit level [508514] with reported qubit lifetimes up
to 30 seconds [508] and robust 2-qubit gates [511]. Nevertheless, experience suggests
that it may take quite some time to build multi-qubit systems. Possible routes may
be on-chip coupling of implanted impurity spin arrays [515], or photonic coupling of
individual spin qubits.
From a QIP point of view, however, the most advanced spin systems involve multiqubit NV-centres in diamond [516,517], with demonstrations of quantum error correction
(QEC) [375] and digital quantum simulation (DQS) [473]. There are also advanced plans
for large-scale QIP in diamond [518].

79


-----


_Interfaces and networks_ In the future Quantum Internet [321,519] interfaces between
stationary qubits and photons will be critically important. Such interfaces involve
the entanglement of qubits with single-photon emitters [520] and are typically based
on semiconductor quantum dots [521, 522] or NV-centres [521, 523]. Important
experimental steps toward large-scale quantum networks have recently been taken
through demonstrations of loophole-free Bell tests [524,525], quantum network memory

[526], perfect state transfer of an entangled photonic qubit [527], and digital photonic
QIP [528530].

_Sensors_ The future ultimate sensor may be a quantum computer at the tip of a
scanning probe - SPQ - where e.g. the measured dephasing of the quantum
device provides the information. Presently the quantum device is typically a diamond
nanocrystal with an NV centre working as an advanced NMR probe with a built-in
quantum pre-processor (see e.g. [531535] and refs. therein).

_Microfabricated ion traps_ There is intense work on scaling up microfabricated ion
traps [536, 537], with applications to benchmarking [538], computing [539541] and
simulation [542,543]. The NIST simulation [543] involves up to 219 ions (qubits) with
global control, simulating spin-dynamics in a classically tractable 2D Ising model, laying
the groundwork for the classically hard case of the transverse Ising model with variable
range interactions.

_Non-equilibrium quantum dynamics_ Strongly driven non-equilibrium Floquet systems
can exhibit persistent time correlations at an emergent subharmonic frequency - referred
to as discrete time crystal (DTC). Very recently discrete time translational symmetry
breaking into a DTC has been observed experimentally in strongly driven spin systems,
in an ion trap with 10 ions [544], and in an NV crystal with 10 6 disordered nuclear
spins [545]. The work creates opportunities for exploring dynamical phases of matter and
to control interacting, disordered many-body systems. This includes topological phases
that might be used for quantum information tasks (see [544,545] and refs. therein).

_Quantum cloud computing_ In May 2016, IBM launched a cloud-enabled quantum
computing platform, called IBM Quantum Experience, to allow users to run algorithms
and experiments on a 5-qubit superconducting transmon-cQED quantum processor.
One year later, in May 2017, the web-connected platform was expanded to 16 qubits

[546548], and a 17-qubit platform was announceed to go commercial in the near future.
Although even a 16-qubit quantum simulator remains a toy, to make it available online
for experimentation represents a kind of intellectual crowd funding - it provides an
interesting new game, and paves the way for new applications. Moreover, it may put
focus on the issue of which platform (and/or which nation in the world) is going to
win the race for the quantum computer. In the authors opinion this is a hyped
non-issue - the dominance of nations, and the fate of the world, will not depend on

80


-----


quantum computers in a long time to come. Nevertheless, serious comparisons of scalable
alternatives [549] are very important and useful. In the end, hybrid platforms has always
been the name of the game - the problem is to develop efficient communication interfaces.

_12.3. Looking ahead_

The field of experimental and applied quantum information processing with
superconducting Josephson junction-based circuits and systems is now preparing for
scaling up to levels of Quantum Supremacy. Within a few years there will be wellcontrolled coherent platforms with 20-50 qubits addressing a range of algorithms and
benchmarking protocols, comparing favourably against the best classical systems and
algorithms. And in view of the commitments of various groups around the world, in 5-7
years there will most likely be coherent functional 100 qubit superconducting systems
claiming Quantum Supremacy.
Despite the experimental evidence of Majorana bound states, there is probably a
long way to go to demonstrate functional Majorana qubits, and to manipulate them
in efficient ways. The situation reminds a bit of the situation with superconducting
qubits 20 years ago: highly developed theory but only emerging experimental evidence
for potential superconducting qubits. Regarding Majoranas, only time will tell.
Quantum computing, emulation and simulation have finally become serious
endeavours at a practical level, promising approximate solutions to hard problems
with quantum speedup. To describe the structure and function of complex biological
molecules, computational chemistry has developed multi-scale modelling (see e.g.
Warshel [550]). This means embedding quantum problems in a classical molecular and
dielectric environment to make the full problem (more) tractable, only involving the
quantum solver when the physics is manifestly quantum. The catalytic centre of an
enzyme, or the protein-producing core a ribosome, do need a full quantum-chemical
treatment. In contrast, the surrounding molecular cage and solvent can be described
by classical molecular dynamics and dielectric screening. In a similar way, a quantum
computer must necessarily be embedded in a classical HPC environment, forming a
hybrid classical system with a quantum accelerator. Since this is the way Biology and
Life works, it looks like a good idea to pursue computational science in a similar way.

# **Acknowledgement**

This work has been supported by the European Commission under contract ICT- FP7
600927 ScaleQIT, and by Chalmers University of Technology. The author is grateful for
illuminating and helpful discussions with Michel Devoret, John Martinis, Will Oliver,
Vitaly Shumeiko and Frank Wilhelm.

81


-----