
####### Introduction to Experimental Quantum Measurement

 with Superconducting Qubits

Mahdi Naghiloo, Murch Lab

Washington University in St. Louis, April 2019

**Abstract** Quantum technology has been rapidly growing due to its potential revolutionary
applications. In particular, superconducting qubits provide a strong light-matter interaction
as required for quantum computation and in principle can be scaled up to a high level of
complexity. However, obtaining the full benefit of quantum mechanics in superconducting
circuits requires a deep understanding of quantum physics in such systems in all aspects. One
of the most crucial aspects is the concept of measurement and the dynamics of the quantum
systems under the measurement process. This document is intended to be a pedagogical
introduction to the concept of quantum measurement from an experimental perspective. We
study the dynamics of a single superconducting qubit under continuous monitoring. We
demonstrate that weak measurement is a versatile tool to investigate fundamental questions
in quantum dynamics and quantum thermodynamics for open quantum systems.


-----


# Contents

**Abstract** **i**

**List of Figures** **v**

**1** **Introduction** **1**
1.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

**2** **The Light-Matter Interaction** **6**
2.1 One-dimensional cavity modes . . . . . . . . . . . . . . . . . . . . . . . . . . 6

2.1.1 How to visualize the state of light . . . . . . . . . . . . . . . . . . . . 9

2.2 Qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.2.1 Josephson junctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2.2.2 Transmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2.3 Qubit-cavity interaction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.3.1 Jaynes-Cummings model . . . . . . . . . . . . . . . . . . . . . . . . . 23

2.3.2 Dispersive approximation . . . . . . . . . . . . . . . . . . . . . . . . 27

2.4 Dynamics of a driven qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

2.4.1 Rabi oscillations: The semi-classical approach . . . . . . . . . . . . . 29

2.4.2 Dynamics in the presence of dissipation . . . . . . . . . . . . . . . . . 34

**3** **Superconducting Quantum Circuits** **38**
3.1 Cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

3.2 Qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.2.1 Transmon fabrication: . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.2.2 JJ characterization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.3 Qubit-cavity system characterization . . . . . . . . . . . . . . . . . . . . . . 47

3.3.1 One-tone spectroscopy: punch-out . . . . . . . . . . . . . . . . . . 48

3.3.2 Two-tone spectroscopy . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.3.3 Time domain measurement: basics . . . . . . . . . . . . . . . . . . . 52

3.3.4 Rabi measurements . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56


3.3.5 _T_ 1 Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58


3.3.6 Ramsey Measurement ( _T_ 2 __ ) . . . . . . . . . . . . . . . . . . . . . . . . 58


3.3.7 Full state tomography . . . . . . . . . . . . . . . . . . . . . . . . . . 59


3.4 Josephson Parametric Amplifier . . . . . . . . . . . . . . . . . . . . . . . . . 60

ii


-----


_Contents_

3.4.1 Classical nonlinear oscillators . . . . . . . . . . . . . . . . . . . . . . 60

3.4.2 Paramp operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.4.3 Phase-sensitive amplification: phase vs amplitude . . . . . . . . . . . 67

**Quantum Measurement** **69**
4.1 Projective measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

4.2 Generalized measurement in the __ _z_ basis . . . . . . . . . . . . . . . . . . . . 72

4.2.1 Simple Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

4.2.2 POVM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

4.2.3 POVM in terms of physical parameters . . . . . . . . . . . . . . . . 76

4.3 Continuous measurement in __ _z_ basis . . . . . . . . . . . . . . . . . . . . . . 79

4.3.1 Stochastic Schr odinger equation . . . . . . . . . . . . . . . . . . . . . 80

4.3.2 Stochastic master equation . . . . . . . . . . . . . . . . . . . . . . . . 81

4.3.3 Inefficient measurement . . . . . . . . . . . . . . . . . . . . . . . . . 82

4.4 Bayesian update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

4.4.1 Bayesian update in terms of the Bloch components . . . . . . . . . . 87

4.5 Bayesian vs SME . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

4.6 Generalized measurement in the __ _x_ basis . . . . . . . . . . . . . . . . . . . . 89

4.6.1 POVM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

4.6.2 SME . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92

4.7 z-measurement procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

4.7.1 Basic characterization . . . . . . . . . . . . . . . . . . . . . . . . . . 95

4.7.2 Paramp calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

4.7.3 Quantum efficiency calibration . . . . . . . . . . . . . . . . . . . . . . 96

4.7.4 Tomography pulse calibration . . . . . . . . . . . . . . . . . . . . . . 101

4.7.5 Data acquisition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

4.7.6 Post-processing: Quantum trajectory update . . . . . . . . . . . . . . 102

4.8 __ _x_ measurement procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

4.8.1 Quantum efficiency calibration . . . . . . . . . . . . . . . . . . . . . . 106

4.8.2 State update and quantum trajectory . . . . . . . . . . . . . . . . . . 106

**Monitoring Spontaneous Emission of a Quantum Emitter** **108**
5.1 Spontaneous emission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

5.2 Photon Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

5.3 Homodyne detection of spontaneous emission . . . . . . . . . . . . . . . . . 111

**Quantum Thermodynamics: Quantum Maxwells Demon** **117**
6.1 Fluctuation theorems: thermodynamics at the microscope scale . . . . . . . 117

6.2 Maxwells demon and the 2nd law . . . . . . . . . . . . . . . . . . . . . . . . 119

6.3 Continuous monitoring: a quantum Maxwells demon . . . . . . . . . . . . . 120

6.3.1 Examining the Jarzynski equality . . . . . . . . . . . . . . . . . . . . 121

6.3.2 The demons information . . . . . . . . . . . . . . . . . . . . . . . . . 123

6.3.3 Test of the generalized Jarzynski equality . . . . . . . . . . . . . . . . 125

iii


-----


_Contents_

6.4 Information gain and loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

**Bibliography** **137**

iv


-----


# List of Figures

1.1 Photon detection vs. homodyne detection . . . . . . . . . . . . . . . . . . . 4

1.2 Quantum Maxwells demon . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.1 One dimensional cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.2 Wigner distribution for photon-number states . . . . . . . . . . . . . . . . . 12

2.3 Photon number distributions for coherent states . . . . . . . . . . . . . . . . 13

2.4 Winger function for a coherent state . . . . . . . . . . . . . . . . . . . . . . 15

2.5 Phase shifts for coherent state in the rotating frame . . . . . . . . . . . . . . 16

2.6 Circuit QED toolbox . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.7 Josephson junction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2.8 Transmon circuit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2.9 Transmon energy levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.10 The qubit-cavity interaction . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2.11 Dressed states vs bare states . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

2.12 Avoided crossing: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

2.13 Rabi oscillations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

2.14 Eigenstates on the Bloch sphere for a driven qubit . . . . . . . . . . . . . . . 32

2.15 Driven qubit evolution in the Bloch sphere . . . . . . . . . . . . . . . . . . . 33

2.16 Relaxation and dephasing of a qubit. . . . . . . . . . . . . . . . . . . . . . . . . . 35

2.17 Dephasing and relaxation for the qubit . . . . . . . . . . . . . . . . . . . . . 37

3.1 TE 101 mode in rectangular 3D cavity . . . . . . . . . . . . . . . . . . . . . . 39

3.2 HFSS simulation for cavity transmission . . . . . . . . . . . . . . . . . . . . 40

3.3 The cavity linewidth characterization . . . . . . . . . . . . . . . . . . . . . . 41

3.4 The cavity phase shift across the resonance . . . . . . . . . . . . . . . . . . . 41

3.5 Double stack e-beam resist . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

3.6 A simple design for transmon qubit . . . . . . . . . . . . . . . . . . . . . . . 44

3.7 e-beam resist development recipe . . . . . . . . . . . . . . . . . . . . . . . . 44

3.8 Double-angle evaporation and Josephson junction fabrication . . . . . . . . . 45

3.9 Qubit pattern SEM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.10 The HFSS simulation for the transmon shunting capacitor . . . . . . . . . . 46

3.11 The minimum experimental setup for basic qubit characterization . . . . . . 49

3.12 The punch-out measurement . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.13 Two-tone spectroscopy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51


-----


_List of Figures_

3.14 _I/Q_ mixer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3.15 Qubit rotation pulses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3.16 Single sideband modulation (SSB) . . . . . . . . . . . . . . . . . . . . . . . . 55

3.17 Qubit state readout, homophone detection . . . . . . . . . . . . . . . . . . . 55

3.18 Readout in phase space representation . . . . . . . . . . . . . . . . . . . . . 56

3.19 Rabi measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

3.20 Chevron plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

3.21 _T_ 1 measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

3.22 Ramsey measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

3.23 Full state tomography readout pulses . . . . . . . . . . . . . . . . . . . . . . 61

3.24 JPA Schematic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.25 Duffing resonator response . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

3.26 JPA transfer function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.27 The minimum experimental setup with paramp . . . . . . . . . . . . . . . . 65

3.28 The paramp single pump operation . . . . . . . . . . . . . . . . . . . . . . . 66

3.29 The paramp double pump operation . . . . . . . . . . . . . . . . . . . . . . 67

3.30 Phase sensitive amplification . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

4.1 Bloch sphere . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70

4.2 Quantum measurement: simple model . . . . . . . . . . . . . . . . . . . . . 73

4.3 Strong measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

4.4 Weak measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

4.5 Weak measurement cQED . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.6 Measurement signal distribution in the weak limit . . . . . . . . . . . . . . . 79

4.7 SSE update trajectory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82

4.8 _x_ -measurement schematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

4.9 Homodyne measurement signal distribution _x_ -measurement . . . . . . . . . . 92

4.10 Dumb-signal cancellation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

4.11 Quantum efficiency calibration setup . . . . . . . . . . . . . . . . . . . . . . 97

4.12 __ calibration result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98

4.13 Mixer output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

4.14 Ramsey measurements for a sweep of different angles . . . . . . . . . . . . . 100

4.15 Calibration of __ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

4.16 Rabi tomography diagnosis . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.17 Driven _z_ -measurement sequence . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.18 Digitized weak measurement signal scaling . . . . . . . . . . . . . . . . . . . 104

4.19 Quantum trajectory updated by SME . . . . . . . . . . . . . . . . . . . . . . 104

4.20 Tomographic reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

5.1 Photon detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

5.2 Homodyne detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

5.3 The experimental setup (spontaneous emission experiment) . . . . . . . . . . 113

5.4 Conditional dynamics of spontaneous decay . . . . . . . . . . . . . . . . . . 113

vi


-----


_List of Figures_

5.5 Backaction vector maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

5.6 Quantum trajectories for a decaying atom . . . . . . . . . . . . . . . . . . . 116

6.1 Work fluctuations in the macroscopic and microscopic limit . . . . . . . . . . 118

6.2 Maxwells demon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119

6.3 Classical demon vs. quantum demon . . . . . . . . . . . . . . . . . . . . . . 120

6.4 Maxwells demon experimental sequence . . . . . . . . . . . . . . . . . . . . 121

6.5 The act of the demon in Step 4 . . . . . . . . . . . . . . . . . . . . . . . . . 122

6.6 Transition probabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

6.7 Violation of the 2nd law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

6.8 Information dynamics for the quantum Maxwells demon . . . . . . . . . . . 124

6.9 Generalized Jarzynski equality for the quantum Maxwells demon . . . . . . 125

6.10 Information gain and loss for the quantum Maxwells demon . . . . . . . . . 126

vii


-----


# Chapter 1

 Introduction

Quantum mechanics has revolutionized our understanding of nature since its development in
the 20th century. Its prescription for the workings of nature is full of unexpected rules that
remain counterintuitive even after over a century of confirmations. In the past decades, we
have witnessed enormous progress in technology and control over quantum systems. These
technologies aim to use the counterintuitive properties of quantum mechanics for real-life
applications such as secure communication [1], high-precision sensing [2], and information
processing [3]. These ambitious and revolutionary goals have driven a tremendous effort
in the implementation of quantum devices in a variety of platforms ranging between, photonics, atomic systems, nano-mechanical structures, and superconducting circuits. Each
platform offers a unique capability over others; photons are suited for transmitting quantum
information, while atoms can serve as long-lived quantum memories. In this regard, superconducting circuits have gained a lot of attention for quantum computation owing to the
strong light-matter interaction achievable in these circuits.
Apart from computational goals, the superconducting circuit architecture is a powerful
technology to explore quantum physics and can serve as a testbed for fundamental questions
in science. In part, this is because the characteristics of quantum systems made of artificial
atoms are rather easy to manipulate which opens possibilities to explore non-trivial quantum
systems by the versatile design and engineering of superconducting circuits. The pronounced
interplay between science and engineering in the superconducting circuit technology brings
on active research from different perspectives ranging from fundamental studies to practical
applications. In particular, understanding the physics of open quantum systems and the
concept of measurement is considered a core problem in modern physics [4].
Open systems appear in many disciplines in science, from environmental science to social
science and atomic physics to biophysics. With recent progress in quantum technology and
its applications, a deeper understanding of open quantum systems is required to face practical
challenges. However, the importance of open quantum systems is not limited to practical
applications. From the fundamental point of view, many questions tie into open quantum
systems in some waysquestions such as how classical laws emerge from underlying quantum


-----


laws, the classical-quantum boundary [57], the arrow of time [810], and exploring quantum
thermodynamics [11].
odinger equation due to the interaction with the environment. This interaction results in dissipation The dynamics of open quantum systems cannot be described by the Schr
and decoherence in quantum systems. Superconducting circuits naturally tend to interact with all available degrees of freedom which makes them highly controllable systems yet
presents a challenge to preserve quantum coherence. Therefore, one of the most active areas
of research in quantum circuit technology is directed toward understanding and controlling decoherence channels and encoding quantum information in states that are protected
from decoherence [1217]. Another approach to cope with dissipation and decoherence is to
come up with clever designs and protocols out of imperfect parts that enable to correct for
imperfections and perform a perfect tasks [1821].
From the quantum measurement point of view, if we are able to monitor dissipation of
a quantum system, we could then maintain its coherence [22, 23]. In fact, measurement
on quantum system can be used as a resource for feedback to control dynamics [24,25], to
herald non-trivial states [26], and to prepare entangled states [2729]. Therefore the concept
of measurement in open quantum systems is important in many ways.
In particular, weak measurement enables one to continuously monitor a quantum system
without destroying its quantum coherence [30]. This provides a powerful tool to explore
quantum dynamics in its most fundamental level [3135]. Understanding the dynamics
of continuously monitored systems in turn opens new ways for novel applications such as
sensing [36,37] and parameter estimation [38].
Also, superconducting circuits and quantum measurement techniques have a lot to offer to
the newly emerging field of quantum thermodynamics [11]. The hope is that understanding
the dynamics of quantum systems lead us to an understanding of underlying thermodynamic
law in the quantum regime. In this context, the quantum system (e.g. a qubit) is in contact
with the environment as a reservoir. By continuous monitoring of the reservoir, we can learn
about energy exchange between the system and the reservoir. These observations would be
helpful to understand the underlying thermodynamical laws and fluctuations in the system.
This raises many new questions about the relevant thermodynamics parameters in the quantum regime like heat, work, and entropy [39], the validity of the classical thermodynamics
laws for quantum systems [40,41], the emergence of thermalization and irreversibility [8,42]
from quantum mechanical principles, and the energy-information connection [43,44]. Many
of these questions can be addressed by a deep understanding of open quantum system dynamics given from quantum measurement techniques.
Finally, the superconducting quantum systems can be engineered to realize non-trivial
systems such as hybrid systems [45], giant atoms [15], engineered baths [46,47], and nonHermitian systems [4850] where each of these hybrid systems opens new opportunities to
explore unprecedented areas in physics. In particular, non-Hermitian systems which obey


-----


_1.1 Overview_

Parity-Time (PT) symmetry have gained a lot of attention both from theoretical [5157] and
experimental [48,58] perspective owing to their topological and nonreciprocal properties.

####### 1.1 ####### Overview

This document is intended to be a pedagogical introduction to quantum measurement with
a focus on experiments in the superconducting qubit platform. A goal of this document is to
provide a clear and simple picture of quantum measurement in superconducting qubit circuits
for those who are new to the field. To this end, I will try to address questions I encountered
when beginning this research and cover questions I have received from other students during
my PhD studies. Chapter 2 provides a basic theoretical discussion about the light-matter
interaction and preliminary theory for measurement and characterization of superconducting
circuits. Chapter 3 provides basic experimental knowledge about quantum measurement and
superconducting circuits in close connection with the theoretical discussions of Chapter 2.
Chapter 4 provides a pedagogical discussion of generalized measurements and continuous
monitoring of a qubit and provides experimental procedures for two types of continuous
measurements corresponding to measurement operators __ _z_ and __ . Chapter 5 and 6 discuss
__
two experiments in close connection with the pedagogical discussions of previous chapters.
In Chapter 5, we will study how measurement affects the dynamics of quantum systems.
In particular, I discuss the situation where the spontaneous emission of a quantum emitter
is measured by homodyne detection. Typically, spontaneous emission is associated with the
sudden jump of an atom or molecule from an excited state to lower energy state by emission
of a photon. Spontaneous jump dynamics occur because most of detectors are sensitive to
energy quanta. However, light has both wave and particle nature, and here we explore how
the spontaneous emission process is altered if we detect the wave rather than the particle
nature of light. To do this, we interfere the spontaneously emitted light from a quantum
emitter with another electromagnetic wave, measuring a specific amplitude of the emission.
The dynamics of the quantum emitter under such a detection scheme are drastically different
than what is observed when photons are detected, for the state of the quantum emitter can
no longer simply jump between energy levels. Rather, the emitters state takes on diffusive
dynamics and follows a continuous quantum trajectory between its excited and ground state.
Chapter 6 discusses quantum thermodynamics under the guise of Maxwells demon. The
thought experiment of Maxwell demon, whereby knowing the position and velocity of the
molecules, a demon can sort hot and cold particle in a box was in apparent violation of 2 nd law
of thermodynamics. This thought experiment revealed a profound connection between energy
and information in thermodynamics and has driven a lot of theoretical and experimental
studies to understand this connection in many different platforms. In Chapter 6, we study
the experimental realization of Maxwells demon in a quantum system using continuous
monitoring. We show that the second law of thermodynamics can be violated by a quantum


-----


_1.1 Overview_

![Intro to quantum measurement.pdf-10-0.png](Intro to quantum measurement.pdf-10-0.png)

![Intro to quantum measurement.pdf-10-1.png](Intro to quantum measurement.pdf-10-1.png)

Figure 1.1: **Photon detection vs. homodyne detection (discussed in Chapter 5):** The behavior
of a quantum emitter depends on how we detect its emission. If we hire a catcher as a detector which is
sensitive to the energy quanta (addresses the particle notion of light), the emitter behaves like a pitcher
(spontaneous jump behavior). However, if we instead listen to the emitter, it behaves according to the
wave nature of its emitted energy (diffusive behavior).

Maxwells demon unless we consider the demons information. In our case, this information
is quantum information which is susceptible to decoherence.


-----


_1.1 Overview_

![Intro to quantum measurement.pdf-11-0.png](Intro to quantum measurement.pdf-11-0.png)

Figure 1.2: **Quantum Maxwells demon (discussed in Chapter 6):** We experimentally study a
quantum version of Maxwells demon who sorts particles that are in a quantum superposition of both hot
and cold. We will see that the information obtained by the demon can be lost due to the decoherence and
inefficient detection. Image adopted from Lis group.


-----


# Chapter 2

 The Light-Matter Interaction

This chapter provides the basic theoretical concepts of the light-matter interaction. The aim
of this chapter is to pedagogically introduce concepts related to the rest of this document,
especially Chapter 3 where we experimentally discuss qubit-cavity characterization.
We consider the simplest example 1
2
of the light-matter interaction where a two-level quantum system (a qubit) interacts only with a single mode of light . In practice, this situation
can be achieved by placing the qubit inside a cavity that supports a discrete set of modes.
By a proper choice of qubit and cavity frequencies, cavity mode geometry, qubit placement
and orientation, the qubit can effectively interact with only one of the modes of the cavity 3 .

####### 2.1 ####### One-dimensional cavity modes

The electromagnetic mode of a cavity can be described by Maxwells equations in classical
electrodynamics. In the next section, we discuss the proper description of an electromagnetic
field in quantum mechanics. Here we focus on a one-dimensional (1D) cavity but we will see
that the result can be simply extended to higher dimensions.
Here, I follow the conventional quantization found in quantum optics textbooks (e.g.
Ref. [61, 62]) and discuss the quantization of electromagnetic field of an actual cavity (a
volume bounded by perfect conductors) which is relevant to the three-dimensional (3D)
architecture of cavity quantum electrodynamics (cQED) 4 .

1 One would think that the simplest situation is a qubit in free space. However free space supports infinite
continuum of modes. In this regard, the free space situation is not the simplest situation.
2 A mode of light contains photons all of the same frequency, polarization, and spatial distribution.
3 However this assumption works fine for many practical situations, it may not be accurate enough in
general. In fact, this is an issue of fundamental importance see for example see [59,60]
4 Often in quantum circuit literature, this discussion is introduced by quantization of an _LC_ circuit; we
will discuss this when we study the qubit. In this chapter we will see theoretically why a cavity bounded by
superconducting walls is an _LC_ circuit, and later study this physically in Chapter 3 (See Fig. 3.1).


-----


_2.1 One-dimensional cavity modes_

In order to quantize the electromagnetic field, we may solve Maxwells equations for
a given set of boundary conditions and identify a corresponding canonical position _q_ and
canonical momentum _p_ . Then we transition to the quantum case by promoting _q_ and _p_ to
operators 1 .

![Intro to quantum measurement.pdf-13-0.png](Intro to quantum measurement.pdf-13-0.png)

Figure 2.1: **One dimensional cavity:** Two infinite superconducting walls separated by distance _L_ form
a cavity that supports a discrete number of electromagnetic modes in the _z_ -dimension (the second mode
is shown). Due to the translational symmetry in _x_ and _y_ directions, the electromagnetic fields are only
functions of _z_ . For simplicity, we assume the electric field (red lines) has polarization along _x_ axis and
consequently the magnetic field (blue lines) is along _y_ axis.

For a one-dimensional cavity, consider a pair of infinite perfect conducting walls separated
by the distance _L_ along the _z_ -direction as depicted in Figure 2.1. This configuration can be
considered as one-dimensional because we have a continuous translational invariance in _x_ and
_y_ dimensions. Therefore the electric and magnetic fields only depend on the _z_ -coordinate.
For simplicity, we assume that the electric field is polarized along _x_ -axis which implies that
the magnetic field is only along the _y_ -axis. This is an empty cavity with no external current
or charge source, therefore for Maxwells equations we have,



__

__
 _E_ =
__ __ _t_


_B_ _E_ _x_ ( _z, t_ )

_t_ __ _z_


_x_ ( _z, t_ ) _B_ _y_ ( _z, t_ )

=
_z_ __ _t_


_,_ (2.1.1a)
_t_



__
__

__
 _B_ = __ 0 __ 0
__ _t_



__
_E_ _B_ _y_ ( _z, t_ )

_t_ __ __ _z_



_y_ ( _z, t_ ) _E_ _x_ ( _z, t_ )

= __ 0 __ 0
_z_ _t_


_,_ (2.1.1b)
_t_



__ _E_ _x_ ( _z, t_ )
 _E_ = 0 = 0 _,_ (2.1.1c)

__ __ _x_



__ _E_ _x_ ( _z, t_ )
 _E_ = 0

__ __ _x_



__ _B_ _y_ ( _z, t_ )
 _B_ = 0 = 0 _._ (2.1.1d)

__ __ _y_



__ _B_ _y_ ( _z, t_ )
 _B_ = 0

__ __ _y_


1 This is a convenient way to quantized photons, massless particles. For massive particles (e.g. electron
in a box) one can solve the Schr odinger equation.


-----


_2.1 One-dimensional cavity modes_

Given perfect conducting walls, the electric field is required to vanish at the boundaries;
_E_ _x_ ( _z_ = 0 _, t_ ) = 0 and _E_ _x_ ( _z_ = _L, t_ ) = 0. One can show that the solution for electric and
magnetic field inside the cavity are,


_E_ _x_ ( _z, t_ ) = _q_ ( _t_ ) sin( _kz_ ) _,_ (2.1.2a)
_E_



__ 0 __
_B_ _y_ ( _z, t_ ) =
_E_ _k_


_q_  ( _t_ ) __ cos( _kz_ ) _._ (2.1.2b)


2 __ 2


The normalization constant is conveniently set to be = _c_ where _V_ is the effective

_V _ 0

_E_ _E_

volume of the cavity 1 . The parameter, _k_ = _m/L, m_ = 1 _,_ 2 _, ..._ is wave number corresponding
to the frequency __ _c_ = __ __ _k_ 0 __ 0 . The function _q_ ( _t_ ) describes the time-evolution for modes and
has a dimension of length 2 . Each integer value _m_ corresponds to one mode of the cavity.
Figure 2.1 shows the electric and magnetic field for the second mode of the cavity ( _m_ = 2).
The total electromagnetic energy (per unit of volume) stored in one mode can be written as,


The normalization constant _E_ is conveniently set to be _E_ =


_dV_ __ 0 _E_ _x_ ( _z, t_ ) 2 +

2 _|_ _|_




__ 0
_dV_

2





1
_H_ =


_B_ _y_ ( _z, t_ ) 2 _._ (2.1.3)
2 __ 0 _|_ _|_


By substituting Equation (2.1.2) in (2.1.3), one can show that total energy is equal to,



1
_H_ =


_p_ 2 ( _t_ ) + __ _c_ 2 _q_ 2 ( _t_ ) _,_ (2.1.4)


where _p_ ( _t_ ) =  _q_ ( _t_ ). From Eq. (2.1.4), it is apparent that the energy of an electromagnetic
mode is analogous to the energy of a classical harmonic oscillator if we consider _q_ ( _t_ ) and
_p_ ( _t_ ) as the canonical position and momentum. Having canonical position and momentum
identified, the Hamiltonian may be treated quantum mechanically by promoting the canonical parameters to be operators ( _p, q_ __ __ _p,_   _q_ ). This results in a _quantum_ Hamiltonian for a
harmonic oscillator:



1

_H_ =


_p_  2 ( _t_ ) + __ _c_ 2 _q_  2 ( _t_ ) _._ (2.1.5)


3
Therefore, we may conclude that each mode of the cavity acts as a quantum harmonic oscillator . Note that in the classical description of Equation (2.1.2), we already found that
the cavity has discrete modes. However in that picture, each mode could have continuous
amount of energy. The transition to a quantum mechanical description happens in Equation (2.1.4) __ (2.1.5) which results in quantization of the energy spectrum for each mode.

1 Here the constant _E_ is defined in a way that the total energy in the cavity finds a compact form in
Equation (2.1.4) which conveniently ensures that  _q_ and  _p_ obey the canonical commutation relation [ _q,_  _p_ ] = _i_  .
2 The actual form for _q_ is _q_ ( _t_ ) = sin( _t_ + __ ). But for now, we rather to implicitly represent it by _q_ ( _t_ ) and
we will see that it acts as the canonical position.
3 In this transition, we may keep/drop the time-dependence to work in Heisenberg/Schr odinger picture.


-----


_2.1 One-dimensional cavity modes_

To see this, it is convenient to define non-Hermitian operators 1

1
_a_  = ( __ _c_ _q_  + _i_ _p_  ) _,_ (2.1.6a)
__ 2 __ _c_

1
_a_  __ = ( __ _c_ _q_  _i_ _p_  ) _,_ (2.1.6b)
__ 2 __ _c_ __

which are annihilation and creation operators for a photon in the corresponding mode of
the cavity and obey the commutation relation [ _a,_  _a_ __ ] = 1. The electric and magnetic fields,
which are now operators, can be represented by  _a_ and  _a_ __ as,


_E_  _x_ ( _z, t_ ) = 0 ( _a_ +  _a_ __ ) sin( _kz_ ) _,_ (2.1.7a)
_E_

_B_  _y_ ( _z, t_ ) = _i_ 0 ( _a_ _a_  __ ) cos( _kz_ ) _._ (2.1.7b)
_B_ __

The Hamiltonian Eq. (2.1.5) also takes a compact representation in terms of  _a_ and  _a_ __ ,



1
_H_  = __ _c_ ( _a_ __ _a_  +



1 1

) = __ _c_ ( _n_ +
2 2



) _,_ (2.1.8)
2


where the operator  _n_ =  _a_ __ _a_  is the _number_ operator. Knowing the Hamiltonian for the
electromagnetic field of a single cavity mode, we can describe the state of the cavity by
solving the corresponding eigenvalue problem. Considering Hamiltonian (2.1.8) we have,


_H_ _n_ = _E_ _n_ _n_ _,_ _n_ = 0 _,_ 1 _,_ 2 _, ..._ (2.1.9)
_|_ __ _|_ __


where the single mode cavity field with the corresponding energy _{|_ _n_ _}_ are _photon number states_ or _Fock states_ representing the energy eigenstate for _E_ _n_ = __ _c_ ( _n_ + 1 2 ). The photon


the single mode cavity field with the corresponding energy _E_ _n_ = __ _c_ ( _n_ + 1 2 ). The photon

number states _{|_ _n_ _}_ form a complete basis to describe any arbitrary state of the cavity.
That means at any given time, the cavity is either in one of states _|_ _n_ __ or in some linear
superposition of them, _n_ _c_ _n_ _n_ . However, In general, the cavity state can be in a mixed

_|_ __
state, an incoherent superposition of Fock states, like thermal states, which are conveniently



represented by the density matrix __ = _P_ _n_ _n_ _n_ .


superposition of them, _n_ _c_ _n_ _n_ . However, In general, the cavity state can be in a mixed

_|_ __
state, an incoherent superposition of Fock states, like thermal states, which are conveniently



represented by the density matrix __ = _n_ _P_ _n_ _n_ _n_ .

_|_ __ _|_




_n_ _P_ _n_ _n_ _n_ .

_|_ __ _|_


########## 2.1.1 ########## How to visualize the state of light


We may describe the quantum state of the light inside the cavity by a wave function _|_ __ __
which can be represented in any arbitrary basis e.g. photon-number basis, __ = _n_ _c_ _n_ _n_ .
_|_ __ _|_ __

Now the question is what is the best way to characterize and visualize __ . One way to
_|_ __ 
do this is by looking at the expectation value of the electric and magnetic fields, __ __ _|_ _E_ _|_ __ __
and __ __ _|_ _B_ _|_ __ __ and their fluctuations. In the previous section we learned that electric and


We may describe the quantum state of the light inside the cavity by a wave function _|_ __
which can be represented in any arbitrary basis e.g. photon-number basis, __ = _n_ _c_ _n_ _n_
_|_ __ _|_ __

Now the question is what is the best way to characterize and visualize __ . One way to
_|_ __ 
do this is by looking at the expectation value of the electric and magnetic fields, __ _E_ __


1 Here  is introduced indicating we enter quantum world. However, we set  = 1 throughout this thesis
except for few confusing situations.


-----


_2.1 One-dimensional cavity modes_

magnetic fields are quantum objects and are described by operators, Eq. (2.1.7). From these
equations, it is apparent that the electric and magnetic operators are directly related to the
canonical position and momentum respectively.


_E_  __ ( _a_ +  _a_ __ ) __ _q_  (2.1.10a)

_B_  __ ( _a_ __ _a_  __ ) __ _p_  (2.1.10b)

 
The only difference between operators _{_ _E,_ _B_ _}_ and _{_ _q,_   _p_ _}_ is an extra spatial dependence
term in the electromagnetic operators which depends on the details of the geometry in the
system 1 . Therefore, a general way to visualize the state of light, regardless of the geometry
of the cavity, is to look at the probability distribution of photons in phase space, _W_ ( _q, p_ ).
This quasi-probability distribution 2 is known as the _Wigner function_ . There are a bunch
of different representations for the Wigner function in different bases. For example, in the
canonical position basis _{|_ _q_ _}_ , the Wigner function has the following definition for a given
pure state _|_ __ __ ,



1
_W_ ( _q, p_ ) =

2 __


+ __ _q_ + _x/_ 2 __ __ _q_ _x/_ 2 _e_ + _ipx_ _dx._ (2.1.11)
 __ _|_ __ _|_ __ __

__



1
_W_ ( _q, p_ ) =


In this section, we will see that Wigner function has an intuitive distribution for classical
light (e.g. coherent light, thermal light) but it is somewhat nonintuitive for non-classical
light (e.g. single photon state). Now we briefly discuss a few common states of light for a
single mode of a cavity.

 As we introduced earlier, Fock states, or photon-number states, are eigenstates of the quantum harmonic oscillator. Thus they have the simplest representation in **_Fock state_**
the photon-number basis 3 and describing the situation where exactly _n_ photons exist in the
cavity,

_|_ __ __ = _|_ _n_ __ (Fock state) (2.1.12)

1 The spatial dependence has to do with the geometry of the problem which sets the spatial property for
all photons in the same way. Let me explain this by a question; What is the difference between a Fock state,
lets say _|_ 1 __ , of a cylindrical cavity and a rectangular cavity? The is no difference. They both represent
having a photon in a cavity. But if you were asked about the spatial probability distribution of that photon
inside that cavity, then the answer indeed depends on the geometry of each cavity. Later when we discuss
the qubit placement inside the cavity, we will see this spatial dependence comes into play implicitly in the
coupling between cavity and qubit.
2 It is called quasi-probability because unlike a normal probability distribution, the Wigner function
may be negative for a non-classical light.
3 They are simple in terms of representation but experimentally, the preparation of a cavity in a Fock
state is not simple [63].

10


-----


_2.1 One-dimensional cavity modes_


including _vacuum_ state _|_ 0 __ where there is no photon in a cavity 1 . Photon-number states are
orthogonal to each other, _n_ _m_ = __ _n,m_ , which means, experimentally, one should be able to
__ _|_ __
distinguish _|_ _n_ __ from _|_ _m_ __ without any ambiguity. Considering this orthogonality, it is easy
to check that the expectation values of the electromagnetic field operators (Eq. 2.1.7) for
photon-number states are zero regardless of the number of photons. But the expectation
 value for the electromagnetic field squared (e.g. _E_ = __ _E_ 2 __ _E_ __ 2 ) are nonzero even for a vacuum state __ _E_ 2 __ ) and electromagnetic fluctuations (e.g. 2 .

**Exercise 1:**  Show that __ _E_ __ = 0, __ _B_ __ = 0 for a Fock state _|_ _n_ __ , but __ _E_ 2 __ = 0, __ _B_ 2 __ = 0.

![Intro to quantum measurement.pdf-17-0.png](Intro to quantum measurement.pdf-17-0.png)

For example the Wigner function for state _|_ 0 __ and _|_ 1 __ has following form,


0 _W_ 0 ( _q, p_ ) = 1 _e_ __ ( _q_ 2 + _p_ 2 ) (2.1.13)
_|_ __ __ 2 __


1 _W_ 1 ( _q, p_ ) = 1 (2 _q_ 2 + 2 _p_ 2 1) _e_ __ ( _q_ 2 + _p_ 2 ) _._ (2.1.14)
_|_ __ __ 2 __ __

It is somewhat easy to find some classical interpretation for a Wigner function when it is not
negative. For that just consider that _q_ and _p_ are related to the electric and magnetic field s .
For example the vacuum state (Eq. (2.1.13)) depicted in Fig. 2.2a shows the probability is
maximum for _q_ = 0 _, p_ = 0, corresponding to zero electric and magnetic field. But there is
some probability for a non-zero electromagnetic field around zero which comes from vacuum
fluctuations and accounts for a vacuum energy __ _c_ _/_ 2. So even an empty cavity has some
amount of energy and electric and magnetic field fluctuate around zero 3 .
However, the Wigner distribution is not very intuitive for photon-number states other
than the vacuum state. For example, as it is apparent from Equation (2.1.14) (also depicted
in Fig 2.2b), the Wigner function is negative in some region for the state _|_ 1 __ . It is hard to
interpret the negative probability density, thus states with negative Wigner functions are
called non-classical states.
Note that the photon-number states are eigenstates of the harmonic oscillator Hamiltonian (Eq. 2.1.8), thus the Fock state Wigner functions are stationary and do not evolve in
time.

1 There is no clear spatial visualization of photon-number states inside a cavity. But for our purpose
one may have some sort of visualization by combining both notions of light; wave and particle. In that
sense, one can imagine that each photon is a packet of energy that extended inside the cavity so that its
spatial probability distribution follows the distribution of the energy on that mode. A conventional way
to characterize the state of the light is by calculating its _Wigner function_ which is somehow a probability
distribution as a function of canonical position and momentum but it doesnt give any visualization in real
space.
2 3 However, This makes the vacuum state non-classical. __ _E_ __ and __ _B_ __ for a superposition of two or more Fock states can be non-zero.

11


-----


_2.1 One-dimensional cavity modes_

######### a ######### p ######### b ######### p

W 0 (q,p) W 1 (q,p)

![Intro to quantum measurement.pdf-18-4.png](Intro to quantum measurement.pdf-18-4.png)

![Intro to quantum measurement.pdf-18-6.png](Intro to quantum measurement.pdf-18-6.png)

![Intro to quantum measurement.pdf-18-0.png](Intro to quantum measurement.pdf-18-0.png)

![Intro to quantum measurement.pdf-18-1.png](Intro to quantum measurement.pdf-18-1.png)

![Intro to quantum measurement.pdf-18-5.png](Intro to quantum measurement.pdf-18-5.png)

![Intro to quantum measurement.pdf-18-3.png](Intro to quantum measurement.pdf-18-3.png)

Figure 2.2: **Wigner distribution for photon-number states: a** , The vacuum state _|_ 0 __ has a Gaussian
distribution centered at the origin of the phase space. **b** , The single photon state _|_ 1 __ exhibits negative
probabilities around the origin.

It is worth here to mention some common operational relations for Fock states:


_a_  _|_ _n_ __ = __ _n_ _|_ _n_ __ 1 __ (2.1.15a)


_a_  __ _|_ _n_


_n_ + 1 _|_ _n_ + 1 __ (2.1.15b)


_n_  _|_ _n_ __ = _a_  __ _a_  _|_ _n_ __ = _n_ _|_ _n_ __ (2.1.15c)


Where  leaves the state intact and gives the number of photons. With that, lets finish the discussion of Fock states by a counterintuitive _a_ ( _a_ __ ) annihilates (creates) a photon and  _n_
question.

![Intro to quantum measurement.pdf-18-2.png](Intro to quantum measurement.pdf-18-2.png)

**_Coherent state_**  One of the most common types of light is _coherent_ light which is also
known as classical light. In fact, the output of a laser or a signal generator is coherent light.
Experimentally, one can simply send the output of a signal generator at the right frequency
to a cavity to produce a coherent state in the cavity. The coherent state can be represented
in the photon-number basis as,


_|_ __ __ = _|_ __ __ =



_n_

__ 2 _/_ 2 __
_c_ _n_ _|_ _n_ __ _, c_ _n_ = _e_ _|_ _|_ __ _n_ ! _,_ (2.1.16)


where _c_ _n_ indicates the contribution of each photon-number state in the coherent state. The

12


-----


_2.1 One-dimensional cavity modes_

parameter __ is a constant 1 whose magnitude is related to the average number of photons,
__ _n_  __ = _|_ __ _|_ 2 , of the coherent state _|_ __ __ . In Figure 2.3 we plot _c_ _n_ versus _n_ for two different
values of __ .

1.0


0.6

0.4

0.2

|=0.5 =4.0|Col2|
|---|---|
|||
|||


0 5 10 15 20 25 30

n

Figure 2.3: **Photon number distributions for coherent states:** The blue (red) distribution shows the
photon number distribution for a coherent state which has an average photon number  _n_ = 1 _/_ 4 ( _n_ = 16). The
photon number distribution for the higher average number of photons is more like a Gaussian distribution.

The blue distribution is for __ = 1 _/_ 2 which corresponds to the average number of photons
_n_ (  _c_ = 2 0 = 0 __ _n_ __ _._ 88 = 1 2 _/_ 4. That means if we measure the number of photons in the cavity, we mostly 0 _._ 78) find zero photons but on average we get 1/4 photon. The red distribu

__
tion shows the distribution of photon-states for the coherent state that has 16 photons on
average 2 . The fact that the distribution for the higher average number of photons is more
like a Gaussian distribution, follows from the _central limit theorem_ for a Poisson distribution.

![Intro to quantum measurement.pdf-19-0.png](Intro to quantum measurement.pdf-19-0.png)

It is easy to show that coherent state is the eigenstate of annihilation operator,

_a_  _|_ __ __ = __ _|_ __ __ _._ (2.1.17)


However, since  _a_ is a non-Hermitian operator, the corresponding eigenstates _{|_ __ _}_ do not

1 Note, __ = _|_ __ _|_ _e_ _i_ can be any complex number. We will later see that the phase __ has a very simple
meaning (the phase of the oscillations) when we discuss the coherent state in analogy with a classical
oscillator.
2 It is important to distinguish coherent light with other incoherent mixed distributions of photons. It
is possible that an incoherent light gives the same distribution of photons as a coherent light does, but a
coherent state requires a certain relative phase between Fock states. For example, a qubit evolves totally
different interacting with coherent light versus incoherent light even if they have a same photon number
distribution.

13


-----


_2.1 One-dimensional cavity modes_

form a orthogonal basis 1 . Unlike the photon-number state, the coherent state is not an
eigenstate of the Hamiltonian (2.1.8), therefore it has time evolution 2 . But it turns out that
the time evolution of a coherent state is simply a rotation in phase space.

![Intro to quantum measurement.pdf-20-0.png](Intro to quantum measurement.pdf-20-0.png)

Now it is the time to discuss why coherent light often is considered classical light. As
we see in Equation (2.1.16), a coherent state is indeed a superposition of quantized photon
number states. But it turns out that most of its characteristics can be understood in a close
analogy with a classical light. In other words, when a cavity is populated with coherent
light, the behavior of the cavity corresponds to classical oscillatory motion. For example,
by considering Equation (2.1.17) and the fact that _|_ __ __ ( _t_ ) = _|_ _e_ __ _i_ _c_ _t_ __ __ , it is easy to show that
the expectation value of the electromagnetic field (Eq. 2.1.7) for a coherent state is non-zero
and oscillatory in time,


__ __ _t_ _|_ _E_ _|_ __ _t_ __ = 2 _R_ [ __ _t_ ] _E_ 0 sin( _kz_ ) cos( __ _c_ _t_ )


2 _|_ __ _|E_ 0 sin( _kz_ ) cos( __ _c_ _t_ + __ ) _,_ (2.1.18a)


__ __ _t_ _|_ _B_ _|_ __ _t_ __ = 2 _I_ [ __ _t_ ] _B_ 0 cos( _kz_ ) sin( __ _c_ _t_ )


2 _|_ __ _|B_ 0 cos( _kz_ ) sin( __ _c_ _t_ __ __ ) _,_ (2.1.18b)


where we used the fact that __ _t_ = _e_ __ _i_ _c_ _t_ __ and __ itself is a complex number __ = _|_ __ _|_ _e_ _i_ . You
may notice that the expectation value for the electric and magnetic fields are similar to the
classical solutions of Maxwells equation (Eq. 2.1.2). Therefore, the quantum description of
the coherent state is consistent with our classical understanding of the oscillating electric
and magnetic modes of a harmonic oscillator.
In addition, one can show that the coherent state has minimum quantum fluctuations
equal to the vacuum fluctuations. This is a minimum uncertainty allowed by the Heisenberg
uncertainty principle, assuming no squeezing. These fluctuations can be considered as an
intrinsic uncertainty related to determining both the amplitude and phase of the electromagnetic field.

![Intro to quantum measurement.pdf-20-1.png](Intro to quantum measurement.pdf-20-1.png)

Thus the Wigner function for a coherent state is a vacuum Wigner function displaced in

1 2 Two coherent states Here we assume that we are in Schr _|_ __ __ and _|_ __ __ are orthogonal only in the limit of odinger picture which is more intuitive and convenient to discuss _|_ __ __ __ _| _ 1.
the evolution of the system. However, calculating the expectation values are often more straightforward in
Heisenberg picture.

14


-----


_2.1 One-dimensional cavity modes_

phase space (Fig. 2.4a) by an amount __ which can be written in this form,


__ _W_ __ ( _q, p_ ) = 1 exp( ( _q_ [ __ ]) 2 ( _p_ [ __ ]) 2 ) _,_ (2.1.19)
_|_ __ __ 2 __ __ _R_ __ _I_

where _R_ [ __ ] ( _I_ [ __ ]) is the real (imaginary) part of __ .

######### a ######### b

####### 
c

|p|Col2|
|---|---|
|||
|||


![Intro to quantum measurement.pdf-21-2.png](Intro to quantum measurement.pdf-21-2.png)

![Intro to quantum measurement.pdf-21-0.png](Intro to quantum measurement.pdf-21-0.png)

![Intro to quantum measurement.pdf-21-1.png](Intro to quantum measurement.pdf-21-1.png)

Figure 2.4: **Winger function for a coherent state: a** , The Wigner function for a coherent state
is a Gaussian distribution displaced from the origin by amount of __ . The coherent state has minimum
uncertainty in each quadrature like a vacuum state. **b** , The evolution of coherent state under harmonic
oscillator Hamiltonian is simply a rotation around the origin.

As illustrated in Figure 2.4b, the coherent state evolves around the origin of phase space
by frequency __ _c_ . That means the energy swings back-and-forth from electric (potential) to
magnetic (kinetic). Therefore one may realize that the coherent states Wigner function is
very similar to the classical phasor diagram of a noisy signal. The difference is that when
considering classical signals, we assume one can in principle reduce the noise and make it
arbitrarily small. But for the coherent state the noise in each quadrature is quantum noise,
originating from vacuum fluctuations as described by the Heisenberg uncertainty principle.
In the limit of large average photon number, the noise (either classical or quantum) is
negligible compared to the actual signal. Therefore, the classical picture and quantum picture
completely overlap in that limit.
It worth mentioning here that the coherent state has a very important role in quantum
measurement. In particular, a precise measurement of the phase of a coherent signal is
an essential component for most quantum measurement experiments. Usually, we are not
interested in the natural oscillation frequency of a coherent signal. Therefore we go to a
frame that exactly rotates with that frequency. In that _rotating frame_ , the coherent state
doesnt rotate anymore in phase space. The coherent state Wigner distribution is either
along _q_ or _p_ or somewhere between and remains a steady-state. So in the rotating frame
we freeze the time evolution for the oscillator. For simplicity let us assume the oscillator

15


-----


_2.2 Qubit_

state is along the _q_ axis, which means all the energy is potential (like a stretched spring or a
pendulum at its turning point). In the rotating frame, the coherent state is stationary and
the phase is fixed unless, for any reason, the coherent state experiences an external phase
shift (or a kick) on top of its normal phase evolution due to a perturbative interaction. In
such case, the coherent state rotates to a new place in phase space. We can easily detect
that displacement in the rotating frame 1 (see Figure 2.5). We will see in the next chapter
that this type of phase detection is the essence of qubit readout measurement.


1.0

0.0

-1.0


![Intro to quantum measurement.pdf-22-6.png](Intro to quantum measurement.pdf-22-6.png)

![Intro to quantum measurement.pdf-22-0.png](Intro to quantum measurement.pdf-22-0.png)

![Intro to quantum measurement.pdf-22-1.png](Intro to quantum measurement.pdf-22-1.png)

Time(ns)

![Intro to quantum measurement.pdf-22-7.png](Intro to quantum measurement.pdf-22-7.png)

Figure 2.5: **Phase shifts for coherent state in the rotating frame:** The phase shift of a coherent
signal is easily detectable in the rotating frame.

####### 2.2 ####### Qubit

Experimentally there are many ways to realize a qubit. Here we discuss theoretically how
to realize a qubit with a superconducting circuit. In our circuit toolbox we have only three
elements to work with: capacitors, inductors, and Josephson junctions (JJ) 2 (Fig. 2.6). The

![Intro to quantum measurement.pdf-22-2.png](Intro to quantum measurement.pdf-22-2.png)

![Intro to quantum measurement.pdf-22-3.png](Intro to quantum measurement.pdf-22-3.png)

![Intro to quantum measurement.pdf-22-4.png](Intro to quantum measurement.pdf-22-4.png)

![Intro to quantum measurement.pdf-22-5.png](Intro to quantum measurement.pdf-22-5.png)

Capacitor Inductor JJ

Figure 2.6: **Circuit QED toolbox:** Quantum circuit technology relies on these three elements. The
required nonlinearity comes from the JJ which is basically a dissipationless nonlinear inductor.

most important element is the Josephson junction which introduces a circuit nonlinearity

1 Rotating frames are useful in many ways; both in theory and experiment. Theoretically, sometimes
it is easier to solve a problem in a rotating frame or it is more clear to see the dynamics of a system.
Experimentally, as we will see in the next chapter, it is very natural and easy to work in a rotating frame.
Otherwise, it wouldnt possible to precisely measure the phase shifts in a rapidly rotating signal (typically
__ _c_ _/_ 2 __ 5 GHz).
2 Of course we wanted to avoid resistors in our toolbox but this is something that comes for free. Even in __
superconducting circuits, there are various ways that energy can dissipate. e.g. photon emission/radiation,
coupling to phonons.

16


-----


_2.2 Qubit_

necessary to form a qubit. In order to realize a qubit, the idea is to make a nonlinear
(anharmonic) oscillator out of Josephson junction and use only the two lowest energy states
as a qubit 1 .

########## 2.2.1 ########## Josephson junctions

The Josephson junction (JJ) comprises of a thin ( __ 1 nm) layer of an insulator sandwiched
between two superconducting slabs (Fig 2.7). The superconducting leads consist of many
atoms, but due to their superconducting state they can be described by a single complex
number,  1 _,_ 2 = __ _n_ 1 _,_ 2 _e_ _i_ 1 _,_ 2 , where _n_ 1 _,_ 2 and __ 1 _,_ 2 indicate the number of Cooper pairs and the
phase of the superconducting order parameter on each side of the junction.

Superconductor

![Intro to quantum measurement.pdf-23-0.png](Intro to quantum measurement.pdf-23-0.png)

Figure 2.7: **Josephson junction:** The JJ consists of two superconductors separated by a thin layer of
insulator. The Cooper pairs on each side can tunnel through the insulator and create a super-current _I_ .
Remarkably, the current can be non-zero even when _V_ = 0. The highly nonlinear _I_ - _V_ characteristics of the
JJ can be exploited for quantum circuits.

It has been shown 2 that, effectively, a JJ can be though of as a dissipationless nonlinear
inductor which has the _I_ - _V_ characteristics,

_I_ = _I_ 0 sin( __ ) (2.2.1a)

 0 
_V_ = _,_ (2.2.1b)
2 __

where __ = __ 2 __ __ 1 and _I_ 0 is a critical current above which the JJ becomes a normal dissipative
junction. One can then infer the effective inductance of the Josephson junction is,



_dI_
_V_ = _L_



_dI_  0

_dt_ __ 2 __



 0    0

__ = _LI_ 0 __ cos( __ ) _L_ =
2 __ __ 2 _I_ 0


 0 _L_ _J_ 0

_L_ =
2 _I_ 0 cos( __ ) __ cos(



_,_ (2.2.2)
cos( __ )


where  0 = 2 _h_


2 _h_ _e_ is the flux quantum, and we define _L_ _J_ 0 = 2  _I_ 0


 0 as the Josephson inductance at

2 _I_ 0


1 Normally in circuit QED literature the transmon discussion is introduced by a circuit called Cooper
pair box. The transmon is a Cooper pair box in a limit of a large shunt capacitancesee a nice discussion
in Ref [64]. Here, I approach the discussion of the qubit by starting from transmon as a nonlinear oscillator.
2 There is a straightforward derivation for Josephson equations based on microscopic BCS theory, See for
example Ref. [65].

17


-----


_2.2 Qubit_

zero current. It is apparent that the Josephson inductance is a function of current _L_ = _L_ ( _I_ ).
This dependence can be explicitly shown by using Equation (2.2.1)a in (2.2.2),


_L_ _J_ 0
_L_ =


1 ( _I_

_I_

__



_._ (2.2.3)

_I_ ) 2

_I_ 0


Moreover, one can use two JJs (assuming identical JJs) in a loop to effectively have a tunable
JJ where the critical current can be tuned by passing an external flux  _ext_ through the loop,


_I_ 0 SQUID = 2 _I_ 0 _|_ cos( __   _ext_ 0 ) _|_ (2.2.4)

where _I_ 0 is the critical current of an individual junction.

![Intro to quantum measurement.pdf-24-0.png](Intro to quantum measurement.pdf-24-0.png)

The total energy stored 1 in a JJ can be calculated by adding up the energy changes
_dU/dt_ = _V I_ (assuming there was no current ( __ = 0) at _t_ = __ ) and obtain 2 ,


_t_



_I_ ( _t_ __ ) _V dt_ __ = _I_ 0  0

2 __

__


2 __


_t_


sin( __ ) _dt_



__


_t_



_t_



_I_ 0 


2 __


sin( __ ) _d_ = _E_ _J_ [1 cos( __ )] _,_ (2.2.5)
__
__


where we define the Josephson energy _E_ _J_ =  0 _I_ 0 _/_ 2 __ =  _I_ 0 _/_ 2 _e_ . In the next subsection, we
will shunt a JJ by a capacitor and quantize the LC circuit (or JJ-C circuit). We will see that
the parameter __ is the canonical position for that anharmonic oscillator. In the next chapter,
we provide details from the experimental perspective, e.g. fabrication and characterization
of a JJ.

########## 2.2.2 ########## Transmon qubit

The fact that the inductance of the JJ is a function of current passing through the JJ,
makes it an interesting nonlinear element which can be leveraged for a qubit architecture. In
particular, one can imagine shunting the JJ by a capacitor to have the anharmonic oscillator
depicted in Figure 2.8. The total energy of the circuit is,

1 Naturally, a JJ also has some small capacitance, but for our purposes and simplicity we ignore this since
we are eventually going to shunt the JJ to a much larger capacitor to make a transmon qubit.
_L_ is a function current 2 For a normal inductor the energy is simply _I_ . _U_ =  _V Idt_ =  _LIdI_ = _LI_ 2 _/_ 2. But for JJ the inductance

18


-----


_2.2 Qubit_

![Intro to quantum measurement.pdf-25-0.png](Intro to quantum measurement.pdf-25-0.png)

Figure 2.8: **Transmon circuit:** The transmon circuit consists of a JJ shunted by a relatively large
capacitor so that _E_ _J_ _E_ _C_ .
__



_Q_ 2
_H_ trans = + _E_ _J_ [1 cos( __ )] _,_ (2.2.6)

2 _C_ __

where _Q_ is the total charge in the capacitor _C_ and we use Equation (2.2.5) for JJ energy. It
is convenient to represent the total charge in capacitor in terms of number of Cooper pairs 1 ,
_Q_ = 2 _em_ . Therefore the total energy can be written in this form,

_H_ trans = 4 _E_ _C_ _m_ 2 + _E_ _J_ [1 __ cos( __ )] _,_ (2.2.7)

where we define the charging energy _E_ _C_ = _e_ 2 _/_ 2 _C_ . The first terms is the kinetic energy
stored in capacitor and last term is the potential energy stored in JJ (inductor). Similar to
quantization of harmonic oscillator, here _m_ and __ are canonical momentum and position for
the transmon circuit. Therefore, we may transition to the quantum regime by promoting
them to be operators and then we arrive at the quantum Hamiltonian,

 2 
_H_ trans = 4 _E_ _C_  _m_ + _E_ _J_ (1 __ cos __ ) _._ (2.2.8)

Now, we have a Hamiltonian for the transmon circuit. In order to find the energy transitions
of the transmon, we need to find the eigenvalues and eigenstates for this Hamiltonian. This

 2
Hamiltonian has an analytic solution in the __ -basis in terms of Matthieu functions (see
for example Ref. [66]). More conveniently, one can truncate the Hilbert space and perform
numerical diagonalization 3 in  _m_ -basis.
In the limit of _E_ _J_ _/E_ _C_ 1 which implies __ 1, one may expand the last term up to the
__ __
4th-order of __ and obtain the harmonic oscillator Hamiltonian plus a nonlinear term,

 2 2 4
_H_ trans = 4 _E_ _C_  _m_ + _E_ _J_ __ _/_ 2 __ _E_ _J_ __ _/_ 24 + _  _ (2.2.9)

This is convenient approximation because we can follow same procedure for harmonic os-


1 When _I < I_ 0 , only pairs of electrons tunnel through the JJ insulating barrier, called Cooper pairs. Thus
in this case it makes sense to represent charge in terms of the number of Cooper pairs, _m_ .
2 In __ -basis you have  _m_ = _i_  __ __ __  then you obtain a solvable 2nd-order differential equation.

3 Numerical calculation in number basis is more convenient because the first term is diagonal and 2nd
term is tri-diagonal, __ _m_ __ 1 _|_ cos( __ ) _|_ _m_ __ = 1 _/_ 2. Note, _e_ _i_ _|_ _m_ __ = _|_ _m_ __ 1 __ .

19


-----


_2.2 Qubit_

cillator quantization and use creation and annihilation operators. Looking at the first two
terms in the Hamiltonian (2.2.9) in analogy to a harmonic LC circuit 1 we have,


4 _E_

_E_ _J_


(2.2.10a)
2 _C_

1

(2.2.10b)
2 _L_


__ _J_ =


8 _E_ _J_ _E_ _c_ __ _LC_ =


_LC_


(2.2.10c)


Similarly one can define creation and annihilation operators 2


and write down the Hamiltonian (2.2.9) in terms of  _b_ and _b_ __ ,


_H_  trans = __ _J_  _b_ __  _b_ _E_ _C_ ( _b_ +  _b_ __ ) 4 + _..._
__ 12


= __ _J_  _b_ __  _b_ _E_ _C_ ( _b_ __  _b_ __  _b_  _b_ + 2  _b_ __  _b_ ) + _...,_ (2.2.11)
__ 2

where the first term comes from first two terms in Equation (2.2.9) and the last terms comes
from the third term in Equation (2.2.9).

![Intro to quantum measurement.pdf-26-0.png](Intro to quantum measurement.pdf-26-0.png)

One can rearrange Equation (2.2.11) in this form,


_H_  trans = ( __ _J_ _E_ _C_ )  _b_ __  _b_ _E_ _C_
__ __ 2


 _b_ __  _b_ __  _b_  _b_ (2.2.12a)



__
__ 01  _b_ __  _b_ +


 _b_ __  _b_ __  _b_  _b,_ (2.2.12b)


where we arrive at a Hamiltonian for an anharmonic oscillator with a lower energy transition
__ 01 = __ 8 _E_ _J_ _E_ _C_ __ _E_ _C_ and an anharmonicity _/_ 2 __ = __ _E_ _C_ as in shown in Figure 2.9.

![Intro to quantum measurement.pdf-26-1.png](Intro to quantum measurement.pdf-26-1.png)

With reasonable anharmonicity _/_ 2 __ = _E_ 12 __ _E_ 01 (typically _/_ 2 __ __ 300 MHz) we can


1 For this analogy, consider a LC circuit energy as _E_ = _m_ 2


2 _C_ 2 + __ 2 2


1 For this analogy, consider a LC circuit energy as _E_ = _m_ 2 _C_ + __ 2 _L_ where _m_ and __ are charge and flux

respectively.


2 Here we have,  __ =


 _Z_ 2 _R_ ( _b_ +  _b_ __ ) _,_  _m_ = _i_


 _Z_ _R_


2 _Z_  _R_ ( _b_  _b_ __ ) , where _Z_ _R_ =
__


8 _E_ _E_ _J_ _C_ .


8 _E_ _C_


20


-----


_2.3 Qubit-cavity interaction_

![Intro to quantum measurement.pdf-27-0.png](Intro to quantum measurement.pdf-27-0.png)

########## 0 ########## 1 ########## 2 ########## 3

#######  ####### (Rad)


########## -3 ########## -2 ########## -1


Figure 2.9: **Transmon energy levels:** A typical transmon ( _E_ _J_ _/E_ _C_ = 40) potential (Eq (2.2.8) in solid
black curve) in comparison with a nonlinear oscillator (Eq. (2.2.9) in the solid red curve) and a harmonic
oscillator (dashed parabola). The first three energy levels are also depicted for the transmon (nonlinear
oscillator) in comparison to the harmonic oscillator. The typical values for transition energies/frequencies
are shown. Note _E_ 01 =  __ 01 and we set  = 1.

individually address the lower states and leave higher levels intact 1 . Therefore we consider
a transmon circuit as a two level system which can be described as a pseudo-spin with the
Pauli operator,


 __ _q_
_H_ _q_ = __ _z_ _,_ (2.2.13)
__ 2

where __ _q_ = __ 01 the lowest transition in the transmon circuit 2 .

####### 2.3 ####### Qubit-cavity interaction

In previous sections, we quantized a single mode of the electromagnetic field for a cavity and
showed that it results in a harmonic oscillator Hamiltonian (Eq. 2.1.8). In this section, we
consider only the lowest mode of the cavity ( _m_ = 1) which has the minimum frequency. This

This is true as long as the Rabi oscillation we induced in the lower transition is much less that anharmonicity,  1 _R_ __ .
2 __
The minus sign is because we use the NMR convention in which __ _z_ = 1 for the ground state.
__ __

21


-----


_2.3 Qubit-cavity interaction_

mode has maximum electromagnetic field amplitude at the center of the cavity ( _z_ = _L/_ 2).
Here, we study the interaction between this mode of the cavity (as a quantum harmonic oscillator) and a two-level quantum system (qubit) which is represented by Hamiltonian (2.2.13).
Assume that we place the qubit right at the center of the cavity. The dimension of the qubit
is much smaller than the dimension of the cavity therefore with a good approximation, the
qubit only interacts with the electromagnetic field at _z_ = _L/_ 2 as depicted 1 in Figure 2.10.


![Intro to quantum measurement.pdf-28-0.png](Intro to quantum measurement.pdf-28-0.png)

Figure 2.10: **The qubit-cavity interaction:** The qubit is placed at the center of the cavity where the
electromagnetic field is maximum for the first mode of the cavity. The qubit interacts with the electric field
via its electric dipole _d_ .

The qubit interacts via its electric dipole moment to the electric field of the cavity via
the interaction Hamiltonian,



_L_ 0

  
_H_ _int_ = _d_ _E_ _x_ ( _, t_ ) _,_ where _d_ =
__ __ 2 _d_ __




(2.3.1)


The parameters _d_ is the magnitude of the dipole of the qubit which can be in any direction.
Lets define _d_ _x_ as the magnitude of the qubit dipole aligned with electric field of the cavity.


Then the effective dipole operator can be represented as _d_ = _d_ _x_ __ _x_ = _d_ _x_ ( __ + + __ ) where __ +
__
( __ ) are the raising (lowering) operators for the qubit. Without loss of generality, we can
__
assume _d_ _x_ is real 2 . Then the interaction Hamiltonian reads,

_H_ _int_ = _g_ ( _a_ +  _a_ __ )( __ + + __ ) _,_ (2.3.2)
__ __

where we use Equation (2.1.7a) and define _g_ = _d_ _x_ _E_ 0 to quantify the interaction strength or

1 The assumption that the qubit interacts only with the electromagnetic field at the center of the cavity
is a classical interpretation. In quantum picture, each photon is a packet of energy extended to the entire
cavity. But this classical picture is very clear to convey the fact that by placing the qubit at the center of
the cavity, statistically, the qubit experiences a stronger electromagnetic field.
2 Note, the complex _d_ _x_ means that the electric dipole has non-zero moment along __ _y_ .

22


########## z=L


-----


_2.3 Qubit-cavity interaction_

qubit-cavity coupling energy 1 .

########## 2.3.1 ########## Jaynes-Cummings model

Now we have all the pieces to describe the combined qubit-cavity system. Note that the
qubit Hamiltonian (Eq. 2.2.13) by itself has two eigenstates _{|_ _g_ __ _,_ _|_ _e_ _}_ corresponding to two
eigenvalues (energies) __ _q_ _/_ 2 . Similarly, a single cavity mode Hamiltonian (Eq. 2.1.8) by
_{_ _}_
itself has an infinite number of eigenstates _n_ with eigenvalues __ _c_ ( _n_ + 1 _/_ 2)
_{|_ _}_ _{_ _}_
corresponding to _n_ photons in that mode. Here we are interested to know what are the eigenstates
and eigenvalues of the hybrid system of the cavity and qubit combined via the interaction
Hamiltonian (Eq. 2.3.2). The total Hamiltonian 2 has three parts,



1
_H_ Rabi = __ _c_ ( _a_ __ _a_  +



1 1

)
2 __ 2


2 __ _q_ __ _z_ __ _g_ ( _a_ +  _a_ __ )( __ __ + __ + ) _._ (2.3.3)


In the case of no interaction between qubit and cavity ( _g_
= 0) the eigenstates of the qubitcavity system are simply the tensor product of the cavity and qubit eigenstates _g_ _n_ _,_ _e_ _n_
_{|_ _|_ __ _|_ _|_ _}_
which are called bare states or the bare basis and, obviously, with eigenvalues that are simply
the sum of eigenvalues for each qubit and cavity eigenstates, __ _q_ _/_ 2 + __ _c_ ( _n_ + 1 _/_ 2) .
_{_ _}_


_|_ _g_ _|_ 0 __ __ qubit in ground state, no photons in the cavity (2.3.4)


_|_ _g_ _|_ _n_ + 1 __ __ qubit in ground state, _n_ + 1 photons in the cavity (2.3.5)


_|_ _e_ _|_ _n_ __ __ qubit in excited state, _n_ photons in the cavity (2.3.6)


However bare states no longer are the energy eigenstates for the system when the qubit
and cavity interact ( _g_ __ = 0). Yet, we can represent the total Hamiltonian in the bare basis
and attempt to diagonalize it to find its eigenstates and eigenvalues. Before we do this,
we simplify the interaction Hamiltonian by the rotating wave approximation (RWA). This
approximation is valid in most practical situations where the coupling strength is much less
than both the qubit and cavity frequency, _g_ __ __ _q_ _, _ _c_ , and also _|_ __ _c_ __ __ _q_ _| |_ __ _c_ + __ _q_ _|_ . Having
this situation in mind, lets revisit the interaction Hamiltonian where we have four terms,

_H_ _int_ _a_  __ __ +  _a_ + +  _a_ __ __ + +  _a_ (2.3.7)
__ __
__

The first term describes the decay of the qubit and creation of a photon for the cavity and
second term accounts for an excitation of the qubit and annihilation of a photon in the
cavity. These processes somehow conserve the total energy in the system since the energy

1 If we place the qubit off-center the coupling _g_ would be smaller. In fact, the placement of the qubit
inside the cavity is, to some extent, a knob to adjust the qubit-cavity coupling.
2 Here we refer to it as the Rabi Hamiltonian the JC Hamiltonian comes from the Rabi Hamiltonian
once taking the RWA.

23


-----


_2.3 Qubit-cavity interaction_

change would be ( __ _c_ __ _q_ ), which is much less that the total energy in the system even
__ __
in the few photon regime where _E_ _tot_ __ __ _c_ + __ _q_ . However, the last two terms correspond
to the excitation (decay) of the qubit and creation (annihilation) of a photon for cavity
which requires a relatively substantial energy change __ ( __ _c_ + __ _q_ ) in the system, especially
when we have only a few photons in the system. This means that the last two processes are
much less likely to occur compared to the first two processes so we can simply ignore those
terms 1 . This also can be understood from energy-time uncertainty principle which implies
that the last two processes happen on much faster time-scales and normally are averaged
out compared to the first two processes 2 . Therefore with this rotating wave approximation
(RWA) we obtain the Jaynes-Cummings Hamiltonian,



1
_H_ JC = __ _c_ ( _a_ __ _a_  +



1 1

)
2 __ 2


2 __ _q_ __ _z_ __ _g_ ( _a_ __ __ __ +  _a_ + ) _._ (2.3.8)


Although the RWA simplifies the Hamiltonian, still we have to deal with an infinite dimensional Hilbert space (since the number of photons _n_ ranges from 0 __ ) which means the
Hamiltonian is a semi-infinite matrix which makes it tricky to diagonalize. Normally in such
situation we truncate the Hilbert space at some point, but fortunately in this case we can
go around this problem and diagonalize the Hamiltonian in the infinite dimension Hilbert
space. If we use the bare basis to represent the _H_ _JC_ in the form of matrix we find,


1 2 __ _c_ __ 2 _q_

__


3 2 __ _c_ __ 2

__


_H_ _JC_ =


3 2 __ _c_ + __ 2 _q_


(2.3.9)


_..._


( _n_ + 1



1 2 ) __ _c_ __ 2

__


__ _n_ + 1 _g_



1
__ _n_ + 1 _g_ ( _n_ +



1 2 ) __ _c_ + __ 2 _q_


which shows the Hamiltonian is block-diagonal and all blocks follow a general form (except
the first block which has only one element 1 __ _c_ __ _q_ corresponding to the absolute ground state



1 2 __ _c_ __ 2

__


the first block which has only one element 1 2 __ _c_ 2 _q_ corresponding to the absolute ground state

__

of the system). Having a block-diagonal Hamiltonian makes it easy to find its eigenvalues.
We only need to diagonalized individual blocks and the resulting eigenvalues of each block
indeed are the eigenvalues of the entire Hamiltonian. For each block _M_ _n_ we have,


( _n_ + 1
_M_ _n_ = __ 2



1 2 ) __ _c_ __ 2 _q_ __ _n_ + 1 _g_

__ 1

__ _n_ + 1 _g_ ( _n_ + ) __ _c_


2 ) __ _c_ __ 2

__



1 2 ) __ _c_ + __ 2


(2.3.10)


1 One would expect RWA breaks in the regime of many photons. See for example [67, 68] for beyond
RWA.
2 For example, see chapter 4 of the Ref. [61] for more detailed discussion of RWA

24


-----


_2.3 Qubit-cavity interaction_

where _n_ = 1 _,_ 2 _, . . ._ . The eigenstates of _M_ _n_ and _|_ _g_ _|_ 0 __ corresponding to _n_ = 0, form a complete
set of eigenstates for the entire qubit-cavity system. For the eigenvalues we have,




_E_ _g_ =
__ 2

1
_E_ = ( _n_ + 1) __ _c_
__ __ 2


(2.3.11)

4 _g_ 2 ( _n_ + 1) +  2 _._ (2.3.12)


where = __ _q_ __ _c_ . The eigenstate associated with each of these eigenvalues are called the
__
_dressed states_ of the qubit and cavity,


_|_ 0 _,_ __ = _|_ _g_ _|_ 0 __ (2.3.13)


_n,_ = cos( __ _n_ ) _g_ _n_ + 1 sin( __ _n_ ) _e_ _n_ (2.3.14)
_|_ __ _|_ _|_ __ _|_ _|_ __


_n,_ + = sin( __ _n_ ) _g_ _n_ + 1 + cos( __ _n_ ) _e_ _n_ (2.3.15)
_|_ __ _|_ _|_ __ _|_ _|_ __



1 1
where __ _n_ = 2 tan __ (2 _g_ __ _n_ + 1 _/_ ) which quantifies the level of hybridization. In the limit

of  __ 0 where qubit and cavity have a the same energy we have __ _n_ = _/_ 4 and the dressed
states are in maximum hybridization,


where __ _n_ = 1


_|_ _n,_ __


2 ( _|_ _g_ _|_ _n_ + 1 _|_ _e_ _|_ _n_ __ ) _,_ (2.3.16)


which means each of the dressed states has a 50 %-50 % characteristic of the cavity photon
and qubit excitations. These states are called _polaritons_ . The energy difference between the
first two polariton states is 2 _g_ .
A nice way to look at dressed state energy levels is by comparing them to the corresponding uncoupled system energy levels, the bare states. For that, consider Figure 2.11 where
we display the energy levels of an uncoupled qubit-cavity system compared to the dressed
state energy levels for different values of the qubit-cavity detuning. The bare state energy
levels are depicted by solid black lines. The dressed states are depicted by bars that are
color-coded by blue (red) for cavity- (qubit-) like states. In the first panel, the qubit and
cavity are far detuned ( 0) which means __ _n_ 0 and the effective coupling is negligible.
__ __
Therefore the dressed states energy levels almost overlap with the uncoupled cavity-quit
state, the bare states (as depicted in panel 1). In the second panel, we change the energy
level for the qubit. The detuning is still negative but it is getting smaller and smaller
in terms of magnitude. The dressed states start pushing away each other and deviate from
the corresponding bare states. In this situation, __ _n_ (0 _, /_ 4) and the upper dressed state
__
acquires some qubit character, and similarly, the lower dressed state acquire some photon
character. In panel three = 0 and the hybridization is its maximum level, __ _n_ = _/_ 4
and the dressed states (which we now call polaritons) push each other away and deviate
maximally from the bare states. The separation between two polaritons is 2 _g_ . Now both

25


-----


_2.3 Qubit-cavity interaction_


![Intro to quantum measurement.pdf-32-16.png](Intro to quantum measurement.pdf-32-16.png)

![Intro to quantum measurement.pdf-32-13.png](Intro to quantum measurement.pdf-32-13.png)

![Intro to quantum measurement.pdf-32-10.png](Intro to quantum measurement.pdf-32-10.png)

![Intro to quantum measurement.pdf-32-11.png](Intro to quantum measurement.pdf-32-11.png)

![Intro to quantum measurement.pdf-32-14.png](Intro to quantum measurement.pdf-32-14.png)

![Intro to quantum measurement.pdf-32-17.png](Intro to quantum measurement.pdf-32-17.png)

![Intro to quantum measurement.pdf-32-15.png](Intro to quantum measurement.pdf-32-15.png)

![Intro to quantum measurement.pdf-32-12.png](Intro to quantum measurement.pdf-32-12.png)

![Intro to quantum measurement.pdf-32-0.png](Intro to quantum measurement.pdf-32-0.png)

![Intro to quantum measurement.pdf-32-1.png](Intro to quantum measurement.pdf-32-1.png)

![Intro to quantum measurement.pdf-32-2.png](Intro to quantum measurement.pdf-32-2.png)

![Intro to quantum measurement.pdf-32-3.png](Intro to quantum measurement.pdf-32-3.png)

![Intro to quantum measurement.pdf-32-4.png](Intro to quantum measurement.pdf-32-4.png)

![Intro to quantum measurement.pdf-32-6.png](Intro to quantum measurement.pdf-32-6.png)

![Intro to quantum measurement.pdf-32-5.png](Intro to quantum measurement.pdf-32-5.png)

![Intro to quantum measurement.pdf-32-7.png](Intro to quantum measurement.pdf-32-7.png)

![Intro to quantum measurement.pdf-32-8.png](Intro to quantum measurement.pdf-32-8.png)

![Intro to quantum measurement.pdf-32-9.png](Intro to quantum measurement.pdf-32-9.png)

Bare states Dressed states Polariton states Dressed states


Bare states


Figure 2.11: **Dressed states vs bare states:** The panels illustrate the dressed states of the qubit-cavity
system for different qubit-cavity detunings in comparison with the bare states (refer to the main text for a
more detailed description). Note that this illustration is not accurate and lacks some details but we rather
to avoid them here.

polaritons have acquired equal photon and qubit character as depicted by color-coded bars
in panel 3. If we further increase the energy level of the qubit (see panel 4) then again we get
dressed states. Note that in panel 4, unlike in panel 3, the lower (upper) polariton has more
photon (qubit) character. By increasing the detuning further, as in panel 5, we effectively
decouple the qubit and cavity and the dressed states again approach the bare states. If we
keep increasing the qubit frequency even further then the qubit energy will approach the
higher level of the cavity and we would see another avoided crossing corresponding to _n_ = 1.
Every time qubit level crosses one of the cavity levels, we may expect an avoided crossing
and hybridization 1 .
It is convenient to plot transition energy versus detuning since (as we will see in Chapter 3) we normally characterize the system by measuring the transition frequencies by doing

1 Considering the higher energy levels of the cavity one might think that it is also possible that qubit
level couples to two or multiple cavity energy levels at the same time. This is true, but usually, this effect is
only significant when the qubit-cavity coupling is so strong ( _g_ __ _c_ _, _ _q_ ) that qubit and cavity energy levels
__
push each other even when they are far detuned. This regime is known as ultra strong coupling [69, 70].
But normally the coupling rate _g_ __ _c_ _, _ _q_ . Therefore, in order to have hybridization the qubit energy has
__
to be very close to the cavity energy ( __ _c_ _, _ _q_ ). In our case, we can safely assume that qubit effectively
__
couples only to one cavity energy level at a time. However, I should warn you that in our description of
the avoided crossing which is represented in Figure 2.11, we have ignored the higher transmon energy levels
which would make the situation much more complicated. Considering the transmon as a two-level system is
good for intuition, but to be accurate one must include more transmon levels.

26


-----


_2.3 Qubit-cavity interaction_

spectroscopy. For example, when _n_ = 0 we have,



1
_E_ __ __ _E_ _g_ = __ _c_ __ 2


4 _g_ 2 +  2 +  _/_ 2 _._ (2.3.17)


In Figure 2.12, we plot the energy _E_ _E_ _g_ versus detuning which clearly shows the avoided
__
__
crossing. The transition energy levels are color coded so that again red (blue) is the qubit(photon-) like transition.

1.4


1

0.8

![Intro to quantum measurement.pdf-33-0.png](Intro to quantum measurement.pdf-33-0.png)

-2 -1 0 1 2
########### / ########### g


Figure 2.12: **Avoided crossing:** The transition energy from higher and lower dressed states to the ground
state versus the detuning . The transition energy is scaled by the energy of the cavity __ _c_ and the detuning
is scaled by the coupling rate _g_ . The dashed lines indicate the bare states transition. Note that
you can somehow see a similar avoided-crossing curve in Figure 2.11 by connecting the upper
(lower) dressed states in different detunings together.

In this section, we learned that if we put a qubit inside a cavity, the energy levels hybridize
and we have dressed states. Yet, just as we considered transmon as a two-level system (TLS)
by addressing only lower transition, here also we consider the ground state and the lower
dressed state as our new qubit.

########## 2.3.2 ########## Dispersive approximation

In this section, we perform another approximation to the interaction Hamiltonian. This
approximation is valid in the regime that cavity and qubit are far detuned  __ _g_ . In such
situations, the interaction is relatively weak. In principle, in this regime, the cavity and qubit
do not directly exchange energy unlike what we explicitly have in the interaction term 1 in

1 Note that this doesnt mean that in this limit the JC interaction term is not valid. It means that the
effect of the coupling is so weak such that we can approximately represent the Hamiltonian in a simpler

27


-----


_2.3 Qubit-cavity interaction_

the JC Hamiltonian (2.3.8). For that, consider the unitary transformation

_T_  = _e_ __ ( __ __ _a_ __ __ __ + _a_ ) _,_


where __ = _g_ . If we apply this transformation 1 to the JC Hamiltonian (2.3.8) and use the


Baker-Campbell-Hausdorff relation to evaluate all terms up to order __ 2 we have,



1
_T_  _H_  _JC_ _T_  __ = __ _c_ ( _a_ __ _a_  +



1 1

)
2 __ 2



1 _g_ 2

__ _q_ __ _z_
2 __ 



_g_ 2 _g_ 2

_a_  __ _a_  _z_ +




__ _z_ _._ (2.3.18)
2


We may ignore constant terms 2 since these do not affect dynamics, and obtain the JC
Hamiltonian in the dispersive limit,



1
_H_  dis = __ _c_ _a_  __ _a_ 
__ 2



1 _g_

__ _q_ __ _z_
2 __ 


_a_  __ _a_  _z_ _._ (2.3.19)



![Intro to quantum measurement.pdf-34-0.png](Intro to quantum measurement.pdf-34-0.png)

The dispersive Hamiltonian (2.3.19) describes the situation were the cavity and qubit are
far detuned and coupling is weak and dressed states are almost overlapping with the bare
states (see Figure 2.11 panel 1). Yet, there is a very small interaction as described by the last
term in Equation (2.3.19). In order to make better sense of this interaction, we re-arrange
the terms in Equation (2.3.19) as follows,



1
_H_  dis = ( __ _c_ __ _z_ ) _a_ __ _a_  __ _q_ __ _z_ _,_ (2.3.20)
__ __ 2


where __ = _g_ 2 is the dispersive shift or dispersive coupling rate 3 . We see that the dispersive


interaction is manifested as a qubit-state-dependent frequency shift for the cavity. If the
qubit is in the ground (excited) state _|_ _g_ __ ( _|_ _e_ __ ) then __ __ _z_ __ = 1 ( __ __ _z_ = __ 1 __ ) which means that
the cavity frequency shifts by + __ ( __ __ ). Therefore one can detect this frequency shift for
the cavity to determine the state of the qubit.


where __ = _g_ 2


form.
1 Applying a unitary transformation is somehow a change of frame. So we do not add/remove any physics.


2 The term 2 _g_ 2 __ _z_ (Lamb shift) is also a constant shift in qubit frequency that we can absorb it into __ _q_ .

3 Note that we define = __ _q_ __ __ _c_ and usually we prefer to have __ _q_ _< _ _c_ because of the transmon higher
levels and also to avoid coupling to higher frequency cavity modes [71]. Therefore the dispersive coupling is
often negative.

28


-----


_2.4 Dynamics of a driven qubit_

Alternatively, one can rearrange the terms in ((2.3.19)) as,



1
_H_  dis = __ _c_ _a_  __ _a_  ( __ _q_ + 2 __ _n_  ) __ _z_ _,_ (2.3.21)
__ 2

and interpret the interaction as a shift in qubit frequency due to photon occupation ( _n_ =  _a_ __ _a_  )
in the cavity 1 .

####### 2.4 ####### Dynamics of a driven qubit

In this section we discuss some of the most basic and important dynamics of the qubit.
Essentially, we want to know what happens to the qubit if we continuously drive it with a
coherent signal. We may take two approaches to solve this problem. One approach is semiclassical, where we treat the coherent drive as a classical signal. The other approach is fully
quantum, where we treat the drive as a coherent state of light. For most purposes, the semiclassical approach works perfectly fine and captures almost all the physics we are interested
in. Therefore, we discuss the semi-classical approach (for fully quantum mechanical approach
see Ref. [61]).

########## 2.4.1 ########## Rabi oscillations: The semi-classical approach

We are interested in qubit dynamics and we ignore the cavity for now 2 . With that, assume we

  __
have a qubit with Hamiltonian _H_ _q_ = __ __ _q_ __ _z_ _/_ 2 and electric dipole moment _d_ = _d_ _x_ . The qubit
interacts with the electric field of the coherent light (a classical signal) _E_ ( _t_ ) = _E_ cos( __ _d_ _t_ ) by

__ 
the interaction Hamiltonian _H_ _int_ = __ _E_ __ _d_ . Therefore, for the total Hamiltonian we have,



1
_H_ semi classic = __ _q_ __ _z_ _E_ ( _t_ )  _d._ (2.4.1)
__ __ 2 __ __

For simplicity we assume that the dipole moment of the qubit is aligned with the electric
field. Therefore we obtain,



1
_H_ semi classic = __ _q_ __ _z_ _A_ cos( __ _d_ _t_ ) __ _x_ _,_ (2.4.2)
__ __ 2 __

1 In chapter 4 we will use this interpretation to calibrate dispersive shift and average photon number in
the system.
2 We have qubit inside the cavity and the qubit and cavity are already hybridized and we consider
lowest two levels of system (ground state and the lowest dressed-state, or polariton state) as our new qubit.
Moreover we assume that the qubit drive is off-resonant with the cavity transition. Therefore in this situation
we effectively have just a qubit. Although experimentally the cavity still plays a crucial rule in terms of
noise protection and will be essential for qubit readout, this is not our focus in this section.

29


-----


_2.4 Dynamics of a driven qubit_


where _A_ = _Ed_ quantifies how strong the interaction is. Now we want to know how the qubit
evolves under this Hamiltonian. There are couple of ways we may solve this Hamiltonian.
The first way is to solve the Schr odinger equation for this time-dependent Hamiltonian. We
start with an _ansatz_ instead of starting from scratch. The idea is that if we have no electric
field or turn off the interaction, then we know the solution for Hamiltonian (2.4.2) would be
__ = _C_ _g_ _g_ + _C_ _e_ _e_ and its time evolution would be __ ( _t_ ) = _C_ _g_ _e_ + _i_ _q_ 2 _g_ + _C_ _e_ _e_ __ _i_ _q_ 2 _e_ . Now,
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __


__ = _C_ _g_ _g_ + _C_ _e_ _e_ and its time evolution would be __ ( _t_ ) = _C_ _g_ _e_ + _i_ 2 _g_ + _C_ _e_ _e_ __ _i_ 2 _e_ . Now,
_|_ __ _|_ __ _|_ __ _|_ __ _|_ __ _|_ __

we hope to find the solutions for (2.4.2) in the form of,


2 _g_ + _C_ _e_ _e_ __ _i_ _q_ 2
_|_ __


__ ( _t_ ) = _C_ _g_ ( _t_ ) _e_ + _i_ _q_ 2
_|_ __


2 _g_ + _C_ _e_ ( _t_ ) _e_ __ _i_ _q_ 2
_|_ __


2 _|_ _e_ __ _,_ (2.4.3)


where we just let the coefficients also be time-dependent. Now we plug this ansatz into the
Schr odinger equation,



__ __ ( _t_ )
_i_ _|_ __



( _t_ ) 1

__ =

_t_ __ 2



__ _q_ __ _z_ _A_ cos( __ _d_ _t_ ) __ _x_
2 __


_|_ __ ( _t_ ) __ (2.4.4)


By substituting Equation (2.4.3) into (2.4.4), one can obtain two coupled ordinary differential
equations (ODEs) for _C_ _g_ ( _t_ ) and _C_ _e_ ( _t_ ),

_C_  _g_ = _iA_ cos( __ _d_ _t_ ) _e_ __ _i_ _q_ _t_ _C_ _e_ _,_ (2.4.5a)

 + _i_ _q_ _t_
_C_ _e_ = _iA_ cos( __ _d_ _t_ ) _e_ _C_ _g_ _._ (2.4.5b)

In order to solve this analytically, we do a simplification which is nothing but the RWA. First,
we expand cos( __ _d_ _t_ ) _e_ __ _i_ _q_ _t_ = _e_ _i_ ( __ _d_ __ __ _q_ ) _t_ + _e_ __ _i_ ( __ _d_ __ __ _q_ ) _t_ , then argue that we are not interested in
very short timescales in the dynamics. In fact, in practically, we normally are not sensitive to
short timescales 1 . Therefore we ignore fast rotating terms _e_ __ _i_ ( __ _d_ + __ _q_ ) _t_ that are comparatively
slow to the rotating terms _e_ __ _i_ ( __ _d_ __ __ _q_ ) _t_ . Then we have

_C_  _g_ = _iA e_ __ _i_ ( __ _q_ __ __ _d_ ) _t_ _C_ _e_ _,_ (2.4.6a)

_C_  _e_ = _iA e_ + _i_ ( __ _q_ __ __ _d_ ) _t_ _C_ _g_ _._ (2.4.6b)

For the qubit initially in the ground state (initial conditions _C_ _g_ (0) = 1, _C_ _e_ (0) = 0) one can
show that the solutions are,


_e_ __ _i_  2
_C_ _g_ ( _t_ ) =



_d_

2


 _R_



 _R_
 _R_ cos(



_R_ _R_

_t_ ) + _i_  _d_ sin(
2 2



_t_ )
2


(2.4.7a)



_A e_ + _i_  2 _d_
_C_ _e_ ( _t_ ) = _i_


2 _d_ _t_



+ _i_ 2 _t_  _R_

sin(
 _R_ 2



_t_ ) _,_ (2.4.7b)
2


1 Assuming that the qubit frequency and drive are both in range of 5 GHz, then the fast oscillatory
terms _e_ __ _i_ ( __ _d_ + __ _q_ ) _t_ oscillate at the 100 picosecond timescale. We are normally interested in qubit dynamics at
microsecond timescale. Even for fast 5 ns rotation pulses, many of these fast oscillations are averaged out.

30


-----


_2.4 Dynamics of a driven qubit_


where  _d_ = __ _q_ __ _d_ and  _R_ = _A_ 2 +  2 _d_ . Having the solution for __ ( _t_ ) , we can obtain the
__ _|_ __

the evolution for any relevant observables. In order to see what the dynamics look like, we



may look at the population of the qubit excited state,


_P_ _e_ ( _t_ ) = _C_ _e_ ( _t_ ) 2 = _A_ 2
_|_ _|_ 


_A_ 2 sin 2 (  _R_

 2 2



_t_ ) _._ (2.4.8)
2


As depicted in Figure 2.13, the qubit doesnt respond that much to a far detuned drive, but
as the detuning gets smaller the oscillations grow. For an on-resonant drive ( _d_ = 0), we
have slowest but highest contrast oscillations of the qubit populations.


1.0

0.8

0.6

0.4

0.2

0.0


![Intro to quantum measurement.pdf-37-2.png](Intro to quantum measurement.pdf-37-2.png)

![Intro to quantum measurement.pdf-37-0.png](Intro to quantum measurement.pdf-37-0.png)

![Intro to quantum measurement.pdf-37-1.png](Intro to quantum measurement.pdf-37-1.png)

Time (  s)


Time (  s)


Figure 2.13: **Rabi oscillations: a** , The chevron plot. The excited state population _P_ _e_ versus time for
different detunings  _q_ . **b** , Three cuts from the chevron plot at different detuning values. The on-resonant
drive gives the maximum contrast for the oscillations.

The fact that we can fully rotate the qubit from the ground to excited by an on-resonant
drive is very practical. All we need is to know how strong and how long to drive the qubit
with light to put the qubit in the excited state 1 .
**_Rotating frame_** There is a rather easy way to solve the Hamiltonian (2.4.2) by going
to a rotating frame of drive. That makes the Hamiltonian time-independent 2 . For this, we
transform the Hamiltonian by a unitary operator _U_ ( _t_ ). The Hamiltonian in the new frame
can be evaluated by the following relation,

  
_H_ = _U_ ( _t_ ) _HU_ __ ( _t_ ) __ _iU_ _U_ __ _._ (2.4.9)


Now consider _U_ ( _t_ ) = _e_ __ _i_ _d_ 2 __ _z_ _t_ , which basically transforms the Hamiltonian to a frame that

rotates with the frequency of drive, __ _d_ . One can show that the Hamiltonian (2.4.2) in the

1 __ pulse calibration! We will see in next chapter how this is done in experiment.
2 This example would be useful to see how rotating frame works. Moreover, this solution will give better
picture of detuned Rabi oscillations in the Bloch sphere.

31


-----


_2.4 Dynamics of a driven qubit_


V+


![Intro to quantum measurement.pdf-38-0.png](Intro to quantum measurement.pdf-38-0.png)

Figure 2.14: **Eigenstates on the Bloch sphere for a driven qubit:** The eigenstates _V_ for a
_|_ __ __
detuned driven qubit make angle __ respect to the equator in the Bloch sphere. This picture gives a better
understanding of why the population doesnt reach to the maximum value for a detuned drive.

rotating frame of the drive would be


 1
=

2

_H_ __



1 2  _d_ __ _z_ _Ed_ 2

__


2 __ _x_ _,_ (2.4.10)


which no longer has time dependence. Now we may diagonalize the Hamiltonian in qubit
energy basis,



1

=
_H_ 2


 _d_ _A_
__ __
_A_ + _d_
 __


(2.4.11)


to obtain its eigenvalues, _E_ __ = __ 2 1


_A_ 2 +  2 _d_ and eigenstates,


_V_ = cos( __ ) _e_ sin( __ ) _g_ _,_ (2.4.12)
_|_ __ __ _|_ __ _|_ __

_V_ + = sin( __ )) _e_ + cos( __ ) _g_ _,_ (2.4.13)
_|_ __ _|_ __ _|_ __


_V_ = cos( __ ) _e_ sin( __ ) _g_ _,_ (2.4.12)
_|_ __ __ _|_ __ _|_ __


where __ = tan __ 1 (


sphere picture. The evolution of the system can be described by


_A_ 2 + _A_ 2 _d_ __  _d_ ). Figure 2.14 demonstrates the eigenstate _|_ _V_ __ __ in the Bloch


_|_ __ ( _t_ ) __ = _C_ + _e_ __ _iE_ + _t_ _|_ _V_ + __ + _C_ __ _e_ __ _iE_ __ _t_ _|_ _V_ __ __ (2.4.14)

where _C_ are constants determined by the initial condition. We may rewrite Equation (2.4.14)
__

32


-----


_2.4 Dynamics of a driven qubit_

in terms of _|_ _g_ __ and _|_ _e_ __ using (2.4.13),


_|_ __ ( _t_ ) __ = _C_ + _e_ __ _iE_ + _t_ sin( __ ) + _C_ __ _e_ __ _iE_ __ _t_ cos( __ ) _|_ _e_ __

+ _C_ + _e_ __ _iE_ + _t_ cos( __ ) _C_ _e_ __ _iE_ __ _t_ sin( __ ) _g_ (2.4.15)

 __ __  _|_ __

 

For example for a qubit starting in the ground state, __ (0) = _g_ , we have _C_ + = cos( __ ) _, C_ =
_|_ __ _|_ __ __
__ sin( __ ), then the time evolution would be,

__ ( _t_ ) = _i_ sin( _E_ + _t_ ) sin(2 __ ) _e_ + cos( _E_ + _t_ ) sin(2 __ ) _g_ _,_ (2.4.16)
_|_ __ __ _|_ __ _|_ __

where we used the fact that _E_ + = _E_ . Once again we can calculate the expectation value
for any observable. For example, the probability of being in the excited state would be __ __ 1 ,


_P_ _e_ = sin 2 (2 __ ) sin 2 ( _E_ + _t_ ) = _A_ 2 _A_ +  2 2 _d_ sin 2

 


_A_ 2 +  2


(2.4.17)


which is consistent with the result we had in lab frame where the Hamiltonian was timedependent (see Eq. 2.4.8). But, this picture gives a visualization of why the population
doesnt reach the maximum value for a detuned drive as illustrated in Figure 2.14.
Generally, in the experiment we use an on-resonance drive to prepare the qubit states.
Figure 2.15 summarizes our discussion of a driven qubit in the lab and rotating frame by
showing Rabi oscillations of a qubit initialized in ground state for both on-resonant and
detuned drives.

![Intro to quantum measurement.pdf-39-0.png](Intro to quantum measurement.pdf-39-0.png)

![Intro to quantum measurement.pdf-39-1.png](Intro to quantum measurement.pdf-39-1.png)

Figure 2.15: **Driven qubit state evolution in the Bloch sphere:** The red (blue) line shows the
evolution of a driven qubit in the lab frame (rotating frame of the drive) **a** , for an on-resonant drive and **b** ,
for a detuned drive.


1 You may need convince yourself that sin 2 [2 tan __ 1 (


_A_ _A_ 2

_A_ 2 + 2 _d_ __  _d_ )] = __ _A_ 2 + 2 _d_


33


-----


_2.4 Dynamics of a driven qubit_

########## 2.4.2 ########## Dynamics in the presence of dissipation

So far we assume that the qubit is an ideal closed system that undergoes unitary evolution given by the Schr odinger equation. However, in reality all systems either classical or
quantum are open systems, meaning they are interacting with their environment to some
extent. For quantum systems, this interaction degrades the peculiar quantum property of
the system (e.g. superposition and entanglement) resulting in energy dissipation and decoherence. Dissipation is a curse in many applications of quantum information. However,
dissipation is believed to be the essential piece for allowing the classical laws to emerge out
of the underlying quantum laws.
For our purposes, there are two main mechanisms which we need to consider to have a
more realistic picture of qubit dynamics: _relaxation_ and _dephasing_ .
**_Relaxation_**  Placing the qubit inside a cavity protects the qubit from environmental
noise and limits the available modes the qubit can interact with. Still, the qubit finds some
ways to relax its energy and decay to the ground state 1 . For example, when you prepare the
qubit in the excited state, the qubit eventually decays to the ground state and relaxes its
energy in the form of a photon to one of the unknown/known decay channels. This process
of jumping Hamiltonian, therefore we need to account for that somewhat phenomenologically 2 from _|_ _e_ _|_ _g_ __ happens in a random time. This process is not included in the 3 .
Lets say you prepare the qubit in the excited state or in some superposition state _|_ __ __ .
Having the qubit relax after a time, you are not sure if the qubit is still in state _|_ __ __ or
has relaxed into the ground state. You might have a mixed feeling about the state of the
qubit and, in quantum mechanics, this is an absolutely legitimate feeling because the qubit
is indeed in a _mixed state_ which can be described by a density matrix __ = _a_ _|_ __ __ __ _|_ + _b_ _|_ _g_ __ _g_ _|_ .
Where has decayed into ground state _a_ is the probability that qubit is still in state _|_ _g_ __ 4 . If you wait longer, the probability _|_ __ __ and _b_ is the probability that qubit _a_ becomes smaller
and smaller while the probability _b_ approaches to 1 meaning that you are getting certain
that the qubit is in the ground state. The time scale that qubit spontaneously relaxes its
energy is called the _relaxation time_ and is indicated by _T_ 1 . Experimentally, identifying the
_T_ 1 is a basic step of any qubit characterization process. As depicted in Figure 2.16a, the _T_ 1
time is the time by which the population of excited state decays to 1 _/e_ of its initial value,
_P_ _e_ ( _t_ ) = _P_ _e_ (0) _e_ __ _t/T_ 1 . We will see soon how we systematically account for this process in the
qubit dynamics.
**_Dephasing_**  There is another imperfection that affects the dynamics of a qubit. In

1 Also, sometimes we intentionally provide the qubit with a decay channel to relax its energy.
For now, we assume this process happens instantaneously which is a very reasonable and valid assumption. Yet, we will see later that the decay of an atom is not always jumpy. 2
3 In principle one can build these processes into the Hamiltonian if write down the Hamiltonian for the
entire universe: qubit+cavity+environment.
4 Here comes a lesson that I learned very late: In quantum mechanics the state of the system is nothing
but your state of knowledge about that system. The reality happens in your mind!?

34


-----


_2.4 Dynamics of a driven qubit_

########## a ########## z ########## Relaxation ########## b ########## z ########## Dephasing

![Intro to quantum measurement.pdf-41-0.png](Intro to quantum measurement.pdf-41-0.png)

![Intro to quantum measurement.pdf-41-1.png](Intro to quantum measurement.pdf-41-1.png)

Figure 2.16: Relaxation and dephasing of a qubit.

reality, due to the various noise sources in the system, the frequency of the qubit shifts
around stochastically. This imperfection doesnt cause the qubit to relax its energy but
instead we lose track of the qubit resonance frequency and thus loose track of the phase of
the qubit wavefunction. Considering the evolution of a superposition state in the lab frame,
the qubit state rotates around the equator of the Bloch sphere. After time _t_ the phase of the
qubit would be __ = __ _q_ _t_ , however, if the qubit frequency stochastically jitters around __ _q_ , then
the final phase at time _t_ would be __ = _t_ + __ ( _t_ ), where __ is our uncertainty about the phase
of the qubit which is growing in time 1 . Therefore, after a time, again we have a mixed feeling
about the state qubit and we lose the quantum coherences as depicted in Figure 2.16b. The
time scale that the qubit loses its coherence is usually called the dephasing time or _T_ 2 __ and
it is characterized by a Ramsey measurement in experiment. In the next section, we discuss
how to systematically account for relaxation and dephasing in qubit dynamics.

########## Lindblad master equation

In order to account for non-unitary and dissipative processes (e.g. dephasing and relaxation)
in qubit dynamics, we consider the Heisenberg picture where the unitary evolution of density
matrix __ is described by,


__  = __ _i_ [ _H_ _, _ ] _,_ (2.4.18)

1 __ ( _t_ ) can be considered as a 1D-random-walk distribution.

35


-----


_2.4 Dynamics of a driven qubit_

where is the driven qubit Hamiltonian in the rotating framesee Eq (2.4.10). Equation (2.4.18) is equivalent to the Schr _H_ 
odinger equation except with the density matrix approach we can also describe unitary evolution for a mixed state. Moreover, the Heisenberg
picture allows us to add more terms for  __ to describe other non-unitary processes for the
system like dephasing and relaxation 1 . In general, we have




__  = __ _i_ [ _H_ _, _ ] +



1
_L_ __ _i_ _L_ _i_ __ 2 _{_ _L_ __ _i_ _L_ _i_ _, _ _}_ _,_ (2.4.19)


where each _L_ _i_ is an Lindbladian operator describing a specific non-unitary process. For
example, the Lindbladian operator for the relaxation process of a qubit is _L_ relaxation = __ __
__
where __ = 1 _/T_ 1 accounts for the rate in which the qubit decays. The dephasing Lindbladian
operator _L_ dephasing = __ __ __ __ _z_ where __ __ = 1 _/T_ 2 __ quantifies in which rate the qubit dephases
and we loose coherences.

![Intro to quantum measurement.pdf-42-0.png](Intro to quantum measurement.pdf-42-0.png)

In Figure 2.17 we plot the evolution of a driven qubit in the presence dephasing and relaxation. We will return to the Lindbladian evolution and non-unitary evolution in Chapter 4
when we discuss continuous measurements.

1 Normally these non-unitary processes are positive and trace preserving.

36


-----


_2.4 Dynamics of a driven qubit_

![Intro to quantum measurement.pdf-43-0.png](Intro to quantum measurement.pdf-43-0.png)

Figure 2.17: **Dephasing and relaxation for the qubit:** The solution of the Lindblad equation for a
driven qubit in presence of dephasing and relaxation.

37


-----


# Chapter 3

 Superconducting Quantum Circuits

The aim of this chapter is to make a clear connection between the theoretical concepts introduced in the previous chapter and their experimental realization. I will discuss measurements
with superconducting circuits including, transmon qubits, 3D cavities, and parametric amplifiers from the experimental point of view. I will try to give a clear explanation of the basic
procedures of fabrication and characterization.

####### 3.1 ####### Cavity

In the previous chapter, we discussed a 1D cavity by considering two perfectly conducting
walls separated by a distance _L_ . Aluminum is a good choice for these walls since it becomes
superconducting below 1 _._ 2 K and can be used to realize a high quality factor cavity. Copper
can also be used when we need to thread external magnetic flux through the cavity to tune
the qubit resonance.
Although we induced the cavity in 1D, it is trivial to extend the result to 3D. One can
show that for a 3D cavity described by _L_ _x_ _, L_ _y_ _, L_ _z_ dimensions and depicted in Figure 3.1, the
Equation 2.1.2 simply generalized to,



__
_E_ ( __ _r, t_ ) = _E_ _q_ ( _t_ ) sin( _k_ __ __ _r_ ) (3.1.1a)



__ 0 __ 0
_B_ ( __ _r, t_ ) =
_E_ _k_



__
_q_  ( _t_ ) cos( _k_ __ __ _r_ ) _,_ (3.1.1b)



__
where _k_ = ( _n_ _x_ _/L_ _x_ _, n_ _z_ _/L_ _z_ _, n_ _z_ _/L_ _z_ ) and __ _r_ = ( _x, y, z_ ) and the corresponding resonance
frequency of modes are,



_c_
_f_ = __ _c_ _/_ 2 __ =



_n_ _x_
(



_n_ _x_ ) 2 + ( _n_

_L_ _x_ _L_



_n_ _y_ ) 2 + ( _n_ _z_ __

_L_ _y_ _L_ _z_


) 2 _,_ (3.1.2)
_L_ _z_


where _c_ is the speed of light inside the cavity. Each mode is described by a set of integers
_n_ _x_ _, n_ _y_ _, n_ _z_ , for example, TE 101 corresponds to a mode with an the electric field profile that

38


-----


_3.1 Cavity_

Electric feld
oscillation





########## x ########## z ########## Equivalent circuit diagram

![Intro to quantum measurement.pdf-45-0.png](Intro to quantum measurement.pdf-45-0.png)

![Intro to quantum measurement.pdf-45-1.png](Intro to quantum measurement.pdf-45-1.png)

Figure 3.1: **TE** 101 **mode in rectangular 3D cavity: a** , The typical cavity geometry is shown. Red lines
shows the electric field profile along _z_ , _x_ spatial directions for the TE 101 mode. The electric field oscillations
are maximum at the center if the cavity. **b** , The surface current oscillations (red arrows) have been depicted
for the TE 101 mode. The induced charges are maximum at the center (opposite charges at the top and
bottom of the cavity). The equivalent circuit diagram is shown for a section of the cavity. The cut-line
(magenta dashed line) indicates one of the planes where the surface current is tangential.

has one anti-node in _x_ and _z_ directions (depicted in Figure 3.1a [72]).
Thus we have spatially distributed electromagnetic modes inside a cavity, and apart from
that, all the quantum mechanical descriptions are essentially identical. Furthermore, we are
still interested only in one of these modes. Therefore we consider only the lowest mode of the
cavity and choose the dimensions so that the other higher modes frequencies are far away
from the lowest frequency. The dimensions that we normally use are _L_ _z_ _L_ _x_ 3 _._ 0 cm and
__ __
_L_ shows the surface current and the equivalent circuit diagram for the TE _y_ __ 0 _._ 8 cm which gives a cavity frequency __ _c_ _/_ 2 __ __ 7 GHz for the TE 101 101 mode. Figure 3.1b mode 1 .
Although it is easy to analytically calculate the resonance frequency for the simple geometries like a rectangular or cylinder cavity, one can use numerical simulations to get more

2
realistic predictions since they can account for geometry imperfections, input-output connectors, and qubit chip . Figure 3.2 shows a simulation result for cavity transmission by
considering other components using Ansys HFSS. The simulation is in a good agreement
with actual transmission measurement of a similar cavity 3 .

1 For a better circuit diagram visualization, you can replace the inductor with a wire and imagine that
the loop has some effective inductance. In this way, the loop magnetic field gives the correct direction for
the cavity magnetic field at that cross-section.
2 Moreover, simulation gives you to have access to more detailed information about the electromagnetic
field distribution inside the cavity.
3 Although, the details of the input/output connectors and pins (e.g. length, shape, soldering parts, ...)
are may not have significant contribution to the cavity frequency, they significantly affect the cavity quality
factor because they can dramatically alter the characteristic impedance of the ports.

39


-----


_3.1 Cavity_


-20

-40

-60

-80


![Intro to quantum measurement.pdf-46-0.png](Intro to quantum measurement.pdf-46-0.png)

Frequency (GHz)


10


![Intro to quantum measurement.pdf-46-2.png](Intro to quantum measurement.pdf-46-2.png)

![Intro to quantum measurement.pdf-46-1.png](Intro to quantum measurement.pdf-46-1.png)

Figure 3.2: **HFSS simulation for cavity transmission:** The cavity transmission is simulated by HFSS
(red curve) which is in agreement with actual measurement (blue curve).


In order to fabricate a cavity, we literally machine a cavity in two chunks of aluminum
as depicted in Figure 3.2c 1 .
, can be determined by measuring the transmission through the cavity. As depicted in Figure 3.3a, we use a vector network analyzer _Cavity linewidth-_ The cavity linewidth __
(VNA) and record S12 (or S21) transmitted power versus the frequency. The parameter
__ is roughly the frequency bandwidth by which the transmitted power drops by 3 dB a
depicted in 3.3b. More rigorously, one can fit the transmitted power (in linear scale) to a
Lorentzian function _F_ ( _x_ ) = ( _x_ __ _f_ _c_ ) _A_ 2 + __ 2 _/_ 4 and extract the cavity frequency _f_ _c_ = __ _c_ _/_ 2 __ and

cavity linewidth __ which is the FWHM of the Lorentzian fit. We will see in Chapter 4, the
parameter __ quantifies how much signal we get from the cavity and this value needed for
calibration of the quantum efficiency during measurement.
_Cavity phase shift-_ It is worth discussing the cavity phase shift across resonance. As
depicted in Figure 3.4, the phase of the transmitted signal shifts by __ across the resonance
of the cavity 2 which can be represented by,


2
__ = arctan

__




2 ( __ _c_ __ ) __ __ __ _c_ __ = 2

__ __ __ __ __ __ __



( __ _c_ __ ) _,_ (3.1.3)
__ __


which varies almost linearly around the cavity resonance frequency with slope 2 _/_ which
quantifies the sensitivity to the frequency by measuring the phase of the transmitted (or

1 Symmetrical pieces are not only convenient in terms of the fabrication, but also in this geometry,
symmetrical pieces minimize the adverse effect of imperfections where two pieces are connected since the
surface current doesnt need to pass between pieces at all. Note the cut-line (magenta dashed line) in
Figure 3.1b.
2 The reflected signal acquires a 2 __ phase shift across the cavity resonance. Does this mean it is better
to use reflection to detect the phase shift?

40


-----


_3.1 Cavity_


-15

-25

-35

|F(x)= (x-f|A )2-2/4 c|
|---|---|

|Col1|Col2|c|Col4|
|---|---|---|---|
|~3dB  2 W = Linear /2=3.5 MHz||0.01|A F(x)= (x-f)2-2/4 c  2|
||W = Linear|W Logmag 10 10||
|||||
|||0||


5.880 5.890 5.900 5.8 5.89 5.90

Frequency (GHz) Frequency (GHz)


5.89 5.90


Weak port Strong port


Frequency (GHz)


![Intro to quantum measurement.pdf-47-0.png](Intro to quantum measurement.pdf-47-0.png)

Figure 3.3: **The cavity linewidth characterization:** The cavity linewidth __ can be quantified by
measuring the scattering parameters of the cavity. **a** , **b** In the transmission measurement S21, the cavity
linewidth can be estimated by the bandwidth that the transmission signal drops by 3 dB. **c** , More carefully,
one can scale the transmission in the linear form and fit to the Lorentzian function. The FWHM of the
Lorentzian function would be the cavity linewidth.

reflected) signal 1 .


50

0

-50


![Intro to quantum measurement.pdf-47-1.png](Intro to quantum measurement.pdf-47-1.png)

5.87 5.88 5.89 5.90 5.91

Frequency (GHz)


5.87 5.88 5.89 5.90 5.91


Figure 3.4: **The cavity phase shift across the resonance:** The transmitted signal through the cavity
experiences a __ phase shift across the resonance of the cavity. Near resonance, the phase shift is approximately
linear with a slope of 2 _/_ .

_Cavity internal and external quality factors-_ The external quality factor _Q_ ext can be
adjusted by the length of the input and output port pin antennas. Normally, we have two
pins corresponding to the weak port and strong ports. The weak port is used as an input
(qubit manipulation and readout) and usually has __ 100 times weaker coupling to the cavity
compared to the strong port. The lengths of the port antennas determine the coupling to
a 50 transmission line, determining the external quality factor _Q_ ext . The internal quality
factor (often called unloaded quality factor) has to do with the losses due to the cavity itself,

1 We will see in Chapter 4 that the cavity phase shift and cavity linewidth come into play for describing
continuous measurement in terms of POVMs.

41


VNA


-----


_3.2 Qubit_

e.g. absorption of photons by the cavity. The total cavity quality factor is then,


_Q_ tot


_Q_ int


_._ (3.1.4)
_Q_ ext


Often, the deliberate coupling to the outside is dominant _Q_ int _Q_ ext . Therefore the total
__
quality factor is almost equal to the external quality factor. Note, that _Q_ tot = __ _c_ _/_ .
For a careful characterization of the internal quality factor and the input and output
coupling strengths, one can perform reflection measurements on each port (while the other
port is terminated by 50 ). By analyzing the amplitude and phase of the reflected signals,
one can obtain both the internal and external quality factors for the cavity and characterize
the coupling strength for each port (see Refs. [73,74]).

####### 3.2 ####### Qubit

In Chapter 2 we studied the Josephson junction and the transmon qubit from a theoretical
perspective. Here we discuss the fabrication and characterization of Josephson junctions and
transmon circuits.

########## 3.2.1 ########## Transmon fabrication:

Josephson junctions can be fabricated by evaporation of aluminum on a silicon wafer using an
electron beam evaporator which allows for directional evaporation. The common technique
for JJ fabrication is the double-angle evaporation technique which utilizes the evaporation
directionality for fabrication. A typical procedure for the JJ fabrication includes; spincoating e-beam resists on a silicon wafer, e-beam lithography, development, pre-cleaning,
double-angle evaporation, lift-off, and post-cleaning.
**_e-beam resist-_** We use a stack of two resists for junction fabrication. The bottom layer
normally is a relatively thick ( __ 1 __ m) and soft resist (MMA). In contrast, the top layer is
a relatively thin ( __ 300 nm) and hard (e.g. ZEP) resist. The reason for this choice of resist
staking is to achieve a wide undercut which is convenient for clean lift-off as depicted in
Figure 3.5. It also enables for a suspended bridge needed for junction fabrication (Fig. 3.5c).
The resist layers can be coated on the substrate by spin-coating. The thickness of the layers is
controlled by the spinning velocity, the total time of spinning, and the viscosity of the resist.
A typical spin-coating recipe for MMA/ZEP double stack resist is displayed in Table 3.1.
**_Electron-beam lithography-_** We use a 30 keV focused beam of electrons in a scanning
electron microscope (SEM) to pattern the resist. The SEM is controlled by Nanometer
Pattern Generation Software (NPGS). For fine features, we need to have a good focus of the
electron beam. To achieve a good focus, we use gold particles which are easily detectable in

42


-----


Deposited thin film


Hard resist


Deposited thin film


_3.2 Qubit_

Deposited thin film

|resist Soft resist|Col2|
|---|---|
|Silicon substrate||


![Intro to quantum measurement.pdf-49-0.png](Intro to quantum measurement.pdf-49-0.png)

![Intro to quantum measurement.pdf-49-1.png](Intro to quantum measurement.pdf-49-1.png)

Figure 3.5: **Double stack e-beam resist: a** , With a single layer of resist, it is often difficult to get small
and clean patterns. Mainly because the wall of the resist may also get deposited which connects top layers to
the bottom layers which make it difficult to properly lift-off the resist without peeling off the actual pattern.
**b** , This issue can be avoided by using two layers of the resist. The top layer provides sharp edges as a mask
and the bottom layer act as a spacer. The proper amount of undercut aids the liftoff process. **c** , Moreover,
the undercut of the lower resist can be used to created suspended resist (free-standing bridge) which is used
for the JJ fabrication in double angle evaporation.

|Step 1 Step 2 Step 3 Step 4|MMA spin-coat, 3000 rpm, 60 seconds Soft bake for 5 minutes,200C ZEP spin-coat, 3000 rpm, 60 seconds Soft bake for 3 minutes,180C|
|---|---|



Table 3.1: **Double-stack e-beam MMA/ZEP resist spin coating recipe**

the SEM for in-situ focus calibration 1 . The transmon pattern is designed in Design CAD
software using polygons in different layers 2 . A simple transmon pattern design in Design
CAD software has been shown in Figure 3.6. Each layer represented in different color.
We use a higher magnification and lower dosage for finer features. Table 3.2 displays
typical focus and dosage for each layers.

|Layer #|smallest feature size|SEM magnification|e-beam current|
|---|---|---|---|
|Layer 0 Layer 1 Layer 2 Layer 3|< 200 nm 1 m  10 m  >100 m|1300X 600X 200X 50X|30 pA 220 pA 600 pA 10000 PA|



Table 3.2: **The NPGS settings for s 30 keV electron beam** .

**_Resist development and pre-cleaning-_** The development recipe has three steps. We

1 We drop gold particles close to the edge of the sample and try to get the best focus at each point. NPGS
uses the focus point data and extrapolates the focus settings for the entire chip. One can also use single
point focus and move the beam by __ 1000 __ m and write the pattern with the same focus settings. Ideally,
for the transmon junction, one should be able to distinguish 2 NPGS allows for different expose/focus setting for each layer. Therefore, with a multi-layer pattern, we __ 5 nm gold particles at each focus point.
can optimize the exposure time.

43


-----


_3.2 Qubit_



![Intro to quantum measurement.pdf-50-0.png](Intro to quantum measurement.pdf-50-0.png)

Figure 3.6: **A simple design for transmon qubit:** A qubit design consists of few polygons in different
layers in DesignCAD software. The free-standing bridge design for a JJ and few micrometer extremities are
shown in red (Layer 0). The connector lines in the two steps (Layer 1,2) shown in blue and capacitor pads
(Layer 3) in green. The corresponding e-beam dosage for each layer is displayed in Table 3.2.

C to slow down the development process. Figure 3.7 demonstrates the development recipe. After the development use an ice bath to bring the developers temperature down to __ 0 __


**Step 1** ZEP developer **Step 2** **Step 3**

(ZED-520A)

MMA developer
(MIBK:IPA::1:3)

Ice



![Intro to quantum measurement.pdf-50-5.png](Intro to quantum measurement.pdf-50-5.png)

![Intro to quantum measurement.pdf-50-1.png](Intro to quantum measurement.pdf-50-1.png)

160 sec

![Intro to quantum measurement.pdf-50-2.png](Intro to quantum measurement.pdf-50-2.png)
Blow dry after 15 sec

![Intro to quantum measurement.pdf-50-3.png](Intro to quantum measurement.pdf-50-3.png)

![Intro to quantum measurement.pdf-50-4.png](Intro to quantum measurement.pdf-50-4.png)

30 sec, blow dry after Blow dry after

![Intro to quantum measurement.pdf-50-6.png](Intro to quantum measurement.pdf-50-6.png)

Figure 3.7: **e-beam resist development recipe: Step 1** , ZEP developer in ice bath, wait for developer
to cool down to T __ 1 __ C. Plunge the sample into the beaker for 30 seconds, then blow dry immediately.
**Step 2** , MMA developer for 160 seconds and blow dry afterward. **Step 3** , Rinse with IPA for 15 seconds.
The left panel shows the JJ area in the simple transmon design (Fig. 3.6) before and after development.
Note the undercut and the suspended bridge in the middle.

we may use oxygen plasma cleaning to further remove resist residue from the substrate
surface.
**_Electron-beam evaporation-_** We use a double angle evaporation method to fabricate
JJs as depicted in Figure 3.8. The transmon capacitor pads are also fabricated during this
process. The thickness of the aluminum film is normally 30 nm for the lower layer and 60
nm for the top layer and there is __ 1 nm thick of aluminum oxide layer grown between two
layers.
**_Lift-off and post-cleaning-_** We use acetone in temperature _T_ __ 60 __ C for 40 minutes
to dissolve the resist which leaves behind the transmon circuit on the substrate. Figure 3.9

44


-----


_3.2 Qubit_

Oxidation

![Intro to quantum measurement.pdf-51-1.png](Intro to quantum measurement.pdf-51-1.png)

Lift off


1 st angle deposition

![Intro to quantum measurement.pdf-51-0.png](Intro to quantum measurement.pdf-51-0.png)

2 nd angle deposition


![Intro to quantum measurement.pdf-51-2.png](Intro to quantum measurement.pdf-51-2.png)

![Intro to quantum measurement.pdf-51-3.png](Intro to quantum measurement.pdf-51-3.png)

Figure 3.8: Considering the indicated cross-section of the freestanding bridge in Figure 3.5 we use double angle evaporation to fabricate the **Double-angle evaporation and Josephson junction fabrication:**
JJ. **a** , The first layer of aluminum evaporation is about 30 nm. **b** , Introducing the oxygen mixture to form a
thin layer of aluminum oxide __ 1 nm as the insulator. **c** , The second layer of aluminum evaporation is about
60 nm at the opposite angle normal to the substrate surface. **d** , Removing the resists and the deposited
aluminum in a lift-off process.

shows the SEM image of the final transmon circuit and the JJ.

########## 3.2.2 ########## JJ characterization


For the qubit design, we have a couple of considerations. First, the qubit frequency and
its anharmonicity need to be in the proper range. We would like to have anharmonicity
somewhere in the range 200 300 MHz. According to Equation 2.2.12b, the anharmonicity
is determined by the energy associated to the shunted capacitor, __ _E_ _C_ = 2 _e_ _C_ 2 . This capacitance

mostly comes from the transmon pads. Therefore _E_ _C_ can be set based on the design of the
transmon pads (the size and separation of pads).

45


-----


_3.2 Qubit_

![Intro to quantum measurement.pdf-52-2.png](Intro to quantum measurement.pdf-52-2.png)

![Intro to quantum measurement.pdf-52-1.png](Intro to quantum measurement.pdf-52-1.png)

Figure 3.9: **Qubit pattern SEM** .

![Intro to quantum measurement.pdf-52-0.png](Intro to quantum measurement.pdf-52-0.png)

Using HFSS simulation, the capacitance of our normal design ( see Fig. 3.9a, pad size
400 __ 400 __ m separated by 200 __ m, with connection arms) is about _C_ = 0 _._ 057 pF. The
contribution of _C_ _J_ in negligible (estimated to be about 0 _._ 35 fF for 200 __ 100 nm JJ area,
assuming oxide layer thickness __ 1 nm).

![Intro to quantum measurement.pdf-52-3.png](Intro to quantum measurement.pdf-52-3.png)

_E_ _J_ 340 MHz.
__

46


-----


_3.3 Qubit-cavity system characterization_


For a certain qubit design _E_ _C_ is fixed and for a certain qubit frequency __ _q_ = __ 8 _E_ _J_ _E_ _c_ __ _E_ _c_ ,

the only knob is the Josephson energy _E_ _J_ = 2 _e_ _I_ _c_ , where the critical current is a function of

the junction area and the thickness of the oxide layer, _I_ _c_ area _/_ oxide thickness. Therefore,
__
having the right critical current is critical. Fortunately, there is a very useful relationship
between the resistance of a JJ at room temperature _R_ _n_ and the JJ critical current,



__ (0)
_I_ _c_ = _,_ (3.2.1)

2 _eR_ _n_

where (0) __ 170 __ eV is the aluminum superconducting energy gap at zero temperature 1 .
The normal resistance of the junction _R_ _n_ can be measured by sending a probe current _I_ prob
through the junction and reading the voltage _V_ probe across the junction. With this room
temperature resistance measurement, and with our prior knowledge about the _E_ _C_ (either
from previous transmon measurements or simulation) we can estimate the frequency of the
qubit before the cool-down. The estimation for transmon energy transition would be,


(0) _e_ 2

_CR_ _n_ __ 2


_h_ (0)


_E_ 01

_f_ = __ 01 _/_ (2 __ )


2 _C_


(0) _e_ 2

_hCR_ _n_ __ 2


(0)


2 _hC_ _,_ (3.2.2)


where _h_ is Plancks constant 2 . For example, in order to have qubit frequency around
__ 01 _/_ (2 __ ) 6 GHz with our normal transmon geometry ( _C_ 0 _._ 057 pF see Fig. 3.10),
__ __
the critical current should be _I_ _c_ __ 0 _._ 015 __ A ( _R_ _n_ = 18 k).

####### 3.3 ####### Qubit-cavity system characterization

In this section, we discuss a typical qubit characterization procedure. Here are the typical
steps before the cool-down:

__ Josephson junction room temperature resistance probe,

__ Choosing a proper cavity and weak/strong pin length adjustment.

__ The qubit placement inside the cavity.

__ Characterizing the cavity transmission (qubit chip included).


1 Basically the gap energy depends on the temperature, ( _T_ ) = (0) tanh[ 2 ( _k_ _B_ _T_ _T_ ) ]. However since the qubit

will be operated at temperature close to zero, _T_ _T_ _c_ , therefore with good approximation ( _T_ ) (0).
2 Here, we would rather  and treat it carefully, since __ _E_ _C_ doesnt explicitly depend on  . __

47


-----


_3.3 Qubit-cavity system characterization_

Then we put the cavity-qubit system inside the fridge and cool them down. The minimum
circuitry inside the fridge is depicted in Figure 3.11. The main qubit characterization includes
five basic experiments.

__ One-tone spectroscopy, or punch-out.

__ Two-tone spectroscopy.

__ Rabi measurement.

__ _T_ 1 measurement.

Ramsey measurement ( _T_ 2 __ ).

__

The first two experiments are in the frequency domain which means we only look at scattering
parameters of the system for characterization. However, the last three experiments are
measured in the time domain and involve preparation and readout of the qubit state. In the
following sections, we discuss how these are performed in the lab and what we learn from
each experiment in more detail.

########## 3.3.1 ########## One-tone spectroscopy: punch-out

The first step is to check if the qubit is alive or not. For that, we need to check whether
the cavity frequency shifts based on the state of the qubit. Of course, at this point, we dont
know the qubit frequency to carefully manipulate it. Fortunately, we dont need it to know
what is the qubit frequency to check if it is there. One way to think about that is if the
qubit is coupled to the cavity, the cavity becomes hybridized with the qubit and we should
be able to detect a little bit of nonlinearity in the cavity.
All we need to do is compare the transmission (or reflection) of the cavity in low power
versus high-power and see if the frequency of the cavity shifts. When we probe the cavity
with very low power we are pretty sure that qubit is in its ground state 1 . Therefore we
measure the resonance frequency of cavity when qubit is in the ground state. Next, we
turn up the power of the VNA to a very high power. In this case, we send a huge amount
of photons into the cavity which essentially overwhelms the qubit. Basically, the driving
amplitude is so high that the induced current exceeds the critical current of the junction.
Practically, in such a high power regime, we measure the bare cavity frequency. Now if there
is a working qubit inside the cavity we can see the cavity frequency shift and we say that the
cavity punched out. There is one more piece of information we can get from the punch-out

1 If you have not convinced, consider that we only sweep the VNA frequency across the cavity resonance
frequency so that VNA span is __ __ . Considering the avoided crossing picture and the fact that _g_ __ __ ,
therefore, the qubit couldnt be in this region. So we are pretty much sure that we are not driving the qubit
in this situation.

48


-----


Input #1 Input #2 Output


_3.3 Qubit-cavity system characterization_

Input #1 Input #2 / Output


300K

40K plate

4K plate

![Intro to quantum measurement.pdf-55-0.png](Intro to quantum measurement.pdf-55-0.png)

1K plate

Mixing
chamber

10mK

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|H 20 dB 10 dB 20 dB||||
|||||
|||||
||20 dB|||
||10 dB|||



Figure 3.11: **The minimum experimental setup for basic qubit characterization:** The input lines
can be used for qubit manipulation signals and cavity probe signals. Note that we dont get any signal back
from input lines (because of __ 2 __ 50 dB of attenuation). However, because we have a circulator connected
to the strong port, the reflection off of the strong port can be measured by sending the signal from the
input #2 and receiving it back from the output. We will refer to the fridge circuitry (depicted in left) by
the short version (depicted in right) throughout this document.

measurement. If the high-power frequency shifts to a lower frequency, we infer that qubit
frequency is below the cavity and vise versa. A bigger shift means that the cavity and qubit
are more strongly coupled 1 . One can consider the phase shift of the cavity resonance as a
rough estimation of __ = _g_ 2 _/_ but a careful characterization of __ can be done with time
domain measurements.
If the qubit bare frequency happens to be very close to the cavity bare frequency  _< g_ ,
then the qubit and cavity may enter the polariton regime and you may clearly see two
peaks (separated by __ 2 _g_ ) in the cavity at low power transmission 2 . If the high power peak
(bare cavity) is exactly on the middle of low-power peaks, then qubit and cavity are exactly
on-resonance and the separation is exactly 3 2 _g_ .

Note, the placement of the qubit inside the cavity also affects the coupling and consequently the punchout shift. 1
2 In this case you are directly resolving polariton qubit.
3 Therefore, one can use a tunable qubit to directly measure the effective coupling strength _g_ .

49


-----


_3.3 Qubit-cavity system characterization_


Dressed cavity




Frequency (GHz)


![Intro to quantum measurement.pdf-56-0.png](Intro to quantum measurement.pdf-56-0.png)

![Intro to quantum measurement.pdf-56-1.png](Intro to quantum measurement.pdf-56-1.png)

Figure 3.12: The low (high) power transmission of the cavity indicated by the blue (red) trace. For low power probe signal, the qubit remains in the ground state and we **The punch-out measurement:**
essentially measure the dressed cavity transition indicated by the blue double-sided arrow. In high power
case, the is qubit washed out and we essentially measure the bare cavity transition as depicted by the red
double-sided arrow.

########## 3.3.2 ########## Two-tone spectroscopy

Knowing that the qubit is working, the next step is to find the qubit frequency. The idea
is to continuously send a weak microwave signal to the cavity at the low power cavity
resonancethe cavity frequency when the qubit is in the ground stateand probe the cavity
transmission. Therefore, we constantly receive a high transmission signal because we probe
at the resonance of the cavity. While this first tone is on, we start sending another microwave
signal (labeled as BNC 1 ) into the cavity. We sweep the frequency of the probe tone BNC and
monitor the cavity transmission as depicted in Figure 3.13. During the sweep, once the BNC
frequency hits the qubit transition frequency (BNC= __ _q_ ), it excites the qubit 2 therefore the
state of the qubit is no longer in ground state (on average) and that causes a shift in the
cavity frequency 3 . Now, because the VNA frequency (which is fixed) is no longer resonant
with the cavity, the transmitted power drops 4 as depicted in Figure 3.13b. If we increase

1 BNC is simply the name of the generator we normally use in the lab.
2 Actually the BNC signal drives Rabi oscillations on the qubit. We saw in previous chapter (Eq. 2.4.17)
that the qubit reaches maximum excitation ( _P_ _e_ = 1) only if the drive is on-resonance with the qubit.
Remember interaction Hamiltonian in the dispersive regime (Eq. 2.3.20) which results in the qubitstate-dependent frequency for the cavity. 3
4 If BNC hits the cavity frequency (which is not shown here) we may also see a dip in transmission.
However, we never mistake that with the qubit dip because that happens exactly at the VNA frequency.
This dip could be due to some nonlinearity induced into the cavity but it is more likely to be the amplification
chain saturation. Which means, when we add the relatively high power BNC signal on top of VNA and both
highly transmitted to amplifiers, the amplifiers may be saturated and this effect may show up as a dip in

50


VNA


-----


_3.3 Qubit-cavity system characterization_


-20


-30


-40


![Intro to quantum measurement.pdf-57-0.png](Intro to quantum measurement.pdf-57-0.png)

4.0 4.5 5.0 5.5 6.0

![Intro to quantum measurement.pdf-57-1.png](Intro to quantum measurement.pdf-57-1.png)
BNC frequency (GHz)




-20


-30


-40


![Intro to quantum measurement.pdf-57-2.png](Intro to quantum measurement.pdf-57-2.png)

4.8 5.0 5.2 5.4

![Intro to quantum measurement.pdf-57-3.png](Intro to quantum measurement.pdf-57-3.png)

![Intro to quantum measurement.pdf-57-4.png](Intro to quantum measurement.pdf-57-4.png)
BNC frequency (GHz)

, The schematics for experimental setup for two-tone spectroscopy. A constant fixed frequency signal from the VNA at the cavity low power probes the cavity while a Figure 3.13: **Two-tone spectroscopy: a**
signal from the BNC sweeps across different frequencies from 4 to 6 GHz. **b** , The cavity transmission versus
BNC frequency shows a dip at qubit frequency. **c** , With higher power for BNC the two-photon transition is
also detectable (red trace). Note that the qubit transition is power broadened.

the BNC signal amplitude (by __ 10 dBm), we can also see a second dip at a slightly lower
frequency. This dip corresponds to the process by which two photons of drive excited the
qubit from the ground state to second excited state 1 , _|_ _g_ _|_ _f_ __ as depicted in Figure 3.13c.
The second dip gives a useful piece of information which allows us to simply calculate the
transmon anharmonicity, __ _eg_ __ __ _fe_ = 2( __ 1 __ __ 2 ) __ 2(5 _._ 2 __ 5 _._ 05) GHz = 300 MHz in this
case.
We just discussed spectroscopy in transmission mode. Equivalently, we may use reflection
off the cavity for spectroscopy 2 . In reflection, most of the signal is reflected from the cavity,
therefore there is not much information in the magnitude of the signal. But, we can look at
the phase of the reflected signal which is sensitive to the cavity resonance frequency 3 .

the VNA trace.
1 Transition from _|_ _g_ _|_ _f_ __ is a two-photon process which is less probable compared to a one-photon
process. Therefore a higher power is needed to drive that transition.
2 The are a couple of reasons we may want to use reflection for spectroscopy. First, we might have a
limited number of input lines so might not have a weak port for the cavity. Or, sometimes we have low
signal-to-noise in transmission and we might have a better chance looking at the reflected phase. Also, we
sometime may not have enough power from the weak port and we can use reflection port which has much
stronger coupling to the cavity.
3 In spectroscopy by reflection you may get a dip or peak depend on the delay offset of the VNA.

51


-----


_3.3 Qubit-cavity system characterization_

########## 3.3.3 ########## Time domain measurement: basics

In this section, we will discuss the time domain measurement of the qubit. Time domain
measurements require initialization, preparation and manipulation of the qubit state, and
readout. In what follows, we briefly discuss these three steps.
**_Initialization_** In our case the initialization is quite simple. The lifetime of the system
is on the order of tens of microseconds, therefore all we need to do is leave the qubit for
fidelity some amount of time ( 1 . __ 100 microseconds) to make sure it is in ground state with fairly high
Unlike the spectroscopy measurements where we constantly send signals and measure the scattering parameters, in time domain measurements **_Preparation/Manipulation_**
we need to carefully send signals to the system with accurate timing and proper duration.
This means we need to be able to switch the signals on and off with reasonable accuracy.
We use analog RF _I/Q_ _mixers_ to perform switching. Mixers can be used for modulating
and demodulating. For switching purposes, we use mixers as a modulator 2 . As depicted
in Figure 3.14a, a typical _I/Q_ mixer, ideally, multiplies the LO signal by signals in port _I_
and _Q_ with 90-degree phase difference 3 . Therefore one can use an _I/Q_ mixer in modulation
mode to switch a continuous signal. For that, we send the continuous signal to LO port and
we switch it by a DC pulse on port . The RF port output is only a segment of the continuous signal LO, as gated by the DC pulses depicted in Figure 3.14b. This technique gives _I_ or _Q_
us enough control to prepare and manipulate the qubit via Rabi oscillations of the qubit.
For example, If we choose the LO frequency to be the qubit frequency then by applying a
DC pulse to the port _I_ , the pulse rotates the qubit. Thus by choosing a proper duration and
amplitude of the DC pulse, we can prepare the qubit in the excited state or a superposition
state. Figure 3.15 demonstrates qubit preparations for the excited state and superposition
states where we define pulses in port _I_ (port _Q_ ) to rotate the qubit along _x_ -axis ( _y_ -axis) 4 .
_Single sideband modulation_ In practice, using DC pulses in _I/Q_ ports to manipulate the
qubit has two drawbacks due to the mixer nonlinearity. First, the mixer may not exactly
provide 90-degree phase difference between _I/Q_ ports which is not convenient and requires
careful corrections for tomography results. The second drawback is that even when we do

1 In our case this fidelity is about 97% which depends on the effective temperature of the system. One
may calculate the probability of thermal excitations for the qubit _P_ _e_ thermal = exp(  _/K_ _B_ _T_ ) given the
__
temperature of the fridge _T_ and energy of the qubit __ _q_ . However, the effective temperature for our system
is slightly higher than the physical temperature of the fridge as we normally measure _P_ _e_ thermal = 0 _._ 03 at 10
mK.
2 We will see that for readout purposes we use mixers as a demodulator.
3 We will see later that this 90-degree phase difference has a very important role in the qubit preparation
and tomography.
4 Of course there is no preferred direction for the qubit as _x_ and _y_ . However, the first pulse (first rotation)
in each run of the experiment sets a clock reference, determining the rotating frame of the coherent drive.
Subsequent signals will rotate the qubit along the same axis if it is in-phase with the first pulse and will
rotate in a different axis if it is out-of-phase with respect to the first rotation pulse.

52


-----


_3.3 Qubit-cavity system characterization_

I(t) cos(  0 t) + Q(t) cos(  0 t +  /2)

I(t)


I(t)

cos(  0 t) LO RF

![Intro to quantum measurement.pdf-59-0.png](Intro to quantum measurement.pdf-59-0.png)

Q(t)


![Intro to quantum measurement.pdf-59-1.png](Intro to quantum measurement.pdf-59-1.png)

![Intro to quantum measurement.pdf-59-2.png](Intro to quantum measurement.pdf-59-2.png)

Figure 3.14: _I/Q_ **mixer: a** , An _I/Q_ mixer can be used as a modulator. Note that the outputs correspond
to _I_ and _Q_ pulses are out of phase by 90 degrees. **b** , The DC pulse in _I/Q_ ports can be used to control
(switch) a continuous signal. The blue (red) DC pulse is the input for port _I_ (port _Q_ ) and its corresponding
output is in-phase (90 out-of-phase) with respect to the local oscillator.

not apply a pulse to the _I/Q_ ports there may be some signal leakage from the LO port to
the RF port. This leakage can be minimized by adding DC offsets to the _I_ and _Q_ inputs.
But even very small leakage constantly drives the qubit and causes imperfections in the
experiment. One way around this issue is to employ a single sideband modulation (SSB)
technique for the qubit pulses. The idea is to set LO frequency to be __ _q_ __  SSB where
 SSB 100-500 MHz is the sideband frequency. Then, for _I/Q_ ports we apply signals with
__
the frequency of  SSB with __ 90 degrees out-of-phase to up-convert (down-convert) the LO
to qubit frequency as depicted in Figure 3.16 for the up-converting case. SSB solves both
drawbacks we had with DC pulsing technique. In this case, we dont need to worry about
mixer non-orthogonality because the phase of the output pulse is set by the phase of the
_I/Q_ signal 1 . Therefore, the phase stability of the arbitrary waveform generator (AWG) sets
our rotation axis accuracy, which is normally good enough for sideband frequencies of a few
hundred MHz. As it is shown in Figure 3.16 the first pulses in _I/Q_ port defines the preferred
axis (we defined this to be the _x_ axis). The phase of subsequent pulses referenced by AWG
determines the rotation axis as it is shown for 90 out-of-phase pulse which results in a qubit
rotation along _y_ axis.
Moreover, we dont need to worry about small leakage of LO to RF because the LO

1 The mixer non-orthogonality, in this case, may cause some issues with carrier leakage or leakages in
opposite sideband and higher harmonics. But that can be compensated by adjusting the phase in AWG
pulses.

53


-----


_3.3 Qubit-cavity system characterization_


![Intro to quantum measurement.pdf-60-0.png](Intro to quantum measurement.pdf-60-0.png)

########  ######## q ######## 10mK

![Intro to quantum measurement.pdf-60-1.png](Intro to quantum measurement.pdf-60-1.png)

![Intro to quantum measurement.pdf-60-2.png](Intro to quantum measurement.pdf-60-2.png)

 
q


![Intro to quantum measurement.pdf-60-3.png](Intro to quantum measurement.pdf-60-3.png)

Figure 3.15: **Qubit rotation pulses:** Pulses in the _I, Q_ ports results in rotation in _x, y_ directions in the
Bloch sphere. **a** , A _/_ 2 pulse in port _I_ rotates the qubit along the _x_ direction and prepares a superposition
state along _y_ axis. **b** , __ pulse prepares the qubit in the excited state. **c** , A _/_ 2 pulse on _Q_ rotates the qubit
around the _y_ axis and prepares the qubit in a superposition along _x_ axis.

frequency is off-resonant by  SSB and wont disturb the qubit.
**_Readout_** We discussed how to manipulate the qubit state by sending signals with
frequency __ _q_ into the system to rotate the qubit. Here we discuss how to actually measure
the qubit state by sending a signal at the cavity frequency __ _c_ . As we discussed in the previous
chapter, the frequency of the cavity depends on the state of the qubit. Therefore, the natural
way to detect the state of the qubit is to measure the phase shift across the cavity by using
homodyne measurement. We take two copies of a coherent signal that has the frequency
of the cavity 1 ) and whenever we decide to readout the state of the qubit, we send one of

1 This frequency is the cavity frequency at low power meaning the dressed-cavity frequency. When we
use the cavity dressed state frequency for readout we usually need to send it at low-power and this readout
is called low-power readout. Often the fidelity of low-power readout is not very good unless we use a
parametric amplifier. However, one can also use cavity bare-frequency and again see the phase shift and
detect the state of the qubit. This method essentially uses the nonlinearity induced by the qubit-cavity
interaction and requires more power. This method is called high-power readout [75] and does not require a

54


-----


###########  ########### q ########### - ###########  ########### SSB ###########  ########### q ########### Frequency


_3.3 Qubit-cavity system characterization_

cos(  SSB t +  /2 )


![Intro to quantum measurement.pdf-61-0.png](Intro to quantum measurement.pdf-61-0.png)

Figure 3.16: **Single Sideband Modulation (SSB):** By up-converting the LO signal by  SSB the mixer
outputs at qubit frequency. The relative phase of SSB pulses determines the phase of the output signal thus
the direction of the rotation for the qubit.

the copies to the cavity and take the transmitted (reflected) signal back and demodulate it
with the other copy 1 . The demodulation results in a DC signal corresponding to the phase
difference between two copies. By reading the DC signal we can infer whether the cavity
frequency shifted up or down. Figure 3.17 demonstrates the readout process. The phase __ 0



![Intro to quantum measurement.pdf-61-1.png](Intro to quantum measurement.pdf-61-1.png)

Figure 3.17: **Qubit state readout, homophone detection:** The qubit-state-dependent phase shift is
detected by comparing the signal which passes the cavity with the reference signal.

accounts for the fixed phase difference between two signals due to the different path length
and can be set to zero by adding a phase shifter ( __ 0 = 0). Therefore the demodulation
gives _I_ = cos( __ _q_ ) and _Q_ = sin( __ _q_ ). For most practical situations the phase shift is small

parametric amplifier.
1 Basically, the idea is to make a microwave interferometer except here instead of adding signals together
we multiply them together.

55


I  cos(  q -  0


-----


_3.3 Qubit-cavity system characterization_

cos( __ _q_ ) 1, and therefore the phase shift (information about qubit state) is encoded in only
__
in one quadrature of the reflected signal _Q_ = sin( __ _q_ ) __ _q_ . The entire readout process can
__
be simply represented in a phasor diagram (see Figure 3.18). In order to measure the qubit


########### I


cos(  c t)


cos(  c t +  q

|Col1|q =|Col3|Col4|Col5|
|---|---|---|---|---|
||q e||||
||||||
||||||
||||||
||g ||||


![Intro to quantum measurement.pdf-62-0.png](Intro to quantum measurement.pdf-62-0.png)

![Intro to quantum measurement.pdf-62-1.png](Intro to quantum measurement.pdf-62-1.png)

Figure 3.18: **Readout in phase space representation:** A coherent signal with a minimum uncertainty
in each quadrature probes the cavity whose frequency shifts by __ __ depends on the state of the qubit. The
transmitted (reflected) signal acquires a state-dependent-phase shift __ 2 _/_ as discussed in Section 3.1.

state, we need to repeat the experiment _N_ times ( _N >_ 100) and each time we detect the
phase shift by a value in the _Q_ quadrature. For positive (negative) values we assign __ 1 (+1),
indicating that we have found the qubit in the excited (ground) state. After repeating the
experiment _N_ times, we gather these statistics and report the population for ground and
excited state as


_N_ +
_P_ _g_ =

_N_ + + _N_
__


_N_ _N_ + _N_ 3 __ _,_ _P_ _e_ = 1 __ _P_ _g_ _,_ (3.3.1)


_N_ + _N_ __


where _N_ is the number of the experiments where we found the qubit in ground (excited)
__
state inferred by positive (negative) values for _Q_ . The error ( _N_ + _N_ __ ) _/N_ 3 is calculated

based on binomial error.




where _N_ is the number of the experiments where we found the qubit in ground (excited)
__
state inferred by positive (negative) values for _Q_ . The error ( _N_ + _N_ ) _/N_ 3 is calculated


########## 3.3.4 ########## Rabi measurements

Now we are ready to discuss Rabi measurements. Once we know the qubit frequency from
spectroscopy, then the first experiment in the time domain is to see Rabi oscillation, since
this experiment doesnt require any pulse calibration. The idea is to send a qubit signal
(with duration _t_ ) to the system and right after that send the cavity readout pulse and
readout the state of the qubit. Normally, we repeat this experiment for different durations 1

_t_ and for each timestep, we repeat the experiment _N_ times. Figure 3.19 summarizes the
Rabi experiment setup and procedure. As we discussed in the previous section, in order to
control the qubit signal, we use a mixer as a switch which is controlled by DC pulses from
an arbitrary waveform generator (AWG). Another mixer is used to control the cavity with
the same technique to perform homodyne measurement on the cavity and detect the phase

1 Normally we sweep _t_ from 0 to 100 ns in 100 steps. In each step the experiment is repeated _N_ __ 200
times to have a reasonably small binomial error so we can see clear Rabi oscillations.

56


-----


_3.3 Qubit-cavity system characterization_

|I(t) Q(t)|Col2|
|---|---|
|||

|Col1|I(t) Q(t)|
|---|---|
|||


![Intro to quantum measurement.pdf-63-0.png](Intro to quantum measurement.pdf-63-0.png)

![Intro to quantum measurement.pdf-63-1.png](Intro to quantum measurement.pdf-63-1.png)

Figure 3.19: **Rabi measurement:** The sequence for the measurement of Rabi oscillations and the typical
room temperature circuitry are shown.

shift to readout the state of the qubit. Figure 3.20 shows a typical Rabi oscillation. The
reason we use a rather short Rabi time (100-200 ns) for Rabi measurement is because we
will use this Rabi sequence to calibrate preparation pulses ( __ -pulse and _/_ 2-pulse) which
are normally short pulses 1 . In this step, we may also tweak the readout power, frequency,
and phase to maximize the oscillation contrast as depicted in Figure 3.20a.
In order to calibrate __ -pulses, we first need to make sure that the qubit frequency is
accurate and oscillations are on-resonance with the qubit. One way to check this is to sweep
the qubit frequency while performing Rabi oscillation measurements. The resulting 2D color
plot is called chevron plot. By fitting a sine-wave to the oscillations, one can find the best
estimate of the minimum oscillation frequency which is the qubit frequency 2 . Later we will
see that with Ramsey measurement we can have a better estimation of the qubit frequency.

1 Moreover it is wise to start off by a short sequence for the experiment because we might have a qubit
with short decoherence times or there might be some calibration issue in the system which could make it
hard to see the qubit evolution at longer qubit evolution times.
2 Rabi spectroscopy is not super sensitive to the detuning in the regime of fast Rabi oscillation. Moreover,
one might think that with a stronger drive we might also stark shift the qubit. So, one would think in order to
find qubit frequency it is better to have longer Rabi sequence and slower Rabi oscillation to improve precision.
But since our main concern is __ -pulse calibration, it makes sense to do Rabi spectroscopy (chevron plot)
with actual power that we are going to use for the __ -pulses.

57


-----


_3.3 Qubit-cavity system characterization_

Time (ns)

20 40 60 80 100 **c**


1.0

0.5

0.0


55


25


![Intro to quantum measurement.pdf-64-0.png](Intro to quantum measurement.pdf-64-0.png)

![Intro to quantum measurement.pdf-64-1.png](Intro to quantum measurement.pdf-64-1.png)

20 40 60 80 100

t (ns)


20 40 60 80 100


5.16 5.52 5.26

Signal Frequency (GHz)

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||


![Intro to quantum measurement.pdf-64-2.png](Intro to quantum measurement.pdf-64-2.png)

Figure 3.20: **Chevron plot: a** , A typical result of Rabi oscillation measurements. **b** , By repeating
the Rabi measurement for different qubit frequencies we obtain the chevron plot which can be used to
calibrate the qubit frequency. **c** , The Rabi oscillation frequency versus qubit pulse frequency. As we discussed
in Chapter 2, the minimum oscillation rate corresponds to the maximum contrast for Rabi oscillations which
happens when the qubit pulse is on-resonance with qubit frequency.

After doing this calibration, we know the power, frequency and the duration for __ -pulse and
_/_ 2-pulse.

########## 3.3.5 ########## T ########## 1 ########## Measurement

One of the main characteristics of a qubit is its relaxation time. In order to measure the
lifetime of the qubit we do the following sequence: 1) We prepare the qubit in the excited
state by sending a __ -pulse to the qubit. 2) We wait for time _t_ , then 3) we measure the qubit
state by sending readout pulse to the cavity. Therefore we use the same setup that we had
in for Rabi oscillation measurements (see Figure 3.19 for schematics) but we use a slightly
different sequence from the AWG. Figure 3.21 summarizes the sequence and a result we get
from a _T_ 1 measurement.

########## 3.3.6 ########## Ramsey Measurement ( ########## T ########## 2 ##########  ########## )


With Ramsey measurement, we characterize the dephasing time for the qubit, _T_ 2 __ . For
that, again we use the same setup as we had for measurements of Rabi oscillations (see
Figure 3.19). The Ramsey sequence follows as: 1) prepare the qubit in superposition state
1 another _/_ __ 2( _|_ _g_ _/_ __ + 2-pulse to bring back the qubit to ground state _i_ _|_ _e_ __ ) by applying a _/_ 2-pulse to the qubit. 2) Wait for a time, then 1 and immediately 4) perform _t_ 3) apply

readout. The sequence for Ramsey measurement and the result has been shown in fig 3.22.

1 If the last _/_ 2-pulse has the same phase as the first _/_ 2-pulse we will put the qubit in the excited state.
If we do negative pulse (opposite rotation) we bring the qubit back to ground state. Either way is fine, all
we need is to bring the qubit to an eigenstate.

58


-----


_3.3 Qubit-cavity system characterization_

1.0

0.6

0.4

0.2


0.0


![Intro to quantum measurement.pdf-65-0.png](Intro to quantum measurement.pdf-65-0.png)

10 20 30 40
t (  s)


![Intro to quantum measurement.pdf-65-1.png](Intro to quantum measurement.pdf-65-1.png)

Figure 3.21: _T_ 1 **Measurement:** The _T_ 1 measurement sequence (consider the experimental setup depicted
in Figure 3.19) and a typical result. The qubit lifetime (relaxation time _T_ 1 ) can be measured by fitting the
result to an exponential decay function.

########## 3.3.7 ########## Full state tomography

The qubit readout projects the state of the qubit along _z_ axis. Therefore one can determine
the expectation value for __ _z_ operator as,


_z_ = __ _z_ = _P_ _g_ _P_ _e_ = _N_ + __ _N_ __ 2
__ __ __ _N_ + + _N_ __

__


_N_ + _N_ __ _._ (3.3.2)

_N_ 3


_N_ + _N_ __


Similarly, one can determine the expectation value for __ _x_ and __ _y_ as well by applying a 90
degree rotation pulse along _y_ and _x_ respectively right before the readout 1 . Therefore, a
full tomography sequence has 3 copy of each sequence with no rotation ( _z_ ), _/_ 2-rotation in
phase ( _x_ ), and _/_ 2-rotation 90 degree out phase ( _y_ ) right before the readout as depicted in
figure 3.23. The expectation values for __ _x_ and __ _y_ , can be determined in a same way,


_x_ = __ _x_ = _P_ _g_ ( _x_ ) _P_ _e_ ( _x_ ) = _N_ + __ _N_ __
__ __ __ _N_ + + _N_


_N_ + + _N_
__


(3.3.3)


_y_ = __ _y_ = _P_ _g_ ( _y_ ) _P_ _e_ ( _y_ ) = _N_ + __ _N_ __
__ __ __ _N_ + + _N_



__ _,_ (3.3.4)

_N_ + + _N_
__


where superscripts ( _x_ ) and ( _y_ )
indicate that the readout has in-phase and out-of-phase rotation pulse respectively.

1 This is exactly what we do in Ramsey where we prepare the qubit in _x_ and measure __ _x_ __ .

59


-----


_3.4 Josephson Parametric Amplifier_


1.0



0.8


0.6

0.4

0.2

0.0


![Intro to quantum measurement.pdf-66-0.png](Intro to quantum measurement.pdf-66-0.png)

10 15
t (  s)


![Intro to quantum measurement.pdf-66-1.png](Intro to quantum measurement.pdf-66-1.png)

Figure 3.22: The sequence for the Ramsey measurement (consider the experimental setup depicted in Figure 3.19) and the typical Ramsey result. The blue (red) curve is when the **Ramsey measurement:**
pulses are on-resonance (0.3 MHz off-resonance) with the qubit frequency. The dephasing time _T_ 2 __ can be
determined by fitting the data to exponentially decaying sine function _F_ ( _t_ ) = _A_ + _B_ sin(2 __  _d_ _t_ + __ ) exp( _t/T_ 2 __ ).

####### 3.4 ####### Josephson Parametric Amplifier

The signals that carry quantum information at cryogenic temperature are feeble microwave
signals. Especially for weak measurement, these signals often contain 1 photon per microsecond or less on average. Therefore measurement signals need to be amplified before __
processing at room temperature where they would otherwise be contaminated by thermal
noise. Amplification is essential and often multiple steps of amplification are needed. However, amplifiers add some noise to the signal at each step of amplification. The added noise
is not just a technical subtlety but it is rather a fundamental property of quantum mechanics [76].
In this section I follow the discussion in Ref. [76] and briefly discuss the Josephson
parametric amplifier and phase sensitive amplification. I will try to connect the discussion
to the previous chapters and add some points from the experimental perspective. For a
detailed study of noise and amplification see the nice discussions in Ref. [76].

########## 3.4.1 ########## Classical nonlinear oscillators

Similar to the transmon circuit discussed in Chapter 2, the Josephson parametric amplifier
(JPA) is a nonlinear oscillator except that the critical current is much higher for a JPA 1

compared to the transmon. This means that for JPA there are many more energy levels
bound in the potential. Moreover, a higher critical current means a weaker nonlinearity.
Therefore a JPA can be treated classically as an oscillator which has a weak nonlinearity.

1 Typically _I_ 0 (JPA) 10 _I_ 0 (Transmon) _,_ ( _E_ _J_ _/E_ _c_ ) (JPA) = 100( _E_ _J_ _/E_ _c_ ) (Transmon) .
__

60


-----


_3.4 Josephson Parametric Amplifier_

/2 - pulse (phase 0)


AWG Ch1

|Col1|Readout x|Col3|
|---|---|---|



AWG Ch3

|Col1|Readout z|Col3|
|---|---|---|



/2 - pulse (phase 90)

AWG Ch1

|Col1|Readout y|Col3|
|---|---|---|



AWG Ch3

|Col1|Readout z|Col3|
|---|---|---|



Figure 3.23: **Full state tomography readout pulses:** A readout pulse without any tomographic pulse
gives the expectation value for __ _z_ since it projects the qubit in ground or excited state. A readout pulse
augmented by tomographic pulse can be used to measure the expectation values for __ _x_ _, _ _y_ or any arbitrary
basis in the Bloch sphere.

Figure 3.24 shows the schematic for a JPA where we include the current source and corresponding impedance _Z_ 0 to drive (pump) the JPA 1 . For the currents flowing in the circuit we

![Intro to quantum measurement.pdf-67-0.png](Intro to quantum measurement.pdf-67-0.png)

Figure 3.24: **JPA Schematic:** A Josephson parametric amplifier can be considered as a nonlinear LC
oscillator (shaded region) connected to a current source via impedance _Z_ 0 .

have,

_i_ _J_ + _i_ _C_ + _i_ _Z_ = _I_ ( _t_ ) (3.4.1a)



_V_


_I_ 0 sin( __ ) + _C_ _V_ + = _I_ ( _t_ ) (3.4.1b)

_Z_ 0


_V_ = _V_ _J_ = 


2  __ __  _I_ 0 sin( __ ) + _C_  0
__ __ 2 __



 0   0

__ +
2 __ 2 _Z_


__ = _I_ ( _t_ ) _,_ (3.4.1c)
2 _Z_ 0


1 Remember, we drive the transmon through the coupling between transmon electric dipole and the
electric field. Here we directly drive the JPA by connecting it to a current source via an effective impedance
_Z_ 0 .

61


-----


_3.4 Josephson Parametric Amplifier_

where we use Josephson relations for _i_ _J_ and _V_ which is the voltage across the components 1 .
We drive the JPA with a coherent classical signal _I_ ( _t_ ) = _I_ _p_ cos( __ _p_ + __ _p_ ) and may assume
_I_ _p_ _< I_ 0 which insures that _i_ _J_ _< I_ 0 . However, we are interested to the regime where the
__ _i_ _J_ 3 __ , _I_ 0 which means the __ is small enough so that we can expand the sin( __ ) to up to order


_I_ 0 ( __ __ 3 _/_ 6) + _C_  0
__ 2 __



 0   0

__ +
2 __ 2


__ = _I_ _p_ cos( __ _p_ + __ _p_ ) (3.4.2a)
2 _Z_ 0



  2 3 2 _I_ _p_
__ __ + 2 __ + __ 0 ( __ __ __ _/_ 6) = __ 0 _I_ 0 cos( __ _p_ + __ _p_ ) _,_ (3.4.2b)


where __ 0 = 2 _C_ _I_  0 0 is the natural frequency 2 of the JPA resonator (shaded region in Fig

ure 3.24). The parameter  = 1  _/_ (2 _CZ_ 0 ) accounts for damping of the resonator due to the
coupling to the _Z_ 0 .
which appears in many nonlinear situations ranging from the pendulum to harmonic frequency generation in nonlinear The Equation (3.4.2)b is the well-known _Duffing Equation_
optics. There are variety of methods for solving the Equation (3.4.2)b. Here I follow the
method in Ref [76].
We set the phase of the pump as a reference __ _p_ = 0 and consider the solution for __ to have
both components; in-phase and out-of-phase with the pump. Therefore we use the following
ansatz,

__ = __ 0 cos( __ _p_ + __ ) = __ cos( __ _p_ _t_ ) + __ sin( __ _p_ _t_ ) _,_ (3.4.3)
__ __


where the __ ( __ ) is the amplitude of in-phase (out-of-phase) oscillations in the JPA circuit 3
__ __

By plugging the ansatz (3.4.3) into (3.4.2)b, we have


( __ 0 2 __ __ _p_ 2 ) __ __ cos( __ _p_ _t_ ) + __ __ sin( __ _p_ _t_ )


+2 __ 0 __ __ cos( __ _p_ _t_ ) __ __ 0 __ __ sin( __ _p_ _t_ )


__ __ 0 2 _/_ 6 __ __ 3 cos 3 ( __ _p_ _t_ ) + __ __ 3 sin 3 ( __ _p_ _t_ )


__ __ 0 2 _/_ 2 __ __ 2 __ __ cos 2 ( __ _p_ _t_ ) sin( __ _p_ _t_ ) + __ __ __ __ 2 cos( __ _p_ _t_ ) sin 2 ( __ _p_ _t_ )


= __ 0 2 _I_ _d_ _/I_ 0 cos( __ _p_ _t_ ) _._ (3.4.4)


1 The voltage across the parallel components are equal, we substitute its value by the voltage across the
JJ.
2 We may call this the unloaded frequency of the JPA when it is disconnected from load _Z_ 0 , or _Z_ 0 .
3 __
Note that __ is the difference between the phases of the superconducting order parameter on each
side of the junction. But it easily parameterizes the current and voltage in the circuit as we shall see in
Equation (3.4.1). So we may simply refer to it as the oscillation in the circuit for now.

62


-----


_3.4 Josephson Parametric Amplifier_

Now we apply the RWA for fast oscillating terms 1 to obtain the following equations,


( __ 0 2 __ __ _p_ 2 ) __ __ + 2 __ 0 __ __ __ __ 0 2 _/_ 8 __ __ 3 + __ __ __ __ 2 ) = __ 0 2 _I_ _p_ _/I_ 0 (3.4.5)

( __ 0 2 __ __ _p_ 2 ) __ __ __ 2 __ 0 __ __ __ __ 0 2 _/_ 8  __ __ 3 + __ __ __ __ 2  = 0 _._ (3.4.6)
 

One can rearrange the above equations in terms of the quality factor of the resonator _Q_ =


__ 0 _Z_ 0 _C_ and dimensionless detuning = 2 _Q_ (1 __ _p_ _/_ 0 ),
__


 _Q_ 2 2
 __ 8 ( __ __ + __ __ ) = _QI_ _p_ _/I_ 0 (3.4.7a)


__ + __
__ __

__ + __
__ __ __


 _Q_ 2 2
 ( __ + __ ) = 0 _._ (3.4.7b)
__ 8 __ __


Figure 3.25 shows the numerical solution to Equation 3.4.7 for __ 0 2 and __ versus dimensionless

 2 2 2
detuning . Note, __ 0 = __ __ + __ __ _, _ = atan[ __ __ _/_ __ ]. Unlike in a linear resonator (e.g. a



0.4


0.0


0.2


-1.0


0.0


![Intro to quantum measurement.pdf-69-0.png](Intro to quantum measurement.pdf-69-0.png)

![Intro to quantum measurement.pdf-69-1.png](Intro to quantum measurement.pdf-69-1.png)

-4 -2 0 2 4 -4 -2 0 2

Dimensionless detuning  ~ Dimensionless detuning  ~


~

Dimensionless detuning 


Figure 3.25: **Duffing resonator response: a** . Solutions to Equations 3.4.7. **a** The resonance frequency
decreases by increasing the power and ultimately the system enters the bi-stable regime where there are
more that one solution to the Equation 3.4.7. **b** , This bifurcation behavior also can be seen in the phase
response of the oscillator. Right before the bifurcation, the system exhibits sharp response respect to the
detuning and power. The sensitivity for power is more clearly shown in Figure 3.26

bare cavity 2 ) where the frequency is independent of the power, for nonlinear resonator the
frequency decreases for higher driving power (Fig. 3.25).
After certain power, the JPA bifurcates signaling that the system has more than one
steady state. For amplification purposes, the sweet spot is right before this bifurcation
where the system exhibits maximum sensitivity as manifest by a sharp slope in phase.
In order to understand how an amplifier works at the sweet spot, lets look at the phase __

1 For example; cos 3 ( __ _p_ _t_ ) 3 _/_ 4 cos( __ _p_ _t_ ) and cos 2 ( __ _p_ _t_ ) sin( __ _p_ _t_ ) 1 _/_ 4 sin( __ _p_ _t_ ).
2 For a cavity which hybridized with a qubit, you may see similar nonlinear behavior in the punch-out __ __
experiment during the transition between low to high power.

63


-----


_3.4 Josephson Parametric Amplifier_

versus deriving power _I_ _p_ _/I_ 0 as depicted in Figure 3.26. Figure 3.26 is a cross section of Fig-


0.8

0.4

0.0


-0.4


Small change

|Q=30 ~ =1.72|giB tfihs ni esahP|
|---|---|

in drive power


0.01 0.02 0.03 0.04 0.05

######### I ######### /I
p 0


0.01 0.02 0.03 0.04


Figure 3.26: **JPA transfer function:** The change in phase of the oscillations in JPA versus the power
of the drive. This curve is a cross section from Figure 3.25b at = 1  _._ 72 (red dashed line), shwing a sharp
response of the phase to the small changes in the power which is the essence of the JPA amplification.


ure 3.25b at = 1 _._ 72 (red dashed line). The fact that the phase response is also sharp with
respect to the small change in the power right before the bifurcation power is the essence of
JPA amplification 1 .

![Intro to quantum measurement.pdf-70-0.png](Intro to quantum measurement.pdf-70-0.png)

########## 3.4.2 ########## Paramp operation

Now we turn to connect our understanding of the JPA and its transfer function to the actual
situation that happens in the experiment. Figure 3.27 displays the minimum circuitry inside
the fridge when we add the paramp in the line.
We use an input line to send the pump signal to the paramp. Ideally, the pump (which
is relatively strong coherent signal) should be isolated from the qubit system. A directional
coupler and a circulator (the circulator C1 in Figure 3.27) prevent the pump signal from
entering the cavity 2 . The other circulator (C2 in Figure 3.27) directs the incoming pump
signal to the paramp and sends the reflected signal to the output line.

1 Note that __ here is the phase of the oscillation inside the resonator. Using the input-output relation,
one can show that the similar behavior also manifested at the phase of the reflected signal from the resonator
(e.g see chapter 3 in Ref. [77]).
2 Practically, sometimes multiple circulators are used for more isolation.

64


-----


_3.4 Josephson Parametric Amplifier_


Input #1 Input #2 Pump Output DC flux bias line


Input #1 Input #2 Pump Output


300K

40K plate

4K plate

1K plate

Mixing
chamber
plate
10mK



300K

10mK

|ut #1 Input #2 Ou Pump|Col2|utpu|
|---|---|---|
|K|||
|K|||
||||
||||

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|H 20 dB 10 dB 20 dB C2 C1 JPA||||
|||||
|||||
||20 dB|||
||10 dB|||


Figure 3.27: **The minimum experimental measurement setup with paramp:** The input lines can
be used for qubit manipulation signals and cavity probe signals. An additional input line is dedicated to the
paramp pump. The pump signal passes by a directional coupler and circulator to reach the paramp and the
reflected signal (which have acquired a phase shift) goes to the output line. A DC line also is used to flux
bias the paramp.

**Paramp calibration: single pump**

The first step in the paramp setup is to find the paramp resonance frequency and tune it
to the frequency where we wanted to operate the paramp. This can be done by looking at
the phase of the reflection tone off of the paramp as depicted in Figure 3.28a 1 . Normally
the phase response of the paramp shifts down by increasing the probe tone power (which
somewhat acts as a pump as well).
After we convince ourselves that we have a resonance frequency of the paramp at the
right place, we start pumping that with a separate signal generator and use VNA as a weak
signal probe as depicted in Figure 3.28b. By increasing the power of the pump and adjusting
the frequency of the pump and several back-and-forths we should be able to see the gain
profile. Once we see some gain we may tweak the pump power and frequency and even

1 The nonlinear response of the paramp helps to find its resonance. Similar to the punch out experiment,
one would see a shift in the phase resonance by increasing the pump power.

65


-----


_3.4 Josephson Parametric Amplifier_

the flux bias to optimize the gain profile. Normally a symmetrical Lorentzian shape gain
profile (20 dB peak/ 100 MHz bandwidth) is desirable as depicted by the dashed line in
Figure 3.28b.




![Intro to quantum measurement.pdf-72-0.png](Intro to quantum measurement.pdf-72-0.png)

-30

|VNA S21 Phase -50dBm -30dBm 1 2 Pump Out 300K|Col2|
|---|---|
|0mK||


120


120

0.0

-120


0.0

-120


![Intro to quantum measurement.pdf-72-1.png](Intro to quantum measurement.pdf-72-1.png)

![Intro to quantum measurement.pdf-72-2.png](Intro to quantum measurement.pdf-72-2.png)

5.86 5.88 5.90 5.92 5.94 5.96
Frequency (GHz)


-40

5.86 5.88 5.90 5.92 5.94 5.96
Frequency (GHz)


Figure 3.28: **The paramp single pump operation: a** , By looking at the phase response of the JPA,
we obtain a rough estimation of proper power and flux bias to have sharp behavior at a desired frequency.
**b** , Then we add a pump and set the power and frequency to the estimated values. We should be able to see
a small amount of gain by adjusting the power. Then we fine tune the power, flux bias, pump frequency,
and pump phase to obtain a reasonable amount of gain __ 20 dB and bandwidth __ 100 MHz.

**Paramp calibration: double pump**

The single pump paramp operation is not the best way to pump the paramp for practical
reasons. Mainly because the isolation provided by the directional coupler and circulator is
not perfect. Therefore the pump signal can leak into the cavity. This issue is important when
the pump frequency is the same as the cavity frequency. This happens in the situation of

66


-----


_3.4 Josephson Parametric Amplifier_

weak z-measurement where the pump and cavity come from a same generator. In low-power
measurement, any leakage of photons in cavity frequency dephases the qubit.
In order to get around this issue, we use a double-pump technique. In this case instead
of pumping the paramp with the frequency of __ _c_ we use two pumps at __ _c_ __  _SB_ where  _SB_
is the sideband frequency which is typically between 100-500 MHz. With the double pump
technique, the paramp effectively works at the cavity frequency but the pump signals are
off-resonance with the cavity.
For the double pump paramp operation, we first operate the paramp in the single-pump
mode and then simply modulate the pump tone by  _SB_ . Normally we should see the gain
profile by adjusting the pump power 1 . Figure 3.29 demonstrates the schematics for the
double pump operation.


Carrier leackage should be avoided




![Intro to quantum measurement.pdf-73-0.png](Intro to quantum measurement.pdf-73-0.png)


20




![Intro to quantum measurement.pdf-73-1.png](Intro to quantum measurement.pdf-73-1.png)

5.4 5.6 5.8 6.0 6.2 6.4

Frequency (GHz)

![Intro to quantum measurement.pdf-73-2.png](Intro to quantum measurement.pdf-73-2.png)

Figure 3.29: **The paramp double pump operation.**

########## 3.4.3 ########## Phase-sensitive amplification: phase vs amplitude

As we discussed in Subsection 3.4.1 The essence of JPA amplification is that right before the
bifurcation the reflected phase is very sensitive to the pump power as depicted in Figure 3.26.
In the phase sensitive mode of amplification, where the signal and pump have the same
frequency 2 , and we can amplify one of the quadratures and de-amplify the other quadrature.
In Figure 3.30 we demonstrate the situation for amplification of each quadrature. Note, that

1 Often double pump needs higher power but will give more stable performance for the paramp.
Not only do the signal and pump have the same frequency, but their phases are fully correlated. Practically they come from a same generator. 2

67


VNA


-----


_3.4 Josephson Parametric Amplifier_

![Intro to quantum measurement.pdf-74-0.png](Intro to quantum measurement.pdf-74-0.png)

![Intro to quantum measurement.pdf-74-1.png](Intro to quantum measurement.pdf-74-1.png)

The upper (lower) panel demonstrates the paramp operation for amplification when the information encoded in the amplitude (phase) of the signal. Figure 3.30: **Phase sensitive amplification:**

in case of qubit readout, or weak z-measurement, the information is encoded in the phase
of the signal, but in the case of homodyne detection of qubit spontaneous emission, the
information is encoded in the amplitude of the signal. We will discuss the qubit measurement
more fully in Chapter 4. We will also discuss more practical situations and some consideration
to improve the performance of the paramp (e.g. dumb-signal cancellation).

68


-----


# Chapter 4

 Quantum Measurement

The concept of measurement is very important in all disciplines of science and technology.
However, measurement is a crucial concept in the science of quantum mechanics. This is not
simply because quantum systems are small and delicate, but this is because measurement
fundamentally disturbs the quantum system.
In this chapter, we will discuss the basics of quantum measurement in a pedagogical manner.
This chapter includes the basic notion of projective measurement and more generalized types
of measurement, including weak measurement. We will discuss continuous measurement
and the stochastic master equation for the qubit-cavity system introduced in the previous
chapters.

####### 4.1 ####### Projective measurement




Consider a quantum two-level system represented by the Hamiltonian _H_ = __ _q_ __ _z_ _/_ 2 with
eigenstates _z_ and eigenvalues __ _q_ . The (pure) state of the system __ is described by __

2

_| _ __ __ _|_ __

a normalized vector in Hilbert space which can be visualized as a vector pointing from the
center of the Bloch sphere to a certain point on its surface 1 with unit radius (Fig. 4.1).
In this visualization, a projective measurement can be thought to project the state _|_ __ __
into a specific basis (direction). A projective measurement along the _i_ -basis (where _i_ can
be any direction but we mostly consider _i_ = _x, y, z_ ) can be described by two projection

 _i_
operators  __ = _| _ _i_ __ _i_ _|_ . Every time we perform a projective measurement in _i_ -basis, we
collapse the state of the qubit and find it either in the _|_ + _i_ __ or _| _ _i_ __ (Fig. 4.1).
At this point, one may ask why we consider this destructive operation as a measurement.
The point is that the probability of the state being collapsed into _|_ _i_ __ is related to the state
_|_ __ __ . To understand this, it is convenient to represent the qubit state in the measurement

1 For a qubit system the Hilbert space is 2D. Note that the surface of the Bloch sphere is a 2D manifold.

69


-----


_4.1 Projective measurement_


########### -y

![Intro to quantum measurement.pdf-76-0.png](Intro to quantum measurement.pdf-76-0.png)

Figure 4.1: **Bloch sphere:** Projective measurement of the state _|_ __ __ in the i-basis. The red and blue
arrows indicates the backaction of the measurement.

basis _{| _ _i_ _}_ ,

_|_ __ __ = _c_ + _|_ + _i_ __ + _c_ __ _| _ _i_ __ _._ (4.1.1)

According to _Borns rule_ , the probability of finding the qubit in the states _i_ are _P_ =
__  __ _z_ __ = _i_ __ 2 = _c_ 2 . Therefore, if we perform a projective measurement for _| _ __ __
__ _|_ _|_ __ _|_ _|_ _|_ _|_ __ _|_
_N_ 1 copies of __ (or repeat the same experiment _N_ times), we would get _N_ _P_ _N_
__ _|_ __ __ __ __
times result __ 1 indicating that we collapse the qubit state into _| _ _i_ __ . Therefore we figure
out the ratio _P_ + _/P_ (note we also know that _P_ + + _P_ = 1). Since the _c_ are complex
__ __ __
numbers, we still need to figure out the relative phase between the eigenstates _|_ _i_ __ . To find
the relative phase we must perform another set of projective measurements along another
basis _j_ __ = _i_ . The best choice for the second basis is when _|_ _j_ _| _ _i_ _|_ 2 = 1 _/_ 2.
We now proceed with an example: Consider a projective measurement in the _z_ -basis,
 __ _z_ = _| _ _z_ __ _z_ _|_ on a qubit state



1
_|_ __ __ = __ 2 ( _|_ + _z_ __ + _| _ _z_ __ ) _._ (4.1.2)

Assume that the measurement apparatus outputs a signal to the state _|_ _z_ __ 1 . Since the qubit is initially prepared in an equal superposition of the state _V_ = __ 1 when the state is projected
of the measurement basis, neither measurement outcome is more likely than the other. The
qubit will be collapsed into _z_ with the probability of _P_ = __  __ _z_ __ = 1 _/_ 2 and outputs
_|_ __ __ __ _|_ _|_ __
__ 1. But after the measurement, we know certainly that the qubit state is _| _ _z_ __ . If we were
to make another measurement, we would find the same result. This means we have gained
information. However, we are now completely uncertain about the measurement result in the

1 We discuss this in the previous chapter for qubit readout measurement. In the next section, we will
discuss the mechanism by which the measurement outcome is actually is generated for general measurements.

70


-----


_4.1 Projective measurement_


_x_ -basis because _z_ = __ 1 2 ( + _x_ _x_ ) . Therefore we have gained full information in _z_
_| _ __ _|_ _ | _ __

basis but lost all information in _x_ -basis. This is a consequence of the Heisenberg uncertainty
principle; we can not be certain about two non-commuting observables at the same time 1 .
In a more general case, the qubit state can be a mixture of __ _n_ s with the probabilities _P_ _n_
_|_ __
which no longer can be written as a single state vector _|_ __ __ . However, this can be represented
by a density matrix,


__ =


_P_ _n_ __ _n_ __ _n_ _._ (4.1.3)
_|_ __ _|_


The density matrix __ fully represents our state of knowledge about the system by accounting
for both the quantum superposition and classical uncertainty of the system. One can simply
visualize the mixed state as a vector (norm _<_ 1) obtained by a weighted average over states
with classical uncertainty. Similarly, projective measurement projects the mixed state along
the measurement basis;

_P_ _n_ __ _n_ __ _n_ _i_ _i_ _._ (4.1.4)
_|_ __ _| | _ __ _|_
_n_



Here we specifically focus on a projective measurement along _z_ -basis, which is the energy
eigenbasis for the qubit. For example, we represent the density matrix __ in the measurement
basis _{| _ _z_ _}_ we have,


_P_ ++ _|_ + _z_ __ + _z_ _|_ + _P_ __ _| _ _z_ __ _z_ _|_


_P_ + __ _|_ + _z_ __ _z_ _|_ + _P_ __ + _| _ _z_ __ + _z_ _|_ (4.1.5)


_P_ ++ _P_ + __
 _P_ __ + _P_ __


(4.1.6)


The diagonal element _P_ ++ ( _P_ ) is a real number that represents the probability of projecting
__
the qubit into + _z_ ( _z_ ) where _P_ ++ + _P_ = 1. The off-diagonal elements are complex
_|_ __ _| _ __ __
numbers and represent quantum coherences and we have _P_ + __ __ = _P_ __ + . Therefore, a density
matrix, in general, has three independent unknowns which means three sets of projective
measurements (e.g. in the _x_ , _y_ , and _z_ bases) are needed to fully characterize the state of the
qubit 2 .
Experimentally, we are usually able to project the qubit only along its energy eigenbasis.
But we can add unitary rotations before projection along _z_ to realize an effective projective
measurement along any arbitrary basis as discussed in the previous chapter. Projective

1 This doesnt mean we can not perform measurements on two non-commuting observables at the same
time, see Ref. [31]
2 Recall the full state tomography discussion in the previous chapter. We will discuss full state tomography
in this chapter more fully.

71


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_

measurements in the _z_ -basis give us the ratio _P_ ++ _/P_ __ , and since the probabilities must
add to one, we obtain diagonal elements. Projective measurements in the _x_ -basis ( _y_ -basis)
give us _R_ _e_ [ _P_ + __ ] ( _I_ _m_ [ _P_ + __ ]).

####### 4.2 ####### Generalized measurement in the #######  ####### z ####### basis

In this section, we discuss quantum measurement in a more detailed approach allowing us to
study generalized quantum measurement. Here we introduce the discussion in close relation
to an actual lab experiment.

########## 4.2.1 ########## Simple Model

A quantum measurement is normally modeled by a system with Hamiltonian _H_ and
_S_ _S_
a meter with Hamiltonian _H_ . The measurement is performed by turning ON the
_M_ _M_
interaction between the meter and system, _H_ int , for a certain time _t_ which entangles the
state of the qubit with the state of the meter. By performing a subsequent measurement on
the meter we collapse the entanglement and gain information.
Lets first study this by a simple model 1 . Consider Figure 4.2 where the system is a qubit

2  2
_H_ = __ _q_ __ _z_ _/_ 2 probed by a free particle _H_ = _P_ _/_ 2 _m_ passing by the qubit. Once the free
_S_ __ _M_


particle is at a minimum distance from the qubit, they interact by _H_ int = __ _g_ _z_ __ _P_ ( _t_ ). Note
that we assume the interaction is instantaneous and happens only at time _t_ = 0 when the
particle has reached a minimum distance from the qubit. The parameter _g_ is measurement
strength and in our model one can think of it as a measure of how close the particle passes
by the qubit 3 .
Here we assume that we have minimum uncertainty in position and momentum of the
particle which results in Gaussian distributions in the screen 4 .
Now, assume the qubit is initially in state __ = __ _|_ 0 __ + __ _|_ 1 __ and the meter is in the state
 which can be effectively represented as,



_x_ 2
 = _Ne_ __ 4 __ 2 _,_ (4.2.1)

1 I follow Andrew Jordans discussion from the KITP conference, 2018.
2 A free particle described by a Gaussian wave packet, which has minimum uncertainty in both position
and momentum.
3 smaller distance causes a stronger push and pull (larger _g_ ) which results in larger separation on the
screen.
4 More realistically one can assume that the interaction happens in a time scale T around _t_ = 0, in
+ _T/_ 2
that case then effective coupling would be _g_ = _T/_ 2 _g_ ( _t_ ) _dt_ and the separation is 2 _g_ . Therefore the
__ __
measurement strength depends on both interaction strength and interaction time. But here we assume that 
_g_ ( _t_ ) = _g_ ( _t_ ), meaning that the qubit and particle intact only at time _t_ = 0 when they have minimum
distance.

72


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_



![Intro to quantum measurement.pdf-79-3.png](Intro to quantum measurement.pdf-79-3.png)

![Intro to quantum measurement.pdf-79-4.png](Intro to quantum measurement.pdf-79-4.png)

![Intro to quantum measurement.pdf-79-1.png](Intro to quantum measurement.pdf-79-1.png)

![Intro to quantum measurement.pdf-79-2.png](Intro to quantum measurement.pdf-79-2.png)

![Intro to quantum measurement.pdf-79-0.png](Intro to quantum measurement.pdf-79-0.png)

Figure 4.2: **Quantum measurement, simple model:** A free particle passes by and interacts with a
qubit. The interaction is in the form of a push or pull depending on the state of the qubit. The position of the
particle when it hits the screen tells us about the state of the qubit. The free particle has its natural Gaussian
distribution. The separation between the two distributions is proportional to the interaction strength and
the interaction time.

where __ quantifies the minimum fluctuation in position for the particle 1 . The qubit and
particle interact at _t_ = 0 and the total system (qubit+meter) evolves under unitary evolution,

_U_ tot = _e_ + _ig_ _z_ __ _P_  (4.2.2)

which entangles the qubit and particle state. Therefore, the state of total system would be,


 tot = tot __ 
_U_ __



( _x_ _g_ ) 2
__ 0 exp( __
_|_ __ __ 4 __ 2



_g_ ) 2 ( _x_ + _g_ ) 2

__ ) + __ 1 exp(

4 __ 2 _|_ __ __ 4 __ 2


) _._ (4.2.3)
4 __ 2


If we then measure the position that particle landed on the screen and found that it to be
_x_ =  _x_ (the wave function of meter collapses) then our state of knowledge about the state of
qubit would be,



_g_ _x_ 
__ exp(+



_g_ _x_  _g_ _x_ 

) 0 + __ exp(
2 __ 2 _|_ __ __ 2 __



) 1 _._ (4.2.4)
2 __ 2 _|_ __




Where _N_ is a normalization constant. Therefore we learn about the state of the qubit via an
indirect measurement. This type of measurement is more general than projective measure-

1 Here we skipped irrelevant details of the free particle wave function and dynamics. Basically, the free
particle is a wave packet moving along _z_ direction, ( _r, t_ ) = _N_ exp( _k_ _r_ __ _p_ _t_ ) exp( _r_ 2 _/_ 4 __ 2 ) where _k_ _r_ = _k_ _z_ _z_ .
__ __ __
Upon the interaction with the qubit at _t_ = 0 _, z_ = 0, the particle gets pulled or pushed and obtains little
bit of momentum along _x_ direction as well, _k_ _r_ = _k_ _z_ _z_ + _k_ _x_ _x_ . We only care about the particle position at
__
the screen, so we describe the particle state by its position in the _x_ -direction at _z_ = _L_ where the screen is
located.

73


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_

ment. As the measurement strength becomes stronger, we approach projective measurement,
and if the measurement strength is weak, we are in the weak measurement limit. Now we
interpret the result of Equation (4.2.4) in these two limits.
_Projective measurement limit_ - Now consider the situation where _g_ __ __ which means the
measurement is strong such that two distributions are well separated with negligible overlap.
That means we are pretty sure about which distribution  _x_ belongs to,  _x_ __ + _g_ or  _x_ __ _g_ as
depicted in Figure 4.3. Therefore one of the terms in 4.2.4 is suppressed.




![Intro to quantum measurement.pdf-80-3.png](Intro to quantum measurement.pdf-80-3.png)

![Intro to quantum measurement.pdf-80-4.png](Intro to quantum measurement.pdf-80-4.png)

![Intro to quantum measurement.pdf-80-1.png](Intro to quantum measurement.pdf-80-1.png)

![Intro to quantum measurement.pdf-80-2.png](Intro to quantum measurement.pdf-80-2.png)

![Intro to quantum measurement.pdf-80-0.png](Intro to quantum measurement.pdf-80-0.png)

Figure 4.3: **Strong measurement:** If the particle strongly interacts with the qubit, the separation
between two distributions would be large enough so that we can readout the qubit state just by knowing in
which distribution the particle has landed.


_x_  __ + _g_ __ _g_ __ __ __ __ __ = _|_ 0 __ _,_ (4.2.5a)

_x_  __ _g_ __ _g_ __ __ __ __ __ = _|_ 1 __ _._ (4.2.5b)

This means that the qubit wave function is also projected to one its eigenstates in this limit.
In this case it is easy to define a threshold at _x_ th = 0 by which two histograms and completely
separated. If  _x > x_ th ( _x < x_ th ) we realize that the qubit has been projected into the ground
(excited) state.
_Weak measurement limit_ - Now consider the situation _g < _
, meaning that the two distributions significantly overlap. Now if we obtain  _x_ , we are not sure which distribution  _x_
belongs to. Yet, based on Equation (4.2.4), our knowledge about the qubit state is updated. If  _x_ is positive (negative) the qubit state shifts more toward the ground (excited)
state because one of the terms dominates over the other in Equation (4.2.4). Therefore by
this measurement we slightly disturb the qubit but still we know what is the qubit state
because we have measured that disturbance. In the next section we will discuss this type of
measurement more rigorously.

74


-----



_4.2 Generalized measurement in the_ __ _z_ _basis_


![Intro to quantum measurement.pdf-81-1.png](Intro to quantum measurement.pdf-81-1.png)

![Intro to quantum measurement.pdf-81-2.png](Intro to quantum measurement.pdf-81-2.png)

![Intro to quantum measurement.pdf-81-3.png](Intro to quantum measurement.pdf-81-3.png)

![Intro to quantum measurement.pdf-81-4.png](Intro to quantum measurement.pdf-81-4.png)

![Intro to quantum measurement.pdf-81-0.png](Intro to quantum measurement.pdf-81-0.png)

Figure 4.4: **Weak measurement:** In the limit that the particle weakly interacts with the qubit, the
separation between the two distributions would be smaller. This gives partial information about the state
of the qubit.

########## 4.2.2 ########## POVM


In the previous section, we studied a general type of measurement which is indirect and applies to a wide range of measurements. Formally, this type of measurement can be described
in terms of POVMs 1 . For that, lets revisit the result we had in the previous subsection in
terms of the density matrix. For a projective measurement, the qubit state which can be
described by __ = _n_ __ _n_ __ _n_ undergoes projection to one of the eigenstate

_|_ __ _|_

 __ _n_ __ _n_ _x>x_  th 0 0 (4.2.6a)


_n_ __ _n_ __ _n_ undergoes projection to one of the eigenstate

_|_ __ _|_


__ _n_ __ _n_ _x>x_  th 0 0 (4.2.6a)
_|_ __ _|_ __ __ __ _|_ __ _|_


__ _n_ __ _n_ _x<x_  th 1 1 _,_ (4.2.6b)
_|_ __ _|_ __ __ __ _|_ __ _|_
_n_



which means the final density matrix is the result of acting with the projector  _n_ on the
initial density matrix,


_x>x_  th  0 __  0
 __ 0 __ = __ _|_ 0 __ __ __ 0 _|_ Tr[ 0 __



_,_ with probability _P_ 0 = Tr[ 0 __  0 ] (4.2.7a)
Tr[ 0 __  0 ]


_x<x_  th  1 __  1
 __ 1 __ = __ _|_ 1 __ __ __ 1 _|_ Tr[ 1 __



_,_ with probability _P_ 1 = Tr[ 1 __  1 ] _,_ (4.2.7b)
Tr[ 1 __  1 ]


where Tr[ _n_ __  _n_ ] in denominator is the normalization factor. Note that we have

0 0 + 1 1 = 1 .
_|_ __ _|_ _|_ __ _|_ 
In a more general manner, one can describe partial measurements (including weak and


where Tr[ _n_ __  _n_ ] in denominator is the normalization factor. Note that we have _n_  _n_ =

0 0 + 1 1 = 1 .
_|_ __ _|_ _|_ __ _|_ 
In a more general manner, one can describe partial measurements (including weak and
strong measurements) by a set of operators  _n_ which obey the constraint _n_  __ _n_  _n_ = 1 . In

1 POVM stands for positive operator-valued measured. 


_n_  __ _n_  _n_ = 1 . In


1 POVM stands for positive operator-valued measured.


75


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_

this case we have similar operations


__ _n_ th outcome  _n_ __  __ _n_ _,_ with probability _P_ _n_ = Tr[ _n_ __  __ _n_ ] _,_ (4.2.8)
__ __ __ __  __ _n_ __ __ __ Tr[ _n_ __  __ _n_ ]

except now  is called POVM and, in general, can be described by a weighted sum over all projection operators. For example the _n_ is not necessarily a projector. Actually  _n_
POVM corresponding to the general measurement discussed in our model (Eq. 4.2.3) can be
described by



( _x_ _g_ )
 _x_  = _N_ exp( __ __ 4 __ 2


_g_ ) 2 ( _x_ + _g_ ) 2
__ ) 0 0 + exp(

4 __ 2 _|_ __ _|_ __ 4 __ 2


) 1 1 _._ (4.2.9)
4 __ 2 _|_ __ _|_


One can check that  _x_  acting on __ = __ __ , according to the Equation (4.2.8), results

_|_ __ _|_
in Equation (4.2.4). Note, the measurement outcome  _x_ is a continuous variable indicating
the position the particle detected on the screen in our model, but can be a discrete value
depending on the type of apparatus one uses for the meter 1 .

########## 4.2.3 ########## POVM in terms of physical parameters

Now we translate our model into the language of cavity QED and describe the actual weak
measurement that we perform on the qubit in experiment. In our case the qubit is probed by
a microwave coherent signal. So essentially we need to replace wave packet of the free particle
with a coherent signal. There is, of course, a exact correspondence between a Gaussian wave
packet and a coherent signal. As depicted in Figure 4.5 the coherent signal is initially
prepared along quadrature _I_ . It has minimum uncertainty along each canonical position and
momentum 2 . When the signal passes the cavity and interacts with the qubit, it acquires a
phase shift which depends upon the state of the qubit. As we discussed in Chapter 2, the
phase shift of the coherent signal can be translated to a displacement in _IQ_ plane. Assuming

3 
the phase shift happens along the _Q_ quadrature , the measurement outcome is a signal _V_
that we obtain for _Q_ quadrature of the homodyne measurement. The corresponding POVM
would be very similar to our model,


 _V_  =

_N_



(  _V_ _g_ )
exp( __
__ 4 __ 2


_g_ ) 2 (  _V_ + _g_ ) 2
__ ) 0 0 + exp(

4 __ 2 _|_ __ _|_ __ 4 __ 2


) 1 1
4 __ 2 _|_ __ _|_


(4.2.10)


1 We will see later in this chapter that this value, in our experiment, is a semi-continuous digitized
homodyne voltage.
2 Remember in our model, the wave packet also has minimum uncertainty for position and momentum.
3 This can be done in the experiment by adjusting the phase of the probe signal.

76


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_

![Intro to quantum measurement.pdf-83-6.png](Intro to quantum measurement.pdf-83-6.png)

![Intro to quantum measurement.pdf-83-7.png](Intro to quantum measurement.pdf-83-7.png)

![Intro to quantum measurement.pdf-83-0.png](Intro to quantum measurement.pdf-83-0.png)

![Intro to quantum measurement.pdf-83-5.png](Intro to quantum measurement.pdf-83-5.png)

![Intro to quantum measurement.pdf-83-3.png](Intro to quantum measurement.pdf-83-3.png)

![Intro to quantum measurement.pdf-83-2.png](Intro to quantum measurement.pdf-83-2.png)

![Intro to quantum measurement.pdf-83-4.png](Intro to quantum measurement.pdf-83-4.png)

![Intro to quantum measurement.pdf-83-1.png](Intro to quantum measurement.pdf-83-1.png)

Figure 4.5: **Weak measurement cQED: a** , The qubit-state-dependent phase shift of the cavity probe
signal. **b** , A more realistic schematic for the phase shift detection.

However we need to figure out _g_ and __ in terms of actual parameters in the measurement

[78]. As we discussed in Chapter 2, the (dimension-less) variance of coherent state in each
quadrature is 1 _/_ 4 which is the minimum fluctuation (see Exercise 7 of Chapter 2). However
in the actual experiment we collect the signal for a certain amount of time  _t_ with collection
efficiency of __ , which means the actual variance we have in the experiment is __ 2 = 1 _/_ (4 __  _t_ )
where __ is the cavity linewidth 1 . The separation between the two Gaussian distributions
results from the phase shift in the cavity frequency and also the number of photons inside
the cavity, as depicted in Figure 4.5. We have a 2 __ frequency shift of the cavity resonance
frequency which, in the limit of __ __ __ , resulting in a phase shift of 4 _/_ of the cavity
probe (see the discussion in Chapter 3 for the cavity phase shift). Therefore the separation
2 _g_ = 4 __ __ _n/_  where __ _n_  accounts for phasor vector length in _IQ_ plane as depicted in
Figure 4.5. So we have,

 _V_  = _e_ __ __  _t_ (  _V_ __ 2 __ __ _n/_  ) 2 0 0 + _e_ __ __  _t_ ( _V_  +2 __ __ _n/_  ) 2 1 1 _._ (4.2.11)

_N_ _|_ __ _|_ _|_ __ _|_

1 You may think it as a shot noise improvement in the variance. We get  __  _t_ amount of signal from the 
cavity during the measurement which improves the uncertainty by a factor of 1 _/_ __ __  _t_ .

77


-----


_4.2 Generalized measurement in the_ __ _z_ _basis_

We also define the signal-to-noise ratio (SNR) to be,


2 _g_
_S_ =

__




2 = 64 __ 2 _n_  

__




(4.2.12)


Normally in this experiment, the separation between two Gaussian distributions is always
scaled 1 to be 2 _g_ = 2. This means, one can rewrite the POVM as

 _V_  = _e_ __ 4 __ 2 _n_   _t/_ ( _V_  __ 1) 2 0 0 + _e_ __ 4 __ 2 _n_   _t/_ ( _V_  +1) 2 1 1 _._ (4.2.13)

_N_ _|_ __ _|_ _|_ __ _|_
 

 2 2
where now _V_ is the scaled signal and the variance of the scaled signal is __ = _/_ (16 __ _n_   _t_ ).
It is convenient to define _k_ = 4 __ 2 _n/_  as the measurement strength 2 which quantifies how
strong we are measuring the system regardless of the measurement time and efficiency.

 _V_  = _e_ __ _k_  _t_ (  _V_ __ 1) 2 0 0 + _e_ __ _k_  _t_ ( _V_  +1) 2 1 1 _._ (4.2.14)

_N_ _|_ __ _|_ _|_ __ _|_
 

We also define a characteristic measurement time __ = 1 _/_ (4 _k_ ) which quantifies how long we
should collect the signal to achieve __ 2 = 1 (SNR=4).
To sum up this discussion, Equation (4.2.14) describes weak measurement on the qubit
state __  _V_  __ or in a more general form,
_|_ __ _|_ __


__ __ Tr[  _V_  _V_  __ __   __ _V_  __ _V_  ] (4.2.15)


and we obtain the signal _V_ with a probability

_P_ ( _V_  ) = Tr[ _V_  __  __ _V_  ] = __ 00 _e_ __ 2 _k_  _t_ (  _V_ __ 1) 2 + __ 11 _e_ __ 2 _k_  _t_ ( _V_  +1) 2 _,_ (4.2.16)

where __ 00 ( __ 11 ) is the probability for the qubit to be in the ground (excited) state before the
measurement 3 .


1 In our model this can be adjusted by the position of the screen and in actual experiment we can simply
amplify/attenuate the signal or just simply scale the signal after digitization. Note that scaling doesnt
change the SNR.
2 The definition for measurement strength _k_ seems to be different from literature by a factor of two. This
wouldnt be an issue if we scaled the signal consistently. Here I define _k_ such that the the measurement
operator in the Lindblad equation is exactly __ _k_ _z_ .

3 Note that there is a factor of 2 difference between exponents in Equation (4.2.14) which is an operator
and Equation (4.2.16) which is a probability distribution.

78


-----


_4.3 Continuous measurement in_ __ _z_ _basis_

####### 4.3 ####### Continuous measurement in #######  ####### z ####### basis

In the previous section we studied how the state of the qubit changes under a generalized
measurement for a time  _t_ . In this section we are going to study continuous monitoring of
the qubit state in the limit of very weak measurement.


For that we start from the probability distribution of signal _V_ Equation (4.2.16). In the
limit of very weak measurement,  _t_ __ 0, the variance of the distributions __ 2 = 1 _/_ (4 _k_  _t_ ) __
1 which means that the two distributions almost overlap as depicted in Figure 4.6. In this
limit one can show that,

_P_ ( _V_  ) __ _e_ __ 2 _k_  _t_ (  _V_ __ __ 00 + __ 11 ) 2 = _e_ __ 2 _k_  _t_ ( _V_  __ __ _z_ __ ) 2 _,_ (4.3.1)

which means we can replace two distributions with one distribution which is centered at __ _z_
__ __
as depicted in Figure 4.6. Consequently the measurement operator  _V_  in Equation (4.2.14)

|V=2 |Col2|
|---|---|
| z >>1 >>1||
|||


-50 0 50


-50 0 50


Figure 4.6: **Measurement signal distribution in the weak limit:** In the limit of weak measurement,
the separation between the two distributions is much smaller than the variance of distributions. In such a
case, we can approximate the two distributions by a distribution centered at __ _z_ as shown in Exercise 1.
__ __

can be represented in a compact form up to a renormalization constant,

 _V_  _e_ __ _k_  _t_ (  _V_ __ __  _z_ ) 2 (4.3.2)

__

![Intro to quantum measurement.pdf-85-0.png](Intro to quantum measurement.pdf-85-0.png)

79


-----


_4.3 Continuous measurement in_ __ _z_ _basis_

The fact that the measurement signal has a Gaussian distribution centered on __ _z_ means
__ __
one can think of the measurement signal as a noisy estimate of __ _z_ which can be represented
as 1 , __ __
_d_

_V_ = __ _z_ + _W_ (4.3.3)
__ __ __ 4 _k_  _t_

where _d_ _W_ is a _Wiener_ increment which is a zero-mean Gaussian random variable with
variance of  _t_ .

########## 4.3.1 ########## Stochastic Schr ########## odinger equation

Now we study qubit evolution under the measurement operator  _V_  . I follow the discussion
in Ref. [79]. For now we assume __ = 1 and consider a normalized qubit pure state _|_ __ ( _t_ ) __ at
time _t_ . The qubit state at a later time _t_ +  _t_ would be,


__ ( _t_ +  _t_ ) =  _V_  __ ( _t_ ) (4.3.4a)
_|_ __ _k_ _|_  _t_ (  _V_ __ __  ) 2


_e_ __ _k_  _t_ (  _V_ __ __  _z_ ) 2 _|_ __ ( _t_ ) __ (4.3.4b)



_k_  _t_ ( __ _z_ 2 2  _V _ _z_ )
_e_ __ __ _|_ __ ( _t_ ) __ _,_ (4.3.4c)



 2
where we ignore the constant term proportional to the _V_ ) in the exponent since we are


eventually going to renormalize _|_ __ ( _t_ + _t_ ) __ . We now substitute _V_ from Equation (4.3.3) (for
now __ = 1),


__ ( _t_ +  _t_ ) = exp( _k_  _t_ __  _z_ 2 + 2 _k_  _t_ __  _z_ __ _z_ +
_|_ __ __ __ __


_k_ __  _z_ _d_ ) __ ( _t_ ) _._ (4.3.5)
_W_ _|_ __


Now we replace  _t_ __ _dt_ implying the continuous limit and expand the exponential but only
keeping terms up to first order in _dt_ ,



_k_ 2 __ _z_ 2 ( _d_ ) 2 __ ( _t_ ) _,_ (4.3.6)

########### W ########### | ########### 
 


###########  ########### ( ########### t ########### + ########### dt ########### ) ########### = ########### 1 ########### kdt ###########  ###########  ########### z ########### 2 ########### + 2 ########### kdt ###########  ###########  ########### z ###########  ########### z ########### + |    


########### k ###########  ###########  ########### z ########### d ########### + ########### k ########### 2 W


then we replace ( _d_ _W_ ) 2 = _dt_ according to stochastic calculus (It o rule) 2 and arrive at,



_k_
__ ( _t_ + _dt_ ) = 1 __  _z_ [ __ _z_ 4 __ _z_ ] _dt_ +
_|_ __ __ 2 __ __ __



_k_
_|_ __ ( _t_ + _dt_ ) __ = 1 __


_k_ __  _z_ _d_ __ ( _t_ ) _._ (4.3.7)
_W_ _|_ __


Now we need to normalize the state _|_ __ ( _t_ + _dt_ ) __ because, so far, we have ignored normalization
constants. One can show that


__ ( _t_ + _dt_ ) __ ( _t_ + _dt_ ) = 1 + 4 _k_ __ _z_ 2 _dt_ +
__ _|_ __ __ __


4 _k_ __ _z_ _d_ + [ _t_ ] 3 _/_ 2 _,_ (4.3.8)
__ __ _W_ _O_


1 In fact, this interpretation in Equation (4.3.3) comes in very handy for simulating quantum trajectories.
2
The Wiener increment _d_ _W_ has dimension of __ _t_ , see Ref. [79] for more details.

80


1 In fact, this interpretation in Equation (4.3.3) comes in very handy for simulating quantum trajectories.
2
The Wiener increment _d_ _W_ has dimension of __ _t_ , see Ref. [79] for more details.


-----


_4.3 Continuous measurement in_ __ _z_ _basis_

where we just keep terms up to the first order in _dt_ and second order in _d_ _W_ . By using a
binomial expansion, one can show that



1

[ __ __ ( _t_ + _dt_ ) _|_ __ ( _t_ + _dt_ ) __ ] __ 2



1 _k_

2
= 1
__ 2



__ _z_ 2 _dt_
2 __ __ __


_k_ __ _z_ _d_ + [ _t_ ] 3 _/_ 2 _._ (4.3.9)
__ __ _W_ _O_


When we multiply the Equation (4.3.9) by Equation (4.3.7) (and again keep terms up to _dt_
and ( _d_ _W_ ) 2 ), we obtain the normalized Stochastic Schr odinger Equation (SSE),


_d_ __ ( _t_ ) = _k_ ( __ _z_ __ _z_ ) 2 _dt_ +
_|_ __ __ 2 __ __


_k_ ( __ _z_ __ _z_ ) _d_ __ ( _t_ ) _,_ (4.3.10)
__ __ _W_ _|_ __




where we define _d_ _|_ __ ( _t_ ) __ = _|_ __ ( _t_ + _dt_ ) _|_ __ ( _t_ ) __ . For a given measurement record _{_ _V_ _}_ one
can infer _d_ _W_ (see Equation 4.3.3) and integrate this equation to obtain the qubit pure state
evolution under measurement with perfect efficiency.
For example, the evolution of a qubit initialized in a pure state __ (0) = __ 0 0 + __ 0 1 and
_|_ __ _|_ __
can be obtained by integrating the Equation (4.3.10) as follows, subject to continuous measurement for time _T_


__ _i_ +1
__ _i_ +1



__ _i_
__ _i_



__ _k_ 2 _dt_ (1 __ 0 _z_ _i_ ) 2 (1 + 0 _z_ _i_ ) 2





_k_ 2 _dt_ (1 __ 0 _z_ _i_ ) 2 (1 + 0 _z_ _i_ ) 2




__ _i_
__ _i_



+ _d_ _W_


1 _z_ _i_ 0
__
0 1 _z_ _i_
 __ __


__ _i_ _,_
__ _i_
 

(4.3.11)


__ _i_
__ _i_



where _z_ _i_ = _|_ __ _i_ _| |_ __ _i_ _|_ 2 and [ _i_ = 1 _,_ 2 _, ..., N_ ] where _N_ = _T/dt_ . Therefore, given the initial
step values 1 and reconstruct the __ 0 _, _ 0 , one can update the next values using the measurement record _quantum trajectory_ as depicted in Figure 4.7 for _N_ _d_ = 101 _W_ _i_ at each _, dt_ =

2

0 _._ 01 _, k_ = 1 _, _ 0 = __ 0 = 1 _/_ __ 2. One can also add any unitary dynamics , the SSE is used to

describe more general dynamics of the qubit state evolution.


where _z_ _i_ = _|_ __ _i_ _| |_ __ _i_ _|_ 2 and [ _i_ = 1 _,_ 2 _, ..., N_ ] where _N_ = _T/dt_ . Therefore, given the initial
step values 1 and reconstruct the __ 0 _, _ 0 , one can update the next values using the measurement record _quantum trajectory_ as depicted in Figure 4.7 for _N_ _d_ = 101 _W_ _i_ at each _, dt_ =

2

0 _._ 01 _, k_ = 1 _, _ 0 = __ 0 = 1 _/_ __ 2. One can also add any unitary dynamics , the SSE is used to


########## 4.3.2 ########## Stochastic master equation

The SSE in the form of (Eq. 4.3.10) is only applicable for pure state evolution. However
one can generalize this equation to describe mixed state evolution as well. An easy way to
obtain the generalized form is to represent (Eq. 4.3.10) in terms of density matrix 3 in this


1 In the actual experiment we obtain _V_ _i_ = _z_ _i_ + _d_ _W_ _/_ 4 _kdt_ as the measurement signal (See, Eq. 4.3.3). So,

one can rewrite 4.3.10 in terms of _V_ _i_ . But since efficient detection is not practical, we leave the 4.3.10 in this
form which is more convenient for simulating a quantum trajectory because one can simply use a Gaussian
noise generator of variance _dt_ to generate _d_ _W_ . Although for simulation purposes, the unnormalized version
of Equation (4.3.7) works even better since one can manually normalize the state at each step.
2 For example, for adding Rabi oscillation to the dynamics one also needs to consider terms like  __ = _i_  _R_ __ _i_
and __  = _i_  _R_ __ _i_ in the state update. Similar to Equation (2.4.6a) and Equation (2.4.6b).
3 The trick here is that we use a pure state _|_ __ __ to obtain the SME, and once we arrived at the equations
for the SME in terms of density matrix, these equations can be applied to any density matrix, either pure

81


-----


-4


0.8

0.4

0.0


_4.3 Continuous measurement in_ __ _z_ _basis_

1.0

  i i 0.5 0.0

-0.5

-1.0


![Intro to quantum measurement.pdf-88-0.png](Intro to quantum measurement.pdf-88-0.png)

![Intro to quantum measurement.pdf-88-1.png](Intro to quantum measurement.pdf-88-1.png)

![Intro to quantum measurement.pdf-88-2.png](Intro to quantum measurement.pdf-88-2.png)

20 40 60 80 100

Time (i dt)


20 40 60 80 100

Time (i dt)


20 40 60 80 100

Time (i dt)


Figure 4.7: **SSE update trajectory:** The measurement signal _V_ _i_ is used to infer _d_ _W_ _i_ . The pure state
evolution can then be reconstructed with the SSE. In the right panel, the evolution is represented in terms
of Bloch coordinates.

form,

__ = _|_ __ __ __ _| _ _d_ = _d_ _|_ __ __ __ _|_ + _|_ __ __ _d_ __ __ _|_ + _d_ _|_ __ __ _d_ __ __ _|_ _,_ (4.3.12)

where by substituting 1 _d_ _|_ __ __
from Equation (4.3.10) we arrive at the Stochastic Master Equation SME



_k_
_d_ = [ __ _z_ _,_ [ __ _z_ _, _ ]] _dt_ +
__ 2


_k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ ) _d_ (4.3.13)
__ __ __ _W_


########## 4.3.3 ########## Inefficient measurement

In last two sections, we assumed that the measurement is perfectly efficient, __ = 1. In this
section we relax this assumption and account for inefficient detection. Inefficient detection
can be modeled by considering two concurrent independent measurements on the system but
ignoring the measurement outcome of one of them. For that, we consider two measurement
apparatuses performing measurements on the system. The measurement strength of the first
(second) apparatus is outcome is _V_ (1) ( _V_ (2) ), _k_ (1) ( _k_ (2) ) where _k_ (1) = _k_ and _k_ (2) = (1 __ __ ) _k_ and the measurement


_V_ ( _m_ ) = __ _z_ + _d_ _W_ ( _m_ ) _,_ (4.3.14)
__ __ __ 4 _k_ ( _m_ )  _t_

or mixed. One can start from the beginning of the subsection 4.3.1 and follow the steps in density matrix
formalism and directly obtain the SME.
1 Note, here we have double-commutator.

82


-----


_4.3 Continuous measurement in_ __ _z_ _basis_

where _m_ = 1 _,_ 2. Considering both measurements, the qubit evolution would be,



_k_ (1)
_d_ = [ __ _z_ _,_ [ __ _z_ _, _ ]] _dt_ +
__ 2


_k_ (2)

[ __ _z_ _,_ [ __ _z_ _, _ ]] _dt_ +
2


_k_ (1) ( __ _z_ __ + __ _z_ 2 __ _z_ __ ) _d_ (1)
__ __ __ _W_

_k_ (2) ( __ _z_ __ + __ _z_ 2 __ _z_ __ ) _d_ (2) (4.3.15)
__ __ __ _W_


Now we ignore the second measurement outcome and average over all possible values for
_d_ _W_ (2) . Since _d_ _W_ (2) 1
is a zero mean Gaussian noise increment, the last term in Equation (4.3.15) vanishes and we arrive at the SME for inefficient detection ,



_k_
_d_ = [ __ _z_ _,_ [ __ _z_ _, _ ]] _dt_ +
__ 2


_k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ ) _d_ (4.3.16)
__ __ __ _W_


where we replace _k_ (1) = _k_ , and _k_ (1) + _k_ (2) = _k_ and have simply dropped the superscript for
_d_ _W_ (1) . For completeness, lets represent the SME in this form,


_d_ = _k_ __ _z_ __ _z_ __ 1 2 ( __ _z_ 2 + __ _z_ 2 __ ) _dt_ +


_k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ ) _d_
__ __ __ _W_


_k_ [ __ _z_ __ _z_ __ ] + 2 _k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ )( _V_ ( _t_ ) __ _z_ ) _,_ (4.3.17)
__ __ __ __ __ __


where in the last line we substitute _d_ _W_ in terms of the actual measurement signal _V_ ( _t_
according to Equation (4.3.3).
The first term in 4.3.17 is the Lindbladian term 2 _L_ __ _L_ 1 2 _L_ __ _L, _ with Lindbladian
__ _{_ _}_


The first term in 4.3.17 is the Lindbladian term 2 _L_ __ _L_ 1 2 _L_ __ _L, _ with Lindbladian
__ _{_ _}_

operator _L_  = __ _k_ _z_ as we introduced in Chapter 2 (See Eq. 2.4.19). The second term which




operator _L_ = _k_ _z_ as we introduced in Chapter 2 (See Eq. 2.4.19). The second term which

includes the measurement record and depends on quantum efficiency is the state update due
to the measurement (which is referred to as unraveling in the literature 3 ).
In last three subsections, we specifically discussed generalized measurements corresponding to the measurement operator __ _k_ _z_ , and found the the resulting SME. This SME has a


general form and simply can be extended to any relevant measurement operator _k_ _z_ , and found the the resulting SME. This SME has a __ _k_ _c_  ,


_k_ _c_  ,



1 _c_  +  _c_
__  = _k_ _c_  _c_  __ ( __ _c_  __ _c_  +  _c_ __ _c_  ) + 2 _k_ ( _c_ + __ _c_  __ _c_  +  _c_ __ __ )( _V_ ( _t_ )
__ 2 __ __ __ 2



1 _c_  +  _c_

( __ _c_  __ _c_  +  _c_ __ _c_  ) + 2 _k_ ( _c_ + __ _c_  __ _c_  +  _c_ __ __ )( _V_ ( _t_ )
2 __ __ __ 2


__ ) _,_

(4.3.18)


1 Similarly, one can model other types of imperfections and sources of decoherence in the system (e.g.
relaxation and dephasing) by considering that the environment performs measurements on the system (via
a measurement operator __ __ _X_  which depends on the type of decoherence) and we do not have access to the
outcomes of these measurements.
2 The term _L_ __ _L_ 2 1 _L_ __ _L, _ = [ _L_ ] __ is usually called dissipation superoperator term.

3 In the literature you might find the argument that unraveling is not unique [77,80]. It is true that there __ _{_ _}_ _D_
are many ways to unravel SME so that the average of many trajectories converge to the same Lindbladian
evolution. But once you choose your efficient detector then the unraveling is unique. What about inefficient
detector?


1 Similarly, one can model other types of imperfections and sources of decoherence in the system (e.g.
relaxation and dephasing) by considering that the environment performs measurements on the system (via
a measurement operator __ __ _X_  which depends on the type of decoherence) and we do not have access to the
outcomes of these measurements.
2 The term _L_ __ _L_ 2 1 _L_ __ _L, _ = [ _L_ ] __ is usually called dissipation superoperator term.

3 __ _{_ _}_ _D_


83


-----


_4.3 Continuous measurement in_ __ _z_ _basis_


where still represents the measurement strength. We will see that the measurement operator can even be non-Hermitian. _k_
We can also add other type of imperfections to the dynamics. For example, the qubit
decoherence due to the dephasing can be modeled by considering that environment also
measures the system with measurement operator __ 2 2 __  _z_ where the __ 2 is the dephasing rate 1 .

However we do not have access to that measurement record. Therefore we sum over all



possible outcomes for the environment (as we did for inefficient detection treatment) and
obtain,



__ 2
( _k_ + ) [ __ _z_ __ _z_ __ ] + 2 _k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ )( _V_ ( _t_ ) __ _z_ )

2 __ __ __ __ __ __


(4.3.19)


One can show that Equation (4.3.19) has following representation in terms of Bloch
components _x_ __ _x_ _, z_ __ _z_ ,
__ __ __ __


4 _k_ (1 __ _z_ 2 )( _V_ ( _t_ ) __ _z_ ) (4.3.20a)



__ 2
__ 2( _k_ +


2 ) _x_ __ 4 _kxz_ ( _V_ ( _t_ ) __ _z_ ) _._ (4.3.20b)


It is worth discussing the ensemble behavior of these equations, which occurs when we average
over all possible measurement signals (that means we measure the system but disregard or
dont have access to the measurement results). Lets consider the special case where the
qubit is prepared in the superposition state _z_ = 0 _, x_ = 1. It is apparent that in this case
that  _z_ = 0 but the quantum coherence _x_ decays by the rate 2 __ + __ 2 ,

_x_ = _e_ __ (2 _k_ + __ 2 ) _t_ _._ (4.3.21)

Apart from the natural dephasing rate __ 2 which is ideally negligible, the qubit also dephases
due to the unmonitored measurement photons,



8 __ 2 
 = 2 _k_ =


(4.3.22)


which is called _measurement induced dephasing_ 2 .
One can also add unitary evolution to the SME (4.3.17) to account for a coherent drive


1 This effect is significant if the total measurement time is comparable to the dephasing time or the
measurement strength _k_ is comparable to the dephasing rate __ 2 . The dephasing rate is ideally __ 2 = __ 1 = 1


2 1 =


2 2 2 2 _T_ 1

where the _T_ 1 is the relaxation time for the qubit.
2 Later we will utilize this equation for calibration.


84


-----


_4.4 Bayesian update_

on the qubit and obtain the full version of SME,


__  = _i_ [ _H_ _R_ _, _ ] + _k_ [ __ _z_ __ _z_ __ ]
__ __

+ 2 _k_ ( __ _z_ __ + __ _z_ 2 __ _z_ __ )( _V_ ( _t_ ) __ _z_ ) _,_ (4.3.23)
__ __ __ __ __


where _H_ _R_ represents the Hamiltonian for a drive on the qubit 1 . In Section 4.7 and 4.8, we will
study the combined unitary and non-unitary evolution of the qubit for both _z_ -measurement

2

__ _k_ _z_ , and __ -measurement __ 1 __ in more details.

__ __ __

####### 4.4 ####### Bayesian update

Although the SME (Eq. 4.3.17) is a formal description for open quantum systems, the fact
that it is a nonlinear equation makes it less convenient to work with. There is a fairly
straightforward method to reconstruct qubit trajectory which is based on Bayes theorem,



_P_ ( _B_ _A_ ) _P_ ( _A_ )
_P_ ( _A_ _B_ ) = _|_ _,_ (4.4.1)
_|_ _P_ ( _B_ )

where _P_ ( _A_ _|_ _B_ ) is the probability of event _A_ given that event _B_ has happened. In connection
with quantum measurement one can assume that:

event _A_ __ finding the qubit in ground/excited state _,_

event _B_ __ obtaining the measurement signal _V._

Therefore, one can use Bayes rule to infer the qubit evolution conditioned on the measurement signal _V_ . According to Bayes rule we have,



_P_ ( _V_ _i_ 0) _P_ _i_ (0)
_P_ _i_ +1 (0) = _P_ (0 _V_ _i_ ) = _|_ (4.4.2a)
_|_ _P_ ( _V_ _i_ )



_P_ ( _V_ _i_ 1) _P_ _i_ (1)
_P_ _i_ +1 (1) = _P_ (1 _V_ _i_ ) = _|_ _,_ (4.4.2b)
_|_ _P_ ( _V_ _i_ )


1 Normally we consider _H_ _R_ =  _R_


2 _R_ __ _x_ or  2 _R_


1 Normally we consider _H_ _R_ =  2 _R_ __ _x_ or  2 _R_ __ _y_ where we assume that drive is resonant. In general, any

coherent drive, detuned, or along any axis can be added to the SME. The coherent drives Hamiltonian
is conveniently represented in the rotating frame of the drive. Note that this is convenient because the
experiment happens in the rotating frame of the drive. The preparation and tomography pulses are from the
same generator that that is used for the drive, therefore we pulse the qubit in rotating frame of the drive.
This should not be confused with cavity homodyne measurement. Homodyne measurement happens in the
rotating frame of the cavity. Therefore, the experiment involves two independent rotating frames for two
different purposes.
2 In this document, we interchangeably use  __ -measurement and  _x_ -measurement for the measurement
__
corresponding to the measurement operator __ __ 1 __ .
__


85


-----


_4.4 Bayesian update_

where _P_ _i_ (0) and _P_ _i_ (1) are the probabilities for the qubit to be in the ground and the excited
state before the measurementthese are our prior knowledge in the _i_ th step of the update.
Then we get the updated probabilities for the qubit state, _P_ _i_ +1 (0) and _P_ _i_ +1 (0) conditioned
on measurement outcome _V_ _i_ . The updated probabilities would be our prior knowledge for
the next step of state update. The probability _P_ ( _V_ _i_ ) is the unconditioned probability for
getting signal _V_ _i_ based on our prior knowledge.
The Bayesian approach is powerful because it connects the unknown conditional probability _P_ (0 _V_ _i_ ) to a well-known conditional probability _P_ ( _V_ _i_ 0). Note that _P_ ( _V_ _i_ 0) and _P_ ( _V_ _i_ 1)
_|_ _|_ _|_ _|_
are nothing but the Gaussian distributions separated by  = 2 as we discussed in Equation (4.2.16), _V_


_P_ ( _V_ _i_ ) __ 00 _e_ __ ( _Vi_ 2 __ __ 2 1)2


2 __ __ 2 1)2 + __ 11 _e_ __ ( _Vi_ 2 +1)2 __ 2


2 __ 2 _,_ (4.4.3a)


_P_ ( _V_ _i_ 0) _e_ __ ( _Vi_ 2 __ __ 2 1)2
_|_ __


2 __ 2 _,_ (4.4.3b)



( _Vi_ +1)2
_P_ ( _V_ _i_ 1) _e_ __ 2 __ 2
_|_ __


2 __ 2 _,_ (4.4.3c)


where __ 2 = 1 _/_ (4 _k_  _t_ ) as we discussed in Section 4.3.
Now in order to clearly connect Bayes theorem to the quantum trajectory, we proceed
by dividing two conditional probabilities in Equation (4.4.2a) and (4.4.2b),


_P_ _i_ +1 (0) (0 _V_ _i_ )

= _P_ _|_
_P_ _i_ +1 (1) _P_ (1 _V_ _i_



(0 _V_ _i_ ) _i_ (0)

_|_ = _P_

_P_ (1 _V_ _i_ ) _P_ _i_ (1)
_|_



_i_ (0) _P_ ( _V_ _i_ 0)

_|_ _,_ (4.4.4)
_P_ _i_ (1) _P_ ( _V_ _i_ 1)
_|_


and substitute the last term form Equation (4.4.3b) and (4.4.3c),


_P_ _i_ +1 (0) _i_ (0)

= _P_
_P_ _i_ +1 (1) _P_ _i_



_i_ (0) _V_

exp(+
_P_ _i_ (1) __ 2



2 _V_ _i_ ) _,_ (4.4.5)
__


where we prefer to explicitly have  _V_ (which equals 2) in our representation 1 . Now by
considering the fact that _P_ _j_ (0) + _P_ _j_ (1) = 1, one can calculate _P_ _i_ +1 (0) and _P_ _i_ +1 (1) given the
prior knowledge _P_ _i_ (0) and _P_ _i_ (1) and measurement outcome _V_ _i_ .
Before we proceed further, lets switch the notation to the density matrix language which
later allows us to make comparison between Bayesian update and SME update. For that we
have _P_ _i_ +1 (0) __ 00 ( _t_ + _dt_ ) and _P_ _i_ (0) __ 00 ( _t_ ) and similarity for _P_ _i_ +1 (1) __ 11 ( _t_ + _dt_ ) and
__ __ __
_P_ _i_ (1) __ 11 ( _t_ ) and obtain,
__


__ 00 ( _t_ + _dt_ ) 00 ( _t_ )

= __
__ 11 ( _t_ + _dt_ ) __ 11 ( _t_



00 ( _t_ ) _V_

exp(+
__ 11 ( _t_ ) __ 2



2 _V_ _i_ ) _._ (4.4.6)
__


1 Note that the sign in the exponent depends on which way the Gaussian shifts for the ground and excited
states. The convenient choice is when the Gaussian shifts in the positive direction for ground state which is
consistent with the interpretation in Equation (4.3.3).

86


-----


_4.4 Bayesian update_


Equation (4.4.6) only allows us to calculate the evolution for diagonal elements of the density
matrix. In order to account for off-diagonal elements 1 . Lets assume that the qubit at time
_t_ , before the _i_ th-measurement, was in state __ ( _t_ ) = __ 00 ( _t_ ) 0 + _e_ _i_ __ 11 ( _t_ ) 1 . After the
_|_ __ _|_ __ _|_ __


_t_ , before the _i_ th-measurement, was in state __ ( _t_ ) = __ 00 ( _t_ ) 0 + _e_ _i_ __ 11 ( _t_ ) 1 . After the

measurement the state would be __ ( _t_ + _dt_ ) _|_ = __ __ 00 ( _t_ + 1) 0 _|_ + __ _e_ _i_ __ 11 ( _t_ + 1) _|_ 1 __ where we
_|_ __ _|_ __ _|_ __


__ 00 ( _t_ ) 0 + _e_ _i_

0 _|_ + __ _e_ _i_ __ 11
_|_ __ 


measurement the state would be __ ( _t_ + _dt_ ) = __ 00 ( _t_ + 1) 0 + _e_ _i_ __ 11 ( _t_ + 1) 1 where we

assume that the measurement doesnt change the relative phase _|_ __ _|_ __ 2 __ . The density matrix _|_ __
before the measurement would be,


00

__ 00 ( _t_ + 1) 0 + _e_ _i_
_|_ __ 2 __




__ ( _t_ ) = __ ( _t_ ) __ ( _t_ ) = __ 00 ( _t_ ) 0 0 + __ 11 ( _t_ ) 1 1
_|_ __ _|_ _|_ __ _|_ _|_ __


+ _e_ __ _i_




__ 00 ( _t_ ) __ 11 ( _t_ ) 0 1 + _e_ _i_
_|_ __ _|_




__ 11 ( _t_ ) __ 00 ( _t_ ) 1 0 (4.4.7)
_|_ __ _|_


and similarly for after measurement __ ( _t_ + _dt_ ) = _|_ __ ( _t_ + _dt_ ) __ __ ( _t_ + _dt_ ) _|_ . Therefore we arrive
at a relation for off-diagonal elements,


__ 01 ( _t_ + _dt_ )

__ 01 ( _t_ )


__ 00 ( _t_ + _dt_ ) __ 11 ( _t_ + _dt_ )

_._ (4.4.8)
__ 00 ( _t_ ) __ 11 ( _t_ )


__ 00 ( _t_ + _dt_ ) __ 11 ( _t_ + _dt_ )


One can add a damping term to this relation to phenomenologically account for additional
dephasing (e.g. a finite _T_ 2 __ time, finite efficiency),


__ 01 ( _t_ + _dt_ )

__ 01 ( _t_ )


__ 00 ( _t_ + _dt_ ) __ 11 ( _t_ + _dt_ ) _e_ __ _dt_ _,_ (4.4.9)

__ 00 ( _t_ ) __ 11 ( _t_ )


__ 00 ( _t_ + _dt_ ) __ 11 ( _t_ + _dt_ )


where __ = 8 __ 2 _n_  __ (1 __ __ ) +1 _/T_ 2 __ accounts for both depashing due to imperfect detection and finite

qubit coherence time.


where __ = 8 __ 2 _n_  (1 __ __ )


########## 4.4.1 ########## Bayesian update in terms of the Bloch components

It is convenient to represent the Bayesian update in terms of _z_ = __ _z_ , _x_ = __ _x_ . By
__ __ __ __
that the Equation 4.4.6 and 4.4.9 can be represented in the following form considering that, _z_ = 2 __ 00 __ 1 and _x_ = 2 __ 01 and the fact that __ 00 + __ 11 = 1, one can show 3 ,


1 + _z_ ( _t_ ) + ( _z_ ( _t_ ) 1) _e_ __ _V_ ( _t_ ) _S/_  _V_
_z_ ( _t_ + _dt_ ) = __


(4.4.10a)
1 + _z_ ( _t_ ) __ ( _z_ ( _t_ ) __ 1) _e_ __ _V_ ( _t_ ) _S/_  _V_


1 __ _z_ ( _t_ + _dt_ )


_e_ __ _dt_ (4.4.10b)
1 __ _z_ ( _t_ ) 2


_x_ ( _t_ + _dt_ ) = _x_ ( _t_ )


1 Here I follow Korotkovs discussion in [81]
2 In the Bloch sphere picture, this is to say that the measurement back-action only kicks the state up
or down but not to the sides. In Korotkovs terminology there is only spooky backaction, no realistic
backaction.
3 We define _z_ = __ _z_ = Tr( __ _z_ ) = __ 00 __ 11 = 2 __ 00 1. Note for off-diagonal elements we have __ 01 = __ __ 10
__ __ __ __
and here we assumed that __ 01 is real. Therefore _x_ = __ __ _x_ __ = Tr( __ _x_ ) = 2 __ 01 and _y_ = 0

87


-----


_4.5 Bayesian vs SME_

where _S_ = ( _V/_ ) 2 is the signal-to-noise ratio. Theses equations, similar to the SME
(4.3.19), can be use to update the qubit trajectory for continuous _z_ -measurement.
Note that, unlike the SME, here we have not made any assumption about _dt_ or the
measurement strength 1 . So the _dt_ can in general be any duration, _dt_  _t_ = _T_ , and in
_T_ __
that case _V_ ( _t_ ) _V_ ( _T_ ) = 1 _/T_ _V_ ( _t_ ) _dt_ . Therefore, the Equation (4.4.10) can be used to
0
obtain final Bloch coordinate positions __  _z_ ( _T_ ) and _x_ ( _T_ ) without integration. For example, in
a simple situation where the qubit starts in a superposition of the measurement operator
eigenstates _x_ (0) = 1 _, z_ (0) = 0 we have,


1 _e_ __ _V_ ( _T_ ) _S/_  _V_
_z_ ( _T_ ) = __

_V_ ( _T_ ) _S/_  _V_ = tanh(
1 + _e_ __


2 _V_ _V_ ( _T_ )) (4.4.11)


_x_ ( _T_ )


1 __ _z_ ( _T_ ) 2 _e_ __ _dt_ = sech(


2 _V_ _V_ ( _T_ )) (4.4.12)


Therefore the final state is determined only by the averaged signal _V_ ( _T_ ). This is because
all measurements commute with one another and commute with the Hamiltonian 2 .

####### 4.5 ####### Bayesian vs SME

We have introduced two approaches for qubit state update. The SME approach (Eqs. 4.3.20)
and the Bayesian update approach (Eqs. 4.4.10). Now the question is What is the difference? And what are the pros and cons of each approach? More importantly, do they even
agree? We know that in order to arrive at the SME, we did a bunch of expansions and
approximations regarding the weak measurement limit. However, for the Bayesian update
we did not make any assumption (except the assumption that Bayess rule applies). So, in
principle one should arrive at the SME by expanding the Bayesian result. For that, lets start
off by Equations (4.4.10a) and substitute _S/_  _V_ = 8 _kdt_ and calculate _dz_ = _z_ ( _t_ + _dt_ ) __ _z_ ( _t_ )
(we drop the notation showing time dependence for compactness),


(1 _z_ 2 ) sinh(4 _kV dt_ )
_dz_ = __ (4.5.1a)

cosh(4 _kV dt_ ) + _z_ sinh(4 _kV dt_ )

= 4 _kV_ (1 __ _z_ 2 ) _dt_ __ (4 _k_ ) 2 _V_ 2 ( _z_ + _z_ 3 ) _dt_ 2 + _O_ [ _dt_ ] 3 _/_ 2 _,_ (4.5.1b)

where we expand 3 sinh and cosh to arrive at Equation (4.5.1b). Now we substitute _V_ =
_z_ + __ 4 _d_ _kdt_ _W_ only in the second term in 4.5.1b and keep terms up to the first order of _dt_


1 We need to make that assumption if we add unitary dynamics to the Bayesian update.
2 Note, if we add a Rabi drive then the Hamiltonian would not commute with the measurement operator.
So we have to do step-wise integration similar to the SME.
3 We keep terms up to the second order of _dt_ , but remember _V_ includes a term which is effectively in the
order of 1 _/_ __ _dt_ , Equation (4.3.3).

88


-----


_4.6 Generalized measurement in the_ __ _x_ _basis_

(remember ( _d_ _W_ ) 2 = _dt_ ), therefore we have,


_dz_ = 4 _kV_ (1 __ _z_ 2 ) _dt_ __ 4 _k_ ( _z_ __ _z_ 3 ) _dt_ + _O_ [ _dt_ ] 3 _/_ 2 (4.5.2)

__ _z_  = 4 _k_ (1 __ _z_ 2 )( _V_ __ _z_ ) + _O_ [ _dt_ ] 1 _/_ 2 _,_ (4.5.3)

where  _z_ = _dz/dt_ . Equation (4.5.3) is in agreement with the SME (4.3.20a).

![Intro to quantum measurement.pdf-95-0.png](Intro to quantum measurement.pdf-95-0.png)

Now the question is why we bother considering SME while we have the exact equations
from the Bayesian update. The answer is that SME has greater flexibility and can be used
for any measurement operator. We will see in the next section that for _x_ -measurement 1

there is no Bayesian update equation.

####### 4.6 ####### Generalized measurement in the #######  ####### x ####### basis

In this section, we study continuous measurement with the measurement operator __ __ .
__
This measurement operator occurs in homodyne detection of qubit emission. We may refer
to this measurement as _x_ -measurement since, as we will see later, we normally set the
measurement phase so that the homodyne signal in related to _R_ _e_ [ __ __ ] = __ _x_ .

########## 4.6.1 ########## POVM

We follow a phenomenological approach to formulate the corresponding POVM. Consider
a qubit which decays into a transmission line by rate of __ 1 as depicted in Figure 4.8. This
configuration can be described by the interaction Hamiltonian 2

_H_ int = __ 1 ( __ _a_  __ + __ + _a_  ) _,_ (4.6.1)
__ __

where __ 1 is the relaxation rate for the qubit and  _a_ __ ( _a_ ) is creation (annihilation) operator
for the corresponding electromagnetic mode of the transmission line 3 . Now assume that the

1 By _x_ -measurement, we mean the measurement with measurement operator __ . We refer to it as _x_
__
measurement because the measurement signal in that measurement is related to the 2 The interaction Hamiltonian before taking the RWA is _H_ int = __ 1 ( __ + __ + )( _a_ +  _R_ _a_ _e_ __ [ __ ). __ ] = __ _x_ .
3 What happens to the cavity in this interpretation? One can think of that the cavity mediates the qubit __ __
emission. In this interpretation, the qubit has faster relaxation into the transmission line when the qubit and
cavity are closer in frequency. However, a more realistic interpretation considers that the qubit and cavity
hybridize. Therefore, the first two eigenstates of the combined qubit-cavity system act as a effective qubit
as discussed in Chapter 2. This interpretation is more accurate in the limit of strong hybridization, where

89


-----


Qubit emission


_4.6 Generalized measurement in the_ __ _x_ _basis_

detector

LO


![Intro to quantum measurement.pdf-96-0.png](Intro to quantum measurement.pdf-96-0.png)

Figure 4.8: _x_ **-measurement schematic:** A qubit decays into a modeof the transmission line where we
perform homodyne measurement.

qubit is initially is in state
__ = __ 0 _g_ + __ 0 _e_ _,_ (4.6.2)
_|_ __ _|_ __

and the transmission line is in the vacuum state _|_  __ = _|_ 0 __ tr where we use superscript __ _tr_ for
the transmission line. After time _dt_ , the unnormalized state of total system would be in an
entangled state,


 tot = __ 0 _|_ 0 _|_ 0 __ tr + __ 0


1 __ __ 1 _dt_ _|_ 1 _|_ 0 __ tr + __ 0


__ 1 _dt_ 0 1 tr _._ (4.6.3)
_|_ _|_ __


If we perform photon detection on transmission line, the (unnormalized) state of the qubit
would be,


detecting no photon 0 tr __ = __ 0 _g_ + __ 0
_|_ __ __ _|_ __


1 __ 1 _dt_ _e_ (4.6.4a)
__ _|_ __


detecting a photon 1 tr __ = _g_ _,_ (4.6.4b)
_|_ __ __ _|_ __


where __ 1 _dt_ is the probability of a relaxation event when the qubit is excited.
However, if we perform homodyne measurement instead of photon detection, then the
field of the transmission line collapses to a coherent state __ tr
_|_ __
and we will obtain a measurement outcome __ ,


 tot = __ 0 _g_ + __ 0
_|_ __


1 __ __ 1 _dt_ _|_ _e_ __ _|_ __ __ tr __ __ _|_ 0 __ tr + __ 0


__ 1 _dt_ _g_ __ tr __ 1 tr
_|_ _|_ __ __ _|_ __


_e_ _|_ __ _|_ 2 _/_ 2 __ 0 _g_ + __
_|_ __

2

 __ _/_ 2


1 __ 1 _dt_ _e_ + __ __ __
__ _|_ __


__ 1 _dt_ _g_ __ tr _,_ (4.6.5)
_|_ __ _|_ __


where we use __ __ _|_ 0 __ tr 1 = _e_ _|_ __ _|_ 2 _/_ 2 and __ __ _|_ 1 __ tr = __ 2 __ _e_ _|_ __ _|_ 2 _/_ 2 and we absorb constants in the
normalization factor . We assume that __ is real and define _V_ = __ __ __ 1 _dt_ where _V_ is the


the qubit state is a polariton state.
1 Note, __ = _e_ _|_ __ _|_ 2 _/_ 2 _n_ __ __ _n_ _n_ ! _n_

2 _|_ __ _|_




1 Note, __ = _e_ _|_ __ _|_ 2 _/_ 2 _n_ __ __ _n_ _n_ ! _n_ therefore, _n_ __ = __ __ _n_ _n_ ! 0 __ where 0 __ = _e_ _|_ __ _|_ 2 _/_ 2 .

2 This choice makes the measurement to be _|_ __ _|_ __ __ _|_ _e_ __ [ __ ] so we call it __ _|_ __ _x_ __ -measurement. Experimentally, the _|_ __

 _R_ __

paramp phase ( the phase of our phase sensitive parametric amplifier) can be set so that all information is
encoded only in the real quadrature.


__ _n_


_n_ _n_ ! _n_ therefore, _n_ __ = __ __ _n_ _n_

_|_ __ __ _|_ __


90


-----


_4.6 Generalized measurement in the_ __ _x_ _basis_

homodyne signal. Therefore the qubit state after the measurement will be


_V_ 2
_e_ __ 2 __ 1 _dt_ __ 0 _g_ + __

_|_ __


1 __ 1 _dt_ _e_ + _V _ 0 _g_ _._ (4.6.6)
__ _|_ __ _|_ __


Note that __ is not normalized yet. One can show that the corresponding POVM connecting
the qubit state before the measurement (Equation 4.6.2) to qubit state after the measurement
(Equation 4.6.6) has this form (up to a normalization factor),


_V_ 2
 _V_ = _e_ __ 2 __ 1 _dt_ _g_ _g_ +

_|_ __ _|_


1 __ 1 _dt_ _e_ _e_ + _V_ _g_ _e_ _,_ (4.6.7)
__ _|_ __ _|_ _|_ __ _|_


_V_
_e_ __ 2 __ 1


2 __ _V_ 1 2 _dt_ 1 __ 1 _dt_
__ 2


2 __ + __ __ + _V _ __


(4.6.8)


where we find Eq. 4.6.8 by expanding Eq. 4.6.7 up to the first order in _dt_ [82].

![Intro to quantum measurement.pdf-97-0.png](Intro to quantum measurement.pdf-97-0.png)

Now lets look at the probability of getting a measurement signal _V_ ,


_P_ ( _V_ ) =  _V_ __ 2 = __  __ _V_  _V_ __ (4.6.9)
_|_ _|_ _|_ __ _|_ _|_ __



_V_ 2

__ 1 _dt_ 1 __ 1 ( _dt_ _V_ 2 ) __ + __ + _V_ __ + + __ _,_ (4.6.10)
__ __ __ __ __ __ __ __

__ _V_ 1 2 _dt_  1 __ 1 _dt_ (1 _V_ 2 )(1 + _z_ ) + _V x_ _,_  (4.6.11)



_V_ 2
_e_ __ __ 1



_V_ 2
_e_ __ __ 1


__ _V_ 1 2 _dt_ 1 __ __ 1 2 _dt_


2 (1 __ _V_ 2 )(1 + _z_ ) + _V x_ _,_ (4.6.11)


where _z_ = __ _z_ and _x_ = __ _x_ . In the limit of continuous measurement _dt_ 0 we have,
__ __ __ __ __



_V_ 2
_P_ ( _V_ ) _e_ __ __ 1 _dt_ (1 + _V x_ ) _,_ (4.6.12)



1
exp ( _V_ 2 2 __ 1 _dtV x_ )
__ __ 1 _dt_ __



( _V_ __ 1 _xdt/_ 2)
exp __
__ __ 1 _dt_


(4.6.13)

(4.6.14)


It is convenient to rescale the signal to have variance __ 2 = __ 1 _dt_ therefore we arrive at 1 ,


1 ( _V_ __ 1 _xdt_ )
_P_ ( _V_ ) __
__ __ 2 __ 1 _dt_ exp __ 2 __ 1 _dt_


(4.6.15)


1 We could do this rescaling right at the beginning by defining the homodyne signal as _V_ = __ 1 _dt/_ 2.

This scaling may have to do with the fact that with homodyne measurement we only collect half of the signal



on average.

91


-----


_4.6 Generalized measurement in the_ __ _x_ _basis_

where we also added the normalization factor.
Equation (4.6.15) is analogous to Equation (4.3.1), However this time the measurement signal distribution is shifted by __ 1 _x_ and
__ __
has variance of __ 1 _dt_ as depicted in Figure 4.9. Therefore, the homodyne signal can be



|x 1dt|Col2|
|---|---|
|>> dt 1||
|||


0.5 0 0.5

Figure 4.9: **Homodyne measurement signal distribution in the weak limit,** _x_ **-measurement:** Note
that __ 1 _dt_ 1 therefore __ __ 1 _dt_ __ 1 _dt_
__ __

described in the form 1 ,

_V_ = __ 1 _x_ _dt_ + __ __ 1 _d_ = __ 1 _x_ _dt_ + __ __ 1 _ddt,_ (4.6.16)
__ __ _W_ __ __

where _d_ _W_ and _d_ are zero-mean Gaussian distributions with variance of _dt_ and _dt_ __ 1
respectively (therefore __ 1 _d_ has variance of __ 1 _dt_ ).
__ _W_

########## 4.6.2 ########## SME

Now we turn to state evolution and calculating the SSE and SME. For the SSE we simply
need to calculate the change in state _|_ __ __ during the measurement time _dt_ ,


_d_ __ = __ ( _t_ + _dt_ ) __ ( _t_ ) = ( _V_ 1) __
_|_ __ _|_ 2 _|_ __ __


_V_ 2
_e_ __ 2 __ 1


2 __ _V_ 1 2 _dt_ __ 1 _dt_
__ 2


2 __ + __ __ + _V _ __


_|_ __ __ _._ (4.6.17)


1 It worth mentioning that, in case of inefficient detection, the signal would be _V_ = __ __ 1 _x_ _dt_ + __ __ 1 _d_ .
__ __ _W_
This intuitively makes sense because we always rescale the signal to have variance __ 1 _dt_ regardless of the
efficiency __ . Still, inefficient measurement decreases the SNR since the greatest mean separation of the
homodyne signal conditioned on __ _x_ __ scales linearly in __ .

92


-----


_4.6 Generalized measurement in the_ __ _x_ _basis_

In order to obtain the SME we calculate _d_ = _d_ _|_ __ __ __ _|_ + _|_ __ __ _d_ __ __ _|_ + _d_ _|_ __ __ _d_ __ __ _|_ ,



__ 1 _dt_
_d_ = __ 2 __ + __ __ + _V _ __



__ 1 _dt_
__ + __ __ 2 __ + __ __ + _V _ +



__ 1 _dt_
__ + __
__ 2



__ 1 _dt_
__ 2 __ + __ __ + _V _ __



__ 1 _dt_
__ 2 __ + __ __ + _V _ +



__ 1 _dt_
__ 2


(4.6.18)


where we used Equation (4.6.17) and ignored normalization constants. Again, we only keep
terms up to the first order of _dt_ 1 ,



__ 1 _dt_
_d_ = __ 2 ( __ + __ __ __ + __ + __ __ ) + _V_ ( __ __ __ + __ + )

+ __ 1 __ __ __ + _dt,_ (4.6.19)

where in the last term, we substitute _V_ from Equation (4.6.16) and keep terms up to _dt_ and
use the It o rule ( _d_ _W_ ) 2 = _dt_ . By rearranging terms we have,



1
_d_ = __ 1 _dt_ __ __ __ + __ 2 ( __ + __ __ __ + __ + __ __ ) + _V_ ( __ __ __ + __ + ) _._ (4.6.20)
 

Since we have ignored the normalization constants, now we need to normalize the result.
One can show that the normalized SME has the form



1
_d_ = __ 1 _dt_ __ __ __ + __ 2 ( __ + __ __ __ + __ + __ __ )


(4.6.21)


+ ( _V_ __ __ 1 Tr[( __ __ + __ + ) __ ] _dt_ ) ( __ __ __ + __ + __ Tr[( __ __ + __ + ) __ ] __ ) _._


![Intro to quantum measurement.pdf-99-0.png](Intro to quantum measurement.pdf-99-0.png)

_L_ __ _L_ Equation (4.6.21) can be represented in terms of the dissipation superoperator 2 1 _L_ __ _L, _ and jump superopertator [ _L_ ] __ = _L_ + _L_ __ Tr[( _L_ + _L_ __ ) __ ] __ in a more _D_ [ _L_ ] __ =
__ _{_ _}_ _H_ __

compact form,


_d_ = __ 1 _dt_ _D_ [ __ __ ] __ + ( _V_ __ __ 1 _xdt_ ) _H_ [ __ __ ] __ (4.6.22a)


__ 1 _dt_ _D_ [ __ __ ] __ + __ __ 1 _d_ _WH_ [ __ __ ] __ (4.6.22b)



_d_
__  =
__ _dt_



_d_

_dt_ = __ 1 _D_ [ __ __ ] __ + __ __ 1 _d_ _H_ [ __ __ ] __ (4.6.22c)


1 Remember _V_ has a term of order


_t_ according to Equation (4.6.16).

93


-----


_4.6 Generalized measurement in the_ __ _x_ _basis_

where we substitute _W_ and _d_ as defined in Equation (4.6.16).
Equation (4.6.22c) describes the evolution of the qubit under radiative decay with rate
__ 1
and continuous perfect monitoring of that radiation with homodyne detection. By comparing to the general form of the SME (Equation 4.3.19), we understand that the homodyne
measurement of the qubit radiation is corresponding to the measurement operator __ and
__
the measurement strength _k_ = __ 1 is the rate in which the detector receives the emission.
In order to account for imperfect detection we can again use the technique of multiple
detectors. Assume that actual detector receives proportion __ of the total emission at rate
__ 1 , thus the measurement strength of this detector is __ 1 . The rest of the emission is then
measured by a fictitious detector (the environment) with measurement strength (1 __ ) __ 1 .
__
Both measurement detectors impose their own backaction on the qubit evolution,

_d_ = __ 1 _D_ [ __ __ ] __ + __ __ 1 _d_ _H_ [ __ __ ] __ + __ __ 1 _d_ ( _f_ ) _H_ [ __ __ ] _,_ (4.6.23)

where _d_ and _d_ ( _f_ ) represents the collected homdyne signal by actual detector and the
fictitious detector respectively. By averaging over all the fictitious detector outcomes we
arrive at the SME for inefficient detection of the qubit emission,

_d_ = __ 1 _D_ [ __ __ ] __ + __ __ 1 _d_ _H_ [ __ __ ] _,_ (4.6.24)

where that the corresponding inefficient homodyne signal can be described by,

_V_ = __ __ 1 _x_ _dt_ + __ 1 _d_ = __ 1 _x_ _dt_ + __ 1 _ddt._ (4.6.25)
__ __ __ _W_ __ __ __ __

Similar to the discussion we had for the SME (4.3.19), one can also add unitary evolution
to the SME (4.6.24) to account for a coherent drive on the qubit and obtain a full version
of the SME,

_d_ = __ _i_ [ _H_ _R_ _, _ ] + __ 1 _D_ [ __ __ ] __ + __ __ 1 _d_ _H_ [ __ __ ] _._ (4.6.26)

To sum up the discussion in this section, we may recast this stochastic master equation
terms of Bloch vector components,


_z_  = + _x_ + __ 1 (1 _z_ ) + __ __ 1 _x_ (1 _z_ ) _d, ,_ (4.6.27a)
__ __


_x_  =  _z_ __

2

__ __



1 _x_ + __ (1 _z_ _x_ 2 ) _d, ,_ (4.6.27b)

2

__ __ __


where we assume _H_ _R_ =  2 __ _y_ .


where we assume _H_ _R_ =  2


94


-----


_4.7 z-measurement procedure_

####### 4.7 ####### z-measurement procedure

In this section, we are going to utilize the basic techniques mentioned in Chapter 3 to
discuss how to actually perform weak measurement and analyze the data to obtain quantum
trajectories. A typical _z_ -measurement includes:

__ Qubit calibration and characterization as discussed in Chapter 3.

__ Paramp calibration, dumb-signal cancellation, readout calibration, as discussed in
Chapter 3.

__ Calibration for _, ,_  _n, k_ .

__ Calibration for preparation and tomography pulses, Rabi tomography.

__ Data acquisition for quantum state tomography and the actual experiment.

__ Post-processing, verifying the measurement trajectory update method by quantum
state tomography.

In the following subsections, we discuss each of these steps in greater detail.

########## 4.7.1 ########## Basic characterization

As discussed in Chapter 3 we first need to characterize the qubit-cavity system. The information we need to obtain in this step is the cavity frequency __ _q_ , cavity linewidth __ , qubit
frequency __ _q_ , qubit relaxation time _T_ 1 , and qubit dephasing time _T_ 2 __ .
In this stage we also find an initial calibration for __ and _/_ 2 pulses (usually _T_ __ = 20 ns
, _T_ _/_ 2 = 10 ns for certain amplitude in arbitrary waveform generator (AWG). More careful
calibration should be performed after paramp calibration and dumb-signal cancellation. See
Chapter 3 for more details on basic experiment characterization.

########## 4.7.2 ########## Paramp calibration

As discussed in Chapter 3, we set up the paramp (preferably in double-pump operation mode)
at the cavity frequency (more precisely at __ _c_ __ so we have an optimum and symmetric
__
response for the states _|_ _g_ __ and _|_ _e_ __ ).
**_Dumb-signal cancellation_** Beside the basic paramp setup and obtaining a proper
gain profile, here we need also consider some practical techniques to optimize the low-power
readout fidelity. The point is that in weak measurement the paramp should be adjusted to
have best performance for weak signal detection 1 . However, during the readout we use a much

1 Moreover the paramp normally works efficiently in the weak signal limit.

95


-----


_4.7 z-measurement procedure_

stronger signal to project the qubit (basically the readout is a very strong measurement).
Having calibrated the paramp for weak measurement, it may not have the best performance
for readout where we send a large number of photons during the readout.
The trick to go around this issue is called dumb-signal cancellation. The idea is following: although we need a high number of photons during the readout inside the cavity, after
passing the cavity we can coherently cancel the unnecessary part of the signal and only net
phase shifts are amplified by the paramp as demonstrated in Figure 4.10. The dumb-signal

![Intro to quantum measurement.pdf-102-4.png](Intro to quantum measurement.pdf-102-4.png)

![Intro to quantum measurement.pdf-102-3.png](Intro to quantum measurement.pdf-102-3.png)

![Intro to quantum measurement.pdf-102-6.png](Intro to quantum measurement.pdf-102-6.png)

![Intro to quantum measurement.pdf-102-2.png](Intro to quantum measurement.pdf-102-2.png)

![Intro to quantum measurement.pdf-102-5.png](Intro to quantum measurement.pdf-102-5.png)

![Intro to quantum measurement.pdf-102-1.png](Intro to quantum measurement.pdf-102-1.png)

![Intro to quantum measurement.pdf-102-0.png](Intro to quantum measurement.pdf-102-0.png)

Figure 4.10: **Dumb-signal cancellation:** A copy of the readout pulse with proper amplitude and
phase cancels the readout signal in _I_ quadrature while maintaining the information along the _Q_ quadrature
(separation Amp __ __ is preserved) since the paramp works efficiently in the weak signal regime.

cancellation is basically a copy of the readout pulse with the right amount of attenuation 1

and proper phase to cancel the readout signal before reaching to the paramp while maintaining the qubit information. The room temperature circuitry for dumb-signal cancellation
is depicted in Figure 4.11.

########## 4.7.3 ########## Quantum efficiency calibration

After the paramp is set up for optimal readout performance, we are ready to calibrate the
quantum efficiency __ . This includes calibration of the dispersive shift __ , the average photon

1 One way to estimate the proper amplitude for the dumb signal in the experiment is to send a continuous
readout pulse to the cavity (e.g. run a long readout sequence in continuous mode, or set the readout pulse
always high at mixer) and look at the output signal power with spectrum analyzer. Now disconnect the
readout input but this time send the dumb signal cancellation through the pump port and adjust to amplitude
to have the same output power signal as we had for continuous readout. By this calibration the amplitude is
roughly calibrated and you can find the optimal phase by looking at average homodyne signals in IQ plane
and comparing the output signal before readout and during the readout.

96


-----


_4.7 z-measurement procedure_

number  _n_ , the measurement strength _k_ , and finally measurement of the quantum efficiency.
In order to obtain values for __ and  _n_ , we use a Ramsey measurement 1 . As discussed
in Chapter 2 (Eq. 2.3.21), the qubit frequency is shifted by the average number of photons
in the cavity,  __ _q_ = 2 __ _n_  . Moreover as discussed earlier in this chapter (Equation 4.3.22),
photons in the cavity also induce dephasing of the qubit coherence by a rate  = 8 __ 2 _n/_  .
We can observe these two effects by performing a Ramsey measurement over a range of
average photon number occupation in the cavity. Fortunately, the ratio  _/_  __ _q_ = 4 _/_ is
independent of  _n_ , which means we just need to sweep the average number of photons in the
cavity (without knowing the actual  _n_ values) and calculate the ratio to obtain __ (the value
for the cavity linewidth __ is independently known from the basic characterization).
For that, we start by running the Ramsey experiment (typically a 5 __ s Ramsey sequence).
We set the frequency to be slightly off-resonant 2 as illustrated in Figure 4.11. The qubit
signal generator (BNC2) is set to be 0 _._ 4 MHz above the qubit resonance frequency. By
changing the DC offset values at the I/Q inputs of the cavity mixer, we let photons to leak
into the cavity and shift the qubit frequency and also dephase the qubit, which is measured
by the Ramsey measurement. The result of this sweep labeled as the Ch3 offset (the applied

|Col1|Col2|4 3 2 1|
|---|---|---|


![Intro to quantum measurement.pdf-103-0.png](Intro to quantum measurement.pdf-103-0.png)

![Intro to quantum measurement.pdf-103-1.png](Intro to quantum measurement.pdf-103-1.png)

Figure 4.11: **Quantum efficiency calibration setup** .

DC offset voltage to the input Q for the cavity mixer) has been shown in Figure 4.12a. The

1 Note that we might have a crude estimation of __ from the punch-out experiment, but that is not
accurate enough for the quantum efficiency calibration.
2 It is more convenient to avoid being on-resonance with qubit so there are always oscillations which
makes an easier fitting procedure. Therefore we prefer to be slightly above the actual qubit frequency (0.4
MHz for 5 __ s Ramsey sequence) and by increasing the  _n_ , qubit will be pushed down (remember __ is typically
negative) and we never Stark shift the qubit into an on-resonance situation. Typically, we set the qubit drive
frequency so that we have __ one oscillation in the limit  _n_ __ 0. This usually ensures we will sample enough
to resolve Ramsey oscillations at higher  _n_ in the cavity.

97


-----


_4.7 z-measurement procedure_

minimum oscillation, which is _f_ _min_ = 0 _._ 4 MHz, happens somewhere around 55 mV for the
Ch3 offset. As the Ch3 offset deviates from a minimum leakage value, the mixer lets photons
populate the cavity and the oscillation frequency increases by 2 __ _n_  . Moreover, the oscillations
decay faster as the average number of photons increases in the cavity as expected by the
relation  = 8 __ 2 _n/_  . Figure 4.12b shows Ramsey oscillations from data both near and far
from minimum leakage. By fitting a decaying sinusoid to the data we obtain the oscillation
frequency _f_ and the Ramsey decay time 1 _/_  as a function of the Ch3 offset value as depicted
in Figure 4.12c. In order to obtain __ we plot  versus _f_ and fit a line to the data as depicted
in Figure 4.12d. The slope would be 4 _/_ (the value of the cavity linewidth __ is known from
the low-power cavity transmission measurement). We need one more piece of information


########## A+ B cos(2 ##########  ########## f t+ ##########  ########## )e ########## - ##########  ########## t


20

50

80


f=1.06
 =0.65

1.0

0.0

-1.0

![Intro to quantum measurement.pdf-104-1.png](Intro to quantum measurement.pdf-104-1.png)

0


f=0.45
 =0.15

2 4
Time (  s)


![Intro to quantum measurement.pdf-104-4.png](Intro to quantum measurement.pdf-104-4.png)

![Intro to quantum measurement.pdf-104-0.png](Intro to quantum measurement.pdf-104-0.png)

Time (  s)

Fit f to: K 0 +K 1 X+ K 2 X 2

K 0 =3.4654
K 1 =-114.03
K 2 =-1059.5


12


1.5

1.0

0.5

0.0


0.5


![Intro to quantum measurement.pdf-104-2.png](Intro to quantum measurement.pdf-104-2.png)

0.02 0.04 0.06 0.08

AWG Ch3 offset (V)


![Intro to quantum measurement.pdf-104-3.png](Intro to quantum measurement.pdf-104-3.png)

0.5 1.0 1.5

f (MHz)


0.5 1.0 1.5


Figure 4.12: **The** __ **calibration result: a** , The Ramsey experiment result for different offset values of
Ch3. **b** , Two cuts from the sweep data in **a** indicated by dashed lines. **c** , The frequency and the damping
rate for the Ramsey data of panel (a) versus the DC offset of Ch3. By fitting the red curve to a parabola we
get coefficients _K_ 0 , and _K_ 1 , and _K_ 2 , which will be used to find the optimal quadrature for the measurement
**d** , The damping rate versus the frequency is ideally a line with a slope of 4 _/_ .

98


-----


_4.7 z-measurement procedure_

from these data. We fit the curve _f_ (frequency versus Ch3 offset) to a polynomial (parabola
is enough) and record the fit parameters as depicted in Figure 4.12. Later, this data will be
used to find the optimal quadrature for the measurement 1 .
We repeat the experiment and apply the same analysis for the DC offset of Ch4 while
keeping the offset of Ch3 fixed at the minimum leakage value 2 .
Now, we use the parabolic fit to parametrize the mixer output power in terms of the
Ramsey oscillation frequency _f_ . Here we briefly discuss what this means. Ideally, the mixer
output power can be represented by,

_f_ _k_ = _K_ 2 (Ch3) (Ch3 Ch3 min ) 2 + _K_ 2 (Ch4) (Ch4 Ch4 min ) 2 (4.7.1)
__ __

(Ch3) (Ch3)
Where we use the fact that Ch3 and Ch4 are orthogonal and Ch3 min = _K_ 1 _/_ 2 _K_ 2 .
__
The phase of the output signal also can be represented as,



(Ch4)

_K_ 2

(Ch3)

 _K_ 2




( _Ch_ 4 Ch4 min )
__
( _Ch_ 3 Ch3 min )
__


__ = atan


(4.7.2)


as depicted in Figure 4.13, the parameter __ sets the angle of the output signal in the _IQ_
plane (phasor) and _f_ _k_ parametrizes the length of the phasor which has to do with the number
of photons  fact, _k_ = 4 __ _n_ but we usually keep it in terms of frequency 2 2 __ ( _f_ _f_ min ) _/_ where _k_ is the measurement strength _f_ _k_ = 2 3 . One can show that for __ ( _f_ __ _f_ min ) = 2 __ _n_  . In
__ __

######### Q

 I

|f k |Col2|
|---|---|
|||
|||



Figure 4.13: **Mixer output:** The output of the mixer is a coherent signal whose phase and amplitude
depend on Ch3/Ch4 amplitude and offset. The parameter _f_ _k_ quantifies the strength of measurement and __
is the measurement quadrature.

1 The relative phase of the cavity photons and the paramp pump is important for optimizing amplification
and hence quantum efficiency.
2 To be more accurate, after finishing the Ch4 offset sweep one can redo the Ch3 offset sweep with Ch4
offset fixed at the corresponding minimum leakage value.
3 Note that, we explicitly express _f_ in MHz (Figure 4.12b). One needs to be careful about this factor of
2 __

99


-----


_4.7 z-measurement procedure_

a given mixer output power _f_ _k_ and angle __ the value for Ch3 and Ch4 should be,


_f_ _k_ __

cos(

(Ch3)
_K_



(Ch3)

__ __ ) _K_ 1

180 __ (Ch3)


_f_


Ch3( _f_ _k_ _, _ ) =

Ch4( _f_ _k_ _, _ ) =


_,_ (4.7.3a)

(Ch3)
2 _K_


_f_ _k_ __

sin(

(Ch4)
_K_



(Ch4)

__ __ ) _K_ 1

180 __ 2 _K_ (Ch4)


_f_


1 _.,_ (4.7.3b)

(Ch4)
2 _K_


where we represent __ in degrees for convenience. Now we use Equation (4.7.3) to once again
sweep the Ramsey measurement, but this time we sweep the angle __ and while keeping the
frequency _f_ _k_ fixed at a certain value 1 . Figure 4.14 shows Ramsey oscillation measurements
for different values of __ value at _f_ _k_ = 0 _._ 5. Ideally the Ramsey oscillation frequency should

######## a b

0

12


1.5

1.0

0.5

0.0


180

360


![Intro to quantum measurement.pdf-106-0.png](Intro to quantum measurement.pdf-106-0.png)

100 200 300
 (degree)


![Intro to quantum measurement.pdf-106-2.png](Intro to quantum measurement.pdf-106-2.png)

![Intro to quantum measurement.pdf-106-1.png](Intro to quantum measurement.pdf-106-1.png)

Time (  s)

Figure 4.14: **Ramsey measurements for a sweep of different angles.**

be fixed, but in practice the mixer may have some imperfections and the Equation (4.7.3)
does not perfectly predict the mixer output. But this is not be a problem for calibration for
a reason that will be clear shortly 2 .
Now we arrive at the last step of the quantum efficiency calibration. In this step we want
to find the optimal angle which gives the best signal-to-noise ratio for measurement of the
qubit state. For that, we compare the weak measurement signal for a certain time ns after preparing the qubit in the ground or excited state 3 . We repeat this measurement _T_ __ 100
for different angles and compare the separation of the two readout histograms to find which
angles gives the optimal SNR as depicted in Figure (4.15). Once we find the SNR for different

1 It is convenient to set _f_ _k_ at or close to the value that you will be performing the actual experiment.
Usually _f_ _k_ = 0 _._ 1 is a very weak measurement and _f_ _k_ = 1 is a relatively strong weak measurement.
2 Eventually, for quantum efficiency calibration, we compare the result of two __ sweeps so imperfections
do not contribute to the final result.
3 Note there is no readout pulse needed in this step.

100


-----


_4.7 z-measurement procedure_

0.4

0.3

0.2

0.1


 V **c**


###########  ########### - ########### pulse


300

200

100


![Intro to quantum measurement.pdf-107-0.png](Intro to quantum measurement.pdf-107-0.png)

0.0


![Intro to quantum measurement.pdf-107-1.png](Intro to quantum measurement.pdf-107-1.png)

![Intro to quantum measurement.pdf-107-2.png](Intro to quantum measurement.pdf-107-2.png)

-40 -20 0 20 40

averaged weak signal


100 200 300

 (degree)


Figure 4.15: **Calibration of** __ **:** Comparison of the measurement histograms for _|_ _g_ __ and _|_ _e_ __ for different
__ .

angles __ , we have all the pieces we need to calculate the quantum efficiency,


_S_
__ =


_S_ _S_

=
64 __ 2 _nT_  64 __ ( _f_



_._ (4.7.4)
64 __ ( _f_ _f_ min ) _T_
__


As depicted in Figure 4.15d, the quantum efficiency is maximum at a certain angle which is
ideally aligned with the paramp amplification quadrature.

########## 4.7.4 ########## Tomography pulse calibration

Before we collect data, it is good to fine-tune the preparation/tomographic pulses. A short
Rabi (100ns) sequence with all three types of tomographic readout for _x, y, z_ (as discussed in
Chapter 3) is a simple test to verify the preparation and tomographic pulses 1 . Figure 4.16a
shows a Rabi tomography result corresponding to a perfect calibration for preparation and
tomography pulses. The fact that the oscillations for both _x_ and _y_ start from the zero
and that Figures 4.16b,c,d,e show some common imperfect calibrations. _y_ remains always zero means that, for most part, the pulses are calibrated 2

########## 4.7.5 ########## Data acquisition

After recalibrating the preparation and tomographic pulses. We are ready to run experimental sequences (including noise calibration and state tomography sequences).
The noise calibration measurement (depicted in Figure 4.15a,b) needs to be collected as

1 We may have already calibrated _, /_ 2-pulses in a basic qubit characterization step but note that we
are now pumping the paramp and may need to revisit the qubit calibration. Moreover, we might need a more
complicated preparation for the actual experiment. So it makes sense to specifically check the preparation
pulses before starting the actual experiment.
2 One can use a longer Rabi sequence with lower amplitude, _T_ 1 , or Ramsey sequence to further tune the
calibration.

101


-----


_4.7 z-measurement procedure_


-1


-1


![Intro to quantum measurement.pdf-108-0.png](Intro to quantum measurement.pdf-108-0.png)

20 40 60 80 100
Time (ns)




![Intro to quantum measurement.pdf-108-1.png](Intro to quantum measurement.pdf-108-1.png)

Figure 4.16: **Rabi tomography diagnosis: a** , A perfect calibration. **b** The _/_ 2 pulses needed to
be weaker, either shorter pulses or lower amplitude. **c** The _/_ 2 pulse for _x_ ( _y_ ) needed lower (higher)
amp/duration. **d** , Mixer orthogonality is slightly higher that 90 degrees. **d** , Mixer orthogonality is slightly
lower that 90 degrees.

a reference to scale the collected digitized weak signal 1 .
For example, the sequence for continuous monitoring of a driven qubit has been depicted
in Figure 4.17a which includes pulses for heralding, preparation, weak measurement, and
readout. The obtained data is depicted as a color plot in Figure 4.17b. Note that we
perform the experiment for different times _t_ (in this case we vary the measurement time
from 0 to 2 __ s) 2 .

########## 4.7.6 ########## Post-processing: Quantum trajectory update

In this step we use the SME (Equations 4.3.20) or Bayesian update (Equations 4.4.10) to
reconstruct quantum trajectories. First, we need to properly scale the digitized measurement signal to obtain _V_ ( _t_ ). For that we use the noise calibration data and subtract the
overall offset 3 . Then we scale the signal so that the separation between measurement signal
histograms of the ground and excited state preparations are equal to two. Moreover, the
sign for the scaling factor is chosen so that the histogram corresponding to the ground state
preparation is centered at _V_ = +1 as depicted in Figure 4.18b which is consistent with our
convention (for example see Equation 4.2.14). One can check at this point to make sure that
the variance of the signal is consistent with the calibrated quantum efficiency.

1 The noise calibration sequence doesnt have drive or readout, only ground and excited state preparations
and weak measurement for a certain time 2 One may think that only repeating the longest trajectory is enough because then you can update __ 1 __ s.
trajectories as long as you wish. However, in order to verify the validity of trajectory update, you will need
to have trajectories which have different lengths, which provides you with readout measurement at different
times. Later we will discuss how to use the trajectory measurements of different times to tomographically
validate the trajectory update method.
3 Note that the overall offset is determined by averaging both signals regardless of the preparation.

102


-----


_4.7 z-measurement procedure_

100

|Col1|Col2|Col3|
|---|---|---|
||b Herald Readout Prep. Pulse x-Pulse t Herald Readout Prep. Pulse y-Pulse Herald Readou Prep. Pulse No-Pulse||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||


![Intro to quantum measurement.pdf-109-0.png](Intro to quantum measurement.pdf-109-0.png)

![Intro to quantum measurement.pdf-109-1.png](Intro to quantum measurement.pdf-109-1.png)

Figure 4.17: **Driven** _z_ **-measurement sequence** .

**SME update**

For quantum trajectories, we use the scaled signal in the SME. In order to account for a
coherent drive _H_ _R_ = __  _R_ __ _y_ _/_ 2, we use the full version of the SME (Equation 4.3.23). We
represent this in terms of Bloch components as,


_z_ [ _i_ + 1] = _z_ [ _i_ ] +  _R_ _x_ [ _i_ ] _dt_ + 4 _k_ (1 _z_ [ _i_ ] 2 )( _V_ [ _i_ ] _z_ [ _i_ ]) _dt_ (4.7.5a)
__ __


_x_ [ _i_ + 1] = _x_ [ _i_ ]  _R_ _z_ [ _i_ + 1] _dt_ (2 _k_ + __ 2 ) _x_ [ _i_ ] _dt_ 4 _kx_ [ _i_ ] _z_ [ _i_ ]( _V_ [ _i_ ] _z_ [ _i_ ]) _dt_
__ __ __ __


(4.7.5b)


where we also discretized 1 the equations to be consistent with the digitized measurement
signal with timestep _dt_ __ 20 ns. Equation (4.7.5) may not be numerically stable or accurate
when the timestep _dt_ in the experiment is not small enough. There is an alternative way to
update the SME which involves two steps. In this method the unitary evolution separately
implemented by a geometric rotation,

_z_ d = _z_ [ _i_ ] cos( _R_ _dt_ ) + _x_ [ _i_ ] sin( _R_ _dt_ ) (4.7.6a)


_x_ d = _x_ [ _i_ ] cos( _R_ _dt_ ) _z_ [ _i_ ] sin( _R_ _dt_ ) (4.7.6b)
__


_z_ [ _i_ + 1] = _z_ d + 4 _k_ (1 _z_ d 2 )( _V_ [ _i_ ] _z_ d ) _dt_ (4.7.6c)
__ __


_x_ [ _i_ + 1] = _x_ d (2 _k_ + __ 2 ) _x_ d _dt_ 4 _kx_ d _z_ d ( _V_ [ _i_ ] _z_ d ) _dt,_ (4.7.6d)
__ __ __


1 Note that, _x_ [ _i_ + 1] uses _z_ [ _i_ + 1] for the rotation terms. Why?

103


Qubit


-----


_4.7 z-measurement procedure_


![Intro to quantum measurement.pdf-110-0.png](Intro to quantum measurement.pdf-110-0.png)

![Intro to quantum measurement.pdf-110-1.png](Intro to quantum measurement.pdf-110-1.png)

Figure 4.18: **Digitized weak measurement signal scaling** .

where _z_ _d_ and _x_ _d_ are dummy variables connecting the two steps. The two-step update has
better performance when _dt_ is not small enough to ensure the stability in single-step update.
In most of practical situations _dt_  _R_ 1 and the two methods are almost the same (see
__
Figure 4.19).


0

-10

![Intro to quantum measurement.pdf-110-2.png](Intro to quantum measurement.pdf-110-2.png)

0.0 0.5 1.0 1.5 2.0


1.0

0.5

0.0

-0.5

-1.0

![Intro to quantum measurement.pdf-110-3.png](Intro to quantum measurement.pdf-110-3.png)

0.0 0.5 1.0 1.5 2.0


Time(  s) Time(  s)

Figure 4.19: **Quantum trajectory updated by SME: a.** A typical homodyne measurement signal _V_ ( _t_ )
corresponding to _z_ -measurement of a driven qubit,  _R_ _/_ 2 __ = 0 _._ 6 _, k_ = 1 _, _ = 0 _._ 35 _, dt_ = 20 ns. **b.** The
corresponding updated quantum trajectory using Equations (4.7.5) for solid lines and Equations (4.7.6) for
dashed line. As you can see, for these drive parameters both methods are practically the same.

104


V avg =138.1


-----


_4.7 z-measurement procedure_

**Tomographic validation**

In order to verify that the updated trajectories accurately predict the state evolution of the
qubit, we show the qubit state predicted by the trajectory is consistent with measurement
from quantum state tomography. The idea is to compare the expectation values for _x_ , _y_ ,
and _z_ predicted by the quantum trajectory to the expectation value obtained by the result
of projective measurements (readouts). Of course the readout is a destructive measurement
with binary outcome. Therefore in order to obtain the expectation values one need to repeat
the readout measurement on the same state many times. But it is not possible to perform
many readouts on a single trajectory hence it is impossible to obtain expectation value for
a single trajectory from a projective measurement.
However, instead of using single trajectory, we can use many different trajectories as long
as all that trajectories have the same prediction for __ _x_ __ _,_ __ _y_ __ _,_ __ _z_ __ at a given verification time
_t_ v . Therefore the tomographic verification at any given time _t_ v involves post-selection of
trajectories that agree at that time.
A nice way to do this is by choosing a random trajectory as a reference, and for each
time step we post-select trajectories that have same prediction as the reference trajectory.
Therefore we can reconstruct the reference trajectory by using the readout outcome of postselected trajectories. Figure 4.20a shows a reference _z_ -trajectory in (black line) and a few
post-selected trajectories that have the same prediction for __ _z_ __ at _t_ v = 0 _._ 8 __ s within some
tolerance indicated by a red window. Note these post-selected trajectories are from the
experiment time _t_ = _t_ v so their readout outcomes at _t_ = _t_ v are available. The average of the
readout outcomes from post-selected trajectories reconstruct the reference trajectory at that
time step which is indicated by a green circular marker in the zoomed-inset. The agreement
between the green circle and the reference trajectory indicates that quantum trajectories
truly predict the state of the qubit at that time step. By repeating this process for both _z_ ,


1.0

0.5

0.0

-0.5

-1.0

|t = v|0.8 s|
|---|---|


0.0 0.5 1.0 1.5 2.0
Time(  s)


1.0

0.5

0.0

-0.5


-1.0

![Intro to quantum measurement.pdf-111-0.png](Intro to quantum measurement.pdf-111-0.png)

0.0 0.5 1.0 1.5 2.0
Time(  s)


Figure 4.20: **Tomographic reconstruction** .

and _x_ for all time steps, one can reconstruct the reference trajectory and validate the state

105


-----


_4.8_ __ _x_ _measurement procedure_

update as depicted in Figure 4.20b. The shaded area indicates the binomial error from the
readout outcomes of post-selected trajectories at each time step. The binomial error can be
calculated as,


_p_ _q_
Bionamial Error = __

_N_




_N_ + _N_ __ _._ (4.7.7)

( _N_ + + _N_ ) 3
__


_N_ + _N_ __


Where _p_ = _N_ + _/N_ and _q_ = _N_ __ _/N_ are the probabilities for two possible outcomes ( _p_ = 1 __ _q_ )
and _N_ = _N_ + + _N_ is the total number of outcomes. In this case, the total number of
__
outcomes is equal to the total number of post-selected trajectories for each verification time.

####### 4.8 #######  ####### x ####### measurement procedure

In this section we discuss the experimental procedure for _x_ -measurement. This section follows
the theoretical discussion of Section 4.6. For most part, the procedure for _x_ -measurement is
similar to _z_ -measurement which is discussed in Section 4.7. Here we discuss only two steps
that are slightly different: the quantum efficiency calibration and the quantum trajectory
update.

########## 4.8.1 ########## Quantum efficiency calibration

The paramp setup is slightly different from the _z_ -measurement. Here, the paramp pump
is similar to the qubit frequency. Practically, the qubit pulses and paramp pump have
to be from the same generator. In an _x_ -measurement the paramp is only used for state
tracking but not readout. Therefore there is no dumb-signal cancellation and no readout
fidelity optimization. High power readout is used and often the fidelity can be improved by
transferring population to the higher excited states prior to the readout pulse.
The quantum efficiency calibration is relatively easier for _x_ -measurement than _z_ -measurement.
For this, we only need to run the noise calibration sequence with __ _x_ state preparations and
plot the histogram of the weak signal after a certain time of integration and scale the variance
to be __ 1 _dt_ . Then the separation would be  _V_ = 2 __ __ 1 .

########## 4.8.2 ########## State update and quantum trajectory

As discussed in Subsection 4.6.2, the SME for _x_ -measurement in terms of Bloch components
is described by Equation (4.6.27). In order to calculate quantum trajectories, the digitized
homodyne signal needs to be properly scaled. For that we first subtract the offset (the offset
can be determined by taking the average of the signal from the noise calibration sequence
regardless of preparation). Then we scale the signal so that the variance of the histograms

106


-----


_4.8_ __ _x_ _measurement procedure_

is __ 1 _dt_ . The signal is then ready to be used in the discretized SME,


_z_ [ _i_ + 1] = _z_ [ _i_ ] +  _R_ _x_ [ _i_ ] + __ 1 (1 _z_ [ _i_ ]) + __ __ 1 _x_ (1 _z_ [ _i_ ])( _V_ [ _i_ ] __ __ 1 _x_ [ _i_ ] _dt_ ) _,_ (4.8.1a)
__ __ __


_x_ [ _i_ + 1] = _x_ [ _i_ ]  _R_ _z_ [ _i_ + 1] __ 2 1
__ __


2 1 _x_ [ _i_ ] + __ (1 _z_ [ _i_ ] _x_ [ _i_ ] 2 )( _V_ [ _i_ ] __ 1 _x_ [ _i_ ] _dt_ ) _._ (4.8.1b)

__ __ __ __


107


-----


# Chapter 5

 Monitoring Spontaneous Emission of a Quantum Emitter

In this chapter, I discuss the experimental study of a continuously monitored quantum
system. We focus on the dynamics of a decaying emitter under homodyne detection of
its radiation. The aim of this chapter is to connect the this experiment with discussions
provided in the previous chapters.
Unlike classical mechanics, measurement has an inevitable disturbance on quantum systems. This disturbance which is known as measurement backaction and depends on the
type of detector that we use for measurement. Therefore, it is natural to ask how the same
quantum system, with the same interaction Hamiltonian to the environment, behaves differently under different detection schemes on the environment. Although this doesnt make
much sense in a classical framework, it is understandable in the quantum case, owing to the
entanglement between the detector and the emitter as we have already seen in the simple
model in Chapter 4 (Section 4.2).
A prime example is the detection of spontaneous emission of an excited emitter. How
does the emitter decay under continuous monitoring? Does the decay dynamics depend on
the type of the detector? In other words, does an atom decay regardless of the detection or
it does decay because of the detection? Exploring these questions underpin the topic of our
study in this chapter.

####### 5.1 ####### Spontaneous emission

Spontaneously emission is ubiquitous in nature and accounts for most of the light that we
see around us [83]. It is often an undesirable effect but also essential for diverse applications
ranging from fluorescence imaging to quantum encryption using single photons.
In the spontaneous emission process, an excited emitter (excited atom) releases its energy

108


-----


_5.2 Photon Detection_

in form of photons into one of the available electromagnetic modes of the environment 1 . From
the quantum measurement point of view, spontaneous emission is due to the light-matter
interaction and entanglement of the state of the emitter to its electromagnetic environment [84, 85]. In this picture, measurements on the environment (e.g. photon detection,
homodyne detection) collapse the entangled wavefunction in a specific basis and convey information about the state of the emitter and consequently cause backaction [86]. Therefore,
the choice of measurement may change the quantum evolution of the emitter [8790].
A goal in this chapter is to study the dynamics of spontaneous emission under continuous homodyne measurement. But before discussing homodyne measurement, it would be
illuminating to discuss photon detection. This will be helpful to draw a connection between
these two types of detection.

####### 5.2 ####### Photon Detection

Consider a qubit (as a quantum emitter) interacting with an electromagnetic mode of the
environment. Assume we use a photon detector to monitor the existence of photon in that
mode of the environment 2 as depicted in Figure 5.1a.


![Intro to quantum measurement.pdf-115-0.png](Intro to quantum measurement.pdf-115-0.png)

P e


P e




![Intro to quantum measurement.pdf-115-1.png](Intro to quantum measurement.pdf-115-1.png)

![Intro to quantum measurement.pdf-115-2.png](Intro to quantum measurement.pdf-115-2.png)

Figure 5.1: **Photon detection: a** , The qubit is initially prepared in the excited state and interacts with
an electromagnetic mode. The qubit state and its emission to the mode are entangled via the interaction
Hamiltonian (5.2.1). **b** , The detection of a photon results is a sudden jump for the emitter state. **c** , The
average of many jump detections results in an exponential decay for the state of the qubit.

The emitter which is initially prepared in the excited state interacts with the electromag-

1 Therefore the spontaneous emission rate can be altered by manipulating the electromagnetic modes
that are available to the emitter via engineering the environment [12,14].
2 In general, one can assume that the emitter is interacting with many modes. Then for our discussion,
we should also assume that the detector is sensitive to all of the modes.

109


-----


_5.2 Photon Detection_

netic mode of the environment via the interaction Hamiltonian,

_H_ int = __ ( _a_ __ __ + _a_ + ) _,_ (5.2.1)
__

where _a_ and _a_ __ correspond to the creation and annihilation of a photon in that mode. The
parameter __ quantifies the interaction strength which, in this case, is related to the decay
rate of the emitter to the environment 1 .
The interaction Hamiltonian entangles the state of the emitter and the electromagnetic
mode which can be represented as 2 (also depicted in Figure 5.1a),


 tot (0) = _e_ 0  tot ( _t_ ) = __ _e_ 0 + __ _g_ 1 _._ (5.2.2)
_|_ _|_ __ _|_ _|_ __ _|_ _|_ __

(5.2.3)

The photon detector monitors the state of the environment by performing measurements
in the photon number basis. If we detect a click we learn that the wave-function of the
environment has been collapsed to the state _|_ 1 __ . This means the state of the qubit must be
in ground state (measurement backaction). If we do not detect a click, then the emitter is
still in the excited state. Therefore the detection of the spontaneous emission in the form of
photons (energy quanta), results in an instantaneous jump of the emitter from the excited
state to the ground state as depicted in Figure 5.1b [91,92]. If we average over many jump
detections (or equivalently, if we disregard the detection results) the state of the qubit would
exponentially decay from the excited to the ground state (Fig. 5.1c).
Before we conclude this subsection, it is worth mentioning a key point. You may notice
that in the quantum measurement interpretation of the spontaneous emission, the atom decays because a detector collapses the wave function. In other words the atom decays because
the detector clicks. This is so counterintuitive with our classical understanding of detection
where we would say that the detector clicks because the atom has decayed 3 . We will return
to this point again in the discussion on homodyne measurement.

![Intro to quantum measurement.pdf-116-0.png](Intro to quantum measurement.pdf-116-0.png)

1 As discussed earlier, __ is proportional to the available density of state for the emitter to decay.
2 Note that this is similar to our discussion in Chapter 4 and Equation (4.6.3), except here the emitter
initially is in the excited state __ 0 = 0 _, _ 0 = 1. This means that if we do not detect a photon, the emitter is
still in the excited state with certainty, which is not the case when the emitter is prepared in a superposition
state as we discussed in Equation (4.6.3).
3 The argument the atom decays because the detector clicks is true when there is an entanglement
between the emitter and the photon.

110


-----



_5.3 Homodyne detection of spontaneous emission_

Homodyne **b**

Q

|Col1| I|
|---|---|


![Intro to quantum measurement.pdf-117-3.png](Intro to quantum measurement.pdf-117-3.png)

![Intro to quantum measurement.pdf-117-4.png](Intro to quantum measurement.pdf-117-4.png)

![Intro to quantum measurement.pdf-117-2.png](Intro to quantum measurement.pdf-117-2.png)

![Intro to quantum measurement.pdf-117-1.png](Intro to quantum measurement.pdf-117-1.png)

Qubit emission


![Intro to quantum measurement.pdf-117-0.png](Intro to quantum measurement.pdf-117-0.png)

LO


Measurment
quadrature


Figure 5.2: **Homodyne detection: a** , The spontaneous emission of the emitter is detected by homodyne
measurement. The local oscillator has a well defined relative phase __ with respect to the qubit rotating frame
which determines the amplification quadrature shown in **b** . The measurement happens only in one quadrature
along __ -axis. The fluctuations in the orthogonal quadrature are de-amplified, which means we do not learn
about fluctuations in that quadrature. This allows for noiseless amplification for the __ -quadrature [93]

####### 5.3 ####### Homodyne detection of spontaneous emission

In the previous section, we discussed a situation where spontaneous emission is measured by
a photon detector. Now the question is, What if the emission is measured with a detector
that is not sensitive to quanta, but rather to the amplitude of the field? In other words,
what if we use a detector that addresses the wave notion of light as opposed to a photon
detector which addresses the particle notion of light. What would the backaction be in this
case? How are measurement outcomes correlated with the state of the emitter? In this
section, we experimentally explore these questions by performing homodyne measurement
of the spontaneous emission of a qubit.
As we discussed in Chapter 4 (Subsection 4.6.1), Homodyne measurement can be thought
of as projections to the coherent basis __ corresponds to the amplitude of the field in the quadrature _|_ __ __ , where __ = _|_ __ _|_ _e_ _i_ _a_ [89]. The measurement outcome __ _e_ _i_ + _ae_ __ _i_ which also contains
fluctuations in that quadrature.
In practice, when we perform homodyne measurement along a certain quadrature, we
basically squeeze the outgoing emission along that quadrature as depicted in Figure 5.2b.
This means we amplify the signal along the __ -axis and de-amplify along the orthogonal
axis. Therefore the measurement (or the collapse) happens only along the quadrature 1 __ .
Returning to our discussion of the atom decays because the detector clicks, this means that
the emitter only decays 2 along the __ -quadrature 3 .
Therefore the idea for the experiment is 1) to study the spontaneous emission dynamics

1 Because we do not obtain any information along the other quadrature.
The word decay is in quotes because, unlike the photon detection, homodyne detection does not necessarily fully collapse the emitter state. 2
3 The fact that collapse happens in a certain quadrature, results in a certain type of backaction on the
qubit which may confine the qubit evolution in a certain subspace.

111


-----


_5.3 Homodyne detection of spontaneous emission_


of a qubit by performing a homodyne measurement along the __ quadrature and 2) to explore
the dynamics for different homodyne quadrature measurements.
Note that the interaction Hamiltonian (Eq. 5.2.1) connects the quadrature _a_ __ _e_ _i_ + _ae_ __ _i_

to the corresponding dipole moment of the qubit (emitter), __ __ _e_ _i_ + __ + _e_ __ _i_ . For example if
we set the phase __ = 0, we showed in Chapter 4 that the homodyne measurement is actually
a noisy estimate of __ _x_ which can be described by (see Equation 4.6.16),
__ __

_dV_ _t_ = __ __ __ __ _x_ __ _dt_ + __ _dW_ _t_ _._ (5.3.1)

We are interested to know what a detection of the homodyne signal _dV_ _t_ tells us about the
state of the decaying qubit. For that, we use the experimental setup to perform the sequence
depicted in Figure 5.3. For the experimental setup, note that the qubit pulse and paramp
pump share a same generator 1 (BNC2) and the paramp is operated in a double-pump mode.
Moreover, regarding the homodyne measurement of the emitters emission, the demodulation
should be happen at the qubit frequency but high-power readout demodulation should be at
the bare cavity frequency. Therefore we use an RF switch to toggle between two frequencies
for demodulation purposes.
For the experimental sequence, we prepare the qubit in an initial state (in this case we
prepared the qubit in the excited state, + _x_ , and + _y_ ) then start collecting the homodyne
signal for a variable time _t_ ( _t_ =40 ns, 80 ns,...). Finally, we perform a projective measurement
to determine the final state of the qubit at that time.
We characterize the correlation between the average of the collected homodyne signal
and the final state (at time _t_ ). For that, we average the projective result conditioned at the
average homodyne signal _V_  . Therefore we obtain the conditional expectation values, __ _x_  _V_ ,
__ _|_
__ _y_  _V_ , __ _z_  _V_ . In Figure 5.4a-c we plot __ _z_  _V_ and __ _x_  _V_ parametrically on the _X_  _Z_ plane
__ _|_ __ _|_ __ _|_ __ _|_
of the Bloch sphere for different integration times.
Looking at the experimental result in Figure 5.4, a few points are noticeable;

__ When the qubit is prepared in the excited state, we see that the _x_ -component of the
state develops a correlation with the averaged homodyne signal.

__ The emitter state evolves in a deterministic curve inside the Bloch sphere. Therefore
one can use these smiley curves for heralding the system in a nearly arbitrary point
in the Bloch sphere.

__ When the emitter is prepared as the + _x_ state, the qubit state sometimes gets more
excited during the decay [88]. This stochastic excitation happens only in the amplitude measurements of the field and such excitations are not possible in the case of
photodetection [89].

1 This is a practical way to ensure that the paramp pump and the qubit pulse have a well defined and
stable relative phase.

112


-----


_5.3 Homodyne detection of spontaneous emission_

Switch Input #1 300K

Pulse BNC1 I 10mK

![Intro to quantum measurement.pdf-119-0.png](Intro to quantum measurement.pdf-119-0.png)

![Intro to quantum measurement.pdf-119-1.png](Intro to quantum measurement.pdf-119-1.png)

Figure 5.3: **The experimental setup and sequence:** The emitter is initialized in the excited state or in
a superposition state by a preparation pulse. Right after the preparation, the homodyne signal is collected.
Finally, we apply a tomographic rotation pulses along different axes followed by a high-power readout pulse
to projectively measure the final state of the emitter.


1.0

0.5

0.0

-0.5

-1.0


80 ns

|a|960 ns 640 ns 320 ns 160 ns 8 40 ns|
|---|---|


![Intro to quantum measurement.pdf-119-2.png](Intro to quantum measurement.pdf-119-2.png)

![Intro to quantum measurement.pdf-119-3.png](Intro to quantum measurement.pdf-119-3.png)

![Intro to quantum measurement.pdf-119-4.png](Intro to quantum measurement.pdf-119-4.png)

-1.0 -0.5 0.0 0.5 1.0 -1.0 -0.5 0.0 0.5 1.0 -1.0 -0.5 0.0 0.5 1.0

X X X

Figure 5.4: **Conditional dynamics of spontaneous decay:** The tomographic result is the averaged
tomographic readout conditioned on the outcome of the homodyne measurement to determine _x_ __ _x_  _V_ ,
__ _|_
and _z_ __ _z_  _V_ . These correlated tomography results are displayed on the _X_ - _Z_ plane of the Bloch sphere
__ _|_
for three different initial states: __ _z_ ( **a** ), + _x_ ( **b** ), and + _y_ ( **c** ). The gray scale indicates the relative occurrence
of each measurement value. Note that different backaction between ( **b** ), and + _y_ ( **c** ) is the result of the
phase-sensitive amplification on different quadratures of the homodyne signal.


-1.0 -0.5 0.0 0.5 1.0 -1.0 -0.5 0.0 0.5 1.0 -1.0 -0.5 0.0 0.5 1.0


113


-----


_5.3 Homodyne detection of spontaneous emission_

__ If we rotate the amplification phase by 90 degrees 1 , As depicted in Figure 5.4c, the
state evolution for qubit is totally different. This is because the backaction happens in
a different quadrature. This demonstrates how the choice of homodyne measurement
phase can be used to control the evolution of the emitter.

We can take advantage of the deterministic smiley evolution of the qubit to characterize
the backaction for the qubit at different points in the Bloch sphere. For that, we let the
system evolve from the excited state to a nearly arbitrary place inside the Bloch sphere on
a smiley curve ( _x_ _i_ _, z_ _i_ ). This acts as heralding of the qubit state to a specific point in the
Bloch sphere, ( _x_ _i_ _, z_ _i_ ). Then we collect the homodyne signal for an additional 40 ns. We
use results from tomography to calculate the final position of the qubit ( _x_ _f_ _, z_ _f_ ). Therefore,
for each point on the smiley curve, we obtain the conditioned evolution of the qubit based
on the sign of the additional collected homodyne signal. This method tells us about the
measurement backaction for positive and negative homodyne signals at each point on the
Bloch sphere. The results are summarized in Figure 5.5. The backaction at a specific
location in state space, associated with the detection of a given value of _dV_ , is demonstrated
by the vector connecting ( _x_ _i_ _, z_ _i_ ) and ( _x_ _f_ _, z_ _f_ ). The backaction vector maps demonstrate how
positive (negative) measurement results push the state toward + _x_ ( __ _x_ ). Furthermore, the
maps suggest that measurement backaction is stronger near the state __ _z_ suggesting that the
measurement strength is proportional to the emitters excitation.
Finally, we can look at the individual quantum trajectories of this process. As we discussed in Chapter 4, all we need is to properly scale the homodyne signal and use that in
the SME (4.6.27),



__
_dx_ =
__ 2



__ _xdt_ + __ (1 _z_ _x_ 2 )( _dV_ _t_ __ __ _xdt_ ) _,_ (5.3.2)

2 __ __ __ __


_dz_ = __ (1 _z_ ) _dt_ + __ _x_ (1 _z_ )( _dV_ _t_ __ __ _xdt_ ) _,_ (5.3.3)
__ __ __



__
_dy_ =
__ 2



__

_ydt_ _xy_ ( _dV_ _t_ __ __ _xdt_ ) _._ (5.3.4)
2 __ __


Figure 5.6 shows the result for state update from the exited state and the + _x_ state for 2 __ s
of continuous measurement. As we see, the evolution of the qubit during the decay process is
no longer jumpy as opposed to the case of photon detection. However, the average of many
trajectories would recover the same exponentially damped behavior as we discussed in the
previous section 2 . Moreover, in Figure 5.6b stochastic excitations of individual trajectories
toward the excited state is clearly apparent. One can quantify the stochastic excitation by
extracting the probability of excitation above a certain threshold at different times. Looking
at the measurement term (proportional to __ __ ) in Equation (5.3.3) it is clear that the state

1 or equivalently prepare the system in + _y_ .
2 Regardless of the type of the detector, we will recover the Lindbladian evolution for the system if we
average over many detection outcomes (this is equivalent to disregarding all measurement outcomes).

114


-----


_5.3 Homodyne detection of spontaneous emission_


R /2 x , R 0 z


/2 x , R 0 z


1600
1200
800
400


Readout


R

![Intro to quantum measurement.pdf-121-1.png](Intro to quantum measurement.pdf-121-1.png)

1.0

0.5

0.0

-0.5


![Intro to quantum measurement.pdf-121-0.png](Intro to quantum measurement.pdf-121-0.png)

-1.0

![Intro to quantum measurement.pdf-121-2.png](Intro to quantum measurement.pdf-121-2.png)

-1.0 -0.5 0.0 0.5 1.0


-1.0 -0.5 0 0.5 1.0

dV

![Intro to quantum measurement.pdf-121-3.png](Intro to quantum measurement.pdf-121-3.png)

-1.0 -0.5 0.0 0.5 1.0


Figure 5.5: **Backaction vector maps [33]. a** , We use the deterministic relation between the average
homodyne signal _V_  and the emitters state to herald a nearly arbitrary initial state in the _X_ - _Z_ plane of
the Bloch sphere. The conditional backaction is obtained by quantum state tomography based on a small
portion of the signal _dV_ . **b** , Histogram of the signals _dV_ which we separate into positive or negative _dV_ . The
corresponding backaction imparted on the emitter for negative ( **c** ) or positive ( **d** ) values of _dV_ are depicted
by arrows at different locations in the _X_ - _Z_ plane of the Bloch sphere.


at + _x_ will be stochastically excited if the Weiner increment _dW_ _t_ , obtained from the detected
signal _dV_ _t_ , is less than _/dt_ , predicting that 35% of the trajectories should be excited
__ __

in the first time step [33].



Having access to the stochastic trajectories of a quantum system opens new doors to investigate the dynamics of open quantum systems. In particular, the stochastic and non-unitary
dynamics of quantum systems combined with a unitary evolution exhibits a rich dynamics
which can be utilized for studying fundamental question in quantum physics [32,35,89,94].

115


-----


_5.3 Homodyne detection of spontaneous emission_


1.0

0.5

0.0

-0.5

-1.0

**b**

1.0

0.5

0.0

-0.5


1.0

0.5

0.0

-0.5

-1.0

**d**

1.0

0.5

0.0

-0.5


![Intro to quantum measurement.pdf-122-0.png](Intro to quantum measurement.pdf-122-0.png)

![Intro to quantum measurement.pdf-122-1.png](Intro to quantum measurement.pdf-122-1.png)

-1.0


-1.0

![Intro to quantum measurement.pdf-122-3.png](Intro to quantum measurement.pdf-122-3.png)

-1.0 0.0 1.0


![Intro to quantum measurement.pdf-122-2.png](Intro to quantum measurement.pdf-122-2.png)

0.0 0.5 1.0 1.5 2.0


Time (  s)


Figure 5.6: **Quantum trajectories for decaying atom: a,b** , Quantum trajectories of spontaneous
decay calculated by the stochastic master equation, initiated from __ _z_ ( **a** ) and + _x_ ( **b** ). Several trajectories
are depicted in gray, and a few individual trajectories are highlighted in black. **c,d** Individual trajectories
( _x,_  _z_ ) that originate from __ _z_ ( **c** ) and + _x_ ( **d** ) are shown as dashed lines and the tomographic reconstruction
(see Chapter 4) based on projective measurements are shown as solid lines.

116


-----


# Chapter 6

 Quantum Thermodynamics: Quantum Maxwells Demon

In this chapter we explore quantum thermodynamics at the extreme level of a single atom
interacting with a bath. The atom is a two level quantum system in contact with a detector
which acts as the atoms environment. In this chapter we attempt to put our understanding
about quantum dynamics into the language of quantum thermodynamics. In particular,
we study the information-energy connection in quantum thermodynamics in the context of
Maxwells demon.

####### 6.1 ####### Fluctuation theorems: thermodynamics at the microscope scale

Thermodynamics is normally considered as a theory which describes systems in the limit
of a large number of particles, _N_ __ . In this limit, often known as the thermodynamic
limit, fluctuations of energy are absolutely negligible compared to the total energy in the
system. Therefore, it makes sense to describe the state of the system by a few macroscopic
parameters regardless of fluctuations in individual degrees of freedom. For example, we
define an equilibrium state and characterize the total energy in terms of heat and work
by only a few thermodynamic parameters (e.g volume, pressure, temperature) for a gas
inside a piston regardless of the position and the velocity of individual gas molecules. As
depicted in Figure 6.1a, the work fluctuations in a thermodynamic process are negligible in
thermodynamic limit so that the work distribution is effectively a delta function.
However, for microscopic systems which have a finite number of degrees of freedom, the
fluctuations are no longer negligible. In this limit, fluctuations basically drive the systems in
a stochastic manner during the process 1 as depicted in Figure 6.1b. Therefore, the traditional

1 Similar to the quantum trajectories which are stochastic due to quantum fluctuations.

117


-----


_6.1 Fluctuation theorems: thermodynamics at the microscope scale_

thermodynamics laws need to be revisited for microscopic systems where thermal fluctuations
are significant.

|P, V,T|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||



![Intro to quantum measurement.pdf-124-0.png](Intro to quantum measurement.pdf-124-0.png)

Figure 6.1: **Work fluctuations in the macroscopic and microscopic limit: a** . The work distribution
for a system (gas inside a cylinder) in the thermodynamic limit (number of particles _N_ ). The

1 __
fluctuations are absolutely negligible _N_ __ 2 0 in this limit. **b** . The corresponding system in the limit of
__ __ 1


a finite number of particles ( _N_ __ 1). The work distribution fluctuates substantially __ _N_ __ 2 __ _N_ due to

thermal fluctuations.



1
fluctuations are absolutely negligible _N_ __ 2 0 in this limit. **b** . The corresponding system in the limit of
__ __ 1

a finite number of particles ( _N_ __ 1). The work distribution fluctuates substantially __ _N_ __ 2 __ _N_ due to


In the past decades, thermodynamics has been successfully extended to nonequilibrium
microscopic systems to account for thermal fluctuations. In particular, the generalized second
law of the thermodynamics, in terms of a fluctuation theorem, has been experimentally
verified for classical systems [95]. For example, it has been shown that work fluctuations in
a nonequilibrium process follow a fairly strong rule known as the Jarsynski equality (JE),

__ _e_ __ _W_ __ = _e_ __ __  _F_ _,_ (6.1.1)

which connects the work distribution _W_ from a nonequilibrium process to the equilibrium
free energy difference  _F_ [96]. One can recover the second law of thermodynamics from JE
by using Jensens inequality,

__ _e_ __ _W_ __ = _e_ __ __  _F_ __ __ __ _e_ _x_ __ __ __ _e_ __ __ __ _x_ __ _W_ __  _F._ (6.1.2)

Therefore, the JE is considered as the 2nd law of thermodynamics for microscopic systems. This equality has been verified experimentally for classical systems (see for example
Ref. [97]). However, the extension of thermodynamics to include quantum fluctuations faces
unique challenges because quantum fluctuations and coherence do not have a clear role in
thermodynamics. The newfound experimental capability to track single quantum trajectories adds to an intense endeavor to study and define thermodynamic quantities for individual
quantum systems.

118


-----


_6.2 Maxwells demon and the 2nd law_

####### 6.2 ####### Maxwells demon and the 2nd law

Consider the schematic in Figure 6.1b in the limit of a few particles in the cylinder. If we
are able to track the particles and react fast enough, we can basically displace the piston
without doing any work! In this case, the work distribution is ideally a delta function at zero,
but we have displacement in the piston  _F_ __ = 0. Thus the JE is no longer valid. In fact,
Maxwell came up with a similar idea which was in apparent violation of the 2nd law soon
after the establishment of thermodynamics. Maxwell considered a box full of air molecules
and an intelligent being who has access to the velocity and position of individual molecules.
The demon can sort the hot and cold particle to either side of the box without doing any
work as depicted in Figure 6.2. The question of, How the demon can make a oven next to

![Intro to quantum measurement.pdf-125-0.png](Intro to quantum measurement.pdf-125-0.png)

![Intro to quantum measurement.pdf-125-1.png](Intro to quantum measurement.pdf-125-1.png)

![Intro to quantum measurement.pdf-125-2.png](Intro to quantum measurement.pdf-125-2.png)

Figure 6.2: **Maxwells demon:** By knowing the position and the velocity of the particles, a demon sorts
hot and cold particle in a box in apparent violation of the 2nd law.

a fridge without doing any work and violate the 2nd law?, reveals a profound connection
between the energy and information in thermodynamics 1 .
Owing to the dominant contribution of fluctuations in the dynamics of microscopic systems, a lot of effort has been directed toward the understanding of the connection between
energy and information in microscopic systems. In particular, the Jarzynski equality (2nd
law) has been generalized to account for the demons information,

__ _e_ __ _W_ __ _I_ __ = _e_ __ __  _F_ _,_ (6.2.1)

where _I_ is the mutual information between the demons measurement outcome and the state
of the system.
The generalized Jarzynski equality (GJE) has been studied and verified for classical
microscopic systems in which the demon is realized by measuring the thermal fluctuations
and by applying subsequent feedback on the system [41,98100].
The recent advances in fabrication and control over quantum systems allow for unprecedented study of the concept of Maxwells demon in quantum systems where instead of thermal
fluctuations, the quantum fluctuations are dominant. For example, in the minimal quan-

1 This question of how the demon actually violates the 2nd law was unsolved for decades.

119


-----


_6.3 Continuous monitoring: a quantum Maxwells demon_

tum situation of a two level quantum system, the generalized Jarzynski equality is verified
in the experiment by considering the mutual information between projective measurement
outcomes and the state of the qubit [101104]. Although these experiments use quantum
systems, their result can be interpreted as a classical mixture either because the dynamics doesnt include quantum coherence or because the projective measurement destroys the
quantum coherence. However, in an actual quantum situation, the demon can also gain
information about the quantum coherences; the off-diagonal elements in the density matrix 1

(Fig. 6.3).


######### P
1

######### P
0


######### P ######### c
 c* P
 0 P


######### P ######### 0
0

######### 0 ######### P


0

######### = c*


![Intro to quantum measurement.pdf-126-0.png](Intro to quantum measurement.pdf-126-0.png)

![Intro to quantum measurement.pdf-126-1.png](Intro to quantum measurement.pdf-126-1.png)

![Intro to quantum measurement.pdf-126-2.png](Intro to quantum measurement.pdf-126-2.png)

![Intro to quantum measurement.pdf-126-3.png](Intro to quantum measurement.pdf-126-3.png)

![Intro to quantum measurement.pdf-126-4.png](Intro to quantum measurement.pdf-126-4.png)

![Intro to quantum measurement.pdf-126-5.png](Intro to quantum measurement.pdf-126-5.png)

![Intro to quantum measurement.pdf-126-6.png](Intro to quantum measurement.pdf-126-6.png)

![Intro to quantum measurement.pdf-126-7.png](Intro to quantum measurement.pdf-126-7.png)

Figure 6.3: **Classical demon vs. quantum demon: a** , A classical demons knowledge about a quantum
system is limited to the populations in the definite states. **b** , A quantum demon also has knowledge about
the quantum coherence in the system.

In previous chapters, we studied continuous monitoring and weak measurement of a
quantum systems. Through weak measurement we can learn about the quantum state and
quantum coherences without destroying them (completely). Therefore in this chapter, we attempt to utilize continuous monitoring to study Maxwells demon in the context of quantum
measurement.

####### 6.3 ####### Continuous monitoring: a quantum Maxwells demon

The idea is to use our ability of tracking and manipulating the quantum state to realize a
truly quantum Maxwells demon. For that, consider the _z_ -measurement setup (discussed in
Chapter 4) and the experimental sequence demonstrated in Figure 6.4. The experimental
protocol consists of five steps:

__ In Step 1, the qubit is prepared in a thermal state characterized by an inverse temperate 2 __ . Practically this can be done by a proper rotation pulse followed by a projective

1 One can think of it in this way that; the classical demon is able to identify the particles as either hot
or cold. But the quantum demon in general can also identify particles that are in superposition of hot and
cold.
2 Here we represent __ in the qubit energy scale so that, initially for the qubit populations we have
_P_ 1 _/P_ 0 = _e_ __ __ .

120


-----


_6.3 Continuous monitoring: a quantum Maxwells demon_

![Intro to quantum measurement.pdf-127-0.png](Intro to quantum measurement.pdf-127-0.png)

![Intro to quantum measurement.pdf-127-1.png](Intro to quantum measurement.pdf-127-1.png)

![Intro to quantum measurement.pdf-127-2.png](Intro to quantum measurement.pdf-127-2.png)

![Intro to quantum measurement.pdf-127-3.png](Intro to quantum measurement.pdf-127-3.png)

![Intro to quantum measurement.pdf-127-4.png](Intro to quantum measurement.pdf-127-4.png)

Figure 6.4: **Experimental sequence** .

measurement and by then disregarding the measurement outcome.

__ In Step 2, a projective measurement is performed so that the qubit is projected to
one of its eigenstates. The binary measurement outcome _X_ _{_ 0 _,_ 1 _}_ is recorded. This
result, along with the projective result in Step 5, will be used to calculate the transition
probabilities and characterize the work distribution for the experiment.

__ In Step 3, the demon, without knowing about the projective measurement result _X_ ,
starts monitoring the qubit state while an external drive also acts on the system.
Note the effective Hamiltonian for a resonantly driven qubit in the rotating frame is
_H_ _t_ = __  _R_ __ _y_ _/_ 2 where  _R_ quantifies the drive strength as discussed in Chapter 2.

__ In Step 4, at a certain time, the demon uses his knowledge about the state of the system to rotate the system back to the ground state and extract work 1 .

__ In Step 5, the experiment is finished by a second projective measurement which results
in a binary measurement outcome _Z_ _{_ 0 _,_ 1 _}_ .

We repeat this experimental protocol and gather measurement statistics to experimentally study the 2nd law of thermodynamics. For example, Figure 6.5 shows the scatter plot
of final states of the qubit before and after the rotation feedback in Step 4 for 200 experiment
runs.

########## 6.3.1 ########## Examining the Jarzynski equality

Now, we examine the Jarsynski equality 6.1.2 in the following form,

_e_ __ _W_ = _P_ ( _W_ ) _e_ __ _W_ _dW_ (6.3.1)
__ __ 

1 In the actual experiment, in order to avoid feedback delay, we perform a random rotation pulse and the
correct pulses are post-selected in the data analysis.

121


-----


_6.3 Continuous monitoring: a quantum Maxwells demon_

_Z_

_X_

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||


![Intro to quantum measurement.pdf-128-0.png](Intro to quantum measurement.pdf-128-0.png)

Figure 6.5: **The act of the demon in Step 4:** The red (blue) dots are the state of the qubit before
(after) rotation feedback. The circular markers shows the average of the states before and after feedback.
All data are from weak measurement and quantum trajectory reconstructions except the black cross which
comes from the projective measurement after feedback. The agreement between the cross and green circular
markers indicates that the trajectory update and feedback rotations are faithfully executed.

where we set  _F_ = 0 since the initial and final Hamiltonian are practically the same in our
experiment. In order to obtain the work distribution _P_ ( _W_
) we only use the projective measurement result and calculate the transition probabilities _P_ _m,n_ as demonstrated in Figure 6.6.
The work distribution then can be calculated in this form 1 ,


_P_ _m,n_ __ _P_ 0 _n_ __ ( _U_ ( _E_ _m_ __ _E_ _n_ 0 )) _,_ (6.3.2)

__ __
_m,n_


_P_ ( _W_ ) =


where the _P_ _n_ 0 denote the initial occupation probabilities, _P_ __ _m,n_ are the transition probabilities
between initial and final eigenvalues _E_ _n_ 0 and _E_ _m_ __ of the Hamiltonian _H_ _t_ , and __ is the duration
of the protocol.
Therefore, we examine the Jarzynski equality by using transition probabilities as follows,

_P_ ( _W_ ) _e_ __ _W_ _dW_ = _P_ 0 (0) _P_ 00 ( __ ) + _P_ 1 (0) _P_ 11 ( __ )


+ _P_ 0 (0) _P_ 10 ( __ ) _e_ + __ + _P_ 1 (0) _P_ 01 ( __ ) _e_ __ __

= 1 _._ (6.3.3)

Figure 6.7 (square markers) shows the experimental result for the left-hand side of the
Equation (6.3.3) for five different duration times. There is no surprise that the result deviates
from unity, because in Equation (6.3.3), we have ignored the act of the demon on the system.
In other words, the demon violates the second law unless we account for the information of
the demon.

Note, because quantum systems do not necessarily occupy states with well defined energy (only eigenstates of the Hamiltonian have a well defined energy), the work distribution is described in terms of transition 1
probabilities between energy eigenstates [105].

122


-----


_6.3 Continuous monitoring: a quantum Maxwells demon_

P 11 1

0

P 00


P


![Intro to quantum measurement.pdf-129-0.png](Intro to quantum measurement.pdf-129-0.png)

Figure 6.6: **Transition probabilities:** The projective measurement results are used to calculate the
transition probabilities. The initial probabilities _P_ 0 (0) and _P_ 1 (0) are simply calculated based on the relative
occurrence of outcome 0 or 1 in the first projective measurement. For the transition probabilities _P_ _nm_ ( __ ), we
calculate the relative occurrence of the result _n_ _{_ 0 _,_ 1 _}_ in the second projective measurement conditioned
that the result _m_ _{_ 0 _,_ 1 _}_ is obtained in the first projective measurement.

1.8


1.4

1.0


![Intro to quantum measurement.pdf-129-1.png](Intro to quantum measurement.pdf-129-1.png)

0.0 0.5 1.0 1.5 2.0

Time (  s)


0.0 0.5 1.0 1.5 2.0


Figure 6.7: **Violation of the 2nd law:** The experimental results violates the Jarzynski equality. This
violation is because we have ignored the demons information.

########## 6.3.2 ########## The demons information

In this section, we quantify the information that the demon obtains during the measurement.
But what is the information? One way to quantify the information is to measure how much
you learned that you didnt already know [106]. If we already know that the qubit state is
__ = 0 _._ 99 _|_ 0 __ 0 _|_ + 0 _._ 01 _|_ 1 __ 1 _|_ and someone measures the qubit and lets us know that the qubit
is in the ground state, we would not learn much. But it turns out that if the qubit is in
the excited state our state of knowledge about the qubit would be substantially changed.
Therefore the amount of information can be quantified by how unexpected the outcome is.
For that, consider _I_ _z_ ( __ ) = ln _P_ _z_ ( __ ) as the information content of __ along _z_ basis which
__ __
quantifies how much we learn if we obtain result _z_ = __ 1 _,_ 1 along the _z_ __ basis. Now we define
information exchange for the demon as the difference between initial and final information

123


-----


_6.3 Continuous monitoring: a quantum Maxwells demon_

content,

_I_ _z_ __ _,z_ ( _t_ ) = ln _P_ _z_ __ ( __ _t_ _|_ _r_ ) __ ln _P_ _z_ ( __ 0 ) _,_ (6.3.4)

where, _P_ _z_ __ represents the probability of getting the result _z_ __ = 1 _,_ 1 in the _z_ __ -basis where
the system is diagonal 1 [107]. We calculate the probabilities in the diagonal basis to account __
for the information encoded in the populations (diagonal elements in density matrix) as well
as coherences (off-diagonal elements) as depicted in Figure 6.8a. For example, the state of


########### 0.0

 -0.2

 -0.4

 -0.6



![Intro to quantum measurement.pdf-130-0.png](Intro to quantum measurement.pdf-130-0.png)

########### 0.0 ########### 0.5 ########### 1.0 ########### 1.5 ########### 2.0

![Intro to quantum measurement.pdf-130-1.png](Intro to quantum measurement.pdf-130-1.png)

Time (  s)

Figure 6.8: **Information dynamics for the quantum Maxwells demon: a** . The information is
quantified by considering the probabilities in the diagonal basis to account for information encoded in the
coherences. **b** . The information exchange dynamics along quantum trajectories; the dashed line shows a
typical trace from the ensemble of data (shaded background color). The black solid line is the average of the
information exchange.

the qubit is indicated by the blue arrow in Figure 6.8a has the same amount of quantum
information as the magenta arrow has provided that the probabilities are calculated in the
diagonal basis for each state.
The expectation value for the information exchange along a quantum trajectory would
be,


_I_ _r_ =



[ _P_ _z_ __ ( __ _t_ _|_ _r_ ) ln _P_ _z_ __ ( __ _t_ _|_ _r_ ) __ _P_ _z_ ( __ 0 ) ln _P_ _z_ ( __ 0 )] _,_ (6.3.5)
_z,z_ __ = __ 1


where the conditional probabilities come from a single quantum trajectory. The subscript _r_
__
indicated by __ _t_ is the conditional evolution found by averaging over many trajectories. We
obtain this average value for the information exchange as,


__ _I_ __ =


_I_ _r_ =


_P_ _z_ __ ( __ _t_ ) ln _P_ _z_ __ ( __ _t_ ) _P_ _z_ ( __ 0 ) ln _P_ _z_ ( __ 0 ) _._ (6.3.6)
__
_z,z_ __ = __ 1 _,r_


1 The initial state is always a thermal state so the diagonal basis initially is _z_ basis.


124


-----


_6.4 Information gain and loss_

########## 6.3.3 ########## Test of the generalized Jarzynski equality

Now we attempt to verify the generalized Jarzynski equality which includes the information
term. For that, we represent Equation (6.2.1) as 1 ,


_e_ __ _W_ __ _I_ + _F_ = _P_ 0 (0) _P_ 00 ( _t_ ) _e_ __ _I_ 00 + _P_ 1 (0) _P_ 11 ( _t_ ) _e_ __ _I_ 11
__ __ (6.3.7)

+ _P_ 0 (0) _P_ 10 ( _t_ ) _e_ __ __ __ _I_ 10 + _P_ 1 (0) _P_ 01 ( _t_ ) _e_ + __ __ _I_ 01 _,_

where _I_ _ij_ = ln _P_ _i_ ( __ _t_ ) __ ln _P_ _j_ ( __ 0 ) as we discussed in the previous Subsection. Figure 6.9 shows
the experimental result for Equation (6.3.7) which indicates that the generalized Jarzynski
is indeed verified.


1.4

1.0

![Intro to quantum measurement.pdf-131-0.png](Intro to quantum measurement.pdf-131-0.png)

0.0 0.5 1.0 1.5 2.0

Time (  s)


Figure 6.9: **Generalized Jarzynski equality for the quantum Maxwells demon:** The blue round
markers are the experimental result for the generalized Jarzynski equality for different time durations. The
agreement between the dashed line and markers indicates that the GJE is verified, as opposed to the JE
(red square markers).

####### 6.4 ####### Information gain and loss

Now, we study the information dynamics at the ensemble level. In Figure 6.8d (solid curve)
we showed the average information change from many trajectories. You may notice that the
average information is negative. This loss of information is due to decoherence which is a
uniquely quantum feature and only appears if coherences contribute to the dynamics, and
is thus not possible in a classical situation (e.g. See reference [104]).
One may categorize the information change in two parts and distinguish the contribution
of information gain through measurement and information loss due to imperfect detection

1 The sign for _W_ in GJE depends on our definition of the work; the work done by the system, or the
work done on the system _e_ __ _W_ __ _I_ + _F_ .

125


-----


_6.4 Information gain and loss_

[107]. In principle, imperfect detection arises because the state evolution of the detector is not
exactly known and we must average over possible configurations of the detector as illustrated
in Figure 6.10a. If we consider the detector uncertainty as an average over inaccessible degrees
of freedom, parameterized by a stochastic variable _a_ , the exchanged information (6.3.6) can
be written as a sum of information gain and information loss __ _I_ __ = _I_ gain __ _I_ loss where [107],


_I_ gain = _S_ ( __ 0 )
__


_p_ ( _a, r_ ) _S_ ( __ _t_ _r,a_ )  0 (6.4.1)
_|_


_p_ ( _a, r_ ) _S_ ( __ _t_ _r,a_ )  0 (6.4.2)
_|_
_a_



0.0 0.4 0.8 1.4 2.2

0.6

0.4

0.2

0.0


_I_ loss


_S_ ( __ _t_ _|_ _r_ ) __


![Intro to quantum measurement.pdf-132-0.png](Intro to quantum measurement.pdf-132-0.png)

![Intro to quantum measurement.pdf-132-1.png](Intro to quantum measurement.pdf-132-1.png)

-0.2

![Intro to quantum measurement.pdf-132-2.png](Intro to quantum measurement.pdf-132-2.png)

![Intro to quantum measurement.pdf-132-3.png](Intro to quantum measurement.pdf-132-3.png)

![Intro to quantum measurement.pdf-132-4.png](Intro to quantum measurement.pdf-132-4.png)

0.0 0.2 0.4 0.6 0.8 1.0

_z_ 0

Figure 6.10: **Information gain and loss for the quantum Maxwells demon: a** , The inefficient
detection can be modeled by averaging over unknown degrees of freedom for the detector. This basically
lowers the signal-to-noise ratio. **b** , By adjusting the initial preparation for the qubit, we change the effective
temperature for the system. The average of information exchange is negative for lower temperature (initially
purer states) but it is positive for higher temperatures (initially more mixed states). Considering that only
information encoded in coherences are susceptible to the loss, the more coherences involved in the dynamics,
the more information will be lost.

However, we do not have access to _a_ in this experiment. But still, we can explore the
regimes where quantum coherence has different contributions to the dynamics meaning that
the loss has different contributions to the total information change. To do this, we prepare
the system in different initial thermal states and calculate the average information exchange
for different initial temperatures. In Figure 6.10b we plot the final information exchange
(at 2 __ s) versus different initial thermal states ( characterized by _z_ _in_ = __ _z_ _|_ _t_ =0 ). The total
information change is positive for higher temperature (for more mixed initial states) but it

126


-----


_6.4 Information gain and loss_

is negative for lower temperature (more pure initial states). This transition of information
gain to information loss can be understood by considering the fact that loss comes from
decoherence of lower temperature (more pure) states. In our case, initially, more pure states
will acquire more coherence through the unitary drive which turns the initial populations
into coherences, these coherences are then lost due to inefficient detection, ultimately leading
to a loss of information.

127


-----