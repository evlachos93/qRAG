
## A Quantum Engineers Guide to Superconducting Qubits
P. Krantz 1 _,_ 2 _,_ __ , M. Kjaergaard 1 , F. Yan 1 , T.P. Orlando 1 , S. Gustavsson 1 , and W. D. Oliver 1 _,_ 3 _,_ __

1 _Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139,_
_USA_
2 _Wallenberg Centre for Quantum Technology (WACQT), Chalmers University of Technology, Gothenburg, SE-41296,_
_Sweden and_
3 _MIT Lincoln Laboratory, 244 Wood Street, Lexington, MA 02420, USA_

(Dated: 9 July 2021)

The aim of this review is to provide quantum engineers with an introductory guide to the central concepts
and challenges in the rapidly accelerating field of superconducting quantum circuits. Over the past twenty
years, the field has matured from a predominantly basic research endeavor to one that increasingly explores
the engineering of larger-scale superconducting quantum systems. Here, we review several foundational
elements  qubit design, noise properties, qubit control, and readout techniques  developed during this
period, bridging fundamental concepts in circuit quantum electrodynamics (cQED) and contemporary, stateof-the-art applications in gate-model quantum computation.


**CONTENTS**

**I. Introduction** 2
A. Organization of this article 2

**II. Engineering quantum circuits** 3
A. From quantum harmonic oscillator to the
transmon qubit 3
B. Qubit Hamiltonian engineering 6
1. Tunable qubit: split transmon 6
2. Towards larger anharmonicity: flux qubit
and fluxonium 7
C. Interaction Hamiltonian engineering 9
1. Physical coupling: capacitive and
inductive 9
2. Coupling axis: transverse and
longitudinal 10

**III. Noise, decoherence, and error mitigation** 12
A. Types of noise 12
1. Systematic noise 12
2. Stochastic noise 12
3. Noise strength and qubit susceptibility 12
B. Modeling noise and decoherence 12
1. Bloch sphere representation 12
2. Bloch-Redfield model of decoherence 13
3. Modification due to 1 _/f_ -type noise 16
4. Noise power spectral density (PSD) 17
C. Common examples of noise 18
1. Charge noise 18
2. Magnetic flux noise 18
3. Photon number fluctuations 19
4. Quasiparticles 19
D. Operator form of qubit-environment
interaction 19

 __ philipk@mit.edu, __ william.oliver@mit.edu


1. Connecting _T_ 1 to _S_ ( __ ) 19
2. Connecting _T_ __ to _S_ ( __ ) 20
3. Noise spectroscopy 21
E. Engineering noise mitigation 21
1. Materials and fabrication improvements 22
2. Design improvements 22
3. Dynamical error suppression 22
4. Cryogenic engineering 22

**IV. Qubit control** 22
A. Boolean logic gates used in classical
computers 23
B. Quantum logic gates used in quantum
computers 24
C. Comparing classical and quantum gates 26
1. Gate sets and gate synthesis 27
2. Addressing superconducting qubits 27
D. Single-qubit gates 27
1. Capacitive coupling for X , Y control 28
2. Virtual Z gate 30
3. The DRAG scheme 30
E. The _i_ SWAP two-qubit gate in tunable
qubits 31
1. Deriving the _i_ SWAP unitary 31
2. Applications of the _i_ SWAP gate 33
F. The CPHASE two-qubit gate in tunable
qubits 33
1. Trajectory design for the CPHASE gate 35
2. The CPHASE gate for quantum error
correction 35
3. Quantum simulation and algorithm
demonstrations using CPHASE 36
G. Two-qubit gates using only microwaves 37
1. The operational principle of the CR gate 37
2. Improvements to the CR gate and
quantum error correction experiments
using CR 38
3. Quantum simulation and algorithm
demonstrations with the CR gate 38


-----


4. Other microwave-only gates: _b_ SWAP ,
MAP , and RIP 39
H. Gate implementations with tunable
coupling 40

**V. Qubit readout** 41
A. Dispersive readout 41
B. Measuring the resonator amplitude and
phase 43
1. Representation of the readout signal 43
2. I-Q mixing 44
3. Homodyne demodulation 44
4. Heterodyne demodulation 45
C. Weak and strong qubit measurements:
Impact of noise 46
D. Purcell filters for faster readout 48
E. Improve signal-to-noise ratio: Parametric
amplification 50
1. Quantum-limited amplification processes 50
2. Operation of Josephson parametric
amplifiers 51
3. The traveling wave parametric amplifier 53

**VI. Summary and outlook** 54

**Acknowledgments** 55

**I.** **INTRODUCTION**

Quantum processors harness the intrinsic properties of

16
quantum mechanical systems  such as quantum parallelism and quantum interference  to solve certain problems where classical computers fall short . Over the
past two decades, rapid developments in the science and

7,8
engineering of quantum systems have advanced the frontier in quantum computation, from the realm of scientific explorations on single isolated quantum systems toward the creation and manipulation of multi-qubit processors . In particular, the requirements imposed by
larger quantum processors have shifted of mindset within
the community, from solely scientific discovery to the development of new, foundational engineering abstractions
associated with the design, control, and readout of multiqubit quantum systems. The result is the emergence of a
new discipline termed _quantum engineering_ , which serves
to bridge the basic sciences, mathematics, and computer
science with fields generally associated with traditional
engineering.
One prominent platform for constructing a multi-qubit
quantum processor involves superconducting qubits, in
which information is stored in the quantum degrees of
freedom of nanofabricated, anharmonic oscillators constructed from superconducting circuit elements. In contrast to other platforms, e.g.
914 1518 1923
electron spins in silicon and quantum dots , trapped ions
2427 28,29
, ultracold atoms , nitrogen-vacancies in diamonds ,


and polarized photons , where the quantum information is encoded in natural microscopic quantum systems, 3033
superconducting qubits are macroscopic in size and lithographically defined.
One remarkable feature of superconducting qubits is
that their energy-level spectra are governed by circuit element parameters and thus are configurable; they can be
designed to exhibit atom-like energy spectra with desired properties. Therefore, superconducting qubits are
also often referred to as _artificial atoms_ , offering a rich
parameter space of possible qubit properties and operation regimes, with predictable performance in terms of
transition frequencies, anharmonicity, and complexity.
While there are many other excellent reviews on superconducting qubits, see e.g. Refs. 3443, this work
specifically aims to introduce new quantum engineers
(academic and industrial alike) to the terminology and
state-of-the-art practices used in the rapidly accelerating field of superconducting quantum computing. The
reader is assumed to be familiar with basic concepts that
span classical physics, quantum mechanics, and electrical
engineering. In particular, readers will find it useful to
have had previous exposure to classical mechanics, the
Schr odinger equation, the Bloch sphere representation of
qubit states, second quantization, basic concepts of superconductivity, electromagnetism, introductory circuit
analysis, classical boolean logic, linear dynamical systems, analog and digital signal processing, and familiarity with microwave components such as transmission
lines and mixers. These topics will be introduced as they
arise, but having basic prior knowledge will be helpful.

**A.** **Organization of this article**

This review is organized in the following four sections;
first, in Sec. II, we explore the parameter space available when designing superconducting circuits. In particular, we look at the promising capacitively-shunted planar
qubit modalities and how these can be engineered with
desired properties, such as transition frequency, anharmonicity, and reduced susceptibility to various sources
of noise. In this section, we also introduce several ways
in which interactions between qubits can be engineered,
in order to implement two-qubit entangling operations,
needed for a universal gate set.
In Sec. III, we discuss systematic and stochastic noise,
the concepts of noise strength and qubit noise susceptibility, and the common sources of noise which lead to
decoherence in superconducting circuits. We introduce
the Bloch-Redfield model of decoherence, characterized
by longitudinal and transverse relaxation times _T_ 1 and
_T_ 2 , and discuss the implications of 1 _/f_ noise. We then
define the noise power spectral density, which is commonly used to characterize noise processes, and describe
how it drives decoherence. Finally, we close the section
with a review of coherent control methods used to mitigate certain types of coherence, reversible noise.


-----


The time-independent Hamiltonian _H_  governs the time
evolution of the system through the operator _e_ __ _i_  _Ht/_  .
Thus, just as with classical systems, determining the
Hamiltonian of a system  whether the classical Hamiltonian _H_ or its quantum counterpart  _H_  is the first step
to deriving its dynamical behavior. In Sec. IV, we consider the case when the Hamiltonian is time-dependent
in the context of qubit control.
To understand the dynamics of a superconducting
qubit circuit, it is natural to start with the classical description of a linear LC resonant circuit [Fig. 1(a)]. In
this system, energy oscillates between electrical energy
in the capacitor _C_ and magnetic energy in the inductor
_L_
. In the following, we will arbitrarily associate the electrical energy with the kinetic energy and the magnetic
energy with the potential energy of the oscillator. The
instantaneous, time-dependent energy in each element is
derived from its current and voltage,


In Sec. IV, we provide a review of how single- and
two-qubit operations are typically implemented in superconducing circuits, by using a combination of local magnetic flux control and microwave drives. In particular, we
discuss the family of two-qubit gates arising from a capacitive coupling between qubits, and introduce several
recent advances that have been demonstrated to achieve
high-fidelity gates, as well as applications in quantum
information processing that use these gates. The continued development of high-fidelity two-qubit gates in superconducting qubits is a highly active research area. For
this reason, we include sufficient technical details that a
reader may use this review as a starting point to critically
assess the pros and cons of the various gates, as well as
develop an appreciation for the types of gate-engineering
already implemented in state-of-the-art superconducting
quantum processors.
Finally, in Sec. V, we discuss the physics and engineering associated with the dispersive readout technique,
typically used to measure the individual qubit states in
modern quantum processors. After a discussion of the
theory behind dispersive coupling, we give an introduction to design of Purcell filters and the development of
quantum-limited parametric amplifiers.

**II.** **ENGINEERING QUANTUM CIRCUITS**

In this section, we will demonstrate how quantum systems based on superconducting circuits can be engineered
to achieve certain desired properties. Using the most
common qubit modalities, we discuss how properties such
as the qubit transition frequency, anharmonicity, and
noise susceptibility can be tailored by the choice of circuit
topology and element parameter values. We also discuss
how to engineer the interactions between different quantum systems, in particular the cases of qubit-qubit and
qubit-resonator couplings.

**A.** **From quantum harmonic oscillator to the transmon**
**qubit**

A quantum mechanical system is governed by the timedependent Schr odinger equation,


_E_ ( _t_ ) =



_V_ ( _t_ __ ) _I_ ( _t_ __ ) _dt_ __ _,_ (3)
__


where _V_ ( _t_ __ ) and _I_ ( _t_ __ ) denote the voltage and current of
the capacitor or inductor.
To derive the classical Hamiltonian, we follow the standard approach used in classical mechanics: the LagrangeHamilton formulation. Here, we represent the circuit elements in terms of one of its generalized circuit coordinates, charge or flux. In the following, we pick flux,
defined as the time integral of the voltage


_t_
( _t_ ) =



_V_ ( _t_ __ ) _dt_ __ _._ (4)
__


In this example, the voltage at the node is also the branch
voltage across the element. In this section, we will simply
refer to these as node voltages and fluxes for convenience.
For a more detailed discussion of nodes and branches in
this context, we refer the reader to Ref. 44.
Note that in the following, we could have exchanged
our associations with kinetic energy (momentum coordinate) and potential energy (position coordinate), and
instead start with the charge variable _Q_ ( _t_ ), which is the
time integral of the current _I_ ( _t_ ).
By combining Eqs. (3) and (4), using the relations _V_ =
_L dI/dt_ and _I_ = _C dV/dt_ , and applying the integration
by parts formula, we can write down energy terms for the
capacitor and inductor in terms of the node flux,


_H_  __ ( _t_ ) = _i_  __ __ ( _t_ ) _,_ (1)
_|_ __ _t_ _|_ __

where __ ( _t_ ) is the state of the quantum system at time
_|_ __
_t_ ,  is the reduced Plancks constant _h/_ 2 __ , and _H_  is the
_Hamiltonian_
that describes the total energy of the system. The hat is used to indicate that  _H_ is a quantum
operator. As the Schr odinger equation is a first-order linear differential equation, the temporal dynamics of the
quantum system may be viewed as a straightforward example of a linear dynamical system with formal solution,

_i_  _Ht/_ 
__ ( _t_ ) = _e_ __ __ (0) _._ (2)
_|_ __ _|_ __



1 2
_C_ = _C_   _,_ (5)
_T_ 2



1
_C_ =
_T_ 2



1 2
_L_ =  _._ (6)
_U_ 2 _L_



1
_L_ =
_U_ 2


The Lagrangian is defined as the difference between
the kinetic and potential energy terms and can thus be
expressed in terms of Eqs. (5) and (6)


-----


across the inductor. These two operators form a canonical conjugate pair, obeying the commutation relation

[ _, n_ ] = _i_ . We note that the factor 4 in front of the
charging energy _E_ _C_ is solely a historical artifact, namely,
that this energy scale was first defined for single-electron
systems and then adopted to two-electron Cooper-pair
systems.
The Hamiltonian in Eq. (13) is identical to the one describing a particle in a one-dimensional quadratic potential, a quantum harmonic oscillator (QHO). We can treat
__ as the generalized position coordinate, so that the first
term is the kinetic energy and the second term is the potential energy. We emphasize that the functional form
of the potential energy influences the eigensolutions. For

2
example, the fact that this term is quadratic ( _U_ _L_ __ )
__
in Eq. (13) gives rise to the shape of the potential in Fig.
1(b). The solution to this eigenvalue problem gives an infinite series of eigenstates _k_ , ( _k_ = 0 _,_ 1 _,_ 2 _, . . ._
_|_ __
), whose corresponding eigenenergies _E_ _k_ are all equidistantly spaced,
i.e. _E_ _k_ +1 _E_ _k_ =  __ _r_ , where __ _r_ = __ 8 _E_ _L_ _E_ _C_ _/_  = 1 _/_ __ _LC_
__

denotes the resonant frequency of the system, see Fig.
1(b). We may represent these results in a more compact
form (second quantization) for the quantum harmonic
oscillator (QHO) Hamiltonian



1
= _C_ _L_ =
_L_ _T_ _U_ 2



1 2 1

_C_  
2 __ 2



2

 _._ (7)
2 _L_


From the Lagrangian in Eq. (7), we can further derive
the Hamiltonian using the Legendre transformation, for
which we need to calculate the momentum conjugate to
the flux, which in this case is the charge on the capacitor



__
_Q_ = _L_ = _C_   _._ (8)

__  

The Hamiltonian of the system is now defined as



2
_H_ = _Q_   = _Q_
_L_ 2 _C_



2 2

_Q_

+ 
2 _C_ 2 _L_



2 1

2 _L_ __ 2



1

_CV_ 2 + 1
2 2



2

_LI_ _,_ (9)
2


as one would expect for an electrical LC circuit. Note
that this Hamiltonian is analogous to that of a mechanical harmonic oscillator, with mass _m_ = _C_
, and resonant frequency __ = 1 _/_ __ _LC_


__ = 1 _/_ _LC_

, which expressed in position, _x_ , and momentum, _p_ , coordinates takes the form

2 2 2
_H_ = _p_ _/_ 2 _m_ + _m_ _x_ _/_ 2.
The Hamiltonian described above is classical. In order
to proceed to a quantum-mechanical description of the
system, we need to promote the charge and flux coordinates to quantum operators. And, whereas the classical
coordinates satisfy the Poisson bracket:


_H_ =  __ _r_



1
_a_ __ _a_ +


(14)


where _a_ __ ( _a_ ) is the creation (annihilation) operator of a
single excitation of the resonator. The Hamiltonian in
Eq. (14) is written as an energy. It is, however, often
preferred to divide by  so that the expression has units
of radian frequency, since we will later resonantly drive
transitions at a particular frequency or reference the rate
at which two systems interact with one another. Therefore, from here on,  will be omitted.
The original charge number and phase operators can
be expressed as _n_ = _n_ zpf __ _i_ ( 1 _a_ _/_ __ 4 _a_ __ ) and __ = __ zpf __ ( _a_ + _a_ 1 __ _/_ ), 4
where _n_ zpf = [ _E_ _L_ _/_ (32 _E_ _C_ )] and __ zpf = (2 _E_ _C_ _/E_ _L_ )

are the _zero-point fluctuations_ of the charge and phase
variables, respectively. Quantum mechanically, the quantum states are represented as wavefunctions that are generally distributed over a range of values of _n_ and __ and,
consequently, the wavefunctions have non-zero standard
deviations. Such wavefunction distributions are referred
to as quantum fluctuations, and they exist, even in the
ground state, where they are called zero-point fluctuations.
The linear characteristics of the QHO has a natural
limitation in its applications for processing quantum information. Before the system can be used as a qubit, we
need to be able to define a computational subspace consisting of only two energy states (usually the two-lowest
energy eigenstates) in between which transitions can be
driven without also exciting other levels in the system.
Since many gate operations, such as single-qubit gates
(Sec. IV), depend on frequency selectivity, the equidistant level-spacing of the QHO, illustrated in Fig. 1(b),


where _a_ __ ( _a_ ) is the creation (annihilation) operator of a
single excitation of the resonator. The Hamiltonian in
Eq. (14) is written as an energy. It is, however, often
preferred to divide by  so that the expression has units
of radian frequency, since we will later resonantly drive
transitions at a particular frequency or reference the rate
at which two systems interact with one another. Therefore, from here on,  will be omitted.
The original charge number and phase operators can
be expressed as _n_ = _n_ zpf __ _i_ ( 1 _a_ _/_ __ 4 _a_ __ ) and __ = __ zpf __ ( _a_ + _a_ 1 __ _/_ ), 4
where _n_ zpf = [ _E_ _L_ _/_ (32 _E_ _C_ )] and __ zpf = (2 _E_ _C_ _/E_ _L_ )



_f_
_f, g_ =
_{_ _}_ __



_f_ _g_

__ 


_g_ _g_

_Q_ __ __



_g_ _f_

__  _Q_


(10)
_Q_



__ 
 _, Q_ =
_{_ _}_ __ 



__ _Q_ _Q_

__  _Q_ __ __ 



_Q_ __ 

= 1 0 = 1 _,_ (11)
__  _Q_ __


the quantum operators similarly satisfy a _commutation_
_relation_ :



[   _,_ _Q_  ] =   _Q_  __ _Q_   =  _i_  _,_ (12)

where the operators are indicated by hats. From this
point forward, however, the hats on operators will be
omitted for simplicity.
In a simple LC resonant circuit [Fig. 1(a)], both the
inductor _L_ and the capacitor _C_
are linear circuit elements. Defining the reduced flux __ 2 __  _/_  0 and the
__
reduced charge , we can write down the following quantum-mechanical Hamiltonian for the circuit, _n_ = _Q/_ 2 _e_



2 1 2
_H_ = 4 _E_ _C_ _n_ + 2 _E_ _L_ __ _,_ (13)

2
where _E_ _C_ = _e_ _/_ (2 _C_ ) is the charging energy required
to add _each_ electron of the Cooper-pair to the island

2
and _E_ _L_ = ( 0 _/_ 2 __ ) _/L_ is the inductive energy, where
 0 = _h/_ (2 _e_
) is the superconducting magnetic flux quantum. Moreover, the quantum operator _n_
is the excess number of Cooper-pairs on the island, and __  the
reduced flux  is denoted the gauge-invariant phase


-----


(a)

(b)


(c)


_L_ _r_ _C_ _r_ _+_ _v_ _C_ _L_ _J_ _J_ _C_ _s_





_I_ = _I_ _c_ sin( __ ) _,_ _V_ =



 _d_

2 _e_ _dt_



_,_ (15)
_dt_


resulting in a modified Hamiltonian

2
_H_ = 4 _E_ _C_ _n_ _E_ _J_ cos( __ ) _,_ (16)
__

2
where _E_ _C_ = _e_ _/_ (2 _C_  ), _C_  = _C_ _s_ + _C_ _J_
is the total capacitance, including both shunt capacitance _C_ _s_ and the
self-capacitance of the junction _C_ _J_ , and _E_ _J_ = _I_ _c_  0 _/_ 2 __ is
the Josephson energy, with _I_ _c_ being the critical current
of the junction . After introducing the Josephson junction in the circuit, the potential energy no longer takes 
a manifestly parabolic form (from which the harmonic
spectrum originates), but rather features a cosinusoidal
form, see the second term in Eq. (16), which makes the
energy spectrum non-degenerate. Therefore, the Josephson junction is the key ingredient that makes the oscillator anharmonic and thus allows us to identify a uniquely
addressable quantum two-level system, see Fig. 1(d).
Once the nonlinearity has been added, the system dynamics is governed by the dominant energy in Eq. (16),
reflected in the _E_ _J_ _/E_ _C_ ratio.
Over time, the superconducting qubit community has converged towards circuit designs with _E_ _J_ _E_ _C_ . In the opposite case when
_E_ _J_ _E_ _C_ , the qubit becomes highly sensitive to charge __
__
noise, which has proven more challenging to mitigate
than flux noise, making it very hard to achieve high coherence. Another motivation is that current technologies
allow for more flexibility in engineering the inductive (or
potential) part of the Hamiltonian. Therefore, working
in the _E_ _J_ _E_ _C_ limit, makes the system more sensitive
__
to the change in the potential Hamiltonian. Therefore,
we will focus here on the state-of-the-art qubit modalities
that fall in the regime _E_ _J_ _E_ _C_ . For readers who are
interested in the physics in the __ _E_ _J_ _E_ _C_ regime, such
__
as the earlier Cooper-pair box charge qubit, we refer to
Refs. 4851.
To access the _E_ _J_ _E_ _C_ regime, one preferred approach
is to make the charging __ _E_ _C_ small by shunting the junction
with a large capacitor, _C_ _s_ _C_ _J_ , effectively making the
__
qubit less sensitive to charge noise  a circuit commonly
known as the transmon qubit 52
. In this limit, the superconducting phase __ is a good quantum number, i.e. the
spread (or _quantum fluctuation_ ) of __ values represented
by the quantum wavefunction is small. The low-energy
eigenstates are therefore, to a good approximation, localized states in the potential well, see Fig. 1(d). We may
gain more insight by expanding the potential term of Eq.
(16) into a power series (since __ is small), that is

 The critical current is the maximum supercurrent that the junction
can support before it switches to the resistive state with non-zero
voltage.


(d)


![qe-guide-scqubits-oliver.pdf-4-0.png](qe-guide-scqubits-oliver.pdf-4-0.png)

![qe-guide-scqubits-oliver.pdf-4-1.png](qe-guide-scqubits-oliver.pdf-4-1.png)

![qe-guide-scqubits-oliver.pdf-4-3.png](qe-guide-scqubits-oliver.pdf-4-3.png)


- /2 0 /2

|Col1|Tran|smon|Col4|
|---|---|---|---|
|||||
|||||
|||||
|p. ace||||
|Com subsp||||
|||||


Superconducting phase,


- /2 0 /2


![qe-guide-scqubits-oliver.pdf-4-2.png](qe-guide-scqubits-oliver.pdf-4-2.png)

FIG. 1. **(a)**
Circuit for a parallel LC-oscillator (quantum harmonic oscillator, QHO), with inductance _L_ in parallel with
capacitance, _C_ . The superconducting phase on the island is
denoted __ , referencing ground as zero. **(b)** Energy potential
for the QHO, where energy levels are equidistantly spaced
 __ _r_ apart. **(c)** Josephson qubit circuit, where the nonlinear
inductance _L_ _J_ (represented with the Josephson-subcircuit in
the dashed orange box) is shunted by a capacitance, _C_ _s_ . **(d)**
The Josephson inductance reshapes the quadratic energy potential (dashed red) into sinusoidal (solid blue), which yields
non-equidistant energy levels. This allows us to isolate the
two lowest energy levels 0 and 1 , forming a computational
_|_ __ _|_ __
subspace with an energy separation  __ 01 , which is different
than  __ 12 .

poses a practical limitation  .
To mitigate the problem of unwanted dynamics involving non-computational states, we need to add anharmonicity (or nonlinearity) into our system. In short, we

0 1 1 2
require the transition frequencies __ q __ and __ q __
be sufficiently different to be individually adressable. In general,
the larger the anharmonicity the better. In practise, the
amount of anharmonicity sets a limit on how short the
pulses used to drive the qubit can be. This is discussed
in detail in Sec. IV D 3.
To introduce the nonlinearity required to modify the
harmonic potential, we use the Josephson junction  a
nonlinear, dissipationless circuit element that forms the
backbone in superconducting circuits 46,47 . By replacing
the linear inductor of the QHO with a Josephson junction, playing the role of a nonlinear inductor, we can
modify the functional form of the potential energy. The
potential energy of the Josephson junction can be derived
from Eq. (3) and the two Josephson relations

 Even though linear resonant systems cannot be addressed properly,
their long coherence times have proven them useful as quantum access memories for storing quantum information, where a nonlinear

45
ancilla system is used as a quantum controller for feeding and extracting excitations to/from the resonant cavity modes .


-----


**B.** **Qubit Hamiltonian engineering**

**_1._** **_Tunable qubit: split transmon_**

To implement fast gate operations with high-fidelity,
as needed to implement quantum logic, many (though
not all 63
6467
) of the quantum processor architectures implemented today feature tunable qubit frequencies . For
instance, in some cases, we need to bring two qubits into
resonance to exchange (swap) energy, while we also need
the capability of separating them during idling periods
to minimize their interactions. To do this, we need an
external parameter which allows us to access one of the
degrees of freedom of the system in a controllable fashion.
One widely-used technique is to replace the single
Josephson junction with a loop interupted by two identical junctions  forming a dc superconducting quantum
interference device (dc-SQUID) . Due to the interference between the two arms of the SQUID, the effective 68
critical current of the two parallel junctions can be decreased by applying a magnetic flux threading the loop,
see Fig. 2(a). Due to the fluxoid quantization condition,
the algebraic sum of branch flux of all of the inductive
elements along the loop plus the externally applied flux
equal an integer number of superconducting flux quanta,
that is

__ 1 __ 2 + 2 __ _e_ = 2 _k,_ (20)
__

where . Using this condition, we can eliminate one degree of freedom and treat the SQUID-loop __ _e_ = __  ext _/_  0
as a single junction, but with the important modification
that _E_ _J_ is tunable (via the SQUID critical current) by
means of the external flux  ext
. The effective Hamiltonian of the so-called split transmon (ignoring the constant) is



1
_E_ _J_ cos( __ ) =



1 2 1

_E_ _J_ __
2 __



1 4 6

_E_ _J_ __ + ( __ ) _._ (17)
24 _O_


The leading quadratic term in Eq. (17) alone will
result in a QHO, recall Eq. (13). The second term,
however, is quartic which modifies the eigensolution and
disrupts the otherwise harmonic energy structure. Note
that, the negative coefficient of the quartic term indicates

1 2 0 1
that the anharmonicity __ = __ q __ __ __ q __ is negative and
its limit in magnitude thus cannot be made arbitrarily
large. For the case of the transmon, __ = _E_ _C_ is usually
__
designed to be 100 300 MHz, as required to maintain
__
a desirable qubit frequency __ q = ( __ 8 _E_ _J_ _E_ _C_ _E_ _C_ ) _/_  =
__
3 6 GHz, while keeping an energy ratio sufficiently large
__ 52
( _E_ _J_ _/E_ _C_ 50) to suppress charge sensitivity
__
. Fortunately, the charge sensitivity is exponentially suppressed
for increased _E_ _J_ _/E_ _C_
, while the reduction in anharmonicity only scales as a weak power law, leading to a workable
device.
Including terms up to fourth order and using the QHO
eigenbases, the system Hamiltonian resembles that of a
Duffing oscillator



__
_H_ = __ q _a_ __ _a_ + 2 _a_ __ _a_ __ _aa._ (18)

Since _|_ __ _| _ __ q , we can see that the transmon qubit is
basically a weakly anharmonic oscillator (AHO). If excitation to higher non-computational states is suppressed
over any gate operations, either due to a large enough __
_|_ _|_
or due to robust control techniques such as the DRAG
pulse, see Sec. IV D 3, we may effectively treat the AHO
as a quantum two-level system, simplifying the Hamiltonian to


__ _z_
_H_ = __ q 2 _,_ (19)

where __ _z_ is the Pauli-z operator. However, one should
always keep in mind that the higher levels physically
exist 53 . Their influence on system dynamics should be
taken into account when designing the system and its
control processes. In fact, there are many cases where
the higher levels have proven useful to implement more
efficient gate operations 54 .
In addition to reducing the charge dispersion, the use
of a large shunt capacitor also enables us to engineer
the electric field distribution of the quantum system, and
thus the participation of surface loss mechanisms. In the
development of the 3D transmon 55 , e.g. a 2D transmon
coupled to a 3D cavity, it was demonstrated that by making the gap between the two lateral capacitor plates large
(compared to the film thickness) the coherence time increases since a smaller portion of the electric field interacts with the lossy interfaces, e.g. metal-substrate

5661
and substrate-vacuum interfaces, which has been studied extensively .



2
_H_ = 4 _E_ _C_ _n_ 2 _E_ _J_ cos ( __ _e_ )
__ _|_ _|_
_E_ _J_ __ ( __ _e_ )
  


cos( __ ) _._ (21)


We can see that Eq. (21) is analogous to Eq. (16), with
_E_ _J_ replaced by _E_ _J_ __ ( __ _e_ ) = 2 _E_ _J_ cos ( __ _e_ ) . The magnitude
of  of the net, effective Josephson energy 0 in applied flux and spans from 0 to its maximum _|_ _E_ _|_ _J_ __ has a period
value 2 _E_ _J_ . Therefore, the qubit frequency can be tuned
periodically with  ext , see Fig. 2(b).
While the split transmon enables frequency tunability by the externally applied magnetic field, it also introduces sensitivity to random flux fluctuations, known
as flux noise. At any working point, the slope of the
qubit spectrum, __ q _/_  ext , indicates to first order how
strongly this flux noise affects the qubit frequency. The
sensitivity is generally non-zero, except at multiples of
the flux quantum,  ext = _k_  0 , where _k_ is an integer,
where __ q _/_  ext = 0.


-----


(a)

(b)


Symmetric transmon Asymmetric transmon C-shunted Flux qubit C-shunted Fluxonium


(c)


(e)


(g)


__ _1_ __ _2_ __ _1_ __

![qe-guide-scqubits-oliver.pdf-6-0.png](qe-guide-scqubits-oliver.pdf-6-0.png)

![qe-guide-scqubits-oliver.pdf-6-3.png](qe-guide-scqubits-oliver.pdf-6-3.png)

(d)


![qe-guide-scqubits-oliver.pdf-6-1.png](qe-guide-scqubits-oliver.pdf-6-1.png)

![qe-guide-scqubits-oliver.pdf-6-2.png](qe-guide-scqubits-oliver.pdf-6-2.png)

(f)


(h)


![qe-guide-scqubits-oliver.pdf-6-4.png](qe-guide-scqubits-oliver.pdf-6-4.png)

![qe-guide-scqubits-oliver.pdf-6-5.png](qe-guide-scqubits-oliver.pdf-6-5.png)

![qe-guide-scqubits-oliver.pdf-6-6.png](qe-guide-scqubits-oliver.pdf-6-6.png)

![qe-guide-scqubits-oliver.pdf-6-7.png](qe-guide-scqubits-oliver.pdf-6-7.png)

![qe-guide-scqubits-oliver.pdf-6-8.png](qe-guide-scqubits-oliver.pdf-6-8.png)

![qe-guide-scqubits-oliver.pdf-6-9.png](qe-guide-scqubits-oliver.pdf-6-9.png)

![qe-guide-scqubits-oliver.pdf-6-10.png](qe-guide-scqubits-oliver.pdf-6-10.png)

![qe-guide-scqubits-oliver.pdf-6-11.png](qe-guide-scqubits-oliver.pdf-6-11.png)

- - /2 0 /2 - - /2 0 /2 - - /2 0 /2 - - /2 0 /2

![qe-guide-scqubits-oliver.pdf-6-12.png](qe-guide-scqubits-oliver.pdf-6-12.png)

![qe-guide-scqubits-oliver.pdf-6-13.png](qe-guide-scqubits-oliver.pdf-6-13.png)

![qe-guide-scqubits-oliver.pdf-6-14.png](qe-guide-scqubits-oliver.pdf-6-14.png)

![qe-guide-scqubits-oliver.pdf-6-15.png](qe-guide-scqubits-oliver.pdf-6-15.png)

FIG. 2. Modular qubit circuit representations for capacitively shunted qubit modalities (orange box Fig. 1c) and corresponding
qubit transition frequencies for the two lowest energy states as a function of applied magnetic flux in units of  0 . **(a-b)**
Symmetric transmon qubit, with Josephson energy _E_ _J_ are shunted with a capacitor yielding a charging energy _E_ _C_ . **(c-d)**
Asymmetric transmon qubit, with junction asymmetry __ = _E_ _J_ 2 _/E_ _J_ 1 = 2 _._ 5. **(e-f)** Capacitively shunted flux qubit, where a
small principle junction (red) is shunted with two larger junctions (orange). Parameters are the same as Yan et al. 62 . **(g-h)**
C-shunted fluxonium qubit, where the small junction is inductively shunted with a large array of _N_ junctions.


- /2 0 /2 - - /2 0 /2 - - /2 0 /2 - - /2 0 /2


One recent development has focused on reducing the
qubit sensitivity to flux noise, while maintaining sufficient tunability to operate our quantum gates. The
idea is to make the two junctions in the split transmon
asymmetric 69 , see Fig. 2(c). This yields the following
Hamiltonian


70
resonance gate is optimized with certain frequency detuning between two qubits . Therefore, by using an
asymmetric transmon, a small frequency-tuning range
is introduced that is sufficient to compensate for fabrication variations, without introducing unnecessary large
susceptibility to flux noise and thus maintaining high coherence. For another example, a surface code scheme
based on the adiabatic -gate requires specific frequency configuration among qubits in order to avoid frequency crowding issues, and asymmetric transmons fit CPHASE
well with its well-defined frequency range 71 . In general,
as the quantum processors scale up and fabrication improves, asymmetric transmons are likely to be found in
wider applications in the future.

**_2._** **_Towards larger anharmonicity: flux qubit and fluxonium_**

We see that split transmon qubits, be it symmetric or
not, still share the same topology as the single junction
version, yielding a sinusoidal potential. Therefore, the
degree to which the properties of these qubits can be engineered has not fundamentally changed. In particular,
the limited anharmonicity in transmon-type qubits intrinsically causes significant residual excitation to higherenergy states, undermining performance of gate operations. To go beyond this, it is necessary to introduce
additional complexity into the circuit.
One outstanding development in this regard is the in-



2 2 2
cos ( __ _e_ ) + _d_ sin ( __ _e_

_E_ _J_ __ ( __ _e_ )
 = (



2
_H_ = 4 _E_ _C_ _n_ __ _E_ _J_ 


cos( __ ) _,_ (22)


where _E_ _J_  = _E_ _J_ 1 + _E_ _J_ 2 and _d_ = ( __ 1) _/_ ( __ + 1) is
__
the junction asymmetry parameter, with __ = _E_ _J_ 2 _/E_ _J_ 1 .
Again, we can treat the two junctions as a single-junction
transmon, with an effective Josephson energy particular, we can recognize the two special cases; for _E_ _J_ __ ( __ _e_ ). In
_d_
= 0, the Hamiltonian in Eq. (22) reduces to the symmetric case with _E_ _J_ __ ( __ _e_ ) = _E_ _J_  cos( __ _e_ ) , as in Eq. (21)
with _E_ _J_  = 2 _E_ _J_ . In the other limit, when _|_ _|_ _d_ 1,
_|_ _| _
_E_ _J_ __ ( __ _e_ ) _E_ _J_  and the flux-tunability of the Josephson

__
energy vanishes, which is equivalent to the single junction
case, recall Eq. (16).
From the discussion above we see that going from symmetric to asymmetric transmons does not change the circuit topology. This seemingly trivial modification, however, has profound impact for practical applications. As
we can see from the qubit spectra, Fig. 2(d), the flux
sensitivity is suppressed across the entire tunable frequency range. For example, the performance of the cross-


_E_ _c_ _/h_ = 0.3 GHz
_E_ _J_ _/h_ = 15 GHz


-----


, where the qubit loop is interrupted by three (or four) junctions, see Fig. 2(e). On vention of the flux qubit 72,73
one branch is one smaller junction; on the other branch
are two identical junctions, both a factor __ larger in size
compared to the small junction. The addition of one
more junction as compared to the split transmon is nontrivial, as it changes the circuit topology and reshapes
the potential energy profile.
Each junction is associated with a phase variable, and
the fluxoid quantization condition again allows us to
eliminate one degree of freedom. Consequently, we have
a two-dimensional potential landscape, which in comparison to the simpler topology of the transmon, complicates the problem both conceptually and computationally. Fortunately, under the assumed setting that the array junctions are larger in size ( _ >_ 1), it is usually a good
approximation to treat the problem as a particle moving
in a quasi-1D potential, which also helps us gain more
insight and intuition about the system and draw qualitative conclusions. The Hamiltonian under this _quasi-1D_
_approximation_ reads,

2
_H_ 4 _E_ _C_ _n_ _E_ _J_ cos(2 __ + __ _e_ ) 2 _E_ _J_ cos( __ ) _._ (23)
__ __ __

Note that the phase variable in Eq. (23) is the sum
of the branch phases across the two array junctions, __ =
( __ 1 + __ 2 ) _/_ 2, assuming the same current direction across
__ 1 and __ 2 . The external magnetic flux is denoted __ _e_ =
2 __  _ext_ _/_  0 . The second term in Eq. (23) is contributed
by the small junction with Josephson energy _E_ _J_ , whereas
the third term takes into account the two array junctions,
together with Josephson energy 2 _E_ _J_ . Clearly, the sum
of these two terms no longer has the characteristics of a
simple cosinusoid, and the final potential profile as well
as the corresponding eigenstates depends on both the
external flux __ _e_ and the junction area ratio __ .
The most common working point for this system is
when __ _e_ = __ + 2 _k_ , where _k_ is an integer  that is
when half a superconducting flux quantum threads the
qubit loop. At this flux bias point, the qubit spectrum
reaches its minimum, and the qubit frequency is firstorder insensitive to flux noise, see Fig. 2(f). This point
is often referred to as _the flux degeneracy point_ , where
flux qubits tend to have the optimal coherence time.
At this operation point, the potential energy may assume a single-well ( __ 2) or a double-well ( _ <_ 2)
__
profile. The single-well case shares some simularities
with the transmon qubit, where the quadratic and quartic terms of the Hamiltonian determines the harmonicity and anharmonicity, respectively.
62,74
The capacitivelyshunted flux qubit (CSFQ) was explored in this
regime, demonstrating long coherence and decently high
anharmonicity. Note that as opposed to the transmon
qubit, the anharmonicity of the CSFQ is _positive_ ( _ >_ 0).
While the improvement in anharmonicity can be associated with reshaping the energy potential, the improved
coherence over the first flux qubits can be attributed to


the introduction of the capacitive shunt, similar to the
modified Cooper-pair box leading to the transmon qubit.
The double-well case obtained for _ <_
72,73
2 was demonstrated and investigated much earlier . The intuitive
picture based on circulating current states  so it gets
the name persisting-current flux qubit (PCFQ)  gives
a satisfying physical description of the qubit degrees of
freedom. However, from the perspective of a quantum
engineer, the qubit properties are of more interest, even
if sometimes we may lose physical intuition about the
system in certain regimes; such as when __ 2 and there
__
are no clear circulating current states. The most important feature of the PCFQ is that its anharmonicity can
be much greater than the transmon and CSFQ and the
transition matrix elements 1 _n_  0 _,_ 1 __  0
_|_ _|_ _|_ _|_ _|_ _|_ _|_ _|_
become considerably smaller given equivalent _E_ _J_ _/E_ _C_ . Therefore, a
longer relaxation time can be expected. These features
have been demonstrated even more prominently in its
close relative, the fluxonium qubit 75 .
The flux qubit is a striking example that illustrates
how one dramatically can engineer the qubit properties
through the choice of various circuit parameters. The introduction of array junctions and consequent biharmonic
profile generates rich dynamics as well as broad applications. An extention of this idea is the fluxonium qubit,
which generated substantial interest recently, due partly
to its capability of engineering the transition matrix elements to achieve millisecond _T_ 1 time, and due partly
to the invention of novel gate schemes applicable to such
well-protected qubits 76,77 .
Compared to flux qubits, which usually contain two
or three array junctions 78 , the number of array junctions
in the fluxonium qubit is dramatically increased 75,79 , in
some cases, to the order of 100, see Fig. 2(g). Following
the same quasi-1D approximation as for the flux qubit,
the last term in Eq. (23) becomes _NE_ _J_ cos( _/N_ ),
__
where _N_ denotes the number of array junctions. For
large _N_ , the argument in the cosine term _/N_ becomes
sufficiently small that a second order expansion is a good
approximation. This results in the fluxonium Hamiltonian,



2 1 2
_H_ 4 _E_ _C_ _n_ _E_ _J_ cos( __ + __ _e_ ) + _E_ _L_ __ _,_ (24)
__ __ 2

where _E_ _L_ = ( _/N_ ) _E_ _J_ is the inductive energy of the
effective inductance contributed by the junction array  often known as superinductance due to its large
value 7981 . Therefore, we can treat the potential energy

82
as a quadratic term modulated by a sinusoidal term, similar to that of an rf-SQUID type flux qubit . However,
the kinetic inductance of the Josephson junction array is
in general much larger than the geometric inductance of
the wire in an rf-SQUID.
Depending on the relative magnitude of _E_ _J_ and _E_ _L_ ,
the fluxonium system could involve plasmon states (in
the same well) and fluxon states (in different wells).
There are a variety of schemes to utilize them for quantum information processing. Generally, the spectrum of


-----


(a) Direct capacitive coupling


the transition between the lowest energy states is similar
to that of the flux qubit, see Fig. 2(h). Both long coherence and high anharmonicity can be expected at the flux
sweet spot.
Lastly, we want to point out a further extension  the
0 __
__ 83,84
qubit  which has even stronger topological protection from noise . However, the strongly suppressed
sensitivity to external fluctuations also makes it hard to
manipulate.

**C.** **Interaction Hamiltonian engineering**

To generate entanglement between individual quantum
systems  it is necessary to engineer an interaction Hamiltonian that connects degrees of freedom in those individual systems. In this section, we discuss the physical
coupling mechanism and its representation in the qubit
eigenbasis. The use of coupling to form 2-qubit gates is
discussed in Sec. IV.

**_1._** **_Physical coupling: capacitive and inductive_**

The Hamiltonian of two coupled systems takes a
generic form

_H_ = _H_ 1 + _H_ 2 + _H_ int _,_ (25)

denote the Hamiltonians of the individual quantum systems, which could be any combination of where _H_ 1 and _H_ 2
the qubit circuits mentioned in Sec. II A and II B. The
last term, _H_ int , is the interaction Hamiltonian, which
couples variables of both systems. In superconducting
circuits, the physical form of the coupling energy is either
an electric or magnetic field (or a combination thereof).
To achieve capacitive coupling, a capacitor is placed
between the voltage nodes of the two participating circuits, yielding an interaction Hamiltonian _H_ int of the
form

_H_ int = _C_ _g_ _V_ 1 _V_ 2 _,_ (26)

where _C_ _g_ is the coupling capacitance and _V_ 1 ( _V_ 2 ) is the
voltage operator of the corresponding voltage node being
connected. Fig. 3(a) illustrates a realistic example of a
direct capacitive coupling between the top nodes of two
transmon qubits. Circuit quantization in the limit of
_C_ _g_ _C_ 1 _, C_ 2 yields
__


_g_ _12_


|V 1 C C 1|V 2 g I C C2 2|
|---|---|


(b) Capacitive coupling via coupler

_g_ _r1_ _g_ _r2_

|C C 1|C g1 L r C r|g2 I C C2 2|
|---|---|---|



(c) Direct inductive coupling


_I_ _1_ _M_ _12_ _I_ _2_


![qe-guide-scqubits-oliver.pdf-8-0.png](qe-guide-scqubits-oliver.pdf-8-0.png)

(d) Inductive coupling via coupler


_I_ _CC_


_M_ _1C_


_M_ _2C_



_I_ _C1_ _L_ _1_ _L_


![qe-guide-scqubits-oliver.pdf-8-1.png](qe-guide-scqubits-oliver.pdf-8-1.png)

![qe-guide-scqubits-oliver.pdf-8-2.png](qe-guide-scqubits-oliver.pdf-8-2.png)

![qe-guide-scqubits-oliver.pdf-8-3.png](qe-guide-scqubits-oliver.pdf-8-3.png)

FIG. 3. Schematic of capacitive and inductive coupling
schemes between two superconducting qubits, labeled 1 and
2. **(a)** Direct capacitive coupling, where the voltage nodes
of two qubits _V_ 1 and _V_ 2 are connected by a capacitance _C_ _g_ .
**(b)** Capacitive coupling via a coupler in form of a linear resonator. **(c)** Direct inductive coupling, where the two qubits
are coupled via mutual inductance, _M_ 12 . **(d)**
Inductive coupling via mutual inductances to a frequencytunable coupler. _M_ 1 _C_ and _M_ 2 _C_

where the expressions in brackets are the two Hamiltonians of the individual qubits, [see Eq. (16)], and we take
_V_ _i_ = (2 _e/C_ _i_ ) _n_ _i_ in Eq. (26). From Eq. (27), we see that
the coupling energy depends on the coupling capacitance
as well as the matrix elements of the voltage operators.
The dependencies are bilinear in the perturbative limit
( _C_ _g_ __ _C_ 1 _, C_ 2 ).
To implement the coupling capacitance, one only need
bring the edges of the capacitor pads into close proximity, as has been demonstrated in state-of-the-art planar
designs 85 . The coupling capacitance is determined by
the planar capacitor geometry as well as the surrounding environment, such as the dielectric constant of the
substrate and the ground plane proximity.


_H_ =


_i_ =1 _,_ 2



2
4 _E_ _C,i_ _n_ _i_ _E_ _J,i_ cos( __ _i_ )

__



2 _C_ _g_
+4 _e_ _n_ 1 _n_ 2 _,_ (27)

_C_ 1 _C_ 2



2 _C_ _g_
+4 _e_


-----


10

this simplifying approximation is only exact in the pathological limit of no coupling.
To realize a mutual inductance, two looped circuits
are brought into close proximity to one another, or, to
make it stronger, overlap with each other 88 , and even

8992
may share the same wire or Josephson junction inductor . In the case of a Josephson junction, and for
certain metals, the inductance is dominated by _kinetic_
_inductance_ contributions, rather than solely geometric
inductance . Kinetic inductance arises from the mechanical, inertial mass of the charge carriers, but is only 93,94
practically witnessed in very high-conductance materials like superconductors. A primary feature of kinetic
inductance is that its values can vastly exceed those of
conventional geometric inductances, which are generally
limited by electromagnetic considerations 79 .

**_2._** **_Coupling axis: transverse and longitudinal_**

Regardless of its physical realization, the effect of a
coupling on system dynamics is determined by its form
as represented in the eigenbasis of the individual systems.
That is, how _H_ int appears in the representation spanned
by the eigenbasis of _H_ 1 __ _H_ 2 .
Let us start with the previous example of two capacitively coupled transmon qubits [Fig. 3(a)]. Using second
quantization, the system Hamiltonian in Eq. (27) can be
expressed as


In the case of inductive coupling, a mutual inductance
shared by two loops is the coupling mechanism, yielding
an interaction Hamiltonian that is of the intuitive form

_H_ int = _M_ 12 _I_ 1 _I_ 2 _,_ (28)

where _M_ 12 denotes the mutual inductance between the
loops and _I_ 1 and _I_ 2 are the current operators for the
currents through the inductors. A typical example comprises two closely positioned (rf-SQUID type) flux qubits,
as illustrated in Fig. 3(c). The system Hamiltonian can
be expressed as (see Refs. 86 and 87):



2
4 _E_ _C,i_ _n_ _i_ _E_ _J,i_ cos( __ _i_ ) + 1

__ 2


_H_ =


 2 _Li_


_i_ =1 _,_ 2



2
_L_ _i_ (1 _K_ )
__



2  _L_ 1
_M_ 12 (1 _K_ )
__ __ _L_ 1 (1


 _L_ 1  _L_ 2

2
_L_ 1 (1 __ _K_ ) _L_ 2 (1 __


_L_ 2

_,_ (29)

2
_L_ 2 (1 __ _K_ )


where the first two terms are the energies associated with
the Josephson junctions, the third term captures the inductor energies, and the fourth term is the mutual coupling energy of the form _MI_ 1 _I_ 2 (note that in general
 = are the magnetic fluxes associated with the currents flowing through the respective _LI_ ).  _L_ 1 and  _L_ 2
inductors, and _K_ is the unitless mutual coupling factor
defined by _M_ 12 = _K_ __ _L_ 1 _L_ 2 . Importantly, note that in

2
Eq. (29), _K_ renormalizes _L_ 1 , _L_ 2 and _M_ 12 , essentially
capturing the loading effect on the circuit due to their
presence, and is found by inverting an inductance matrix
(see Refs. 86 and 87).
As we did with the charge degree of freedom, we will
normalize the inductor and externally applied magnetic
fluxes  in this case, by the reduced quantum unit of
flux  0 _/_ 2 __  to define phases __ __  _/_ ( 0 _/_ 2 __ ) that are
on the same footing as the junction phases __ 1 _,_ 2 . Due
to fluxoid quantization around the closed loop, these
phases must sum to zero or an integer multiple of 2 __ .
For current directions entering the top of the junctions

[with _I_ 1 counterclockwise and _I_ 2 as shown in Fig. 3(c)],
__ _i_ __ _Li_ = __ _ei_ +2 _n_ with _n_ = 0 _,_ 1 _, . . ._ (see, for example,
__ __
Ref. 72). Replacing __ _L_ 1( _L_ 2) with __ 1(2) __ 1( _e_ 2) yields:
__


_H_ =


_i_ __ 1 _,_ 2


__ _i_ _a_ __ _i_ _a_ _i_ + __ 2 _i_ _a_ __ _i_ _a_ __ _i_ _a_ _i_ _a_ _i_


__ _g_ _a_ 1 __ _a_ __ 1 _a_ 2 __ _a_ __ 2 _,_ (31)
  


_i_ =1 _,_ 2



2
4 _E_ _C,i_ _n_ _i_ _E_ _J,i_ cos( __ _i_ ) + 1

__ 2


 0

2 __




 0 2 2

2 __ ( __ _i_ __ _ei_ )
__ 2

_L_ _i_ (1 _K_ )

 __



2
_L_ _i_ (1 _K_ )
__


where the expression within brackets represent the Duffing oscillator Hamiltonian for the qubits and _g_ is the
coupling energy. Since we define _V_ __ _n_ __ _i_ ( _a_ __ _a_ __ ), and
consequently _I_ __ __ __ ( _a_ + _a_ __ ), the original _n_ 1 _n_ 2 -term
becomes what is shown in Eq. (31). Such a coupling is
called _transverse_ , because the coupling Hamiltonian has
non-zero matrix elements only at off-diagonal positions
with respect to both oscillators, i.e. _i_ _k_ _a_ _i_ _a_ __ _i_ _k_ _i_ = 0

__ _|_ __ _|_ __
for any integer _k_ and for _i_ 1 _,_ 2 and in this case
__


_i_ _k_ 1 _a_ _i_ _a_ __ _i_ _k_ _i_ = 0.

__ If we can ignore higher energy levels ( __ _|_ __ _|_ __ __ _k_ 2) either
__
because of sufficient anharmonicity or through careful
control protocols that ensure these levels never have influence, we may truncate the Hamiltonian in Eq. (31)
to



2
__ _M_ 12 (1 __ _K_ )


 0

2 __

_L_




 2 __ 0 ( __ 1 __ _e_ 1

__



2
_L_ 1 (1 __ _K_ )


 0

2 __

_L_




 2 __ 0 ( __ 2 __ _e_ 2 )

__


__ __ 2 _e_ _._ (30)

_L_ 2 (1 __ _K_ )


The coupling is of the form _M_ 1 _,_ 2 _I_ 1 _I_ 2
, with both the mutual coupling and the circulating currents (via the _L_ 1

2
and _L_ 2 ) renormalized by the factor (1 __ _K_ ). To
capture the renormalization explicitly, the Hamiltonian
is generally simulated using phase operators (Eq. 30),
rather than current operators. In the weak-coupling limit

2 2
_K_ __ 1 (equivalently, _M_ __ _L_ 1 _L_ 2 ), the coupling term
may be approximated by the Josephson currents with
_M_ 12 _I_ 1 _I_ 2 _M_ 12 _I_ _c_ 1 sin __ 1 _I_ _c_ 2 sin __ 2 . Note, however, that
__


_H_ =



__ _i_ __ _z,i_ + _g_ _y,_ 1 __ _y,_ 2 _._ (32)
2


_i_ __ 1 _,_ 2


This is a Hamiltonian of two spins, coupled by an exchange interaction. As we will see in Sec. IV D 1, such


-----


11

and approximation  be treated as an isolated system,
and the composite system simplified to two transversely
coupled qubits, see Eq. (32).
We now turn to the previous example of two inductively coupled flux qubits, see Fig. 3(c). Assume that
the double-well potential [Fig. 2(g)] has a relatively
high inter-well barrier, which leads to an exponentially
small qubit transition frequency at the energy degeneracy point, ( _e_ = __ ). Around this degeneracy point, the
off-diagonal matrix element of sin( __ ) is zero, i.e. the
ground and excited states are localized in different wells
and 1 sin( __ ) 1 0 sin( __ ) 0 = 0. We can then rewrite
__ _|_ _|_ __ _|_ _|_ __
the Hamiltonian in Eq. ( **??** ) as


a Hamiltonian is most commonly used in contemporary
implementations and can generate various types of twoqubit entangling gates. Note that, more often, we see
that the interaction term is expressed in __ _x_ __ _x_ instead of
__ _y_ __ _y_ . The choice in the context here is arbitrary and does
not change the dynamics. However, when both capacitive and inductive couplings are present in the system,
both __ _x_ __ _x_ and __ _y_ __ _y_ may be needed. In this case, the
voltage operator _V_ _i_ ( _a_ _a_ __ ) (reduced to __ _y_
__ __
after twolevel approximation in the lab frame) is transversal to the
current operator _I_ ( _a_ + _a_ __ ) (reduced to __ _x_ ) and both of
__
them may be transverse to the qubit. A similar example
is demonstrated between a qubit and a resonator by Lu
et al. 95

Transverse coupling can be engineered between a qubit
and a harmonic oscillator, see Fig. 3(b). In this case, the
Hamiltonian becomes


a Hamiltonian is most commonly used in contemporary
implementations and can generate various types of twoqubit entangling gates. Note that, more often, we see
that the interaction term is expressed in __ _x_ __ _x_ instead of
__ _y_ __ _y_ . The choice in the context here is arbitrary and does
not change the dynamics. However, when both capacitive and inductive couplings are present in the system,
both __ _x_ __ _x_ and __ _y_ __ _y_ may be needed. In this case, the
voltage operator _V_ _i_ ( _a_ _a_ __ ) (reduced to __ _y_
__ __
after twolevel approximation in the lab frame) is transversal to the
current operator _I_ ( _a_ + _a_ __ ) (reduced to __ _x_ ) and both of
__
them may be transverse to the qubit. A similar example
is demonstrated between a qubit and a resonator by Lu
et al. 95


_H_ =



__ _i_ __ _zi_ + _g_ _z_ 1 __ _z_ 2 _._ (35)
2


_i_ =1 _,_ 2


Now, the coupling axis is the same as the qubit quantization axes and therefore termed _longitudinal coupling_ .
Note, however, that the physical __ _x_ __ _x_ and __ _z_ __ _z_ couplings
can change in the qubit frame.
Longitudinal coupling is an important type of interaction, because it can generate entanglement without
energy exchange. Moreover, it is found a necessary ingredient in the application of quantum annealing, where
certain hard combinatorial optimization problems can be
modeled by the Ising Hamiltonian in Eq. (35) and finding
its ground state would solve this problem.
An intermediate qubit mode may also be used as a coupler in the longitudinal case. In Fig. 3(d), an additional
rf-SQUID is used to mediate the coupling. The coupling
strength can be tuned by the flux bias of the coupler
SQUID 103
63
. Note that a tunable coupler may also be realized in a structure with capacitive couplings
. A tunable coupler is useful because it provides a wide range of
coupling strengths 87 , a high on-off ratio 104 for reducing
gate error-rates, and more ways of achieving high-fidelity
entangling gates 67,105107 . The trade-off is an additional
control line.
In addition to the pure transversal and longitudinal
qubit-qubit interactions, there are also examples of mixed
types of interaction Hamiltonians 108



1
_H_ = __ q __ _z_ + __ _r_ _a_ __ _a_ + _g_ ( __ + _a_ + __ _a_ __ ) _,_ (33)

2 __



1
_H_ =


where __ q and __ _r_
denote the qubit and resonator frequencies, and __ + = 0 1 and __ = 1 0 describes
_|_ __ _|_ __ _|_ __ _|_
the processes of exciting and de-exciting the qubit, respectively. Here, we have assumed that the coupling is
in the dispersive limit, i.e. _g_ __ __ q _, _ _r_ , hence ignoring
the double (de)excitation terms proportional to __ + _a_ __ and
__ _a_
__
, which under typical operation regimes oscillate sufficiently fast to average to zero. The Hamiltonian in Eq.
(33), is the standard model used for describing how a twolevel atom interacts with a resonant cavity that houses
it. Such a structure is also known as cavity quantum
electrodynamics (cQED), and it is extended to the circuit version here. It has many useful applications in superconducting quantum information architectures, such
as high-fidelity readout 96 , see Sec. V, cavity buses 97 ,
quantum memory 98,99 , quantum computation with cat
states 100102 , etc.
Here, we briefly mention the use of a cavity or resonator to mediate coupling between two qubits, which
may be physically well-separated ( 1 cm). Since most
__
superconducting resonators are in the GHz frequency
range, they can be made much longer than any dimension of a qubit circuit ( 1 mm). One can use such a
__
resonator to mediate coupling between two or more otherwise non-interacting qubits. An example is shown in
Fig. 3(b), where two transmon qubits are both capacitively coupled to the center resonator. The two-level
system Hamiltonian is:



1
_H_ = __ q __ _z_ + __ _r_ _a_ __ _a_ + _g_ _z_ ( _a_ + _a_ __ ) _,_ (36)

2

which are longitudinal with respect to a qubit, but transverse with respect to a harmonic oscillator in a qubitresonator system. Such a model is called longitudinal
but one should note that it is only longitudinal to one
participating system. It is hard to engineer physically
longitudinal coupling with respect to a harmonic oscillator, since either the _E_ -field ( _V_ ) or the _B_ -field ( _I_ ) is
transverse with respect to the eigen field of the harmonic
oscillator. Note, however, that a transversal model such
as in Eq. (33) may be transformed into a longitudinal
one in certain operating regimes, see Sec. V.


_H_ =


_i_ =1 _,_ 2


__ _i_ _a_ __ _i_ _a_ _i_ + __ 2 _i_ _a_ __ _i_ _a_ __ _i_ _a_ _i_ _a_ _i_ + __ _r_ _a_ __ _r_ _a_ _r_


+ _g_ 1 _r_ _a_ __ 1 _a_ _r_ + _a_ 1 _a_ __ _r_ + _g_ 2 _r_ _a_ __ 2 _a_ _r_ + _a_ 2 _a_ __ _r_ _._ (34)
   

It can be shown that in the dispersive limit, i.e. _g_ _ir_
__ _i_ __ _r_ , the resonator can  after proper transformation __
_|_ __ _|_


-----


In some applications, such as for quantum annealing,
both longitudinal and transverse couplings are desired
coupling for enhancing the annealing performance) and require independent control. ( __ _z_ __ _z_ coupling for mapping the problem and __ _x_ __ _x_

**III.** **NOISE, DECOHERENCE, AND ERROR**
**MITIGATION**

Random, uncontrollable physical processes in the qubit
control and measurement equipment or in the local environment surrounding the quantum processor are sources
of noise that lead to decoherence and reduce the operational fidelity of the qubits. In this section, we introduce
the basics of noise leading to decoherence in superconducting circuits, and we discuss coherent control methods
to mitigate certain types of noise.

**A.** **Types of noise**

In a closed system, the dynamical evolution of a qubit
state is deterministic. That is, if we know the starting
state of the qubit and its Hamiltonian, then we can predict the state of the qubit at any time in the future.
However, in open systems, the situation changes. The
qubit now interacts with uncontrolled degrees of freedom
in its environment, which we refer to as fluctuations or
noise. In the presence of noise, as time progresses, the
qubit state looks less and less like the state we would
have predicted and, eventually, the state is lost. There
are many different sources of noise that affect quantum
systems, and they can be categorized into two primary
types: systematic noise and stochastic noise.

**_1._** **_Systematic noise_**

Systematic noise arises from a process that is traceable to a fixed control or readout error. For example, we
apply a microwave pulse to the qubit that we believe
will impart a 180-degree rotation. However, the control field is not tuned properly and, rather than rotating
the qubit 180 degrees, the pulse slightly over-rotates or
under-rotates the qubit by a fixed amount. The underlying error is _systematic_ , and it therefore leads to the same
rotation error each time it is applied. However, when
such erroneous pulses are used in practice in a variety
of control sequences, the observed results may appear
to be influenced by random noise. This is because the
pulse is generally not applied in the same way for each
experiment: it could be applied a different number of
times, interspersed with different pulses in different orders, and therefore generally differs from experiment to
experiment. However, once systematic errors are identified, they can generally be corrected through proper
calibration or the use of improved hardware.


12

**_2._** **_Stochastic noise_**

The second type of noise is stochastic noise, arising
from random fluctuations of parameters that are coupled
to our qubit . For example, thermal noise of a 50resistor in the control lines leading to the qubit will have 109
voltage and current fluctuations  Johnson noise  with a
noise power that is proportional to both temperature and
bandwidth. Or, the oscillator that provides the carrier
for a qubit control pulse may have amplitude or phase
fluctuations. Additionally, randomly fluctuating electric
and magnetic fields in the local qubit environment  e.g.,
on the metal surface, on the substrate surface, at the
metal-substrate interface, or inside the substrate  can
couple to the qubit. This creates unknown and uncontrolled fluctuations of one or more qubit parameters, and
this leads to qubit decoherence.

**_3._** **_Noise strength and qubit susceptibility_**

The degree to which a qubit is affected by noise is
related to the amount of noise impinging on the qubit,
and the qubits susceptibility to that noise. The former
is often a question of materials science and fabrication;
that is, can we make devices with lower levels of noise.
Or, it may be related to the quality of the control electronics and cryogenic engineering to limit the levels of
noise on the control lines that necessarily connect to the
qubits to control them. The latter  qubit susceptibility
 is a question of qubit design. Qubits can be designed to
trade off sensitivity to one type of noise at the expense of
increased sensitivity to other types of noise. Thus, materials science, fabrication engineering, electronics design,
cryogenic engineering, and qubit design all play a role
in creating devices with high coherence. In general, one
should strive to eliminate the sources of noise, and then
design qubits that are insensitive to the residual noise.
The qubit response to noise depends on how the noise
couples to it  either through a longitudinal or a transverse coupling as referenced to the qubit quantization
axis. This can be visualized using a Bloch Sphere picture
of the qubit state, as illustrated in Fig. 4 and discussed
in detail in Section III B.

**B.** **Modeling noise and decoherence**

**_1._** **_Bloch sphere representation_**

The _Bloch sphere_ is a unit sphere used to represent the
quantum state of a two-level system (qubit). Fig. 4(a)
shows a Bloch sphere with a _Bloch vector_ representing
the state __ = __ 0 + __ 1 . If we visualize the Bloch
_|_ __ _|_ __ _|_ __
sphere as the planet Earth, then by convention, the north
pole represents state 0 and the south pole state 1 . For
_|_ __ _|_ __
pure quantum states such as __ , the Bloch vector is of
_|_ __


-----


13


(a) Bloch sphere (b) Longitudinal relaxation (c) Pure dephasing (d) Transverse relaxation


(Longitudinal)


Longitudinal

noise


|  =  |0  +  |1  |0  Pure |0  |0 


Excitation



Pure
Dephasing


Decoherence


![qe-guide-scqubits-oliver.pdf-12-7.png](qe-guide-scqubits-oliver.pdf-12-7.png)

![qe-guide-scqubits-oliver.pdf-12-35.png](qe-guide-scqubits-oliver.pdf-12-35.png)

![qe-guide-scqubits-oliver.pdf-12-94.png](qe-guide-scqubits-oliver.pdf-12-94.png)

![qe-guide-scqubits-oliver.pdf-12-21.png](qe-guide-scqubits-oliver.pdf-12-21.png)

![qe-guide-scqubits-oliver.pdf-12-1.png](qe-guide-scqubits-oliver.pdf-12-1.png)

![qe-guide-scqubits-oliver.pdf-12-45.png](qe-guide-scqubits-oliver.pdf-12-45.png)

![qe-guide-scqubits-oliver.pdf-12-44.png](qe-guide-scqubits-oliver.pdf-12-44.png)

![qe-guide-scqubits-oliver.pdf-12-4.png](qe-guide-scqubits-oliver.pdf-12-4.png)

![qe-guide-scqubits-oliver.pdf-12-31.png](qe-guide-scqubits-oliver.pdf-12-31.png)

![qe-guide-scqubits-oliver.pdf-12-90.png](qe-guide-scqubits-oliver.pdf-12-90.png)

![qe-guide-scqubits-oliver.pdf-12-17.png](qe-guide-scqubits-oliver.pdf-12-17.png)

![qe-guide-scqubits-oliver.pdf-12-109.png](qe-guide-scqubits-oliver.pdf-12-109.png)

![qe-guide-scqubits-oliver.pdf-12-115.png](qe-guide-scqubits-oliver.pdf-12-115.png)

![qe-guide-scqubits-oliver.pdf-12-133.png](qe-guide-scqubits-oliver.pdf-12-133.png)

![qe-guide-scqubits-oliver.pdf-12-134.png](qe-guide-scqubits-oliver.pdf-12-134.png)

![qe-guide-scqubits-oliver.pdf-12-135.png](qe-guide-scqubits-oliver.pdf-12-135.png)

![qe-guide-scqubits-oliver.pdf-12-74.png](qe-guide-scqubits-oliver.pdf-12-74.png)

![qe-guide-scqubits-oliver.pdf-12-3.png](qe-guide-scqubits-oliver.pdf-12-3.png)

![qe-guide-scqubits-oliver.pdf-12-14.png](qe-guide-scqubits-oliver.pdf-12-14.png)

![qe-guide-scqubits-oliver.pdf-12-5.png](qe-guide-scqubits-oliver.pdf-12-5.png)

![qe-guide-scqubits-oliver.pdf-12-89.png](qe-guide-scqubits-oliver.pdf-12-89.png)

![qe-guide-scqubits-oliver.pdf-12-101.png](qe-guide-scqubits-oliver.pdf-12-101.png)

![qe-guide-scqubits-oliver.pdf-12-108.png](qe-guide-scqubits-oliver.pdf-12-108.png)

![qe-guide-scqubits-oliver.pdf-12-118.png](qe-guide-scqubits-oliver.pdf-12-118.png)

![qe-guide-scqubits-oliver.pdf-12-119.png](qe-guide-scqubits-oliver.pdf-12-119.png)

![qe-guide-scqubits-oliver.pdf-12-137.png](qe-guide-scqubits-oliver.pdf-12-137.png)

![qe-guide-scqubits-oliver.pdf-12-91.png](qe-guide-scqubits-oliver.pdf-12-91.png)

![qe-guide-scqubits-oliver.pdf-12-16.png](qe-guide-scqubits-oliver.pdf-12-16.png)

![qe-guide-scqubits-oliver.pdf-12-28.png](qe-guide-scqubits-oliver.pdf-12-28.png)

![qe-guide-scqubits-oliver.pdf-12-48.png](qe-guide-scqubits-oliver.pdf-12-48.png)

![qe-guide-scqubits-oliver.pdf-12-49.png](qe-guide-scqubits-oliver.pdf-12-49.png)

![qe-guide-scqubits-oliver.pdf-12-61.png](qe-guide-scqubits-oliver.pdf-12-61.png)

![qe-guide-scqubits-oliver.pdf-12-62.png](qe-guide-scqubits-oliver.pdf-12-62.png)

![qe-guide-scqubits-oliver.pdf-12-63.png](qe-guide-scqubits-oliver.pdf-12-63.png)

![qe-guide-scqubits-oliver.pdf-12-18.png](qe-guide-scqubits-oliver.pdf-12-18.png)

![qe-guide-scqubits-oliver.pdf-12-30.png](qe-guide-scqubits-oliver.pdf-12-30.png)

![qe-guide-scqubits-oliver.pdf-12-32.png](qe-guide-scqubits-oliver.pdf-12-32.png)

![qe-guide-scqubits-oliver.pdf-12-75.png](qe-guide-scqubits-oliver.pdf-12-75.png)

![qe-guide-scqubits-oliver.pdf-12-107.png](qe-guide-scqubits-oliver.pdf-12-107.png)

![qe-guide-scqubits-oliver.pdf-12-116.png](qe-guide-scqubits-oliver.pdf-12-116.png)

![qe-guide-scqubits-oliver.pdf-12-117.png](qe-guide-scqubits-oliver.pdf-12-117.png)

![qe-guide-scqubits-oliver.pdf-12-125.png](qe-guide-scqubits-oliver.pdf-12-125.png)

![qe-guide-scqubits-oliver.pdf-12-126.png](qe-guide-scqubits-oliver.pdf-12-126.png)

![qe-guide-scqubits-oliver.pdf-12-127.png](qe-guide-scqubits-oliver.pdf-12-127.png)

![qe-guide-scqubits-oliver.pdf-12-128.png](qe-guide-scqubits-oliver.pdf-12-128.png)

![qe-guide-scqubits-oliver.pdf-12-136.png](qe-guide-scqubits-oliver.pdf-12-136.png)

![qe-guide-scqubits-oliver.pdf-12-129.png](qe-guide-scqubits-oliver.pdf-12-129.png)

![qe-guide-scqubits-oliver.pdf-12-130.png](qe-guide-scqubits-oliver.pdf-12-130.png)

![qe-guide-scqubits-oliver.pdf-12-132.png](qe-guide-scqubits-oliver.pdf-12-132.png)

![qe-guide-scqubits-oliver.pdf-12-131.png](qe-guide-scqubits-oliver.pdf-12-131.png)

![qe-guide-scqubits-oliver.pdf-12-69.png](qe-guide-scqubits-oliver.pdf-12-69.png)

![qe-guide-scqubits-oliver.pdf-12-70.png](qe-guide-scqubits-oliver.pdf-12-70.png)

![qe-guide-scqubits-oliver.pdf-12-71.png](qe-guide-scqubits-oliver.pdf-12-71.png)

![qe-guide-scqubits-oliver.pdf-12-80.png](qe-guide-scqubits-oliver.pdf-12-80.png)

![qe-guide-scqubits-oliver.pdf-12-53.png](qe-guide-scqubits-oliver.pdf-12-53.png)

![qe-guide-scqubits-oliver.pdf-12-54.png](qe-guide-scqubits-oliver.pdf-12-54.png)

![qe-guide-scqubits-oliver.pdf-12-60.png](qe-guide-scqubits-oliver.pdf-12-60.png)

![qe-guide-scqubits-oliver.pdf-12-72.png](qe-guide-scqubits-oliver.pdf-12-72.png)

![qe-guide-scqubits-oliver.pdf-12-73.png](qe-guide-scqubits-oliver.pdf-12-73.png)

![qe-guide-scqubits-oliver.pdf-12-76.png](qe-guide-scqubits-oliver.pdf-12-76.png)

![qe-guide-scqubits-oliver.pdf-12-77.png](qe-guide-scqubits-oliver.pdf-12-77.png)

![qe-guide-scqubits-oliver.pdf-12-78.png](qe-guide-scqubits-oliver.pdf-12-78.png)

![qe-guide-scqubits-oliver.pdf-12-79.png](qe-guide-scqubits-oliver.pdf-12-79.png)

![qe-guide-scqubits-oliver.pdf-12-59.png](qe-guide-scqubits-oliver.pdf-12-59.png)

![qe-guide-scqubits-oliver.pdf-12-114.png](qe-guide-scqubits-oliver.pdf-12-114.png)

![qe-guide-scqubits-oliver.pdf-12-124.png](qe-guide-scqubits-oliver.pdf-12-124.png)

![qe-guide-scqubits-oliver.pdf-12-68.png](qe-guide-scqubits-oliver.pdf-12-68.png)

(Transverse)

![qe-guide-scqubits-oliver.pdf-12-34.png](qe-guide-scqubits-oliver.pdf-12-34.png)

![qe-guide-scqubits-oliver.pdf-12-6.png](qe-guide-scqubits-oliver.pdf-12-6.png)

x

Transverse

|Col1||0 |Col3|
|---|---|---|
|||(Tra|
||||


|Col1|Col2||0|Col4|
|---|---|---|---|
||||y|
|||||


![qe-guide-scqubits-oliver.pdf-12-0.png](qe-guide-scqubits-oliver.pdf-12-0.png)

![qe-guide-scqubits-oliver.pdf-12-29.png](qe-guide-scqubits-oliver.pdf-12-29.png)

noise


![qe-guide-scqubits-oliver.pdf-12-87.png](qe-guide-scqubits-oliver.pdf-12-87.png)

![qe-guide-scqubits-oliver.pdf-12-103.png](qe-guide-scqubits-oliver.pdf-12-103.png)

![qe-guide-scqubits-oliver.pdf-12-47.png](qe-guide-scqubits-oliver.pdf-12-47.png)

![qe-guide-scqubits-oliver.pdf-12-122.png](qe-guide-scqubits-oliver.pdf-12-122.png)

![qe-guide-scqubits-oliver.pdf-12-66.png](qe-guide-scqubits-oliver.pdf-12-66.png)

![qe-guide-scqubits-oliver.pdf-12-83.png](qe-guide-scqubits-oliver.pdf-12-83.png)

![qe-guide-scqubits-oliver.pdf-12-84.png](qe-guide-scqubits-oliver.pdf-12-84.png)

![qe-guide-scqubits-oliver.pdf-12-43.png](qe-guide-scqubits-oliver.pdf-12-43.png)

![qe-guide-scqubits-oliver.pdf-12-85.png](qe-guide-scqubits-oliver.pdf-12-85.png)

![qe-guide-scqubits-oliver.pdf-12-86.png](qe-guide-scqubits-oliver.pdf-12-86.png)

![qe-guide-scqubits-oliver.pdf-12-102.png](qe-guide-scqubits-oliver.pdf-12-102.png)

![qe-guide-scqubits-oliver.pdf-12-46.png](qe-guide-scqubits-oliver.pdf-12-46.png)

![qe-guide-scqubits-oliver.pdf-12-105.png](qe-guide-scqubits-oliver.pdf-12-105.png)

![qe-guide-scqubits-oliver.pdf-12-51.png](qe-guide-scqubits-oliver.pdf-12-51.png)

![qe-guide-scqubits-oliver.pdf-12-10.png](qe-guide-scqubits-oliver.pdf-12-10.png)

![qe-guide-scqubits-oliver.pdf-12-38.png](qe-guide-scqubits-oliver.pdf-12-38.png)

![qe-guide-scqubits-oliver.pdf-12-104.png](qe-guide-scqubits-oliver.pdf-12-104.png)

![qe-guide-scqubits-oliver.pdf-12-113.png](qe-guide-scqubits-oliver.pdf-12-113.png)

![qe-guide-scqubits-oliver.pdf-12-97.png](qe-guide-scqubits-oliver.pdf-12-97.png)

![qe-guide-scqubits-oliver.pdf-12-50.png](qe-guide-scqubits-oliver.pdf-12-50.png)

![qe-guide-scqubits-oliver.pdf-12-58.png](qe-guide-scqubits-oliver.pdf-12-58.png)

![qe-guide-scqubits-oliver.pdf-12-24.png](qe-guide-scqubits-oliver.pdf-12-24.png)

![qe-guide-scqubits-oliver.pdf-12-112.png](qe-guide-scqubits-oliver.pdf-12-112.png)

![qe-guide-scqubits-oliver.pdf-12-57.png](qe-guide-scqubits-oliver.pdf-12-57.png)

![qe-guide-scqubits-oliver.pdf-12-2.png](qe-guide-scqubits-oliver.pdf-12-2.png)

![qe-guide-scqubits-oliver.pdf-12-121.png](qe-guide-scqubits-oliver.pdf-12-121.png)

![qe-guide-scqubits-oliver.pdf-12-65.png](qe-guide-scqubits-oliver.pdf-12-65.png)

![qe-guide-scqubits-oliver.pdf-12-13.png](qe-guide-scqubits-oliver.pdf-12-13.png)

![qe-guide-scqubits-oliver.pdf-12-120.png](qe-guide-scqubits-oliver.pdf-12-120.png)

![qe-guide-scqubits-oliver.pdf-12-100.png](qe-guide-scqubits-oliver.pdf-12-100.png)

![qe-guide-scqubits-oliver.pdf-12-123.png](qe-guide-scqubits-oliver.pdf-12-123.png)

![qe-guide-scqubits-oliver.pdf-12-106.png](qe-guide-scqubits-oliver.pdf-12-106.png)

![qe-guide-scqubits-oliver.pdf-12-64.png](qe-guide-scqubits-oliver.pdf-12-64.png)

![qe-guide-scqubits-oliver.pdf-12-27.png](qe-guide-scqubits-oliver.pdf-12-27.png)

![qe-guide-scqubits-oliver.pdf-12-67.png](qe-guide-scqubits-oliver.pdf-12-67.png)

![qe-guide-scqubits-oliver.pdf-12-52.png](qe-guide-scqubits-oliver.pdf-12-52.png)

![qe-guide-scqubits-oliver.pdf-12-9.png](qe-guide-scqubits-oliver.pdf-12-9.png)

![qe-guide-scqubits-oliver.pdf-12-41.png](qe-guide-scqubits-oliver.pdf-12-41.png)

![qe-guide-scqubits-oliver.pdf-12-42.png](qe-guide-scqubits-oliver.pdf-12-42.png)

![qe-guide-scqubits-oliver.pdf-12-37.png](qe-guide-scqubits-oliver.pdf-12-37.png)

![qe-guide-scqubits-oliver.pdf-12-96.png](qe-guide-scqubits-oliver.pdf-12-96.png)

![qe-guide-scqubits-oliver.pdf-12-23.png](qe-guide-scqubits-oliver.pdf-12-23.png)

![qe-guide-scqubits-oliver.pdf-12-138.png](qe-guide-scqubits-oliver.pdf-12-138.png)

![qe-guide-scqubits-oliver.pdf-12-81.png](qe-guide-scqubits-oliver.pdf-12-81.png)

![qe-guide-scqubits-oliver.pdf-12-139.png](qe-guide-scqubits-oliver.pdf-12-139.png)

![qe-guide-scqubits-oliver.pdf-12-82.png](qe-guide-scqubits-oliver.pdf-12-82.png)

![qe-guide-scqubits-oliver.pdf-12-33.png](qe-guide-scqubits-oliver.pdf-12-33.png)

![qe-guide-scqubits-oliver.pdf-12-93.png](qe-guide-scqubits-oliver.pdf-12-93.png)

![qe-guide-scqubits-oliver.pdf-12-110.png](qe-guide-scqubits-oliver.pdf-12-110.png)

![qe-guide-scqubits-oliver.pdf-12-111.png](qe-guide-scqubits-oliver.pdf-12-111.png)

![qe-guide-scqubits-oliver.pdf-12-92.png](qe-guide-scqubits-oliver.pdf-12-92.png)

![qe-guide-scqubits-oliver.pdf-12-20.png](qe-guide-scqubits-oliver.pdf-12-20.png)

![qe-guide-scqubits-oliver.pdf-12-55.png](qe-guide-scqubits-oliver.pdf-12-55.png)

![qe-guide-scqubits-oliver.pdf-12-56.png](qe-guide-scqubits-oliver.pdf-12-56.png)

![qe-guide-scqubits-oliver.pdf-12-19.png](qe-guide-scqubits-oliver.pdf-12-19.png)

(Transverse)


Transverse

|sing ||0|
|---|---|

|erence 2 1 ||0 y|
|---|---|


![qe-guide-scqubits-oliver.pdf-12-8.png](qe-guide-scqubits-oliver.pdf-12-8.png)

![qe-guide-scqubits-oliver.pdf-12-36.png](qe-guide-scqubits-oliver.pdf-12-36.png)

![qe-guide-scqubits-oliver.pdf-12-95.png](qe-guide-scqubits-oliver.pdf-12-95.png)

![qe-guide-scqubits-oliver.pdf-12-22.png](qe-guide-scqubits-oliver.pdf-12-22.png)

![qe-guide-scqubits-oliver.pdf-12-12.png](qe-guide-scqubits-oliver.pdf-12-12.png)

![qe-guide-scqubits-oliver.pdf-12-11.png](qe-guide-scqubits-oliver.pdf-12-11.png)

![qe-guide-scqubits-oliver.pdf-12-40.png](qe-guide-scqubits-oliver.pdf-12-40.png)

![qe-guide-scqubits-oliver.pdf-12-39.png](qe-guide-scqubits-oliver.pdf-12-39.png)

![qe-guide-scqubits-oliver.pdf-12-88.png](qe-guide-scqubits-oliver.pdf-12-88.png)

![qe-guide-scqubits-oliver.pdf-12-99.png](qe-guide-scqubits-oliver.pdf-12-99.png)

![qe-guide-scqubits-oliver.pdf-12-98.png](qe-guide-scqubits-oliver.pdf-12-98.png)

![qe-guide-scqubits-oliver.pdf-12-15.png](qe-guide-scqubits-oliver.pdf-12-15.png)

![qe-guide-scqubits-oliver.pdf-12-26.png](qe-guide-scqubits-oliver.pdf-12-26.png)

![qe-guide-scqubits-oliver.pdf-12-25.png](qe-guide-scqubits-oliver.pdf-12-25.png)

|1


|1


|1


|1 


FIG. 4. Transverse and longitudinal noise represented on the Bloch sphere. **(a)** Bloch sphere representation of the quantum
state __ = __ 0 + __ 1 . The qubit quantization axis  the _z_ axis  is _longitudinal_ in the qubit frame, corresponding to __ _z_
_|_ __ _|_ __ _|_ __
terms in the qubit Hamiltonian. The _x_ - _y_ plane is _transverse_ in the qubit frame, corresponding to __ _x_ and __ _y_ terms in the
qubit Hamiltonian. **(b)** Longitudinal relaxation results from energy exchange between the qubit and its environment, due
to transverse noise that couples to the qubit in the _x_ _y_ plane and drives transitions 0 1 . A qubit in state 1 emits
__ _|_ _|_ __ _|_ __
energy to the environment and relaxes to _|_ 0 __ with a rate  1 __ (blue arched arrow). Similarly, a qubit in state _|_ 0 __ absorbs energy
from the environment, exciting it to _|_ 1 __ with a rate  1 __ (orange arched arrow). In the typical operating regime _k_ B _T_ __  __ q ,
the up-rate is suppressed, leading to the overall decay rate  1 __  1 __ . **(c)** Pure dephasing in the transverse plane arises from
longitudinal noise along the _z_ axis that fluctuates the qubit frequency. A Bloch vector along the _x_ -axis will diffuse clockwise or
counterclockwise around the equator due to the stochastic frequency fluctuations, depolarizing the azimuthal phase with a rate
 __ . **(d)** Transverse relaxation results in a loss of coherence at a rate  2 =  1 _/_ 2+ __ , due to a combination of energy relaxation
and pure dephasing. Pure dephasing leads to decoherence of the quantum state (1 _/_ __ 2)( 0 + 1 ), initially pointed along the

_|_ __ _|_ __
_x_ -axis. Additionally, the excited state component of the superposition state may relax to the ground state, a phase-breaking
process that loses the orientation of the vector in the _x_ - _y_ plane.


FIG. 4. Transverse and longitudinal noise represented on the Bloch sphere. **(a)** Bloch sphere representation of the quantum
state __ = __ 0 + __ 1 . The qubit quantization axis  the _z_ axis  is _longitudinal_ in the qubit frame, corresponding to __ _z_
_|_ __ _|_ __ _|_ __
terms in the qubit Hamiltonian. The _x_ - _y_ plane is _transverse_ in the qubit frame, corresponding to __ _x_ and __ _y_ terms in the
qubit Hamiltonian. **(b)** Longitudinal relaxation results from energy exchange between the qubit and its environment, due
to transverse noise that couples to the qubit in the _x_ _y_ plane and drives transitions 0 1 . A qubit in state 1 emits
__ _|_ _|_ __ _|_ __
energy to the environment and relaxes to _|_ 0 __ with a rate  1 __ (blue arched arrow). Similarly, a qubit in state _|_ 0 __ absorbs energy
from the environment, exciting it to _|_ 1 __ with a rate  1 __ (orange arched arrow). In the typical operating regime _k_ B _T_ __  __ q ,
the up-rate is suppressed, leading to the overall decay rate  1 __  1 __ . **(c)** Pure dephasing in the transverse plane arises from
longitudinal noise along the _z_ axis that fluctuates the qubit frequency. A Bloch vector along the _x_ -axis will diffuse clockwise or
counterclockwise around the equator due to the stochastic frequency fluctuations, depolarizing the azimuthal phase with a rate
 __ . **(d)** Transverse relaxation results in a loss of coherence at a rate  2 =  1 _/_ 2+ __ , due to a combination of energy relaxation
and pure dephasing. Pure dephasing leads to decoherence of the quantum state (1 _/_ __ 2)( 0 + 1 ), initially pointed along the



2 2
unit length, __ + __ = 1, connecting the center of the
_|_ _|_ _|_ _|_
sphere to any point on its surface.

The _z_ -axis connects the north and south poles. It
is called the _longitudinal axis_ , since it represents the
_qubit quantization axis_ for the states 0 and 1 in the
_|_ __ _|_ __
qubit eigenbasis. In turn, the _x_ - _y_ plane is the
_transverse plane_ with _transverse axes_ _x_ and _y_ . In this
Cartesian coordinate system, the unit Bloch vector __ _a_ =
(sin __ cos _,_ sin __ sin _,_ cos __ ) is represented using the polar
angle 0 __ __ and the azimuthal angle 0 _ <_ 2 __ , as
__ __ __
illustrated in Fig. 4 (a). Following our convention, state
0 at the north pole is associated with +1, and state 1
_|_ __ _|_ __
(the south pole) with 1. We can similarly represent the
__
quantum state using the angles __ and __ ,


__ __ for a pure state __ is equivalently
_|_ __ _|_ _|_ __



1 1
__ = ( _I_ + __ _a_ __ __ ) =

2 __



1
__ =


1 + cos _ e_ __ _i_ sin __
_e_ _i_ sin __ 1 + sin __


(38)



(39)

(40)


cos 2 __


_e_ __ _i_ cos __



__ 2 sin __ 2


_e_ _i_ cos __



__ 2 sin __ 2


sin 2 __



2
_|_ __ _|_ __ 2 __

__ __ __ _|_ __ _|_



2
_|_ __ _|_ __ 2 __


where _I_ is the identity matrix, and __ __ = [ __ _x_ _, _ _y_ _, _ _z_ ] is a
vector of Pauli matrices. If the Bloch vector __ _a_ is a unit

2
vector, then __ represents a pure state __ and Tr( __ ) = 1.
More generally, the Bloch sphere can be used to represent
_mixed states_ , for which __ _a_ _<_ 1; in this case, the Bloch
_|_ _|_
vector terminates at points _inside_ the unit sphere, and

2
0 Tr( __ ) _<_ 1. To summarize, the surface of the unit
__
sphere represents pure states, and its interior represents
mixed states 6 .

**_2._** **_Bloch-Redfield model of decoherence_**

Within the standard Bloch-Redfield 110112 picture of
two-level system dynamics, noise sources weakly coupled
to the qubits have short correlation times with respect
to the system dynamics. In this case, the relaxation pro-



__
__ = __ 0 + __ 1 = cos
_|_ __ _|_ __ _|_ __ 2



__ 0 + _e_ _i_ sin __

2 _|_ __



1 _._ (37)
2 _|_ __


The Bloch vector is stationary on the Bloch sphere in
the _rotating frame picture_ . If state 1
_|_ __
has a higher energy than state 0
_|_ __
(as it generally does in superconducting qubits), then in a stationary frame, the Bloch vector
would precess around the _z_ -axis at the qubit frequency
( _E_ 1 __ _E_ 0 ) _/_  . Without loss of generality (and much easier
to visualize), we instead _choose_ to view the Bloch sphere
in a reference frame where the _x_ and _y_ -axes also rotate
around the _z_ -axis at the qubit frequency. In this _rotating_
_frame_ , the Bloch vector appears stationary as written in
Eq. (37). The rotating frame will be described in detail
in Section IV D 1 in the context of single-qubit gates.

For completeness, we note that the density matrix __ =


-----


14

ground state ( 0 ) at the north pole, _p_ = 1 is entirely
_|_ __ __
in the excited state ( 1 ) at the south pole, and _p_ = 0 is
_|_ __
a completely depolarized mixed state at the center of the
Bloch sphere.
As illustrated in Fig. 4(b), longitudinal relaxation is
caused by _transverse noise_ , via the _x_ - or _y_ -axis, with
the intuition that off-diagonal elements of an interaction
Hamiltonian are needed to connect and drive transitions
between states 0 and 1 .
_|_ __ _|_ __
Depolarization occurs due to energy exchange with an
environment, generally leading to both an up transition
rate  1 __ (excitation from _|_ 0 __ to _|_ 1 __
), and a down transition rate  1 __ (relaxation from _|_ 1 __ to _|_ 0 __ ). Together,
these form the longitudinal relaxation rate  1 :


cesses are characterized by two rates (see Fig. 4):



1
longitudinal relaxation rate:  1
__ _T_


(41)
_T_ 1



1
transverse relaxation rate:  2
__ _T_



1  1

=
_T_ 2



1 +  __

2


(42)


which contains the pure dephasing rate  __ . We note
that the definition of  2 as a sum of rates presumes that
the individual decay functions are exponential, which occurs for Lorentzian noise spectra (centered at __ = 0)
such as white noise (short correlation times) with a highfrequency cutoff.
The impact of noise on the qubit can be visualized on
the Bloch sphere in Fig. 4(a). For an initial state ( _t_ = 0)

__ = __ 0 + __ 1 _,_ (43)
_|_ __ _|_ __ _|_ __

the Bloch-Redfield density matrix __ BR for the qubit is
written 113,114 ,



1
 1 __ _T_ 1 =  1 __ +  1 __ _._ (45)

_T_ decay time in the exponential decay function in Eq. (44), and it is the characteristic time scale 1 is the 1 _/e_
over which qubit population will relax to its steadystate value.
For superconducting qubits, this steadystate value is generally the ground state, due to Boltzmann statistics and typical operating conditions. Boltzmann equilibrium statistics lead to the detailed balance relationship  1 = exp(  __ q _/k_ B _T_ ) 1 , where _T_
__ __ __
is the temperature and _k_ B is the Boltzmann constant,
with an equilibrium qubit polarization approaching _p_ =
tanh(  __ q _/_ 2 _k_ B _T_ ).
Typical qubits are designed at frequency __ q _/_ 2 __ __ 5 GHz and are operated at dilution
refrigerator temperatures _T_ 20 mK. In this limit, the
__
up-rate  1 __
is exponentially suppressed by the Boltzmann factor exp( __  __ q _/k_ B _T_
), and so only the downrate  1 __
contributes significantly, relaxing the population to the ground state. Thus, qubits generally spontaneously lose energy to their cold environment, but the
environment rarely introduces a qubit excitation. As a
result, the equilibrium polarization approaches unity [see
Eq. (44)] 118,119 .
Only noise at the qubit frequency mediates qubit transitions, whether absorption or emission, and this noise is
generally well behaved (short correlation time, many
modes weakly coupled to qubit, no divergences) around
the qubit frequency for superconducting qubits. The intuition is that qubit-transition linewidths are relatively
narrow in frequency, and so the noise generally does not
vary much over this narrow frequency range. Although
there are a few notable exceptions, for example, qubit
decay in the presence of hot quasiparticles 120122 , which
can lead to non-exponential decay functions, longitudinal
depolarization measurements generally present exponential decay functions consistent with the Bloch-Redfield
picture.
An example of a _T_ 1 measurement is shown in Fig. 5(a).
The qubit is prepared in its excited state using an X __
pulse, and then left to spontaneously decay to the ground
state for a time __ , after which the qubit is measured. A
single measurement will project the quantum state into
either state 0 or state 1 , with probabilities that cor-
_|_ __ _|_ __


1 + ( __ 2 1) _e_ __  1 _t_ __ __ _e_ _it_ _e_ __  2 _t_
__ BR = __ __ _e_ _|_ __ _|_ _it_ __ _e_ __  2 _t_ __ 2 _e_ __  1 _t_
 _|_ _|_


(44)


There are a few important distinctions between Eq. (44)
and Eq. (40), which we list here and then describe in
more detail in subsequent sections.

-  First, we have introduced the _longitudinal decay_
_function_ exp( __  1 _t_
), which accounts for longitudinal relaxation of the qubit.

-  Second, we introduced the
_transverse decay function_ exp( __  2 _t_
), which accounts for transverse decay of the qubit.

-  Third, we have introduced an explicit phase accrual exp( _it_ ), where __ = __ q __ __ d
, which generalizes the Bloch sphere picture to account for
cases where the qubit frequency __ q differs from the
rotating-frame frequency __ d , as we will see later
when discussing measurements of _T_ 2 using Ramsey
interferometry 115,116 , and in Section IV D 1 in the
context of single-qubit gates.

-  And, fourth, we have constructed the matrix such
that for _t_ __ ( _T_ 1 _, T_ 2
), the upper-left matrix element will approach unit value, indicating that all
population relaxes to the ground state, while the
other three matrix elements decay to zero. This is
related to the assumption that the environmental
temperature is low enough that thermal excitations
of the qubit from the ground to excited state rarely
occur.

**Longitudinal relaxation**
The longitudinal relaxation rate  1
describes depolarization along the qubit quantization axis, often referred
to as energy decay or energy relaxation. In this language, a qubit with polarization _p_ = 1 is entirely in the


-----


15


(a)

(b)


(c)


|E|X X/2 /2X/2 /2 cho: t|Col3|
|---|---|---|
||||


(d)

|Relaxation:|X Readout  t|
|---|---|

|Rams|X/2  X/2 ey: t|
|---|---|


![qe-guide-scqubits-oliver.pdf-14-0.png](qe-guide-scqubits-oliver.pdf-14-0.png)


117
FIG. 5. Characterizing longitudinal ( _T_ 1 ) and transverse ( _T_ 2 ) relaxation times of a transmon qubit . **(a)** Longitudinal
relaxation (energy relaxation) measurement. The qubit is prepared in the excited state using an X __ -pulse and measured after
a waiting time __ . For each value __ , this procedure is repeated to obtain an ensemble average of the qubit polarization: +1
corresponding to 0 , and 1 corresponding to 1 . The resulting exponential decay function has a characteristic time _T_ 1 = 85
_|_ __ __ _|_ __
__ s. **(b)** Transverse relaxation (decoherence) measurement via Ramsey interferometry. The qubit is prepared on the equator
using an X _/_ 2 -pulse, intentionally detuned from the qubit frequency by __ , causing the Bloch vector to precess in the rotating
frame at a rate __ around the _z_ -axis. After a time __ , a second X _/_ 2 pulse then projects the Bloch vector back on to the
_z_ axis, effectively mapping its former position on the equator to a position on the _z_ axis. The oscillations decay with an
approximately (but not exactly) exponential decay function, with a characteristic time _T_ 2 __ = 95 __ s. **(c)** Transverse relaxation
(decoherence) measurement via a Hahn echo experiment 116 . The qubit is prepared and measured in the same manner as the
Ramsey interfometry experiment, except that a single _X_ pulse is applied midway through the free-evolution time __ . The
decay function is approximately exponential, with a characteristic time _T_ 2 _E_ = 120 __ s. The coherence improvement using the
Hahn echo over panel (b) indicates that some low-frequency dephasing noise has been mitigated; however, a small amount
remains since _T_ 2 _E_ has not yet reached the 2 _T_ 1 limit. **(d)** Coherence function incorporating _T_ 1 loss and Gaussian dephasing
components of the Ramsey interferometry data in panel (b). The Gaussian-distributed 1 _/f_ noise spectrum of magnetic flux

2 2
noise leads to a decay function exp( __ _t/_ 2 _T_ 1 ) exp( __ __ _N_ ) = exp( __ _t/_ 2 _T_ 1 ) exp( __ _t_ _/T_ _,_ G ) in Eq. (46). These two decay functions
together match well the Ramsey data in panel (b).


respond to the qubit polarization. To make an estimate
of this polarization, one needs to identically prepare the
qubit and repeat the experiment many times. This is
analogous to flipping a coin: any single flip will yield
heads or tails, but the probability of obtaining a heads
or tails can be estimated by flipping the coin many times
and taking the ensemble average. The resulting exponential decay has a characteristic time _T_ 1 = 85 __ s.

**Pure dephasing**

The _pure dephasing_ rate  __ describes depolarization


in the _x_ _y_ plane of the Bloch sphere. It is referred to
__
as pure dephasing, to distinguish it from other phasebreaking processes such as energy excitation or relaxation.

As illustrated in Fig. 4(c), pure dephasing is caused
by _longitudinal noise_ that couples to the qubit via the _z_
axis. Such longitudinal noise causes the qubit frequency
__ q to fluctuate, such that it is no longer equal to the
rotating frame frequency __ _d_
, and causes the Bloch vector to precess forward or backward in the rotating frame.


-----


16

Bloch vector back on to the -axis. Repeated measurements are made to take an ensemble averaged estimate of _z_
the qubit polarization, as a function of __ . The resulting
oscillations in Fig. 5(b) feature an approximately exponential decay function with time _T_ __ 2 = 98 __ s. The *
indicates that the Ramsey experiment is sensitive to _inhomogeneous broadening_ . That is, it is highly sensitive
to quasi-static, low-frequency fluctuations that are constant within one experimental trial, but vary from trial
to trial, e.g., due to 1 _/f_ -type noise. This sensitivity to
quasi-static noise is related to the corresponding _N_ = 0
noise filter function shown in Fig. 5(d) being centered
at at zero-frequency, as described in more detail in Section III D 2.
The Hahn echo shown in Fig. 5(c) is an experiment
that is less sensitive to quasi-static noise. By placing
a _Y_ __
pulse at the center of a Ramsey interferometry experiment, the quasi-static contributions to dephasing can
be refocused, leaving an estimate _T_ 2 _E_
that is less sensitive to inhomogeneous broadening mechanisms. The
pulses are generally chosen to be resonant with the qubit
transition for a Hahn echo, since any frequency detuning
would be nominally refocused anyway. The resulting decay function in Fig. 5(c) is essentially exponential with
time _T_ 2 _E_ = 120 __ s.
With the known _T_ 1 and _T_ 2 times, one can infer the pure
dephasing time _T_ __ from Eq. (42), provided the decay
functions are exponential. In superconducting qubits,
however, the broadband dephasing noise (e.g., flux noise,
charge noise, critical-current noise, ...) tends to exhibit
a 1 _/f_ -like power spectrum. Such noise is singular near
__ = 0, has long correlation times, and generally does
not fall within the Bloch-Redfield description. The decay function of the off-diagonal terms in Eq. (44) are
generally non-exponential, and for such cases, the simple
expression in Eq. (42) is not applicable.

**_3._** **_Modification due to_** 1 _/f_ **_-type noise_**

If we assume that the qubit is coupled to many independent fluctuators, then, regardless of their individual statistics, they will in concert generate noise with
a Gaussian distribution due to the central limit theorem. We therefore say that the longitudinal fluctuations

123,124
exhibit Gaussian-distributed 1 _/f_ noise . For 1 _/f_

2
noise spectra, the phase decay function is itself a Gaussian exp ( _t/T_ _,_ G ) , where we write _T_ _,_ G to distinguish
__
it from _T_ __ used in Eq. (42). Furthermore, this function
 
is separable from the _T_ 1 -type exponential decay, because
the _T_ 1 -noise remains regular at the qubit frequency. The
density matrix in Eq. (44) becomes, following Refs. 78
and 113,


Intuitively, we can imagine identically preparing several
instances of the Bloch vector along the _x_ -axis. For each
instance, the stochastic fluctuations of qubit frequency
will result in a different precession frequency, resulting
in a net fanout of the Bloch vector in the _x_ _y_ plane.
__
This eventually leads to a complete depolarization of the
azimuthal angle __ . Note that this stochastic effect will be
captured in the transverse relaxation rate  2
(next section); it is _not_ the deterministic term exp( _it_ ) that
__
appears in Eq. (44), which represents intentional detuning of the qubit reference frame.
There are a few important distinctions between pure
dephasing and energy relaxation. First, in contrast to
energy relaxation, pure dephasing is a resonant phenomenon; noise at any frequency can modify the qubit _not_
frequency and cause dephasing. Thus, qubit dephasing
is subject to broadband noise. Second, since pure dephasing is elastic (there is no energy exchange with the
environment), it is in principle _reversible_ . That is, the
dephasing can be undone  with quantum information being preserved  through the application of unitary
operations, e.g., dynamical decoupling pulses 78 , see Sec.
III D 2.
The degree to which the quantum information can be
retained depends on many factors, including the bandwidth of the noise, the rate of dephasing, the rate at
which unitary operations can be performed, etc. This
should be contrasted with spontaneous energy relaxation,
which is an _irreversible_ process. Intuitively, once the
qubit emits energy to the environment and its myriad
uncontrollable modes, the quantum information is essentially lost with no hope for its recovery and reconstitution
back into the qubit.
**Transverse relaxation**
The transverse relaxation rate  2 =  1 _/_ 2 +  __ describes
the loss of coherence of a superposition state, for example
(1 _/_ __ 2)( 0 + 1 ), pointed along the _x_ -axis on the equator

_|_ __ _|_ __
of the Bloch sphere as illustrated in Fig. 4(d). Decoherence is caused in part by longitudinal noise, which fluctuates the qubit frequency and leads to pure dephasing  __
(red). It is also caused by transverse noise, which leads
to energy relaxation of the excited-state component of
the superposition state at a rate  1
(blue). Such a relaxation event is also a phase-breaking process, because once
it occurs, the Bloch vector points to the north pole, 0 ,
_|_ __
and there is no longer any knowledge of which direction
the Bloch vector _had_ been pointing along the equator;
the relative phase of the superposition state is lost.
Transverse relaxation _T_ 2
can be measured using Ramsey interferometry, as shown and described in Fig. 5(b).
The protocol positions the Bloch vector on the equator
using a _X_ _/_ 2 -pulse. Typically, the carrier frequency of
this pulse is slightly detuned from the qubit frequency
by an amount __
. As a result, the Bloch vector will precess around the _z_ -axis at a rate __ . This is done for
convenience sake, so that the resulting Ramsey measurement will oscillate, making it easier to analyze. After
precessing for a time __ , a second X _/_ 2 -pulse projects the


Intuitively, we can imagine identically preparing several
instances of the Bloch vector along the _x_ -axis. For each
instance, the stochastic fluctuations of qubit frequency
will result in a different precession frequency, resulting
in a net fanout of the Bloch vector in the _x_ _y_ plane.
__
This eventually leads to a complete depolarization of the
azimuthal angle __ . Note that this stochastic effect will be
captured in the transverse relaxation rate  2
(next section); it is _not_ the deterministic term exp( _it_ ) that
__
appears in Eq. (44), which represents intentional detuning of the qubit reference frame.
There are a few important distinctions between pure
dephasing and energy relaxation. First, in contrast to
energy relaxation, pure dephasing is a resonant phenomenon; noise at any frequency can modify the qubit _not_
frequency and cause dephasing. Thus, qubit dephasing
is subject to broadband noise. Second, since pure dephasing is elastic (there is no energy exchange with the
environment), it is in principle _reversible_ . That is, the
dephasing can be undone  with quantum information being preserved  through the application of unitary
operations, e.g., dynamical decoupling pulses 78 , see Sec.
III D 2.
The degree to which the quantum information can be
retained depends on many factors, including the bandwidth of the noise, the rate of dephasing, the rate at
which unitary operations can be performed, etc. This
should be contrasted with spontaneous energy relaxation,
which is an _irreversible_ process. Intuitively, once the
qubit emits energy to the environment and its myriad
uncontrollable modes, the quantum information is essentially lost with no hope for its recovery and reconstitution
back into the qubit.
**Transverse relaxation**
The transverse relaxation rate  2 =  1 _/_ 2 +  __ describes
the loss of coherence of a superposition state, for example
(1 _/_ __ 2)( 0 + 1 ), pointed along the _x_ -axis on the equator


__ =


__ __ _e_ __ _it_ _e_ __ 1 2


1 + ( _|_ __ _|_ 2 __ 1 1) _e_ __  1 _t_ __ __ _e_ _it_ _e_ __ 1 2


2 _t_ _e_ __ __ _N_ ( _t_ )


2 _t_ _e_ __ __ _N_ ( _t_ ) _|_ __ _|_ 2 _e_ __  1


(46)


-----


17

For completeness, in addition to 1 _/f_
dephasing mechanisms, we note that there are also white pure dephasing mechanisms, which give rise to an exponential decay function for the dephasing component of _T_ 2 . One
common example is dephasing due to the shot noise of
residual photons in the readout resonator coupled to superconducting qubits, as we discuss in Section III C 3.

**_4._** **_Noise power spectral density (PSD)_**

The frequency distribution of the noise power for a stationary noise source __ is characterized by its PSD _S_ __ ( __ )

|uubbiitt eemmiissssiioonn|Col2|
|---|---|
|eennvviirroonnmmeenntt||


![qe-guide-scqubits-oliver.pdf-16-1.png](qe-guide-scqubits-oliver.pdf-16-1.png)

Low-frequency

![qe-guide-scqubits-oliver.pdf-16-0.png](qe-guide-scqubits-oliver.pdf-16-0.png)
noise

FIG. 6. Examples of symmetric and asymmetric noise spectral densities.
Noise at positive (negative) frequencies corresponds to the qubit emitting (absorbing) energy to (from)
its environment.
Thermal noise is proportional to temperature _T_ and carries essentially a white noise spectrum. As
it represents a classical fluctuating parameter, such as electric current, the noise power spectral density is symmetric
in frequency. When resonant with the qubit, it will drive
both stimulated emission and absorption processes. The qubit

125
may also spontaneously emit energy to its environment, represented as Nyquist noise , a quantum mechanical effect
that is not symmetric in frequency. At sufficiently low temperatures or high frequencies,  _ >_ 2 _k_ B _T_ , the Nyquist noise
dominates thermal noise. Another common example is 1 _/f_
noise, which is also a classical noise fluctuation and symmetric in frequency.

where the decay function exp( __ _N_ ( _t_ )) contains the
__ __ __
_coherence function_ __ _N_ ( _t_
), which generalizes pure dephasing to include non-exponential decay functions. As we
shall see later, the subscript _N_
labeling the decay function refers to the number of __ -pulses used to refocus the
low-frequency noise, which impacts the form of the decay function. Because the function is no longer purely
exponential, we cannot formally write the transverse relaxation decay function as exp( __ _t/T_ 2
). However, an exponential decay remains a practically reasonable approximation for _T_ __  _T_ 1 . We also note that the energy decay
component of the transverse relaxation is exp( __ _t/_ 2 _T_ 1 ),
and so _T_ 2 can never be larger than 2 _T_ 1 . In the absence
of pure dephasing, the maximum _T_ 2 = 2 _T_ 1 is reached.
As an example, consider the Ramsey interferometry
data in Fig. 5(b). Since the dephasing is relatively weak,
the transverse relaxation function as exp( __ _t/T_ 2 ) is a
reasonable fit and yields _T_ 2 = 95 __ s.
However, using the value _T_ 1 = 85 __ s from Fig. 5(a) and dividing
out exp( __ _t/_ 2 _T_ 1
) from the data in Fig. 5(b), the remaining pure dephasing decay function is shown in Fig. 5(d)
and assumes a Gaussian envelope exp( __ _N_ ( _t_ )) =

2 __ __ __
exp ( _t/T_ _,_ G _t_ ) , with _T_ _,_ G = 98 __ s. The Hahn echo
__
data in Fig. 5(c) may be treated similarly.
 


_S_ __ ( __ ) = __ _d_ __ ( __ ) __ (0) _e_ __ _i_ _._ (47)

__ __

 __

The Wiener-Khintchine theorem states that the PSD
is the Fourier transform of the autocorrelation function
_c_ __ ( __ ) = __ ( __ ) __ (0) of the noise source __
__ __
. Since the integration limits are ( _,_ ), this is the bilateral PSD.
__ __
Symmetrizing the PSD allows one to consider only positive frequencies, which is termed a unilateral PSD. Both
unilateral and bilateral PSDs are used, often with the
same notation, and so one needs to know how the PSD
is defined, keep track of the factors of 2 and __ , and also
be aware of the implications for quantum systems.
For classical systems, the noise power spectral density
is symmetric. This is because the autocorrelation function of real signals is itself a real function, and the Fourier
transform of a real temporal function is symmetric in the
frequency domain. Dephasing noise is caused by real,
fluctuating fields, and so its PSD is generally symmetric.

126
Examples of such classical noise include thermal (Johnson) noise and 1 _/f_ noise (see Fig. 6).
In turn, the inverse Fourier transform of the PSD will
yield the autocorrelation function:



1
_c_ __ ( __ ) =

2 __


__ _d S_ __ ( __ ) _e_ _i_ _._ (48)
 __


_c_ __ ( __ ) =


This implies that integrating the noise power spectral
density with __ = 0 yields the second moment of the noise,
or, for zero-mean fluctuations, the variance.
However, the autocorrelation function for a quantum
system may be complex-valued due to the fact that quantum operators generally do not commute at different
times. This means that time-ordering of the operators
matters, and the PSD need not be symmetric in frequency. This is generally the case for transverse noise
causing longitudinal energy relaxation. Noise at a positive frequency _S_ ( __ q ) corresponds to energy transfer from
the qubit to the environment, including both stimulated
and spontaneous emission, associated with the down-rate
 1 __ . Noise at a negative frequency _S_ ( __ __ q ) corresponds
to energy transfer to the qubit from the environment, associated with the up-rate  1 __ . For a detailed discussion,
see Refs. 127 and 128. Spontaneous emission to a cold
environment or electromagnetic vacuum, represented by


-----


18

2 2
_S_ _Q_ ( __ ) = _B_ _Q_ [ _/_ (2 __ 1Hz)], where the noise strength _B_ _Q_

__
at 1 Hz can assume a range of values depending on the
level of dissipation in the system. Likewise, the cross-over
from 1 _/f_ -like behavior to _f_ -like behavior generally occurs
at around 1 GHz, but will vary higher or lower between
samples depending on the degree of dissipation 62,136 .

**_2._** **_Magnetic flux noise_**

Another commonly observed noise in solid-state devices is magnetic _flux noise_ . The origin of this noise is
understood to arise from the stochastic flipping of spins

137
(magnetic dipoles) that reside on the surfaces of the superconducting metals comprising the qubit , resulting
in random fluctuations of the effective magnetic field that
biases flux-tunable qubits.

For example, in the case of the split transmon, the
external magnetic field threading the loop couples longitudinally to the qubit and modulates the transition frequency via the Josephson energy _E_ _J_ (except at __ _e_ = 0,
where the qubit is first-order insensitive to magneticfield fluctuations). Because the flux noise is longitudinal
to the transmon, it contributes to pure dephasing ( _T_ __ ).
However, in the case of the flux qubit, and depending on
the flux-bias point, the flux noise may be either longitudinal  causing dephasing _T_ __
62,78
 or it may couple transversely and thus contribute to _T_ 1 relaxation . The
noise power spectrum of these fluctuations generally exhibits a quasi-universal dependence,


Nyquist noise in Fig. 6, is an example of an asymmetric
noise PSD 125 .
In general, making a connection between _S_ __ ( __ ) and
the measured qubit decay functions is the basis for noise
spectroscopy up to second-order statistics 78,129132 . The
search for higher-order spectra related to non-Gaussian
noise is a current topic of active research 133 .

**C.** **Common examples of noise**

There are many sources of stochastic noise in superconducting qubits, and we refer the reader to Ref. 40 for
a review. Here, we briefly present several of the most
common types of noise, their affect on coherence, and
refer the reader to the references for a more detailed discussion.

**_1._** **_Charge noise_**

_Charge noise_ is ubiquitous in solid-state devices. It
arises from charged fluctuators present in the defects or
charge traps that reside in interfacial dielectrics, the junction tunnel barrier, and in the substrate itself. These
are often modeled as an ensemble of fluctuating two-level
systems or as bulk dielectric loss 134,135 . For example, in
the case of a transmon qubit, the electric field between
the capacitor plates traverses and couples to dielectric
defects residing on the metal surfaces of the plates (for
lateral-plate-type capacitors) or the capacitor dielectric
between the plates (for parallel-plate-type capacitors).
The electric field variable is transverse with respect to
the quantization axis of the transmon qubit, which means
that this noise is mainly responsible for energy relaxation
( _T_ 1 ). Additionally, if the _E_ _J_ _/E_ _C_ ratio of the transmon is
not made sufficiently large (smaller than around 60), the
qubit frequency itself will also be sensitive to broadband
charge fluctuations. In this case, low-frequency charge
noise couples longitudinally to the transmon and causes
pure dephasing ( _T_ __ ).
Charge noise is modeled primarily as a combination of
inverse-frequency noise and Nyquist noise, also referred
to as _ohmic_ noise. At lower frequencies, the spectral
density takes the form


2 __ 1Hz
__

__




__ 
_,_ (50)




2
_S_  ( __ ) = _A_



2 2
with __  __ 0 _._ 8 __ 1 _._ 0 and _A_  __ (1 __  0 ) _/_ Hz, and has
been shown to extend from less than millihertz to beyond
gigahertz frequencies 78,131,132,138,139 .

The large, low-frequency weighting of the 1 _/f_ power
distribution enables the use of engineered error mitigation techniques  such as dynamical decoupling  to
achieve better coherence 78,140142
143
and for improving single and two-qubit gate fidelity
. It was recently demonstrated that 1 _/f_ flux noise is also a _T_ 1 -mechanism when
extended out to the qubit frequency 62 , and one similarly
expects a crossover to ohmic flux noise at high enough
frequencies 144 .

Although much is known about the statistics and
number of the defects presumed responsible for flux

137,145
noise, their precise physical manifestation remains uncertain . The fact that the 1 _/f_ noise is quasi-universal
and largely independent of device, strongly suggests a
common origin for the noise. Recent studies suggest that

145,146
adsorbed molecular oxygen may be responsible for fluxnoise .


2 __ 1Hz
__

__




__ _Q_
_,_ (49)




2
_S_ _Q_ ( __ ) = _A_



2 3 2
with quasi-universal values _A_ _Q_ = (10 __ _e_ ) _/_ Hz at 1 Hz,
and __ _Q_ 1. In addition to large 1 _/f_ fluctuations, early
__
charge qubits often witnessed discrete, charge offsets reminiscent of random telegraph noise. Together, these two
mechanisms severely limited the utility of charge qubits,
and served as a strong motivation to move to capacitively shunted charge qubits (transmons), which greatly
reduced the qubit longitudinal sensitivity to charge noise.
At higher frequencies, the power spectrum takes the form


-----


19

pair . Although this quasiparticle generation mechanism is not yet well understood, it has been shown that 149,150

122
quasiparticles can be transiently pumped away, improving _T_ 1 times and reducing _T_ 1 temporal variation .

**D.** **Operator form of qubit-environment interaction**

Similar to the way that two qubits are coupled, a qubit
may couple and interact with uncontrolled degrees of
freedom (DOF) in its environment (the noise sources).
The interaction Hamiltonian between the qubit DOF
( _O_  _q_ ) and those of the noise source ( __  ) may be expressed
in a general form

_H_  int = __ _O_  _q_ __  (53)

where __ denotes the coupling strength  which is related
to the sensitivity of the qubit to environmental fluctuations __ _H_  _q_ _/_  and we assume that _O_  _q_
is a qubit operator within the qubit Hamiltonian  _H_ _q_
. The noisy environment represented by the operator  __ produces fluctuations
__
. Note that we retained the hats in this section to remind us that these are quantum operators.

**_1._** **_Connecting_** _T_ 1 **_to_** _S_ ( __ )

If the coupling is transverse to the qubit, e.g. _O_  _q_
is of the type __ _x_ or ( _a_ + _a_ __ )  see the related case of
qubit-qubit coupling treated in Sec. II C  then noise
at the qubit frequency can cause transitions between
the qubit eigenstates. Since this is a stochastic process,
the ensemble-average manifests itself as a decay (usually
exponential) of the qubit population towards a certain
equilibrium value (usually the qubit ground state 0 for
_|_ __
_k_ _B_ _T_ __  __ q ). Again, this process is equivalently referred
to as  _T_ 1
relaxation, energy relaxation, or longitudinal relaxation. As stated above, _T_ 1 is the characteristic
time scale of the decay. Its inverse,  1 = 1 _/T_ 1 is called
the relaxation rate and depends on the power spectral
density of the noise _S_ ( __ ) at the transition frequency of
the qubit __ = __ q :


**_3._** **_Photon number fluctuations_**

_photon number fluctuation_ In the circuit QED architecture, is another major decoherence resonator
source 147 . Residual microwave fields in the cavity have
photon-number fluctuations that in the dispersive regime
impact the qubit through an interaction term __ _z_ _n_ , see
Sec. II C 2, leading to a frequency shift  Stark = 2 __ _n_  ,

2 2
where  _n_ is the average photon number, and __ = __ _/_ ( __ +

2
4 __ ) effectively scales the photon population seen by the
qubit due to the interplay between the qubit-induced dispersive shift of the resonator frequency ( __
) and the resonator decay rate ( __ ).
In the dispersive limit, the noise is longitudinally coupled to the qubit and leads to pure dephasing at a rate,



2

4 __
 __ = __ _n._  (51)

__

The fluctuations originate from residual photons in the

107,148
resonator, typically due to radiation from higher temperature stages in the dilution refrigerator . The
corresponding noise spectral density is of a Lorentzian
type,



2 2 __ _n_ 
_S_ ( __ ) = 4 __ (52)

__ 2 + __ 2 _,_

which exhibits an essentially white noise spectrum up to
a 3dB cutoff frequency __ = __ set by the resonator decay
rate __ , see Ref. 62.

**_4._** **_Quasiparticles_**

_Quasiparticles_
121
, i.e. unpaired electrons, are another important noise source for superconducting devices . The
tunneling of quasiparticles through a qubit junction may
lead to both , depending on the type of qubit, the bias point, and the _T_ 1 relaxation and pure dephasing _T_ __
junction through which the tunneling event occurs 120,122 .
Quasiparticles are naturally excited due to thermodynamics, and the quasiparticle density in equilibrium
superconductors should be exponentially suppressed as
temperature decreases. However, below about 150 mK,

8 6
the quasiparticle density observed in superconducting devices  generally in the range 10 __ __ 10 __ per Cooper pair
 is much higher than BCS theory would predict for a superconductor in equilibrium with its cryogenic environment at 10 mK. The reason for this excess quasiparticle
population is unclear, but it is very likely related to the
presence of additional, non-thermal mechanisms that increase the generation rates, bottleneck effects that occur at millikelvin temperatures to reduce recombination
rates, or a combination of both.
It has been shown that the observed _T_ 1 and excess
excited-state population measured in todays state-ofthe-art high-coherence transmon are self-consistent with

7 6
excess hot nonequilibrium quasiparticles at the quasiuniversal density of around 10 __ __ 10 __ per Cooper



0 __ _H_  _q_
 __ _|_ __







1
 1 =  2



1
 1 =


_q_ 1

__ _|_ __


_S_ __ ( __ q ) _,_ (54)


where __ _H_  _q_ _/_ is the qubit transverse susceptibility to

2
fluctuations __ , such that __ is the ensemble average
_|_ _|_
value of the environmental noise sources as seen by the
qubit. Eq. (54) is equivalent to Fermis Golden Rule,
in which the qubits transverse susceptibility to noise is
driven by the noise power spectral density. The qubit
, the relevant term in the transmon Hamiltonian in Eq. (16) is transverse susceptibility can be used to calculate the prefactors; for example, for fluctuations __ = _n_


-----


20

cally modulate the transition frequency of the qubit and
thereby introduce a stochastic phase evolution of a qubit
superposition state. This gradually leads to a loss of
phase information, and it is therefore called
_pure dephasing_ (time constant _T_ __ ). Unlike _T_ 1 relaxation, which is
generally an irreversible (incoherent) error, pure dephasing _T_ __ is in principle reversible (a coherent error). The
degree of pure dephasing depends on the control pulse
sequence applied while the qubit is subject to the noise
process.
Consider the relative phase __ of a superposition state
undergoing free evolution in the presence of noise. The
superposition states accumulated phase,


##### (a)


N -pulses ( N > 1) t

|Col1|Col2|CP / CPMG|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||2N N|N|N|N N 2N|


![qe-guide-scqubits-oliver.pdf-19-0.png](qe-guide-scqubits-oliver.pdf-19-0.png)

0          2          4          6          8
Frequency, f (MHz)

|Col1|Col2|
|---|---|
||Ramsey (N=0)|



1          10         100       1000
Number of  pulses, N


_t_
__ ( _t_ ) =

0




__ _q_ _dt_ __ = __ __ q __ _t_ + __ ( _t_ ) (55)


diffuses due to adiabatic fluctuations of the transition
frequency,


##### (b)

10



__ q
__ ( _t_ ) =

__


0





__ q
__ ( _t_ ) =


__ ( _t_ __ )d _t_ __ _,_ (56)


where __ q _/_ = (1 _/_  ) _|_ __ _H_  _q_ _/_ _|_
is the qubits longitudinal sensitivity to __ -noise. For noise generated by a
large number of fluctuators that are weakly coupled to
the qubit, its statistics are Gaussian. Ensemble averaging
over all realizations of the Gaussian-distributed stochastic process __ ( _t_ ), the dephasing is


_e_ _i _ ( _t_ ) = _e_ __ 1 2 __ __ 2 ( _t_ ) __ _e_ __ __ _N_ ( _t_ ) _,_ (57)
__ __ __

leading to a coherence decay function,


0.1


FIG. 7. Dynamical error suppression. **(a)**
Carr-PurcellMeiboom-Gill (CPMG) pulse sequence applies _N_ equally
spaced __ pulses within an otherwise free-evolution time __ .
Pulses in the time domain correspond to bandpass filters in
the frequency domain (lower panel) which serve to shape the
noise power spectrum seen by the qubit. The centroid of the
bandpass filter shifts to higher frequencies as _N_ is increased.
For noise that decreases with frequency, such as 1 _/f_ noise,
larger _N_ corresponds to less integrated noise impinging on
the qubit. **(b)** CPMG pulse sequence applied to a flux qubit
biased at a point that is highly sensitive to 1 _/f_ flux noise. The
Ramsey ( _N_ = 0) time is approximately 300 ns, and the Hahn
echo ( _N_ = 1) time is approximately 1 _._ 5 __ s. Increasing the
number of CPMG pulses continues to increase the effective
_T_ 2 time towards the 2 _T_ 1 limit. Adapted from Ref. 78.

2
4 _E_ _C_ ( _n_ _n_ _g_ ) , where we allow for an offset charge _n_ _g_ ,
__
and the susceptibility is given by 8 _E_ _C_ _n_  . We refer the
reader to Refs. 151153 for more details.

**_2._** **_Connecting_** _T_ __ **_to_** _S_ ( __ )

If the coupling to the qubit is instead longitudinal,
e.g. _H_  _q_ is of the type __ _z_ or _a_ __ _a_ , the noise will stochasti-


_e_ __ __ _N_ ( __ ) = exp __ 2
__ __ __ 2


__



__ q


__


_g_ _N_ ( _, _ ) _S_ ( __ ) _d_
__


(58)
where _g_ ( _, _ ) is a dimensionless weighting function.
The function _g_ _N_ ( _, _
) can be viewed as a frequencydomain filter of the noise _S_ __ ( __
) [see Fig. 7(a)]. In general, its filter properties depend on the number _N_ and
distribution of applied pulses. For example, considering

78,154158
sequences of __ -pulses ,



1+ _N_
1 + ( 1) exp( _i_ )+
__


 _j_


_g_ _N_ ( _, _ ) =



2
( __ )


2
( 1) _j_ exp( _i_ _j_ __ ) cos( __ __ _/_ 2) _,_ (59)
__
_j_ =1


where __ _j_ [0 _,_ 1] is the normalized position of the centre
of the _j_ th __ __ -pulse between the two _/_ 2-pulses, __ is the
total free-induction time, and __ __ is the length of each

157,158
__ -pulse , yielding a total sequence length __ + _N_ __ .
As the number of pulses increases for fixed __ , the filter
functions peak shifts to higher frequencies, leading to a
reduction in the net integrated noise for 1 _/f_ __ -type noise
spectra with _ >_ 0. Similarly, for a fixed _N_ , the filter


-----


21

during  periods of time for which no control is applied to the qubit, except for very short dynamical decoupling pulses  and during  periods of time during which the control fields are applied _free evolution_ _driven evolution_
to the qubit. Both free-evolution and driven-evolution
noise is important to characterize, as the noise PSD may
differ for these two types of evolution, and both are utilized in the context of universal quantum computation.
We refer the reader to Ref. 132 for a summary of noise
spectroscopy during both types of evolution.
The Ramsey frequency itself is sensitive to longitudinal
noise, and monitoring its fluctuations is one means to
map out the noise spectral density over the sub-millihertz
to 100 Hz range 131,163 .
__
At higher frequencies, the CPMG dynamical decoupling sequence can be used to create narrow-band filters that sample the noise at different frequencies as a
function of the free-evolution time __ and the number of
pulses _N_ . This has been used to map out the noise PSD
in the range 0.1 - 300 MHz 78 . One must be careful of
the additional small peaks at higher-frequencies, which
all contribute to the dephasing used to perform the noise
spectroscopy 164 .
In fact, using pulse envelopes such as Slepians 165 
which are designed to have concentrated frequency response  to perform noise spectroscopy is one means to
reduce such errors 157 .
At even higher frequencies, measurements of _T_ 1 can be
used in conjunction with Fermis golden rule to map out
the transverse noise spectrum above 1 GHz 62,78,166 .
The aforementioned are all examples of noise spectroscopy during free evolution. Noise spectroscopy during driven evolution was also demonstrated using a spinlocking technique, where a strong drive along _x_ or _y_
axes defines a new qubit quantization axis, whose Rabi
frequency is the new qubit frequency in the spin-locking
frame. The spin-locking frame is then used to infer the
noise spectrum while the qubit is continually subject to
a driving field. For more information, we refer the reader
to Ref. 132.

**E.** **Engineering noise mitigation**

Here, we briefly review a few examples of techniques
that have been developed to reduce noise or reduce its impact on decoherence (sensitivity). We stress that improving gate fidelity is a comprehensive optimization task, one
that is full of trade-offs. It is thus important to identify
what the limiting factors are, what price we have to pay
to diminish these limiting factors, and what advantage we
can achieve until reaching a better trade-off. These all
require an accurate understanding the limitations on the
gate fidelity, the sources of decoherence, the properties
of the noise, and how it affects the system performance.


function will shift in frequency with __ . Additionally, for a
fixed time separation __ __ = _/N_ (valid for _N_ __
1), the filter sharpens and asymptotically peaks at __ __ _/_ 2 __ = 1 _/_ 2 __ __

as more pulses are added. _g_ _N_ ( _, _
78,156
) is thus called the filter function , and it depends on the pulse sequences
being applied. From Eq. (58), the pure dephasing decay arises from a noise spectral density that is shaped
or filtered by the sequence-specific filter function. By
choosing the number of pulses, their rotation axes, and
their arrangement in time, we can design filter functions
that minimize the net noise power for a given noise spectral density within the experimental constraints of the experiment (e.g., pulse-modulation bandwidth of the electronics used to control the qubits).
To give a standard example, we compare the coherence
integral for two cases: a Ramsey pulse sequence and a
Hahn echo pulse sequence. Both sequences involve two
_/_ , during which free evolution of the qubit occurs in the presence of low-frequency 2 pulses separated by a time __
dephasing noise. The distinction is that the Hahn echo
will place a single __ pulse ( _N_ = 1) in the middle of the
free-evolution period, whereas the Ramsey does not use
any additional pulses ( = 0). The resulting filter functions are: _N_


function will shift in frequency with __ . Additionally, for a
fixed time separation __ __ = _/N_ (valid for _N_ __
1), the filter sharpens and asymptotically peaks at __ __ _/_ 2 __ = 1 _/_ 2 __ __



2 __
_g_ 0 ( _, _ ) = sinc



2 __ 2 __
_g_ 1 ( _, _ ) = sin sinc

4 4


(60)

(61)


where the subscript _N_ = 0 and _N_
= 1 indicate the number of __ -pulses applied for the Ramsey and Hahn echo
experiments, respectively. The filter function _g_ 0 ( _, _ ) for
the Ramsey case is a sinc-function centered at __ = 0. For
noise that decreases with frequency, e.g., 1 _/f_ flux noise
in superconducting qubits, the Ramsey experiment windows through the noise in _S_ ( __ ) where it has its highest
value. This is the worst choice of filter function for 1 _/f_
noise. In contrast, the Hahn echo filter function has a
centroid that is peaked at a higher frequency, away from
__ = 0. In fact, it has zero value at __ = 0. For noise
that decreases with frequency, such as 1 _/f_ noise, this is
advantageous. This concept extends to larger numbers
_N_ of __ pulses, and is called a Carr-Purcell-Meiboom-Gill

159,160
(CPMG) sequence . In Fig. 7(b), the _T_ 2 time of a
qubit under the influence of strong dephasing noise is increased toward the 2 _T_ 1 limit using a CPMG dynamical
error-suppression pulse sequence with an increasing number of pulses, _N_ . We refer the reader to Refs. 78, 161, and
162, where these experiments were performed with superconducting qubits.

**_3._** **_Noise spectroscopy_**

The qubit is highly sensitive to its noisy environment,
and this feature can be used to map out the noise power
spectral density. In general, one can map the noise PSD


-----


22

Returning to excess quasiparticles, it has been shown
that quasiparticles can be stochastically pumped away

122
from the qubit region, resulting in longer, and more stable _T_ 1 times . Although the pumping technique uses
a series of -pulses, this technique differs from dynamical error suppression of coherent errors in that pulses are __
stochastically applied, and that it addresses incoherent
errors ( _T_ 1 ).

**_4._** **_Cryogenic engineering_**

In the case of photon shot-noise, in addition to applying dynamical decoupling techniques, there have been
several recent works aimed at reducing the thermal photon flux that reaches the device. This include optimizing
the attenuation of the cryogenic setup , remaking the cryogenic attenuators with more efficient heat 107,149,173
sinking 148 , adding absorptive black material to absorb
stray thermal photons 174,175
176
, and adding additional cavity filters for thermalization .

**IV.** **QUBIT CONTROL**

In this section, we will introduce how superconducting qubits are manipulated to implement quantum algorithms. Since the transmon-like variety of superconducting qubits has so far been the most widely deployed
modality for implementing quantum programs, the discussion throughout this section will be focused on modern
techniques for transmons. Nonetheless, the techniques
introduced here are applicable to all types of superconducting qubits.
We start with a brief review of the gates used in classical computing as well as quantum computing, and the
concept of universality. Subsequently we discuss the most
common technique of driving single qubit gates via a
capacitive coupling of a microwave line, coupled to the
qubit. We introduce the notion of virtual Z gates and
DRAG pulsing. In the latter part of this section, we review some of the most common implementations of twoqubit gates in both tunable and fixed-frequeny transmon
qubits. The single-qubit and two-qubit operations together form the basis of many of the medium-scale superconducting quantum processors that exist today.
Throughout this section, we write everything in the
computational basis 0 _,_ 1 where 0
_{|_ __ _|_ _}_ _|_ __
is the +1 eigenstate of __ _z_ and 1 is the
_|_ __ __
1 eigenstate. We use capitalized serif-fonts to indicate the rotation operator of a
qubit state, e.g. rotations around the _x_ -axis by an angle
__ is written as


**_1._** **_Materials and fabrication improvements_**

Numerous efforts have been undertaken to reduce

40,167
noise-induced defects due to materials and fabrication . In the case of charge noise, significant efforts
have been made to reduce the number of defects, such
as substrate cleaning 59,168 , substrate annealing 169 , and
trenching 41,61 . In the case of flux noise, several groups
have performed experiments to characterize the behavior
and properties of magnetic-flux defects 137,170,171 . More
recently, a number of groups have tried optical surface
treatments to remove these defects 145 .
In the context of residual quasiparticles, it has been
shown that adding quasiparticle traps to the circuit design can reduce the quasiparticle number, particularly in
devices that create excess quasiparticles, such as classical digital logic or operation in the presence of thermal
radiation 172

**_2._** **_Design improvements_**

Another strategy is to reduce qubit sensitivity to the
noise by design. A qubit can only lose energy to defects
if it couples to them. It has been demonstrated that
altering the capacitor geometry to increase the electricfield mode volume reduces the electric field density in the
thin dielectric regions that cause loss. This effectively
reduces the participation of the defects and makes the
qubits less senstivie to these noise sources. 55,62,134 .
In another example, the split transmons built using
asymmetric junctions have lower sensitivity to flux noise

69
than their symmetric counterparts at the expense of decreased frequency tunability . This is a good trade-off
to make, because generally one is interested in tuning the
qubit frequency over a somewhat restricted range (typically around 1 GHz) about the qubit frequency. When
such asymmetric transmons are used in a gate scheme
such as the adiabatic CPHASE -gate 65 , (see Sec.IV F) the
qubit is less sensitive to flux noise, has a lower dephasing
rate, and this should improve the gate fidelity in general.

**_3._** **_Dynamical error suppression_**

As introduced in the previous section, it is advantageous to leverage the 1 _/_ distribution of flux noise,
wherein a considerable amount of the noise power resides at low frequencies, and so the noise is quasi-static.
The spin-echo technique 116
, which disrupts the free evolution by a __ -pulse, is extremely effective in mitigating
the pure dephasing by refocusing the coherent phase dispersion due to low-frequency noise. The more advanced
versions, such as the CPMG-sequence, use multiple __
pulses to interrupt the system more frequently, pushing
the filter band to even higher frequencies  a technique
known as _dynamical decoupling_ 78 .


X __ = _R_ _X_ ( __ ) = _e_ __ _i_ __ 2 __ _x_ = cos( _/_ 2) 1 _i_ sin( _/_ 2) __ _x_ (62)

__

and we use the shorthand notation  X  for a full __ rotation
about the _x_ axis (and similarly for Y := Y __ and Z := Z __ ).


-----


23

**A.** **Boolean logic gates used in classical computers**

Universal boolean logic can be implemented on classical computers using a small set of single-bit and two-bit
gates. Several common classical logic gates are shown in
Fig. 8 along with their truth tables. In classical boolean
logic, bits can take on one of two values: state 0 or state
, and state 1 represents logical 1. The state 0 represents logical TRUE . FALSE
Beyond the trivial identity operation, which simply
passes a boolean bit unchanged, the only other possible
single-bit boolean logic gate is the NOT gate. As shown
in Fig. 8, the NOT gate flips the bit: 0 1 and 1 0.
__ __
This gate is _reversible_ , because it is trivial to determine
the input bit value given the output bit values. As we
will see, for two-bit gates, this is not the case.
There are several two-bit gates shown in Fig. 8. A
two-bit gate takes two bits as inputs, and it passes as
an output the result of a boolean operation. One common example is the AND gate, for which the output is
1 if and only if both inputs are 1; otherwise, the output
is 0. The AND gate, and the other two-bit gates shown
in Fig. 8, are all examples of _irreversible_ gates; that is,
the input bit values cannot be inferred from the output
values. For example, for the gate, an output of logical 1 uniquely identifies the input 11, but an output of 0 AND
could be associated with 00, 01, or 10. Once the operation is performed, in general, it cannot be undone and
the input information is lost. There are several variants
of two-bit gates, including,

-  AND and OR ;

-  NAND (a combination of NOT and AND ) and NOR
(a combination of NOT and OR );

-  XOR (exclusive OR ) and NXOR ( NOT XOR ).

The XOR gate is interesting, because it is a _parity_ gate.
That is, it returns a logical 0 if the two inputs are the
same values (i.e., they have the same parity), and it returns a logical 1 if the two inputs have different values
(i.e., different parity). Still, the XOR and NXOR gates
are not reversible, because knowledge of the output does
not allow one to uniquely identify the input bit values.
refers to the ability to perform any boolean logic algorithm using a small set of The concept of _universality_
single-bit and two-bit gates. A universal gate set can in
principle transform any state to any other state in the
state space represented by the classical bits. The set of
gates which enable universal computation is not unique,
and may be represented by a small set of gates. For example, the NOT gate and the AND gate together form
a universal gate set. Similarly, the NAND gate itself is
universal, as is the NOR gate. The efficiency with which
one can implement arbitrary boolean logic, of course, depends on the choice of the gate set.

|GATE|CIRCUIT SYMBOL|TRUTH TABLE|
|---|---|---|
|NOT The output is 1 when the input is 0 and 0 when the input is 1.||Input Output 0 1 1 0|
|AND The output is 1 only when both inputs are 1, otherwise the output is 0.||Input Output 0 0 0 0 1 0 1 0 0 1 1 1|
|OR The output is 0 only when both inputs are 0, otherwise the output is 1.||Input Output 0 0 0 0 1 1 1 0 1 1 1 1|
|NAND The output is 0 only when both inputs are 1, otherwise the output is 1.||Input Output 0 0 1 0 1 1 1 0 1 1 1 0|
|NOR The output is 1 only when both inputs are 0, otherwise the output is 0.||Input Output 0 0 1 0 1 0 1 0 0 1 1 0|
|XOR The output is 1 only when the two inputs have diferent value, otherwise the output is 0.||Input Output 0 0 0 0 1 1 1 0 1 1 1 0|
|XNOR The output is 1 only when the two inputs have the same value, otherwise the output is 0.||Input Output 0 0 1 0 1 0 1 0 0 1 1 1|


FIG. 8. Classical single-bit and two-bit boolean logic gates.
For each gate, the name, a short description, circuit representation, and input/output truth tables are presented. The
numerical values in the truth table correspond to the classical
bit values 0 and 1. Adapted from Ref. 177.


-----


24

|GATE|CIRCUIT REPRESENTATION|MATRIX REPRESENTATION|TRUTH TABLE|BLOCH SPHERE|
|---|---|---|---|---|
|I Identity-gate: no rotation is performed.|I|( 1 0 ) I = 0 1|Input Output |0 |0 |1 |1|z y x|
|X gate: rotates the qubit state by  radians (180) about the x-axis.|X|( 0 1 ) X = 1 0|Input Output |0 |1 |1 |0|z 180 y x|
|Y gate: rotates the qubit state by  radians (180) about the y-axis.|Y|( 0  i) Y = i 0|Input Output |0 i |1 |1 i |0|z 180 y x|
|Z gate: rotates the qubit state by  radians (180) about the z-axis.|Z|( 1 0 ) Z = 0 1|Input Output |0 |0 |1 |1|z 180 y x|
|S gate: rotates the qubit state by  2 radians (90) about the z-axis.|S|(1 0 ) S = ei 0 2|Input Output |0 |0 |1 e i 2 |1|z 90 y x|
|T gate: rotates the qubit state by  4 radians (45) about the z-axis.|T|(1 0 ) T = ei 0 4|Input Output |0 |0 |1 e i  4 |1|z 45 y x|
|H gate: rotates the qubit state by  radians (180) about an axis diagonal in the x-z plane. This is equivalent to an X-gate followed by a  rotation 2 about the y-axis.|H|1 ( 1 1 ) H = 2 1 1|Input Output |0 |0 + |1 2 |1 |0  |1 2|z 180 y x|


![qe-guide-scqubits-oliver.pdf-23-55.png](qe-guide-scqubits-oliver.pdf-23-55.png)

![qe-guide-scqubits-oliver.pdf-23-56.png](qe-guide-scqubits-oliver.pdf-23-56.png)

![qe-guide-scqubits-oliver.pdf-23-54.png](qe-guide-scqubits-oliver.pdf-23-54.png)

![qe-guide-scqubits-oliver.pdf-23-53.png](qe-guide-scqubits-oliver.pdf-23-53.png)

![qe-guide-scqubits-oliver.pdf-23-52.png](qe-guide-scqubits-oliver.pdf-23-52.png)

![qe-guide-scqubits-oliver.pdf-23-51.png](qe-guide-scqubits-oliver.pdf-23-51.png)

![qe-guide-scqubits-oliver.pdf-23-50.png](qe-guide-scqubits-oliver.pdf-23-50.png)

![qe-guide-scqubits-oliver.pdf-23-48.png](qe-guide-scqubits-oliver.pdf-23-48.png)

![qe-guide-scqubits-oliver.pdf-23-49.png](qe-guide-scqubits-oliver.pdf-23-49.png)

![qe-guide-scqubits-oliver.pdf-23-46.png](qe-guide-scqubits-oliver.pdf-23-46.png)

![qe-guide-scqubits-oliver.pdf-23-47.png](qe-guide-scqubits-oliver.pdf-23-47.png)

![qe-guide-scqubits-oliver.pdf-23-45.png](qe-guide-scqubits-oliver.pdf-23-45.png)

![qe-guide-scqubits-oliver.pdf-23-44.png](qe-guide-scqubits-oliver.pdf-23-44.png)

![qe-guide-scqubits-oliver.pdf-23-43.png](qe-guide-scqubits-oliver.pdf-23-43.png)

![qe-guide-scqubits-oliver.pdf-23-42.png](qe-guide-scqubits-oliver.pdf-23-42.png)

![qe-guide-scqubits-oliver.pdf-23-97.png](qe-guide-scqubits-oliver.pdf-23-97.png)

![qe-guide-scqubits-oliver.pdf-23-98.png](qe-guide-scqubits-oliver.pdf-23-98.png)

![qe-guide-scqubits-oliver.pdf-23-96.png](qe-guide-scqubits-oliver.pdf-23-96.png)

![qe-guide-scqubits-oliver.pdf-23-95.png](qe-guide-scqubits-oliver.pdf-23-95.png)

![qe-guide-scqubits-oliver.pdf-23-94.png](qe-guide-scqubits-oliver.pdf-23-94.png)

![qe-guide-scqubits-oliver.pdf-23-93.png](qe-guide-scqubits-oliver.pdf-23-93.png)

![qe-guide-scqubits-oliver.pdf-23-91.png](qe-guide-scqubits-oliver.pdf-23-91.png)

![qe-guide-scqubits-oliver.pdf-23-92.png](qe-guide-scqubits-oliver.pdf-23-92.png)

![qe-guide-scqubits-oliver.pdf-23-90.png](qe-guide-scqubits-oliver.pdf-23-90.png)

![qe-guide-scqubits-oliver.pdf-23-89.png](qe-guide-scqubits-oliver.pdf-23-89.png)

![qe-guide-scqubits-oliver.pdf-23-88.png](qe-guide-scqubits-oliver.pdf-23-88.png)

![qe-guide-scqubits-oliver.pdf-23-87.png](qe-guide-scqubits-oliver.pdf-23-87.png)

![qe-guide-scqubits-oliver.pdf-23-86.png](qe-guide-scqubits-oliver.pdf-23-86.png)

![qe-guide-scqubits-oliver.pdf-23-85.png](qe-guide-scqubits-oliver.pdf-23-85.png)

![qe-guide-scqubits-oliver.pdf-23-83.png](qe-guide-scqubits-oliver.pdf-23-83.png)

![qe-guide-scqubits-oliver.pdf-23-84.png](qe-guide-scqubits-oliver.pdf-23-84.png)

![qe-guide-scqubits-oliver.pdf-23-82.png](qe-guide-scqubits-oliver.pdf-23-82.png)

![qe-guide-scqubits-oliver.pdf-23-81.png](qe-guide-scqubits-oliver.pdf-23-81.png)

![qe-guide-scqubits-oliver.pdf-23-80.png](qe-guide-scqubits-oliver.pdf-23-80.png)

![qe-guide-scqubits-oliver.pdf-23-79.png](qe-guide-scqubits-oliver.pdf-23-79.png)

![qe-guide-scqubits-oliver.pdf-23-77.png](qe-guide-scqubits-oliver.pdf-23-77.png)

![qe-guide-scqubits-oliver.pdf-23-78.png](qe-guide-scqubits-oliver.pdf-23-78.png)

![qe-guide-scqubits-oliver.pdf-23-76.png](qe-guide-scqubits-oliver.pdf-23-76.png)

![qe-guide-scqubits-oliver.pdf-23-75.png](qe-guide-scqubits-oliver.pdf-23-75.png)

![qe-guide-scqubits-oliver.pdf-23-74.png](qe-guide-scqubits-oliver.pdf-23-74.png)

![qe-guide-scqubits-oliver.pdf-23-73.png](qe-guide-scqubits-oliver.pdf-23-73.png)

![qe-guide-scqubits-oliver.pdf-23-72.png](qe-guide-scqubits-oliver.pdf-23-72.png)

![qe-guide-scqubits-oliver.pdf-23-71.png](qe-guide-scqubits-oliver.pdf-23-71.png)

![qe-guide-scqubits-oliver.pdf-23-69.png](qe-guide-scqubits-oliver.pdf-23-69.png)

![qe-guide-scqubits-oliver.pdf-23-70.png](qe-guide-scqubits-oliver.pdf-23-70.png)

![qe-guide-scqubits-oliver.pdf-23-68.png](qe-guide-scqubits-oliver.pdf-23-68.png)

![qe-guide-scqubits-oliver.pdf-23-67.png](qe-guide-scqubits-oliver.pdf-23-67.png)

![qe-guide-scqubits-oliver.pdf-23-66.png](qe-guide-scqubits-oliver.pdf-23-66.png)

![qe-guide-scqubits-oliver.pdf-23-65.png](qe-guide-scqubits-oliver.pdf-23-65.png)

![qe-guide-scqubits-oliver.pdf-23-64.png](qe-guide-scqubits-oliver.pdf-23-64.png)

![qe-guide-scqubits-oliver.pdf-23-62.png](qe-guide-scqubits-oliver.pdf-23-62.png)

![qe-guide-scqubits-oliver.pdf-23-63.png](qe-guide-scqubits-oliver.pdf-23-63.png)

![qe-guide-scqubits-oliver.pdf-23-60.png](qe-guide-scqubits-oliver.pdf-23-60.png)

![qe-guide-scqubits-oliver.pdf-23-61.png](qe-guide-scqubits-oliver.pdf-23-61.png)

![qe-guide-scqubits-oliver.pdf-23-59.png](qe-guide-scqubits-oliver.pdf-23-59.png)

![qe-guide-scqubits-oliver.pdf-23-58.png](qe-guide-scqubits-oliver.pdf-23-58.png)

![qe-guide-scqubits-oliver.pdf-23-57.png](qe-guide-scqubits-oliver.pdf-23-57.png)

![qe-guide-scqubits-oliver.pdf-23-12.png](qe-guide-scqubits-oliver.pdf-23-12.png)

![qe-guide-scqubits-oliver.pdf-23-13.png](qe-guide-scqubits-oliver.pdf-23-13.png)

![qe-guide-scqubits-oliver.pdf-23-11.png](qe-guide-scqubits-oliver.pdf-23-11.png)

![qe-guide-scqubits-oliver.pdf-23-10.png](qe-guide-scqubits-oliver.pdf-23-10.png)

![qe-guide-scqubits-oliver.pdf-23-9.png](qe-guide-scqubits-oliver.pdf-23-9.png)

![qe-guide-scqubits-oliver.pdf-23-8.png](qe-guide-scqubits-oliver.pdf-23-8.png)

![qe-guide-scqubits-oliver.pdf-23-7.png](qe-guide-scqubits-oliver.pdf-23-7.png)

![qe-guide-scqubits-oliver.pdf-23-6.png](qe-guide-scqubits-oliver.pdf-23-6.png)

![qe-guide-scqubits-oliver.pdf-23-4.png](qe-guide-scqubits-oliver.pdf-23-4.png)

![qe-guide-scqubits-oliver.pdf-23-5.png](qe-guide-scqubits-oliver.pdf-23-5.png)

![qe-guide-scqubits-oliver.pdf-23-3.png](qe-guide-scqubits-oliver.pdf-23-3.png)

![qe-guide-scqubits-oliver.pdf-23-2.png](qe-guide-scqubits-oliver.pdf-23-2.png)

![qe-guide-scqubits-oliver.pdf-23-1.png](qe-guide-scqubits-oliver.pdf-23-1.png)

![qe-guide-scqubits-oliver.pdf-23-0.png](qe-guide-scqubits-oliver.pdf-23-0.png)

![qe-guide-scqubits-oliver.pdf-23-26.png](qe-guide-scqubits-oliver.pdf-23-26.png)

![qe-guide-scqubits-oliver.pdf-23-27.png](qe-guide-scqubits-oliver.pdf-23-27.png)

![qe-guide-scqubits-oliver.pdf-23-25.png](qe-guide-scqubits-oliver.pdf-23-25.png)

![qe-guide-scqubits-oliver.pdf-23-24.png](qe-guide-scqubits-oliver.pdf-23-24.png)

![qe-guide-scqubits-oliver.pdf-23-23.png](qe-guide-scqubits-oliver.pdf-23-23.png)

![qe-guide-scqubits-oliver.pdf-23-22.png](qe-guide-scqubits-oliver.pdf-23-22.png)

![qe-guide-scqubits-oliver.pdf-23-20.png](qe-guide-scqubits-oliver.pdf-23-20.png)

![qe-guide-scqubits-oliver.pdf-23-21.png](qe-guide-scqubits-oliver.pdf-23-21.png)

![qe-guide-scqubits-oliver.pdf-23-19.png](qe-guide-scqubits-oliver.pdf-23-19.png)

![qe-guide-scqubits-oliver.pdf-23-18.png](qe-guide-scqubits-oliver.pdf-23-18.png)

![qe-guide-scqubits-oliver.pdf-23-17.png](qe-guide-scqubits-oliver.pdf-23-17.png)

![qe-guide-scqubits-oliver.pdf-23-16.png](qe-guide-scqubits-oliver.pdf-23-16.png)

![qe-guide-scqubits-oliver.pdf-23-15.png](qe-guide-scqubits-oliver.pdf-23-15.png)

![qe-guide-scqubits-oliver.pdf-23-14.png](qe-guide-scqubits-oliver.pdf-23-14.png)

![qe-guide-scqubits-oliver.pdf-23-40.png](qe-guide-scqubits-oliver.pdf-23-40.png)

![qe-guide-scqubits-oliver.pdf-23-41.png](qe-guide-scqubits-oliver.pdf-23-41.png)

![qe-guide-scqubits-oliver.pdf-23-39.png](qe-guide-scqubits-oliver.pdf-23-39.png)

![qe-guide-scqubits-oliver.pdf-23-38.png](qe-guide-scqubits-oliver.pdf-23-38.png)

![qe-guide-scqubits-oliver.pdf-23-37.png](qe-guide-scqubits-oliver.pdf-23-37.png)

![qe-guide-scqubits-oliver.pdf-23-36.png](qe-guide-scqubits-oliver.pdf-23-36.png)

![qe-guide-scqubits-oliver.pdf-23-35.png](qe-guide-scqubits-oliver.pdf-23-35.png)

![qe-guide-scqubits-oliver.pdf-23-34.png](qe-guide-scqubits-oliver.pdf-23-34.png)

![qe-guide-scqubits-oliver.pdf-23-32.png](qe-guide-scqubits-oliver.pdf-23-32.png)

![qe-guide-scqubits-oliver.pdf-23-33.png](qe-guide-scqubits-oliver.pdf-23-33.png)

![qe-guide-scqubits-oliver.pdf-23-31.png](qe-guide-scqubits-oliver.pdf-23-31.png)

![qe-guide-scqubits-oliver.pdf-23-30.png](qe-guide-scqubits-oliver.pdf-23-30.png)

![qe-guide-scqubits-oliver.pdf-23-29.png](qe-guide-scqubits-oliver.pdf-23-29.png)

![qe-guide-scqubits-oliver.pdf-23-28.png](qe-guide-scqubits-oliver.pdf-23-28.png)

FIG. 9. Quantum single-qubit gates. For each gate, the name, a short description, circuit representation, matrix representation,
input/output truth tables, and Bloch sphere represenation are presented. Matrices are defined in the basis spanned by the
state vectors 0 [1 0] _T_ and 1 [0 1] _T_ . The numerical values in the truth table correspond to the quantum states 0 and
_|_ __ _|_ __ _|_ __
1 . Adapted from Ref. 177.
_|_ __


**B.** **Quantum logic gates used in quantum computers**


course assume the classical states 0 and 1 , at the north
_|_ __ _|_ __


Quantum logic can similarly be performed by a small
set of single-qubit and two-qubit gates. Qubits can of


-----


25

|GATE|CIRCUIT REPRESENTATION|MATRIX REPRESENTATION|TRUTH TABLE|
|---|---|---|---|
|Controlled-NOT gate: apply an X-gate to the target qubit if the control qubit is in state |1 Controlled-phase gate: apply a Z-gate to the target qubit if the control qubit is in state |1|Z|1 0 0 0 0 1 0 0 CNOT = 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 CPHASE = 0 0 1 0 0 0 0 1|Input Output |00 |00 |01 |01 |10 |11 |11 |10 Input Output |00 |00 |01 |01 |10 |10 |11 |11|



FIG. 10. Quantum two-qubit gates: the controlled NOT ( CNOT ) gate and the controlled phase ( CPHASE or CZ ). For each
gate, the name, a short description, circuit representation, matrix representation, and input/output truth tables are presented.
Matrices are defined in the basis spanned by the two-qubit state vectors 00 [1 0 0 0] _T_ , 01 [0 1 0 0] _T_ , 10 [0 0 1 0] _T_ ,

_T_ _|_ __ _|_ __ _|_ __
and 11 [0 0 0 1] , where the first qubit is the _control_ qubit, and the second qubit is the _target_ qubit. The CNOT gate flips
_|_ __
the state of the target qubit conditioned on the control qubit being in state 1 . The CPHASE gate applies a Z gate to the
_|_ __
target qubit conditioned on the control qubit being in state 1 . Adapted from Ref. 177.
_|_ __


pole and south pole of the Bloch sphere, but they can also
assume arbitrary superpositions __ 0 + __ 1
_|_ __ _|_ __
, corresponding to any other position on the sphere.


can be built from the CNOT -gate and single-qubit gates.


Single-qubit operations translate an arbitrary quantum state from one point on the Bloch sphere to another
point by rotating the Bloch vector (spin) a certain angle about a particular axis. As shown in Fig. 9, there
are several single-qubit operations, each represented by
a matrix that describes the quantum operation in the
computational basis represented by the eigenvectors of
the __ _z_ operator, i.e. 0 [1 0] _T_ and 1 [0 1] _T_ .
_|_ __ _|_ __

For example, the _identity gate_ performs no rotation on
the state of the qubit. This is represented by a two-bytwo identity matrix. The X -gate performs a __ rotation
about the _x_ axis. Similarly, the Y -gate and Z
-gate perform a __ rotation about the _y_ axis and _z_
axis, respectively. The S -gate performs a _/_ 2 rotation about the _z_
axis, and the T-gate performs a rotation of _/_ 4 about
the _z_ axis. The Hadamard gate H is also a common
single-qubit gate the performs a __ rotation about an axis
diagonal in the _x_ - _z_ plane, see Fig. 9.

_conditional_ Two-qubit quantum-logic gates are generally gates and take two qubits as inputs. Typically,
the first qubit is the _control_ qubit, and the second is the
_target_ qubit. A unitary operator is applied to the target
qubit, dependent on the state of the control qubit. The
two common examples shown in Fig. 10 are the controlled
NOT ( CNOT -gate) and controlled phase ( CZ or CPHASE
gate). The CNOT -gate flips the state of the target qubit
conditioned on the control qubit being in state 1 . The
_|_ __
gate to the target qubit, conditioned on the control qubit being in state CPHASE -gate applies a Z 1 . As we will
_|_ __
shown later, the _i_ SWAP gate  another two-qubit gate 


-----


26

Quantum X gate


The unitary operator of the CNOT gate can be written
in a useful way, highlighting that it applies an depending on the state of the control qubit. X


(a) (b)

Classical NOT gate


(a) (b)


1 0 0 0
0 1 0 0
0 0 0 1
0 0 1 0


![qe-guide-scqubits-oliver.pdf-25-0.png](qe-guide-scqubits-oliver.pdf-25-0.png)

_U_ CNOT =


= 0 0 1 + 1 1 X (63)
_|_ __ _| _ _|_ __ _| _




![qe-guide-scqubits-oliver.pdf-25-1.png](qe-guide-scqubits-oliver.pdf-25-1.png)

![qe-guide-scqubits-oliver.pdf-25-2.png](qe-guide-scqubits-oliver.pdf-25-2.png)

and similarly for the CPHASE gate,


FIG. 11. Comparison of the classical inverter ( NOT ) gate
and quantum bit flip ( X ) gate. **(a)** The classical NOT gate
that inverts the state of a classical bit. **(b)** The quantum X
gate, which flips the amplitudes of the two components of a
quantum bit.

A universal set of single-qubit and two-qubit gates is
sufficient to implement arbitrary quantum logic. This
means that this gate set can in principle reach _any_ state
in the multi-qubit state-space. How efficiently this is
done depends on the choice of quantum gates that comprise the gate set. We also note that each of the singlequbit and two-qubit gates is _reversible_ , that is, given the
output state, one can uniquely determine the input state.
As we discuss further, this distinction between classical
and quantum gates arises, because quantum gates are
based on _unitary_ operations _U_ . If a unitary operation _U_
is a particular gate applied to a qubit, then its hermitian
conjugate _U_ __ can be applied to recover the original state,
since _U_ __ _U_ = _I_ resolves an identity operation.

**C.** **Comparing classical and quantum gates**

The gate-sequences used to represent quantum algorithms have certain similarities to those used in classical computing, with a few striking differences. As an
example, we consider first the classical gate (discussed previously), and the related quantum circuit version, shown in Fig. 11. NOT
While the classic bit-flip gate inverts any input state,
the quantum bit-flip does not in general produce the antipodal state (when viewed on the Bloch sphere), but
rather exchange the prefactors of the wavefunction written in the computational basis. The operator is sometimes referred to as the quantum NOT (or quantum X
bit-flip), but we note that X only acts similar to the
classical NOT gate in the case of classical data stored in
the quantum bit, i.e. X _g_ = _g_  for _g_ 0 _,_ 1 .
_|_ __ _|_ __ _{_ _}_
As briefly mentioned in Sec. IV B, _all_ quantum gates
are _reversible_ , due to the underlying unitary nature of
the operators implementing the logical operations. Certain other processes used in quantum information processing, however, are irreversible. Namely, measurements
(see Sec. V for detailed discussion) and energy loss to the
the environment (if the resulting state of the environment
is not known). Here, we will not consider how these processes are modeled, but refer the interested reader to e.g.
Ref. 178, and will only consider unitary control oper-


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
__


= 0 0 1 + 1 1 Z (64)
_|_ __ _| _ _|_ __ _| _




_U_ CPHASE =


Comparing the last equality above with the unitary for
the CNOT [Eq. (63)], it is clear that the two gates are
closely related. Indeed, a CNOT can be generated from
a CPHASE by applying two Hadamard gates,


_U_ CNOT = ( 1 H ) _U_ CPHASE ( 1 H ) _,_ (65)
__ __

since HZH = X . Due to the form of Eq. (64), the CPHASE
gate is also denoted the gate, since it applies a controlled Z operator, by analogy with CZ CNOT (a controlled
application of X operator). Inspection of the definition of
CPHASE in Fig. 10 makes no distinction between which
qubit acts as the target and which as the control and,
consequently, the circuit-diagram is sometimes drawn in
a symmetric fashion


CPHASE = __


(66)

||Col2|
|---|---|


The CNOT in terms of CPHASE can then be realized as


CNOT =


(67)


||Col2|Col3|Col4|Col5|
|---|---|---|---|---|
| H  H|||||
||H||H||
||||||


Some two-qubit gates such as CNOT and CPHASE are
, because they can take product states as inputs and output entangled states. They also called _entangling gates_
are thus an indispensable component of a universal gate
set for quantum logic. For example, consider two qubits
_A_ and _B_ in the following state:


__ =
_|_ __



( 0 + 1 ) _A_ 0 _B_ _._ (68)
2 _|_ __ _|_ __ _|_ __


If we perform a CNOT gate, _U_ CNOT , on this state, with
qubit A the control qubit, and qubit B the target qubit,
the resulting state is (see the truth table in Fig. 10):


_U_ CNOT _|_ __ __ =



( 0 _A_ 0 _B_ + 1 _A_ 1 _B_ ) = ( _. . ._ ) _A_ ( _. . ._ ) _B_ _,_
2 _|_ __ _|_ __ _|_ __ _|_ __ __


(69)
which is a state that cannot be factored into an isolated
qubit-A component and a qubit-B component. This is
one of the two-qubit entangled _Bell states_ , a manifestly
quantum mechanical state.


-----


27

as possible, and one wants to use as many of the native
gates as possible, to reduce the amount of time spent synthesising. Moreover, running a quantum algorithm also
depends on the qubit connectivity of the device. The
process of designing a quantum gate sequence that efficiently implements a specific algorithm, while taking into
account the considerations outlined above is known as
_gate synthesis_ and _gate compilation_ , respectively. A full
discussion of this large research effort is outside the scope
of this review, but the interested reader may consult e.g.
Refs. 183185 and references therein as a starting point.
As a concrete (and trivial) example of how gate identities
can be used, in Eq. (74) we illustrate how the Hadamard
gate from 1 can be generated by two single-qubit gates
_G_
(from _G_ 0 ) and an overall phase gate,


ations throughout the rest of this section. Finally, we
note that quantum circuits are written left-to-right (in
order of application), while the calculation of the result
of a gate-sequences, e.g the circuit

_|_ __ in __ _U_ 0 _U_ 1 _  _ _U_ _n_ _|_ __ out __ (70)

|Col1|U 0|Col3|U 1|Col5|
|---|---|---|---|---|
||||||


|Col1|U n|Col3|
|---|---|---|
||||


is performed right-to-left, i.e.


_|_ __ out __ = _U_ _n_ _  _ _U_ 1 _U_ 0 _|_ __ in __ _._ (71)

As discussed in Sec. IV A, the NOR and NAND gates are
each individually universal gates for classical computing.
Since both of these gates have no direct quantum analogue (because they are not reversible), it is natural to
needed to build a universal quantum computer. ask which gates _are_ It turns out that the ability to rotate
about arbitrary axes on the Bloch-sphere (i.e. a complete
single-qubit gate set), supplemented with any entangling
2-qubit operation will suffice for universality 178,179 . By
using what is known as the Krauss-Cirac decomposition,
any two-qubit gate can be decomposed into a series of
CNOT operations 178,180 .

**_1._** **_Gate sets and gate synthesis_**

A common universal quantum gate set is

0 = X __ _,_ Y __ _,_ Z __ _,_ Ph __ _,_ CNOT (72)
_G_ _{_ _}_

where Ph __ = _e_ _i_ 1 applies an overall phase __ to a single
qubit. For completeness we mention another universal
gate set which is of particular interest from a theoretical
perspective, namely

1 = H _,_ S _,_ T _,_ CNOT _,_ (73)
_G_ _{_ _}_


2 Z __ = _i_ 1
__


1 1 _i_ 0
__ __
1 1 0 _i_




H = Ph __



__ 2 Y __ 2


1 1
__

(74)


1 1
__


As a technical aside, we mention that the restriction to
a discrete gate set still gives rise to universality. This
fact relies on using the so-called Solovay-Kitaev 181,182

theorem, which (roughly) states that any other singlequbit gate can be approximated to an error __ using only
_O_ (log _c_ (1 _/_ )) (where _c >_ 0) single-qubit gates from _G_ 1 .
The gate-set 1 is typically referred to as the Clifford +
_G_
_T_  set, where H , S and CNOT are all Clifford gates.
Each quantum computing architecture will have certain gates that are simpler to implement at the hardware level than others (sometimes referred to as native gates of the architecture). These are typically the
gates for which the Hamiltonian governing the gateimplementation gives rise to a unitary propagator that
corresponds to the gate itself. We will show several examples of this in Sections IV E, IV F, and IV G. Regardless
of which gates are natively available, as long as one has a
complete gate set, one can use the Solovay-Kitaev theorem to synthesize any other set efficiently. In general one
wants to keep the overall number of time steps in which
gates are applied (denoted the _depth_ of a circuit) as low


As we show in Sec. IV D 1, the gates X __ , Y __ and Z __
are all natively available in a superconducting quantum
processor.
We now address the question of how single qubit rotations and two-qubit operations are implemented in
transmon-based superconducting quantum processors.

**_2._** **_Addressing superconducting qubits_**

The modes of addressing transmon-like superconducting qubits can roughly be split into two main categories:
_i_ ) Capacitive coupling between a resonator (or a feedline)
and the superconducting qubit dipole-field allows for microwave control to implement single-qubit rotations (see
Sec. IV D) as well as certain two-qubit gates (see Sections IV G and IV G 4). _ii_ ) For flux-tunable qubits, local
magnetic fields can be used to tune the frequency of individual qubits. This allows the implementation of _z_ -axis
single-qubit rotation as well as multiple two-qubit gates
(see Sections IV E, IV F and IV H).

**D.** **Single-qubit gates**

In this section we will review the steps necessary to
demonstrate that capacitive coupling of microwaves to a
superconducting circuit can be used to drive single-qubit
gates. To this end we consider coupling a superconducting qubit to a microwave source (sometimes referred to
as a qubit drive) as shown in Fig. 12(a). A full circuit
analysis of the circuit in Fig. 12(a) is beyond the scope
of this review, so here we settle for highlighting the steps
that elucidate the physics of the qubit/drive coupling.
The interested reader may consult a number of lectures
notes and pertinent theses (e.g. Refs. 44, 163, 186188).
Here we follow Ref. 163.


-----


28


To elucidate the role of the drive, we move into a frame
rotating with the qubit at frequency __ q (also denoted
the rotating frame or the the interaction frame). To
see the usefulness of this rotating frame, consider a state

_T_
_|_ __ 0 __ = (1 1) _/_ __ 2. By the time-dependent Schr odinger

equation this state evolves according to


_V_ _d_ ( _t_ ) _R_ _w_ _C_ _d_

|Col1|Col2|Col3|
|---|---|---|



_C_

room

![qe-guide-scqubits-oliver.pdf-27-0.png](qe-guide-scqubits-oliver.pdf-27-0.png)

temperature wiring on-chip

FIG. 12. Circuit diagram of capacitive coupling of a microwave drive line (characterized by a time-dependent voltage
_V_ _d_ ( _t_ )) to a generic transmon-like superconducting qubit.

**_1._** **_Capacitive coupling for X,Y control_**

We start by modeling the qubit as an harmonic oscillator, for which the (classical) circuit Hamiltonian can
be calculated by circuit quantization techniques, starting
from Kirchoffs laws, and is given by 163


__ 0 ( _t_ ) = _U_ _H_ 0 __ 0 =
_|_ __ _|_ __


_e_ _i_ q _t/_ 2

_e_ __ _i_ q _t/_ 2


(80)


where _U_ _H_ 0 is the propagator corresponding to _H_ 0 . By
calculating e.g. __ __ 0 _|_ __ _x_ _|_ __ 0 __ = cos( __ q _t_ ) it is evident
that the phase is winding with a frequency of __ q due
to the __ _z_ term. By going into a frame rotating with
the qubit at frequency __ q , the action of the drive can
be more clearly appreciated. To this end we define
_U_ rf = _e_ _iH_ 0 _t_ = _U_ _H_ __ 0 and the new state in the rotating
frame is _|_ __ rf ( _t_ ) __ = _U_ rf _|_ __ 0 __ . The time-evolution in this
new frame is again found from the Schr odinger equation
(using the shorthand __ _t_ = _/t_ ),


_Q_  ( _t_ ) 2
_H_ =


_i_ _t_ __ rf ( _t_ ) = _i_ ( __ _t_ _U_ rf ) __ 0 + _iU_ rf ( __ _t_ __ 0 ) (81)
_|_ __ _|_ __ _|_ __


 ( _t_ ) 2 + 

2 _C_  2



+ _C_ d
2 _L_ _C_



d _V_ d ( _t_ ) _Q,_  (75)

_C_ 


= _i_ _U_  rf _U_ rf __ _|_ __ rf __ + _U_ rf _H_ 0 _|_ __ 0 __ (82)


_i_ _U_  rf _U_ rf __ + _U_ rf _H_ 0 _U_ rf __


where _C_  = _C_ + _C_ d is the total capacitance to ground
and _Q_  = _C_    __ _C_ d _V_ d ( _t_
) is a renormalized charge variable for the circuit. We can now promote the flux and
charge variables to quantum operators and assume weak
coupling to the drive-line, so that _Q_  _Q_  , and arrive at
__


_|_ __ rf __ (83)


_H_



We can think of the term _H_ 0 in the parentheses in
Eq. (83) as the form of _H_ 0
in the rotating frame. Simple insertion shows that _H_ 0 
= 0 as expected (the rotating frame should take care of the time-dependence).
However, one could also think of the term in brackets

in Eq. (83) as a prescription for calculating the form of
any Hamiltonian in the rotating frame given by _U_ rf , by
replacing _H_ 0 with some other _H_ . In general, we will not
find _H_ = 0.
Returning to Eq. (79), the form of _H_ d in the rotating
frame is found to be 



_C_ d
_H_ = _H_ LC +



_C_ d _V_ d ( _t_ ) _Q,_  (76)

_C_ 


where _H_ LC = _Q_  2 _/_ (2 _C_ ) +   2 _/_ (2 _L_ ) and we have kept
only terms that couple to the dynamic variables. Similar
to the momentum operator for a harmonic oscillator in
( _x, p_ )space, we can express the charge variable in terms
of raising and lowering operators, as done in Sec. II


_Q_  = __ _iQ_ zpf _a_ __ _a_ __ (77)

2 _Z_ is the zero-point charge fluctations  


where _Q_ zpf =  _/_ 2 _Z_ is the zero-point charge fluctations

and _Z_ = _L/C_ is the impedance of the circuit to ground.


where _Q_ zpf =


_H_ d =  _V_ d ( _t_ ) (cos( __ q _t_ ) __ _y_ sin( __ q _t_ ) __ _x_ ) _._ (84)
__

We can in general assume that the time-dependent part



of the voltage ( _V_ d ( _t_ ) = _V_ 0 _v_ ( _t_ )) has the generic form


_H_ d =  _V_ d ( _t_ ) (cos( __ q _t_ ) __ _y_ sin( __ q _t_ ) __ _x_ ) _._ (84)
__


and _Z_ = _L/C_ is the impedance of the circuit to ground.

Thus, the _LC_ oscillator capacitively coupled to a drive



line can be written as,



1
_H_ = __ _a_ __ _a_ +



_C_ d

_V_ _d_ ( _t_ ) _iQ_ zpf _a_ _a_ __ _._ (78)
_C_  __
 



_C_
__ _C_


_v_ ( _t_ ) = _s_ ( _t_ ) sin( __ d _t_ + __ ) (85)
= _s_ ( _t_ ) (cos( __ ) sin( __ d _t_ ) + sin( __ ) cos( __ d _t_ )) _,_ (86)

where _s_ ( _t_ ) is a dimensionless envelope function, so that
the amplitude of the drive is set by _V_ 0 _s_ ( _t_ ). Adopting the
definitions

_I_ = cos( __ ) (the in-phase component) (87)
_Q_ = sin( __ ) (the out-of-phase component) (88)

_H_ 0 = (( _E_ 0 + _E_ 1 ) _/_ 2) 1 __ (( _E_ 1 __ _E_ 0 ) _/_ 2) __ _z_ . In the main text we
have ignored the constant offset term.


+
Finally, by truncating to the lowest transition of the oscillator we can make the replacement _a_ __ __ __ and _a_ __ __ __


throughout and arrive at



__ q
_H_ =
__ 2


+  _V_ d ( _t_ ) __ _y_

_H_ d

__ q  = (  _E_ 1 


(79)




where = ( _C_ d _/C_  ) _Q_ zpf and __ q = ( _E_ 1 _E_ 0 ) _/_  .
__



__ _z_

__ 2

_H_ 0
 zpf and



Starting from a generic qubit Hamiltonian, _H_ 0 = _E_ 0 _|_ 0 __ 0 _|_ +
_E_ 1 _|_ 1 __ 1 _|_ , we can rewrite in terms of Pauli matrices, and get


-----


29

(a) (b)

LO AWG


the driving Hamiltonian in the rotating frame takes the
form

_H_ d =  _V_ 0 _s_ ( _t_ ) ( _I_ sin( __ d _t_ ) _Q_ cos( __ d _t_ ))
__
 __ (cos( __ q _t_ ) __ _y_ __ sin( __ q _t_ ) __ _x_ ) (89)

Performing the multiplication and dropping fast rotating
terms that will average to zero (i.e. terms with __ q + __ _d_ ),
known as the rotating wave approximation (RWA), we
are left with


pulses

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||

|Col1|WG|Col3|Col4|
|---|---|---|---|
||Q||b|
|||||


_s_ ( _t_



(c)




1
_H_ d =  _V_ 0 _s_ ( _t_ ) ( _I_ cos( _t_ ) + _Q_ sin( _t_ )) __ _x_

2 __




+ ( _I_ sin( _t_ ) _Q_ cos( _t_ )) __ _y_
__



|I Q LO RF|Col2|Col3|
|---|---|---|
||||
|||= d|


(90)


_V_ d ( _t_ )

_s_ ( _t_ )

__ d = __ LO _+_ AWG

to qubits


![qe-guide-scqubits-oliver.pdf-28-0.png](qe-guide-scqubits-oliver.pdf-28-0.png)

FIG. 13. **(a)**
Schematic of a typical qubit drive setup. A microwave source supplies a high-frequency signal ( __ LO ), while
an arbitrary waveform generator (AWG) supplies a pulseenvelope ( _s_ ( _t_ )), sometimes with a low frequency component,
__ AWG , generated by the AWG. The IQ-mixer combines the two
signals to generate a shaped waveform _V_ _d_ ( _t_ ) with a frequency
__ _d_ = __ LO __ AWG , typically resonant with the qubit. **(b)**
__
Example of how a gate sequence is translated into a waveform
generated by the AWG. Colors indicate _I_ and _Q_ components.
**(c)** The action of a X _/_ 2 pulse on a 0 state to produce the
1 _|_ __
_|_ _i_ __ = __ 2 ( _|_ 0 __ _i_ _|_ 1 __ ) state.

sequence of pulses (see Fig. 13(a))  _k_ _,_  _k_ __ 1 _, ..._  0
is converted to a sequence of gates operating on a qubit as


where __ = __ q __ __ d . Finally, by re-using the definitions
from Eq. (86), the driving Hamiltonian in the rotating
frame using the RWA can be written as




_H_ d =
__ 2



 0 _e_ _i_ ( _t_ + __ )

_V_ 0 _s_ ( _t_ ) _i_ ( _t_ + __ )
2 _e_ __ 0



_i_ ( _t_ + __
_e_ __


(91)


Equation (91) is a powerful tool for understanding singlequbit gates in superconducting qubits. As a concrete
example, assume that we apply a pulse at the qubit frequency, so that __ = 0, then




_H_ d = _V_ 0 _s_ ( _t_ ) ( _I_ _x_ + _Q_ _y_ ) _,_ (92)
__ 2

showing that an  _in-phase_ pulse ( __ = 0, i.e. the _I_
component) corresponds to rotations around the _x_ -axis,
while an out-of-phase pulse ( __ = _/_ 2, i.e. the _Q_
component), corresponds to rotations about the _y_ -axis.
As a concrete example of an in-phase pulse, writing out
the unitary operator yields


_U_ _k_ _U_ 1 _U_ 0 =
_  _ _T_


_e_ [ __ 2 _i_  _n_ ( _t_ )( _I_ _n_ __ _x_ + _Q_ _n_ __ _y_ ) ] _,_ (95)
_n_ =0


where
_T_
is an operator that ensures the pulses are generated in the time-ordered sequence corresponding to
_U_ _k_ _  _ _U_ 1 _U_ 0 .
In Fig. 13 we outline the typical IQ modulation setup
used to generate the pulses used in Eq. (95). Fig. 13(a)
shows how a pulse at frequency __ d is generated using a
low phase-noise microwave generator (typically denoted
the local oscillator (LO)), while the pulse is shaped by
combining the LO signal in an IQ mixer with pulses generated in an AWG. To allow for frequency multiplexing,
the AWG signal will typically be generated with a lowfrequency component, __ AWG , and the LO signal will be
offset, so that __ LO + __ AWG = __ d . By mixing in more than
one frequency __ AWG1 _, _ AWG2 _, ..._ it is possible to address
multiple qubits (or readout resonators) simultaneously,
via the superposition of individual drives.
mixer will multiply the baseband signal to the in-phase (out-of-phase) component of The _I_ ( _Q_ ) input of the _IQ_
the LO. In Fig. 13(b) we schematically show the comparison between _XY_ gates in a quantum circuit and the
corresponding waveforms generated in the AWG (omitting for clarity the frequency __ AWG component). The
inset in Fig. 13(b) shows an example of a gate on the



__ =0 _i_
_U_ rf,d ( _t_ ) = exp 2  _V_



0




_s_ ( _t_ __ )d _t_ __ __


(93)


which depends only on the macroscopic design parameters of the circuit as well as the envelope of the baseband
pulse _s_ ( _t_ ) and amplitude _V_ 0 , which can both be controlled
using arbitrary waveform generators (AWGs). Equation
(93) is known as and can serve as a useful tool for engineering the circuit parameters needed for _Rabi driving_
efficient gate operation (subject to the available output
voltage _V_ 0 ). To see this we define the shorthand


( _t_ ) = __  _V_ 0


_t_

0




_s_ ( _t_ __ )d _t_ __ (94)


which is the angle by which a state is rotated given the
capacitive couplings, the impedance of the circuit, the
magnitude _V_ 0 , and the waveform envelope, _s_ ( _t_ ). This
means that to implement a __ -pulse on the _x_ -axis one
would solve the equation ( and output the signal in-phase with the qubit drive. In this language, a _t_ ) = __


LO


-----


30

Finally we mention one more salient feature of the
virtual- Z gates. As shown in Ref.63, any single-qubit
operation (up to a global phase) can be written as


) axes. More sophisticated and compact approaches exist to reduce the Bloch sphere, with indication of ( _I, Q_
hardware needed for _XY_ qubit control, relative to the
setup shown in Fig. 13, see e.g. 189191 .

**_2._** **_Virtual Z gate_**

As we saw in Sec. IV D, the distinction between _x_ 
rotations was merely a choice of phase on the microwave signals, and the angle to be rotated is given by and _y_
( _t_ ), both of which are generated using an AWG. Since
the choice of phase __ has an arbitrary starting point, we
could consider __ __ + _/_ 2. This would lead to _I_ _Q_
__ __
and _Q_ _I_ . Therefore, changing the phase effectively
__
changes rotations around _x_ to rotations around _y_ (and
vice-versa, with a change of sign). This is reminiscent of
the result of applying a Z __ rotation to _x_  and _y_ rotations,
where Z __ X __ = _i_ Y __ and Z __ Y __ = _i_ X __
__
. This analogy between shifting a phase of an AWG-generated signal and
applying Z rotations can be utilized to implement _virtual_
Z gates 192 . As shown by McKay _et al._ , this intuition
can be formalized via the following example: consider
the case of applying a pulse with an angle __ on the _I_
channel (i.e. a X __ ) followed by another __ pulse on the _I_
channel, but with a phase __ 0 relative to the first pulse
(denoted X ( __ __ 0 ) , where X indicates we still use the _I_
channel, but the rotation axis is now an angle __ 0 away from
the _x_ -axis). Using Eq. (95) this corresponds to a pulse
sequence


_U_ ( _, , _ ) = Z __ __ __ 2



__ 2 X __ 2



__ 2 Z __ __ __ X __ 2



__
2 Z __ __ 2



__ 2 _,_ (100)


for appropriate choice of angles _, , _ . This means
that access to a single physical X __ combined with the


that access to a single physical virtual- Z gives access to a complete single qubit gate X __ 2 combined with the

set! An explicit example of Eq. (100) in action is the
Hadamard gate, which can be written as H = Z __ X __ Z __ ,


but since the s can be virtual, it is possible to implement Hadamards as an effective single pulse operation in Hadamard gate, which can be written as Z H = Z __ 2 X __ 2 Z __ 2 ,
superconducting qubits.



__ 2 X __ 2


2 Z __ 2


**_3._** **_The DRAG scheme_**


In going from Eq. (78) to Eq. (79) we assumed we
could ignore the higher levels of the qubit. However,
for weakly anharmonic qubits, such as the transmon (see
Sec. II), this may not be a justified assumption, since

1 2 0 1
__ q __ only differs from 1 2 __ q ( __ __ q __ ) by the anharmonicity,
__ = __ q __ __ __ q , which is negative and typically around
200 to 300 MHz. This situation is sketched in Fig. 14(ac), where we illustrate how Gaussian pulses with standard deviations __ = 1 _,_ 2 _,_ 5 ns have spectral content
_{_ _}_ 1 2
that leads to non-zero overlaps with the __ q __ = __ q _|_ __ _|_
frequency. This leads to two deleterious effects: ( ) leakage errors which take the qubit out of the computational _1_
subspace, and ( _2_
) phase errors. Effect 1 can occur because a qubit in the state 1 may be excited to 2 as a __
_|_ __ _|_ __
pulse is applied, or be excited directly from the 0 , since
_|_ __
the qubit spends some amount of time in the 1 state
_|_ __
during the __ pulse. Effect 2 occurs because the presence
of the drive results in a repulsion between the 1 and 2

0 1 _|_ __ _|_ __
levels, in turn changing __ q __ as the pulse is applied. This
leads to the accumulation of a relative phase between
0 and 1 194 . The so-called DRAG procedure 195197
_|_ __ _|_ __

(Derivative Reduction by Adiabatic Gate) seeks to combat these two effects by applying an extra signal in the
out-of-phase component. The trick is to modify the waveform envelope _s_ ( _t_ ) according to


X ( __ __ 0 ) X __ = _e_ __ _i_ __ 2


_e_ __ _i_ __ 2 (cos( __ 0 ) __ _x_ +sin( __ 0 ) __ _y_ ) X __ (96)

= Z __ __ 0 X __ Z __ 0 X __ (97)


from which we see that the effect of the offset phase __ 0
is to apply Z __ 0 . The equality above can be verified with
a little trigonometric footwork. The final Z __ __ 0 is due to
the rotation being in the frame of reference of the qubit.
However, since readout is along _z_ -axis (see Sec. V), a
final phase rotation about will not change the measurement outcome. Thus, if one wants to to implement _z_
the gate sequence


|Col1|U i|Col3|Z 0|Col5|U i+1|Col7|Z 1|Col9|U i+2|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||


where _U_ _i_
s are arbitrary gates, this can be done by revising the gate sequence (in the control software for the
AWG) and changing the phase of subsequent pulses

|Col1|U i|Col3|U ( +0 1) i|Col5|U ( +0 2+1) i|Col7|
|---|---|---|---|---|---|---|
||||||||



which reduces the number of overall gates. Moreover,
the virtual- Z gates are perfect, in the sense that no
additional pulses are required, and the gate takes zero
time, and thus the gate fidelity is nominally unity. As
we show in Sections IV E and IV F, operation of twoqubit gates can incur additional single-qubit phases. Using the virtual- Z strategy, these phases can be cancelled
out, leaving a pure two-qubit interaction.


_s_ ( _t_ ) on


_s_ ( _t_ ) _s_ __ ( _t_ ) =
__


_s_  ( _t_ )
__


_,_ (101)
on _Q_


where __ is a dimensionless scaling parameter, and __ =
0 correspond to no DRAG pulse and  _s_ ( _t_ ) is the time
derivative of _s_ ( _t_ ). The theoretically optimal choice for
reducing dephasing error is __ = 0 _._ 5 and an optimal choice

196,198
for reducing leakage error is __ = 1 . Interchanging
_I_ and _Q_ in Eq. (101) corresponds to DRAG pulsing for
the _Q_ component.
In practice there can be a deviation from these two
optimal values, often due to pulse distortions in the lines
leading to the qubits. Typically, randomized benchmarking experiments combined with single-shot measurements


-----


31

quency), i.e.

_i_ 2 _ft_
_s_ __ _f_ ( _t_ ) = _s_ __ ( _t_ ) _e_ _,_ (102)

and choosing __ to minimize leakage errors, then phase
errors can be reduced simultaneously 199 . Similarly,
by a judicious use of the virtual- Z gate, it is also
possible to reduce phase errors in combination with
DRAG pulsing to reduce leakage 192 . Modern single-qubit
gates using DRAG pulsing now routinely reach fidelities

65,67,199,202205
_F_ 1qb  0 _._ 99 . Other techniques also exist
for operating single-qubit gates in a spectrally crowded
device 206,207 .

**E.** **The** _i_ **SWAP two-qubit gate in tunable qubits**

As briefly mentioned in Sec. IV C, single-qubit gates
supplemented with an entangling two-qubit gate can
form the gate set required for universal quantum computation. The two-qubit gates available in the transmonlike superconducting qubit architecture can roughly be
split into two broad families as outlined previously:
one group requiring local magnetic fields to tune the
transition frequency of qubits and one group consisting of all-microwave control.
There exist several hybrid schemes that combine various aspects of these two
categories and, in particular, the notions of tunable
coupling and parametric driving are proving to be important ingredients in modern superconducting qubit
processors 63,67,91,104,107,208214 . In this section, however,
we start by introducing the _i_ SWAP gate, and then review
the CPHASE (controlled-phase) in Section IV F and the
CR (cross-resonance) in Section IV G. We briefly review
a few other two-qubit gates and discuss their merits in
Sections IV G 4 and IV H.

**_1._** **_Deriving the_** _i_ **_SWAP unitary_**

As we saw in Sec. II, Eq.32 the interaction term between two capacitively coupled qubits (in the two-level
approximation) is given by


(a)


(b)


2 _E_ 1

_E_ 2

_E_ 1


-20 -10 0 10 20

![qe-guide-scqubits-oliver.pdf-30-0.png](qe-guide-scqubits-oliver.pdf-30-0.png)

(c) Time (ns)


-20 -10 0 10 20
Time (ns)


![qe-guide-scqubits-oliver.pdf-30-1.png](qe-guide-scqubits-oliver.pdf-30-1.png)

![qe-guide-scqubits-oliver.pdf-30-2.png](qe-guide-scqubits-oliver.pdf-30-2.png)

__ q 01 _E_


![qe-guide-scqubits-oliver.pdf-30-3.png](qe-guide-scqubits-oliver.pdf-30-3.png)

![qe-guide-scqubits-oliver.pdf-30-4.png](qe-guide-scqubits-oliver.pdf-30-4.png)


-0.5 -0.25 0 0.25 0.5
Frequency (GHz)


|Col1|Col2|Col3|Col4|(e)|
|---|---|---|---|---|
|0|||||
||||I Q||
||||||
||||||
||||||
||||||


![qe-guide-scqubits-oliver.pdf-30-5.png](qe-guide-scqubits-oliver.pdf-30-5.png)

![qe-guide-scqubits-oliver.pdf-30-6.png](qe-guide-scqubits-oliver.pdf-30-6.png)



|tim|me (|(ns)|Col4|(g)|
|---|---|---|---|---|
|= 0.5|||||
||||I Q||
||||||
||||||
||||||
||||||


![qe-guide-scqubits-oliver.pdf-30-8.png](qe-guide-scqubits-oliver.pdf-30-8.png)

time (ns)


![qe-guide-scqubits-oliver.pdf-30-7.png](qe-guide-scqubits-oliver.pdf-30-7.png)

FIG. 14. **(a)** Schematic level diagram of a weakly anharmonic
transmon qubit subjected to a drive at transition frequency
__ d = __ q . **(b)** Gaussian waveform with standard deviation
__ . **(c)** Fourier transform of (b) showing how the short pulse
lengths lead to significant overlap with the __ q 1 __ 2 transition,
separated from __ q by the anharmonicity __ . **(d)** Waveform
of a X __ pulse without DRAG modulation. **(e)** Effect of the
waveform from (d) on a qubit initialized in the 0 state with
_|_ __
__ = 200 MHz and __ q = 4 GHz. The dephasing error is
__
visible as a deviation from the 1 after the pulse. **(f)**
_|_ __
Waveform of a X __ pulse with DRAG modulation for a qubit with
anharmonicity __ = 200 MHz and DRAG parameter __ = 0 _._ 5
__
to cancel dephasing errors (see text for details). **(g)** Effect of
the waveform from (f) on the same qubit as (e). Calculated
using mesolve in the software package QuTiP 193 .


_H_ qq = _g_ _y_ 1 __ _y_ 2 _,_ (103)
__

where _g_ is the coupling strength and
__
is used to emphasize the tensor product. If the capacitive coupling is
mediated through a bus resonator, then 215,216



_g_ 1 _g_ 2 ( 1 +  2 )
_g_ _g_ q-r-q = _,_ (104)
__ 2 1  2

where _g_ _i_ is the resonator coupling to qubit _i_
(dependent on the qubit-resonator coupling capacitance _C_ q _i_ r )
and  _i_ = __ q _i_ __ r is the detuning of qubit _i_
__
to the resonator. In the simpler case where the qubits are directly
coupled 217 ,


(see Sec. V) of the 2
_|_ __
state is used to determine the optimal value of __ . The __ = 0 _._ 5 _,_ 1
192,199 _{_ _}_
tradeoff was demonstrated explicitly in . However, by extending the
original DRAG pulse implementation , it is is possible to reduce _both_ errors _simultaneously_ 200,201 . By introducing

196
a frequency detuning parameter _f_ to the waveform

(defined such that _f_ = 0 corresponds to qubit fre-



1
_g_ _g_ q-q =
__


_C_ q-q
__ __ q1 __ q2

_C_ q-q + _C_ 1


_C_ q-q
__ __ q1 __ q2


_,_ (105)
_C_ q-q + _C_ 2


-----


32


where _C_ q-q is the qubit-qubit coupling capacitance and
_C_ . Throughout this section, we will assume a direct capacitive coupling between _i_ is the capacitance of qubit _i_
qubits of the flux-tunable transmon type, so that _g_ = _g_ q-q
). For simplicity, we suppress the explicit flux dependence of the and __ q _i_ __ __ q _i_ ( _i_ __ q _i_ s and simply refer to the
coupling as _g_ . Equation (103) can be rewritten as

+ +
_H_ qq = _g_ [ __ __ __ ] [ __ __ __ ] _,_ (106)
__ __ __ __

and then using the rotating wave approximation again  
( _i.e._ dropping fast rotating terms) we arrive at


(a)


5.0

4.5

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||||initial point final point|
||||||
||||||
||||||
||||||



0.0 0.1


0.2 __ iSWAP 0.3 0.4


Magnetic flux, qubit 1 ( __ 0


_H_ qq = _g_ _e_ _i_ 12 _t_ __ + __ __ + _e_ __ _i_ 12 _t_ __ __ __ + _,_ (107)

where we have introduced the notation  __ 12  = __ q1 __ q2
__
and suppressed the explicit tensor product between qubit
subspaces. If we now change the flux of qubit 1 to bring
it into resonance with qubit 2 ( __ q1 = __ q2 ), then



![qe-guide-scqubits-oliver.pdf-31-0.png](qe-guide-scqubits-oliver.pdf-31-0.png)

![qe-guide-scqubits-oliver.pdf-31-4.png](qe-guide-scqubits-oliver.pdf-31-4.png)


+ + _g_
_H_ qq = _g_ __ __ __ + __ __ __ =
 


4/2

3/2

2/2

1/2


2 ( __ _x_ __ _x_ + __ _y_ __ _y_ ) _._ (108)


The first part of Eq. (108) shows that a capacitive interaction leads to a swapping of excitations between the two
qubits, giving rise to the swap in _i_ SWAP . Moreover, due
to the last part of Eq. (108), this capacitive coupling is

218
also sometimes said to give rise to an  _XY_  interaction .
The unitary corresponding to a _XY_ (swap) interaction
is


![qe-guide-scqubits-oliver.pdf-31-3.png](qe-guide-scqubits-oliver.pdf-31-3.png)

![qe-guide-scqubits-oliver.pdf-31-1.png](qe-guide-scqubits-oliver.pdf-31-1.png)


0.5


![qe-guide-scqubits-oliver.pdf-31-2.png](qe-guide-scqubits-oliver.pdf-31-2.png)

Magnetic flux, qubit 1 ( __ 0 ) Probability


FIG. 15. **(a)** Spectrum of two transmon qubits (written in the
combined basis as QB1 _,_ QB2 ) as the local flux through the
_|_ __
loop of qubit 1 is increased. Black/dashed lines with arrows
indicate a typical flux trajectory to demonstrate operation of
_i_ SWAP gate. **(b)** Probability of swapping into the 01 state
_|_ __
as a function of time and flux. The pulse sequence corresponds
to preparing 10 and performing a typical _i_ SWAP operation
_|_ __
(for a time __ ). **(c)** Probabilities of 01 (black) and 10 (gray)
_|_ __ _|_ __
at  =  _i_ SWAP (white dashed line in (b)) as the time spent
at the operating point ( __ ) is increased. This simulation does
not include any decay effects.


0 cos( _gt_ ) _i_ sin( _gt_ ) 0
__
0 _i_ sin( _gt_ ) cos( _gt_ ) 0
__


_U_ _qq_ ( _t_ ) = _e_ __ _i_ _g_ 2 ( __ _x_ __ _x_ + __ _y_ __ _y_ ) _t_ =



_g_ 2 ( __ _x_ __ _x_ + __ _y_ __ _y_ ) _t_

=


(109)
Since the qubits are tunable in frequency, we can now
consider the effect of tuning the qubits into resonance
for a time _t_ __ = 2 __ _g_ ,


(109)
Since the qubits are tunable in frequency, we can now
consider the effect of tuning the qubits into resonance
for a time _t_ __ = __ ,


__

2 _g_




__

2




0 0 _i_ 0
__
0 _i_ 0 0
__


_i_ SWAP _._ (110)
__




_U_ _qq_


To elucidate the operating principle behind an _i_ SWAP
implementation fluxtunable qubit using typical transmon-like parameters in we show the spectrum of a
Fig. 15(a). The is performed at the avoided crossing where  =  _i_ SWAP _i_ SWAP . By preparing QB1 in state _|_ 1 __ ,
moving into the avoided crossing, waiting there for a time
__
(see pulse-sequence in inset in Fig. 15(b)), the excitation is swapped back and forth between the two qubits,
as shown in Fig. 15(b). In Fig. 15(c), we plot linecuts
of (b) at  _i_ SWAP , showing the excitation oscillating back
and forth between 01 and 10 with the predicted time
_|_ __ _|_ __
_t_ __ = _/_ 2 _g_ . In turn, the frequency of the oscillation can
be used to extract the strength of the coupling, 2 = _g_ .


From this result, we see that a capacitive coupling between qubits turned on for a time _t_ __ (inversely related to
the coupling strength in units of radial frequency) leads

216,217,219222
to implementing a so called  _i_ SWAP  gate ,
which acts to swap an excitation between the two qubits,

_i/_ 2
and add a phase of _i_ = _e_ . For completeness, we note
that for _t_ __ = __ the resulting unitary,


4 __ _g_ the resulting unitary,


__

4 _g_




__

4




0 1 _/_ __ 2 _i_ _/_ __ 2 0

0 _i_ _/_ __ 2 __ 1 _/_ __ 2 0
__


_U_ _qq_


1 _/_


__ _i_ _/_


_i_ SWAP _,_ (111)


__




1 _/_


_t_ 2 __ = _g_ __


__


So far we have ignored the role of the single-qubit
phases acquired by tuning the qubit frequency. Referring to the pulse-sequence shown in the top panel of
Fig. 15(a), we see that each qubit will acquire a phase


is typically referred to as the squareroot- _i_ SWAP  gate.
The __ _i_ SWAP


The _i_ SWAP

gate can be used to generate Bell-like superposition states, e.g. 01 + _i_ 10 .
_|_ __ _|_ __


-----


33

_i_ SWAP gate interspersed with single-qubit rotations was
used to generate successive _XY_ , _XZ_ and _Y Z_ interactions
that lead to an aggregate _H_ Heisenberg
Hamiltonian. Stateof-the-art operation of the _i_ SWAP gate has also been used
to demonstrate a ten-qubit GHZ state 226 .

**F.** **The CPHASE two-qubit gate in tunable qubits**

In our discussion of the _i_ SWAP gates, we assumed that
the higher energy levels of the superconducting qubit do
not play a role. As we show below, it turns out that for
the case of transmon qubits (with negative anharmonicity), the higher levels can in fact be utilized to generate
a the CPHASE gate directly 64,227 .
gate implements the following unitary, Recall from Sec. IV C that the CPHASE


given by


__
__ _z_ =

0




d _t_ ( __ q __ __ ( _t_ )) _._ (112)


This phase can be conveniently removed either by subsequent application of virtual- Z gates to all following
pulses 192 , or by shaping the waveform of the excursion
such that single-qubit phases are exactly cancelled 223 .
Equations (105) and (109) together present a useful result from a quantum processor design perspective: The
operating regime, frequency and time __ of the _i_ SWAP
can be calculated (typically simulated) to high precision,
before any processor fabrication is undertaken. The only
quantum parts that enter _g_ qq (and _g_ q-r-q ) are the qubit
frequencies, __ q1 ( 1 ) and __ q2 ( 2
). If the Josephson energies of the qubits are known (which they typically are,
from fabrication parameters), then by simulating the capacitances in _g_ qq or _g_ q-r-q , the time __ and the pulseshape
needed to implement an _i_ SWAP can be estimated to
high precision. Typical values of the coupling strength,
_g/_ (2 __ ), for architectures using the _i_ SWAP gate is 5-40
MHz and are often very close to expectations from EM
simulations 220,222224 .


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
__


_U_ CPHASE =


(115)


Our goal for the remainder of this section is to show that
the unitary operator of the gate appears naturally for capacitively coupled transmon superconducting CPHASE
qubits and review a few of the modern applications of this
gate. We have chosen to include a considerable amount of
details for the implementation of this gate, as a means to
review some of the issues one has to resolve, to engineer
high quality two-qubit gates.
The structure of the matrix in Eq. (64) indicates that
we need to apply a phase ( 1 = _e_ _i_
__
) to the qubits whenever both are in the excited state 11 . Considering the
_|_ __
nature of the _XY_ interaction, which couples 01 10
_|_ _|_ __
and leads to the _i_ SWAP gate (see previous section), we
expect avoided level crossings to exist between higher levels, e.g. 11 20 and 11 02 . The flux-tunable
_|_ _|_ __ _|_ _|_ __
implementation of the gate relies on this higherlevel avoided crossing. CPHASE
To motivate this intuition we plot the spectrum for two
coupled transmon qubits, in Fig. 16(a), including levels
with two excitations, as the local magnetic flux in qubit
1 is being tuned. The Hamiltonian for this spectrum,
written in the 00 _,_ 01 _,_ 10 _,_ 11 _,_ 02 _,_ 20
_{|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ _}_
-basis, is approximately given by,


**_2._** **_Applications of the_** _i_ **_SWAP gate_**

The _i_ SWAP cannot generate a CNOT gate by itself.
Rather, to implement a CNOT gate requires stringing

218
together two _i_ SWAP s and several single qubit gates ,



|Col1|Z -  2|
|---|---|

||Col2|
|---|---|


(113)

|Col1|Col2|Col3|Z-  2|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||X  2||Z  2||Z  2||
||||||||

As evident from Eq. (113), the _i_ SWAP gate in general
needs to be used twice to generate a single CNOT , leading
to a significant overhead when compiling CNOT dense
circuits from _i_ SWAP gates. However, depending on the
. Typically such circuits will not be completely equivalent, but will share certain salient features context, the without any two-qubit gate overhead) to mimic the behavior of a CNOT _i_ SWAP can be used efficiently (i.e.

221
for specified input states. As an example of this procedure, Neeley _et al._ demonstrated the generation of a
3-qubit Greenberger-Horne-Zeilinger (GHZ) state (which
requires two subsequent s in the simplest construction), by using only two s in a circuit that correctly generates the 3-qubit GHZ state on the CNOT _i_ SWAP 000 input.
_|_ __
Moreover, the _XY_
225
interaction is a powerful tool for certain types of quantum simulation algorithms . If one
is interested in digital quantum simulation of spinlike
systems, then the _XY_ interaction can natively simulate
e.g. a Heisenberg interaction,

_H_ Heisenberg = _J_ _x_ __ _x_ __ _x_ + _J_ _y_ __ _y_ __ _y_ + _J_ _z_ __ _z_ __ _z_ _._ (114)

This approach to the _XY_ interaction was demonstrated
by Salath e _et al._ 223 , where repeated application of the


_H_ 2 excitations =


_E_ 00
0 _E_ 01 _g_ 0
0 _g_ _E_ 10 0
0 0 0 _E_ 11


2 _g_


2 _g_


2 _g E_ 02


2 _g_ 0 _E_ 20


(116)

q1 q2
where _E_ _nm_ = _E_ _n_ ( 1 )+ _E_ _m_ ( 2 ) and _E_ _n_ ( _i_ ) is the flux
52
dependent energy of the _i_ -th level of a transmon , and
the 02 _,_ 20 11
_{|_ __ _|_ _} |_ __
transitions are scaled by a factor __ 2 due to the higher photon number. In Fig. 16,


2 due to the higher photon number. In Fig. 16,
we plot the frequencies __ _nm_ = _E_ _nm_ _E_ 00 calculated
__


-----



34

where


__
__ _ij_ ( __ ( __ )) =

0




d _t _ _ij_ [ __ ( _t_ )] (118)


is the phase acquired by the state _ij_ along the trajectory
_|_ __
__ in (, _t_ )-space during time __ . The movement should be
that the moving state never populates the sufficiently slow on a time-scale set by 20 _g_
_|_ __
state, i.e. the movement should be adiabatic. In terms of applied flux, the
avoided crossing between the 11 20 state happens
_|_ _|_ __
before 10 01 (due to the negative anharmonicity of
_|_ _|_ __
the transmons, __ _E_ _c_ ) and consequently __ does not
__
take the states through the  _i_ SWAP operating point. As
shown in Fig. 16(b) we can define a parameter (typically
denoted __ ) quantifying the difference in phase acquired
by the 11 relative to the single excitation states,
_|_ __

__ = ( __ 11 ( __ 01 + __ 10 )) _._ (119)
__


![qe-guide-scqubits-oliver.pdf-33-0.png](qe-guide-scqubits-oliver.pdf-33-0.png)

0.3 0.4



The parameter __ can be thought of as the result (in the
computational space) of the repulsion of 11 due to the
_|_ __
20 state. If we now choose a trajectory __ __ , designed so
_|_ __ __
that 0 __ ( __ __ ( _t_ )) _dt_ = __ , then



0.15 __ CPHASE 0.2

|(a)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|CPHASE in 10 fi () 9 8 (GHz) 7 2 6 / iSWAP 5 4 0.0 0.1 0.2 0.3   CPHASE iSWAP Magnetic flux, qubit 1 ( ) b) 0 (GHz) ()  2 /|||||CPHASE in||
||()||||fi||
||||||||
||||||||
||||||||
||||||iSWAP||
||||||||
||||||||
||() ||||||
||||||||
||||||||


![qe-guide-scqubits-oliver.pdf-33-1.png](qe-guide-scqubits-oliver.pdf-33-1.png)

Magnetic flux, qubit 1 ( __ 0 )

FIG. 16. **(a)** Spectrum of two coupled transmon qubits (using
typical transmon-like values for Josephson energies and capacitances) as the local magnetic flux for qubit 1 is varied. The
two lower branches corresponding to 01 and 10 are involved
_|_ __ _|_ __
in the _i_ SWAP gate operation at  =  iSWAP . The avoided
crossing indicated in the black rectangle is used to implement
the conditional phase gate ( CPHASE ), at  =  CPHASE . Black
line with arrows indicate a typical trajectory used to implement a CPHASE gate (starting at the black circle and ending
at the gray circle). **(b)** Zoom in of the 20 11 avoided
_|_ _|_ __
crossing highlighted in the black box in (a) at  =  CPHASE .
The parameter __ quantifies the difference in energy between
11 and 01 + 10 and __ ( __ ) is the trajectory in ( _, t_ )space.
_|_ __ _|_ __ _|_ __

from Eq. (116), using standard, symmetric, transmonlike parameters, as the local magnetic field of qubit 1 is
increased.
The result of the higher levels on the computational
basis can be understood by considering a concrete example. By preparing the combined qubit state 11 and
_|_ __
moving slowly towards the avoided crossing between 11
_|_ __
and _|_ 20 __ at  CPHASE , waiting for some time __
and moving back (see black line with arrows in Fig. 16(b)), the
resulting unitary operator in the computational basis is
given by


__

0




__ ( _t_ ) _dt_ = __ = __ 11 ( __ __ ) __ ( __ 01 ( __ __ ) + __ 10 ( __ __ )) _._ (120)


Inserting this expression into Eq. (117) we see that


0 _e_ _i_ 01 ( __ __ ) 0 0
0 0 _e_ _i_ 10 ( __ __ ) 0
0 0 0 _e_ _i_ ( __ + __ 01 ( __ __ )+ __ 10 ( __ __ ))


_U_ ad =


 _._
 (121)


After the adiabatic excursion, one can now apply singlequbit pulses (or use virtual- Z gates) to exactly cancel the
single-qubit phases such that __ 10 ( __ __ ) = __ 01 ( __ __ ) = 0. This
changes _U_ ad to


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 _e_ _i_


1 0 0 0
0 1 0 0
0 0 1 0  = _U_ CPHASE _._ (122)
0 0 0 1
__ 




_U_ ad =


 =



From Eq. (122) it is evident that an adiabatic movement
of 11 , followed by single-qubit gates (virtual or real)
_|_ __
efficiently implements a CPHASE and, through Eq. (67),
also efficiently implements a CNOT . The CPHASE gate is
one of the workhorses of modern superconducting qubit

65,228
processesors with gate fidelities  0 _._ 99 .
One is, of course, free to choose an arbitrary trajectory __ __ that implements the phase _e_ __ _i_ on the 11 state.
_|_ __
Assuming that the single-qubit phases are properly cancelled, one sees that the arbitrary phase version of the


0 _e_ _i_ 01 ( __ ) 0 0
0 0 _e_ _i_ 10 ( __ ) 0 _,_ (117)
0 0 0 _e_ _i_ 11 ( __ ) 





_U_ ad =


-----


35

form (based on a Slepian waveform 242 ) to parametrize
the trajectory __ __ __ ( __ ).

**_2._** **_The CPHASE gate for quantum error correction_**


CPHASE gate (typically denoted CZ __ ) can be written as


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 _e_ __ _i_


CZ __ =



__
= exp _i_ ( __ _z_ __ _z_ __ _z_ 1 1 __ _z_ ) _._ (123)
__ 4 __ __ __ __ __



__
= exp _i_
__


Using the approach of Martinis and Geller, Barends
_et al._ were able to demonstrate a two-qubit gate fidelity
CPHASE = 0 _._ 9944 (determined via a technique known
_F_ as interleaved randomized benchmarking 243246 ). This
implementation had a gate time __
__ 65 85
= 43 ns and was implemented with the  a transmon with a +-shaped capacitor. A two-qubit __ __ waveform , in an xmon device

gate fidelity _>_ 0 _._ 99 represents a significant milestone,
_F_
not just from a technical and engineering perspective,
but also from a foundational standpoint: The surface
code (a quantum error correcting code) has a lenient
fault-tolerance threshold of 1% 247249 . This means,
__
roughly speaking, that if the underlying operations on
the qubits have fidelities _>_ 0 _._ 99, then by adding
_F_
more qubits to the circuit (and correctly implementing
the fault-tolerant quantum error correction protocol) the
overall error-rate can be reduced, and one can in principle
perform arbitrarily long quantum computations, without errors spreading uncontrollably and corrupting the
calculation. Because of its relatively lenient threshold
under circuit noise (compared to e.g., Steane or Shor
codes 178,250,251 ) and its use of solely nearest-neighbor
coupling, the surface code is one of the most promising
quantum error correction codes for medium-to-large scale
quantum computing in solid state systems 247 . Therefore,
surpassing the fault-tolerance threshold using CPHASE
represents a significant milestone for the field . Moreover, practical blueprints for implementing scalable subcells of the surface code using the CPHASE 252
71
as the fundamental two-qubit gate have also been proposed as well
as _in-situ_
253
calibration protocols for large-scale systems operating with CPHASE . For a full review of the pros and
cons of various quantum error correcting codes we refer
the interested reader to e.g. an introductory review article Ref. 254, or any of the excellent textbooks and more
detailed review articles in Refs. 178, 180, 251, 254257.


Because of the form of Eq. (123), one can think of the
avoided crossing with the higher levels outside the computational subspace as giving rise to an effective __ _z_ __ _z_

227 __
coupling within the computational subspace .
An alternative to the adiabatic approach outlined
is to make a sudden excursion to the  above to realize CPHASE CPHASE operating point, after waiting a
time _t_ = _/_ __ 2 _g_ , the state will have completed a single

Larmor-type rotation from 11 to 02 and back again to
_|_ __ _|_ __
11 , but in the process, acquired an overall __
_|_ __ 54
phase, similar to the _i_ SWAP gate, but in the 11 _,_ 20 subspace .
_{|_ __ _|_ _}_
In fact, such excursions near or through avoided crossings
leading to adiabatic and non-adiabatic transitions have
been studied extensively in the context of interferometry,
cooling, spectroscopy, and quantum control 119,229238 .
The remainder of this subsection is devoted to an
gate since its first demonstration in 2009 where it was used to generate Bell-states overview of some of the recent advances and demonstrations using the CPHASE
and demonstrate two-qubit algorithms 64 .


Because of the form of Eq. (123), one can think of the
avoided crossing with the higher levels outside the computational subspace as giving rise to an effective __ _z_ __ _z_

227 __
coupling within the computational subspace .
An alternative to the adiabatic approach outlined
is to make a sudden excursion to the  above to realize CPHASE CPHASE operating point, after waiting a
time _t_ = _/_ __ 2 _g_ , the state will have completed a single


**_1._** **_Trajectory design for the CPHASE gate_**

The (adiabatic) implemention of _U_ CPHASE outlined
above assumed that the trajectory __ __ was completely
adiabiatic and that the 11
_|_ __
state never left the computational subspace. Since the fidelity of gates is bounded
from above by the coherence times of the qubits, short
gate times are desirable 239 . This presents a tension for
optimally operating the CPHASE gate  fast operation
in conjunction with the need for adiabatic operation. A
relevant question is then: what is the _optimal_ trajectory
__ sible, with as little leakage as possible, for a given size __ __ that implements the necessary phase as fast as pos
of the avoided crossing between 11 and 20 ? Given a
_|_ __ _|_ __
typical coupling rate _g/_ 2 __ 20 MHz (as discussed in
__
Sec. IV E), one expects a heuristic lower time limit to be
2 _/g_ 50 ns (stronger coupling of course leads to shorter
__
gate times, but will limit the on/off ratio of the gate).
Traditional optimal control of adiabatic movement assumes the movement is _through_ the avoided crossing (see
e.g. Ref. 240), but the trajectory __ __ moves close to and
then back from the avoided crossing. This modification
to the adiabatic movement protocol was addressed by
Martinis and Geller , specifically in the context of errors for a CPHASE gate implemention. The authors show 241
that non-adiabatic errors can be minimal for gate times
only slightly longer than 2 _/g_ using an optimal wave-


Returning to the CPHASE
__ 228
gate, numerical optimization of interleaved randomized benchmarking sequence fidelity __ __ was demonstrated by Kelly _et al._ using the
as a cost function to push a native implementation of
__ __ __ with a fidelity = 0 _._ 984 up to = 0 _._ 993, sur

_F_ _F_
passing the surface code fault tolerance threshold. In
the same work that demonstrated CPHASE = 0 _._ 9944,
Barends _et al._ 65 used the CPHASE _F_ gate to generate

_N_ _N_
GHZ states, _|_ GHZ __ = _|_ 0 __ __ + _|_ 1 __ __ _/_ __ 2, of up to

_N_ = 5 qubits, with a fidelity for the _N_ = 5 state of

 

_F_ = Tr ( __ ideal __ _N_ =5 ) = 0 _._
817. The protocol for generating the GHZ state with _N_ = 2 and _N_ = 3 from CPHASE
was originally demonstrated by DiCarlo _et al._ 54,64 . The

+
textbook route to generating the _N_ = 2 GHZ state, 
_|_ __


-----


36


(a Bell state) from the all-zero input is


exp _i_ __ 2 __ _z_ __ _z_ unitary can be generated via
__ __


exp _i_ __ 2
__


0
_|_ __

0
_|_


(124)

=  +
 _|_ __


CPHASE 


|Col1|H|Col3|Col4|
|---|---|---|---|
|||||



An equivalent circuit using and native singlequbit gates in superconducting qubits is: CPHASE

|Col1|U () ZZ|Col3|
|---|---|---|
||||

|Col1|X |Col3|CZ |Col5|A |Col7|CZ |Col9|
|---|---|---|---|---|---|---|---|---|
|||||||||X|


(129)
where _A_ __ X __ _,_ Y __
_{_ _}_
is used to allow for small and negative angles. Finally, for completeness, we mention an

42,264
alternative approach to creating _U_ ZZ , given by



(125)

|Col1|Y /2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|||| Y Y /2  /2||||||
|||||Y /2||Y /2|||
||||||||||



(130)


By repeating the operation inside the dashed box
on additional qubits, an _N_ -qubit GHZ state can be

65
generated . Since the demonstration of the _N_ = 5 GHZ
state using the CPHASE gate, the gate has been deployed
to demonstrate several important aspects of quantum information processing using superconducting qubits. A
nine-qubit implementation of the five-qubit repetition
code (five data qubits + four syndrome qubits) 254 was
demonstrated, and the error suppression factor of a single logical quantum bit was shown to increase as the encoding was changed from three data qubits to five data
qubits . Similarly, in a five qubit processor the threequbit repetition code with artificially injected errors was 66
demonstrated 258 , building on earlier results utilizing a
combination of _i_ SWAP and CPHASE gates to perform
parallelized stabilizer readout 259 .

**_3._** **_Quantum simulation and algorithm demonstrations_**
**_using CPHASE_**

As an example of the utility of the CPHASE gate, we
briefly discuss a particular demonstration of a digital
quantum simulation. In this context, the CPHASE gate
has been utilized to simulate a two-site Hubbard model
with four fermionic modes, using four qubits 260 . Using
the Jordan-Wigner transformation 261,262 , it is possible to
map fermionic operators onto Pauli spin matrices 263 . As
shown in Ref.260 a Hubbard model with two fermionic
modes, whose Hamiltonian is given by

_H_ Hubbard, two mode = __ _t_ ( _b_ __ 1 _b_ 2 + _b_ __ 2 _b_ 1 ) + _Ub_ __ 1 _b_ 1 _b_ __ 2 _b_ 2 (126)

can be written in terms of Pauli operators as,

|Col1|U () ZZ|Col3|
|---|---|---|
||||
||||

||Col2|Col3|Col4|
|---|---|---|---|
||Z /2|||
|||||


which has the benefit of relying on CPHASE (through
the CNOT s), and the angle can be controlled using the
single-qubit Z gates. We refer the interested reader to
two reviews on quantum simulations, see e.g. Refs. 265
and 266.
The CPHASE
gate has also been used in a variety of other contexts, e.g., for calculating the dissociation of diatomic hydrogen ( _H_ 2 ) using the variational
quantum eigensolver method 267 , for feed-forward based
teleportation experiments 268,269 , as well as initial steps
towards demonstrating quantum supremacy 270 and a
2 2 implementation of the Harrow-Hassidim-Lloyd
algorithm __ 271,272 . In the field of hybrid semiconducting

273275
nanowire/superconducting qubits (known as the gatemon approach ), where the qubit frequency is
modified by electrostatically changing the density of carriers in a semiconducting region with proximity-induced
superconductivity, the CPHASE
276
gate was also demonstrated between two nanowire qubits .
One may worry that operating a qubit by moving its
frequency can lead to overlap with frequencies already
used by other qubits, in a system with multiple qubits.
This issue is known as _frequency crowding_ . While the
use of asymmetric transmons (with two sweet spots in
the range [ __  0 _,_ + 0
], recall Fig. 2(c)) may help alleviate some frequency crowding issues, a more long-term
strategy is needed. One way to circumvent the problem
is to utilize on/off tunable coupling schemes, in which
qubits can exchange energy only if a coupler activates
the interaction 63,104 . To address this issue in the context
of the demonstrated a device (named the gmon) where the qubit interaction can CPHASE gate, Chen _et al._ 104
be tuned with an on/off ratio on the order of 1000, and a
CPHASE gate fidelity of = 0 _._ 9907 was demonstrated.
_F_
This concludes the introduction to the physics and operation of the CPHASE gate in its native form. In the
remainder of this section we will introduce a few of the
microwave-only gates that have been demonstrated in an
effort to sidestep the need for local tunability (and the
resulting increased sensitivity to noise) as required by the
_i_ SWAP and CPHASE gate.



_t_
_H_ =


2 ( __ _x_ __ __ _x_ + __ _y_ __ __ _y_ ) (127)


+ _U_



( __ _z_ __ _z_ + __ _z_ 1 + 1 __ _z_ ) _,_ (128)
4 __ __ __


where _U_ is the repulsion energy and _t_ is the hopping
strength. Similar to the Heisenberg interaction discussed
briefly in Sec. IV E, it is now a question of producing
__ _i_ __ _i_ -type interactions, where the prefactor __ can be
tuned. Using the __ CZ __ version of CPHASE , a _U_ ZZ ( __ ) =


-----


37


**G.** **Two-qubit gates using only microwaves**

One common (potential) drawback for the _i_ SWAP
gates is that their operation requires fluxtunable qubits. Introducing a new control knob, such as and CPHASE
flux control, in turn also introduces a new noise channel
for the system. Furthermore, the need for flux-tunability
increases the sensitivity of the devices to flux noise by
tuning the qubits from their sweet spots, increases the
dephasing rate. From this perspective, one could envision using all-microwave-based gates to remedy these issues. To this end, the cross-resonance ( CR ) gate was
developed for operating fixed-frequency superconducting
qubits 277279 , which typically feature longer lifetimes and
reduced sensitivity to flux noise.

**_1._** **_The operational principle of the CR gate_**

To elucidate the operation of the CR gate, we briefly
revisit the driving Hamiltonian derived in Sec. IV D.
There, we considered only a single qubit. However, if
one extends this formalism to two qubits, see Fig. 17(a)
denoting the frequency difference by  12 = __ q1 __ q2 and
__
the coupling by _g_ __  12
, and performing a SchriefferWolff transformation to go to the dressed state picture,
the driving Hamiltonians for qubit 1 and 2 become 278,280


(a)


(b)
_g_


__ 2


_g_ 2
2 12

|~  1|Col2|~  2|
|---|---|---|


![qe-guide-scqubits-oliver.pdf-36-0.png](qe-guide-scqubits-oliver.pdf-36-0.png)

![qe-guide-scqubits-oliver.pdf-36-1.png](qe-guide-scqubits-oliver.pdf-36-1.png)

QB1 coupler QB2

(c) (d)


QB1 coupler QB2


-1

1

0

-1


![qe-guide-scqubits-oliver.pdf-36-2.png](qe-guide-scqubits-oliver.pdf-36-2.png)

100 200

Time (ns)


100 200


![qe-guide-scqubits-oliver.pdf-36-3.png](qe-guide-scqubits-oliver.pdf-36-3.png)

Time (ns)


FIG. 17. **(a)** Schematic circuit diagram of two fixed frequency
transmons coupled through a resonator yielding an overall
coupling coefficient _g_ . Qubit 1 driven at the frequency of
qubit 2 leads to the CR gate. **(b)** Schematic level diagram
of the always-on coupling leading to dressed states 01 and
_|_ __
10 with  12 = __ 1 __ 2 . **(c)** Simulations of the expectation
_|_ __ __
values of __ _z_ and __ _y_ for qubit 2 as a drive at the frequency
__ __ __ __ 
of qubit 2 is applied to qubit 1. Upper panel shows regular


Rabi oscillations when qubit 1 is in the 0 state. Bottom
_|_ __
panel shows a modified Rabi frequency when qubit 1 is in 1
_|_ __
state, in accordance with Eq. (135). (d) Difference in angle
in the ( _z, y_ ) plane as a function of length of the applied drive
to qubit 1. At approximately 200 ns __ -phase shift has been
acquired.


_H_ d _,_ 1 =  _V_ d1 ( _t_ ) __ _x_ __ 1 + __ 1 __ 1 __ __ _x_ + __ __ 1 __ _z_ __ __ _x_

(131)


_H_ d _,_ 2 =  _V_ d2 ( _t_ ) 1 __ __ _x_ + __ 2 + __ _x_ __ 1 + __ + 2 __ _x_ __ __ _z_

(132)


where


__ __ _i_ = _g_

__  12


__


_i_ (133)

( __ _i_ __  12 )


This strategy was first demonstrated using fluxtunable transmons in Ref.282, where a Bell state with

+ +
fidelity bell =  __  = 0 _._ 90 was achieved. Using
_F_ __ _|_ _|_ __
quantum process tomography the gate fidelity was found
to be QPT = 0 _._ 81. By moving to fixed-frequency qubits
_F_
with increased lifetimes, the gate fidelity was increased
to QPT = 0 _._ 98 (with subtraction of state initialization
and measurement errors) _F_ 281 . For completeness, we note
that due to the form of the last term in Eq. (131), the
CR gate is also sometimes denoted the ZX __ gate. The
unitary matrix representaion of the CR __ gate is


__ _i_ __ = _g_

__ 


__  12


__ 12 (134)

( __ _i_ __  12 )


and  _V_ d _i_ ( _t_ ) is the driving for qubit _i_ . From Eq. (131),
it is evident that if we drive qubit 1 at the frequency of
qubit 2, then to qubit 2, this will look like a combination
of __ 1 __ 1 __ __ _x_ and __ __ 1 __ _z_ __ __ _x_ . This means that the Rabi
oscillations of qubit 2 will have a frequency given by


 Rabi QB2 =  _V_ d1 __ 1 __ + _z_ 1 __ __ 1 _,_ (135)

where _z_ 1 = __ _z_ 1 , and _z_ 1 depends on the state of qubit  
__ __
1. This effect is demonstrated in Fig. 17(c), where a
simulated drive is applied to qubit 1 while the resulting
Rabi oscillations in qubit 2 are recorded. We have used
typical fixed-frequency transmon parameters from experiments, and we have included a spurious cross-talk term

246,281
__ = 0 _._ 03. . In Fig. 17(d), we plot the difference in
angle in the ( _z, y_ ) plane acquired by qubit 2 for different
initializations of qubit 1,  __ = __ _zy_ 00 __ _zy_ 10 . For this
_|_ __ __ _|_ __
particular choice of parameters, the cross-resonance gate
achieves a __ -phase shift in 200 ns.
__



_i_
_U_ CR __ = _e_ __ 2


2 _i_ __ _z_ __ __ _x_


cos __


_i_ sin __ 2
__


_i_ sin __
__ cos __


_i_ sin __
__ __


(136)


cos __ 2

_i_ sin __


cos __


_i_ sin __ 2

cos __


_i_ sin __


where __ = __ __ __ 1  _V_ d1 ( _t_ ), which can be used to generate a


-----


38

gate times ( __ CPHASE = 30  60 ns and __ CR = 300  400
ns), which to a large extent accounts for the observed
CR gate fidelities. The time scale for CR operation is set
by the frequency detuning, the anharmonicity, and the
coupling strength, through Eq. (133). This has the unfortunate drawback that if qubits do not have intended
frequencies (due to fabrication variation), it will be immediately manifest as longer gate times, and in turn, reduced gate fidelity. As fabrication techniques are becoming more sophisticated and reliable, this problem may be
of reduced importance. However, since the coupling in
the CR scheme is always on, there is an inherent tension
between well-isolated qubits for high-fidelity single-qubit
operations, and coupling qubits, for fast/high-fidelity two
qubit gates.

**_3._** **_Quantum simulation and algorithm demonstrations_**
**_with the CR gate_**

Since the form of the CR Hamiltonian ( __ _z_ __ _x_ ) is
not a ( __ _x_ __ _x_ + __ _y_ __ _y_ )-type interaction (leading to __
_i_ SWAP gate) nor is it an the effective ( __ __ __ _z_ __ _z_ )-type
__
(leading to gate), one could question its applicability to quantum-simulation-type experiments, which CPHASE
often involves terms of the form __ _i_ __ _i_
__
. However, by developing a variational quantum eigensolver routine that
efficiently generates entangled trial states using just the
CR calculated the groundstate energy for H interaction, Kandala 2 , LiH, and BeH _et al._ 288 2 . This experiment was
performed on six fixed-frequency qubits, and it employed
a technique for compact encoding of the Hamiltonians
corresponding to each molecule 289 . As of this writing,
this experiment represents the largest molecule for which
the ground state has been found using a purely quantum
processing approach.
The CR gate is also the native two-qubit gate available
on the IBM Quantum Experience quantum processor 290 ,

291
which is accesible online. Using the IBM Quantum Experience processor, Takita _et al._

292
demonstrated an implementation of a two-logical-qubit (four physical qubit) error detection code . The implementation was inspired
by the proposal of Gottesman , which proposed a minimal experiment to claim observation of fault-tolerant 293
encodings 255 , using a four qubit error detection code in
demonstrated a modified version of the Gottesman encoding, in which two a five qubit setup. Due to constraints on the connectivity, the work by Takita _et al._
logical qubits are initialized, but only one of them in a
fault-tolerant manner. By artificially injecting an error
in the state preparation circuit, the authors demonstrate
that the probability of correctly preparing a fault tolerant
state is greater than the probability of correctly preparing a non-fault-tolerant qubit. This behavior is consistent
with expectations for how fault-tolerant encodings work.
Simultaneously, Vuillot 294 also used the IBM Quantum
Experience machine to study fault-tolerant schemes encoded in that connectivity.


CNOT with the addition of only single-qubit gates,




(137)

|Col1|Z  2|Col3|CR  2|Col5|
|---|---|---|---|---|

||Col2|
|---|---|

|Col1|X  2|Col3|
|---|---|---|
||||



_i/_ 4
up to a phase _e_ .

**_2._** **_Improvements to the CR gate and quantum error_**
**_correction experiments using CR_**


Since qubit 1 is being driven off-resonance, an ac-Stark
shift will add a term __ _z_ 1 to the driving Hamiltonian of
__
qubit 1. The effect of both the spurious ac Stark shift and
the direct __ 1 __ 1 __ _x_ single-qubit rotations was studied in
protocol to effectively echo away the two unwanted contributions from Ref.246. By modifying the original CR
the __ _z_ 1 and 1 __ _x_ terms, the fidelity of the CR gate was

246
improved to CR = 0 _._ 8799 , using quantum process
_F_
tomography. Using interleaved randomized benchmarking of this improved echo-CR-gate (e CR __ __ 2 ), a gate


CR __ __ 2 ), a gate

fidelity of e CR __ = 0 _._ 9347 was achieved. This gate
_F_ __ 2


fidelity of e CR __ = 0 _._ 9347 was achieved. This gate
_F_ __ 2

283
implementation was used to demonstrate two-qubit parity measurements in a three-qubit device , as well as

284
detecting bit-flip and phase-flip errors in a Bell state encoded in a four-qubit device , with gate fidelities from
interleaved randomized benchmarking in the range 0.94
to 0.96. Using a similar device, but with five qubits,
weight-four parity measurement of the forms _ZZZZ_ and

285
_XXXX_ were demonstrated , where the crosstalk to
qubits not involved in the CR gates was studied, leading
to the development of a four pulse e CR 4-pulse scheme.

203
Based on improvements in the analysis of the Hamiltonian describing the CR drive, Sheldon _et al._
subsequently demonstrated a version of the CR
which reduced the gate time to __
= 160 ns and added an active cancellation tone to the e CR previously developed.
Using this active cancellation echo CR  (ace CR ), the
fidelity was increased to ace CR __ = 0 _._ 991, measured
_F_ __ 2


fidelity was increased to ace CR __ = 0 _._ 991, measured
_F_ __ 2

with interleaved randomized benchmarking. The same
sequence without active cancellation on the same qubits
yielded e CR __ = 0 _._ 948. The interested reader may con
_F_ __ 2


yielded e CR __ = 0 _._ 948. The interested reader may con
_F_ __ 2

sult the followup theoretical work 286 with more details
on the effective Hamiltonian models. Other approaches
to fast, high-fidelity cross-resonance gates have also been
proposed 287 . This series of improvements to the original
gate. Although improvements should still be made, with the advent of the gate, superconducting qubit based quantum computing platforms now offer two entangling twoqubit gates that can be used for implementing surfacecode based error correction schemes. cross-resonance implementation has increased the gate fidelity to beyond the threshold for fault-tolerance in a surface code, with similar quality to the CR CPHASE
In the initial experiments using CR gates, the gate
times were significantly longer than the typical CPHASE


-----


39

The two unitaries _U_ _ZZ_ and _U_ _IZ_ _ZI_ only contain terms
__
that commute with _U_ _b_ SWAP ( _, _ ), and their effects can be

280
offset in post-processing . In Eq. (139), __ is the phase
of the drive relative to the single-qubit drive pulses, and
__ =  _B_ _t_ with


Beyond the applications to error-correction and errordetection, the cross-resonance gate has also been employed in early demonstrations of quantum advantages
in machine learning. Rist e _et al._ 295 studied the so-called
learning parity with noise problem, in which one attempts to learn a bit-string **k**
by querying an oracle function _f_ ( **D** _,_ **k** ) = **D** **k** mod 2 with a user-input bit-string
__
**D** . In a first implementation of this problem, the authors
show that for a specific instance of the bit-string **k** = 11 ,
a learner with access to quantum operations needs fewer
queries to the function _f_ . However, by extending the
model of learning parity with noise, the authors demonstrated a consistent advantage of the learner with access
to quantum operations 295 .
gate was also used to demonstrate the implementation of a supervised learning algorithm where the The CR
feature space is encoded as quantum data on the Bloch
sphere 264 . In typical supervised learning, an algorithm

296
is exposed to a training set of labeled data, and is subsequently asked to classify a new, unlabeled set of data .
In the support vector machine (SVM) approach to such
problems, the data is then mapped non-linearly onto the
so-called feature space, in which the trained algorithm
has constructed a separating hyperplane to classify the
data. While a full quantum Support Vector Machine
proposal exists, the algorithm assumes that the data are
already present in a coherent superposition 297 . Instead,
proposed, and demonstrated, that mapping the classical data non-linearly onto the Bloch sphere Havlicek _et al._ 264
can also be utilized to provide a quantum advantage.
For a wider discussion of the important role of quantum
data in many quantum machine learning algorithms, the
reader is referred to Ref.298

**_4._** **_Other microwave-only gates: bSWAP, MAP, and RIP_**

gate (as outlined above) is not the only allmicrowave two-qubit gate available. The CR In particular, the
_b_ SWAP gate 299 is an interesting alternative. The _b_ SWAP
gate directly drives the 00 11
_|_ _|_ __
transition, made possible by interactions with the higher levels of the qubit,
see Fig. 18. Usually, the matrix element for such a
transition is small (3rd order in the coupling strength),
but if the detuning between the qubits is equal to the
anharmonicity, the transition rate is enhanced. Applying a sequence of Schrieffer-Wolff transformations to the
coupled-qubit system, and using a carefully chosen drive
frequency (close to the midpoint of __ q1 and __ q2 ), it can
be shown 280 that the drive gives rise to a unitary operator



2 2

2 _g_  _g_  + __ __ 2 ( __ 1 +  12 ) + __ 1 ( __ 2  12 )
 _B_ = __ __ 2 __

 ( __ 1 +  12 )( __ 2 __  12 ) 12



2
( __ 1 +  12 )( __ 2 __  12 ) 12


(140)
where is the amplitude of the drive, is a dimensionless parameter quantifying the coupling coefficient __
of the drive to qubit 2 in units of coupling strength
to qubit 1, and __  = __ 1 + __ 2 . Explicit derivations
leading to Eq. (138) can be found in the supplement
of Ref.299. By applying _U_ _b_ SWAP for a time that yields
__ = _/_ 2, and with __ = 0, the resulting gate is denoted
_b_ SWAP and can act as the entangling gate (together with
single-qubit gates) that forms a universal gate set. Moreover, the power of the _b_ SWAP becomes apparent when
one applies it for the time that yields __ = _/_ 4, which
from the ground state 00
directly produces the entangled Bell state 00 + _|_ _e_ _i_ __ 11 .
_|_ __ _|_ __
In line with the definition of __ _i_ SWAP , this gate is denoted the __ _b_ SWAP . In


_i_ SWAP , this gate is denoted the _b_ SWAP . In

the work by Poletto _et al._ 299 , the fidelity of the _b_ SWAP
gate was _b_ SWAP = 0 _._
_F_
9 (determined from quantum process tomography). The main source of error was the increased dephasing during the relatively long high-power
pulse needed to drive the 00 11 transition. The
_|_ _|_ __
_b_ SWAP gate can be viewed as the superconducting qubit
analogue of the MlmerSrensen gate 300 . In Fig. 18, we
outline the level diagram of two coupled qubits, along
with the higher levels of the qubits. The arrows indicate
which coupled states are utilized to implement the corresponding gate. As an application of the _b_ SWAP gate,
Colless _et al._ 301 used this gate to calculate energies of
the excited states of a _H_ 2 molecule using a two-qubit
transmon processor 301 .
Another all-microwave gate is the so-called
microwave-activated CPHASE  (or  MAP  for short) 70 .
The MAP gate is in spirit similar to the CPHASE gate,
where noncomputational states are used to impact a
conditional phase inside the computational subspace.
In contrast to CPHASE , the MAP gate is implemented
without tuning individual qubit frequencies. Rather,
the canonical implementation of this gate comprises two
fixed-frequency qubits, where the frequencies are carefully designed (and fabricated), such that the 12 and
_|_ __
03 levels are resonant. This leads to a splitting of the
_|_ __
otherwise degenerate 02 01 , and 12 11
_|_ _|_ __ _|_ _|_ __
transitions. By driving near resonance with the _n_ 2 _n_ 1
_|_ _|_ __
transition, an effective __ _z_ __ _z_ interaction is generated.
__
In a setup comprising two fixed-frequency qubits, the
MAP gate was used to implement the unitary


_i_ SWAP , this gate is denoted the


_U_ = _U_ _b_ SWAP ( _, _ ) _U_ _ZZ_ _U_ _IZ_ __ _ZI_ (138)


with



_i_ 2 __
cos __ 0 0 __ _ie_ __ sin __
0 1 0 0
0 0 1 0

_i_ 2 __
__ _ie_ __ sin __ 0 0 cos __


_U_ _b_ SWAP ( _, _ ) =



__
_U_ MAP = exp _i_ __ _z_ __ _z_ _,_ (141)
__ 4 __



__
_U_ MAP = exp _i_
__ 4


 _,_

(139) 


with a gate fidelity MAP = 0 _._
_F_ 70
87 (determined via quantum process tomography) in a time __ MAP = 514 ns .


-----


40

bus, __ is the dispersive shift, and  cd is the detuning of
the drive (d) from the cavity (c). By choosing _t_  = _/_ 4, it
is possible to implement the CPHASE gate. The power of
the RIP gate lies in its capability to accommodate large
differences in qubit frequencies. To demonstrate this,
Paik performed two-qubit randomized benchmarking between pairs of qubits in a four-qubit device _et al._ 304
with frequency differences spanning 0 _._ 38 GHz to 1 _._ 8 GHz,
all with fidelities in the range 0.96-0.98 and gate times in
the range 285 to 760 ns.

**H.** **Gate implementations with tunable coupling**

Finally, we briefly review tunable coupling architectures, which have recently emerged as a promising alternative.
The idea is to engineer an effective qubitqubit coupling _g_
that is tunable (typically by applying a flux), and such gates are referred to as parametric gates. This can be implemented in two different

ways: ( _i_ ) The coupling strength between two qubits is

199,208,305307
tuned by a flux, _g_ _g_ (( _t_ )) , or ( _ii_ ) the
__
resonant frequency of the coupling element is modified

91,107,308312
__ coupler __ __ coupler (( _t_ )) , with a fixed _g_ ,
leading to an effective time-dependent coupling parameter. When the tunable coupling element is driven at
frequencies corresponding to the detuning of the qubits
from the coupler, an entangling gate can be implemented.
In a setup of type ( _ii_ ), an implementation of the
_i_ gate was demonstrated by parametrically driving a flux-tunable coupler between two fixed-frequency SWAP

63
qubits , yielding a fidelity _i_ SWAP = 0 _._
_F_
9823 (using interleaved randomized benchmarking) in a time __ = 183 ns.
Similarly, the _b_ SWAP (and _i_ SWAP ) gates were recently
demonstrated, using a flux-tunable transmon connecting two fixed-frequency transmons. Driving the flux
through the tunable qubit at the sum frequency of the
fixed-frequency transmons results in the _b_ SWAP 105 gate.
This parametrically driven approach is generally significantly faster than implementations relying solely on
fixed-frequency qubits.
A hybrid approach, in which a combination of tunable

67,106,212
and fixed-frequency qubits is used, was recently demonstrated for both _i_ SWAP and CPHASE gates .
This scheme has no added tunable qubits (or resonators)
acting as the coupling element, but rather, relies solely
on an always-on capacitive coupling between the qubits,
and the effective coupling is roughly half that of the
always-on coupling. The operational principle here is
to modulate the frequency of the tunable qubit (using
local flux control) at the transition frequency correponding to 01 10 for _i_ SWAP and 11 02 for
_|_ _|_ __ _|_ _|_ __
CPHASE . Using interleaved randomized benchmarking,
the authors demonstrated _i_ SWAP = 0 _._ 94 ( __ = 150 ns),

02 _F_ 20
and _F_ CPHASE = 0 _._ 93 ( __ = 210 ns) and _F_ CPHASE = 0 _._ 88
( = 290 ns), showing a slight asymmetry in the direction in which the is applied. This hybrid technique was used in Ref.67 to demonstrate a four-qubit __ CPHASE

|E a E b computational subspace|Col2|
|---|---|
|||


FIG. 18. Schematic of the level structure of two coupled
qubits (including higher levels) with indication of the transitions utilized in the _i_ SWAP , _b_ SWAP , CPHASE and MAP
gate. See text for details. Figure inspired from Ref. 70.

As the number of qubits in a system increase, one drawback of this gate is the need for a precise matching of
higher energy levels across multiple qubits, while simultaneously avoiding spurious couplings to other modes in
the system.
gates all have quite stringent requirements on the spectral landscape of the qubits The CR , _b_ SWAP and MAP
in order to obtain fast, efficient gate operation. To
address this issue, another all-microwave gate was developed, the so-called resonator induced phase gate
( RIP ) 302,303 . The RIP gate operates by coupling two
fixed-frequency qubits to a bus cavity, from which they
are far detuned. By adiabatically applying and removing
an off-resonant pulse to the cavity, the system undergoes
a closed loop in phase space, after which the cavity is
left unchanged, but the qubits acquire a state-dependent
phase. By a careful choice of the amplitude and detuning
of the pulse, and taking into account the dispersive shift
of the cavity, a CPHASE gate can be implemented on the
two qubits. This effect was experimentally demonstrated
by Paik _et al._ 304 in a 3D transmon system 55 , where four
qubits are coupled to the same bus. In this setup, the
RIP gate operation results in unitaries with weight on all
four qubits simultaenously. In order to isolate just the
desired two-qubit coupling terms, Paik _et al._ developed
a refocused RIP (r RIP ) gate that implements


_U_ rRIP = exp _i_ __  _z_ __ _z_ _t_ _,_ (142)
__ __

where the coupling rate (for an unmodulated drive) scales  
as


__  _|_  _V_ d _|_
__ 2 cd



2 cd





_,_ (143)
 cd


where  _n_ denotes the average number of photons in the


_n_ 



-----


41

Jaynes-Cummings Hamiltonian , previously introduced in Sec. II, 315317


GHZ state with fidelity 4 qubit GHZ = 0 _._ 79 (using state
_F_
tomography). Finally, this gate-architecture was used to
demonstrate a hybrid quantum/classical implementation
of an unsupervised learning task (determining clustering
of data), using nineteen qubits and supplemented by a
classical computer as part of the minimization loop 313 .

**V.** **QUBIT READOUT**

The ability to perform fast and reliable (high fidelity)
readout of the qubit states is an important cornerstone
of any quantum processor 3 .
In this section, we give a brief introduction to how
readout is performed on superconducting qubits. We
start by reviewing the fundamental theory behind _dispersive readout_  the most common readout technique used
today in the circuit QED architecture  in which each
qubit is coupled to a readout resonator. In the dispersive
regime, i.e. when the qubit is detuned from the resonator
frequency, the qubit induces a state-dependent frequency
shift of the resonator from which the qubit state can be
inferred by interrogating the resonator.
Dispersive readout allows us to map the quantum degree of freedom of the qubit onto the classical response of
the linear resonator, thus transforming the readout optimization process into obtaining the best signal-to-noise
ratio (SNR) of the microwave signal used to probe the
resonator.
We then provide guidance on how to optimize system
parameters to perform high-fidelity, single-shot readout.
After choosing parameters, such as resonant frequencies
and coupling rates, we address the filter and amplifier
circuitry positioned in-between the qubit plane and the
data aquisition hardware outside of the dilution refriderator. On this note, we review the basic principles of
Purcell filters as well as parametric amplifiers, both of
which are necessary to obtain fast, high-fidelity readout
in scaled-up quantum processors.

**A.** **Dispersive readout**

A quantum measurement can be described as an
entanglement of the qubit degree of freedom with a

314
pointer variable of a measurement probe with a quantum Hamiltonian , followed by classical measurement
of the probe. In circuit QED, the qubit (the quantum system) is entangled with an observable of a superconducting resonator (the probe), see Fig. 19(a), allowing us to
gain information about the qubit state by interrogating
the resonator  rather than directly interacting with the
qubit. Therefore, the optimization of the readout performance is translated to maximizing the signal-to-noise
ratio of a microwave probe tone sent to the resonator,
while minimizing the unwanted _back-action_ on the qubit.
The qubit-resonator interaction is described by the



1
_a_ __ _a_ +



q

__ _z_ + _g_ __ + _a_ + __ _a_ __ _,_ (144)
2 __
 


_H_ JC = __


+ __ q


where __ _r_ and __ q
denote the resonator and qubit frequencies, respectively, and _g_ is the transverse qubit-resonator
coupling rate. The operators __ + and __ represent the
__
processes of exciting and de-exciting the qubit, respectively.
In the limit when the detuning between the qubit and
the resonator is small compared with their coupling rate,
i.e. = _|_ __ q __ __ _r_ _| _ _g_ , the energy levels of the two
systems hybridize and a vacuum Rabi splitting of frequency _ng/_ opens up, where _n_ = 1 _,_ 2 _,_ 3 _..._ denotes the
__
resonator mode. In this regime, excitations are coherently swapped between the two systems. Although useful for certain two-qubit gate operations, recall Sec. IV E,
such transverse interactions change the qubit state (since
energy is directly exchanged between the resonator and
the qubit) and is therefore not desired in the context of
_quantum non-demolition_ (QND) readout, in which the
outcome of the quantum measurement is not altered in
the act of reading out the system.
In the dispersive limit, i.e., when the qubit is far detuned from the resonator compared with their coupling
rate _g_ and the resonator linewidth __ ,  _g, _ , there
__
is no longer a direct exchange of energy between the
two systems. Instead, the qubit and resonator push
each others frequencies. To see this, the Hamiltonian
can be approximated using second-order perturbation

215,318
theory in terms of _g/_ , taken in the limit of few
photons in the resonator. This is known as the _dispersive approximation_ , after which the Hamiltonian takes
the form



1
_a_ __ _a_ +

2




+ __ q

2




_H_ disp = __ _r_ + __ _z_


q

2 __ _z_ _,_ (145)



2
where __ = _g_ _/_ is the qubit-state dependent frequency
shift, a so-called , see Fig. 19(b), allowing us to distinguish the two qubit states. _dispersive shift_ This is an
asymptotically longitudinal interaction, yielding a QND
measurement.

2
Note that, in addition, the qubit frequency also picks up a , induced by the vacuum fluctuations in the resonator. Also _Lamb shift_ , __ q = __ q + _g_ _/_


note that the dispersive Hamiltonian in Eq. (145) is derived for a two-level atom . Taking the second excited
state into account and introducing the anharmonicity


 In reality, superconducting qubits, just like natural atoms, have
higher energy levels. These higher levels are outside of the computational subspace, but need to be taken into account for most
qubit simulations to get accurate predictions of frequency shifts.


-----


42


(a)

![qe-guide-scqubits-oliver.pdf-41-0.png](qe-guide-scqubits-oliver.pdf-41-0.png)

(b)


SIGNAL CREATION SIGNAL DETECTION


(a)



0.2

0.1

0.0

-0.1

-0.2

0

-2

-4

-6

-8

|/2|= 0 /2|= EC/h|
|---|---|---|
|g/2 = 50 MHz g/2 = 100 MHz|||
||SSttrraaddddlliinngg rrreeegggiiimmmeee||


(b)


-0.4 -0.2 0.0 0.2 0.4

Frequency detuning, _/2_ (GHz)


![qe-guide-scqubits-oliver.pdf-41-7.png](qe-guide-scqubits-oliver.pdf-41-7.png)

![qe-guide-scqubits-oliver.pdf-41-9.png](qe-guide-scqubits-oliver.pdf-41-9.png)

![qe-guide-scqubits-oliver.pdf-41-10.png](qe-guide-scqubits-oliver.pdf-41-10.png)

![qe-guide-scqubits-oliver.pdf-41-8.png](qe-guide-scqubits-oliver.pdf-41-8.png)

|Col1|50 MHz|Col3|Col4|
|---|---|---|---|
|g/2 = g/2||||


-10
-2.0 -1.5 -1.0 -0.5 0.0


![qe-guide-scqubits-oliver.pdf-41-3.png](qe-guide-scqubits-oliver.pdf-41-3.png)

![qe-guide-scqubits-oliver.pdf-41-5.png](qe-guide-scqubits-oliver.pdf-41-5.png)

![qe-guide-scqubits-oliver.pdf-41-4.png](qe-guide-scqubits-oliver.pdf-41-4.png)

![qe-guide-scqubits-oliver.pdf-41-6.png](qe-guide-scqubits-oliver.pdf-41-6.png)

Frequency detuning, _/2_ (GHz)


FIG. 20. **(a)** Dispersive frequency shift _/_ 2 __ as a function
of qubit-resonator detuning  _/_ 2 __ , according to Eq. (146),
for a transmon qubit with anharmonicity _/_ 2 __ = _E_ _C_ _/h_ =
__
300 MHz, for qubit-resonator coupling rates _g/_ 2 __ = 50 MHz
__
(blue) and _g/_ 2 __
= 100 MHz (red). The two vertical asymptotes at  _/_ 2 __ = 0 and  _/_ 2 __ = _E_ _C_ divides the dispersive
shift into three regimes; For  _/_ 2 _ <_ 0, and  _/_ 2 _ > E_ _C_ _/h_ ,
the dispersive shift is negative and _/_ 2 __ 0 __ as  .
__ __
For 0 _<_  _/_ 2 _ < E_ _C_ _/_ 2 __ , the dispersive shift _/_ 2 _ >_ 0. This
Zoomed-in plot for negative qubit-resonator detuning, the most commonly used operating regime. is called the _straddling regime_ 52 . **(b)**

which for a transmon qubit with _ <_ 0 implies that the
dispersive shift will depend on the detuning. This effect is plotted in Fig. 20(a), where the second energy
level manifests itself as a second vertical asymptote at
 _/_ 2 __ = _E_ _C_ _/h_ . It is also worth noting that for qubit
modalities with positive anharmonicity, e.g. flux qubits,
the dispersive shift will also shift the sign 62 .
In the small photon-number limit, the interaction term
of the Hamiltonian in Eq. (145) commutes with the qubit

 314
observable , __ _z_ , resulting in a QND measurement .
This is an important condition for many applications in
quantum information processing.
In the case when the resonator photon number _n_ = _a_ __ _a_

2 2
exceeds a _critical photon number_ _n_ _c_  _/_ (4 _g_
__
), the dispersive Hamiltonian in Eq. (145) is no longer a valid
approximation Therefore, the critical photon number sets an upper bound for the power level 215,319,320 .

 This commutation is approximate and has an asyptotic dependence
on the qubit-resonator detuning


(c)


1.0

0.5

0.0

-

-2

|/2|2|/2|Col4|Col5|
|---|---|---|---|---|
||||||
||||||


![qe-guide-scqubits-oliver.pdf-41-17.png](qe-guide-scqubits-oliver.pdf-41-17.png)

![qe-guide-scqubits-oliver.pdf-41-12.png](qe-guide-scqubits-oliver.pdf-41-12.png)

![qe-guide-scqubits-oliver.pdf-41-16.png](qe-guide-scqubits-oliver.pdf-41-16.png)

![qe-guide-scqubits-oliver.pdf-41-15.png](qe-guide-scqubits-oliver.pdf-41-15.png)

![qe-guide-scqubits-oliver.pdf-41-14.png](qe-guide-scqubits-oliver.pdf-41-14.png)

![qe-guide-scqubits-oliver.pdf-41-11.png](qe-guide-scqubits-oliver.pdf-41-11.png)

![qe-guide-scqubits-oliver.pdf-41-13.png](qe-guide-scqubits-oliver.pdf-41-13.png)

![qe-guide-scqubits-oliver.pdf-41-1.png](qe-guide-scqubits-oliver.pdf-41-1.png)

-2 -1 0 1

Frequency, __ RF _- _ r (a.u)


-2 -1


![qe-guide-scqubits-oliver.pdf-41-2.png](qe-guide-scqubits-oliver.pdf-41-2.png)

FIG. 19. Simplified schematic of a representative experimental setup used for dispersive qubit readout. **(a)**
The resonator probe tone is generated, shaped and timed using an
arbitrary waveform generator (AWG), and sent down into the
cryostat. The reflected signal _S_ 11
is amplified, first in a parametric amplifier and then in a low-noise HEMT amplifier,
before it is downconverted using heterodyne mixing and finally sampled in a digitizer. **(b)** Reflected magnitude _|_ _S_ 11 _|_
and phase __ response of the resonator with linewidth __ , when
the qubit is in its ground state 0 (blue) and excited state 1
_|_ __ _|_ __
(red), separated with a frequency 2 _/_ 2 __ . **(c)** Corresponding
complex plane representation, where each point is composed
of the in-plane Re[ _S_ 11 ] and quadrature Im[ _S_ 11 ] components.
The highest state discrimination is obtained when probing the
resonator just in-between the two resonances, (dashed line in
(b)), thus maximizing the distance between the states.

1 2 0 1
__ = __ q __ __ __ q __
modifies the expression for the dispersive shift:



__ 12
__ = __ 01 +



2
= _g_ 01
__ 


1 +  _/_


(146)


__ IF


-----


43

![qe-guide-scqubits-oliver.pdf-42-0.png](qe-guide-scqubits-oliver.pdf-42-0.png)

FIG. 21. Schematic of an I-Q mixer. A readout pulse at
frequency __ RO enters the RF port, where it is equally split
into two paths. A local oscillator at frequency __ LO enters
the LO port, where it is equally split into two paths, one
of which undergoes a _/_ 2-radian phase rotation. To perform
analog modulation, the two signals in each path are multiplied
at a mixer, yielding the outputs _I_ ( _t_ ) and _Q_ ( _t_ ), each having
frequencies __ RO __ LO . _I_ ( _t_ ) and _Q_ ( _t_ ) are then low-pass-filtered
__
(time averaged) to yield _I_ IF ( _t_ ) and _Q_ IF ( _t_ ) at the intermediate
frequency __ IF = __ RO __ LO , and subsequently digitized using
_|_ __ _|_
an analog-to-digital (ADC) converter. If __ IF = 0, then digital
__
signals _I_ IF [ _n_ ] and _Q_ IF [ _n_ ] are further digitally demodulated
using digital signal processing (DSP) techniques to extract
the amplitude and phase of the readout signal.

maximal when the resonator is probed just in-between
the two qubit-state dependent resonance frequencies 163 ,
__ RF = ( __ _r_ _|_ 0 __ + __ _r_ _|_ 1 __ ) _/_ 2. In this case, the reflected magni
tude is identical for 0 and 1 , and all information about
_|_ __ _|_ __
the qubit state is encoded in the phase __ , see dashed
line in Fig. 19(b). In turn, the qubit-resonator detuning should be designed to obey the criterion for maximal
state visibility, __ = _/_ 2, which is maximized for phase
measurements while constraining qubit dephasing.
Once we have picked the resonator probe frequency, the
quantum dynamics of the qubit can be mapped onto the
phase of the classical microwave response. In the following, we discuss how we can use heterodyne detection to
measure the phase of the resonator response. We assume
that the reader is already somewhat familiar with basic
mixer operations, such as modulation and de-modulation
of signals. For interested readers, we refer to Ref. 326.

**_1._** **_Representation of the readout signal_**

A readout event commences with a short microwave
tone directed to the resonator at the resonator probe frequency __ RO . After interacting with the resonator, the
reflected (or transmitted) microwave signal has the form

_s_ ( _t_ ) = _A_ RO cos( __ RO _t_ + __ RO ) _,_ (148)



of the resonator probe signal to maintain (an approximate) QND measurement . This limitation could be
lifted by implementing a pure (and not only approximate) QND readout using a manifestly longitudinal coupling between a qubit and the resonator. Several groups
are currenly pursuing the implementation of _longitudinal_
_readout_ , in which QND readout could be performed even
with larger number of resonator photons, thus improving
the SNR 108,322,323 .
We can also interpret the dispersive qubit-resonator
interaction in another way; by rearranging the terms in
Eq. (145), we can equivalently write


_H_ disp = __ _r_



1
_a_ __ _a_ +



1
+



2
_g_
__ q +



2
2 _g_



_a_ __ _a_

ac-Stark shift



__ _z_ _,_


Lamb shift



(147)
where the bare qubit frequency is shifted by a fixed

2 
amount _g_ _/_ , known as the _Lamb shift_ as well as an

52,215
amount proportional to the number of photons populating the resonator _acStark shift_ . It has the consequence that photon number . This effect is known as the
fluctuations (noise) in the resonator induce small shifts
of the qubit frequency, slightly bringing the qubit out of
its rotating frame and thus causing dephasing 147 . This
means that spurious photon occupation and fluctuation
in the resonator, be it thermal or coherent photons, shift
the qubit frequency and causing dephasing 319,324 . For

107
this reason, it is important to make sure that the processor is properly thermalized , and its control lines well
filtered 325 and attenuated 148 , to reduce photon number
fluctuation.


**B.** **Measuring the resonator amplitude and phase**

In the previous section, we outlined the underlying
physics behind the dispersive readout technique, in which
we concluded that the qubit induces a state-dependent
frequency shift of the resonator. We now focus our attention on how to probe the resonator to read out the
qubit, that is, best distinguish the two classical resonator signatures corresponding to our qubit states, see
Fig. 19(b)-(c).
The readout circuit can be set up in measuring either reflection or transmission. The best state discrimination is obtained by maximizing the separation between the two states in the ( the inphase and quadrature component of the voltage, see _I, Q_ )-plane, i.e.
Fig. 19(c). It can be shown that this separation is


 It has been demonstrated that it is still possible to read out the

321
qubit state by applying a very strong resonator drive tone, eventhough this readout scheme is not QND

 It is worth mentioning that the observed qubit frequency is always
the Lamb-shifted frequency and not the bare qubit frequency.


-----


44

operation is a combination of a balanced (50-50) beamsplitter followed by optical photodetectors, as shown in
the inset of Fig. 22(a). The signal and local-oscillator optical fields are first combined at the beamsplitter, yielding superpositions of both fields, and then detected at
the photodetectors, which act as square-law devices. To
build intuition for how this works, tbe square of the sum

2 2 2
of two electric fields ( _E_ 1 + _E_ 2 ) = _E_ 1 + _E_ 2 + 2 _E_ 1 _E_ 2 has
a cross term that is the multiplication of the two fields.
We refer the reader to Ref. 327 for further details.

**_3._** **_Homodyne demodulation_**

One direct means to extract _I_ and _Q_ is to perform a
microwave _homodyne_ measurement using an analog I-Q
mixer of the type shown in Fig. 21. In an analog homodyne measurement, the local oscillator (LO) is chosen to
be at the carrier frequency __ LO = __ RO . Upon mixing, _I_ ( _t_ )
and _Q_ ( _t_ ) contain terms at both DC ( __ IF = 0) and terms
at twice the carrier frequency. Time-averaging (filtering)
_I_ ( _t_ ) and _Q_ ( _t_ ) directly yield the DC terms _I_ _IF_ ( _t_ ) = _I_ and
_Q_ _IF_ ( _t_ ) = _Q_ :


where __ RO is the _carrier frequency_
used to probe the resonator. are, respectively, the qubit-statedependent amplitude and phase that we want to measure. _A_ RO and __ RO
One can equivalently use a _complex analytic representation_ of the signal,


_s_ ( _t_ ) = Re _A_ RO _e_ _j_ ( __ RO _t_ + __ RO ) _,_ (149)
 


= Re _A_ RO cos( __ RO _t_ + __ RO ) + _j_ sin( __ RO _t_ + __ RO )
_{_ _}_


where Re takes the real part of an expression, e.g.,
Re[exp( _jx_ )] = Re(cos _x_ + _j_ sin _x_ ) = cos _x_ .
To gain intuition, we can rewrite Eq. (149) in a static
phasor notation that separates out the time dependence exp( _j_ RO _t_ ),


_s_ ( _t_ ) = Re



_A_ RO _e_ _j_ RO _e_ _j_ RO
phasor

exp(   _j_  RO )  _A_ RO



_,_ (150)



 __ RO


where the phasor _A_ RO exp( _j_ RO ) __ _A_ RO  __ RO
is a shorthand that fully specifies a harmonic signal _s_ ( _t_ ) at a known
frequency __ RO . To perform qubit readout, we want to
measure the in-phase component _I_ and a quadrature
component _Q_ of the complex number represented by the
phasor,


_T_

0





1
_I_ =


_dt s_ _I_ ( _t_ ) _y_ _I_ ( _t_ )


_A_ RO _e_ _j_ RO = _A_ RO cos __ RO + _jA_ RO sin __ RO (151)
_I_ + _jQ_ (152)
__

to determine the amplitude _A_ RO and the phase __ RO .


_A_ RO _e_ _j_ RO = _A_ RO cos __ RO + _jA_ RO sin __ RO (151)
_I_ + _jQ_ (152)
__


= _A_ RO _A_ LO


cos( __ RO ) _,_ (153)


_T_

0





1
_Q_ =


_dt s_ _Q_ ( _t_ ) _y_ _Q_ ( _t_ )


= _A_ RO _A_ LO


**_2._** **_I-Q mixing_**

One direct means to extract _I_ and _Q_ is to perform a
_IQ mixer_ _homodyne_ . Figure or _heterodyne_ 21 shows a basic electrical schematic measurement using an analog
of an I-Q mixer. The readout signal _s_ ( _t_
) and a reference local-oscillator signal _y_ ( _t_ ) = _A_ LO cos __ LO _t_ are fed
into the mixer via the RF and LO mixer ports. The
mixer then equally splits the signal and local oscillator
into two branches and multiplies them in the following
way: in the _I_ -branch, the signal _s_ _I_ ( _t_ ) = _s_ ( _t_ ) _/_
2 is multiplied by the local oscillator _y_ _I_ ( _t_ ) = ( _A_ LO _/_ 2) cos __ LO _t_ ;
and in the _Q_ -branch, the signal _s_ _Q_ ( _t_ ) = _s_ ( _t_ ) _/_
2 is multiplied by a _/_
2-phase-shifted version of the local oscillator, _y_ _Q_ ( _t_ ) = ( _A_ LO _/_ 2) sin __ LO _t_ . The - sign arises from
__
the choice of using a _A_ (cos _t_ + __ ) as the reconstructed
real signal. At the _I_ and _Q_ ports, the output signals _I_ ( _t_ )
) contain terms at the sum and difference frequencies, generally referred to as an and _Q_ ( _t_ _intermediate frequency_ ,
__ IF = __ RO __ LO
__
. The resulting signals are low-pass filtered, passing only the terms at the difference frequency,
_I_ _IF_ ( _t_ ) and _Q_ _IF_ ( _t_ ), which are then digitized. After digital
signal processing, one obtains the static in-phase ( _I_ ) and
quadrature ( _Q_ ) components, from which one calculates
the amplitude _A_ RO and the phase __ RO .
Microwave mixers use square-law-type diodes to implement multiplication. The optical analog of a mixer


sin( __ RO ) _,_ (154)


where _T_
is a time interval taken to be an integer number of periods of the readout signal. _I_ and _Q_ are then
sampled and used to calculate the amplitude and phase:



2 2

_A_ RO _I_ + _Q_ _,_ (155)
__

__ RO = arctan(  _Q/I_ ) _._ (156)


Note that the global value of _A_ RO or __ RO
is not what matters; what matters is the _change_ in _A_ RO and __ RO between
the qubit being in state 0 and state 1 . For example,
__ __
the value of _A_ leaving the resonator and the value _G_ _A_
__
reaching a measurement stage are different, where represents the net gain in the measurement amplifier chain. _G_
However, the gain is the same, independent of the qubit

(0)
state, whereas (1) _A_ may be different, e.g., _A_ RO = _G_ __ _A_ _|_ 0 __
or _A_ RO = _G_ __ _A_ _|_ 1 __ . Similarly, the propagation phase
__
accumulated while a signal travels between the resonator and the measurement stage is also independent
of the qubit state, and simply imparts a phase offset to

(0)
the qubit-induced phase shift, e.g., __ RO = __ _|_ 0 __ + __ or

(1)
__ RO = __ _|_ 1 __ + __ .
Homodyning works in principle, but there are two
drawbacks. First, signals directly demodulated to DC
may be subject to lower signal-to-noise ratios, since they


-----


45


(a)


ANALOG DEMOD.


(b) DATA SAMPLING (c) DIGITAL SIGNAL PROCESSING (DSP)




-1

1

0

-1

|Col1|DATA SAMPL|
|---|---|
|| rd|
|||
|||
|||
|||
|||


![qe-guide-scqubits-oliver.pdf-44-6.png](qe-guide-scqubits-oliver.pdf-44-6.png)

![qe-guide-scqubits-oliver.pdf-44-5.png](qe-guide-scqubits-oliver.pdf-44-5.png)

![qe-guide-scqubits-oliver.pdf-44-4.png](qe-guide-scqubits-oliver.pdf-44-4.png)

![qe-guide-scqubits-oliver.pdf-44-3.png](qe-guide-scqubits-oliver.pdf-44-3.png)

![qe-guide-scqubits-oliver.pdf-44-2.png](qe-guide-scqubits-oliver.pdf-44-2.png)

![qe-guide-scqubits-oliver.pdf-44-0.png](qe-guide-scqubits-oliver.pdf-44-0.png)

![qe-guide-scqubits-oliver.pdf-44-1.png](qe-guide-scqubits-oliver.pdf-44-1.png)

FIG. 22. Schematic of the heterodyne detection technique. **(a)** The signal with frequency __ RF from the cryostat is mixed with
a carrier tone with frequency __ LO , yielding two quadratures at a down-converted intermediate frequency __ IF = __ RO __ LO , and
90 __ out-of-phase with each other. **(b)** The two signals are passed into two different analog-to-digital converter (ADC) channels. _|_ __ _|_
To avoid sampling the resonator transient, some readout delay ( __ _rd_ ) corresponding to the resonator linewidth may be added,
and the two signals are sampled for a time __ _s_ . In this case, the white dots represent the sampled points. **(c)** The sampled
traces are post-processed and after some algebra, the sampled data points are averaged into a single point in the ( _I, Q_ )-plane.
To extract statistics of the readout performance, i.e. single-shot readout fidelity, a large number of ( _I, Q_ )-records are acquired,
yielding a 2D-histogram, with a Gaussian distributed spread given by the noise acting on the signal.


fight against 1 _/f_ electronics noise, as well as any other
noise signals that may have inadvertently been demodulated (e.g., via a square-law detector). The second is
that homodyning is not compatible with frequency division multiplexing (FDM), where a single pulse can be
used to interrogate _N_ resonators at different frequencies
by applying tones at each resonator frequency using the
superposition principle, e.g.,


**_4._** **_Heterodyne demodulation_**

In a heterodyne scheme, a local oscillator at frequency
__ LO is offset by an intermediate frequency __ IF to target a
unique readout frequency __ RO . Up-conversion techniques
such as single-sideband modulation with suppressed carrier (SSB-SC) using balanced I-Q mixers (operated in reverse compared with Fig. 21) are commonly used to create such readout signals. We refer the reader to Ref. 326
for more information on how to create such pulses.
Here, we want to extract _A_ RO and __ RO (or their scaled
and offset versions) from the reflected/transmitted tone
using a heterodyning scheme. The first step is to perform analog I-Q mixing, as illustrated in Fig. 22(a). In
contrast to the homodyning case, here, the local oscillator and readout tone are at different frequencies,
__ IF = __ RO __ LO _>_ 0.
Mixing the LO and RO signals yields the signals _|_ __ _|_ _I_ ( _t_ ) and _Q_ ( _t_ ) with terms at both
sum and difference frequencies. Filtering out the sum frequencies using low-pass filtering (time averaging) yields



( _i_ ) ( _i_ ) ( _i_ )
_A_ RO cos( __ RO _t_ + __ ) _._ (157)
_i_ =1


_s_ ( _t_ ) =


Homodyning an FDM signal will put _all_ resonator signals
at DC, and once downconverted, they cannot be differentiated. To work around this, it is generally advantageous
to use _heterodyning_ , which uses a two-step demodulation
process via an intermediate frequency __ IF . Such a scheme
is easily compatible with the concept of FDM, because a

( _i_ )
readout signal is first demodulated to unique IF frequencies __ IF , and then digitally demodulated to extract each

( _i_ ) ( _i_ )
_A_ RO and __ . In the following, we will consider _N_ = 1
for simplicity, but the process is applicable to larger _N_
provided the frequencies a sufficiently spaced to avoid
interference with one another during the demodulation
process.


LO


-----


46

Fig. 22(c-d),


the IF signals:

1
_I_ IF ( _t_ ) =


_T_

0




( _dt_ ) _s_ _I_ ( _t_ ) _y_ _I_ ( _t_ )


_z_ IF [ _n_ ] = _I_ IF [ _n_ ] + _jQ_ IF [ _n_ ] _V_ _I_ [ _n_ ] + _jV_ _Q_ [ _n_ ] (164)
__


= _A_ RO _A_ LO



[cos( IF _n_ + __ RO ) + _j_ sin( IF _n_ + __ RO )]

(165)

_e_ _j_ RO _e_ _j_  IF _n_ (166)


= _A_ RO _A_ LO


cos( __ IF _t_ + __ RO ) (158)


_T_

0





1
_Q_ IF ( _t_ ) =


( _dt_ ) _s_ _Q_ ( _t_ ) _y_ _Q_ ( _t_


= _A_ RO _A_ LO


where the digital in-phase and quadrature signals are represented here as the voltages _V_ _I_ [ _n_ ] and _V_ _Q_ [ _n_ ] sampled
by the ADC, and we have separated the static phasor
( _A_ RO _A_ LO _/_ 8) exp[ _j_ RO ] from the rotating term exp[ _j_  IF _n_ ].
One can digitally demodulate the time series _z_ IF [ _n_ ] by
multiplying by the complex conjugate of the oscillatory
exponential,

_z_ [ _n_ ] = _z_ IF [ _n_ ] _._ _e_ __ _j_  IF _n_ (167)
__

where _._ indicates a point-by-point multiplication, and
__
the result is a vector of length _M_ of nominally identical
values of the phasor  one for each sample point  with a
small amount of additive noise due to noise in measurement chain, digitization errors, etc. A singular phasor
value is then estimated by taking average,


= _A_ RO _A_ LO


sin( __ IF _t_ + __ RO ) _._ (159)


As before, we have omitted any offset phases from the
LO or from the wave propagation between the resonator
and the measurement. Again, these offset values are not
what matters; it is the change in _A_ RO and __ RO with a
change in qubit state that allows state discrimination.
The analog-demodulated _I_ IF ( _t_ ) and _Q_ IF ( _t_
) are now oscillating at a frequency that is generally low enough to
be digitized using commonly available analog-to-digital
converters (ADCs). The resulting digital signals are now
written as _I_ IF [ _n_ ] and _Q_ IF [ _n_ ],



_A_ RO _A_ LO
_I_ IF [ _n_ ] = 8

_A_ RO _A_ LO
_Q_ IF [ _n_ ] =


cos( IF _n_ + __ RO ) (160)

sin( IF _n_ + __ RO ) _,_ (161)



1
_z_  [ _n_ ] =


_z_ [ _n_ ] (168)


= _A_ RO _A_ LO


_e_ _j_ RO _._ (169)


where _n_ = _t/_  _t_ indexes the sample number of the
continuous-time signals _I_ IF ( _t_ ) and _Q_ IF ( _t_ ),  IF = __ IF  _t_ is
the digital frequency, and  is the sampling period (typically around 1 ns). Pulsing the resonator is necessarily _t_
accompanied by a ring-up time, related to the quality
factor of the resonator, and the first few samples may
decrease overall signal-to-noise. Consequently, a delayed
window of samples [ _n_ 1 : _n_ 2 ] is often used to perform the
second digital demodulation of the discrete-time signals
]. Note that more complicated windowing functions may also be used to improve _I_ IF [ _n_ 1 : _n_ 2 ] and _Q_ IF [ _n_ 1 : _n_ 2
state discrimination, but here we use a simple boxcar [see
Fig. 22(b)].
Digital demodulation comprises the point-by-point
multiplication of _I_ IF [ _n_ 1 : _n_ 2 ] and _Q_ IF [ _n_ 1 : _n_ 2 ] by cos  IF _n_
and sin  IF _n_
. Averaging the resulting time series eliminates the 2 IF
component while retaining the DC component, as in a homodyne measurement, one obtains


Such single-shot measurements may then be repeated
a large number of times to obtain an ensemble average
_z_  [ _n_ ] .
__ __

**C.** **Weak and strong qubit measurements: Impact of noise**

In quantum measurements, noise plays an essential role
as it dictates the fidelity of its outcome 128,328 , recall Fig.
22(c). In the absence of noise, any non-zero dispersive
shift (resulting in a resonator field displacement) would
suffice to unambigously separate the qubit states, given
a properly chosen resonator linewidth. In practice, however, the outcome of the quantum measurement is generally Gaussian distributed in the ( _I, Q_
)-plane due to presence of classical and quantum noise. In this section, we
review the main sources of noise, as well as how it impedes our ability to extract information from the quantum system. For a rigorous discussion of noise and quantum measurements, the interested reader is referred e.g.
to the work by Clerk _et al_ 128 and to the textbook by
Haus 127 .
The total noise added to the signal has multiple origins.
One part of the noise is associated with the microwave
signal used to probe the resonator, where each photon
has an intrinsic quantum noise power of  _/_ 2 per unit
bandwidth. Another contribution comes from the phasepreserving amplifiers, adding both classical noise and at



1
_I_ =

_M_

1
_Q_ =


_n_



_A_ RO _A_ LO
_I_ IF [ _n_ ] cos[ IF _n_ ] = 16
_n_ 1


_n_



LO

16 cos __ RO _,_ (162)



_A_ RO _A_ LO
_Q_ IF [ _n_ ] sin[ IF _n_ ] = 16
_n_ 1



LO

16 sin __ RO _,_ (163)


where _M_ = _n_ 2 _n_ 1 + 1. As before, _I_ and _Q_ can then be
used to find _A_ RO __ and __ RO .
The same procedure may be view in the complex _I_ _Q_
__
plane by the analytic function _z_ IF [ _n_ ], as illustrated in


-----


47

relative separation in the complex plane is maximized  .
The line that is used to separate between 0 and 1 is
_|_ __ _|_ __
called a _separatrix_ .
The noise can now be quantified by comparing the
widths of the Gaussian probability distribution surrounding the mean with the peak separation in the
( _I, Q_ )-plane, thus defining a signal-to-noise ratio SNR =
_/_ ( __ 1 + __ 0 ), see Fig. 23(a), with __ = __ 1 __ 0
representing the signal and  __ 0 ,  __ 1 represent the noise (2 _|_ __ _|_ __ )
of each distribution. The SNR allows us to distinguish
between a weak and a strong quantum measurement, as
illustrated in Fig. 23(b)-(d).
In a weak measurement, the probabilities are broadly
distributed as compared to their relative separation
(SNR _<_ 1), which means that only partial information
of the quantum state is revealed to the observer, see
Fig.23(b). In a strong measurement, on the other hand,
the quantum state is collapsed onto one of the two eigenstates. In this case, the outcome of the measurement can
be distinguished unambigously, which is reflected in two
fully separated distributions (SNR _>_ 1), see Fig. 23(d).
In many applications of quantum measurements, it
is necessary to unambigously (and with high fidelity)
tell the outcome without repeating the readout measurement. This is known as _single-shot readout_ and it often
requires the use of a parametric amplifier  a preamplifier
used to increase system SNR  which is further discussed
in Sec. V E 3.
Assuming that the widths of the two distributions are
identical,  __ 0 =  __ 1 =  __ , the separation error can
be calculated by deriving the weight of the overlapping
region of the Gaussian distributions as 163


(a)


__ _1_

__


![qe-guide-scqubits-oliver.pdf-46-6.png](qe-guide-scqubits-oliver.pdf-46-6.png)

![qe-guide-scqubits-oliver.pdf-46-27.png](qe-guide-scqubits-oliver.pdf-46-27.png)

![qe-guide-scqubits-oliver.pdf-46-33.png](qe-guide-scqubits-oliver.pdf-46-33.png)

![qe-guide-scqubits-oliver.pdf-46-31.png](qe-guide-scqubits-oliver.pdf-46-31.png)

![qe-guide-scqubits-oliver.pdf-46-29.png](qe-guide-scqubits-oliver.pdf-46-29.png)

![qe-guide-scqubits-oliver.pdf-46-25.png](qe-guide-scqubits-oliver.pdf-46-25.png)

![qe-guide-scqubits-oliver.pdf-46-23.png](qe-guide-scqubits-oliver.pdf-46-23.png)

![qe-guide-scqubits-oliver.pdf-46-21.png](qe-guide-scqubits-oliver.pdf-46-21.png)

![qe-guide-scqubits-oliver.pdf-46-28.png](qe-guide-scqubits-oliver.pdf-46-28.png)

![qe-guide-scqubits-oliver.pdf-46-34.png](qe-guide-scqubits-oliver.pdf-46-34.png)

![qe-guide-scqubits-oliver.pdf-46-32.png](qe-guide-scqubits-oliver.pdf-46-32.png)

![qe-guide-scqubits-oliver.pdf-46-30.png](qe-guide-scqubits-oliver.pdf-46-30.png)

![qe-guide-scqubits-oliver.pdf-46-24.png](qe-guide-scqubits-oliver.pdf-46-24.png)

![qe-guide-scqubits-oliver.pdf-46-26.png](qe-guide-scqubits-oliver.pdf-46-26.png)

![qe-guide-scqubits-oliver.pdf-46-19.png](qe-guide-scqubits-oliver.pdf-46-19.png)

![qe-guide-scqubits-oliver.pdf-46-22.png](qe-guide-scqubits-oliver.pdf-46-22.png)

![qe-guide-scqubits-oliver.pdf-46-20.png](qe-guide-scqubits-oliver.pdf-46-20.png)

![qe-guide-scqubits-oliver.pdf-46-38.png](qe-guide-scqubits-oliver.pdf-46-38.png)

![qe-guide-scqubits-oliver.pdf-46-17.png](qe-guide-scqubits-oliver.pdf-46-17.png)

![qe-guide-scqubits-oliver.pdf-46-15.png](qe-guide-scqubits-oliver.pdf-46-15.png)

![qe-guide-scqubits-oliver.pdf-46-7.png](qe-guide-scqubits-oliver.pdf-46-7.png)

![qe-guide-scqubits-oliver.pdf-46-18.png](qe-guide-scqubits-oliver.pdf-46-18.png)

![qe-guide-scqubits-oliver.pdf-46-5.png](qe-guide-scqubits-oliver.pdf-46-5.png)

![qe-guide-scqubits-oliver.pdf-46-37.png](qe-guide-scqubits-oliver.pdf-46-37.png)

![qe-guide-scqubits-oliver.pdf-46-13.png](qe-guide-scqubits-oliver.pdf-46-13.png)

![qe-guide-scqubits-oliver.pdf-46-16.png](qe-guide-scqubits-oliver.pdf-46-16.png)

![qe-guide-scqubits-oliver.pdf-46-11.png](qe-guide-scqubits-oliver.pdf-46-11.png)

![qe-guide-scqubits-oliver.pdf-46-8.png](qe-guide-scqubits-oliver.pdf-46-8.png)

![qe-guide-scqubits-oliver.pdf-46-10.png](qe-guide-scqubits-oliver.pdf-46-10.png)

![qe-guide-scqubits-oliver.pdf-46-36.png](qe-guide-scqubits-oliver.pdf-46-36.png)

![qe-guide-scqubits-oliver.pdf-46-35.png](qe-guide-scqubits-oliver.pdf-46-35.png)

![qe-guide-scqubits-oliver.pdf-46-9.png](qe-guide-scqubits-oliver.pdf-46-9.png)

![qe-guide-scqubits-oliver.pdf-46-14.png](qe-guide-scqubits-oliver.pdf-46-14.png)

![qe-guide-scqubits-oliver.pdf-46-12.png](qe-guide-scqubits-oliver.pdf-46-12.png)

![qe-guide-scqubits-oliver.pdf-46-3.png](qe-guide-scqubits-oliver.pdf-46-3.png)

![qe-guide-scqubits-oliver.pdf-46-4.png](qe-guide-scqubits-oliver.pdf-46-4.png)

![qe-guide-scqubits-oliver.pdf-46-2.png](qe-guide-scqubits-oliver.pdf-46-2.png)

Sampling time _, _ _s_ (a.u.)


![qe-guide-scqubits-oliver.pdf-46-0.png](qe-guide-scqubits-oliver.pdf-46-0.png)



![qe-guide-scqubits-oliver.pdf-46-77.png](qe-guide-scqubits-oliver.pdf-46-77.png)

![qe-guide-scqubits-oliver.pdf-46-61.png](qe-guide-scqubits-oliver.pdf-46-61.png)

![qe-guide-scqubits-oliver.pdf-46-79.png](qe-guide-scqubits-oliver.pdf-46-79.png)

![qe-guide-scqubits-oliver.pdf-46-52.png](qe-guide-scqubits-oliver.pdf-46-52.png)

![qe-guide-scqubits-oliver.pdf-46-58.png](qe-guide-scqubits-oliver.pdf-46-58.png)

![qe-guide-scqubits-oliver.pdf-46-67.png](qe-guide-scqubits-oliver.pdf-46-67.png)

![qe-guide-scqubits-oliver.pdf-46-70.png](qe-guide-scqubits-oliver.pdf-46-70.png)

![qe-guide-scqubits-oliver.pdf-46-40.png](qe-guide-scqubits-oliver.pdf-46-40.png)

![qe-guide-scqubits-oliver.pdf-46-41.png](qe-guide-scqubits-oliver.pdf-46-41.png)

![qe-guide-scqubits-oliver.pdf-46-71.png](qe-guide-scqubits-oliver.pdf-46-71.png)

![qe-guide-scqubits-oliver.pdf-46-69.png](qe-guide-scqubits-oliver.pdf-46-69.png)

![qe-guide-scqubits-oliver.pdf-46-59.png](qe-guide-scqubits-oliver.pdf-46-59.png)

![qe-guide-scqubits-oliver.pdf-46-56.png](qe-guide-scqubits-oliver.pdf-46-56.png)

![qe-guide-scqubits-oliver.pdf-46-68.png](qe-guide-scqubits-oliver.pdf-46-68.png)

![qe-guide-scqubits-oliver.pdf-46-76.png](qe-guide-scqubits-oliver.pdf-46-76.png)

![qe-guide-scqubits-oliver.pdf-46-75.png](qe-guide-scqubits-oliver.pdf-46-75.png)

![qe-guide-scqubits-oliver.pdf-46-39.png](qe-guide-scqubits-oliver.pdf-46-39.png)

![qe-guide-scqubits-oliver.pdf-46-63.png](qe-guide-scqubits-oliver.pdf-46-63.png)

![qe-guide-scqubits-oliver.pdf-46-80.png](qe-guide-scqubits-oliver.pdf-46-80.png)

![qe-guide-scqubits-oliver.pdf-46-47.png](qe-guide-scqubits-oliver.pdf-46-47.png)

![qe-guide-scqubits-oliver.pdf-46-44.png](qe-guide-scqubits-oliver.pdf-46-44.png)

![qe-guide-scqubits-oliver.pdf-46-46.png](qe-guide-scqubits-oliver.pdf-46-46.png)

![qe-guide-scqubits-oliver.pdf-46-62.png](qe-guide-scqubits-oliver.pdf-46-62.png)

![qe-guide-scqubits-oliver.pdf-46-55.png](qe-guide-scqubits-oliver.pdf-46-55.png)

![qe-guide-scqubits-oliver.pdf-46-74.png](qe-guide-scqubits-oliver.pdf-46-74.png)

![qe-guide-scqubits-oliver.pdf-46-78.png](qe-guide-scqubits-oliver.pdf-46-78.png)

![qe-guide-scqubits-oliver.pdf-46-66.png](qe-guide-scqubits-oliver.pdf-46-66.png)

![qe-guide-scqubits-oliver.pdf-46-57.png](qe-guide-scqubits-oliver.pdf-46-57.png)

![qe-guide-scqubits-oliver.pdf-46-51.png](qe-guide-scqubits-oliver.pdf-46-51.png)

![qe-guide-scqubits-oliver.pdf-46-60.png](qe-guide-scqubits-oliver.pdf-46-60.png)

![qe-guide-scqubits-oliver.pdf-46-50.png](qe-guide-scqubits-oliver.pdf-46-50.png)

![qe-guide-scqubits-oliver.pdf-46-54.png](qe-guide-scqubits-oliver.pdf-46-54.png)

![qe-guide-scqubits-oliver.pdf-46-65.png](qe-guide-scqubits-oliver.pdf-46-65.png)

![qe-guide-scqubits-oliver.pdf-46-73.png](qe-guide-scqubits-oliver.pdf-46-73.png)

![qe-guide-scqubits-oliver.pdf-46-43.png](qe-guide-scqubits-oliver.pdf-46-43.png)

![qe-guide-scqubits-oliver.pdf-46-45.png](qe-guide-scqubits-oliver.pdf-46-45.png)

![qe-guide-scqubits-oliver.pdf-46-64.png](qe-guide-scqubits-oliver.pdf-46-64.png)

![qe-guide-scqubits-oliver.pdf-46-53.png](qe-guide-scqubits-oliver.pdf-46-53.png)


![qe-guide-scqubits-oliver.pdf-46-49.png](qe-guide-scqubits-oliver.pdf-46-49.png)

![qe-guide-scqubits-oliver.pdf-46-72.png](qe-guide-scqubits-oliver.pdf-46-72.png)

![qe-guide-scqubits-oliver.pdf-46-42.png](qe-guide-scqubits-oliver.pdf-46-42.png)

|(b) Weak: SNR < 1|(c)|
|---|---|


Counts (a.u.)


![qe-guide-scqubits-oliver.pdf-46-1.png](qe-guide-scqubits-oliver.pdf-46-1.png)

Counts (a.u.) Counts (a.u.)


![qe-guide-scqubits-oliver.pdf-46-48.png](qe-guide-scqubits-oliver.pdf-46-48.png)

FIG. 23. **(a)** Qubit state distribution throughout the course
of sampling the readout signal, in the presence of noise. The
separation between the peaks (solid lines) increases linearly in
time, whereas the peak widths only increase as __ _t_

128
. Image inspired by Clerk _et al_ . The three black arrows represent line
cuts for three sampling times: **(b)** For short sampling time,
the states are not separated, resulting in a weak meaurement
(SNR _<_ 1). **(c)** After a longer sampling time, the peaks starts
to get separated, **(d)** finally getting fully resolved, resulting
in a strong measurement (SNR _>_ 1).


FIG. 23. **(a)** Qubit state distribution throughout the course
of sampling the readout signal, in the presence of noise. The
separation between the peaks (solid lines) increases linearly in
time, whereas the peak widths only increase as __ _t_


__
 __ = __ 0 __ 2 __



2
exp ( __ __ __ 1 )

2

__ 2( __ )


__ sep =


_d_

(170)



2
2 __ ( __ )


= 1 erfc

2


_|_ __ 0 __ __ 1 _|_

2
2( __ )


_|_ __ 0 __ __ 1 _|_


where erfc(x) denotes the complementary Gaussian error
function, defined as


least 2 of noise as required by Heisenbergs uncertainty relation.  _/_ Finally, any attenuation of the signal
prior to the first amplifier will appear as added noise.
Combined, these noise sources amount to a _system noise_
_temperature_ , which can be characterized using a sensitive
thermometer, such as a shot-noise tunnel junction 329 or
a qubit 330 as a sensor.

The noise results in time-dependent fluctuations of the
measured signal, which in turn translates into uncertainty in our demodulated signals, see Fig. 22(c). This
can be intuitively understood by considering that our
heterodyne detection method requires us to sample for a
finite amount of time.

To quantify the impact of the noise on our measurement, we first project the distributed ( _I, Q_
) data  corresponding to 0 and 1  onto the axis for which their
_|_ __ _|_ __


__

_x_




erfc( _x_ ) = 1
__ __ __



2
_e_ __ _t_ _dt._ (171)


Using the erfc in Eq. (171), the separation error in
Eq. (170) can be compactly expressed in terms of the
signal-to-noise ratio,



1 SNR
__ sep = erfc

2 2




1 SNR

erfc
2 2



(172)


 When analyzing the readout data, we have the freedom to choose
projections.


-----


48

its environment. This is known as the Purcell effect 331 ,

332
and is an important consideration when designing qubitresonator systems
. The portion of spontaneous emission that is mediated by the resonator describes how
qubit relaxation is enhanced by the resonator Q when onresonance, and suppressed off-resonance. The aim of this
section is twofold: first, we develop an intuition for how
the Purcell decay limits qubit coherence, and second, how
to properly mitigate this limitation by designing a socalled _Purcell filter_ , which modifies the impedance seen
by the qubit through the readout resonator. This allows
us to maintain fast readout, while protecting the qubit
from relaxing into its environment.
If we would just choose qubit and resonator operation
frequencies guided by the resonator linewidth __
, qubitresonator coupling _g_ , and the amount of dispersive shift
__ , we would reduce the detuning between the qubit and
the resonator, thus maximizing the dispersive shift (recall
Fig. 20). However, this presents a trade-off between two
important system parameters; on one hand, we want the
qubit to be isolated from the resonator environment offresonant to avoid Purcell-enhanced decay. On the other
hand, looking at the dispersive shift, we want the two
rates, _g_ and __ to be strong, yielding larger dispersive
shift as well as short resonator transient and thus a faster
readout.
Fortunately, when operating in the dispersive regime,
the qubit and resonator are far detuned from each other
 _g, _
__
, which means that their impedance (environment) can be independently engineered through filter
design. In essence, one designs a filter to have strong
coupling to the readout port at the resonator frequency
(large __ ), but isolates the qubit from its environment at
the qubit frequency 333,334 . In other words, an impedance
transformation.
Depending on the design of the readout for the quantum processor to which the filter should be coupled,
there are different ways to design a Purcell filter; such as
quarter-wave stubs 333 , low-Q bandpass filters 66,334 , and
stepped-impedance filters . Which one is optimal depends on system properties such as qubit-resonator detunings, required bandwidth, and allowed insertion loss. 335
The most promising Purcell filter designs are the ones
that allow for frequency multiplexing, such as the low-Q
bandpass filter design 66,334 , which in addition to Purcell
filtering has the function of a quantum bus, connecting
several frequency-multiplexed readout resonators sharing
the same amplifier chain.
The Purcell effect can be framed in terms of Fermis
golden rule, where noise in the environment causes the
qubit to decay with some probability. We can gain intuition about the Purcell effect (as well as how the qubit can
be protected from it) by replacing the Josephson junction
in the qubit circuit with an ac-current source, outputting
_I_ ( _t_ ) = _I_ 0 sin( _t_ ), with _I_ 0 = _e_ and study the rate at
which power is lost into an environmental load resistor
_R_ = _Z_ 0 = 50 , see Fig. 24(a).
Expressing the power lost in the resistor as _P_ =


Note, however, that the separation error between the
two state distributions only tells us the signal-to-noise
ratio of our detection scheme. On top of the separation
error, fidelity is reduced if the qubit relaxes (or is excited)
during the readout. This will result in a count on the
wrong side of the threshold. This leads to an additional
constraint on the readout; The readout cycle needs to be
completed on a timescale much shorter than the qubit
relaxation time.
In summary, we see that to optimize the qubit readout fidelity, the readout needs to fulfill the following two
requirements:

-  **Fast readout** : The readout cycle needs to be completed within a time that is short compared with
the qubit coherence time. The longer the readout
time, the more likely the qubit is to relax, thus reducing readout fidelity.

-  **High signal-to-noise ratio** : The signal-to-noise
ratio needs to be sufficiently large to suppress the
state separation errors below an acceptable limit
where it does not limit the readout fidelity.

In sections V D and V E 3, we review how these two
conditions are met by carefully engineering the signal
path of the readout circuitry.

**D.** **Purcell filters for faster readout**

To ensure high-fidelity readout performance, it is important to perform single-shot readout at a timescale
much shorter than the qubit coherence time, __ _ro_ __ _T_ 1 .
This motivates us to: _(i)_ make the resonator linewidth
wide, thus reducing its ring-up time, __ _rd_ , and _(ii)_ keep
the integration time __ _s_ as short as possible, see Fig.22(b).
The ability to isolate a quantum system from decohering
into its environment while, at the same time, being able

328
to read out its state in a short time represents two contradictory criteria, which must be traded-off .
Even though dispersive readout (in the few-photon
limit) has only a small back-action on the qubit state,
the qubit will still suffer from _T_ 1 -relaxation while we are
performing a measurement. In fact, this decay during
the readout often limits the readout fidelity, reducing it
to


_F_ ( __ _ro_ ) = 1 _e_ __ __ _ro_ _/T_ 1 _,_ (173)
__

where __ _ro_ = __ _rd_ + __ _s_ _/_ 2 denotes the total time for the
readout, consisting of the readout delay __ _rd_ due to the
resonator transient, and half the sampling time __ _s_ _/_ 2. The
fidelity drop in Eq. (173) can be interpreted as a manifestation of the competition between the time scales at
which our quantum information reaches our detector or
the environment first.
The limitation of qubit coherence originates from an
enhanced spontaneous emission of photons, induced by


-----


49

We can now introduce the Purcell filter [Fig. 24(c-d)]
in between the readout resonator and the 50 environment, leading to a reduction of the decay rate according
to 333



2 2 2
_I_ 0 ( _C_ _g_ _/C_  ) _R_ = ( _e_ ) _Z_ 0 , with __ = _C_ _g_ _/C_  , the qubit
Purcell decay rate into the continuum can be written as



Purcell 1
__ env =



1 _P_

=
_T_ 1 



2

_P_ = ( _e_ ) _Z_

 __  __



2 2

) _Z_ 0 = _g_

 __ __



_._ (174)
__


To protect the qubit from decaying into the 50 environment (as well as for deploying our dispersive readout)
we can now add a resonator in parallel with the qubit,
see Fig. 24(b). The presence of the resonator has the
effect of shaping the impedance at the qubit frequency,
which in turn modifies the decay rate in Eq. (174) into



Purcell _g_
__ res-filter-env = __



2
__ q

__ _r_

 


__ _r_

2 _Q_ _F_ 




__ _r_

2 _Q_ _F_




(179)



Purcell
__ res-env = _g_


Re[ _Z_ _r_ ( __ )]

_,_ (175)
_Z_ 0


Re[ _Z_ _r_ ( __ )]


where _Q_ _F_ denotes the quality factor of the Purcell filter.
This is schematically depicted in Fig. 24(d), where the
Purcell filter is placed around the resonator frequency,
while far detuned from the qubit.


where _Z_ _r_ ( __
) denotes the impedance of the shunted resonator. We can express the real-part of the impedance
in terms of the resonator quality factor _Q_ = __ _r_ _/_ and
qubit-resonator detuning = __ _q_ __ _r_ ,
__


(a)


_I(t)_ _g_ (b) _I(t)_


(b)



_QZ_ 0
Re[ _Z_ _r_ ( __ )] = 1 + 2( _/_ ) 2 _._ (176)

Now, by substituting Eq. (176) into Eq. (175), we
see that the Purcell decay rate for the qubit depends on
the detuning between the resonator and the qubit. This
is intuitive, since the resonator can be thought of as a
bandpass filter, with center frequency __ _r_ and bandwidth
__ . For resonant condition, i.e. when = 0, the emission
rate into the resonator takes the form


|C g C   q Qubit|Z 0 Env.|
|---|---|


| q Qubit|Col2|Col3|Z 0 Env.|
|---|---|---|---|
|| r||Z 0|
||Res.|||


_I(t)_ _g_ __


(c)

(d)

|C   q Qubit|Col2|Col3|0 nv.|
|---|---|---|---|
||  r p|Z||
||Res. Purcell|filter E||



2
__ res-env Purcell = _g_

__


Re[ _Z_ _r_ ]



2

_Z_ _r_ ] = _g_

_Z_ 0 =0 __



2 2
_g_ _g_

_Q_ =
__ _r_



_._ (177)
__


In the dispersive regime  _g, _
__
, which is also relevant for us in the context of qubit readout, we can make

2
the approximation Re[ _Z_ _r_ ] __ _QZ_ 0 ( _/_ ) , yielding the
familiar expression for the Purcell decay rate in circuit
QED 332


__ q Frequency, (a.u.) __


__ q __

|Qubit|Col2|Purcell filter R|esonator|
|---|---|---|---|


![qe-guide-scqubits-oliver.pdf-48-0.png](qe-guide-scqubits-oliver.pdf-48-0.png)


2
_g_ __

_Q_
__ _r_



2 = _g_
 


2
_._




2

Purcell
__ res-env = _g_


__


Re[ _Z_ _r_


_Z_ _r_ ] = _g_

_Z_ 0  __ _g,_ __


FIG. 24. **(a)**
Circuit representation of qubit (orange) coupled to an environment (blue) with a load resistor, _Z_ 0 , via a
capacitor _C_ _g_
. To study the decay rate, the Josephson junction has been replaced with a current source, _I_ ( _t_ ). **(b)** By
adding a resonator (red) with frequency __ _r_ in-between the
qubit and the 50 environment, we get the case found in regular dispersive readout. **(c)** A Purcell-filter (green) is added
to the circuit, providing protection for the qubit, while allowing the resonator field to decay fast to the environment.
**(d)** Transmission spectrum of a Purcell filter (dashed green),
centered around the resonator frequency (red arrow), whereas
the qubit frequency (orange arrow) is far detuned.


(178)
The relation for the Purcell limit in Eq. (178) thus
provides us with a useful guide on how to design the coupling rates _g_ and __ , as well as how large qubit-resonator
detuning is necessary to avoid the Purcell limit.
In recent years, however, the intrinsic coherence times
for superconducting qubits have reached above 100 __ s,
recall Sec. II, imposing practical limitations on how to
simultaneously optimize _g_ and __ , to render fast readout
without compromising the qubit coherence. Considering
the parameters in Eq. (178), it is not possible to just
increase the bound on the relaxation time _T_ 1 , without at
the same time trading off the readout speed and contrast.


-----


50

fields and therefore considered to be coherent light comprising microwave photons. As such, they must obey the
commutation relations 127,328,339,340

[ _a_ in _, a_ __ in ] = [ _a_ out _, a_ __ out ] = 1 _,_ (182)

from which it can be shown that it is not possible to
simultaneously amplify both quadratures of _a_ in without
also adding noise. This is known as _Caves theorem_ after
the work by Caves 328 , based on earlier work by Haus and
Mullen 339 . This can be seen by considering the scattering
relation between the input and output microwave fields


**E.** **Improve signal-to-noise ratio: Parametric amplification**

In light of the aforementioned limited signal-to-noise
ratio associated with the low photon number of the dispersive qubit readout, and the short sampling time, the
noise temperature of the amplifier chain plays a crucial
role in determining the fidelity of the measurement.
A useful benchmark for quantum measurements is the
_quantum efficiency_ , defined as



 __ RF
__ SQL = _,_ 0 _< _ SQL _<_ 1 _,_ (180)

_k_ _B_ _T_ sys

which quantifies the photon energy to the system noise
temperature _T_ sys , thus yielding a measure of how close
the signal is to the standard quantum limit (SQL), as
imposed by Heisenbergs uncertainty relation, adding
1/2 photon of noise when __ SQL approaches unity. Since
the energy of each microwave photon is much smaller
than that of optical photons, it is not easy to build
a single-photon detector operating in the microwave
domain . Instead, for heterodyne detection in circuit QED, a set of cascaded microwave amplifiers are 336,337
used. The system noise temperature for the amplifier
chain can be expressed in terms of the individual gain figures _G_ _n_ and noise temperatures _T_ _N,n_ of each constituent
amplifier 338


_a_ out =


_Ga_ in _._ (183)


The gain relation in Eq. (183) constitutes our ideal
scenario for an amplifier process. However, the problem
is that that this relation does not satisfy the commutation
relation in Eq. (182). To satisfy this relation, we need to
also take into account the vacuum fluctuations of another

128,341343
mode  called the _idler_ mode _b_ in , also satisfying
the same communtation relation [ _b_ in _, b_ __ in ] = 1. To satisfy
the commutation relation, the idler mode is amplified by
the gain factor __ _G_ 1. For large gain, it can be shown


the gain factor _G_ 1. For large gain, it can be shown

__
that a minimum amount of half a photon of noise  _/_ 2
needs to be added to a signal amplified with gain __ _G_ .


needs to be added to a signal amplified with gain _G_ .

Finally, taking the idler mode into account, the scattering relation for the coherent output field takes the form



_T_ _N,_ 2
_T_ sys = _T_ _N,_ 1 +



_N,_ 2 + _T_ _N,_ 3

_G_ 1 _G_ 1 _G_



_N,_ 3

+ _..._ (181)
_G_ 1 _G_ 2


_a_ out =


_G_ 1 _b_ __ in _._ (184)
__

Added idler noise


 _Ga_ in


_G_ 1 _b_ __ in
__



Amplification


where _n_ = 1 _,_ 2 _,_ 3 _, ..._ denotes the order of the amplifiers,
starting from the qubit chip. From Eq. (181), we see that
the noise temperature _T_ sys
is dominated by the noise contribution from the first amplifier, whereas the gain of the
first amplifier has the effect of suppressing the noise from
the second amplifier, and so on. If the first amplifier is a
low-noise high-electron mobility transistor (HEMT) amplifier ( _T_ _N_ 2 K), the system noise temperature when
__
implemented in a cryostat is around 7-10 K, corresponding to around 10-20 added photons of noise per signal
photon around 5 GHz. In practice, this is generally too
much noise to perform single-shot readout.
This inherently poor signal-to-noise ratio has revived
interest in developing quantum-limited parametric amplifiers (PA)  tailored for readout of superconducting
qubits  featuring the ability to amplify small microwave
signals, and adding only approximately the minimum
amount of noise allowed by quantum mechanics 127,128,328 .

**_1._** **_Quantum-limited amplification processes_**


_phaseinsensitive_ Generally, this process results in a so-called parametric amplification process, in which
both quadratures of the input field gets equally amplified. This is illustrated in Fig. 25, where the in-phase
( _I_ in ) and quadrature ( _Q_ in ) components of the fields are
plotted, before and after the parametric amplifier.
Considering the amplification process in Eq. (184), we
can find a special case for the idler mode, for which noiseless amplification can be accomplished for one of the two
quadratures, but at the expense of adding more noise
to the other, thus not violating Heisenbergs uncertainty
relation for the two field quadratures. This mode of operation is known as _phase-sensitive_ amplification, and is
obtained when the idler mode oscillates at the same frequency as the signal (or a multiple thereof), but can be
shifted with an overall phase __ [0 _,_ 2 __
]. By substituting the idler mode in Eq. (184) with __ _b_ in = _e_ _i_ _a_ in , the
scattering relation becomes



_i_

__ _Ga_ in + _e_ __ __

Amplification


_a_ out =



_i_ _G_ 1 _a_ __ in _._ (185)

__

Phase-dep. noise


 _Ga_ in


_G_ 1 _a_ __ in
__



In a linear, phase-insensitive amplifier, an input state
_a_ in is amplified to an output state _a_ out
__ __ __ __
, with an amplitude gain factor __ _G_ . Microwaves are electromagnetic


The overall phase factor allows us to tune the orientation of the amplification (or de-amplification) by means


-----


51


(a) AMPLIFIER INPUT (b) MIXING PROCESSES (c) AMPLIFIER OUTPUT


(a) AMPLIFIER INPUT (b) MIXING PROCESSES (c)


|Col1|Pump  p|
|---|---|


![qe-guide-scqubits-oliver.pdf-50-14.png](qe-guide-scqubits-oliver.pdf-50-14.png)

![qe-guide-scqubits-oliver.pdf-50-13.png](qe-guide-scqubits-oliver.pdf-50-13.png)

![qe-guide-scqubits-oliver.pdf-50-11.png](qe-guide-scqubits-oliver.pdf-50-11.png)

![qe-guide-scqubits-oliver.pdf-50-12.png](qe-guide-scqubits-oliver.pdf-50-12.png)

![qe-guide-scqubits-oliver.pdf-50-26.png](qe-guide-scqubits-oliver.pdf-50-26.png)

![qe-guide-scqubits-oliver.pdf-50-10.png](qe-guide-scqubits-oliver.pdf-50-10.png)

![qe-guide-scqubits-oliver.pdf-50-4.png](qe-guide-scqubits-oliver.pdf-50-4.png)

![qe-guide-scqubits-oliver.pdf-50-8.png](qe-guide-scqubits-oliver.pdf-50-8.png)

![qe-guide-scqubits-oliver.pdf-50-9.png](qe-guide-scqubits-oliver.pdf-50-9.png)

![qe-guide-scqubits-oliver.pdf-50-25.png](qe-guide-scqubits-oliver.pdf-50-25.png)

![qe-guide-scqubits-oliver.pdf-50-16.png](qe-guide-scqubits-oliver.pdf-50-16.png)

![qe-guide-scqubits-oliver.pdf-50-6.png](qe-guide-scqubits-oliver.pdf-50-6.png)

![qe-guide-scqubits-oliver.pdf-50-7.png](qe-guide-scqubits-oliver.pdf-50-7.png)

![qe-guide-scqubits-oliver.pdf-50-15.png](qe-guide-scqubits-oliver.pdf-50-15.png)

![qe-guide-scqubits-oliver.pdf-50-24.png](qe-guide-scqubits-oliver.pdf-50-24.png)

![qe-guide-scqubits-oliver.pdf-50-23.png](qe-guide-scqubits-oliver.pdf-50-23.png)

![qe-guide-scqubits-oliver.pdf-50-22.png](qe-guide-scqubits-oliver.pdf-50-22.png)

![qe-guide-scqubits-oliver.pdf-50-21.png](qe-guide-scqubits-oliver.pdf-50-21.png)

![qe-guide-scqubits-oliver.pdf-50-27.png](qe-guide-scqubits-oliver.pdf-50-27.png)

![qe-guide-scqubits-oliver.pdf-50-2.png](qe-guide-scqubits-oliver.pdf-50-2.png)

![qe-guide-scqubits-oliver.pdf-50-3.png](qe-guide-scqubits-oliver.pdf-50-3.png)

![qe-guide-scqubits-oliver.pdf-50-20.png](qe-guide-scqubits-oliver.pdf-50-20.png)

![qe-guide-scqubits-oliver.pdf-50-5.png](qe-guide-scqubits-oliver.pdf-50-5.png)

![qe-guide-scqubits-oliver.pdf-50-17.png](qe-guide-scqubits-oliver.pdf-50-17.png)

![qe-guide-scqubits-oliver.pdf-50-18.png](qe-guide-scqubits-oliver.pdf-50-18.png)

![qe-guide-scqubits-oliver.pdf-50-19.png](qe-guide-scqubits-oliver.pdf-50-19.png)

![qe-guide-scqubits-oliver.pdf-50-0.png](qe-guide-scqubits-oliver.pdf-50-0.png)

![qe-guide-scqubits-oliver.pdf-50-1.png](qe-guide-scqubits-oliver.pdf-50-1.png)

FIG. 25. Schematic illustration of a quantum-limited, phase-preserving parametric amplification process of a coherent input
state, _a_ in = _I_ in + _iQ_ in . **(a)** The state is centered at ( _I_ in _,_ _Q_ in ) and has a noise represented by the radii of the circles along the
__ __ __ __
real and imaginary axes, respectively. **(b)** Scattering representation of parametric mixing, where the signal and pump photons
are interacting via a purely dispersive nonlinear medium. **(c)** In the case of phase-preserving amplification, both quadratures
get amplified by a factor __ _G_ , while (in the ideal case) half a photon of noise gets added to the output distribution (blue).

Image inspired by Flurin 340 .


of the pump phase, thus allowing us to choose a quadrature for which we want to reduce the noise, see Fig. 26.
Intuitively, this can be understood by considering the interference that occurs when two waves with the same frequency are confined in space, where we obtain constructive or destructive interference, depending on the phase
between the two waves. Due to this interference, the
noise can be suppressed even below the standard quantum limit (without violating Heisenbergs uncertainty relation). This is known as _single-mode squeezing_ and was
first observation in superconducting circuits by Yurke _et_
_al._ 344 . In particular, after the theoretical prediction by
Gardiner 345 , Murch _et al._ showed that the coherence

346,347
time of a qubit can be enhanced when the qubit is exposed to squeezed vacuum . Also
348
_two-mode squeezing_ was demonstrated by Eichler _et al._

108
, where the demodulation setup squeezes both quadratures of the acquired signal .
In the context of qubit readout, however, phasesensitive amplification tends to be experimentally inconvenient. This is mainly due to its phase-dependent
gain, which imposes stringent requirements on continuous phase-calibration of the readout signal.
For a detailed theoretical framework developed for
quantum limited amplification, the reader is referred to
earlier work by Roy and Devoret 349 , Clerk _et al._ 128 , and
Wustmann and Shumeiko 350 .

**_2._** **_Operation of Josephson parametric amplifiers_**

In this section, we review the basic operation characteristics of parametric amplifiers, and in particular the
Josephson parametric amplifiers (JPAs), that have been


exploited for qubit readout. Although many different
flavors of parametric systems exist, we here focus on the
resonant implementations of the Josephson parametric
amplifier (JPA), serving as a good system for reviewing
the fundamental concepts around parametric amplification.
All parametric amplifiers operate based on one fundamental principle: the incoming _signal_ photons are mixed
with an applied _pump_ tone via an intrinsic nonlinearity,
by which energy from the pump is converted into signal
photons and thereby providing gain. As we recall from

351
Sec. II, such a nonlinearity can be engineered in the microwave domain using Josephson junctions , and the
resonant parametric amplifiers are built from slightly anharmonic oscillators.
The first Josephson parametric amplifiers were built
from a coplanar waveguide resonator, made nonlinear by
adding a nonlinear Josephson contribution to its total
inductance, see Fig. 27(a). The word _parametric_ refers
to the process of modulating (or _pumping_ ) one of the
parameters of the systems equation-of-motion (such as
frequency or damping) in time 350,352,353 . The natural
way to perform this parametric pumping is to modulate
the nonlinear Josephson inductance, which in turn has
the effect of modulating the resonator frequency __ _r_ ( _t_ ) =
1 _/_ _L_ ( _t_ ) _C_ .

Depending on how the pumping is implemented, there



are two different mixing processes that can be exploited
in Josephson parametric amplifiers, which determines
the characteristics of the amplifier. These are illustrated in Fig. 27(b)-(c) and are referred to as
352,354357 97,350,353,358363
_currentpumping_ , respectively. The type of mixing process that takes place and _flux-pumping_
depends on the leading order of the nonlinearity of the


exploited for qubit readout. Although many different
flavors of parametric systems exist, we here focus on the
resonant implementations of the Josephson parametric
amplifier (JPA), serving as a good system for reviewing
the fundamental concepts around parametric amplification.
All parametric amplifiers operate based on one fundamental principle: the incoming _signal_ photons are mixed
with an applied _pump_ tone via an intrinsic nonlinearity,
by which energy from the pump is converted into signal
photons and thereby providing gain. As we recall from

351
Sec. II, such a nonlinearity can be engineered in the microwave domain using Josephson junctions , and the
resonant parametric amplifiers are built from slightly anharmonic oscillators.
The first Josephson parametric amplifiers were built
from a coplanar waveguide resonator, made nonlinear by
adding a nonlinear Josephson contribution to its total
inductance, see Fig. 27(a). The word _parametric_ refers
to the process of modulating (or _pumping_ ) one of the
parameters of the systems equation-of-motion (such as
frequency or damping) in time 350,352,353 . The natural
way to perform this parametric pumping is to modulate
the nonlinear Josephson inductance, which in turn has
the effect of modulating the resonator frequency __ _r_ ( _t_ ) =
1 _/_ _L_ ( _t_ ) _C_ .


-----


52

(a) Josephson parametric amplifier (JPA)


(a)

(b)

| Resonator|SQUID|
|---|---|


![qe-guide-scqubits-oliver.pdf-51-4.png](qe-guide-scqubits-oliver.pdf-51-4.png)

![qe-guide-scqubits-oliver.pdf-51-0.png](qe-guide-scqubits-oliver.pdf-51-0.png)

(b) Current-pumping (4-wave mixing): _2_ p = __ s + __ i


30

20

10

0

-10

-20



![qe-guide-scqubits-oliver.pdf-51-5.png](qe-guide-scqubits-oliver.pdf-51-5.png)

![qe-guide-scqubits-oliver.pdf-51-6.png](qe-guide-scqubits-oliver.pdf-51-6.png)

![qe-guide-scqubits-oliver.pdf-51-7.png](qe-guide-scqubits-oliver.pdf-51-7.png)

![qe-guide-scqubits-oliver.pdf-51-9.png](qe-guide-scqubits-oliver.pdf-51-9.png)

![qe-guide-scqubits-oliver.pdf-51-8.png](qe-guide-scqubits-oliver.pdf-51-8.png)

![qe-guide-scqubits-oliver.pdf-51-10.png](qe-guide-scqubits-oliver.pdf-51-10.png)

__ s __ r __ s __ r __

||| a | in|p|Col4|Col5|Col6|
|---|---|---|---|---|---|

|G|| a | in|p|Col4|Col5|
|---|---|---|---|---|
||||||
||||||


![qe-guide-scqubits-oliver.pdf-51-1.png](qe-guide-scqubits-oliver.pdf-51-1.png)

(c) Flux-pumping (3-wave mixing): __ p = __ s + __


-30


![qe-guide-scqubits-oliver.pdf-51-11.png](qe-guide-scqubits-oliver.pdf-51-11.png)

![qe-guide-scqubits-oliver.pdf-51-13.png](qe-guide-scqubits-oliver.pdf-51-13.png)

![qe-guide-scqubits-oliver.pdf-51-12.png](qe-guide-scqubits-oliver.pdf-51-12.png)

![qe-guide-scqubits-oliver.pdf-51-14.png](qe-guide-scqubits-oliver.pdf-51-14.png)

__ s __ r _2_ r __ s __ r __ i _2_


/2 3 /2 5 /2 7 /2 9 /2


3 /2


![qe-guide-scqubits-oliver.pdf-51-2.png](qe-guide-scqubits-oliver.pdf-51-2.png)

Pump-phase angle _,  _ (rad)


FIG. 26. Phase-sensitive parametric amplification. **(a)** In
contrast to the phase-insensitive operation, phase-sensitive
parametric amplification allows us to suppress the noise along
one axis. Consequently, the noise is added to the other
quadrature. **(b)** Voltage gain as a function of pump-phase
angle, in which the amplification depends on the phase of the
pump, providing either amplification or de-amplification of
the quadrature voltage.

system, as reflected in its Hamiltonian. In the following, we briefly review the difference between these two
pump-schemes.

364
In the current-pumped case, the dynamics of the system has characteristics of a Duffing oscillator , with a
fourth-order nonlinear term in addition to the harmonic
oscillator term in its Hamiltonian

_H_ = __ _r_ _c_ __ _c_ + _Kc_ __ _c_ __ _cc,_ (186)

where _c_ denotes the resonator field operator and _K_ is the
Kerr-nonlinearity. This process is a so-called _four-wave_
_mixing_ process, since it mixes four photons: one signal
( __ _s_ ), one idler ( __ _i_ ), and two pump photons ( __ _p_ ), obeying
the energy conservation relation __ _s_ + __ _i_ = 2 __ _p_ , see Fig.
27(b). Pioneered by Yurke , this was the first demonstration of microwave amplification using a Josephson 352
parametric amplifier. When the signal and idler modes
are at the same frequency, the amplification is said to be
_degenerate_ . This pumping scheme is the foundation for
the Josephson Bifurcation Amplifier (JBA), developed
, which has been used to perform single-shot qubit readout, by mapping the quantum by Siddiqi _et al._ 356,365,366
states onto the high and low resonator field originating
from the sharp bifurcation point of the amplifier 367 .
In the other case, when the system is flux-pumped,
the parametric process is driven by threading a magnetic

|||a | in|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
| p||||||

|G||a | in|Col3| p|Col5|
|---|---|---|---|---|
||||||
||||||


![qe-guide-scqubits-oliver.pdf-51-3.png](qe-guide-scqubits-oliver.pdf-51-3.png)

FIG. 27. Circuit schematics and pump schemes of a Josephson parametric amplifier. The device consists of a quarterwavelength resonator (blue), represented as lumped elements, **(a)**
shorted to ground via a Kerr-nonlinearity consisting of two
parallel Josephson junctions (orange) forming a SQUID. The
pump (red) can be applied in two ways; either by modulating the current through the junctions (four-wave mixing) **(b)**
at the resonant frequency, __ _p_ __ _r_ , or **(c)** by modulating the
__
ac-flux  ac around a static dc-flux point  dc using a separate
fast-flux line (three-wave mixing). The flux pump is applied
at twice the resonant frequency, __ _p_ 2 __ _r_ .
__

flux  ac through a SQUID loop, thereby modulating the
frequency of the resonator. This results in a _three-wave_
_mixing_ process, comprising three photons: one signal,
one idler, and one pump photon, with __ _s_ + __ _i_ = __ _p_ , see
Fig. 27(c). Therefore, we see that the pump frequency is
about twice that of the signal __ _p_ 2 __ _s_ for __ _s_ __ _i_ . For
__ __
degenerate, flux-pumped systems, the leading nonlinearity is a third-order term, yielding a Hamiltonian

_H_ = __ _r_ _c_ __ _c_ + _K_ _pc_ __ _c_ __ + _p_ __ _cc_ _,_ (187)

where the _p_ operator denotes the flux-pump mode. This  

359
approach to building parametric amplifiers was developed by Yamamoto _et al._ , as well as by Sandberg _et_
_al._ 97 .
The flux-pumping scheme has several practical advantages. First, the large detuning of the pump makes it easier to filter, isolating the readout signal as its passing into
the digitizer downstream and preventing the saturation
of following amplifier stages. Second, if the resonator is


-----


53

distributing the nonlinearity across an array consisting of
many identical junctions, reducing the Kerr-nonlinearity

2
by a factor 1 representing the number of junctions in the array. This has been demonstrated by using _/N_ with _N_
a an array of SQUIDs in a resonator, rather than a single
one 360 .

However, despite the above mentioned engineering efforts to improve the resonator-based JPAs, the most
prominent approach to date is to get rid of the resonator
altogether and, instead, construct a microwave analog to
optical parametric amplifiers, where kilometers of weakly
nonlinear fibers are used. Such device is called a _traveling_
_wave parametric amplifier_ (TWPA) and was developed
to surmount the bandwidth and dynamic range limitations of the resonator-based JPAs.

Although operated in similar way, the nonlinearity of

391393
TWPAs can be realized in different ways, such as the kinetic inductance of a superconducting film or using
an array of Josephson junctions 330,394,395 , through which
the four-wave mixing process is distributed across a nonlinear lumped element transmission line, see Fig. 28(a).


a quarter-wavelength resonator, it has no resonant mode
at the pump frequency __ _p_ , reducing spurious population
or saturation of the system as well as backaction on the
qubits in the processor. Third, since the flux pump line
is a separate on-chip microwave line, no additional directional coupler is needed.
Due to its rich dynamics, flux-pumping has also
proven a useful platform to study the quantum dynamics of Josephson parametric oscillators, both in the
context of qubit readout 368371 , the dynamical Casimir
effect 372374 , and to better understand their complex
nonlinear dynamics 361,364,375379 .
In addition to the degenerate parametric interactions
described above, parametric gain can be obtained between different resonant modes; either between different
modes of the same resonator 329,380
381
, or in-between different resonators
340,382386
, as with the Josephson parametric converter (JPC) . In addition to the possibility of
isolating and amplifying certain frequencies, the JPC can
implement frequency conversion for which it has some
other areas of applications compared with other types of
parametric amplifiers.

**_3._** **_The traveling wave parametric amplifier_**

In the previously described JPA, parametric amplification is realized using resonators that enhance the
parametric interaction between the input signal and the
Josephson junction nonlinearity. Essentially, the Qenhancement of the resonator forces each photon to pass
through the junction on average Q times before leaving
the resonator, thereby enhancing the non-linear interaction. Albeit proven to be able to reach near the standardquantum limit of noise for readout of a small number of
qubits, the future direction of the community is heading
towards amplifier technologies which are compatible with
multiplexed readout of several qubits coupled to the same
amplifier chain In this context, resonatorbased parametric amplifiers suffer from two major drawbacks: First, the amplifier bandwidth is limited to the 65,66,387389 .
resonator linewidth, typically 10 50 MHz, practically
__ __
limiting the number of multiplexed frequencies that can
be amplified. Second, since the Josephson nonlinearity
is realized by a small number of junctions, the saturation power is low due to the interplay of higher order
nonlinearities, effectively taking the system outside its
desired operation regime 364,375,376,386 . In practice, this
limits how many readout resonators that can be simultanously read out.
These two bottlenecks can, to a degree, be overcome
with microwave engineering. For instance, the linewidth
can be made an order of magnitude wider by altering the
impedance along the resonator. This is called a steppedimpedance transformer, where the impedance is ramped
down from a matched 50 at the capacitor down to a
small impedance at the SQUID 390 shorting the device to
ground. Also the saturation power can be increased by


The Josephson TWPA consists of a few thousand identical unit cells, each comprising a shunt capacitor to
ground and a nonlinear Josephson inductor, together
yielding a characteristic impedance of _Z_ 0 = _L_ _J_ _/C_

__
50 , see Fig. 28(a).



The fact that the nonlinearity is distributed allows for
high saturation power, since each Josephson junction is
accessed once. However, even though energy conservation is satisfied, the four-wave mixing process in the device, there is a problem with phase (or momentum) conservation. This is associated with the system nonlinearity as well as the large frequency detuning between signal
and pump photons, yielding a difference in phase-velocity
between the two, which in turn gives rise to a non-flat
gain profile, as well as an overall reduction in gain 394 .

Again, by taking inspiration from the dispersive engineering developed in quantum optics and photonics,
where the refractive index can be periodically altered to
engineer the momentum of a transferred signal, the solution to this phase-mismatch problem was introduced
by OBrien . By introducing resonators at periodic intervals of TWPA unit cells, the pump tone can be _et al._ 394
given a momentum kick, effectively slowing it down and
phase-matching the device by means of its wave vector.
This technique is called resonant-phase matching (RPM),
see Fig. 28(d), and requires that the pump frequency
is set on the left side of the dispersion feature (where
the wave vector diverges), defined by the resonant frequency of the phase-matching resonators. Note, finally,
that broadband parametric amplification with high dynamic range has been demonstrated in other Josephsonbased circuits, e.g. the superconducting nonlinear asymmetric inductive element (SNAIL) parametric amplifier
(SPA) 396 .


-----


54


ments with high signal-to-noise ratio. Putting these advances together, we hope that it is clear that the planar
superconducting qubit modality is a promising platform
for realizing near-term medium scale quantum processors. While we have focused on highlighting the advances
made within the fields of realizing, controlling and reading out planar superconducting qubits specifically used
for quantum information processing, there has of course
also been tremendous activity in the surrounding fields.
In this final section, we briefly mention a few of those
fields, and invite the reader to look into the references,
for further details.
Quantum annealing: Superconducting qubits
also form the basis for certain quantum annealing
platforms . Quantum annealing operates by finding the ground state of a given Hamiltonian (typically 397,398
a classical Ising Hamiltonian), and this state will
correspond to the solution of an optimization problem.
By utilizing a flux-qubit type design (see Sec.II, the

88
company D-Wave have demonstrated quantum annealing processors which have now reached beyond 2000
qubits 399 . The benchmarking of quantum annealers
and attempts to demonstrate a quantum speedup for a
general class of problems is a highly active research field,
and we refer the reader, for example, to recent papers
Refs. 400402 and references therein.
Cavity based QIP: A parallel effort to the planar superconducting qubits discussed in this review is the development of 3D cavity-based superconducting qubits.
In these systems, quantum information is encoded
in superpositions of coherent photonic modes of the
cavity 101 . The cat states can be highly coherent due
to the inherently high quality factors associated with 3D
cavities 102,403,404
405
. This approach has a fairly small hardware overhead to encode a logical qubit , and lends
itself to certain implementations of asymmetric errorcorrecting codes due to the fact that errors due to singlephoton loss in the cavity is a tractable observable to
decode. Using this architecture, several important advances were recently demonstrated including extending

100
the lifetime of an error-corrected qubit beyond its constituent parts , randomized benchmarking of logical
operations 405 , a CNOT gate between two logical qubits 406

as well as Ramsey interference of an encoded quantum
error corrected qubit 407 .
Cryogenics and software development: We briefly
mentioned the electrical engineering, software development, and cryogenic considerations associated with the
control wiring and on-chip layout of medium-scale quantum processors. While dilution refrigerators are now
readily available, off-the-shelf commercial products, the
details of how to optimally do signal-routing and rapid
data processing in a scalable fashion, is also a field in
rapid development.

408414
However, with the recent demonstrations of enabling technologies such as 3D integration, packages for multi-layered devices and superconducting interconnects
, some of the immediate concerns for how to scale the _number_ of qubits in the su-


(a) Josephson traveling wave parametric amplifier (JTWPA)

![qe-guide-scqubits-oliver.pdf-53-0.png](qe-guide-scqubits-oliver.pdf-53-0.png)

(b)

![qe-guide-scqubits-oliver.pdf-53-1.png](qe-guide-scqubits-oliver.pdf-53-1.png)

(c)


15

10


![qe-guide-scqubits-oliver.pdf-53-2.png](qe-guide-scqubits-oliver.pdf-53-2.png)

Frequency (GHz)

4 6

![qe-guide-scqubits-oliver.pdf-53-3.png](qe-guide-scqubits-oliver.pdf-53-3.png)

Frequency (GHz)


10

10


(d)

0.20


(d)


0.15

0.10

0.05

0.00


FIG. 28. Simplified circuit representation of a Josephson traveling wave parametric amplifier (JTWPA). The characteristic impedance for each unit cell is set by the in-line **(a)**
Josephson inductor, _L_ _J_ (orange) and the shunt capacitor, _C_
(blue). A resonant LC-circuit (red) is used to phase match
the four-wave amplification process. **(b)** Schematic of how the
signal gets amplified in each unit cell as it propagates through
the device. **(c)** Gain vs. frequency for a JTWPA, with and
without the resonant phase matching (RPM). **(d)** Dispersion
relation of the TWPA, where the LC-resonators collectively
open up a stopband at the resonant frequency. By applying
the pump close to this frequency, the wave vector of the pump
can be set to obtain a phase-matching. The optimal pump
frequency depends on the pump power, as indicated in the
inset. Image courtesy of Kevin OBrien 330,394

**VI.** **SUMMARY AND OUTLOOK**

In this review, we have discussed the phenomenal
progress over the last decade in the engineering of superconducting devices, the development of high-fidelity
gate-operations, and quantum non-demolition measure-


-----


55

of remote entanglement, enabling quantum information

429,430
to be distributed across different nodes of a quantum processing network .
Quantum computational supremacy: Finally, we mention one of the grand challenges for superconducting

431
qubits in the coming years: the demonstration of quantum computational supremacy . The basic idea is to
demonstrate a calculation, using qubits and algorithmic
gates, which is outside the scope of classical computers (assuming some plausible computational complexity
conjectures). For a recent review article, the reader is
referred to Ref. 432 . A first step towards an approach

270
to demonstrating quantum supremacy was recently reported, using 9 tunable transmons . It is expected
that with somewhere between 50-100 qubits , an extension of the protocol from Refs.270 and 434, will allow researchers to sample from a classically intractable 433
distribution, and thereby demonstrate quantum computational supremacy. The success of this program would
constitute a phenomenal result for all of quantum computing.

**ACKNOWLEDGMENTS**

The authors gratefully acknowledge Mollie KimchiSchwartz, Jochen Braum uller, Niels-Jakob Se Loft, and
David DiVincenzo for careful reading of the manuscript
and Youngkyu Sung for use of his time-dependent qubit
drive simulation suite and useful feedback from the entire Engineering Quantum Systems group at MIT. The
authors also acknowledges fruitful discussion with Anton
Frisk Kockum, Anita Fadavi Roudsari, Daryoush Shiri,
and Christian Kri zan.
This research was funded in part by the U.S. Army Research Office Grant No. W911NF-14-1-0682; and by the
National Science Foundation Grant No. PHY-1720311.
P.K. acknowledges partial support by the Wallenberg
Centre for Quantum Technology (WACQT) funded by
Knut and Alice Wallenberg Foundation. M.K. gratefully
acknowledges support from the Carlsberg Foundation.
The views and conclusions contained herein are those of
the authors and should not be interpreted as necessarily
representing the official policies or endorsements of the
US Government.


perconducting modality, have been addressed. On the
control software side, there currently exist multiple commercial and free software packages for interfacing with
quantum hardware, such as QCoDeS 415 , the related
pyCQED . However, many laboratories use software platforms developed in-house, often due to the concurrent development of custom-built, 416 , qKIT 417 and Labber 418
highly specialized electronics and FPGA circuits (many

420
of these developments are not always published, but readers may consult Refs. 190, 191, and 419 for three examples). There is currently also a large ongoing development of quantum circuit simulation and compiling software packages. Packages such as Qiskit , Forest (with
pyQUIL 421 ), ProjectQ 422 , Cirq 423 , OpenFermion 424 , the
Microsoft Quantum Development kit provide higherlevel programming languages to compile and/or optimize 425
quantum algorithms. For a recent review and comparison of these different software suites, we refer to Ref.426
and Ref.183 for a general review on advances in designing quantum software. Since the connectivity and gate
set of quantum processors can differ, details of the gate
compilation implementation is an important non-trivial
problem for larger-scale processors. We note that some
of these software packages already interface directly with
quantum processors that are available online, supplied,
for example, via Rigetti Computing or the IBM Quantum Experience.

Quantum error correction: While the qubit lifetimes
and gate fidelity have improved dramatically in the last
decades, there remains a need for error correction to

427
reach large-scale processors. While certain strategies exist to extend the computational reach of current state-ofthe-art physical qubits , for truly large-scale algorithms
addressing practical problems, the quantum data will
have to be embedded in an error-correcting scheme. As
briefly mentioned in Sections IV F 2 and IV G 2, certain
components of the surface code quantum error correcting
scheme have already been demonstrated in superconducting qubits (see e.g. Refs.66, 258, and 285). However,
the demonstration of a logical qubit with greater lifetime than the underlying physical qubits, remains an outstanding challenge. While the surface code is a promising quantum error correcting code due to its relatively
lenient fault tolerance threshold, it cannot implement a
_universal_ gate set in a fault-tolerant manner. This means
that the error-corrected gates in the surface code need to
be supplemented, for example, with a T gate, to become
universal.
428
Such gates can be implemented by a technique known as _magic state distillation_ . The process
of , a pre-cursor to magic state distillation, has already been demonstrated using FPGA-based _gate-teleportation_
classical feedback with planar superconducting qubits 191 ,
but showing distillation and injection into a surface code
logical state remains an open challenge. The development of new quantum codes is also a field in rapid development, and the reader may consult a recent review for
more details e.g. Ref.184. Another important step towards large-scale quantum processor architecture is that
