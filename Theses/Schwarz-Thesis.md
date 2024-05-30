
**Engineering Dissipation to Generate Entanglement Between Remote**

**Superconducting Quantum Bits**

by

Mollie Elisheva Schwartz

A dissertation submitted in partial satisfaction of the

requirements for the degree of

Doctor of Philosophy

in

Physics

in the

Graduate Division

of the

University of California, Berkeley

Committee in charge:

Professor Irfan Siddiqi, Chair

Professor Holger M uller

Professor K. Birgitta Whaley

Fall 2016


-----


**Engineering Dissipation to Generate Entanglement Between Remote**

**Superconducting Quantum Bits**

Copyright 2016

by

Mollie Elisheva Schwartz


-----


**Abstract**

Engineering Dissipation to Generate Entanglement Between Remote Superconducting

Quantum Bits

by

Mollie Elisheva Schwartz

Doctor of Philosophy in Physics

University of California, Berkeley

Professor Irfan Siddiqi, Chair

Superconducting quantum circuits provide a promising avenue for scalable quantum com-

putation and simulation. Their chief advantage is that, unlike physical atoms or electrons,
these artificial atoms can be designed with nearly-arbitrarily large coupling to one another
and to their electromagnetic environment. This strong coupling allows for fast quantum bit
(qubit) operations, and for efficient readout. However, strong coupling comes at a price: a
qubit that is strongly coupled to its environment is also strongly susceptible to losses and
dissipation, as coherent information leaks from the quantum system under study into inaccessible bath modes. Extensive work in the field is dedicated to engineering away these
losses to the extent possible, and to using error correction to undo the eects of losses that
are unavoidable.

This dissertation explores an alternate approach to dissipation: we study avenues by

which dissipation itself can be used to generate, rather than destroy, quantum resources. We
do so specifically in the context of quantum entanglement, one of the most important and
most counter-intuitive aspects of quantum mechanics. Entanglement generation and stabilization is critical to most non-trivial implementations of quantum computing and quantum
simulation, as it is the property that distinguishes a multi-qubit quantum system from a
string of classical bits. The ability to harness dissipation to generate, purify, and stabilize
entanglement is therefore highly desirable.

We begin with an overview of quantum dissipation and measurement, followed by an in-

troduction to entanglement and to the superconducting quantum information architecture.
We then discuss three sets of experiments that highlight and explore the powerful uses of dissipation in quantum systems. First, we use an entangling measurement to probabilistically
generate entanglement between two qubits separated by more than one meter of ordinary
cable. This represents the first achievement of remote entanglement in a superconducting
qubit system, which will be a critical capability as quantum computers and simulators scale.
We then use a nearly-quantum limited amplifier to unravel individual quantum trajectories
of the system under that entangling measurement, performing the first systematic explo-


-----


ration of entangled trajectories in any physical implementation. We finally demonstrate

deterministic entanglement by engineering a lossy quantum environment to efficiently generate and stabilize entangled states with both frequency and symmetry selectivity. These
experiments provide evidence that explicitly building dissipation into an engineered quantum system can enable, rather than hinder, the study of fundamental quantum mechanics
and complex many-body Hamiltonians.


-----


_Nothing works unless you do._

_Maya Angelou_


-----


ii

# Contents

**Contents** **ii**

**List of Figures** **v**

**1** **Introduction** **1**

1.1 Superconducting Qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.2 Strong Coupling: A Blessing and a Curse . . . . . . . . . . . . . . . . . . . . 3

1.3 Complementary Approaches to Dissipation . . . . . . . . . . . . . . . . . . . 4

1.4 Overview and Summary of Results . . . . . . . . . . . . . . . . . . . . . . . 5

**2** **Dissipation and Continuous Measurement** **7**

2.1 Introduction to Weak Quantum Measurements . . . . . . . . . . . . . . . . . 8

2.1.1 Projective Measurements . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.1.2 The Stern-Gerlach Experiment: Projective Regime . . . . . . . . . . 9

2.1.3 The Stern-Gerlach Experiment: Weak Measurement Regime . . . . . 11

2.2 The Quantum Bayesian Formalism . . . . . . . . . . . . . . . . . . . . . . . 14

2.3 The Stochastic Master Equation . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.3.1 Dissipation via Fluctuation: Lindblad Operators . . . . . . . . . . . . 17

2.3.2 Measurement in the SME formalism . . . . . . . . . . . . . . . . . . . 19

2.4 Measurement Rate and Inefficient Measurements . . . . . . . . . . . . . . . . 20

2.5 Summary of Measurement and Dissipation . . . . . . . . . . . . . . . . . . . 22

**3** **Entanglement: A Primer** **23**

3.1 Introduction to Entanglement . . . . . . . . . . . . . . . . . . . . . . . . . . 24

3.2 Defining Entanglement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

3.3 Useful Measures of Entanglement . . . . . . . . . . . . . . . . . . . . . . . . 26

3.3.1 Von Neumann entanglement entropy . . . . . . . . . . . . . . . . . . 26

3.3.2 Entanglement of formation . . . . . . . . . . . . . . . . . . . . . . . . 27

3.3.3 Entanglement witnesses . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.3.4 CHSH measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.3.5 Tomographic methods . . . . . . . . . . . . . . . . . . . . . . . . . . 29


-----


iii

**The Superconducting cQED Architecture** **32**

4.1 Superconducting Qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

4.1.1 The transmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

4.2 The Jaynes Cummings Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . 37

4.2.1 Derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

4.2.2 Near-resonant case . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

4.2.3 Dispersive (far-detuning) limit . . . . . . . . . . . . . . . . . . . . . . 39

4.3 Dispersive Readout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

4.3.1 Semiclassical treatment . . . . . . . . . . . . . . . . . . . . . . . . . . 41

4.3.2 Coherent states and measurement uncertainty . . . . . . . . . . . . . 42

4.3.3 Unconditioned master equation . . . . . . . . . . . . . . . . . . . . . 43

4.3.4 Dispersive measurement: Bayesian approach . . . . . . . . . . . . . . 46

4.3.5 Dispersive measurement: Master equation approach . . . . . . . . . . 47

4.4 Parametric Amplification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

4.4.1 The lumped Josephson parametric amplifier . . . . . . . . . . . . . . 49

4.4.2 Phase-sensitive amplification . . . . . . . . . . . . . . . . . . . . . . . 50

4.5 Summary: The Superconducting Qubit Toolbox . . . . . . . . . . . . . . . . 52

**Remote Measurement-Induced Entanglement** **53**

5.1 Historical Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

5.2 Design of an Entangling Continuous Measurement . . . . . . . . . . . . . . . 56

5.2.1 Joint dispersive measurement . . . . . . . . . . . . . . . . . . . . . . 56

5.2.2 Tuning the entangling measurement . . . . . . . . . . . . . . . . . . . 59

5.2.3 Verification of the half-parity measurement . . . . . . . . . . . . . . . 60

5.3 Bayesian Theory of the Entangling Measurement . . . . . . . . . . . . . . . 60

5.4 Full Calibration of the Experimental Apparatus . . . . . . . . . . . . . . . . 64

5.4.1 Detailed experimental setup . . . . . . . . . . . . . . . . . . . . . . . 65

5.4.2 Cavity parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

5.4.3 Qubit lifetimes and coherences . . . . . . . . . . . . . . . . . . . . . . 67

5.4.4 Calibration of photon number, dispersive shifts, and inter-cavity transmission efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

5.4.5 Calibration of __ meas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

5.5 Tomographic Reconstruction of Entanglement Dynamics . . . . . . . . . . . 69

5.5.1 Characterizing the tomographic reconstruction . . . . . . . . . . . . . 71

5.5.2 Entanglement dynamics . . . . . . . . . . . . . . . . . . . . . . . . . 74

5.6 Discussion of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

**Quantum Trajectories** **79**

6.1 Experimental Generation and Verification of Entangled Trajectories . . . . . 80

6.1.1 Generating quantum trajectories . . . . . . . . . . . . . . . . . . . . 81

6.1.2 Validating the quantum trajectories . . . . . . . . . . . . . . . . . . . 82

6.2 Statistical Properties of Concurrence Trajectories . . . . . . . . . . . . . . . 85


-----


iv

6.2.1 Concurrence-readout relationship . . . . . . . . . . . . . . . . . . . . 85

6.2.2 Probability density function for concurrence trajectories . . . . . . . 87

6.2.3 Distribution of time to maximum concurrence . . . . . . . . . . . . . 90

6.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

**7** **Symmetry-Selective Bath Engineering** **93**

7.1 Experimental Design and Protocol . . . . . . . . . . . . . . . . . . . . . . . 94

7.1.1 Entangling protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

7.1.2 Symmetry-selectivity of protocol . . . . . . . . . . . . . . . . . . . . . 98

7.2 Theoretical Treatment of the Bath Drives . . . . . . . . . . . . . . . . . . . 98

7.2.1 Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

7.2.2 Eective driven-dissipative _XY_ model . . . . . . . . . . . . . . . . . 100

7.2.3 Protocol for generating entanglement . . . . . . . . . . . . . . . . . . 104

7.3 Full Experimental Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . 106

7.3.1 Detailed Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . 106

7.3.2 Coupling of the cavities . . . . . . . . . . . . . . . . . . . . . . . . . 108

7.3.3 Qubit parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

7.3.4 Path length calibration . . . . . . . . . . . . . . . . . . . . . . . . . . 111

7.3.5 Balancing the cooling drive amplitudes . . . . . . . . . . . . . . . . . 111

7.3.6 Tomography calibration . . . . . . . . . . . . . . . . . . . . . . . . . 113

7.4 Experimental Implementation of the Bath Engineering Protocol . . . . . . . 115

7.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

**8** **Conclusions and Outlook** **120**

8.1 Extensions of Measurement-Induced Entanglement . . . . . . . . . . . . . . 121

8.2 Further Applications of Dissipation-Induced Entanglement . . . . . . . . . . 122

**Bibliography** **124**


-----


# List of Figures

2.1 Stern-Gerlach Experiment (Strong) . . . . . . . . . . . . . . . . . . . . . . . . . 11

2.2 Stern-Gerlach Experiment (Weak) . . . . . . . . . . . . . . . . . . . . . . . . . . 12

4.1 Josephson Junctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

4.2 Cooper Pair Box Spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

4.3 Transmon Qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

4.4 cQED Readout Schematic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

4.5 Dispersive measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

4.6 Lumped Josephson Parametric Amplifier . . . . . . . . . . . . . . . . . . . . . . 50

4.7 Phase-Sensitive Amplification . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

5.1 Hong-Ou-Mandel Eect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

5.2 Simplified experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

5.3 Sequential joint dispersive measurement . . . . . . . . . . . . . . . . . . . . . . 58

5.4 Choosing an operating frequency . . . . . . . . . . . . . . . . . . . . . . . . . . 59

5.5 Fiducial state readout histograms . . . . . . . . . . . . . . . . . . . . . . . . . . 61

5.6 Full experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

5.7 _n_ , __ loss , and __ calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

5.8 Calibration of __ meas and _G_ chain . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

5.9 Pulse sequence for entanglement generation and verification . . . . . . . . . . . 70

5.10 Tomography calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

5.11 Entangled density matrix dynamics . . . . . . . . . . . . . . . . . . . . . . . . . 75

5.12 Selected full density matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

5.13 Evolution of concurrence of entangled state . . . . . . . . . . . . . . . . . . . . 76

6.1 Modified setup for trajectories . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

6.2 Conditional tomography at fixed time . . . . . . . . . . . . . . . . . . . . . . . . 83

6.3 Full tomographic mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

6.4 An exemplar quantum trajectory . . . . . . . . . . . . . . . . . . . . . . . . . . 85

6.5 Readout histograms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87

6.6 Concurrence probability distribution function . . . . . . . . . . . . . . . . . . . 88

6.7 Time-to-maximum concurrence distribution . . . . . . . . . . . . . . . . . . . . 90


-----


vi

7.1 Base-Temperature Schematic . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94

7.2 Avoided crossings in cavity and qubit sectors . . . . . . . . . . . . . . . . . . . . 96

7.3 Protocol for symmetry-selective cooling . . . . . . . . . . . . . . . . . . . . . . . 97

7.4 Detailed experimental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

7.5 Calibration of _g_ and __ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110

7.6 Path length calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

7.7 Cooling drive amplitude calibration . . . . . . . . . . . . . . . . . . . . . . . . . 113

7.8 Tomography pulse crosstalk calibration . . . . . . . . . . . . . . . . . . . . . . . 114

7.9 Pulse sequence for entanglement generation and verification . . . . . . . . . . . 115

7.10 Demonstration of symmetry- and frequency- selective bath engineering . . . . . 116

7.11 Cooling dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117


-----


vii

### Acknowledgments

Graduate school is alternately an exhilarating, terrifying, rejuvenating, depressing, elat-

ing, anxiety-baiting, and confidence-building experience - and often, it is all of these things
simultaneously. I am so grateful for the network of people that bolstered me through the
last five years. I have grown tremendously as a woman and as a scientist, and I have many
people to thank for shepherding me through this process.

Professionally and scientifically, I could not have asked for a more competent, generous,

and supportive group of people to work with than the members of the Quantum Nanoelectronics Laboratory. Of course the credit for this begins with our adviser Irfan Siddiqi, whose
scientific acumen, collegiality, and thoughtful leadership set the tone for our group. I have
enjoyed our technical, strategic, and personal conversations over the years, and you have set
a strong example for what a career in science can become. Im particularly thankful to Chris
Macklin, who answered many stupid questions during my first year in lab; to Nicolas Roch,
with whom I spent many mornings, evenings, and weekends fighting with microwaves and
qubits and from whom I learned a great deal technically and professionally; to Leigh Martin
and Manu Flurin, who engineered baths with me and helped me pull oan extraordinary
eleventh-hour result; and to the entire group, for demonstrating that openness, curiosity,
teamwork, ambition, and mutual support can grow and thrive in an academic setting.

I also must acknowledge the people who guided me along the path to graduate school. The

Pennsylvania Governors School for the Sciences gave me an early taste of rigorous scientific
study and physics research, and I am so glad that this program has survived budget cuts
and economic downturns through the heroic work of the PGSS Alumni Association. Prof.
Tom Solomon, my first research adviser during my undergraduate degree, treated me as a
colleague, and gave me room to experiment, fail, and grow. He taught me to be technically
creative and resourceful, skills that have carried through my career. Horst Stormer, Philip
Kim, and Erik Henriksen introduced me to the excitement of research at the forefront of a
hot field, and have served as mentors and friends in the years since. I am also grateful to my
colleagues at the Science and Technology Policy Institute, particularly Sarah Ryker, Sarah
Rees, and Jason Gallo, for giving me the opportunity to explore the role and limitations of
science in society at large.

I am deeply grateful to the Fannie and John Hertz Foundation, which funded my graduate

degree. The Hertz fellowship represents far more than the financial means to pursue a

Ph.D.: it also has provided professional development to build an expanded perspective about
scientific career paths, and an invaluable community of peers and alumni who have provided
commiseration, perspective, and reinforcement throughout the course of my degree. I have
loved being a part of this community, and hope to benefit from and give back to it over the
course of my career.

Physics can be a lonely enterprise for women, and even more so for other under-represented

minorities. I am grateful for the talented, brilliant, sassy women with whom I found solidarity
and inspiration: Natania Antler, Sydney Schreppler, Allison Dove, Kristi Beck, Tova Holmes,
Kate Kamdin, Abi Polin, Hilary Jacks, Simca Bouma, Tess Smidt, Shawna Seth, Justine


-----


viii

Sherry, and so many others. Our afternoon teas, evening ports, and weekend brunches

brought levity and lightness to my time at Berkeley, and I look forward to seeing the paths
you travel.

The support of my family has been central to my success and happiness over the last five

years. My parents, Jan and Elaine, never doubt my abilities, and help give me confidence to
push myself deeper and farther into my work. My brothers, Eben, Isaac, and David, keep
me grounded and provide comic relief in themselves, their fabulous spouses (Kate, Elyse,
and Joni, who are sisters to me), and their adorable children (Margot, Asa, Haim, Lida, and
counting). And the influence of my grandparents Howard, Harriet and Mary, whom I miss
very much, reverberates in my life and my profession. I am so grateful for the example they
set with their lives and their counsel.

Finally, to my husband Itamar. I never would have imagined that going to the Physics

Social Hour to relax after handing in a problem set would lead to meeting the love of
my life and kicking oa lifetime adventure together. Thank you for your love, support,
patience, compassion, company, laughter, and strength. We have stuck together through
dierent cities, opposite coasts, late nights, early mornings, high moments and low, and I
cant imagine doing any of this without you.


-----


# Chapter 1

 Introduction

All the mental eort of an assiduous investigator must indeed
appear vain and hopeless, if he does not occasionally run across
striking facts which form incontrovertible proof of the truth he
seeks, and show him that after all he has moved at least one step
nearer to his objective.

Max Planck, _The Origin and Development of the Quantum Theory_ ,

1920

Entanglement is perhaps the most puzzling component of quantum theory, one that

challenges classical conceptions of causality and locality. Two quantum objects that are
entangled with one another carry coherent quantum information in their joint correlations,
rather than in their individual states. The information shared between the two quantum
systems remains entangled, even if the systems are separated by light years. As a result,
making a measurement of one of the system causes an instantaneous projection of the other.
This spooky action at a distance, as famously described by (and philosophically reviled
by) Albert Einstein, is at the heart of quantum physics.

In addition to the fascinating philosophical questions raised by the existence of entangle-

ment, it also is fundamental to a number of very practical applications of quantum mechanics.
Quantum computation, networking, cryptography, and simulation all rely on the ability to
generate, manipulate, and measure entangled states. However, bringing entanglement out
of the abstract world of thought-experiments and into the physical realm of experimental
apparatuses requires us to grapple with the inevitable nonidealities of the physical world.
Even the most highly-isolated quantum systems must interact with their environment in
some way, and therefore gradually lose information to it in dissipative processes. Moreover,
a perfectly isolated and noninteracting quantum object by definition cannot be measured,
and therefore cannot be useful for the study of fundamental physics or for more practical
applications. We therefore need to develop an understanding of how noisy processes aect
entangled states.


-----


_CHAPTER 1. INTRODUCTION_ 2

In this dissertation, we will explore the interfaces between entanglement, measurement,

and dissipation. We will see that entanglement is critical to the process of measurement, even
as measurement of an entangled state generally destroys that entanglement. We will also
discover that dissipation and measurement are complementary processes: they both involve
carrying information away from a quantum system, and either observing or losing that
information. We will then describe a series of experiments that demonstrate the potential
for noisy processes to serve as a resource for generating and stabilizing entanglement. We
will do all of this in the context of the superconducting quantum circuit architecture, which
represents a promising approach to scalable quantum experiments.

## 1.1 ## Superconducting Qubits

In order to study fundamental quantum mechanics or to work toward a practical quantum
computer or simulator, we must move beyond the realm of _gedanken_ experiments and build
a physical apparatus for trapping, stabilizing, and manipulating single quantum degrees of
freedom. Deep interest in exploring the details of quantum physics has led to an explosion
of experimental eorts dedicated to designing and perfecting long-lived, addressable quantum systems. This is no mean task: we do not feel quantum eects in daily life because
quantum information is quickly destroyed when a coherent quantum system is brought into
contact with the larger classical world occupied by bulk experimental equipment and brutish,
macroscopic physicists.

Most practical quantum systems are based around conceptual building blocks of quantum

systems that are restricted to two levels. In analogy with classical computational building
blocks, these are known as quantum bits, or qubits: these are two-level quantum systems
that, unlike their classical binary counterparts, are able to exist in a superposition of their two
states and to become entangled with one another so that information is distributed across the
entire qubit array. There are a broad range of physical qubit implementations, all of which
have advantages and disadvantages. A number of quantum information implementations,
including trapped ions [16], neutral atoms [711], nitrogen-vacancy (NV) centers in diamond

[12, 13], and semiconductor quantum dots [1416] utilize a physical atom or electron to carry
quantum information. The advantage of these approaches is that the system under study is
inherently a fully quantum object, whose well-defined energy levels are unevenly spaced such
that individual transitions can be readily and uniquely addressed. However, electrons and
atoms are inherently tiny, and have a small scattering cross-section. Generating large dipole
interactions between the qubit and a macroscopic electromagnetic measurement apparatus
can therefore be quite challenging [1719]. Similarly, generating significant couplings between
these spins in order to create entanglement can be difficult; these systems typically require
relatively long gate times.

Superconducting qubits [2022], the physical system that we will use to study quantum

physics in this dissertation, represent an artificial atom generated from the collective behavior
of Cooper pairs as they tunnel across a weak barrier. The superconducting qubit is a


-----


_CHAPTER 1. INTRODUCTION_ 3

macroscopic object that, rather amazingly, behaves like a single quantum degree of freedom.
Because of its macroscopic nature, it is straightforward to design the superconducting qubit
circuit to have an intrinsically large dipole moment: its physical extent can be on the order
of millimeters (in comparison to the nanometer-sized dipole of a physical atom). As we will
see in Chapter 4, the designability of the form factor in the superconducting qubit is one of
its chief strengths and defining features. The strong coupling limit, in which the qubit-cavity
coupling _g_ _qc_ is larger than the cavity leakage rate __ and the qubit decay rate __ can be met
using superconducting qubits with minimal design eort.

## 1.2 ## Strong Coupling: A Blessing and a Curse

The inherent strong coupling in the superconducting qubit architecture is one of its greatest
strengths. The ease of generating strong interactions means that performing single-shot qubit
state readout mediated by a cavity (Chapter 4.3) is relatively straightforward [9, 2325]. In
addition, two-qubit gates can be accomplished quickly: qubits that can be strongly coupled
to the environment can also be strongly-coupled to one another, either directly or via cavitymediated coupling [2631]. As a result, single- and multiple-qubit gates can be performed on
the nanosecond timescale. The ease of readout and tunable multi-qubit coupling have made
superconducting qubits one of the most promising avenues for scalable quantum computation.
This is evidenced by growing investment in the technology on the part of profit-driven
industrial leaders, building on decades of fundamental research in universities and national
laboratories.

While strong coupling is critical to the operation of superconducting qubits, it also comes

with significant drawbacks. Superconducting qubits couple not only to one another and to
a carefully engineered readout mechanism: they couple strongly to virtually everything!
Although the collective behavior of Cooper pairs in an aluminum substrate causes them to
act like a single quantum object, the physical circuit can extend over hundreds of micrometers
to millimeters. The qubit interacts with defects in the silicon or sapphire substrate, with
impurities in the superconductor, with quasiparticle excitations, with residual photons in
the cavity, and with any number of other spurious quantum systems that form the qubits
environment. These local interactions carry quantum information away from the system,
storing it instead in bath modes. This information still exists, but it is no longer in a
form that the experimenter can capture or utilize; from our perspective, it is lost. Often,
these inacessible degrees of freedom fluctuate stochastically: as qubits interact with a noisy
variable, they themselves take on random behavior that makes it increasingly difficult to
reliably prepare and maintain a desired state.

From the standpoint of the observer, local interactions that cannot be detected appear as

dissipation, or lost information. Dissipation generally manifests as qubit decay (if the dissipation is caused by the qubit directly exchanging photons with a lossy mode) or as decoherence
(if the interaction causes un-measured shifts in the qubit frequency). For superconducting
qubits, state-of-the-art coherence times are in the tens to hundreds of microseconds [3235].


-----


_CHAPTER 1. INTRODUCTION_ 4

This is orders of magnitude longer than the lifetime of coherent oscillations observed in the
first Cooper pair box qubit [36], but still well short of the lifetimes in atomic systems. Qubit
decoherence and decay puts a ceiling on the achievable fidelity of a quantum gate, which
is performed in finite time. The eects of dissipation diminish the quality of quantum manipulations in operations that require multiple gates and a significant fraction of the qubit
coherence times. As superconducting qubit circuits grow to include tens of qubits in increasingly sophisticated circuits, perhaps including several chips organized in a quantum network,
dissipation therefore rapidly becomes a limiting eect.

## 1.3 ## Complementary Approaches to Dissipation

Dissipation, unsurprisingly, is almost universally viewed as the enemy of coherent quantum
computation. Great eorts are taken to prevent, mitigate, and correct for the eects of
dissipation. Historically, this has taken the form of improved microwave engineering [32, 37
40], intelligent sculpting of the electromagnetic environment [41, 42], and detailed materials
study in order to limit quasiparticle and dielectric loss [4349]. If the intrinsic error rate is
sufficiently limited (even to 1% for some applications), it then becomes possible to introduce
active error correction in order to extend the eective lifetime of the qubits and perform
extended algorithms [5052]. There are already a number of exciting experiments that

implement active error correction [5357].

In this dissertation, we will take a complementary and somewhat counterintuitive ap-

proach. We take dissipation as a given in our system, and explore ways in which we can
actively _use_ that dissipation as an asset, rather than as a liability. This is a methodology
inspired by the axiom if you cant beat them, join them: understanding that one can never
fully eliminate dissipation from a physical system, it behooves us to find ways to explicitly
build dissipation into our quantum protocols and take advantage of its presence. This dissertation will probe a number of powerful contexts in which dissipation can be channeled
and harnessed to generate and stabilize entanglement between superconducting qubits. We
focus particularly on generating entanglement between remote qubits.

We utilize dissipation in two primary ways, the first of which is in the form of measure-

ment. It may be slightly odd at first to think of measurement as a form of dissipation.
However, measurement, as we will see in Chapter 2, is achieved by entangling a quantum
system of interest with a noisy degree of freedom, and then recording the fluctuations of
that degree of freedom. From the standpoint of the quantum system, the dynamics are identical to information being dissipated in a lossy mode; the only dierence is that when the
observer monitors that lossy channel, she is able to reconstruct the eects of the dissipation
and update her estimate of the quantum state accordingly. We will utilize a carefully designed measurement, coupled with a high-efficiency amplification chain, to probabilistically
generate entanglement between remote superconducting qubits. This is a critical capability: generating entanglement between quantum objects that do not directly interact with
one another is not a trivial task, but may play an important role in a distributed quantum


-----


_CHAPTER 1. INTRODUCTION_ 5

network.

We are also interested in using purely dissipative protocols to generate entanglement.

This approach is often referred to as bath engineering for its reliance on tailoring the
spectrum of the lossy bath modes. Bath engineering, which originated in the ion trapping
community [58, 59] and has seen a recent resurgence in the superconducting qubit community

[6064], typically relies on Raman-type scattering processes: we o-resonantly drive the bath
mode(s) such that the detuning between the drive and the bath corresponds to a relevant
transition in the qubit system. Suppose the drive is red-detuned from the bath: In order for
a drive photon to dissipate into the bath, it must first absorb the requisite energy from the
system in order to satisfy the conservation of energy. When the photon is absorbed in the
bath, it projects the quantum system into its lower energy state. This is the equivalent of
cooling the system. If instead the drive is blue-detuned from the bath, emitting a photon
requires exciting a transition in the system, or bath-mediated heating. Should the system, via
some other fluctuating interaction, decay to its original state, the drive re-pumps the system
into the target state at a rate limited by the dissipation rate in the bath mode. Thus, bath
engineering relies explicitly on dissipative processes in order to stabilize the quantum system
into a target state. In this dissertation, we will use bath engineering to deterministically
generate and stabilize entanglement, thus harnessing dissipation to preserve entanglement
rather than to destroy it.

## 1.4 ## Overview and Summary of Results

In this dissertation, we explore the uses and limitations of dissipation, through the lens
of generating entanglement in superconducting quantum systems. In Chapter 2, we will
provide an introduction to a fully quantum treatment of dissipation, as well as to a more
sophisticated mathematical and conceptual understanding of quantum measurement. In

doing so, we will uncover the deep connections between dissipation and measurement, which
will be critical for understanding the remainder of the dissertation. In Chapter 3, we will
review quantum entanglement: what it is, what it is not, and how we can quantify it in a
physical system. Chapter 4 is a broad overview of the constituents of the superconducting
qubit toolbox: the Josephson junctions and transmon circuits that form the qubits we utilize
in this dissertation; the coupling of those qubits to microwave cavities that we use to perform
sensitive, non-demolition measurements; and the parametric amplifiers that we use to bring
those measurements into the nearly quantum-limited regime.

In Chapters 5-7, we present a range of experiments in which we utilize dissipation to

generate, stabilize, and study entanglement. Chapter 5 describes the first demonstration
of entanglement between distant superconducting qubits: we house two qubits in cavities
that are separated by more than one meter of ordinary copper cable, and use a finely-tuned
measurement in order to probabilistically entangle them. In Chapter 6, we take a deep dive
into this measurement-induced entanglement scheme: we use highly-sensitive quantum amplifiers to unravel the instantaneous back-action of the measurement on the cascaded qubit


-----


_CHAPTER 1. INTRODUCTION_ 6

system, peering into the ensemble to study the distribution of individual system trajectories.
In Chapter 7, we utilize a purely dissipative protocol (requiring no measurement) to generate and stabilize bipartite entanglement. By engineering the symmetry of the dissipative
environment, we are able to selectively stabilize entangled states of a dynamically tunable
symmetry, while suppressing states of the opposite symmetry due to parity selection rules.
This demonstrates the power of engineering not just the energetic density of states, but also
the symmetry profile of lossy modes in a system. In Chapter 8, we discuss several avenues
for future developments of this work.

The original work reported in Chapters 5-7 was initially published in the following pub-

lications:

-  Chapter 5: Roch, N. et al. Observation of measurement-induced entanglement and

quantum trajectories of remote superconducting qubits. Phys. Rev. Lett. 112, 170501
(2014).

-  Chapter 6: Chantasri, A., Kimchi-Schwartz, M. E., Roch, N., Siddiqi, I. & Jordan,

A. N. Quantum trajectories and their statistics for remotely entangled quantum bits.
(2016). at http://arxiv.org/abs/1603.09623

-  Chapter 7: 1. Kimchi-Schwartz, M. E. et al. Stabilizing Entanglement via Symmetry-

Selective Bath Engineering in Superconducting Qubits. Phys. Rev. Lett. 116, 240503
(2016).

Other research undertaken and published during the course of the authors Ph.D training,
but not substantially included in this dissertation, include:

-  Macklin, C. et al. A near-quantum-limited Josephson traveling-wave parametric am-

plifier. Science 350, 307-10 (2015).

-  Weber, S. J., Murch, K. W., Kimchi-Schwartz, M. E., Roch, N. & Siddiqi, I. Quantum

trajectories of superconducting qubits. Comptes Rendus Phys. 17, 766-777 (2016).

-  McClean, J. R., Kimchi-Schwartz, M. E., Carter, J. & de Jong, W. A. Hybrid Quantum-

Classical Hierarchy for Mitigation of Decoherence and Determination of Excited States.
(2016). http://arxiv.org/abs/1603.05681


-----


# Chapter 2

 Dissipation and Continuous Measurement

[O]ne can hardly view the quantum theoretical description as a
complete representation of the physically real. If one attempts,
nevertheless, so to view it, then one must assume that the physically
real in B undergoes a sudden change because of a measurement in
A. My physical instincts bristle at that suggestion.

Albert Einstein, _Letter to Max Born_ , 1948

This dissertation, at its heart, is an exploration of the connections between measurement

and dissipation and the ways in which those connections can be harnessed. Quantum measurement is typically thought of as a process, more or less mysterious, that brings a system
from an initial superposition state into a single, final state: an electron exists everywhere
until it is detected, a quantum bit is simultaneously in its ground and excited state until it
is stochastically projected into one or the other. Dissipation plays a similar role in reducing
quantum coherence, by carrying quantum information away from the system under study
and storing it instead in inaccessible environmental degrees of freedom. Key to both of these
processes is a lack of fore-knowledge about what the ultimate state of the quantum system
will be. One could therefore speculate that perhaps there is a connection between dissipative
processes and measurement.

In this chapter, we will see that indeed, dissipation and measurement are intimately con-

nected. We will show that measurement can be considered a special case of a dissipative
process, one in which the environmental modes into which information dissipates can be
monitored, and the information thus extracted and preserved. In order to elucidate this
connection, we will require a more sophisticated understanding of quantum measurement,
and particularly of quantum measurement. We will begin with a phenomenological overview of quantum measurement in both the strong and weak regimes, and then will _continuous_
present two mathematical formalisms - the quantum Bayesian approach, and the stochastic


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 8

master equation - that allow us to treat and understand both measurement and dissipative
processes. This will provide us with a foundation and a context for the studies of entanglement under measurement and dissipation that will follow in this dissertation.

## 2.1 ## Introduction to Weak Quantum Measurements

In a typical quantum mechanics course, measurements are introduced as an instantaneous,
fully projective process. As we will see, this is a gross over-simplification of the physical
processes that underlie an experimentally-realizable quantum measurement. However, it is
useful to briefly review the physics of projective measurements in order to provide a starting
point for the more complicated discussion of continuous measurements.

### 2.1.1 ### Projective Measurements


For a measurement operator _A_  with measurement outcomes _a_ _n_ and non-degenerate eigen-


states _|_ _n_ _i_ , we can construct projection operators  _n_ = _|_ _n_ _i_ _h_ _n_ _|_ . The postulates of quan-


tum mechanics [66] then provide the following relations, for an arbitrary initial pure state
_i_ = _c_ _n_ _n_ :
_|_ _i_ _|_ _i_

P



_i_  _n_ _i_
P _a_ _n_ = _h_ _|_ _|_ _i_

_i_ _i_


; (2.1a)
_i_ _i_
_h_ _|_ _i_



_i_  _i_
= _h_ _|_ _A|_ _i_

_i_ _i_


_a_ _n_ P _n_ ; (2.1b)

(2.1c)


_i_ _i_
_h_ _|_ _i_


 _n_ _i_
_|_ _f_ _i |_ _a_ _n_ = _|_  _i_


_i_  _n_ _i_
_h_ _|_ _|_ _i_


These postulates state that the probability of measurement outcome _a_ _n_ is given by the


normalized matrix product of the starting state with the _n_ -th projector [Eq. (2.1a)]; that
the expectation value of _A_  is given by the weighted sum of the measurement outcome prob-

abilities [Eq. (2.1b)]; and that the final state of the system after measuring the outcome _a_ _n_
is given by the _n_ -th projector acting on the initial state [Eq. (2.1c)]. The final postulate
represents the famous collapse postulate [67].

In order to discuss mixed states, it is useful to translate these postulates into the language

of density matrices. The density matrix construction of these postulates, for arbitrary pure


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 9

or mixed initial density matrix __ _i_ is given by the following:


P _a_ _n_ = Tr _{_ __ _i_  _n_ _}_ ; (2.2a)


_h_ _Ai_  = Tr


__ _i_ 


(2.2b)


 _n_ __ _i_  _n_
__ _f_ _a_ _n_ = _._ (2.2c)
_|_ Tr  _n_ __ _i_  _n_

_{_ _}_


 _n_ __ _i_  _n_
__ _f_ _a_ _n_ =
_|_ Tr  _n_ __ _i_ 


In order to create a quantum _non-demolition_ (QND) measurement, the eigenstates _n_
_|_ _i_


of  must be identical to the eigenstates of the unperturbed system Hamiltonian _H_  0 . Equiv-
_A_


alently, _A_  must commute with _H_  0 . If _|_ _n_ _i_ is a simultaneous eigenstate of _H_  0 and _A_  , then


a system that begins in an eigenstate of the un-measured Hamiltonian will be projected
deterministically into that same state by the measurement operator. This is not to say that
a QND measurement has no eect at all - if the system were to begin in a superposition
of several eigenstates, the QND measurement would project it stochastically into one of the
eigenstates, thus destroying the superposition. However, once the system is in one of those
eigenstates, repeated measurements will not drive the system out of that state.


Thus far we have discussed only non-degenerate measurement operators. However, con-

sider the case of a degenerate measurement operator, in which two or more eigenstates
correspond to the same eigenvalue, or measurement outcome. This is particularly interesting in the QND case, as it implies that several eigenstates of  _H_ 0 may generate the same

measurement outcome. In this case, the measurement projects onto a multidimensional


eigenspace _n_ , rather than onto a single eigenvector. The projection operator is built of a
_E_
linear sum of eigenvectors that span _n_ , such that for _k_  _k_ = _a_ _n_ _k_ ,
_E_ _A |_ _i_ _|_ _i_


 _n_ =


_k_ _k_
_|_ _i_ _h_ _|_



 _k_ = _a_ _n_ _k_
_A |_ _i_ _|_ _i_





_._ (2.3)
_k_ _k_
_h_ _|_ _i_


This projection operator can be represented as a matrix whose rank corresponds to the
degeneracy of the eigenspace. As we will see in Chapter 5, such a degenerate measurement
can be exploited to project onto coherent superposition states, rather than onto a single
eigenstate.

### 2.1.2 ### The Stern-Gerlach Experiment: Projective Regime

Until this point, we have discussed projection operators in their mathematical sense. But
how do we physically implement a quantum measurement? The Stern-Gerlach experiment

[68] is an oft-discussed example of a projective quantum measurement (Figure 2.1). In this
experiment, a furnace is used to produce a collimated beam of silver (Ag) atoms, which have
one unpaired electron that carries spin _S_ = 1 _/_ 2. The beam is unpolarized, and comprises
an incoherent mixture of _|"i_ and _|#i_ . The initial spin state of the beam can be represented


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 10


by a density matrix


1 _/_ 2

0




__ spin =


1 _/_ 2


(2.4)


in a basis for which the eigenvectors are the __ _Z_ . We will also need to account for spatial degrees of freedom, which we will indicate by a _|"i_ and _|#i_ eigenstates of the Pauli spin matrix
state _|_ _z_  _i_ where  _z_ represents the expectation value of the vertical position of the beam. Since

the beam is initially collimated, we can write the total density matrix as


in a basis for which the eigenvectors are the __ _Z_ . We will also need to account for spatial degrees of freedom, which we will indicate by a _|"i_ and _|#i_ eigenstates of the Pauli spin matrix
state _|_ _z_  _i_ where  _z_ represents the expectation value of the vertical position of the beam. Since


__ _i_ = __ spin __ __ _z_ =


1 _/_ 2

0




1 _/_ 2


_|_ 0 _i_ _h_ 0 _|_ (2.5)


The collimated beam is passed through an inhomogeneous magnetic field **B** , which in-

teracts with the spins via the Zeeman eect:


_U_ _int_ = __ **__** **__** **B** = __ _g_ _b_ _S_ _z_ _B_ _z_ _._ (2.6)

Here, _g_ is the gyromagnetic ratio of the silver atom, __ _b_ is the Bohr magneton, and _S_ _z_ is

the spin moment of the unpaired electron, which can take values of __ 1 _/_ 2. The force in the
z-direction is given by



_@U_
_F_ _z_ = = _g_ _b_ _S_

_@z_


_@B_


_z_ 1

=
_@z_ __ 2


_@B_ _z_

(2.7)
_@z_


_@B_



_g_ _b_
2


As the ion beam travels through the inhomogeneous magnetic field, the _|"i_ and _|#i_

components are deflected in opposite directions. In eect, the presence of the magnetic field
_entangles_ the spin degree of freedom with the positional degrees of freedom (we will discuss
entanglement more in Chapter 3). The state of the system can now be represented as


As the ion beam travels through the inhomogeneous magnetic field, the _|"i_ and _|#i_


1

0




0

0





1
__ =


_|_ _z_  _i_ _h_ _z_  _|_ +


_|_ + _z_ _i_ _h_ + _z_


(2.8)


where _|_ _z_  _i_ corresponds to the position of the upward (+) and downward (-) deflected beams.

After exiting the magnetic field, the Ag atoms impinge on a detector screen, which makes


where _|_ _z_  _i_ corresponds to the position of the upward (+) and downward (-) deflected beams.


a projective measurement of the position. If the ion beams corresponding to _|"i_ and _|#i_ are
sufficiently well-separated, the screen simultaneously makes a projective measurement of the
spin degrees of freedom. Thus, we see that the positional degree of freedom acts as an


_ancilla_ : it is a macroscopically-measurable quantity that can be used to infer the state of a
quantum degree of freedom. If we were to move the screen such that it blocked the lower
beam and allowed the upper beam alone to propagate, a second Stern-Gerlach measurement
of the spin moment would show the resultant propagating beam to be fully polarized, having
been projected into the _|#i_ spin state. _X_


Suppose instead we were to start in a pure quantum state polarized along __ _X_ , such that


spin = _|"i_ _p_ + 2 _|#i_
_|_ _i_


or


1

1





1
__ spin =


(2.9)


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 11

![SchwarzThesis.pdf-22-2.png](SchwarzThesis.pdf-22-2.png)

![SchwarzThesis.pdf-22-3.png](SchwarzThesis.pdf-22-3.png)

![SchwarzThesis.pdf-22-0.png](SchwarzThesis.pdf-22-0.png)

![SchwarzThesis.pdf-22-1.png](SchwarzThesis.pdf-22-1.png)

![SchwarzThesis.pdf-22-4.png](SchwarzThesis.pdf-22-4.png)

Figure 2.1: The Stern-Gerlach experiment. A beam of unpolarized Ag atoms passes through
an inhomogeneous magnetic field, and emerges as two spatially-separated, spin-polarized
beams. The position of the atoms is recorded at a detector screen, where the position of the
atom is used to infer its spin.


__ _X_




with


= +1. At the end of the measurement, the spins will be fully polarized into


__ has now been destroyed: _Z_ = __ 1, but the coherent phase relationship between __ _X_ = 0. This is what we mean by measurement destroys coherence: by _|"i_ and _|#i_


__ _X_




= 0. This is what we mean by measurement destroys coherence: by


measuring a quantum system via a given operator, we scramble information contained in a
non-commuting observable.


### 2.1.3 ### The Stern-Gerlach Experiment: Weak Measurement Regime


So far, we have neglected the intrinsic uncertainty in the z-component of the individual
atoms in the atom beam. In fact, the atoms propagate in a Gaussian beam with standard
deviation __ . In the limit where the separation between the centers of the _|_ _z_  _i_ beams is much

larger than __ , we can safely ignore the uncertainty in _z_ (Figure 2.2b): the wavepackets are
very well-separated, and one can draw a line of discrimination that well-separates the two
spin-polarized beams. We refer to this regime as the _projective_ measurement regime, as the
measurement has eectively projected the system into two fully spin-polarized sub-ensembles.
However, if the magnetic field gradient is weak or the propagation length short (Figure 2.2a),
there is no good discrimination line; any such line of discrimination will inevitably lead to
many post-selection errors. We refer to this as a _weak_ , or _non-projective_ measurement. It is
also sometimes described as a partial measurement.

It is important to note that these post-selection errors do not mean that the measurement


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 12


![SchwarzThesis.pdf-23-3.png](SchwarzThesis.pdf-23-3.png)

![SchwarzThesis.pdf-23-4.png](SchwarzThesis.pdf-23-4.png)

![SchwarzThesis.pdf-23-0.png](SchwarzThesis.pdf-23-0.png)

![SchwarzThesis.pdf-23-5.png](SchwarzThesis.pdf-23-5.png)

![SchwarzThesis.pdf-23-1.png](SchwarzThesis.pdf-23-1.png)

![SchwarzThesis.pdf-23-2.png](SchwarzThesis.pdf-23-2.png)

Figure 2.2: The Stern-Gerlach experiment in the weak- (a) and strong- (b) measurement
regimes. Here, we show the measurement profile of an un-polarized input beam (blue)

as a line, and the expected profile of a polarized _|"i_ (green) and _|#i_ (purple) state as a
shaded object. By varying the propagation length, the separation between the spin-polarized
beams can be varied continuously. In the strong-measurement regime (b), the ensembles are
well-separated, and we can eectively post-select a spin-polarized ensemble. In the weakmeasurement regime (a), the separation is on the order of the intrinsic beam width; a
post-selected ensemble will not be fully projected into either spin polarization.

is _bad_ : a bad measurement would be one in which a quantum observer, one with access to all
of the fluctuations in the system, would have been able to do an accurate post-selection, but
our measurement apparatus is too noisy to accomplish the same feat. In a _weak_ measurement,
there is no quantum or classical observer that is able to do an accurate post-selection, because
there is insufficient quantum information to do so. This means that the system has been
perturbed, but not projected, by the measurement. In a bad measurement, the system has
been projected by the measurement, but the experimenter is not able to determine into
which state it has been projected.

To understand weak measurement in the context of the Stern-Gerlach experiment, sup-

pose we were to to cut a small hole in the detector screen at position _z_ = 0, such that the
fraction of the beam that is undeflected is allowed to propagate. A second Stern-Gerlach


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 13


__  _Z_




device operating in the projective regime would measure this beam to have


= 0, just


as the original beam was. This is because the Gaussian amplitude for both the _|_ _z_ _i_ beams
is equal at this point. Although the beam has passed through a measurement device, it
has not projected onto an eigenstate of the measurement. If we instead cut a small hole
at _z_ = + __ , a second projective Stern-Gerlach device will find that the propagating beam is
slightly polarized in the _|#i_ direction, but still contains significant amplitude in the _|"i_ state.


Rather than implementing a projection operator, the Stern-Gerlach device in the weak


measurement case implements an operation known as a _positive operator-valued measurement_
(POVM), which we will label ( _z_ ). POVMs are a _non-orthogonal_ set of operators that span
the Hilbert space of the measurement, but are generally made of linear combinations of the
traditional projection operators. In the particular case of the Stern-Gerlach experiment, the
POVMs are given by


( _z_ ) = _f_ ( _z,_ + _z, _ ) + _f_ ( _z,_ _z, _  ) ; (2.10a)
_#_ __ _"_


( _z_ __ _z_  ) 2


_f_ ( _z,_  _z, _ ) =



_e_
2 __


2 __ __ _z_  2 ) _._ (2.10b)


In other words, the extent to which the measurement projects onto _|"i_ or _|#i_ becomes a

continuous function of position, and the measurement in general projects into a combination
of both eigenstates of the measurement operator.


In other words, the extent to which the measurement projects onto _|"i_ or _|#i_ becomes a


The Stern-Gerlach experiment begins with an incoherent (mixed) starting state, so the


weak measurement described here will itself only allow postselection mixed states with varying proportions of the two spin polarizations. However, we could just as easily have begun our
experiment with an ensemble of atoms all in the coherent superposition state _i_ = _|"i_ _p_ + 2 _|#i_
_|_ _i_


1

1





1
or __ spin =


, which has the same net-zero spin polarization but is a pure state. In


this case, we can see that the POVM actually preserves the purity of the state, as measured
by Tr _{_ __ 2 _}_ . This is an surprising result, as we are accustomed to considering measurement
a process that decoheres a quantum superposition into a classical mixture of measurement
eigenstates. However, here we see that performing a POVM and accurately recording its
outcome _z_ allows us to precisely predict the back-action of the measurement kick on the
quantum system, thus ensuring no information about the quantum state is lost. The POVM
formalism, along with the continuous, stochastic state tracking that it implies, suggests the
need for an alternative method of conceptualizing the measurement process. Two such useful
methods, the quantum Bayesian formalism (QB) and the stochastic master equation (SME),
will be reviewed in the next sections.


Note that thus far we have considered an atom beam comprised of many individual

atoms, providing to a probability distribution in _z_ as the atoms hit the detection screen. We
also will be interested, however, in exploring the eect of the measurement on a single atom
within that ensemble. Additionally, the Stern-Gerlach experiment performs a destructive
measurement, in that once an atom hits the detector screen, no further measurements of


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 14

its state can be made. We will be interested in measurements that are both _weak_ and

_continuous_ , allowing for multiple sequential measurement of the same quantum state that
allow us to track an individual quantum trajectory.

## 2.2 ## The Quantum Bayesian Formalism

The quantum Bayesian (QB) formalism [6973] is a straightforward extension of classical
Bayesian conditional probabilities to a coherent quantum system. The QB formalism takes a
personalist view of the state vector and the density matrix: it posits that the density matrix
represents the current state of the observers knowledge about the state of the quantum
system under study, but makes no claims of objective realism.

The classical Bayes rule describes the conditional probability of event _A_ , given the oc-


currence of event _B_ :



_P_ ( _A_ ) _P_ ( _B_ _A_ )
_P_ ( _A_ _B_ ) = _|_ _._ (2.11)
_|_ _P_ ( _B_ )



_P_ ( _A_ ) _P_ ( _B_ _A_ )
_P_ ( _A_ _B_ ) = _|_
_|_ _P_ ( _B_ )


This rule states that a prior assessment of the probability of event _A_ - that is, _P_ ( _A_
) must be updated by the probability of _B_ given _A_ , normalized by the prior probability of
_B_ . Since the diagonal elements of a density matrix similarly represent the probability that
the quantum system is in the given state, we can guess a similar rule for a quantum system.
Lets specialize to a single two-level system, whose density matrix is given by


__ g _,_ g __ g _,_ e

__ e _,_ g __ e _,_ e




__ =


(2.12)


where _g_ and _e_
represent the ground and excited states of the two-level system. Lets suppose we know the measurement probability distributions _p_ ( _V_ ), where _V_ is a generalized
__
measurement outcome. In the Stern-Gerlach experiment, for example, we would replace _V_
with _z_ , and _p_ ( _V_ ) with Eq. (2.10b). We can then write an equivalent _quantum_ Bayes rule
__
for the diagonal terms:


__ g _,_ g _p_ + ( _V_ )
( __ g _,_ g _V_ ) =
_|_ _p_ + ( _V_ ) + _p_ (


__ g _,_ g _p_ + ( _V_ ) ; ( __ e _,_ e _V_ ) = __ e _,_ e _p_ __ ( _V_ )

_p_ + ( _V_ ) + _p_ __ ( _V_ ) _|_ _p_ + ( _V_ ) + _p_ __


__ _._ (2.13)

_p_ + ( _V_ ) + _p_ __ ( _V_ )


Here, we update the diagonal density matrix elements based on the measurement result,

and our prior knowledge of the probability of that result assuming that the system was
in the respective eigenstates. If the measurement being performed is nondestructive and
continuous, one can use the output of one Bayesian update step as the input to the next,
resulting in a _trajectory_ of updates due to the full measurement record **V** = _V_ 1 _, V_ 2 _, ..., V_ _N_ .
_{_ _}_
In the special case that the noise giving rise to the measurement distributions is colorless
and memoryless - the Markov approximation - one can equivalently average the measurement
record and perform an update based on the integrated measurement.


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 15

The diagonal density matrix elements are in some sense trivial to predict via probability

rules, since they represent classical probabilities of finding the system in their respective
states. The o-diagonal elements, which contain information about the phase coherence and
thus the purity of a superposition state, have a less obvious equivalent to the Bayes rule.
However, here as well we can be equally obvservationalist in our approach. The Bayes rule
for the o-diagonal elements becomes


( __ g _,_ e _V_ ) = ( __ __ e _,_ g _V_ ) = __ g _,_ e
_|_ _|_


( __ g _,_ e _V_ ) = ( __ __ e
_|_


( __ g _,_ g _V_ )( __ e _,_ e _V_ )
_|_ _|_

__ g _,_ g __ e _,_ e


_e_ __ _t_ (2.14)


where __ is a damping term which goes to zero for a perfectly efficient measurement system
and for a quantum system with infinite lifetime [69]. We will see in Section 2.4 how to handle
the eects of inefficient measurement. Eq. (2.14) states that, in the absence of additional
unitary dynamics, the o-diagonal density matrix elements can be determined simply by
updating the diagonal density matrix elements. It is also possible to include deterministic
evolution at rate _!_ into the Bayesian formalism [74], as long as we perform a Bayesian update
in timesteps __ __ 1 _/!_ . This formalism generalizes naturally to a higher-dimensional Hilbert
space according to



__ i _,_ i _p_ _i_ ( _V_ )
( __ i _,_ i _V_ ) =
_|_ _j_ _p_ _j_ ( _V_ )


( __ i _,_ j _V_ ) = __ i _,_
_|_


( __ i _,_ i _V_ )( __ j _,_ j _V_ )
_|_ _|_

__ i _,_ i __ j _,_ j


(2.15)

_e_ __ __ _ij_ _t_


where _i_ and _j_ are eigenstates of the Hamiltonian and __ _ij_ is a generalized decoherence rate
between states . Eq. (2.15) reduces to the general statement, applicable to both onand o-diagonal elements _i_ and _j_


__ i _,_ j
( __ i _,_ j _V_ ) =
_|_ _k_ _p_ _k_ ( _V_ )


_p_ _i_ ( _V_ ) _p_ _j_ ( _V_ ) _e_ __ _i_ _ij_ _t_ _._ (2.16)


We will derive a Bayesian update rule for a half-parity entangling measurement in Chapter
5, where we will see its power in understanding and interpreting a noisy measurement signal.

Everything that we have developed in this section has been perfectly empirical - we have

assumed knowledge of an arbitrary measurement distribution (conditioned on the eigenstates), and also have assumed knowledge of the starting state of the system. The physics,
of course, comes in predicting these distributions, based on a quantitative understanding of
the measurement processes being utilized, and the quantum noise that is associated with
them. In Chapter 4, we will present the dispersive measurement of a superconducting quantum bit embedded in a resonator, in order to provide a concrete example of this process.

The chief advantage of the QB approach is its mathematical and conceptual simplicity.

One must only know an estimated starting state, and an expected distribution of measurement outcomes given the eigenstates of the system, in order to update the (diagonal)


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 16

density matrix elements based on the measurement outcome. From a philosophical standpoint, however, it requires a major concession: we cede any notion that the density matrix
represents the true state of the system, or of an ensemble of identically prepared systems,
instead stipulating that it is specific to the observer, and that another observer with more or
less information might construct a dierent density matrix to which the quantum Bayesian
update can just as reasonably be applied.

## 2.3 ## The Stochastic Master Equation

The stochastic master equation is a powerful, minimal, and general formalism for understanding and interpreting the eects of the interaction between a quantum system of interest and
a fluctuating degree of freedom ( _i.e._ quantum noise). There are many resources [9, 7578]
for deriving and understanding SMEs, but here we will closely follow a wonderful introduction from Jacobs and Steck [79]. Our goal is to gain intuition for the relationship between
quantum fluctuations and measurement outcomes; for how to infer a quantum trajectory
from a continuous measurement record; and for how to account for an inefficient measurement process. Along the way, we will see that dissipation - broadly, any process that reduces
the purity of a quantum system - is intimately related to the measurement process, and we
will learn to quantify that relationship. In this section we will derive the SME completely
generally; later, we will see its connection to physical measurement processes.

We first consider the unitary evolution of the quantum state, beginning with the Schroedinger


equation:



_@_
_i_ ~


Written in dierential form and considering a short time interval, we have



=  _H_ (2.17)
_@t_ _|_ _i_ _|_ _i_


_d_ _|_ _i_ =



_i_
__


_H dt_ 


_|_ _i_ (2.18)


If we make the approximation that the system evolves slowly (the Born approximation), the
evolution of a pure state vector in the time interval is given by


_|_ _0_ _i_ = _|_ _i_ + _d_ _|_ _i_ =



_i_
1 __


_H dt_


_|_ _i_ (2.19)


A similar transformation will apply to the density matrix:


__ _0_ = __ + _d_ =


1 __


_H dt_ 


1 +


_H dt_ 



_i_
= __ __


_H, _ 


_dt ._ (2.20)


This defines the instantaneous evolution of the density matrix under a unitary Hamiltonian,
and is the Schroedinger equation for density matrices.


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 17

### 2.3.1 ### Dissipation via Fluctuation: Lindblad Operators


Eq. (2.20) completely describes the instantaneous evolution of a density matrix for which
all dynamics are described by a unitary Hamiltonian, and represents a completely positive
transformation of the form __  __  __ , where  = 1 _i_ _H dt_  . However, as noted in Section

~

_!_ _A_ _A_ _A_ __



_i_ _H dt_  . However, as noted in Section

~


2.1, we often must account for the interaction between a system of interest and a fluctuating
degree of freedom. Therefore, let us add two terms - completely generally - to our transformation:


_A_  = 1 __


_H dt_  +  _b dt_ +  _c dW_ (2.21)


Here, we have an additional deterministic evolution operator  _b_ , which we assume to be Her-

mitian, and a _stochastic_ evolution term  _c_ that grows with _dW_ , which represents a Wiener


process. A Wiener process is equivalent to a classical random walk centered at the origin.
Random walks can be represented by a normal distribution whose width scales with _p_ _t_ , such

that the probability density is given by


_P_ ( _W, t_ ) =



_e_ __ _W_ 2 _/_ 2 _t_ _._ (2.22)
2 _t_


Thus, we can consider the additional term in our evolution operator

_d_ _y_  =  _b dt_ +  _c dW_ (2.23)


to be the equivalent of a _drifting_ random walk operator where the increment _dW_ is the step
taken in time increment _dt_ . In the quantum context, the walker can be any fluctuating
quantity, such as position and momentum, electromagnetic field quadrature amplitudes, or
other zero-point fluctuating modes. Just as _P_ ( _W, t_ ) represents a Gaussian distribution, _dW_
is itself a normally-distributed random variable with a distribution width of _p_ _dt_ . The Wiener


process is a _white-noise_ process, such that _dW_ ( _t_ ) is statistically independent of _dW_ ( _t_ _0_ ) for
all _t_ _6_ = _t_ _0_ .

There are a number of useful properties of Wiener processes which we will cite here but

will not prove [80]:


_hh_ _dW_ _ii_ = 0 (2.24a)

_dW_ 2 = _dt_ (2.24b)

_hh_ _y dW_  _ii_ = _hh_ _dW_ _ii_ = 0 (2.24c)


Here, we define the _ensemble average_ _hh ii_ as the mean over all possible Wiener processes.

Eq. (2.24a) simply reflects that the random variable has zero mean; Eq. (2.24b) is a

formulation of the It o Rule that is the foundation of stochastic calculus; and Eq. (2.24c)

states that the expectation value of  _y_ is statistically independent from _hh_ _dW_ _ii_ .


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 18

With this context for the Wiener process, we substitute (2.21) into (2.20) and keep terms

only up to first-order in _dt_ (that is, we throw out terms proportional to _dW dt_ and _dt_ 2 , and
use Eq. (2.24b) to substitute _dW_ 2 = _dt_ ), and find


_c_  + __ _c_  __




_d_ = __


_H, _


_dt_ +


_b, _


_dt_ +  _c_ _c_  __ _dt_ +


_dW ,_ (2.25)


where _{_ _A, B_ _}_ is the anticommutator _AB_ + _BA_ .


We now are interested in the ensemble average of all possible Wiener processes in this





_c_  + __ _c_  __







system. Using Eq. (2.24c) to set


_dW_


= 0, we have



_i_
_d_ _hh_ __ _ii_ = __


_H,_ _hh_ __ _ii_


_dt_ +


_b,_ _hh_ __ _ii_


_dt_ +  _c_ _hh_ __ _ii_  _c_ __ _dt ._ (2.26)


Note that Eq. (2.26) represents an average over all possible realizations of a the density
matrix under the stochastic evolution process we are studying, and therefore _hh_ __ _ii_ itself is
a density matrix. Specifically, it must maintain unit trace over all realizations, such that
_d_ this condition holds for the first term. For the terms containing Tr[ _hh_ __ _ii_ ] = Tr[ _d_ _hh_ __ _ii_ ] = 0. We have defined _H_  to be a unitary operation, so we know  _b_ and  _c_ , we use the cyclic


Note that Eq. (2.26) represents an average over all possible realizations of a the density
matrix under the stochastic evolution process we are studying, and therefore _hh_ __ _ii_ itself is
a density matrix. Specifically, it must maintain unit trace over all realizations, such that
_d_ Tr[ _hh_ __ _ii_ ] = Tr[ _d_ _hh_ __ _ii_ ] = 0. We have defined _H_  to be a unitary operation, so we know


property of the trace to find


 _b_ _hh_ __ _ii_ + _hh_ __ _ii_  _b_ +  _c_ _hh_ __ _ii_  _c_ __

i


h


Tr


= Tr


2  _b_ +  _c_ __ _c_ 


_hh_ __ _ii_


= 0 _._ (2.27)


In order for Eq. (2.27) to hold for arbitrary density matrix, this provides a restriction on  _b_


and  _c_


_c_  __ _c_ 
 _b_ = _._ (2.28)
__ 2


_c_  __ _c_ 
 _b_ =
__ 2


We can use this relationship to define [81] the _Lindblad superoperator_ _D_ [ _c_ ] __



1
[ _c_ ] __ _c_  _c_  __
_D_ __ __ 2


_c_  __ _c_  + __ _c_  __ _c_ 


(2.29)


which we can use to rewrite Eq. (2.26):


_d_ _hh_ __ _ii_ =



_i_
__


_H,_  _hh_ __ _ii_


+ _D_ [ _c_ ] _hh_ __ _ii_


_dt ._ (2.30)


This is in fact the unconditioned master equation for ensemble evolution in the presence


of a noisy process. Note that the evolution of the ensemble of fluctuation realizations is
purely deterministic (proportional to _dt_ ), and that while we have required that Tr[ __ ] =

2 _hh_ _ii_

1, we have made no such requirement of Tr __ . In fact, a Lindblad term is almost


_hh_ __ _ii_ 2




. In fact, a Lindblad term is almost


always associated with a reduction in the square trace of the ensemble density matrix. This
represents a reduction in the purity of the density matrix, as it becomes an average over
a noisy ensemble. Lindblad superoperators are often referred to as _Lindblad dissipators_ for


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 19

this reason. Also note that one can trivially multiply  _c_ by a constant to increase or decrease


the rate at which the dissipation occurs; we will examine the eects of the measurement rate
in Section 2.4.


For example, suppose we neglect the unitary dynamics (i.e. set _H_  = 0) and apply a


Lindblad operator with  _c_ =  __ _Z_

p


__ __ _/_ 2. Dropping the ensemble average notation, we then


see that the density matrix evolution is given by


__
h __ __


2 __ __  _Z_ __ __  _Z_ __ __ 4 __


( __ _Z_ ) 2 __ + __ ( __ _Z_ ) 2

_dt_  i


( __ _Z_ ) 2 __ + __ ( __ _Z_ ) 2

i


_d_ =



__ __
=


__  _Z_ __ __  _Z_ __ __


_dt_

(2.31)


= __ __


__ g _,_ e
__


_dt_


__ e _,_
__


Integrating, we find


__ g _,_ g __ g _,_ e _e_ __ __ __

__ e _,_ g _e_ __ __ __ _t_ __ e _,_ e




__ ( _t_ ) =


__ e _,_ g _e_ __ __ __ _t_ __ e _,_


(2.32)


The diagonal density matrix elements remain constant, but the o-diagonal terms decay to
zero. If we were to begin in a pure x-polarized state, it would decay under the back-action of
a  __ _Z_ dissipation into an incoherent mixture of _Z_ _|_ _g_ _i_ and _|_ _e_ _i_ , with Tr[ __ 2 ( _t_ _! 1_ )] = 1 _/_ 2. Thus,


a Lindblad operator with  _c_ _/_  __ _Z_ represents dephasing.


### 2.3.2 ### Measurement in the SME formalism

We now return to the un-averaged form of the master equation, which in light of Eq. (2.28)
we can write as:


_c_  + __ _c_  __





_i_
_d_ = __


_H, _


_dt_ + _D_ [ _c_ ] _dt_ +


_dW ._ (2.33)


The first two terms, as we have determined, are trace-preserving; however, because  _c_ is


still arbitrary, the final term does not in general preserve the trace. In order to allow  _c_ to

remain an arbitrary operator, we will renormalize __ by the term





_c_  + __ _c_  __




_c_  +  _c_ __

] __ : 


_c_  +  _c_ __




__ Tr


_dW_


= __ Tr


_dW_ = __


_dW ._ (2.34)

(2.35)


We define the measurement superoperator _H_ [ _c_ ] __ :


_c_  +  _c_ __




_H_ [ _c_ ] __ __ _c_  + __ _c_  __ __


and rewrite the nonlinear master equation as


_d_ = __


_H, _


_dt_ + _D_ [ _c_ ] _dt_ + _H_ [ _c_ ] _dW_ (2.36)


In the case  _c_ is a Hermitian operator (as is required for any observable), Eq. (2.36) is the

stochastic master equation (SME) describing the evolution of the density matrix under a


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 20


single trajectory of randomly-sampled steps _dW_
, representing fluctuations in the expectation value of the observable  _c_ . More intuitively, _H_ [ _c_ ] __ represents the stochastic back-action


of the measurement on the state of the quantum system. Critically, this back-action is proportional to _dW_ , so if we know the measurement operator that is being applied and have
a means to collect information about the quantum fluctuations, we can update our density
matrix to follow the state evolution, thus eectively undoing the dissipation caused by the
_D_ [ _c_ ] __ term.


Note that though we are using the language of density matrices here, the SME formalism


derived here does _not_ represent an ensemble of realizations; rather, it allows us to derive the
stochastic evolution of a single instantiation of the quantum system of interest, and a single
noise record. In principle, if we have full access to the measurement record, it is possible to
continually update the density matrix in a way that preserves not just trace-normalization,
but also the _purity_ of the quantum state, thus turning a dissipative process into a coherent
process.

## 2.4 ## Measurement Rate and Inefficient Measurements

In any physically realizable system, we cannot hope to have a perfect collection of the
measurement record. Whether due to photon scattering, resistive losses, or external noise
sources, the measurement record we collect with macroscopic, room-temperature, classical
equipment will inevitably be corrupted to some degree, even using the most state-of-the-art
detectors. We therefore must consider the eect of measurement efficiency on our ability to
accurately track the evolution of the density matrix.

First, we would like to draw a more physical connection between the distribution of

measurement outcomes and the strength of the measurement back-action. To do so, we will
return to a more physically-motivated derivation of the SME formalism. Recall that the
partial measurement performed by a weak Stern-Gerlach apparatus can be written per Eq.
(2.10b) as a sum of Gaussian-weighted POVM partial projectors. For a general two-level
system in which we measure  __ _Z_ by tracking a variable _z_ , we can write


2





1
( _z_ ) =


_|_ _g_ _i_ _h_ _g_ _|_ _e_ __ 1 2 (



1
_|_ _g_ _i_ _h_ _g_ _|_ _e_ __ 2


_z_ __ __ _zg_ )


_z_ __ _zg_



1
+ _|_ _e_ _i_ _h_ _e_ _|_ _e_ __ 2



1 2 ( _z_ __ __ _ze_



_ze_

__


(2.37)


where _N_ is a normalization and _z_ _i_ is the centroid of the Gaussian distribution for state _|_ _i_ _i_ .
Since we have restricted our measurement to the Markovian approximation, we expect the
variance of the distributions to decrease as 1 _/t_ . Let us therefore define __ 2 = 1 _/_ 2 _t_ , for
reasons that will soon become apparent. We then have


_|_ _g_ _i_ _h_ _g_ _|_ _e_ __  _t_ ( _z_ __ _z_ _g_ ) 2 + _|_ _e_ _i_ _h_ _e_ _|_ _e_ __  _t_ ( _z_ __ _z_ _e_ ) 2





1
( _z_ ) =


(2.38)


The probability of measurement outcome _z_ is given by


_P_ ( _z_ ) = Tr


( _z_ ) __  __ ( _z_


= _P_ ( _g_ ) _e_ __ 2 _t_ ( _z_ __ _z_ _g_ ) 2 + _P_ ( _e_ ) _e_ __ 2 _t_ ( _z_ __ _z_ _g_ ) 2 (2.39)


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 21


In the limit where  _t_ 1 _/_  such that __ _z_ _g_ _z_ _e_ , we can approximate _P_ ( _z_ ) as a single
__ _Z_ _|_ __ _|_
Gaussian, centered at _z_ = __  :


__  _Z_





1
_P_ ( _z_ ) __



_e_ __ 2 _t_ ( _z_ __ __  _Z_ )

_h_ _i_
_N_


(2.40)

(2.41)


Alternatively, we can write _z_ as a stochastic variable given by


__  _Z_




_z_ =


 _W_

4


where _W_ as usual is a zero-mean Wiener variable. Substitution into Eq. (2.40) gives _P_ ( _z_ )
as a normally distributed stochastic variable with variance  _t_ , as desired. Thus we can see
that  defines a measurement strength or measurement rate. Sending  _W,_  _t_ _!_ _dW , dt_
and generalizing back to an arbitrary measurement operator, we can define the measurement
record according to a series of increments



_dW_
_dz_ = _h_ _c_  _i_ _dt_ + _p_ 4



_dW_
_dz_ = _h_ _c_  _i_ _dt_ + _p_


(2.42)


Thus, we see that the measurement output _z_ evolves with a deterministic component, which
is proportional to the true expectation value of the measurement operator, and a stochastic
component, whose magnitude is scaled by . In the limit where  is very small, the measurement record is dominated by noise and the expectation value is washed out by fluctuations,
such that the measurement occurs slowly; when  is large, the measurement quickly resolves
to the true eigenvalue of the measured operator. By following a procedure similar to Section
2.3, we can derive the master equation with a measurement strength built in organically:


_d_ =  _D_ [ _c_ ] _dt_ +


 _H_ [ _c_ ] _dW ._ (2.43)


The details of this derivation can be found in Ref. [79]; however, note that in that text one
must make the substitution  = 2 _k_ . Thus, we see that the measurement rate enters linearly
into the dissipation term, and as a square root into the measurement update operator. In
general,  is set by the signal-to-noise ratio of the ancilla that is used to measure the system:
the better separated the histograms become in unit time, the stronger the measurement
back-action.

Now that we have understood how to translate from a quantum noise distribution to the

SME formalism, we can consider the eects of inefficient collection. This derivation is again
adapted from Ref. [79]. Suppose the system now has two observers, Alice and Eve (the
latter of whom represents the environment). Alice measures observable  _a_ at rate  1 , and

Eve measures the same observable at rate  2 . Alices knowledge of the state of the system
is denoted by __ 1 , and Eves by __ 2 . From the perspective of Alice, the measurement made
by Eve is lost information, so  2 enters into her master equation as a pure dissipation term.
The opposite is true for Eve. Thus, the SMEs for the two systems are given by


_d_ 1 =  1 _D_ [ _a_ ] __ 1 +  2 _D_ [ _a_ ] __ 1 +

_d_ 2 =  1 _D_ [ _a_ ] __ 2 +  2 _D_ [ _a_ ] __ 2 +


 1 [ _a_ ] __ 1 (2.44)
_H_

 2 [ _a_ ] __ 2 (2.45)
_H_


 1 [ _a_ ] __ 1 (2.44)
_H_


-----


_CHAPTER 2. DISSIPATION AND CONTINUOUS MEASUREMENT_ 22

The measurement signals at the two ports are given by



_dW_ 1
_dy_ 1 = _h_ _a_  _i_ 1 _dt_ + _p_ 4

_dW_ 2
_dy_ 2 = _h_ _a_  _i_ 2 _dt_ + _p_ 4


(2.46)

(2.47)


where the notation _h_ _a_  _i_ _i_ denotes the expectation value from the standpoint of __ _i_ , and because


the measurement/dissipation rates are dierent on the two channels we do not in general
expect _h_ _a_  _i_ 1 = _h_ _a_  _i_ 2 . Notice also that _dW_ 1 and _dW_ 2 are independent noise sources - we expect


the fluctuations observed by Alice and Eve to be uncorrelated.


Now let  =  1 +  2 and __ =  1 _/_ . We can then rewrite Alices SME according to


_d_ 1 =  _D_ [ _a_ ] __ 1 +


 __ _H_ [ _a_ ] __


(2.48)



_dW_
_dy_ 1 = _h_ _a_  _i_ 1 _dt_ + _p_ 4 __


The dissipation rate is governed, as we expect, by the total leakage rate of information
from the system; however, the back-action and the eective measurement rate are scaled
by a factor of __ . Since _<_ 1 by definition, this means that if the system begins in an
initial superposition state, the purity of __ 1 will in general decrease under the influence of the
measurement. For example, if we measure  __ _Z_ at rate  with efficiency __ , the o-diagonal

elements __ e _,_ g _, _ g _,_ e will decay at an additional rate (1 __ __ ), leading to an overall dephasing
eect that is mitigated, but not completely undone, by the state update protocol. Only
when the quantum efficiency is unity and all fluctuations captured by the observer can
the square-trace purity of the density matrix after measurement match the purity before
measurement.

## 2.5 ## Summary of Measurement and Dissipation

In this chapter, we have developed a sophisticated understanding of quantum measurements,
dissipation, and the connections between the two. In Section 2.1, we saw the dierence
between strong (fully projective) and weak (partially projective) measurement, and introduced the POVM formalism that describes a partial measurement. In Section 2.2, the

quantum Bayesian formalism was developed, and we saw its strength as a mathematicallystraightforward, fully empirical approach to continuous measurement. In Section 2.3, we derived a more mathematically rigorous approach to continuous measurement via the stochastic
master equation, which captures both the dissipative eects of measurement and the ability
to undo that dissipation by performing a state update conditioned on the measurement
outcome. Finally, in Section 2.4 we explored the connection between the physical measurement distributions and the measurement rate, which allowed us to understand the eects of
inefficient measurement on the quantum state update. These concepts will be critical for
understanding the experiments and developments presented throughout this dissertation.


-----


23

# Chapter 3

 Entanglement: A Primer

If two separated bodies, about which, individually, we have maximal
knowledge, come into a situation in which they influence one
another and then again separate themselves, then there regularly
arises that which I just called _entanglement [Verschr_ _ankung]_ of our

knowledge of the two bodies. At the outset, the joint catalogue of
expectations consists of a logical sum of the individual catalogues;
during the process the joint catalogue develops necessarily according
to the known law... Our knowledge remains maximal, but at the
end, if the bodies have again separated themselves, that knowledge
does not again decompose into a logical sum of knowledge of the
individual bodies.

Erwin Schr odinger, _Die gegenw_ _artige Situation in der_

_Quantenmechanik_ , 1935

Entanglement, a special class of quantum superposition, is perhaps the strangest and

most defining aspect of quantum mechanics. Strange, because the idea of an action on

one quantum system instantaneously aecting a second, isolated system runs counter to all
classical intuition; most defining, because the ability to generate entanglement allows us to
directly test predictions of quantum mechanics that are in conflict with concepts of locality.
Since generating and characterizing entanglement will be at the heart of this dissertation,
we present here a brief summary of entanglement, specifically: what it is and is not; how it
is generated; and how it is quantified. We will pay special attention to measures of _bipartite_
entanglement, or entanglement between two quantum objects. Our goal here is not to make
a comprehensive review of the history of entanglement, but rather to provide context and
background for the remainder of the dissertation.


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 24

## 3.1 ## Introduction to Entanglement

Suppose a linearly-polarized photon of frequency 2 _!_ is spontaneously converted into two
photons of frequency _!_ . Conservation of angular momentum require that the photons are
comprised of one horizontally (H-) polarized and one vertically (V-) polarized photon. However, because they are indistinguishable photons, the photons (labeled _A_ and _B_ ) are in fact
converted into a superposition state given by



_H_ _A_ _V_ _B_ + _V_ _A_ _H_ _B_
= _|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_
_|_ _i_ _p_ 2


(3.1)


This process, known as parametric down-conversion, is precisely the process used to produce
some of the first experimental entangled pairs to convincingly violate Bells inequality [82
84].

Let us recall the basic physics of such entangled Bell pairs. If we create many such


entangled pairs, but only interrogate the state of photon _A_ , we will find that it has a 50%
chance of being in state _|_ _H_ _i_ and 50% chance of being in state _|_ _V_ _i_ , but we cannot predict
into which state it is projected for each photon. This is the equivalent of reaching into
a bag of blue and red balls and choosing one at random - a perfectly classical probability
problem. If we were to measure the system along a perpendicular axis say, along the linear
combination **** **__** = ( **x** **** + **** **y** ) _/_ _p_ 2 we would similarly find the expectation value to be zero. No

coherent information is contained along any single-qubit measurement axis. The same holds
for photon _B_ . It is only by examining the two photon states _together_ that we see that the
state of the system is in fact highly correlated: each time system _A_ is found to be in state
_|_ _V_ _i_ , system _B_ will be found in state _|_ _H_ _i_ (and vice versa). In addition, there are also perfect
correlations for simultaneous measurements along **** **__** : this state contains higher correlations

than a pair of blue and red balls that are arbitrarily given to _A_ and _B_ .

These correlations in theory exist even if the photons are space-like separated and mea-

sured in an interval brief enough that the event cones do not intersect, such that there is
insufficient time for one system to signal to the other, at sub-light speeds, what the outcome of its measurement was. Entanglement is thus considered to violate local realism and
classical notions of causality [8587]. Although there are a number of challenging experimental loopholes that must be closed in order definitively demonstrate nonlocal correlations
in excess of what is classically possible, several recent experiments report to have done just
that [8890].

The high levels of correlation inherent in entangled states make them attractive for a

number of purposes. Entanglement has inspired the concept of a universal quantum information processor that could efficiently factor large numbers [91] and perform efficient
searches [92]. Such a processor must generate entanglement across an array of hundreds,
or perhaps thousands, of individually addressable quantum systems. In addition, quantum
cryptography protocols rely on the distribution and correlated measurement of entangled
pairs across a secure network [9395]. Recently, there has been growing interest in developing specialty quantum processors that, although not capable of universal computation, are


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 25

nevertheless able to surpass classical devices in the simulation of high-dimensional problems
in chemistry and physics [9699]; these processors again harness the power of entanglement
to handle matrices that stretch the capabilities of supercomputers. More fundamentally,
entanglement itself is a subject of intrinsic interest - putting aside any technological applications of entanglement, physicists are interested in generating, manipulating, and studying
entangled states of matter.

## 3.2 ## Defining Entanglement

Given its importance to the enterprise of quantum mechanics, entanglement is surprisingly
difficult to define. The clearest definition comes as a negative - that is, we define entanglement by defining what it is _not_ . For pure states, the definition is fairly straightforward. For
_N_ quantum systems, each spanning a Hilbert space _i_ 1 _,_ 2 _, ...,_ _N_ , a pure entangled
_H_ _2 {H_ _H_ _H_ _}_
state is any state which _cannot_ be written as a separable product state

= 1 2 _..._ _N_ _._ (3.2)
_|_ _i_ _|_ _i |_ _i _ _|_ _i_

In other words, an entangled state is one in which quantum information exists within interqubit correlations, rather than in single-qubit states. An entangled state is therefore a

superposition of multi-qubit, correlated states.


To specialize to a bipartite (subspaces _H_ _A_ and _H_ _B_ ), two-level system with eigenstates


_|_ we prepare both systems in an _gg_ _i_ _,_ _|_ _ge_ _i_ _,_ _|_ _eg_ _i_ _,_ and _|_ _ee_ _i_ , we can examine two exemplar states for an illustration. Suppose _X_ -polarized state, = _|_ _g_ _i_ _p_ + 2 _|_ _e_ _i_ . Then the full quantum state
_|_ _i_


is given by



_|_ _i_ . Then the full quantum state

2



_gg_ + _ge_ + _eg_ + _ee_
= _|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_
_|_ _i_ 2



_g_ + _e_
= _|_ _i_ _|_ _i_
_p_ 2



_|_ _g_ _i_ + _|_ _e_ _i_
__ _p_ 2


(3.3)


While this is a highly _coherent_ quantum state with a high degree of quantum super-

position, it is not an _entangled_ state: the fact that we can perform the direct product
decomposition on the right indicates that the systems are in a separable state. If we instead
consider the singlet state



_ge_ _eg_
= _|_ _i |_ _i_
_|_ _i_ _p_ 2


(3.4)


we can immediately see that there is no decomposition in which we can write Eq. (3.4)
as a product of states _A_ _B_ . Indeed, the singlet state is a maximally-entangled Bell
_|_ _i |_ _i_
state. Other often-referenced entangled states in three-particle systems include variants of
the Greenberger-Horne-Zeilinger (GHZ) state,



_ggg_ + _eee_
GHZ = _|_ _i_ _|_ _i_
_|_ _i_ _p_ 2


(3.5)


and the W-states,



_gge_ + _geg_ + _egg_
_W_ = _|_ _i_ _|_ _i_ _|_
_|_ _i_ _p_ 3


(3.6)


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 26

These states generalize in the obvious way to many-qubit systems.

What about quantum systems that are not in a pure state, but rather must be represented

as a statistical mixture of pure states? For these, we can write a similar rule: the density
matrix represents an entangled state if there is _no_ density matrix decomposition such that


__ =


_g_ _i_ __



_i_ 1 __ _i_

__



_i_ 2 _..._ __

__ __


(3.7)


where _g_ _i_ are real-valued degeneracy indices. The density matrix definition allows us to define
entanglement even for partially mixed states, which will be critical for studying entanglement
in experimental systems, where we often generate an ensemble of identically-prepared states
and reconstruct the density matrix representing their average.

## 3.3 ## Useful Measures of Entanglement

We now have a definition for entanglement; however, verifying that a particular state meets
the definition can be a complicated task. When studying entanglement, however, it is critical
to be able to quantify the degree of entanglement. There are a number of useful entanglement
measures that one can use for this purpose. Here we present several such measures, and
briefly discuss the advantages, disadvantages, and implications of each. Again, this list is
representative of measures we will use or reference in this dissertation; Refs. [87, 100, 101]
contain a more comprehensive list.

### 3.3.1 ### Von Neumann entanglement entropy

In some senses the entanglement entropy is the essential measurement of the amount of
entanglement in a bipartite system. It measures how much information is lost if the system
is divided into two subspaces _H_ _A_ and _H_ _B_ , and subspace _B_ is traced over (averaged out,
from the perspective of subspace _A_ ). For an unentangled system made up of product states,
tracing over the degrees of freedom in _B_ has no eect on _A_ , and no information is lost from
the perspective of . For maximal entanglement between the two subspaces, tracing over
_H_ _A_
_B_ takes _A_ into a fully mixed state, and all phase coherence is lost.

Quantitatively, the entanglement entropy of subspace _A_ is given by


_S_ ( __ _A_ ) = __ Tr _{_ __ _A_ log 2 __ _A_ _}_ (3.8)

__ _A_ = Tr _B_ _{_ __ _}_

where _S_ ( __ ) is the von Neumann entanglement entropy and Tr _B_
is the partial trace over subspace _B_ . _S_ ( __ ) is zero for a density matrix representing a pure state, because there is only
_H_
one configuration in which the system can exist. Nonzero entanglement entropy indicates
that the partial trace has caused mixing - an indication that information was contained in
multi-qubit correlations, and therefore that entanglement exists. Of course, nonzero von


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 27

Neumann entanglement entropy indicates nonseparability only if acting on a pure initial
state in _A_ _B_ , because a mixed state intrinsically has nonzero entanglement entropy
_H_ _H_
regardless of whether or not the state is in fact separable. In addition, weve arbitrarily
chosen the subdivision of spaces, while a general multi-qubit system will have many possible subdivisions. Nonzero entanglement entropy therefore does not confirm or reject the
hypothesis that the system as a whole is in a non-separable state.

### 3.3.2 ### Entanglement of formation

The entanglement of formation is designed to extend the entanglement entropy to better
capture the entanglement in a mixed state. It represents the minimum total entanglement
entropy according to the following:


_E_ ( __ ) = inf

_g_ _k_ _,_ _|_ __ _k_ _i_


_p_ _k_ _S_ [( __ _A_ ) _k_ ] (3.9)


__ =


_g_ _k_ __ _k_ __ _k_ (3.10)
_|_ _i_ _h_ _|_


Here, the summed term in Eq. (3.9) represents the weighted entanglement entropy of pure
states in the non-unique decomposition (Eq. (3.10)) of the density matrix __ . The infimum
represents the greatest lower bound of that entropy across all possible decompositions of __
into a weighted sum of pure states [101, 102]. If there is no possible decomposition of the
density matrix such that the entropy of entanglement is zero, then subspace _H_ _A_ is entangled
with subspace _B_ .
_H_

In order to see the dierence between entanglement entropy and the entanglement of


Here, the summed term in Eq. (3.9) represents the weighted entanglement entropy of pure
states in the non-unique decomposition (Eq. (3.10)) of the density matrix __ . The infimum
represents the greatest lower bound of that entropy across all possible decompositions of __
into a weighted sum of pure states [101, 102]. If there is no possible decomposition of the
density matrix such that the entropy of entanglement is zero, then subspace _H_ _A_ is entangled
with subspace _B_ .
_H_


formation, consider the density matrix spanning two two-level systems, given by



1
__ =


(3.11)


This is obviously a highly mixed, completely separable state. The von Neumann entanglement entropy of this density matrix, however, is _S_ = 2 ln 2, which is manifestly nonzero.
However, we can make the decomposition



1
__ =



1 1

_gg_ _gg_ +
4 _|_ _i_ _h_ _|_ 4



1 1

_ge_ _ge_ +
4 _|_ _i_ _h_ _|_ 4



1 1

_eg_ _eg_ +
4 _|_ _i_ _h_ _|_ 4



_gg_ _gg_ (3.12)
4 _|_ _i_ _h_ _|_


such that __ represents an equally weighted sum of pure separable states. We immediately
see that _E_ ( __ ) = 0 in this case, and therefore there is no entanglement according to this
measure. This demonstrates why _E_ ( __ ) may be a more informative measure of entanglement
in mixed density matrices.


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 28

The advantage of the entanglement of formation is that it can be applied to a system

of arbitrary size. However, evaluating it generally requires doing a full tomographic reconstruction of the density matrix, which can be experimentally prohibitive. Therefore, it is not
often practical to calculate the entanglement of formation for a multiqubit epxeriment.

### 3.3.3 ### Entanglement witnesses


Entanglement witnesses are a class of useful measurements _W_  which take on a negative value


(Tr _{_ __ _W_  _}_ _<_ 0) if and only if __ is an entangled state. Entanglement witnesses are generally


linear combinations of correlation measurements between _H_ _A_ and _H_ _B_ , such that the witness
is evaluated using joint probability distributions within the quantum state. Witnesses are
extremely useful in that they are observables, and can therefore be constructed without prior
knowledge of the quantum state; however, they are not in general universal measures - for
a given witness, there may be an entangled state for which Tr _{_ __ _W_  _} _ 0. Entanglement


witnesses can therefore be used to confirm entanglement, but not to rule it out [101]. A
useful method to optimize entanglement witnesses is provided in Ref. [103].


### 3.3.4 ### CHSH measurement

The CHSH inequality, originally derived by Clauser, Horne, Shimony and Holt [104, 105] as
a generalization of the Bell inequality experiment [106] is perhaps the most famous of all
bipartite entanglement witnesses. The Bell inequality showed for the first time that one could
design an experiment to directly test the hotly debated question of whether the presence of a
local hidden variable, shared between two distant quantum systems, could suffice to restore
determinism to quantum mechanics. The violation of a Bell-type inequality is a direct

indication of stronger correlations than are possible in a classically deterministic system; if
the violation were to occur in a _loophole-free_ manner, this would provide confirmation of
quantum non-locality. Several recent landmark experiments [8890] claim to have done just
that, although the completeness of these experiments is still the subject of some scrutiny.

A Bell witness is constructed by preparing many copies of a test state spanning two-level


Hilbert spaces _H_ _A_ and _H_ _B_ that are separately addressable and measurable. For each copy,
a random decision is made to measure the two systems on one of two axes **** **n** _A_ **n** **** _A,_ 1 _,_ **** **n** _A,_ 2
_2 {_ _}_


**n** **** _B_ **n** **** _B,_ 1 _,_ **** **n** _B,_ 2 . Here, the unit-length measurement axis defines a measurement operator
_2 {_ _}_ _X_ _Y_ _Z_


 _i,j_ = **** **n** _i,j_ **** __ _i_ , where **** __ _i_ __  _i_ _X_
_M_ **__** __


_i_ _X_ **x** **** +  __ _i_ _Y_


_i_ _Y_ **y** **** +  __ _i_ _Z_


_i_ _Z_ **** **z** . One then constructs the Bell witness,


_B_ =


 
_A,_ 1 _B,_ 1
_M_ _M_


 
_A,_ 1 _B,_ 2
_M_ _M_


 
_A,_ 2 _B,_
_M_ _M_


 
_A,_ 2 _B,_
_M_ _M_


(3.13)


It can be shown that no system which is classical or respects local realism can produce
measures _|B| _ 2; however, an entangled state can produce up to _|B| _ 2 _p_ 2 due to quantum


2 due to quantum


correlations. The equality holds when the system is in a pure entangled state, the local
measurement axes are perpendicular ( **n** **** _i,_ 1 **__** **** **n** _i,_ 2 = 0), and the measurement axes are rotated


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 29

between the two systems by __ = _/_ 4. Thus, a CHSH outcome with _B_ _>_ 2 indicates that the
system under study is indeed entangled.

A chief advantage of the CHSH approach is that it involves a set of direct measurements

of the quantum system. Unlike other measures we will see later in this section, one need
not infer the full density matrix of the quantum system in order to show CHSH inequality
violation using a Bell witness. However, a CHSH inequality violation is a more stringent
requirement than other entanglement measures. Entanglement is a necessary but insufficient
condition for violating the CHSH inequality; or, violating local realism is more difficult than
proving entanglement.

### 3.3.5 ### Tomographic methods

There are a number of useful measures of entanglement that require the reconstruction of
the full density matrix. At first glance, these methods might seem to be redundant - after
all, once one knows the full quantum state of a system, it would seem trivial to declare
whether or not that state is entangled. However, when we consider a partially mixed density
matrix that perhaps resembles, but is not perfectly identical to, a known entangled state, it
is useful to be able to quantitatively analyze the degree of entanglement within that system
and compare it to the entanglement in other mixed states.


The concurrence _C_ , first derived by Wootters [107], is a oft-cited measure of entanglement

in two-qubit systems. Concurrence is a monotone of two-qubit entanglement: it ranges from
zero, for a state that cannot be distinguished from a classical mixture, to unity, for a pure
entangled state. As with the entanglement of formation, any nonzero concurrence is evidence
of a nonseparable density matrix. Concurrence is generated by first reconstructing the full
density matrix via tomographic methods (which will be discussed in greater detail in the
experimental chapters to follow). We then take the ranked eigenvalues __ 1 _, ..._ 4 , in increasing
order, of the matrix __ __  , where  __ is the time-reversed density matrix 1 generated by

__  =  __ _Y Y_ __ __ __  _Y Y_ (3.14)


and __ _ij_ represents the joint Pauli operator  __ _i_


_A_ _i_ __ 

__


_B_ . The concurrence is then given by


_C_ = max


0


__ 4
__


__ 3
__


__ 2
__


__


(3.15)


This formula, while exact, is rather opaque. To provide a more intuitive understanding


of concurrence, we note that there are two entangled subspaces of a two-qubit system: the
odd-parity subspace, spanned by _|_ _ge_ _i_ and _|_ _eg_ _i_ , and the even-parity subspace, spanned by

1 As Sakurai shows on pp. 277-280 of Ref. [108], time-reversed equivalently means spin-flipped. As

noted by Wootters in [109], the spin-flip operation takes a density matrix representing a product state into
an orthogonal state, such that __ __  goes to zero. A pure entangled state, however, is invariant under this

operation (up to a global phase). This gives some intuition for the utility of the product __ __  in quantifying

entanglement.


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 30

_|_ _gg_ _i_ and _|_ _ee_ _i_ . In the special case that we know into which subspace we expect the system
to fall, we can use a more transparent approximation for the concurrence [110]. Writing the
density matrix as


__ =


__ ij _,_ kl _ij_ _kl_ _,_ (3.16)
_|_ _i_ _h_ _|_


_ij,kl_ =g,e


we approximate the concurrence as:


_C_ = 2 max

_C_ = 2 max


0 _,_ __ ge _,_ eg _p_ __ gg _,_ gg __ ee _,_ ee
_|_ _| _

0 _,_ __ gg _,_ ee _p_ __ ge _,_ ge __ eg _,_ eg
_|_ _| _


_C_ = 2 max


(Odd parity) (3.17)

(Even parity) (3.18)


These formulae are most valid when the o-diagonal elements outside the target subspace
are all negligible: that is, when __ ge _,_ eg is the only significant o-diagonal [Eq. (3.17)] or when
__ gg _,_ ee is the only significant o-diagonal [Eq. (3.18)].

Now the meaning of the concurrence becomes clear: it is in essence the balance between

the amplitude of the coherent o-diagonal element within the desired subspace on the one
hand, and the residual population in the subspace of opposite parity on the other. These
formulae are valid when the system under study is well-projected into either the even- or
the odd-parity subspace, such that the o-diagonal elements not included in the concurrence
calculation become negligible.

Concurrence is extremely useful as a quantitative measure of entanglement in a bipartite

system, and we will use it extensively in this dissertation (Chapters 5 and 6 in particular).
The drawback of concurrence, however, is that it does not provide information about _which_
entangled state is generated, given that Eq. (3.17)-(3.18) rely only on the magnitude of the
o-diagonal element and not on its phase. For applications in which we are interested not
in generating entanglement _per se_ but in generating a specific entangled state, concurrence
may not be a useful measure.

For experiments in which we require the generation of a specific entangled state, the

fidelity _F_ becomes the most natural measure. Here, we simply take the projection of the
density matrix onto the pure entangled state of choice [111]:

( __ ) = __ _._ (3.19)
_F_ _|_ _i_ _h_ _|_ _|_ _i_


In the case that the density matrix represents a pure state _|_ _i_ _h_ _|_ , state vector normalization


gives _F_ max = 1. One can also show that a fully mixed state in the subspace of interest
will give _F_ mixed = 0 _._ 5. Thus if 0 _._ 5 _<_ _F _ 1, we have both confirmed the existence of


entanglement and further shown that we have produced, with varying quality, the entangled
state of our choice. We will us fidelity in Chapter 7, where we will be interested in preparing
specific entangled states.


Fidelity can also be a useful measure if we are comparing our density matrix not to a

pure state, but to another mixed or pure density matrix. In this case, letting __ _t_ represent
the target density matrix, the generalized fidelity is given by [111]


( __ _t_ _, _ ) =
_F_



2
( _p_ __ _t_ __ _p_ __ _t_ ) 1 _/_ 2

oi


Tr


(3.20)


-----


_CHAPTER 3. ENTANGLEMENT: A PRIMER_ 31


One can show that this reduces to Eq. (3.19) in the special case that __ _t_ represents a pure
state. We should also note that some papers use _F_ _0_ = _p_ _F_ to represent fidelity, so one should


be careful to note which convention is in use when assessing and comparing claims.


_F_ to represent fidelity, so one should


-----


32

# Chapter 4

 The Superconducting cQED Architecture

The theory of quantum electrodynamics describes Nature as absurd
from the point of view of common sense. And it agrees fully with
experiment. So I hope you accept Nature as She is absurd.

Richard Feynman, _QED: The Strange Theory of Light and Matter_ ,

1985

In this chapter, we review the experimental building blocks of the superconducting qubit

architecture. Specifically, we discuss the quantum circuits used to generate an approximate
two-level system with lifetimes sufficient to do coherent quantum operations [20, 35, 36,
39, 113117]; the light-matter interactions used to control, couple, and read out the state
of the qubits [23, 75, 118, 119]; and the amplifiers used to transport the quantum-limited
signals used to make measurements from their 30 mK base temperature through to room
temperature electronics while adding minimal noise.

Superconducting quantum information is a rapidly developing experimental field, and

it is beyond the scope of this dissertation to provide a comprehensive review of the field.
Instead, we will focus here on the techniques and circuits used to implement the experiments
in this dissertation: the transmon qubit, coupled dispersively to a linear resonator, and read
out using a Josephson parametric amplifier. There are a number of extremely useful texts
which provide a more in-depth accounting of the scope of techniques in superconducting
circuit and cavity quantum electrodynamics (cQED) [22, 119123]. In this review chapter,
we will not present detailed derivations, but rather will outline the mathematics required
to derive and understand the system and provide references to original and pedagogical
resources, such that the reader will have sufficient context for understanding the remainder
of this dissertation.


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 33

#### a #### b
 S

![SchwarzThesis.pdf-44-0.png](SchwarzThesis.pdf-44-0.png)

![SchwarzThesis.pdf-44-1.png](SchwarzThesis.pdf-44-1.png)

Figure 4.1: Josephson junctions, defined by (a) a superconducting phase dierence across
the junction, which is equivalently a nodal flux. (b) If two junctions are joined in parallel
by a closed loop, the flux can be tuned by the introduction of an external magnetic field.

## 4.1 ## Superconducting Qubits

The field of superconducting quantum information has exploded since the observation of
the first coherent quantum oscillation in a Cooper pair box (CPB) circuit [36]. There are a
multitude of superconducting qubit implementations with relative strengths and weaknesses,
but all rely on the Josephson junction [124], a weak link that creates a tunneling barrier for
Cooper pairs between two (or more) superconducting islands. The Josephson current and
voltage relations for a superconducting tunnel junction give



2 __
_I_ = _I_ 0 sin __ =





_E_ _J_ sin __ ; (4.1a)



~
_V_ =

2 _e_



~
_V_ =


_d_


_d_ 0

= 
_dt_ 2 __


_d_

(4.1b)
_dt_


_d_


2 __


where  0 is the flux quantum _h/_ 2 _e_ , _E_ _J_ is the Josephson energy, and __ is the dierence
in superconducting phase between the two islands (Figure 4.1a). _I_ 0 sets the current above
which the tunneling gap is crossed and normal (resistive) current can propagate. The phase
__ can be written alternatively as




__ = 2 __




(4.2)


where  is the nodal flux at a fixed point in the circuit. This definition becomes particularly
useful if we join two Josephson junctions in parallel by a closed loop; then,  represents the
flux through the loop, which is typically an externally controllable parameter (Figure 4.1b).

We can re-arrange these equations to find the nonlinear Josephson inductance



~
_L_ _J_ =

2 _e_


 0

2 __




2




~
_L_ _J_ =



=
_I_ 0 cos __


1 _L_ _J_ 0

_._ (4.3)

_E_ _J_ cos __ __ cos __


1 _L_ _J_ 0

_E_ _J_ cos __ __ cos


The Hamiltonian describing the Cooper pairs moving through junction is given by

_H_  = 4 _E_ _C_ ( _n_ __ _n_ _g_ ) 2 __ _E_ _J_ cos __  (4.4)


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 34

where _E_ _C_ = _e_ 2 _/_ 2 _C_ is the charging energy required to move a single electron from one island
to the next, _C_ is the total capacitance of the junction (including that intrinsic to the junction
and any additional geometric capacitance),  _n_ is the number of Cooper pairs on one of the

islands, and _n_ _g_ represents an oset charge due to external electrical field or native charge
impurities. The _E_ _J_ cos __  term emerges from a tight binding model of Cooper pair tunneling.

If we take __ to be small and consider only the linear inductance, this Hamiltonian can be
rewritten as a simple Harmonic oscillator,



1
_H_  =

2 _C_


_Q_  2 +


2 _L_ _J_ 0


  2 _,_ (4.5)


where _Q_  and , representing charge and flux, are conjugate variables [125]. This represents 

a linear resonator with transition energy


_!_ q =


1 = 1

_L_ _J_ 0 _C_


8 _E_ _J_ _E_ _C_ _._ (4.6)


Of course, a linear resonator, whose quadratic potential produces a harmonic oscillator

with evenly spaced excitations, will not serve our purposes as a quantum bit. We require
a nonlinearity in the energy required to excite nearest-neighbor level transitions in order
to have any hope of isolating the lowest two levels _|_ _g_ _i_ and _|_ _e_ _i_ and treating them as an
approximate two-level system. In order to see the eects of the nonlinearity we must consider
higher order terms by evaluating the full Hamiltonian Eq. (4.4), whose eigenfunctions are
given by the Mathieu functions. As shown in Figure 4.2, these functions are periodic in
_n_ _g_ , and so we expect a qubit based on this Hamiltonian to be sensitive to charge noise,
particularly at bias points detuned from the charge degeneracy points at _n_ _g_ = __ _m/_ 2 (where
_m_ is an integer). Indeed, the first coherent oscillations seen in a superconducting circuit were
performed in a CPB, and had a phase coherence time of only 2 ns [36]. The wide range of
qubit designs developed over the last nearly twenty years aim to overcome this charge noise
without introducing other sources of noise sensitivity.

### 4.1.1 ### The transmon qubit

The transmon qubit, which we will use exclusively in this dissertation, uses a large external
capacitance to ameliorate the charge noise sensitivity in the CPB. Koch _et al._ showed

that the charge dispersion for the _k_ -th level is exponentially suppressed in the ratio _E_ _J_ _/E_ _C_
according to [114]



__ _k_
_E_ _k_ ( _n_ _g_ ) = _E_ _k_ + 2 cos(2 _n_ _g_ ); (4.7a)


_E_ _k_ __ _E_ _J_ +


8 _E_ _J_ _E_ _C_



1
_k_ +



_E_ _C_
__ 12


12


6 _k_ 2 + 6 _k_ + 3


(4.7b)


_E_ _J_

2 _E_ _C_




_k_

2




_k_ 2 + 3 4



4 _k_ +5

_k_ 2
__ _k_ ( 1)
__ __ _k_ !



_E_ _C_
__



_p_ 8 _E_ _J_ _/E_ _C_
_e_ __ _._ (4.7c)


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 35

![SchwarzThesis.pdf-46-0.png](SchwarzThesis.pdf-46-0.png)

Figure 4.2: The CPB spectrum, as a function of _n_ _g_ , for a range of _E_ _J_ _/E_ _C_ . We see that
as this ratio increase (from panels a - d), the undulations of the bands as a function of _n_ _g_
decrease, indicating an amelioration of charge-noise sensitivity. Reproduced with permission
from Ref. [114].

The modulation of the energy spectrum as a function of oset charge is now approximated
as a sinusoidal term whose amplitude is given by __ _k_ . Eq. (4.7c) indicates that this amplitude
is exponentially damped by the ratio _E_ _J_ _/E_ _C_ ; reducing _E_ _C_
therefore ought to be a straightforward route to damping the charge dependence of the energy level splittings. Figure 4.2
shows this damping for a range of _E_ _J_ _/E_ _C_ ; we see that when this ratio is greater than 50,
the oscillations are eectively flat and the circuit has been made charge-insensitive. This is
referred to as the transmon regime of the CPB architecture.

the transmon qubit is implemented by shunting the CPB by a large parallel capacitance,

such that _E_ _C_ _/h_ 200 MHz. The addition of a shunt capacitance leads to a renormalization
__
of the resonant frequency of the circuit; the bare energy levels in Eq. (4.7b) indicate that the

q
resonant qubit frequency becomes ~ _!_ = _E_ 1 __ _E_ 0 __ _p_ 8 _E_ _J_ _E_ _C_ __ _E_ _C_ . In Figure 4.3, we show
a circuit and schematic design for a transmon qubit, and a SEM micrograph of Josephson
junctions similar to those used in this dissertation to implement the transmon circuit.


With a typical Josephson energy given by _E_ _J_ _/h_ 20 GHz, the transmon _E_ _J_ _/E_ _C_
__ __

100 is sufficient to dramatically reduce the charge sensitivity, and thus to ameliorate a
critical source of dephasing. Because typical temperature _T_ _Q_ = ~ _!_ q _/k_ _B_ __ 300 mK, we perform experiments in a dilution refrigerator _!_ q _/_ 2 __ __ 6 GHz has a characteristic transition
with base temperature _T_ _B_ 10 30 mK in order to limit spurious thermal excitations of
__ __


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 36

**a** **b** **c**

![SchwarzThesis.pdf-47-0.png](SchwarzThesis.pdf-47-0.png)

![SchwarzThesis.pdf-47-1.png](SchwarzThesis.pdf-47-1.png)

![SchwarzThesis.pdf-47-2.png](SchwarzThesis.pdf-47-2.png)

Figure 4.3: Transmon qubit. a) The circuit design for a transmon qubit, with _E_ _C_ _E_ _J_
__
in order to suppress charge noise. b) The schematic design of a typical transmon qubit
implementation (not to scale), with a large dipole moment _~_ **p** aligned with the axis of the

antenna pads as shown. c) A SEM micrograph at 50,000x of the central SQUID junction,
which provides the nonlinear inductance required for a well-isolated two level system. SEM
image courtesy of Vinay Ramasesh.

the qubit.

The price that we pay for the reduction in charge sensitivity in the transmon qubit is

the anharmonicity. While the un-shunted CPB can have anharmonicity on the order of

several GHz at the charge-insensitivity bias point, the transmon anharmonicity is reduced to
__ __ _!_ _ef_ __ _!_ _ge_ = __ _E_ _C_ _/_ ~ , where ~ _!_ _ij_ = _E_ _j_ __ _E_ _i_ and _{_ _g, e, f_ _}_ represent the first three energy
levels of the transmon. An anharmonicity of several hundred MHz is sufficient to allow us to
drive transitions between _|_ _g_ _i_ and _|_ _e_ _i_ without exciting o-resonant transitions to the second
excited state _|_ _f_ _i_ , provided that the pulses used to drive the transitions are sufficiently long,
on the order of _>_ 20 ns such that 1 _/_ _|_ __ _|_ . However, additional pulse shaping [126129]
can be used to relax this limit, so the reduced anharmonicity is not a critical barrier.

The transmon qubit and its variants, because of their simplicity and straightforward

design, have become one of the workhorses of the superconducting qubit community. (Other
qubit geometries - most notably the flux qubit [116, 130132] - are also in use and have
some comparative advantages, most notably an increased anharmonicity.) Transmon qubits
can be designed and fabricated using now-standard techniques and are easily integrated into
complex circuits for readout and coupling. They also are readily tunable via the application
of external flux. In this dissertation, we implement the 3D transmon architecture [115]: we
fabricate transmon qubits on undoped silicon, and load them in a resonant microwave cavity.
Placing the qubit in a cavity is useful both for providing shielding from the electromagnetic
environment (enhancing qubit lifetime via the Purcell eect), and as we will see in the
upcoming sections, for enabling us to perform a QND measurement of the qubit state.


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 37

## 4.2 ## The Jaynes Cummings Hamiltonian

The elongated design of the capacitor pads that we use to shunt the Josephson junction(s)
in our qubits, shown in Figure 4.3b, allows them to serve a dual purpose. They reduce _E_ _C_ ,
providing a qubit well into the transmon regime of _E_ _J_ _E_ _C_ , while also providing an electric
__
dipole moment that enhances the qubits coupling to its local electromagnetic environment.
Eective qubit control and readout relies on understanding and control of this coupling.
The minimal description of atom-light interactions is provided by the Jaynes-Cummings
Hamiltonian, which we will derive and describe in this section.

### 4.2.1 ### Derivation

The interaction between a dipole and an electric field is given classically by 1

_H_  int = __ **E** _~_ ( _t_ ) **__** _~_ **p** = __ **__** **** _E_ ( _t_ ) **__** _~_ **p** (4.8)

Quantum mechanically, a microwave cavitys field modes can be described as quantum harmonic oscillators [9] with creation and annihilation operators  _a_ __ and  _a_ and resonant frequency

_!_ c . The vacuum fluctuations of the field are given by [125]

**E** _~_ = **** **__** _E_ _ZPF_ ( _a_ +  _a_ __ ) (4.9)

where _E_ _ZPF_ = ( ~ _!_ c _/_ 2 __ 0 _V_ ) is the RMS amplitude of the field fluctuations, and _V_ is the
eective mode volume. The Hamiltonian describing the interaction between the field mode
and a dipole with two states _{|_ _g_ _i_ _,_ _|_ _e_ _i}_ is thus given by


_H_ int =


_i,j_ = _g,e_


_E_ _ZPF_ _i_ _~_ **p** **** **__** _j_ ( _a_ +  _a_ __ ) _i_ _j_ (4.10)
__ _h_ _|_ **__** _|_ _i_ _|_ _i_ _h_ _|_


By parity arguments, we know that the dipole-field coupling cannot have diagonal density

matrix elements; if we (without loss of generality) assume the o-diagonal matrix element
to be real, we can then write the interaction Hamiltonian as 2

_H_  int = ~ _g_ _qc_ ( _a_ +  _a_ __ ) __ _X_ (4.11a)



1
_g_ _qc_ = __



_g_ _~_ **p** **** **__** _e_ _E_ _ZPF_ (4.11b)
~ _h_ _|_ **__** _|_ _i_


1 There is an ambiguity in the notation here that we inherit from physics conventions. Both geometric


unit vectors and Hamiltonian operators are indicated with a  x circumflex diacritic. The two rarely ap-


pear together in this dissertation, but for the sake of clarity we distinguish them by showing unit vectors
additionally in bold.

2 We use the notation _g_ _qc_ here to denote the qubit-cavity coupling rate. The standard notation for this

coupling is _g_ ; however, since we use _{_ _g, e, f_ _}_ to index qubit states, we add a subscript to the coupling term
to avoid ambiguity.


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 38


It is convenient to rewrite the qubit terms using raising and lowering operators  _X_ _Y_ + __ __ __


( __ _X_ __ _i_ __  _Y_ ) _/_ 2. The Hamiltonian then becomes _H_  int = ~ _g_ _qc_ ( _a_ +  _a_ __ )( __ + +  __ __ ) _._ The full


(nondissipative) system Hamiltonian is given by the sum of the bare resonator terms ( _H_  _a_ ),


the bare qubit terms ( _H_  _q_ ), and the interaction ( _H_  int ):


_H_  tot = _H_  _a_ + _H_  _q_ + _H_  int


(4.12)

= +1 state.


= ~ _!_ c _a_  __ _a_  + ~ _!_ 2 q __  _Z_ + ~ _g_ _qc_ ( _a_ __  + +  _a_ __ __  __ ) + ~ _g_ _qc_ ( _a_ __  __ +  _a_ __ __  + )


= ~ _!_ c _a_  __ _a_  + ~ _!_ q


__  _Z_




__  _Z_




where _|_ _g_ _i_ has been chosen to represent the


= __ 1 state and _|_ _e_ _i_ the


In Eq. (4.12) we have grouped the terms according to excitation-conserving and excitation
non-conserving terms. If _!_ c and _!_ q are reasonably close to one another, then going into
a rotating frame with respect to either will lead to rapid oscillations in the  _a_ __  __ and  _a_ __ __  +


terms; it is thus customary to drop these terms (the rotating wave approximation, RWA).
While the RWA is not always appropriate [133], it is usually a good approximation at the
single-photon levels we will typically use in this work. We will refer to the Hamiltonian
under the RWA as _H_  _JC_ , the Jaynes-Cummings (JC) Hamiltonian:


_H_  _JC_ = ~ _!_ c _a_  __ _a_  + ~ _!_ 2 q __  _Z_ + ~ _g_ _qc_ ( _a_ __  + +  _a_ __ __  __ ) (4.13)


Defining  __ _!_ q __ _!_ c , there are two useful limits to the JC Hamiltonian: near-resonant

(  _g_ _qc_ ) and dispersive (  _g_ _qc_ ). We will generally work within the dispersive limit
_|_ _| _ _|_ _| _
in this dissertation, but we can gain useful intuition by first examining the opposite limit,
 _g_ _qc_ .
_|_ _| _

### 4.2.2 ### Near-resonant case

The JC Hamiltonian is well-parametrized by states _|_ _n, g/e_ _i_ , where _n_ represents the Fock
state of the resonator. Under the RWA, the Hamiltonian is block-diagonal, coupling terms
of the form _|_ _n, e_ _i $ |_ _n_ + 1 _, g_ _i_ . In a two-dimensional subspace indexed by the _n_ -th Fock
state, the Hamiltonian is


_H_  _JC_ ( _n_ ) = ~ _!_



1
_n_ +


__  _I_ + ~ ( _!_ q __ _!_ c


__  _Z_ + ~ _g_ _qc_


_n_ + 1 __ _X_ (4.14)


where  __ _Z_ = +1 now corresponds to _n, e_ and  __ _Z_ = 1 corresponds to _n_ + 1 _, g_ . If _g_ _qc_ 0,

c ~ _!_ q _|_ _i_ __ _|_ _i_ _!_


the eigenvalues become ~ _!_ c ~ _!_ 2 q

q c __


as expected. If the qubit and cavity are near resonance


such that  _!_ q _!_ c _g_ _qc_ , nearly-degenerate perturbation theory shows that there is
_|_ _| |_ __ _| _


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 39

an avoided crossing between the qubit and cavity modes according to [134]


_E_ ( _n_ ) = ~ _!_ c
__



1
_n_ +



~
__ 2


 2 + 4 _g_ _qc_ 2 ( _n_ + 1) (4.15a)


 2 + 4 _g_ 2


 _n_

2




 _n_

2



 _n_

2




_|_ _n,_ + _i_ = sin


_|_ _n_ + 1 _, g_ _i_ + cos


 _n_

2




_|_ _n, e_ _i_ (4.15b)

_|_ _n, e_ _i_ (4.15c)

(4.15d)


_|_ _n,_ _i_ = cos


 _n_

2




_p_ _n_ + 1


_|_ _n_ + 1 _, g_ _i _ sin



2 _g_ _qc_
tan( _n_ ) =


When = 0 and the qubit and resonator modes are degenerate, the dressed eigenstates become symmetric and antisymmetric combinations of the bare eigenstates c _|_ _n,_ _i_ = ( _|_ _n_ + 1 _, g_ _i_
_n, e_ ) _/_ _p_ 2 with energies _E_ ( _n_ ) = ~ ( _n!_ _g_ _qc_ ). An excitation that is initialized in the qubit
_|_ _i_ __ __


(or in the cavity) will coherently oscillate between the two systems at a rate 2 _g_ _qc_


2 with energies _E_ ( _n_ ) = ~ ( _n!_ c _g_ _qc_ ). An excitation that is initialized in the qubit
__ __


_p_ _n_ + 1.


For transmon qubits with _g_ _qc_ on the order of tens to hundreds of MHz and qubit lifetimes
in excess of 10 __ s, the upper and lower polaritons defined by _E_ can be well-resolved in
__
frequency-domain spectroscopy, leading to a vacuum Rabi splitting well into the stronglycoupled regime ( _g_ _qc_ _,_ 1 _/T_ 1 _,_ 1 _/T_ __ ).
__

### 4.2.3 ### Dispersive (far-detuning) limit

When we go to the limit of  _g_ _qc_ , we intuitively no longer expect coherent swapping
__
of excitations between the cavity and the qubit, but the eect of the finite coupling must
still manifest in some way. To determine the eect of the coupling, we will transform to a
rotating frame in which the o-diagonal terms in the _|_ _n, e_ _i_ _,_ _|_ _n_ + 1 _, g_ _i_ subspace go to zero,
such that there are no undriven transitions between the two states. For this purpose, we will
treat the coupling as a perturbation:

_H_  = _H_  0 + _H_  1 ; (4.16a)


_H_  0 = ~ _!_ c _a_  __ _a_  + ~ _!_ 2 q __  _Z_ ; (4.16b)

_H_  1 = ~ _g_ _qc_ ( _a_ __ __  __ +  _a_ __  + ) (4.16c)


We would like to find a unitary rotation that cancels the perturbation to lowest order. In
the rotated frame, the Hamiltonian will be given by _H_  _0_ = _U_  _H_  _U_  __ _,_ where _U_  is a unitary

transformation _U_  = _e_ _c_  . The Baker-Hausdorrelation


+ 1

2!


ii


_e_ _c_   _He_ __ _c_  =  _H_ +


_c,_  


+ 1


_c,_ 


_c,_  _H_ 


+ _..._ (4.17)


suggests that a good unitary transformation will be one in which the perturbation is cancelled
at lowest order: in other words, we need an operator  _c_ such that the first commutator satisfies


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 40


_c,_  _H_ 


= _H_  1 . This condition is met when we use
__



~ _g_ _qc_
_c_  =


_a_  __  + __ _a_  __ __  __




(4.18)


Since we are treating _g_ _qc_ as a perturbative term, we keep only terms in Eq. (4.17) that are
up to quadratic in _g_ _qc_ . Defining the dispersive cross-Kerr term __ = _g_ _qc_ 2 _/_ , we are thus left


_qc_ 2 _/_ , we are thus left


with the JC Hamiltonian in the dispersive limit:


_H_  _0_


_JC_ _0_ _/_ ~ = _!_ c _a_  __ _a_  + _!_ q


2 __  _Z_ + __



1
_a_  __ _a_  +


__  _Z_ _._ (4.19)


The factor of ( _/_ 2) __ _Z_ represents the Lamb shift of the qubit frequency due to the interaction


with the cavity mode; the interaction in the rotated frame is given by _H_  int _0_ = ~ __ _a_  __ _a_  __  _Z_ .

The dressed eigenstates in this approximation are identical to the bare eigenstates, al-

though there is in general some weak mixing of the eigenstates given by Eq. (4.15). For
a transmon qubit, whose weak nonlinearity makes the two-level system approximation less
valid, the dispersive shift is slightly renormalized [114] by


__ = _g_ _qc_ 2



_._ (4.20)
__ + 


We can interpret _H_  int _0_ in two useful ways. The coupling between the qubit and the


We can interpret _H_ 


resonator manifests equivalently as a qubit-state dependent shift in the resonator frequency
( _!_ c q _!_ _!_ q c + __ __  _Z_ ); or as a resonator-occupation dependent shift in the qubit frequency


( _!_ q _!_ _!_ q + __ _a_  __ _a_  ). Critically, _H_ 


int _0_ commutes with the qubit state such that, as long as


the dispersive approximation holds, we can use the Jaynes-Cummings interaction to nondestructively read out the state of the qubit by probing the resonant frequency of the cavity.
In the next section, we will explore how this is achieved.


## 4.3 ## Dispersive Readout

Performing a measurement of the resonant frequency of the cavity in the dispersive regime is
the chief method we use in this dissertation to infer the state of the qubit. In this section, we
will first provide a semiclassical introduction to dispersive readout in order to gain intuition
for the the measurement process, and then will discuss a fully quantum treatment of the
measurement using both the Bayesian and the SME formalisms developed in Chapter 2.

Our dispersive measurements are carried out by fabricating a 3D copper resonator in

which we place a transmon qubit (shown schematically in Figure 4.4). The cavities generally
have two ports: one weakly coupled (input) port for transmission measurements, and one
strongly coupled (output) port such that virtually all photons, and thus all qubit state
information, leaks from the cavity via the latter. We will monitor the output port to read


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 41

![SchwarzThesis.pdf-52-0.png](SchwarzThesis.pdf-52-0.png)

Transmission Reflection

Figure 4.4: Schematic of a 3D cavity containing a transmon qubit, with weakly- and stronglycoupled ports ( __ in and __ out , respectively) for transmission and reflection measurements.

out the state of the qubit. The two ports are labeled by their bandwidths ( __ in __ __ out ); we
neglect internal losses. The bandwidths of the ports are set by their position in the cavity
(closer to a modal field maximum for stronger coupling), and by the extension of an antenna
coupler into the cavity (the longer the coupling pin, the stronger the coupling of the port).

### 4.3.1 ### Semiclassical treatment

To understand the mechanism of the dispersive readout, we will first treat the resonator as
a classical harmonic oscillator with a precisely defined amplitude and phase. We denote the
complex field amplitude inside the resonator as _A_ , where +(-) indicates the intra-cavity
__
field associated with the qubit in state cavity with frequency _!_ c , probed at frequency _|_ _e_ _i_ ( _|_ _g_ _i_ ). We can write the equations of motion for a _!_ d with an input drive amplitude _A_ in as


_A_  = __ _A_ _i_ ( _!_ c __ _!_ d ) _A_ +
__ __ 2 __ __ __ __ __


__ d _A_ in _._ (4.21)


Here, __ __ __ in + __ out and __ d is the decay rate of the driving port, which can be chosen from
the weakly coupled port for transmission measurements or the strongly coupled port for
reflection measurements (Figure 4.4). The steady state internal field solution is given by


_A_ =
__


__ d _A_ _d_

__ 2 + _i_ ( _!_ c __ _!_ d ) _._ (4.22)

__ __


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 42

When driven on resonance ( _!_ d = _!_ c ), the amplitude of the internal field is not qubit-state
dependent ( _A_ + = _A_ ), but there is a state-dependent phase shift given by
__

__ Arg _A_ = arctan( 2 _/_ ) _._ (4.23)
__ _{_ __ _}_ __


For a transmission measurement, the field propagating from the cavity is given by _A_ _,_ out =
__


__ out _A_ and therefore contains the same conditional phase shift as the intracavity field; the
__


output field in reflection interferes with the input drive according to _A_ _,_ out =
__


__ out _A_ __ __ _A_ in


yielding a net doubling of the phase shift in the propagating reflected field in comparison to
the intracavity field. By measuring the phase shift of the propagating field using standard
homodyne or heterodyne detection methods, we can thus infer the state of the qubit.


A measurement of the phase shift is typically the most eective means of inferring the

qubit state in the weak-measurement limit, where _/_ __ 1 such that the resonance profile
of the cavity conditioned on the qubit in state _|_ _g_ _i_ is very close to the resonance profile
conditioned on _|_ _e_ _i_ . In the opposite limit, _/_ __ 1 (often referred to as the number-resolved
regime, as the qubit will have well-resolved spectral peaks conditioned on the Fock state in the
cavity), qubit state information can be inferred from transmission amplitude measurements.
The transmission amplitude at _!_ d = _!_ c __ __ will be large if the qubit is in _|_ _g_ _i_ , but vanishing
if the qubit is in _|_ _e_ _i_ . In Chapters 5 and 6 we will work in the small _/_ limit and will
use homodyne detection to infer the phase shift. In Chapter 7 we will work in the numberresolved regime but will use high-power readout [135] rather than dispersive readout of the
field amplitude.

To this point, we have considered the field to have a well-defined amplitude and phase


with no uncertainty, and have further neglected to consider the implications of the qubit
existing in a superposition state of _|_ _g_ _i_ and _|_ _e_ _i_ . However, to understand the dispersive


measurement properly we must consider the intracavity field as a quantum object, one with
conjugate variables that enforce a Heisenberg uncertainty relationship, and we further must
allow the qubit to exist in a coherent superposition. In fact, we will see that it is precisely
the quantum uncertainty in the intracavity field mode that causes the qubit to stochastically
collapse into one of the measurement eigenstates __  _Z_ = 1.


__  _Z_




= __ 1.


### 4.3.2 ### Coherent states and measurement uncertainty


As we have seen, a quantized electromagnetic field can be represented as a harmonic oscillator. The in-phase [ _I_ = ( _a_ +  _a_ __ ) _/_ 2] and quadrature [ _Q_  = ( _i_ _a_  __ _i_ _a_  __ ) _/_ 2] components of


the field, corresponding to the real and imaginary components of the complex amplitude,
are incompatible observables with  _I_   _Q_  __ 1 _/_ 4. _I_  and _Q_  are the field equivalents of  _x_ and


_p_  in a physical quantum oscillator.


If the uncertainty in _I_  and _Q_  is equally distributed between the two quadratures such


that  _I_  =  _Q_  and the variance is isotropic in the IQ plane, the field is represented by

a coherent state. A coherent state [136] is a minimum-uncertainty state represented by a


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 43

superposition of photonic Fock states,


_|_ __ _i_ = _e_ _|_ __ _|_ 2 _/_ 2

_n_

X


__ _n_

_n_ _,_ (4.24)
( _n_ !) 1 _/_ 2 _|_ _i_


__ _n_


where __ is a complex displacement coefficient. The average photon number in the cavity

2
is given by _n_ = _|_ __ _|_ , and the photon number fluctuations are Poissonian: ( _a_ __ _a_  ) = _p_ _n_


_n_


These photon-number fluctuations are the source of the uncertainty in the field quadrature amplitudes. Coherent states are generated mathematically by applying a displacement
operator


_D_ ( __ ) = exp


__ _a_  __ __ __ __ _a_ 


(4.25)


to the vacuum state _|_ 0 _i_ , and they are eigenstates of the lowering operator according to

_a_  _|_ __ _i_ = __ _|_ __ _i_ _._ (4.26)

### 4.3.3 ### Unconditioned master equation

With this background on coherent states, we can now consider the eect of a cavity drive on
the qubit density matrix, both in the unconditioned (dissipated) and conditioned (measured)
case. Here, we follow Gambetta _et al._ [118] and sketch the important pieces of the derivation;
for a full development, see the original paper. Our goal here is not to perform an exhaustive
derivation, but rather to elucidate the connection between the experiments performed in this
dissertation and the stochastic measurement formalism described in Chapter 2.

The cavity drive Hamiltonian is described by

_H_  _d_ = ~ __ d [ _a_ __ _e_ __ _i!_ d _t_ +  _ae_ _i!_ d _t_ ] _,_ (4.27)


where for simplicity we have treated the drive amplitude as real. The drive rate __ d is


connected to the classical drive amplitude _A_ in in Section 4.3.1 by __ d =


__ d _A_ in . The non-


dissipative Hamiltonian, in the dispersive limit and in a frame rotating at _!_ d , is given by


_H_  e _/_ ~ = _!_ 2 q __  _Z_ +  cd _a_  __ _a_  + __ _a_  __ _a_  __  _Z_ + __ d ( _a_ __ +  _a_ ) _,_ (4.28)



_!_ q
_H_  e _/_ ~ =


where  cd __ _!_ c __ _!_ d is the cavity-drive detuning.

To study the full dynamics of the system, we must now include several loss mechanisms.


where  cd __ _!_ c __ _!_ d is the cavity-drive detuning.


Photons leak from the cavity at a rate __ __ __ out ; the qubit decays from the excited state to
the ground state at a rate  1 ; and phase coherence in the o-diagonal elements in the qubit
subspace occurs at a rate  __ . In the absence of a measurement, the Lindblad form of the
master equation including each of these decay channels is given by [136]


__  __




__  _Z_




_d_ _i_

=
_dt_ __


_d_



 __
__ +

2 _D_


_H_ e _, _


+ __ [ _a_ ] __ +  1
_D_ _D_



 __
__ +


(4.29)


= tot __
_L_


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 44

**a** **b** **c**
Q Q Q

![SchwarzThesis.pdf-55-4.png](SchwarzThesis.pdf-55-4.png)

![SchwarzThesis.pdf-55-6.png](SchwarzThesis.pdf-55-6.png)

![SchwarzThesis.pdf-55-5.png](SchwarzThesis.pdf-55-5.png)

![SchwarzThesis.pdf-55-0.png](SchwarzThesis.pdf-55-0.png)

![SchwarzThesis.pdf-55-1.png](SchwarzThesis.pdf-55-1.png)

![SchwarzThesis.pdf-55-2.png](SchwarzThesis.pdf-55-2.png)

![SchwarzThesis.pdf-55-3.png](SchwarzThesis.pdf-55-3.png)

Vacuum Displaced Vacuum After Interaction

Figure 4.5: Schematic representation of the dispersive measurement. The cavity is initialized
in a minimum-uncertainty coherent vacuum state (Panel a); a drive is applied to displace
the vacuum along the in-phase quadrature (Panel b); and the dispersive interaction leads
to a conditional phase accumulation that entangles the phase of the intra-cavity field with
the state of the qubit (Panel c). The blurred lollipops represent the intrinsic quantum
uncertainty of the intracavity field.


Here, _D_ [ _c_ ] __ is the Lindblad superoperator introduced in Section 2.3, and the density matrix

spans both the two-dimensional qubit space and the infinite-dimensional Fock space of the
cavity mode. We will shortly examine the dynamics in just the qubit sector (which is our
primary system of interest).

If we neglect qubit decay and make a fast-cavity approximation (i.e. assume the cav-

ity reaches steady state quasi-instantaneously and neglect transient dynamics), the density
matrix evolution is described by [118, 137]


__ ( _t_ ) =


__ i _,_ j ( _t_ ) _i_ _j_ __ _i_ __ _j_ _._ (4.30)
_|_ _i_ _h_ _| |_ _i_ _h_ _|_


_i,j_ = _g,e_


Here __ _i_ are coherent states whose mean displacement amplitudes and phases are identical
_|_ _i_
to those derived semiclassically in Eq. (4.22). Evidently, the qubit state is entangled with
the coherent state amplitude and phase within the cavity. We expect the measurement rate
to be related to the overall phase shift (governed by __ and __ ), and to the total displacement
(governed by __ d ).

The diagonal density matrix elements are given by their initial values __ i _,_ i ( _t_ ) = __ i _,_ i (0),


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 45

consistent with a QND measurement, and the o-diagonal terms evolve as


__ g _,_ e ( _t_ ) = __ g _,_ e (0) exp[ _i!_ q _t_  __ _t_ ] _e_ __ _i_ 2 __ _e_ __ _g_ __
__ __ _g_ __ _e_


__ _g_ __ _e_
_h_ _|_ _i_


(4.31)


__ e _,_ g ( _t_ ) = __ __ g _,_ e ( _t_ )


__ e _,_ g ( _t_ ) = __ __


The quantum description of the unconditioned eect of the measurement drive is now clear.
The intracavity coherent state serves as a pointer state for the qubit degree of freedom,
precisely as we expect given our semiclassical intuition. We begin in a vacuum state (Figure
4.5a), apply a drive amplitude __ d to generate a displaced coherent state (Figure 4.5b), and
allow the qubit and field to interact such that the qubit state information becomes encoded
on the average phase of the coherent state (Figure 4.5c). In the small _/_ limit, the phase
can be well-approximated by the projection onto the _Q_  quadrature, and the amplitude of

the field (and thus the mean and fluctuating photon number) is given by projection onto the

_I_  quadrature. If we measure the fluctuations in _Q_ -quadrature of the field propagating from
the cavity, we expect to be able to make a continuous measurement of the qubit state.

Let us now consider the unconditioned eects of the cavity drive on the qubit. To isolate


the evolution in the qubit sector, we make a unitary transformation _U_  _U_  __ , where _U_  is given

by

_U_  = _e_ _e_ _D_ ( __ _e_ ) + _g_ _g_ _D_ ( __ _g_ ) _._ (4.32)
_|_ _i_ _h_ _|_ _|_ _i_ _h_ _|_

This transformation is the equivalent of an unconditioned displacement of the coherent state
back to the vacuum, and is often referred to as the _polaron transformation_ . Under the

polaron transformation, one can straightforwardly trace over the cavity degrees of freedom,
yielding a reduced qubit master equation


__  __


__  _Z_




_d_ _q_ _!_ q

= _i_ 
_dt_ __ 2


_q_ _!_ q

= _i_ 
_dt_ __ 2


__  _Z_ _, _ _q_ ( _t_ )


+  1
_D_



 __ +  _d_
__ _q_ ( _t_ ) +


__ _q_ ( _t_


(4.33)


= _q_ __ _q_ ( _t_
_L_


Here, __ _q_ ( _t_ ) = Tr _c_ __ ( _t_ ) is the reduced qubit density matrix traced over the cavity degrees
of freedom,  _!_ q is the ac Stark-shifted qubit frequency, and  _{_ _}_ _d_ is a measurement-induced

dephasing rate. These are given by


_!_  q = _!_ q + 2 __ Re __ _g_ __ _e_
_{_


_e_ __ (4.34)

_}_


 _d_ = 2 __ Im __ _g_ __ _e_
_{_


_e_ __ _}_ = __ 2



__ _g_ __ _e_ 2 (4.35)
2 _|_ __ _|_


Thus, we have derived the unconditioned eects of the measurement drive on the qubit:

the qubit frequency shifts, and an initial coherent superposition of _|_ _g_ _i_ and _|_ _e_ _i_ dephases at
an additional rate  _d_ . The additional dephasing is caused by the fundamental uncertainty in
the coherent pointer state, which provides the fluctuations that generate a stochastic backaction on the qubit. In the unconditioned case, we average over these fluctuations, leading
to an overall dephasing.


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 46

### 4.3.4 ### Dispersive measurement: Bayesian approach


Now that we understand the unconditioned interaction between the qubit and the cavity
drive, we can consider a measurement process that monitors the output of the cavity mode.
As in Chapter 2, we can apply either a phenomenological Bayesian approach, or a more
fundamental stochastic master equation. We will begin here with the Bayesian approach,
outlined by Korotkov [138].

Suppose we monitor the _Q_  quadrature of the light, which in Figure 4.5 contains the qubit


state information. We expect the instantaneous homodyne measurement voltage _V_ _Q_ ( _t_ ) to be
proportional to


_V_  _e_ _V_  _g_
__


__  _Z_




_V_ _Q_ ( _t_ ) =



+ __ ( _t_ ) (4.36)
_t_


where the spectral density of the fluctuating __ ( _t_ ) is related to the photon shot noise and


_V_  _i_ is the mean value of _V_  if the qubit is prepared in state _i_ . Here we have introduced


__  _Z_


the conditional expectation value



, which denotes the updated expectation value of
_t_


__  _Z_ given the measurement record up until time _t_ . The Markovian approximation and the
QND nature of the measurement allow us to assess this expectation value using the mean
integrated signal,


_t_

0

Z



1
_V_  _Q_ ( _t_ ) =


_V_ _Q_ ( _t_ _0_ ) _dt_ _0_ _._ (4.37)


In other words, we can update our estimate of the density matrix without regard to the
specific path of the instantaneous _V_ _Q_ ( _t_ ), but rather by considering only the accumulated
signal as of time _t_ . The conditional probability for the outcome _V_  _Q_ given the qubit eigenstate


_|_ _i_ _i_ is given by the Gaussian function


_p_ _i_ ( _V_  _Q_ ) =



_e_ (  _V_ _Q_ __ _V_  _i_ ) 2 _/_ 2 __ 2 _._ (4.38)
2 __


If we choose _!_ d = _!_ c and operate in the small-angle limit appropriate for weak measurements,
we can approximate _V_  _g_ = (2 _/_ ) _p_ _n_ and _V_  _e_ = _V_  _g_ _V_  ; we now need only determine the


_n_ and _V_  _e_ = __ _V_  _g_ __ _V_  ; we now need only determine the


variance __ 2 . Recalling that  _I_   _Q_  __ 1 _/_ 4, and that in a coherent state the fluctuations are 2


symmetric in the two quadratures, we can denote the single-quadrature variance as __ 2


0 2 = 1 _/_ 4.


As we integrate the signal, the variance decreases as __ 2 ( _t_ ) = __


0 2 _/_ ( _t_ ): information leaks


from the cavity at rate __ , with a total efficiency __ , which is related to the collection efficiency
__ coll by __ = __ out __ __ coll . The SNR of the measurement is thus given by


from the cavity at rate __ , with a total efficiency __ , which is related to the collection efficiency
__ coll by __ = __ out __ coll . The SNR of the measurement is thus given by


_Q_  _g_ _Q_  _e_
__

__ ( _t_ )




2
!


SNR 2 _S_ ( _t_ ) =

= 64 __ 2 _nt_


(4.39)


Given the nondimensional measurement strength _S_ ( _t_ ), we can now calculate the conditional
probabilities in Equation (4.38), and can perform the Bayesian update as outlined in Section


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 47

2.2. Because the measurement is QND, we can integrate the signal continuously and perform
a Bayesian update at each timestep in order to reconstruct the full quantum trajectory. The
measurement-induced evolution in the qubit state is given by


_S_ 2 ( _t_

4 _V_ 







__  _Z_

__  _X_ 




__  _Z_




( _t,_ _V_  _Q_ ) = tanh


_V_ _Q_


(4.40)


2 _e_ __  _t_ (4.41)



( _t,_ _V_  _Q_ ) =


1 __


__  _Z_ ( _t,_ _V_  _Q_ )
_h_ _i_


 = 1


+ 8 __ 2 _n_


(1 __ __ ) (4.42)


_T_ 2 __


In the case where the collection efficiency is unity, there is no measurement-induced dephasing
and the purity of the density matrix is degraded only by intrinsic dephasing in the qubit. This
was the approach used by Murch _et al._ [61] in the first continuous trajectory reconstruction
in superconducting qubits.

Notice that we have only considered here the fluctuations in the _Q_  quadrature - but as


we know, there are additional fluctuations in the _I_  quadrature that should contribute to

the dynamics. In the small-angle limit, fluctuations in _I_  correspond to fluctuations in the

amplitude _|_ __ _|_ , which Eq. (4.34) tells us causes a Stark-shift of the qubit frequency and
therefore causes a stochastic accumulation of phase between _|_ _g_ _i_ and _|_ _e_ _i_ . However, if we
use a nearly quantum-limited parametric amplifier that is sensitive to only one quadrature
(Section 4.4), the fluctuations in the _I_  quadrature are eectively erased, and therefore

do not contribute to the dynamics of the system. We will see in Section 4.4 how such an
erasure is accomplished. If instead we use a phase-preserving amplifier, which amplifies

both quadratures of the light, we will need to record both _V_ _Q_ and _V_ _I_ , using _V_ _Q_ to update
the projection onto  __ _Z_ and _V_ _I_ to update the azimuthal phase on the Bloch sphere. For a

detailed description of quantum noise and amplification, see Ref. [75].

### 4.3.5 ### Dispersive measurement: Master equation approach

While the Bayesian approach is powerful in its simplicity, it is also useful to understand
quantum trajectories in cQED using the master equation approach. Let us therefore return
to the master equation formalism of Section 4.3.3, and now add the conditional dynamics
that arise from monitoring the cavity decay channel. Again, we will use homodyne detection
to measure the _Q_  quadrature of the propagating field. The measurement signal in this case

can be represented by [136, 139]


_i_ _a_  __ _i_ _a_  __




_V_ _Q_ ( _t_ ) = _p_ __


_t_ + __ ( _t_ ) = 2 _p_ __



+ __ ( _t_ ) _,_ (4.43)
_t_


where __ ( _t_ ) again represents a Gaussian approximation for the photon shot noise and


represents the expectation value of _Q_  given the continuously updated estimate of the density

matrix. Note the dierence between this equation and Eq. 4.36: here, the deterministic


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 48

component of the signal is related directly to the observed field quadrature, where in Eq.
4.36 the deterministic component is scaled phenomenologically to the expected voltages given
the two qubit states. The Bayesian approach in eect skips the intermediate step of deriving
the transformation between the field quadrature signal and the qubit state; in the SME
formalism we must explicitly derive that scaling.

Given the stochastic quadrature signal, we can update the unconditioned master equation

Eq. (4.29) to include a measurement back-action term:


_d_

= tot __ + __ ( _t_ ) _p_ __
_dt_ _L_ _H_


_d_


(4.44)


= tot __ + __ ( _t_ ) _p_ __ [ _i_ _a_  ] __
_L_ _H_


Since _d_


_dt_ now depends on a stochastic term, we consider __ to now be a _conditioned_ density


matrix. The stochastic master equation contains a measurement superoperator defined in
Chapter 2 corresponding to monitoring photon leakage from the cavity. Just as in Section
4.3.3, we can apply the unitary transformation in Eq. (4.32) which, if all the qubit state
information is contained in the _Q_ -quadrature, yields 3


__  _Z_




_d_



= _q_ __ _q_ ( _t_ ) + __ ( _t_ )
_dt_ _L_


__  _m_
_H_


__ _q_ (4.45a)



__
 _m_ =



__ __ _g_ __ _e_ 2 =  _d_ _/_ 2 (4.45b)

4 _|_ __ _|_


Ignoring intrinsic qubit decay, the full conditioned qubit state evolution is thus given by


__  _Z_




__  _Z_




_d_ _q_ _!_ q

= _i_ 
_dt_ __ 2


_q_ _!_ q

= _i_ 
_dt_ __ 2


__  _Z_ _, _ _q_ ( _t_ )



 _d_
+


2 _D_


__ _q_ ( _t_ ) +


__  _m_
_H_


__ _q_ __ ( _t_ ) _._ (4.46)


Thus, we can correlate the instantaneous homodyne measurement current _V_ _Q_ ( _t_ ) with a
stochastic evolution of the qubit state. However, notice that the measurement rate saturates
to half the dephasing rate as defined in Eq. (4.35), leading to a maximum eective quantum
efficiency __ e = __  _m_ _/_  _d_ of 1/2. This is because half of the fluctuations to which the qubit
is exposed are in the unmeasured _I_  quadrature. The formalism developed in Ref. [118]


implicitly assumes the use of a phase-preserving amplifier, after which only one quadrature
is recorded; half of the fluctuations are therefore lost, and half of the qubit state evolution
is untraceable and manifests as dissipation.

## 4.4 ## Parametric Amplification

In both the Bayesian approach and the SME formalism, continuous state tracking depends
critically on near-unity quantum efficiency. If 1, the conditioned dynamics are essentially indistinguishable from the pure measurement-induced dephasing seen in Section 4.3.3; __ __

3 Observant readers will note a dierence between Eq. (4.45b) and the equivalent in Ref. [118]. This


is due to a dierence in the definition of the measurement operator. The translation is given by _H_ [ _c_ ] __ =

2 _M_ [ _c_ ] __ , where _M_ [ _c_ ] __ is the measurement operator used in the original source.


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 49

only when the quantum efficiency is high can we hope to perform continuous state tracking.
Efficient measurement requires amplifying the signal, whose quantum fluctuations give it
an eective temperature _T_ _Q_ = ~ _!_ d _/_ 2 _k_ _b_ __ 170 mK, enough to overcome room-temperature
thermal fluctuations that are five orders of magnitude larger. This amplification must be
accomplished without adding significant uncorrelated noise in order to reconstruct the quantum state with high fidelity. Needless to say this task is technically challenging - but it can
be accomplished using an amplifier circuit that is quite similar to the transmon circuit itself.

### 4.4.1 ### The lumped Josephson parametric amplifier

The amplifier we use in this dissertation is the lumped Josephson parametric amplifier
(LJPA) [120, 140, 141]. It consists of a pair of Josephson junctions with relatively large
critical current (several __ A) fabricated in a parallel loop, shunted by a correspondingly large
capacitance (several pF) such that the zero-flux resonant frequency is near the measurement
frequency (near 8 GHz) and can be tuned down to resonance if desired. The large shunt capacitance means that the anharmonicity is relatively small such that when the intra-resonator
photon number is low, the LJPA acts as a linear resonator. However, when the amplifier is
biased with a large pump tone, its resonance bends to lower frequencies due to the negative
anharmonicity of the circuit, as in Figure 4.6a. When the bias exceeds a critical power, the
resonance bifurcates. The parametric amplification regime requires a bias pump power just
below the bifurcation point, such that the resonant frequency of the resonator is maximally
dependent on the power. We combine the pump tone with our small experimental signal
and reflect the total field oof the LJPA. The phase response of the reflected field (Figure
4.6b) provides the amplification we desire.

When the amplifier is biased with a large pump, its weak nonlinearity generates a __ (3)


dispersive medium that is able to do four-wave mixing. Specifically, a coherent pump drive
at _!_ p modulates the eective Josephson inductance, and thus the resonant frequency, of
the circuit. This modulation, which occurs at 2 _!_ p , can be accomplished either by the

combination of two degenerate pump photons, or of two detuned photons at _!_ p _!_ _IF_
__
Conservation of energy requires that the two photons generated by the four-wave mixing
process, labelled the signal and idler photons, satisfy 2 _!_ p = _!_ _s_ + _!_ _i_ . In the case where
_!_ _s_ = _!_ _i_ = _!_ p , the amplifier performs doubly-degenerate four-wave mixing. This is the regime
in which we will operate. Typical LJPAs operate with 20 dB of gain over a bandwidth of 1050 MHz; recent advances in impedance matching and microwave engineering [142, 143] enable _>_
similar gain over 500-700 MHz of bandwidth. There are other useful Josephson junctionbased amplifier designs, notably including the Josephson parametric converter (JPC) [144
147] which is another resonant superconducting amplifier that performs three-wave mixing.
Recently, a nearly quantum-limited Josephson traveling-wave parametric amplifier (TWPA)
was demonstrated [148], which exhibits 20 dB of gain over several GHz of bandwidth. For
a full derivation of the JPA amplification and performance properties, see Refs. [120] and

[140].


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 50

180


90

-90


![SchwarzThesis.pdf-61-0.png](SchwarzThesis.pdf-61-0.png)

-180


![SchwarzThesis.pdf-61-1.png](SchwarzThesis.pdf-61-1.png)

0.02 0.04 0.06 0.08 0.10


### Pump Current (I ### /I ### )

![SchwarzThesis.pdf-61-3.png](SchwarzThesis.pdf-61-3.png)
d 0


![SchwarzThesis.pdf-61-2.png](SchwarzThesis.pdf-61-2.png)

Figure 4.6: LJPA characteristics. (a) Resonant frequency: as pump power increases, the
resonant frequency of the amplifier ( _!_ _p_ 0 ) bends downward, eventually bifurcating after a
critical point ( _!_ _c_ _, P_ _c_ ). (b) Phase response: as injected power increases, the reflected phase
changes accordingly. Adapted from Ref. [120].

We briefly note that 20 dB of gain is not yet sufficient to overcome room-temperature

fluctuations. In order to provide the necessary additional amplification, we follow the LJPA
with a low-noise HEMT ( 10) at the 4 K stage of the dilution refrigerator, which provides 30 dB of amplification, and utilize additional room-temperature amplifiers. However, __ __ 1 _/_
the noise temperature of the full amplification chain is dominated by the quantum efficiency
of the lowest stage, provided that its amplification is large enough [120]. Therefore, the
quantum efficiency of the overall measurement chain depends critically on the quality of the
first cryogenic amplifier.

### 4.4.2 ### Phase-sensitive amplification

One of the features that makes the LJPA an attractive choice in comparison to the JPC
and the TWPA is its ability to perform phase-sensitive amplification, amplifying a single
quadrature of light while de-amplifying, or squeezing, the other. Phase sensitive amplification
occurs when _!_ _i_ and _!_ _s_ are degenerate with _!_ p , such that the input signal adds coherently
with the pump tone. Figure 4.7 illustrates the phase sensitivity of the amplifier at degeneracy.
The component of the measurement signal that is in-phase (or 180 __ out of phase) with the
pump increases (or decreases) the intra-cavity power directly by vector addition, causing an
amplified phase shift in the reflected field. The components of the signal that are __ 90 __ out


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 51


![SchwarzThesis.pdf-62-4.png](SchwarzThesis.pdf-62-4.png)

![SchwarzThesis.pdf-62-5.png](SchwarzThesis.pdf-62-5.png)

![SchwarzThesis.pdf-62-0.png](SchwarzThesis.pdf-62-0.png)

![SchwarzThesis.pdf-62-1.png](SchwarzThesis.pdf-62-1.png)

![SchwarzThesis.pdf-62-2.png](SchwarzThesis.pdf-62-2.png)

Total Power (Pump + Signal)

![SchwarzThesis.pdf-62-3.png](SchwarzThesis.pdf-62-3.png)

Figure 4.7: Schematic demonstration of phase-sensitive amplification. a) A strong pump
tone combines with a much weaker readout signal via vector addition. b) If the signal is
directly parallel or antiparallel to the pump tone (A, C), the total power in the nonlinear
resonator changes maximally, and the phase response is maximized. Weak signals that are
out of phase with the pump (B, D) do not aect the total power to first order; therefore, the
out-of-phase signal is reduced. c) After passing through an LJPA operating in phase-sensitive
mode, a coherent state is reflected as a squeezed state.

of phase with the drive, however, only cause a change in the intra-cavity power at second
order, since the pump tone is much larger than the signal. In this case, the out-of-quadrature
components of the signal are actually de-amplified, or squeezed. If the amplification and
squeezing are sufficiently large, the LJPA essentially erases the fluctuations in the out-ofphase quadrature, such that they no longer cause a back-action on the qubit state. This is
precisely the situation we described in Section 4.3.4, which allows us to eectively perform a
single-quadrature measurement while ignoring the back-action caused by fluctuations in the
complementary quadrature.

The squeezing performed in phase-sensitive amplification additionally enables noiseless

amplification. If the gain of the amplifier is given by _G_ and the input signal represented by
the bosonic modes  _a_ , then we can represent the output of the amplifier as  _b_ , where


 _b_ =

 _b_ __ =


_G_ _a_  ;

(4.47)
_a_  __ _._


 _b,_  _b_ __

i


It is straightforward to show that


= 1, such that the outgoing amplified field need


contain no additional fluctuations. This noiseless amplification is useful for efficient readout,
and is critical for the reconstruction of quantum trajectories. In contrast, phase-preserving


-----


_CHAPTER 4. THE SUPERCONDUCTING CQED ARCHITECTURE_ 52

amplification (in which both quadratures are equally amplified, for example by an LJPA
operating oof degeneracy or by a TWPA) requires the addition of, at minimum, one
photon of uncorrelated noise in order to preserve the unitary commutation of  _b_ and  _b_ __ . This

additional noise reduces the rate at which a projective measurement can be performed, and
limits the ability to reliably reconstruct a quantum trajectory (since at minimum half of
the fluctuations observed by the experimenter are uncorrelated with the back-action on the
qubit). For an intensive treatment of quantum noise and parametric amplification, see Ref.

[75].

## 4.5 ## Summary: The Superconducting Qubit Toolbox

We now have a basic understanding of all the elements required to perform quantum experiments using superconducting circuits. The superconducting Josephson junction creates
a nonlinear inductance that, when embedded in an LC circuit, generates a nonlinear resonator with unequal spacing between neighboring energy levels (Section 4.1). The capacitive
element in the qubit LC circuit can be designed with a significant electric dipole moment,
allowing the qubit to couple strongly to the electromagnetic field modes inside a resonator
via the Jaynes-Cummings Hamiltonian (Section 4.2). When the qubit and cavity are fardetuned from one another, this interaction enables us to use a displaced coherent state inside
the cavity as a pointer state for the qubit; by monitoring the reflected or transmitted phase
of a measurement signal passing through the cavity, we can continuously infer the qubit state
(Section 4.3). The qubit state inference can be done continuously and with high fidelity by
employing a nearly-quantum limited amplifier, in this case an LJPA, which squeezes fluctuations in the undesired quadrature and amplifies the quadrature containing qubit information
(Section 4.4). Thus, we have all the tools we need to create, manipulate, and measure

coherent quantum circuits.


-----


53

# Chapter 5

 Remote Measurement-Induced Entanglement

I cannot seriously believe in [quantum mechanics] because the theory
cannot be reconciled with the idea that physics should represent a
reality in time and space, free from spooky actions at a distance.

Albert Einstein, _Letter to Max Born_ , 1947

We now proceed to investigate a first practical use of dissipation in our superconduct-

ing cQED architecture: we use a carefully-tailored measurement to generate entanglement
between qubits that are separated from one another by many wavelengths, have no local
coupling, and are therefore functionally remote. Entanglement schemes for superconducting qubits have traditionally relied on direct qubit-qubit coupling [26, 27, 39, 149151],
cavity-mediated interactions [2830, 152154], or local photon-mediated interactions [155].
However, the creation of a quantum network requires the distribution of coherent information across macroscopic distances. Measurement-induced entanglement (MIE) [156161] is
a particularly important resource in these spatially-separated quantum systems, for which
no local interactions and therefore no direct methods of creating entanglement exist. Such
remote entanglement has been demonstrated using optical photons in several atomic systems

[162164] and nitrogen vacancy centers [88, 165], but has remained elusive for superconducting qubits, which operate in the microwave regime.

In this chapter, we demonstrate measurement-induced entanglement between two super-

conducting qubits, each dispersively coupled to a separate cavity for readout and separated
by 1.3 meters of ordinary coaxial cable, by engineering a continuous measurement for which
one of the three outcomes is a Bell state [166]. This measurement constitutes a _half-parity_
_measurement_ , in which the odd-parity states ( _|_ _ge_ _i_ and _|_ _eg_ _i_ ) are indistinguishable from one
another, but the even-parity states ( ) are distinguishable both from the oddparity manifold _and_ from each other. The use of continuous measurements allows us to access _|_ _gg_ _i_ and _|_ _ee_ _i_
the ensemble-averaged _dynamics_ of entanglement generation, which are well-described by a


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 54

statistical model and by a full master-equation treatment. As we will see in Chapter 6, our
measurement efficiency is sufficiently high to resolve the individual quantum trajectories in
the ensemble, thus enabling the observation of the stochastic evolution of a joint two-qubit
state under measurement. This functionality sheds new light on the fundamental interplay
between entanglement, measurement, and decoherence in a quantum network. This work
was originally published as Ref. [167].

## 5.1 ## Historical Perspective

Using a continuous measurement to generate entanglement remotely represents one of the
chief innovations in our approach to remote measurement-induced entanglement. To understand why this development is important, we first must understand previous MIE schemes,
which rely on photon-counting and post-selection, necessarily reducing the success rate of
the protocol. For quantum architectures building upon transitions at optical frequencies [88,
162, 164, 165], MIE has typically been achieved by relying on the correlated detection of
photons at the output of a beam-splitter [168] to herald an entangled state. While powerful,
this measurement protocol is binary and practically instantaneous, and allows no insight into
the dynamical processes underlying the generation of the entangled state. In solid state systems with transitions in the microwave, there has been tremendous interest in _continuously_
generating bipartite [156, 158, 169171] and multi-partite [160, 161, 172] entangled states,
using weak measurements that slowly interact with the qubits, in such a way that enables
the resolution of the dynamical aspects of the entangling backaction. Such a measurement
was demonstrated in a local system (two qubits housed within the same cavity) concurrent
with this work [154]; our work represents the first use of continuous measurement to generate
entanglement between quantum objects separated by many wavelengths of their characteristic frequencies. The use of weak measurements additionally opens the door to feedback
stabilization [139, 173176], bringing the protocol from a probabilistic to a deterministic
method of generating entanglement [171, 177, 178].

A second critical dierence between photon detection and continuous measurement for

the purpose of generating entanglement is the eect of losses. Photon detection-based experiments typically exploit the Hong-Ou-Mandel Eect [168], which states that identical photons
simultaneously incident on two input arms of a 50/50 beam splitter will emerge on the same
output arm. One can understand this trivially by considering the time-reversed case: two
photons simultaneously arriving on one arm of such a beam splitter must emerge with equal
amplitude on both arms. Equivalently, one can coherently add the four transmission and
reflection possibilities as shown in Figure 5.1; the negative signs come from reflection from
the bottom of the beam splitter. If the incoming photons are indistinguishable, the second
and third amplitudes cancel, leading to photon bunching.

In a photon detection MIE experiment, the two qubits are each prepared in an x-polarized


state = _|_ _g_ _i_ _p_ + 2 _|_ _e_ _i_
_|_ _i_



_|_ _i_ , after which a Raman scattering mechanism is used to stimulate emission of

2


a photon into a traveling mode conditioned on the qubit in state _|_ _e_ _i_ such that the total system


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 55

+ --

![SchwarzThesis.pdf-66-0.png](SchwarzThesis.pdf-66-0.png)

![SchwarzThesis.pdf-66-1.png](SchwarzThesis.pdf-66-1.png)

![SchwarzThesis.pdf-66-2.png](SchwarzThesis.pdf-66-2.png)

![SchwarzThesis.pdf-66-3.png](SchwarzThesis.pdf-66-3.png)

Figure 5.1: An illustration of the Hong-Ou-Mandel eect which is typically used for

measurement-induced entanglement in photon-counting experiments. Two photons incident
on opposite arms of the beam splitter can emerge in four possible arrangements. Due to an
overall phase shift of __ caused by reflection from the bottom of the beam splitter, the second
and third possibilities interfere destructively, leading to photon bunching.


state becomes 1



1 2 [ _g,_ 0 + _e,_ 1 ] _A_ [ _g,_ 0 + _e,_ 1 ] _B_ . The photons act as flying qubits: they

_|_ _i_ _|_ _i_ __ _|_ _i_ _|_ _i_


interfere with one another at the beam splitter, and are then counted at photon detectors
coupled to both output modes of the beam splitter.


If the transmission and detection efficiencies are both unity such that all photons arrive


at the beam splitter and are accurately counted at the detectors, there are three possible
outcomes. A measurement of zero photons at either node projects the qubits into the state
_|_ _gg_ _i_ ; two photons detected at either node projects into _|_ _ee_ _i_ . However, a single photon


detected at either node does not provide which-path information: the photon could have
been emitted from either sample, and therefore from the standpoint of the measurement has
come simultaneously from _both_ . This projects the system into the degenerate odd-parity
subspace, leading to an entangled state _|_ _ge_ _i_ _p_ _e_ 2 _i_ _|_ _eg_ _i_ , where __ is determined by the path length


, where __ is determined by the path length


and the __ phase is heralded by the arm of the detector on which the photon emerged. Thus,
a single photon detection event can be said to herald an entangled state.


The chief eect of transmission loss in such a system is clearly to reduce the success rate

of the experiment. For experimental iterations in which a single photon is emitted, but is
absorbed by fiberoptic cable before reaching the photodetector, from the standpoint of the
experimentalist there was never a photon emitted at all. This iteration is excluded from
the heralded ensemble, although it would have otherwise generated an entangled state (and
if the photon dissipated after the beam-splitter, in fact _did_ generate entanglement). Thus,
the entanglement generation rate is diminished. If the qubits are in _|_ _ee_ _i_ and two photons
are generated, but one is absorbed and one detected, there is the possibility of an error:
the experimentalist may include this experiment in the heralded ensemble, leading to an
excess of _|_ _ee_ _i_ population and degrading the quality of the ensemble. To protect against this
decoherence mode, however, one can perform bit flips on the two qubits and then repeat
the experiment. If the qubits were in _|_ _ee_ _i_ , the bit flip takes the system to _|_ _gg_ _i_ and no
photons will be detected; if a single photon is detected again, the entanglement is confirmed.
If the fiberoptic cable and the detectors are reasonably high in transmission and detection
efficiency, the odds of a double absorption error are vanishingly small. Thus, the chief eect


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 56

of inefficiency in a photon counting experiment is to diminish the heralding rate; the ensemble
of measurements that pass the herald will be reasonably pure.

For a continuous dispersive measurement using a coherent state, however, the eects of

losses are dierent. Recall that coherent states are eigenstates of the annihilation operator  _a_ :

even in the case of a photon scattering event, a measurement signal will reach the homodyne
detector, and the experimentalist will be able to make an estimate of whether or not the
outcome is consistent with an entangled state. The advantage here is that the entanglement
generation rate is preserved, and can be orders of magnitude larger than the rate in photon
counting case. However, any photons absorbed before the detector will carry away with
it information about the qubits, and unlike in the photon counting case we cannot postselect away the eects of spurious photon absorption. As we will see, photon scattering on
the path between the two cavities leads to an unavoidable measurement-induced dephasing
of the entangled ensemble. This eect provides us an opportunity to study in detail the
interplay between measurement and dissipation in a quantum system.

## 5.2 ## Design of an Entangling Continuous Measurement

Our experimental apparatus consists of two superconducting transmon qubits placed in
spatially separated copper waveguide cavities (3D transmon architecture) [115]. Each cavity
is wound with a superconducting bias coil to enable tuning of the qubit frequency. A weakly
coupled port is used for transmission measurements and single qubit control, and a strongly
coupled port enables qubit state readout. The strongly coupled ports of the two cavities are
connected via two microwave circulators and 1.3 meters of coaxial cable to enable directional
transfer of information from Cavity 1 to Cavity 2 (Figure 5.2).

### 5.2.1 ### Joint dispersive measurement

A joint qubit state measurement can be performed by sequentially driving the cavities in
reflection with a near-resonant microwave tone at frequency _!_ m
that can be described semiclassically as a complex coherent drive _A_ _d_ , as in Section 4.3.1. For clarity, we use _A_ ( _t_ ) and
_B_ ( _t_ ) to represent the intracavity fields in Cavity 1 and Cavity 2, respectively, and _A_ out , _B_ out
to represent the propagating fields traveling _from_ the respective cavities. For a single qubit
in an eigenstate, measured in reflection, the output state is given by _A_ out = _r_ __ _A_ _d_ , where



__ 2 _i_ ( _!_ c _!_ m __ )
_r_ __ = __ __ __ _,_ (5.1)

__ + 2 _i_ ( _!_ c __ _!_ m __ __ )


and the signifier + (-) represents the single qubit state _|_ _g_ _i_ ( _|_ _e_ _i_ ). Here, _!_ c is the bare cavity
frequency; __ is the total cavity decay rate; and __ is the dispersive shift due to the interaction
between the qubit and the cavity. The measurement tone acquires a qubit state-dependent
phase shift __ __ = Arg _A_ __ out . For the following analysis it is convenient to define the average


_A_ __


out


. For the following analysis it is convenient to define the average


and relative phase shifts, __ = 1



1 2 ( __ + + __ __ ) and  __ = __ + __ __ , respectively (See Figure 5.2.1a).

__


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 57

**a**

![SchwarzThesis.pdf-68-0.png](SchwarzThesis.pdf-68-0.png)

**b**

![SchwarzThesis.pdf-68-1.png](SchwarzThesis.pdf-68-1.png)

Figure 5.2: Simplified representation of the experimental setup. Panel (a) displays a

schematic representation of the measurement path as an input signal is reflected oof a
first cavity; transmitted through a 1.3 m delay cable; reflected oof a second cavity; and
then routed to a parametric amplifier. Panel (b) is a picture of the base-temperature setup,
showing the two copper cavities, two circulators, and the coiled delay cable.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 58

**a** **b** **c**

Q Q Q

|Col1|I|
|---|---|
|||


|Col1|I|
|---|---|
|||


|Col1|Col2|
|---|---|
|||



Figure 5.3: Schematic representation of the joint qubit measurement. Panel (a) displays the
output of a dispersive measurement at a single cavity, defining the angles  __ and __ . Panel
(b) shows the joint dispersive measurement in the general case  __ 1 =  __ 2 : all four states
_6_
are distinguishable. In Panel (c), we see that a half-parity measurement is accomplished
when  __ 1 =  __ 2 .


For a sequential reflective measurement of two qubits, the output coherent state becomes


_B_ out = _p_ __ loss _r_ 1 __


1 __ _r_ 2 __


2 __ _A_ _d_ , where __ loss represents the efficiency of power transfer between the two


cavities. In the general case,  __ 1 _6_ =  __ 2 and the phase shifts corresponding to the four basis
states _|_ _gg_ _i_ , _|_ _ge_ _i_ , _|_ _eg_ _i_ and _|_ _ee_ _i_ are all distinct (Figure 5.2.1b); the associated measurement
decoheres any quantum superposition of states and projects the system into one of the four
basis states. However, if we carefully engineer the cavities and the dispersive coupling, there
exists _!_ m such that  __ 1 =  __ 2 . In this situation, the phase shifts associated with states
_|_ _ge_ _i_ and _|_ _eg_ _i_ are identical and equal to __ 1 + __ 2 ; the measurement therefore cannot decohere
a quantum superposition of are odd eigenvalues of the parity operator  _|_ 01 _i_ and _|_ 10 _i_ (Figure 5.2.1c). Because the states __ _ZZ_ =  __ _Z_ __  _Z_ , this measurement is referred _|_ _ge_ _i_ and _|_ _eg_ _i_


1 _Z_ __  2 _Z_

__


2 _Z_ , this measurement is referred


to as a half-parity measurement. Equivalently, the odd-parity states span one of the three
eigenspaces of the half-parity operator  __ _Z_ +  __ _Z_ .


1 _Z_ +  __ 2 _Z_


2 _Z_ .


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 59

2 


- 

-2 

![SchwarzThesis.pdf-70-0.png](SchwarzThesis.pdf-70-0.png)

7.14 7.16 7.18 7.2 7.22 7.24 7.26

Frequency (GHz)


Figure 5.4: Double-reflection phase shift calculated for the four prepared states _|_ _gg_ _i_ , _|_ _ge_ _i_ ,
_|_ _eg_ _i_ , and _|_ _ee_ _i_ . The reflection curves pass through a 4 __ , indicating reflection from two

sequential cavities. The inset shows the crossing between the reflected phases for _|_ _eg_ _i_ at _!_ m = 7 _._ 19326 GHz. _|_ _ge_ _i_ and

### 5.2.2 ### Tuning the entangling measurement

How, then, do we make such a half-parity measurement? If we were able to engineer the
qubit and cavity parameters _!_ c _, ,_ and __ to be identical, the condition  __ 1 =  __ 2 would
be met automatically. However, even careful design and machining only allows us to match
these parameters within a 5-10% margin of error; we require an _in-situ_ tuning mechanism
to allow us to finely tune the cavity phase shifts. Allowing for qubit and cavity parameters
to vary between the cavity, we find


1 c _!_ m __ 1 )

__ __

c


2 c _!_ m __ 2

__ __

c


__


2 1 _i_ ( _!_ 1 c

__

1 c


__ 2


2 2 _i_ ( _!_

__

2


2 c _!_ m __ 2 )

2 c __ _!_ m __ __ 2 ) __ loss _A_ _d_ (5.2)

__ __ _p_


_B_ out =


1 c _!_ m __ 1 )

__ __ __


__


2 1 + _i_ ( _!_ 1 c


__ 2


2 2 + _i_ ( _!_ 2


We have assumed that _Q_ _int_ _Q_ _ext_ , such that we can neglect internal losses. This leads
__


to four distinct cavity resonance curves conditioned on the qubits in states and _ee_ (Figure 5.4). Solving for the frequency at which _B_ out ( _ge_ ) = _B_ out ( _eg_ ) results in a quadratic _|_ _gg_ _i_ _,_ _|_ _ge_ _i_ _,_ _|_ _eg_ _i_ _,_
_|_ _i_ m


equation in _!_ m that has real solutions if the following inequality is satisfied:


out ( _ge_ ) = _B_ out ( _eg_ )


out results in a quadratic


2 c ) 2

__


1

4




__ 1 __ 2

__ 1 __ 2


+ 1




( __ 1 __ 2 ) 2 __ 1 __ 2
__ __ __ 1 __ 2


( __ 1 __ 2 ) 2
__


( _!_


1 c _!_ 2 c

__


(5.3)


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 60


Careful manufacture of qubits and cavities enables us to match __ 1 and __ 2 within 2-3 MHz, and
__ 1 and __ 2 within several hundred kHz. As a result, this condition is fairly straightforward
to meet by adjusting the cavity frequencies such that _!_ 1 c _!_ 2 c __ . It is possible to
_|_ __ _| _


1 c _!_ 2 c

__


2 c __ . It is possible to

_| _


theoretically calculate the correct _!_ m ; in practice, we sequentially prepare the computational
states _|_ _gg_ _i_ _,_ _|_ _ge_ _i_ _,_ _|_ _eg_ _i_ _,_ and _|_ _ee_ _i_ , and adjust _!_ m until the single-shot Gaussian measurement
histograms for the _|_ _ge_ _i_ and _|_ _eg_ _i_ states completely overlap.


### 5.2.3 ### Verification of the half-parity measurement

Before studying the dynamics of the measurement-induced entanglement process, we first
would like to verify that the measurement does not distinguish between _|_ _ge_ _i_ and _|_ _eg_ _i_ . To
do so, we sequentially prepare the states _|_ _gg_ _i_ _,_ _|_ _ge_ _i_ _,_ _|_ _eg_ _i_ _,_ and _|_ _ee_ _i_
, and integrate the measurement signal for a variable time _t_ . Repeating this process several thousand time yields
measurement histograms for each of the four states (Figure 5.5). For short integration time,
the weak, continuous nature of the measurement is evident: the four histograms are all
indistinguishable from one another. As _t_ increases, the measurement Gaussians begin to
separate and we see that the measurements corresponding to _|_ _gg_ _i_ and _|_ _ee_ _i_
become distinguishable, but the _|_ _ge_ _i_ and _|_ _eg_ _i_ histograms are identical. At longer _t_ , the histograms further
separate, and we begin to see the eects of qubit decay (manifesting as the shoulder on the
_|_ _ee_ _i_ histogram). The near-perfect overlap between the _|_ _ge_ _i_ and _|_ _eg_ _i_ histograms provides
a preliminary confirmation that the measurement should be able to perform an entangling
projection.

## 5.3 ## Bayesian Theory of the Entangling Measurement

Here, we briefly describe a simplified phenomenological method of understanding and predicting the back-action of this half-parity measurement using a Bayesian approach. For a more
rigorous demonstration using equivalent stochastic master equation method, see Ref. [179]
and the supplement to Ref. [167]. As we will see in Section 5.5, despite its phenomenological nature this theory reproduces the experimental data quantitatively, with some potential
deviations at short timescales that are accounted for by the full stochastic master equation
approach.

Writing the two qubit density matrix as


__ =


__ _ij,kl_ _ij_ _kl_ _,_ (5.4)
_|_ _i h_ _|_


_ijkl_


we can estimate concurrence [107] as described in Section 3.3 using the simplified formula

[110]


_C _ max


0 _,_ __ ge _,_ eg _p_ __ gg _,_ gg __ ee _,_ ee
_|_ _| _


(5.5)


This formulation implies that for simplicity we can neglect the o-diagonal elements __ gg _,_ ge
__ gg _,_ eg , __ ee _,_ ge , __ ee _,_ eg , and __ ee _,_ gg (which should be small in the interesting regime).


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 61


400

200


1000


500

1500

1000

500


0.06 0.04 0.02 0 0.02 0.04 0.06

![SchwarzThesis.pdf-72-0.png](SchwarzThesis.pdf-72-0.png)

V m (Volts)


0.06 0.04 0.02 0 0.02 0.04 0.06


Figure 5.5: Measurement histograms for the four fiducial states, at increasing integration
times of (a) 0.010 __ s, (b) 0.650 __ s, and (c) 1.61 __ s. Solid lines represent a Gaussian fit.

To find __ gg _,_ gg , __ ee _,_ ee , and __ ge _,_ eg after the measurement, we first consider the case without

energy relaxation or intrinsic dephasing of the qubits; then the dynamics of the two-qubit
state are only due to measurement. For each of four initial fiducial states of the qubits ( _|_ _gg_ _i_ ,
_|_ _ge_ _i_ , _|_ _eg_ _i_ , _|_ _ee_ _i_ ) it is easy to calculate the evolution of the classical field amplitudes _A_ ( _t_ ) and
_B_ ( _t_ ) in the first and second resonators,


_A_  = __ 1
__ 2



1

_A_ _i_ ( _!_
2 __


1 c __ 1 _!_ m ) _A_ + __ _s,_ 1 _A_ _d_ ( _t_ ) _,_ (5.6)

__ __ _p_


_B_  = __ 2
__ 2


2 2 _B_ __ _i_ ( _!_ 2 c


2 c __ 2 _!_ m ) _B_ + __ _s,_ 2

__ __ _p_


_p_ __ loss _A_ out ( _t_ ) _,_ (5.7)


Here the rotating frame ( _e_ __ _i!_ m _t_ ) is based on the measurement drive, the time for _B_ ( _t_ )

is shifted by the flying time between resonators, and __ _i_ = __ _s,i_ + __ _w,i_ + __ _l,i_ is the total
bandwidth of the resonators including the bandwidth due to strongly ( __ _s_ ) and weakly ( __ _w_ )
coupled ports - see Fig. 5.6 - and to dissipative loss in the cavity ( __ _l_ ). The energy decay for
the microwave propagation _between_ the resonators is described by the efficiency __ loss . Notice
that in Eqs. (5.6) and (5.7) the resonator field amplitudes _A_ and _B_ are normalized such
that _|_ _A_ _|_ 2 and _|_ _B_ _|_ 2 are equal to the average number of photons in the corresponding coherent


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 62

states, while for the propagating field _A_ _d_ the squared amplitude _|_ _A_ _d_ _|_ 2 is equal to the average
number of photons per unit time.

Similar normalization is used for the propagating field

_A_ out ( _t_ ) = __ _A_ _d_ ( _t_ ) + _p_ __ _s,_ 1 _A_ ( _t_ ) _,_ (5.8)


and the field


_B_ out ( _t_ ) = __ _p_ __ loss _A_ out ( _t_ ) + _p_ __ _s,_ 2 _B_ ( _t_ ) _,_ (5.9)


which goes from the second resonator through the circulator to the amplifier. In the steadystate limit (  _A_ = 0) and for __ _s_ __ __ _w_ + __ _l_ , we recover the expression in Equation 5.1 for the


amplification coefficient, and additionally find the photon number population inside Cavity
1:



__ 1 = 2 __ _s,_ 1



c 1 m 2 _A_ _d_ 2 _._ (5.10)

1 _!_ __ 1 ) _|_ _|_

__ __


_n_  __


( __ _s,_ 1 _/_ 2) 2 + ( _!_ 1 c


To produce the entangled state in our experiment, the steady-state fields _B_ ( _ge_ )


out ( _ge_ ) and _B_ out ( _eg_ )


out


for the states _ge_ and _eg_ should be indistinguishable, _B_ out ( _ge_ )
_|_ _i_ _|_ _i_ ( _gg_ )


be sufficiently well distinguishable from the fields _B_ ( _gg_


out ( _gg_ ) and _B_ out ( _ge_


out ( _ge_ ) = _B_ out ( _eg_ )


out . For amplification and


out , while they should


homodyne measurement of the field quadrature _e_ _i_ , the average time-integrated measurement
result for the state _|_ _ij_ _i_ is


out ( _ij_ ) ( _t_ _0_ ) _e_ __ _i_

o



1
_S_ _ij_ =


Re


_B_ ( _ij_ )


_f_ _w_ ( _t_ _0_ ) _dt_ _0_ _,_ (5.11)


where _f_ _w_ ( _t_ ) is the weight function, which we take to be a constant-weight integration with
an oset to account for cavity ring-up. The amplifier noise is also accumulated during

this time-integration, so that for the two-qubit state _|_ _ij_ _i_ the random measurement result
is characterized by the Gaussian distribution with the mean value of _S_ _ij_ and the standard
deviation


__ =


2 _p_ __ meas


_f_ _w_ 2 ( _t_ ) _dt,_ (5.12)


_f_ 2


where __ meas is the quantum efficiency of the measurement setup, which includes quantum
efficiency of the phase-sensitive amplifier and losses in the circulators and cables. Notice
that the noise __ does not depend on the two-qubit state. In our experiment, the homodyne
detection phase __ = Arg _B_ ( _ge_ ) __ = Arg is chosen to be perpendicular to the output states for _B_ ( _eg_ ) . _|_ _ge_ _i_ and _|_ _eg_ _i_


_B_ ( _ge_ )


out


= Arg


_B_ ( _eg_ )


out


Because our entangling process is probabilistic and not deterministic, we must post-select

only realizations for which the integrated signal falls within a certain range, centered near
( _S_ _ge_ + _S_ _eg_ ) _/_ 2. The total probability of selection in our model (assuming no energy relaxation
of qubits) is then


_p_ ent =


__ _ij,ij_ (0) _p_ sel ( _i, j_ ) _,_ (5.13)

_i,j_


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 63

where __ (0) is the two-qubit density matrix before the measurement and _p_ sel ( _i, j_ ) is the
selection probability for the initial state _ij_ . The probability _p_ sel ( _i, j_ ) is equal to the integral,
_|_ _i_
within the selection range, of a Gaussian with mean value _S_ _ij_ and standard deviation __ , such
as those in Figure 5.5.

Since the two-qubit state evolution is only due to measurement, the diagonal matrix

elements of the final density matrix __ ( _t_ ) should obey [69] the classical Bayes rule



__ _ij,ij_ (0) _p_ sel ( _i, j_
__ ij _,_ ij ( _t_ ) =

_p_ ent


(5.14)


For the main o-diagonal matrix element __ ge _,_ eg ( _t_
) needed to calculate concurrence, the quantum Bayesian approach [69] cannot be applied rigorously; however, we can modify it phenomenologically by using the following approximation:


__ ge _,_ eg ( _t_ ) = __ ge _,_ eg (0)
_|_ _|_ _|_


__ ge _,_ ge ( _t_ ) __ eg _,_ eg ( _t_ )

__ ge _,_ ge (0) __ eg _,_ eg (0)



1
__ 2

1
__ 2

1
__


_B_ out ( _ge_ )

 __ _s,_ 1


out ( _ge_ ) ( _t_ ) _B_ out ( _ge_ )

__


__ exp

__ exp

__ exp


(1 __ meas )
__


out ( _t_ )


_dt_


_A_ ( _ge_ ) ( _t_ ) __ _A_ ( _eg_ ) ( _t_ )





2
_dt_





[(1 __ __ loss ) __ _s,_ 1 + __ _w,_ 1 + __ _l,_ 1 ]


_B_ ( _ge_ ) __ _B_ ( _eg_ ) 2 _dt_
 
 


( __ _w,_ 2 + __ _l,_ 2 )


(5.15)


where the last three factors describe the dephasing due to potential distinguishability of states
_|_ from the first and second resonators. The form of these dephasing factors directly follows from the overlap between _ge_ _i_ and _|_ _eg_ _i_ in the field _B_ out and lost fractions of the fields _A_ and _B_
two coherent states _A_ 1 and _A_ 2 in a resonator [136]: _A_ 1 _A_ 2 = exp( _A_ 1 _A_ 2 2 _/_ 2).
_|_ _i_ _|_ _i_ _|h_ _|_ _i|_ _|_ __ _|_


The remaining o-diagonal elements can also be calculated by substituting the respective


states for ( _ge_ ) and ( _eg_ ). In the analysis to follow, we will neglect these elements for two
reasons. First, the diagonal elements __ gg _,_ gg and __ ee _,_ ee go to zero as we successfully post-select
the entangled subspace, such that the first term in Eq. (5.15) goes to zero. Additionally, the


_B_ out ( _ge_




out ( _ge_ ) _B_ out ( _eg_ )

__


term in which the exponent is proportional to


out


is negligible in the odd-parity


subspace, but represents significant distinguishability between all other states. Thus, the
o-diagonal matrix terms outside the odd-parity subspace are doubly suppressed. For the
terms __ gg _,_ ge , __ gg _,_ eg , __ eg _,_ ee , __ ge _,_ ee , and their conjugates, these terms follow straightforwardly
from the single-qubit Bayesian formalism developed in Section 4.3.4. The application of this
formula to the even-parity coherence factor __ gg _,_ ee is a phenomenological extension of this
theory, just as __ ge _,_ eg is.


Only the absolute value of __ ge _,_ eg ( _t_ ) is needed to calculate the concurrence (5.5). For

completeness, the phase change of __ ge _,_ eg due to measurement can be approximately calculated


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 64

Table 5.1: Calibrated system parameters

|System Parameters|Col2|Col3|
|---|---|---|
||Qubit 1|Qubit 2|
|!q/2|4.31143 GHz|4.46143 GHz|
|!c/2|7.1864 GHz|7.1984 GHz|
|/2|18.5 MHz|21 MHz|
|/2|1.275 0.025 MHz  |1.085 0.035 MHz  |
|T 1|27 5 s |20 3 s |
|T 2|16 3 s |12 2 s |
| loss|0.81 0.05 ||
| meas|0.4 0.10 ||
|G chain|19.8 1.6 ||



using the master equation result [118]


Arg __ ge _,_ eg ( _t_ ) Arg __ ge _,_ eg (0) =
_{_ _} _ _{_ _}_


_A_ ( _ge_ ) ( _t_ ) _A_ ( _eg_ ) ( _t_ ) __


_B_ ( _ge_ ) ( _t_ ) _B_ ( _eg_ ) ( _t_ ) __


2 __ 1


Re


_dt_ __ 2 __


Re


(5.16)
_dt._


(Here we use a rotating frame with respect to bare frequencies of the qubits.)


So far we have assumed absence of intrinsic decoherence of the qubits. Pure dephasing of

the qubits with the corresponding dephasing time _T_ _',_ 1 and _T_ _',_ 2 can be easily included into the
calculation of concurrence by multiplying the main o-diagonal element __ ge _,_ eg ( _t_ ) by the factor
exp( _t/T_ _',_ 1 _t/T_ _',_ 2 ), where _t_ is the total duration of the measurement procedure. Including
__ __
the energy relaxation is not so easy, but since its contribution is quite small in the experiment,
this can be done in a very crude way. For example, instead of the energy relaxation occurring
during the measurement, we can phenomenologically introduce the energy relaxation for time
_t_ _before_ before the measurement and then for time _t_ _after_ after the measurement. A better way
can be realized by assuming energy decay at a specific random time, and then adding two
corresponding parts of the signal integration (5.11); however, we do not apply this protocol
to our data. We account for intrinsic dephasing, but not for intrinsic qubit decay.

## 5.4 ## Full Calibration of the Experimental Apparatus

Armed with a Bayesian theory for the back-action of the measurement on a cascaded pair
of qubits, we turn to a full characterization of the experimental apparatus. Section 5.3 has
providd a comprehensive list of experimental parameters that we will need to calibrate in
order to quantitatively understand the experiment. These parameters are tabulated in Table
5.1, and a full calibration methodology is provided in this section.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 65

### 5.4.1 ### Detailed experimental setup

In Figure 5.6, we show a detailed schematic of the room- and base-temperature experimental
setup. The joint measurement requires the use of two GHz microwave generators (to act as
local oscillators for qubit and readout pulses); one MHz generator (for double-pumping a
cryogenic amplifier); three DC current sources (for biasing the qubits and the amplifier); and
an arbitrary waveform generator (AWG, for shaping qubit and readout pulses). The qubits
are housed at the base stage of a Vericold cryogen-free dilution refrigerator. Input lines
contain 50-60 dB of attenuation and additional homemade lossy Eccosorb low-pass filters
at base stage to filter stray infrared radiation. The qubits and cavities are placed inside a
blackened copper can, and the cavities are themselves indium-sealed to provide additional
infrared shielding. Magnetic shielding is provided by wrapping the cavities individually with
aluminum foil and by a __ -metal outer shield that encompasses the copper can.


To implement qubit pulses, the qubits are first tuned to an operating frequency of


_!_ q


1 q _/_ 2 __ = 4 _._ 31143 GHz and _!_ 2 q


2 _/_ 2 __ = 4 _._ 46143 GHz. Qubit pulses are implemented using


single-sideband modulators (SSBs) with the output of a first generator operating at the
midpoint of the two qubit frequencies _!_ LO q _/_ 2 __ = 4 _._ 38643 GHz serving as the local oscillator


single-sideband modulators (SSBs) with the output of a first generator operating at the
midpoint of the two qubit frequencies _!_ q _/_ 2 __ = 4 _._ 38643 GHz serving as the local oscillator


(LO). The AWG provides intermediate frequency (IF) pulses at 75 MHz to a lower-sideband
SSB (Qubit 1) and an upper-sideband SSB (Qubit 2); these pulses are routed to base and
perform single qubit gates via the weakly-coupled ports of the respective cavities.

A second generator operating at the measurement frequency _!_ m _/_ 2 __ = 7 _._ 19326 GHz

is split three ways. The joint measurement readout pulses are implemented via a mixer
using _!_ m as the LO and DC pulses from the AWG as the IF. The output of the mixer
passes through a variable phase shift and attenuation and into the dilution refrigerator. At
base, the readout passes through a circulator to measure cavity 1 in reflection; is routed back
through the circulator and through 1.3 meters of copper cable; measures cavity 2 in reflection
via a second circulator; and is routed via an additional isolator to a lumped Josephson
parametric amplifier (LJPA) [141] for phase-sensitive amplification. We double-pump the
LJPA symmetrically at _!_ m __ _!_ _dp_ to reduce pump leakage at _!_ m that could propagate toward
the cavities and cause additional unwanted dephasing. The double pump for the LJPA is
generated via an IQ mixer with a third generator operating at _!_ _dp_ _/_ 2 __ = 369 MHz on the I
port and _!_ m as the LO. After the LJPA, the amplified readout passes through two isolators
and a low-pass filter en route to a 4K HEMT; at room temperature, the signal is further
amplified before demodulation (using the third branch of _!_ m as the LO) and digitization for
processing.

### 5.4.2 ### Cavity parameters

The bare cavity frequencies are measured using a standard transmission measurement performed with a vector network analyzer. A probe tone is injected via _!_ c and linewidths __
the weakly-coupled port and collected at the output of the total measurement chain; the
transmission spectrum has a characteristic Lorentzian shape, which we fit to extract the


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 66

 q  RO

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|||-20dB -20dB||-20dB||HE|
|||-10dB|-10dB|-10dB|-10dB||
|||-10dB -10dB||-10dB|||
|-10dB|||-10dB||-10dB||


Figure 5.6: Full experimental setup.




LO

RF


LO

RF


AWG


LO

RF


LO

RF


LO

RF


IF






HEMT


4K

1K


100mK

20mK

(x2)


LJPA


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 67


cavity parameters. Note that, since there is no qubit drives and the qubits are quite cold,
we are actually measuring _!_ c , the dressed cavity frequency conditioned on the qubit in state



c , the dressed cavity frequency conditioned on the qubit in state

__


_|_ _g_ _i_ . Upon an accurate measurement of __ , we can adjust our estimate of the bare resonant
frequency.


### 5.4.3 ### Qubit lifetimes and coherences


We calibrate _T_ 1 , the qubit relaxation time, and _T_ 2 __


2 __ , the Ramsey decay time, using standard


time-resolved measurements. Specifically, _T_ 1 is calibrated by performing a _R_ __


_X_ __ rotation


into the _|_ _e_ _i_ state, waiting a variable delay time, performing a strong readout measurement,
and fitting the resulting data to a decaying exponential. _T_ 2 __ is calibrated using a Ramsey


2 __ is calibrated using a Ramsey


sequence that measures the total loss rate of azimuthal phase coherence. We extract _T_ _'_ , the
pure dephasing rate, from _T_ 2 __ using _T_ 1 2 __ = _T_ 1 _'_ + 2 _T_ 1 1 .


2 __ using


_T_ 2



=
2 __


_T_ 1 _'_ +


1

2 _T_ 1


### 5.4.4 ### Calibration of photon number, dispersive shifts, and inter-cavity transmission efficiency

We would like to be able to translate from a calibrated room-temperature measurement power
_P_ _m_ into an equivalent photon number present in the cavities. For this, the qubits themselves
provide a highly sensitive meter, allowing us to simultaneously calibrate the photon number
( _n_ 1 ), the dispersive shifts at each cavity ( __ ), and the inter-cavity transmission efficiency
( __ meas ). To calibrate these system parameters, we use a technique similar to Vijay _et al._ [175].
The additional _P_ _m_ (calibrated at room-temperature with a spectrum analyzer) corresponds
to a coherent state in the first cavity given by


_p_ _P_ _m_ __


_A_ =
__


__ 1 _/_ 2 + _i_ ( _!_ 1 c


1 c _!_ m __ 1 ) _,_ (5.17)

__ __


where __
represents an unknown (but constant at fixed frequency) attenuation from roomtemperature to the cavity. All variables but __ 1 and __ have been independently calibrated.
Similarly, because Qubit 1 stays in its ground state when undriven, if we do not drive Qubit
1 we can write the intracavity field at Cavity 2 as


_p_ __ loss _P_ _m_ __ 2


2 c _m_ _!_ m 2 __ 2 ) _e_ __ _i_  __ 1 _._ (5.18)

__ __


_B_ =
__


__ 2 _/_ 2 + _i_ ( _!_ c


This is the equivalent of Equation 5.17, with the addition of an attenuation _p_ __ loss and an
overall phase shift due to the presence first cavity.


The intracavity coherent state _A_ creates a measurement-induced dephasing rate given by


 _d,_ 1 = __ 1


2 1 _|_ _A_ + __ _A_ __ _|_ 2 and an ac-Stark shift of  _!_ = __ 2 __ Re


_A_ _A_ __
__



[118]. An equivalent


eect occurs at Qubit 2 due to _B_ . We can measure both  _d_ and  _!_ by performing Ramsey
measurements in the presence of the oset power _P_ _m_ . The frequency of the Ramsey fringes
gives  _!_ , and their exponential decay envelope gives  tot =  _d_ + 1 _/T_ 2 __ .


2 __ .


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 68

**Qubit 1** **Qubit 2**


![SchwarzThesis.pdf-79-0.png](SchwarzThesis.pdf-79-0.png)

![SchwarzThesis.pdf-79-1.png](SchwarzThesis.pdf-79-1.png)

10

20

30

40


![SchwarzThesis.pdf-79-2.png](SchwarzThesis.pdf-79-2.png)

![SchwarzThesis.pdf-79-3.png](SchwarzThesis.pdf-79-3.png)

50

![SchwarzThesis.pdf-79-5.png](SchwarzThesis.pdf-79-5.png)
0 2 4 6 8 10 12

Input Power (a.u.)


10

20

30

40

![SchwarzThesis.pdf-79-4.png](SchwarzThesis.pdf-79-4.png)
0 2 4 6 8 10 12

Input Power (a.u.)


Figure 5.7: _n_ , __ loss , and __ calibration. We display the measurement-induced dephasing (a-b)
and ac-Stark shift (c-d) for Qubit 1 (left) and Qubit 2 (right) as a function of measurement
power _P_ _m_ in arbitrary units. We fit these data in order to determine __ 1 _, _ 2 _, _ loss _,_ and _n_ 1 .

We sweep the applied power _P_ _m_ and perform Ramsey measurements first on Qubit 1 and


then on Qubit 2, in order to generate a linear fit of both  _d_ vs. _P_ _m_ and  _!_ vs. _P_ _m_ for
both qubits independently. Removing the _P_ _m_ = 0 oset and taking the ratio  _!_ _/_  _d_ removes
dependency on _P_ _m_ (Qubit 1) and __ loss _P_ _m_ (Qubit 2); we fit these ratios to a constant from
which we extract __ 1 and __ 2 . We then use these values of __ in linear fits of  _!_ ( _P_ _m_ ) and
 _d_ ( _P_ _m_ ); this provides two independent fits for __ (when we measure Ramsey on Qubit 1) and
for __ loss (when we subsequently measure Ramsey on Qubit 2). In Figure 5.7, we show these
fits for both qubits. The calibration of __ also provides a sensitive photon-number calibration
as a function of _P_ _m_ : once __ 1 and __ have been determined, _n_ __ 1 = _A_ __ 2 is fully determined,



__ 1 = _A_ __ 2 is fully determined,

_|_ _|_


as is the drive amplitude _m_ _A_ _d_ 1 = _p_ _P_ _m_ .


### 5.4.5 ### Calibration of ###  ### meas


The final remaining parameter is the measurement efficiency __ meas . In addition, there is an
implicit parameter to calibrate, which we will call _G_ chain . _G_ chain links the amplified, digitized
measurement voltage _V_ _m_ ( _t_ ) as measured in our physical system, and _B_ out as defined in Section
5.3. _G_ chain is thus the slope of the line _V_ _m_ ( _ee_ ) _V_ _m_ ( _gg_ ) vs. _S_ _ee_ _S_ _gg_ , where _V_ _m_ ( _ij_ ) is the center


_V_ _m_ ( _gg_
__


vs. _S_ _ee_ _S_ _gg_ , where _V_ _m_ ( _ij_
__


is the center


of the histogram actually measured with the digitizer (as in Figure 5.5), and _S_ _ij_ is defined
in Equation 5.11. Once _G_ chain is determined, we fit the histograms corresponding to the
prepared state _|_ _gg_ _i_ , _|_ _ge_ _i_ , _|_ _eg_ _i_ , and _|_ _ee_ _i_ to Gaussian distributions for every measurement time
_t_ . The amplification efficiency __ meas is linked to the standard deviation of these Gaussians via
1 _/_ = 2 _p_ __ meas _t_ (Equation 5.12). We extract __ meas by fitting __ vs 1 _/_ _p_ _t_ to a line (Figure 5.8).


_t_ to a line (Figure 5.8).


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 69


20

40

![SchwarzThesis.pdf-80-0.png](SchwarzThesis.pdf-80-0.png)

60

80

![SchwarzThesis.pdf-80-1.png](SchwarzThesis.pdf-80-1.png)

100

120


2.5


1.5


![SchwarzThesis.pdf-80-2.png](SchwarzThesis.pdf-80-2.png)

![SchwarzThesis.pdf-80-3.png](SchwarzThesis.pdf-80-3.png)

6 4 2


0.5

0.5 1 1.5 2 2.5 3 3.5


Figure 5.8: Calibration of __ meas and _G_ chain . a. Center of the measured histograms as a
function of prediction given by the Bayesian theory. We plot the dierence between _|_ _gg_ _i_
and _|_ _ee_ _i_ to remove possible osets. b. Evolution of the standard deviation of the histogram
corresponding to prepared state _|_ _eg_ _i_ versus measurement time _t_ .

We define __ meas as the mean of the extracted values from the four fiducial states.

## 5.5 ## Tomographic Reconstruction of Entanglement Dynamics

With a preliminary confirmation of a half-parity measurement and a fully-calibrated experimental apparatus, we would now like to be quantitative about the quality and dynamics of
the entangling process. We control the rate of entanglement generation


 meas = 1 __ meas __ loss _A_ _d_ 2 sin(2 __ ) 2 _,_ (5.19)

2 _|_ _|_

by adjusting the measurement strength via the average intracavity photon number in the
first cavity (Equation 5.10). A photon number _n_ 1 = 1 _._ 2 results in  meas _/_ 2 __ __ 210 kHz,
which sets the characteristic timescale of entanglement generation __ meas 1 _/_  meas 750 ns.
__ __
Thus, the dynamics of the measurement process, which are significantly faster than qubit
decay rates, can be readily resolved using conventional digital electronics. We therefore


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 70

![SchwarzThesis.pdf-81-0.png](SchwarzThesis.pdf-81-0.png)

Figure 5.9: Sequence of measurement and rotation pulses required for entanglement and
tomographic state reconstruction. Pulses at the qubit frequency are shown in green; pulses
at the cavity frequency are in purple (with pulse strength indicated schematically via color
intensity).

use _n_ 1 = 1 _._ 2 for our weak measurements. In contrast, our projective readout is performed
with _n_ 1 = 6 _._ 2 photons, corresponding to  meas _/_ 2 __ __ 5 _._ 6 MHz, or __ meas = 28 ns. __ meas is
significantly faster than intrinsic qubit decay timescales in this regime, which fulfills our need
for a fast, high-fidelity readout.

A reader might well inquire as to the dierence between strong and weak measure-

ment. Indeed, the strong and weak measurements used here lie on the same continuum and
can be tuned at will. The terms, therefore, are a descriptive and relative shorthand (and
a relatively sloppy one) for comparison of measurement rates within an experiment such
as this one. We might interchange strong with projective, but again, the ability of a
measurement to fully project a system is also relative. The strong measurements used
here are measurement for which we are not interested in reconstructing the underlying dynamics or for which the dynamics are too fast to be captured by our electronics; the weak
measurements are those for which we wish to and are able to study the dynamical processes.

To generate and verify entanglement, we implement a sequence of three readout protocols


and two qubit rotations (Figure 5.9). We first perform a projective readout and post-select
the _gg_ ground state [180]. We then perform _R_ _Y_ _/_ 2 rotations on both qubits to create the
_|_ _i_ 1


equal superposition state 1


rotations on both qubits to create the



1 2 ( _gg_ + _ge_ + _eg_ + _ee_ ). The second readout, which is done in

_|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_


the weak regime with varying state 1 ( _ge_ + _eg_ ), as documented in the measurement output _t_ , stochastically steers the system toward _V_ _m_ . We then apply one of _|_ _gg_ _i_ , _|_ _ee_ _i_ , or the Bell



( _ge_ + _eg_ ), as documented in the measurement output _V_ _m_ . We then apply one of
2

_|_ _i_ _|_ _i_


a set of tomographic rotations [181] immediately followed by a final projective readout into
_|_ _gg_ _i_ , _|_ _ee_ _i_ , or _{|_ _ge_ _i_ _,_ _|_ _eg_ _i}_ . The tomography is described in greater detail in the next section.


The tomographic and state preparatory rotations are tuned to 40 ns, and we provide a


10 ns window between the end of a qubit pulse and the beginning of a readout protocol in
order to ensure that the rotations are not distorted by photon-induced qubit frequency shifts.
Similarly, after a readout is performed, we wait a minimum of _t_ = 6 _/_ 2 __ before applying a
qubit pulse in order to ensure the cavity is fully depopulated.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 71

We repeat the entangling process 8,000 times for each tomographic rotation and for each

_t_ to form a single well-averaged data set; we generate an error margin by taking the average
and standard deviation of 17 data sets. To produce the density matrix of the entangled
state for each time _t_ , we choose an entanglement probability _p_ ent to constitute the entangled
state, select an integration window to contain the _p_ ent most-likely-entangled experimental
iterations, and tomographically reconstruct the density matrix from the data set contained
in this window using a maximum-likelihood estimator [167, 182]. For perfectly separated
histograms, 50% of the counts will lie in the odd-parity subspace, but we utilize _p_ ent = 10%
to compensate for imperfect measurement efficiency.

### 5.5.1 ### Characterizing the tomographic reconstruction

The joint dispersive measurement that we have designed randomly projects the system into
_|_ _gg_ _i_ , _|_ _ee_ _i_ , or _{|_ _ge_ _i_ _,_ _|_ _eg_ _i}_
. Repetitively performing the measurement on an identically prepared ensemble therefore yields the probabilities _p_ _gg_ , _p_ _ee_ , and _p_ _ge_ + _p_ _eg_
_|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_
. These probabilities, in turn, represent the diagonal density matrix elements __ gg _,_ gg , __ ee _,_ ee , and __ ge _,_ ge + __ eg _,_ eg .
The tomographic process utilizes our ability to measure a subset of these density matrix elements and to rotate other matrix elements into these readable slots in order to reconstruct
the full density matrix.

To reconstruct the density matrix, we need at least fifteen linearly independent mea-

surements in order to span the degrees of freedom of the two-qubit density matrix (a 4x4
Hermitian matrix, with a trace-normalization constraint). These degrees of freedom can
alternatively be considered as projections of the density matrix onto the two-qubit Pauli
operators  __ _ij_ . However, one can easily see that the only Pauli operators with nonzero di-


agonal density matrix elements are __  _II_ _,_  __ _IZ_ _,_  __ _ZI_ _,_  __ _ZZ_ . Measuring _p_ _gg_ is the equivalent
_{_ _}_ _|_ _i_


of measuring Tr


 _gg_ __
_M_


, where _M_  _gg_ =  __ _II_ +  __ _IZ_ +  __ _ZI_ +  __ _ZZ_ . We can write a similar


measurement operator for a measurement of _|_ _ee_ _i_ : _M_  _ee_ =  __ _II_ __ __  _IZ_ __ __  _ZI_ +  __ _ZZ_ . Similar


decompositions can be written for _p_ _|_ _ge_ _i_ and _p_ _|_ _eg_ _i_
. However, because we cannot use our measurement to distinguish between _|_ _ge_ _i_ and _|_ _eg_ _i_ in this experiment, we will use only the _|_ _gg_ _i_
and _|_ _ee_ _i_ proobabilities for tomographic purposes.


In order for our measurements to span the full Hilbert space, we must design a set of


rotations that take the remainder of the Pauli matrix projections


__  _IY_ _,_  __ _XZ_ _,_ etc.


into one


of these four measurable positions. Thus we can build up a set of measurement operators
that, taken together, can determine the full Pauli matrix decomposition of the system and
thus reconstruct the density matrix. Of course, since we are discussing probabilities, we
must prepare the system and perform each rotation and measurement many times in order
to build an accurate estimate of the probabilities, and thus a true picture of the ensemble
density matrix.

Our tomography procedure utilizes a set of 30 qubit rotations (15 positive and negative

rotations) in order to reduce systematic bias from qubit rotations and power drifts. The
rotations are identical to those in Ref. [181] and are given explicitly in Table 5.2. For


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 72


each rotation, we independently measure _p_ _gg_ and _p_ _ee_ in order to double the amount of
_|_ _i_ _|_ _i_
information we extract from each experiment. These probabilities represent measurements
of the form


_p_ _ij_ = Tr  _ij_ __ ;
_|_ _i_ _{_ _M_ _|_ _i_ _}_


(5.20)


 _ij_ = __ _II_ __  _II_ __ _IZ_ __  _Im_ __ _ZI_ __  _nI_ __ _ZZ_ __  _nm_ _._
_M_ _|_ _i_ __ __ __


Here +( __ ) corresponds to _p_ _|_ _gg_


_p_ _|_ _ee_ _i_


, and _m, n_ _2 {_ _X, Y, Z_ _}_ . The choice of _m, n_ depends on


the prerotation performed before the measurement. The __ -coefficients are calibrated using
a double-Rabi measurement as described in Chow _et al._ [181] and allow us to account for
measurement inefficiency and qubit decay during readout.


Our measurement set results in an overspecified measurement set: 60 eective mea-

surements for 15 degrees of freedom. We convert this data into a density matrix using

a least-squares maximum likelihood estimation method [182] to enforce trace normalization
and Hermiticity of the reconstructed density matrix. Specifically, we define a sixteen element
real vector _~_ **t** and use its elements to construct a lower-triangular matrix of the form

_t_ 1 0 0 0


_T_ =


_t_ 5 + _it_ 6 _t_ 2 0

_t_ 7 + _it_ 8 _t_ 9 + _t_ 10 _t_ 3


(5.21)


_t_ 11 + _it_ 12 _t_ 13 + _it_ 14 _t_ 15 + _it_ 16 _t_ 4


and write


_T_ __ _T_
__ _t_ =


(5.22)
Tr _{_ _T_ __ _T_ _}_


As long as _T_ is invertible, __ _t_
is semipositive definite, and is therefore a Hermitian, tracenormalized density matrix. This is the constraint we seek. We then construct a minimization
vector **L** _~_ where each element is given by


_ij_ _,k_ = Tr  _ij_ _,k_ __ _t_ _p_ _ij_ _,k_ _._ (5.23)
_L_ _|_ _i_ _{_ _M_ _|_ _i_ _} _ _|_ _i_

Here, _k_ indexes the prerotations that are performed to complete the tomographic set.The
vector **L** _~_ represents a comparison of the expected measurement outcome for the test matrix __ _t_


under measurement  _k_ , to the experimentally measured outcomes (with a separate vector
_M_


element for the _|_ _gg_ _i_ and _|_ _ee_ _i_ measurements, which we consider independent). Using a


nonlinear least-squares minimization protocol (in our case, the lsqnonlin function native to
the MATLAB environment), we vary _~_ **t** until **L** _~_ is minimized, and consider the corresponding


__ _t_ to represent the true density matrix __ .

One could also consider using standard matrix methods to construct a matrix of mea-


surement operators and a corresponding vector of outcomes, then taking the pseudoinverse
in order to reconstruct the density matrix. These methods produce qualitatively similar
results. The data shown in this dissertation are based on the maximum likelihood method.


We verify the accuracy of the tomography by preparing the state _|_ _g_ _i_ _p_ + 2 _|_ _e_



_||_ _g_ _i_ + _e_ _i_ _|_ _e_ _i_
_p_ 2
__


and


calculating the fidelity of the resulting density matrix to the target state (Figure 5.10).
The average fidelity across the prepared states is 98.8%, indicating highly eective state
initialization and tomographic reconstruction.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 73

Table 5.2: Tomographic rotations and measurement operators



|Col1|Rotation |ggi Measurement Operator |eei Measurement Operator|Col3|Col4|
|---|---|---|---|
|P 1 P 2 P 3 P 4 P 5 P 6 P 7 P 8 P 9 P 10 P 11 P 12 P 13 P 14 P 15|I  I R X  I I  R X R X/2  I R X/2  R X/2 R X/2  R Y/2 R X/2  R X R Y/2  I R Y/2  R X/2 R Y/2  R Y/2 R Y/2  R X I  R X/2 R X  R X/2 I  R Y/2 R X  R Y/2|+ II +  ZI +  IZ +  ZZ II ZI IZ ZZ + II  ZI +  IZ  ZZ II ZI IZ ZZ + II +  ZI  IZ  ZZ II ZI IZ ZZ + II +  Y I +  IZ +  Y Z II ZI IZ ZZ + II +  Y I +  IY +  Y Y II ZI IZ ZZ + II +  Y I  IX  Y X II ZI IZ ZZ + II +  Y I  IZ  Y Z II ZI IZ ZZ + II  XI +  IZ  XZ II ZI IZ ZZ + II  XI +  IY  XY II ZI IZ ZZ + II  XI  IX +  XX II ZI IZ ZZ + II  XI  IZ +  XZ II ZI IZ ZZ + II +  ZI +  IY +  ZY II ZI IZ ZZ + II  ZI +  IY  ZY II ZI IZ ZZ + II +  ZI  IX  ZX II ZI IZ ZZ + II  ZI  IX +  ZX II ZI IZ ZZ|+ II  ZI  IZ +  ZZ II ZI IZ ZZ + II +  ZI  IZ  ZZ II ZI IZ ZZ + II  ZI +  IZ  ZZ II ZI IZ ZZ + II  Y I  IZ +  Y Z II ZI IZ ZZ + II  Y I  IY +  Y Y II ZI IZ ZZ + II  Y I +  IX  Y X II ZI IZ ZZ + II  Y I +  IZ  Y Z II ZI IZ ZZ + II +  XI  IZ  XZ II ZI IZ ZZ + II +  XI  IY  XY II ZI IZ ZZ + II +  XI +  IX +  XX II ZI IZ ZZ + II +  XI +  IZ +  XZ II ZI IZ ZZ + II  ZI  IY +  ZY II ZI IZ ZZ + II +  ZI  IY  ZY II ZI IZ ZZ + II  ZI +  IX  ZX II ZI IZ ZZ + II +  ZI +  IX +  ZX II ZI IZ ZZ|
|N 1 N 2 N 3 N 4 N 5 N 6 N 7 N 8 N 9 N 10 N 11 N 12 N 13 N 14 N 15|I  I R X  I I  R X R X/2  I R X/2  R X/2 R X/2  R Y/2 R X/2  R X R Y/2  I R Y/2  R X/2 R Y/2  R Y/2 R Y/2  R X I  R X/2 R X  R X/2 I  R Y/2 R X  R Y/2|+ II +  ZI +  IZ +  ZZ II ZI IZ ZZ + II  ZI +  IZ  ZZ II ZI IZ ZZ + II +  ZI  IZ  ZZ II ZI IZ ZZ + II  Y I +  IZ  Y Z II ZI IZ ZZ + II  Y I  IY +  Y Y II ZI IZ ZZ + II  Y I +  IX  Y X II ZI IZ ZZ + II  Y I  IZ +  Y Z II ZI IZ ZZ + II +  XI +  IZ +  XZ II ZI IZ ZZ + II +  XI  IY  XY II ZI IZ ZZ + II +  XI +  IX +  XX II ZI IZ ZZ + II +  XI  IZ  XZ II ZI IZ ZZ + II +  ZI  IY  ZY II ZI IZ ZZ + II  ZI  IY +  ZY II ZI IZ ZZ + II +  ZI +  IX +  ZX II ZI IZ ZZ + II  ZI +  IX  ZX II ZI IZ ZZ|+ II  ZI  IZ +  ZZ II ZI IZ ZZ + II +  ZI  IZ  ZZ II ZI IZ ZZ + II  ZI +  IZ  ZZ II ZI IZ ZZ + II +  Y I  IZ  Y Z II ZI IZ ZZ + II +  Y I +  IY +  Y Y II ZI IZ ZZ + II +  Y I  IX  Y X II ZI IZ ZZ + II +  Y I +  IZ +  Y Z II ZI IZ ZZ + II  XI  IZ +  XZ II ZI IZ ZZ + II  XI +  IY  XY II ZI IZ ZZ + II  XI  IX +  XX II ZI IZ ZZ + II  XI +  IZ  XZ II ZI IZ ZZ + II  ZI +  IY  ZY II ZI IZ ZZ + II +  ZI +  IY +  ZY II ZI IZ ZZ + II  ZI  IX +  ZX II ZI IZ ZZ + II +  ZI  IX  ZX II ZI IZ ZZ|


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 74

1

0.9

0.8


0.7

0.6

0.5

0.4

0.3

0.2

0.1


![SchwarzThesis.pdf-85-0.png](SchwarzThesis.pdf-85-0.png)

50 100 150 200 250 300 350 400 450

Preparation Phase


50 100 150 200 250 300 350 400 450


Figure 5.10: Fidelity to the states _|_ _g_ _i_ _p_ + 2 _|_ _e_ _i_



_|_ _g_ _i_ + _|_ _e_ _i_
_p_ 2
__


(XX), _|_ _g_ _i_ _p_ + 2 _|_ _e_



_|_ _g_ _i_ + _i_ _|_ _e_ _i_
_p_ 2
__


(XY) and _|_ _g_ _i_ _p_ + 2 _|_ _e_ _i_


_|_ _g_ _i_ + _e_ _i_ _|_ _e_


(Target State) as a function of Qubit 2 preparation phase __ . Fidelities to XX


and XY oscillate 90 degrees out of phase with one another, as expected; the fidelity to the
prepared state is an average of 98.8% across all preparation angles.

### 5.5.2 ### Entanglement dynamics

The ability to perform time-continuous measurements enables us to directly observe the
ensemble dynamics of the emergence of entanglement. As noted in Section 5.3, we can

estimate concurrence [107] using the simplified formula [110] (Equation 5.5) to characterize
the quality of the entanglement during this process. This simplified formula holds when the
only non-negligible o-diagonal elements are __ ge _,_ eg and its conjugate, which is applicable to
our setup since the high distinguishability between _|_ _gg_ _i_ _,_ _|_ _ee_ _i_ and the _{|_ _ge_ _i_ _,_ _|_ _eg_ _i}_ manifold
results in rapid decay of all other o-diagonal elements. Recall that concurrence ranges from
zero (for a separable or mixed state) to one (for a maximally entangled two qubit state),
and is greater than zero for all non-separable two qubit states [107]. Maximizing _C_ requires
limiting decoherence within the odd-parity manifold, and minimizing stray counts of _|_ _gg_ _i_
and _|_ _ee_ _i_ by maximizing the signal-to noise ratio (SNR), defined by the ratio of the separation
of the Gaussian measurement histograms (in Figure 5.5) to their width, or

SNR 2 _A_ _d_ sin (2 __ ) _p_ __ loss __ meas _t._ (5.24)
__ _|_ _|_


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 75


0.5

0.4

0.3

0.2

0.1


![SchwarzThesis.pdf-86-0.png](SchwarzThesis.pdf-86-0.png)

0.4 0.8 1.2 1.6

### t ### (s)
m


0.4 0.8 1.2 1.6


Figure 5.11: Generation and verification of entanglement between two spatially-separated
superconducting qubits. The figure displays the evolution of the basis state populations
( __ gg _,_ gg , etc.) and odd-parity coherence ( __ ge _,_ eg ). The shaded region represents the standard
deviation centered about the average (geometric shapes). Dashed lines are theoretical simulations based on a Bayesian approach and solid lines are calculated using a master equation
approach; in both cases no fitting parameters are used.

Figures 5.11 and 5.12 show the evolution of the density matrix as a function of . Figure 5.11 details the evolution of the relevant density matrix elements (the diagonal elements, _t_
representing population probabilities, and the o-diagonal element __ ge _,_ eg , representing the
coherence of the odd-parity subspace), as the entangled ensemble is better and better postselected. Figure 5.12 shows the full density matrix for five selected values of _t_ . As expected,
the o-diagonal elements not associated with the odd-parity subspace rapidly decay to zero.
Note that we plot here the amplitude of the density matrix elements, when in fact the odiagonal elements are in general complex. In particular, the o-diagonal density matrix

element evolves deterministically due to the slight dierences in __ between the two qubits
(Equation 5.16). However, note that Equation 5.5 refers only to the amplitude __ ge _,_ eg , and
_|_ _|_
not to its complex phase. Therefore, the amplitudes contain all the information we need to
study entanglement. In Figure 5.13, we show the concurrence calculated from these density
matrices as a function of measurement integration time.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 76

t m =0.01 s t m =0.25 s t m =0.65 s t m =1.13 s t m =1.61 s


0.4
0.2


0.4
0.2

0


0.4
0.2


0.4
0.2


0.4
0.2


gg gg










gg

|ge eg|eg ge|
|---|---|

|ge eg|eg e ge|
|---|---|

|ge eg|eg ge|
|---|---|

|ge eg ee|eg ge|
|---|---|

|ge eg|eg ge|
|---|---|


Figure 5.12: Full density matrices of the post-selected entangled subspace for increasing _t_ .
The o-diagonal elements corresponding to coherences outside of the odd-parity subspace
decay much more rapidly than __ ge _,_ eg
, as required for entanglement generation. The odiagonal elements outside the entangled subspace can be calculated phenomenologically using _|_ _|_
the Bayesian formalism, and from first-principles using the SME formalism [179].

0.4


0.3

0.2

0.1

|SNR-Limited|Optimum|Losses-Limited|
|---|---|---|


improvement and losses; and a region of decay where the dynamics are dominated by loss

![SchwarzThesis.pdf-87-0.png](SchwarzThesis.pdf-87-0.png)
mechanisms.


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 77

## 5.6 ## Discussion of Results


In describing the evolution of the density matrix elements and overall concurrences in Figures 5.11, 5.12, and 5.13, we note three qualitative regimes: SNR-dominated evolution;
stabilization; and decay due to decoherence. Since the SNR for integrated gaussian noise
is proportional to _p_ _t_ , it dominates the evolution at short times _t <_ 0 _._ 75 __ meas . Here, the


dynamics are governed by changes to population probabilities; i.e., the increase of __ eg _,_ eg and
__ ge _,_ ge and decrease of __ gg _,_ gg and __ ee _,_ ee in the post-selected ensemble. The rapid decay of __ gg _,_ gg
and __ ee _,_ ee compared to __ ge _,_ eg
, results in growth of concurrence in this regime. For intermediate times (0 _._ 75 __ meas _< t <_ 1 _._ 25 __ meas ), the SNR improvement rate decreases and decoherence
begins to take a more noticeable eect. Decoherence is caused by intrinsic dephasing of
the qubits  __ = 1 _/T_ and by __ loss , which contributes an additional measurement-induced



__ 2 _,i_ = 1 _/T_ __ 2


2 _,i_ and by __ loss , which contributes an additional measurement-induced


dephasing of the first qubit at a rate


 loss 2 (1 __ loss ) _A_ _d_ 2 sin( __ ) 2 _._ (5.25)
_'_ __ _|_ _|_

At intermediate times, the SNR improvement rate and  loss are roughly equal, and hence


the concurrence reaches a maximum value of 0.35. This value is comparable to what was
obtained recently using optical communications [164, 165], however, thanks to our timecontinuous measurement scheme, the rate at which an entangled state is created is orders
of magnitude higher ( creation _/_ 2 __ = 1 kHz). For longer times ( _t >_ 1 _._ 25 __ meas ), the density
matrix evolution is dominated by decoherence, which eventually drives the system into an
incoherent mixture of _|_ _ge_ _i_ and _|_ _eg_ _i_ .

These ensemble dynamics are well-described both by a Bayesian statistical model (dashed

lines), and by a rigorous stochastic master-equation treatment (solid lines) [179]. The models,
which account for the chief technical limitations of our scheme (i.e. the inefficiencies __ loss , the
losses between the cavities and __ meas , the finite detection efficiency), indicate that reasonable
technical improvements could lead to concurrence of 70% [167, 179]. The two theories

used to model our data represent a rigorous microscopic analysis that natively accounts for
all density matrix elements, in the case of the stochastic master equation formalism; and
a straightforward phenomenological extension of the single-qubit Bayesian theory, in the
case of the Bayesian formalism. The agreement between these models indicates a thorough
understanding of the experimental system that enables our entangling measurement.

This work beautifully demonstrates the delicate interplay between measurement and


dissipation. Without performing an entangling measurement, there is no direct means of
entangling the qubits in our system, so the measurement serves to purify, rather than destroy, an important quantum resource. However, that purification is impeded by two loss
mechanisms, __ loss and __ meas , which aect the measurement dynamics in very dierent ways.
The additional dephasing of the first qubit, and therefore of the entangled state, is principally caused by losses between the two cavities ( __ loss ). Along the path between the cavities,
the propagating coherent state only carries information about the state of the first qubit.
In the language of SMEs developed in Chapter 2, this is a dissipation term takes the form


 loss

2

_D_


__  _ZI_




 loss


__ , a dephasing term on the Qubit 1 subspace. Any information lost between the


-----


_CHAPTER 5. REMOTE MEASUREMENT-INDUCED ENTANGLEMENT_ 78

cavities - particularly at the circulators, which contribute an intrinsic loss of nearly 0.4 dB
each - is equivalently a measurement of the first qubit that we must average over, which
contributes to an eective measurement-induced dephasing.


However, after the second cavity, the signal no longer contains information that distin-


__  _ZI_ +  __ _IZ_




guishes between _ge_ and _eg_ : the dissipator being applied is of form  meas
_|_ _i_ _|_ _i_ _D_


__ .


In the odd-parity subspace, this term has an expectation value of zero, so the odd-parity
subspace is protected from further decoherence due to inefficient transmission to and amplification by the LJPA (captured in __ meas ). Thus, this second form of loss serves only to
limit the rate at which entanglement is generated by slowing the rate of SNR improvement,
but does not itself contribute to decoherence. The overall dynamics of the entanglement
generation process are governed by an interplay between measurement, dissipation-induced
dephasing and collection efficiency, nicely capturing all of the relevant dynamics in a measurement/dissipation process.


Our experiments demonstrate that quantum entanglement can be established between

distant systems that interact only through a coherent signal propagating along low loss electrical wires, a functionality that will be integral to the realization of complex, distributed
quantum networks. We take advantage of the versatility of continuous measurement to monitor the dynamics of entanglement generation, and demonstrate quantitative agreement to a
theoretical model that captures the experimental details of the physical circuit. Moreover,
our characterization of the state of the joint system under continuous measurement suggests
the feasibility of future _continuous_ feedback stabilization of entanglement [171, 177, 183].
Further technical improvements in quantum efficiency, coherence times, and transmission
characteristics hold the promise of on-demand, stabilized remote entanglementa powerful
resource for quantum information processing.


-----


79

# Chapter 6

 Quantum Trajectories in an Entangling Measurement

A careful analysis of the process of observation in atomic physics
has shown that the subatomic particles have no meaning as isolated
entities, but can only be understood as interconnections between the
preparation of an experiment and the subsequent measurement.

Erwin Schr odinger, _Unsourced Attribution_

Our high-efficiency continuous measurement allows us to go one step further in decom-

posing the dynamics of measurement-induced entanglement: we can directly observe the
individual quantum trajectories [176, 184187] of our two qubit system. The ability to reconstruct individual quantum trajectories is a tremendous advantage of weak measurements:
we can ask not only Where did the qubits start? (state initialization) and Where did
they end? (projective readout) but also How did they get there?. By peering into the
ensemble to resolve the _single-shot_ , dynamical evolution of a quantum system, we gain access
to a rich new tapestry of scientific questions:

1. What is the complete characterization of the dynamics of entanglement creation as a

continuous trajectory?

2. What is the statistical distribution of the entanglement at any time during the process?

3. What is the most likely way in which entanglement is created?

In this chapter, we give a systematic answer to these questions and more, by analyzing en-

tangled quantum trajectories of jointly measured qubits and by developing a comprehensive
theory to understand them. We resolve and describe the full spectrum of evolution paths as
the two-qubit state gradually projects onto the entangled subspace or onto a separable state.


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 80

|Transmon|Col2|Transmon|
|---|---|---|



Figure 6.1: Schematic of experimental setup optimized for transmission losses. The cavities
are directly connected to a single microwave circulator in order to reduce __ loss and therefore
to enable the generation of higher-quality entangled states.

We explore the probability distribution of the qubits concurrence to understand how the distribution changes in time, from a separable state with zero concurrence, to projected states
in either a separable subspace or an entangled subspace [170]. This can also be seen from the
most likely path analysis, showing the emergence of dierent most probable paths for each
final state. Moreover, we investigate the distribution of the time-to-maximum-concurrence,
finding that the most probable time to maximum values of concurrence has a bimodal structure. Studying the statistics of a large set of trajectories - rather than averaging over all of
them to study the dynamics of the ensemble - enables an unprecedented understanding of
the dynamics of entanglement creation under measurement.

This work was originally published in Ref. [188], and also appears in the thesis of Areeya

Chantasri.

## 6.1 ## Experimental Generation and Verification of Entangled Trajectories

The experimental setup for this experiment is quite similar to that in Chapter 5. However,
in this set of experiments we are more interested in the entanglement generation process
than in the remoteness of the measurement; we therefore remove the 1.3 meters of delay
cable and one of the circulators (Figure 6.1). By removing these components, we increase
the signal transmission efficiency __ loss
from 0.75 to 0.92, which reduces the measurementinduced dephasing and allows us to reach higher values of concurrence. We characterize
and calibrate the system as in Section 5.4; the qubit and cavity parameters are tabulated in
Table 6.1.


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 81

Table 6.1: Calibrated system parameters

|System Parameters|Col2|Col3|
|---|---|---|
||Qubit 1|Qubit 2|
|! /2 q|4.27225 GHz|4.37226 GHz|
|! /2 r|7.1871 GHz|7.1988 GHz|
|/2|19.8 MHz|18.2 MHz|
|/2|1.015 0.025 MHz  |1.085 0.035 MHz  |
|T 1|27 4 s |17 3 s |
|T 2|18 3 s |14 2 s |
| loss|0.92 0.03 ||
| meas|0.22 0.05 ||
|G chain|12.8 1.3 ||



### 6.1.1 ### Generating quantum trajectories

The pulse sequence used is identical to that shown in Figure 5.9; however, the data collection
and processing required to generate trajectories diers. In order to track the trajectories we
keep the entire instantaneous homodyne detection signal rather than averaging it over _t_ . The
dynamics or the trajectory of the system state can be obtained via the full master equations

[177, 179], using a two-cavity polaron transformation to account for the cavity degree of
freedom, giving the stochastic master equation for the qubit trajectories. This is a similar
procedure to that outlined in Section 4.3. Alternatively, in a limit of large cavity decay
rate __ _|_ __ _|_ , the qubits evolution can be continuously tracked via the quantum Bayesian
approach [156, 172], inferring the current states of the system from the measurement readouts
and how likely they are to occur.

In this chapter, as in the previous one, we focus on the quantum Bayesian approach, as it


is directly related to the probability distribution of the measurement readout and naturally
leads to the probability distribution of quantum trajectories. Following Section 2.2, let us
denote _p_ ij ( _V_ _t_ ) as a probability density function of a measurement readout _V_ _t_ conditioned on
the two-qubit fiducial states _|_ _ij_ _i_ . Here, we define


_t_

0

Z


_V_ _t_ ( _f/t_ )
__


_V_  ( _t_ _0_ )d _t_ _0_


_v_ 0 (6.1)
__


as the scaled, averaged readout signal, where _V_  ( _t_ ) is the instantaneous measurement voltage,

and _f_ and _v_ 0 are scaling factors enabling us to translate from the raw experimental data to
the theoretical distributions. The quantum Bayesian update for this type of double-qubit
measurement provides a convenient way to calculate the joint state at time _t_ , given a known


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 82

state at the initial time and the integrated signal _V_ _t_ ,



__ ij _,_ kl (0)
__ ij _,_ kl ( _t_ ) =


_p_ ij ( _V_ _t_ ) _p_ kl ( _V_ _t_ ) _e_ __ __ _ij,kl_ _t_


__ mn _,_ mn (0) _p_ mn ( _V_ _t_ ) _,_ (6.2)
P


where __ _ij,kl_
is a generalized decoherence rate associated to the matrix element. The decoherence rates combine pure dephasing with measurement-induced dephasing due to __ loss and
__ meas . The form of __ _eg,ge_ is given by Eq. (5.15); we do not explicitly derive the other terms
decay rates, although they have a similar form. Eq. (6.2) is a generalized formulation of Eq.
(5.14) that applies to all density matrix elements. We have neglected _T_ 1 -type decay.


Given a properly calibrated measurement chain, we can _a priori_ predict the distributions

_p_ ij ( _V_ _t_ ) using the Bayesian update formulae in Eqs. (5.11) and (5.12); predicting the density
matrix evolution given a measurement record _V_  ( _t_ ) is then straightforward. Specifically, the

conditional readout distributions _p_ ij ( _V_ _t_ ) are well-approximated by Gaussian functions

_p_ ij ( _V_ _t_ ) = ( _t/s_ ) __ 1 _/_ 2 exp [ _V_ _t_ _S_ _ij_ ] 2 _t/s_ (6.3)
_{_ __ _}_


with the signal centroids _S_ _ij_ as defined in Eq. (5.11) and _s_ = 1 _/_ 2 __ meas . The measurement
process cannot distinguish the two states in the odd-parity subspace, therefore the readout
distributions corresponding to the states _|_ _ge_ _i_ and _|_ _eg_ _i_ are completely (or nearly) overlapped,
giving _S_ _ge_ _S_ _eg_ 0 and _S_ _gg_ _S_ _ee_ _S_ . The measurement strength is characterized by
__ __ __ __ __ 2
an inverse of a characteristic measurement time __ _m_ 1 _/S_ __ meas . The dephasing rates __ _ij,kl_
__
for _S_ _ij_ _6_ = _S_ _kl_ are dominated by the eect of the distinguishability between states 1 2 _|_ _ij_ _i_ and
_kl_ , __ _ij,kl_ ( __ meas __ 1)( _S_ _ij_ _S_ _kl_ ) _/_ 4 _s_ , resulting in the strong suppression of all o-diagonal
_|_ _i_ __ __ __


elements except __ ge _,_ eg when the system is projected towards the entangled subspace. In


meas __ 1 1)( _S_ _ij_ _S_ _kl_ ) 2 _/_ 4 _s_ , resulting in the strong suppression of all o-diagonal

__ __


an ideal half-parity measurement, the decay of __ ge _,_ eg would be limited only by the intrinsic
lifetimes of the qubits; however, we must additionally account for experimental imperfections
in the matching of _S_ _ge_ and _S_ _eg_ and for the loss of photons between the two cavities. These
eects are included in the (slightly time-dependent) dephasing rate __ _ge,eg_ .

### 6.1.2 ### Validating the quantum trajectories

The previous development allows us to predict, based on a thorough calibration of the experimental system and a careful collection of the measurement output signal, the continuous
trajectory of a single experimental iteration. However, we would like to experimentally verify
that the actual trajectory of the system matches the Bayesian prediction. In other words, we
would like to experimentally generate a mapping _V_ _t_ __ ( _V_ _t_ ) and compare it to the Bayesian
_7!_
update provided by Eq. (6.2). To do so, we perform a series of experiments very similar to
those described in Chapter 5. We collect a large set of trajectories for which we record only
the integrated signal _V_ _t_ , not the instantaneous signal _V_  ( _t_ ), while varying the integration

time _t_ . Instead of post-selecting an entangled ensemble, however, we collect all experiments
with similar weak measurement outcomes _V_ _t_ __ at _fixed_ time _t_
, and perform a conditional tomographic state reconstruction of those trajectories. This is in principle the same procedure __


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 83


![SchwarzThesis.pdf-94-0.png](SchwarzThesis.pdf-94-0.png)

Figure 6.2: Comparison of conditional tomography to predicted __ ( _V_ _t_ ) at fixed _t_ = 0 _._ 48
__ s. Experimentally constructed conditional density matrices are shown using open symbols;
the colored shaded regions denote error bars. The predicted density matrix __ ( _V_ _t_ ) from the
Bayesian formalism is shown by dashed lines.

carried out in Section 5.5; however here, we use _p_ ent __ 1 and sweep the target _V_ _t_ over all
values, rather than specializing to the _V_ _t_ most likely to maximize entanglement. Figure 6.2
shows a comparison between the experimentally constructed __ and the Bayesian prediction
for all _V_ _t_ at a single _t_ : we see in fact that there is excellent agreement between the Bayesian
prediction and the experimental trajectory 1 .

Having verified the Bayesian trajectory at a single measurement time, we can proceed

to reproduce this data for all time, and thus generate a complete experimental mapping
_V_ _t_ __ ( _V_ _t_ ). Figure 6.3 which presents full tomographic mappings for the diagonal matrix
_7!_
elements __ gg _,_ gg _, _ ge _,_ ge _, _ eg _,_ eg _,_ and __ ee _,_ ee at all times. We then record a set of trajectories

in which we keep the full instantaneous voltage, and integrate it in post-processing for a
range of _t_ so that we can reconstruct the full continuous trajectories __ ( _t_ ) for the _individual_
experimental realizations. Figure 6.4 shows an exemplar trajectory for a full measurement
time of 1.6 __ s. The Bayesian update (shown as solid lines) is performed every 10 ns; due to
hardware limitations, the experimental conditional tomography is updated every 80 ns. The
slightly jagged nature of the Bayesian data is due to finite bin size.

This particular trajectory takes a very interesting path through state space. Early fluctu-


1 It is of some philosophical interest to note that, in constructing the mapping _V_ _t_ __ ( _t_ ) in this way, we
_7!_

have explicitly made the Markov approximation. There is no _a priori_ reason to presume that the final state
of the system should depend only on the average signal, and not on the specific path (fluctuations) that led
to that average signal. Indeed, the thousands of trajectories making up the ensemble used to reconstruct __ ( _t_ )
for a given _V_ _t_ will in general all have unique paths up until _t_ , when their mean signals coincide. Therefore,
in some sense the quantitative agreement seen in Figure 6.2 between theory and data is a confirmation that
the Markov approximation is appropriate in this system


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 84


0.04

0.02

0

0.02

0.04


0.06

![SchwarzThesis.pdf-95-0.png](SchwarzThesis.pdf-95-0.png)
0 0.5 1 1.5

t (s)

0.04

0.02

0

0.02

0.04


0.04

0.02

0

0.02

0.04

0.06

![SchwarzThesis.pdf-95-1.png](SchwarzThesis.pdf-95-1.png)
0 0.5 1 1.5

t (s)

0.04

0.02

0

0.02

0.04


0.06


0.06


![SchwarzThesis.pdf-95-2.png](SchwarzThesis.pdf-95-2.png)

![SchwarzThesis.pdf-95-3.png](SchwarzThesis.pdf-95-3.png)

0.5 1 1.5

t (s)


0.5 1 1.5

t (s)


Figure 6.3: Full experimental mapping _V_ _t_ __ ( _V_ _t_ ) for the diagonal density matrix elements.
_7!_

ations appear to be driving the system toward the joint ground state as __ gg _,_ gg
increases; however, the system then seems to stabilize into the entangled subspace for 0 _._ 4 __ s _< t <_ 1 __ s,
with concurrence _C _ 0 _._
45. After this, fluctuations again take the system out of the entangled state and toward _|_ _gg_ _i_ , only to return to the entangled state as the measurement
concludes. We emphasize here that this is the true trajectory of this iteration of the entangling measurements, and that this exciting path represents the predicted and experimentally
confirmed back-action of the fluctuating measurement field on the qubit pair. The excellent agreement between the tomographic reconstructions of the trajectories and theoretical
predictions based on Bayesian updates, even for this complicated trajectory, demonstrates
the validity of Bayesian quantum trajectory theories for cascaded quantum systems. In Ref.

[167], we show equally clean agreement between tomographically reconstructed trajectories
and the full master equation approach laid out in Ref. [179], providing further, more theoretically rigorous support for the quantum trajectory approach first developed in Refs. [189,
190].


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 85

1


0.8

0.6

0.4

0.2


![SchwarzThesis.pdf-96-0.png](SchwarzThesis.pdf-96-0.png)

0.4 0.8 1.2 1.6

Time (s)


0.4 0.8 1.2 1.6


Figure 6.4: Comparison of experimentally constructed trajectories to the Bayesian prediction. Experimental data are shown with open signals and shaded error bars; the Bayesian
prediction is shown in solid lines. The inset displays the trajectory of the concurrence as
calculated from the Bayesian formalism.

## 6.2 ## Statistical Properties of Concurrence Trajectories

We have now seen that a minimal Bayesian formula well-describes the evolution of a bipartite
quantum system under the influence of an entangling measurement. We would now like to go
a step further: we will use our well-calibrated experimental system to explore the statistical
properties of entangled trajectories. Doing so allows us to peer inside the ensemble dynamics
observed in Chapter 5 and to develop a deeper and more sophisticated understanding of
continuous measurement-induced entanglement.

As we saw in Chapter 3, concurrence is a convenient choice of measure for bipartite

entanglement because can be computed directly from the density matrix of the system [107].
The concurrence formula for the partial-parity setup is greatly simplified because of the
suppression of most matrix elements, so for the theoretical development below we use the
simplified formula. In this section, we will develop a Bayesian prediction of the concurrence
directly from the measurement readout, which then leads to the derivation of the concurrence
probability distribution as a function of the measurement readout and measuring time.

### 6.2.1 ### Concurrence-readout relationship

Let us consider the concurrence formula for the odd-parity subspace,

= 2 max 0 _,_ __ ge _,_ eg _p_ __ gg _,_ gg __ ee _,_ ee _._ (6.4)
_C_ _|_ _| _


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 86

We will define the comparator function as


_c_ _t_ = 2


__ ge _,_ eg ( _t_ )
_|_ _| _


__ gg _,_ gg ( _t_ ) __ ee _,_ ee ( _t_ )


(6.5)


If _c_ _t_ is non-negative, then the concurrence is simply given by _C_ ( _t_ ) = _c_ _t_ . We will show at
the end of this section that this is always the case for our chosen initial qubit state and
parameter regimes, but is not true in general [170]. From the Bayesian update and the
readout distribution functions in Section 6.1.1, we calculate the quantity,



2
_c_ _t_ ( _V_ _t_ ) =


__ ge _,_ eg (0)
_|_ _|_


_p_ ge ( _V_ _t_ ) _p_ eg ( _V_ _t_ ) _e_ __ _ t_ __


__ gg _,_ gg (0) __ ee _,_ ee (0) _p_ gg ( _V_ _t_ ) _p_ ee ( _V_ _t_ )


(6.6)


where __ __ __ _ge,eg_ and _N_ is a normalized factor given by _N_ =

P

widths __ ( _t_ ) we obtain a form of _c_ _t_ ( _V_ _t_ ) explicitly as a function of


_ij_ __ ij _,_ ij (0) _p_ ij ( _V_ _t_ ). Substituting


the arbitrary probability distribution functions for Gaussian functions with mean _S_ _ij_ and
widths __ ( _t_ ) we obtain a form of _c_ _t_ ( _V_ _t_ ) explicitly as a function of _V_ _t_ and _t_ ,



2
_c_ _t_ ( _V_ _t_ ) =


__ ge _,_ eg (0) _e_ [ __ _ge,eg_ _V_ _t_ __ __ _ge,eg_ __ __ ] _t_
_|_ _|_ __


__ gg _,_ gg (0) __ ee _,_ ee (0) _e_ [ __ _gg,ee_ _V_ _t_ __ __ _gg,ee_ ] _t_


(6.7)


where the prefactor is given by _M_ =

__ _ij_ = _S_ _ij_ _/s_ P

2


_ij_ __ ij _,_ ij (0) _e_ 2 __ _ij_ _V_ _t_ _t_ __ 2 __ _ij_ _t_ using a set of defined variables:


__ _ij_ = _S_ _ij_ _/s_ __ _ij,kl_ = __ _ij_ + __ _kl_ ; (6.8)


__ _ij_ = _S_


_ij_ 2 _/_ 2 _s_ __ _ij,kl_ = __ _ij_ + __ _kl_ _._ (6.9)


Critically, _c_ _t_ ( _V_ _t_
) depends only on the starting state of the system and the integrated measurement voltage, such that we can quantitatively predict the entanglement using only the
inputs already required for the Bayesian update.


The quantity _c_ _t_ ( _V_ _t_ ) represents the true concurrence of the joint qubit state if _c_ _t_ 0 is
__

satisfied. For our chosen initial state, a product of single qubit  _x_ -states, _c_ _t_ ( _V_ _t_ ) is non-negative

whenever the condition


( __ __ __ _ge,eg_ _V_ _t_ + __ _ge,eg_ ) _<_ ( __ _gg,ee_ __ __ _gg,ee_ _V_ _t_ ) (6.10)

is true. In our experiment, we have __ _S_ _gg_ __ _S_ _ee_ and _S_ _ge_ __ _S_ _eg_ __ 0, giving __ _gg,ee_ _, _ _ge,eg_ _, _ _ge,eg_ __
0. For __ _m_ = 0 _._ 60 _s_ we have __ _gg,ee_ __ 3 _._ 4 MHz, while _ <_ 1 _._ 7 MHz. With these values,
the condition in Eq. (6.10) is always satisfied. The second term in the bracket of Eq. (6.7)
decays faster than the first term, so that the concurrence is always nonzero. Consequently,
we can define the concurrence-readout relationship ( _V_ _t_ ) = _c_ _t_ ( _V_ _t_ ), such that the concurrence
_C_
at any time _t_ can be determined directly from the time-average measurement readout _V_ _t_ .

The concurrence formula in Eq. (6.7) can be simplified further by considering a perfectly

symmetric partial-parity measurement, _S_ _ge_ = _S_ _eg_ = 0 and __ _S_ _gg_ = _S_ _ee_ = _S_ . Given the initial
state, a product of two qubit  _x_ -states, the concurrence is then given by,


_e_ __ _t_ _e_ __ _S_ 2 _t/s_
_C_ sp _,_ _x_  ( _V_ _t_ ) = 1 + cosh[2 __ _V_ _t_ _St/s_ ] _e_ __ _S_ 2 _t/s_ _,_ (6.11)

where the subscript sp, _x_  indicates the perfectly symmetric partial-parity measurement given

the specific initial state.


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 87

![SchwarzThesis.pdf-98-0.png](SchwarzThesis.pdf-98-0.png)

Figure 6.5: Evolution of _p_ tot ( _V_ _t_ ) as integration time increases.

### 6.2.2 ### Probability density function for concurrence trajectories

From the direct relationship between the measurement readout and the concurrence of the
qubits state, the probability density function of the concurrence can be derived from the
probability distribution of the measurement signal. The distribution of the time-average
readout is given by a sum of Gaussians,


_p_ tot ( _V_ _t_ ) =


__ ij _,_ ij (0) _p_ ij ( _V_ _t_ ) _._ (6.12)

_ij_


The variance of the distribution __ 2 = _s/_ 2 _t_ narrows as time increases, leading to the collapse
of the joint qubit state into three categories: _|_ _gg_ _i_ , _|_ _ee_ _i_ , and some superposition state of _|_ _ge_ _i_
and _eg_ after a few characteristic measurement times __ _m_ . The experimental measurement
_|_ _i_
probability distribution shown in Figure 6.5 slowly resolves into the three peaks expected
for a half-parity measurement, and the resulting concurrence probability density is shown in
Figure 6.6.

Given the distribution of the time-averaged signal, we follow the transformation of ran-

dom variables _V_ _t_ ( _V_ _t_ ) using the concurrence-readout relationship. The concurrence is
_7! C_
not a monotonic function in _V_ _t_ ; instead it has a bell-like shape as shown in the inset of Figure
6.6a. We write the cumulative distribution function of the concurrence

_F_ ( _c, t_ ) = _p_ ( _C _ _c, t_ ) = _p_ tot ( _V_ _t_ __ _V_ __ ) + [1 __ _p_ tot ( _V_ _t_ __ _V_ + )] _,_ (6.13)

where _V_ + , _V_ __ are two solutions that arise from solving Eq. (6.7) for _C_ ( _V_ _t_ ) = _c_ . The concur-


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 88


0.6

0.4

0.2

0

0.6

0.4

0.2

0.


1.0
0.8
0.6
0.4
0.2
0

1.0
0.8
0.6
0.4
0.2


![SchwarzThesis.pdf-99-0.png](SchwarzThesis.pdf-99-0.png)

![SchwarzThesis.pdf-99-7.png](SchwarzThesis.pdf-99-7.png)

![SchwarzThesis.pdf-99-1.png](SchwarzThesis.pdf-99-1.png)

![SchwarzThesis.pdf-99-2.png](SchwarzThesis.pdf-99-2.png)


0.4 0.8 1.2 1.6

![SchwarzThesis.pdf-99-8.png](SchwarzThesis.pdf-99-8.png)

![SchwarzThesis.pdf-99-4.png](SchwarzThesis.pdf-99-4.png)

0.4 0.8 1.2 1.6


![SchwarzThesis.pdf-99-6.png](SchwarzThesis.pdf-99-6.png)

![SchwarzThesis.pdf-99-3.png](SchwarzThesis.pdf-99-3.png)

![SchwarzThesis.pdf-99-5.png](SchwarzThesis.pdf-99-5.png)

Figure 6.6: Concurrence distribution for the qubits under the partial-parity measurement.
In panel (a), we plot the concurrence probability density function Eq. (6.14) for dierent
values of time. The values of time for the presented curves are chosen so as to see their
unique features as they develop. The grey dotted curve joining the high-concurrence peaks
shows the concurrence upper bound Eq. (6.15). The inset shows an example of how the
concurrence (at time _t_ = 1 _s_ ) varies as a function of the readout _V_ _t_ . (b) and (c) are the
histograms of the concurrence at any time points from _t_ = 0 to _t_ = 1 _._ 6 _s_ (with a step size
0 _._ 01 _s_ ), comparing theory and experimental data. For the theory plot, we coarse-grain the
distribution _p_ _C_ _,t_ ( _c_ ) in Eq. (6.14) by integrating it with a pixel size _c_ __ 0 _._ 015, which is the
bin size of the experimental histogram. For presentation purposes, a histogram at any time
_t_ is normalized by its maximum element.

rence distribution is then obtained by taking a derivative of the cumulative distribution,


_p_ ( _c, t_ ) = _p_ tot ( _V_ __ )


_@V_
__

_@c_


_@V_ +

_@c_


noting that _V_ __ ( _c, t_ ) and _V_ + ( _c, t_ ) are functions of the concurrence _c_ and time _t_ . The full
solution of _p_ ( _c, t_ ) is quite lengthy and is not shown.



+ _p_ tot ( _V_ + )





_,_ (6.14)
 _c_ and time _t_ . The full



We show in Figure 6.6a the plots of concurrence probability distributions Eq. (6.14)

for several dierent values of time _t_ . In Figure 6.6b-c, we show a comparison between

the theoretical _p_ ( _c, t_ ) and the experimental distribution of concurrence. At an early time,
the distribution of concurrence is narrowly peaked near its maximum which increases over
time, whereas at later times, a second peak emerges near the zero concurrence, showing
a bimodal distribution. In Figure 6.6b, the theoretical histogram for the concurrence is

obtained by integrating the theory curve Eq. (6.14) for the probability over small intervals


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 89


_c_ __ 0 _._ 015. This is to make a fair comparison with the histogram of the experimental

data in Figure 6.6c, calculated with a bin size of 0 _._ 015. We note that a short delay in the
experimental entanglement creation is a result of the cavity ring-up time.

Examining the probability distributions, we see a number of interesting features. First,

we note that there are two apparent most likely branches of the concurrence trajectories,
one high and one low. This is what we expect given that the qubits may project into an
entangled (high) or an unentangled (low) subspace. However, note that for short times, even
the low-concurrence branch shows increasing entanglement: the two branches increase in
concurrence together before separating into their two paths, which occurs at _t_ __ _m_ . One
__
might expect that the separation between entangled and unentangled trajectories happens
on average at a time near __ _m_ ; we see clearly from the concurrence probability distribution
function that in general, that separation happens much more rapidly.

Finally, we see that the concurrence distribution has a sharp upper bound (shown as

a grey dotted curve in Figure 6.6a), which the concurrence cannot exceed. In order to

understand why the probability distribution for the concurrence has a sharp upper cut-o
at any time, we recall that the density matrix of the two-qubit system, conditioned on the
time-integrated readout _V_ _t_ , is entirely specified by that (random) outcome, together with
the initial state, the dephasing rate, and other parameters of the problem according to Eq.
(6.2). As can be seen from the inset of Figure 6.6a, the concurrence, plotted as a function
of the measured signal _V_ _t_ , is bounded from above for any fixed time _t_ by some amount we
call max . Because ( _V_ _t_ ) is determined entirely by _V_ _t_ , a value of concurrence higher than
_C_ _C_
that maximum (whose value will change as the time increases) cannot physically be realized.
Therefore the probability distribution of concurrence has a sharp upper cut-ogiven by
max ( _t_ ). Physically, this indicates that there is an upper limit on how fast entanglement
_C_
can be created by the continuous measurement in this situation, even for rare events of the
measurement process.


The value of _C_ max evolves based on the interaction between SNR improvement, pure


dephasing and decay, and loss-induced measurement dephasing. For the perfectly symmetric
case in Eq. (6.11), we can find an analytic solution for the upper bound of the concurrence.
Noting that cosh( _x_ ) has its minimum at _x_ = 0, sp _,_ _x_  ( _V_ _t_ ) must have its maximum at _V_ _t_ = 0.
_C_


Consequently, the concurrence upper bound is given by



__ _t_ _e_ __ _S_ 2 _t/s_
max _,_ sp _,_ _x_  ( _t_ ) = _e_ __ _S_ 2 _t/s_ _._ (6.15)
_C_ 1 + _e_ __



__ _t_ _e_ __ _S_ 2 _t/s_
_C_ max _,_ sp _,_ _x_  ( _t_ ) = _e_ 1 + __ _e_ __ _S_ 2 _t/s_


The behavior of this bound is a result of two competing rates, between the extra dephasing
rate __ and a measurement rate _S_ 2 _/s_ . Eq. (6.15) increases from zero for small time and
decays for long time after reaching its maximum concurrence as seen in Figure 6.6. The
maximum possible concurrence for this qubit partial-parity measurement and the time this
happens can be obtained from this relation.


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 90

0.15

0.10

0.05

0.00

|C 1,2|Col2|Col3|Col4|Col5|Col6|A 1,2|Col8|Col9|Col10|D|Col12|Col13|Col14|Col15| = 0.36 s m  = 0.60 s m  = 2.10 s m B|Col17|Col18|Col19|Col20|Col21|Col22|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||


0.4


0.8 1.2 1.6


Figure 6.7: Histograms of the time-to-maximum concurrence for individual trajectories for
three measurement strengths indicated by the values of __ _m_ . For the two cases with strong
readout powers (shown in red and green histograms), there exists two peaks corresponding
to two most likely times to reach their most entangled states. The theoretical prediction of
these times are shown as vertical dashed lines labelled as _A_ 1 _,_ 2 _, B, C_ 1 _,_ 2 _, D_ .

### 6.2.3 ### Distribution of time to maximum concurrence

In the process of the entanglement generation, there are interesting quantities to investigate
such as the maximum concurrence each individual trajectory can reach, and the time it takes
to reach the highest value. Using a most-likely-path analysis developed in Ref. [188], we
can show that the high- and low- concurrence trajectory branches correspond to projection
onto the odd-parity subspace, and onto the _|_ _gg_ _i_ and _|_ _ee_ _i_ states respectively. Therefore, one
would expect that there are at least _two_ most likely times for the qubit trajectories to reach
their maximum concurrences (or their most entangled states).

We show in Figure 6.7 the normalized histograms of time for transmon qubit trajectories

to reach their maximum concurrence. The histograms for the measurement cases explicitly show double peaks, which agree with the branching of concurrence __ _m_ = 0 _._ 36 _s_ and 0 _._ 60 _s_
and the most likely qubit paths in Figure 6.6b-c. The times at which these peaks are located
can be theoretically predicted from the time-to-maximum-concurrence of the solutions of the
most likely paths; as shown by the vertical dashed lines in Figure 6.7: _A_ 1 _,_ 2 , _B_ are the two


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 91

most likely times to reach maximum concurrence (for low and high concurrence branches,
respectively) for __ _m_ = 0 _._ 60 _s_ , and _C_ 1 _,_ 2 , _D_ are the same but for the case with __ _m_ = 0 _._ 36
_s_ . We note that for the weak measurement regime, __ _m_ = 2 _._ 10 _s_ , the bifurcation has not
occurred yet during the measurement time _T_ = 1 _._ 6 _s_ . One would expect to see a branching
eect, when the total measurement time is long enough.

## 6.3 ## Conclusion

We have investigated the process of entanglement generation between two spatially separated superconducting transmon qubits, and their statistical properties. The entanglement
of the two qubits is created as a result of the partial-parity dispersive measurement, via the
microwave pulses sequentially interacting with both qubits. The strength of the joint measurement is arbitrary and we have studied three dierent values of the measurement strength.
We examine the concurrence of individual trajectories both as experimentally generated and
as theoretically calculated from the quantum Bayesian approach, gradually projecting the
two-qubit states to entangled states with high concurrence, and to separable states with zero
concurrence. We remind the reader that the Bayesian approach is purely phenomenological:
we trade oan accurate microscopic theoretical model for reduced computational intensity
in comparison to the stochastic master equation approach. It also can be susceptible to
the integration timescale - one must ensure that the data acquisition rate is significantly
faster than the underlying system and measurement dynamics in order to fully capture the
evolution of the system. Therefore, the eectiveness of the Bayesian approach is somewhat
surprising, and remarkable.

Because we can generate arbitrarily many trajectories, we can investigate the statis-

tical properties of the concurrence probability distribution, which immediately shows two
interesting and nontrivial properties: a sharp cutoabove which there are rigorously zero
concurrence trajectories, and an initial transient period, much shorter than the characteristic measurement time __ _m_ , during which all trajectories develop significant concurrence.
Moreover, we have presented the distributions of the time to the maximum concurrence for
individual trajectories, which has clear applications to entanglement optimization. Our ability to reconstruct the full spectrum of possible concurrences for all times and all measurement
strengths represents an exceptional level of insight into the internal dynamics underlying an
ensemble of states that are entangled by measurement.

We conclude that the accurate tracking of quantum trajectories of a jointly measurement

qubit system is possible, and that the physics of the entanglement creation statistics is
well described by a quantum trajectory theoretical approach, which produces a concurrence
distribution that matches the experiment excellently. Because the Bayesian approach relies
only on a well-calibrated experimental system and the calibration protocols are the same
for an N-qubit system as for a 2-qubit system, we expect the Bayesian protocol to scale
nicely to multiple-qubit systems, enabling continuous trajectory tracking in a multipartite
system. Of course, in order to verify the trajectories, one must still perform a complete


-----


_CHAPTER 6. QUANTUM TRAJECTORIES_ 92

tomography. The number of measurements required scales in the worst case as 2 2 _n_ __ 1 and
presents a well-known barrier to the full characterization of a large quantum system. In
addition, intra-cavity losses create a technological barrier: we expect the Bayesian approach
to perform perfectly well, but the quality of entanglement generated may suer without
the development of low-loss intra-cavity components [191, 192]. The work described here
represents an important means to use measurement processes as a control mechanism to
entangle remote systems for quantum information processing purposes.


-----


93

# Chapter 7

 Deterministic Entanglement via Symmetry-Selective Dissipation Engineering

We have to remember that what we observe is not nature herself,
but nature exposed to our method of questioning.

Werner Heisenberg, _Physics and Philosophy_ , 1958

To this point, we have used dissipation in the form of a measurement to generate entangle-

ment, and to comprehensively study the dynamics of the entangling back action. However,
there is a central limitation to the approach described in Chapters 5 and 6: because we
generate entanglement using a _half-parity_ measurement, the process is probabilistic: at best,
we have a 50% chance to generate entanglement. In this chapter, we develop a dissipative method to generate entanglement _deterministically_ - that is, without any post-selection
required. Interestingly, this approach relies only on dissipation; as we will see, the very
presence of a dissipative mode is sufficient to generate entanglement, with out any need to
record the instantaneous cavity output or to track qubit state evolution.

In this chapter, we use an approach that is often called quantum bath engineering,

reservoir engineering, or dissipation engineering [58, 59, 194, 195]. Bath engineering explicitly
utilizes the coupling of the qubits to their environment as a resource. By designing the density
of states in a lossy mode and driving that mode unconditionally, we modify the dissipative
environment and dynamically cool to a desired quantum state. We essentially use additional
microwave drives to alter the driven ground state of the system into a non-trivial - in this
case, entangled - quantum state. Bath engineering in superconducting qubits has resulted in
the stabilization of a single qubit on the Bloch sphere [61], a Bell-state of two qubits housed
in the same cavity [63], many-body states [62], and non-classical resonator states [64, 196].
Additionally, theoretical proposals have been put forward for dissipative error correction

[197199] and ultimately universal quantum computation [200].


-----



![SchwarzThesis.pdf-105-0.png](SchwarzThesis.pdf-105-0.png)

![SchwarzThesis.pdf-105-1.png](SchwarzThesis.pdf-105-1.png)

![SchwarzThesis.pdf-105-2.png](SchwarzThesis.pdf-105-2.png)

![SchwarzThesis.pdf-105-3.png](SchwarzThesis.pdf-105-3.png)

__ in _i_ , strongly-coupled output port __ out , and inter-cavity coupling _J_ .

Bath engineering approaches require careful selection of the bath modes, and often many

drives to excite these modes so as to produce a non-trivial ground state. Bath engineering
schemes have typically focused on sculpting a density of states conducive to cooling, relying
on the conservation of energy between drive, qubit, and resonator modes in multi-photon
processes. Here, we harness an additional degree of freedom: the spatial symmetry of the
bath, which mandates conservation of parity. We combine both spectral and symmetry selectivity of the bath to provide a scalable protocol for generating on-demand entanglement
using only a single microwave drive with a controllable spatial profile. As a demonstration of
this scheme, we stabilize two-qubit entangled states in the single-excitation subspace using
two tunable 3D transmon qubits [115] in independent microwave cavities. Our results demonstrate the viability of this protocol for stabilizing many-body entangled states in extended
arrays.

## 7.1 ## Experimental Design and Protocol


The experiments are implemented (Figure 7.1) using two copper waveguide cavities (indexed as _A_ and _B_ ) that are aperture-coupled on the transverse (magnetic) axis, with an
independent flux-tunable transmon embedded in each cavity. The cavities are fabricated
with near-identical resonance frequencies _!_ c _!_ c ; the qubits are flux-tuned to resonance


at _!_ q


_A,B_ c _!_ c ; the qubits are flux-tuned to resonance

__


cavities are individually addressable via a weakly-coupled port ( __ in


_A,B_ q _!_ q . The full set of qubit and cavity parameters are tabulated in Table 7.1. The

__ in



in _i_ ) through which we apply


qubit pulses and bath drives; cavity has an additional strongly coupled port for readout. A full elaboration of the cavity design, experimental setup and calibration procedure is _A_
provided in Section 7.3.


The unitary dynamics of the system are described by a Hamiltonian that can be subdi-


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 95

vided in the rotating wave approximation into qubit, cavity, and drive components:


_!_ q








__  _i_ _Z_
2


__  +


_i_ + _a_  _i_ +  __ _i_ __


_i_ __ _a_  __ _i_


_H_ _q_ =

_H_  _a_ =

_H_  _d_ =


_i_ _Z_ + _g_ _i_


(7.1a)

(7.1b)

(7.1c)


_i_ = _A,B_

_i_ = _A,B_

X

_i_ = _A,B_

X


_!_ c _a_  __ _i_ _a_ 


_!_ c _a_  __


+ _J_


_a_  _A_ _a_  __



__ _B_ +  _a_ __



__ _A_ _a_  _B_



_i_ ( _!_ d _t_ + __ _i_ ) _i_ ( _!_ d _t_ + __ _i_ )

_a_  __ _i_ _e_ __ +  _a_ _i_ _e_

i



_i_ ( _!_ d _t_ + __ _i_ ) _i_ ( _!_ d _t_ + __ _i_ )

__ _i_ _e_ __ +  _a_ _i_ _e_

i


__ d


Here,  __ _Z,_ __


are Pauli operators on the qubits;  _a_ __


_i_ are creation operators on the cavity modes;


__ d



d _i_ are Rabi drives applied at a single frequency _!_ d to the respective cavities with a tunable


phase __ _i_ ; and _g_ _i_ are the qubit-cavity couplings. Decay mechanisms not accounted for in
these unitary dynamics include qubit energy relaxation ( 1 ) and dephasing ( __ ), and cavity
photon leakage ( __ ).


The eects of the coupling terms _g_ _i_ and _J_ manifest in both the qubit and cavity sectors.


The central cavity resonances hybridize into symmetric and antisymmetric modes, with the
former having a lower frequency (Figure 7.2a). We define these modes as _!_ c _!_ c _J_ . In



c _!_ c _J_ . In

__ __ __


the dispersive limit where the qubit-cavity detuning  qc



qc _!_ q _!_

__ __ __



c is large in comparison to

__


_g_ , the qubit-cavity coupling creates a photon-mediated _XY_ interaction between the qubits,

_g_ _A_ _g_ _B_
lifting the degeneracy in the single-excitation subspace [201]. Defining __ = _J_ , the


 qc


, the


coupled eigenstates and eigenenergies are given by the following:



qc +  qc


_T_ + _ee_ _!_ _T_ + = 2 _!_ q (7.2a)
_|_ _i |_ _i_ _|_ _i_



_ge_ _eg_
_S_ _|_ _i |_ _i_
_|_ _i _ _p_ 2



_ge_ + _eg_
_T_ 0 _|_ _i_ _|_ _i_
_|_ _i _ _p_ 2


_!_ _S_ = _!_ q + __ (7.2b)
_|_ _i_

_!_ _T_ 0 = _!_ q __ (7.2c)
_|_ _i_ __


_T_ _gg_ _!_ _T_ = 0 (7.2d)
_|_ __ _i |_ _i_ _|_ __ _i_

We can then define full basis states of the system including the cavity modes, as

_|_ _i, j, k_ _i_ = _|_ _n_ + _i |_ _n_ __ _i |_ _q_ _i_ (7.3)

where _n_ indexes the Fock state of the respective hybridized cavity modes and _q_ is a
__ _|_ _i_
coupled qubit state _|_ _q_ _i 2 {|_ _S_ _i_ _,_ _|_ _T_ 0 _,_ __ _i}_ . Figure 7.2b shows the qubit-sector avoided crossing
of width 2 __ = 2 __ __ 2 _._ 7 MHz, in quantitative agreement with independently-characterized
system parameters.

### 7.1.1 ### Entangling protocol

Because the Bell states _S_ and _T_ 0 are eigenstates of the coupled Hamiltonian, it is in
_|_ _i_ _|_ _i_
principle possible to coherently pulse to these states. However, because the splitting is


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 96


6.21

6.20


-20

-40

-60


6.19

![SchwarzThesis.pdf-107-0.png](SchwarzThesis.pdf-107-0.png)

![SchwarzThesis.pdf-107-2.png](SchwarzThesis.pdf-107-2.png)
6.194 6.204

Nominal (GHz)


-80


![SchwarzThesis.pdf-107-1.png](SchwarzThesis.pdf-107-1.png)

6.9 7.1 7.3


Frequency (GHz)


Figure 7.2: Avoided crossings in cavity and qubit sectors. **a** : Transmission spectrum of
the coupled cavity modes, showing the symmetric (blue) and antisymmetric (red) peaks.
**b** : Pump-probe spectroscopy of the coupled qubit modes, exhibiting an avoided crossing.
Cavity and cavity _B_ is driven at the symmetric cavity resonance conditioned on the qubit state _A_ is driven at a swept frequency _!_ R . A dip in transmission (blue) indicates that _|_ _gg_ _i_ ,
_!_ R is resonant with a qubit mode. The dashed line is a fit of the spectral data, from which
we extract __ .

small, a coherent pulse with narrow enough bandwidth to drive selectively to one of these
states would need to be several microseconds long, and therefore would be spoiled by qubit
decay. Bath engineering, which stabilizes against this decay, provides an alternative means
of entanglement in this system.


the distinct symmetries of the bath modes at _!_ c


We aim to stabilize the entangled state of choice ( _S_ or _T_ 0 ) by taking advantage of

c _|_ _i_ c _|_ _i_


+ c and _!_ c



c . We do this by simultaneously

__


applying a two-photon drive at the individual cavity ports while varying the relative phase
between the cavities (Figure 7.3). This work represents a generalization to arbitrary drive
phase of the proposal in [201]; a full theoretical treatment (including dynamics) is presented
in Section 7.2


Our cooling protocol relies on transitions between the neighboring _n_ = 0 _,_ 1 rungs of
__ _{_ _}_

the Jaynes-Cummings ladder. The appropriate drive frequencies are given by


Our cooling protocol relies on transitions between the neighboring _n_ = 0 _,_ 1 rungs of
__ _{_ _}_


_!_


_|_ d _T_ 0 _i_ ( __ )


_!_ c



c + [ _!_ q + 2 __ ] __

__ __ __


(7.4)


_!_ d


_|_ d _S_ _i_ ( __ )


_!_ c



c + [ _!_ q + 2 __ ] + __

__ __


where __ is a cross-Kerr term leading to a _n_ -dependent shift in the eective qubit frequency,
and  _!_ q __ represents the dressed qubit frequency, which has a power-dependent red shift due __

to the o-resonant displacement of the cavity field by the drive. Because the qubit-cavity
couplings _g_ _i_ dier, the qubit frequencies shift by dierent amounts when exposed to the
same intra-cavity field. To correct for this, we place the bare qubit frequencies slightly o


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 97


![SchwarzThesis.pdf-108-0.png](SchwarzThesis.pdf-108-0.png)

![SchwarzThesis.pdf-108-1.png](SchwarzThesis.pdf-108-1.png)

![SchwarzThesis.pdf-108-2.png](SchwarzThesis.pdf-108-2.png)

Figure 7.3: Protocol for cooling to 0 _,_ 0 _, T_ 0 via _!_ c
_|_ _i_



c (left) and _!_ c

__


+ c (right). Each set of levels


outlined in grey represents a rung on the Jaynes-Cummings ladder; the states _q_ are the
coupled qubit states. The illustrated drives (arrows) represent _!_ d ( ) from Equation 7.4. _|_ _i_


_|_ d _T_ 0 _i_ ( __ ) from Equation 7.4.


Parity conservation requires that if cooling via _!_ c


+ c , the drive must be overall symmetric


(indicated by blue lines), with __ = _{_ 0 _, _ _}_ ; if cooling via _!_ c



c , the drive must comprise one

__


antisymmetric (red) photon for each symmetric photon. If this condition is met, leakage of
cavity photons (purple, __ ) brings the system to the entangled state 0 _,_ 0 _, T_ 0 . Leakage from
_|_ _i_
the entangled state is dominated by qubit decay (green,  1 ).


of resonance such that the _dressed_ qubit frequencies  _!_ _i_ q are identical. This adjustment is


of resonance such that the _dressed_ qubit frequencies  _!_


power-dependent, but is on the order of 1 MHz.

When a microwave drive is applied at one of these frequencies, a two-photon transi-


tion is created between the un-driven ground state 0 _,_ 0 _, T_ and the resonant partner state
_|_ __ _i_
1 _,_ 0 _, S_ _,_ 1 _,_ 0 _, T_ 0 _,_ 0 _,_ 1 _, S_ _,_ 0 _,_ 1 _, T_ 0 . However, when _n_ _>_ 0 the cavities decay
_|_ _i 2 {|_ _i_ _|_ _i_ _|_ _i_ _|_ _i}_ __

stochastically and irreversibly at a rate __ to 0 _,_ 0 _, T_ 0 or 0 _,_ 0 _, S_
; this is the critical dissipative element in the protocol. There are no transitions from this state that are resonant with __ _|_ _i_ _|_ _i_
the drive. In the case of a _T_ 1 decay, the drive rapidly repumps the qubits, thus creating a
stabilized entangled state. A weak o-resonant pumping into _T_ + , which is depleted by _T_ 1
_|_ _i_
rather than by active cooling, sets an upper limit on the cooling rate.


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 98

### 7.1.2 ### Symmetry-selectivity of protocol

Until now we have only described the _frequency_ of the bath drive; we have said nothing
about its symmetric properties. Because we can drive the two cavities individually, we are
able to continuously tune phase relationship between the drive at Cavity A and that at
Cavity B, __ __ _B_ __ _A_ . The phase-dependent properties of the bath engineering protocol
__ __
can be understood as a parity selection rule that is dynamically generated by altering the
drive profile across the cavities. The starting permutation-exchange parity is comprised of
the initial qubit state ( _T_ , a symmetric state) and the two photons used to generate the
_|_ __ _i_
drive (which vary from symmetric to antisymmetric with __ ); the output parity is comprised
of the qubit state symmetry and the dissipated photon. Conservation of parity requires that
the net parity of the output state respect that of the input state - remembering that the
net exchange symmetry of two antisymmetric components is overall even. By varying the
relative phase of the drives, we vary the input symmetry and therefore control the parity
selection rules. We therefore expect special symmetry points to exist at __ = 0, __ = __ , and
__ = __ __ _/_ 2, the first two of which represent exchange-symmetric drives, and the final of
which are exchange-antisymmetric drives. We will derive this rigorously in Section 7.2.

## 7.2 ## Theoretical Treatment of the Bath Drives

In this section, we will provide a thorough theoretical treatment of the coupled cavity system
that we study here. We will show the following:

-  A coupling Hamiltonian that leads to a degeneracy lifting in both the qubit and cavity

sectors;

-  A rigorous derivation of the two-photon drive used to generate transitions into the

entangled state of our choosing;

-  The origin of the parity selection rules discussed above, which fall naturally out of the

drive dynamics.

Our experimental setup can be modeled by a pair of two identical two-level systems

housed in two identical single-mode optical cavities which can exchange photons via coherent
tunneling. Both cavities are driven out of equilibrium by two coherent microwave drives with
same frequency _!_ d detuned from the cavity frequency. In the frame rotating at _!_ d , after
a rotating-wave approximation ( _i.e._ neglecting counter-rotating terms), the setup is well
described by the following Hamiltonian [201]:

_H_  = _H_  _q_ + _H_  _q,a_ + _H_  _a_ _,_ (7.5)


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 99


with _H_  _q_ , _H_  _q,a_ , and _H_  _a_ respectively being the qubit, the light-matter coupling, and the photon

Hamiltonians given by (we set ~ = 1)


( _!_ q __ _!_ d ) __  2 _i_ _Z_ ; (7.6a)


_H_ _q_ =

_H_  _q,a_ =

_H_  _a_ =


_g_ _i_


_a_ 



__ _i_ __  _i_ __


_i_ __ +  _a_ _i_ __  _i_ +


(7.6b)


( _!_ c _!_ d ) _a_ _i_
__



__ _i_ _a_  _i_ + __ d ( _a_ __ _i_



_i_ _i_

__ _i_ _e_ + h.c.)


__ _J_ ( _a_



__ _A_ _a_  _B_ + _a_



__ _B_ _a_  _A_ ) _._ (7.6c)


This is identical to the Hamiltonian in Eq. (7.1) in the rotating frame, regrouped for convenience here. The two-level systems are represented by Pauli matrices obeying [ __ _a_ _,_  __ _b_


_i_ _a_ _,_  __ _j_


_j_ _b_ ] =


2 _i_ _ij_ __ _abc_ __  _i_ _c_


_i_ _c_ where the indices _a, b, c_ _X, Y, Z_ , the cavity indices _i, j_ = _A, B_ and  __ _i_ __

_2 {_ _}_


_i_ _X_ _i_ __  _Y_ ) _/_ 2. All parameters are as defined in Section 7.1; given that physics only depends

__


( __ _X_


on the relative phase dierence, we shall henceforth work with __ __ _B_ __ _A_
__ __


Let us neglect the light-matter coupling for a moment. On the qubit side, the eigenstates


and eigenenergies of _H_  _q_ in the rotating frame are given by the triplet and singlet states:


_|_ _T_ + _i_ _|_ _ee_ _i_ _,_ _E_ _|_ _T_ + _i_ =  qd _,_


_|_ _S_ _i_ __ [ _|_ _ge_ _i |_ _eg_ _i_ ] _/_


2 _,_ _E_ _|_ _S_ _i_ = 0 _,_


(7.7)


_T_ 0 [ _ge_ + _eg_ ] _/_
_|_ _i_ __ _|_ _i_ _|_ _i_


2 _,_ _E_ _|_ _T_ 0 _i_ = 0 _,_


_|_ _T_ __ _i_ _|_ _gg_ _i_ _,_ _E_ _|_ _T_ __ _i_ = __  qd _,_


where  qd __ _!_ _q_ __ _!_ d is the detuning between the qubits and the drive. On the photonic side,
the two coupled cavities being identical, the eigenmodes of the undriven photonic backbone
are naturally symmetric and antisymmetric excitations with the creation operators


_A_  __ __ _a_  __ _A_ _p_ +  2 _a_


and  _a_ __ _a_  __ _A_ __ _a_  __
__ _p_ 2


_a_  __
and  _a_ __ __


respectively. In this basis, _H_  _a_ reads


_H_  _a_ =  cd +



cd + _A_  __  _A_ +  cd



cd _a_  __ _a_  +

__


2 __ d [ _A_  __ cos ( _/_ 2) __ _i_ _a_  __ sin ( _/_ 2)] + h.c. _,_ (7.8)


with  cd


We will include the total photon leakage outside the cavities with a rate __ + for the sym-



cd _!_ c

__ __



c _!_ d

__ __


metric mode and __ for the antisymmetric mode. The density of states for the antisymmetric
and symmetric modes are __ __ ( _!_ ) = Im _G_ R ( _!_ ) _/_ where the retarded Greens function are
__ R __ __ cd


given by, in the rotating frame, _G_ R



R ( _!_ ) _/_ where the retarded Greens function are

__



R ( _!_ ) = 1 _/_ [ _!_  cd

__ __ __



cd + _i_ _/_ 2]. We also include qubit decay

__ __


and pure dephasing rates,  1 and  _'_ respectively. These dissipative processes will play a
paramount role in the cooling scheme and protocol.


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 100

### 7.2.1 ### Dynamics

Altogether, the driven-dissipative dynamics of the entire system (qubits and photons) is well
described by the following Master equation on the density matrix __ :

__  = __ _i_ [ _H, _  ]


+ __ +
_D_


__ + __ [ _a_ ] __
__ _D_


(7.9)

_,_


__  __


__  _B_ __

_Z_
__  


+  1 _,A_
_D_


__ +  1 _,B_
_D_



 _',A_
+


__  _Z_



 _',B_
__ +


2 _D_


2 _D_


where the Lindblad dissipators are defined as in Chapter 2. This SME includes photon leakage from the two cavity modes at generally non-equal rates; individual qubit decay; and eective qubit dephasing rates. Eq. (7.9) can be solved numerically and __ ( _t_ ) rigorously accessed
at all times, so in principle writing down the SME provides the final story. In particular,
the knowledge of the non-equilibrium steady-state (NESS) density matrix __ NESS = lim __ ( _t_ )



__ ( _t_ )
_t_ _!1_


allows us to compute the fidelities of interest. However, the implications of the SME for
the dynamics in the qubit sector are not transparent, and we would like to do a more thorough analytical development in order to predict the behavior of the system more intuitively.
The results obtained from full numerical computations agree with the experimental results
and are also a way to check the validity of the dierent layers of approximations that are
performed in the analytic approach developed below.


### 7.2.2 ### Eective driven-dissipative ### XY ### model

We now present an analytic approach to compute the steady-state fidelities for the qubit
subsystem. In a nutshell, it consists of eliminating the explicit time-dependence of the

problem by means of a rotating-wave approximation; treating the light-matter interaction
by second-order perturbation theory; linearizing the photonic degrees of freedom around
mean-field solutions; and integrating out the remaining photon-fluctuations by means of
a Master-equation approach. The result is a set of rate equations that characterize the

population of the qubit eigenstates, directly in the steady state, _by-passing_ the transient
dynamics. The expressions for these rates make transparent the cooling protocol described
in Section 7.1.1 and also allow to quantify the expected fidelity of this protocol.

For clarity and relative ease of calculation our approach is presented for a setup without

asymmetry in the parameter values, _i.e._

_g_ _A_ = _g_ _B_ = _g,_

 1 _,A_ =  1 _,B_ =  1 _,_

 _',A_ =  _',A_ =  _'_ _._


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 101

Furthermore, the experimental energy scales correspond to the following hierarchies:


 qc __ _g,_

_J_ __ __ __ __  1 __  _'_


In order to make the calculation more transparent, we have made the additional approximation _!_ c = _!_ c such that  qc =  qc  qc . This is justified when  qc _J_ , which is not a


+ c = _!_ c


__ c such that  qc +



qc + =  qc



qc  qc . This is justified when  qc

__ __ __



_J_ , which is not a
__ __


particularly good approximation for our system (as we will see). However, this approximation does not qualitatively impact the features of the experiment, and it is straightforward
to describe the eects of this approximation not holding well. We will do so throughout this
section.


The non-linear light-matter coupling in _H_  _q,a_ can be eliminated by means of a second-


order perturbation theory in _g/_  qc using methods similar to the dispersive approximation
derived in Section 4.2.3. In the coupled-cavity case, the good unitary transformation is given
by _e_ _c_  where


 _A_
"


__  +


_A_ + +  __ _B_ +


__  +



_g_
_c_  =


 qc


+ _a_ 


_A_ + __  _B_ +

__ qc


 qc


+ h.c


(7.10)


Carrying through the transformation reveals a photon-mediated interaction between the
qubits, providing an experimental realization of a two-site transverse-field _XY_ model, as
in Eq. (7.2). We furthermore decompose the photon fields into mean fields plus bosonic
fluctuations: _A_  __ _A_  + _D,_   _a_ __ _a_  + _d,_  _N_  + _|_ _A_  _|_ 2 and _N_ __ _|_ _a_  _|_ 2 where, to the lowest order in

the light-matter coupling,


Carrying through the transformation reveals a photon-mediated interaction between the
qubits, providing an experimental realization of a two-site transverse-field _XY_ model, as
in Eq. (7.2). We furthermore decompose the photon fields into mean fields plus bosonic
fluctuations: _A_  __ _A_  + _D,_   _a_ __ _a_  + _d,_  _N_  + _|_ _A_  _|_ 2 and _N_ __ _|_ _a_  _|_ 2 where, to the lowest order in


2 __ d cos( _/_ 2)


2 __ d sin( _/_ 2)


_A_ _'_


 cd +
__



d cos( _/_ 2) _i_

cd + + _i_ + _/_ 2 and  _a_ _' _


 cd
__ __



cd + _i_ _/_ 2 _._ (7.11)

__ __


We neglect the resulting quadratic terms in the fluctuations which couple to the qubits, _e.g._
( _g/_  qc ) 2  _D_ __  _D_ __  _Z_ [61]. Notice that for fixed drive amplitude __ d at relevant drive frequencies


_i_ _Z_ [61]. Notice that for fixed drive amplitude __ d at relevant drive frequencies


_!_ d _< !_ c



c , the intra-cavity field is larger at the symmetric mode because the detuning is

__


smaller. As a result, the value of __ at which _N_ + = _N_ __ is not generically equal to __ __ _/_ 2.
Rather, it is given by


tan( _/_ 2) =  cd
__ __



cd __ _/_  cd +



cd + _._ (7.12)


This is one of the places in which the failure of the approximation _!_ c


+ c = _!_ c



c has an impact.

__


To maintain consistency with Schrieer-Wolperturbation theory we make sure to work


in regimes where the photon fluctuations are relatively small [202]. Altogether, this yields
the following Hamiltonian


with


_H_ = _H_ _q_ + _H_ _q,d_ + _H_ _d_ _,_ (7.13)
e e e e



**__** _i_
**_h_**
__ 2



_i_ 1

2 __ 2


_g_






2



_H_ _q_ =



_J_
2


 qc



[ __ _X_


_A_ _X_ __  _B_ _X_


_B_ _X_ +  __ _Y_


_A_ _Y_ __  _Y_


_B_ ] _,_ (7.14)


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 102

where


_h_ _x_



_x_

_A_ = 2 _g_



__ d cos( _/_ 2) _,_ _h_ _y_
 qc



_y_

_A_ = __ 2 _g_ 



d

_g_ __ sin( _/_ 2) _,_ (7.15)

 qc


_h_



_x_

_B_ = 2 _g_



d _y_

_g_ __ cos( _/_ 2) _,_ _h_

 qc



_y_

_B_ = 2 _g_



d

_g_ __ sin( _/_ 2) _,_ (7.16)

 qc


_h_



_z_ _A,B_ =   _qd_ _,_ (7.17)


 qd __  qd +  qc ( _g/_  qc ) 2
e h


__ d _/_  cd 2

 


1 +  cd _/_  qc

i


1 + 2


(7.18)


Equation 7.18 is a formulation of the ac-Stark shift on the qubits due to the presence of


the drive, such that  qd represents the detuning between the drive tone and the Stark-shifted

qubit frequency _!_ d . Under the approximation that  cd + __  cd __ it is independent of phase;

experimentally it has a slight phase dependence. Thus, we have derived and quantified the e


qubit frequency _!_ d . Under the approximation that  cd +

eective _XY_

e



cd + __  cd __



cd it is independent of phase;

__


experimentally it has a slight phase dependence. Thus, we have derived and quantified the
eective _XY_ coupling between the qubits that is mediated by the coupling between the
cavities.


The eigenstates of _H_ __ are, to first order in _g/_  qc ,

_g_ d

_T_ = e _T_ + _p_ 2 _/_ 2)


_g_ d


_T_ +

 e _S_


= _T_ + +
_|_ _i_



_/_ 2) _T_ 0 _i_ sin( _/_ 2) _S_ ] _,_
 qd  qc [cos( _|_ _i _ _|_ _i_


_g_ d
2 _i_ _/_ 2) [ _T_ + _T_ ] _,_

 qd  qc sin( _|_ _i |_ __ _i_


_g_ d
2 _i_


_S_

 _T_ e 0


= _|_ _S_ _i _

= _T_ 0
_|_ _i _

= _T_
_|_ __ _i _


(7.19)

(7.20)


_g_ d

_/_ 2) [ _T_ + _T_ ] _,_
 qd  qc cos( _|_ _i |_ __ _i_


_g_ d


_T_ 0

 _T_ e


_g_ d

_/_ 2) _T_ 0 _i_ sin( _/_ 2) _S_ ] _._
 qd  qc [cos( _|_ _i _ _|_ _i_


_g_ d


_T_
__


e



The corresponding eigenenergies of _H_ _q_ are

_E_ _T_ +  e qd

_'_


_E_ _T_ + _'_  qd + 2( _n_ + __ + + _n_ __ __ __ )

_E_ _ ,_
_S_

e _'_

_E_ e _ ,_


_E_ _ ,_
_S_
_'_

_E_
_T_ 0

e _' _


_E_ _ ,_
_T_ 0

_' _

_E_ 
_T_

e __ _' _


_E_ _T_ __ _' _  qd __ 2( _n_ + __ + + _n_ __ __ __ )
e

e


where __ _J_ ( _g/_  qc ) 2 and _n_ is the Fock state of the relevant coupled cavity mode. The
__ __
degeneracy between _S_ and _T_ 0 has been lifted by the eective photon-mediated qubit-qubit
_|_ _i_ _|_ _i_
interaction. The photon fluctuations on top of the coherent mean-field part are governed by
the quadratic Hamiltonian


_H_ _d_ =  cd +



cd + _D_  __  _D_ +  cd



cd _d_  __  _d._ (7.21)

__


We shall assume that these non-interacting degrees of freedom equilibrate with the outside
environment at zero temperature. Furthermore, these photon fluctuations couple to the


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 103

qubits via


_g_

 qc




2






_D_  __




1
_H_  _q,d_ =


__ d


 qc _/_  cd + + 1 _/_ 2


 qc _/_  cd


cos ( _/_ 2) ( __ _Z_


_A_ _Z_ +  __ _B_ _Z_


_B_ _Z_ ) _i_ sin ( _/_ 2) ( __ _A_ _Z_

__


_A_ _Z_ __  _B_ _Z_

__


_B_ _Z_ )





_d_ 



 qc _/_  cd + 1 _/_ 2

__


 qc _/_  cd


cos ( _/_ 2) ( __ _Z_


_A_ _Z_ __  _B_ _Z_

__


_B_ _Z_ ) _i_ sin ( _/_ 2) ( __ _A_ _Z_

__


_A_ _Z_ +  __ _B_ _Z_


_B_ _Z_ )


+ h _._ c _._

(7.22)


which induces transitions between the eigenstates of _H_ _q_ .

We integrate the photon-fluctuation degrees of freedom by treating

to _H_ _q_ e


We integrate the photon-fluctuation degrees of freedom by treating _H_ _q,d_ as a perturbation

_H_ _q_ and we derive the dynamics of the reduced density matrix of the qubit sector, __ _q_

Under standard assumptions, we obtain the following non-equilibrium steady-state Master e


to _H_ _q_ and we derive the dynamics of the reduced density matrix of the qubit sector, __ _q_

Under standard assumptions, we obtain the following non-equilibrium steady-state Master
equation [201] e


Under standard assumptions, we obtain the following non-equilibrium steady-state Master
equation [201]


_@_ _t_ __ NESS _q_


= 0 = __ _i_


_E_ _k_


_k_ _k_ _, _ NESS _q_
_|_ _i_ _h_ _|_


 _k_ _!_ _l_ _D_ [ _|_ _k_ _i_ _h_ _l_ _|_ ] __ NESS _q_


(7.23)


_kl_


where _k_ and _l_ span the eigenstates of _H_ _q_

 _k_ The  _l_ =  _b_ _k_ _k_ _!_ _l_ _l_ +  _d_ _k_ _l_ with e


The  _k_ _!_ _l_ s are steady-state transition rates between the qubit eigenstates. They read


 _k_ _l_ =  _b_
_!_



_b_ _k_ _!_ _l_ +  _d_ _k_



_d_ _k_ _!_ _l_ with


 1  1 0


 _b_ =


 __  1
__

 __ 


(7.24)


originating from the qubit decay and pure dephasing processes, and with the non-equilibrium
drive part given by


 _d_



_d_ _k_ _!_ _l_ = 2 __ _|_  + _kl_



+ _kl_ 2 __ + ( _E_ _k_ _E_ _l_ + _!_ d ) + 2 __  __

_|_ __ _|_



__ _kl_ _|_ 2 __ __ ( _E_ _k_ __ _E_ _l_ + _!_ d ) _,_ (7.25)


where


sin( _/_ 2)


cos( _/_ 2)


 + = __ +

in which


_,_  __ = __
__
C
A


_,_ (7.26)
C
A


sin( _/_ 2)


cos( _/_ 2)


2 ( _g/_  qc ) 2 __ d

2 ( _g/_  qc ) ( __ d _/_




__
__
__


1 _/_ 2 +  qc _/_  cd ;


2 ( _g/_  qc ) ( __ d _/_  qd ) cos __

2 ( _g/_  qc ) ( __ d _/_  qd ) sin __

e


__ __


(7.27)


2 ( _g/_  qc ) ( __ d _/_  qd ) sin __

e


__ __


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 104


Recall that __ ( _!_ ) here are the density of states of the bath modes. Matrix rows (columns)
__
are ordered according to that in equilibrium, _i.e._ __ _|_ d _T_ = 0, one has  __ _i_ , _|_ _T_ 0 _i_ , _|_ _S_ _i_ , and _d_ _k_ _!_ _l_ _|_ = 0. _T_ + _i_ from left to right (top to bottom). Note

One can re-write the SME (7.23) as the rate equations governing the population of each e e e e


that in equilibrium, _i.e._ __ d = 0, one has  _d_



_d_ _k_ _!_ _l_ = 0.


One can re-write the SME (7.23) as the rate equations governing the population of each


of the eigenstates _k_ of _H_ _q_ , _n_ _k_ _k_ __ _q_ _k_
_|_ _i_ _h_ _|_ _|_ _i_

_dn_ e NESS _k_ = 0 =


_dn_ NESS


_k_ = 0 =

_dt_


_n_ NESS


 _l_ _!_ _k_ _n_ NESS _k_  _k_ _!_ _l_ _,_ (7.28)
__


which in conjugation with the conservation law

P


non-equilibrium steady-state fidelities, by-passing the transient dynamics.


_k_ _n_ _k_ = 1, provides a direct access to the


### 7.2.3 ### Protocol for generating entanglement


By judiciously tuning the drive frequency amplitude __ d , frequency _!_ d , and phase __ , one can
drive the qubit subsystem to one of the maximally entangled eigen-states. We will discuss the
protocol to achieve convergence to the singlet state, __ NESS _S_ _S_ and compute its fidelity


_S_


e



and compute its fidelity




_S_


e



_n_ NESS


__ NESS _q_

_!_





. The extension to cooling to the triplet state is straightforward.


By selecting _!_ d such that _!_ d = _!_


__ c + _E_ _S_ __ _E_ _T_ __ , _i.e._ _!_ _|_ d

e e



c + _!_ q + 2 __ + __

__

_/_ ( __

__

e


_|_ d _S_ _i_ ( __ ) __ 1 2


_!_ c


, the


__ term in the expression of  _d_
__


we have a maximal pumping rate



_d_ given in Eq. (7.25) is maximized to 2 _/_ ( __ ). Therefore,

_T_ e __ _!_ _S_ e __


_g_

 qc




_g_






6 __ d 4

( qc

 
  


cos 2 ( __ )

__
__






_d_ 400

_T_ _S_
e __ _!_ e __


( qc ) 2


(7.29)


The mechanism associated with this rate corresponds to a two-photon process in which the
incoming energy is used to add a photon in the antisymmetric cavity mode and simultaneously perform a qubit transition from _T_ to _S_ (Stokes scattering). Note that the phase


_T_
__


e



_S_


e



to


(Stokes scattering). Note that the phase


at which  _d_



_d_ _T_  __ _!_ _S_  goes to zero when cooling via the antisymmetric cavity mode is exactly


equal to _/_ 2 in this derivation because we have approximated  cd



cd + __  cd __



cd . Experimentally,

__


when this equality does not hold, the phase at which the transition rate goes to zero is given
by Equation 7.12.


By selecting _!_ d such that _!_ d = _!_


+ c + _!_ q + 2 __ + __

e


_|_ d _S_ _i_ (+) __


+ c + _E_ _S_ __ _E_ _T_ __ , _i.e._ _!_ _|_ d

_S_ e e


_!_ c


, it is


the __ + term in the expression of 


the pumping rate is given by,



_d_ given in Eq. (7.25) which is maximized. Therefore,

_T_ e __ _!_ _S_ e


_g_






6 __ d 4

( qc )

 
  


 _d_


sin 2 ( __

__ +



_d_ 400

_T_ _S_
e __ _!_ e __


 qc


( qc ) 2


(7.30)


Here, it is the symmetric-cavity mode which is used in the Stokes scattering process. Noting
that this transition rate goes to zero at __ = 0 and at __ = __ .


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 105


In both cases, if the condition  _d_



_d_ 

_T_ _S_
e __ _!_ e __



_d_ _S_ _!_ _T_ __ =  1 is met, this facilitates a rapid pump-

e e _S_ via Stokes (red-shifted) scattering.


_T_
__


e



_S_


e



ing from the ground state


to the singlet state


via Stokes (red-shifted) scattering.


_S_


e



_T_ +


e



One must also avoid o-resonant pumping from


to the


state, labeled as  _d_


here. Altogether, the cooling to the singlet state is achieved with high fidelity whenever the
hierarchy


_S_ e _!_ _T_ e +


 _d_



_d_ _S_ _T_ +  1  _d_

_!_ __ __
e e _S_ to _T_ +


(7.31)
_T_ e __ _!_ _S_ e


is obeyed where the o-resonant rate from _S_ to _T_ + is given by

 _d_ 25( _g/_  qc ) 2 ( __ d 2 _/_  qc _J_ ) 2 __

_T_ __ _!_ _S_ __ e e __


__ d 2 _/_  qc _J_ ) 2 __ cos 2 ( __ ) (7.32)
__
 
 


 _d_


or



_d_ 25( _g/_  qc ) 2 (

_T_ _S_
e __ _!_ e __


 _d_



_d_ _T_ _S_ 25( _g/_  qc ) 2 ( __ d 2 _/_  qc _J_ ) 2 __ + sin 2 ( __ ) (7.33)

e __ _!_ e __ _|_ _|_


depending whether the antisymmetric or the symmetric cavity mode is used. The condition
(7.31) transparently elucidates that the fidelity is the result of a delicate interplay between
drive, cavity decay, qubit dissipation and light-matter coupling. In particular, __ d enters both
sides of the inequality above, and thus, large fidelity is obtained in a finite window of the
drive strength __ d .


In regimes where all the o-resonant rates ares strongly suppressed compared to the other


_T_
__


e



_S_


e



rates involved, _i.e._  _d_



_d_ _k_ _!_ _l_ __ 0 except from


to


, the steady-state population of the


singlet state can be approximated to


1 +  __ _/_ 


_S_


e



_n_ NESS


__ NESS _q_




1 + 2 __ _/_ 


1 +  1 _/_  _d_


(7.34)


_T_ e __ _!_ _S_ e


Therefore, if the hierarchy given in Eq. (7.31) is satisfied, the maximum steady-state fidelity
to cooling to the singlet state simply reads


_n_ max


1 + 2 __ _/_ 


(7.35)


This result clearly highlights that, in contrast to the the dephasing rate  __
which is detrimental to the protocol, the dissipative qubit decay process is instrumental in achieving large
fidelities.

In this section, we have seen that the coupled cavity Hamiltonian that we realize here gives

rise to natural exchange symmetries in the dissipation mechanisms. We can purposefully
harness these symmetries order to turn a given entangled state into a symmetry-protected
state under the bath drive, or conversely, in order to suppress the state. We have rigorously
derived the drive dynamics using a master equation approach, and have examined the steadystate populations in order to provide an estimate for the degree of entanglement we expect
to produce under a detailed balance picture. The expected entangled state populations can
be quite large, if the rates are well tuned: we can hope to generate significant entanglement
using this protocol.


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 106

Table 7.1: Calibrated experimental parameters

|!c/2 +|6.9524 GHz|
|---|---|
|!c/2 |7.2310 GHz|
|!q/2|6.2000 GHz|
| /2 +|650 kHz|
| /2 |820 kHz|
| /2 A|-210 MHz|
| /2 B|-210 MHz|
|J/2|139.3 MHz|
|g /2 A|89 MHz|
|g /2 B|98 MHz|
|T 1,A|4 s|
|T 1,B|7.2 s|
|T 2,A|2.6 s|
|T 2,B|3 s|



## 7.3 ## Full Experimental Calibration

As always, a full calibration of the experimental setup is critical for understanding and predicting the behavior of quantum system under the presence of the bath drives described
above. Here, we provide a full accounting of the experimental system design and char-


acterization methodologies. The full set of relevant qubit and cavity parameters include
the coupled cavity mode frequencies ( _!_ c ); the cavity-cavity coupling ( _J_ ); the qubit anhar-



c ); the cavity-cavity coupling ( _J_ ); the qubit anhar-

__


monicities ( __ _i_ ); the qubit-cavity couplings ( _g_ _i_ ); the symmetric and antisymmetric cavity
linewidths ( __ __ ); and the qubit lifetimes ( _T_ 1 _,i_ ) and dephasing times ( _T_ _,i_ ). These parameters
are tabulated in Table 7.1.


### 7.3.1 ### Detailed Experimental Setup

There are three principal drives used in this experiment (Figure 7.4), generated by APSIN
and Agilent microwave generators. The readout drive (purple block) is mixed at DC with
readout pulses generated by a marker output of a Tektronix AWG520 two-channel arbitrary
waveform generator (AWG); amplified to achieve sufficient power for high-power singleshot readout [135]; gated by a fast switch to avoid excessive qubit dephasing from readout
leakage; and sent through a LabBrick digital attenuator for fine-tuning of readout amplitude.
The readout is combined with qubit and cooling drive pulses that are input at cavity _B_ .
Additionally, half of the generator output signal serves as the local oscillator (LO) for an IQ
demodulator for homodyne detection of the readout signal.

The qubit drives are generated by a microwave source at 6.075 GHz. This drive serves


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 107


3 dB Splitter

Fast Switch

Isolator

RF Generator

Arbitrary
Waveform
Generator


![SchwarzThesis.pdf-118-0.png](SchwarzThesis.pdf-118-0.png)

![SchwarzThesis.pdf-118-1.png](SchwarzThesis.pdf-118-1.png)

-10 dB Fixed
Attenuator

Variable
Attenuator

Variable
Phase Shifter

Room-Temp
Amplifier


LNF
HEMT

IQ Mixer/
Demodulator


|I RF IF RF|Q LO LO|
|---|---|



Single-Sideband
Mixer

K&L Low-Pass
Filter

Lossy IR Filter

|IF RF S|SB LO|
|---|---|

|SSB Pulses LO RF IF AWG Qubit IF SSB LO RF Digitizer Digitization Q LO I RF and RF Readout IF (x2) LO Input B Input A|Col2|Col3|Col4|
|---|---|---|---|
|||||
||||70 K|
|LN|dB F -20|-20 dB|4 K|
||-10 dB|-10 dB|1 K|
||||100 mK|
|30 mK dB dB -20 -20 K&L IR-Shielded Can (x3)||-20 dB||
|||IR-Shielded Can||


Figure 7.4: Experimental setup. Not shown is an SRS DG535 Digital Delay Generator, which
is responsible for triggering the AWG (which generates qubit rotations and gated readout
pulses), the cooling drive generator, and the Alazar digital acquisition card.


AWG


LNF


K&L


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 108

as the LO for two single-sideband modulators (SSBs) optimized for upper sideband signal
output. The two channel outputs of the AWG generate qubit rotation pulses at 125 MHz,
with _X_ - and _Y_ - rotations defined by the relative starting phases of the pulses; these are
mixed up to 6.2 GHz, the operating frequency of the qubits. Since the qubits are resonant,
the dierence in path length between the generator and the two cavity inputs is important;
we describe the calibration of this angle in the next section. Qubit pulse amplitudes are
calibrated via the AWG.

The cooling drive is split in two: the tone that is sent to cavity _A_ passes through a digital

attenuator for amplitude balance, and the drive _en route_ to cavity _B_ passes through a digital
phase shifter to enable facile manipulation of the symmetry of the drives.

The timing of the experiment is controlled by an SRS DG535 digital delay generator (not

shown). the DG535 serves three purposes: it gates the cooling drive generator, setting the
start and length of the cooling operation; it triggers the AWG to perform qubit rotations
and readout; and it triggers the Alazar digital acquisition card to accept input data.

The qubit, cavity, and cooling drives are thermalized to base by 20-, 10-, and 20- dB

attenuators thermalized to the 4 K, 1 K, and 30 mK stages of a closed-cycle He-3 dilution
refrigerator. At base, they are further filtered for stray infrared (IR) by homemade lossy
Eccosorb filters, and input into a secondary copper containment canister containing the coupled cavity system. This can is indium-sealed and coated with further IR-absorbing material.
The coupled-cavity output passes through three cryogenic isolators and a commercial K&L
low-pass filter at base. It is then amplified by a Low Noise Factory HEMT at 4 K and by
two room-temperature amplifiers before being demodulated and digitized.

### 7.3.2 ### Coupling of the cavities

The cavities are designed with dimensions of 1.20 x 0.20 x 1.00, with the long axis
terminated cylindrically at both ends with a diameter of 0.20 inches (see Figure 7.1). HFSS
modal analysis predicts these cavities to have a TE 101 mode at 7.2 GHz in the absence of
a qubit chip. The measured resonator frequency in the presence of a qubit chip is 7.114
GHz at base temperature; the silicon chip lowers the cavity frequency due to the silicon
dielectric. The two cavities are machined in HOFC copper and are coupled by an aperture
on the transverse axis of width 0.04 and height 0.52. HFSS modeling again predicts that
this aperture will couple the two cavity modes with a splitting 2 _J_ = 290 MHz, where the
magnitude of _J_ is highly sensitive to the machining tolerances of the cavity. This compares
well to 2 _J_ = 280 MHz that we measure experimentally.

Since we cannot separate the cavities to directly measure their bare frequencies, we

manually fine-tune the cavity frequencies by referring to the avoided crossing between them,


which results in two coupled cavity modes at _!_ c



c = 1

__


2 ( _!_ c


_A_ c + _!_ c


_B_ c ) 1 2

__


( _!_ c


_A_ c _!_

__


_B_ c ) 2 + 4 _J_ 2 . The


splitting between the two modes is minimized when the cavities are exactly on resonance
( _!_ c = _!_ c ). By slightly adjusting the positions of the qubit chips and employing standard _S_


_A_ c = _!_ c


_B_ c ). By slightly adjusting the positions of the qubit chips and employing standard _S_ 21


transmission measurements to find the coupled cavity modes, we minimize this splitting and


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 109


thus tune the cavities to resonance. These fine adjustments are on the order of millimeters,
and correct for minor inhomogeneities in machining as well as for chip size mismatch. The
coupling of the cavities shifts the spatial mode structure of the symmetric and antisymmetric
modes, leading to unequal photon decay rates __ via the strongly-coupled output port. We
calibrate _!_ c and __ via a standard transmission measurement, as shown in Figure 7.2. __

__ __

### 7.3.3 ### Qubit parameters


The qubit-cavity couplings _g_ _i_ are calibrated by measuring the cross-Kerr nonlinearity of the
antisymmetric mode ( __ ) as a function of qubit-cavity detuning. Unlike in Chapter 5, the
__
ratio _|_ __ _|_ _/_ is quite large, so the __ -calibration method described in Section 5.4 cannot be used.
Instead, we calibrate __ by performing two-tone qubit spectroscopy (as in Figure 7.2b) at a
slightly higher readout power, such that the photon number occupation of the measurement
mode ( _!_ c , in this instance) is equal to _n_ 0 _._ 5. The experiments are performed in the



c , in this instance) is equal to _n_ 0 _._ 5. The experiments are performed in the

__ __


photon number-resolved limit ( _ > ,_ 1 _/T_ 2 ), such that we can resolve two spectral lines at
_!_ q _n_ =0 and _!_ q _n_ =1 , which are split by 2 __ . The splitting __ is related to _g_ by
_|_ __ _|_ __ __ __


__ =
__


( qc + __ )

__


( qc


_g_ 2

 qc


(7.36)


Here, __ is the transmon nonlinearity. We sweep the bias coils that independently govern


the qubit frequencies and plot 2 __ as a function of  qc
_|_ __ _|_ _|_ __



for both qubits independently.
__ _|_


Fitting to Equation 7.36 provides the fit shown in Figure 7.5(c-d) and tabulated in Table
7.1. We extract a fit for both __ and for __ ; the fits for __ are consistent with independent
__
calibrations accomplished by high-power two-tone spectroscopy that drives the two-photon
_g_ _f_ transition. Note that we can also independently calibrate __ + , the cross-Kerr
_|_ _i ! |_ _i_


coupling to the symmetric cavity mode, and from it extract _g_ _i_ and __ _i_ ; we do not show
these fits here, but they are quantitatively consistent with _g_ _A_ _, g_ _B_ as extracted from the
_{_ _}_
__ calibration.
__


The bare (uncoupled) qubit coherence times _T_ 1 _, T_ 2 are calibrated via standard _T_ 1 and


Ramsey measurement protocols. These measurements are performed for each qubit at the
operating frequency of 6.2 GHz, while the qubit not under test is detuned by 50 MHz and
is therefore unaected by qubit excitation pulses at 6.2 GHz. This detuning is additionally
important because when the qubits are on resonance, an excitation in Qubit A will begin
to oscillate coherently into Qubit B; we would like to avoid these oscillations in order to
characterize the bare qubit parameters. The Purcell limit is set by the photonic density of
states at the individual qubit positions, summed over all the normal modes of the system.
The qubits couple most strongly to the symmetric and antisymmetric combinations of the
TE 101 modes, but the higher-order modes also participate. The total Purcell decay limit
on _T_ 1 considering only the lowest two modes is approximately 8-10 __ s (although we note
that the 3D multimode Purcell eect typically reduces Purcell decay when the qubits are
red-detuned from the fundamental cavity mode due to interference between the modes).


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 110


**Qubit A Spectroscopy**

![SchwarzThesis.pdf-121-6.png](SchwarzThesis.pdf-121-6.png)

![SchwarzThesis.pdf-121-0.png](SchwarzThesis.pdf-121-0.png)

-10 -5 0 5 10

Coil Current (mA)


**Qubit B Spectroscopy**

![SchwarzThesis.pdf-121-7.png](SchwarzThesis.pdf-121-7.png)

![SchwarzThesis.pdf-121-1.png](SchwarzThesis.pdf-121-1.png)

-10 -5 0 5 10

Coil Current (mA)

![SchwarzThesis.pdf-121-5.png](SchwarzThesis.pdf-121-5.png)

400 600 800 1000


6.6

6.4

6.2

6

14

12

10


6.6

6.4

6.2

6

25

20

15

10


![SchwarzThesis.pdf-121-2.png](SchwarzThesis.pdf-121-2.png)

![SchwarzThesis.pdf-121-3.png](SchwarzThesis.pdf-121-3.png)

![SchwarzThesis.pdf-121-4.png](SchwarzThesis.pdf-121-4.png)

400 500 600 700 800 900


(MHz) (MHz)

Figure 7.5: Calibration of the qubit-cavity couplings _g_ _i_ . We sweep the qubit frequency and
measure the cross-Kerr nonlinearity of the antisymmetric cavty mode ( __ ) as a function of
__
qubit-cavity detuning for qubit _A_ (panels a, c) and _B_ (panels b, d). This provides a fit of _g_ _i_
as per Equation 7.36. The outlier points in Panel d result from an avoided crossing as qubit
_B_ tunes through qubit _A_ .


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 111

The coherence times we achieve are shorter than state-of-the-art 3D transmons, although

_T_ 1 is near the single-mode Purcell limit. However, note that _T_ 1 is built as a feature into
our cooling protocol, as it depopulates unwanted qubit states, and _T_ __ , the pure dephasing


rate that can be extracted from 1

_T_ 2


= 1

_T_


= 1


2 _T_ 1


, is lengthened by a factor of 10 or more by


the lifting of the degeneracy between the _S_ and _T_ 0 states when the qubits are tuned to
_|_ _i_ _|_ _i_
resonance, as we will see in Section 7.4. Lifting this degeneracy implies that the noise that
couples these two states is no longer at DC, but is in fact the noise at _!_ = 2 __ . This eect
provides protection from low-frequency noise, and results in an increased eective phase
coherence between _S_ and _T_ 0 .
_|_ _i_ _|_ _i_

### 7.3.4 ### Path length calibration

Because the qubits are tuned to degeneracy, the qubit pulses are performed in the same
rotating frame. It is critical to properly calibrate the path length dierence between pulses
arriving at cavities in order to ensure that pulses are performed along common Xand Y-axes. In principle, we can use our knowledge that the higher-energy state to which _A_ and _B_
we cool using our bath engineering scheme is the _|_ _S_ _i_ state, but we also must independently
verify this hypothesis.

We follow the methods in the supplementary material of Ref. [26]: noting that the _XY_


Hamiltonian drives oscillations between _ge_ and _i_ _eg_ , we perform a _R_ _X_ _/_ 2
_|_ _i_ _|_ _i_


_A_ , along with a _R_ _/_ 2


rotation about an arbitrary axis on qubit _B_ , and then allow the coupled


rotation on qubit


qubit state to freely evolve, performing tomographic reconstructions along the way in order
to resolve the joint density matrix __ ( _, t_ ). When __ = _/_ 2 (that is, when we perform a qubit
_B_ rotation about the true y-axis), the oscillation amplitudes between __ ge _,_ ge and __ eg _,_ eg (that
is, the qubit populations in _|_ _ge_ _i_ and _|_ _eg_ _i_ , respectively) are maximized, and oscillations are
minimized at __ = _{_ 0 _, _ _}_ . We perform a first Rabi oscillation measurement at arbitrary __ ; we
then fix the Rabi oscillation time to a maximum of __ ge _,_ ge and sweep __ . We add a constant
phase oset to the qubit rotation pulses applied to qubit _B_ such that the oscillations are
suppressed at __ = _{_ 0 _, _ _}_ (Figure 7.6).

### 7.3.5 ### Balancing the cooling drive amplitudes


Achieving symmetry-selective bath engineering in our experimental setup requires a careful
calibration of the relative drive amplitudes inside the two cavities, such that the two-photon
coherent driving rate is the same for both qubits. If the cavity input amplitudes are not
properly balanced, then even when the phases are properly aligned (say, fully symmetrically),
the excess drive in one of the cavities means that the decomposition of the total drive
into symmetric and antisymmetric drives will have a nonzero amplitude in the undesired
component (antisymmetric, in this case). This reduces the symmetry selectivity, so balancing
the cavity amplitudes is critical. Quantitatively, this condition is met if _g_ 2 _n_ = _g_ 2 _n_ , or


_A_ 2 _n_ _A_ = _g_ 2


_B_ 2 _n_ _B_ , or


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 112

0.6


0.5

0.4

0.3

0.2

0.1


![SchwarzThesis.pdf-123-0.png](SchwarzThesis.pdf-123-0.png)

50 100 150 200 250 300 350

Angle of Qubit B Rotation


Figure 7.6: Calibration of the relative path lengths of qubit pulses. We prepare the qubits
using _R_ _/_ 2 on qubit _A_ and _R_ _/_ 2 on qubit _B_ , and fix the free evolution time to __ = 400 ns,


on qubit _A_ and _R_ _/_ 2


on qubit _B_ , and fix the free evolution time to __ = 400 ns,


where we find a maximum in the oscillation amplitude between __ ge _,_ ge and __ eg _,_ eg . We then
vary __ and fix an oset such that the amplitude of oscillation is damped at __ = _{_ 0 _, _ _}_ .

alternatively, if


_g_


__ _A_ _P_ _in_


__ _B_ _P_ _in_


where we emphasize that _P_ _in_


is a controllable parameter and is related to __ d


__ _A_ _P_ _A_ _in_ = _g_ _B_

_!_ c __ _!_ d


_._ (7.37)
_!_ c __ _!_ d



d _i_ by


__ _i_ _P_ _i_ _in_


= __ d _i_ 2 _._ (7.38)
_|_ _|_


= __ d _i_
_|_


Several of these parameters are not experimentally measurable - in particular, we cannot


independently extract the cavity decay rates __ _i_ because the resonances that we measure are
hybrids of both cavity modes and are aected by both . Therefore, we use pumpprobe spectroscopy of the bath engineering drive to directly balance the drive amplitudes __ _A_ and __ _B_
(Figure 7.7). We adjust the relative phase of the drives to __ = __ such that the drive is fully
antisymmetric; we then sweep the cooling drive across the expected frequencies for cooling
to both _|_ _S_ _i_ and _|_ _T_ 0 _i_ . In Figure 7.7, we calibrate the drive amplitudes for cooling via _!_ __ c



c

__


the antisymmetric cavity mode; in this case, we expect _T_ 0 to be a forbidden state when
_|_ _i_
the amplitudes are properly balanced. We choose the digital attenuation setting that best
suppresses _T_ 0 as our operating point (as indicated by the arrow). A similar, independent
_|_ _i_


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 113

6.72


6.71

6.7


![SchwarzThesis.pdf-124-0.png](SchwarzThesis.pdf-124-0.png)

![SchwarzThesis.pdf-124-1.png](SchwarzThesis.pdf-124-1.png)

10 12 14 16 18 20

Digital Attenuator (dB)


Figure 7.7: Calibration of the relative cooling drive amplitudes. Here, we cool via _!_ c



c and

__


fix __ = __ , such that we expect _T_ 0 to be fully suppressed when the drive amplitudes are
_|_ _i_
balanced. We perform spectroscopy of the cooling drive while varying the set point of the
digital attenuator that controls the relative amplitude of the two cavity drives. Away from
the ideal balance, both the upper and the lower cooling lines appear; however, when the
drives are balanced (arrow), symmetry selectivity suppresses _T_ 0 . The red-shifting of the
_|_ _i_
cooling frequencies that occurs at lower attenuator settings is due to the AC Stark eect.


calibration is performed when cooling via _!_ + c , in order to account for any potential frequency-


calibration is performed when cooling via _!_ c


dependent losses in the system.

### 7.3.6 ### Tomography calibration


Tomography in this experiment is performed, as in Chapter 5, based on the method outlined in Chow et al. [181]. Because the cavity bandwidth is narrow, we use high-power
readout [135] that is optimized to discriminate the joint ground state _|_ _gg_ _i_ from the other
three eigenstates of the system. Thus, unlike in the measurement-induced entanglement and
trajectories experiments, we do _not_ have access to the _|_ _ee_ _i_ population: we must base our
tomography only on readout of the _|_ _gg_ _i_ state. Also note that because high-power readout
is a latching measurement that involves flooding the cavities with tens of thousands of photons, it is not possible to use it to do a ground-state heralding measurement. Thus, in these
experiments we have no post-selected state initialization.


__ _ZI_ __  _ZI_ + __ _ZZ_ __  _ZZ_ , where the __ -coefficients are calibrated using the double-Rabi oscillation


The high-power readout accomplishes a measurement of the form = __ _II_ __  _II_ + __ _IZ_ __  _IZ_ +
_M_


method in the previous reference. We perform a set of 30 (overspecified) positive and negative


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 114

1 0.9 0.8 0.7

![SchwarzThesis.pdf-125-2.png](SchwarzThesis.pdf-125-2.png)

![SchwarzThesis.pdf-125-3.png](SchwarzThesis.pdf-125-3.png)

after crosstalk correction

0

100


200

300


![SchwarzThesis.pdf-125-0.png](SchwarzThesis.pdf-125-0.png)

![SchwarzThesis.pdf-125-1.png](SchwarzThesis.pdf-125-1.png)

0 0.1 0.2

Relative Pulse Amplitude

Figure 7.8: Calibration of the qubit pulse cross-talk. We apply the equivalent of a __ -

pulse to Cavity A while Qubit A is detuned, and implicitly measure the eect on Qubit
B by performing crosstalk correction pulses at swept relative amplitude (x-axis) and phase
(y-axis). The point at which the ground-state population is maximized (yellow) indicates
that the cross-talk rotation has been corrected. The color scale indicates the ground-state
population.

qubit rotations in order to fully determine the 15 degrees of freedom of the density matrix,
and use maximum likelihood estimation to infer the trace-normalized, positive-semidefinite
density matrix that is consistent with our tomographic data. In order to accomplish singlequbit pulses despite the resonant coupling of the qubits, we apply 32-ns qubit pulses such
that the pulse envelope is broader than the qubit splitting, enabling single-qubit rotations.
While the qubit coupling induces mixing between the _|_ _ge_ _i_ and _|_ _eg_ _i_ states, it does not aect
the _|_ _gg_ _i_ population from which we infer the density matrix; this limits the eect of the qubit
coupling on tomographic reconstruction.

Finite-element simulations show that a pulse at the qubit frequency, when applied to

a given cavity, remains localized in that cavity and does not propagate to the neighboring
cavity. However, we would like to calibrate _in-situ_ the qubit pulse cross-talk (i.e. the amount
by which a rotation on Qubit A will also rotate Qubit B). To do so, we calibrate a __ -pulse
on Qubit A, and then detune it by 50 MHz so that the pulse does not in fact aect the
state of Qubit A. We then (Figure 7.8) apply compensating pulses to Qubit B at a swept
amplitude and frequency. When the _|_ _gg_ _i_ population is maximized (yellow), the crosstalk
has been undone; this provides a direct calibration of the crosstalk. We see a slight phasedependence in the data, indicating that the crosstalk occurs at a relative phase of 250 __ ,


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 115

Cavity A

Cavity B

|Col1|Col2|Col3|Col4|Col5|Readout|
|---|---|---|---|---|---|
|||||||



Figure 7.9: Pulse sequence. A bath tone (blue) is applied, for varying time __ and with
varying relative phase __ ; a set of tomography pulses are performed, followed by a readout in
order to reconstruct the density matrix.

and estimate that the amplitude of the crosstalk is less than 5%. The fact that we do both
positive and negative tomographic rotations partially corrects for this crosstalk, as the two
sets of rotations will induce opposite cross-talk.

## 7.4 ## Experimental Implementation of the Bath Engineering Protocol

With a fully calibrated experimental system, we can now proceed to realizing the symmetryselective bath engineering protocol. The pulse sequence used to implement the protocol


is shown in Figure 7.9. We apply simultaneous, amplitude-balanced drives with a relative
phase __ to the input of the cavities. In a first experiment, we apply the bath drive for a fixed
interval of __ = 10 __ s, and sweep the drive frequency ( _!_ d , _y_ -axis) and relative phase ( __ , _x_
axis). We then reconstruct the joint qubit density matrix __ using tomographic reconstruction
techniques [26, 181] based on high-power readout [135]. Figure 7.10 shows the fidelity to _|_ _S_ _i_
(red) and to _T_ 0 (blue), where the fidelity to a target state is given by = __ .
_|_ _i_ _|_ _i_ _F_ _h_ _|_ _|_ _i_
We use fidelity here instead of concurrence because, unlike in Chapters 5 and 6, we are
specifically concerned here not with just the quality of the entanglement, but the specific
entangled state generated. In this context, a fidelity _F _ 0 _._ 50 corresponds to nonzero

concurrence, and therefore is a confirmation of entanglement.

The _symmetry-selective_ aspect of the protocol manifests at three symmetry points. In


particular, there are four bands in which the protocol achieves entanglement, corresponding to the frequencies in Equation 7.4: entanglement via _!_ c ( _!_ c ) occurs at _!_ d = 2 __


+ c ( _!_ c



c ) occurs at _!_ d = 2 __

__ __


6 , the resonant transitions are selectively suppressed for one of the target states, and the suppressed _._ 572 (6 _._ 713) __ 0 _._ 0013 GHz. However, at __ = 0 _, _ = __ , and __ __ 180 __ __ 67 __
states are reversed between the _!_ c and _!_ c cooling bands. At these symmetry points, the


+ c and _!_ c



c cooling bands. At these symmetry points, the

__


frequency-crowding of the qubit spectrum is alleviated: it is eectively lifted from __ to _J_
representing two orders of magnitude of improvement.


Under an even-parity drive, when the cooling drive is comprised of two symmetric or two

antisymmetric photons ( _i.e._ __ = 0 or __ ), we can only cool to the qubit state whose parity is


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 116

6.715

6.71

![SchwarzThesis.pdf-127-2.png](SchwarzThesis.pdf-127-2.png)

![SchwarzThesis.pdf-127-1.png](SchwarzThesis.pdf-127-1.png)

_6_


6.705

6.575

6.57

_6_


![SchwarzThesis.pdf-127-0.png](SchwarzThesis.pdf-127-0.png)

![SchwarzThesis.pdf-127-3.png](SchwarzThesis.pdf-127-3.png)

![SchwarzThesis.pdf-127-4.png](SchwarzThesis.pdf-127-4.png)

![SchwarzThesis.pdf-127-5.png](SchwarzThesis.pdf-127-5.png)

Figure 7.10: Symmetry- and frequency- selective bath engineering. We plot _S_ _T_ 0 such
_F_ _|_ _i_ _F_ _|_ _i_
that _S_ is red and _T_ 0 is blue. At the symmetry points __ = 0 _, _ = __ , and _n_ + = _n_ , the
_|_ _i_ _|_ _i_ __
drive is both frequency- and symmetry- selective. The 1 2 notation indicates the
_|_ _i $ |_ _i_
transition with which the drive is resonant for the labelled band. Transitions between higher
cavity occupation states are red-detuned by __ + = __ 2 __ __ 2.5 MHz for the lower-frequency
bands, and __ = 2 __ 1.4 MHz for the higher-frequency bands.
__ __ __

_6_


the same as the cavity output photon. Indeed, population in the antisymmetric _|_ _S_ _i_ is fully
suppressed in the lower (symmetric) band at __ = 0 _, _ , and _T_ 0 is similarly suppressed in
_{_ _}_ _|_ _i_
the upper band (where the scattered photon is antisymmetric). There also exits a relative
phase at which the drive is comprised equally of symmetric and antisymmetric photons,
leading to an overall odd-parity drive. This phase is which diers from __ __ _/_ 2 because of the detuning __ _!_ __ __ c 180 = _6_ _!_ __ + c __ , and is well-predicted by 67 __ in these experiments,



c = _!_

__ _6_


+ c , and is well-predicted by

_6_



_6_

Equation 7.12. At these phases, the parity of the target qubit state must be _opposite_ that
of the cavity output photon. Cooling to _T_ 0 occurs only via the antisymmetric mode in this
case, and cooling to _S_ occurs via the _!_ _|_ + _c_ mode. These symmetry restrictions are lifted for _i_
_|_ _i_



_6_

+ _c_ mode. These symmetry restrictions are lifted for



_6_

generic __ , in which case both cavity modes can be equivalently used to target _T_ 0 or _S_ , and
_|_ _i_ _|_ _i_
only energy conservation of input and output photons is required. Thus, simply by tuning a
readily-adjustable drive parameter, we turn a given entangled state from a forbidden into a
symmetry-protected state.



_6_

The undulation in the cooling bands is an eect of the phase-dependence of  _!_ q , due to



_6_

the detuning between _!_ c



_6_

+ c and _!_ c



_6_

c : a drive of fixed amplitude is closer in frequency and there-

__


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 117

**a**

1

0.8

0.6

0.4

![SchwarzThesis.pdf-128-2.png](SchwarzThesis.pdf-128-2.png)

0.2

![SchwarzThesis.pdf-128-3.png](SchwarzThesis.pdf-128-3.png)

0

![SchwarzThesis.pdf-128-0.png](SchwarzThesis.pdf-128-0.png)

0 10 20 30 40 50

**b**

1

0.8

0.6

0.4

![SchwarzThesis.pdf-128-4.png](SchwarzThesis.pdf-128-4.png)

0.2

![SchwarzThesis.pdf-128-5.png](SchwarzThesis.pdf-128-5.png)

0

![SchwarzThesis.pdf-128-1.png](SchwarzThesis.pdf-128-1.png)

0 10 20 30 40 50

Figure 7.11: Cooling dynamics. (a) We prepare _|_ _S_ _i_ using __ = __
by cooling via the antisymmetric cavity mode (inset). (b) Similarly, we prepare _T_ 0 using __ = __ via the symmetric
cavity mode. In both cases, we fix ; and then tomographically reconstruct the resultant joint qubit state. The experimental data are represented as __ and _!_ d ; apply the drive for time _|_ _i_ __
dots; solid lines are fits to a coupled rate equation with rates as noted. The preparation of
_S_ reaches maximum entanglement in approximately 3.5 __ s; _T_ 0
_|_ _i_ _|_ _i_
reaches maximum entanglement in 3.8 __ s.

fore coupled more strongly to the lower-frequency symmetric mode, resulting in a stronger
AC Stark shift at __ __ 0. The broadening of the cooling spectrum at __ = 0 represents the
same phenomenon, this time manifesting as power-broadening. The faint red-shifted cooling bands, detuned by __ , represent cooling between higher photon-number subspaces, as
__
labeled.


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 118

By moving to the time-domain (Figure 7.11), we can resolve the eects of the several


dynamical rates that govern the non-equilibrium steady state. For each experiment we fix
_!_ d and __ , and apply the bath drive for a variable time __ , again finally tomographically
reconstructing the joint qubit state. We utilize __ = __ such that parity rules require cooling
to _|_ _S_ _i_ ( _|_ _T_ 0 _i_ ) via _!_ __ c _!_ + c . The dominant rates in the system are  _p_ , the pumping rate from


_!_ c


. The dominant rates in the system are  _p_ , the pumping rate from


_T_ to the target state;  _0_
_|_ __ _i_



_0_ _p_ , a weak o-resonant pumping to _T_ + ;  1 , the spontaneous decay

_|_ _i_


rates of the qubits; and  __ , the eective dephasing rate between _S_ and _T_ 0 . Provided
_|_ _i_ _|_ _i_
that we meet the inequality  __ _,_  _0_ _<_  1 _<_  _p_ , we expect the steady-state population to be



_0_ _p_ _<_  1 _<_  _p_ , we expect the steady-state population to be


entangled. We fit the data to a coupled rate equation and extract the pumping and decay
rates. The quality of the fit to a simple exponential indicates that the dynamics of this
system are dominated by incoherent processes, which is consistent with __ __  _p_ : in this
__
regime, photons stochastically leak from the cavity much more quickly than the drive is able
to repopulate them.

The steady state saturates to the entangled state of choice after a transient ring-up

(dominated by  _p_ ) and a small-overshoot (related to  __ ). The steady-state fidelities are
( _T_ 0 ) = 0 _._ 70 and ( _S_ ) = 0 _._ 71, well beyond the threshold _F_ = 0 _._ 5 indicative of quantum
_F_ _|_ _i_ _F_ _|_ _i_
entanglement. The fidelity loss is dominated by residual _T_ population and by transitions
_|_ __ _i_
to the entangled state of opposite symmetry _|_ _T_ 0 _i $ |_ _S_ _i_ . Increasing  _p_ in principle helps
to depopulate the inital _T_
_|_ __ _i_
state; however, increasing the pump power leads to powerbroadening of both the desired transition and of the o-resonant pumping to _T_ + . Since
_|_ _i_
_T_ + decays equally to _S_ and to _T_ 0 , this creates a drive-dependent dephasing that sets
_|_ _i_ _|_ _i_ _|_ _i_
an upper limit on the pumping rate. In an on-chip implementation with currently-accessible
qubit coherence times, this protocol can be expected to produce on-demand entanglement
with fidelity in excess of 0.90.

## 7.5 ## Discussion


In this chapter, we have demonstrated symmetry-selective bath engineering, harnessing both
the spatial symmetry and the density of states of the dissipative environment to achieve and
preserve on-demand entanglement. The engineered symmetries in our system distinguish
it from the two-qubit bath engineering experiment in Ref. [63], where cooling to _|_ _S_ _i_ is

achieved by utilizing far-detuned qubits in a single cavity; stabilizing entanglement in this
system required six microwave drives, and only _|_ _S_ _i_ was accessible. In our implementation,
the resonant construction of the photonic lattice imprints itself onto the eective qubit
Hamiltonian and lifts the degeneracy in the single-excitation subspace. The lifting of this
degeneracy allows us to reduce the number of required drives from six to one, and the use
of separate cavities allows us to easily modify the spatial profile of this drive in order to
capitalize on the permutation symmetries of the coupled cavity resonances.

Our work demonstrates that engineering symmetries of a dissipative environment pro-

vides a powerful route to quantum control. Furthermore, this protocol is highly amenable
to scaling beyond bipartite entanglement into multiple qubits and cavities. In this case, the


-----


_CHAPTER 7. SYMMETRY-SELECTIVE BATH ENGINEERING_ 119

symmetric and antisymmetric combinations generalize to highly-entangled quasi-momentum
eigenstates, represented by many-body -states [203]. Critically, adjusting the phase relationships of a single driving tone applied across the lattice still provides symmetry selectivity, _W_
allowing for efficient stabilization of many-body entanglement in an extended system. The
ease of access to single-qubit manipulation and readout makes this experimental geometry a
promising testbed for transport and studies of high-symmetry (e.g. quadrupole) states and
long-range entanglement in Bose-Hubbard systems and other quantum lattices.


-----


120

# Chapter 8

 Conclusions and Outlook

A scientist in his laboratory is not a mere technician: he is also a
child confronting natural phenomena that impress him as though
they were fairy tales.

Marie Curie

In this dissertation, we have explored a number of ways in which dissipation can serve as

a useful tool for generating quantum resources in superconducting cQED systems. We first
engineered a half-parity measurement that, when properly tuned, probabilistically generates
entanglement between remote superconducting qubits. This experiment demonstrates that
coherent quantum information can be efficiently transferred along ordinary microwave cables,
which is a crucial capability for any potential quantum network with superconducting qubits
at the nodes. We also performed a deep dive into this half-parity measurement by unravelling
individual quantum trajectories in the system. This allowed us to explore the full distribution
of stochastic trajectories that lead the system into an entangled state or into one of the two
unentangled states, and to study both the most likely path and the most likely time to
entanglement. Through these sets of experiments, we developed a deeper understanding the
interplay between measurement and dissipation: the measurement signal we collect allows
us to generate entanglement, but the signal that is lost along the way leads to dissipation
that destroys that entanglement.

We then continued to demonstrate a purely dissipative means of generating entanglement

in a two-qubit, two-cavity system. By directly coupling the cavities to generate a dissipative
bath with opposite spatial symmetries imprinted on bath modes at distinct frequencies,
we preserve the ability to perform individual qubit manipulations while still coupling the
qubits to common dissipative modes. We drive the bath with a single microwave tone with
a controllable spatial profile in order to achieve symmetry-enhanced dissipative stabilization
of an odd-parity entangled state of choice. This represents a first demonstration of a scalable
protocol for generating multipartite entangled states.

Throughout these experiments, we have grown to appreciate that dissipative processes

need not be the enemy of a coherent quantum system. When understood and utilized


-----


_CHAPTER 8. CONCLUSIONS AND OUTLOOK_ 121

properly, dissipation can serve a unique role in both generating and stabilizing entanglement.
The half-parity measurement that we perform in the remote entanglement experiments uses
a propagating coherent state to carry information from one qubit to the next, generating
an eective interaction between the qubits where no local entangling interactions exist. In
fact, entanglement in this system is made possible precisely by the measurement. In the
bath engineering experiments, the interaction between two cavity modes creates an eective
interaction between the qubits; driving those modes allows us to generate entanglement ondemand, and stabilize it for arbitrary time. These complementary techniques demonstrate
the power and flexibility of tailored dissipation in the generation of quantum resources.

## 8.1 ## Extensions of Measurement-Induced Entanglement

There are a number of interesting follow-on experiments that one could imagine for the remote measurement-induced entanglement work. The most interesting are targeted at making
the experiment amenable to deterministic, rather than probabilistic entanglement. If one
could precisely tune the phase shifts at the cavities to 2, the measurement would implement a full-parity measurement. Zero phase shift would correspond to projection onto _/_
the odd-parity subspace, and a phase shift would correspond to projection onto the evenparity subspace. The technical challenge to this approach is that, as the phase shift increases, __ __
the dephasing rate for a fixed cavity displacement increases as well, such that the measurement induced dephasing caused by losses between the cavities becomes a more significant
experimental hurdle. Ongoing eorts to engineer a lossless circulator [191, 204] would be an
important enabling technology for such an experiment.

Moreover, our characterization of the state of the joint system under continuous mea-

surement suggests the feasibility of future _continuous_ feedback stabilization of entanglement

[171, 177, 178, 183], even when using a half-parity measurement. These proposals apply a
drive to the qubits that is proportional to the homodyne current. If the signal fluctuations
indicate that the system is projecting toward _|_ _gg_ _i_ , a positive rotation is applied to repopulate
the entangled subspace; if the signal indicates projection toward _|_ _ee_ _i_ , a negative rotation
is applied. This stabilizes the two-qubit system in the odd-parity subspace. In addition,
the proposal in Ref. [177] includes a means not only for stabilizing the population in the
odd-parity subspace, but also for stabilizing the phase _within_ that subspace. This protocol
is a particularly attractive option because it can correct for dephasing as well as for qubit
decay.

Finally, the cascaded qubit chain can be extended to the multi-qubit domain. In the

three-qubit case, if we are able to engineer all three phase shifts to be identical, then we
can probabilistically generate W-states, which share a single excitation amongst all three
qubits. In addition, it is often possible (given appropriate asymmetries in the system) to
engineer a combination of phase shifts such that the phase shifts for _|_ gge _i_ and _|_ eeg _i_ coincide;


-----


_CHAPTER 8. CONCLUSIONS AND OUTLOOK_ 122

we can then perform a bit flip on the final qubit to generate the GHZ state. Again, however,
inter-cavity losses will create a dissipation-induced dephasing that limits the applicability of
this protocol in the absence of lossless directional elements [191, 192]. An additional source
of complication is the exponentially increasing number of measurements required in order
to perform a full tomographic reconstruction: the number of free parameters in an _n_ -qubit
density matrix scales as 2 2 _n_ __ 1, which rapidly becomes intractable. However, there are a
number of proposals for continuous-measurement based tomography and compressed sensing

[205207] that may ameliorate the scaling issue.

Because the Bayesian approach is phenomenological, extends naturally from the single-

qubit Bayesian formalism, and has been validated in a two-qubit cascaded measurement, we
expect it to perform well in a multipartite system (conditioned on a well-calibrated measurement chain). However, one always needs a model for the eective cascaded dynamics
originating from a microscopic understanding of the system in order to justify and validate the extension of the phenomenological Bayesian model. This is particularly true as
the expanse of o-diagonal elements becomes larger, or for experiments in which there are
significant or interesting dynamics outside of the target subspace.

## 8.2 ## Further Applications of Dissipation-Induced Entanglement

There are a number of interesting extensions of the pure dissipation-induced entanglement
scheme. When moving to the coupled-cavity architecture, we gave up the remote aspect of
our system in order to gain determinism in the entanglement protocol. The reason for this
is that, if there is significant spatial distance between the cavities, the cable used to connect
the two cavities can no longer be treated as a lumped element. The cavities act as mirrors at
the ends of the connecting cable, setting up a third resonant mode that mediates the qubit
coupling and leads generally to a reduction in the coupling. However, there is an interesting
recent proposal that overcomes this challenge, and enables bath engineering of entanglement
in fully remote cQED systems [208]. This is a promising approach because it allows us to
couple determinism with spatial separation in the generation of entanglement. While this
system would not be appropriate for loophole-free tests of Bells inequalities - the protocol
relies on the exchange of photons between the two cavities - it nevertheless could be a useful
approach for distributing entanglement in a multiple-qubit device of arbitrary size.

In addition, the symmetry-selective bath engineering scheme we describe in Chapter 7 is

itself well-suited for scaling to larger system size [203]. The protocol relies on spatial symmetries for entangled state selectivity, which allows us to utilize only a single measurement
tone with a controllable spatial profile in order to generate an entangled state of our choosing
within the odd-parity subspace. We note that the entangled states _S_ and _T_ 0 are in fact
_|_ _i_ _|_ _i_
many-body W-states for a two-qubit system. Our protocol scales naturally to a chain of
multiple qubits and cavities. The cavity-mediated coupling leads to a lifting of the degener-


-----


_CHAPTER 8. CONCLUSIONS AND OUTLOOK_ 123

acy between the W-states in the single-excitation subspace; by driving the bath modes with
a tone at the appropriate frequency and with a well-adjusted spatial profile, we can stabilize
the W-state of our choosing. This opens the door to studying driven-dissipative dynamics
in many-body systems, which is a subject of great theoretical interest. More broadly, the
approach of purposefully designing symmetry-based selection rules in a dissipative bath is
quite general, and will provide a useful tool for tailoring cavity-induced qubit interactions
to simulate a Hamiltonian of interest.


-----


124