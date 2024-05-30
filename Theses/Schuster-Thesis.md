
Abstract

######### Circuit Quantum Electrodynamics

David Isaac Schuster

2007

This thesis describes the development of circuit quantum electrodynamics (QED), architecture

for studying quantum information and quantum optics. In circuit QED a superconducting qubit

acting as an artificial atom is electrostatically coupled to a 1D transmission line resonator. The

large effective dipole moment of the qubit and high energy density of the resonator allowed this

system to reach the strong coupling limit of cavity QED for the first time in a solid-state system.

Spectroscopic investigations explore effects of different regimes of cavity QED observing physics

such as the vacuum Rabi mode splitting, and the AC Stark effect. These cavity QED effects are

used to control and measure the qubit state, while protecting it from radiative decay. The qubit

can also be used to measure and control the cavity state, as shown by experiments detecting and

generating single photons. This thesis will describe the theoretical framework, implementation, and

measurements of the circuit QED system.


-----


####### Circuit Quantum Electrodynamics

A Dissertation

Presented to the Faculty of the Graduate School

of

Yale University

in Candidacy for the Degree of

Doctor of Philosophy

by

David Isaac Schuster

Dissertation Director: Professor Robert J. Schoelkopf

May 2007


-----


 c 2007 by David Schuster.

All rights reserved.


-----


## Acknowledgements

I would first like to thank my advisor Rob Schoelkopf. He gave me the freedom to explore an

amazing world of quantum physics, while his guidance prevented me from ever feeling lost in all of

its complexity. He taught me what it means to be a scientist, and the importance of eliminating

ground loops. I will always remember our late night brainstorming sessions, and his willingness to

suspend more critical demands to provide advice. Most of all I thank him for creating RSL and

giving me the opportunity to participate.

I have been fortunate to work with many amazing people in the course of this research. In

particular, most of the work presented in this thesis was the joint effort of Andreas Wallraff and

myself. His influence on me runs deep extending from small things like my (near fanatical) use of

mathematica and my much improved graphics design skills to the way I now approach experimental

questions. More importantly, Andreas has become one of my closest friends. More recent work,

presented in sections 4.3, 8.3.1, and 9.3, related to the Transmon was performed with my evil

twin, Andrew Houck. His scientific abilities are matched only by his unbounded enthusiasm, and

hopefully the former is as contagious as his excitement. I thank Alexandre Blais and Jay Gambetta

for teaching me everything I know about cavity QED and quantum measurement. Their patience

exceeds even Andrews optimism. I also owe a great debt to Luigi Frunzio for teaching me everything

I know about the dark arts of fabrication.

Steve Girvin has an uncanny ability to make tangible connections between theory and experiment,

while simultaneously telling a hilarious story. Similarly, I often found myself emerging from Michel

Devorets office with new understanding of a question much deeper than the one with which I had

entered. Dan Prober is to be thanked not only for his direct role in helping to convince me to come

to Yale, serving on my committee, and advising me throughout my time here, but also for helping

to build such an amazing community on the 4 th floor.

My lab mates have made graduate school the best of times, providing help, camaraderie, and close


-----


friendship. All of my friends from graduate, undergraduate, and high school have provided invaluable

support. I would especially like to thank my roommate(s) Matt and Sam for their tolerance and

friendship.

Most importantly I would like to thank my family, who have encouraged my curiosity and

provided me with unending love. Finally, I thank Carol who helped me to grow as a person as well

as a scientist.


-----


## Contents

1 Introduction 18

1.1 Quantum Computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

1.2 Cavity Quantum Electrodynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

1.3 Quantum Circuits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

1.4 Circuit Quantum Electrodynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

1.5 Thesis Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

2 Cavity Quantum Electrodynamics 34

2.1 Dispersive Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

2.2 Strong Dispersive Interactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

3 Cavity QED with Superconducting Circuits 45

3.1 Transmission Line Cavities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.1.1 The LCR Oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.1.2 Transmission Line as Series of LC Circuits . . . . . . . . . . . . . . . . . . . . 47

3.1.3 Capacitively Coupled LCR Resonator . . . . . . . . . . . . . . . . . . . . . . 49

3.1.4 Capacitively Coupled Transmission Line Resonator . . . . . . . . . . . . . . . 51

3.1.5 Coplanar Waveguide Cavities . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3.1.6 Kinetic Inductance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

3.1.7 Intrinsic Resonator Losses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

3.1.8 Quantization of the LC Oscillator . . . . . . . . . . . . . . . . . . . . . . . . 60

3.2 Cooper Pair Box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.2.1 Charge Basis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.2.2 Phase Basis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65


-----


CONTENTS 4

3.2.3 Split CPB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

3.3 Coupling CPB to Cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

3.3.1 Comparison with Traditional Cavity QED . . . . . . . . . . . . . . . . . . . . 71

3.4 Measurement Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

3.4.1 Quantum Non-Demolition Measurements . . . . . . . . . . . . . . . . . . . . 73

3.4.2 Mapping Qubit State onto Cavity State . . . . . . . . . . . . . . . . . . . . . 73

3.4.3 Distinguishing Cavity States . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

3.4.4 Small Phase Shift Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

3.4.5 Optimizing SNR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

4 Decoherence in the Cooper Pair Box 82

4.1 Relaxation and Heating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82

4.1.1 Voltage Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

4.1.2 Voltage Noise Inside a Cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

4.1.3 Material Loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

4.1.4 Dipole Radiation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

4.2 Dephasing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92

4.2.1 Charge Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

4.2.2 Flux Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

4.2.3 Critical Current/Josephson Energy 1 /f Noise . . . . . . . . . . . . . . . . . . 101

4.2.4 E C Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.2.5 Summary of Cooper pair box decoherence . . . . . . . . . . . . . . . . . . . . 102

4.3 Transmon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.3.1 Charge Dispersion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.3.2 Anharmonicity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

4.3.3 Transmon as a Josephson Oscillator . . . . . . . . . . . . . . . . . . . . . . . 108

4.3.4 Transmon for Circuit QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

4.3.5 Other Sources of Decoherence . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

4.3.6 Transmon Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

5 Design and Fabrication 119

5.1 Cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119


-----


CONTENTS 5

5.1.1 Design Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119

5.1.2 Optical Lithography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

5.1.3 Deposition and Liftoff . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

5.1.4 Substrates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

5.2 Cooper Pair Box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

5.2.1 Josephson Energy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

5.2.2 Charging Energy and Voltage Division . . . . . . . . . . . . . . . . . . . . . . 130

5.2.3 Electron Beam Lithography . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

5.2.4 Veil of Death . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

5.3 Transmon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137

5.4 Printed Circuit Boards and Sample Holders . . . . . . . . . . . . . . . . . . . . . . . 137

6 Measurement Setup 141

6.1 Cryogenics and Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

6.2 Pulse Synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

6.3 Demodulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

6.3.1 Digital Homodyne . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148

7 Characterization of CQED 154

7.1 Cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154

7.1.1 Temperature Dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

7.1.2 Magnetic Field Dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

7.2 Cooper pair box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

7.2.1 Charge Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

7.2.2 Measured CPB properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

7.3 Transmon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

8 Cavity QED Experiments with Circuits 169

8.1 Resonant Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171

8.1.1 Vacuum Rabi Mode Splitting with CPB . . . . . . . . . . . . . . . . . . . . . 171

8.1.2 Vacuum Rabi Mode Splitting With Transmon . . . . . . . . . . . . . . . . . . 173

8.2 Dispersive Weak Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177


-----


CONTENTS 6

8.2.1 AC Stark Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177

8.2.2 Off-Resonant AC Stark Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . 182

8.2.3 Sideband Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185

8.3 Dispersive Strong Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191

8.3.1 Photon Number Splitting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191

8.3.2 Anharmonic Strong Dispersive Limit . . . . . . . . . . . . . . . . . . . . . . . 197

9 Time Domain Measurements 200

9.1 Single Qubit Gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

9.2 Single Shot Readout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207

9.3 Single Photon Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211

10 Future work 220

10.1 Evolution of Circuit QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

10.1.1 New Cavity and Qubit Designs . . . . . . . . . . . . . . . . . . . . . . . . . . 220

10.1.2 Scaling Circuit QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221

10.1.3 Other quantum circuits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222

10.1.4 Hybrid Circuit QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

11 Conclusions 225

Appendices 226

A Operators and Commutation Relations 227

A.1 Harmonic Oscillators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

A.2 Spin 1/2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

A.3 Jaynes-Cummings Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

A.3.1 Interaction with Harmonic oscillator operators . . . . . . . . . . . . . . . . . 228

A.3.2 Interaction with Spin 1/2 Operators . . . . . . . . . . . . . . . . . . . . . . . 228

B Derivation of Dressed State Atom Picture 229

C Mathematica Notebooks 233

C.1 Cooper Pair Box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233


-----


CONTENTS 7

D Recipes 234


-----


## List of Figures

1.1 Relaxation and dephasing of qubits leads to decoherence . . . . . . . . . . . . . . . 21

1.2 Cavity QED setup with alkali atoms at optical frequencies . . . . . . . . . . . . . . . 24

1.3 Cavity QED setup with Rydberg atoms at microwave frequencies . . . . . . . . . . . 24

1.4 Cavity QED setup with quantum dots in semiconductors . . . . . . . . . . . . . . . . 25

1.5 Gallery of superconducting qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

1.6 Cooper pair box as tunable atom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

1.7 Cavity QED setup with superconducting circuits . . . . . . . . . . . . . . . . . . . . 30

1.8 Circuit QED sample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

2.1 Illustration of atomic cavity QED system . . . . . . . . . . . . . . . . . . . . . . . . 35

2.2 Energy level diagrams of Jaynes-Cummings Hamiltonian . . . . . . . . . . . . . . . . 36

2.3 Exact calculation of vacuum Rabi avoided crossing and indirect decay rates . . . . . 38

2.4 A phase diagram for cavity QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

2.5 Spectra of cavity and atom in strong dispersive limit . . . . . . . . . . . . . . . . . . 43

3.1 LCR oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.2 Transmission line as series of LC oscillator . . . . . . . . . . . . . . . . . . . . . . . . 48

3.3 Impedance of transmission line resonator . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.4 Capacitive coupling to an LCR resonator . . . . . . . . . . . . . . . . . . . . . . . . 51

3.5 Transmission of asymmetric cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3.6 Coplanar waveguide cavity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3.7 Dependence of characteristic impedance, Z 0 , on the CPW geometry. . . . . . . . . . 55

3.8 Dependence of kinetic inductance prefactor on geometry. . . . . . . . . . . . . . . . . 57

3.9 Dependence of kinetic inductance on penetration depth and center-pin width. . . . . 57


-----


LIST OF FIGURES 9

3.10 CPB circuit diagram / junction diagram . . . . . . . . . . . . . . . . . . . . . . . . . 62

3.11 CPB energy levels and charge staircase . . . . . . . . . . . . . . . . . . . . . . . . . . 63

3.12 Energy in two state approximation and fictitious field figure . . . . . . . . . . . . . . 64

3.13 CPB Matrix elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

3.14 Split CPB sketch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

3.15 Dipole moment of the Cooper Pair Box . . . . . . . . . . . . . . . . . . . . . . . . . 70

3.16 Measurement schematic and derivatives of CPB energy levels . . . . . . . . . . . . . 74

3.17 State dependent transmission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

3.18 Q function of coherent states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

3.19 State dependent transmission with small phase shift . . . . . . . . . . . . . . . . . . 77

3.20 Selecting  r for optimal SNR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

3.21 Selecting / 2  for optimal SNR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

4.1 Decoherence through gate voltage coupling circuit diagram and S V (  ) at different temperatures 84

4.2 Quality factor of qubits coupled to transmission line and cavity . . . . . . . . . . . . 86

4.3 CPB coupling to slotline mode in resonator . . . . . . . . . . . . . . . . . . . . . . . 87

4.4 Flux noise circuit diagram and flux transition matrix elements . . . . . . . . . . . . 88

4.5 Electric Field distribution in CPB . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

4.6 Derivatives of energy with respect to gate charge . . . . . . . . . . . . . . . . . . . . 96

4.7 Thermal Dephasing of the qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97

4.8 Dephasing of qubit due to 1 /f charge noise . . . . . . . . . . . . . . . . . . . . . . . 98

4.9 Dephasing times due to flux and critical current noise . . . . . . . . . . . . . . . . . 101

4.10 CPB energy bands at different E J /E C ratios . . . . . . . . . . . . . . . . . . . . . . 104

4.11 Anharmonicity vs. E J /E C ratios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

4.12 Anharmonic barrier and dimensionless dephasing rates . . . . . . . . . . . . . . . . . 107

4.13 Sketch and circuit diagram of the transmon . . . . . . . . . . . . . . . . . . . . . . . 108

4.14 Analogy of transmon as quantum rotor . . . . . . . . . . . . . . . . . . . . . . . . . . 110

4.15 Transmon matrix elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

4.16 Transmon dispersive couplings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

5.1 Resonator sample and gap capacitors . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

5.2 Optical lithography equipment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124


-----


LIST OF FIGURES 10

5.3 Resist Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124

5.4 Optical image of gap capacitor in resist . . . . . . . . . . . . . . . . . . . . . . . . . 125

5.5 Pictures of sputtered Nb resonators showing the apron and flagging . . . . . . . 127

5.6 Diagram of rotating angle evaporation process . . . . . . . . . . . . . . . . . . . . . . 128

5.7 Edge profiles of deposited Aluminum . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

5.8 CPB sample and equivalent circuit including parasitic capacitances . . . . . . . . . . 131

5.9 Dolan bridge process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

5.10 SEM images of tunnel junctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

5.11 Photograph of scanning electron microscope and electron beam evaporator . . . . . . 136

5.12 Transmon pictures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136

5.13 Sample mounts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138

5.14 Coffin style printed circuit board . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

5.15 Next generation PCB schematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

6.1 Measurement setup for cQED experiments . . . . . . . . . . . . . . . . . . . . . . . . 142

6.2 Annotated images of the cryostat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144

7.1 Transmission of a high Q resonator . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

7.2 Quality factor as a function of temperature . . . . . . . . . . . . . . . . . . . . . . . 156

7.3 a) Comparison of Q s between under and over coupled resonators and their harmonics 157

7.4 Resonance frequency shift with temperature due to kinetic inductance . . . . . . . . 158

7.5 Resonator quality factor dependence on magnetic field . . . . . . . . . . . . . . . . . 158

7.6 Resonance frequency shift due to magnetic field . . . . . . . . . . . . . . . . . . . . . 159

7.7 Footballs showing phase shift of cQED system as function of gate voltage and magnetic field.161

7.8 3D images of qubit spectroscopy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

7.9 Spectroscopic determination of qubit energy . . . . . . . . . . . . . . . . . . . . . . . 164

7.10 Saturation and power broadening of the qubit . . . . . . . . . . . . . . . . . . . . . . 165

7.11 Footballs showing parity effects and the presence of charge switchers . . . . . . 166

7.12 Spectroscopic characterization of the transmon . . . . . . . . . . . . . . . . . . . . . 168

8.1 A phase diagram for cavity QED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

8.2 Vacuum Rabi avoided crossing as function of bias charge . . . . . . . . . . . . . . . . 172


-----


LIST OF FIGURES 11

8.3 Transmission spectra of cQED system at and away from cavity-qubit degeneracy . . 172

8.4 Vacuum Rabi avoided crossing as function of bias flux . . . . . . . . . . . . . . . . . 174

8.5 Level separation and linewidth near flux avoided crossing . . . . . . . . . . . . . . . 176

8.6 Vacuum Rabi mode splitting at different drive powers . . . . . . . . . . . . . . . . . 176

8.7 Density plot showing the AC Stark shift and slices at different drive powers . . . . . 178

8.8 AC Stark shift and dephasing rate vs. input power . . . . . . . . . . . . . . . . . . . 179

8.9 Non-linear corrections to the AC Stark effect . . . . . . . . . . . . . . . . . . . . . . 180

8.10 Dephasing due to measurement photons showing higher powers and a more comprehensive theory183

8.11 Measurement setup for off-resonant AC Stark effect and sideband experiments . . . 184

8.12 Lorentzian cavity transmission spectrum and experimental signal frequencies . . . . 185

8.13 AC Stark shift using tone detuned from cavity frequency . . . . . . . . . . . . . . . . 186

8.14 Plots of AC Stark shifted qubit transition frequency and linewidth with and off-resonant tone186

8.15 Qubit-cavity energy levels illustrating sideband transitions. . . . . . . . . . . . . . . 187

8.16 Sideband spectroscopy density plot and spectrum . . . . . . . . . . . . . . . . . . . . 188

8.17 Tracking sidebands as function of spectroscopy and AC Stark drive tone parameters 190

8.18 Strong dispersive spectral features . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193

8.19 Direct spectroscopic observation of quantized cavity photon number . . . . . . . . . 195

8.20 Density and waterfall plots of the dispersive cavitys inherited non-linearity from its coupling to the qubit1

8.21 Anharmonic cavity shifts and linewidths . . . . . . . . . . . . . . . . . . . . . . . . . 199

9.1 Time resolved measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202

9.2 Rabi oscillation experiment and individual time slices . . . . . . . . . . . . . . . . . 204

9.3 Rabi oscillations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206

9.4 Ramsey fringes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206

9.5 Histograms of single shot measurements . . . . . . . . . . . . . . . . . . . . . . . . . 210

9.6 Single photon source protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212

9.7 Mapping of qubit state onto photon states . . . . . . . . . . . . . . . . . . . . . . . . 215

9.8 Spontaneous emission from qubit Rabi oscillations in cavity . . . . . . . . . . . . . . 217

9.9 Single photon fluorescence tomography . . . . . . . . . . . . . . . . . . . . . . . . . . 218

10.1 Sketch of two cavities and two qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . 221

10.2 Sketch of hybrid circuit QED with molecules . . . . . . . . . . . . . . . . . . . . . . 223


-----


LIST OF FIGURES 12

B.1 Radiative decay in the presence of coupling . . . . . . . . . . . . . . . . . . . . . . . 231


-----


## List of Tables

1.1 Types of qubits and effects of different types of noise . . . . . . . . . . . . . . . . . . 27

3.1 Table of superconductor properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

3.2 Key rates and parameters for different CQED systems . . . . . . . . . . . . . . . . . 72

4.1 Comparison of representative relaxation and dephasing times for various superconducting qubit designs. T

7.1 Sample Info . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167

D.1 Optical Lithography Recipe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235

D.2 Electron beam resist spinning recipe . . . . . . . . . . . . . . . . . . . . . . . . . . . 235

D.3 Electron beam resist development recipe . . . . . . . . . . . . . . . . . . . . . . . . . 236

D.4 Nb sputtering recipe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237

D.5 Deposition and Liftoff recipe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238

13


-----


## List of Symbols and Abbreviations

a  , a Photon creation and annihilation operators
 

b  , b Transmon excitation creation and annihilation operators
 

( C g ) Gate capacitance

C in / out Resonator input/output coupling capacitor

(  C n )  Effective resonator capacitance for the n th cavity mode

( C j ) Junction capacitance

( C s ) Stray capacitance between islands

( C  ) Total capacitance between islands

( C s ) Shunting capacitance used to increase C  and lower E C and g

Cooper Pair Box - consisting of two small superconducting islands connected by a
( CPB )
Josephson junction

Conditional Not, a two qubit gate in which one qubit is flipped depending on the
( CNOT )
state of the other

( E  ,n ) Energies with n excitations from exact diagonalization of Jaynes-Cummings Hamiltonian

( | g/e, n  ) State vector with atom in ground/excited state and n-photons

Exact eigenstates of Jaynes-Cummings Hamiltonian, n is total number of excitations

![SchusterThesis.pdf-16-0.png](SchusterThesis.pdf-16-0.png)
, n
|  (not photon number)

 

( E C ) Cooper pair box charging energy (in single e units)

( E J ) Josephson energy

( g ) Interaction rate between qubit and photon

( g ij ) Cavity-qubit coupling between qubit levels i and j

14


-----


List of Symbols and Abbreviations 15

( I c ) Josephson critical current

( J c ) Josephson critical current density (per unit area)

( L J ) Josephson inductance

( L J 0) Josephson inductance in zero current limit

( L K ) Kinetic inductance per unit length of the (superconducting) CPW

( L m ) Magnetic inductance per unit length of the CPW

( L n ) Effective resonator inductance for the n th cavity mode

( n ) Average photon number in the cavity

![SchusterThesis.pdf-17-0.png](SchusterThesis.pdf-17-0.png)

Number of photons before dispersive approximation fails to converge, n crit =
( n crit )  2 / 4 g 2


Number of photons before second order term in dispersive Taylor expansion of
( n  ) energy is comparable to cavity linewidth, n  =  2  g 4 3

![SchusterThesis.pdf-17-1.png](SchusterThesis.pdf-17-1.png)

( n g ) Gate polarization charge

( n s ) Density of Cooper pairs

( n n ) Density of quasiparticles

( Q ) Cavity quality factor ( Q =  r / )

Q int / ext Quality factor due to internal/external losses
 

( Q op ) Operations quality factor, defined as number of oscillations in one decay time T op /T 2

( Q  ) Pure dephasing quality factor

( Q res ) Quality factor due to resistivity of CPW

( Q rad ) Quality factor due to radiative losses

q in / out External inverse q factor, the external resonator quality factor is Q int = 1 /q in 2 / out
 

( QED ) quantum electrodynamics

( qubit ) A quantum mechanical bit, referring to any quantum system with two levels

( R K ) The resistance quantum (Von Klitzing constant) R K = h/e 2  25 . 8 k

( R n ) Resistance of tunnel junction in normal state


-----


List of Symbols and Abbreviations 16

Rivest-Shamir-Adelman public key cryptosystem, which bases its security on the
( RSA )
computational difficulty of factoring products of large primes

( S I ) Spectral density of current noise in units of A 2 / Hz 1 / 2

( S  ) Spectral density of flux noise in units of  2 0 / Hz 1 / 2

( S V ) Spectral density of voltage noise in units of V 2 / Hz 1 / 2

( S Q ) Spectral density of charge noise in units of e 2 / Hz 1 / 2

(1 /T ) Inverse transit time for atom to leave the cavity

( T 1 ) Qubit state relaxation time

( T 2 ) Total dephasing time

( T 2  )
Inhomogenous dephasing time, due to ensembles of different qubit frequencies (usually due to 1 /f noise)

( T op ) Operation time

( T  ) Pure dephasing time

( V g ) Cooper pair box gate voltage

( V j ) Voltage across the junction when a gate voltage is applied elsewhere

( Z L ) Load impedance

( Z C ) Characteristic impedance

(  ) Fine structure constant or anharmonicity (depending on context)

(  r ) Relative anharmonicity / a

() Atom-cavity detuning =  a  r


(  m ) Charge dispersion of m th CPB energy level

(  eff ) Effective dielectric constant of CPW mode

 re / im Real and imaginary parts of the substrate dielectric constant
 

(  r ) Relative dielectric constant

(  ) Decay rate of atom into modes other than the cavity


( eff ) Decay rate of atom including all channels of decay

(   ) Radiative decay of the atom by radiating through the cavity


-----


List of Symbols and Abbreviations 17

(  ) Decay rate of photon out of the cavity

(   ) Decay of photons by decaying through the atom via non-radiative means

 in / out Photon decay rate due to the input/output coupling
 

(  L ) The London penetration depth, describing the depth within which currents flow

(  r ) Relative magnetic permeability

(   ) Qubit excitation creation and annihilation operators

(  x , y , z ) Pauli matrices for a spin 1/2 particle used to measure x,y,z components of qubit

(  n ) Conductivity of the normal fluid

Scattering time of the normal fluid (Drude model), which is a measure of the real
(  n ) part of the conductivity

(  ) Cavity shift or Stark shift per photon,  = g 2 / for a two level atom

(  ij ) Dispersive shift between cavity and qubit levels i and j

(  eff ) Effective dispersive shift due to interactions of all qubit levels with the cavity

(  a ) Ground-excited state transition (angular) frequency

(  r ) Cavity resonance (angular) frequency

(  s ) Spectroscopy (angular) frequency


-----


### Chapter 1

## Introduction

Progress in science is often a result of exchanging principles and techniques between seemingly

disparate disciplines. Often this interaction leads both fields in new directions. The subject of this

dissertation, circuit quantum electrodynamics is an excellent example of such cross-pollination.

In this work, techniques imported from atomic cavity quantum electrodynamics (QED), a field

developed to study the quantum interaction of light and matter, are applied to superconducting

circuits to realize the building blocks of a quantum computer. Amazingly, some circuits, though

containing billions of atoms, can be accurately described as a single atom. Leveraging techniques

from atomic physics, this metaphor is exploited to enhance the circuits fidelity and develop new ways

of coupling them together. While circuits can behave much like artificial atoms, their properties are

quite supernatural, allowing circuit QED to explore new regimes of cavity QED that are difficult to

reach with ordinary atoms. The introduction will first discuss quantum computation, its importance,

and the challenges associated with its realization. Next, some simple questions that arise in a

quantum theory of light lead to a brief discussion of beautiful experiments in cavity QED. Finally,

these ideas are brought together to describe an architecture for quantum computing employing a

superconducting circuit version of cavity QED.

####### 1.1 ####### Quantum Computation

Information is inherently a physical quantity, and the physics of information is the physics of all

matter [Landauer1991]. The concept of the computer was developed in part as a concrete means

to answer fundamental questions about information, such as What questions can and cannot be

answered? The idea of a quantum computer arose out of studying the thermodynamics of compu-

18


-----


CHAPTER 1. INTRODUCTION 19

tation [Bennett1982], and asking what is information in a world described by quantum mechanics,

where apparently there exist inherent randomness and non-locality. The pursuit of a quantum com-

puter can be thought of as a way to improve current computer technology, as a way to simulate

quantum mechanics, or simply as a universal quantum problem stimulating interaction between

disparate scientific disciplines.

In 1985 David Deustch proposed a simple algorithm [Deutsch1985] exploiting quantum informa-

tion to solve a model problem inherently faster than could be done classically. While the particular

problem was somewhat contrived, it was the first demonstration that the richer physics available to

a quantum computer might allow it to perform faster than a classical computer. Later, in 1994 Peter

Shor devised quantum algorithms which could factor and take discrete logarithms of large numbers,

exponentially faster than the best known classical algorithm [Shor1994]. These two longstanding

computational problems are particularly important because they are one-way, that is, its easy

to pose the problem and verify the solution (e.g. by multiplying two numbers together), but ex-

tremely difficult (the best known classical algorithm requires exponentially more steps than the size

(in bits) of the number) to factor. Multiplying numbers with hundreds of digits can be completed

essentially instantaneously, while with the best current algorithms and classical computers, it would

take the lifetime of the universe to factor them. The ease of multiplication and difficulty of fac-

toring has been exploited to create the Rivest-Shamir-Adelman (RSA) public-key cryptography

system [Rivest1978]. The idea that a quantum computer could mount a successful attack on RSA

(and other similar systems) has stimulated much interest in both the theory and construction of

quantum computers. Since then, new algorithms have been developed, most notably the Grover

search algorithm [Grover1997] which speeds the time to search unstructured data quadratically, and

though there is not an exponential speed-up, searching is quite important.

The physical basis of information not only allows current encryption schemes to be defeated,

but also provides for new quantum encryption schemes which are based not on the computational

difficulty of a one-way problem, but instead on limits of measurement imposed by quantum mechan-

ics [Bennett1984, Bennett1992]. When properly implemented, such systems are unbreakable with

known physics. Quantum cryptography systems have now been demonstrated and are even sold

commercially.

While cryptography is relevant to national security and central in the study of computational

complexity, there is another important application for quantum computing, namely simulating quan-


-----


CHAPTER 1. INTRODUCTION 20

tum physics. Classical computers are ill-equipped to simulate quantum physics, folding under the

weight of even small problems involving only a modest number of degrees of freedom. Richard Feyn-

man noticed this difficulty and postulated that it might be possible to use a quantum computer to

simulate quantum physics more efficiently [Feynman1982]. For very small quantum systems involv-

ing only a few degrees of freedom, brute force calculations can sometimes capture the important

physics of a system. For quantum systems with a large number of degrees of freedom, consisting

of millions, even 10 23 objects, usually individual fluctuations can be ignored. The mean behavior

can usually be described in classical terms using parameters derived from quantum considerations.

However, there exists a large class of physical situations, involving from tens to hundreds of degrees

of freedom, which cannot be addressed by these methods. This class of problems are central in

topics including nuclear physics, atomic physics, and chemistry. If a quantum computer could be

harnessed to predict from first principles the behavior of many-body systems in these areas, it could

revolutionize every aspect of technology.

The rest of this dissertation will concern itself with the physical realization of a quantum com-

puter. A computer is built of bits that store information and gates which operate on those bits. To

create a quantum computer one must first build these fundamental components. A classical bit can

be made from any system with two states, a coin or a MOSFET transistor. Of course the transistor

is a superior choice for most applications. Similarly, a quantum bit or qubit can be created from any

two quantum states, and while coins are not likely candidates, we have yet to find the equivalent of

the quantum transistor. This means that essentially any quantum system could be used to create

qubits, with attempts underway using ion traps [Monroe1995], nuclear [Gershenfeld1997, Cory1997]

and electron spins [Loss1998], neutral atoms [Deutsch2000], photons [Knill2001], and also supercon-

ducting circuits [Wallraff2004, Devoret2004, Chiorescu2004, Martinis2002] among others.

The primary requirements for a physical system used to study quantum information are that it

be controllable. That is, it must be easy to couple multiple qubits together and for the experimenter

to measure them [DiVincenzo2000]. More challenging still, it must be coherent, avoiding both decay

and dephasing. Much like a classical bit, when set to one it should not change, or relax back to

zero (see Fig. 1.1a). Unlike a classical bit though, a qubit can be in a superposition of states. In

this state, much like a spinning top (why qubits are often called spins), it precesses, acting as a

sort of clock measuring the frequency difference between the two states. If the qubit is subject to

noise (internal or external) the clock can lose time or dephase, a subtle form of decoherence that


-----


CHAPTER 1. INTRODUCTION 21

######### |1 ######### 

![SchusterThesis.pdf-23-0.png](SchusterThesis.pdf-23-0.png)

![SchusterThesis.pdf-23-3.png](SchusterThesis.pdf-23-3.png)

 |0 

![SchusterThesis.pdf-23-1.png](SchusterThesis.pdf-23-1.png)

![SchusterThesis.pdf-23-2.png](SchusterThesis.pdf-23-2.png)

Figure 1.1: a. Any two quantum energy levels can be used as a qubit. Relaxation occurs when the
qubit decays from the excited state to the ground state. b. When in a superposition, the phase,  ,
of the qubit precesses at a frequency determined by the energy difference between the two levels. If
this energy varies in time, the clock speed will vary causing it to lose time or dephase.

is the bane of most would-be qubits (see Fig. 1.1b). It is for this reason that there is an intimate

relationship between the study of atomic clocks and quantum bits [Monroe1995].

In order to prevent decoherence, this loss of quantum character, the elements of a quantum

computer must both be isolated from sources of noise, and yet be strongly coupled to each other,

all the while being controlled by the classical experimenter. These nearly antithetical requirements

pose a shared challenge for all quantum computing experiments, and have stimulated the flow of

ideas among disciplines. In this project, we apply analogies of atomic physics to superconducting

circuits, as a means of taming the large decoherence present in solid-state environments. Applying

these analogies in reverse we use superconducting circuits to access areas difficult or impossible to

study in natural atomic systems.

####### 1.2 ####### Cavity Quantum Electrodynamics

The electromagnetic field, though it has a wave-like nature, is composed of discrete packets known

as photons. At first glance, this seems like a rather innocuous postulate, a matter of bookkeeping

rather than a qualitative shift from classical waves. This discretization, however, has subtle and far

reaching effects, explaining many mysteries, including the color of a hot object such as our sun, and

why excited atoms decay, emitting light only at certain frequencies. The complexities of the photon

postulate become more apparent when asking even a simple question like, What is the shape of

a photon? The answer to this is subtle. Both the spatial and temporal distributions of energy

are not fixed, but are dependent and controllable by the boundary conditions imposed upon the

photon by matter. If a photon is so malleable how can it be discrete? How does matter interact


-----


CHAPTER 1. INTRODUCTION 22

with light on the single photon level? Quantum optics [Walls2006] which studies the implications

of quantum mechanics on light, attempts to answer such questions. The laser, one of the most

important inventions of the past century, and one of the first fruits of such endeavors, exploits the

principles of quantum mechanics to generate exquisitely well defined, but classical light. Much like

the transistor, this device uses quantum properties to perform with incredible speed and precision

in a classical task. As it is possible to make a bit that is inherently quantum mechanical, it is also

possible to make states of light which bear no classical analogue. Both classical and quantum states

of light must have some intrinsic noise, but using quantum optics, one can redistribute this noise

to create states in which the noise is reduced in one parameter (i.e. the number of photons) at the

expense of another (i.e. the phase of those photons). Such squeezed states can be used to measure

with superior precision [Huelga1997] and also to transport quantum information [Duan2001].

Perhaps the truest quantum state of light is an electromagnetic field containing exactly one

photon. The first way one might think to do this is to take a coherent or incoherent light source,

and attenuate it until there is on average a single photon. However, despite having on average one

photon an attenuated classical state will retain most of its classical nature, and there will still be a

probability to have more or less than a single photon. To get a single photon one needs a non-linear

system, ideally one with only two states, such as an atom. If this atom is put into its excited state,

it will decay, emitting exactly one photon. Typically the cross-section for interactions between a

single atom and photon is quite small, making it difficult to observe their effect on one another.

Cavity quantum electrodynamics [Berman1994] (QED) gives a means by which to overcome

these technical difficulties to experimentally answer fundamental questions about photons and their

interaction with matter. The prototypical cavity QED system is an atom modeled as a two-level

system coupled to a harmonic oscillator, whose excitations are photons. The system has the the-

oretical virtue that it is relatively easy to describe while capturing the essence of the matter-

light interaction. Discussed in section 2, the ubiquity of this type of interaction makes the con-

cept generalizable to many different physical systems, including ions [Monroe1995], semiconduc-

tors [Reithmaier2004, Yoshie2004], nanomechanical structures [Irish2003], and the subject of this

work, superconducting electrical circuits [Blais2004].

Normally, when an atom couples to its electromagnetic environment, noise present even in the

vacuum will cause it to spontaneously decay, emitting a photon never to be seen again, and destroying

the atoms coherence. In cavity QED, a very different environment is created, in which the cavity acts


-----


CHAPTER 1. INTRODUCTION 23

like a hall of mirrors, reflecting photons back and forth as many as one million times [Vahala2003]

before they leak out. In this way, the cavity confines photons to a small volume, increasing their

energy density and giving them many chances to interact with the atom, and thereby enhancing the

effective interaction strength. One might think that this would enhance the atom decay, however

only photons of a precisely defined energy (the resonant frequency of the cavity) can fit in this cavity.

If the atom and cavity do not share the same frequency, the emitted photon does not fit inside the

cavity, and the spontaneous decay can be suppressed, allowing it to remain coherent far longer than

in free space. When they are resonant, and the cavity is designed to be very leaky, the atom can be

made to decay even faster than in free space. When they are resonant and the cavity is not leaky,

then an even stranger thing happens. If this interaction strength is large enough, the strong coupling

limit is reached, and the atom can emit and reabsorb a single photon many times before the atom

decays or the photon has time to escape. Apparently, inside a cavity the spontaneous decay can be

made coherent! Cavity QED allows one to suppress, enhance, and even make coherent the radiative

decay of an atom, allowing one to study and engineer this mysterious quantum process.

The last process, a periodic oscillation between photon and atom excitation, is known as a

vacuum Rabi oscillation, called such in honor of I. I. Rabi and because it is as if the oscillation is

stimulated by the zero point noise of the vacuum (see Fig. 1.3b). Another way to think about this

phenomenon, is that the atom and cavity share a single quantum of energy, in an analogous manner

to that of two atoms sharing an electron in a molecule. Like in a molecule, this system has two states

similar to a bonding and anti-bonding orbital, which can be measured spectroscopically by looking

at the energies of photons allowed to pass through the atom-cavity system (1.2b). Our observation

of this vacuum Rabi splitting in a solid state system is one of the central results of this work and is

discussed further in section 8.1.

Because the physics of cavity QED is so fundamental there are many systems in which it can

be observed. One such system traps a cloud of hydrogen-like alkali atoms above an optical cavity

formed by two highly reflective mirrors (see Fig. 1.2a). Atoms are then released from the trap such

that on average only a single atom falls into the cavity. As the atom drops through, it slightly

changes the cavitys properties, which can then be probed by shining a laser through the cavity.

This allows one to count how many atoms are in the cavity [McKeever2004] (see Fig. 1.2c) and even

detect the state of a single atom. An analogous measurement technique is used in this work and is

discussed in sections 2.1 and 3.4.


-----


CHAPTER 1. INTRODUCTION 24

from quantum optics group, Caltech


Probe
Laser


Measure


![SchusterThesis.pdf-26-6.png](SchusterThesis.pdf-26-6.png)

![SchusterThesis.pdf-26-3.png](SchusterThesis.pdf-26-3.png)

![SchusterThesis.pdf-26-5.png](SchusterThesis.pdf-26-5.png)

![SchusterThesis.pdf-26-4.png](SchusterThesis.pdf-26-4.png)

![SchusterThesis.pdf-26-0.png](SchusterThesis.pdf-26-0.png)

Fabry-Perot Optical Cavity

Figure 1.2: a. Cavity QED setup dropping a cloud of cesium atoms into a Fabry-Perot optical
cavity. Transmission of a laser through a cavity is monitored to determine the atomic state. b.
First observation of vacuum Rabi splitting. The spectrum is similar to that of the response of a
molecule with two a pair energy levels split by the bond strength. c. Plot of cavity transmission
used to count the number of atoms inside it.

a) b) Rydberg Cavity QED group, ENS

![SchusterThesis.pdf-26-1.png](SchusterThesis.pdf-26-1.png)

![SchusterThesis.pdf-26-2.png](SchusterThesis.pdf-26-2.png)

microwave cavity Time (  s)

![SchusterThesis.pdf-26-8.png](SchusterThesis.pdf-26-8.png)

![SchusterThesis.pdf-26-7.png](SchusterThesis.pdf-26-7.png)

Figure 1.3: a. Model of Rydberg atom cavity QED setup. At left atoms are prepared into highly
excited Rydberg states, then prepared into an intial state and filtered for velocity. They then pass
through a high finesse three-dimensional microwave cavity which is cooled to  1 K interacting with
photons inside. Finally the atom state is measured by selective ionization. b. First observation of
vacuum Rabi oscillation. An excited state atom is sent into the cavity where it coherently emits and
absorbs a single photon, the excited state population of the atom is then measured as a function of
time spent in the cavity.


-----


CHAPTER 1. INTRODUCTION 25

![SchusterThesis.pdf-27-0.png](SchusterThesis.pdf-27-0.png)

![SchusterThesis.pdf-27-1.png](SchusterThesis.pdf-27-1.png)

![SchusterThesis.pdf-27-2.png](SchusterThesis.pdf-27-2.png)

Figure 1.4: a. A self assembled quantum dot inside a micro-pillar of alternating dielectrics (GaAs
and AlAs) to create a distributed bragg reflector cavity [Reithmaier2004]. b. A two-dimensional
photonic band gap crystal supported by a micro pillar [Yoshie2004]. c. Top view of the photonic
crystal showing defect in crystal forming the cavity. The quantum dot is located underneath the
surface inside the defect.

Another atomic cavity QED system that heavily influences this work, uses Rydberg atoms and

three-dimensional microwave cavities [Raimond2001]. Rydberg atoms are highly excited alkali atoms,

with much larger electron orbits than ground state atoms (1000  A vs. 1  A). Their large size allows

them to possess much larger dipole moments, and thus to interact more strongly with light. In

addition, radiative decay is much slower for microwave excitations than optical excitations, giving

more time for the atoms to interact with the photons. However, these benefits come at the price of

having less energy available, making direct detection of the photons difficult and requiring cryogenic

cooling of the cavity to  1 K. Fortunately, the atoms can be detected directly by selective ioniza-

tion. This leads to a different and interesting reversal of focus from the previous implementation,

with atoms as meters, probing the cavity photons. In addition to measuring the vacuum Rabi

oscillations described above (see Fig. 1.3b), the Rydberg atoms can be used to count the number

of photons in the cavity [Brune1996] (see Fig. 1.3c). Another experiment measured the presence of

a single photon without destroying it, constituting a quantum non-demolition (QND) measurement

of a single photon [Nogues1999], while a more recent experiment measured quantum jumps as the

number of cavity photons changed [Gleyzes2007]. In section 8.3 we present a new technique for

counting photons without destroying them.

In addition to atomic systems, rapid progress is also being made in semiconducting systems,

using quantum dots as artificial atoms. In one technique, self assembled dots and a distributed

Bragg reflector cavity made from alternating layers of epitaxially grown dielectric materials are


-----


CHAPTER 1. INTRODUCTION 26

used [Reithmaier2004](see Fig. 1.4a). Another uses a quantum well in a defect of two dimensional

photonic band gap crystal acting as a cavity to confine the photon [Yoshie2004] (see Fig. 1.4a). While

not yet as sophisticated as atomic cavity QED, these efforts provide a natural path to integrate

quantum optics techniques with current solid state optical technology.

####### 1.3 ####### Quantum Circuits

The goal of this project is to realize a cavity QED system using superconducting electrical circuits

rather than natural atoms. Superconducting circuits can be engineered to have discrete, non-linear

spectra and long coherence times, making them resemble artificial atoms. The toolbox of supercon-

ducting circuit elements consists of capacitors, inductors, and the Josephson element. The Josephson

junction is the only 1 known dissipationless non-linear circuit element[Devoret2004]. It acts much

like a non-linear inductor which, like the semiconductor transistor, provides the basis for gain, and

non-trivial logic. These building blocks are the elements of a circuit periodic table, which has its

own unique and highly versatile chemistry. By arranging the elements in different topologies, one

can realize circuits which operate on quantized photon number, charge, flux, or phase states (see

Fig. 1.5).

The simplest combination is the LC circuit, which creates an electrical simple harmonic oscil-

lator 2 . This circuit, if built at high enough frequencies (gigahertz) and operated at low enough

temperatures ( < 100 mK), will have thermally resolvable energy levels corresponding to microwave

photons. Unfortunately, because it is harmonic (the levels are evenly spaced), there is no way,

with an LC oscillator alone, to observe the discrete nature of these photons. In order to detect the

quantization of energy one must have a non-linear element. If the inductor is replaced with a small

Josephson junction, then one realizes a Cooper pair box, a type of charge qubit [Nakamura1999].

The junction allows Cooper pairs to tunnel between sides of the capacitor but weakly enough that

the states of the qubit can be labeled by the charge difference between the islands. The conjugate

quantum variable to charge is flux. One can also make a qubit, by storing a flux quantum in a loop

interrupted by a Josephson junction [Mooij1999]. The quantum variable is then the number of flux

quanta (or sign of the persistent current). One can also replace the inductor in the harmonic oscil-

![SchusterThesis.pdf-28-0.png](SchusterThesis.pdf-28-0.png)

1 Some microscopic ferromagnetic or ferroelectric materials might also be usable to make non-linear inductors or
capacitors.
2 While it is possible to make a lumped element LC oscillator, one can also use a distributed cavity approximating
the resonance as that of an effective LC (see Sec. 3.1).


-----


CHAPTER 1. INTRODUCTION 27

![SchusterThesis.pdf-29-0.png](SchusterThesis.pdf-29-0.png)

Control Readout Charge Noise Flux Noise Critical Current Noise

![SchusterThesis.pdf-29-1.png](SchusterThesis.pdf-29-1.png)

![SchusterThesis.pdf-29-2.png](SchusterThesis.pdf-29-2.png)

![SchusterThesis.pdf-29-3.png](SchusterThesis.pdf-29-3.png)

![SchusterThesis.pdf-29-4.png](SchusterThesis.pdf-29-4.png)

![SchusterThesis.pdf-29-5.png](SchusterThesis.pdf-29-5.png)

![SchusterThesis.pdf-29-6.png](SchusterThesis.pdf-29-6.png)

![SchusterThesis.pdf-29-7.png](SchusterThesis.pdf-29-7.png)

![SchusterThesis.pdf-29-8.png](SchusterThesis.pdf-29-8.png)

![SchusterThesis.pdf-29-9.png](SchusterThesis.pdf-29-9.png)

Charge Charge High Low Medium

![SchusterThesis.pdf-29-10.png](SchusterThesis.pdf-29-10.png)

![SchusterThesis.pdf-29-11.png](SchusterThesis.pdf-29-11.png)

![SchusterThesis.pdf-29-12.png](SchusterThesis.pdf-29-12.png)

![SchusterThesis.pdf-29-13.png](SchusterThesis.pdf-29-13.png)

![SchusterThesis.pdf-29-14.png](SchusterThesis.pdf-29-14.png)

![SchusterThesis.pdf-29-15.png](SchusterThesis.pdf-29-15.png)

![SchusterThesis.pdf-29-16.png](SchusterThesis.pdf-29-16.png)

![SchusterThesis.pdf-29-17.png](SchusterThesis.pdf-29-17.png)

Flux Flux Low High Medium

![SchusterThesis.pdf-29-18.png](SchusterThesis.pdf-29-18.png)

![SchusterThesis.pdf-29-19.png](SchusterThesis.pdf-29-19.png)

![SchusterThesis.pdf-29-20.png](SchusterThesis.pdf-29-20.png)

![SchusterThesis.pdf-29-21.png](SchusterThesis.pdf-29-21.png)

![SchusterThesis.pdf-29-22.png](SchusterThesis.pdf-29-22.png)

![SchusterThesis.pdf-29-23.png](SchusterThesis.pdf-29-23.png)

![SchusterThesis.pdf-29-24.png](SchusterThesis.pdf-29-24.png)

![SchusterThesis.pdf-29-25.png](SchusterThesis.pdf-29-25.png)

Phase Phase Low Low High

![SchusterThesis.pdf-29-26.png](SchusterThesis.pdf-29-26.png)

![SchusterThesis.pdf-29-27.png](SchusterThesis.pdf-29-27.png)

![SchusterThesis.pdf-29-28.png](SchusterThesis.pdf-29-28.png)

![SchusterThesis.pdf-29-29.png](SchusterThesis.pdf-29-29.png)

![SchusterThesis.pdf-29-30.png](SchusterThesis.pdf-29-30.png)

![SchusterThesis.pdf-29-31.png](SchusterThesis.pdf-29-31.png)

![SchusterThesis.pdf-29-32.png](SchusterThesis.pdf-29-32.png)

![SchusterThesis.pdf-29-33.png](SchusterThesis.pdf-29-33.png)

Flux magnetic susceptibility Low Medium Medium

![SchusterThesis.pdf-29-34.png](SchusterThesis.pdf-29-34.png)

![SchusterThesis.pdf-29-35.png](SchusterThesis.pdf-29-35.png)

![SchusterThesis.pdf-29-36.png](SchusterThesis.pdf-29-36.png)

![SchusterThesis.pdf-29-37.png](SchusterThesis.pdf-29-37.png)

![SchusterThesis.pdf-29-38.png](SchusterThesis.pdf-29-38.png)

![SchusterThesis.pdf-29-39.png](SchusterThesis.pdf-29-39.png)

![SchusterThesis.pdf-29-40.png](SchusterThesis.pdf-29-40.png)

![SchusterThesis.pdf-29-41.png](SchusterThesis.pdf-29-41.png)

Charge electric susceptibility Medium Low Medium

![SchusterThesis.pdf-29-42.png](SchusterThesis.pdf-29-42.png)

![SchusterThesis.pdf-29-43.png](SchusterThesis.pdf-29-43.png)

![SchusterThesis.pdf-29-44.png](SchusterThesis.pdf-29-44.png)

![SchusterThesis.pdf-29-45.png](SchusterThesis.pdf-29-45.png)

![SchusterThesis.pdf-29-46.png](SchusterThesis.pdf-29-46.png)

![SchusterThesis.pdf-29-47.png](SchusterThesis.pdf-29-47.png)

![SchusterThesis.pdf-29-48.png](SchusterThesis.pdf-29-48.png)

![SchusterThesis.pdf-29-49.png](SchusterThesis.pdf-29-49.png)

Table 1.1: Each qubit is sensitive to different types of noise. Simple qubits which use the same
quantum variable for controlling and reading out the qubit tend to be more sensitive to noise in that
parameter. Qubits which exploit dispersive readout techniques can moderate the effects of noise by
working at first order insensitive points and measuring second order properties.

lator with a large Josephson junction. By itself this configuration would also be nearly harmonic,

but clever application of a bias current can enhance the nonlinearity 1 .

The atom is natures quantum system, built from a small number of tightly bound fundamental

particles, able to exist in the exquisite isolation of an ultra high vacuum environment, an atom

can easily maintain its quantum purity for an astonishing 10 14 oscillation periods [Diddams2001]!

Artificial atoms made with quantum circuits are made from billions of atoms, allowing the engineer

to tune the atom parameters at a level difficult or impossible with natural atoms. However, these

macroscopically coherent systems, also involve many more degrees of freedom which can contribute

to decoherence. Any fluctuation or imperfection in the system that couples to the circuit is a

potential source of decoherence. Noise which couples to a circuits preferred quantum variable (or

its conjugate) is particularly harmful (see Table 1.1). Minimizing sources of environmental noise

and its coupling to the circuit is a primary goal of all quantum circuit research.

Circuits must be measured to project their quantum state, and this can provide a natural channel

for noise to couple to the circuit. This has led to new designs, which rather than measuring charge,

flux, or phase directly measure a second order (dispersive) property, such as the electric [Blais2004],

or magnetic susceptance (dipole moment) [Born2004, Siddiqi2006]. These methods allow one to

reduce the sensitivity of the qubit to noise via the measurement port. There has been rapid progress

in improving resilience to noise in all of these flavors of qubit, via a very productive exchange of

ideas between the various groups. These issues are discussed in depth in chapter 4.

For this work we chose to explore the Cooper pair box (CPB) [Buttiker1987, Bouchiat1998,

Cottet2002] as an artificial atom and a qubit. This qubit was chosen because, with clever readout

technique to measure the dipole moment (see Sec. 3.4), it is only moderately sensitive to known

![SchusterThesis.pdf-29-50.png](SchusterThesis.pdf-29-50.png)

1 This type of qubit is especially sensitive to fluctuations in the bias current.


-----


CHAPTER 1. INTRODUCTION 28


![SchusterThesis.pdf-30-3.png](SchusterThesis.pdf-30-3.png)

![SchusterThesis.pdf-30-2.png](SchusterThesis.pdf-30-2.png)

![SchusterThesis.pdf-30-0.png](SchusterThesis.pdf-30-0.png)

![SchusterThesis.pdf-30-1.png](SchusterThesis.pdf-30-1.png)

![SchusterThesis.pdf-30-4.png](SchusterThesis.pdf-30-4.png)

![SchusterThesis.pdf-30-5.png](SchusterThesis.pdf-30-5.png)

Figure 1.5: A gallery of superconducting qubits. a) A charge qubit based on a Cooper pair box
(CPB) with single electron transistor (SET) readout. b) A charge/phase qubit quantronium which
is a CPB which is excited via charge but readout in phase. c) A phase qubit which uses phase both
for its quantum variable and its readout. d) A flux qubit which uses the direction of a persistent
current as its quantum state and is readout using flux.


-----


CHAPTER 1. INTRODUCTION 29


![SchusterThesis.pdf-31-0.png](SchusterThesis.pdf-31-0.png)


2


######### E ######### c


######### E ######### J

![SchusterThesis.pdf-31-1.png](SchusterThesis.pdf-31-1.png)

Figure 1.6: The Cooper pair box as a tuanble atom. Cooper pairs (pair of green circles) can tunnel
between islands (light blue) separated by the two tunnel junctions (orange), under the influence of
an applied gate voltage (electric field, E) and current (magnetic flux through the ring). The Cooper
pair box can be thought of as an atom, with tunable energy scales. The electrostatic energy ( E c )

can be modified by applying an electric field (Stark shift), while the Josephson tunneling energy
( E J ) can be tuned with a magnetic field (Zeeman shift). These low lying excitations are protected

from a lossy continuum of normal electron states by the superconducting gap (2).

sources of noise (see Ch. 4). The Cooper pair box, discussed theoretically in section 3.2 and ex-

perimentally in sections 5.2 and 7.2, consists of two small superconducting islands coupled via a

Josephson tunnel junction [Josephson1962, Tinkham2004] (see Fig. 1.8 for an image of an actual

CPB sample). The CPB has two energy scales, the charging energy, which is the energy to add an

electron to one of the islands, and the Josephson energy gained when a Cooper pair tunnels between

islands through the tunnel junction (a thin  1 nm insulating barrier between the islands). In the

Cooper pair box, both of these energy scales correspond to gigahertz frequencies. The maximum

values of both the charging and Josephson energies can be designed by specifying the geometry of

the box, and further can be tuned in-situ by applying a gate voltage or magnetic field respectively

(see Fig. 1.6).

####### 1.4 ####### Circuit Quantum Electrodynamics

Superconducting circuits can be made to act like coherent artificial atoms. Such circuits typi-

cally operate at microwave frequencies and their quantum variables manifest themselves in familiar

macroscopic parameters such as current and voltage. Though the circuits themselves are manifestly

quantum, the electromagnetic fields used to interact with them were, prior to the present work, used

in a classical manner. This is analogous to the interactions between a laser and atom before the


-----


CHAPTER 1. INTRODUCTION 30

![SchusterThesis.pdf-32-0.png](SchusterThesis.pdf-32-0.png)

Figure 1.7: Schematic representation of cavity QED with superconducting circuits. Cooper pair
box (green) at the center of a coplanar waveguide resonator (blue). The cavity resonant frequency
(  5 GHz) is set by the length between two gap capacitors at the ends, which act as highly reflective
microwave mirrors. The cavity is driven from one side and the transmitted signal is measured on
the other side. The box is placed at an antinode in the spatial voltage profile for the first harmonic
(pink). The system can be accurately modeled as a series of lumped element circuits.

advent of cavity QED. The primary contribution of this thesis is to apply the notions of cavity QED

to the study of quantum circuits, a notion we dub Circuit Quantum Electrodynamics.

Though microwaves do not seem to have much in common with visible light, they are both

electromagnetic fields and thus composed of photons. Even when studying qubits, the quantum

properties of microwaves are often ignored. However cavity QED shows that these properties can be

an asset rather than just a complication, enabling one to engineer the decoherence properties of these

circuits, making them decay slower or faster. By embracing the quantum nature of microwaves, we

are able to solve many problems associated with measuring quantum circuits without exposing them

to sources of decoherence. We can protect them from radiative decay, and use single microwave

photons as a means of coupling distant qubits together.

The circuit QED architecture [Blais2004] places a superconducting qubit, which can be thought

of as an artificial atom, inside of a transmission line resonator that forms a microwave cavity (see

Fig. 1.7).

The key to this cavity QED readout is the use of a one-dimensional coplanar waveguide resonator

as a cavity, which is discussed in detail in sections 3.1, 5.1.4, and 7.1. The coplanar waveguide

(transmission line) can be thought of as a two-dimensional version of a coaxial cable for television,


-----


CHAPTER 1. INTRODUCTION 31

![SchusterThesis.pdf-33-2.png](SchusterThesis.pdf-33-2.png)

![SchusterThesis.pdf-33-0.png](SchusterThesis.pdf-33-0.png)

![SchusterThesis.pdf-33-1.png](SchusterThesis.pdf-33-1.png)

![SchusterThesis.pdf-33-3.png](SchusterThesis.pdf-33-3.png)

![SchusterThesis.pdf-33-4.png](SchusterThesis.pdf-33-4.png)

inside the cavity (beige) on the silicon substrate (green). The box consists of two aluminum islands
(blue) connected by a small tunnel junction (the overlap of the two fingers on the thin island).

which has a center-pin and a coaxial shield separated by an insulator (see Fig. 1.7). As anyone

who has tried to install cable knows, if there is a gap in the cable the signal is reflected, and if the

connection is almost but not quite right there can be interference, seen on the television as waves in

the picture. In a transmission line resonator, gaps in the center-pin at either end of the resonator

act as mirrors for the microwave photons inside. In TV, cable signals can only travel the line a few

times before being absorbed as heat, but in a superconducting transmission line, there are almost

no losses and the gaps can be designed to cause anywhere from a few hundred to nearly a million

reflections before allowing the photons to escape. This shows that the losses in the superconductor

are so low that a microwave photon can travel tens of kilometers (10 6 cm = 10 km) without being

absorbed. Thus the CPW transmission lines act much like optical fibers do for visible photons.

Microwave resonators have long been used as filters to block all but a narrow band of frequencies.

This filtering is the circuit analogy to the suppression of spontaneous decay in atomic cavity QED,

and it helps protect the qubit from undesired environmental noise. One of the reasons it is so difficult

to maintain coherence in circuits is that with many wires and other circuits around it is difficult


-----


CHAPTER 1. INTRODUCTION 32

to control the environment seen by the qubit. The transmission line resonator has a very simple

geometry making it an environment that is relatively easy to model and control. The simplicity of

the environment, though not glamorous, is one of the most important aspects of this architecture.

Cavity QED offers many benefits to quantum circuits, but circuit QED also contributes to

traditional cavity quantum electrodynamics. Quantum circuits are fabricated on a microchip using

conventional lithography techniques, eventually allowing complex integrated quantum circuits to

be manufactured. Unlike natural atoms, the properties of artificial atoms made from circuits can

be designed to taste, and even manipulated in-situ. However, with this flexibility comes more

channels for decoherence. Because the qubit contains many atoms, the effective dipole moment

can be 10,000 times larger than an ordinary alkali atom and 10 times larger than even a Rydberg

atom! This allows circuits to couple much more strongly to the cavity. Further, in atomic cavity

QED the three dimensional cavities must be a minimum of one wavelength in each dimension.

In our one-dimensional transmission line cavity (see Figs. 1.7 and 1.8), the other two dimensions

have been compressed to much less than a wavelength, increasing the energy density by 1,000,000

over 3D microwave cavities (see Fig. 1.3a), and further increasing the dipole coupling by 1,000.

This large coherent coupling allows circuits to achieve strong coupling even in the presence of the

larger decoherence present in the solid state environment. In both cases, the strength of coherent

interactions is larger than the rates of decoherence, allowing one to observe the quantum interactions

of matter with single photons. Because circuits arrive at this end by such different means (exceptional

coupling strength and moderate coherence) than atoms (using exceptional coherence and moderate

coupling) circuit QED can explore new regimes of cavity QED.

####### 1.5 ####### Thesis Overview

The dissertation first puts the experiment on firm theoretical footing. Chapter 2 gives a theoretical

review of cavity QED, exploring the Jaynes-Cummings Hamiltonian, wavefunctions, and lifetime of

excited states. We explore resonant and dispersive regimes of cavity QED, introducing new regimes

exploiting the strength of the dipole coupling we can attain in circuit QED. Chapter 3 discusses

how to realize cavity QED with superconducting circuits. The focus in this section is to connect

electrical engineering intuition of classical circuits with a second quantization based quantum optics

approach. The cavity, Cooper pair box, and coupling between them are discussed in both languages

and compared with traditional cavity QED implementations. Chapter 4 analyzes decoherence pro-


-----


CHAPTER 1. INTRODUCTION 33

cesses in the Cooper pair box, with a focus on how the CPB can be made robust against each type

of noise. As a result of this type of analysis a new derivative of the CPB called the transmon is

introduced that has very promising characteristics. Next, in chapter 5, the design and fabrication

of the cavities and qubits is discussed. This section is meant to be a design guide, by which one can

realize the desired parameters in a physical circuit. The appendices associated with these chapters,

while not necessary for understanding, present some more involved derivations and perhaps most

importantly provide a convenient formulary for circuit QED. The measurements are performed at

gigahertz frequencies at one-hundredth of a degree above absolute zero, requiring demanding mi-

crowave and cryogenic engineering. The cryogenic and microwave engineering techniques used in

these experiments are explained in chapter 6. The data begins to flow in chapter 7 where the cavities

and circuit QED system are experimentally characterized, with a focus on how to find ones way in

a rather large parameter space. The rest of the results are divided into two general classes of exper-

iments focusing on spectroscopic and time domain results respectively. In Chapter 8 spectroscopic

experiments observe the vacuum Rabi splitting, emphatically demonstrating that these circuit QED

experiments reach the strong coupling limit. Spectroscopy in the dispersive limit shows the ac Stark

effect, where the transition frequency of the qubit is shifted proportional to the number of photons in

the cavity. Further experiments take this one step further making the dispersive coupling so strong

that the qubit absorption spectrum splits into photon-number peaks, the first demonstration of the

strong dispersive coupling regime. Chapter 9 then studies time resolved measurements performing

detection and manipulation of the qubit state. While spectroscopic measurements are well suited to

study the static energy spectrum of the system, time domain measurements are particularly adept

at observing the dynamics of a single qubit or photon. In this section we realize the first high visi-

bility measurement of a superconducting qubit, and study the fidelity of single-shot readout. Using

the cavity-qubit coupling we are also able to map the qubit state onto a single photon, creating an

on-demand single photon source. This thesis work was not a single experiment, but the creation of

a platform for studying cavity QED and quantum information in a new way. Chapter 10 discusses

a few possible directions for further experiments.


-----


### Chapter 2

## Cavity Quantum Electrodynamics

A prototype system for studying the interaction between matter and light is a two-level atom,

interacting via a dipole coupling with a cavity, described by a harmonic oscillator whose excitations

are photons (see Fig. 2.1). The coherent behavior of this coupled system is described by the Jaynes-

Cummings Hamiltonian [Walls2006]:


H JC =   r ( a  a + 1 / 2) +   a  z +  g ( a    + a + ) (2.1)

![SchusterThesis.pdf-36-0.png](SchusterThesis.pdf-36-0.png)

2

where the first term represents the energy of the electromagnetic field, where each photon contains an

energy,   r . The second term represents the atom as a spin-1/2, with transition energy   a , and will

be henceforth referred to as a spin, qubit, atom, or simply two level system. Finally, the third term

describes a dipole interaction 1 where an atom can absorb (  + a ) and emit ( a    ) a photon from/to

the field at rate g . There are many systems besides atoms and photons which can be represented by

this Hamiltonian, circuits [Wallraff2004], quantum dots [Reithmaier2004, Yoshie2004], and nanome-

chanical [Irish2003] systems, with the values of these parameters arising from the specific physics of

the system. Chapter 3 contains a derivation of these parameters and typical approximations made

in using the Jaynes-Cummings Hamiltonian to describe superconducting circuits. While specific to

superconducting circuits, the techniques are general and could be applied to any physical system

which couples Bosonic (harmonic oscillator) and Fermionic (two level system) degrees of freedom.

In addition to the coherent behavior described by the Jaynes-Cummings Hamiltonian, there are

also incoherent phenomena that obscure the evolution of the coupled system(see Fig. 2.1). Any

![SchusterThesis.pdf-36-1.png](SchusterThesis.pdf-36-1.png)

1 The dipole interaction term is the result of a rotating wave approximation, valid in all experiments performed
here and discussed in more depth in section 3.3.

34


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 35

from quantum optics group at CalTech

|Col1|Col2||
|---|---|---|


![SchusterThesis.pdf-37-0.png](SchusterThesis.pdf-37-0.png)

transit

![SchusterThesis.pdf-37-1.png](SchusterThesis.pdf-37-1.png)

Figure 2.1: A two level atom interacts with the field inside of a high finesse cavity. The atom
coherently interacts with the cavity at a rate, g . Also present are decoherence processes that allow
the photon to decay at rate  , the atom to decay at rate  into modes not trapped by the cavity,

and the rate at which the atom leaves the cavity, 1 /T . To reach the strong coupling limit the
interaction strength must larger than the rates of decoherence g > ,   , 1 /T transit .

leakage or absorption by the cavity results in a photon decay rate,  , sometimes expressed in terms

of the quality factor Q =  r / . Often, and particularly in circuit QED,  is set by the desired

transparency of the mirrors to allow some light to be transmitted to a detector as a means of

probing the dynamics of the system. In the absence of other decay mechanisms, the radiative decay

of the atom can be completely described in terms of the coherent interaction with the cavity and

decay of cavity photons (which are measured). This very well modeled (and often slow) decay makes

cavity QED a good test-bed for studying quantum measurement and open systems [Mabuchi2002].

In practice, the atom may also decay at rate,  , into non-radiative channels or radiative modes


not captured by the cavity. Finally in atomic implementations, the atoms have a finite lifetime or

transit time T transit , before exiting the cavity.

The competition between coherent and incoherent processes is most evident when the atom is

resonant with the cavity, and the two systems can freely exchange energy. In the absence of decay, an

excitation placed in the system will coherently oscillate between an atomic excitation and a photon

in the cavity. This is often called a vacuum Rabi oscillation because it can be interpreted as vacuum

fluctuations which stimulate photon emission and absorption by the atom to and from the cavity.

When many oscillations can be completed before the atom decays or the photon is lost, the system

reaches the strong coupling limit of cavity QED ( g >   , , 1 /T transit ).


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 36

 a =  r  a -  r =  > g



|n 

|2 

|1 

|0 


|n

|3

|2

|1

|0


|n-1

|2 

|1 


|n+1

|n 

|2 


2g n

|2g 2|Col2|
|---|---|


![SchusterThesis.pdf-38-0.png](SchusterThesis.pdf-38-0.png)

|0


|1 


(  r -g 2 /  )




|0 

|Col1| r|
|---|---|


|Col1| r|
|---|---|


![SchusterThesis.pdf-38-1.png](SchusterThesis.pdf-38-1.png)

![SchusterThesis.pdf-38-2.png](SchusterThesis.pdf-38-2.png)

|g  |e  |g  |e 


|0 


Figure 2.2: Energy level diagrams of the Jaynes-Cummings Hamiltonian 1 . The dashed lines are
the eigenstates of the uncoupled Hamiltonian, where left is qubit in the | g  state and right in the | e 
state, and | n  corresponding to the photon number. The solid lines are the energies in the presence
of the dipole coupling. a. When the uncoupled qubit and resonator are resonant (  a  r g )
 
the levels split forming new eigenstates that have both photon and qubit character. These levels
are split proportional to the dipole coupling strength, and to the square root of the number of
excitations, 2 g  n , making the system very anharmonic. b. The energy levels in the dispersive limit

![SchusterThesis.pdf-38-3.png](SchusterThesis.pdf-38-3.png)
(  a  r g ) of the Jaynes-Cummings Hamiltonian. The effective cavity frequency is the difference
  2
between successive number states,  r   r g / depending on the atom state. The effective atom
frequency is  a   a (2 n + 1) g 2 / , where   n is the number of photons in the cavity.

 

Another way to see the significance of the strong coupling limit is to look at the energy levels

of the joint system. When the cavity and atom frequencies are degenerate, photon number states,

| n  , and atom ground and excited states denoted by | g  and | e  , are no longer eigenstates of the

full Hamiltonian (Eq. 2.1). The eigenstates must also diagonalize the interaction term, which (for

exact resonance) is accomplished by superpositions of atom states and cavity states of the form,


![SchusterThesis.pdf-38-4.png](SchusterThesis.pdf-38-4.png)

 = ( g n e n 1 ) /
|   | |  | |  


2. The energies of these new states are split by 2 g  n (see Fig. 2.2a).


![SchusterThesis.pdf-38-5.png](SchusterThesis.pdf-38-5.png)

The finite lifetime due to decay or dephasing manifests itself by giving the energy levels a finite

width. When the width of the levels becomes so great that the splitting is obscured, it means

that the atom/photon decays before a single oscillation is complete. When in the strong coupling

limit (i.e. the levels are resolved), the atom-cavity system becomes anharmonic even for a single

photon, allowing creation of photon number states, squeezed states, and other quantum optics

phenomena [Birnbaum2005].

One should not get the idea that once in the strong coupling limit decoherence is unimportant.

On the contrary, strong coupling cavity QED can be used to study decoherence. Decoherence

is often the bane of experimental attempts to observe naked quantum effects, but it is also the

source of irreversibility and entropy in an otherwise unitary world. Decoherence literally moves the


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 37

universe forward! A canonical example of an irreversible process, cooling of trapped atoms relies on

spontaneous decay to break the symmetry between heating and cooling. Long decay times associated

with atomic microwave transitions, while good for coherence, make it difficult to cool and trap such

atoms based on their microwave transitions. Because excitations are equally shared between atoms

and the cavity, they decay at the average of the two rates,  eff = (  +  ) / 2. When   the
 

cavity speeds up the atom decay, allowing faster extraction of energy. Future experiments might

couple circuit based cavities to increase the cooling efficiency of atom trapping/cooling. In fact, this

particular trick known as the Purcell effect [Purcell1946] works even if g <  , where the effective

decay rate becomes  eff = g 2 / . In addition, the Purcell effect allows one to redirect decay from

lossy internal modes (  ) to controlled radiative modes (  ), a property sometimes used to enhance


the emission of LEDs [Boroditsky1999].

Exercise 2.0.1. Using degenerate perturbation theory find the eigenstates and energies for the res-

onant (  a =  r ) Jaynes-Cummings Hamiltonian in Eq. 2.1.

Exercise 2.0.2. Derive the Purcell effect, by calculating the overlap of the cavity and qubit wave-

functions. Does the decay depend on the photon number? Why or why not?

####### 2.1 ####### Dispersive Limit

In the resonant limit (  a  r g ), the atom and photon can exchange energy causing them to lose
 

their individual character, and forming a strongly coupled system. In many cases it is preferable for

the interaction to be dispersive, where no actual photons are absorbed by the atom. This can be

achieved by detuning the atom and cavity by =  a   r where g  . In this dispersive limit,

the effect of the dipole interaction can be modeled using (non-degenerate) perturbation theory (see

Ex. 2.1.1)). Expanding in powers of g/ to second order yields the approximate Hamiltonian:


a  a + 1 / 2 +   a  z / 2 (2.2)
 



g 2
H   r + 
 



g 2
H   r +
 


![SchusterThesis.pdf-39-0.png](SchusterThesis.pdf-39-0.png)

The atom and cavity still interact through the dispersive shift term proportional to g 2 / . Because


it commutes with the rest of the Hamiltonian it conserves both the photon number and the atom

state, but shifts the energies of both the atom and the photons (see Fig. 2.2b). The first term

remains the Hamiltonian of a harmonic oscillator, but the effective frequency  r  =  r g 2 / ,



depends on the state of atom (see Fig 2.2b). This atom state dependent cavity shift can be used to


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 38



 r -4g

 r -2g

 r

 r -2g

 r -4g


|e  |0  2 phobit   |e  |0  |e  |0


![SchusterThesis.pdf-40-0.png](SchusterThesis.pdf-40-0.png)

![SchusterThesis.pdf-40-1.png](SchusterThesis.pdf-40-1.png)

4g 2g 0 2g 4g

Detuning, 


-10g -5g 0 5g 10g

detuning, 


Figure 2.3: a. A plot of the avoided crossing in the transition frequency between the ground
state in the one excitation manifold. The dashed lines show the uncoupled resonator frequency,  r

![SchusterThesis.pdf-40-2.png](SchusterThesis.pdf-40-2.png)
(black) and qubit frequency,  a (green). The solid red and blue lines show the energy for the + , 1

![SchusterThesis.pdf-40-3.png](SchusterThesis.pdf-40-3.png)

and , 1 states as a function of detuning. At large detunings these energies and the associated
  
eigenstates approach that of the uncoupled system. When  0 the photon and qubit become 
  
entangled forming phobit and quton states.  b. Indirect decay rates   and  


Figure 2.3: a. A plot of the avoided crossing in the transition frequency between the ground
state in the one excitation manifold. The dashed lines show the uncoupled resonator frequency,  r
(black) and qubit frequency,  a (green). The solid red and blue lines show the energy for the + , 1

and , 1 states as a function of detuning. At large detunings these energies and the associated
  
eigenstates approach that of the uncoupled system. When  0 the photon and qubit become 


perform a Quantum Non-Demolition (QND) measurement of the atom state. QND measurements

are important because they project the atom into the state they measure, allowing a measurement

to be repeated to improve its fidelity and results in squeezing [Caves1980]. This type of QND

measurement is discussed in depth in section 3.4.

The interaction can also be rewritten to highlight the interactions effect on the atom instead

writing the Hamiltonian in Eq. 2.2 as




H   r a  a + 1 / 2 +
 2



2 g 2
 a + a  a + g

![SchusterThesis.pdf-40-5.png](SchusterThesis.pdf-40-5.png)

![SchusterThesis.pdf-40-6.png](SchusterThesis.pdf-40-6.png)

 



2 g 2
 a +


 z (2.3)


![SchusterThesis.pdf-40-4.png](SchusterThesis.pdf-40-4.png)

In this grouping, one can see that the interaction gives the atom frequency a light shift consisting

of a photon number-dependent Stark shift (2 ng 2 / ) and vacuum noise induced Lamb shift

( g 2 / ). Physically when the atom state is changed it must electrically compress (or expand) the

photons wavelength, increasing (or decreasing) the frequency of each photon in the cavity, which

will require extra energy (  g 2 / ). The atom-photon symmetry of the dispersive interaction is a

manifestation of the Heisenberg uncertainty principle required backaction. It means that photons

which are used to measure the state of the atom will also modify its frequency. This quantum Stark

Hamiltonian is special because the interaction can also perform a QND measurement on the photon

number. Experiments measuring photon number and measurement induced dephasing are the topics

of sections 8.2 and 8.3.

Because the Jaynes-Cummings Hamiltonian connects only states with the same number of excita-


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 39

tions, it is relatively straightforward to go beyond perturbation theory diagonalizing the Hamiltonian

exactly, to calculate the energy levels and eigenstates (see appendix B). A plot of the transition

frequency between the ground state and one excitation manifold based on these calculations is shown

in figure 2.3. The energies are:




E ,n =  n r
  2


![SchusterThesis.pdf-41-1.png](SchusterThesis.pdf-41-1.png)

4 ng 2 +  2 (2.4)

  

E g, 0 =
 2


![SchusterThesis.pdf-41-0.png](SchusterThesis.pdf-41-0.png)

![SchusterThesis.pdf-41-2.png](SchusterThesis.pdf-41-2.png)

Where the n used in Eq. 2.4 is the total number of excitations 1 in the system not the number of

photons and  refer to the higher energy or lower energy state in the n excitation manifold not the

atom state. Well into the dispersive limit, one can Taylor expand the square root in eq. 2.4 in the

small dispersive energy shift, n ( g/ ) 2 , yielding




E  ,n   n r  + 2 ng 2 /  (2.5)
 

![SchusterThesis.pdf-41-3.png](SchusterThesis.pdf-41-3.png)

The coupling effectively scales with the number of excitations, so for a given detuning there is a

critical number of excitations, n crit , which will make the dispersive limit break down (and the Taylor

expansion diverge).



 2
n crit = 4 g 2 (2.6)

![SchusterThesis.pdf-41-4.png](SchusterThesis.pdf-41-4.png)

While n crit sets an upper limit on the number of photons in the dispersive limit, a more quantitative

measure of dispersiveness is the orthogonality of the wavefunctions. The eigenstates can be expressed

as:

, n = cos  n g, n sin  n e, n 1 (2.7)
|  |  |  


![SchusterThesis.pdf-41-5.png](SchusterThesis.pdf-41-5.png)

+ , n = sin  n g, n + cos  n e, n 1
|  |  |  


![SchusterThesis.pdf-41-6.png](SchusterThesis.pdf-41-6.png)


1 2 g  n

![SchusterThesis.pdf-41-8.png](SchusterThesis.pdf-41-8.png)

2 arctan 




1
 n =


(2.8)


![SchusterThesis.pdf-41-7.png](SchusterThesis.pdf-41-7.png)

![SchusterThesis.pdf-41-9.png](SchusterThesis.pdf-41-9.png)

If the system is well into the dispersive limit, then these can be approximated by (or computed

directly using perturbation theory)

![SchusterThesis.pdf-41-10.png](SchusterThesis.pdf-41-10.png)

1 This also differs slightly from the convention in [Blais2004]. My n is his n + 1 so that n = 1 is one excitation.


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 40


| , n  = | g, n  g  n/  | e, n  1  (2.9)
 

![SchusterThesis.pdf-42-1.png](SchusterThesis.pdf-42-1.png)

![SchusterThesis.pdf-42-0.png](SchusterThesis.pdf-42-0.png)

| + , n  = g  n/  | g, n  + | e, n  1 
 

![SchusterThesis.pdf-42-3.png](SchusterThesis.pdf-42-3.png)

![SchusterThesis.pdf-42-2.png](SchusterThesis.pdf-42-2.png)

(2.10)

In the presence of a dispersive coupling (when  > 0), the | most resemble qubit states, but

![SchusterThesis.pdf-42-4.png](SchusterThesis.pdf-42-4.png)

they also have some photon component. This overlap can be interpreted to mean that the qubit

excitation lives some of the time as a photon in the cavity. If multiple qubits are strongly coupled

to the same cavity the photonic part of their wavefunctions can overlap, creating an entanglement

bus. The atoms or qubits could be centimeters apart creating a non-local gate. The photonic aspect

of the qubit also gives a new decay means that the qubit has some probability to decay as a photon

emitted from the cavity, which occurs at a rate   . Similarly photons live partly as qubit excitations

and so can be emitted by the qubit into non-radiative modes at a rate   . These rates are derived

in appendix B. Well into the dispersive limit they are given by


g
 

 g

![SchusterThesis.pdf-42-5.png](SchusterThesis.pdf-42-5.png)

 




2
 (2.11)
 2

 (2.12)



2
 (2.11)
 2


![SchusterThesis.pdf-42-6.png](SchusterThesis.pdf-42-6.png)

Were an atom coupled to an infinite transmission line, it would radiatively decay at a rate g 2 / .

The atom inside the cavity decays at rate g 2 / , which can be over 100,000 (Q) times slower than

an atom coupled to a continuum bath! Thus, even atoms/qubits very strongly coupled to the cavity,

the effective decay rates from these indirect radiative processes are very favorable for quantum

computation [Blais2004] and the study of cavity QED, but often non-radiative sources of decay (  )


will begin to dominate before the limit set by suppressed radiative decay. By eliminating radiative

sources of decay, we can begin to understand these non-radiative sources more quantitatively.

Exercise 2.1.1. Derive the dispersive JC Hamiltonian to second order in g/  using the Baker-

Haussdorf Lemma [Sakurai1994] to find a unitary transformation of the form

U = exp i (  + a +   a    )
 

for which the transformed Hamiltonian UHU  gives Eq. 2.2 to second order in g/  . If you prefer


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 41

(i.e. dislike the BH Lemma) you may expand the exponential to the appropriate order and compute

the Hamiltonian directly to the requested order in g/  .

Exercise 2.1.2. Applying the unitary transformation found in exercise 2.1.1 instead to the wave-

functions, find the eigenstates of the dispersive Hamiltonian to first order in g/  . Show that these

agree with the exact eigenstates first order.

Exercise 2.1.3. Apply (to first order) the unitary transformation found in exercise 2.1.1 to the

photon annihilation operator UaU  . What does this say about the radiative decay of the qubit?

Exercise 2.1.4. Using Fermis Golden Rule find the decay rate of a qubit-like excitation in the

dispersive Jaynes-Cummings Hamiltonian with a decay Hamiltonian H  =   b  a + a  b . The

solution can be found in appendix B. b. Along similar lines derive the rate of photon loss through  

![SchusterThesis.pdf-43-0.png](SchusterThesis.pdf-43-0.png)

the atom decay channel.

Exercise 2.1.5. a. Derive the energy levels of Eq. 2.4 by diagonalizing the n-excitation manifold

exactly. See appendix B for solution. b. By taking appropriate energy differences to second order

find the cavity, Stark, and Lamb shifts.

Exercise 2.1.6. The 1/2 in the harmonic oscillator Hamiltonian H =   r ( a  a + 1 / 2) is often

neglected as it appears to be a constant offset which can be eliminated by appropriate gauge choice.

The Lamb shift arises from this 1/2 term. Using CQED, design an experiment to measure the Lamb

shift.

####### 2.2 ####### Strong Dispersive Interactions

In the previous section, nothing was mentioned about the strength of the coupling relative to decay,

the only constraint was that ng/   1 (outside of blue region in Fig. 2.4). In fact in the dispersive

limit the old definition of strong coupling, that the rate of atom-photon oscillations were faster than

decay, contradicts the notion of dispersiveness, that no (very little) mixing occurs between atom and

photon. Instead one can compare the manifestation of the dipole coupling, the dispersive frequency

shifts, to the decay rates. To access the strong dispersive regime one must have  = g 2 /  > , 

(white region in Fig. 2.4). The hallmark of this type of strong coupling is that the qubit spectrum

resolves into individual photon number peaks. Also above this threshold, the cavity shift is larger

than the cavity linewidth, splitting the cavity, based on the state of the atom (see Fig. 2.5). When


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 42

40


30

20

10


![SchusterThesis.pdf-44-0.png](SchusterThesis.pdf-44-0.png)

0 100 200 300 400 500

 / 

Figure 2.4: A phase diagram for cavity QED. The parameter space is described by the atom-photon
coupling strength, g , and the detuning, , between the atom and cavity frequencies, normalized
to the rates of decay represented by  = max [ , , 1 /T ]. Different cavity QED systems, including
Rydberg atoms, alkali atoms, quantum dots, and circuit QED, are represented by dashed horizontal
lines. In the blue region the qubit and cavity are resonant, and undergo vacuum Rabi oscillations.
In the red, weak dispersive, region the ac Stark shift g 2 /  <  is too small to dispersively resolve
individual photons, but a QND measurement of the qubit can still be realized by using many photons.
In the white region, quantum non-demolition measurements are in principle possible with demolition
less than 1%, allowing 100 repeated measurements. In the green region single photon resolution is
possible but measurements of either the qubit or cavity occupation cause larger demolition. In the
yellow region the cavity becomes anharmonic, allowing it to create squeezed states and inherit some
inhomogeneous broadening, and the Stark shift becomes non-linear.


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 43

   2  + 

|  r a  g|Col2|Col3|
|---|---|---|
|e  g 0 2 4 r r r a a a 1 3 5   a a a|||
||||



Figure 2.5: Spectrum of coupled cavity and atom system in strong dispersive limit. (left) Cavity
spectrum when atom is in ground (blue), excited (red) state or not present (dashed black). (right)
Atom spectrum when cavity has different (exact) photon numbers.

measuring the state of a single atom using the cavity, one has the luxury of using many photons

to compensate for a small dispersive shift  <  , even in the weak dispersive limit (pink region in

Fig. 2.4). Because there is only a single atom in the cavity, single photon precision requires dispersive

strong coupling.

Perhaps even more interesting is when the Stark shift per photon exceeds the atom decay (  >

 ). In this case the atom is shifted by more than a linewidth for each photon, only responding

when driven at a given frequency when a specific number of photons are present in the cavity. By

probing the response of the atom at different frequencies one can measure the exact photon number

distribution (see section 8.3). The qubit can not only measure the photon number but be coherently

controlled by it. If the qubit is made only to respond when a single photon is present this can be

considered a conditional-not (CNOT) gate. If multiple atoms in the cavity (which might be far

apart from each other) perform a CNOT on the same photon state they can be entangled without

ever interacting directly.

In the weak dispersive limit (red region in Fig. 2.4), the cavity, though its frequency became atom

state-dependent, remained harmonic at photon numbers below n crit . If the coupling becomes strong

enough, even in the dispersive limit well below n crit (where perturbation theory is still accurate)

higher order terms in the expansion of equations 2.4 and 2.7 can become significant compared with

the cavity linewidth. A new critical photon number can be defined for when the 4 th order shift

( n 2 / ), changes the resonator frequency by more than a linewidth per photon.


-----


CHAPTER 2. CAVITY QUANTUM ELECTRODYNAMICS 44



 
n  =



    3

 2 = g 4


(2.13)

![SchusterThesis.pdf-46-1.png](SchusterThesis.pdf-46-1.png)
g 4


![SchusterThesis.pdf-46-0.png](SchusterThesis.pdf-46-0.png)

While the wavefunction overlap between atom and cavity is small in absolute terms (( g/ )  1),

the coupling can be large enough ( g   ) for the cavity to inherit a significant non-linearity. Note

that the qubit remains mostly in the ground state. Depending on how the cavity is being used, this

could be a blessing or a curse. If linearity is desired, then it is not sufficient to stay below n crit , one

must also keep the number of photons to be much less than n  . However, an anharmonic oscillator

can also be an extremely useful device. It can be used to squeeze light (in a less extreme way than

in the resonant case), or as a hysteretic latching measurement of another atom [Siddiqi2006].

If the coupling is stronger still, it is even possible to have n  < 1 (the orange line in Fig. 2.4).

In this limit, the cavity becomes anharmonic on the single photon level, acting more like a many

level atom than a harmonic oscillator. As such it can also be used as a photonic qubit which is

discussed briefly in section 8.3.2.

Cavity QED can be used to explore a wide variety interaction types and decoherence effects. All

of these regimes have useful properties for quantum information. The resonant interaction between

an atom and a single photon can be used to transport quantum information. The dispersive shifts can

be used to measure the photon number or qubit state, while the radiative lifetime enhancement can

be used to protect it from decoherence. In the strong dispersive regime, one can use the dispersive

shifts to measure photons, creating and characterizing exotic states of light, which could be used

for communication of quantum information or to be studied in their own right. It might even be

possible to make fundamentally new quantum bits based on the non-linearities present in cavity

QED. As the phase diagram in figure 2.4 and as chapter 3 will show, superconducting circuits can

be made into an excellent CQED system, exhibiting a wealth of interesting physics.


-----


### Chapter 3

## Cavity QED with Superconducting Circuits

This chapter describes the process of building a cavity QED system out of circuits. A special

emphasis is placed on connecting the languages of microwave engineering to that of quantum optics.

First, each component is described in classical circuit terms. Because the energy scales of these

circuits ( E/   5 GHz) correspond to temperatures of  250 mK and the experimental temperature

is 20 mK ( k B T 400 MHz) the circuits are quantized to understand their full behavior. Special
 

attention is paid to the conditions under which it is valid to approximate the quantum circuits, a

coplanar waveguide resonator and Cooper pair box, to a single mode harmonic oscillator and two

level atom. With these approximations in mind, we can then describe these circuits in the language

of quantum optics. Dissipation can mask any coherent quantum effects so attention is given to

decoherence, with several sections describing engineering of the cavity decay and all of chapter 4

devoted to describing various decoherence mechanisms in the CPB.

####### 3.1 ####### Transmission Line Cavities

In cavity QED, the cavity creates a single harmonic mode 1 , which couples to the qubit state. In

the microwave domain, a cavity can be realized using electrical circuits. In order to observe the

quantum properties of a cavity it should have a high quality factor so that each energy state lives for

a long time. This is important both so that its discreteness can be resolved and so that the cavity

does not contribute decay to any qubits which are coupled to it.

![SchusterThesis.pdf-47-0.png](SchusterThesis.pdf-47-0.png)

1 The cavity actually creates an infinite number of discrete modes spaced by  r , but there is only one near the
atom frequency.

45


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 46

######### a) ######### b) ######### 1


0.5

0

 0.5

 1

![SchusterThesis.pdf-48-0.png](SchusterThesis.pdf-48-0.png)

 10  5 0 5 10

/


#########  ######### =LI

|++|++|
|---|---|
|||
|||
|||

|++ C - -|++ R - -|
|---|---|

|. I = -q ++ C - -|V q=C V ++ R - -|
|---|---|


Figure 3.1: a. A parallel LCR circuit can be described in terms of the canonical variables, q = CV ,
the charge on the capacitor, and  = LI , the magnetic flux in the inductor. They are linked by
Lenzs law and the fact that the current draws charge from the capacitor. b. Plot of real (solid)
and imaginary (dashed) parts of the impedance Z (  ) of an LCR circuit (Eq. 3.3). The frequency
is normalized to the full width at half max and the impedance is normalized to the resistance at
resonance.

First, we will analyze the LCR oscillator, a simple lumped element circuit which realizes a

harmonic oscillator Hamiltonian. However, at microwave frequencies, it is difficult to realize a true

lumped element circuit. This is because to measure the lumped element we must attach wires which

extend more than a wavelength, and so there is almost invariably at least one large dimension.

Therefore it is much easier to make a 1D oscillator, a transmission line cavity, which can be modeled

as a series of LCR circuits. We will then discuss coupling these resonant circuits to the input and

output transmission lines. After gaining a classical intuition for these circuits, we can quantize the

LCR circuit connecting our basic intuition from electrical engineering to fully quantum mechanical

notions of decoherence and measurement.

######### 3.1.1 ######### The LCR Oscillator

The equation of motion for the amount of charge on the capacitor (from currents summing to zero

and voltages all equal) in a parallel LCR oscillator can be written


d 2 q

![SchusterThesis.pdf-48-1.png](SchusterThesis.pdf-48-1.png)

dt 2




1 dq

+

![SchusterThesis.pdf-48-2.png](SchusterThesis.pdf-48-2.png)

![SchusterThesis.pdf-48-3.png](SchusterThesis.pdf-48-3.png)

RC dt


1 dq

RC dt



= 0 (3.1)

![SchusterThesis.pdf-48-4.png](SchusterThesis.pdf-48-4.png)
LC


The solution to this differential equation is




q ( t ) = q 0 exp i (  0 + i 2 ) t +  (3.2)


![SchusterThesis.pdf-48-5.png](SchusterThesis.pdf-48-5.png)

![SchusterThesis.pdf-48-6.png](SchusterThesis.pdf-48-6.png)

which describes a charge oscillation with frequency  0 = 1 /


LC and decay rate  = 2 /RC . In


the frequency domain the circuit can be described by its impedance Z (  ) or its admittance Y (  ) =


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 47

1 /Z (  ). For a parallel LCR oscillator the impedance is given by


1 + 1

![SchusterThesis.pdf-49-0.png](SchusterThesis.pdf-49-0.png)

![SchusterThesis.pdf-49-1.png](SchusterThesis.pdf-49-1.png)

jL


 1
(3.3)



Z LCR (  ) = jC +


The imaginary 1 part of this impedance will be zero at the resonance frequency  0 = 1 /


![SchusterThesis.pdf-49-2.png](SchusterThesis.pdf-49-2.png)

LC . Near


resonance, this expression can be expanded to first order in  =   0 , allowing the approximation


 2  0 2 2  (   0 ), and yielding
  


resonance, this expression can be expanded to first order in  =   0 , allowing the approximation



Z LCR (  ) =


(3.4)

![SchusterThesis.pdf-49-3.png](SchusterThesis.pdf-49-3.png)
1 + 2 jQ/ 0


where the quality factor is Q =  0 RC =  0 / . The quality factor is dimensionless and can be

thought of as the number of oscillations in a cavity decay time 2 / = RC , before the system comes

to equilibrium. Large resistance results in high Q, with the limit as R  giving the lossless

impedance


Z LC (  ) =


(3.5)

![SchusterThesis.pdf-49-4.png](SchusterThesis.pdf-49-4.png)
2 jC (   0 )



which now approaches infinity at  = 0. As with the differential equation one can use the lossless

expression with a complex frequency  0  =  0 (1 + j/ 2 Q ) to represent the decay.

######### 3.1.2 ######### Transmission Line as Series of LC Circuits

The microwave frequency regime is a particularly interesting slice of the electromagnetic spectrum

because its characteristic wavelength,  = c/f , occurs at human size scales of 100  m to 1 m. Because

the waves interfere constructively and destructively on these scales, the electrical response of a

structure becomes highly dependent on its geometry. In a microwave circuit both the topology and

the geometry are critical, which presents a challenge when engineering microwave circuits. It is well

worth facing this challenge, as the geometric dependence brings the opportunity to make fantastically

sharp resonances, and even to make a short act as an open! Here, a section of transmission line is

used to create an effective LCR resonator.

A quick review of transmission line resonators following [Pozar1990] chapters 2 and 3 is given. A

transmission line can be modeled as consisting of many small lumped elements that have the same

impedances (admittances) per unit length as the transmission line (see Fig. 3.2). The impedance of

one small section is


![SchusterThesis.pdf-49-5.png](SchusterThesis.pdf-49-5.png)

Z 0 =


R  + jL 
(3.6)

![SchusterThesis.pdf-49-6.png](SchusterThesis.pdf-49-6.png)
G  + jC 


![SchusterThesis.pdf-49-7.png](SchusterThesis.pdf-49-7.png)

1 In electrical engineering it is conventional to use exp( jt ) whereas quantum mechanics uses exp( it ) and j =  i .


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 48


a) b) c)




R l L l L 1 C 1 G 1


Z 0 , L

|C 1|Col2|
|---|---|

|C 2|Col2|
|---|---|

|Ll Rl Ll Rl|Col2|Col3|
|---|---|---|
|Cl Gl Cl Gl|||
|||Gl|

|L 1 L 2 L n|C G 1 1 C G 2 2 C G n n|Col3|
|---|---|---|
||C n||


![SchusterThesis.pdf-50-0.png](SchusterThesis.pdf-50-0.png)

Figure 3.2: The transmission line can be represented as an infinite series of Ls and Cs which have the correct inductance a. A transmission line with characteristic impedance Z 0 and length L. b.
( L ) and capacitance ( C ) per unit length, to give the transmission line characteristic impedance

![SchusterThesis.pdf-50-1.png](SchusterThesis.pdf-50-1.png)
Z 0 = L/C . c. This circuit can be transformed into a series of parallel LCR oscillators,

whose characteristic impedance is Z 0



and whose inductances/capacitances are given by the values in Eq. 3.13. It is interesting to note that model c incorrectly predicts the DC impedance (see
Fig. 3.3).

where R  , L  , G  , and C  are the resistance, inductance, conductance, and capacitance per unit

length of the transmission line. The R  can usually be associated with conductor loss, while the G 

can be thought of as leakage in the dielectric (see sec. 3.1.7). If the loss is small, the impedance


![SchusterThesis.pdf-50-2.png](SchusterThesis.pdf-50-2.png)

simplifies to Z 0 =


L  /C  . Signals on a transmission line propagate as waves with a complex


![SchusterThesis.pdf-50-3.png](SchusterThesis.pdf-50-3.png)

propagation coefficient  =


( R  + jL  )( G  + jC  ). The imaginary part of the propagation


coefficient (  = Im [  ]) describes the phase of the wave. For a given frequency  , this defines a phase


![SchusterThesis.pdf-50-4.png](SchusterThesis.pdf-50-4.png)

velocity v = / . If the line is nearly lossless, v 


1 /L  C  and the wavelength  = 2 / = 2 v/ .


The attenuation is described by the real part of the propagation constant

 = Re [  ]  R  /Z 0 + G  Z 0 (3.7)

The effective input impedance of an arbitrary load Z L , at a distance  , through a transmission line

of characteristic impedance Z 0 , is

Z L + Z 0 tanh 
Z in = Z 0 (3.8)

![SchusterThesis.pdf-50-5.png](SchusterThesis.pdf-50-5.png)
Z 0 + Z L tanh 

When the load impedance is an open or a short, this expression simplifies to

Z in short = Z 0 tanh  (3.9)

Z in open = Z 0 coth 


In this thesis, transmission lines terminated with high impedances (opens or nearly opens) are

usually used. With these boundary conditions there will be two types of resonance (see Fig. 3.3).

Whenever the length of line is an integer multiple of a half wavelength (  = n/ 2 = v/ 0 ), there


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 49

will be a high impedance resonance. Whenever the length is odd multiple of a quarter wavelength

(  = (2 n + 1) / 4), there will be a high admittance resonance. The input impedance will determine

which case applies, and for this thesis, we selected a near open, which selects the / 2 high impedance

resonances.


Z in open = Z 0 1 + tanh j tan  +  j tanh tan   (3.10)

![SchusterThesis.pdf-51-0.png](SchusterThesis.pdf-51-0.png)

Note that when  0 the impedance returns to the lossless case, Z in open j cot  , which will
 

have poles when   ( n + 1)  .

 = ( /v )( v/ / 2 ) =  ( n / 2 +  n ) / / 2 (3.11)

Expanding Z in open for small  n and  yields


Z in open = Z 0 /


![SchusterThesis.pdf-51-1.png](SchusterThesis.pdf-51-1.png)

n 

![SchusterThesis.pdf-51-2.png](SchusterThesis.pdf-51-2.png)

![SchusterThesis.pdf-51-3.png](SchusterThesis.pdf-51-3.png)

2  n
 


(3.12)


1 + 2 j 2 n



n /


This looks exactly like the impedance in Eq. 3.3 where


 n = n / 2 (3.13a)



n
Q n = R n /Z cn = (3.13b)

![SchusterThesis.pdf-51-4.png](SchusterThesis.pdf-51-4.png)

2 

R n = Z 0 / = R   (3.13c)


C n =



=

![SchusterThesis.pdf-51-5.png](SchusterThesis.pdf-51-5.png)
 n R


 = 1 C   (3.13d)

![SchusterThesis.pdf-51-6.png](SchusterThesis.pdf-51-6.png)

![SchusterThesis.pdf-51-7.png](SchusterThesis.pdf-51-7.png)

2 Z 0  / 2 2


L n =


1 2 Z 0

 n 2 C = n 2  / 2


1 2 Z 0

 n 2 C = n 2 


 2 n 2 L   (3.13e)


![SchusterThesis.pdf-51-8.png](SchusterThesis.pdf-51-8.png)

![SchusterThesis.pdf-51-9.png](SchusterThesis.pdf-51-9.png)

![SchusterThesis.pdf-51-10.png](SchusterThesis.pdf-51-10.png)

![SchusterThesis.pdf-51-11.png](SchusterThesis.pdf-51-11.png)

Z cn =



2 Z 0
L n /C n = (3.13f)

![SchusterThesis.pdf-51-12.png](SchusterThesis.pdf-51-12.png)

n



2 Z 0
L n /C n =


A comparison of the model in Fig. 3.2 using the effective LCR values in Eq. 3.13, is shown in

Fig. 3.3a. The agreement is quite close except for the DC behavior (see Fig. 3.3b). The error is

reduced to 1 /Q at about 10% of the fundamental frequency independent of Q , and the imaginary

part is suppressed much faster by  0 /Q . The agreement in both the real and imaginary parts gets

better at higher Q, contributing a negligible error due to the use of a single pole model.

######### 3.1.3 ######### Capacitively Coupled LCR Resonator

The previous subsection discusses a transmission line resonator with no coupling to the outside

world, a rather lonely circuit. One could directly connect the resonator to a transmission line, but


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 50


0.5

0

 0.5




 2


![SchusterThesis.pdf-52-0.png](SchusterThesis.pdf-52-0.png)

![SchusterThesis.pdf-52-1.png](SchusterThesis.pdf-52-1.png)

0 0.5 1 1.5

 /  0  /  0


0.5 1 1.5


Figure 3.3: Real and imaginary parts of the impedance of resonator formed terminating a transmission line with an open-circuit (green and purple) and model of LCR resonators (red and blue) a)
normalized to the attenuation (  ). b) Error in normalized impedance, ( Z TL Z LC ) / , in units

of 1 between the impedance predicted by the LCR model and exact impedance of an open terminated transmission line. As can easily be seen in /Q a , both the real and imaginary parts of the
impedance differ significantly between the transmission line and the simple LC model. The solid red
and dashed purple curves show the error in the real part of the impedance at Q  15 and Q  1500.
Note that while the frequency scale on which the error falls off is independent of the Q, the error in
the normalized impedance scales with 1 /Q (and the absolute impedance with 1 /Q 2 . The solid blue
and dashed green curves show the error in the imaginary part of the impedance. The error falls off,
does on scale proportional to 1 /Q , so that it becomes negligible (even measured in units of 1 /Q )
very quickly.

this would allow the radiation to escape too quickly by shunting the effective impedance to Z 0

and destroying the Q. A less invasive technique connects the resonator to a transmission line via a

small capacitor (see Fig. 3.4a). The large impedance mismatch the capacitor causes is analogous

to a dielectric mirror, since it is lossless and reflects most incident radiation, but transmits a small

amount. Through this mirror, photons can be added to the cavity or allowed to leak out. To see

how this coupling affects the resonator, it is convenient to transform the source impedance into its

Norton equivalent (see Fig. 3.4b). The effective admittance of this circuit is


jC in
Y in =


1 + jC jC in in Z 0 = jC 1 + in + q q 2 in 2 /Z


1 + q in 2 (3.14)


![SchusterThesis.pdf-52-2.png](SchusterThesis.pdf-52-2.png)

![SchusterThesis.pdf-52-3.png](SchusterThesis.pdf-52-3.png)

where q in = C in Z 0 is small when the C in  Z 0 . In this limit, one can approximately ignore the


denominator in Eq. 3.14 (1+ q in 2 1). Thus the effect of the coupling is to add an effective capacitance



C in , which will shift the resonance frequency, and an effective parallel resistance 1 /Re [ Y in ] = Z 0 /q in 2 ,

which will change the Q. The quality factor will be the ratio of the impedance on resonance to the


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 51


######### a) ######### Z ######### 0 ######### C ######### in ######### b) ######### Z ######### 0 ######### / q ######### in ######### 2 ######### C ######### in

|L|C|R|
|---|---|---|


|C|R|
|---|---|


|b) Z / q 2 C 0 in in I|Col2|
|---|---|
|||
|||


![SchusterThesis.pdf-53-0.png](SchusterThesis.pdf-53-0.png)

![SchusterThesis.pdf-53-1.png](SchusterThesis.pdf-53-1.png)

![SchusterThesis.pdf-53-2.png](SchusterThesis.pdf-53-2.png)

![SchusterThesis.pdf-53-3.png](SchusterThesis.pdf-53-3.png)

Figure 3.4: The capacitive coupling ( a ) to an environment of impedance Z 0 through a capacitor, C in ,
such that C in   Z 0 can be modeled by an effective circuit ( b ). The transformed input impedance,
seen by the oscillator, can be made much larger than the impedance of the environment.

characteristic impedance 1 Z res /Z 0 . If the internal resistance is negligible then 2


Z cn Re 1 [ Y in ] = 1 q in 2


Z 0 n

Z cn  2 q 2


Q ext =


Z 0


2 q in 2 (3.15)


![SchusterThesis.pdf-53-4.png](SchusterThesis.pdf-53-4.png)

![SchusterThesis.pdf-53-5.png](SchusterThesis.pdf-53-5.png)

![SchusterThesis.pdf-53-6.png](SchusterThesis.pdf-53-6.png)

![SchusterThesis.pdf-53-7.png](SchusterThesis.pdf-53-7.png)

If the internal resistance is significant compared to the loading then


![SchusterThesis.pdf-53-8.png](SchusterThesis.pdf-53-8.png)

![SchusterThesis.pdf-53-9.png](SchusterThesis.pdf-53-9.png)

![SchusterThesis.pdf-53-10.png](SchusterThesis.pdf-53-10.png)

Q L


Q ext


(3.16)
Q int


where Q int = R n /Z cn . This gives some insight on how coupling to the system gives an effective loss

(effectively loading the resonator), and how that can be engineered (by adding a large impedance in

series).

######### 3.1.4 ######### Capacitively Coupled Transmission Line Resonator

In the previous subsection we discussed a one-sided cavity, which could be measured in reflection,

however when measuring in this mode the important signal sits on top of a large background of

reflected power that contains no information. This is not in principle a limitation, but in practice

it is more convenient to use transmission of a two sided cavity where only the signal is present 3 ,

making it easier to analyze the signal. If the internal losses are negligible and Q  1, then the

transmission coefficient can be expressed as


T 0
S 21 =


 n (3.17)

![SchusterThesis.pdf-53-11.png](SchusterThesis.pdf-53-11.png)

![SchusterThesis.pdf-53-12.png](SchusterThesis.pdf-53-12.png)

(  in +  out ) / 2


1 j (  in +  



![SchusterThesis.pdf-53-13.png](SchusterThesis.pdf-53-13.png)

1 The characteristic impedance is Z c1 = L/C and need not be Z 0 but for all cases here the resonator has been

![SchusterThesis.pdf-53-14.png](SchusterThesis.pdf-53-14.png)

designed such that Z c = Z 0 .
2 Note that even though it appears that Q  increases at higher harmonics, q in =  n C in Z 0  n , so overall, for fixed
C in the quality factor is inversely proportional to n ( Q ext  1 /n ).
3 Control pulses applied to the atom are strongly detuned from the cavity and are heavily filtered by the cavity.


1 The characteristic impedance is Z c1 =


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 52

where


2
 in / out =

![SchusterThesis.pdf-54-0.png](SchusterThesis.pdf-54-0.png)






q in 2 / out  n (3.18)


  in  out

![SchusterThesis.pdf-54-1.png](SchusterThesis.pdf-54-1.png)
T 0 =


(3.19)

![SchusterThesis.pdf-54-2.png](SchusterThesis.pdf-54-2.png)
(  in +  out ) / 2


 n = n / 2 (1  ( q in + q out )) (3.20)

One can also measure the reflection of incident radiation which will be proportional to


 in
S 11 =


j n  1 (3.21)

![SchusterThesis.pdf-54-3.png](SchusterThesis.pdf-54-3.png)



 in +  out


![SchusterThesis.pdf-54-4.png](SchusterThesis.pdf-54-4.png)

Equation 3.17 describes transmission with a Lorentzian line shape, which looks much like the ex-

pression for the impedance of an LCR circuit (Eq. 3.3). Here the resonance frequency is shifted by

the extra capacitance contributed by the coupling capacitors (as in Eq. 3.14). The numerator of the

expression gives the peak transmission (when  n = 0). If the input/output coupling is symmetric

(  in =  out ) then the transmission will be unity ( T 0 = 1). If the resonator is asymmetric some of the

input power will be reflected, satisfying energy conservation. To be concrete, let the input capacitor

be smaller than the output. In equilibrium, the amount of power flowing out must equal the amount

coming in, but if the input capacitor is smaller, then the input rate will not be sufficient to maintain

the internal voltage, which is drained at a faster rate by the output, unless it is driven with a higher

input amplitude to compensate. Since there is no loss, the remaining input power must be reflected.

A similar argument holds for if the output is smaller.

The Q of the capacitively coupled transmission line resonator comes from the parallel combination

of the input and output Qs


 n
Q CCTL =


 n n

 in +  out = 2( q in 2 +


n 

![SchusterThesis.pdf-54-6.png](SchusterThesis.pdf-54-6.png)

![SchusterThesis.pdf-54-7.png](SchusterThesis.pdf-54-7.png)

2( q in 2 + q out 2 ) 2




n / 2 2 Z 0 2 ( C in 2 + C out 2 ) (3.22)


![SchusterThesis.pdf-54-5.png](SchusterThesis.pdf-54-5.png)

![SchusterThesis.pdf-54-8.png](SchusterThesis.pdf-54-8.png)

Note that the quality factor for the capacitively coupled resonator Q CCTL 1 /n . This can be


thought of as the result of a competition between the higher frequency and the increase in conductive

losses, which is proportional to the square of the frequency, resulting in overall decrease in Q at higher

harmonics.

Thus far, we have only discussed the magnitude of the transmitted signal. The complex trans-

mission coefficient of Eq. 3.17 indicates the signal will also acquire a phase shift,



 = arctan ( Im [ S 21 ] /Re [ S 21 ]) = arctan

![SchusterThesis.pdf-54-9.png](SchusterThesis.pdf-54-9.png)

/ 2




(3.23)


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 53

a) b) 1


Z


C in Z 0 , L /2 C out 0 _qin_ 2 + _qout_


![SchusterThesis.pdf-55-0.png](SchusterThesis.pdf-55-0.png)

q in =  C in Z 0 q out =  C out Z


0 0


 n n  /2


![SchusterThesis.pdf-55-1.png](SchusterThesis.pdf-55-1.png)

Figure 3.5: Transmission of asymmetric cavity near one of its resonances (  n ), using an exact
analytic calculation (solid red) and a lorentzian model (dashed blue). The lorentzian is a very good
approximation to the full transmission spectrum near resonance. The input and output capacitor
act as extra stray capacitance to ground shifting the center frequency of the resonance,  n , down by
 n from the unloaded half-wave resonance n / 2 . The width of the resonance is proportional to the
square of the capacitances. If the input and output couplings are the same and the line is lossless
transmission will be unity. This plot was generated using q out /q in = 5 and Q = 2 /q out 2 +2 /q in 2 = 20.

Both the magnitude, S 21 , and phase  of the transmitted amplitude, can be exquisitely sensitive
| |

probes of the cavity frequency (see Fig. 3.5) with a relative frequency shift of 1 /Q giving a change

in transmitted amplitude/phase of order unity. As will be discussed in detail in sections 3.3 and 3.4,

the effective cavity resonance frequency is shifted differently depending on the state of the qubit.

The resulting change in the transmitted amplitude or phase of a tone passing through the cavity is

then used as a readout of the qubit state.

Exercise 3.1.1. a. Derive an exact expression for the transmission coefficient S 21 in Eq. 3.17 using

the ABCD representation for the coupling capacitors and transmission line (see Pozar [Pozar1990]).

b. Use a similar technique but this time approximately expand about a frequency such that   n .

c. Make the approximate substitution C in / out Z 0 q in / out . In reality the capacitors are frequency


dependent. By approximating q in / out as constant this dependence is neglected in the small range

near resonance. To connect to the quantum optics language in the following sections one can then


![SchusterThesis.pdf-55-2.png](SchusterThesis.pdf-55-2.png)

substitute q in / out



 in / out / n .


######### 3.1.5 ######### Coplanar Waveguide Cavities

Thus far the description of transmission line resonators and their properties has been geometry

independent. In any physical realization a transmission line geometry must be chosen. A myriad

of options exist, including balanced lines such as the coplanar stripline (CPS), or unbalanced lines


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 54

b

######### t

 h

|Col1|Col2|
|---|---|
|b|s a|
|||


|Col1|s|a|Col4|Col5|
|---|---|---|---|---|
||||||
|Substrate|||||
||||||



Figure 3.6: Sketch of coplanar waveguide. Length is defined by gap capacitors at end. The ratio
s/a determines the impedance, Z 0 . The extent of the ground planes should be much larger than s
so that they can be approximated as infinite.

like microstrip and coplanar waveguide (CPW). In deciding to use CPW, the primary factor was

the method of grounding. In the microstrip geometry, the ground is beneath the substrate, meaning

that it would either be far away (300 m ), involve a potentially lossy deposited dielectric, or require

more complicated fabrication techniques (strained silicon or molecular beam epitaxy). Balanced

lines such as the CPS have no ground by definition, a blessing and curse as it requires less metal

(allowing it to be fabricated with electron beam lithography in the same step as the qubit), but since

the cryostat uses all balanced (coaxial) lines a balun is required to make the transition, potentially

complicating the mode structure. The CPS is certainly a viable choice and is currently being tested

by the QuLab group at Yale. The CPW has its ground in the same plane, separated by a gap

from the centerpin, resembling a 2d version of a coaxial cable. This gap can be scaled from microns

(where the fields are intense and well localized) to millimeters (to easily interface with printed circuit

boards) while maintaining the same impedance. These convenient grounding and scaling properties

led us to choose the CPW geometry for these experiments.

While any of these lines can be described by the general transmission line equations, their prop-

erties, especially the impedance ( Z 0 ) and wave propagation velocity ( v ), will depend on the exact

geometry (see Fig. 3.7). For a CPW these parameters are given by [Simons2002]


Z 0 CP W =  60  eff 


K ( k )

![SchusterThesis.pdf-56-2.png](SchusterThesis.pdf-56-2.png)

K ( k 




K ( k ) ( k 3

+ K
K ( k  ) K ( k 3 


![SchusterThesis.pdf-56-0.png](SchusterThesis.pdf-56-0.png)

![SchusterThesis.pdf-56-3.png](SchusterThesis.pdf-56-3.png)

K ( k 3 


 1
(3.24)



![SchusterThesis.pdf-56-1.png](SchusterThesis.pdf-56-1.png)

The speed of propagation is v eff =   eff  eff    eff (for non-magnetic substrates) and the effective

![SchusterThesis.pdf-56-4.png](SchusterThesis.pdf-56-4.png)

![SchusterThesis.pdf-56-6.png](SchusterThesis.pdf-56-6.png)

![SchusterThesis.pdf-56-7.png](SchusterThesis.pdf-56-7.png)

![SchusterThesis.pdf-56-5.png](SchusterThesis.pdf-56-5.png)

dielectric constant  eff is


The speed of propagation is v eff =   eff  eff    eff (for non-magnetic substrates) and the effective



1 +  r K
 eff = (3.25)

![SchusterThesis.pdf-56-8.png](SchusterThesis.pdf-56-8.png)

1 + K







1 +  r K
 eff =

1 + K




-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 55


175

150

125

100

75

50

25


H


40

30

20

10


![SchusterThesis.pdf-57-0.png](SchusterThesis.pdf-57-0.png)

![SchusterThesis.pdf-57-1.png](SchusterThesis.pdf-57-1.png)

50 100 150 200 250


10


gap spacing, s (  m) substrate thickness, h (  m)

Figure 3.7: Dependence of characteristic impedance, Z 0 , on the CPW geometry. a)
Plot of characteristic impedance, Z 0 vs. the gap spacing, s assuming a h = 300  m thick substrate and a = 1  m
center-pin thickness. The importance is that regardless of the ratio of a/s the impedance will be from
 10  200 . This puts constraints on how well (and with how much bandwidth) one can match to a
very high or low impedance load. b) Dependence of characteristic impedance on substrate thickness
showing that as soon as h  s , Z 0 is independent of the substrate thickness.


gap spacing, s (  m) substrate thickness, h (  m)


where K is the complete elliptic integral of the first kind 1



K ( k  ) K ( k 3 )
K = (3.26a)

![SchusterThesis.pdf-57-2.png](SchusterThesis.pdf-57-2.png)

K ( k ) K ( k 3  )



a
k =


(3.26b)


![SchusterThesis.pdf-57-3.png](SchusterThesis.pdf-57-3.png)

k 3 = tanh( a 4 h


![SchusterThesis.pdf-57-4.png](SchusterThesis.pdf-57-4.png)

![SchusterThesis.pdf-57-5.png](SchusterThesis.pdf-57-5.png)

tanh( b


4 h )


4 b 4 h h ) (3.26c)


![SchusterThesis.pdf-57-6.png](SchusterThesis.pdf-57-6.png)

k  =

k 3  =


![SchusterThesis.pdf-57-7.png](SchusterThesis.pdf-57-7.png)

1  k 2 (3.26d)

![SchusterThesis.pdf-57-8.png](SchusterThesis.pdf-57-8.png)

1 k 3 2 (3.26e)



and  r is the relative dielectric constant of the substrate of height h , with center conductor width a

and s the width of the gap, b = 2 s + a , as shown by Fig. 3.6.

######### 3.1.6 ######### Kinetic Inductance

When current flows in a wire it induces a magnetic flux. In addition to energy stored in these

magnetic fields, there is also the kinetic energy present in the electrons themselves. Normally this

kinetic inductance is masked by the conductivity of normal metals. In a superconductor, where the

resistivity is suppressed this hidden inductance can become significant. The total inductance per

unit length of a superconductor is the sum of the magnetic and kinetic inductances, L  = L m + L K .

![SchusterThesis.pdf-57-9.png](SchusterThesis.pdf-57-9.png)

1 Complete elliptic integrals of the first kind can be calculated using the Mathematica function EllipticK.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 56

In a coplanar waveguide geometry the magnetic inductance per unit length is given by [Yoshida1995]




L m =


K ( k  )

(3.27)

![SchusterThesis.pdf-58-1.png](SchusterThesis.pdf-58-1.png)
K ( k )


![SchusterThesis.pdf-58-0.png](SchusterThesis.pdf-58-0.png)

The kinetic energy of a current can be expressed as [Tinkham2004]


E = 1 n s mv 2 dV = 1

![SchusterThesis.pdf-58-2.png](SchusterThesis.pdf-58-2.png)

![SchusterThesis.pdf-58-3.png](SchusterThesis.pdf-58-3.png)

2 2

 


n s m


n s m 2

= 1
Ae 2 I





![SchusterThesis.pdf-58-5.png](SchusterThesis.pdf-58-5.png)
2



I 2 (3.28)

![SchusterThesis.pdf-58-6.png](SchusterThesis.pdf-58-6.png)
A


![SchusterThesis.pdf-58-4.png](SchusterThesis.pdf-58-4.png)

where A = at is the cross sectional area and  L = ( m/n s e 2 )  1 / 2 is the London penetration depth.

Because this kinetic energy is proportional to I 2 it can be interpreted as a kinetic inductance of the

form


L K =   at 2 L g ( s, a, t ) (3.29)

![SchusterThesis.pdf-58-7.png](SchusterThesis.pdf-58-7.png)

where g ( s, a, t )  5 is a geometric factor arising from the conformal mapping to the coplanar waveg-

uide configuration [Yoshida1995]


t
ln
 4 a



+ 2( a + s ) ln

( a + 2 s )


(3.30)



g ( s, a, t ) =


![SchusterThesis.pdf-58-8.png](SchusterThesis.pdf-58-8.png)

![SchusterThesis.pdf-58-9.png](SchusterThesis.pdf-58-9.png)

![SchusterThesis.pdf-58-10.png](SchusterThesis.pdf-58-10.png)

![SchusterThesis.pdf-58-11.png](SchusterThesis.pdf-58-11.png)

![SchusterThesis.pdf-58-12.png](SchusterThesis.pdf-58-12.png)

![SchusterThesis.pdf-58-13.png](SchusterThesis.pdf-58-13.png)

2 k 2 K ( k ) 2


+ 2( a + s )


a + s



ln
( a + 2 s )


4( a + 2 s )


Because g ( s, a, t ) is only weakly dependent on t and a (see Fig. 3.8), the kinetic inductance decreases

with the cross sectional area of the center-pin. In addition to the geometry of the CPW, the kinetic

inductance depends strongly on the London penetration depth,  L , the depth to which supercurrents

flow.  L depends on magnetic field, temperature, and any optical radiation which could break Cooper

pairs (as is discussed in Sec. 7.1). This derivation implicitly assumes that the thickness of the film

is smaller than the depth of current flow (  L ), such that the current distribution is uniform. If

it is much thicker then it may be more accurate to approximate the thickness as t 2  L . The


penetration depth itself also depends on the film thickness and this may lead to further corrections.

If any kinetic inductance dependencies have any temporal fluctuations on timescales faster than the

decay time, the resulting shifts in the resonance frequency (  L  1 / 2 ), will cause inhomogeneous

broadening of the resonance. Since the kinetic inductance makes up only a fraction of the total

inductance (see Fig. 3.9), such fluctuations will be suppressed by roughly L K /L m 10  1 10  2 ,
 

depending on the geometry of the CPW and superconductor chosen.

######### 3.1.7 ######### Intrinsic Resonator Losses

Ideally, all of the cavity loss would be determined by intentional coupling as in section 3.1.4. Though

the primary experiments in this dissertation were performed in this over coupled case, at higher


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 57

12



10


![SchusterThesis.pdf-59-0.png](SchusterThesis.pdf-59-0.png)

![SchusterThesis.pdf-59-1.png](SchusterThesis.pdf-59-1.png)

10


10


center  pin width, a


(  m) film thickness, t (  m)


Figure 3.8: Dependence of kinetic inductance prefactor on geometry as in Eq. 3.30. a. Plot of
g ( s, a, t ) vs. the centerpin width a . For this plot s = a/ 2 and t = 0 . 2  m. b. Plot of g ( s, a, t ) vs.
the film thickness t . Here a = 10  m and s = 5  m.



10


10


120

80

40


0.06


0.04

0.02


10

10

10


0.1

0.01

0.001


![SchusterThesis.pdf-59-2.png](SchusterThesis.pdf-59-2.png)

![SchusterThesis.pdf-59-3.png](SchusterThesis.pdf-59-3.png)

50 100 150 200


50 100 150 200

penetration depth,  L H nm L


center pin width, a


(  m)


Figure 3.9: a. Kinetic inductance vs. penetration depth (with a = 10  m) and b. kinetic inductance
vs. center-pin width (with  L = 105 nm). Depending on parameters the kinetic inductance can be
a significant percentage of the total resonator inductance.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 58

temperatures or at ultrahigh quality factors, even in a superconducting resonator intrinsic losses

can be the dominant factor limiting the photon lifetime. Three primary mechanisms of internal loss

are resistive, dielectric, and radiative losses. These mechanisms are also present as qubit relaxation

processes. Understanding these processes in the cavity, a simpler system, is very important for

improving qubit lifetimes and is sure to be explored further in future dissertations. Here, the focus

is to describe the basis of these loss mechanisms and show that they do not prevent resonators from

attaining Q  10 6 .

Resistive Losses

A superconductor can be thought of as consisting of two fluids consisting of a density, n n , of normal

quasiparticles with finite resistance and n s , of superconducting Cooper pairs, having zero DC resis-

tance but finite AC kinetic inductance. These fluids can be modeled as an inductor (the superfluid)

and resistor (the quasiparticles) in parallel. The normal fluids resistance is inversely proportional

to the number of quasiparticles, so at temperatures below the critical temperature it becomes very

large, and most of the current goes through the inductor. At any finite temperature and frequency,

some current will flow through the lossy resistor, limiting the maximum Q due to resistive loss.

The conductance of a superconductor



A
 =  n + i (3.31)

![SchusterThesis.pdf-60-0.png](SchusterThesis.pdf-60-0.png)

L K

where the normal conductivity  n = n n e 2  n /m , A is the cross-sectional area, and  n  10  12 s is the

scattering time [Tinkham2004] of the quasiparticles. One can transform this parallel conductance

per unit length to a series resistance per unit length [Yoshida1995],


R  = L 2 K  2  n = n n n s L K  2  n g ( s, a, t ) (3.32)

![SchusterThesis.pdf-60-1.png](SchusterThesis.pdf-60-1.png)

This form of the effective resistance per unit length shows the strong temperature dependence as the

BCS theory predicts n n /n s = exp( 1 . 76 T c /T ), and L K  2 L  L (0) 2 (1 ( T c/T ) 4 ). Substituting
   

R  into Eq. 3.6, the Q due to resistive losses can be expressed as



Z cn
Q res =



Z cn nZ 0

=

![SchusterThesis.pdf-60-2.png](SchusterThesis.pdf-60-2.png)

![SchusterThesis.pdf-60-3.png](SchusterThesis.pdf-60-3.png)
R n 2 R ,n



nZ 0

= n

![SchusterThesis.pdf-60-4.png](SchusterThesis.pdf-60-4.png)
2 R ,n  n


![SchusterThesis.pdf-60-5.png](SchusterThesis.pdf-60-5.png)

n n


Z 0   r 1 / 2

(3.33)
nL K  / 2  n c g ( s, a, t )


where the last step is achieved by substituting  = c/ / 2   r 1 / 2 . Ideally, the resistive Q can be

increased exponentially in T c /T , to values > 10 10 [Kuhr2006]. Resonators are often characterized

(see Sec. 7.1) at temperatures near T c , where the resistive Q can be a limiting factor. For ultra high


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 59

Material T c (K) H C1 (G) Coherence length,  (nm) London length,  L (nm)  L /

![SchusterThesis.pdf-61-0.png](SchusterThesis.pdf-61-0.png)
Aluminum 1.14 105 1600 16 0.01

![SchusterThesis.pdf-61-1.png](SchusterThesis.pdf-61-1.png)
Niobium 9.5 1980 38 39 1.02

![SchusterThesis.pdf-61-2.png](SchusterThesis.pdf-61-2.png)
Tantalum 4.48 830 90 54 0.6

![SchusterThesis.pdf-61-3.png](SchusterThesis.pdf-61-3.png)

Table 3.1: Important length scales and temperatures for superconductors of interest. Data taken
from [Kittel1996] and tantalum data from [Hauser1964, Kittel1996].

Q resonators non-equilibrium effects could also result in higher than expected residual quasiparticle

population, and resistive losses.

Dielectric Losses

Even if a resonator could employ perfect conductors, energy would be lost if the electric (or magnetic)

field lines pass through a lossy material. The dielectric loss is can be expressed as an imaginary

component in the dielectric constant  =  re + i im . A capacitor made from this material with

capacitance C , will acquire a conductance

G = C tan  (3.34)

where tan  =   im / re is called the loss tangent of the dielectric. The Q of an LCR resonator made

with such a capacitor is



 r C
Q diel =


(3.35)

![SchusterThesis.pdf-61-5.png](SchusterThesis.pdf-61-5.png)
tan 


![SchusterThesis.pdf-61-4.png](SchusterThesis.pdf-61-4.png)

One must take the utmost care to use only the most lossless dielectrics such as sapphire, high

resistivity silicon, and thermally grown (or crystalline) SiO 2 . Specifically it is almost certainly wise

to avoid deposited dielectrics. The substrate is thought to be the Q limiting factor [Mazin2004] and

one might hope to reduce losses by using a suspended resonator.

Radiative Losses

Even with no material loss the resonator can still lose energy to microwaves radiated into space. A

simple model [Mazin2004, Mazin2002] which treats the cavity as a straight CPW transmission line,


gives a radiation quality factor,



Q rad 3 . 5
 b



2
(3.36)



![SchusterThesis.pdf-61-6.png](SchusterThesis.pdf-61-6.png)

where  is the length of the resonator and b is the distance between the CPW ground planes (see

Fig. 3.6). For the experimental parameters  2 . 5 cm and b 20  m, giving Q rad 5 10  6 . This
   

formula is approximate and does not take into account the meanders or the ground plane backing,

and multiple dielectrics, but says that radiation should allow high quality factors to be achieved.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 60

######### 3.1.8 ######### Quantization of the LC Oscillator

In the previous subsections, lumped element and distributed effective LC circuits were used to make

an electronic harmonic oscillator. In this subsection, a LC circuit will be described as a (quantum)

harmonic oscillator, with the operators expressed in terms of electrical circuit quantities[Devoret2003].

For a lossless parallel LC circuit the inductor and capacitor share the same voltage so



I
V = L = q/C (3.37)
 t

![SchusterThesis.pdf-62-0.png](SchusterThesis.pdf-62-0.png)

The energy of the LC oscillator is



1
E =



1 2

LI + 1

![SchusterThesis.pdf-62-1.png](SchusterThesis.pdf-62-1.png)

![SchusterThesis.pdf-62-2.png](SchusterThesis.pdf-62-2.png)
2 2



CV 2 (3.38)
2


Which can be conveniently expressed as the Hamiltonian



q 2
H =



q 2 2

+ 

![SchusterThesis.pdf-62-3.png](SchusterThesis.pdf-62-3.png)

![SchusterThesis.pdf-62-4.png](SchusterThesis.pdf-62-4.png)
2 C 2


(3.39)
2 L


where q is the charge stored in the capacitor, and  = LI , is the flux stored in the inductor. I have

rewritten the energy in these variables because in this formulation


H


H

= q/C = LI
q  t



=   (3.40)
t 


![SchusterThesis.pdf-62-5.png](SchusterThesis.pdf-62-5.png)

![SchusterThesis.pdf-62-6.png](SchusterThesis.pdf-62-6.png)

H

= /L = I =  q (3.41)

![SchusterThesis.pdf-62-7.png](SchusterThesis.pdf-62-7.png)



H


which defines  and q as generalized canonical position and momentum variables. In this form,

the classical variables map directly to quantum mechanical operators ( H,   q,   ) and because they are

canonical the commutator is

[ q,   ] =  i  (3.42)

The Hamiltonian for a particle moving in a harmonic potential is


H =  p 2 / 2 m + 1 m 2 x  2 (3.43)

![SchusterThesis.pdf-62-8.png](SchusterThesis.pdf-62-8.png)

2

By analogy, the charge is the momentum ( q  p  ), the flux is the position (    x  ), and  


![SchusterThesis.pdf-62-9.png](SchusterThesis.pdf-62-9.png)

1 /


LC . As with the mechanical oscillator, this Hamiltonian can be written in terms of dimensionless


operators

H =   ( a  a + 1 / 2) (3.44)

where the photon annihilation operator is given by

1
a =  2  Z c (  + iZ c q ) (3.45)


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 61


![SchusterThesis.pdf-63-0.png](SchusterThesis.pdf-63-0.png)

where Z c =


L/C is the characteristic impedance of the circuit. In this language, the charge and


flux can be expressed in terms of creation and annihilation operators as


![SchusterThesis.pdf-63-1.png](SchusterThesis.pdf-63-1.png)

( a  a ) (3.46)
2 Z c 


q = i

 =


![SchusterThesis.pdf-63-2.png](SchusterThesis.pdf-63-2.png)

 Z c

![SchusterThesis.pdf-63-3.png](SchusterThesis.pdf-63-3.png)

2 ( a + a  ) (3.47)


![SchusterThesis.pdf-63-4.png](SchusterThesis.pdf-63-4.png)

![SchusterThesis.pdf-63-5.png](SchusterThesis.pdf-63-5.png)

Note the prefactors of Z c



/  50which can have implications when coupling to an atom


or qubit via charge or phase/flux. Using input-output theory, described in chapter 7 of Walls and

Milburn [Walls2006], the effect of coupling to the environment can be modeled. In their treatment,

the cavity is represented by a single electromagnetic mode, coupled to a continuum of bath modes.

A quick read through this chapter is highly recommended for a quantum optics view of the cavity,

as it is well written and very penetrable.

####### 3.2 ####### Cooper Pair Box

The Cooper pair box (CPB) 1 consists of a superconducting island connected to a reservoir via a

Josephson junction. The Josephson junction can be thought of as a circuit element which allows

Cooper pairs to coherently couple between the island and reservoir, with a stray capacitance in

parallel. A gate voltage ( V g ) can be used to electrostatically induce Cooper pairs to tunnel. Usually,

a two junction SQUID geometry is used which allows the tunnel coupling to be adjusted by

application of a magnetic flux (). In this section, the CPB Hamiltonian will be described, first

in the charge basis, which naturally incorporates the voltage bias and gives intuitive meaning to

the two logical qubit states. Next, the Hamiltonian is rederived in the phase basis, which allows

for analytic calculation of the energy levels and wavefunctions. The phase basis will also provide a

natural way of approaching a new manifestation of the CPB in section 4.3.

######### 3.2.1 ######### Charge Basis

To lowest order, the CPB can be thought of as a superconducting island with total capacitance to

ground, C  = C g + C j + C s , a gate induced polarization charge, n g = C g V g /e , which can be thought

of as the preferred amount of excess island charge (in electrons). However, the actual excess charge

is a quantized, integer number, N , of excess Cooper pairs, allowing the box to be electrostatically

![SchusterThesis.pdf-63-6.png](SchusterThesis.pdf-63-6.png)

Two particularly good resources for learning about the CPB are the Cottet [Cottet2002] and Bouchiat [Bouchiat1998] theses. Much of the following discussion closely follows these works. 1


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 62



a) b)


######### e ######### 2 E c = 2(Cj+Cg)


######### e


|Cg Z()|Col2|
|---|---|
|E c E J||
|||
|||


![SchusterThesis.pdf-64-0.png](SchusterThesis.pdf-64-0.png)

Figure 3.10: a. Sketch of CPB circuit. The CPB consists of an island connected to a reservoir
via a tunnel junction and is electrostatically biased by a voltage coupled through a small capacitor.
b. A circuit diagram of the CPB. The island (green) is connected to a ground via a Josephson
junction which is represented by a pure Josephson element with energy E J and a stray capacitance
C j . The charging energy, which sets the scale of electrostatic excitations, is determined by the total
capacitance of the island to ground.

frustrated by the gate voltage. The Hamiltonian for this electrostatic component 1 ,


2
H el = 4 E C N   n g / 2 (3.48)
 

where E C = e 2 / 2 C  is the electrostatic charging energy to add a single electron 2 to the island.

These electrostatic energy levels, the parabolas (dashed and dotted lines) in Fig. 3.11, are just

the energies of a capacitor with some fixed charge. If the junction were only capacitive, allowing

no tunneling, then Eq. 3.48 would fully describe the Cooper pair box. Charge would be perfectly

quantized, but there would be no way of changing the charge state, a rather uninteresting quantum

circuit. However, the Josephson effect allows Cooper pairs to coherently tunnel across the junction,

described by the Hamiltonian



E J
H J =


( | n  n + 1 | + | n + 1  n | ) (3.49)


![SchusterThesis.pdf-64-1.png](SchusterThesis.pdf-64-1.png)

where E J is the Josephson energy and n is the number of Cooper pairs on the island. This operator

in the Hamiltonian allows Cooper pairs to hop on and off the island, acting much like a discrete

kinetic energy term in a tight binding model of a lattice.

The shape of the energy bands and composition of the wave functions can be expressed purely in

![SchusterThesis.pdf-64-2.png](SchusterThesis.pdf-64-2.png)

1 An energy  C g V g 2 / 2 has been subtracted off as a gauge choice because it does not depend on any of the dynamical
qubit variables.
2 The convention in this thesis is that all electrostatic energies and polarization charges are expressed in terms of
single electrons.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 63

2

8


0.5


E J =0


|e|N|e g|N|g|Col2|Col3|E/E=1 J c|
|---|---|---|---|
||e|N|e g|N|g|||


![SchusterThesis.pdf-65-0.png](SchusterThesis.pdf-65-0.png)

0 1 2 3 4 0 1 2 3 4

n g (e) n g (e)

Figure 3.11: a) CPB energy levels. Dotted and dashed black lines show electrostatic energy of
island for 0 and 1 Cooper pairs present on the island. The (from bottom to top) blue, red, and green
solid bands show the ground, and first two excited state energy levels with E J = E C . At n g = 1
there is an avoided crossing, where the eigenstates are superpositions of n and n + 1 Cooper pairs.
The midpoint of the avoided crossing occurs at an energy E C , and the difference between states at
even n g of Cooper pairs is 4 E C . b) A plot of the expected number of Cooper pairs (each with charge
of 2 e ) of the ground (blue) and first excited (red) state. The dashed/dotted curves have E J = 0 and
so the expected value is just the lowest energy integer charge state, whereas the solid curves with
E J = E C have non-integer expected charge values indicating strongly overlapping superpositions of
charge states. At n g = 1 they have the same expected charge 2 e  N   = 1 e , meaning that they can
not be distinguished by a charge based measurement or affected (to first order) by charge noise.

terms of the ratio 1 E J /E C . When the characteristic tunneling energy is much less than the charging

energy ( E J 4 E C ), in the charge qubit regime, then the qubit state can be accurately expressed


in terms of the nearest two charge states. In the charge qubit regime, the most important effect

shown in Fig. 3.11a is that the Josephson coupling lifts the degeneracy present when the Cooper

pair box is electrostatically frustrated at n g = 1. At this bias condition, the ground and excited


![SchusterThesis.pdf-65-1.png](SchusterThesis.pdf-65-1.png)

eigenstates are superpositions of charge states ( | 0  | 1  ) /


2 with a ground-excited state energy


difference E eg = E J . When E eg > k B T then there will be no thermal population of the first (or any

higher lying) excited state.

When using the CPB as a qubit, it is convenient to reexpress the lowest two levels of the Hamil-

tonian in the language of a spin-1/2, which can be done by taking the first two levels, subtracting

their mean energy, and approximating the operators as n n + 1 + n + 1 n  x  and  N  z  / 2.
|  | |  |  



1
H CPB = (4 E C (1 n g )  z  + E J  x  ) (3.50)
 2 

![SchusterThesis.pdf-65-2.png](SchusterThesis.pdf-65-2.png)

This is the Hamiltonian of a spin 2 (with  = 1) subject to a fictitious magnetic field, B = E J x   +

![SchusterThesis.pdf-65-3.png](SchusterThesis.pdf-65-3.png)

1 The effects of different E J /E C ratios will be discussed in more detail chapter 4.
2 Even well into the transmon regime, where E J  4 E C , the CPB can be expressed in this form, but the field


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 64


######### a) ######### b)


######### 


 1

 2


![SchusterThesis.pdf-66-0.png](SchusterThesis.pdf-66-0.png)

0.5 1 1.5

n g H e L



![SchusterThesis.pdf-66-1.png](SchusterThesis.pdf-66-1.png)

Figure 3.12: a. Energy levels from the two state approximation in Eq. 3.52, are (solid) hyperbolas,
which asymptote (dashed lines) to 4 E C (1  n g ). b. Fictitious field picture of a point close to n g = 1,
in the x   z  basis and the showing transformation to the basis where  z is along the quantization
axis.

4 E C (1  n g ) z   .

As can be seen from Fig. 3.12 the Coulomb energy away from degeneracy depends nearly linearly

on n g . Fluctuations in n g , which arise from noise on the voltage bias and charge noise due to

impurities in the box itself, can lead to fluctuations in the qubit transition energy. At n g = 1

however the transition energy is insensitive, to first order, to small fluctuations of n g . This allows

one to obtain much longer coherence times (see section 4.2. For this reason, the CPB is usually

operated at n g = 1, and the discussion that follows will focus on this bias condition. More detail on

optimizing the CPB parameters and operating point to minimize decoherence will be discussed in

chapter 4.

The effective field and quantization axis is parallel to the net magnetic field (see Fig. 3.12). It is

often convenient to work in a coordinate system rotated about the y   -axis by a mixing angle


E J
 m = arctan

![SchusterThesis.pdf-66-2.png](SchusterThesis.pdf-66-2.png)

4 E C (1 n g )


(3.51)


In this new coordinate system, quantization is along the  z -axis and H CPB =   a  z where


![SchusterThesis.pdf-66-3.png](SchusterThesis.pdf-66-3.png)

  a =


E J 2 + (4 E C (1 n g )) 2 (3.52)




At n g = 1, the electrostatic component is H el = 0 and  m = / 2, leaving the Josephson component

![SchusterThesis.pdf-66-4.png](SchusterThesis.pdf-66-4.png)

strengths will have a more complicated functional form. The two energy level (not charge state) approximation is
useful as long as the ground-excited energy difference is not harmonic with the next transition. The dependence of
this anharmonicity on E J /E C and its implications for using the CPB as a qubit will be discussed in chapter 4.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 65



0.5

0.25


0.5

0

 0.5

 1

|Col1|Col2|Col3|E/E=0 J c E/E=0.25 J c E/E=1 J c E/E=4 J c|
|---|---|---|---|


![SchusterThesis.pdf-67-0.png](SchusterThesis.pdf-67-0.png)

n g (e)


n g (e)


Figure 3.13: a) Charge difference between ground and first excited state (  e | N  | e  g | N  | g  ) at
different E J /E C ratios. The charge difference is largest away from n g = 1. The dashed black lines
are calculated using a two charge-state approximation cos(  m ) b) The transition (dipole) matrix
element (  g | N  | e  ) however does not go to zero at degeneracy, and in fact is largest at n g = 1. The
dashed two charge approximation is | sin(  m ) / 2 | , which is 1 / 2 at n g = 1 because the state is an
even superposition of charge states. The cusps at n g = 2 are due to the coupling of the first and
second excited states. In both cases the approximations begin to break down as E J /E C increases.
In the two charge approximation one would expect the transition matrix element to never rise above
1 / 2 (an even superposition of two states one Cooper pair apart). At E J /E C = 4 the superpositions
contain more states raising the expectation value.

to determine the quantization axis,  x   z . Qubit manipulations are performed via electrostatic



excitation along what is now the  x direction. At an arbitrary n g , gate excitations affect both the

perpendicular (as  x sin  m ), allowing the qubit to be flipped, and the longitudinal component (as

 z cos  m ) allowing implementation of electrostatic phase gates. Thermal and vacuum fluctuations

are similarly divided, affecting the CPB decoherence properties discussed in chapter 4.

######### 3.2.2 ######### Phase Basis

The charge basis provides an intuitive framework for visualizing the states of the Cooper pair box.

However, because it is an unbounded discrete basis most calculations must be done approximately by

numerically diagonalizing a subspace including many nearest charge states. Phase is the canonical

conjugate to charge and while the charge is discrete the phase is continuous (though periodic).

In the phase basis the energies and wavefunctions can be solved analytically, making it cheaper

computationally and less susceptible to truncation error 1 . The superconducting phase difference,   ,

![SchusterThesis.pdf-67-1.png](SchusterThesis.pdf-67-1.png)

1 The number of charge states increases when E J  4 E C , making the phase basis more appropriate for analysis of
CPBs with large E J /E C .


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 66

is related to the tunneling current across the junction and can be defined by the relations




n  = i (3.53)

![SchusterThesis.pdf-68-0.png](SchusterThesis.pdf-68-0.png)



n  exp  i = exp  i ( n + 1) (3.54)

and eigenstates corresponding to


|   =


e in | n  (3.55)
n =  


2 
| n  = 0



de  in |   (3.56)


Rewriting the | n  s in Eqs. 3.48 and 3.49 in the |   basis, one can rewrite the box Hamiltonian

H CPB = H el + H J in the phase basis as 1


2

 E J
i n g / 2  

  |  |  2



e i + e  i |    | (3.57)




H CPB = 4 E C


![SchusterThesis.pdf-68-1.png](SchusterThesis.pdf-68-1.png)

![SchusterThesis.pdf-68-2.png](SchusterThesis.pdf-68-2.png)

The time independent Schr odinger equation becomes H CPB k = E k k . The phase wave func-
|  | 


tion  k (  )  k is then the solution of the differential equation
 | 


2



n g / 2  k E J  k cos  = E k  k (3.58)
  



4 E C


i 


![SchusterThesis.pdf-68-3.png](SchusterThesis.pdf-68-3.png)

This equation resembles the equation of motion of a pendulum which is allowed to make large angular

excursions, and lies in the class of Mathieu equations, which can be solved analytically[Cottet2002,

Arscott1964]. Their solutions are prepackaged in Mathematica and a specific implementation is

presented in Appendix C, or for a more detailed derivation see ref.[Cottet2002].

######### 3.2.3 ######### Split CPB

In the previous Hamiltonian, the electrostatic ( x field) component can be tuned by application of

a gate voltage ( V g ). The ability to tune the tunneling ( E J ) portion of the Hamiltonian is readily

achieved by splitting the Josephson junction, as shown in Fig. 3.14. Each junction will have a char-

acteristic tunneling energy ( E J1 , E J2 ) and superconducting phase (   1 ,   2 ) across it. The Josephson

part of the Hamiltonian is just the sum of the contributions of the two junctions.

H J = E J1 cos(  1 ) + E J2 cos(  2 ) (3.59)

![SchusterThesis.pdf-68-4.png](SchusterThesis.pdf-68-4.png)

1 The implicit integral over  has been suppressed in Eq. 3.57 for clarity.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 67

######### E ######### J2 ######### , #########  ######### 2

|Col1|Col2|
|---|---|


![SchusterThesis.pdf-69-0.png](SchusterThesis.pdf-69-0.png)

Figure 3.14: Sketch of the split Cooper pair box. The island is connected to a reservoir by two
junctions, each with a Josephson energy E J1 , E J2 and phase difference   1 ,   2 . Splitting the box gives
the ability to tune the effective E J = ( E J1 + E J2 ) cos(   /  0 ) by applying a magnetic flux .

It is convenient to define two new variables



 1 + 
 =


(3.60)


![SchusterThesis.pdf-69-1.png](SchusterThesis.pdf-69-1.png)

 =  1  2 (3.61)


Using flux quantization 1 the phase difference,  , can be rewritten in terms of the magnetic flux

piercing the loop (see Fig. 3.14), , as  = 2   /  0 where  0 = h/ 2 e is the superconducting flux

quantum. Substituting the relations in Eq. 3.61, and using trigonometric substitutions one can

rewrite this expression as




H J = ( E J1 + E J2 ) cos 

![SchusterThesis.pdf-69-2.png](SchusterThesis.pdf-69-2.png)

 0




cos  + ( E J2 E J1 ) sin 
  0




cos  + ( E J2 E J1 ) sin 
 


sin  (3.62)


![SchusterThesis.pdf-69-3.png](SchusterThesis.pdf-69-3.png)

If the two junctions are symmetric ( E J1 = E J2 ), or there is no external flux ( = 0), the expression

simplifies to the single junction Hamiltonian (as in Eq. 3.57), with a flux tunable effective Josephson

energy

E J sum = ( E J1 + E J2 ) (3.63)



E J1 E J2
d = E  sum (3.64)


![SchusterThesis.pdf-69-4.png](SchusterThesis.pdf-69-4.png)

![SchusterThesis.pdf-69-5.png](SchusterThesis.pdf-69-5.png)

1 Flux quantization [Tinkham2004] arises because the wavefunction inside of a superconductor must be single
valued meaning that,   -  ds = 2 n . For a superconducting loop interrupted by a junction, this integral is most
conveniently expressed in terms of the phase difference across the junction,  and the magnetic flux enclosed as
  + 2  ( m  v s /h + A/   0 ) -  ds = 2 n , where because no current flows inside the bulk of the superconductor the
net Cooper pair velocity, v s = 0. Using Stokes theorem the integral can be rewritten as  /  0 = S B/  0 -  dA .



Substituting and solving for   , yields   = 2   /  0 + 2 n . It is valid to treat this phase as a classical variable



because the asymmetric mode of the squid has the junctions effectively shunted by the rest of the loop[Cottet2002].


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 68

In our typical devices the junction asymmetry is d  10% and so the Josephson terms in Eq. 3.62

cannot be suppressed completely. Typically the CPB is operated with integer flux in the ring,

 = n  0 , then sin(   /  0 ) = 0, further suppressing the difference term, and one can hope to ignore

its effects to first order. When E J sum is suppressed by applying a field, then flux noise in the difference

term could potentially contribute to decoherence. Also the sin  term presents an opportunity couple

the qubit states through flux, even at n g = 1. This might allow a non-cavity excitation channel,

and may also be relevant with the transmon geometry, where charge noise is almost completely

suppressed, potentially leaving flux noise to dominate the decoherence properties (see Sec. 4.3).

One can transform this split CPB Hamiltonian in the phase basis back to the charge basis using

the Eq. 3.55 to map



1
cos  ( n n + 1 + n + 1 n )  x  (3.65)
 2 |  | |  | 


![SchusterThesis.pdf-70-0.png](SchusterThesis.pdf-70-0.png)


i
sin  ( n n + 1 n + 1 n )  y  (3.66)
 2 |  | |  | 

![SchusterThesis.pdf-70-1.png](SchusterThesis.pdf-70-1.png)

so the junction Hamiltonian in the charge basis is


cos (   /  0 )


H J = E J sum



id sin (   /  0 )
( n n + 1 + n + 1 n ) +
|  | |  | 2


( | n  n + 1 | | n + 1  n | )

(3.67)


![SchusterThesis.pdf-70-2.png](SchusterThesis.pdf-70-2.png)

![SchusterThesis.pdf-70-3.png](SchusterThesis.pdf-70-3.png)

In the two state approximation the total Hamiltonian can be written


H CPB = E J sum


(cos (   /  0 )  x + d sin (   /  0 )  y ) + 4 E C (1  n g )  z (3.68)


![SchusterThesis.pdf-70-4.png](SchusterThesis.pdf-70-4.png)

The transition energy of the split CPB is


![SchusterThesis.pdf-70-5.png](SchusterThesis.pdf-70-5.png)

E J sum 2 cos 2 (   /  0 ) + d 2 sin 2 (   /  0 ) + 16 E C 2 (1 n g ) 2 (3.69)



 


E =


####### 3.3 ####### Coupling CPB to Cavity


The electrostatic Hamiltonian, H el of Eq. 3.48, depends on a polarization charge n g = C g V g /e .

Inside of a cavity, the gate voltage, V g , is the voltage between the center-pin and ground planes (See

Fig. 3.15). The total voltage can be written as the sum of a classical DC voltage and a quantum

voltage due to the photons inside the resonator.

V g = V DC + V  (3.70)


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 69

where V  =  q/C . Substituting into Eq. 3.46 yields 1


![SchusterThesis.pdf-71-0.png](SchusterThesis.pdf-71-0.png)

V =


  r ( a + a  ) (3.71)

![SchusterThesis.pdf-71-1.png](SchusterThesis.pdf-71-1.png)

2 C


Plugging this into the H el (Eq. 3.48) and expanding the square gives


2 4 E C C g V  2 V g + V 
H el = 4 E C N  n g / 2 +
 e
 



4 E C C g  V N 
 e


(3.72)


![SchusterThesis.pdf-71-2.png](SchusterThesis.pdf-71-2.png)

![SchusterThesis.pdf-71-3.png](SchusterThesis.pdf-71-3.png)

The first term is just the original electrostatic Hamiltonian with classical bias. The second term

is extra energy stored in the geometric capacitance of the qubit, and is not qubit state dependent,

thus it does not affect any of the qubit(-cavity) dynamics. The final term, which represents the

resonator-CPB coupling Hamiltonian, H c , depends both on the CPB state and the quantum field

state of the resonator.

H c = 2  g ( a  + a ) N  (3.73)



eV 0
g =  (3.74)




![SchusterThesis.pdf-71-4.png](SchusterThesis.pdf-71-4.png)

![SchusterThesis.pdf-71-5.png](SchusterThesis.pdf-71-5.png)

V 0 =


  r

(3.75)

![SchusterThesis.pdf-71-6.png](SchusterThesis.pdf-71-6.png)
2 C


Where  = C g /C  accounts 2 for the division of voltage in the CPB. The coupling constant 2  g can

be seen as the energy in moving a Cooper pair (2 e ) across the portion (  = C g /C  ) of the rms

vacuum voltage fluctuations ( V 0 ) in the resonator. Eq. 3.75 for the zero point voltage can be derived


from the following relation,


1

 

![SchusterThesis.pdf-71-8.png](SchusterThesis.pdf-71-8.png)
2




1

2





1
= 2 CV 0 2 (3.76)


= 1


![SchusterThesis.pdf-71-7.png](SchusterThesis.pdf-71-7.png)

![SchusterThesis.pdf-71-9.png](SchusterThesis.pdf-71-9.png)

where the first 1 / 2 is because half of the zero point energy is stored in the electric field and half is

in the magnetic field. How large can this dipole coupling get? To answer this critical question most

generally, one can look at the dimensionless coupling g/ r


![SchusterThesis.pdf-71-12.png](SchusterThesis.pdf-71-12.png)

g eV 0

 r   r


g eV

=
 r   r


Z c e 2

(3.77)
2 


![SchusterThesis.pdf-71-10.png](SchusterThesis.pdf-71-10.png)

![SchusterThesis.pdf-71-11.png](SchusterThesis.pdf-71-11.png)

![SchusterThesis.pdf-71-13.png](SchusterThesis.pdf-71-13.png)

where we have employed Z c = 1 / r C to reexpress the coupling in terms of the characteristic

impedance. One can rewrite the characteristic impedance of the effective resonance in terms of

![SchusterThesis.pdf-71-14.png](SchusterThesis.pdf-71-14.png)

1 I have made a slight change of convention changing to q  ( a + a  ) rather than ( a  a  ) so that the resulting
Jaynes-Cummings Hamiltonian will be in its standard form. For a harmonic oscillator this is purely a phase convention.
2  = C g /C  assumes a well grounded box with C g  C  . By judicious design of the capacitance network (see
Sec. 5.2)  can be engineered to be anywhere between zero and one.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 70

a) b) c)

|w = 1|0 m|
|---|---|



|E|= V /|w|
|---|---|---|

|-- -- -- -- -- --|Col2|Col3|
|---|---|---|
||||
|++++++++ + +|||

|Col1|-- -- w = 10 m -- -- -- -- r 1 nm E = V / w g g ++++++++ + +|
|---|---|
|||


![SchusterThesis.pdf-72-0.png](SchusterThesis.pdf-72-0.png)

![SchusterThesis.pdf-72-1.png](SchusterThesis.pdf-72-1.png)

![SchusterThesis.pdf-72-2.png](SchusterThesis.pdf-72-2.png)

![SchusterThesis.pdf-72-3.png](SchusterThesis.pdf-72-3.png)

Figure 3.15: a) Schematic depiction of dipole moment of an atom d  = q x in an electric field E  ,
which has energy U =  E  -  d  . b) The CPB can be thought of as molecule inside of an electric field
produced by applying a gate voltage V g across a gap of width w . Because the Cooper pairs can move
freely on each island, a Cooper pair can move by microns even though the junction is only  1 nm,
allowing the dipole moment to be adjusted. c) A more appropriate picture of the dipole energy of
a circuit is U =  2 eV j , where V j = V g is the voltage dropped across the actual junction, a fraction
 of the original gate voltage (See chapter 5 for details).

the transmission line impedance Z 0 = nZ C / 2 (Eq. 3.13)


![SchusterThesis.pdf-72-5.png](SchusterThesis.pdf-72-5.png)

![SchusterThesis.pdf-72-7.png](SchusterThesis.pdf-72-7.png)

2 Z 0


nh/e 2 =


Z 0

(3.78)

![SchusterThesis.pdf-72-9.png](SchusterThesis.pdf-72-9.png)
R K


Z


= 

![SchusterThesis.pdf-72-4.png](SchusterThesis.pdf-72-4.png)
 r


![SchusterThesis.pdf-72-6.png](SchusterThesis.pdf-72-6.png)

![SchusterThesis.pdf-72-8.png](SchusterThesis.pdf-72-8.png)

where R K = h/e 2  25 . 8 kis the resistance quantum. The line impedance is Z 0 =  0


![SchusterThesis.pdf-72-10.png](SchusterThesis.pdf-72-10.png)

 r / r ,


![SchusterThesis.pdf-72-11.png](SchusterThesis.pdf-72-11.png)

where  0 =


 0 / 0 377 is the impedance of free space and  0 . 4(for a CPW) is a dimensionless
 


geometry dependent factor of order unity. Substituting for Z 0 yields


 r

![SchusterThesis.pdf-72-15.png](SchusterThesis.pdf-72-15.png)

 r




1 / 4
(3.79)



![SchusterThesis.pdf-72-13.png](SchusterThesis.pdf-72-13.png)

2 


= 

![SchusterThesis.pdf-72-12.png](SchusterThesis.pdf-72-12.png)
 r


![SchusterThesis.pdf-72-14.png](SchusterThesis.pdf-72-14.png)

which consists of dimensionless constants, and amazingly, the fine structure constant,  ! Here we see

the fine structure constant in circuit form as the ratio of the vacuum impedance and the resistance

quantum



 0
 =



 0 e 2

=

![SchusterThesis.pdf-72-16.png](SchusterThesis.pdf-72-16.png)

![SchusterThesis.pdf-72-17.png](SchusterThesis.pdf-72-17.png)
R K 2  0


2  0 hc 


(3.80)

![SchusterThesis.pdf-72-18.png](SchusterThesis.pdf-72-18.png)
137


If the coupling is maximized (  = 1) the maximum dimensionless coupling strength can be made

about  10%. The Hamiltonian in Eq. 3.73 describes the interaction between any two CPB states.

At n g = 1 in the charge regime 1

N  g N  e  x sin  m  x / 2 + cos  m  z / 2 (3.81)
 | |  

![SchusterThesis.pdf-72-19.png](SchusterThesis.pdf-72-19.png)

1 At high E J /E C one has to be more careful when evaluating  g |  N | e  .


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 71

At n g = 1 where the CPB is usually operated N  =  x / 2. In addition one can make the dipole or

rotating wave approximation that

( a  + a )  x = a    + a + (3.82)

which ignores terms like a   + and a  which change the number of excitations in the system. This

assumption is valid when the energy of adding both a photon and qubit excitation is much larger

than the coupling and the energy difference between a photon and a qubit excitation (  r +  a 


g,  r  a ).
|  |


H c =  g ( a    + a + ) (3.83)


adding this to the harmonic oscillator and qubit contributions gives the Jaynes-Cummings Hamil-

tonian


H jc =   r ( n + 1 / 2) +   r  z +  g ( a    + a + ) (3.84)

![SchusterThesis.pdf-73-0.png](SchusterThesis.pdf-73-0.png)

2

Exercise 3.3.1. Derive the fine structure limit of g/ for a dipole inside a three-dimensional cavity.

a. g/ = dE 0 /   . Find rms vacuum electric field, E 0 , inside a 3D cavity assuming that the electric

field is uniformly distributed in the volume   3 of the cavity. b. Assuming that the dipole moment

is d = e  x , rewrite g/ in terms of the fine structure constant  . What quantity plays the role of

 ? What does this say about relative coupling strengths of atoms to 3D cavities and 1D cavities?

######### 3.3.1 ######### Comparison with Traditional Cavity QED

A cavity QED experiment can be characterized by several frequency scales. The transition frequen-

cies of the atom/qubit (  a ) and cavity (  r ) determine the overall energy scale of the system. The

dipole coupling rate g sets the interaction rate of the cavity and qubit. Finally the decoherence

times 1 / and 1 / set the length of time before the interactions are polluted. To study interactions

between these quantum systems, the ratios of the coupling to the decoherence rates ( N 0 , m 0 , and

n Rabi ) are most important. For example, N 0 2 /g 2 , is the critical atom number, which can be


interpreted as the number of atoms required in the cavity to split the cavity line, and characterizes

the maximum rate at which a single photon measures the qubit state. Similarly the critical photon

number, m 0 =  2 / 2 g 2 , tells how many photons in the cavity in its steady state are required to sat-

urate the qubit, and indicates how sensitive the qubit is as a photon detector. Finally the number


of vacuum Rabi oscillations possible, n Rabi =  2 + g  , determines whether one is in the strong coupling

![SchusterThesis.pdf-73-1.png](SchusterThesis.pdf-73-1.png)

regime ( n Rabi > 1) and is related to the maximum efficiency of converting an excitation between a


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 72

qubit state and a photon. Table 3.3.1 shows circuit QED attains similar values to traditional atomic

cavity QED. It does so by having a much stronger dimensionless coupling g/  1  10%.

To compare the CPB to an atom independent of the cavity one can define a transition dipole


moment. The dipole moment can be reexpressed as  g = ( ew ) w 1 V 0 = dE 0 where w is the transverse

![SchusterThesis.pdf-74-0.png](SchusterThesis.pdf-74-0.png)

dimension of the CPW, E 0 is the rms vacuum electric field, and d is the effective dipole moment

of the CPB. While this language furthers the image of CPB as artificial atom, from this definition

it is clear that circuit QED behaves fundamentally differently from atomic QED where the dipole

moment is a fixed property of the atom. Here the dipole moment of the box can be adjusted to

give the maximum g for any E 0 . If the cavity is made larger or smaller (reducing E 0 ) the box can

be adjusted to maintain the same coupling. With circuits the properties of the two systems really

are inextricably linked. Currently atomic experiments have truly fantastically coherent atoms and

resonators, but achieve only a small fraction of their maximum potential dimensionless coupling

g/ . One promising avenue for increasing this coupling is to use cavities with higher E 0 (smaller

transverse dimension). The 1D transmission line resonators, might be very promising as they allow

the field to be adjusted by changing the gap between center conductor and ground planes.

![SchusterThesis.pdf-74-1.png](SchusterThesis.pdf-74-1.png)

parameter symbol 3D optical 3D microwave Semiconductor 1D circuit

![SchusterThesis.pdf-74-3.png](SchusterThesis.pdf-74-3.png)

![SchusterThesis.pdf-74-4.png](SchusterThesis.pdf-74-4.png)

![SchusterThesis.pdf-74-5.png](SchusterThesis.pdf-74-5.png)

![SchusterThesis.pdf-74-6.png](SchusterThesis.pdf-74-6.png)

![SchusterThesis.pdf-74-7.png](SchusterThesis.pdf-74-7.png)

![SchusterThesis.pdf-74-8.png](SchusterThesis.pdf-74-8.png)

![SchusterThesis.pdf-74-9.png](SchusterThesis.pdf-74-9.png)

resonator/atom frequency  r / 2  ,  / 2  350 THz 51 GHz 250 THz 5 GHz

vacuum Rabi frequency g/ , g/ r 220 MHz, 3  10  7 47 kHz, 5  10  7 41 GHz, 8  10  5 100 MHz,10  2

![SchusterThesis.pdf-74-11.png](SchusterThesis.pdf-74-11.png)

![SchusterThesis.pdf-74-12.png](SchusterThesis.pdf-74-12.png)

![SchusterThesis.pdf-74-13.png](SchusterThesis.pdf-74-13.png)

![SchusterThesis.pdf-74-14.png](SchusterThesis.pdf-74-14.png)

![SchusterThesis.pdf-74-15.png](SchusterThesis.pdf-74-15.png)

![SchusterThesis.pdf-74-16.png](SchusterThesis.pdf-74-16.png)

![SchusterThesis.pdf-74-17.png](SchusterThesis.pdf-74-17.png)

transition dipole d/ea 0  1 1  10 3 2  10 4 30

![SchusterThesis.pdf-74-19.png](SchusterThesis.pdf-74-19.png)

![SchusterThesis.pdf-74-20.png](SchusterThesis.pdf-74-20.png)

![SchusterThesis.pdf-74-21.png](SchusterThesis.pdf-74-21.png)

![SchusterThesis.pdf-74-22.png](SchusterThesis.pdf-74-22.png)

![SchusterThesis.pdf-74-23.png](SchusterThesis.pdf-74-23.png)

![SchusterThesis.pdf-74-24.png](SchusterThesis.pdf-74-24.png)

![SchusterThesis.pdf-74-25.png](SchusterThesis.pdf-74-25.png)

cavity lifetime 1 /, Q 10 ns, 3  10 7 1 ms, 3  10 8 4 ps, 6  10 3 160 ns, 10 4

![SchusterThesis.pdf-74-27.png](SchusterThesis.pdf-74-27.png)

![SchusterThesis.pdf-74-28.png](SchusterThesis.pdf-74-28.png)

![SchusterThesis.pdf-74-29.png](SchusterThesis.pdf-74-29.png)

![SchusterThesis.pdf-74-30.png](SchusterThesis.pdf-74-30.png)

![SchusterThesis.pdf-74-31.png](SchusterThesis.pdf-74-31.png)

![SchusterThesis.pdf-74-32.png](SchusterThesis.pdf-74-32.png)

![SchusterThesis.pdf-74-33.png](SchusterThesis.pdf-74-33.png)

![SchusterThesis.pdf-74-35.png](SchusterThesis.pdf-74-35.png)

![SchusterThesis.pdf-74-36.png](SchusterThesis.pdf-74-36.png)

![SchusterThesis.pdf-74-37.png](SchusterThesis.pdf-74-37.png)

![SchusterThesis.pdf-74-38.png](SchusterThesis.pdf-74-38.png)

![SchusterThesis.pdf-74-39.png](SchusterThesis.pdf-74-39.png)

![SchusterThesis.pdf-74-40.png](SchusterThesis.pdf-74-40.png)

![SchusterThesis.pdf-74-41.png](SchusterThesis.pdf-74-41.png)

atom lifetime 1 / 61 ns 30 ms 7 ps 2  s

![SchusterThesis.pdf-74-43.png](SchusterThesis.pdf-74-43.png)

![SchusterThesis.pdf-74-44.png](SchusterThesis.pdf-74-44.png)

![SchusterThesis.pdf-74-45.png](SchusterThesis.pdf-74-45.png)

![SchusterThesis.pdf-74-46.png](SchusterThesis.pdf-74-46.png)

![SchusterThesis.pdf-74-47.png](SchusterThesis.pdf-74-47.png)

![SchusterThesis.pdf-74-48.png](SchusterThesis.pdf-74-48.png)

![SchusterThesis.pdf-74-49.png](SchusterThesis.pdf-74-49.png)

atom transit time t transit  50  s 100  s  


![SchusterThesis.pdf-74-2.png](SchusterThesis.pdf-74-2.png)

![SchusterThesis.pdf-74-10.png](SchusterThesis.pdf-74-10.png)

![SchusterThesis.pdf-74-18.png](SchusterThesis.pdf-74-18.png)

![SchusterThesis.pdf-74-26.png](SchusterThesis.pdf-74-26.png)

![SchusterThesis.pdf-74-34.png](SchusterThesis.pdf-74-34.png)

![SchusterThesis.pdf-74-42.png](SchusterThesis.pdf-74-42.png)

critical atom number N 0 = 2 /g 2 6  10  3 3  10  6 1.1  6  10  5


![SchusterThesis.pdf-74-50.png](SchusterThesis.pdf-74-50.png)

![SchusterThesis.pdf-74-51.png](SchusterThesis.pdf-74-51.png)

![SchusterThesis.pdf-74-52.png](SchusterThesis.pdf-74-52.png)

![SchusterThesis.pdf-74-53.png](SchusterThesis.pdf-74-53.png)

![SchusterThesis.pdf-74-54.png](SchusterThesis.pdf-74-54.png)

![SchusterThesis.pdf-74-55.png](SchusterThesis.pdf-74-55.png)

![SchusterThesis.pdf-74-56.png](SchusterThesis.pdf-74-56.png)

![SchusterThesis.pdf-74-57.png](SchusterThesis.pdf-74-57.png)

critical photon number m 0 =  2 / 2 g 2 3  10  4 3  10  8 0.5  1  10  6


![SchusterThesis.pdf-74-58.png](SchusterThesis.pdf-74-58.png)

![SchusterThesis.pdf-74-59.png](SchusterThesis.pdf-74-59.png)

![SchusterThesis.pdf-74-60.png](SchusterThesis.pdf-74-60.png)

![SchusterThesis.pdf-74-61.png](SchusterThesis.pdf-74-61.png)

![SchusterThesis.pdf-74-62.png](SchusterThesis.pdf-74-62.png)

![SchusterThesis.pdf-74-63.png](SchusterThesis.pdf-74-63.png)

![SchusterThesis.pdf-74-64.png](SchusterThesis.pdf-74-64.png)

![SchusterThesis.pdf-74-65.png](SchusterThesis.pdf-74-65.png)

# of vacuum Rabi flops n Rabi = 2


 2 + g   10  5 1.3  10 2


![SchusterThesis.pdf-74-66.png](SchusterThesis.pdf-74-66.png)

![SchusterThesis.pdf-74-67.png](SchusterThesis.pdf-74-67.png)

![SchusterThesis.pdf-74-68.png](SchusterThesis.pdf-74-68.png)

![SchusterThesis.pdf-74-69.png](SchusterThesis.pdf-74-69.png)

![SchusterThesis.pdf-74-70.png](SchusterThesis.pdf-74-70.png)

![SchusterThesis.pdf-74-71.png](SchusterThesis.pdf-74-71.png)

![SchusterThesis.pdf-74-72.png](SchusterThesis.pdf-74-72.png)

![SchusterThesis.pdf-74-73.png](SchusterThesis.pdf-74-73.png)

![SchusterThesis.pdf-74-76.png](SchusterThesis.pdf-74-76.png)

![SchusterThesis.pdf-74-74.png](SchusterThesis.pdf-74-74.png)

![SchusterThesis.pdf-74-75.png](SchusterThesis.pdf-74-75.png)

![SchusterThesis.pdf-74-77.png](SchusterThesis.pdf-74-77.png)

![SchusterThesis.pdf-74-78.png](SchusterThesis.pdf-74-78.png)

![SchusterThesis.pdf-74-79.png](SchusterThesis.pdf-74-79.png)

![SchusterThesis.pdf-74-80.png](SchusterThesis.pdf-74-80.png)

![SchusterThesis.pdf-74-81.png](SchusterThesis.pdf-74-81.png)

![SchusterThesis.pdf-74-82.png](SchusterThesis.pdf-74-82.png)

Table 3.2: Key rates and parameters for atomic [Hood2000] and microwave [Raimond2001] atomic
systems using 3D cavities, semiconductors [Reithmaier2004, Yoshie2004] and superconducting circuits. For the 1D superconducting system, a full-wave ( L =  ) resonator,  r / 2  = 10 GHz, a
relatively low Q of 10 4 and coupling  = C g /C  = 0 . 1 are assumed. For the 3D microwave case, the
number of Rabi flops is limited by the transit time. For the 1D circuit case, the intrinsic Cooper-pair
box decay a conservative value equal to typical experimental   1 / (2  s) is assumed.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 73

####### 3.4 ####### Measurement Theory

######### 3.4.1 ######### Quantum Non-Demolition Measurements

Measurement is the process of coupling a small ephemeral system quantity, A , to a robust quantity,

M , of a meter system. Quantum mechanically, this is done by performing a projective measurement

with a measurement operator  M  A  , with  characterizing the measurement strength. An ideal

classical measurement maps the system state to the measurement apparatus perfectly and without

destroying the original state. However, even assuming that the meter is otherwise independent of the

system, the Heisenberg uncertainty principle requires that reducing the uncertainty in one system

variable (measuring A ) increases the uncertainty in (modifies) another conjugate system variable. To

illustrate this effect concretely, imagine two quantities measured by the operators A  and B  . If both

operators leave the state they measure intact, then the order of measurement should not matter,

and the following quantity should be zero.

A  B  |   B  A  |   = [ A,  B  ] | S  (3.85)

If the commutator [ A,  B  ] is zero, then a measurement of A does not effect a measurement of B ,

though it may change  . Because an operator always commutes with itself, it is possible in principle

to measure an observable and then faithfully obtain the same result many times. In order to perform

repeated measurements over a finite period of time, the measurement operator (or state property)

cannot change during the measurement process, implying


d M  A 


M A = 1

![SchusterThesis.pdf-75-0.png](SchusterThesis.pdf-75-0.png)

![SchusterThesis.pdf-75-1.png](SchusterThesis.pdf-75-1.png)

dt i



[  M A,  H  ] = 0 (3.86)
i 


When equation 3.86 is satisfied, repetitions are possible, and the measurement is said to be quantum

non-demolition (QND). Demolition can occur either if the probe is not exactly along the desired

measurement axis, or if the observable itself is not an eigenstate of the Hamiltonian. QND measure-

ments are important because in addition to allowing more faithful measurements, the same type of

interactions generate entanglement, which can be used to generate logic gates.

######### 3.4.2 ######### Mapping Qubit State onto Cavity State

The interaction between the cavity and the qubit can be used to map the qubit state onto the phase

or amplitude of the cavity photons. A single qubit can be mapped on to many photons, giving energy

gain, which can be used to overcome any detector inefficiencies, such as photons lost in the line, or


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 74


a) b)


bias T Cin Cout RF amp


Cin


Cout



|C|Col2|
|---|---|

||Col2|
|---|---|


![SchusterThesis.pdf-76-0.png](SchusterThesis.pdf-76-0.png)

![SchusterThesis.pdf-76-1.png](SchusterThesis.pdf-76-1.png)

![SchusterThesis.pdf-76-2.png](SchusterThesis.pdf-76-2.png)

Gate Charge, n g =C g V g /e

Figure 3.16: a) Simplified measurement schematic. The amplifier adds k B T N B of noise for an
effective efficiency  =   r /k B T N . The CPB box acts as a state dependent capacitance which adds
to the resonator capacitance, shifting its resonance frequency. b) Energy levels and derivatives of
the CPB vs. gate charge. Measurements of the CPB can use the charge, which is similar to the
first derivative of the energy, or the effective capacitance which (at low frequencies) is related to the
curvature of the bands.

masked by noise inside the amplifier. First, let us describe the interaction in electrical engineering

terms. The CPB acts as a capacitor except near degeneracy where there is an avoided crossing. For

a capacitor E = CV 2 / 2 and one can define a dynamical capacitance by the relation



d 2 E
C = (3.87)

![SchusterThesis.pdf-76-3.png](SchusterThesis.pdf-76-3.png)

dV 2

As shown in Fig. 3.16 the capacitance is approximately constant (and state-independent) everywhere

except near n g = 1, where it becomes positive or negative depending on the state. This quantum

capacitance [Widom1984, Averin2003] will load the resonator differently depending on the qubit

state, changing its resonance frequency slightly. Because both the capacitance of the CPB and

the resonator impedance are purely reactive, or dispersive, no energy is deposited on the chip, an

important property since excess energy can excite quasi-particles [Lutchyn2005, Lutchyn2006] or two-

level fluctuators [Simmonds2004]. Because it can be so non-invasive, the technique has since been

adapted to make dispersive readouts of other systems like single Cooper pair transistors [Duty2005].

This semiclassical argument should be considered the low frequency limit of a more general dipole

coupling. It is valid when variations in gate voltage are very slow compared to the transition

frequency. At high frequencies, the simple dynamical capacitance argument gets the sign wrong,

and at high E J /E C the simple argument incorrectly predicts that the capacitance goes to zero. It

is more appropriate to treat the system quantum mechanically, where the frequency shift of the

resonator can be computed directly by diagonalization. One can avoid this confusion entirely by


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 75


a) b)

1.0


 /2


0.8

0.6

0.4

0.2

0.0


|g  |e  |g  |e


 /2


![SchusterThesis.pdf-77-0.png](SchusterThesis.pdf-77-0.png)

![SchusterThesis.pdf-77-1.png](SchusterThesis.pdf-77-1.png)

 2 


0 1 2  2  1 0 1 2

 r/   r/ 


Figure 3.17: State dependent transmitted amplitude ( a ) and phase ( b ) of the resonator in the qubit
ground (blue) and excited (red) states, as well as the bare resonator spectrum (dashed). The peaks
are located at   and can be distinguished either by measuring in amplitude or in phase.

looking directly at the dispersive Hamiltonian (Eq. 2.2 repeated below).

######### 3.4.3 ######### Distinguishing Cavity States

The following discussion is based on the steady state solutions derived in reference [Gambetta2006],

which contains more detailed derivations and transient effects that can lead to additional inhomo-

geneous broadening, and number splitting (discussed in section 8.3).

H   (  r +  z ) a  a + 1 / 2 +   a  z / 2 (3.88)
 

The first term in the dispersive Hamiltonian describes a cavity, which now has a resonance

frequency,  r  , where  = g 2 / is a qubit state dependant frequency shift. The problem of


measuring the CPB can now be rephrased as the problem of determining the frequency of the

cavity. The cavity is interogated with a coherent drive of amplitude (inside the cavity),  rf , at a

detuning of  rf =  RF   r from the bare resonator frequency. The coherent state phasor inside the

cavity is


 rf
  =  in +  out +


![SchusterThesis.pdf-77-2.png](SchusterThesis.pdf-77-2.png)

 in +  out


(3.89)
+ i (  rf  )



![SchusterThesis.pdf-77-3.png](SchusterThesis.pdf-77-3.png)

with amplitudes


|   | 2 = n  = (  in +  out ) 2  2 rf


![SchusterThesis.pdf-77-4.png](SchusterThesis.pdf-77-4.png)

(  in +  out )


rf (3.90)

+ (  rf  ) 2



![SchusterThesis.pdf-77-5.png](SchusterThesis.pdf-77-5.png)

The amplitude inside the cavity is related to the input amplitude by  rf =  in   in . The amplitude


![SchusterThesis.pdf-77-6.png](SchusterThesis.pdf-77-6.png)

of the transmitted wave (to the amplifier) is related to the cavity amplitude 1 as  out =  rf   in .

![SchusterThesis.pdf-77-7.png](SchusterThesis.pdf-77-7.png)

![SchusterThesis.pdf-77-8.png](SchusterThesis.pdf-77-8.png)

1 Note that  in ,  rf , and  out have different units. This is due to some issues in the way discrete and continuous
modes are normalized.


2


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 76


-5


![SchusterThesis.pdf-78-1.png](SchusterThesis.pdf-78-1.png)

![SchusterThesis.pdf-78-0.png](SchusterThesis.pdf-78-0.png)

-5


Re[  ]


Figure 3.18: Plot in phase space of the Q-function defined in Eq. 3.91, which shows the probability
of measuring a given coherent state. This would be the plot of the superposition |  +  + |    with
n = 16 photons. Since the q-function of a coherent state is a gaussian, the overlap of the states
can be expressed in terms of the distance between their centers  D =  + +  2 . It is often useful
|  |
to think about this distance per photon, equivalent to sin  0 , where  0 = arctan(2 / ). In this plot
the  states are symmetric about the real axis ( r = 0) and  0 = / 2, which is typically optimal
|  
for measurement.

Coherent states are conveniently plotted in phase space (see Fig. 3.18), where the amplitude and

phase of the wave are the radius and angle respectively. The probability distribution or Q function,

can be expressed as

Q ( ,  )   |    |   (3.91)

which if |   = |   is a coherent state then the overlap probability is

Q ( ,  ) = exp(  D 2 ) (3.92)

where the distinguishability D 2 = |  +    | 2 , can be thought of as the information about the

qubit state stored in the cavity. From figure 3.18 one can see that this quantity represents the

difference in IQ space of the coherent states associated with either qubit state, or more practically

the difference signal when the cavity is measured at the optimal phase. The cavity is not really a

classical meter, having coherent dynamics of its own, therefore we will say the information becomes

classical or measured once it leaves the cavity. Information leaks out of the cavity to the amplifier

at rate [Gambetta2006]



D out
 m =


( n + + n )  2 
 (3.93)

![SchusterThesis.pdf-78-3.png](SchusterThesis.pdf-78-3.png)

 2 r + (  in +  out ) 2 / 4 +  2


![SchusterThesis.pdf-78-2.png](SchusterThesis.pdf-78-2.png)

While the qubit is being measured it also has a rate of decay  , limiting the integration time before

the qubit state changes. Therefore one should compare the measurement rate to its decay rate to


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 77


1.0

0.8

0.6

0.4

0.2

0.0


1.0


|g  |e   0 =2  / 


0.5


0.0

 0.5

 1.0

||g =g2/|Col2||e|
|---|---|---|


![SchusterThesis.pdf-79-0.png](SchusterThesis.pdf-79-0.png)

 10  5 0 5 10

 r/ 


 10  5 0 5 10

 r/ 


Figure 3.19: State dependent transmitted amplitude ( a ) and phase ( b ) of the resonator in the qubit
ground (blue) and excited (red) states, as well as the bare resonator spectrum (dashed). The peaks
are located at   and though they overlap significantly they can be distinguished by measuring the
phase shift of transmitted photons.

compute a dimensionless signal-to-noise ratio (SNR)



  m
SNR =


(3.94)


![SchusterThesis.pdf-79-1.png](SchusterThesis.pdf-79-1.png)

where  =   r /k B T N and T N is the noise temperature of the amplifier in Fig. 3.18a.

######### 3.4.4 ######### Small Phase Shift Limit

Before continuing with the formal optimization of the measurement efficiency it is instructive to

explore the small phase shift limit. This limit is both simplest to understand and most important

for small couplings or large detunings. Most of the intuition gained here can be applied to some


extent in the large shift limit. As before, the cavity is given a dispersive frequency shift g  2 which


![SchusterThesis.pdf-79-2.png](SchusterThesis.pdf-79-2.png)

will be assumed small when compared to the cavity linewidth  (see Fig. 3.19). In this limit, the

ground excited state phase shift is  0 = 2 g 2 /   . The amount of signal can be calculated very easily.

If the local oscillator phase is adjusted so that the transmitted tone is in-phase then the out-of-

phase (quadrature) component of the transmitted signal will by definition be null. The qubit state

dependent phase shift will manifest itself as an increase of the quadrature transmission coefficient,

sin 2 (  0 ), which was expressed more fully as D this distance between the blobs in Fig. 3.18. The

signal in power will be the change in coefficient times the average number of photons, n , in the cavity

![SchusterThesis.pdf-79-3.png](SchusterThesis.pdf-79-3.png)

and the rate,  , that they pass through the cavity. For a given integration time (usually related to

T 1 ) this signal is to be compared with effective number of noise photons, k B T N /   r , of the amplifier.


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 78

This yields an expression for the signal to noise,


SNR = sin 2 (  0 )   r  T



 r  T 1 4g 4 T 1

k B T N   2 



4 T 1   r

![SchusterThesis.pdf-80-1.png](SchusterThesis.pdf-80-1.png)

![SchusterThesis.pdf-80-2.png](SchusterThesis.pdf-80-2.png)

 2  k B T


(3.95)
k B T N


![SchusterThesis.pdf-80-0.png](SchusterThesis.pdf-80-0.png)

What this equation says is that when in the small phase shift limit, the vacuum Rabi coupling,

g , is extremely important. Also important are T 1 and the noise temperature of the amplifier, T N .

While this form gives an intuition for the signal-to-noise, one must be careful to only apply it when

g 2 /    . Because can be tuned, if one is in the strong limit ( g > ,  ) then it is always possible

to violate this approximation. However, by using the formalism introduced above it is possible to

optimize the SNR for arbitrarily strong dispersive shifts.

######### 3.4.5 ######### Optimizing SNR

The signal-to-noise ratio depends on many variables, and some of those variables are implicitly linked

by both theoretical constraints (the break down of the dispersive limit), and practical constraints

(limits on ability to fabricate devices with arbitrary g ,  r , etc.). While the exact optimization

depends on the specific experiment being performed, in this subsection, the SNR is optimized under

various typical experimental limits. A specific warning is that while the general ideas apply to

the high E J /E C qubits, the smaller anharmonicity in such qubits means that one must take into

account the presence and location of several auxiliary levels which can significantly alter the SNR.

Under nearly all circumstances increasing  in lowers SNR by making it less sensitive without

increasing the rate of photons leaking to the amplifier. In principle, one could make it identically

zero and use a one-sided cavity, but as a practical matter it is easier to measure in transmission than

reflection because the amplifier is not disturbed by control pulses reflected from the cavity. Instead

one typically works in the limit  in   out but with  in large enough that  in can be made large

enough to achieve the desired  rf .

If the formula for  m (Eq. 3.93) held for any photon number, then it would be possible to achieve

arbitrary SNR, but at high enough photon numbers the dispersive Hamiltonian (Eq. 3.88) breaks

down, mixing occurs, and parasitic modes can be excited. A typical constraint is to maximize

the SNR at a given photon number 1 , but which photon number, n + , n , or ( n + + n ) should be
 

constrained? In order for one to never exceed a specified photon number when measuring either

the ground or excited state one should constrain max[ n + , n  ]. With this additional constraint, one

![SchusterThesis.pdf-80-3.png](SchusterThesis.pdf-80-3.png)

1 Note that for a given n  that  rf must be adjusted based on the values of  ,  out , and  r .


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 79


0.8

0.6

0.4

0.2


0.8

0.6

0.4

0.2


![SchusterThesis.pdf-81-0.png](SchusterThesis.pdf-81-0.png)

![SchusterThesis.pdf-81-1.png](SchusterThesis.pdf-81-1.png)

![SchusterThesis.pdf-81-2.png](SchusterThesis.pdf-81-2.png)

-4 -2


 r


-4 -2 0 2 4
 r


Figure 3.20: a) Plot of SNR at fixed  ,  , and max[ n + , n ] = n max vs  r . The optimum is created

by the intersection of the constraints on n + and n rather than by a local maximum in SNR [ r ]. b)

Plot of n + (blue dashed) and n (red solid) vs  r . Because SNR is always improved by increasing

n , one of the two amplitudes is always constrained. Deviations from optimum  r lose signal to

noise because they decrease one of n from n max .


can find the optimum  r , whose main effect is to control the ratio n + /n  . As can be seen from

Fig. 3.20, SNR is maximized when n + = n and  r = 0. Using this information, the optimal SNR


can be simplified to




SNR = 


n 2

![SchusterThesis.pdf-81-4.png](SchusterThesis.pdf-81-4.png)

(3.96)

![SchusterThesis.pdf-81-5.png](SchusterThesis.pdf-81-5.png)
 2 / 4 +  2


![SchusterThesis.pdf-81-3.png](SchusterThesis.pdf-81-3.png)

where n = ( n + + n ) / 2 and  =  in +  out  out . First lets take Eq. 3.96 at face value and
 

![SchusterThesis.pdf-81-6.png](SchusterThesis.pdf-81-6.png)

optimize assuming control at design of  and  , but that n and  are fixed constants which cannot

![SchusterThesis.pdf-81-7.png](SchusterThesis.pdf-81-7.png)

be changed.

At constant n and  , and assuming that cannot be made infinitely small (as the dispersive

![SchusterThesis.pdf-81-8.png](SchusterThesis.pdf-81-8.png)

limit breaks down), at the optimum point  = / 2 (see Fig. 3.21) the phase difference between  +


and  is / 2 and




n

![SchusterThesis.pdf-81-9.png](SchusterThesis.pdf-81-9.png)
SNR =


(3.97)


![SchusterThesis.pdf-81-10.png](SchusterThesis.pdf-81-10.png)

Unfortunately, even ideally, the maximum number of photons n is not independent of g ,  ,and

![SchusterThesis.pdf-81-11.png](SchusterThesis.pdf-81-11.png)

, but is limited (by the dispersive limit) to a maximum (see Eq. 2.6) n crit =  2 / 4 g 2 . This extra

dependence does not change the optimum point of  = / 2, but the extra condition makes the

maximum SNR



ng 2

![SchusterThesis.pdf-81-12.png](SchusterThesis.pdf-81-12.png)
SNR =



ng 2

= 

![SchusterThesis.pdf-81-13.png](SchusterThesis.pdf-81-13.png)

![SchusterThesis.pdf-81-14.png](SchusterThesis.pdf-81-14.png)
2  N


(3.98)
N 0


where N 0 = 2 /g 2 is the critical atom number often used in traditional cavity QED to measure

how many atoms must be used to detect a single photon in the cavity. In the strong coupling limit

by definition, N 0 1, allowing single shot measurement with an ideal detector. Complications



-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 80

1.5


0.5


![SchusterThesis.pdf-82-0.png](SchusterThesis.pdf-82-0.png)

 /2 

Figure 3.21: Plot of SNR vs. / 2  , with insets demonstrating transmission of  + (red) and 

(blue) to show effect of / 2  . When   2  , photons exit the cavity out very fast but they carry
very little information. When   2  , each photon carries a full bit of information, but because
 is small they dont come out fast enough to acquire that information in a T 1 . Thus, one would
increase  to get photons faster until the two states begin to have significant overlap at the optimum
 = 2  .


may arise even at the smaller critical photon number n = n  =    2 , where the cavity becomes

![SchusterThesis.pdf-82-1.png](SchusterThesis.pdf-82-1.png)

![SchusterThesis.pdf-82-2.png](SchusterThesis.pdf-82-2.png)

inhomogeneously broadened due to its inherited non-linearity from the qubit. In the future, it may

be possible to use this non-linearity as an asset to make a latching measurement of the qubit state as

is done with the Josephson Bifurcation Amplifier [Siddiqi2006], but for now the effect is treated as

a complication to be avoided. In the limit of  constant and n = n  , SNR is maximized by making

![SchusterThesis.pdf-82-3.png](SchusterThesis.pdf-82-3.png)

 while still being small compared to  r .



  2 / 4 2  r 5

![SchusterThesis.pdf-82-5.png](SchusterThesis.pdf-82-5.png)

![SchusterThesis.pdf-82-6.png](SchusterThesis.pdf-82-6.png)

 2 / 4 +  2 4 g 4  +






SNR =


  2 / 4


2  r 5 2  r

![SchusterThesis.pdf-82-7.png](SchusterThesis.pdf-82-7.png)

4 g 4  +  4 




(3.99)


![SchusterThesis.pdf-82-4.png](SchusterThesis.pdf-82-4.png)

If this expression does not make a lot of sense, that is partially because it is not terribly realistic.

If the qubit is very long lived then even well into the dispersive limit (4 ng 2 /  2  1) the decay into

cavity modes may contribute to the total decay rate  =   +   , meaning that  can no longer

be treated as a constant in the optimization. The Purcell effect (Eq. 2.11 and appendix B) gives

  = ( g 2 /  2 )  .

To get a feel for the effect of   let us temporarily work in the limit where  = 0. This means


that without   one could measure forever achieving arbitrary SNR, so the optimum in Eq. 3.99


occurs as   0



g
SNR =



g 2 n

![SchusterThesis.pdf-82-9.png](SchusterThesis.pdf-82-9.png)

![SchusterThesis.pdf-82-8.png](SchusterThesis.pdf-82-8.png)

![SchusterThesis.pdf-82-10.png](SchusterThesis.pdf-82-10.png)

 2 g 2 /  2


n  2

n
g 2 /  2 +  2 / 4  g 2


(3.100)

![SchusterThesis.pdf-82-12.png](SchusterThesis.pdf-82-12.png)
g 2


![SchusterThesis.pdf-82-11.png](SchusterThesis.pdf-82-11.png)

The above equation states the obvious result, that when  is infinite then one must be as dispersive


as possible, trading speed (   0) for longevity. When n crit is factored in, the dispersiveness counts


-----


CHAPTER 3. CAVITY QED WITH SUPERCONDUCTING CIRCUITS 81

double, limiting the number of photons and the lifetime making SNR =  ( 4 / 4 g 4 ). This points

to a looming obstacle, whereby as qubits become more long lived one will have to measure more

slowly. This issue could be circumvented by having a  that can be pulsed on and off, which could

be implemented by coupling to the outside world through a junction or other qubit.

For current experiments,  is anything but negligible. Letting  be held constant (since it
 

seems to be relatively independent of any variable we have measured it against), and allowing   to

enter the optimization one can find the optimal   at fixed photon number


  =  (  ) 2 (3.101)
 2 


![SchusterThesis.pdf-83-0.png](SchusterThesis.pdf-83-0.png)

substituting   into Eq. 3.96 and optimizing to find   ( g 2  ) 1 / 3 the SNR becomes


4 ng 2 4

![SchusterThesis.pdf-83-1.png](SchusterThesis.pdf-83-1.png)

(2 g (  / ) 1 / 2 +  ) 2 = 9

![SchusterThesis.pdf-83-3.png](SchusterThesis.pdf-83-3.png)

![SchusterThesis.pdf-83-2.png](SchusterThesis.pdf-83-2.png)

![SchusterThesis.pdf-83-4.png](SchusterThesis.pdf-83-4.png)



g

![SchusterThesis.pdf-83-5.png](SchusterThesis.pdf-83-5.png)






1 / 3
(3.102)



4 ng 2
SNR = 






At n crit the pressure to be dispersive is strong enough that one wants to make as large as possible

once more yielding


g 2  4 
SNR =


g 2  4  

(   2 + g 2  )(4 g 4 +  2  2 )  N

![SchusterThesis.pdf-83-6.png](SchusterThesis.pdf-83-6.png)

![SchusterThesis.pdf-83-7.png](SchusterThesis.pdf-83-7.png)



(3.103)
N 0


Exercise 3.4.1. Show that the Q-function of two coherent states is

Q ( ,  ) = exp( |    | 2 )


-----


### Chapter 4

## Decoherence in the Cooper Pair Box

This chapter will focus on the decoherence properties of the CPB, both inside and outside of a

cavity. The first section will discuss relaxation and mixing processes which incoherently change the

state of the qubit. The second section discusses dephasing, a form of decoherence which does not

cause the qubit to change state but results in noise in the relative phase of superpositions of the two

states. In addition to identifying mechanisms which impede progress in quantum computing, and

obscure aspects of cavity QED, studying decoherence in the CPB provides a tool to measure quantum

noise [Schoelkopf2001], a window onto the underlying physics of the decoherence mechanisms, and a

concrete test-bed for observing the collapse of a quantum wavefunction. In both cases the focus will

be to optimize the design of the CPB rather than developing the exact lineshapes or functional form

of the phase correlator. Good references for these topics include [Cottet2002] and [Martinis2003].

####### 4.1 ####### Relaxation and Heating

This section closely follows Qubits as Spectrometers reference [Schoelkopf2001], and complete

derivations of the results presented here are provided in that work. Heating and relaxation are

processes which excite and de-excite the qubit. They can be thought of as arising from random

fluctuations at the transition frequency connecting the ground and excited states. Relaxation can

be thought of as a perturbation

H 1 =   M  (4.1)

82


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 83

coupling a qubit operator   , to a bath operator M  . For weak noise sources the excitation (  ) and

relaxation (  ) transition rates are given by Fermis golden rule (FGR)


  =  1 2 |  g |   | e | 2 S M (   a ) (4.2)

![SchusterThesis.pdf-85-0.png](SchusterThesis.pdf-85-0.png)

where S M (  a ) is the spectral density of the bath noise. It is often more convenient to characterize


these upward and downward transition rates in terms of the (energy) relaxation time which is the

inverse sum of the rates

T 1 = 1 / ( +  ) (4.3)
 

and the steady state polarization p is given by



 
p =   



     = S M (  a )  S M (   a

![SchusterThesis.pdf-85-1.png](SchusterThesis.pdf-85-1.png)

![SchusterThesis.pdf-85-2.png](SchusterThesis.pdf-85-2.png)

  +   S M (  a ) + S M (   a


(4.4)
S M (  a ) + S M (  a )



The polarization ranges from p = 1 when the qubit ensemble is completely in the ground state to

p =  1 if the qubit population is completely inverted, and is said to be completely depolarized when

p = 0. Because the qubit transition selects a particular frequency, the qubit acts as a spectrometer

of noise at the transition frequency [Schoelkopf2001]. Further, unlike a classical spectrometer the

qubit distinguishes between the positive (qubit emits) and negative (qubit is excited) frequency

components of the noise. The total magnitude of the noise is given by 1 /T 1 where the ratio of

positive to negative frequency components can be deduced from the polarization, p . The process of

investigating relaxation and heating can thus be thought of as identifying sources of environmental

noise, S M , understanding the system matrix elements, g A e , and coupling rates to each source of
 | | 

noise. The rest of this section will consist of relaxation (heating) processes and models for how they

couple to the CPB.

######### 4.1.1 ######### Voltage Noise

The CPB is primarily controlled through a gate voltage coupled to the electrostatic part of the

Hamiltonian via a (not-so) small gate capacitor. The strength of this coupling can be found as in

section 3.3 and similarly to Eq. 3.72 of that section, is given by

  V = 2 eV g N  (4.5)

By creating a channel for electrostatic control we have also created a means for decay (or heat-

ing). If the qubit is coupled to an electrical environment with impedance Z (  ) then the associated


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 84





0.5

0.4

0.3

0.2

0.1



########## V


########## C

|Bath Emission T=250 mK T=50 mK T=100 mK|Bath Absorption T=0 K|
|---|---|


-10 -5 0 5 10

|Cg Z()  = C 2(C|Col2|
|---|---|
|2(C j E J||
|||
|||


Frequency H GHz L

Figure 4.1: a) When coupling to the box via a gate capacitance, one opens a channel for decoherence.
The impedance presented by the source, as well as the voltage division  between the gate capacitance
and junction capacitance, will be critical factors in determining the decoherence. b) Plot of the
voltage spectral density S V (  ) at different temperatures in units of S V (0) = 2 k B T R at T = 1 K .
At high temperatures and low frequencies the spectral density is relatively symmetric about  =
0. However at high frequencies   > k B T , most notably at T = 0, the spectral density is very
asymmetric. It is zero for frequencies  < 0 (at T = 0 the bath cannot emit) and linear (   R ) in
frequencies  > 0 (the bath can still absorb).

voltage noise of that environment is given by the Johnson-Nyquist formula, which resembles a one-

dimensional blackbody (Bose-Einstein) and is described by the voltage spectral density



2   Re[Z(  )]
S V (  ) =  


``   (4.6)

![SchusterThesis.pdf-86-0.png](SchusterThesis.pdf-86-0.png)

![SchusterThesis.pdf-86-1.png](SchusterThesis.pdf-86-1.png)
k B T


One thing to note about to about Eq. 4.6 is that at low temperatures the voltage noise is not


1  e


symmetric in positive and negative frequencies. This inherently quantum mechanical property has a

straight forward meaning. At low temperatures there is not enough energy ( k B T <   ) to emit any

photons and therefore the positive frequency side will approach zero. However, even at absolute zero

the environment can absorb photons leaving only a voltage spectral density at positive frequencies.

S V (  ) 2  Re [ Z (  )] (4.7)
 

The effective decay rate at low temperatures is thus


 V = 16  2  a Re [ Z (  a )]


Z (  a )] g N  e 2 = 2  g 2

R K |  | | | 


(4.8)

![SchusterThesis.pdf-86-3.png](SchusterThesis.pdf-86-3.png)
 a


![SchusterThesis.pdf-86-2.png](SchusterThesis.pdf-86-2.png)

where R K = h/e 2 is the resistance quantum. The lifetime T 1 = 1 /  is enhanced by having a


small real environmental impedance Re [ Z (  a )], and by reducing the coupling (  and g N  e ) of
 | | 


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 85

the transition to that impedance.

The dependence on  g | N  | e  gives the decay rate a dependence on the bias charge, n g (see

Fig. 3.13). In the charge regime one can make the approximation



1
 g | N  | e 



1 E

2 sin  m = 2


E J E J

16 E C 2 (1 n g ) + E J 2  2 

![SchusterThesis.pdf-87-1.png](SchusterThesis.pdf-87-1.png)

![SchusterThesis.pdf-87-3.png](SchusterThesis.pdf-87-3.png)

![SchusterThesis.pdf-87-2.png](SchusterThesis.pdf-87-2.png)




(4.9)
2  a


![SchusterThesis.pdf-87-0.png](SchusterThesis.pdf-87-0.png)

This means that the decay rate should be approximately independent of gate charge. It is perhaps

better to think about a normalized measure of the coherence, the relaxation quality factor Q 1 =

 a / , which can be thought of as the number of oscillations the qubit makes before decaying. So

at fixed  a the quality factor is maximized by having E J /    a and implicitly operating at small

bias charge ( n g  0). However, as discussed in section 3.2, having very small E J means that there is

no way to change the qubit state. Though at n g = 1 the matrix element is maximal, it only rises to

a constant of order unity  g | N  | e  1 / 2. In practice the dephasing due to low frequency voltage or

charge noise will make n g = 1 a more favorable operating point despite the price of faster relaxation.

The effective environmental impedance is typically or order 50, so for the traditional CPB the

lifetime is mainly determined by the choice of  . For these parameters Q 1 3 / 2 , meaning that


if the qubit is connected directly to a transmission line then it would decay almost immediately.

In principle the Q 1 due to voltage noise could be made arbitrarily large by making   1, but in

practice it is difficult to make  = C g /C  smaller than   1 aF / 1 fF for a traditional CPB implying

a maximum Q 1  10 6 . While this Q 1 would not limit current CPBs in the next section we will see

how one can improve the lifetime even more!

######### 4.1.2 ######### Voltage Noise Inside a Cavity

Observation of cavity QED phenomena and any non-local gates implemented via the cavity rely on

having the qubit strongly coupled to the cavity   0 . 1  1 which would appear to reduce the qubit

lifetime. Luckily, placing the CPB inside of a cavity allows one to control the impedance Z (  ) of the

environment (see Fig. 3.3), allowing larger coupling with similar or reduced decay. In the dispersive

limit ( g ), one can treat the qubit in a cavity as seeing an effective Re[Z(  a )] presented by the


cavity, which can be modeled by an LCR as in Eq. 3.3.


Z C
Re[Z LCR (  )] =


![SchusterThesis.pdf-87-4.png](SchusterThesis.pdf-87-4.png)

1 + (  a   r 2 )


( a /  2)  r 2 ) 2 (4.10)


![SchusterThesis.pdf-87-5.png](SchusterThesis.pdf-87-5.png)

At large detunings, the effective impedance seen by the qubit is much smaller then the characteristic

impedance of the resonator, dramatically enhancing the qubit lifetime (see Fig 4.2). This can be


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 86


10 8


10 6

10 4

10 2

10 0

|Fine structure limit|Col2|
|---|---|
|||



10 -5 10 -4 10 -3 10 -2 10 -1


10 9

10 7

10 5

10 3


![SchusterThesis.pdf-88-0.png](SchusterThesis.pdf-88-0.png)

10


coupling strength, g/  qubit frequency,  a  2  (GHz)


coupling strength, g/  qubit frequency,   2  (GHz)


Figure 4.2: Quality factor of qubits coupled to transmission line and cavity. a) Plot of Q 1 for a
qubit coupled to a bare transmission line as a function of the dimensionless coupling strength g/ a .
The dashed lines indicate the fine structure limit, where g/ is made maximal by setting  = 1.
At this maximum coupling strength the relaxation quality factor is only Q 1 40. b) Plot of the

relaxation Q 1 of the maximally coupled (  = 1) CPB inside of a cavity due to vacuum noise from
outside the resonator. Plot is shown for a cavity frequency  r / 2  = 5 GHz and Q = 10 , 000. The
qubit is in the charge regime  a = E J /  , and is fully coupled to the resonator and for detunings
 7
 > 10% the relaxation Q 1 > 10 .

thought of as an electrical engineering description of the Purcell Effect 1

Parasitic Cavity Modes

With great coupling, comes great responsibility...to control the environmental impedance! By placing

the qubit inside a cavity one can couple strongly while preventing the decay. In doing so one must

be especially careful not to excite any modes in which the impedance is not carefully controlled.

One must avoid any extra parasitic modes on the circuit board and inside the sample holder which

might couple to the CPB. Precautions taken in the design of the circuit board and sample holder

are discussed in chapter 5.

One particular suspected loss mode is the parasitic mode which may exist between the ground

planes of the resonator. In current designs, the CPB is placed in between one of the ground planes

and the center pin. The coupling can be thought of as driving a superposition of two modes, a mode

symmetrically (see Fig. 4.3a) driving a voltage between the center-pin and ground planes, and an

antisymmetric mode (see Fig. 4.3b) driving a voltage from one ground plane to the other. In the

![SchusterThesis.pdf-88-1.png](SchusterThesis.pdf-88-1.png)

Fermis Golden Rule assumes that if the qubit decays into the environment (in this case a cavity) that it immediately leaves and does not affect further dynamics of the system. This is effectively true when in the dispersive 1
limit, where the rate of real transitions is by definition small, and when the cavity decay rate is much faster than the
coupling rate (the weak limit). However this assumption breaks down in the strong coupling limit when the qubit
comes into resonance with the cavity because the photon can be reabsorbed by the qubit.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 87

a) b) c)

|Slotline mode|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||


![SchusterThesis.pdf-89-0.png](SchusterThesis.pdf-89-0.png)

![SchusterThesis.pdf-89-1.png](SchusterThesis.pdf-89-1.png)

![SchusterThesis.pdf-89-2.png](SchusterThesis.pdf-89-2.png)

![SchusterThesis.pdf-89-3.png](SchusterThesis.pdf-89-3.png)

![SchusterThesis.pdf-89-4.png](SchusterThesis.pdf-89-4.png)

![SchusterThesis.pdf-89-5.png](SchusterThesis.pdf-89-5.png)

![SchusterThesis.pdf-89-6.png](SchusterThesis.pdf-89-6.png)

![SchusterThesis.pdf-89-7.png](SchusterThesis.pdf-89-7.png)

Figure 4.3: The CPB in its current geometry effectively couples only the bottom ground plane
and the centerpin. If the two ground planes are not well grounded it is possible that this drives a
superposition of the desired CPW mode and a parasitic slot line mode which is not well defined.

design of the resonators and circuit board, care is taken to ensure the two ground planes are always

at the same potential, which would eliminate this uncontrolled antisymmetric mode. However due

to limitations of local fabrication equipment (inability to make on-chip superconducting vias), there

maybe some small but finite inductance between the ground planes. If this inductance presents an

effective impedance similar to the intended cavity impedance, then it might be a significant source

of decoherence. In addition to improved engineering reducing such impedance, one can also design

qubits which do not couple to the mode by symmetry.

The effect of flux noise on the qubit is very similar to that of voltage noise. However, instead of

coupling via a voltage division to the electrostatic component of the Hamiltonian, it couples to the

Josephson term via a magnetic inductance. Like the voltage noise, it depends both on the coupling of

the field to the qubit and on n g through the matrix elements. For small fluctuations, we can expand

the junction Hamiltonian H J in Eq. 3.62 around the bias point  to give a linearized coupling to

flux to give


   =    E J sum

![SchusterThesis.pdf-89-8.png](SchusterThesis.pdf-89-8.png)

 0


 
sin

![SchusterThesis.pdf-89-9.png](SchusterThesis.pdf-89-9.png)

 0




 
cos   + d cos

![SchusterThesis.pdf-89-10.png](SchusterThesis.pdf-89-10.png)

 0




   =    E J sum


sin   (4.11)


In the two state approximation the fictitious field picture developed in Fig. 3.12 and Eq. 3.68,

  can be thought of as a driving magnetic field. The part of the field that is perpendicular to the

quantization axis defined by the net field will drive the e  g transition. Using this fictitious field

picture


|  g |   | e | 2 = | B   B B 2 | 2 (4.12)

![SchusterThesis.pdf-89-11.png](SchusterThesis.pdf-89-11.png)

| |


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 88

######### a) ######### b) ######### 1
########## Z( ##########  ########## )

0.8


0.6

0.4

0.2


########## E ########## J2


![SchusterThesis.pdf-90-0.png](SchusterThesis.pdf-90-0.png)

0 0.5 1

![SchusterThesis.pdf-90-1.png](SchusterThesis.pdf-90-1.png)

Flux bias (  /  0 )

Figure 4.4: a. Circuit diagram showing how the environment can couple a flux to the CPB through a
mutual inductance M . b) Flux transition matrix element vs.  /  0 at different junction asymmetries
d = 0 . 01 , 0 . 1 , 0 . 25 , 0 . 5. They are very close to zero at  = 0 and as long as there is some asymmetry
go to 1 at  =  0 / 2. This occurs because at that point, even if the asymmetry is small it is exactly
perpendicular to the field so it couples with order unity. The size of d determines the robustness
(flatness) near  = 0.

Using this relation the FGR from Eq. 4.2, becomes



 2 S  (  )
  =  2  2


E J 4 d 2 + 16 E C 2 E J 2 (1 ng ) 2 sin 2    0



16 E C 2 (1 ng ) 2 + E J 2 sin  2     0


+ d 2 cos 2    0

2 cos 2     0






 2 S  (  )
  =


![SchusterThesis.pdf-90-3.png](SchusterThesis.pdf-90-3.png)

![SchusterThesis.pdf-90-4.png](SchusterThesis.pdf-90-4.png)

![SchusterThesis.pdf-90-5.png](SchusterThesis.pdf-90-5.png)

16 E C 2 (1 ng ) 2 + E J 2 sin 2    0


 


 (4.13)


![SchusterThesis.pdf-90-2.png](SchusterThesis.pdf-90-2.png)

+ d 2 cos 2    0


![SchusterThesis.pdf-90-6.png](SchusterThesis.pdf-90-6.png)

![SchusterThesis.pdf-90-7.png](SchusterThesis.pdf-90-7.png)

At the degeneracy point ( n g = 1) the expression no longer has any dependence on E C leaving



 2 S  (  )
  =  2  2



 2 S  (  )
  =


E J 2 d 2

![SchusterThesis.pdf-90-9.png](SchusterThesis.pdf-90-9.png)

+ d 2 cos 2    0


sin 2    0




(4.14)


![SchusterThesis.pdf-90-8.png](SchusterThesis.pdf-90-8.png)

![SchusterThesis.pdf-90-10.png](SchusterThesis.pdf-90-10.png)

![SchusterThesis.pdf-90-11.png](SchusterThesis.pdf-90-11.png)

and at the most favorable operating point ( n g = 1 and  = 0) this rate simplifies to



 2 d 2 S  (  )
  =  2


E J






2
(4.15)




 2 d 2 S  (  )
  =


![SchusterThesis.pdf-90-12.png](SchusterThesis.pdf-90-12.png)

![SchusterThesis.pdf-90-13.png](SchusterThesis.pdf-90-13.png)

If one biases the qubit flux with a current coupled to the CPB loop with a mutual inductance

M then one can rewrite S  in terms of S I the current fluctuations in the bias.


S  = M 2 S I = M 2 2  

![SchusterThesis.pdf-90-14.png](SchusterThesis.pdf-90-14.png)

Re [ Z (  )]


![SchusterThesis.pdf-90-15.png](SchusterThesis.pdf-90-15.png)

1  e


``   (4.16)

![SchusterThesis.pdf-90-16.png](SchusterThesis.pdf-90-16.png)
k B T


At T = 0, n g = 1, and  = 0, one can use Eqs. 4.15 and 4.16 to find the relaxation quality factor


Q  1 =    a


Q  1 = 


2  2 d 1 2 M 2 R E  2 2 0  (4.17)


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 89

######### 4.1.3 ######### Material Loss

Resistive (Quasiparticle) Loss

Even though the CPB is superconducting there can still be resistive loss. In this section we will

treat the superconductor in the two fluid model where residual normal fluid (quasiparticle) tunneling

across the junction in parallel with a finite Josephson inductance leads to loss. In section 4.3.5 a more

sophisticated treatment of quasiparticle loss will be applied which takes into account the density

of states. These quasiparticle losses in the CPB are analogous to resistive loss in the cavity due

to the finite kinetic inductance. The shunting in the CPB is actually even a bit worse because the

Josephson inductance L J   / 2 eI c = R K / 16  2 E J is typically larger than the total (magnetic and

kinetic) inductance of the cavity (the characteristic impedance Z CPB 50 . As for the cavity


(Eq. 3.33) the resistive quality factor is


Q res =


(4.18)

![SchusterThesis.pdf-91-0.png](SchusterThesis.pdf-91-0.png)
L J


Using the Ambegoakar-Baratoff relation one can express the critical current in terms of the super-

conducting gap and normal state resistance as



 
I c = tanh

![SchusterThesis.pdf-91-1.png](SchusterThesis.pdf-91-1.png)

2 eR n


![SchusterThesis.pdf-91-2.png](SchusterThesis.pdf-91-2.png)

2 k B T


(4.19)


At degeneracy ( n g = 1) for a traditional CPB the transition frequency is the Josephson energy

E J /  = I c / 2 e . The effective resistance should be inversely proportional to the normal population


+ n s = R n 1 + e 1 . 76 T c/T (4.20)

![SchusterThesis.pdf-91-3.png](SchusterThesis.pdf-91-3.png)

n n
 


n n + n s
R = R n


Substituting this into Eq. 4.18 yields


1 + e 1 . 76 T c /T (4.21)





E J
Q res = 8   



E J
Q res = 8 


R n

![SchusterThesis.pdf-91-5.png](SchusterThesis.pdf-91-5.png)

R


![SchusterThesis.pdf-91-4.png](SchusterThesis.pdf-91-4.png)

For a CPB with transition frequency E J /h 5 GHz, the ratio R n /R K 1. The exponential scaling
 


with temperature means that if the quasiparticle population is in equilibrium, then Q res should be

10 5 at 250 mK, and 10 20 by 50 mK. However, it is possible the effective quasiparticle temperature

is higher than the bath temperature. As long as the effective temperature is below  250 mK it

probably is not limiting the lifetime of the box.

Dielectric Loss

Another channel for decay is loss in dielectrics in which qubit electrical fields live. For this decay

mechanism one can think of a CPB as an LC resonator, whose Q 1 1 / tan  just like the cavities



-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 90

######### Electric Fields ######### Currents

|Electric Fields|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||||C g|


![SchusterThesis.pdf-92-0.png](SchusterThesis.pdf-92-0.png)

 C j C e

|Col1|C j|Col3|
|---|---|---|
||||


![SchusterThesis.pdf-92-1.png](SchusterThesis.pdf-92-1.png)

Figure 4.5: a. Electric fields in the CPB, black arrows represent E-field lines. Much of the field
is in the junctions which form an overlap capacitor with C j 4 fF of capacitance. Some of the

field is resides in the gate capacitance, C g and stray or intentional external capacitance C e . b.
Currents flowing through the CPB and induced currents in the ground plane. If there is a nonzero flux or asymmetry in the junctions, the amount of current flowing through each junction is
different, meaning that there is a net circulating current. This AC circulating current can induce
currents in nearby pieces of metal or radiate directly into the vacuum. If quasiparticles are present,
the Josephson inductance will shunt some current into the normal, resistive branch, reducing the
excited state lifetime.

in section 3.1.7. The electric fields of the CPB pass through many materials with potentially widely

varying loss tangents. Thus in addition to the materials themselves, the participation ratio of

field energy in each material is of paramount importance. A diagram of CPB fields and materials

is presented in figure 4.5. In a traditional CPB most of the electrical energy is stored in the

junction capacitance whose fields pass through a 1 2 nm thick tunnel barrier of AlO X . The loss


tangent of most materials is not that well known at low temperatures, and in fact our current


best lifetime T 1 10  s probably sets the current lower limit on the loss tangent of such a barrier


(tan  AlO X 10  5 10  6 ). One way to test whether this loss mechanism is limiting the current
 

qubit lifetimes is to add a shunting capacitor to the CPB. The electric fields of this capacitor will

ideally 1 live in the substrate which should have less loss. If the lifetime were to improve this would

implicate the junction dielectric losses.

Inductive Losses

Inductive losses can be treated in a similar manner to dielectric losses. Because the insulators used

have magnetic permeabilities very close to unity, one does not expect them to have much loss.

Ideally the superconductors would have no inductive loss, though as seen in section 3.1.7, even

![SchusterThesis.pdf-92-2.png](SchusterThesis.pdf-92-2.png)

1 Current fabrication processes can leave residue of unknown chemical composition and electrical properties near
the qubit. This may make the effective loss of planar capacitors larger than one would expect from the losses in the
Si /Sapphire/ SiO 2 substrate.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 91

superconductors may have some loss. Any magnetic fields in the normal metal circuit board might

also induce lossy currents. These mechanisms are not thought to be limiting factors, the loop is

quite small 10  m 2 compared to the distance to the nearest lossy material. It is possible that local

non-equilibrium effects, namely vortices, might present an additional inductive loss mechanism. The

magnetic fields produced by the qubit are nominally suppressed at zero flux bias if the junctions are

symmetric, and could be eliminated altogether by using a single junction.

######### 4.1.4 ######### Dipole Radiation

One can also calculate the energy radiated by an electric or magnetic dipole in free space. A CPB

in free space would have these as ultimate limits to its lifetime. As seen in section 4.1.2, placing

the CPB inside a cavity can enhance (or reduce) its lifetime dramatically. However these radiation

mechanisms still serve as useful scales of decoherence.

Electric Dipole Radiation

The power emitted by an electric dipole is given by [Griffiths1999]


 0

![SchusterThesis.pdf-93-0.png](SchusterThesis.pdf-93-0.png)
P ed =

![SchusterThesis.pdf-93-1.png](SchusterThesis.pdf-93-1.png)

 0




d 2 

![SchusterThesis.pdf-93-2.png](SchusterThesis.pdf-93-2.png)

![SchusterThesis.pdf-93-3.png](SchusterThesis.pdf-93-3.png)

 2 3


d 2


(4.22)


where d = q -  x  e   m is the CPB electric dipole moment. The energy relaxation rate is just the

power divided by the energy per decay.



P
 ed = (4.23)

 

![SchusterThesis.pdf-93-4.png](SchusterThesis.pdf-93-4.png)

The quality factor of the CPB can then be expressed as


 0

![SchusterThesis.pdf-93-5.png](SchusterThesis.pdf-93-5.png)
Q ed =

![SchusterThesis.pdf-93-6.png](SchusterThesis.pdf-93-6.png)

 0




 2 3 

![SchusterThesis.pdf-93-7.png](SchusterThesis.pdf-93-7.png)

![SchusterThesis.pdf-93-8.png](SchusterThesis.pdf-93-8.png)

d 2 


(4.24)


For the typical CPB at  5 GHz transition frequency one expects, depending on the dipole moment,

a Q ed 10 8 10 10 ! May we one day encounter such limits!
 


For the typical CPB at  5 GHz transition frequency one expects, depending on the dipole moment,


Magnetic Dipole Radiation

The power emitted via magnetic dipole radiation is given [Griffiths1999] is



4  3 

![SchusterThesis.pdf-93-10.png](SchusterThesis.pdf-93-10.png)

![SchusterThesis.pdf-93-9.png](SchusterThesis.pdf-93-9.png)

![SchusterThesis.pdf-93-11.png](SchusterThesis.pdf-93-11.png)

3  0



m

![SchusterThesis.pdf-93-12.png](SchusterThesis.pdf-93-12.png)

 2




m






2
(4.25)




4
P md =





where m = I  A is the magnetic dipole moment, with I the current around the SQUID loop of

area A . For a typical CPB the current is given by the critical current I 0 1 nA, and the loop area


is A  10  m 2 .


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 92

Following the same procedure as for the electric dipole one can derive a quality factor for magnetic


radiation.



3 
Q md = 4  3


 0

![SchusterThesis.pdf-94-1.png](SchusterThesis.pdf-94-1.png)

![SchusterThesis.pdf-94-2.png](SchusterThesis.pdf-94-2.png)













 2

![SchusterThesis.pdf-94-3.png](SchusterThesis.pdf-94-3.png)

m




2
 2 (4.26)




3 
Q md =


![SchusterThesis.pdf-94-0.png](SchusterThesis.pdf-94-0.png)

For typical parameters the magnetic quality factor is even higher, approximately Q md = 10 14 !

Other Sources of Decay

Other sources of decay have been proposed for the CPB. If there is any piezoelectricity or magne-

tostriction in any of the nearby materials, the electromagnetic oscillations in the CPB could lose

energy in the form of phonons [Ioffe2004]. It is possible that other quasiparticle related phenomena,

such as non-equilibrium populations, vortices, or subgap states could affect the lifetime. Vortices

might be reduced by better magnetic shielding of the sample and by intentionally pinning vortices

which might arise by putting an array of holes in the resonator. Non-equilibrium quasiparticle pop-

ulations might be reduced by adding a normal metal quasiparticle trap to the box or by making the

two halves of the CPB out of superconductors with dissimilar gaps, creating a barrier to quasiparticle

tunneling.

####### 4.2 ####### Dephasing

Dephasing is caused by processes that randomly modify the effective transition frequency of the

qubit, which cause the qubit to accumulate a random phase. Dephasing is typically caused by low

frequency noise far below the transition frequency, and can be treated in a semi-classical manner.

There are several types of dephasing. First, any process which causes energy relaxation will also

dephase the qubit at a rate 1  1 / 2. Second, there are fluctuations which occur during the course

of a single experiment (during one decay lifetime) which dephase at a rate   . Finally, there are

fluctuations which occur on longer timescales from experiment to experiment, creating an ensemble

dephasing denoted by the rate    . This last type is analogous to having spatial magnetic field

inhomogeneities in nuclear magnetic resonance (NMR), and is often referred to as inhomogeneous

broadening. Like its NMR counterpart, because it is not intrinsic to a single experiment, it can

theoretically be reduced using spin echo techniques. Though it is possible to compensate for inho-

mogeneous broadening, doing so can be the bane of practical experiments, because inhomogeneous

![SchusterThesis.pdf-94-4.png](SchusterThesis.pdf-94-4.png)

1 Dephasing represents decay of an amplitude and so goes at half of the rate of energy relaxation  2   1 / 2.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 93

broadening often represents drifting conditions, which significantly complicate experimental proto-

cols. The total dephasing is the sum of all of these rates

 2 =  1 / 2 +   +    (4.27)

and one can define a dephasing quality factor, which is the number of coherent oscillations before

the qubit will accumulate a random  phase shift.

Q  =  a /   (4.28)

In the frequency domain   manifests itself as a broadening of the intrinsic linewidth. To find

the deviation of the transition frequency due to (slow) fluctuations in a parameter  , with spectral

density S  (  ), one can Taylor expand the frequency about the bias point  0 .



 =   0 = 
 





+

![SchusterThesis.pdf-95-1.png](SchusterThesis.pdf-95-1.png)
 0 2


 2 

![SchusterThesis.pdf-95-2.png](SchusterThesis.pdf-95-2.png)

 2




 0 + -    (4.29)


![SchusterThesis.pdf-95-0.png](SchusterThesis.pdf-95-0.png)

Typically the first order term dominates the expansion, however it is often possible by artful selection

of the bias conditions to null the first term, leaving the second order term at the lowest non-trivial

order.

The variance is the time averaged expectation of  2


 2 =  2 
    



2  4

+  

![SchusterThesis.pdf-95-4.png](SchusterThesis.pdf-95-4.png)
 0 4




2



 2 

![SchusterThesis.pdf-95-5.png](SchusterThesis.pdf-95-5.png)

 2




2  3

+  

![SchusterThesis.pdf-95-6.png](SchusterThesis.pdf-95-6.png)
 0 2









![SchusterThesis.pdf-95-7.png](SchusterThesis.pdf-95-7.png)






![SchusterThesis.pdf-95-3.png](SchusterThesis.pdf-95-3.png)

![SchusterThesis.pdf-95-8.png](SchusterThesis.pdf-95-8.png)




 2 

 2




 0 + -    (4.30)


For most distributions the last, cross term is small due to the fact if the distribution is not very

skewed the average value of  3  0. Additionally it is convenient to reexpress the kurtosis (   4  )


![SchusterThesis.pdf-95-9.png](SchusterThesis.pdf-95-9.png)

  2  as



 4 =   4 ( K + 3) (4.31)
 


in terms of the standard deviation   =


where K is the excess kurtosis, which may in principle lie between  2 and +  , but is zero for the

normal distribution and typically of order unity for most other distributions encountered. Dropping

the cross term and reexpressing Eq. 4.30 in terms of the variance gives


 2 =   2
 




![SchusterThesis.pdf-95-10.png](SchusterThesis.pdf-95-10.png)






2

 0 +   4 3 + 4 K




2



 2 

![SchusterThesis.pdf-95-12.png](SchusterThesis.pdf-95-12.png)

 2




2

 0 + -    (4.32)




2



![SchusterThesis.pdf-95-11.png](SchusterThesis.pdf-95-11.png)

The time average 1 is most conveniently taken in the frequency domain where can be expressed

![SchusterThesis.pdf-95-13.png](SchusterThesis.pdf-95-13.png)

1 In general one should take the time average over derivatives as well as  itself, as they too may have some
frequency dependence, which might correlate with the fluctuations in  . However, for dephasing the maximum cutoff
frequency  max  1 /T 2 is typically still in the adiabatic limit, where the derivatives are frequency independent.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 94


as


 max
 2 = S  (  ) W (  ) d (4.33)
   min



 max
  2  =  min



where W (  ) is the spectral weight function, which depends on the specific experiment being per-

formed [Martinis2003]. While nominally the cut-offs are  min 0 and  max , in practice
 

the maximum frequency is effectively capped to  1 /T 2 by the spectral density functions 1 . The

minimum cut-off is set by the inverse single shot experiment time when calculating   , and by the

total length of ensemble measurements when finding    . Weight functions for common experiments

are

Experiment Spectral Weight Function


Ramsey / Idle W 0 = sin 2 ( ft 2


( f ) 2 (4.34)


![SchusterThesis.pdf-96-0.png](SchusterThesis.pdf-96-0.png)

2

 Rabi f

 Rabi 2 f 2 W 0 (4.35)

![SchusterThesis.pdf-96-1.png](SchusterThesis.pdf-96-1.png)





 Rabi f
Rabi W R = 2


SpinEcho W SEn = tan 2 ( ft/ 2 n ) W 0 (4.36)


where t is the time at which one wants to know the accumulated phase noise which is often T 2 ,  Rabi

is the Rabi oscillation frequency (see section 9.1 for definition and experiments) , and n refers to

the number of spin echos in a given decay time. In general the accumulated phase noise depends

on the experiment being performed and the type of noise. In all cases, the spectral weight function

suppresses noise above 1 /T 2 . In the Rabi or spin echo experiments noise at very low frequencies is

also suppressed. For the examples in this chapter, rates will be calculated using W 0 which is most

pessimistic. For noise with gaussian statistics which is white on the scale of the characteristic decay

time, the decay will be exponential characterized by a rate,   . If the noise is predominantly at

frequencies lower than   then the decay will be gaussian. If the statistics are non-gaussian 2 then

one can have an overall loss of contrast rather than decay in time [Martinis2003]. In the charge

regime the transition frequency from Eq. 3.69 is


![SchusterThesis.pdf-96-3.png](SchusterThesis.pdf-96-3.png)

 
cos 2

![SchusterThesis.pdf-96-4.png](SchusterThesis.pdf-96-4.png)

 0




+ d 2 sin 2  

![SchusterThesis.pdf-96-5.png](SchusterThesis.pdf-96-5.png)

 0




+ 16 E C 2 (1 n g ) 2 (4.37)






1
 a =


E 2


![SchusterThesis.pdf-96-2.png](SchusterThesis.pdf-96-2.png)

Variations in any of the parameters in the Eq. 4.37 will lead to fluctuations in the energy and dephas-

ing the qubit. The following subsections investigate the types of noise each parameter experiences,

and find optimal bias points to minimize these channels of dephasing.

![SchusterThesis.pdf-96-6.png](SchusterThesis.pdf-96-6.png)

1 This cut-off is one reason a low-frequency Taylor series approximation is valid
2 When many distributions (even non gaussian ones) are added they will typically have gaussian statistics due to
the central limit theorem. However if there are not very many distributions (such as a small number of telegraph
fluctuators) then one can have non-gaussian statistics.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 95

######### 4.2.1 ######### Charge Noise

When operated in the charge regime, the Cooper pair box is affected most by charge noise. This

is both because the charge plays such a critical role in the charge regime CPB and because the

fluctuations in charge are both substantial and pathological. Much of the effort on the CPB has

been directed towards understanding and minimizing the effects of this charge noise, which can be

divided into three categories. The first intrinsic, expected, and relatively benign is the thermal

noise introduced by the presence of a gate, in which Johnson-Nyquist voltage noise causes effective

fluctuations in the bias charge. The second, pathological, and not well-understood so-called 1 /f

charge noise is thought to arise from local charges in the substrate, or junction barrier, and has

fluctuations which diverge at low frequencies [Zorin1996]. In other words; there is unexplained

random drifting of charge on large scales and over large times. This presents a significant problem

for single short experiments, but is devastating for long term biasing, and thus, to the efficient

scaling of CPB-based qubits. The final mechanism comes in the form of quasi-particles, which when

one tunnels across the barrier changes the gate charge by one electron.

To estimate noise and optimize the choice of n g let us apply formalism in Eq. 4.32. For sim-

plicity we will assume that the CPB is made with a single junction 1 (operated at zero flux). The

dimensionless first order decay rate (inverse Q  ) is


1 =  n g

![SchusterThesis.pdf-97-0.png](SchusterThesis.pdf-97-0.png)

![SchusterThesis.pdf-97-1.png](SchusterThesis.pdf-97-1.png)

Q   a


 a ( n g 1)
=  n g 

![SchusterThesis.pdf-97-2.png](SchusterThesis.pdf-97-2.png)

![SchusterThesis.pdf-97-3.png](SchusterThesis.pdf-97-3.png)
n g


( n g 1) 2 + 4 E E J



2 (4.38)



![SchusterThesis.pdf-97-4.png](SchusterThesis.pdf-97-4.png)

4 E C


Before attempting to estimate the dephasing rate, one can immediately see that Eq. 4.38 can be


made zero by letting n g = 1. At this ideal bias point, referred to as the sweet or clock point the

energy transition is first order insensitive to any (small) fluctuations in gate [Vion2002]. Further,

the ratio E J / 4 E C appears in the denominator, meaning that the insensitive region will grow more

robust as this quantity is increased (see Fig 4.6).

The second order contribution to the dimensionless dephasing rate is given by


1 =  n 2 g

![SchusterThesis.pdf-97-5.png](SchusterThesis.pdf-97-5.png)

![SchusterThesis.pdf-97-6.png](SchusterThesis.pdf-97-6.png)

Q   a


 n 2  2 a =  n 2


4 E C

![SchusterThesis.pdf-97-8.png](SchusterThesis.pdf-97-8.png)

E J




2
 


4 E C
1 +

![SchusterThesis.pdf-97-9.png](SchusterThesis.pdf-97-9.png)

E J




2  2
 ( ng  1) 2 


 2  a


(4.39)


![SchusterThesis.pdf-97-7.png](SchusterThesis.pdf-97-7.png)

Normally, the first order contribution dominates for small fluctuations but when the prefactor in

![SchusterThesis.pdf-97-10.png](SchusterThesis.pdf-97-10.png)

1 In section 4.2.2 the optimal flux bias point will be  = 0. To get the full expression simply let E J 2  E J1 2 +


E J1 E J2 cos 2   0 


+ E J2 2 .


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 96



40


E /E =0.5 E /E =0.5


30

20


E J /E c =2 E J /E c =2


10

|Col1|E/E=0.5 J c E/E=1 J c E/E=2 J c|
|---|---|


![SchusterThesis.pdf-98-0.png](SchusterThesis.pdf-98-0.png)

0.5 1 1.5

n g


0.5 1 1.5 2

n g


Figure 4.6: a) Dimensionless first derivative of energy with respect to charge. Note that the
derivative goes to zero at n g = 1 for all E J /E C , meaning that the first order charge noise, which is
proportional to this derivative will also disappear. At larger E J /E C this minimum is more robust.
b) If the first order noise is eliminated the second order noise will dominate. The robustness in the
first derivative at higher E J /E C is reflected in the maximum value of the second derivative.

Eq. 4.38 is zero at n g = 1 the second order noise dominates 1 , and at this point the dimensionless


dephasing rate becomes


1  n 2

=

![SchusterThesis.pdf-98-1.png](SchusterThesis.pdf-98-1.png)

![SchusterThesis.pdf-98-2.png](SchusterThesis.pdf-98-2.png)
Q   a


 2 

![SchusterThesis.pdf-98-3.png](SchusterThesis.pdf-98-3.png)

n 2 g




4 E C

![SchusterThesis.pdf-98-4.png](SchusterThesis.pdf-98-4.png)

E J




2
(4.40)



=  n 2


A more complete treatment of dephasing at optimal points can be found in [Makhlin2004],

which discusses the rather interesting lineshape produced by the rectification of the parabolic en-

ergy dependence on the bias parameter. This behavior confirms that large E J / 4 E C reduces the

dimensionless dephasing rate and thus improves Q  . The two charge state approximation, on which

Eq. 4.37 is based, relies on E J / 4 E C 1, but the result of Eq. 4.40 provides motivation to explore


beyond this regime. This transmon regime (see Sec. 4.3) that lies beyond is fraught with interesting

surprises, and looks very promising as a new qubit indeed.

To determine the actual Q  one must find S n g (  ) for each dephasing mechanism. Though each

mechanism has a different spectral density and different origin, at present we have little control

over these distributions and our attempts to improve the overall performance have mostly centered

around optimizing the way that the noise propagates into the qubit itself as shown above.

Voltage Noise

Thermal voltage noise from the 50 environment applied to the gate capacitor will make fluctuations

in the gate charge n g = C g  V g /e , which is just C g for the isolated box and C g  ( C in /C r ) C g inside a



![SchusterThesis.pdf-98-5.png](SchusterThesis.pdf-98-5.png)

1 Note that at n g = 1 the cross term in Eq. 4.30 is also zero.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 97

a) b)

8  10 9


4  10


2  10 9

1  10 9


![SchusterThesis.pdf-99-0.png](SchusterThesis.pdf-99-0.png)

![SchusterThesis.pdf-99-1.png](SchusterThesis.pdf-99-1.png)

E J /E


0.05 0.1 0.15 0.2 0.25

Temperature (K)


Figure 4.7: a) Dephasing of the qubit (at T = 100 mK) due to low frequency thermal radiation
(Johnson noise) as a function E J /E C . b) Dephasing of the qubit vs. temperature at E J /E C = 1.
These clearly show that the thermal dephasing is a negligible contributor of dephasing.

resonator. The charge spectral density comes directly from the voltage spectral density of Eq. 4.6,

and shown in Fig. 4.1.


S n th g (  ) = C g 


2  Re [ Z (  )]


  (4.41)

![SchusterThesis.pdf-99-3.png](SchusterThesis.pdf-99-3.png)

k B T  1





![SchusterThesis.pdf-99-2.png](SchusterThesis.pdf-99-2.png)

![SchusterThesis.pdf-99-4.png](SchusterThesis.pdf-99-4.png)

If this were a bare CPB than one could integrate this out to the qubit frequency 1 but inside


a cavity from Fig. 3.3 one can see that cavity begins filtering heavily at the cavity bandwidth,

 . Therefore one can approximate the RMS charge fluctuations by the low frequency limit of the

Eq. 4.41 with bandwidth  .


 n 2 g 

 0



dW 0 S n th g (  ) = 2 C g  k B T Re [ Z (  )]


(4.42)


![SchusterThesis.pdf-99-5.png](SchusterThesis.pdf-99-5.png)

Substituting Eq. 4.42 one finds the optimal bias point is n g = 1 giving


Q  =  n 2


4 E C

![SchusterThesis.pdf-99-7.png](SchusterThesis.pdf-99-7.png)

E J




2
(4.43)



![SchusterThesis.pdf-99-6.png](SchusterThesis.pdf-99-6.png)

Q  > 10 7 even with modest E J / 4 E C = 1. (see Fig. 4.7).

1 /f Charge Noise

The voltage noise is a remote thermal source of noise which can be filtered and though not white,

is well-behaved at low frequencies. In some sense that type of noise is not really charge noise but

![SchusterThesis.pdf-99-8.png](SchusterThesis.pdf-99-8.png)

1 One must be careful because at high frequencies the adiabatic approximation does not apply so large Stark shifts
and real transitions can occur.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 98

a) b)

10 5


1000

100

10

1

0.1


1000

100

10


10 4

10 3

10 2

10 1


10 4

10 2

10 0

|Col1|E/E = 4 J c E/E = 1 J c E/E = 0.25 J c|
|---|---|


![SchusterThesis.pdf-100-0.png](SchusterThesis.pdf-100-0.png)

0.75 1 1.25 0 1 2 3 4


n


E J / E c


Figure 4.8: a) Dephasing quality factor Q  due to first and second order contributions from 1 /f
noise. Note that there is more than an order of magnitude improvement due to working at the
degeneracy point n g = 1, and that the overall Q  and robustness of the maximum scale favorably
with E J /E C . b) Plot of maximal Q  at n g = 1 at different E J /E C . In both plots a transition
frequency of  a = 5 GHz and 1 /f charge noise with magnitude S Q (1 Hz) = 1  10  3 e / Hz 1 / 2 is
assumed.

actually photon noise which just happens to couple through the electrostatic part of the Hamiltonian.

Unfortunately, there also exists charge noise in the simple sense of charges moving around near the

box, either on in the dielectric nearby or in the barrier of the junction itself. Because such local

charge noise can not really be filtered (though its effects can be minimized by proper design of the

CPB), it can make large excursions in rare cases, which is typically described using a 1 /f spectral

density given by

S n 1 g /f ( f ) = A 2 /f (4.44)


The origin of this noise is not well-known but is typically of order A  10  3  10  4 e/


![SchusterThesis.pdf-100-1.png](SchusterThesis.pdf-100-1.png)

Hz . To find


the RMS deviations in n g one must integrate this spectral density over the appropriate bandwidth.


 max
 n 2 g dW 0 S n 1 g /f (  ) A 2 ln (  max / min ) (4.45)

  min 


It is more important to set a cutoff frequency, especially on the low side to prevent the distribution

from diverging, though for most reasonable choices for cutoffs  n g 3 5 A . If one desires to find
 

Q  the single shot dephasing Q, one should set the cutoff to the single shot time (  min = 1 / ss ). If

the Q   is desired, then the total experiment time  min = 1 / expt is more appropriate. For an upper

bound the spectral density weighting function, or some property of the fluctuators themselves may

set an upper bound.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 99

Quasiparticle Noise

A very special form of charge noise is caused by quasi-particles which can tunnel across the junction

instantly changing the gate charge by one electron. The treatment developed to treat thermal noise

and 1 /f noise assumes small fluctuations and is inadequate to deal with such large fluctuations. For

these, it is best to take the worst case (and most likely) scenario, that the bias point switches over

the whole energy range from the lowest n g = 1 to highest n g = 0 transition energy.

R = E eg ( n g = 0)  E eg ( n g = 1) (4.46)

One can characterize the dephasing devastation wrought by a quasiparticle tunneling event by the

![SchusterThesis.pdf-101-0.png](SchusterThesis.pdf-101-0.png)

ratio of R/E eg , which can be expressed in the charge regime as


![SchusterThesis.pdf-101-4.png](SchusterThesis.pdf-101-4.png)

2 R J

= 1 + 2 E
E eg ( n g = 0) E eg ( n g = 1) 4 E

![SchusterThesis.pdf-101-1.png](SchusterThesis.pdf-101-1.png)

![SchusterThesis.pdf-101-2.png](SchusterThesis.pdf-101-2.png)



E J
1 +

![SchusterThesis.pdf-101-5.png](SchusterThesis.pdf-101-5.png)

4 E C




2



2 R



E J

![SchusterThesis.pdf-101-3.png](SchusterThesis.pdf-101-3.png)

4 E




4 E C


4 E C


(4.47)


This ratio ranges from 1 at E J / 4 E C = 0 to about 20% at E J / 4 E C = 1, meaning that the relative


change in frequency is always of order unity, and that any quasiparticle tunneling event is fatal.

However, the Eq. 4.37 is only an approximate expression, valid only when E J 4 Ec . The energy


range and thus the dephasing clearly gets smaller as E J / 4 E C is increased, so what happens beyond

the charge regime? In fact something remarkable happens, and the ground and excited state energy

bands become very flat, exponentially suppressing the impact of charge noise.

Before discussing potential cures (see section 4.3) it is prudent to also discuss prevention. While

quasiparticle tunneling is devastating, one can take several measures to reduce both the population

of quasiparticles available to tunnel and the probability that they will do so. Superconductors

possess an energy gap to creating quasiparticles, and thus thermal quasiparticles are suppressed

exponentially at temperatures below the critical temperature. In aluminum at 250 mK there might

be  1 quasiparticle on a typical CPB island, but at 50 mK there is only about a one in one hundred

chance of finding one, and by 20 mK there is ideally less than one chance in one hundred thousand

that even a single quasiparticle is present [Lutchyn2005]. If these statistics were followed all the

way down to the bath temperature of 20 mK quasiparticles would be only a minor inconvenience.

Unfortunately, there are many mechanisms which can limit this scaling. There may be radiation

from outside sources which breaks Cooper pairs (unlikely), or impurities which lower the effective

gap (possible), magnetic fields which create areas of normal metal (likely though preventable), or


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 100

there could just be an odd number of electrons leaving one quasiparticle out of the BCS dance (coin

flip).

On average then, one must assume at least one quasiparticle on the island, and since a single

tunneling event destroys coherence, it is manifestly important to prevent that quasiparticle from

tunneling. One option is to give it a place to go in the form of a quasiparticle trap made of normal

metal, though a metal can act as both a source and sink of quasiparticles. Preventing tunneling

can also be accomplished by using superconductors of dissimilar gaps, which exponentially suppress

tunneling (in one direction at least). This can be done by using two different metals for the two

reservoirs, changing the purity of the metals, or using a magnetic field to slightly change the gaps in

situ [Aumentado2004]. In summary, when quasiparticles are present and mobile, they dephase the

qubit quickly, but through proper engineering can be minimized.

######### 4.2.2 ######### Flux Noise

The flux noise is the dual of charge noise. It can arise from thermal fluctuations in nearby wires,

vortices in the superconducting ground planes, or if not well shielded, from the motion of external

magnetic materials.

The dimensionless first order dephasing rate in the charge regime is


1 d 2 sin 2  
  0





 


  

=

![SchusterThesis.pdf-102-0.png](SchusterThesis.pdf-102-0.png)

![SchusterThesis.pdf-102-1.png](SchusterThesis.pdf-102-1.png)
 a  a


E J 2

  2





![SchusterThesis.pdf-102-2.png](SchusterThesis.pdf-102-2.png)

![SchusterThesis.pdf-102-3.png](SchusterThesis.pdf-102-3.png)

![SchusterThesis.pdf-102-4.png](SchusterThesis.pdf-102-4.png)

![SchusterThesis.pdf-102-5.png](SchusterThesis.pdf-102-5.png)

 a


 a 

=  
  2 0


2 0


 0


(4.48)


Note that as for charge there exist sweet spots at  = 0 and  =  0 / 2 where the first order dephasing


rate goes to zero. When at or near the flux sweet spot the second order noise will dominate the

dephasing rate. At the more favorable sweet spot ( = 0) and in the charge regime this second

order dephasing rate is given by


1  d 2 (4.49)

![SchusterThesis.pdf-102-10.png](SchusterThesis.pdf-102-10.png)

1 + (4 E C /E J ) 2 (1 ng ) 2

  


 


    2

=

![SchusterThesis.pdf-102-6.png](SchusterThesis.pdf-102-6.png)

![SchusterThesis.pdf-102-7.png](SchusterThesis.pdf-102-7.png)
 a 


 2  a


![SchusterThesis.pdf-102-8.png](SchusterThesis.pdf-102-8.png)

![SchusterThesis.pdf-102-9.png](SchusterThesis.pdf-102-9.png)

 a



2  a 2 

  2 =   2


 2


The dimensionless dephasing rate at the two charge degeneracy points are

  2 2


![SchusterThesis.pdf-102-11.png](SchusterThesis.pdf-102-11.png)

![SchusterThesis.pdf-102-12.png](SchusterThesis.pdf-102-12.png)

 a



 2  2
=  2 0
n g =1


 2


1  d 2 (4.50)




  

![SchusterThesis.pdf-102-13.png](SchusterThesis.pdf-102-13.png)

 a



 2  2
=  2 0

![SchusterThesis.pdf-102-14.png](SchusterThesis.pdf-102-14.png)
n g =0


(4.51)

![SchusterThesis.pdf-102-15.png](SchusterThesis.pdf-102-15.png)
1 + (4 E C /E J ) 2


1  d 2

E C /E




In the charge regime where E J / 4 E C is large, n g = 0 is clearly more favorable for flux dephasing,

however it is much worse for charge dephasing. In practice, E J /E C 1 / 4, so the lever arm is not that



-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 101


10

10

10

10

10


10 3

10 2

10 1

1

10  1


![SchusterThesis.pdf-103-0.png](SchusterThesis.pdf-103-0.png)

 0.5 0 0.5

bias flux,  /  0

Figure 4.9: Dephasing times at the charge sweet spot ( n g = 1) due to flux and critical current noise.
These values are independent of the E J /E C ratio when in the charge regime. The flux dephasing time
is calculated assuming a 1 /f distribution of flux noise with amplitude S  (1 Hz) = 10  5  0 / Hz 1 / 2 ,
qubit frequency,  a = 5 GHz, and junction asymmetry d 10%. The dephasing due to critical
current noise was calculated using a critical current noise amplitude  S I c = 10  6 I 0 / Hz 1 / 2 .

large and thus it is more important to minimize the effects of charge noise and one works at n g = 1.

Since | d | < 1 / 2, at this operating point the dimensionless dephasing rate is roughly just the fraction

of a flux quantum that the noise presents. Efforts to minimize the impact of flux noise therefore

cannot depend on making the matrix elements small and must focus on reducing the amount of flux

noise   . In addition to external shielding, the qubit can be designed to have a very small loop so as

to only couple weakly to any fluctuating magnetic fields, and if one were to get really desperate one

could use a single junction CPB, which would deprive oneself of the ability to tune E J with flux but

would eliminate the noise channel completely. Luckily even with modest measures to reduce the flux


noise, the residual 1 /f component is quite small, 10  5  0 /



![SchusterThesis.pdf-103-1.png](SchusterThesis.pdf-103-1.png)

Hz [Wellstood1987], and of course at


the sweet spot one is only sensitive to second order. In our measurements, flux noise seems to be

quite minimal, and can only be noticed if the charge noise is suppressed dramatically (see Sec. 4.3),

and then, even without explicit external shielding, only at very low frequencies (  1 Hz).

######### 4.2.3 ######### Critical Current/Josephson Energy ######### 1 ######### /f ######### Noise

Critical current noise is effectively noise in the value of E J itself. The origin of this noise is not well

understood, but is thought to arise from fluctuations inside the tunnel junction barrier which add

or remove conductance channels from the junction. The first order dimensionless dephasing rate is


cos 2  

![SchusterThesis.pdf-103-6.png](SchusterThesis.pdf-103-6.png)

 0




+ d 2 sin 2  

![SchusterThesis.pdf-103-7.png](SchusterThesis.pdf-103-7.png)

 0




(4.52)



 E J


  E

=

![SchusterThesis.pdf-103-2.png](SchusterThesis.pdf-103-2.png)

![SchusterThesis.pdf-103-3.png](SchusterThesis.pdf-103-3.png)
 a  a


 a


![SchusterThesis.pdf-103-4.png](SchusterThesis.pdf-103-4.png)

![SchusterThesis.pdf-103-5.png](SchusterThesis.pdf-103-5.png)




 a E J

=
E J  


  2


Unlike charge noise and flux noise there is no sweet spot for critical current/ E J noise. There is a

very general argument why there must always be at least one parameter for which no sweet spot


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 102

exists. The shape of the energy bands can be determined completely by dimensionless quantities

and for any inputs into these quantities one can in principle arrange a sweet spot. However, if the

transition energy is not zero then some parameter must set the absolute scale,   a . The transition

frequency must depend linearly on this parameter (by definition) and so any fluctuations in that

parameter will translate directly into fluctuations in the transition frequency. While the first order

dephasing rate may never be zero, in principle it can be made arbitrarily small by choosing a very

stable quantity. This means that if one wants a qubit to have a certain Q then there must be some

physical quantity (which the transition frequency is based on) that has that Q . In the case of the

CPB that quantity (especially at n g = 1) is E J . At n g = 1 the dimensionless dephasing rate due to


E J fluctuations is then just
 E J


 =  E J

![SchusterThesis.pdf-104-0.png](SchusterThesis.pdf-104-0.png)

![SchusterThesis.pdf-104-1.png](SchusterThesis.pdf-104-1.png)

 a E J



J (4.53)

E J


Variations in E J (as measured by normal resistance fluctuations) have a 1 /f like spectral density


with  E J /E J 10  6 /



![SchusterThesis.pdf-104-2.png](SchusterThesis.pdf-104-2.png)

Hz [Eroms2006, Wakai1986].


######### 4.2.4 ######### E ######### C ######### Noise

Another energy scale in the problem is E C , which physically arises from the capacitance of the

reservoirs. While noise in these capacitances has never been quantified, were any present it could

contribute to dephasing. The first order dimensionless dephasing rate for noise in E C is


 E J


 =  E C

![SchusterThesis.pdf-104-3.png](SchusterThesis.pdf-104-3.png)

![SchusterThesis.pdf-104-4.png](SchusterThesis.pdf-104-4.png)

 a  a


 a 16 E C (1 n g ) 2

E C =  E C  2   a 2





![SchusterThesis.pdf-104-5.png](SchusterThesis.pdf-104-5.png)

![SchusterThesis.pdf-104-6.png](SchusterThesis.pdf-104-6.png)




(4.54)
 2  2


This dephasing rate does have a sweet spot at n g = 1, so to get the dephasing rate one must go to

second order where the rate (at  = 0 for simplicity) is


 E J



E  J =  E 2 C

![SchusterThesis.pdf-104-7.png](SchusterThesis.pdf-104-7.png)

![SchusterThesis.pdf-104-8.png](SchusterThesis.pdf-104-8.png)

 a  a


 2  a


![SchusterThesis.pdf-104-9.png](SchusterThesis.pdf-104-9.png)

![SchusterThesis.pdf-104-10.png](SchusterThesis.pdf-104-10.png)

 a


 E 2  2 a =  E 2 C (1 + (4 E 16(1 C /E  J ) 2 n (1 g ) 2


(4.55)
(1 + (4 E C /E J ) 2 (1 n g ) 2 ) 2



Remarkably the degeneracy point is doubly sweet, and in fact (as we could have observed immedi-

ately) since E C is always multiplied by (1  n g ) it will not contribute at any order 1 .

######### 4.2.5 ######### Summary of Cooper pair box decoherence

Coherent qubit operation of the CPB is limited by the energy relaxation ( T 1 ) processes, which affect

the ability to perform single shot measurements, and the dephasing ( T  ) processes, which typically

![SchusterThesis.pdf-104-11.png](SchusterThesis.pdf-104-11.png)

1 The ability to null E C noise to all orders is only present in the two-state approximation where E J  4 E C . In the
transmon regime the behavior is quite different


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 103

limit the number of gate operations. When examining the effect of placing the CPB inside of a

cavity we found that the qubit could be coupled much more strongly to the gate and other qubits

while at the same time improving its radiative relaxation time. This innovation should allow for

non-local gates in future experiments.

####### 4.3 ####### Transmon

This section is a bit strange as it describes what is to come and what has just begun rather than

that which has been completed. It is a new way of thinking about the Cooper pair box that may be

the shape of things to come, and will doubtless be the subject of further investigations and theses.

The transmon, as it has come to be called, is a CPB, rediscovered as an anharmonic oscillator

rather than a frustrated Cooper pair weakly tunneling between two islands. It was born out of the

desire to immunize the CPB from charge noise, by decreasing the charging energy scale. At first

glance, it appeared that doing so would destroy the CPBs ability to couple to the cavity, preventing

measurement and the qubit-photon interactions we hoped to study. However, a more careful analysis

reveals that with appropriate design the CPB can be made even more strongly coupled, and while

remarkably suppressing charge noise exponentially ! When discussed in the language of a charge

qubit, these results seem to defy intuition, but when the transmon is described from the perspective

of an oscillator, its behavior becomes elegantly simple. The ideas in this section are not fully mature,

but they are not simply theoretical, having been employed in the most recent experiments.

The section will proceed by extending analysis of the Cooper pair box out of the charge regime,

using exact solutions to the Hamiltonian rather than two-state charge approximations as in previ-

ous sections. Next, the asymptotic behavior of the transmon will be derived as an LC oscillator,

which employs the non-linear Josephson inductance to achieve anharmonicity. Finally the transmon

will be coupled to a cavity, taking care to keep track of auxiliary levels ignored in the two-state

approximation. This section follows closely a work in preparation [Koch2007], which will present

some additional information.

######### 4.3.1 ######### Charge Dispersion

Charge noise has been the most significant problem for the CPB. In section 4.2.1 we saw that

dephasing due to charge noise could be eliminated to first order by operating at the degeneracy

point ( n g = 1) and that the second order dephasing is reduced by increasing E J /E C . The reason


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 104

E J / E c = 1 E J / E c = 5


![SchusterThesis.pdf-106-0.png](SchusterThesis.pdf-106-0.png)

![SchusterThesis.pdf-106-1.png](SchusterThesis.pdf-106-1.png)

 2  1

![SchusterThesis.pdf-106-2.png](SchusterThesis.pdf-106-2.png)

 2  1


0 1 2  2  1 0 1 2

E J / E c = 10 2 E J / E c = 50

1

0

![SchusterThesis.pdf-106-3.png](SchusterThesis.pdf-106-3.png)

0 1 2  2  1 0 1 2

n g (C g V g /e) n g (C g V g /e)


Figure 4.10: CPB energy bands at different E J /E C ratios. As the E J /E C ratio is increased the charge
dispersion (minimum/maximum energy difference) becomes substantially reduced, immunizing the
CPB to charge fluctuations. A side effect is that anharmonicity is also reduced (compare differences
between levels in different plots). At high enough E J /E C the levels resemble a harmonic oscillator.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 105

dephasing is reduced, seen in Fig. 4.10, is that as E J /E C increases, the energy bands begin to lose

their dependence on the bias charge. In the charge regime this is only noticeable near degeneracy

where the electrostatic energy is suppressed, but when E J > 4 E C , it becomes energetically favorable

to have currents traveling through the junction, thereby spreading the support of the wavefunction

over many Cooper pairs. Looking at the flatness of the bands in Fig. 4.10, it appears that it may

be possible to not only reduce the charge noise at degeneracy, but to make the qubit independent

of charge all together. To quantify this possibility, one can define the total charge dispersion as the

peak to peak difference in the m th energy band over one charge period.

 m = | E m ( n g = 0)  E m ( n g = 1) | (4.56)

In the charge regime this is simply



4 E C
 m = 0 4 E C = 4 E C = E J (4.57)
|  | E J

![SchusterThesis.pdf-107-0.png](SchusterThesis.pdf-107-0.png)

but a more thorough treatment [Koch2007] shows that this is really just the suppression as E J /E C

is increased, is just the first term in an exponential reduction in the charge dispersion given by


E J

![SchusterThesis.pdf-107-4.png](SchusterThesis.pdf-107-4.png)

2 E C





m 2 + 3 4




m

![SchusterThesis.pdf-107-5.png](SchusterThesis.pdf-107-5.png)

2




2 4 m +5
 m E C
 m !



 8 E J /E C

![SchusterThesis.pdf-107-7.png](SchusterThesis.pdf-107-7.png)
e  (4.58)


![SchusterThesis.pdf-107-2.png](SchusterThesis.pdf-107-2.png)

![SchusterThesis.pdf-107-6.png](SchusterThesis.pdf-107-6.png)

![SchusterThesis.pdf-107-1.png](SchusterThesis.pdf-107-1.png)

![SchusterThesis.pdf-107-3.png](SchusterThesis.pdf-107-3.png)

This exponential insensitivity to charge holds great promise but as is apparent from the way the

energy bands change in Fig. 4.10, it is a significant change that may come with unintended conse-

quences.

######### 4.3.2 ######### Anharmonicity

Another change visible in Fig. 4.10 in addition to the flatness of the bands, is that they become

more evenly spaced, that is their anharmonicity is reduced. In order to treat the CPB as a two

level qubit, one must ignore its higher excited states. Higher states can be neglected when pulses

manipulating the qubit transition do not match the frequency to excite the CPB to the next lowest

level. The frequency difference between the qubit transition and the transition from excited state to

the lowest unoccupied state, can be classified by the absolute and relative anharmonicity, defined as

 E 12 E 01 (4.59)
 

 r = /E 01 (4.60)


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 106

Because in frequency space, the length of a pulse determines its frequency spread, the anharmonicity

places a speed limit on manipulation of the qubit. Initially, as E J /E C 8 the anharmonicity


plummets, even passing through zero, and making it difficult to operate the CPB as a qubit, but

later the anharmonicity becomes negative only slowly returning to zero. At large values of E J /E C

the anharmonicity approaches

lim  E C (4.61a)
E J /E C 1 



![SchusterThesis.pdf-108-0.png](SchusterThesis.pdf-108-0.png)

lim  r
E J /E C  1 


E C

(4.61b)

![SchusterThesis.pdf-108-1.png](SchusterThesis.pdf-108-1.png)
8 E J


This result will be explained in the following section but for now lets explore its implications.

As E J /E C the anharmonicity is reduced,  r 0. While the charge dispersion vanished
 

exponentially, the anharmonicity does so only algebraically, allowing the dispersion to be suppressed

significantly before the anharmonicity becomes impractically small. While in the previous section

we measured the dephasing quality factor Q  , perhaps a better metric is the operation quality factor

( Q op ), the number of operations that can be completed in one T 2 . If there were no real decay and

we assume a worst case scenario of random bias charge, which gives a dephasing time related to the


inverse charge dispersion 1 ( T 2 1 / 1 ). The operation quality factor can be written as



Q op = / 1 5 10  3 2 E C
  E J



5 /



![SchusterThesis.pdf-108-3.png](SchusterThesis.pdf-108-3.png)

![SchusterThesis.pdf-108-2.png](SchusterThesis.pdf-108-2.png)

E J


8 E J /E C (4.62)


This means that even at modest E J /E C the Q op will become very large, even with no control

over charge! This is a huge boon for the scalability of CPB based qubits, as it would eliminate the

need for a separate DC charge bias to compensate random offset charges, on each individual qubit.

Though Q op goes up, the overall speed of qubit operations does go down. In the presence of some

other means of decay there will be an optimum value where the T 2 has equal contributions from

decay and pure dephasing. In practice, huge benefits can be gained without any appreciable sacrifice.

For example assuming 10 ns pulse length 2 , a typical pulse length in our experiments, is within the

anharmonicity for E J /E C 300. If charge noise were the only limiting factor the operation quality


factor would be Q op > 10 16 ! If a different mechanism limits the dephasing time, then we still havent

lost any significant bandwidth by limiting ourselves to 10 ns pulses so weve essentially eliminated

the charge noise contribution with no obvious performance penalties.

![SchusterThesis.pdf-108-4.png](SchusterThesis.pdf-108-4.png)

1 For simplicity the charge dispersion of the upper band (  1 ) is used to describe the dispersion of the qubit transition
energy. This is an approximation but in the large E J /E C limit this will tend to dominate over the ground state
dispersion (  0 ).
2 Our arbitrary waveform generator has 1 ns resolution so a shaped (gaussian) pulse usually spans around 10 ns.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 107



![SchusterThesis.pdf-109-0.png](SchusterThesis.pdf-109-0.png)

10 20 30 40 50

E J / E c


15

10


-1


![SchusterThesis.pdf-109-1.png](SchusterThesis.pdf-109-1.png)

20 40 60 80 100

E J / E c


Figure 4.11: a) Anharmonicity vs. E J /E C ratio. The anharmonicity, displayed in units of E C ,
drops rapidly at low E J /E C crossing zero at E J /E C = 0. It then becomes negative, asymptoting at
 =  E C at large E J /E C . The inset shows the relative anharmonicity,  r = / a , and compares the

![SchusterThesis.pdf-109-3.png](SchusterThesis.pdf-109-3.png)
exact calculation (solid) to the asymptotic (dashed) expression  r E C / 8 E J . The approximate


expression proves to be a good approximation above E J /E C 20. b) The formation of the transmon
 
frequency comb. The transition frequency is plotted of transition energies at the degeneracy point
( n g = 1). At high E J /E C the transition energies become evenly distributed with anharmonicity,
  E C . There are two classes of transitions. Note also that at small E J /E C the even to odd
transitions start degenerate (zero), while the odd to even ones start out large, though eventually
they all fall into the comb.


Figure 4.11: a) Anharmonicity vs. E J /E C ratio. The anharmonicity, displayed in units of E C ,
drops rapidly at low E J /E C crossing zero at E J /E C = 0. It then becomes negative, asymptoting at
 =  E C at large E J /E C . The inset shows the relative anharmonicity,  r = / a , and compares the
exact calculation (solid) to the asymptotic (dashed) expression  r E C / 8 E J . The approximate



10 2

10 0

10  2

10  4


10

10 

10 

10 

10 

10  10

|CPB E < 4E J c|T 2 Anharmonicity Barrier ( = 0) Transmon E < 4E J c T op|
|---|---|


![SchusterThesis.pdf-109-2.png](SchusterThesis.pdf-109-2.png)

10 15 20 25 30

E J / E c


20 40 60 80 100 120 140

E J / E c


Figure 4.12: a) Plot of T 2 (blue) and T op = 1 / (red) at n g = 1 due to second order charge noise.
A 1 /f spectrum with magnitude S Q = 1  10  3 e/ Hz 1 / 2 ) is assumed for the charge noise. While high
Q s can be obtained in the traditional CPB regime ( E J /E C < 4), once passed the anharmonicity
barrier (pink), where T op as  0, the Q can be substantially improved at higher E J /E C
 
ratios in the transmon regime. b) Plot of charge dispersion  m of the first few transmon transitions
(solid lines) and asymptotic approximations (dashed lines). Plotting in units of E C makes this a
conservative estimate dimensionless dephasing rate  2 / = 1 /Q op in the asymptotic limit (where
 E C ).



-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 108

![SchusterThesis.pdf-110-3.png](SchusterThesis.pdf-110-3.png)

######### c ######### s

![SchusterThesis.pdf-110-6.png](SchusterThesis.pdf-110-6.png)

![SchusterThesis.pdf-110-4.png](SchusterThesis.pdf-110-4.png)

![SchusterThesis.pdf-110-24.png](SchusterThesis.pdf-110-24.png)

![SchusterThesis.pdf-110-20.png](SchusterThesis.pdf-110-20.png)

![SchusterThesis.pdf-110-22.png](SchusterThesis.pdf-110-22.png)

![SchusterThesis.pdf-110-8.png](SchusterThesis.pdf-110-8.png)

![SchusterThesis.pdf-110-16.png](SchusterThesis.pdf-110-16.png)

![SchusterThesis.pdf-110-10.png](SchusterThesis.pdf-110-10.png)

![SchusterThesis.pdf-110-12.png](SchusterThesis.pdf-110-12.png)

![SchusterThesis.pdf-110-14.png](SchusterThesis.pdf-110-14.png)

![SchusterThesis.pdf-110-18.png](SchusterThesis.pdf-110-18.png)

![SchusterThesis.pdf-110-19.png](SchusterThesis.pdf-110-19.png)

![SchusterThesis.pdf-110-23.png](SchusterThesis.pdf-110-23.png)

![SchusterThesis.pdf-110-21.png](SchusterThesis.pdf-110-21.png)

![SchusterThesis.pdf-110-9.png](SchusterThesis.pdf-110-9.png)

![SchusterThesis.pdf-110-11.png](SchusterThesis.pdf-110-11.png)

![SchusterThesis.pdf-110-7.png](SchusterThesis.pdf-110-7.png)

![SchusterThesis.pdf-110-13.png](SchusterThesis.pdf-110-13.png)

![SchusterThesis.pdf-110-17.png](SchusterThesis.pdf-110-17.png)

![SchusterThesis.pdf-110-15.png](SchusterThesis.pdf-110-15.png)

![SchusterThesis.pdf-110-41.png](SchusterThesis.pdf-110-41.png)

![SchusterThesis.pdf-110-31.png](SchusterThesis.pdf-110-31.png)

![SchusterThesis.pdf-110-34.png](SchusterThesis.pdf-110-34.png)

![SchusterThesis.pdf-110-28.png](SchusterThesis.pdf-110-28.png)

![SchusterThesis.pdf-110-37.png](SchusterThesis.pdf-110-37.png)

![SchusterThesis.pdf-110-43.png](SchusterThesis.pdf-110-43.png)

![SchusterThesis.pdf-110-40.png](SchusterThesis.pdf-110-40.png)

![SchusterThesis.pdf-110-26.png](SchusterThesis.pdf-110-26.png)

![SchusterThesis.pdf-110-46.png](SchusterThesis.pdf-110-46.png)

![SchusterThesis.pdf-110-51.png](SchusterThesis.pdf-110-51.png)

![SchusterThesis.pdf-110-49.png](SchusterThesis.pdf-110-49.png)

![SchusterThesis.pdf-110-5.png](SchusterThesis.pdf-110-5.png)

![SchusterThesis.pdf-110-47.png](SchusterThesis.pdf-110-47.png)

![SchusterThesis.pdf-110-52.png](SchusterThesis.pdf-110-52.png)

![SchusterThesis.pdf-110-39.png](SchusterThesis.pdf-110-39.png)

![SchusterThesis.pdf-110-32.png](SchusterThesis.pdf-110-32.png)

![SchusterThesis.pdf-110-35.png](SchusterThesis.pdf-110-35.png)

![SchusterThesis.pdf-110-29.png](SchusterThesis.pdf-110-29.png)

![SchusterThesis.pdf-110-38.png](SchusterThesis.pdf-110-38.png)

![SchusterThesis.pdf-110-44.png](SchusterThesis.pdf-110-44.png)

![SchusterThesis.pdf-110-45.png](SchusterThesis.pdf-110-45.png)

![SchusterThesis.pdf-110-50.png](SchusterThesis.pdf-110-50.png)

![SchusterThesis.pdf-110-48.png](SchusterThesis.pdf-110-48.png)

![SchusterThesis.pdf-110-30.png](SchusterThesis.pdf-110-30.png)

![SchusterThesis.pdf-110-33.png](SchusterThesis.pdf-110-33.png)

![SchusterThesis.pdf-110-27.png](SchusterThesis.pdf-110-27.png)

![SchusterThesis.pdf-110-36.png](SchusterThesis.pdf-110-36.png)

![SchusterThesis.pdf-110-42.png](SchusterThesis.pdf-110-42.png)

![SchusterThesis.pdf-110-25.png](SchusterThesis.pdf-110-25.png)

![SchusterThesis.pdf-110-54.png](SchusterThesis.pdf-110-54.png)

![SchusterThesis.pdf-110-0.png](SchusterThesis.pdf-110-0.png)

![SchusterThesis.pdf-110-1.png](SchusterThesis.pdf-110-1.png)

![SchusterThesis.pdf-110-2.png](SchusterThesis.pdf-110-2.png)

![SchusterThesis.pdf-110-53.png](SchusterThesis.pdf-110-53.png)

Figure 4.13: a) Sketch of the transmon inside of a resonator. The transmon is essentially a CPB
with a large geometric gate capacitance which lowers E C while maintaining  close to unity. The
finger capacitor can be used as a shunt capacitance to lower  if unity coupling isnt desired. b)
Simplified circuit diagram of the transmon which looks very similar to the CPB circuit diagram
but with larger values for the capacitors. For a more complete circuit diagram and discussion of
capacitance ratios see section 5.3.

######### 4.3.3 ######### Transmon as a Josephson Oscillator

The transmon appears to have the correct spectral characteristics for a qubit (high Q and sufficient

anharmonicity) but though topologically the same as a CPB, it is clearly a new type of qubit

demanding a new approach for understanding it. The name Cooper pair box arises from thinking

about the qubit as a pair of islands where the bit is the location of a single Cooper pair, and intuition

for this device is gained from modeling it as two capacitors and small coupling between them. At

high E J /E C the CPB does not behave like this at all, and is more closely related to an LC oscillator.

The transmon can be thought of as an oscillator based on the Josephson junction and a geo-

metrically defined capacitor (see Fig. 4.13). The argument will proceed similarly to that of the LC

oscillator in 3.1.8, but with the inductor replaced by a Josephson element described by the Josephson

relations [Tinkham2004]




2 eV =  (4.63)

![SchusterThesis.pdf-110-55.png](SchusterThesis.pdf-110-55.png)

t

I = I c sin  (4.64)

where I c is the critical current and  is the superconducting phase difference across the junction.

To reveal the Josephson junctions inductive nature, one can find the relation between voltage and


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 109

current by substituting Eq. 4.63 into the derivative of Eq. 4.64 to yield


I
V = L J (4.65)

![SchusterThesis.pdf-111-0.png](SchusterThesis.pdf-111-0.png)

t



L J0
L J =



L J0 L J0

=

![SchusterThesis.pdf-111-1.png](SchusterThesis.pdf-111-1.png)

![SchusterThesis.pdf-111-2.png](SchusterThesis.pdf-111-2.png)
cos 


(4.66)

![SchusterThesis.pdf-111-3.png](SchusterThesis.pdf-111-3.png)
1  I 2 /Ic 2


L J0 =


(4.67)

![SchusterThesis.pdf-111-4.png](SchusterThesis.pdf-111-4.png)
2 eIc


To first order the junction behaves as an inductor but it becomes non-linear, the inductance rising

as the current approaches the critical current. An oscillator built from this non-linear inductor and

a standard capacitor will be anharmonic. According to the RCSJ model [Tinkham2004] the total

current can be written as



dV
I = C + V/R + I c sin  (4.68)

![SchusterThesis.pdf-111-5.png](SchusterThesis.pdf-111-5.png)

dt

When there is no net current one can use the Josephson relations (Eqs. 4.63 and 4.64) to get the

equation of motion (in the phase) of


d 2  J0

L
dt 2 + R


d

+ sin  = 0 (4.69)

![SchusterThesis.pdf-111-9.png](SchusterThesis.pdf-111-9.png)
dt


d


![SchusterThesis.pdf-111-6.png](SchusterThesis.pdf-111-6.png)

![SchusterThesis.pdf-111-7.png](SchusterThesis.pdf-111-7.png)

![SchusterThesis.pdf-111-8.png](SchusterThesis.pdf-111-8.png)

 2


 p =  L J0 C (4.70)

![SchusterThesis.pdf-111-10.png](SchusterThesis.pdf-111-10.png)

![SchusterThesis.pdf-111-11.png](SchusterThesis.pdf-111-11.png)

This is the equation of motion for a rigid pendulum, with small angle resonant frequency,  p the

plasma frequency, and viscous drag L J0 /R , and mass  2 / 4 E C . The corresponding Hamiltonian

is [Tinkham2004]


 2
H trans =  4 E C  2  E J cos  (4.71)

![SchusterThesis.pdf-111-12.png](SchusterThesis.pdf-111-12.png)

This is of course exactly the CPB Hamiltonian (though in our simplistic treatment n g is not present 1 ).

Rather than using the exact Mathieu solution, lets continue the harmonic oscillator analogy, ex-

panding the cosine potential of Eq. 4.71 as a power series.


 2
H trans 4 E C
 


 2  2

 2  E J (1 



2

+ 
2


4! + -    ) (4.72)


![SchusterThesis.pdf-111-13.png](SchusterThesis.pdf-111-13.png)

![SchusterThesis.pdf-111-14.png](SchusterThesis.pdf-111-14.png)

![SchusterThesis.pdf-111-15.png](SchusterThesis.pdf-111-15.png)

As in section 3.1.8 the harmonic oscillator portion can be reexpressed in dimensionless units as


2 Z C
 +

 R K



![SchusterThesis.pdf-111-18.png](SchusterThesis.pdf-111-18.png)

2 Z C

=

![SchusterThesis.pdf-111-19.png](SchusterThesis.pdf-111-19.png)
R K


![SchusterThesis.pdf-111-16.png](SchusterThesis.pdf-111-16.png)

b =


R K

![SchusterThesis.pdf-111-17.png](SchusterThesis.pdf-111-17.png)

4 Z C


(4.73)


![SchusterThesis.pdf-111-20.png](SchusterThesis.pdf-111-20.png)

8 E C

(4.74)

![SchusterThesis.pdf-111-21.png](SchusterThesis.pdf-111-21.png)
E J


8 E C


![SchusterThesis.pdf-111-22.png](SchusterThesis.pdf-111-22.png)

1 The effect of n g is difficult to understand in this interpretation and is best thought of as a constant vector potential
added to the momentum, equivalent to acquiring an Aharonov-Bohm phase when the rotor makes a full revolution.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 110


![SchusterThesis.pdf-112-3.png](SchusterThesis.pdf-112-3.png)

![SchusterThesis.pdf-112-8.png](SchusterThesis.pdf-112-8.png)

![SchusterThesis.pdf-112-13.png](SchusterThesis.pdf-112-13.png)

![SchusterThesis.pdf-112-5.png](SchusterThesis.pdf-112-5.png)

![SchusterThesis.pdf-112-10.png](SchusterThesis.pdf-112-10.png)

![SchusterThesis.pdf-112-14.png](SchusterThesis.pdf-112-14.png)

![SchusterThesis.pdf-112-4.png](SchusterThesis.pdf-112-4.png)

![SchusterThesis.pdf-112-6.png](SchusterThesis.pdf-112-6.png)

![SchusterThesis.pdf-112-9.png](SchusterThesis.pdf-112-9.png)

![SchusterThesis.pdf-112-11.png](SchusterThesis.pdf-112-11.png)

![SchusterThesis.pdf-112-15.png](SchusterThesis.pdf-112-15.png)

![SchusterThesis.pdf-112-35.png](SchusterThesis.pdf-112-35.png)

![SchusterThesis.pdf-112-36.png](SchusterThesis.pdf-112-36.png)

![SchusterThesis.pdf-112-37.png](SchusterThesis.pdf-112-37.png)

![SchusterThesis.pdf-112-38.png](SchusterThesis.pdf-112-38.png)

![SchusterThesis.pdf-112-49.png](SchusterThesis.pdf-112-49.png)

![SchusterThesis.pdf-112-39.png](SchusterThesis.pdf-112-39.png)

![SchusterThesis.pdf-112-40.png](SchusterThesis.pdf-112-40.png)

![SchusterThesis.pdf-112-41.png](SchusterThesis.pdf-112-41.png)

![SchusterThesis.pdf-112-42.png](SchusterThesis.pdf-112-42.png)

![SchusterThesis.pdf-112-43.png](SchusterThesis.pdf-112-43.png)

![SchusterThesis.pdf-112-44.png](SchusterThesis.pdf-112-44.png)

![SchusterThesis.pdf-112-45.png](SchusterThesis.pdf-112-45.png)

![SchusterThesis.pdf-112-48.png](SchusterThesis.pdf-112-48.png)

![SchusterThesis.pdf-112-46.png](SchusterThesis.pdf-112-46.png)

![SchusterThesis.pdf-112-47.png](SchusterThesis.pdf-112-47.png)

![SchusterThesis.pdf-112-0.png](SchusterThesis.pdf-112-0.png)

![SchusterThesis.pdf-112-33.png](SchusterThesis.pdf-112-33.png)

![SchusterThesis.pdf-112-34.png](SchusterThesis.pdf-112-34.png)

![SchusterThesis.pdf-112-30.png](SchusterThesis.pdf-112-30.png)

![SchusterThesis.pdf-112-31.png](SchusterThesis.pdf-112-31.png)

![SchusterThesis.pdf-112-32.png](SchusterThesis.pdf-112-32.png)

![SchusterThesis.pdf-112-27.png](SchusterThesis.pdf-112-27.png)

![SchusterThesis.pdf-112-28.png](SchusterThesis.pdf-112-28.png)

![SchusterThesis.pdf-112-29.png](SchusterThesis.pdf-112-29.png)

![SchusterThesis.pdf-112-24.png](SchusterThesis.pdf-112-24.png)

![SchusterThesis.pdf-112-25.png](SchusterThesis.pdf-112-25.png)

![SchusterThesis.pdf-112-26.png](SchusterThesis.pdf-112-26.png)

![SchusterThesis.pdf-112-21.png](SchusterThesis.pdf-112-21.png)

![SchusterThesis.pdf-112-22.png](SchusterThesis.pdf-112-22.png)

![SchusterThesis.pdf-112-23.png](SchusterThesis.pdf-112-23.png)

![SchusterThesis.pdf-112-18.png](SchusterThesis.pdf-112-18.png)

![SchusterThesis.pdf-112-19.png](SchusterThesis.pdf-112-19.png)

![SchusterThesis.pdf-112-20.png](SchusterThesis.pdf-112-20.png)

![SchusterThesis.pdf-112-12.png](SchusterThesis.pdf-112-12.png)

![SchusterThesis.pdf-112-16.png](SchusterThesis.pdf-112-16.png)

![SchusterThesis.pdf-112-17.png](SchusterThesis.pdf-112-17.png)

![SchusterThesis.pdf-112-2.png](SchusterThesis.pdf-112-2.png)

![SchusterThesis.pdf-112-7.png](SchusterThesis.pdf-112-7.png)

E J cos 


1.5

1

0.5

0

-0.5

-1




|Col1|Col2|Col3|Col4|
|---|---|---|---|


![SchusterThesis.pdf-112-1.png](SchusterThesis.pdf-112-1.png)

Figure 4.14: a) Rotor analogy for the transmon. The transmon Hamiltonian can be understood
as a quantum rotor with offset charge n g acting as a constant vector potential. For large E J /E C ,
there is a significant gravitational pull on the pendulum and the system typically remains in the
vicinity of vanishing angle  . Only tunneling events between adjacent cosine wells (i.e. a full 2 
rotor movement) will acquire an Aharonov-Bohm like phase due to n g . The tunneling probability
decreases exponentially with E J /E C , explaining the exponential decrease of the charge dispersion.
b) Cosine potential (black solid line) with corresponding eigenenergies and squared moduli of the
eigenfunctions.

where as before R K = h/ 4 e 2 is the resistance quantum. Writing the phase  in terms of the

dimensionless operators 1 (as in Eq. 3.46)


8 E C

![SchusterThesis.pdf-112-54.png](SchusterThesis.pdf-112-54.png)

E J




1 / 4
(4.75)


1 / 4
(4.76)



1 / 4
(4.75)




b + b 
 =

![SchusterThesis.pdf-112-50.png](SchusterThesis.pdf-112-50.png)

2

b b 
N  = 



b + b 

![SchusterThesis.pdf-112-51.png](SchusterThesis.pdf-112-51.png)
4 Z C /R K =  2

![SchusterThesis.pdf-112-52.png](SchusterThesis.pdf-112-52.png)

![SchusterThesis.pdf-112-53.png](SchusterThesis.pdf-112-53.png)

b b
R K /Z C = 


E J


E J

![SchusterThesis.pdf-112-59.png](SchusterThesis.pdf-112-59.png)

8 E




![SchusterThesis.pdf-112-56.png](SchusterThesis.pdf-112-56.png)

![SchusterThesis.pdf-112-55.png](SchusterThesis.pdf-112-55.png)

![SchusterThesis.pdf-112-57.png](SchusterThesis.pdf-112-57.png)

8 E


![SchusterThesis.pdf-112-58.png](SchusterThesis.pdf-112-58.png)

Substituting Eq. 4.75 into the Hamiltonian of Eq. 4.71 one obtains



1
H trans   p ( b  b +
 2



1 E C

)
2 


12 C ( b + b  ) 4 (4.77)


![SchusterThesis.pdf-112-60.png](SchusterThesis.pdf-112-60.png)

![SchusterThesis.pdf-112-61.png](SchusterThesis.pdf-112-61.png)

In perturbation theory, the energy will be changed to first order, only by diagonal matrix elements,

therefore we can simplify H trans by collecting only the diagonal terms from ( b + b  ) 4 that can be

written in the form ( b  b ) 2 . Plugging these terms (see Ex. 4.3.1 to derive the prefactor) into Eq. 4.77

gives the energy of the j th level to be



1
E trans j   p ( j +
 2



1 E C

)
2  12


12 C (6 j 2 + 6 j + 3) (4.78)


![SchusterThesis.pdf-112-62.png](SchusterThesis.pdf-112-62.png)

![SchusterThesis.pdf-112-63.png](SchusterThesis.pdf-112-63.png)

Something truly magical has happened here, a mathematical accident or a deep and beautiful

piece of physics depending on how one looks at it. The anharmonic (last) term which came from

![SchusterThesis.pdf-112-64.png](SchusterThesis.pdf-112-64.png)

1 For convenience in section 3.1.8 the charge operator q was chosen as the position coordinate but here the phase
 is chosen as the position coordinate. This is merely a sign convention and has no physical significance. Also where
as the operators in section 3.1.8 were written in terms of charge,flux, and impedance, in this section everything is
written in terms of dimensionless number, phase, and dimensionless impedance ( Z C /R K ).


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 111

the E J term in the original Hamiltonian only depends on E C . This is the origin of Eq. 4.61a, and is

the equivalent of the anharmonicity of a mass in a quartic potential only depending on the particle

mass ( E C ) not the height of the potential well ( E J ) in which it resides 1 (see Fig. 4.14). This
 

means that one can pick the anharmonicity by choosing E C and then choose E J to get the desired

 p .

Since to first order in this perturbation the wavefunctions are the same as harmonic oscillator

wavefunctions we can easily determine all of the matrix elements of the system, as well as exploit

all of the symmetries of the harmonic oscillator, while still getting the anharmonicity of a qubit.

Exercise 4.3.1. Find

 j | ( b + b  ) 4 | j 

where | j  is a harmonic oscillator number state 2 .

######### 4.3.4 ######### Transmon for Circuit QED

In the previous sections, we saw that the transmon by itself had at least the spectral characteristics

to perform as a qubit. In order to use it for circuit QED (or any other application), it must still have

a reasonable coupling to the cavity. At first glance, the transmon seems to be doomed. The simple

quantum capacitor argument in the measurement was that the curvature in the CPB bands was like

a capacitor which shifted the cavity frequency. In order to suppress the charge noise we flattened

the bands completely, essentially eliminating all curvature. However, as I said earlier the quantum

capacitor/curvature argument is really just an approximate DC limit for the dipole coupling. And

though the static dipole moment is suppressed in the large E J /E C limit, the transition dipole remains

large.

In the asymptotic limit, the proper expression for the dipole coupling is given (as in Eq. 3.73) by


g ij = eV 0  i | N  | j  =


E J

![SchusterThesis.pdf-113-0.png](SchusterThesis.pdf-113-0.png)
2 g

![SchusterThesis.pdf-113-1.png](SchusterThesis.pdf-113-1.png)

8 E C




1 / 4
 i | ( b  b  ) | j  (4.79)



This is the same expression 3 for g derived in section 3.3, but now that the energy eigenstates involve

many charge states we take care to include the matrix elements for different transitions explicitly.

![SchusterThesis.pdf-113-2.png](SchusterThesis.pdf-113-2.png)

1 This would present an interesting if not practical spectroscopic means of determining the local gravitational
acceleration g (or other restoring force independent of the inertia of the particle being acted on)
2 Hint: Expand ( b + b  ) 4 and use the commutation relations to rewrite it in terms of the number operator N = b  b .
3 Because  = C g /C  and E C  1 /C  is made large, it might appear that  can no longer be made close to unity
for large coupling. However, C  = C g + C j + C s , so by adding the new capacitance through the C g ,  can actually
be made larger in the high E J /E C regime. Further as discussed in detail in section 5.2 the extra degree of freedom
afforded by the shunt capacitor C s allows realization of nearly any  independent of other parameters.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 112

2

| 2|N|1 |  + 

1.5

|5|(b) |
|---|---|
|5||
|+ ||


0.5


![SchusterThesis.pdf-114-0.png](SchusterThesis.pdf-114-0.png)

50 100


0 |f 

|e 

|g 


E J / E c

Figure 4.15: a) Plot of transmon charge matrix elements vs. E J /E C . Note that despite the fact that
the curvature in the bands disappears quickly (see Fig. 4.12), the matrix element responsible for the
transmon-cavity coupling (  1 | n | 0  ) actually increases. Also while the matrix elements for single level
transitions remain large, that of two-level transitions are small and are strongly suppressed. This
is due to parity of the CPB energy levels which begin to resemble harmonic oscillator eigenstates,
which alternate between even and odd parity. The number operator (which resembles the position of
the harmonic oscillator) is odd, so transitions involving an even number of excitations are strongly
suppressed. This parity property becomes strong as the resemblance of a CPB to a harmonic
oscillator grows with E J /E C . The quartic potential of the transmon preserves the harmonic oscillator
parity while the cubic potential of a phase qubit, which does not, allows such transitions. The fact
that higher order transitions are suppressed greatly simplifies the treatment of the transmon in
circuit QED. b) Energy level diagram for circuit QED with multilevel qubit. The vertical levels
represent photon numbers in the cavity while the qubit levels are listed left to right. The cavity
levels are detuned from the g  e transition by and the higher auxiliary levels are each detuned
by  from the previous CPB transition at high E J /E C .


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 113

A plot of several relevant matrix elements is shown in Fig. 4.15.

For the especially relevant case of adjacent levels one gets a coupling of


E J

![SchusterThesis.pdf-115-0.png](SchusterThesis.pdf-115-0.png)
2( j + 1)

![SchusterThesis.pdf-115-1.png](SchusterThesis.pdf-115-1.png)

8 E C




E J
2( j + 1)

8 E




1 / 4
 


g j , j+1 = g


(4.80)


The quantity in parenthesis is the scale of n 1 / 2 , the number of Cooper pairs tunneling in the oscillator.

In the traditional CPB, there is one Cooper pair, but even at E J /E C = 100 there are only  15

Cooper pairs sloshing back and forth. Because more Cooper pairs are involved the dipole moment

actually increases 1 , but only very slowly. Although it is tempting to again truncate the Hilbert

space, ignoring the non-qubit levels, in this new regime of lower anharmonicity one does so at ones

peril. The responsibility to keep track of all the CPB levels is in a certain sense the main price one

pays using the transmon. One should never have ignored higher levels even in the charge regime,

but it was difficult keep track of them since they were at energies difficult to measure directly, and

were highly sensitive to charge noise. Now their effects are felt explicitly, but can also be kept track

of more easily.

The reason we cannot ignore higher levels is that in this E J /E C regime one often works with the

charging energy similar to the coupling ( E C g ). That means that though the transition frequencies


are different enough to use fast pulses (1 / E C /h ) they are similarly detuned  E C , especially
 

well into the dispersive limit. Graphically these auxiliary levels can be accounted for by extending

the energy ladder diagrams to the right as in Fig. 4.15. At minimum we must keep the lowest three

levels to write down the dispersive Hamiltonian



  
H eff =


+ (   r  +   eff  z ) a  a (4.81)


![SchusterThesis.pdf-115-2.png](SchusterThesis.pdf-115-2.png)

with an effective Lamb-shifted transition frequency  a  =  01 +  01 and cavity frequency  r  =

 r  01  02 . With these dressed transitions the Hamilitonian looks similar to the traditional CPB
 

case except that one gets an effective dispersive shift which depends on the next highest level



 12
 eff =  01
 2



 02
+


(4.82)


![SchusterThesis.pdf-115-3.png](SchusterThesis.pdf-115-3.png)

![SchusterThesis.pdf-115-4.png](SchusterThesis.pdf-115-4.png)

where


g ij 2
 ij (4.83)
  ij  r

![SchusterThesis.pdf-115-5.png](SchusterThesis.pdf-115-5.png)



![SchusterThesis.pdf-115-6.png](SchusterThesis.pdf-115-6.png)

1 The derivation of the fine structure limit assumes only a single Cooper pair tunneling. Too make it apply at
high E J /E C one can multiply by the term in parenthesis in Eq. 4.80.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 114

150


b)

100


100

0

-100


50

0

-50

|Col1| > 0|
|---|---|


80


![SchusterThesis.pdf-116-0.png](SchusterThesis.pdf-116-0.png)


20

|a) 0 -0.1 0 0.1   / 01|60 E / 40 E J|
|---|---|

0.2


-0.1 0 0.1 0.2
 /  01


Figure 4.16: a) Dispersive frequency shift,  as a functino of detuning between cavity and
transmon and energy ratio E J /E C , for fixed transition frequency  01 , with  = 1 and n g = 1. b)
The bottom panel depicts cross-sections of the 3D plot for E J /E C = 20 (a),40(b), 60 (c), and 80(d).
Inset shows energy level configuration and regimes for the dispersive shift. When the transmon
is detuned negatively or by more than  then the dispersive shift is negative (  < 0). In the
straddling regime, when 0 <  <  , the dispersive shift is positive (  > 0).

is the dispersive shift for each transition inside the transmon. Using equation 4.79,  ij can be written


as


E J
 ij = 2

![SchusterThesis.pdf-116-1.png](SchusterThesis.pdf-116-1.png)

8 E C




E J
 ij = 2

8 E




1 / 2 2 2
g i ( b b  ) j
|  |  | | (4.84)

![SchusterThesis.pdf-116-2.png](SchusterThesis.pdf-116-2.png)

 ij




1 / 2 2 2
g |  i | ( b  b  ) | j |

 ij




where  ij  ij  r . Plugging this approximate expression into Eq. 4.82 gives
 



g 2
 eff
 


  p

(4.85)
4(   E C )

![SchusterThesis.pdf-116-4.png](SchusterThesis.pdf-116-4.png)



![SchusterThesis.pdf-116-3.png](SchusterThesis.pdf-116-3.png)

Because of the interplay between the anharmonicity and the detuning there are three distinct regimes

of dispersive coupling (see Fig. 4.16). When both and   E C are the same sign then  eff < 0.

In the special case where they are opposite signs, which occurs when 0 <  < E C , then  eff > 0

and is also significantly enhanced. Another thing to note in Fig. 4.16 is that when =  or any

other integer multiple of the anharmonicity, one of the transitions will be resonant with the cavity.

If this occurs even for higher transitions (if there are enough photons in the cavity) then even if

the matrix elements for such a process are small the energy denominator will go to zero causing the

dispersive shift to explode. This can be a source of charge noise based dephasing because higher

levels are more sensitive to charge. Using a negative detuning ( < 0) can help avoid some of these

complications 1 .

Whereas before we only concerned ourselves with the coupling induced decay due to the qubit

![SchusterThesis.pdf-116-5.png](SchusterThesis.pdf-116-5.png)

1 Negative detuning does not eliminate the problem altogether as high levels may change their energy by more than
 01 with charge.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 115

transition (  01 ), now we must consider higher lying transitions. If these transitions are resonant

with the cavity or its excitations, the qubit could be excited to the one of the auxiliary levels,

incoherently absorbing one or more photons. During logic operations when the cavity would be

empty, this process would not be possible, but it might interfere with a measurement of the qubit

state.

######### 4.3.5 ######### Other Sources of Decoherence

While we have already discussed the effects of charge noise we must also consider how the transmon

responds to other decay and dephasing mechanisms. In this section we will discuss the action of

critical current and flux noise, as well as briefly discuss the transmons tolerance to charging energy

fluctuations and dielectric noise.

Flux noise

At degeneracy flux noise will enter through the dependence of the plasma frequency  p on E J and

the effective E J on the flux. At  = 0 the qubit is first order insensitive to flux fluctuations, and so

the second order contribution will dominate. The dimensionless dephasing rate is then


![SchusterThesis.pdf-117-5.png](SchusterThesis.pdf-117-5.png)

  

![SchusterThesis.pdf-117-0.png](SchusterThesis.pdf-117-0.png)

 p


  2

![SchusterThesis.pdf-117-3.png](SchusterThesis.pdf-117-3.png)

 p


 2

![SchusterThesis.pdf-117-4.png](SchusterThesis.pdf-117-4.png)

  2


 
8 E C E J cos

![SchusterThesis.pdf-117-6.png](SchusterThesis.pdf-117-6.png)

 0




  2  2

![SchusterThesis.pdf-117-9.png](SchusterThesis.pdf-117-9.png)

4 2


tan 2  

![SchusterThesis.pdf-117-10.png](SchusterThesis.pdf-117-10.png)

 0




   2  2 2 (4.86)


  2  2


![SchusterThesis.pdf-117-1.png](SchusterThesis.pdf-117-1.png)

![SchusterThesis.pdf-117-7.png](SchusterThesis.pdf-117-7.png)

![SchusterThesis.pdf-117-11.png](SchusterThesis.pdf-117-11.png)

= 


+ 2 


![SchusterThesis.pdf-117-2.png](SchusterThesis.pdf-117-2.png)

![SchusterThesis.pdf-117-8.png](SchusterThesis.pdf-117-8.png)

![SchusterThesis.pdf-117-12.png](SchusterThesis.pdf-117-12.png)

![SchusterThesis.pdf-117-13.png](SchusterThesis.pdf-117-13.png)

Assuming a universal flux noise[Wellstood1987] of   = 3  10  5  0 , gives a quality factor of Q  

10 8 , well beyond current limitations.

Critical current noise

Noise in the critical current will once again directly translate into noise of E J . In the large E J /E C

limit the transition frequency is well approximated by the plasma frequency  p and the first order

deviations are characterized by



E J

  p =  E J    8  E  J p E C


 E J


![SchusterThesis.pdf-117-15.png](SchusterThesis.pdf-117-15.png)

8 E J E C =  E J

   p 2 E



J  (4.87)

![SchusterThesis.pdf-117-17.png](SchusterThesis.pdf-117-17.png)

2 E J


![SchusterThesis.pdf-117-14.png](SchusterThesis.pdf-117-14.png)

![SchusterThesis.pdf-117-16.png](SchusterThesis.pdf-117-16.png)

which, because of the square root is half as sensitive as it was in the charge regime.

Charging energy fluctuations

The same argument can be made for charging energy fluctuations.


 E  C

 p =  E C


(4.88)

![SchusterThesis.pdf-117-19.png](SchusterThesis.pdf-117-19.png)
2 E C


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 116

However remember that at degeneracy ( n g = 1) the charge qubit could be made nominally insensitive

to charging energy fluctuations. That fact was derived using the two charge state approximation, in

practice at E J /E C 1 the first order fluctuations are only reduced by a factor of ten. At present


the amount of charging energy fluctuations is unknown and thought not to be a limiting factor. The

transmon the capacitance has changed from being mostly in the junction barrier with high fields and

small distances to being a large geometric capacitance. If significant charging energy fluctuations

exist, studying the transmon would help determine their location.

Dielectric noise

While the dielectric noise has the potential to cause decay in the same manner and at the same

rate (half of the energy is always in the electric field), the transmon gives the freedom to choose

the participation ratio, the locations of the fields. By choosing a large external capacitance one

can make most of the field live in the substrate, whereas by increasing the junction capacitance or

making an overlap capacitor one can put the fields in a thin insulating barrier. This freedom will

allow (better) controlled experiments on the electrical quality factor of the junctions.

Quasiparticles

The transmon can have a large Q because energy can only be lost by photons at the transmission

frequency, and the impedance of the environment at that frequency is very carefully controlled.

Quasiparticles once created, can lose arbitrarily small amounts of energy, making them very efficient

at dissipating the energy stored in the coherent qubit oscillations. In section 4.1.3, this loss was

modeled by assuming a two fluid model, where a resistive fluid (quasiparticles) were shunted by a

superconducting but inductive fluid. That model captured much of the essential physics, describing

the exponential temperature dependence and effect of junction tunnel resistance on the qubit decay

rate.

Here that model is extended to include the density of states of the superconductor and the matrix

elements for transitions out of the qubit excited state [Lutchyn2006].


![SchusterThesis.pdf-118-2.png](SchusterThesis.pdf-118-2.png)

 qp 1 = N 4 N qp e


i QP e 2
|  |  i | | QP | | e | | 2 (4.89)


 qp 1 = N qp


R K

![SchusterThesis.pdf-118-1.png](SchusterThesis.pdf-118-1.png)

R n


![SchusterThesis.pdf-118-0.png](SchusterThesis.pdf-118-0.png)

![SchusterThesis.pdf-118-3.png](SchusterThesis.pdf-118-3.png)

![SchusterThesis.pdf-118-4.png](SchusterThesis.pdf-118-4.png)




where N qp is the number of quasiparticles in the transmon, N e is the total number of electrons, and


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 117

QP is an operator which represents suddenly changing the gate voltage n g by one electron.



1
1 + e  /k B T  (4.90)




N qp = 1 + N e


![SchusterThesis.pdf-119-0.png](SchusterThesis.pdf-119-0.png)




There is a lot happening in Eq. 4.89, so lets analyze the origin of each term. The ratio of the resis-


tances and quasiparticle fraction are the same terms as in the more naive treatment in section 4.1.3,

though now we have assumed that even at zero temperature there will be one quasiparticle (an odd

number of electrons in the metal). If the number of quasiparticles is independent of the volume of

the CPB then N qp /N e 1 /V and quasiparticle dissipation will be reduced in the larger transmon.


It is thought that the quasiparticle number may scale with the volume ( N qp /N e const). The


additional quasiparticles able to tunnel would be compensated by additional Cooper pairs shunting


![SchusterThesis.pdf-119-1.png](SchusterThesis.pdf-119-1.png)

them. In addition, there is now a factor representing the density of states 


T/ a to which a


quasiparticle can tunnel. Finally, a quasiparticle tunneling event can be modeled as a sudden change

from n g = 1 to n g = 0, which might not change the state of the qubit. For a CPB in the charge

regime, going from n g = 1 to n g = 0 goes from an even superposition of zero and one Cooper pair to

a state with zero Cooper pairs, giving a transition probability of 1 / 2. In the transmon, this amount

can be reduced.

######### 4.3.6 ######### Transmon Summary

The transmon is an elegant new qubit which appears to eliminate the effect of charge noise. This

should dramatically enhance the ability for such qubits to be operated at high Qs and to later scale

(eliminating the need for individual charge biasing) to larger numbers of qubits, where individual

voltage biasing and feedback would be difficult. It does so while improving nearly every other

performance metric over the traditional CPB and thus is a very promising qubit candidate. The

only penalty is that the anharmonicity formerly of order unity is now only 10% requiring much more

careful attention to the effects of extra levels. This initial theoretical analysis does not predict the

smaller anharmonicity to be a significant barrier, but care must be taken. More information on the

design and fabrication of the transmon, which was used for the last two experiments performed, is

presented in section 5.3. Experimental work is also reported in sections 8.3 and 9.3.


-----


CHAPTER 4. DECOHERENCE IN THE COOPER PAIR BOX 118

Noise transmon CPB flux qubit phase qubit
E J /E C = 85 E J /E C = 1


![SchusterThesis.pdf-120-0.png](SchusterThesis.pdf-120-0.png)

![SchusterThesis.pdf-120-1.png](SchusterThesis.pdf-120-1.png)

Dephasing 1 /f amp. T 2 T 2 T 2 T 2

charge 10  4 e E A 0 . 4 ms T  1  s  T 110 ns T B  0 . 1 s T C


![SchusterThesis.pdf-120-2.png](SchusterThesis.pdf-120-2.png)

flux 10  6 5  0 E F D 0 . 4 ms  T 0 . 1 ms  T   120 ns E E


I 0 10  6 I 0 E F  35  s T 17  s T H I J   40 ns E K G


measured 150 ns E > 500 ns E H 20 ns E I ; 120 ns E J 160 ns E K


![SchusterThesis.pdf-120-3.png](SchusterThesis.pdf-120-3.png)

![SchusterThesis.pdf-120-4.png](SchusterThesis.pdf-120-4.png)

relaxation T 1 T 1 T 1 T 1

90 ns E  7  s E H 900 ns E L 110 ns E K

![SchusterThesis.pdf-120-5.png](SchusterThesis.pdf-120-5.png)

Table 4.1: Comparison of representative relaxation and dephasing times for various superconducting
qubit designs. The symbol E denotes experimental data, T indicates theoretical predictions, and   
marks the noise channel most likely limiting the performance of the qubit. Entries marked with   
are evaluated at a sweet spot (i.e. second-order noise). A: [Zorin1996] B: [Bertet2007] C: [Tian2000]
D: [Wellstood1987, Yoshihara2006] E: [Bertet2004] F: [VanHarlingen2004] G: [Simmonds2004] H:

[Wallraff2005] I: [Chiorescu2004] J: [Bertet2004] K: [Steffen2006] L: [Chiorescu2004]


-----


### Chapter 5

## Design and Fabrication

This chapter is intended to be a practical guide for the design and fabrication of circuit QED

components. The focus is towards creating robust processes which are tolerant of variations in envi-

ronmental conditions and operator procedure. Robustness comes not just from making lithography

and depositions repeatable, but also from designing circuits which realize optimal parameters with

large tolerances. The chapter is divided in to a section for each component, the cavity, the CPB,

and the circuit board. For each component the simulations and calculations are performed to esti-

mate the circuit parameters of a given geometry. The circuits are created with different lithography

(optical and electron beam) and deposition techniques (evaporation and sputtering), each imposing

its own unique constraints. A description of the thought process behind each design decision and

examples of what things should look like when they are working are shown for each step of the

process.

####### 5.1 ####### Cavity

######### 5.1.1 ######### Design Considerations

There are three primary cavity parameters, the resonator impedance, frequency, and quality factor.

The frequency is determined by the length. The impedance is controlled by the ratio of the center pin

thickness to the size of the gap between the center pin and ground planes. Finally, the quality factor is

determined by the size of coupling capacitors at the input and output. The geometric realizations of

these parameters are nearly independent. Small effects such as the loading of the coupling capacitors

adjust the frequency and impedance on resonance can be modeled and compensated. In addition,

while errors in the design or fabrication will affect the exact values of the cavity parameters, the

119


-----


CHAPTER 5. DESIGN AND FABRICATION 120

![SchusterThesis.pdf-122-0.png](SchusterThesis.pdf-122-0.png)

![SchusterThesis.pdf-122-1.png](SchusterThesis.pdf-122-1.png)

![SchusterThesis.pdf-122-2.png](SchusterThesis.pdf-122-2.png)

Figure 5.1: Resonator sample and input/output capacitors. a) The resonator is composed of a half
wave coplanar waveguide. The CPW structure can be resolved at the input and output end with
metal being beige and substrate dark. In the resonator itself the magnification cannot be resolved


-----


CHAPTER 5. DESIGN AND FABRICATION 121

physics is such that only extreme errors such as metal flakes in the gap will cause device failure.

This sort of intrinsic robustness allows us to use the same mask on different substrates and change

the coupling or experiment with different qubit geometries without drastically changing the cavity

design.

The fundamental frequency of the cavity is set by the effective speed of light and the length of the

resonator. When using a substrate mad e from a single material the effective dielectric constant, and

thus effective speed of light can be calculated analytically using Eq. 3.25. The length of transmission

line required to attain a / 2 resonance frequency is then given by


 =


(5.1)

![SchusterThesis.pdf-123-1.png](SchusterThesis.pdf-123-1.png)
 r


![SchusterThesis.pdf-123-0.png](SchusterThesis.pdf-123-0.png)

 eff 1 / 2


The use of multiple dielectrics (such as SiO 2 on Si) is much more difficult to calculate exactly

and slightly modify the effective dielectric constant. Small perturbations in the electrical length

also arise from the loading due to the kinetic inductance [Yoshida1995] and the coupling capacitors.

While it may be difficult to calculate the exact effective speed, the frequency can still be adjusted

linearly by adjusting the length. In practice, it is easier to make a set of resonators once, and

then adjust the length, keeping all other parameters the same, to compensate these shifts if higher

precision is required. The typical shifts due to kinetic inductance (see Sec. 7.1.1) are approximately

5  10%. The loading of the coupling capacitors gives a shift  ( q in + q out )  r . These shifts are

in principle very repeatable, but in practice fabrication errors can lead to some randomness in their

values. If the pattern is over or under exposed it can change the effective wave velocity somewhat,

and the value of the coupling capacitors significantly. When the same pattern is made it is typically

repeatable to within 1  2% or about 50  100 MHz. Adding a few hundred nanometers of oxide

to the silicon substrates changes the frequency by  500 MHz. Resonators are very repeatable on

repeated cool downs with resonant frequencies changing by of order 1 MHz which is about one part

in 10  4 . The resonators are designed to be as modular as possible. In order to allow resonators of

substantially different lengths to mate to the same printed circuit board they are made to meander

(see Fig. 5.1). This has the additional advantage of making the circuit smaller and thus helping to

avoid parasitic modes. If the curvature of the meanders is much less than the gap size the impedance

will not be affected (see 5.1).

The characteristic impedance ( Z 0 ) can be calculated using Eq. 3.24. The kinetic inductance and

dielectric composition also affect the exact value of the impedance. One might think that the cavity


-----


CHAPTER 5. DESIGN AND FABRICATION 122

coupling would be very sensitive to its characteristic impedance, but actually for a Fabry-Perot

cavity small differences in the internal impedance are not very important. Rather the coupling

is determined almost completely by the ratio and size of the coupling capacitors. The internal

impedance does affect the vacuum field strength, but it depends on geometry and dielectric constant

rather weakly, so variations away from 50 are typically small.

The quality factor can be determined by the size of the coupling capacitors using Eq. 3.18. For

the highest quality factors the coupling capacitors can be formed by having a gap in the centerpin.

The strength of this coupling can be made arbitrarily small by making the gap larger (see Fig. 5.1).

For larger coupling (lower external Q), the capacitors are realized using planar interdigitated finger

capacitors. The minimum width and spacing of the fingers is set by the minimum feature size for our

optical lithography process 1 of 2  m. The length of the fingers can be adjusted as can the number of

fingers. In order for the fingers to be accurately represented as a lumped element capacitor they must

be much smaller than the wavelength. If the fingers get too long their inductance becomes significant,

which can alter the capacitance values or create undesired parasitic resonances. In practice 2  m

fingers with 2  m spacing that are 200  m or less are safe. To find the values of the capacitors,

we simulate their DC capacitance with Maxwell , a commercial electromagnetic simulation package.

Their RF performance was also be simulated using another simulation program, Sonnet . Some

capacitance values are given in Table XX, but a good rule of thumb is that a symmetric resonator

with coupling capacitors each consisting of one pair of fingers 100  m in length, gives a quality factor

of  10 , 000, and that the Q scales inversely with the square of the number of fingers (as per Eq.

3.18).

The frequency shifts due to the coupling capacitors can be calculated using Eq. 3.20. The trans-

mission coefficient (Eq. 3.19) is determined by the ratio of the coupling capacitors. Initially sym-

metric capacitors were used, but as described in section 3.4.5, it is more efficient to use asymmetric

coupling capacitors with a larger output capacitor limiting the external quality factor.

The desired characteristic impedance determines the ratio of the pin size to the gap, but it does

not say what the absolute scale should be. We attempt to keep the gap size as small as possible

without straining the design tolerances. This approach keeps the electromagnetic field confined to

a small volume, and away from lossy PCB materials and the backing ground plane which might

![SchusterThesis.pdf-124-0.png](SchusterThesis.pdf-124-0.png)

1 While our optical lithography equipment is in principle capable of realizing sub-micron feature sizes, imposing a
2  m feature limit, reduces mask costs and more importantly makes the process more robust.


-----


CHAPTER 5. DESIGN AND FABRICATION 123

also be lossy or give parasitic modes. For most resonators a center pin width of 10  m was chosen,

though 5  m has also been tested successfully.

Such a center pin width can be realized with standard optical lithography, but is well beyond

the capabilities of commercial PCB makers. Typical PCB tolerances are  75  m. In order to

accommodate these tolerances the input and output CPWs on the PCB have a centerpin width

 500  m. In order to prevent reflections which could reduce the measurement efficiency, one must

smoothly taper the centerpin (and gap) width from the PCB to the chip. The overall transverse

dimension can be reduced without reflections if the ratio between the gap and centerpin widths is

maintained and they are reduced gradually. In a CPW, on a very thick subsrate, this can be done

with a simple linear taper. However, when the transverse width is comparable to the thickness of

the substrate, the CPW mode acquires some microstrip character. This additional length scale is

taken into account by equation 3.24 for the impedance, but creates some curvature when going from

widths comparable to the substrate thickness to very narrow lines 1 . This taper is one of the primary

reasons for selecting the CPW geometry as its characteristic impedance can remain unchanged over

a wide range of transverse dimensions. This allows one to couple to large circuit board features

easily while attaining high electric field densities and confinement (high Q) in the actual resonator.

######### 5.1.2 ######### Optical Lithography

The resonator patterns are made using optical lithography, based on a resist system which uses

Microchem lift off resist (LOR5A) as a sacrificial bottom layer and Shipley (S1808) photoresist

as a primary layer. The base recipe is presented in table D. In this resist system, the pattern is

transferred through a chrome mask via hard contact lithography to the top layer which is sensitive

to UV. The bottom layer behaves as though pre-exposed, due to a chemical additive and its etch

rate depends only on how it was pre-baked, not on the exposure. Areas which are exposed etch

through the top layer, exposing the sacrificial layer. The same developer can then uniformly etch

the bottom layer below the exposed regions at a well defined rate. With appropriately selected bake

temperatures and development time, an undercut profile such as the one shown in Fig. 5.3 can be

realized. Figure 5.3b is an example of how successful lithography should look, with the top layer

possessing a steep vertical wall, with no sagging, and an undercut of approximately two to three

times the LOR thickness.

![SchusterThesis.pdf-125-0.png](SchusterThesis.pdf-125-0.png)

1 For both the old and new resonator designs the dimensions were chosen such that all dimensions are small
compared to the substrate thickness allowing a simple linear taper to be used.


-----


CHAPTER 5. DESIGN AND FABRICATION 124

![SchusterThesis.pdf-126-2.png](SchusterThesis.pdf-126-2.png)

![SchusterThesis.pdf-126-4.png](SchusterThesis.pdf-126-4.png)

![SchusterThesis.pdf-126-3.png](SchusterThesis.pdf-126-3.png)

![SchusterThesis.pdf-126-1.png](SchusterThesis.pdf-126-1.png)

Figure 5.2: a) Lesker sputtering system. This system is used to deposit Nb via DC magnetron
sputtering. b) EVG mask aligner used in hard-contact mode to expose the photoresist through a
chrome mask. It is capable of sub-micron accuracy. c) A processed wafer of resonators prior to
dicing (hand modeling by Andreas Wallraff).

######### a) ######### b)

![SchusterThesis.pdf-126-5.png](SchusterThesis.pdf-126-5.png)

![SchusterThesis.pdf-126-0.png](SchusterThesis.pdf-126-0.png)

Figure 5.3: a) Ideal bi-layer resist profile. The wafer is spun with two layers of photoresist. The
undercut layer is made from LOR5A a photoresist with an additive which makes it etch at a rate
dependent only on the prebake temperature, not on exposure to light, and spins to about 500 nm.
The top layer is S1808, a positive photoresist, which spins to about 800 nm. When an exposed
portion is placed in a solution of developer it will dissolve. The bottom layer will then etch at a
uniform, slow, rate which can be used to control the undercut. This profile facilitates smooth
liftoff by ensuring that the deposited film on top of the resist is not connected to the film on the
substrate. b) SEM image of resist profile. Note that the top layer has a nearly vertical sidewall. If
the sidewall is not vertical the exposure is bad possibly due to poor contact with the mask. The top
layer should not sag and the thicknesses of both layers should be as desired.


-----


CHAPTER 5. DESIGN AND FABRICATION 125

![SchusterThesis.pdf-127-0.png](SchusterThesis.pdf-127-0.png)

![SchusterThesis.pdf-127-1.png](SchusterThesis.pdf-127-1.png)

![SchusterThesis.pdf-127-2.png](SchusterThesis.pdf-127-2.png)

Figure 5.4: This image shows the a gap capacitor in resist. Note that all resist characteristics
except the resist cross-section (shown in Fig. 5.3b) can be seen in this optical image, which can
be taken immediately after development (and before deposition). The top, bottom, and centerpin
appear as exposed substrate (beige). The gaps of the resonator are formed by continuous sections of
unexposed (and undeveloped) resist (darker). Finally the light beige on the border between the two
regions is the undercut. Note that the undercut still has resist on top, and so the final metal pattern
will be determined by the border between the undercut ring and the substrate, not the undercut
and the resist (which is substantially rounded). This sample had a little bit to much undercut and
so the resist protecting the gap capacitor is completely suspended. While this sample would be fine,
other resonators with longer gap capacitors might be damaged, so this is something to pay extra
attention too.

This process can be very sensitive to the baking temperature of the first layer, which determines

the etch rate. If developing this process on new equipment, one must check the hotplate uniformity

and temperature with a calibrated thermometer. If uniformity is a problem or if the surface is dirty

one can use an eighth inch thick piece of aluminum plate to spread the heat. It is probably also wise

to limit air flow over the wafer by placing it under a beaker cover (raised on glass slides to allow

some air flow).

The recipe in Table D should serve as a good starting point for optically patterning the resonators.

Because all optical mask aligners have slightly different spectral characteristics one must calibrate

the exact dosing to the specific machine. One should first start with a single layer of S1808 making

sure that the top layer will faithfully reproduce the edges.

Characterization of the resist processing is most easily done directly after development via optical

microscope (see Fig. 5.4). At this stage the patterns should be visible, as should the undercut. One

should check the dimensions against the design, and pay extra attention to the undercut making

sure there are no suspended regions.


-----


CHAPTER 5. DESIGN AND FABRICATION 126

######### 5.1.3 ######### Deposition and Liftoff

When making a metallic pattern, one must decide between an etching process and a liftoff process.

In the etching process, one deposits a film and then defines an etch mask to protect the parts that

are needed. This has the advantage that the film can be deposited under more ideal conditions,

without being contaminated by resist outgassing, and at high temperatures without fear of burning

the resist. Etching processes can be either dry, involving physical etching or reactive gasses, or

alternatively it can be wet, involving submersion in liquid etchants. Unfortunately, until recently we

did not have facilities to perform dry etching, and wet etching was found to be difficult to control,

so in this work we chose a lift-off process. In this type of deposition, the wafer is coated with resist

and patterned before the deposition. Areas of the resist which are removed expose the substrate,

and metal is deposited on the whole wafer. The resist is then dissolved, and only metal in direct

contact with the substrate is left, with the rest lifted off with the resist.

The ideal metal for this work would probably have been tantalum, with a T c above 4 K and

a single high quality oxide. Unfortunately, tantalum is only deposited well at high temperatures,

and so is not compatible with our lift-off process which uses polymer resists. The next best choice

would be niobium with T c 9 . 2 K, but it has many oxides with low temperature behavior varying


from insulator to superconductor. Niobium, like tantalum, is a refractory metal, and cannot be

thermally evaporated, but good film quality can be achieved by DC magnetron sputtering at room

temperature (see Table D for recipe and Fig. 5.2a for picture of sputtering machine).

Unfortunately, as shown in Fig. 5.5, sputtering is not a very directional deposition technique. It

is certainly possible to make resonators using sputtering and a liftoff technique, but the edge quality

is often quite poor. At the lowest temperatures (20 mK), it is still possible to get high quality factors

in the 10 5  10 6 range. However, the properties of these poor edges make it difficult to place the

qubit close to an edge, which hurts the coupling. Its behavior in the presence of a magnetic field is

also not well known and may affect the qubit.

For this reason, the most recent devices have been made with aluminum. The major disadvantage

of Al is its low critical temperature T c 1 . 2 K, meaning that it cannot be measured at 4 K in a


storage dewar or at 1 . 5 K in a pumped helium system. It does, however, have a low melting point,

making it suitable for thermal or electron-beam evaporation. These are very directional deposition

techniques, and they are well-suited to clean liftoff. For this reason, most of the original development


-----


CHAPTER 5. DESIGN AND FABRICATION 127

![SchusterThesis.pdf-129-0.png](SchusterThesis.pdf-129-0.png)

Figure 5.5: Pictures of sputtered Nb resonators showing the apron and flagging. a) A tilted
SEM image of a gap capacitor in a sputtered Nb resonator, showing the edge profile. Nb must be
sputtered because it is a refractory metal with melting temperature too high for clean thermal or
electron-beam evaporation. Notice that there are two distinct pathologies, a slow tapering of the
film thickness which extends for several hundred nanometers, referred to as the apron, and thin
films of metal which are partially detached from the substrate, called flags. b) A closer view
of the apron and flags. The apron occurs because sputtering is not very directional, so it spreads
underneath the undercut region of the resist, getting somewhat thinner but extending far beyond
the region defined by the top layer. c) Zoomed image of some flags, which are formed by parts of the
apron coating up the sidewall of the undercut layer. When the resist is dissolved the film remains
and is not well attached to the substrate. The superconductivity of these films is not well known
and could be a source of loss in Nb resonators. Further, these flags make it difficult to align a CPB
to close tolerance inside the resonator.

was done using niobium despite its rough edges. Once aluminum resonators were known to work

well and reliably, they became the preferred option, for their ease of deposition and liftoff.

It is often useful to be able to control the slope of the edge profile of a deposited film. Because the

aluminum deposition is so directional it is possible to use the shadow between the top and bottom

of the upper layer of resist to tailor the slope of the film edge (see Fig. 5.6 for description). This

technique has been used very successfully (see Fig. 5.7) and is a dramatic improvement over the

poor control (see Fig. 5.5) afforded by sputtered niobium.

######### 5.1.4 ######### Substrates

Three substrates were used throughout this work, sapphire, thermally oxidized silicon, and silicon

with only native oxide. All substrates were able to support high quality factor resonators. While

sapphire worked well for cavities, it has not been used yet for actual qubit experiments because it

is slightly more difficult to define the qubit pattern, because, as a good insulator, it is suscepti-

ble to charging. Some lithography tests were performed successfully but no devices were actually

measured cold. Undoped (or lightly doped) silicon has the convenient property for lithography that

it is somewhat (though weakly) conductive at room temperature, but an excellent insulator when


-----


CHAPTER 5. DESIGN AND FABRICATION 128

![SchusterThesis.pdf-130-0.png](SchusterThesis.pdf-130-0.png)

![SchusterThesis.pdf-130-1.png](SchusterThesis.pdf-130-1.png)

Figure 5.6: Diagram of rotating angle evaporation process. If one wants to place something inside
the gap of a resonator and make good contact with the ground planes or centerpin it is helpful to
have an angled sidewall. One way to do this is to tilt the substrate and rotate it rapidly as the metal
is being deposited. By adjusting the angle of tilt one can change the steepness of the sidewall from
shallow to nearly vertical.

![SchusterThesis.pdf-130-3.png](SchusterThesis.pdf-130-3.png)

![SchusterThesis.pdf-130-2.png](SchusterThesis.pdf-130-2.png)

Figure 5.7: Edge profiles of deposited Aluminum. a) An aluminum film with nearly vertical sidewalls.
Note that there is no apron nor flagging. b) An aluminum film with a slight slope to make it
easier to coat continuously with a film.


-----


CHAPTER 5. DESIGN AND FABRICATION 129

at cryogenic temperatures. Both thermally oxidized and bare silicon were measured with qubits.

Excellent results were achieved with both substrates, though there is some suspicion that the bare

silicon might leak at high gate voltages.

####### 5.2 ####### Cooper Pair Box

The CPB has three primary parameters, the Josephson energy, E J , the charging energy, E C , and

the coupling strength g , which is most closely related to the voltage division,  . It is possible to

realize nearly arbitrary combinations of these parameters, but in doing so one must navigate a host

of ancillary variables including, parasitic capacitances, critical current densities, proximity effect,

and many other less glamorous occurrences, which must be exploited and compensated for. This

section describes how to calculate and then realize these energy scales, and couplings.

######### 5.2.1 ######### Josephson Energy

In the traditional CPB, the atom transition frequency,  a E J /  , is set by the Josephson energy.


This energy is chosen to be much larger than the thermal energy scale k B T 20 mK, but not so


high that microwave engineering becomes a significant obstacle. Throughout this work, I aimed to

create CPBs with transition frequencies from  4  8 GHz, corresponding to thermal energy scales

of  200  400 mK. The Josephson junction is created by making a small overlap junction of two

pieces of aluminum separated by a thin barrier of thermally grown oxide. The Josephson energy

depends on the critical current, I c , which in turn depends on two parameters of the junction, its

area, A , and the thickness of the oxide barrier. The barrier is typically around 1 nm, only a few

atoms thick, and conduction can be dominated by imperfections which make the barrier locally

thinner. Therefore a more empirical measure, the critical current density, J c = I c /A , or sometimes

the resistance-area product RA is used. The critical current of a Josephson junction is related to

the junction resistance by the Ambegoakar-Baratoff relation



 
I c = tanh

![SchusterThesis.pdf-131-0.png](SchusterThesis.pdf-131-0.png)

2 eR


![SchusterThesis.pdf-131-1.png](SchusterThesis.pdf-131-1.png)

2 k B T


(5.2)


The important dependence is that the critical current is proportional to , which here refers to the

gap energy of the superconductor, and is inversely proportional to the resistance R . The resistance

is an exponentially-sensitive function of the effective barrier thickness, and proportional to the

area. Hence the RA product is a constant, measuring the effective barrier thickness. Luckily, the


-----


CHAPTER 5. DESIGN AND FABRICATION 130

thermal growth of aluminum oxide,is self-limiting and is relatively insensitive to the exact oxidation

conditions, allowing the RA product to be controlled. The critical current density is related to the

resistance area product by Eq. 5.2 as J c   / 2 eRA . Expressed in terms of the critical current,


the Josephson energy is





 I c
E J = (5.3)

![SchusterThesis.pdf-132-0.png](SchusterThesis.pdf-132-0.png)

2 e

For typical oxidation parameters in our evaporator (see Tab. D), the critical current density is

approximately J c 30 40 A/ cm 2 , but can change substantially for small junctions (see Table XX).
 

These correspond to a resistance area product RA  1  0 . 75 k. These are the two common metrics

for expressing junction transparency, and while the resistance area product is useful for basic testing,

our primary experiment measures E J , so I prefer to characterize devices in terms of their Josephson

energy density E J /A , which is typically around 150 200 GHz / m 2 . This last metric clearly states


that to get E J /h 5 GHz we must fabricate sub-micron ( 150 150 nm 2 ) junctions, a task beyond
  

standard optical patterning, but easily obtainable with electron beam lithography.

######### 5.2.2 ######### Charging Energy and Voltage Division

Both the charging energy, E C , and voltage division,  , are related to the capacitive network formed

by the two CPB reservoirs and resonator. The goal of this section, is to explain how one expresses

the complicated capacitive network in Fig. 5.8c as the simple effective network in Fig. 5.8d. In the

simplified circuit, the charging energy is E C = e 2 / 2 C  , and the voltage division is just   V g /V j =

C g /C  .

There are many pieces of metal, and while one is not likely to call the exact expressions beautiful,

using a little linear algebra, one can compute all of the island voltages and charges, analytically and

quite compactly. Let C ij be the capacitance between nodes i and j in Fig. 5.8c. One can then define

a capacitance matrix

C ji =  C ij (5.4)




C ii =




C ij

j =  i




This capacitance matrix has the property that

q  = C -   v (5.5)

where  q is a vector of island charges, and  v is a vector of island voltages. If all of the charges are

known, or all of the voltages are known, the capacitance matrix C allows one to easily find the other


-----


CHAPTER 5. DESIGN AND FABRICATION 131


![SchusterThesis.pdf-133-3.png](SchusterThesis.pdf-133-3.png)

![SchusterThesis.pdf-133-4.png](SchusterThesis.pdf-133-4.png)

![SchusterThesis.pdf-133-8.png](SchusterThesis.pdf-133-8.png)

![SchusterThesis.pdf-133-11.png](SchusterThesis.pdf-133-11.png)

![SchusterThesis.pdf-133-7.png](SchusterThesis.pdf-133-7.png)

![SchusterThesis.pdf-133-10.png](SchusterThesis.pdf-133-10.png)

![SchusterThesis.pdf-133-5.png](SchusterThesis.pdf-133-5.png)

![SchusterThesis.pdf-133-6.png](SchusterThesis.pdf-133-6.png)

![SchusterThesis.pdf-133-9.png](SchusterThesis.pdf-133-9.png)

![SchusterThesis.pdf-133-14.png](SchusterThesis.pdf-133-14.png)

![SchusterThesis.pdf-133-16.png](SchusterThesis.pdf-133-16.png)

![SchusterThesis.pdf-133-13.png](SchusterThesis.pdf-133-13.png)

![SchusterThesis.pdf-133-15.png](SchusterThesis.pdf-133-15.png)

![SchusterThesis.pdf-133-12.png](SchusterThesis.pdf-133-12.png)

![SchusterThesis.pdf-133-18.png](SchusterThesis.pdf-133-18.png)

![SchusterThesis.pdf-133-0.png](SchusterThesis.pdf-133-0.png)

![SchusterThesis.pdf-133-17.png](SchusterThesis.pdf-133-17.png)

![SchusterThesis.pdf-133-19.png](SchusterThesis.pdf-133-19.png)

C 34 C


 = C g /(C g +C j )


e 2
E c = 2(C j +C g )

E J


![SchusterThesis.pdf-133-1.png](SchusterThesis.pdf-133-1.png)

![SchusterThesis.pdf-133-2.png](SchusterThesis.pdf-133-2.png)

Figure 5.8: a) False colored SEM image of a CPB, blue is the aluminum CPB, beige is the niobium
resonator, and green is the silicon substrate. The CPB consists of two reservoirs joined by a pair of
tunnel junctions in a SQUID formation. There is some flagging of the resonator which shows up as
white. Because of the flagging, there is (intentionally) no DC contact between the lower reservoir
and the ground plane of the resonator as depicted in the model in part c . b) A color coded cartoon
model of the CPB inside of a resonator with each conductor labeled (does not include input and
output capacitors). c) Circuit diagram including capacitances between each pair of conductors. Also
shown is the location of relevant voltage sources, or places that the voltage should be measured.
Source V g can be thought of as photons or zero-point energy in the resonator, while V j can be
thought of as the voltage measured across the junction due to V g or as a voltage created by an
excess charge on the CPB island, depending on whether one is trying to find  or E C . d) Despite
the apparent complexity of the circuit diagram in c there are only two relevant parameters, which
can be represented by this simple CPB circuit.


-----


CHAPTER 5. DESIGN AND FABRICATION 132

quantity. Unfortunately for the box, there are typically mixed boundary conditions, with the charge

of the box specified, and voltage on the gate specified. One can phrase the problem of finding 

and E C in terms of solving this mixed boundary condition problem. From there, it is easy to find

a voltage between any two nodes, or the electrostatic energy XX cite Michel XX, given a voltage

or charge bias across the junction. Let us write Eq. 5.5 explicitly as a sum in terms of the voltage

biased nodes and charge biased nodes,


q  =


C  v  +
  I


C i v i (5.6)

i  S


where q  is the charge on island  , v i is the voltage on island i , and both of these are specified by

the boundary conditions. From this point forward we will use a convention that greek indices are

used for nodes in the set of islands (I), and roman indices are used for voltage source nodes (S). If

we knew all of the v  then we would know everything about the system, but unfortunately only the

charge of the island nodes is held fixed by the boundary conditions. Like any algebra problem one

should attempt to separate the knowns and unknowns. Equation 5.6 can be reexpressed as


q  +  q  =


C   v  (5.7)

  I


q   = 


C i v i
i  S


The result is just a simple linear matrix equation, where C  is just a reduced matrix containing only

island nodes C   = C  for ,   I. The solution to this equation is


v  =


C    1 ( q  +  q  ) (5.8)
  I


With this knowledge any electrostatic property of the system can be calculated. To calculate  =

V j /V 0 one imagines a voltage V 0 put between the resonator ground planes and center pin. Then one

calculates the voltage across the junction 1 , V j , with the charge boundary condition that the islands

start off neutral, that is q  = 0 for all island nodes. For calculating E C , one can imagine putting a

voltage across the junction and look at the resulting energy given by



1
E =



1  v T C  v = 1

2 -  2


2 C  V j 2 (5.9)


![SchusterThesis.pdf-134-0.png](SchusterThesis.pdf-134-0.png)

![SchusterThesis.pdf-134-1.png](SchusterThesis.pdf-134-1.png)

which is easy to calculate now that we know all of the voltages. Once an effective C  is known the

![SchusterThesis.pdf-134-2.png](SchusterThesis.pdf-134-2.png)

1 For electrostatic purposes the junction is just modeled as a capacitor. When calculating dynamics, one accounts
for tunneling by allowing the island charge to change by integer electrons.


-----


CHAPTER 5. DESIGN AND FABRICATION 133

charging energy is just E C = e 2 / 2 C  . Once  and E C are calculated, one can solve for an effective

C g and C  for the simplified CPB circuit.

This analysis can also be used to determine the DC gate voltage necessary to bias the CPB

to n g = 1. For a small input capacitor to the resonator, the effective gate capacitance, as seen

from outside the resonator, is reduced 1 by a factor C in /C r and of course there can be some direct

capacitance as well if the CPB is close to the gate 2 . For DC gating 3 it is also straightforward to

extend this to gating from both sides, which allows independent biasing of two qubits. Using this

approach one can control two qubits inside a resonator without adding dedicated gate lines.

######### 5.2.3 ######### Electron Beam Lithography

The desired junction size about 150  150 nm is too small to reliably use optical lithography, but it

is in an ideal range for electron beam lithography. Such feature sizes do not push the limits of our

scanning electron microscope (SEM), on which 50 nm features are regularly fabricated, and it is not

so large that substrate charging, or prohibitive write times are problematic. Like the optical process,

a bilayer resist system is used, but this time both layers are sensitive to electrons rather than UV

light. The top layer is made using PMMA A3 (955k weight) from Microchem , which forms a layer

approximately 120 nm thick. This sits on top of a copolymer MMA-MAA EL13 (Ethyl-lactate 13%),

which spins to about 550 nm. The bottom layer is more sensitive than the top, and so a natural

undercut of about  80 nm will occur when writing features. This natural undercut is enough to

get good liftoff with aluminum.

For making junctions one needs a three dimensional structure which overlaps two pieces of metal.

To do this we use a Dolan bridge technique (see Fig. 5.9) which creates a suspended bridge of resist,

used to cast a shadow in the deposited film. This technique is ideal because it allows one to make

small junctions, in a single step, which are self-aligned, and can be made without breaking vacuum

(necessary for high quality junctions). In order to expose PMMA, one needs to deposit approximately

 150  200  C / cm 2 of charge at 30 keV. The copolymer can be sensitized with just  60  C / cm 2

of exposure. By exploiting this difference in sensitivity, it is possible to expose only the underlayer

![SchusterThesis.pdf-135-0.png](SchusterThesis.pdf-135-0.png)

1 This reduction provides some intrinsic protection against DC gate noise.
2 When putting the CPB close to the gate, one must make sure that the direct coupling to the input lead does not
exceed the desired Purcell effect limited decay rate.
3 While it is possible to use this method to find the DC voltage division from the input to the junction, one cannot
apply this treatment which assumes that the circuit is made from lumped elements to RF drives. The best approach
for that is to use this technique to calculate the lumped element behavior near the qubit. Then the local resonator
voltage can be found taking into account the mode structure of the cavity. This drive can then be put into the lumped
element model.


-----


CHAPTER 5. DESIGN AND FABRICATION 134


a) Expose resist b)


Expose resist


c)


Aluminum is evaporated at angle


120 nm 120 nm
550 nm 550 nm


![SchusterThesis.pdf-136-0.png](SchusterThesis.pdf-136-0.png)

![SchusterThesis.pdf-136-1.png](SchusterThesis.pdf-136-1.png)

![SchusterThesis.pdf-136-2.png](SchusterThesis.pdf-136-2.png)

Aluminum is evaporated at 2 nd angle


d) Al + Al 2 O 3 e) Al Al f)


Al+Al 2 O e -

|Col1|Col2|Col3|e-|
|---|---|---|---|
|e-||||
|||||


![SchusterThesis.pdf-136-3.png](SchusterThesis.pdf-136-3.png)

![SchusterThesis.pdf-136-4.png](SchusterThesis.pdf-136-4.png)

Figure 5.9: a) A bilayer of resist is patterned. b) A suspended bridge of top layer material is left
after the exposed resist is dissolved in the development step. c) Next, aluminum is evaporated at
an angle. The bridge creates a shadow leaving a gap in the film. d) Then a small pressure of O 2
is let into the evaporation chamber and allowed to create a thin film of aluminum oxide, which will
act as the tunnel barrier. e) A second layer of aluminum is deposited at a different angle. In most
areas this results in a double layer of aluminum, but under the bridge the shadows create regions
where there is only a single layer. d) A side profile of the metal after the resist is lifted off. In order
for an electron to get from one side of where the bridge was to the other it must tunnel from the
top layer to the bottom layer.

without damaging the top layer 1 .

Using this technique, one can easily design small overlap junctions. There are a few things worth

mentioning, which can be observed in Fig. 5.10. In general, using this technique, all features are

doubled. A notable exception can be seen in Figs. 5.10 and 5.8a. A copy of the island would be

small enough that it might have resonances at similar frequencies to the box. By clever design the

image of the island is made to land on the sidewall of the resist, where it is lifted off. In order to

minimize errors due to imprecision of angles and or charging based misalignments, one can make

the junctions in a cross geometry 2 (see Fig. 5.10). This makes the area of the junction first order

insensitive to errors in the deposition angle, the rotation angle, and vertical or horizontal shifts. To

make sure that the top layer is able to continuously coat the island, the island is deposited to be

30 nm thick while the second layer is  100 nm thick. Additionally, the different thicknesses is used

as a form of superconducting gap energy engineering, which suppresses quasiparticle decoherence as

discussed in section 4.1.3. This gap engineering is thought to be the reason that parity improves at

![SchusterThesis.pdf-136-5.png](SchusterThesis.pdf-136-5.png)

1 While it takes  150  200  C / cm 2 to expose PMMA reliably, damage (holes/weak bridges) can set in as early
as 80  100  C / cm 2 . The exposure time for small undercut doses is often short enough that the limited bandwidth
of the deflecting coils can give significant variation in the exposure. One must be careful to not damage the top layer
too much.
2 There is some worry that this makes the tip of the junction susceptible to breaking off which might cause excess
charge noise.


-----


CHAPTER 5. DESIGN AND FABRICATION 135


![SchusterThesis.pdf-137-0.png](SchusterThesis.pdf-137-0.png)

![SchusterThesis.pdf-137-1.png](SchusterThesis.pdf-137-1.png)

![SchusterThesis.pdf-137-2.png](SchusterThesis.pdf-137-2.png)

![SchusterThesis.pdf-137-3.png](SchusterThesis.pdf-137-3.png)

Figure 5.10: SEM images of tunnel junctions. a) An image from sample CQED63 showing two
junctions. The shifted image is visible in the fingers. The island is  30 nm thick and the overlapping
fingers are  100 nm thick. b) A junction from a different sample (CQED97). Both images show a
thin film surrounding the metal features known as the veil of death which is a film of unknown
composition (thought to be oxidized aluminum). This seems to show the region of resist that was
undercut during the development process.

increased (but still small) magnetic fields (see Fig. 7.11).

######### 5.2.4 ######### Veil of Death

During the evaporation process we have observed a mysterious thin film around the defined features,

colloquially known as the veil of death because we fear that it may be hurting the coherence times

of our qubits (see Fig. 5.10). This film is thought to be composed of aluminum scattered by residual

pressure due to outgassing of the resist. It is also possible that it is some sort of organic residue from

the development process. Because it appears to be extremely thin (  1 nm) and has not completely

destroyed the qubit it is thought that if the film was aluminum that it is fully oxidized. However,

the loss tangent of this dielectric which is very close to the qubit could be particularly pathological.

Ideas to eliminate this film in future samples include, using an inorganic mask, etching the film away

after the fact (briefly exposing chip to acid or base), or using an all optical process (which does not

seem to have this residue). Losses from this mechanism should scale with the ratio of capacitance

inside and outside of the junction itself and studies measuring this dependence could a provide a

window into decay due to this film.


-----


CHAPTER 5. DESIGN AND FABRICATION 136

![SchusterThesis.pdf-138-2.png](SchusterThesis.pdf-138-2.png)

Figure 5.11: a) An FEI XL30 Sirion scanning electron microscope. It is capable of 4 nm viewing
resolution, and has been modified with the Nanometer Pattern Generation System NPGS to allow
it to act as electron beam lithography tool. It has successfully been used to write features as small as
40 nm, well beyond the requirements of this project. b) A custom made (by Plassys ) electron beam
evaporator. It is capable of depositing aluminum, gold, copper, titanium, chrome, and alumina. It
features a stage which can be rotated about two axes to allow multi-angle depositions. This feature
is used to create the overlap junctions and to control the edge profile of aluminum resonators. It is
a load locked system which can pump down to  1  10  7 .


![SchusterThesis.pdf-138-0.png](SchusterThesis.pdf-138-0.png)

![SchusterThesis.pdf-138-4.png](SchusterThesis.pdf-138-4.png)

![SchusterThesis.pdf-138-1.png](SchusterThesis.pdf-138-1.png)

![SchusterThesis.pdf-138-3.png](SchusterThesis.pdf-138-3.png)

Figure 5.12: a) Optical image of transmon inside of a resonator. Visible are the two reservoirs
which have interdigitated fingers to help increase the shunt capacitance, and lower the vacuum Rabi
coupling, g . There is also a capacitance between the top island and the center-pin, and the bottom
island and the ground plane, as well as other stray capacitances. The actual junctions and SQUID
loop are indicated with a blue box. b) Zoomed in image with a scanning electron microscope which
shows the Josephson tunnel junctions and the loop. The junctions are approximately 150 and the loop is approximately 4  m 2 .  150 nm 2


-----


CHAPTER 5. DESIGN AND FABRICATION 137

####### 5.3 ####### Transmon

The transmon design is really identical to the traditional CPB design. The only major difference is

the parameters which one tries to realize. In the traditional CPB, the natural junction capacitance

C  C j 4 fF is sufficient to provide the desired charging energy E C 5 GHz. However, for the
  

transmon one would like to have C  75 fF for a charging energy E C 250 MHz. In terms of
 

fabricating capacitors, nothing fundamental changes, bigger pieces of metal give larger capacitances.

A primary consideration is making sure that as one increases C  , that the vacuum Rabi coupling

g , controlled by way of  , does not become to large. If one wanted to maximize the vacuum Rabi

coupling, one could push  towards unity by adding all of the capacitance in between the reservoirs

and the resonator. That would increase C g until C g  C  and   1. However, if one were to

do that they would actually get too much vacuum Rabi coupling! In circuit QED it is possible

to get enough coupling that one begins to violate the rotating wave approximation 1 . While one

could possibly still operate in such a regime, at this early stage of exploration we choose to be more

conservative. Thus, we need a way of lowering  . This can be easily done by lowering the effective

C j . One could make the junction area larger but that would change the Josephson energy. Rather

we add an interdigitated capacitor which shunts away much of the coupling gained by having larger

effective gate capacitance. By interdigitating the shunting capacitor and not the gate capacitors

we can keep  < 0 . 2, which is relatively safe from a rotating wave standpoint. When looking

at Fig. 5.12 it is tempting to think that the interdigitating capacitance, the most prominent new

feature, is responsible for increased g compared to the traditional CPB. In fact the opposite is the

case, and the interdigitation is added specifically to shunt the gate capacitor lowering g.

####### 5.4 ####### Printed Circuit Boards and Sample Holders

The primary design consideration for the printed circuit board (PCB), see Figs. 5.14 and 5.15, and

the sample holder (see Fig. 5.13) is the suppression of parasitic resonances. The circuit boards launch

from SMP to coplanar waveguide via a right angle surface mount SMP connector from Rosenberger .

These are specified up to 40 GHz and have good performance up to about 20 GHz. In order to

suppress parasitic modes between the ground planes between the top and bottom of the circuit

board, the top ground planes are periodically connected to the bottom using copper vias spaced by

![SchusterThesis.pdf-139-0.png](SchusterThesis.pdf-139-0.png)

1 Due to a common way of writing the vacuum Rabi coupling  C g E C , we were initially worried that by lowering
E C we would lose g . However, of course since E C can be lowered by making C g large this is not an issue.


-----


CHAPTER 5. DESIGN AND FABRICATION 138

![SchusterThesis.pdf-140-0.png](SchusterThesis.pdf-140-0.png)

![SchusterThesis.pdf-140-1.png](SchusterThesis.pdf-140-1.png)

Figure 5.13: a) Coffin style sample mount with penny for size comparison. The PCB connects to
semirigid coaxial cables via SMP surfacemount connectors and a compliant bullet. An inner lip
is used to press the PCB against its backing for good ground contact. b) A next generation sample
mount and PCB. This sample holder accepts eight incoming RF lines, and is sometimes called the
octobox or more flavorfully the arachnipus. Using different PCB designs shown in Fig. 5.15
one can either measure two devices simultaneously or use all eight connections to measure a single
device, allowing for flux bias lines or multiple cavities on a single chip. This sample holder is also
designed to fit in the vacuum line of site port of the cryostat, allowing the possibility of transferring
the sample to the cold stage without cycling the cryostat to increase sample throughput.

40 mil, which should provide protection to any modes until well above 100 GHz.

However, while the circuit boards are well protected, there can still be impedance mismatches

when coupling to the chip, creating opportunities for parasitic resonances. One way that there can

be a mode mismatch is due to differences in the dielectric constant between the chip and PCB

substrate. This was minimized by using Arlon , a low loss, high dielectric (XX), teflon and ceramic

based microwave substrate. One must also connect the on-chip CPW to the circuit board CPW, via

wirebonds. The inductance of these wirebonds is approximately proportional to the length of the

wire bond with about (1 nH/mm). In order to minimize this length, and also match the on-chip

and circuit board modes as closely as possible, the circuit board has a recess (see Fig. 5.13), making

the chip flush with the top of the circuit board. The circuit board is connected to the chip via as

many wirebonds as can easily fit around the edges of the chip, to lower the inductance as much as

possible.

Even if all of these measures could be implemented perfectly, one would still have to contend

with parasitic resonances of the chip itself. Unfortunately, we do not possess the equipment to make

vias in the silicon substrate, and suppress such modes, as was done with the printed circuit boards.

To minimize this effect, we made the chip itself small to raise the minimum cutoff frequency of such

a mode.


-----


CHAPTER 5. DESIGN AND FABRICATION 139

SMP Connector Pad 3x10 mm 2 chip cutout vias

![SchusterThesis.pdf-141-0.png](SchusterThesis.pdf-141-0.png)

2.25

Figure 5.14: Coffin style printed circuit board. Visible on the circuit board are mounting pads
for the SMP surface mount connectors. There is also a 3  10 mm 2 cutout for the chip, which is
milled out by the PCB manufacturer, such that the chip will be flush with the top surface. Initial
versions were 25 mil thick and milled only 12 mil deep, but more recent versions are only 15 mil
thick and milled down to the ground plane.

In the end the sample holders both perform nearly perfectly up to 9 GHz with reasonable per-

formance but some parasitic resonances up to about 20 GHz.


-----


CHAPTER 5. DESIGN AND FABRICATION 140

4 SMP connectors 8 SMP connectors


Connectors
can be rotated

2x7 mm 2
chip cutout


![SchusterThesis.pdf-142-0.png](SchusterThesis.pdf-142-0.png)

1.18


2 chips


![SchusterThesis.pdf-142-1.png](SchusterThesis.pdf-142-1.png)

Figure 5.15: The next generation octobox PCB is substantially more versatile than the initial
design. Most importantly it provides more RF lines which can be tasked for a variety of purposes.
These designs use thinner boards (15 mil) and narrower traces (3 mil). Allowing more chips and
CPWs to fit in a smaller package than the Coffin style shown in Fig. 5.14 a) This version allows one
to measure two devices simulataneously, and is primarily used to speed up resonator characterization.
b) This design can use all eight connections for interacting with a single chip. The extra lines
enable future experiments with multiple cavities, independent dedicated gate and flux biasing, and
additional dedicated qubit readouts. Note that the rotational degree of freedom given by the bullet
connectors is used to place the surface mount connectors at different angles than in a .


-----


### Chapter 6

## Measurement Setup

This section is intended to be a brief discussion of the cryogenic, microwave, and digital signal

processing techniques used to interrogate the circuit QED system. First, a rough outline of the

measurement setup will be given. Next, the cryogenic design and filtering will be discussed. Then,

back at room temperature, the qubit is controlled by a variety of RF and low frequency gate pulses.

Finally, the demodulation hardware and software will be discussed, and in particular the digital

homodyne technique will be explained.

The system state will be probed by monitoring microwave transmission through the resonator

as described in section 3.4. In principle one can probe the resonator (qubit) properties either in

reflection or transmission, but for all experiments in this work transmission was used. Transmission

is beneficial because the signal does not sit on a large background of reflected measurement/control

pulses 1 . The measurement setup diagram is shown in figure 6.1. Microwave control and measurement

pulses are generated at room temperature and fed through semirigid coaxial cable to the sample.

The bias charge n g is set via a DC voltage at room temperature, combined at low temperature with

the RF signals, and applied on the input of the resonator. Unfortunately, these same coaxial cables

that transmit desired signals can also carry thermal noise to the sample. Several layers of filters are

employed to reduce the room temperature fluctuations down to acceptable levels at the sample.

The signals transmitted are quite small, with the resonator only having on average a few photons,

corresponding to a power P = n   r  10  17 W. In order to measure this faint signal, many stages


of amplification are employed. The signal is then mixed down to a low frequency which can then be

digitally sampled and processed by a computer.

![SchusterThesis.pdf-143-0.png](SchusterThesis.pdf-143-0.png)

1 While careful microwave design can be used to cancel these reflected pulses, such interference techniques, place
a heavy burden on the microwave calibration and can limit the bandwidth of applied pulses. Dispersion in the line
could make particularly annoying pulse length dependent effects.

141


-----


CHAPTER 6. MEASUREMENT SETUP 142

|Bias T Cin Cout 20 mK Cg coax coax resonator CPB copper 30 dB powder filter|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
||||||||circulator 100 mK|
|30 dB||||||copper powder filter|RF amp TN = 5 K 4 K|
|RF amp mixer TN = 75 K   V dc gate RF RF s p  LO V g LO mixer IF amp RT||||||||



Figure 6.1: Measurement setup for cQED experiments. The control and measurement pulses, as
well as any DC gate sweeps are synthesized at room temperature. Pulses are then sent down an RF
pathway which attenuates the signal at 4 K and then again at 20 mK to eliminate thermal Johnson
noise from room temperature and warmer parts of the cryostat. The DC gate signals are low pass
filtered to about 1 GHz using Copper powder filters and then joined with the RF using a bias-tee.
After interacting with the sample, the transmitted signal passes through a circulator which diverts
noise from the cold amplifier. The signal is then amplified by a low noise temperature HEMT
T N 5 K, and sent to room temperature where it is further amplified. Finally the signal is mixed

down to low frequencies using an IQ mixer, where it is digitally acquired and post-processed by a
computer using LabView software.


-----


CHAPTER 6. MEASUREMENT SETUP 143

####### 6.1 ####### Cryogenics and Filtering

These experiments were performed using a Kelvinox 400  W dilution cryostat capable of reaching

a base temperature of  6 mK and the sample is measured at  15  20 mK. Principles of cryostat

design and operation can be found in [Pobell2006]. The primary cryogenic design concern is to

minimize the amount of heat and noise that reach the sample from thermal or terrestrial microwave

sources. There are three types of pathways, the RF input, the DC lines, and the RF output, each

of which requires a different style of filtering.

The RF drive on the sample requires only nanowatts of power, but operates at the qubit frequency

of  5 GHz. At all temperatures above 100 mK thermal Johnson noise will be significant at these

frequencies. Since the signal and noise are in the same band and we require a large bandwidth,

the easiest way to filter is to attenuate. If the effective temperature of interest is much less than

the thermal temperature then the voltage noise is just linear in temperature S V (  ) 4 k B T R . In


order to kill noise from a high temperature at a lower temperature, one can just attenuate, at

the cold stage, by a factor,  = T hot /T cold . For going from room temperature (290 K) to liquid

helium temperature (4 K), a 23 dB of attenuation is used. To go from 4 K to 20 mK another 30 dB

of attenuation was used. The cables provide an additional  10 dB of attenuation, for a total of

 63 dB. With so much attenuation one must worry about not having enough power to perform

fast pulses, and heating the attenuators at the cold stage. Measurement requires only a few photons

per cavity lifetime  110 dBm, and 1 ns control pulses typically take a few thousand photons

 80 dBm, neither of which heats the fridge or provides a challenge at room temperature. Off

resonant pulses or multiphoton processes which require substantially larger powers, can noticeably

raise the base temperature of the fridge if the duty cycle isnt small enough. Overall this hasnt

been a substantial limitation thus far.

The DC lines have very different requirements. They do not require high bandwidth like the RF

pulses, but they employ much higher voltages. For example, the sample studied in [Wallraff2004],

one electron of gate charge corresponded to about 1 V. If one tried to use a line with 65 dB of

attenuation, one would require a megavolt at room temperature! Since only a small bandwidth is

needed, we can use a low pass filter which has no attenuation at DC, but very large attenuation at

RF frequencies where most of the thermal noise power is located. There are many different flavors

of low pass filter available but for this experiment, copper and stainless steel powder filters (see


-----


CHAPTER 6. MEASUREMENT SETUP 144

|4 K|1K pump Attenuators Cold Amp|Heat Exchanger Mixing Chamber Cu powder filter Attenuators Bias Tee Sample Holders|
|---|---|---|
|1 K|||
||Still SS powder filters Circulators||
|100 mK|||
|20 mK|||


![SchusterThesis.pdf-146-2.png](SchusterThesis.pdf-146-2.png)

![SchusterThesis.pdf-146-9.png](SchusterThesis.pdf-146-9.png)

![SchusterThesis.pdf-146-7.png](SchusterThesis.pdf-146-7.png)

![SchusterThesis.pdf-146-15.png](SchusterThesis.pdf-146-15.png)

![SchusterThesis.pdf-146-3.png](SchusterThesis.pdf-146-3.png)

![SchusterThesis.pdf-146-10.png](SchusterThesis.pdf-146-10.png)

![SchusterThesis.pdf-146-14.png](SchusterThesis.pdf-146-14.png)

![SchusterThesis.pdf-146-6.png](SchusterThesis.pdf-146-6.png)

![SchusterThesis.pdf-146-11.png](SchusterThesis.pdf-146-11.png)

![SchusterThesis.pdf-146-8.png](SchusterThesis.pdf-146-8.png)

![SchusterThesis.pdf-146-4.png](SchusterThesis.pdf-146-4.png)

![SchusterThesis.pdf-146-13.png](SchusterThesis.pdf-146-13.png)

![SchusterThesis.pdf-146-12.png](SchusterThesis.pdf-146-12.png)

![SchusterThesis.pdf-146-0.png](SchusterThesis.pdf-146-0.png)

![SchusterThesis.pdf-146-5.png](SchusterThesis.pdf-146-5.png)

![SchusterThesis.pdf-146-1.png](SchusterThesis.pdf-146-1.png)

Figure 6.2: Annotated images of the cryostat (left), color coded by temperature. Everything shown
in the larger images is inside the vacuum can. The 1 K pot is visible in orange section, which has the
cold amplifier as well as thermalizing attenuators and copper powder filters. The 100 mK section
has the still, which recovers the 3He from the mix. In early experiments the circulators were also at
100 mK though they have since been moved to the cold stage. There is also another stage of copper
powder filtering. The cold stage is cooled by the mixing chamber and holds two samples. There
is a final layer of filtering and attenuation, as well as the bias tees which combine the DC and RF
signals. Note that the cryostat has a very large cross-sectional area which allows for the bulky RF
components to be placed inside.


-----


CHAPTER 6. MEASUREMENT SETUP 145

Fig. 6.2) were chosen, because they attenuate strongly ( > 80 dB) and have no resonances at high

frequencies (often a problem with lumped element filters). They consist of a long wire traveling

through an epoxy/partially oxidized metal powder mixture, which is a good insulator at DC but

very lossy at RF. One filter is placed at each temperature stage. Both copper and stainless steel

powder filters work well, but it is feared that stainless may not thermalize at the lowest temperatures

so it is generally used only at 100 mK and above. These filters begin to cutoff around 30 MHz but

the DC port of the bias tee, used to join the RF and DC signal at the base temperature, actually

cuts off at  5 MHz, limiting the performance of the DC gate. That could be a limitation for trying

to sweep the CPB through the resonator quickly using the gate voltage. That method is not ideal

as the it would require leaving the sweet spot ( n g = 1) which would degrade performance. It would

have been easy and probably would have worked if we had had  100 MHz of bandwidth on those

lines.

Finally, the signal must get to the amplifier which is at the 1 K stage. Here there is a delicate

balance. While one needs to avoid noise from above, attenuation reduces the signal, and thus the

signal-to-noise ratio. Ideally, this would be accomplished by a one-way microwave valve which lets

the signal through without attenuation, but lets none of the noise back through. Amazingly, a

circulator does exactly this, using a ferrite component to break time reversal symmetry. Circulators

typically provide about 20 dB of isolation and have a bandwidth up to one octave ( Pamtech 4  8 GHz

in our setup). We use two of them in series to increase the isolation (see Fig. 6.2). Circulators often

have resonances outside of their specified operating band. This can be obviated to some extent by

using a bandpass filter to protect the sample, which was not done in this case, but probably should

have been.

At low temperatures, thermal conductivity, especially due to phonons is substantially reduced.

This is good, because it lowers the heat load on the cold stages, but also means that care must be

taken to ensure that cables and components are properly heat sunk. The filtering elements actually

serve an additional purpose of providing thermal anchoring of the cable (especially the center pin)

to the cryostat. Attenuators provide a resistive connection through which heat can be dissipated

from the center pin to cable shield (and cryostat). The copper powder filters also allow the center

pin to come to thermal equilibrium, as there is only a very thin layer of oxide on the metal grains.

The circulators are typically used as an isolator with the third port terminated with a 50 resistor

to ground, which can be anchored to the base temperature (though in early experiments it was


-----


CHAPTER 6. MEASUREMENT SETUP 146

actually at 100 mK). Semi-rigid coax with both the center pin and shield made out of stainless steel

(UT85 SS-SS) was used to provide isolation between temperature stages. Unfortunately, in addition

to its high thermal resistance, it is also quite lossy electrically, attenuating signal as well as noise.

While this is not terribly important on the input side where there is already a lot of attenuation,

the short section of stainless cable between the output of the sample and the input of the amplifier

have around 3 dB of attenuation raising the system noise temperature substantially. It is possible to

use superconducting coax to have good thermal isolation while retaining high electrical conductivity,

but it is somewhat difficult to make the cables and it was not done for this experiment.

####### 6.2 ####### Pulse Synthesis

All of the fast control and measurement of the qubit is performed using RF pulses. These envelopes

of the pulses are generated by a Tektronix 520 arbitrary waveform generator (AWG) capable of

generating pulses with 1 ns resolution. This AWG can hold waveforms of up to 4 million points

per channel, with two analog channels, and 4 digital markers, and the second channel can also be

used as 10 digital channels, all at the full speed. The analog channels are used for pulsing and the

digital markers are used to trigger gate sweeps, and RF generators. Pulse sequences are designed

in Mathematica and loaded into the AWG memory. Two types of pulses are used. Square pulses

are simple to design and easy to time relative to one another, but in frequency space, they have

frequency components in a wide band, which can create crosstalk between the qubit and resonator.

One can also define gaussian pulses which use the minimum bandwidth. These pulse envelopes are

then upconverted to the qubit or resonator frequency by mixing them with an RF tone generated by

an Agilent 20 GHz continuous wave source. Various models of generator are used, depending on the

model, the mixer can be internal or external and either vector (IQ) or scalar. Initial experiments,

used two external mixers in series (model ZMX-8GH from minicircuits ) to make a pulse with enough

contrast. A high degree of contrast is necessary in order to make fast pulses when the mixer is open,

but not create any excited state population when the mixer is closed. With the external mixer

it was difficult to get good linearity while maintaining good contrast with these mixers. Using the

internal IQ mixer of a newer vector microwave source, it is possible to get very linear response

without sacrificing contrast. The vector capability also allows one to synthesize the pulses necessary

to perform tomography. In both cases, it is difficult to prevent leakage below about 30 dB, so the

internal switch of the source (which has  80 dB of contrast) was used as a backup in both cases. The


-----


CHAPTER 6. MEASUREMENT SETUP 147

pulse is essentially stopped by turning off the mixer, and having the backup prevents any residual

population from building up while the experiment is resetting.

####### 6.3 ####### Demodulation

The state of the qubit is encoded in the phase (and amplitude) of a pulse transmitted at  5 GHz. To

extract this information two stages of demodulation are required. The eventual goal is to acquire the

phase and amplitude information digitally on a computer, but unfortunately no acquisition boards

can stably acquire at 5 GHz. In order to slow the the signal down to below 1 GHz, where it can

be sampled, the signal once amplified cold and at room temperature, must be mixed down to an

intermediate frequency (IF) by an IQ demodulator. The two quadratures of this IF signal can be

mixed down to anywhere from DC-500 MHz, and are then amplified by either a mini-circuits model

ZFL-500LN RF amplifier, or a SRS 350 MHz preamplifier, before being acquired by an Acqiris data

acquisition board.

The acquisition board has two channels so that it can acquire both quadratures simultaneously

at 1GS / s. Because this experiment primarily measures phase, frequency synchronization between

all components of the utmost importance. An SRS 10 MHz rubidium frequency standard is used

to provide a reference frequency to all RF sources, arbitrary waveform generators, and the data

acquisition card which can take an external clock source. If the internal clock rather than the fre-

quency standard is used, a noticeable phase drift will occur during long acquisitions. This particular

board also has an onboard FPGA hard-coded to average the signals in real time. This feature is

useful because of the quantity of data which is taken. At the full acquisition rate of the board, the

large amount of data, which is transferred into memory takes almost one hundred times longer than

actually acquiring the data. This means that one is only doing useful experiments for 1% of the

time. If one is performing single shot measurements, where every trace must be stored separately,

this poor duty cycle is unavoidable. For any measurement which studies ensembles that can be

averaged, this board will allow up to 65,000 averages to be taken without having to transfer the

buffer to memory. If more than  1 , 000 averages are taken the transfer time becomes negligible

compared to the acquisition time.

At very high amounts of averaging, one begins to notice that there is correlated noise on the

card, which arises from cross-talk between the digital components and analog-to-digital converter.

This card noise is noticeable on timescales less than 20 ns and averages around 65 , 000. It can be


-----


CHAPTER 6. MEASUREMENT SETUP 148

measured and digitally subtracted, to reduce its magnitude significantly but not completely. For

slow phenomena, I suggest filtering it out, and for fast things it helps to subtract it off, but it will

always be present to some extent.

Once the data is acquired, the phase and amplitude information must be extracted. If the signal

is mixed down to DC in hardware, it can simply be averaged and decimated, and then converted

from I and Q to phase and amplitude. If there is a finite IF frequency, the I and Q must first be

extracted, in a process I call digital homodyne.

######### 6.3.1 ######### Digital Homodyne

There are two flavors of digital homodyne, which can either use a single or both quadratures to

extract the phase and amplitude. The first method, which uses a single channel, does not require

an IQ mixer and is very robust to imperfections and offsets in the mixer or amplifier chain, but

its bandwidth is limited to the IF frequency. The second method, which uses both quadratures,

allows one to have more bandwidth than the IF frequency! However, it is much more sensitive to

any imbalance between the arms of the mixer and IF amplification chain. The following subsections

will explain these two methods, describing the effect of various imperfections and how one can

compensate.

Definition of problem

There is a signal of the form

S ( t ) = A ( t ) sin( t +  ( t )) (6.1)

The goal is to extract A ( t ) and  ( t ).

IQ Mixer

An IQ mixer has two inputs. One is used for the signal and the other is typically driven with a local

oscillator (LO). The LO signal LO = B sin((  +  if ) t ) is split and one branch is phase shifted by

/ 2. The signal is split and multiplied with each branch of the LO. The resulting signals are then

low-passed by a filter with a cutoff at IF max . For our Miteq IQ-mixer IF max 500MHz. After low


passing each branch has the form

I IF ( t ) = A ( t ) cos(  if t +  ( t )) (6.2)


-----


CHAPTER 6. MEASUREMENT SETUP 149

Q IF ( t ) = ( A ( t ) +  A ) sin(  if t +  ( t ) +   ) (6.3)

The amplitude and phase of the original signal have been mapped onto two lower frequency

signals, the  s represent small imbalances between the two arms of the mixer. If  if = 0 and only a

single quadrature is mixed down, then the measurement is called homodyne, whereas if  if = 0 then


it is called heterodyne. Both techniques are mathematically equivalent 1 , however the homodyne

signal is at DC, making it easy to work with, but also susceptible to 1 /f noise and drifts. The

original signal can be reconstructed from either of these two signals alone and will be correct within

a bandwidth of  if around the original signal. Imagine finding A ( t ) from one arm alone, say I . At

the point where the signal is maximum, one has very good sensitivity. However, at the zero crossing

where one is sensitive to the phase, one has absolutely no information about A ( t ). Therefore, with

a single channel, it is impossible to know both the phase and amplitude precisely at the same time.

While it is not possible to measure both quantities instantaneously, one can recover the average

of both quantities during a complete IF period. This single channel technique will be discussed in

detail in the next section. Using two channels separated by  = / 2, whenever I is maximum, Q is

at a zero-crossing. These two channels simultaneously determine A ( t ) and  ( t ) at every point. In

the third section I will discuss how to extract this information, and discuss how imbalances manifest

themselves and how they can be compensated for.

Single Channel Digital Homodyne

In this method a single channel IF signal of the form

IF ( t ) = A ( t ) cos(  if t +  ( t )) (6.4)

is digitally mixed down to DC in an IQ fashion. The low pass is accomplished by integrating over

exactly one period of the IF frequency to extract two signals.


t +2 / if

t



t +2 / if

t




I ( t ) =

Q ( t ) =


![SchusterThesis.pdf-151-0.png](SchusterThesis.pdf-151-0.png)

2 / if

1

![SchusterThesis.pdf-151-1.png](SchusterThesis.pdf-151-1.png)

2 / if


cos(  if  ) IF (  ) d  (6.5)


sin(  if  ) IF (  ) d  (6.6)



and


This yields

![SchusterThesis.pdf-151-4.png](SchusterThesis.pdf-151-4.png)

![SchusterThesis.pdf-151-2.png](SchusterThesis.pdf-151-2.png)

![SchusterThesis.pdf-151-3.png](SchusterThesis.pdf-151-3.png)

I ( t ) = A ( t ) cos(  ( t )) (6.7)

![SchusterThesis.pdf-151-5.png](SchusterThesis.pdf-151-5.png)

1 Homodyne and (IQ) heterodyne are equivalent methods for any classical signal. In quantum mechanics the extra
port introduced when splitting the signal, results in a minimum addition of  / 2 of extra noise.


-----


CHAPTER 6. MEASUREMENT SETUP 150

![SchusterThesis.pdf-152-2.png](SchusterThesis.pdf-152-2.png)

![SchusterThesis.pdf-152-0.png](SchusterThesis.pdf-152-0.png)

![SchusterThesis.pdf-152-1.png](SchusterThesis.pdf-152-1.png)

Q ( t ) = A ( t ) sin(  ( t )) (6.8)

Where the bar represents the average value in a window size T IF = 2 / if . This is equivalent to

knowing the amplitude and phase which are just

A ( t ) = ( I ( t ) 2 + Q ( t ) 2 ) 1 / 2 (6.9)

![SchusterThesis.pdf-152-3.png](SchusterThesis.pdf-152-3.png)

![SchusterThesis.pdf-152-4.png](SchusterThesis.pdf-152-4.png)

![SchusterThesis.pdf-152-5.png](SchusterThesis.pdf-152-5.png)

and

![SchusterThesis.pdf-152-6.png](SchusterThesis.pdf-152-6.png)

![SchusterThesis.pdf-152-7.png](SchusterThesis.pdf-152-7.png)

![SchusterThesis.pdf-152-8.png](SchusterThesis.pdf-152-8.png)

 ( t ) = arctan( Q ( t ) /I ( t )) (6.10)

Since in practice the data is in discrete timesteps, the integrals become sums. This method has many

advantages. With a single input channel, one can extract both the amplitude and phase information.

Because there is a single IF channel, there is no error due to any imbalances between arms of the IQ

mixer (which is effectively just a regular mixer in this mode). However, the bandwidth is reduced

from IF max to  if . If we would like to get the full bandwidth out of the mixer we will need to use

both arms.

Dual Channel Digital Homodyne

In the previous section, we used a digital technique which was very analogous to how a real IQ mixer

works. It multiplied the desired signal by two LOs that were / 2 apart and then low-passed (by

integrating). If you have only one channel, you cant really do much better. With both channels

however, one should be able to extract the information from each IQ point, rather than requiring a

whole IF period. Even if one channel is only sensitive to the amplitude, the other will measure the

phase, so at each point we are sensitive to all of the information. To think about extracting I and Q,

imagine plotting them in cartesian coordinates, where x = I IF (t) and y = Q IF (t). If there were no

imbalances, this would just trace out a circle with an angular frequency  if . What we would like to

do, is go to a rotating frame where the IF frequency is stationary. This is accomplished by applying

a transformation which rotates the IQ coordinates at  if .


R ( t ) = cos(  if t ) sin(  if t )
sin(  if t ) cos(  if t



(6.11)


If there are no imbalances then when R ( t ) is applied to ( I IF ( t ) , Q IF ( t )), one gets.

I ( t ) = A ( t ) cos(  ( t )) (6.12)

Q ( t ) = A ( t ) sin(  ( t )) (6.13)


-----


CHAPTER 6. MEASUREMENT SETUP 151

but now there is no averaging. The transformation can be applied point-by-point making it more

efficient and having the maximal time resolution allowed by the acquisition and the bandwidth of

the mixer.

Unfortunately, because there are now two arms, there can be slight imbalances between them.

This transformation preserves all of the signal but also acts on these imbalances. If they are constant

as suggested by the form given in Eqs. 6.5 and 6.6 then they can be compensated for relatively easily.

The first step is to measure all of the  s. This can be done for a large data set or for every

period separately. In order to correct for amplitude imbalances one simply rescales the data which

in matrix form looks as.


E A = (1 +  0 a 1 )  1 (1 +  0 a 2 )  1



(6.14)


The phase correction matrix R  is a little more complicated. One could obtain the transformation

by some educated guess and check, however, a more formal method solves the problem based on the

following criteria:

1. The transformation must work ( I IF ( t ) , Q IF ( t ))  ( I ( t ) , Q ( t )).

2. Because it is a rotation it must be unitary det( R  ) = 1.

3. It must be antisymmetric.

This gives four constraints which define the 4 matrix coefficients. The equations can then be solved


to yield,


cos t +   sin t
sin t +   cos t



R  =


![SchusterThesis.pdf-153-0.png](SchusterThesis.pdf-153-0.png)

cos 


(6.15)


Essentially, the transformation just rotates one of the quadratures a little extra to make up the

phase offset. This transformation works well for small   , but near   / 2 the prefactor blows


up and the matrix maps both quadratures to the same value. This effect describes the transition

between having two orthogonal IQ ports and the behavior of a single channel mixer. As one might

expect, if the phase of the two quadratures is the same, the second channel provides no additional

information.

The error corrected R  = R  E A , ( I IF ( t ) , Q IF ( t )) perfectly reproduces a digital version of the DC

IQ homodyne signal. After this the resulting signals can be averaged, filtered, and decimated as

desired.


-----


CHAPTER 6. MEASUREMENT SETUP 152

Advantages of the Digital IQ method

The main advantage of the digital IQ over single channel version, centers on the fact that it is a

point-by-point method, where all information (at the sample time) about the amplitude and phase

are known (quantum limit not withstanding 1 ). The method can have higher bandwidth for a given

IF frequency. The BW limiting factor for the IQ method is the maximum IF bandwidth of the mixer,

whereas for the single channel it is the IF frequency . So with the IQ one can work at an IF just

high enough to avoid 1 /f noise. In the single channel one has to make the IF frequency as high as

possible and can run into limits of the data acquisition card (in order to oversample the IF) .

Digital IQ Pitfalls

Unfortunately, there are some issues with the DIQ measurement technique. Because it is a point-

by-point method it can be very sensitive to certain types of noise. Any kind of DC voltage noise

is mixed up to the IF frequency. Further any noise or signals at the harmonics or negative

fundamental frequency will not be suppressed. These can come from non-idealities in the mixer,

acquisition card or other sources. At the time of this writing some remaining sources of noise exist.

Since these seem to be at the fundamental and its harmonics, they can be easily filtered out by

averaging over an integral number of IF periods. However, this essentially eliminates the advantages

of the IQ over the single channel.

Digital Homodyne Summary

The digital homodyne techniques allow one to use RF amplifiers which are stable with high band-

width, rather than DC amplifiers which are susceptible to drift and are harder to find with high

bandwidth. As an additional practical benefit, they allow a lot of flexibility in tuning measurement

parameters within software.

Post processing

In addition to the digital homodyne process, one typically does some minor postprocessing to the

data. One can apply a digital low pass filter, which is equivalent to averaging the data over some

interval, and eliminate some of the experiment and acquisition card noise. After that, one can safely

decimate the data to lessen the load on the acquisition program, save storage space, and improve

![SchusterThesis.pdf-154-0.png](SchusterThesis.pdf-154-0.png)

1 At this stage there is much more noise than just the half photon required by the quantum limit and so the signals
can be treated classically. If this procedure was done in a quantum limited set up it would be impossible to determine
both quadratures without introducing an extra port (and thus extra noise).


-----


CHAPTER 6. MEASUREMENT SETUP 153

analysis performance. One can also digitally apply a phase or amplitude offset, to the data and

display it in terms of I and Q, or phase and amplitude. In addition, one can apply filters to do a

quick analysis of data to extract Rabi or Ramsey oscillations as the data is acquired.


-----


### Chapter 7

## Characterization of CQED

This chapter begins the presentation of circuit QED experimental results. In this chapter we will

develop methods to measure all of the basic circuit QED parameters, including the energy scales,

decay rates, as well as the gate capacitance and loop mutual inductance. The first section will

discuss cavities without CPBs inside. The transition frequency and decay rate ( Q ) of resonators

made from aluminum and niobium will be studied as a function of temperature and magnetic field.

Then we will use the cavity to interrogate an embedded CPB/transmon to determine its spectral

properties and coupling to the cavity.

####### 7.1 ####### Cavity

Transmission line cavities are incredibly sensitive tools to measure any quantity that can be mapped

to an electric or magnetic reactance. In this thesis we focus on using them as a means of reading out a

superconducting qubit, or to store photons which can be measured by the qubit (and eventually lead

to non-local quantum logic gates). While circuit QED is only one application of this very promising

technology, the task requires the quality factors ranging from Q = 100 to as high as possible. This

has led us to develop a wide range of quality factors, and test the magnetic field and temperature

dependence of the cavity resonance frequency and quality factor.

The frequency dependence of the transmission through the resonators was measured using a vec-

tor network analyzer 1 . The equivalent circuit of the measurement setup is shown in the inset of Fig.

7.1. The sample was mounted on a PC board in a closed copper sample box (Fig. 5.13a) equipped

with blind mate SMP connectors that launch the microwaves onto the PC board CPWs. The sample

![SchusterThesis.pdf-156-0.png](SchusterThesis.pdf-156-0.png)

1 The power transmission is measured in dB = 10 log | V 2 / V 1 | 2 , where V 2 is the voltage measured at the input
port of the analyzer and V 1 is the voltage applied at the output port of the analyzer for equal input and output line
impedances.

154


-----


CHAPTER 7. CHARACTERIZATION OF CQED 155


-40

![SchusterThesis.pdf-157-0.png](SchusterThesis.pdf-157-0.png)

3.03685 3.03695 3.03705

Frequency,  (GHz)


Figure 7.1: Measured transmission power spectrum of an under-coupled resonator. The solid line is
a fit to a lorentzian line.

was cooled to temperatures ranging from the critical temperature, T c of the superconducting films

down to T = 30 mK.

The transmission S 21 through the resonator around its fundamental resonant frequency  1 is

shown in Fig. 7.1 at T = 30 mK. The curve was acquired using a  60 dBm input power and a room

temperature amplifier. The input power was lowered until no distortion of the resonance curve due

to excessive input power could be observed. The network analyzer was response calibrated ( S 21 ) up

to the input and output ports of the cryostat and the absorption of the cabling in the cryostat was

determined to be approximately  7 dB in a calibrated S 11 and S 22 reflection measurement. The

quality factor of the resonator is determined by fitting a Lorentzian line to the measured power

spectrum as shown by the solid line in Fig. 7.1. This is the transmission spectrum of an under-

coupled resonator and from the fit we have extracted  1 = 3 . 03694 GHz. At this frequency the

insertion loss, defined as the ratio of transmitted power to input power, is L 1 =  13 dB. The

quality factor is determined from the full width at half max of the fitted power spectrum and is

found to be Q L  Q ext =  1 / 2  1 = 2  1 / = 0 . 55  10 6 .

######### 7.1.1 ######### Temperature Dependence

In Fig. 7.2, we show the temperature dependence of the quality factor of an under-coupled (see

Fig. 7.2a) and an over-coupled (see Fig. 7.2b) Nb resonator. In both cases the harmonics have

lower Q than the fundamental. This is expected for both intentional coupling via the input/output

capacitors and resistive losses.

In Fig. 7.3a, we show the measured temperature dependence of the quality factor Q for an

under-coupled resonator (solid dots) and an over-coupled one (open dots). The lines in Fig. 7.3a


-----


CHAPTER 7. CHARACTERIZATION OF CQED 156


Q 1 under-coupled a) 2 x 10 4 Q 1 over-coupled b)


3 x 10 5

2 x 10 5

10 5


|Q over- 1 Q 2 Q 3|coupled b)|
|---|---|


0

![SchusterThesis.pdf-158-0.png](SchusterThesis.pdf-158-0.png)

1 2 3 4 5 0

temperature, T (K)


temperature, T (K)


Figure 7.2: Temperature dependence of the fundamental and harmonics of an under ( a ) and over
( b ) over coupled Nb resonator.

are generated by summing a Q ext that scales exponentially with the reduced temperature, T c /T , in

parallel with a constant Q int . At low temperature, the coupling saturates the Q of the over-coupled

resonator, while it seems that Q for the under-coupled one has still some weak temperature depen-

dence whose nature is still unknown. We speculate that either vortices or losses in the dielectrics

could limit the Q of this resonator but neither of these interpretations offer an easy understanding

of the weak temperature dependence.

In Fig. 7.3b, we plot the ratios of the quality factors for the first ( Q 2 /Q 1 ) and second harmonics

( Q 3 /Q 1 ). According to calculations in sections 3.1.4 and 3.1.7, both quality factor due to capacitive

coupling to the transmission line and resistive losses should scale like Q n /Q 1 = 1 /n , for the n th

resonance of the cavity. In both cases this results from the competition between having more

wavelengths which tends to increase Q   and the losses which tend to decrease Q   2 . In

the measured data, the general trend is obeyed. There is more loss at higher harmonics and the

ratios are similar whether the Q is dominated by resistive loss or by capacitive coupling. However,

there doesnt appear to be quantitative agreement as one can see by comparing the dashed lines

in Fig. 7.3b, to the experimental data. The under-coupled resonator also has some non-trivial

dependence which appears to be non-uniform in harmonic number. This might be due to the onset

of some other frequency dependent loss mechanism.

We have observed a shift of the resonant frequency  1 with temperature as shown in Fig. 7.4,

which can be understood in terms of the temperature dependent kinetic inductance of the resonator


![SchusterThesis.pdf-158-1.png](SchusterThesis.pdf-158-1.png)


[Day2003, Yoshida1995].  1 is proportional to 1 /


L , where the total inductance of the resonator


L is the sum of the temperature independent geometric inductance L m and the temperature de-


-----


CHAPTER 7. CHARACTERIZATION OF CQED 157



temperature, T (K) temperature, T (K)
10 2 1 0. 5 0. 3 10 2 1 0.5


10 2 1 0.5 0.3


10 6


10 5

10 4

10 3


0.8

0.6

0.4

0.2


![SchusterThesis.pdf-159-0.png](SchusterThesis.pdf-159-0.png)

![SchusterThesis.pdf-159-1.png](SchusterThesis.pdf-159-1.png)

10 15 20 25 30 0 5 10 15 20 25 30
temperature, T c / T temperature, T c / T


10 15 20 25 30 0 5 10 15 20
temperature, T c / T temperature, T c / T


Figure 7.3: Temperature dependence of the quality factor Q of two 3 GHz superconducting Nb
coplanar waveguide resonators at their first harmonic resonant frequency (6 GHz). Solid dots are
data collected on a under-coupled resonator and open dots are from an over-coupled one. The lines
are generated by summing a Q ext that scales exponentially with the reduced temperature, T c /T , in
parallel with a constant Q int . b) Plot of the ratios between the Q of the fundamental and higher
harmonics for under (blue) and over (red) coupled cavities. Dashed lines indicate expected values
of Q 2 /Q 1 = 1 / 2 and Q 3 /Q 1 = 1 / 3.

pendent kinetic inductance L K . The kinetic inductance scales as L k  L ( T ) 2 , where  L ( T ) is the


temperature dependent London penetration depth. The best fit in Fig. 7.4 was achieved for a ratio

L K /L m 7% and a critical temperature of T c 9 . 1 K , which we have independently measured on
 

a test sample fabricated on the same wafer.

######### 7.1.2 ######### Magnetic Field Dependence

As explained in section 3.2, we need to apply a magnetic field perpendicular to the qubit loop in

order to tune E J . It is important that small these small fields ( T ) not destroy the resonator


quality factor. In Fig. 7.5, we measure the quality factor of two resonators as a function of the

magnetic field at T = 300 mK, as shown in Fig. 7.5. It is evident that the Nb film ( a ) is less

sensitive to the applied field than the Al film ( b ). In both cases there seems to be a reproducible

and irreversible hysteretic behavior that can be reset by thermal cycling the sample. In our initial

experiments (see Sec. 7.2), we have observed a magnetic field focusing effect, such that the effective

field in the gap of the resonator was approximately two orders of magnitude larger than the applied

magnetic field. We believe that the hysteretic phenomena could be a result of vortices being trapped

in the resonator film due to these large effective fields.

A magnetic field not only affects the quality factor of a resonator, it also slightly changes the

kinetic inductance, shifting the resonance frequency. The magnetic field dependence of Nb and Al


-----


CHAPTER 7. CHARACTERIZATION OF CQED 158

temperature, T  T c

0 0.25 0.5


3.005

3

2.995

2.99


![SchusterThesis.pdf-160-0.png](SchusterThesis.pdf-160-0.png)

temperature, T H K L

Figure 7.4: Temperature dependence of the fundamental resonant frequency  r of a superconducting
Nb coplanar waveguide resonator. Solid line is a fit to a kinetic inductance model.


20000

15000

10000

5000


20000


20000


![SchusterThesis.pdf-160-1.png](SchusterThesis.pdf-160-1.png)

![SchusterThesis.pdf-160-2.png](SchusterThesis.pdf-160-2.png)

 40  20 0 20 40

magnetic field, B (G)


15000

10000

5000

0

 40  20 0 20 40

magnetic field, B (G)


Figure 7.5: Magnetic field dependence of the quality factor Q of two different superconducting
coplanar waveguide resonators at T = 300 mK. In the upper part data refer to a Nb resonator,
while in the lower part they refer to an Al resonator. Arrows indicate the direction in which the
magnetic field was swept in both cases starting from zero.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 159



2.65

2.648

2.646

2.644

2.642

2.64


2.696


![SchusterThesis.pdf-161-0.png](SchusterThesis.pdf-161-0.png)

![SchusterThesis.pdf-161-1.png](SchusterThesis.pdf-161-1.png)

 40  20 0 20 40

magnetic field, B (G)


2.694

2.692

2.69

2.688

2.686

 40  20 0 20 40

magnetic field, B (G)


Figure 7.6: Magnetic field dependence of the fundamental resonance frequency of two different
superconducting resonators at T = 300 mK. Both the Nb ( a ) and Al datasets are plotted on the
same scale (10 MHz). The arrows indicate the direction in which the magnetic field was swept in
both cases starting from zero.

resonators is plotted in Fig. 7.6. Both plots are on a 10 MHz scale and show that the Al resonator

shifts significantly more than the Nb one. However, though it shifts more it has significantly less

hysteresis. While tuning the qubit in circuit QED experiments, both the shift and the different

hysteresises are quite noticeable. This lends further weight to the suspicion that vortices are trapped.

Vortices should be less stable in Al than in Nb and therefore have less hysteresis once the field is

removed. Though these vortices clearly affect the quality factor of the resonators it is unclear

whether they have a negative impact on the qubit decay.

The resonators are quite stable drifting much less than a linewidth over many months of data

taking. They are very reproducible upon warming and cooling (with no field) returning to the

same frequency within less than a few MHz. Run to run the cavities can be made with resonant

frequencies repeatable to  100 MHz and with Q  s generally repeatable to  20%, with variation

due mainly to over or under exposure of the optical resist. In practice the exact values are not

critical as the dispersive coupling falls off slowly (like 1 / ) and the qubit is also tunable allowing

one to accommodate a wide range of resonator parameters.

####### 7.2 ####### Cooper pair box

To characterize the effect of the Cooper pair box on the cavity, we will continuously probe the

amplitude and phase of a microwave tone at at frequency  RF =  r . Most parameters can be

extracted from cavity response to the qubit in its ground state, via its dependence on bias voltage,

V g , and flux,  B . Such a ground state characterization process is advantageous because such probes


-----


CHAPTER 7. CHARACTERIZATION OF CQED 160

are relatively insensitive to the qubit decay rates and require no additional tones or pulse synthesis.

A very similar inductive technique has also been used to characterize the CPB [Born2004], but this

was done at low frequency using a magnetic coupling rather than at high frequency (and with electric

coupling). By interacting with the qubit on energy scales greater than the thermal background we

are able to study cavity QED with the same coupling.

The resonator frequency is given a dispersive shift due to the presence of the qubit.

 r  =  r  (7.1)




The dispersive shift is  g  2 with the is determined by the qubit state. This qubit state-
 

![SchusterThesis.pdf-162-0.png](SchusterThesis.pdf-162-0.png)

dependence of the cavity frequency is used for the qubit readout. However, even in the ground state

the resonator frequency depends on the qubit detuning, and coupling strength g , which both in

turn depend on the bias parameters of the CPB. The qubit frequency  a (plotted in Fig. 7.7a) can

be tuned with either gate or flux. The phase (or amplitude) of a tone at the bare resonator frequency

(  RF =  r ) is a sensitive probe of the dispersive shift. As the gate voltage or flux is tuned so that

the qubit frequency approaches the resonator frequency, the frequency shift gets larger, resulting

in a phase shift of the probe beam (Fig. 7.7b top). When the qubit transition frequency crosses

the resonator (changes sign) the dispersive shift, and thus the phase shift will also change sign

(Fig. 7.7b bottom). This large feature can act as a marker as to how the gate and flux biases affect

the CPB. The location of these sign changes can be thought of as the intersection of the transition

frequency landscape with a plane at  =  r (see Fig. 7.7c).

The resulting response, resembling footballs, has several important features. The first is that

it is periodic along both the flux and charge axes. This periodicity results from the quantized nature

of charge on the island and flux in the loop of the CPB. We can find the effective gate capacitance

by equating the periodicity of the gate voltage with one Cooper pair 1 , C g V g = 2 e . The periodicity

in the magnetic field (vertical) direction measures the field necessary to apply a single flux quantum

(giving the effective loop area).

In addition to the periodicity one can learn about the CPB energy scales, E J max and E C by

looking at the major and minor axes of the footballs relative to the periodicity. Considering the

![SchusterThesis.pdf-162-1.png](SchusterThesis.pdf-162-1.png)

1 According to the CPB Hamiltonian the periodicity of the gate charge should be 2 e . However, if there are
quasiparticles (single electrons) which are free to tunnel the response can appear to be 1 e periodic. To eliminate
this possibility the periodicity was observed as it was cooled and heated to about 250 mK where the number of
quasiparticles increases dramatically. At low temperatures the curves (of the type in Fig. 7.7b) were 2 e periodic with
occasional 1 e jumps, where as when the temperature was increased, the number of jumps increased, and eventually
the curves became 1 e periodic.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 161

a b gate voltage, V g (V)

 1 0 1 2


20

10

0

 10

 20

 30

 40

1.

0.5


20

15

10

5

0


![SchusterThesis.pdf-163-0.png](SchusterThesis.pdf-163-0.png)

![SchusterThesis.pdf-163-1.png](SchusterThesis.pdf-163-1.png)

 2  1 0

gate charge, n g

![SchusterThesis.pdf-163-7.png](SchusterThesis.pdf-163-7.png)

![SchusterThesis.pdf-163-6.png](SchusterThesis.pdf-163-6.png)

![SchusterThesis.pdf-163-5.png](SchusterThesis.pdf-163-5.png)

![SchusterThesis.pdf-163-9.png](SchusterThesis.pdf-163-9.png)

![SchusterThesis.pdf-163-8.png](SchusterThesis.pdf-163-8.png)

![SchusterThesis.pdf-163-2.png](SchusterThesis.pdf-163-2.png)

 2  1 0


 2  1 0 1 2

gate charge, n g

gate voltage , V g (V)

1 0 1 2

50


 B / 0

 0.5 5

 1


45

40

35


0.


 0.5




20


10


![SchusterThesis.pdf-163-4.png](SchusterThesis.pdf-163-4.png)

![SchusterThesis.pdf-163-3.png](SchusterThesis.pdf-163-3.png)

 2 


gate charge, n g gate charge, n


Figure 7.7: Response of cqed system to charge and flux bias, using data taken from sample
CQED057 [Wallraff2004]. a) Calculated level separation  a =  a / 2  = E a /h between ground
| g  and excited state | e  of qubit for two values of flux bias  B = 0 . 8 (orange line) and  B = 0 . 35
(green line). The resonator frequency  r =  r / 2  is shown by a blue line. Resonance occurs at
 a =  r symmetrically around degeneracy n g = 1, see red arrows. The detuning  / 2  =  =  a   r
is indicated. b) Measured phase shift  of the transmitted microwave for values of  B in a. Green
curve is offset by 25 deg for visibility. c) Calculated qubit level separation  a
versus bias parameters n g and  B . The resonator frequency   r is indicated by the blue plane. At the intersection, also
indicated by the red curve in the lower right hand quadrant, resonance between the qubit and the
resonator occurs (  = 0). For qubit states below the resonator plane the detuning is  < 0, above
 > 0. d) Density plot of measured phase shift  versus n g and  B . Light colors indicate positive 
(  > 0), dark colors negative  (  < 0). The red line is a fit of the data to the resonance condition
 a =  r . In c and d, the line cuts presented in a and b are indicated by the orange and the green
line, respectively. The microwave probe power P RF used to acquire the data is adjusted such that
the maximum intra-resonator photon number n at  r is about 10 for g 2 /    1. The calibration of
the photon number has been performed in situ by measuring the ac-Stark shift of the qubit levels

[Schuster2005].


-----


CHAPTER 7. CHARACTERIZATION OF CQED 162

extent of the football in the flux direction yields


E J max = cos(     r r /  0 ) (7.2)

![SchusterThesis.pdf-164-0.png](SchusterThesis.pdf-164-0.png)

where  r /  0 is the ratio of the bias flux when the qubit and resonator are degenerate to the

periodicity (one flux quantum). When attempting to find the charging energy in a similar way, one

immediately notices that the signal is absent along the footballs gate charge axis. The magnitude

of the phase response is expected to vary with both gate charge and flux. The phase shift is largest

when the transition frequency (  a ) intersects the resonator frequency (  r ) at degeneracy n g = 1.

This is because the coupling strength is proportional to the charge transition matrix element

g 2 g N  e 2 E J 2 / (16 E C 2 (1 n g ) + E J 2 ) (7.3)
|  | | |  

which as E J = E J max cos(   B /  0 ) approaches zero 1 at  B =  0 / 2.
| |

To get a rough idea of the charging energy one can extrapolate the qubit-resonator degeneracy

curve to  B  0 / 2 which would (in the charge regime) yield



  r
E C (7.4)
 4(1 n g )

![SchusterThesis.pdf-164-1.png](SchusterThesis.pdf-164-1.png)



While looking at these two slices is the most conceptually simple way to find E J max and E C , one

can improve the accuracy by extracting the qubit-resonator degeneracy contour and numerically

fitting it to an exact expression for the CPB transition energy. This method is a good way of getting

the energy scales to  10% accuracy, with little initial idea of the box parameters. However, it is a

quite inefficient method with only an infinitesimal curve being selected out of the entire area of the

large 2D data set in figure 7.7d. So while its ability to capture the rough behavior of a device with

nearly any parameters is a great asset, the absolute accuracy is limited by the large dynamic range

required in the presence of potentially large amounts of charge noise.

Using an additional spectroscopy tone (at  s =  r ) and measuring the transmitted phase shift of


a tone at the resonator frequency,  r , one can probe the qubit at frequencies away from degeneracy

with the cavity. This allows the qubit spectrum to be determined directly, with accuracy of  2 ,

better than a part in 10  4 relative accuracy. When the qubit is excited, the phase shift of the probe

tone is opposite from when the qubit is in the ground state (see Fig. 7.9a). When the spectroscopy

frequency matches the qubit transition frequency  s =  a and the qubit is excited, reducing the

![SchusterThesis.pdf-164-2.png](SchusterThesis.pdf-164-2.png)

1 E J  0 at  B =  0 / 2 if the junctions are perfectly symmetric. If there is an asymmetry then some Josephson
coupling will remain. For more details about the effects of junction asymmetry see section 3.2.3.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 163



 B /  0

0.5


40

20

0

6.5



10

|Col1|2|
|---|---|
||2 1. 1|
|||


2 3 4 n g = C g V g /e

|0.9 0.95 1 = C V /e 1.05 g g g|6 6.4 (GH 6.3  s 6.2|
|---|---|


n g = C g V g /e


1.1


Figure 7.8: a) The spectroscopy experiment can be thought of as taking the intersection between
the transition energy surface and a plane at constant  B . b) A surface plot of spectroscopy data
from sample CQED057.

phase shift. For example, when the qubit is saturated, the qubit has an equal chance of being in the

ground or excited state, resulting in zero phase shift. The reduction in phase shift (see Fig. 7.9b)

allows one to directly trace out the transition energy of the qubit. While the footballs plot in Fig.

7.7 can be thought of slicing the transition energy landscape with a plane at constant frequency,

such spectroscopy experiments can be thought of as taking a slice at constant  B . By tuning the

flux to  B = n  0 , and measuring the transition frequency at n g = 1, one can calculate E J max to

better than a Megahertz 1 . Fitting to the whole spectroscopy curve gives a good estimate of the

charging energy, E C , as well.

The width and the saturation level of the spectroscopic lines discussed above, depend sensitively

on the power ( P s ) of the spectroscopic drive. Both quantities are related to the excited state

population



1
P e = 1 P g =
 2


n s (2 g ) 2 T 1 T 2

1 + ( T 2  s , a ) 2 + n s (2 g ) 2 T 1 T 2 , (7.5)


![SchusterThesis.pdf-165-0.png](SchusterThesis.pdf-165-0.png)

![SchusterThesis.pdf-165-1.png](SchusterThesis.pdf-165-1.png)

where  s , a is the detuning between the spectroscopy drive and the qubit frequency, and n s is the

number of photons in the spectroscopy drive. The lineshape of the qubit is given by the steady state

Bloch equations [Abragam1961], where 2 g is the vacuum Rabi frequency, n s the average number

of spectroscopy photons in the resonator, T 1 the relaxation time and T 2 the dephasing time of the

qubit. We have extracted the transition line width and saturation from spectroscopy frequency scans

for different drive powers ( P s ) with the qubit biased at charge degeneracy ( n g = 1). We observe

that the spectroscopic lines have a lorentzian line shape (also see Fig. 7.10a), with width and depth

![SchusterThesis.pdf-165-2.png](SchusterThesis.pdf-165-2.png)

1 In order to get the best value for E J max one can measure the transition frequency at degeneracy and sweep the
flux to find its maximum.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 164


a) c 4 b) 6.2 GHz c)


40


![SchusterThesis.pdf-166-0.png](SchusterThesis.pdf-166-0.png)

50

25

0

 25

 50

![SchusterThesis.pdf-166-1.png](SchusterThesis.pdf-166-1.png)

0.8 1 1.2


20

0

40

20

0

40

20

0

![SchusterThesis.pdf-166-3.png](SchusterThesis.pdf-166-3.png)

0.9 0.95 1 1.05 1.1


6.4

6.35

6.3

6.25

6.2

6.15

![SchusterThesis.pdf-166-4.png](SchusterThesis.pdf-166-4.png)

![SchusterThesis.pdf-166-2.png](SchusterThesis.pdf-166-2.png)

0.9 0.95 1 1.05 1.1


gate charge, n g gate charge, n g gate charge, n g


Figure 7.9: Spectroscopic interrogation of qubit transition energy using data from
CQED057 [Schuster2005]. a) Ground | g  and excited | e  state energy levels of CPB vs. gate
charge n g and calculated phase shift  in ground and excited state vs. n g for  a , r / 2  = 100 MHz.
b) Plots of measured dispersive shift vs. n g showing qubit response to an applied spectroscopy tone.
c) Plot of phase shift (intensity) vs. gate charge, n g and spectroscopy frequency,  s . The curve of
suppressed phase shift is a direct measurement of the qubit transition frequency,  a .

in accordance with Eq. (7.5). The half width at half max (HWHM) of the line is found to follow the


expected power dependence 2  HWHM = 1 /T 2  =


1 /T 2 2 + n s (2 g ) 2 T 1 /T 2 [Abragam1961], where


![SchusterThesis.pdf-166-5.png](SchusterThesis.pdf-166-5.png)

the input microwave power P s is proportional to n s (2 g ) 2 , see Fig. 7.10a. In the low power limit

( n s (2 g ) 2 0), the unbroadened line width is found to be small  HWHM 750 kHz, corresponding
 

to a long dephasing time of T 2 > 200 ns at n g = 1, where the qubit is only second order sensitive to

charge fluctuations limiting the dephasing time in this sample. At larger drive, the width increases

proportionally to the drive amplitude. The depth of the spectroscopic dip at resonance ( s , a = 0)

reflects the probability of the qubit to be in the excited state P e , and depends on P s as predicted by

Eq. (7.5), see Fig. 7.10b. At low drive the population increases linearly with P s and then approaches

0 . 5 for large P s . From time resolved measurements (data not shown), T 1 is found to be on the

order of a few microseconds, a value which is much shorter than that expected for radiative decay of

the qubit in the cavity [Blais2004], indicating the existence of other, possibly non-radiative, decay

channels.

######### 7.2.1 ######### Charge Noise

A significant obstacle to performing long duration experiments with high fidelity on the CPB is

charge noise, which comes in several flavors. White noise blurs the features along the bias charge axes

in Figs. 7.7-7.8, limiting the resolution of these features and coherence time of the qubit. In addition


6.2 GHz


-----


CHAPTER 7. CHARACTERIZATION OF CQED 165


photon number, n s

0.2 0.4 0.6


photon number, n s

0.2 0.4 0.6

![SchusterThesis.pdf-167-1.png](SchusterThesis.pdf-167-1.png)

0.5 1 1.5

spec power, P s (  W)


0.5

0.4

0.3

0.2

0.1


3.

2.

1.
0.


50

40

30

20

10


![SchusterThesis.pdf-167-0.png](SchusterThesis.pdf-167-0.png)

0.5 1 1.5 2

input spec. power, P s (  W)


Figure 7.10: a) Measured qubit line width  HWHM vs. input spectroscopy power P s (solid circles)
with fit (solid line). Probe beam power P RF is adjusted such that n < 1. (b) Measured peak depth
 and excited state population probability P e on resonance  s , a = 0 vs. P s (solid circles) with fit
(solid line).

to this disruptive, but well-behaved noise, there are also two types of discrete events known as charge

switchers. These switchers cause discrete jumps in the apparent bias charge, n g . One class of

switchers are due to quasiparticles tunneling, which cause jumps with magnitude 1 e (see Fig. 7.11a).

In our devices at zero flux, there are usually many parity jumps in one averaging time, causing

a shadow pattern to appear shifted by one electron. As magnetic field is increased, the shadow

can be reduced significantly. While the exact cause of this effect is unknown, we suspect that the

superconducting gap of the island and fingers are reduced differently by application of the magnetic

fields. This would not eliminate quasiparticles, but does prevent them from tunneling across the

junction. The preferred parity can also change on timescales of seconds to hours depending on the

exact device and bias conditions (see Fig. 7.11). One also notices sub-electron switching events,

such as the particularly pathological switcher in figure 7.11c, and barely noticeable deviations in

the spectrum shown in figure 7.9c. Particularly, bad switchers can sometimes be eliminated by

warming and cooling the sample, or by careful selection of the bias point. In decent samples, data

can be taken for periods of  1hr (see Fig. 7.11c) without a large switching event ( > 0 . 01 e ). Every

device cooled showed working samples, and could be characterized. Of these, about two thirds could

had sufficiently long windows of stability that more intense investigations were deemed worthwhile.

These discrete jumps have in practice caused the most difficulty in acquiring the data, as they make

it difficult to bias the qubit for a long enough time to measure.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 166


a) bad parity b) 4.75 switcher c)


100

80

60

20

0

![SchusterThesis.pdf-168-5.png](SchusterThesis.pdf-168-5.png)

![SchusterThesis.pdf-168-2.png](SchusterThesis.pdf-168-2.png)

 1.5  1  0.5 0 0.5 1 1.5

gate charge, n g


![SchusterThesis.pdf-168-3.png](SchusterThesis.pdf-168-3.png)

![SchusterThesis.pdf-168-4.png](SchusterThesis.pdf-168-4.png)

![SchusterThesis.pdf-168-0.png](SchusterThesis.pdf-168-0.png)

![SchusterThesis.pdf-168-1.png](SchusterThesis.pdf-168-1.png)

 1


3.25


 1


gate charge, n g


gate charge, n


Figure 7.11: a) A plot of transmitted amplitude as a function of charge and flux bias, showing a
preferred parity and residual off-parity shadow. At n g = 0 there is a repetition of the pattern at
n g = 1, due to imperfect parity. As the magnetic field is increased it the parity improves significantly.
b) A sub-electron charge switcher which switches fast (compared to the averaging time of  1s),
relatively even duty cycle, and is large  0 . 3e. Both a and b use data from CQED061 the device
used in [Wallraff2005]. c) In a and b the switching is so fast that it just looks like a shadow. In c
the magnetic field is fixed, and the same trace is repeated (this measurement done on CQED097).
It clearly shows both parity jumps (infrequent) and sub-e switching events (more frequent). This
sample is fairly typical, and the best data would be taken in an interval (typically 20  30 minutes)
where no switching events occurred.

######### 7.2.2 ######### Measured CPB properties

It is useful to take a survey of all of the samples that were measured. Despite a small number

of samples table 7.1 explores a large range of parameters. Quality factors from 10 2  10 4 were ex-

plored allowing experiments based on fast measurements (single photon generation) and long photon

coherence (number splitting). Less intentionally a large range of E J max was also explored. These

fluctuations were largely due to drift in fabrication parameters. More interestingly, the charging

energy, E C , which is very well controlled, was varied from 5 GHz a typical CPB scale to as low as

370 MHz well into the new transmon regime. By varying size of the island and capacitive division

a large range of vacuum Rabi couplings, g , were explored from rather small (but still well into the

strong coupling limit) values of 2 . 25 MHz to values approaching the fine structure limit, 115 MHz.

####### 7.3 ####### Transmon

The transmon, gloriously, has no charge dependence, so we must measure its energy scales without

exploiting the charge dependence of the energy levels as we did when measuring the traditional CPB.

Because the transmon has one less degree of freedom, it is actually much easier to characterize. In

the traditional CPB, the parameter space was sufficiently large that one had to do a first pass to


-----


CHAPTER 7. CHARACTERIZATION OF CQED 167

ID Cavity  r (GHz) Q E J max (GHz) E C (GHz) g/ 2  (MHz) T 1 (  s) T 2 (ns)

![SchusterThesis.pdf-169-0.png](SchusterThesis.pdf-169-0.png)

![SchusterThesis.pdf-169-1.png](SchusterThesis.pdf-169-1.png)

052 R5-008 6.0413 8534 6.7 5 2.25 1.2 48
057 R5-005 6.0435 10469 8 5.2 5.8 0.6 227
061 R6-008 5.4262 7807 4.312 5.2 17 7 500
063 R6-005 5.4139 8462 8.2 3.45 10 4.1 159
80a R22-107 5.0987 6101 40 2.49 58 0.52 159
80b R22-107 5.0987 6101 43 2.65 25 > 31
971R R49-105 5.5331 10300 12 5.25 17 3 200
971R R49-105 5.5331 24822 13 5.25 25

![SchusterThesis.pdf-169-2.png](SchusterThesis.pdf-169-2.png)

![SchusterThesis.pdf-169-3.png](SchusterThesis.pdf-169-3.png)

120c R062-06 5.6705 24822 18.5 0.518 105 53
128 R96-C1 5.173 120 20.19 0.371 115 0.09 145

Table 7.1: Summary of sample parameters.

get an approximate idea of the energy scales, then use this knowledge to set up a spectroscopy

experiment rather carefully. With the transmon, the lack of charge dependence and the extra

stability that provides, one can immediately jump to spectroscopy. In a single two dimensional data

acquisition, one can scan transition frequency vs. magnetic flux (see Fig. 7.12). By fitting this flux

dependence, one can determine both E J max and E C . Because of the transmons small anharmonicity,

another technique, which is even more accurate, becomes available. One can measure the transition

frequencies of auxiliary levels, which are now at accessible frequencies. Because the whole spectrum

is determined by E J and E C , a measurement of any two transition frequencies, uniquely determines

the both energy scales. By using two photon spectroscopy, one can easily measure  12 in addition to

the usual transition energy. This method is especially good because it does not require the qubit bias

point to be changed, so it can be performed immediately before an experiment. In the asymptotic

limit, where the energy levels are given by Eq. 4.78, E J and E C are given by


E J  (  12  2  01 ) 2
 8(  01  12 )


(7.6)

![SchusterThesis.pdf-169-4.png](SchusterThesis.pdf-169-4.png)
8(  01  12 )



E C   =  (  01  12 ) (7.7)
 


For more accurate results, one can numerically solve for E J and E C , using the exact expression

based on the Mathieu functions given in appendix C.1.


-----


CHAPTER 7. CHARACTERIZATION OF CQED 168


8.15

8.1

8.05

8

![SchusterThesis.pdf-170-2.png](SchusterThesis.pdf-170-2.png)

![SchusterThesis.pdf-170-0.png](SchusterThesis.pdf-170-0.png)

 0.075 0 0.075

magnetic flux,    0


![SchusterThesis.pdf-170-1.png](SchusterThesis.pdf-170-1.png)

6.8 6.9 7.0 7.1 7.2 7.3 7.4 7.5

Frequency,  s (GHz)


Figure 7.12: a) Spectroscopy of the qubit transition frequency  01 vs. flux near E J max . b) The
transition frequencies from the ground to the first and second excited states can be used to determine
E J and E C . To find  01 conventional spectroscopy is used. To find  02 / 2 a single spectroscopy tone
is used at very high powers to exciting a two photon process. One can find  12 by taking  02   12
but it can also be measured directly by using two spectroscopy generators, tuning the first to  01
and sweeping the second near  12 .


-----


### Chapter 8

## Cavity QED Experiments with Circuits

This chapter will focus on exploring the different regimes of cavity QED as depicted by the phase

diagram in figure 8.1. First, in the resonant regime (Fig. 8.1 blue region where  < g ), we observe

strong coupling for the first time in a solid state system, in the form of vacuum Rabi mode splitting.

We explore tuning the qubit in and out of resonance with the cavity, using both charge and flux.

When the qubit is detuned sufficiently (  g ), the qubit enters the dispersive regime.

We study the transition from resonant to dispersive measuring the Purcell effect, a mechanism

of indirect qubit decay through the cavity, which enhances decay near resonance, and suppresses it

when far detuned. Once firmly in the dispersive regime, we first study the weak dispersive limit

(Fig. 8.1 red region where   g and  < max ,  ). Here, the effects of the dispersive coupling can

be seen through the AC Stark shift on the qubit. This study explores the mechanism of quantum

backaction in the cavity-based qubit measurement. A slight modification allows the effect to be used

without backaction (and making no measurement) to create a frequency shift/phase gate.

While in the resonant regime there are spontaneous vacuum Rabi oscillations between qubit

excitations and photons, in the dispersive regime such transitions must be stimulated. By exciting

the qubit-cavity sidebands, one can make simultaneous qubit-photon transitions, which could allow

for teleportation and quantum logic over centimeter distances. While we most commonly think of

the cavity as measuring the qubit, the nature of the dispersive Hamiltonian implies that the qubit

also measures the photon number.

When the coupling strength is large enough, but still dispersive (Fig. 8.1 white region where

g 2 /  >  and g <  / 10), we observe the qubit spectrum resolving into separate photon number

169


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 170

40


30

20

10


![SchusterThesis.pdf-172-0.png](SchusterThesis.pdf-172-0.png)

0 100 200 300 400 500

 / 

Figure 8.1: A phase diagram for cavity QED. The parameter space is described by the atom-photon
coupling strength, g , and the detuning, , between the atom and cavity frequencies, normalized
to the rates of decay represented by  = max [ , , 1 /T ]. Different cavity QED systems, including
Rydberg atoms, alkali atoms, quantum dots, and circuit QED, are represented by dashed horizontal
lines. In the blue region the qubit and cavity are resonant, and undergo vacuum Rabi oscillations.
In the red, weak dispersive, region the ac Stark shift g 2 /  <  is too small to dispersively resolve
individual photons, but a QND measurement of the qubit can still be realized by using many photons.
In the white region, quantum non-demolition measurements are in principle possible with demolition
less than 1%, allowing 100 repeated measurements. In the green region single photon resolution is
possible but measurements of either the qubit or cavity occupation cause larger demolition. In the
yellow region the cavity becomes anharmonic, allowing it to create squeezed states and inherit some
inhomogeneous broadening, and the Stark shift becomes non-linear.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 171

peaks. Finally, in a hint of the anharmonic coupling regime, (Fig. 8.1 yellow region where g 4 /  3 > 

and  > g ), the cavity becomes non-linear with even just a few photons in the cavity.

####### 8.1 ####### Resonant Limit

Cavity QED at its heart seeks to create a coherent coupling between a two level system and a single

photon. Once established, the qubit-photon coupling can be used to detect and generate quantum

states of light, cool or invert the qubit, and make logical gates between distant qubits. This section

discusses perhaps the most important result in this thesis, a direct measurement of the qubit-photon

coupling. Using bias charge ( n g ) or flux ( B ), the qubit is tuned into resonance with the cavity.

Two experiments will be discussed. In the first case, a traditional CPB is used with charge as the

primary control parameter, while employing a modest dipole coupling ( g = 6 MHz), and similar

cavity ( / 2  = 0 . 8 MHz) and qubit (  2 / 2  = 0 . 7 MHz) linewidths. In the second case, a transmon

is used with flux as the control parameter and employs a dipole coupling which approaches the limit

set by the fine structure constant (2 g = 228 MHz)! For this sample, a much higher cavity decay rate

 = 43 MHz relative to qubit decay rate (  2 / 2  = 2 . 5 MHz) was chosen, both to increase visibility

of coupled peaks, and to observe fast dynamics in other experiments (see Sec. 9.3).

######### 8.1.1 ######### Vacuum Rabi Mode Splitting with CPB

To perform this experiment, the qubit is first characterized (see Sec. 7.2), and then tuned by magnetic

flux to have its minimum transition frequency  a E J /h degenerate with (see Fig. 8.2a) or just


below the resonator frequency,  r (see Fig. 8.2b). To acquire the data in figure 8.2, the transmitted

amplitude of a single tone is measured in a narrow band via a heterodyne technique as a function

of  RF . The gate charge bias is then stepped near n g = 1. As described in chapter 2, when the

cavity and qubit approach degeneracy (  0), excitations become shared between them. The

eigenstates of the system are no longer | e, 0  and | g, 1  , but even and odd superpositions of those


![SchusterThesis.pdf-173-0.png](SchusterThesis.pdf-173-0.png)

states ( | g, 1  | e, 0  ) /


2. In order to see transmission, the drive tone must be resonant with the


transition from the ground state | g, 0  to one of these eigenstates of the strongly coupled system.

The measured spectra in figure 8.2 are compared with the eigenfrequencies predicted by the Jaynes-

Cummings Hamiltonian for the parameters found in section 7.2, and have very good agreement.

In figure 8.3, a spectrum extracted from Fig. 8.2a at = 0 (Fig. 8.3b) is compared with one

taken at   g . Fig. 8.2b also visually, and dramatically, demonstrates that the system is in


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 172


######## gate voltage, V ######## g

########## -0.14 ########## -0.1 ########## -0.06


######## gate voltage, V ######## g

########## -0.6 ########## -0.55 ########## -0.5

![SchusterThesis.pdf-174-4.png](SchusterThesis.pdf-174-4.png)

![SchusterThesis.pdf-174-1.png](SchusterThesis.pdf-174-1.png)

 0.95 1. 1.05

######## gate charge, n ######## g


########## 6.06

 6.05

 6.04

 6.03


########## 6.06

 6.05

 6.04

 6.03

 6.02


![SchusterThesis.pdf-174-5.png](SchusterThesis.pdf-174-5.png)

![SchusterThesis.pdf-174-0.png](SchusterThesis.pdf-174-0.png)

########## 0.98 1.00 1.02 1.04

######## gate charge, n ######## g


Figure 8.2: a) Vacuum Rabi avoided crossing as function of gate charge ( n g ) where the qubit and
cavity are resonant at charge degeneracy n g = 1. Color shows transmission (blue is low, red is high)
of a microwave probe tone at  RF . The dashed white curve shows the transition frequency as a
function of n g , of an uncoupled cavity and qubit ( g = 0). The solid white line shows the expected
transition frequencies from the ground state to first and second excited states of the strongly coupled
cavity-qubit system. b) The same as a except that the cavity-qubit degeneracy does not occur at
n g = 1 but slightly away, yielding two avoided crossings. The states far away from the avoided
crossing resemble either a single photon or qubit excitation, but near the cavity-qubit where the
transition spectrum is curved the excitations have both photon and qubit character. At these points
the upper and lower branch are whimsically called a phobit and quton, to signify their joint nature.



0. 8

0. 6

0. 4

0. 2


0.1

0.08

0.06

0.04

0.02


![SchusterThesis.pdf-174-2.png](SchusterThesis.pdf-174-2.png)

![SchusterThesis.pdf-174-3.png](SchusterThesis.pdf-174-3.png)

6.02 6.03 6.04 6.05 6.06 6.07 6.02 6.03 6.04 6.05 6.06 6.07

frequency,  RF (GHz) frequency,  RF (GHz)

Figure 8.3: Vacuum Rabi mode splitting. a) Measured transmission T 2 (blue line) versus microwave
probe frequency  RF for large detuning ( g 2 /    1) and fit to Lorentzian (dashed red line). The
peak transmission amplitude is normalized to unity. a) Measured transmission spectrum for the
resonant case = 0 at n g = 1 (blue line) showing the vacuum Rabi mode splitting compared to
numerically calculated transmission spectra (red and light blue lines) for thermal photon numbers
of n = 0 . 06 and 0 . 5, respectively. The dashed line is the calculated transmission for g = 0 and
/ 2  = 0 . 8 MHz. b) Measured transmission spectrum for the resonant case = 0 at n g = 1 (blue
line) showing the vacuum Rabi mode splitting compared to numerically calculated transmission
spectra (red and light blue lines) for thermal photon numbers of n = 0 . 06 and 0 . 5, respectively and
2 g = 12 MHz. The dashed line is the calculated transmission for g = 0 and / 2  = 0 . 8 MHz.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 173

the strong coupling regime. The fact that there are two well-resolved peaks clearly shows that the

vacuum Rabi mode splitting of the cavity line (2 g = 12 MHz), is much larger than the average of the

cavity and qubit line widths, (  +  2 ) / 2, the definition of strong coupling. In fact, 4 g/ (  +  2 ) = 16,

putting the system well into the strong coupling regime. We claim that this is evidence of a single

photon interacting with the qubit. In a harmonic oscillator spectrum (see Fig. 8.3a) it is difficult

to perform an absolute calibration of the photon number. However, the transmission spectrum of

the joint system, which is highly anharmonic when degenerate, is very sensitive to the intracavity

photon number. Theory predictions for n = 0 . 06, and n = 0 . 5 photons are plotted on top of the

measured spectrum (see Fig. 8.3b). There is excellent agreement 1 with the n = 0 . 06, and the shape

would be noticeably distorted with even n = 0 . 5 photons present in the cavity. Another significant

feature of the spectrum in Fig. 8.3b is the significantly reduced transmission of both peaks. In some

sense, this is the strongest evidence that the states are truly the entangled states of a qubit and

harmonic oscillator. The reason they are reduced is that the qubit (and thus the joint system) is

very anharmonic, leading to inhomogenous broadening and also decay into a non-radiative bath.

Because the excitation is shared between the two systems, the decay of the qubit into non-radiative

channels eats the photons, and the inhomogenous broadening scatters them into other frequencies

filtered out by the heterodyne spectroscopy technique used. The qubit has in effect stolen some of

the photons from the cavity, which reduces the overall transmission significantly.

######### 8.1.2 ######### Vacuum Rabi Mode Splitting With Transmon

The strong coupling limit can also be reached using the transmon (see Fig. 8.4). Though the

principles of the experiment are similar, there are several differences from the previous experiment.

The transmon itself is quite different, having effectively no bias charge dependence due to the ratio

of E J = 9 . 1 GHz and E C = 371 MHz with E J /E C = 24. The flux bias is much more stable than the

charge bias as there appear to be no large fluctuations due to local sources. Therefore the avoided

crossing in flux (see Fig. 8.4a) was measured with much higher resolution. In addition, the vacuum

Rabi splitting, 2 g = 228 MHz is more than an order of magnitude larger than the previous result

(see Fig. 8.4a). In the previous experiment, the transmission was significantly reduced by absorption

and scattering to out-of-band frequencies by the qubit. In order to avoid this problem, and allow

efficient generation of single photons (see Sec. 9.3), we significantly increased the output coupling

![SchusterThesis.pdf-175-0.png](SchusterThesis.pdf-175-0.png)

1 While n = 0 . 06 was used in the plot, this should not be construed as a lower bound on the photon number as the
spectrum is normalized and smaller ns might also fit well.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 174


a)


/ 0

-0.35 -0.3 -0.25


5.8

5.6

5.4

5.2

5.0

4.8

4.6

1.5

1.25

0.75

0.5

0.25


![SchusterThesis.pdf-176-0.png](SchusterThesis.pdf-176-0.png)

![SchusterThesis.pdf-176-3.png](SchusterThesis.pdf-176-3.png)

-2.2 -2 -1.8 -1.6

V B (V)

![SchusterThesis.pdf-176-1.png](SchusterThesis.pdf-176-1.png)

![SchusterThesis.pdf-176-2.png](SchusterThesis.pdf-176-2.png)

4.6 4.8 5 5.2 5.4 4.6 4.8 5 5.2 5.4

probe frequency,  RF (GHz) probe frequency,  RF (GHz)


Figure 8.4: a) A transmon qubit has its transition frequency,  a , tuned through the resonator
frequency,  r , and the vacuum Rabi coupling results in an avoided crossing. The transition frequency,
by modulating the Josephson energy E J by applying a small magnetic flux. The color represents
transmission (blue is low, red is high) of a probe beam at  RF . The dashed white curve shows the
transition frequency as a function of  B /  0 , of an uncoupled cavity and qubit ( g = 0). The solid
white line shows the expected transition frequencies from the ground state to first and second excited
states of the strongly coupled cavity-qubit system (with 2 g = 228 MHz). The asymmetry in these
peaks is not well understood and is thought to be due to a parasitic resonance on the circuit board.
b) Transmission spectrum when qubit and cavity are degenerate (=  a   r = 0), showing vacuum
Rabi mode splitting. c) Transmission spectrum for cavity-qubit system when = 550 MHz > g.
The larger peak is mostly cavity while the smaller peak is mostly qubit with only a little bit of
photon character (hence the smaller amplitude). The widths of the two lines are  = 42 . 9 MHz for
the larger one, and  =  +   = 2 . 5 MHz + 1 . 85 MHz 4 MHz. The qubit-like state is slightly
 
broader on the low frequency side of the cavity because its E J /E C ratio is smaller making it more
sensitive to charge noise.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 175

of the cavity, with / 2  = 43 MHz. Because the cavity decay rate is much greater than the rate

( / 2  = 2 . 5 MHz) at which the qubit decays 1 , nearly all of the excitations should decay as photons.

To ensure that all photons are emitted into the amplifier, the cavity was made asymmetric, with

much larger coupling to the output side than the input side.

In comparing the resonant case (see Fig. 8.4b), having = 0, to the dispersive case (see

Fig. 8.4b), with = 550 MHz > g, one can immediately see that the (larger) peaks are nearly

the same size, in both cases indicating that few of the photons are being absorbed or scattered

significantly by the qubit. Unfortunately, one also immediately notices that as in the degenerate

case (see Fig. 8.4b) the two peaks are asymmetric. While the exact cause of this is unknown, it

is thought to be due to a low Q parasitic resonance, which gives some frequency structure on the

200 MHz scale of the vacuum Rabi splitting. The amplitude difference in the dispersive trace (see

Fig. 8.4c) is not an artifact, but is actually a direct observation of the Purcell effect [Purcell1946].

The large peak (right) is the state which is mostly cavity and thus easily visible. The small state

(left) is the qubit, normally invisible to direct detection, but it can be seen because it acquires a

small photonic component. Because the dipole coupling, g  , and the cavity decay rate,  , is so

large compared to  , the indirect decay through the cavity   = ( g/ ) 2  becomes the dominant


decay mechanism, even though g/   1 / 5. The qubit excitations are emitted into the output line

and fed to our amplifier where they contribute to the spectrum. This effect will be the basis for an

on-demand single photon generator.

One good way to quantify the wavefunction overlap between the qubit and cavity is to look at

the peak widths. When the state is qubit-like the linewidth should approach  , while the linewidth

of cavity-like states should approach  . The peak information is extracted by fitting a lorentzian to a

small region around the modeled peak locations in figure 8.4a for each branch. The level separation

and peak widths are plotted in figure 8.5. The minimum level separation gives the vacuum Rabi

splitting (2 g = 228 MHz), for a strong coupling ratio 4 g/ (  +  ) = 10. The peak widths can

be examined closely in figure 8.5b, and show the qualitatively correct behavior. There is some

asymmetry in the widths as well as the amplitudes and this may also be due to the same parasitic

resonance, either directly or indirectly due to small amplitude induced errors in the fit.

It is also interesting to look at the vacuum Rabi splitting as a function of input power (see

![SchusterThesis.pdf-177-0.png](SchusterThesis.pdf-177-0.png)

1 The linewidth is a conservative measure of the decay rate, as it is also affected by dephasing. In fits to time
domain data (see Fig. 9.8) it is likely that the actual non-radiative decay rate is closer to   = 200 kHz corresponding
to T 1  800 ns.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 176



50

40

30

20

10


600


500

400

300

200

100


![SchusterThesis.pdf-178-0.png](SchusterThesis.pdf-178-0.png)

![SchusterThesis.pdf-178-1.png](SchusterThesis.pdf-178-1.png)

 400  200 0 200 400 600

bare detuning, = a  r (MHz)


 400  200 0 200 400 600

detuning, = a  r (MHz)


Figure 8.5: Level separation (solid green) between first and second excited states of joint cavityqubit system. a) The minimum level separation is a direct measure of the vacuum Rabi splitting
2 g = 228 MHz. Below on the same scale, are the linewidths of the first (blue) and second (red)
excited states, as a function of the bare detuning . b) is shows the linewidths of the first (blue
triangles) and second (red circles) excited states as a function of detuning. The width gives an
indication of the amount of wavefunction overlap, with small linewidth indicating the excitation is
mostly qubit, and large linewidth indicating mostly cavity.


n RF  10 -4 n RF  4 x 10 -3 n RF  6.3 x 10 -3 n RF  10 -2


100


100

60

20


35

25

15

5

175

125

75

25


60

20


100

60

20


![SchusterThesis.pdf-178-2.png](SchusterThesis.pdf-178-2.png)

![SchusterThesis.pdf-178-3.png](SchusterThesis.pdf-178-3.png)

![SchusterThesis.pdf-178-4.png](SchusterThesis.pdf-178-4.png)

![SchusterThesis.pdf-178-5.png](SchusterThesis.pdf-178-5.png)

n RF  1.6 x 10 -2 n RF  4 x 10 -2 n RF  6.3 x 10 -2 n RF  10 -1


500


700


300

100


500

300

100


800
600
400
200


![SchusterThesis.pdf-178-6.png](SchusterThesis.pdf-178-6.png)

![SchusterThesis.pdf-178-7.png](SchusterThesis.pdf-178-7.png)

![SchusterThesis.pdf-178-8.png](SchusterThesis.pdf-178-8.png)

![SchusterThesis.pdf-178-9.png](SchusterThesis.pdf-178-9.png)

5.2 5.4


5.2 5.4


5.2 5.4


5.2 5.4


probe frequency,  RF (GHz)

Figure 8.6: Plots of the transmission spectrum at = 0 at different drive powers. The powers
are referenced to the output and displayed in terms of n RF given by the relation P RF =   r n RF  .
They should not be confused with the actual photon occupation of the cavity which can be much
smaller or larger depending on the probe frequency  RF . At low powers the vacuum Rabi splitting
splitting is clearly visible. At higher powers inherited non-linearity from the qubit causes the peaks
to become inhomogenously broadened. At intermediate powers additional bumps in the spectrum
are suggestive of multiphoton transitions to higher excited states.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 177

Fig. 8.6). The first thing one notices is that, unlike a harmonic oscillator, the peaks are inhomo-

geneously broadened with power. This is consistent with a harmonic oscillator coupled to a highly

non-linear system, like a qubit, and is further evidence that this is not simply the avoided crossing

of two harmonic oscillators. Also note that this non-linearity sets in at what seem to be very small

photon numbers, but due to the non-linear nature of the cavity-qubit system, even small drives can

quickly saturate the system. In the range of 4  6  10  3 photons, there is a small bump inside

the main peaks, suggestive of multiphoton transitions to the next excitation manifold which is split


![SchusterThesis.pdf-179-0.png](SchusterThesis.pdf-179-0.png)

by 2


2 g . Quantitative predictions were not made for this sample due to the inability to model


the asymmetry properly and also because while this data is suggestive, it is not clean enough to be

definitive. Further experiments might understand this better, using a slightly higher Q resonator

perhaps with   5  10 MHz and a similar (or ideally better) qubit. To see the higher levels, one

could also use an additional tone to populate the first excited state, and then measure transitions

from that to the two excitation manifold. This was attempted briefly but without much initial

success, in the same sample.

####### 8.2 ####### Dispersive Weak Limit

In this section we will discuss experiments in the dispersive limit, where the qubit is detuned from

the cavity by much more than the vacuum Rabi frequency (  g ). The focus will be to study

the effect of the cavity photons on the qubit. We will study the AC Stark effect and show how it

is responsible for the measurement backaction. After explaining this backaction using both a first

order model, and adding non-linear corrections, we demonstrate a technique to AC Stark shift the

qubit transition frequency without any dephasing. Such a tool could in principle allow the creation

of a phase gate, or be used to move the qubit in or out of resonance with the cavity or another

qubit. The resonant limit reveals the qubit-photon coupling very directly, but because the qubit and

cavity are so strongly coupled, it is difficult to work them independently at small detunings. In the

section on sidebands, we hope to regain the ability to make joint transitions, but with the coupling

controlled by an RF tone, which can be switched on or off at gigahertz speeds.

######### 8.2.1 ######### AC Stark Effect

In the chapter 7 on characterization, we saw the effect on the cavity of having a qubit inside. In

this section, the effect of the cavity photons on the qubit will be explored. The Jaynes-Cummings


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 178

a) b) c)


 5

 10

 15

 20

 25

 30


50

40

30

20

10


100

25



![SchusterThesis.pdf-180-3.png](SchusterThesis.pdf-180-3.png)

![SchusterThesis.pdf-180-0.png](SchusterThesis.pdf-180-0.png)

![SchusterThesis.pdf-180-1.png](SchusterThesis.pdf-180-1.png)

![SchusterThesis.pdf-180-2.png](SchusterThesis.pdf-180-2.png)

6.14 6.18 6.22 6.26

spec frequency,  s (GHz)


6.14 6.16 6.18


6.14 6.16 6.18


frequency,  s (GHz)


Figure 8.7: a) Density plot showing transmitted phase shift (dark is negative, white is positive) as
function of spectroscopy frequency,  s , and measurement drive power, P RF . The dip corresponding
to the qubit transition frequency is AC Stark shifted as the power is increased. Discontinuities are
due to phase delays when switching attenuators, and are not due to the physics of the system. b)
Slice at n RF 1 and fits. The dephasing rate is given by the linwidth,  HWHM . c) A slice at

n RF 20, which is AC stark shifted by 12 MHz. It is also significantly broadened when compared

to the n RF = 1 lineshape. At low intracavity photon numbers the lineshape is predicted to be
Lorentzian while at high photon numbers it should be Gaussian. In both plots the red is a fit to
a Lorentzian lineshape, while the orange is a fit to a gaussian, and the solid is expected to be the
correct choice. The Lorentzian to Gaussian crossover is certainly noticeable in these two plots.

Hamiltonian in the dispersive limit is as derived in chapter 2,




H   r a  a + 1 / 2 +
 2



2 g 2
 a + a  a + g

![SchusterThesis.pdf-180-5.png](SchusterThesis.pdf-180-5.png)

![SchusterThesis.pdf-180-6.png](SchusterThesis.pdf-180-6.png)

 



2 g 2
 a +


 z (8.1)


![SchusterThesis.pdf-180-4.png](SchusterThesis.pdf-180-4.png)

The quantity  a  =  a + 2  g 2


 g 2 a  a + g  2


 can be interpreted as the dressed frequency of the qubit,


![SchusterThesis.pdf-180-7.png](SchusterThesis.pdf-180-7.png)

![SchusterThesis.pdf-180-8.png](SchusterThesis.pdf-180-8.png)

which is shifted by 2   2 g 2 / per photon in the cavity. By changing the power of the measurement,

we can easily vary the average number of photons n =  a  a  . Figure 8.7 shows spectroscopy of the

![SchusterThesis.pdf-180-9.png](SchusterThesis.pdf-180-9.png)

qubit at different RF powers. Two effects are immediately noticeable. The qubit response peak can

be shifted by many linewidths, and it also gets much broader.

First, let us investigate the mean behavior. For the powers shown in figure 8.8a, the Stark shift

is proportional to the input power. Because the vacuum Rabi coupling g/ 2  = 6 MHz is known, and

the can be determined from the y-intercept of the figure 8.8a, one can calculate the Stark shift

per photon to be 2  = 2 g 2 / = 2  0 . 6 MHz. That means that the Stark shift per photon is almost

as large as the qubit linewidth   2 . The Stark shift per photon, 2  also corresponds to the slope


of the line in figure 8.8a. This provides a calibration for the power of a single photon, which in


this case is P RF ( n = 1) = 29 dBm with the 63 dB and 40 dB of cold and warm attenuation, giving


![SchusterThesis.pdf-180-10.png](SchusterThesis.pdf-180-10.png)

an input power at the resonator of  5  10  17 W which is within a few dB of predictions based


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 179


6.2

6.19

6.18

6.17

6.16

6.15


25 50 75

![SchusterThesis.pdf-181-1.png](SchusterThesis.pdf-181-1.png)

100


50

25


![SchusterThesis.pdf-181-0.png](SchusterThesis.pdf-181-0.png)

25 50 75


20

40

60
80
100


probe power, P RF (  W) photon number, n

Figure 8.8: a) Measured qubit level separation  a and fit (solid line) vs. input microwave probe
power P RF . The ac-stark shift and the intra-resonator photon number n extracted from the fit
are also indicated. b) Measurement broadened qubit line width   HWHM vs. n RF . Error bars are
reflecting estimated systematic uncertainties in the extracted line width. The corresponding total
dephasing time T  = 1 / 2  HWHM is also indicated. The solid line is obtained from Eq. 8.3 with a
spectroscopy power broadened T 2  80 ns.



on explicit attenuations. The remaining is likely due to reflections from connectors and launching

onto the circuit board. This method is used to calibrate the power in terms of intra-cavity photon

number in each experiment.

If figure 8.8a describes the mean behavior of cavity photons, then figure 8.8b gives insight into

the photon quantum fluctuations  n about that mean. When we drive the cavity, we use a coherent

signal, which does not create a photon number state in the cavity. Rather, it creates a Poisson

distribution of photons, which have fluctuations of order  n . These fluctuations in photon number

![SchusterThesis.pdf-181-2.png](SchusterThesis.pdf-181-2.png)

translate into fluctuations in the qubit precession frequency. One can make this notion quantitative,

by defining the phase accumulated due to the AC Stark effect as,



2 g 2
 ( t ) =

![SchusterThesis.pdf-181-3.png](SchusterThesis.pdf-181-3.png)

 a ,


0





2 g
 ( t ) =


dt  n ( t  ) (8.2)


The linewidth which can be thought of as a dephasing rate, is thus related to the correlator of

photon number  n ( t ) n (0)  . If the Stark shift per photon is not too large (  <  ) then one can

make a gaussian approximation [Gambetta2006] yielding the absorption spectrum



1
S  (  ) =

![SchusterThesis.pdf-181-4.png](SchusterThesis.pdf-181-4.png)

2 



1
S  (  ) =


( 2   m



  m )


1 2  


![SchusterThesis.pdf-181-5.png](SchusterThesis.pdf-181-5.png)

![SchusterThesis.pdf-181-7.png](SchusterThesis.pdf-181-7.png)

2 2 (8.3)

![SchusterThesis.pdf-181-8.png](SchusterThesis.pdf-181-8.png)

(    a 2 n ) 2 + 1 2   j
 
 


![SchusterThesis.pdf-181-6.png](SchusterThesis.pdf-181-6.png)

j


![SchusterThesis.pdf-181-9.png](SchusterThesis.pdf-181-9.png)

![SchusterThesis.pdf-181-10.png](SchusterThesis.pdf-181-10.png)

where   j = 2(  2 +   m ) + j . The spectroscopic line shape is given by a sum of Lorentzians, all


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 180


a) b) c)


400

300

200

100


120


100

80

60

40

20


0.2

0

-0.2


![SchusterThesis.pdf-182-0.png](SchusterThesis.pdf-182-0.png)

![SchusterThesis.pdf-182-1.png](SchusterThesis.pdf-182-1.png)

![SchusterThesis.pdf-182-2.png](SchusterThesis.pdf-182-2.png)

50 100 150 200


50 100 150 200


50 100 150 200 250

probe power, P RF (  W)


photon number, n photon number, n


50 100 150 200 250


Figure 8.9: a) solid, red curve: ac-Stark shift as a function of the average intra-cavity photon number
using the lowest order dispersive approximation. Dashed, blue curve: ac-Stark shift as a function
of photon number calculated from the exact eigenvalues of the Jaynes-Cummings Hamiltonian. b)
Cavity pull as a function of average photon number n . The red solid line is the result of the

![SchusterThesis.pdf-182-3.png](SchusterThesis.pdf-182-3.png)
dispersive approximation (   ) while the dashed blue curve is obtained from the exact eigenvalues
of the Jaynes-Cummings model. textbfc) Average photon number as a function of input power. The
full red line is the result of the lowest order dispersive dispersive approximation 8.4 fit to the data in
(b) at low power. The dotted green line is the non-linear model with  replaced by  ( n ) in 8.4 The

![SchusterThesis.pdf-182-4.png](SchusterThesis.pdf-182-4.png)
vertical line in all plots indicates the critical photon number n crit =  2 / 4 g 2 which indicates the scale
at which the lowest order dispersive approximation breaks down. For the experimental parameters
n crit 82 which corresponds (within the lowest order dispersive approximation) to P RF 110  W
 15 
corresponding to about 10  W at the input of the resonator .

centered on the ac-Stark shifted qubit transition but of different widths and weights. From Eq. 8.3

we see that if the measurement rate   m is much smaller than the cavity decay rate / 2, then only a

few terms in the sum contribute and the spectrum is Lorentzian, with width   m 2 n 0 2 where  0 =


![SchusterThesis.pdf-182-5.png](SchusterThesis.pdf-182-5.png)

2 / = 2 g 2 /   the ground-excited state phase shift. On the other hand, when the measurement

rate is fast compared to the cavity damping, the spectrum will be a sum of many Lorentzians,

resulting in a gaussian profile, with a standard deviation  =  n 0 . In this situation, dephasing

![SchusterThesis.pdf-182-6.png](SchusterThesis.pdf-182-6.png)

occurs before the cavity has had time to significantly change its state, leading to inhomogeneous

broadening. This Lorentzian to Gaussian crossover is evident in figures 8.7b-c.

The expression 8.3 for the spectrum can be summed analytically but yields an unsightly result

which is not reproduced here. To compare with the experimental results, we evaluate numerically

the half-width at half maximum from S (  ). The results are plotted as a function of probe power in

figure 8.8 (red line). The agreement with the experimental results (symbols) is good, especially given

that there are no adjustable parameters apart from  2 which only sets the value of the dephasing at

n = 0.

![SchusterThesis.pdf-182-7.png](SchusterThesis.pdf-182-7.png)

The measured AC-Stark shift is remarkably linear. While one expects linearity at low powers,


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 181

there should be some non-linearity due to higher order corrections to the simple dispersive Hamilto-

nian of Eq. 8.1. In this case, the apparent linearity masks competing non-linear effects. In the lowest

order dispersive approximation (Eq. 8.1), the predicted ac-Stark shift  AC = 2 n will be a linear

![SchusterThesis.pdf-183-0.png](SchusterThesis.pdf-183-0.png)

function of the mean photon number, n . However, this approximation only holds at low photon num-

![SchusterThesis.pdf-183-1.png](SchusterThesis.pdf-183-1.png)

bers, and breaks down on a scale given by the critical photon number n crit =  2 / 4 g 2 [Blais2004].

This is illustrated in Fig. 8.9a where the ac-Stark shift, calculated from the lowest order dispersive

approximation (red solid line) and the exact eigenvalues (blue dashed line) of the Jaynes-Cummings

model [Blais2004] are plotted for the experimental parameters. Also shown in this figure is n crit

(vertical blue line) which for the experimental parameters is about 82 photons. Here we see that

as n increases, the exact Stark shift begins to fall below the lowest order dispersive approximation

![SchusterThesis.pdf-183-2.png](SchusterThesis.pdf-183-2.png)

even before n reaches n crit .

![SchusterThesis.pdf-183-3.png](SchusterThesis.pdf-183-3.png)

In Fig. 8.9b, the experimental results (solid blue points) are plotted as a function of probe power,

P RF (extending up to powers larger than those presented in Fig. 8.8). To convert between n and

![SchusterThesis.pdf-183-4.png](SchusterThesis.pdf-183-4.png)

P RF , we assume that P RF =    RF p where p is the photon flux at the resonator and  is a scaling

factor that takes into account the large attenuation that is placed between the probe generator and

the resonator (to eliminate black body radiation). From the lowest order dispersive approximation,

the average photon number when driving the cavity at  r = 0 is


p/ 2
n  = (8.4)

( / 2) 2 +  2 .

![SchusterThesis.pdf-183-5.png](SchusterThesis.pdf-183-5.png)

By using the lowest order dispersive approximation for the ac-Stark shift and the line of best fit to

the experimental points (in the linear regime at low power),  can be determined. Doing this gives

the red solid line in Figs. 8.9b and d. The calibration shows that n crit occurs at  110  W. The

experimental results clearly show the breakdown of the lowest order dispersive approximation. The

data points fall below the linear prediction, but not nearly as much as the blue dashed curve in (a)

predicts. In fact, the data points follow fairly closely the linear in n dependence of the lowest order

![SchusterThesis.pdf-183-6.png](SchusterThesis.pdf-183-6.png)

dispersive approximation in 8.1 for larger powers than expected (up to and well above n crit ).

It is possible to understand why the experiment agrees with the simple dispersive approximation

for larger probe powers than expected by considering the following simple model. We assume that,

at these large powers, the ac-Stark shift is still given by the dispersive approximation 2 n , but we

![SchusterThesis.pdf-183-7.png](SchusterThesis.pdf-183-7.png)

now take into account the non-linear cavity pull (which is  at low n ). From the eigenvalues of the

![SchusterThesis.pdf-183-8.png](SchusterThesis.pdf-183-8.png)

Jaynes-Cummings Hamiltonian the cavity pull can be calculated as a function of n . This is shown


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 182

in Fig. 8.9b. From this figure, we see that the cavity pull reduces as the number of photons in

the resonator is increased. We thus replace  by  ( n ). The second aspect of our simple model is

![SchusterThesis.pdf-184-0.png](SchusterThesis.pdf-184-0.png)

the non-linear dependence of the average photon number n with input power P due to the power-

![SchusterThesis.pdf-184-1.png](SchusterThesis.pdf-184-1.png)

dependence of the cavity frequency. To account for this we simply replace  in Eq. 8.4 with  ( n )

and n becomes a non-linear function of input power. This non-linear dependence of the photon

![SchusterThesis.pdf-184-2.png](SchusterThesis.pdf-184-2.png)

number on the input power is illustrated in Fig. 8.9c as the green dotted line. This is a precursor

to bistability in this system [Walls2006]. Using these two expressions, we have for our simple model

of the non-linear ac-Stark shift 2  ( P ) n ( P ). This expression is plotted in Fig. 8.10a (green dotted

![SchusterThesis.pdf-184-3.png](SchusterThesis.pdf-184-3.png)

line) with a new scaling factor    0 . 905  calculated by the best fit for the experimental data (here

we use the complete data set). This simple model produces a result that is linear for a larger range

of powers and is closely consistent with the experimental results. It happens that for the particular

experimental parameters, the two non-linear effects almost cancel each other out and result in the

green dotted line being more linear than expected. Comparison with the results of the non-linear

model shown here in Fig. 8.9c, shows that the calibration of the cavity photon number in terms

of the drive power is low by approximately 50% at the highest power, for the simple linear model

used in Fig. 8.8. It should be emphasized that the treatment here of the non-linearities is only

approximate.

######### 8.2.2 ######### Off-Resonant AC Stark Effect

Study of the AC-Stark effect, created by measurement photons in the cavity, elucidates the role of

photon number fluctuations in dephasing the qubit. The ability to manipulate the qubit transition

frequency by application of an RF tone could be very useful in the construction of conditional phase

gates. When resonant cavity photons are used to measure the qubit state, corresponding qubit

dephasing is demanded by the uncertainty principle. So in order to make a coherent gate one must

use a tone which does not measure the qubit state (and can thus avoid dephasing it). If the Stark

shifting tone at  AC , is applied at a detuning from the resonator,  AC =  AC   r , that is much

larger than the state-dependent cavity pull, 2   2 g 2 / , then it will not reveal much information

about the qubit state, and also not cause much dephasing. Quantitatively, the information leakage


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 183


a) b)


12

10


120

100

80

60

40

20


![SchusterThesis.pdf-185-0.png](SchusterThesis.pdf-185-0.png)

![SchusterThesis.pdf-185-1.png](SchusterThesis.pdf-185-1.png)

50 100 150 200 250


50 100 150 200 250


probe power, P RF (  W) probe power, P RF (  W)

Figure 8.10: a) AC Stark shift as function of input power P RF . Includes points past n crit 110  W

(indicated by vertical blue line) with fits to the simple dispersive approximation (solid red line) and
a model which includes non-linearity of the photon number in input power as well as the reduction
in Stark shift per photon at high photon numbers. Blue dots: experimentally measured ac-Stark
shift as a function of external microwave input power. The conversion factor from photon number
to external microwave drive power was determined by fitting the red curve to the linear portion of
the data at low power. Green, dotted curve: Same as red but taking into account the non-linear
reduction in the cavity pull (see Fig. 8.9b) and the non-linear increase in the average photon number
(see Fig. 8.9c) with microwave drive power. For the particular experimental parameters these two
effects almost cancel each other out and result in the green dotted line being nearly linear out to
much greater input powers than expected. b) Measurement broadened qubit line width  HWHM as a
function of the input measurement power or average photon number as predicted by the lowest order
dispersive approximation (solid red). Dispersive prediction with a non-linear reduction in the cavity
pull and plotted as a function of input power (dotted green). The symbols are the experimental
results. Symbols and color scheme are described in the text. The vertical line indicates the critical
photon number n crit . The blue dashed line is the calculated HWHM for  R / 2  = 32 MHz. It clearly
shows that measurement induced dephasing is small at large  R where information about the state
of the qubit in the transmitted signal is also small and should be compared with the experimental
measurement in Fig. 8.13.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 184


|C|Col2|
|---|---|


||Col2|
|---|---|


|bias tee microwave drives amp. circulator mixer Cin Cout|Col2|amp. mixer|Col4|
|---|---|---|---|
|RF IF Cg LO   V  F AC s g  LO V L C C ,E J J||RF IF||
||Cg LO   LO C ,E J J|||
|| C ,E J J|||


| AC| s|V g|Col4|Col5|
|---|---|---|---|---|


Figure 8.11: The qubit is measured via the digital homodyne technique, using a weak tone  RF , at
the cavity frequency, and comparing it to a local oscillator  LO . A spectroscopy tone at  s is used
to interrogate the qubit state and transition frequency. In addition a new tone at  AC is applied
at a small detuning from the cavity  AC , to modify the qubit transition frequency, or help excite
sideband transitions.

rate due to the Stark photons is given by Eq. 3.93, which is approximately 1


2 n 2 

![SchusterThesis.pdf-186-0.png](SchusterThesis.pdf-186-0.png)
 m =  AC 2 + (  ) 2 / 4 +  2 (8.5)

![SchusterThesis.pdf-186-1.png](SchusterThesis.pdf-186-1.png)

For given experimental parameters the Stark shift is given by 2 n . Therefore we can define a

![SchusterThesis.pdf-186-2.png](SchusterThesis.pdf-186-2.png)

dimensionless Stark dephasing factor


n =  AC 2 +  2 / 4 +  2

![SchusterThesis.pdf-186-3.png](SchusterThesis.pdf-186-3.png)

![SchusterThesis.pdf-186-4.png](SchusterThesis.pdf-186-4.png)

![SchusterThesis.pdf-186-5.png](SchusterThesis.pdf-186-5.png)

 m 


2 n


(8.6)



By using a suitably large detuning this can be approximated as  AC 2 / , which can be made quite

large. Adjusting the amplitude accordingly it is possible to get a large AC Stark shift without any

noticeable dephasing. By setting  AC 0 in Eq. 8.5, we can recover the earlier (weak measurement)


result, / 4  = 1 / 2  0 . To perform such experiments, we use a weak measurement tone at the

resonator frequency as a probe, while adding an additional generator to produce the AC Stark tone

(see Fig. 8.11). The Stark tone detuning is chosen such that it is large enough to not dephase

the qubit substantially, while also not filtered so strongly that the input power required heats the

cryostat (see Fig. 8.12).

To observe the off-resonant Stark effect, one performs the same types of experiments, but in place

of the RF measurement power, P RF , one sweeps the AC-Stark power, P AC as shown in figure 8.13.

When one can compares figure 8.13 with figure 8.7, one immediately sees that for an even larger

![SchusterThesis.pdf-186-6.png](SchusterThesis.pdf-186-6.png)

1 In Eq. 3.93  m is written in terms of n + and n  which are the average photon numbers in the ground or excited
state. Since for the large detunings  AC   or very small detunings  AC   n  n +  n  we use n + + n   2 n

![SchusterThesis.pdf-186-7.png](SchusterThesis.pdf-186-7.png)

![SchusterThesis.pdf-186-8.png](SchusterThesis.pdf-186-8.png)
for simplicity.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 185


a) b)

detuning,  r  rf (MHz)

50 0 350

0

 10


detuning,  r  rf (MHz)

 3  2  1 0 1 2 3


 5

 10

 15

 20


 20

 30

 40

 50



| r  ac|Col2|Col3|
|---|---|---|
|| a||
||||

|Col1|Col2|
|---|---|
| r||


5.5 5.6 5.7 5.8 5.9

frequency,  rf (GHz)


 25

5.53318

frequency,  rf (GHz)


Figure 8.12: a) Calculated lorentzian cavity transmission spectrum over large frequency range.
The cavity drives at frequencies  s   a ,  RF   r and  AC and the cavity transmission at these
frequencies are indicated. b) Measured cavity spectrum (dots) and lorentzian fit (line) around cavity
resonance frequency.

Stark shift (32 MHz vs. 12 MHz) the linewidth remains essentially unchanged. By fitting the peaks

as a function of P AC we can extract the dressed transition frequency and linewidth (see Fig. 8.14).

This shows that the line can be shifted by many linewidths without any significant broadening,

meaning that it could be used to create a coherent phase gate.

######### 8.2.3 ######### Sideband Experiments

In the resonant limit, the cavity-qubit coupling directly manifests itself in the form of vacuum Rabi

splitting, which naturally creates coherent oscillations between a qubit excitation and a photon.

Unfortunately, it can be difficult to control these oscillations 1 . In the dispersive limit, the system

exists as an independent qubit and cavity, with state-dependent dressed states, rather than real

transitions as evidence of their interaction. The ability of cavity QED to convert a qubit excitation

into a cavity photon, spontaneous in the resonant case, requires stimulation in the dispersive regime.

One natural way of driving a qubit-photon transition, is to exploit the state-dependence of the qubit

and cavity frequencies, using energy conservation to make a simultaneous change of qubit state and

photon number. Such sideband transitions allow one to switch the qubit-cavity coupling on and off

using an RF pulse. This can be done with very high contrast and on nanosecond timescales.


More concretely, imagine applying an RF tone at  red =  a   r , which would drive a transition

![SchusterThesis.pdf-187-0.png](SchusterThesis.pdf-187-0.png)

1 This is mainly due to our current experimental configuration which has heavily low-passed ( < 5 MHz) electrostatic
gates, and extremely (unintentional) strong magnetic low passing ( < 1 Hz) due to inductive shielding of the very high
conductivity OFHC copper sample holder. Fast flux control will be added in future experiments, which will make
control substantially easier by tuning the qubit transition frequency on timescales comparable to the vacuum Rabi
coupling rate.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 186


a) b) P AC = 10  W c)


50


P AC = 10  W c) P AC = 610  W


800

600

400

200


40

30

20

10


![SchusterThesis.pdf-188-5.png](SchusterThesis.pdf-188-5.png)

![SchusterThesis.pdf-188-0.png](SchusterThesis.pdf-188-0.png)

![SchusterThesis.pdf-188-1.png](SchusterThesis.pdf-188-1.png)

![SchusterThesis.pdf-188-2.png](SchusterThesis.pdf-188-2.png)

6.02 6.04 6.06 6.08 6.02 6.05 6.08 6.02 6.05 6.08

spectroscopy frequency,  s (GHz) spectroscopy frequency,  s (GHz)


6.02 6.04 6.06 6.08 6.02 6.05 6.08 6.02 6.05 6.08


Figure 8.13: a) Density plot of spectroscopy taken as a function of the power of the AC stark tone,
 AC . The tone is detuned by  AC =  AC   r =  50 MHz, and so does not excite any real photons
in the cavity. b) Slice taken at P AC = 10  W, where the AC Stark shift shift is negligible. The
linewidth is due to power broadening by the spectroscopy tone and the intrinsic qubit dephasing. c)
Slice taken at P AC = 610  W, showing that the qubit transition has been shifted by  a   a = 32 MHz,


without significant broadening.


40


50.


6.07

6.06

6.05

6.04



20


1.5


100.


![SchusterThesis.pdf-188-3.png](SchusterThesis.pdf-188-3.png)

![SchusterThesis.pdf-188-4.png](SchusterThesis.pdf-188-4.png)

350 700


300.

350 700


AC Stark power, P AC (  W) AC Stark power, P AC (  W)

Figure 8.14: a) Plot of the AC-Stark shift as function of Stark tone power P AC . The qubit transition
frequency is shifted by more than 30 linewidths. b) Plot of linewidths/ T 2 , which essentially do not
change in the experimental power range. The linewidth is limited by the intrinsic dephasing rate
and power broadening due to the spectroscopy tone.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 187

########## a) ########## b)


######### 


#########  ######### blue #########  ######### a #########  ######### ac





![SchusterThesis.pdf-189-0.png](SchusterThesis.pdf-189-0.png)

![SchusterThesis.pdf-189-1.png](SchusterThesis.pdf-189-1.png)

Figure 8.15: Qubit-cavity energy levels illustrating sideband transitions. a) Illustration of direct
sideband transitions from | g, 0 | e, 1  at  blue =  a +  r and from | g, 1 | e, 0  at  red =  a   r .
b) At the CPB charge degeneracy point ( n g = 1) where the qubit is most coherent, direct sideband
transitions are forbidden by a parity selection rule. Sidebands transitions can still be driven by using
two tones, at  AC and  s . Two-photon transitions can occur when the sum (  AC +  s =  blue ) or
difference (  AC +  s =  red ) of these tones satisfies energy conservation.

between | e, n  1  and | g, n  , effectively converting a qubit excitation into a photon (see Fig. 8.15).

Energy conservation demands that the photon number and qubit state are changed simultaneously.

Similarly driving at  blue =  a   r , one can couple | g, n  and | e, n + 1  , which adds or subtracts a

photon and a qubit excitation. These transitions are particularly special when the system starts in

the ground state, | g, 0  . In that case, only the blue sideband is allowed, as there is no state, | e,  1  ,

that would satisfy energy conservation. Similarly, when the system starts in the | e, 0  state, only the

red sideband is allowed, as there is no | g,  1  state with which the blue sideband can couple. These

dark states can act as the basis of quantum SWAP gate between a qubit and photon, using the

following protocol. Assume the cavity is empty to start, then apply a  strength pulse on the red

sideband. If the qubit is in the ground state, nothing will happen since a transition would require

absorption of a photon which is not present (see 8.15). While the SWAP is a classical gate, using a


![SchusterThesis.pdf-189-2.png](SchusterThesis.pdf-189-2.png)

/ 2 pulse would create the entangled state, ( | e, n  1  + | g, n  ) /


2 and could be used as the basis


for universal quantum logic. Even the classical swap gate would allow the teleportation of a state

between two qubits present in the cavity. This could be accomplished, by first swapping a qubit

possessing an unknown quantum state into a photon. Then the other qubit, initialized to the ground

state, could be swapped with the cavity photon (superposition) state, restoring the qubit in the new

location. In a standard cavity, this could be done over distances  1 cm.

Unfortunately, at the charge degeneracy point, n g = 1, there is a parity selection rule that does


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 188


70

60

50

40

30

20

10

0

![SchusterThesis.pdf-190-1.png](SchusterThesis.pdf-190-1.png)

5.75 5.8 5.85 5.9 5.95 6

spec. frequency,  s (GHz)



5.95

5.9

5.85

5.8

5.75


![SchusterThesis.pdf-190-2.png](SchusterThesis.pdf-190-2.png)

![SchusterThesis.pdf-190-0.png](SchusterThesis.pdf-190-0.png)

5.46 5.47 5.48 5.49 5.5

AC Stark tone frequency,  AC (GHz)


Figure 8.16: a) Density plot showing the spectrum near the qubit transition frequency,  a as a
function of the (off-resonant) AC Stark tone frequency and spectroscopy frequency (at P AC =  20 dB
and P s =  14 dB). The central line is the Stark shifted bare qubit transition. Also present are blue
and red sidebands which result in a simultaneous change of the qubit state and the addition or
subtraction of a photon from the cavity. b) A line cut of the spectroscopy near the qubit transition
frequency,  a , at  AC = 50 MHz. The sidebands are clearly visible.

not allow direct transitions involving an even number of energy quanta. Because of this it is not

possible to do single tone sidebands as can be done with a flux qubit[Chiorescu2004]. However, two

photon transitions are not forbidden and can be exploited to the same end. Nominally any two

tones, which together satisfy the condition that  AC +  s =  red / blue or even a single tone at half the

frequency 2  s =  red / blue , can be used to create the sideband (see Fig. 8.15b). The strong filtering

property of the cavity, encourages one to choose the tones such that one tone is relatively close to

the cavity,  AC  r , and the other is near the qubit transition frequency,  s  a . One way to
 

think about this is that, we know we can make transitions in the qubit and cavity with one beam

at  r and the other  a . That is just normal spectroscopy, but in that case because each process is

individually relevant, there are no correlations between the addition of a photon and the flipping of

a qubit. By detuning both beams by  AC , but keeping the difference of the two beams fixed to ,

energy conservation is only satisfied by simultaneous flips (see Fig. 8.15b). Thus the challenge is to

detune as little as possible (to keep the rate high), while detuning by enough (so that there is no

independent absorption).

In this experiment, a qubit with vacuum Rabi coupling strength g/ 2  = 17 MHz, is placed

at one end of a  r / 2  = 5 . 5 GHz resonator with decay rate / 2  = 0 . 5 MHz, at a detuning of

 / 2   350 MHz  g. Figure 8.16b shows spectroscopy near the qubit, while a second tone drives

the cavity at a detuning of  AC =  50 MHz, and clearly shows the sidebands as well as the Stark


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 189

shifted direct qubit transition. This experiment is identical in setup to the off-resonant Stark effect,

but now (using higher powers and larger detunings) we focus on the sidebands, rather than the Stark

shift. The sideband spectroscopy is a line cut taken from the density plot of cavity transmission

in response to a scan of the two beam frequencies,  s and  AC (see Fig. 8.16a). At the relatively

low powers used in the scan, the sideband detuning is roughly proportional to the AC-Stark tone

detuning  AC . At higher powers or smaller detunings significant non-linearities are present. These

arise due to the Stark shifts, which necessarily accompany the two off-resonant tones at detuning of

 AC and  AC + . The resulting dressed atom frequency is given by


 a  =  a + 2  2 AC


 2 AC + 2  2 s

![SchusterThesis.pdf-191-0.png](SchusterThesis.pdf-191-0.png)

![SchusterThesis.pdf-191-1.png](SchusterThesis.pdf-191-1.png)

 a  AC  a
 


(8.7)
 a  s



which depends on the drive strengths  ac , s (expressed as frequencies) that we parameterize in terms

of their Rabi frequencies


g ac
 AC =


![SchusterThesis.pdf-191-2.png](SchusterThesis.pdf-191-2.png)

g s
 s =


(8.8)
 r  AC
 g


(8.9)

![SchusterThesis.pdf-191-3.png](SchusterThesis.pdf-191-3.png)
 r  s



That means that the correct frequencies for  s must be determined self consistently from the

non-linear equation,

 s =  a   AC (8.10)



The drive amplitudes can be calibrated using the resonant AC-stark effect which gives the power

for a single photon ( n = 1)to be P RF =  28 dBm, corresponding to a power at the input of the

resonator of 1 . 2  10  17 . The cavitys lorentzian line shape then gives


 2
n = (8.11)

 2 + ( / 2) 2 ,

![SchusterThesis.pdf-191-4.png](SchusterThesis.pdf-191-4.png)

where  has units of frequency and is related to the incident photon put power by  2 = P in /   and

the output power is just P out = n   .

Figure 8.17 plots the location of the qubit transition and its sidebands as a function of the

detuning  AC and the power of the two beams. Figure 8.17a shows that the sidebands are nearly

proportional to the detuning but begin to be shifted significantly at small detunings. This is in

some sense an artifact of performing the scan at constant input power, rather than as a function of

cavity occupation. This becomes clear when looking at 8.17b which shows the shift due to changes


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 190


(a) detuning,  AC =  r -  AC (MHz) (b) (c)


80 70 60 50 40 30 20 10

![SchusterThesis.pdf-192-2.png](SchusterThesis.pdf-192-2.png)

5.46 5.48 5.5 5.52


6.05

6

5.95

5.9

5.85

5.8


150

100

50

0

-50


-100


5.975

5.95

5.925

5.9

5.875

5.85

5.825


5.94

5.92

5.90

5.88

5.86

5.84

5.82


![SchusterThesis.pdf-192-0.png](SchusterThesis.pdf-192-0.png)

![SchusterThesis.pdf-192-1.png](SchusterThesis.pdf-192-1.png)

30  25  20  15  10


35  25  15  5


AC-Stark frequency,  ac (GHz) AC-Stark power, P AC (dBm) spec. power, P AC (dBm)

Figure 8.17: a) Two-tone red and blue sidebands (red/blue dots) and fundamental (black dots)
qubit transition frequencies for fixed P s and P AC varying  AC . Lines are fits to Eqs. (8.7-8.11) (b)
For fixed  AC , and varying P AC . (c) For fixed  AC , P AC and varying P s . (a-c) All measurements
are done at fixed measurement frequency  RF =  r and power P RF weakly populating the resonator
with n RF 2 photons.


in amplitude. Finally we can see that  s is self-consistently matching Eq. 8.10, by monitoring the

peak position as a function of the spectroscopy power, P s , in figure 8.17b. The data fits remarkably

well over two orders of magnitude of power in both the tones and to detunings which are nearly

resonant with the cavity.

There were some aspects of the sidebands experiment that were unable to observe that would be

very interesting to study in the future. One issue was the finite width of the direct qubit transition.

Looking at figure 8.16b, one can see that though the sideband is well-resolved, there is some overlap

between the direct transition (which is very power broadened at these amplitudes) and the sideband.

For this reason, we were unable to observe any time domain oscillations associated with the sideband

transitions. In future experiments, this could be addressed by increasing the coupling strength, which

would allow larger detunings and smaller amplitudes. Of course, improving the qubit dephasing time

would help immensely. Reducing the cavity decay rate, which can easily done by at least an order

of magnitude, would allow one to operate at smaller detunings and drive the transition rates higher.

It is also possible that another beam at the direct qubit transition could be used to compensate for

the direct precession. Another interesting phenomena that we were unable to observe conclusively

is the asymmetry of the red and blue sidebands when the system is in its ground state. Though in

the ground state only the blue sideband should be allowed, we observed only a slight asymmetry

between the two sidebands. This was likely due to photons in the cavity from the weak measurement,

or possibly due to direct excitation of the qubit. A pulsed measurement protocol, would allow one


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 191

to eliminate the former possibility and the direct excitation could be reduced by the ways stated

above.

####### 8.3 ####### Dispersive Strong Limit

In the dispersive limit, the cavity and qubit frequencies are shifted by their interaction, which is

characterized by the shift per photon, 2  . In the previous section, the dispersive coupling was

relatively weak compared with the decoherence rates, resulting in a small state-dependent phase

shift (  <  ) of the cavity and small AC Stark shift per photon (  <  ). Despite this, by using

many photons, we were able to make a strong measurement of the qubit state and (equivalently)

AC Stark shift the qubit by many linewidths. In principle, the quantum Stark Hamiltonian (Eq. 8.1

allows one to make a strong measurement of the cavity photon number state, using the qubit as well.

Because there is only a single qubit, a measurement of the exact photon number requires each photon

to shift the qubit by more than one linewidth, and for the number of photons to stay constant during

the measurement,  > ,  . When this additional constraint is met, (and the dispersive condition

  g ) then one enters the strong dispersive regime, the hallmark of which is the ability to measure

the photon number state of the cavity. When the qubit is so strongly coupled to the cavity, the

anharmonic dispersive regime (see Fig. 8.1). The defining characteristic of this regime is that the

second order non-linearity the cavity dispersively inherited from the qubit, leads to single-photon

level anharmonicity, and inhomogeneous power broadening of the cavity.

######### 8.3.1 ######### Photon Number Splitting

In this experiment, we would like to make a quantum non-demolition (QND) measurement of cavity

the photon number state using the AC Stark effect of those photons on the qubit. This measurement

could be performed by driving the atom at its Stark shifted atom frequency  n =  a + 2 n (see

Fig. 8.18a), followed by an independent measurement of the atom state. If the atom is excited, then

the field must have exactly n photons. Because the photon number is not changed in this process,

the QND protocol can be repeated indefinitely. In practice, all measurements have some demolition,

which limits the number of repetitions before the measurement process changes the measured variable

(the number of photons). In our experiment, the cavity transmission is used to measure the atom

state, so while the interaction is QND, the detection performed here is not. Any cavity QED

experiment that employs a fixed coupling, will have demolition arising from the overlap of the atomic


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 192

and photonic wavefunctions, creating a probability, ( g/ ) 2 , that a measurement of photon number

will absorb a photon or a measurement of the atomic state will induce a transition, demolishing

the measured state. If the coupling strength, g , can be changed adiabatically the demolition can be

substantially reduced[Gleyzes2007]. In that work despite having a ratio of g/   1, the demolition

was still  10  4 , but in our current implementation g is fixed, and this limit applies.

In order for this measurement protocol to have single photon resolution, the Stark shift per pho-

ton must be greater than the qubit and cavity lifetimes,  > ,  . It has been proposed that the

dispersive photon shift could be used to make a QND measurement of photon number state of the

cavity using Rydberg atoms [Brune1990]. Previously attainable interaction strengths required pho-

ton number detection experiments to employ absorptive quantum Rabi oscillations in the resonant

regime[Brune1996], allowing a QND measurement [Nogues1999], restricted to distinguishing only

between zero and one photon. More recently, a non-resonant Rydberg atom experiment entered the

strong dispersive limit, measuring the single photon Wigner function with demolition ( g/ ) 2 = 6%,

in principle allowing  15 repeated measurements [Bertet2002]. For the parameters in this experi-

ment, g/ 2  = 105 MHz, and = 1 . 2 GHz it is possible to have a demolition less than ( g/ ) 2 < 1%,

which should allow up to  100 repeated measurements.

The primary innovation that allowed this experiment to succeed was the incredibly large vacuum

Rabi coupling g/ 2  = 105 MHz afforded by the transmon which sees its first realization here. The

dimensionless coupling strength g/ = 2% of the total photon energy. This approaches the fine

structure limit (Eq. 3.79) and is 10 4 times larger than currently attainable in atomic systems, which

allows the system to overcome the larger decoherence present in the solid-state environment. This

experiment was capable of making g/ eff = 40 possible coherent vacuum Rabi oscillations in the

strong resonant regime, where  eff = (  +  ) / 2 is the combined photon-qubit decay rate. The

equivalent comparison, of the dispersive interaction to decoherence, examines the Stark shift per

photon in relation to the qubit decay, 2 / = 6, and determines the resolution of the photon number

peaks. Comparing instead to the cavity lifetime yields an estimate of the maximum number of peaks

that could possibly be resolved, 2 / = 70, and determines the contrast of a qubit measurement by a

single cavity photon. The charge stability of the transmon, though not the focus of this experiment,

is attested to by signal-to-noise ratio in the data (see Fig. 8.19). The experiment would have also

been far more difficult, if not impractical without this stability.

The photon number-dependent frequency shift of the qubit is detected by performing spec-


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 193


a)


b)

 r  a

  2  +  


|n 

|3 

|2 

|1 

|0 


|n

|3

|2

|1

|0


![SchusterThesis.pdf-195-0.png](SchusterThesis.pdf-195-0.png)

![SchusterThesis.pdf-195-1.png](SchusterThesis.pdf-195-1.png)

| **g**  | **e** 


![SchusterThesis.pdf-195-2.png](SchusterThesis.pdf-195-2.png)

Figure 8.18: a) Dispersive cavity-qubit energy levels. Each level is labeled by the qubit state,
| g  or | e  , and photon number | n  . Dashed lines are qubit/cavity energy levels with no interaction
( g = 0), where solid lines show eigenstates dressed by the dispersive interaction. Transitions from
| n | n + 1  show the qubit-dependent cavity shift. Transitions at constant photon number from
g n e n show a photon number dependent frequency shift 2 n eff . b) Cavity-qubit spectral
| | | | 
response. To measure the qubit state and populate the cavity, a coherent tone is driven at  rf
(bottom left), which is blue detuned from the cavity by several linewidths, reducing any cavity
nonlinearity. Thermal fields are generated with gaussian noise applied in the red envelope, spanning
the cavity. The qubit spectrum (bottom right), is detuned from the cavity by  / 2  = 1 . 2 GHz 
g/ 2  . Information about photon number is measured by monitoring transmission at  rf while driving
the qubit with a spectroscopy tone at  s . Each photon shifts the qubit transition by more than a
linewidth ( / 2  > / 2  = 1 . 9 MHz , / 2  = 250 kHz) giving a distinct peak for each photon number
state. The maximum number of resolvable peaks is 2 / .


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 194

troscopy on the qubit-cavity system (Fig. 8.18b). The cavity is coherently excited by applying a

microwave signal (the cavity tone) at frequency (  rf ) near the cavity resonance (Fig. 8.18b). A

spectrum is taken by sweeping the frequency (  s ) of a second microwave signal (the spectroscopy

tone), which probes the qubit absorption, without significantly populating the resonator as it is

detuned by many linewidths (  s  r  ). The detection is completed by exploiting the dual
 

nature of the qubit-photon coupling, reusing the cavity photons as a measure of cavity transmis-

sion, as in Sec. 7.2, to measure the qubit excited state population. The measured transmission

amplitude (Fig. 8.19) is an approximate measure of the actual qubit population, which could in

principle be measured independently. For clarity, the transmission amplitude in Figure 8.19 is plot-

ted from high to low frequency. In order to reduce non-linearities in the response, the cavity tone

was applied at a small detuning from the resonator frequency when the qubit is in the ground

state / 2  = (  rf  r g ) / 2  = 2 MHz which also slightly modifies the peak splitting[Gambetta2006]


(Fig. 8.18b).

The measured spectra reveal the quantized nature of the cavity field, containing a separate peak

for each photon number state (Fig. 8.19)[Gambetta2006, Irish2003]. These peaks approximately

represent the weight of each Fock state in a coherent field with mean photon number n , which is

![SchusterThesis.pdf-196-0.png](SchusterThesis.pdf-196-0.png)

varied from zero to seventeen photons. At the lowest photon powers, nearly all of the weight is

in the first peak, corresponding to no photons in the cavity, and confirming that the background

cavity occupancy is n th < 0 . 1. It is reasonable to wonder how one can measure a zero photon peak

when information is only extracted from the cavity when photons are transmitted. The solution

to this apparent paradox is that the qubit can be excited while the cavity is empty which then

prevents photons from entering. Another interesting feature in Fig. 8.19 at the lowest power is the

dip (representing an overall increase in transmission). While this feature is not well-understood it

appears in both the experiment and numerical simulations, and is thought to be an interference

effect of some sort. As the input power is increased, more photon number peaks can be resolved and

the mean of the distribution shifts proportional to n . The data agree well with numerical solutions

![SchusterThesis.pdf-196-1.png](SchusterThesis.pdf-196-1.png)

at low powers (solid lines in Fig. 8.19) to the Markovian Master equation[Walls2006, Gambetta2006]

with three damping sources, namely the loss of photons at rate / 2  = 250 kHz, energy relaxation

in the qubit at rate  1 / 2  = 1 . 8 MHz and the qubit dephasing rate   / 2  = 1 . 0 MHz. However,

adequate numerical modeling of this strongly coupled system at higher photon numbers is quite

difficult and has not yet been achieved.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 195

|b) |1 |n=0 |2 |3|Coherent |4 |5 |6|
|---|---|


12

|c)|Thermal|
|---|---|


![SchusterThesis.pdf-197-0.png](SchusterThesis.pdf-197-0.png)

6.95 6.85 6.75
Spectroscopy Frequency,  s (GHz)


6.95 6.85 6.75

Spectroscopy Frequency,  s (GHz)


Figure 8.19: Direct spectroscopic observation of quantized cavity photon number. a) Qubit spectra
with coherent cavity drive at different average cavity occupations ( n ). The spectra have resolved

![SchusterThesis.pdf-197-1.png](SchusterThesis.pdf-197-1.png)
peaks corresponding to each photon number. The peaks are separated by 2  eff / 2 
= 17 MHz. Approximately ten peaks are distinguishable. The data (blue) is well described by numerical simulations | |
(red) with all parameters predetermined except for a single frequency offset, overall power scaling,
and background thermal photon number ( n th = 0 . 1) used for all traces. Computational limitations
prevented simulations of photon numbers beyond  3. At the lowest power nearly all of the weight
is in the | 0  peak, meaning that the cavity has a background occupation less than ( n th < 0 . 1).
Peaks broaden as ( n + n ) / 2 plus some additional contributions due to charge noise. At higher

![SchusterThesis.pdf-197-2.png](SchusterThesis.pdf-197-2.png)
powers the peaks blend together and the envelope approaches a gaussian shape for a coherent state.
Since  < 0, spectra are displayed from high to low frequency, and also have been normalized and
offset for clarity. b)
Reduction in transmitted amplitude is plotted as a proxy for qubit absorption for the case of a coherent drive with n = 3 photons. c) Spectrum when cavity is driven with

![SchusterThesis.pdf-197-3.png](SchusterThesis.pdf-197-3.png)
Gaussian white noise approximating a thermal state also with n = 3. The coherent spectrum is

![SchusterThesis.pdf-197-4.png](SchusterThesis.pdf-197-4.png)
clearly non-monotonic and qualitatively consistent with the Poisson distribution, P ( n ) = e  n n n /n !,

![SchusterThesis.pdf-197-5.png](SchusterThesis.pdf-197-5.png)

![SchusterThesis.pdf-197-6.png](SchusterThesis.pdf-197-6.png)
while the thermal spectrum monotonically decreases consistent with the Bose-Einstein distribution
P ( n ) = n n / ( n + 1) n +1 .


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 196

In earlier work[Brune1994, Schuster2005] in the weak dispersive limit ( / < 1), the measured

linewidth resulted from an ensemble of Stark shifts blurring the transition, while here in the strong

limit ( / > 1) each member of the ensemble is individually resolved. In the spectra measured

here (Fig. 8.19), the linewidth of a single peak can be much less than the frequency spread of

the ensemble, but changes in photon number during a single measurement can still completely

dephase the qubit. Taking this into account, yields a predicted photon number dependent linewidth,

 n = / 2+   +( n + n ) / 2 for the n th peak[Gambetta2006]. The lowest power peak (in the n = 0 . 02

![SchusterThesis.pdf-198-0.png](SchusterThesis.pdf-198-0.png)

![SchusterThesis.pdf-198-1.png](SchusterThesis.pdf-198-1.png)

trace) corresponds to zero photons and measures the unbroadened linewidth,  0 / 2  = 1 . 9 MHz.

When n = 2  eff / the peaks should begin to overlap once more, returning the system to the classical

![SchusterThesis.pdf-198-2.png](SchusterThesis.pdf-198-2.png)

field regime. If this effect were the only limitation, we might hope to count as many as 70 photon

number peaks before they merge. In practice the higher number peaks are also more sensitive to

charge fluctuations in the Cooper pair box, which limits us to about 10 resolvable photon states in

this measurement.

The relative area under each peak in the transmission amplitude (Fig. 8.19) contains informa-

tion about the photon statistics of the cavity field. We can compare two cases having the same

average cavity occupation ( n  3), but containing either a coherent field (Fig. 8.19b) or a thermal

![SchusterThesis.pdf-198-3.png](SchusterThesis.pdf-198-3.png)

field (Fig. 8.19c). To create the thermal field, gaussian noise was added in a wide band around the

cavity (red in Fig. 8.18b). The coherent and thermal states are clearly distinguishable. The weights

of the peaks are non-monotonic for a coherent distribution while in the thermal distribution they

monotonically decrease[Dykman1987] for all noise intensities measured. However, for the sample

parameters and measurement protocols used here, several effects prevent quantitative extraction

of photon number probabilities from the data. First, the inhomogeneous broadening of the higher

number peaks due to charge noise prevents independent extraction of their areas. Additionally,

though it has been analytically shown that the qubit absorption spectrum should accurately rep-

resent the cavity photon statistics[Gambetta2006], this experiment did not have an independent

means to measure the qubit, and there are imperfections in mapping the qubit spectrum onto the

cavity transmission. Finally, numerical simulations show that spectroscopic driving of the qubit

results in complex dynamics which squeezes the cavity photon number, pointing to a path to create

exotic states of light, but also obscuring the initial photon statistics. The measured data is con-

sistent with numerical predictions which do take into account such squeezing effects (see Fig. 8.19)

for photon numbers ( n  3) which we could simulate. While these effects are large in the present


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 197

experiment, an independent measurement of the qubit could be introduced using a second cavity

or Josephson-bifurcation amplifier[Siddiqi2006], allowing the realization of a quantitative photon

statistics analyzer. Previous experiments have also measured analogous statistics of other Bosonic

systems including phonons in an ion trap[Leibfried1996, Leibfried1997], excitations in a single elec-

tron cyclotron oscillator[Peil1999], and the number of atoms in a Bose-Einstein condensate passing

through a cavity[Ottl2005].

The results obtained here also suggest a method for photon-qubit conditional logic. The qubit re-

sponse is now strongly dependent on the number of photons in the cavity. For example, a controlled-

not (CNOT) gate between a photon and qubit could be implemented by applying a  control pulse

at the frequency corresponding to one photon in the cavity. This would flip the qubit if there were

exactly one photon in the cavity, but do nothing for all other number states. Since the qubit does

not absorb the cavity photon, the number is unchanged after the operation and could be used to en-

tangle with distant qubits. A photon number based gate is analogous to the phonon common mode

coupling used in ion-traps[Monroe1995], but since the photons travel along transmission lines and

not through qubits themselves, many qubits can be placed in a single wavelength, and the photons

could be sent to distant qubits, including those in other cavities.

######### 8.3.2 ######### Anharmonic Strong Dispersive Limit

The dispersive limit is conventionally defined as having g/   1. This limit has many physical

implications. One, which weve explored at length, is that the wavefunction overlap will be small

allowing for quantum non-demolition measurements. Mathematically, one can also think of this as

the condition for perturbation theory to converge 1 . Typically, this perturbation is only taken to

second order, but the fourth order effect is also quite interesting. Expanding Eq. 2.4 to fourth order


gives,
E  ,n



 a
= n r +



2

+ ng
2 



2 4

2 g

n
  



a

(
2 



) (8.12)
 3 + -   


![SchusterThesis.pdf-199-0.png](SchusterThesis.pdf-199-0.png)

![SchusterThesis.pdf-199-1.png](SchusterThesis.pdf-199-1.png)

![SchusterThesis.pdf-199-2.png](SchusterThesis.pdf-199-2.png)

![SchusterThesis.pdf-199-3.png](SchusterThesis.pdf-199-3.png)

![SchusterThesis.pdf-199-4.png](SchusterThesis.pdf-199-4.png)

As a result of this new fourth order coupling term the resonator transition frequency becomes photon

number dependent,


g 2

![SchusterThesis.pdf-199-7.png](SchusterThesis.pdf-199-7.png)






g 2 g 4

  



g 4 4

2 n g

![SchusterThesis.pdf-199-8.png](SchusterThesis.pdf-199-8.png)

![SchusterThesis.pdf-199-9.png](SchusterThesis.pdf-199-9.png)
 3 




 r , n = E  ,n +1  E  ,n



1
=  r
 2


![SchusterThesis.pdf-199-5.png](SchusterThesis.pdf-199-5.png)

![SchusterThesis.pdf-199-6.png](SchusterThesis.pdf-199-6.png)




(8.13)


![SchusterThesis.pdf-199-10.png](SchusterThesis.pdf-199-10.png)

1 The convergence criteria is best seen as the condition for a Taylor series expansion in g/ of Eq. 2.4, describing
the exact energies, to converge.


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 198



 40

 50

 60

 70

|Col1|aliased e r drive o w p tone rive d g sin a cre in|drive tone|
|---|---|---|


![SchusterThesis.pdf-200-1.png](SchusterThesis.pdf-200-1.png)

![SchusterThesis.pdf-200-0.png](SchusterThesis.pdf-200-0.png)

5.66175 5.6625 5.66325

probe frequency (GHz)


0.8

0.6

0.4

0.2

0

5.661 5.6615 5.662 5.6625 5.663 5.6635 5.664

probe frequency (GHz)


Figure 8.20: a) Density plot showing the dispersive cavitys inherited non-linearity from its coupling
to the qubit. The cavity is driven with a tone of order n  1 at a slight positive detuning,  d =

![SchusterThesis.pdf-200-2.png](SchusterThesis.pdf-200-2.png)
210 kHz. A weak probe signal is then scanned as the drive tones power is increased. b) A waterfall
plot of the same data, normalized to the low power transmission. As the power is increased the
cavity transmission peak shifts downward in frequency and the linewidth decreases. The two large
features are the drive tone, and an aliased version of it at twice the IF frequency below.

The fourth order correction makes the cavity anharmonic! This non-linearity can be thought of as

coming from the small part of the photon which lives in the qubit. More amazing still, while the

sign of the anharmonicity depends on the qubit state, it is present even when the qubit never leaves

the ground state. The dispersive limit implies that the number dependent term will always be much

smaller than the first order light shift, but when considering the anharmonicity of the cavity, it is

appropriate to compare instead to the cavity linewidth  . The cavity can be considered anharmonic

at a new critical photon number, n  =   3 / 2 g 4 , which is the condition for the non-linear shift to

be equal to the linewidth. For this experiment n  3.


To observe this non-linearity most directly, two-tone spectroscopy of the cavity is performed. A

drive tone at is applied at a detuning from the cavity  d and has its power scanned near n  1

photons. If the detuning is chosen so as to repel the cavity line from the drive tone, it will be more

heavily filtered as the power is increased. In this case photon number fluctuations are suppressed

potentially below the vacuum noise. If it is detuned such that the anharmonicity brings the line closer

it will tend towards bistability, which is very similar to a Josephson bifurcation amplifier[Siddiqi2004].

In this experiment, we will focus on the case where number fluctuations are suppressed rather than

enhanced. A second probe tone, at very low powers, is used to interrogate the cavity resonance. As

the drive power is increased (see Fig. 8.20), the cavity line is red-shifted and becomes broadened. The

broadening occurs because the line is moved by 2 g 4 /  3 whenever the photon number changes, so in

addition the homogenous broadening due to decay, the line is also shifted by significant fraction of


-----


CHAPTER 8. CAVITY QED EXPERIMENTS WITH CIRCUITS 199


a) b)


0.


5.663

5.6625

5.662

5.6615


575

550

525

500

475

450

425


 0.5

 1.

 1.5

![SchusterThesis.pdf-201-0.png](SchusterThesis.pdf-201-0.png)

0.05 0.1 0.15 0.2 0.25


![SchusterThesis.pdf-201-1.png](SchusterThesis.pdf-201-1.png)

0.1 0.2 0.3 0.4


RF power, P RF (  W) RF power, P RF (  W)

Figure 8.21: a) Anharmonic cavity frequencies  r  , as extracted from fitting the data in Fig. 8.20.
The total shift is 1 . 5 MHz about 3  . b) As the peak is shifted it is also broadened increasing by
about 20% in the dataset. The peak amplitude is also reduced because the cavity now experiences
inhomogenous broadening due to its significant non-linearity.

a linewidth. This can be thought of as a manifestation of the uncertainty principle, which demands

that any reduction of uncertainty in photon number be accompanied by a corresponding increase in

the fluctuations of its conjugate variable, the phase.

This experiment presents a first glance a cavity which is anharmonic on the single photon level.

A better understanding of this regime will be especially important for understanding experiments

with two strongly coupled cavities. It could be used to make a single photon detector, or even-

tually perhaps even a photonic qubit. There is much yet to be done along this direction. Future

experiments might increase the dispersive coupling (or decrease the cavity linewidth) to see still

stronger anharmonic effects. The positive feedback regime has been studied a little (though is not

presented here) and should be studied more closely. Such investigations could see how the discrete

nature of the photon affects the transition from qubit (non-linearity strong even at one excitation)

to Josephson bifurcation effects[Siddiqi2004] (quasi-classical non-linearity at hundreds of photons).


-----


### Chapter 9

## Time Domain Measurements

All of the experiments discussed until now have been spectroscopic in nature. These allow one to

efficiently study the energy levels of the cavity-qubit system over decades of frequency scales with

incredible precision. Each of these spectroscopic studies has a dual in the time domain, and many

of the cavity QED or quantum computation concepts, such as gates or single shot measurements

are expressed more naturally in the time domain. In the first section, I present single qubit gates,

demonstrating full control over the qubit state. The quantum non-demolition measurement process

is explained and used to demonstrate > 95% visibility of qubit control. The next section goes

a step further, looking at single shot detection rather than ensemble measurements, realizing a

measurement fidelity of 30  40%. Finally, the ability to manipulate the qubit is mapped onto the

state of a single photon creating an on-demand, single photon source, which can provide arbitrary

superposition states of zero and one photon.

####### 9.1 ####### Single Qubit Gates

An outstanding question for superconducting qubits, and in fact for all solid-state implementations

of quantum information processors, is whether the qubits are sufficiently well-isolated to allow long

coherence times and high-fidelity preparation and control of their quantum states. This question

is complicated by inevitable imperfections in the measurement. A canonical example is a Rabi

oscillation experiment, where the experimenter records the oscillations of a meters response as a

function of pulse length to infer the qubits excited state population immediately after the pulse. The

measurement contrast (e.g. the amplitude of the meters measured swing relative to its maximum

value) is reduced in general by both errors in the qubit preparation and readout, and sets a lower

200


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 201

limit on the visibility of oscillations in the qubit population. Most experiments with superconducting

qubits to date have reported only the measurement contrast, setting only a lower limit on the

visibility in the range of 10  50 % [Nakamura1999, Vion2002, Martinis2002, Yu2002, Chiorescu2004,

Collin2004, Yamamoto2003].

A full understanding of the measurement process is required to extract the qubit population

from the meters output. The qubit control is then characterized by the visibility, defined as the

maximum qubit population difference observed in a Rabi oscillation or Ramsey fringe experiment.

It is essential to demonstrate that a qubit can be controlled without inducing undesired leakage

to other qubit states or entanglement with the environment. Some experiments [Simmonds2004]

observe a substantial reduction of the visibility due to entanglement with spurious environmental

fluctuators [Meier2005]. In the few experiments in which the contrast has been characterized, it was

close to the expected value [Duty2004, Astafiev2004], which implies that high visibility should be

achievable with superconducting qubits.

In the experiments presented here, we coherently control the quantum state of a Cooper pair box

in the resonator by applying microwave pulses of frequency  s , which are resonant or nearly resonant

with the qubit transition frequency  a / 2   4 . 3 GHz, to the input port C in of the resonator, see

Fig. 9.1a. Even though  s is strongly detuned from the resonator frequency  r , the resonator can

be populated with n s drive photons which induce Rabi oscillations in the qubit at a frequency of

 Rabi =  n s g/ . Simultaneously, we perform a continuous dispersive measurement of the qubit state

![SchusterThesis.pdf-203-0.png](SchusterThesis.pdf-203-0.png)

by determining both the phase and the amplitude of a coherent microwave beam transmitted through

the resonator at frequency  RF which is resonant or nearly resonant with the resonator frequency


 r / 2   5 . 4 GHz [Blais2004, Wallraff2004]. The phase shift  = tan  1 2 g 2 /   z =   0 is the

response of our meter from which we determine the qubit population. For the measurement, we 



chose a resonator that has a quality factor of Q  0 . 7  10 4 corresponding to a photon decay rate of

/ 2  = 0 . 73 MHz. The resonator is populated with n  1 measurement photons on average, where

n is calibrated using the ac-Stark shift [Schuster2005]. All experiments are performed in a dilution

refrigerator at a temperature of 20 mK. The charging energy of the box is E C = e 2 / 2 C   h 5 . 2 GHz.

Details on the device fabrication can be found in Ref. [Frunzio2005].

We initially determine the maximum swing of the meter in a calibration measurement by first

maximizing the detuning to minimize the interaction ( g 2 /   0) and defining  = 0. We prepare

the Cooper pair box in the ground state | g  by relaxation, the thermal population of excited states


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 202


######### (a)


######### bias tee ######### Cin ######### Cout ######### RF amp ######### mixer


######### Cin


######### Cout


|C|Col2|
|---|---|

||Col2|
|---|---|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
| s|LO  RF|V g|||||


![SchusterThesis.pdf-204-0.png](SchusterThesis.pdf-204-0.png)


######### (b)

 (c)


######### 0 #########  ######### s #########  ######### t ######### 6 #########  ######### s ######### 50 #########  ######### s

|Col1|s ~ a|RF ~ r|
|---|---|---|
|n n RF s|Rabi|weak cont. meas.|
||||
||||



######### 0 #########  ######### s #########  ######### t ######### 6 #########  ######### s


######### 50 ######### 

||s ~ | a|Col4|Col5|s ~ |a RF ~ r|
|---|---|---|---|---|---|---|
||/2||||/2|pulsed measurement|
||||||||
||||||||


Figure 9.1: a) Simplified circuit diagram of measurement setup. A Cooper pair box with charging
energy E C and Josephson energy E J is coupled through capacitor C g to a transmission line resonator,
modeled as parallel combination of an inductor L and a capacitor C . Its state is determined in a
phase sensitive heterodyne measurement of a microwave transmitted at frequency  RF through
the circuit, amplified and mixed with a local oscillator at frequency  LO . The Cooper pair box
level separation is controlled by the gate voltage V g and flux  B . Its state is coherently manipulated
using microwaves at frequency  s with pulse shapes determined by V p [Collin2004]. b) Measurement
sequence for Rabi oscillations with Rabi pulse length  t , pulse frequency  s and amplitude   n s

![SchusterThesis.pdf-204-1.png](SchusterThesis.pdf-204-1.png)
with continuous measurement at frequency  RF and amplitude   n RF . c) Sequence for Ramsey

![SchusterThesis.pdf-204-2.png](SchusterThesis.pdf-204-2.png)
fringe experiment with two / 2-pulses at  s separated by a delay  t and followed by a pulsed
measurement.


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 203

being negligible. The box is biased at charge degeneracy ( E el = 0), where its energy is to first-order

insensitive to charge noise [Vion2002]. Using flux bias, the detuning is adjusted to  / 2   1 . 1 GHz

corresponding to a maximum in the Josephson coupling energy of E J /h 4 . 3 GHz <  r / 2  . In


this case we measure a minimum meter response of  | g  =  35 . 3 deg corresponding to a coupling

strength of g/ 2  = 17 MHz. Saturating the qubit transition by applying a long microwave pulse

which incoherently mixes the ground and excited states such that the occupation probabilities are

P | g  = P | e  = 1 / 2, the measured phase shift is found to be  = 0, as expected [Schuster2005]. From

these measurements, the predicted phase shift induced by a fully polarized qubit ( P | e  = 1) would

be  | e  = 35 . 3 deg. Thus, the maximum swing of the meter is bounded by  | e    | g  .

In our measurement of Rabi oscillations, a short microwave pulse of length  t is applied to

the qubit in its ground state with a repetition rate of 20 kHz while the measurement response  is

continuously monitored and digitally averaged 5  10 4 times, see Fig. 9.1b. The signal to noise ratio

(SNR) in the averaged value of  in an integration time of 100 ns is approximately 25, see Fig. 9.2,

corresponding to a SNR of 0 . 1 in a single shot. For the present setup the single shot read-out

fidelity for the qubit state integrated over the relaxation time ( T 1 7  s) is approximately 30 % (see


Sec. 9.2). Either a read-out amplifier with lower noise temperature or a larger signal power would

potentially allow a high fidelity single shot measurements of the qubit state in this setup.

The time dependence of the averaged value of  in response to a  pulse of duration  t  16 ns

applied to the qubit is shown in Fig. 9.2b. Before the start of the pulse the measured phase shift is

 | g   35 . 3 deg corresponding to the qubit being in the ground state. Due to the state change of the

qubit induced by the pulse, the resonator frequency is pulled by 2 g 2 / and, thus, the measured phase

shift is seen to rise exponentially towards  | e  with the resonator amplitude response time 2 / 

400 ns, i.e. twice the photon life time. After the  pulse, the qubit excited state decays exponentially

with its energy relaxation time T 1 7 . 3  s, as extracted from the decay in the measured phase shift,


see Fig. 9.2b. As a result, the maximum measured response  max does not reach the full value of  e .
| 

In general, the measurement contrast C = (  max   min ) / (  | e    | g  ) will be reduced in any qubit

read-out for which the qubit lifetime is not infinitely longer than the measurement response time.

Additionally, in non-QND measurements the contrast is reduced even further due to mixing of the

qubit states induced by the interaction with the measurement apparatus. In our QND measurement

presented here, the qubit lifetime is about 15 times the response time of the measurement, allowing

us to reach a high maximum contrast of C  85 % in the bare measurement response  .


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 204

20

a) 0

-20

100


-40

0

-20

-40

40

20

0

-20

-40


80

60

40

20


![SchusterThesis.pdf-206-0.png](SchusterThesis.pdf-206-0.png)

![SchusterThesis.pdf-206-5.png](SchusterThesis.pdf-206-5.png)

![SchusterThesis.pdf-206-1.png](SchusterThesis.pdf-206-1.png)

![SchusterThesis.pdf-206-4.png](SchusterThesis.pdf-206-4.png)

![SchusterThesis.pdf-206-2.png](SchusterThesis.pdf-206-2.png)

10 15 20 25 30 35 40

time, t (  s)


![SchusterThesis.pdf-206-3.png](SchusterThesis.pdf-206-3.png)

5 10 15 20 25 30 35 40

time, t (  s)

Figure 9.2: a) Color density plot of phase shift  (see inset for scale) versus measurement time t
and Rabi pulse length  t . Data shown in b - d are slices through this data set at the indicated pulse
lengths. They show the measurement response  (blue lines) and theoretical prediction (red lines)
vs. time. At t = 6  s (a) a  pulse, (b) a 2  pulse, and (c) a 3  pulse is applied to the qubit. In
each panel the dashed lines correspond to the expected measurement response in the ground state
 | g  , in the saturated state  = 0, and in the excited state  | e  .


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 205

In Figs. 9.2c and d, the measured response  of the meter to a 2  and a 3  pulse acting on the

qubit is shown. As expected, no phase shift is observable for the 2  pulse since the response time

of the resonator is much longer than the duration  t = 32 ns of the pulse. In agreement with the

expectations for this QND scheme, the measurement does not excite the qubit, i.e.  min =  max =

 | g  . The response to the 3  pulse is virtually indistinguishable from the one to the  pulse, as

expected for the long coherence and energy relaxation times of the qubit. In the 2D density plot

Fig. 9.2a, Rabi oscillations are clearly observed in the phase shift acquired versus measurement time

t and Rabi pulse length  t .

The observed measurement response  is in excellent agreement with theoretical predictions, see

red lines in Fig. 9.2, demonstrating a good understanding of the measurement process. The temporal

response  ( t ) = arg { i  a ( t ) } of the cavity field a is calculated by deriving and solving Bloch-type

equations of motion for the cavity and qubit operators using the Jaynes-Cummings Hamiltonian in

the dispersive regime [Blais2004] as the starting point. A semi-classical factorization approximation

is done to truncate the resulting infinite set of equations to a finite set (e.g. a  a z a  a  z ; all
   

lower order products are kept). This amounts to neglecting higher order correlations between qubit

and field which is a valid approximation in the present experiment. The calculations accurately model

the exponential rise in the observed phase shift on the time scale of the resonator response time due

to a state change of the qubit. They also accurately capture the reduced maximum response  max

due to the exponential decay of the qubit. Overall, excellent agreement in the temporal response of

the measurement is found over the full range of qubit and measurement time scales with only T 1 as

a fit parameter, see Fig. 9.2.

The visibility of the excited state population P | e  in the Rabi oscillations is extracted from the

time dependent measurement response  for each Rabi pulse length  t . We find P | e  by calculating

the normalized dot product between the measured response  and the predicted response, taking

into account the systematics of the measurement. This amounts to comparing the area under a

measured response curve to the theoretically predicted area, see Fig. 9.2. The averaged response of

all measurements taken over a window in time extending from the start of the Rabi pulse out to

several qubit decay times T 1 is used to extract P e . This maximizes the signal to noise ratio in the
| 

extracted Rabi oscillations.

The extracted qubit population P | e  is plotted versus  t in Fig. 9.3a. We observe a visibility of

95  6 % in the Rabi oscillations with error margins determined from the residuals of the experi-


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 206


0.8

0.6

0.4

0.2


50

40

30

20

10


![SchusterThesis.pdf-208-0.png](SchusterThesis.pdf-208-0.png)

![SchusterThesis.pdf-208-1.png](SchusterThesis.pdf-208-1.png)

20 40 60 80 100

pulse length,  t (ns)


0.02 0.04 0.06 0.08

drive,  (arb)


Figure 9.3: a) Rabi oscillations in the qubit population P e vs. Rabi pulse length  t (blue dots) and
fit with unit visibility (red line). b) Measured Rabi frequency  Rabi vs. pulse amplitude  s (blue
dots) and linear fit.

detuning,  a,s (MHz)

80 60 40 20 0


0.8

0.6

0.4

0.2


80

60

40

20

|Col1|Col2|
|---|---|
|||


![SchusterThesis.pdf-208-2.png](SchusterThesis.pdf-208-2.png)

200 400 600 800 1000

pulse separation,  t (ns)


4250 4300

drive frequency,  s (MHz)


Figure 9.4: a) Measured Ramsey fringes (blue dots) observed in the qubit population P e vs. pulse
separation  t using the pulse sequence shown in Fig. 9.1b and fit of data to sinusoid with gaussian
envelope (red line). b) Measured dependence of Ramsey frequency  Ramsey on detuning  a , s of drive
frequency (blue dots) and linear fit (red line).

mental P | e  with respect to the predicted values. Thus, in a measurement of Rabi oscillations in a

superconducting qubit, a visibility in the population of the qubit excited state that approaches unity

is observed for the first time. Moreover, the decay in the Rabi oscillation amplitude out to pulse

lengths of 100 ns is very small and consistent with the long T 1 and T 2 times of this charge qubit, see

Fig. 9.3a and Ramsey experiment discussed below. We have also verified the expected linear scaling

of the Rabi frequency  Rabi with the pulse amplitude  s   n s , see Fig. 9.3b.

![SchusterThesis.pdf-208-3.png](SchusterThesis.pdf-208-3.png)

We have determined the coherence time of the Cooper pair box from a Ramsey fringe experiment

at charge degeneracy using / 2 pulses of 20 ns duration, see Fig. 9.1c. To avoid dephasing induced by

a weak continuous measurement beam [Schuster2005] we switch on the measurement beam only after


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 207

the end of the second / 2 pulse. The resulting Ramsey fringes, oscillate at the detuning frequency

 a , s =  a   s  6 MHz, decaying with a long coherence time of T 2  500 ns (see Fig. 9.4a). The

corresponding qubit phase quality factor of Q  = T 2  a / 2  6500 is similar to the best values

measured so far in qubits biased at an optimal point [Vion2002]. The Ramsey frequency is shown to

depend linearly on the detuning  a , s , as expected, see Fig. 9.4b. We note that a measurement of the

Ramsey frequency is an accurate time resolved method to determine the qubit transition frequency

 a =  s + 2   Ramsey .

####### 9.2 ####### Single Shot Readout

Quantum computation, like its classical counterpart, operates on digital information. While per-

forming computations, a qubit can be prepared in any superposition of | g  and | e  . When the qubit

is measured though, it will produce a digital, 0 or 1 result. From the data presented thus far the

binary nature of the qubit is only expressed subtly through oscillatory behavior in response to being

driven, and agreeing well with the predictions for a two-level system interacting with a harmonic

oscillator. The reason the binary nature is masked in the previous experiments is that they are

always composed of many (tens of thousands) of individual experiments ensemble averaged again.

These experiments measured the expectation value rather than the projection of the qubit state. In

this section, we will store each experiment consisting of preparation of the qubit state and subse-

quent measurement of the qubit state individually, histogramming them to see not only the mean

behavior as studied in section 9.1, but also the distribution of the measurements. We find that our

measurement has a fidelity of approximately  33  40% meaning that in an individual experiment

we get about 1 / 3 of a bit of information. This means that the measurement is currently suitable

for ensemble measurements where we get 1 / 3 of the available information (given the qubit decay

time). The measurement fidelity should be > 99% for reliable quantum computation, a goal for

future experiments.

This measurement is somewhat unique for superconducting qubits in that it is a continuous

measurement whereas most experiments employ latching measurements[Lupascu2006, Steffen2006,

Siddiqi2006]. When measuring a small signal one uses an amplifier which adds noise in addition to

amplifying the signal, and can obscure the original signal. In our system the noise temperature is

T N = 5 K, giving an efficiency  = 0 . 025. This corresponds to approximately 40 photons of amplifier

noise in one cavity bandwidth, meaning that we must acquire that many photons in order to achieve


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 208

a signal-to-noise ratio (SNR) of one. To have high fidelity ( > 90%) one must have a SNR > 30 in a

decay time, T 1 . This corresponds to having SNR = 10 by the time there is a 10% chance of decay.

A continuous measurement must acquire that SNR by averaging away any classical noise before the

qubit decays. A latching measurement attempts to reduce the effect of the amplifier noise by first

mapping the fragile quantum state onto a more robust classical state, such as the switching current of

a SQUID[Lupascu2006], a phase slip in a phase qubit[Steffen2006] or a meta-stable oscillation state

in a non-linear cavity[Siddiqi2006]. Once latched into this robust state, the signal can be averaged

until the amplifier noise has been reduced sufficiently. Though latching can be advantageous, there

is typically a finite arming time which must be much faster than the qubit lifetime ( t arm T 1 ).


Latching measurements also often involve large unknown excursions in parameter space during the

measurement which can lead to reduced contrast, though this problem has been addressed to some

extent. The latching measurement of [Siddiqi2006] is compatible with our system and could be used

as a readout, though currently it has a similar fidelity to our continuous measurement.

The continuous measurement protocol used here consists of preparing the qubit in the excited

state (by applying a  pulse) or ground state (by doing nothing) and then measuring the transmission

of the cavity. The local oscillator phase is configured such that in the ground state the amplitude

is all in the in-phase channel (I), and that when in the excited state most of the amplitude is in the

out-of-phase (Q) channel. To first order the Q can be considered the phase, and I the amplitude

(though there are deviations if the phase shifts are large). The measurement tone can be left on

during the pulse (if the dephasing rate is small compared to the  pulse time  10 ns), or turned on

after the preparation pulse has been completed. Several T 1 s worth of data is collected and stored

individually for each experiment.

Once collected each trace must be analyzed individually to assess the most likely prepared qubit

state[Braff2007]. The simplest method is to just average the data for a certain period of time. In

this method one has to find an optimum measurement time. By measuring longer, one can reduce

the uncertainty due to random amplifier noise, but the chances that an excited state qubit has

decayed also grows. Using this simple scheme, the fidelity is fairly sensitive to the exact measuring

time used[Braff2007]. A better technique takes into account the decay of the qubit by weighting the

average with an exponential. While there is still an optimal measurement time, the fidelity is much

less sensitive to measuring a little bit too long[Braff2007]. The best method relies on a non-linear

filtering method which uses the early data to assess the value of data taken later (in the same trace),


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 209

which gives a substantial improvement compared with the linear simple or weighted average filters.

This non-linear filter gives the most improvement at very high fidelities, where a substantial amount

of information is revealed even after a short period of time. At the current level of fidelity 30  40%

all of these methods, once optimized, give similar results.

For this data a slight variation on the exponential weighting method was used. To see how the

weighting function was chosen we first discuss the behavior of an arbitrary filter function. The score,

s , is just the weighted average of the data is just the dot product of the filter function f ( t ), and the


signal  ( t ).


t m
s =

0




f ( t )  ( t ) dt (9.1)


For these experiments rather than using an exponential filter function, a calibration trace of a

measurement of the excited state (like in Fig. 9.2b) was used. The ensemble average is very similar

to an exponential decay and gives similar results to those described in [Braff2007], but has the

convenient property that it is self-aligning in time. In the case of pulsed measurements, where

there might be transients in both the ground and excited states, one can use a Graham-Schmidt

orthonormalization procedure to adjust the weighting accordingly, creating a filter function with the

following prescription


f  =


![SchusterThesis.pdf-211-0.png](SchusterThesis.pdf-211-0.png)

  e avg   e avg

- 


  e avg (   e avg   g avg )   g avg (9.2)
 - 


where   g avg / e are averages taken over many shots and the dot product represents integration over time


as in Eq. 9.1. This function has the property that the average value of the f    g avg / e , will be zero or
- 

one respectively for averages of the ground or excited state. It gives a good measure of how much

information is at each timestep and is convenient to apply. In the future, the non-linear filter should

not be significantly more complex and may improve performance once our signal to noise improves

to get higher fidelity.

With this filtering technique we took many single shot measurements, (10 , 000 , 000 for Fig. 9.5a),

and histogrammed the scores. The histograms can be thought of as probability distributions of

getting a certain score given that the qubit was prepared in the ground or excited state. The two

distributions in figure 9.5a are resolved, but have substantial overlap indicating that there was too

much amplifier noise broadening the distributions. To determine the fidelity of the measurement we

have to define a threshold which decides between scores belonging to the ground state or excited

state. This can easily be found by integrating the distributions (in Figs. 9.5a and d) to compute


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 210


0.14

0.07

0

1

0.5

0

40

30

20

10


840.


0.06

0.03

0

1

0.5

0

40

30

20

10


9000.

4500.


420.

|a)|Col2|
|---|---|


![SchusterThesis.pdf-212-0.png](SchusterThesis.pdf-212-0.png)

![SchusterThesis.pdf-212-1.png](SchusterThesis.pdf-212-1.png)

![SchusterThesis.pdf-212-2.png](SchusterThesis.pdf-212-2.png)

![SchusterThesis.pdf-212-3.png](SchusterThesis.pdf-212-3.png)

![SchusterThesis.pdf-212-4.png](SchusterThesis.pdf-212-4.png)

 4  2


 4  2 0 2 4


filter value, s (arbs) filter value, s (arbs)

Figure 9.5: Histograms of single shot measurements after preparation with a  pulse (red) and no
pulse (blue), using measurement power equivalent to n  7 photon ( a - c ) and n  30 photons ( d - f ).

![SchusterThesis.pdf-212-5.png](SchusterThesis.pdf-212-5.png)

![SchusterThesis.pdf-212-6.png](SchusterThesis.pdf-212-6.png)
The data in a and d are obtained by histogramming, the filter value (method described in the text)
of many single shots (approximately 10 , 000 , 000 in a and 6 , 000 in d ), to form a probability density
p e /p g of excited/ground state vs. filter value. By integrating these probability distributions one
can create s-curves ( b and e ), which give the probabilities P g ( s ) /P e ( s ) of the qubit being in the
ground/excited state if the measured filter value is less than s . The fidelity ( c and f ) for a given
threshold s is given by the quantity P g ( s ) P e ( s ). The maximum threshold at n 7 is F 32%,
  

![SchusterThesis.pdf-212-7.png](SchusterThesis.pdf-212-7.png)
whereas it is n  30 is F  38%. The histogram in d shows the effects of demolition with evidence

![SchusterThesis.pdf-212-8.png](SchusterThesis.pdf-212-8.png)
of an excited state population in the ground state histogram and excess ground state in the excited
state histogram. This demolition prevents the fidelity from increasing as expected with photon
number. The histograms have been scaled and offset such that the mean of the excited and ground
state distributions lie at  1 for clarity.


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 211

the probability P g ( s ) /P e ( s ) of being in the ground/excited state and measuring a score below a

given threshold (see Figs. 9.5b and e). The difference of these two, P g ( s ) P e ( s ), gives the average


fidelity of a measurement at that particular threshold. The maximum fidelity was about 32% for

the distribution in figure 9.5a which had n  7 photons and 38% for the distribution in figure 9.5d.

While the fidelities are (disappointingly) similar, the cause of errors is quite different. In fig-

ure 9.5a the distributions are broad and basically symmetric (though a little asymmetry is noticeable

in the ground state distribution), while the in figure 9.5d they are quite narrow but they are asym-

metric, even bimodal. The width of the histograms arises from the random noise from the amplifier,

while the asymmetry gives information about the effect of decay (or measurement induced demoli-

tion). Ideally the signal to noise ratio should improve by increasing the power from n  7 to n  30,

improving the fidelity significantly. While the signal to noise ratio (as evident by the width of the

ground state peaks in Fig. 9.5d) does improve the fidelity does not because the measurement itself

induces transitions in the qubit.

The exact cause of this demolition is not well understood. One known source of measurement

based demolition arises from the wavefunction overlap, described in Eq. 2.7. For small photon

number ( n  n crit = 3000 for this sample), this overlap should be  n ( g/ ) 2 < 1%. This implies

that an effect outside the simple Jaynes-Cummings Hamiltonian is responsible for the demolition.

One possibility is that the measurement excites the Cooper pair box out of the qubit Hilbert space

into higher excited states, via a multiphoton process. Such processes have been seen at certain bias

points and powers and could be responsible but we havent been able to definitively confirm or deny

that this is the culprit here.

Solving this mystery and improving the single shot fidelity should be considered one of the top

priorities for future experiments. Higher fidelity readout would allow us to study quantum measure-

ment, observing quantum jumps, and with qubit gates also to perform tests of Bells inequalities.

It is also possible that the same type of process which causes demolition in the presence of the

measurement is responsible for the relaxation of the qubit when the measurement is off, which is

the biggest unsolved mystery in all superconducting quantum computing applications.

####### 9.3 ####### Single Photon Source

Conventional electronic circuits are only capable of interacting with classical electromagnetic signals,

which consist of superpositions of many different photon number states [Schuster2007]. Though


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 212

####  #### t = 12 ns

|Col1|Col2|
|---|---|
|||




![SchusterThesis.pdf-214-0.png](SchusterThesis.pdf-214-0.png)

Figure 9.6: The single photon source is made by applying a short (  12 ns) gaussian control pulse
(dark blue), to prepare the desired qubit state. The qubit then decays in a time T 1 90 ns,

primarily through radiating into the transmission line through the cavity, resulting in the release a
single photon or superposition state.

recently developed quantum circuits have the ability to interact with single photons, they are still

usually controlled and measured using classical voltages and currents [Nakamura1999, Vion2002,

Martinis2002, Yu2002, Chiorescu2004, Collin2004, Yamamoto2003]. Here, we demonstrate an on-

chip single photon source which employs the circuit quantum electrodynamics architecture to map

an arbitrary state of a superconducting qubit onto a single photon in a transmission line resonator

with 80% efficiency [Houck2007]. A photon is created via enhanced fluorescence of the qubit due

to the Purcell effect of the cavity, allowing single photons to be requested, on-demand, every

 100 ns. Tomography of both the qubit and photon states demonstrate the ability to convert the

stationary qubit into a flying qubit. The ability to generate and detect [Schuster2007] single photons

are key tools to study microwave quantum optics on a chip.

The underlying principle for generating single photons from atoms or qubits is simple. An

excited qubit can relax to its ground state by emitting a photon, so a pulse that excites the

qubit can trigger a single photon emission [Clauser1974, Kimble1977] (see Fig. 9.6). Early ex-

periments demonstrated this photon generation from ions [Diedrich1987], atoms [Darquie2005],

molecules [Basche1992, Brunel1999, Lounis2000], nitrogen vacancies [Kurtsiefer2000], and quan-

tum dots [Michler2000, Michler2000a, Pelton2002] though radiation in all directions made effi-

cient collection difficult. Collection is also difficult in solid state turnstile approaches to photon

generation[Imamoglu1994, Kim1999]. In a cavity QED source, the atom or qubit is coupled to

a single photonic mode of a cavity, enhancing the rate of decay to that mode through the Pur-

cell effect [Purcell1946] and allowing a source where photons are emitted into a controlled chan-


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 213

nel. Atoms [Brattke2001, Kuhn2002, Maitre1997, McKeever2004], ions [Keller2004] and quantum

dots [Moreau2001, Santori2002, Pelton2002] have been used to generate optical photons efficiently

in this manner.

Here, we implement a cavity QED system in a circuit, where a superconducting qubit and

transmission line resonator are coupled such that the dominant channel for relaxation of the qubit is

to spontaneously emit a photon into the resonator. Each time the qubit is excited, the mostly likely

outcome is the generation of one (and only one) photon on a timescale given by the characteristic

decay rate of the qubit. The challenge is to create a system where spontaneous emission dominates

other relaxation channels.

When in the dispersive limit ( >> g ), the artificial atom (qubit) has a small photonic compo-

nent of the wavefunction, of magnitude ( g/ ) 2 (see App. B). This opens a new source of decay for

the qubit, as the photonic component of the qubit can decay at the cavity decay rate,  , resulting in

a new qubit decay rate   = ( g/ ) 2  . The qubit can be an efficient photon source if this new decay

rate (the Purcell effect [Purcell1946]) dominates over other non-radiative decay rates,   >  .


Verifying the single photon output is a substantial challenge in on-chip microwave experiments.

At this time, microwave single photon detectors are in their infancy[Schuster2007] and there isnt yet

an equivalent to the optical single photon detector such as a photomultiplier or avalanche photodiode.

Fortunately, several unique characteristics of the source are evident in the average signal generated

by many single photon events, together yielding a convincing verification even with noisy detectors.

Most simply, the output of the single photon source is expected to be oscillatory in the amplitude of

the control pulse. Second, the average amplitude produced should agree well with the expected value

for a single photon. Finally, and most importantly, if the output of the system depends only on the

state of the qubit, the measured photons should show complete agreement with that expected from

independent measurements of the qubit. The source reported here meets all three of these criteria.

The circuit designed to generate photons consists of a superconducting transmon qubit, an opti-

mized version of the Cooper Pair Box, capacitively coupled to a half-wave transmission line resonator

with fundamental frequency  r / 2  = 5 . 18 GHz. Two important design differences between this cir-

cuit and previous incarnations of circuit QED are needed to achieve efficient single photon generation.

First, the cavity is asymmetric in that the capacitors (mirrors) at either end of the transmission

line are no longer equally coupled (reflective), resulting in asymmetric decay rates to the input and

output ports (  in / 2  200 kHz for the input side and  out / 2  = 44 MHz for the output). As a



-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 214

result, photons generated in the cavity are emitted at the output port more than 99% of the time. In

addition, the total decay rate for the cavity, / 2  = 44 MHz, is substantially higher than in previous

samples, a necessary change for spontaneous emission to be the dominant relaxation channel for the

qubit. The qubit dephasing rate in the absence of spontaneous emission,   , is frequency dependent,

with  2 / 2  < 3 MHz for all measured frequencies between 4 . 3 and 7 . 3 GHz.

Transmission measurements are used to probe the energy spectrum of this system while the

qubit frequency is tuned via an external magnetic field (see Fig. 8.4). When the qubit is far detuned

from the cavity, only a single transmission peak is expected, centered at the cavity frequency with

a Lorentzian lineshape and width given by the bare cavity width. When the qubit and cavity are

resonant, two peaks in transmission are expected, a phenomenon known as the vacuum rabi splitting.

Each peak corresponds to one of the two single-excitation eigenstates of the system, superpositions

of the separate qubit and photon excitation states (see Fig. 8.4b). The width of each peak is the

average of the qubit and photon decay rates, (  +  ) / 2. In the dispersive limit, where the detuning 

is much larger than the coupling g , spontaneous emission is enhanced by the Purcell effect, resulting

in decay rates [1  ( g/ ) 2 ]  +( g/ ) 2  and [1  ( g/ ) 2 ]  +( g/ ) 2  (see Fig. 8.4c) . Experimentally

determined linewidths agree well with theoretical predictions (see Fig. 8.5), demonstrating the

ability to tune the rate of radiative decay of the qubit by changing its resonant frequency.

By choosing the qubit-resonator detuning, (  a / 2  = 4 . 66 GHz and  / 2  ) one can make the

radiative channel dominate the qubit decay. With a coupling g/ 2  = 107 MHz, the qubit wave

functions had a ( g/ ) 2 = 4% photonic nature, resulting in a spontaneous emission lifetime of

  / 2  = 1 . 7 MHz. When the qubit was tuned to this frequency, the measured relaxation rate of the

qubit was / 2  = 1 . 9 MHz, indicating a non-radiative decay time T 1 = 1 / 2  800 ns. With the
 

current experimental parameters the expected radiative efficiency is  =   / 90%.


To verify single photon generation, we first show that the output of the cavity is an oscillatory

function of the input drive, as at most one photon is generated, regardless of the magnitude of

the input drive. A 24 ns gaussian control pulse rotates the qubit state by a Rabi angle that is

proportional to the pulse amplitude. After the control pulse leaves the cavity, the excited qubit

will relax, generating a new photon state at the qubit frequency. Because the control pulse leaves

the cavity at a rate  that is much faster than the rate of spontaneous emission   , the control

pulse and generated photons can easily be separated in time. As seen in Figure 9.7a, the measured

control signal increases monotonically, while the spontaneous emission oscillates as the qubit is


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 215

|a )|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|


![SchusterThesis.pdf-217-0.png](SchusterThesis.pdf-217-0.png)

![SchusterThesis.pdf-217-1.png](SchusterThesis.pdf-217-1.png)

Figure 9.7: Mapping of qubit state onto photon states. a) Measured drive and spontaneous emission
voltage. When the drive rotating the qubit is increased, the initial output of the cavity increases
linearly, while after many lifetimes the output voltage of the cavity is oscillatory, due to photons
stored in the qubit. b) Output power of the cavity (  a  a  ) measured with a diode, and measured
qubit state (  z ). These peak when the qubit is in the excited state, after a  pulse; the agreement
 
between qubit and photon states verifies the photon generation occurs as expected. The peak power
is 80% of the power expected from an ideal qubit, indicating that 1 / 5 of the time, the qubit decays
non-radiatively. Because of measurement transients, spontaneous emission can be collected earlier
after the drive than the qubit state can be measured. While the qubit and photon states do agree
in amplitude at this time, the earlier emission is plotted here with a scaled version of the qubit
state for signal to noise reasons. c) Average voltage of the output photons (  a + a   ) compared with
the qubit state  x measured with a Ramsey experiment. The agreement shows that the phase
 
of superpositions states is also transferred from qubit to photon. The photon output here is only
50% of that expected for an ideal qubit due to non-radiative decay in b. and dephasing. The qubit
amplitude here agrees with the qubit amplitude at later times, but is again scaled to match the
photon amplitude at the earlier measurement time presented here.


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 216

rotated through increasing angles from the ground to the excited state and back, confirming that

the spontaneous emission is proportional to the qubit state, not simply the applied drive amplitude.

We characterize both the power and electric field of the single photon source, using independent

measurements of the qubit state and control pulse to verify performance (see Fig. 9.7). If the qubit

state is mapped to the photon state, then an arbitrary superposition of the ground and excited

states  | g  +  | e  will result in the same superposition of photon states:  | 0  +  | 1  , where | 0 

and | 1  refer to states with zero or one photon. The average photon number is proportional to the

average qubit state in the ground-excited basis: a  a = 2  z 1. The power output is minimum
   

with no rotation or a 2  rotation, and maximum for a  rotation, when the qubit is in the purely

excited state and a single photon is generated. The two quadratures of homodyne voltage, on the

other hand, are proportional to the x and y-components of the qubit state: a + a  =  x and
   

a a  =  y . The qubit emits in the conjugate quadrature from the control pulse separating the
    

spontaneous emission from the control. Because a Fock state has no average phase the averaged

voltage of spontaneous emission is exactly zero whenever the photon number is known completely.

Thus, for 0,  , and 2  rotations, no voltage is expected (see Fig. 9.7). However, superpositions of

ground and excited states do give a voltage, a maximum for a / 2 rotation, and a minimum for

3 / 2 rotations.

Both the power and voltage of the photon output match the qubit state, demonstrating the

ability to generate single photons, as well arbitrary superpositions of zero and one photon, simply

by controlling the qubit. Moreover, the amplitude of the pulse is as expected. The measured

control pulse is used to calibrate the amplitude of the spontaneous emission. The frequency of qubit

oscillations and a measurement of the control pulse on the output of the cavity together yield a

calibration for the gain of the amplifiers, which in turn allows us to determine the efficiency of our

single photon source. Simulations that include non-radiative channels of decay and dephasing agree

well with the observed data. The homodyne voltage peaks at around 50% of the expected value for

an otherwise lossless qubit, due to dephasing. The power efficiency is 80%, larger than for the voltage

efficiency because only energy relaxation and not pure dephasing reduces the efficiency in power. It

is likely reduced from the maximum 90% due to dephasing during the pulse and in practical use the

efficiency may be reduced further from this 80% to separate the control pulse from the emission. By

waiting to collect photons, some early emission events are missed, but double photon events due to

the control pulse are prevented.


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 217

######### Theory ######### Experiment


12 

10 

8

6 

4 

2 

12 

10 

8

6 

4 

2 


12 

10 

8

6 

4 

2 

0

12 

10 

8

6 

4 

2 


![SchusterThesis.pdf-219-0.png](SchusterThesis.pdf-219-0.png)

![SchusterThesis.pdf-219-1.png](SchusterThesis.pdf-219-1.png)

![SchusterThesis.pdf-219-4.png](SchusterThesis.pdf-219-4.png)

![SchusterThesis.pdf-219-5.png](SchusterThesis.pdf-219-5.png)

20 0 20 40 60

![SchusterThesis.pdf-219-2.png](SchusterThesis.pdf-219-2.png)

![SchusterThesis.pdf-219-6.png](SchusterThesis.pdf-219-6.png)

20 0 20 40 60

Time (ns)


20 0 20 40 60

![SchusterThesis.pdf-219-3.png](SchusterThesis.pdf-219-3.png)

![SchusterThesis.pdf-219-7.png](SchusterThesis.pdf-219-7.png)

20 0 20 40 60

Time (ns)


Figure 9.8: Measuring the free induction decay of a single qubit. Theoretical predictions for both
quadratures of the homodyne voltage, both in-phase ( a ) and out-of-phase ( b ) with the drive, agree
well with experimental measurements of the in-phase ( c ) and out-of-phase ( d ) signals. Because
emission is always orthogonal to the rotation axis, the spontaneous emission and control signal are
phase separable. The homodyne sine waves in the previous figure are vertical slices through the
emission in d . The frequency of these oscillations, coupled with a gain known from measurements
of the control pulse, provide a calibration. The theory presented in b uses this calibration and
parameters known from separate measurements to predict the data in d . Because the qubit and
drive are slightly detuned by a fluctuating amount due to flux instability (on the order of 3 MHz),
there is a slow beat note in the time direction. This fluctuating detuning is modeled by adding two
homodyne emissions predictions at  1 . 5 MHz detuning. The fast oscillations in the time domain are
a direct measure of the Rabi oscillations of the qubit.


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 218

#########  ######### z ######### I (a+a #########  ######### ) ######### Q (a-a #########  ######### )

2 


2 


![SchusterThesis.pdf-220-0.png](SchusterThesis.pdf-220-0.png)

![SchusterThesis.pdf-220-1.png](SchusterThesis.pdf-220-1.png)

![SchusterThesis.pdf-220-3.png](SchusterThesis.pdf-220-3.png)

![SchusterThesis.pdf-220-4.png](SchusterThesis.pdf-220-4.png)

![SchusterThesis.pdf-220-5.png](SchusterThesis.pdf-220-5.png)

![SchusterThesis.pdf-220-2.png](SchusterThesis.pdf-220-2.png)

2  0 2  2  0 2  2  0 2 

X Angle X Angle X Angle

Figure 9.9: Single photon fluorescence tomography. a) Measurement of qubit state after rotations
by pulses of arbitrary amplitude and phase. Regardless of the phase of the pulse, the qubit oscillates
to a peak after a  pulse. b and c. Fluorescence tomography. The amplitude of the voltage measured
in each homodyne quadrature agree with expectations for  x and  y . Oscillations around the
   
x-axis produce a signal in  y while none in  x . This shows the ability to map an arbitrary qubit
   
state onto a photon state, as well as the ability to characterize a qubit state through spontaneous
emission.


2  0 2  2  0 2  2  0 2 

X Angle X Angle X Angle


Using this calibration technique and numerical simulations, complete time dynamics can be

predicted to excellent accuracy, as shown for the homodyne voltage in Figure 9.8. Several features

of the time dynamics are striking. First, because the control pulse sets the rotation axis, and the

qubit state sets the emission phase, the control and generated photons are orthogonal in phase,

which allows the two signals to be completely separated in homodyne detection. In the generated

photon quadrature, rapid time oscillations are apparent during the control pulse; this is a direct

observation of the Rabi oscillation of the qubit through its spontaneous emission. After the pulse,

the qubit emits with a phase depending on its final state, resulting in a smooth connection between

the time and power oscillations. Finally, there is a very low frequency oscillation in time. Photons

are emitted at the qubit frequency, which in the data shown here, is slightly detuned from the drive

frequency. The result is a beating, with a half period shown in the image. This beating indicates

that there is a slight frequency separation between the input and output photons in addition to the

phase and time separations.

Tomography represents an even more powerful tool for characterizing the qubit[Steffen2006]

and photon states, and demonstrating a complete mapping of the qubit state onto the photons.

Tomography plots a measured quantity (  z , a + a  , and a a  ) as function of control pulses
      

applied with all phases and amplitudes. Here, qubit tomography (of  z ) is measured using a
 


-----


CHAPTER 9. TIME DOMAIN MEASUREMENTS 219

dispersive measurement of the qubit state  z . This yields the expected concentric rings for a
 

qubit initially in the ground state. Tomography of the photon state is performed by measuring the

fluorescence directly in both homodyne quadratures (  a + a   , and  a  a   ). These show excellent

agreement with the expected  x and  y components of the qubit state. This means that a qubit

state can be copied onto a photon state, thus transferring information from a stationary qubit to a

flying qubit, one of the extended DiVincenzo criteria [DiVincenzo2000] for quantum computation.

The mapping of qubit states onto photon states allows for the use of photons as a true resource for

quantum information on a chip. This is a convenient means of creating non-classical states of light

to interact with atoms, all in the wires of an integrated circuit, allowing them to be shuttled around

a chip. This work also stresses the need for true single shot, single photon detectors at microwave

frequencies, which would allow for tests of many of the tenets of basic quantum mechanics on a chip.

The source presented here has a high efficiency ( > 80%), a high repeat rate (  100 ns), and is robust

to first order noise in the control pulse. Further, it not only generates single photon Fock states,

but also any single photon superposition state. These abilities will be important tools for on-chip

quantum optics in the microwave regime.


-----


### Chapter 10

## Future work

The biggest results of this work are not just its current achievements, but in the tradition of science,

are new questions, and new ideas for future experiments. These fall into two basic categories. The

first class consists of ideas to improve the understanding of current experiments and overcoming

current barriers, using this knowledge to make progress towards furthering our understanding of

cavity QED and realizing a quantum information processor. The second class combines quantum

circuits with other physical systems, allowing the interaction of systems with potentially disparate

and interesting properties.

####### 10.1 ####### Evolution of Circuit QED

This work has just scratched the surface of circuit QED. The cavity and Cooper pair box, though

already quite remarkable systems, have much room for improvement both in concept and in their

fabrication. As we gain control over the interaction of single qubits and cavities, the next logical

step is to study the interaction of multiple cavities and qubits. Finally, the knowledge gained in

circuit QED can be applied to create new architectures.

######### 10.1.1 ######### New Cavity and Qubit Designs

Substantial progress on improving the cavities and qubits are possible and likely in the next few years.

The cavities currently can have quality factors in excess of Q > 10 5 , but this was essentially a first

try. Cavities with similar geometries of Q  1 , 000 , 000 have already been demonstrated [Day2003],

but the limiting factors are not well understood. Though the cavity decay rates are not limiting

current experiments they will certainly limit multi-cavity experiments (discussed in the next section).

Also cavities are large distributed objects with a very simple energy spectrum; understanding their

220


-----


CHAPTER 10. FUTURE WORK 221

|Col1|Col2|Col3|
|---|---|---|
||||
||||


|Col1|Storage Cavity|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Readou Cavity|t gg 11|||||
||||| 1||
|||||||
||gg 22  2|||||


![SchusterThesis.pdf-223-0.png](SchusterThesis.pdf-223-0.png)

Figure 10.1: a) Schematic of a single artificial atom or qubit coupled to two cavities. The qubit
would have a separate coupling, g , to each cavity, and the cavities could have different decay rates,
 . One cavity could be be optimized for measurement with a very fast  while the other could
be optimized for coherence with very slow  . b) One could also put two qubits inside the same
cavity. Even though the qubits might be centimeters apart and have no direct contact, they could
communicate through the cavity. This entanglement bus could avoid many of the pitfalls associated
with nearest neighbor interactions.

decay mechanisms may shed insight onto the unknown decay mechanisms afflicting the qubits.

The Cooper pair box was chosen because of familiarity, its large dipole moment, and moderate

sensitivity to known dephasing mechanisms. Recently we have begun to rethink the CPB, working

with the transmon, a CPB in a very different regime, which is nearly immune from charge noise. If

this new type of qubit can be mastered it will allow our previous experiments to be performed better,

and allow experiments that were impractical or impossible due to charge-based dephasing. While no

one knows what causes relaxation in the CPB, there are many culprits and means to eliminate each

one. By using a balanced transmission line or by proper balanced design of the CPB-cavity coupling

any possible radiation into parasitic modes could be reduced. By using materials with different

gaps for the two CPB reservoirs, one might reduce the impact of quasiparticles. By using different

deposition techniques, it could be possible to eliminate potentially lossy films (veil of death) that

might be causing decay. In addition, other traditional types of superconducting qubits could also be

coupled to the cavity in a similar manner. There are also radically different schemes which might

use qubits with topological protection, or a way to turn off the coupling between the ground and

excited state.

######### 10.1.2 ######### Scaling Circuit QED

The experiments in this work demonstrated control and readout of a single qubit inside of a cavity.

Some initial experiments with two qubits in a cavity have already been performed, showing that is


-----


CHAPTER 10. FUTURE WORK 222

possible to detect them simultaneously 10.1b. It has been difficult to measure the coupling between

them because of the number of bias parameters (two charges, and two fluxes, as well as the resonator

frequency) which have to be precisely set. Using the new transmon design, which eliminates the

two charges and the larger couplings that are now regularly attained, all of the technical aspects are

ready to study two qubit gates. These experiments would be different from all previous gates in a

solid state system in that they would be non-local, interacting with each through the cavity, which

is used as an entanglement bus.

Another interesting direction to explore is multiple cavities coupled to a single qubit 10.1a. In

current experiments there is a trade-off between a high quality factor, useful for exploring quantum

optics phenomena, and the fast readout necessary for high fidelity readout of the qubit. By having

two cavities each one could be optimized for these tasks separately. Lack of an independent readout

was one of the main limiting factors in the photon number splitting experiment (see Sec. 8.3.1). A

two cavity implementation of this experiment might realize a practical photon detector or quantum

memory.

Whileit is easy to make a large number of qubits using standard lithography, a functional quantum

information processor will require an architecture which allows information to be processed in parallel

and transported between distant qubits. An implicit requirement of scalability is direct interaction

between distant qubits (or the ability to bring distant qubits together). Cavities could provide a

direct long distance coupling between qubits. In order to manage the complexity inherent in having

many qubits and many cavities coupled together directly and indirectly, it will be necessary to

control the couplings of the cavities and qubits. By loading cavities with active elements such as a

SQUID (current work at Chalmers at KTH), one can tune their frequency. A similar scheme could

also be used for changing the coupling between resonators. It would be perhaps even more useful

to have the ability to turn off the coupling of individual qubits to the cavity. There is a long and

interesting road towards making circuit QED a viable architecture for quantum computing, and it

is one that promises to be an exciting ride.

######### 10.1.3 ######### Other quantum circuits

The experiments here can be seen as a sample of one way that Josephson elements can be used to

control microwaves on the single photon level. They are very non-linear and can be fantastically

coherent, and other architectures and uses might be also be productive. One in particular that might


-----


CHAPTER 10. FUTURE WORK 223

![SchusterThesis.pdf-225-0.png](SchusterThesis.pdf-225-0.png)

Figure 10.2: Molecules are electrostatically trapped above a coplanar waveguide resonator. The
rotational modes of these molecules can be used as qubits and the cavity can be used to cool
the molecules into both the rotational and translational ground, where they would be suitable for
quantum computation or other investigations.

be exciting is that of transmission lines made from many Josephson elements in series[Yurke1996].

These can have impedances that are unrealizable by any geometric inductance and are quite non-

linear. Such systems could be used as the microwave analog of non-linear optical quantum compu-

tation, with the advantage that the Josephson element is a much more readily accessible source of

single photon non-linearity than is available in the optical domain. More immediately, these could be

used as quantum-limited distributed parametric amplifiers which would be useful for all microwave

cryogenic experiments.

######### 10.1.4 ######### Hybrid Circuit QED

Circuit QED can be thought of as a versatile platform for manipulating microwave photons, and

interacting with non-linear quantum systems at microwave frequencies. Microwaves can be thought

of as something of a universal language spoken by circuits, atoms, molecules, nuclear spins and

electron spins, as well as phonons in ion traps or nanomechanical systems. The high energy density

of the 1D transmission line resonators would allow these systems to be efficiently coupled into an

electronic circuit. That would provide a natural path for readout, detection, and even cooling of these

systems. One could envision performing cavity QED experiments with any or many of these diverse

systems, coupled to a superconducting cavity 10.2. Atoms have hyperfine transitions exploited for

atomic clocks, cooling, and quantum computation and ion traps already use microwaves for trapping,

just not for computation. Molecules have rotational modes at gigahertz frequencies which could be

used[Andre2006, Rabl2006]. One could also envision coupling to nuclear or electron[Lyon2006] spins

which have Zeeman splittings from MHz to GHz. Nanomechanical systems can have resonant


-----


CHAPTER 10. FUTURE WORK 224

frequencies up to about a gigahertz and be made to couple electrostatically or magnetically to a

transmission line[Irish2003]. There are nearly limitless possibilities and it will be interesting to see

which ones have the most impact.


-----


### Chapter 11

## Conclusions

The result of this thesis work is the development of circuit QED, which is a platform upon which many

interesting experiments in quantum information and cavity QED have been and will be performed.

Circuits are incredibly versatile, they can be quite coherent ( Q > 10 6 ), their electrical properties

(like impedance) can be varied over 10 orders of magnitude, easily connecting elements from meters

to nanometers, and are made through well-understood, scalable, fabrication techniques. Quantum

circuits provides an immense opportunity to develop new experiments, with new geometries and

topologies that might be difficult or impossible in natural physical systems. In this work we have

used this versatility to explore very different regimes of cavity QED, performing many experiments

which I hope will inspire even deeper study of these interesting topics.

One of the most important contributions was to harness light (the quantum aspects at least)

as a resource for quantum circuits and solid-state quantum computation. The quantum nature of

microwave radiation is not usually exploited, even when dealing with quantum circuits, but single

microwave photons have great potential to act as carriers of quantum information. Their small

energy (  eVs) and large spatial extent ( cms) stretch the limits of our concept of the photon, but

have the advantage of being guided by wires, which could be up to 10 km long based on current

experiments. Our first experiment[Wallraff2004] demonstrated the potential for coupling qubits

to single photons. Later experiments generating[Houck2007] and measuring[Schuster2007] single

photons began to provide first steps towards exploiting this coupling. I hope among other things

that they will provoke interest in and perhaps create a path to the creation of quantum (un)limited

amplifiers and single photon counters, which would improve the efficiency of cryogenic microwave

measurements by at least two orders of magnitude (current cryogenic amplifiers have T N 10 K).


225


-----


CHAPTER 11. CONCLUSIONS 226

There is still a great mystery which remains unsolved: What causes decoherence in supercon-

ducting qubits? While we still have no definitive answer, we have made significant progress. One

goal of the circuit QED architecture is to simplify the qubit circuit, making a very clean system.

The cavity is used to create a well-controlled electromagnetic environment, allowing us to model

and observe the radiative decay of the qubit. The simplicity of the system allowed us to fully model

the measurement process of the qubit, verifying our control of the qubit. Finally, in our initial

development of the transmon, we have begun the process of eliminating the effect of charge noise,

which is primarily responsible for the inhomogeneous broadening of the qubit. Fully understanding

the implications of this new type of qubit will be the subject of future theses, but is very promising

for obtaining long coherence times.

I hope that the reader has come to be as excited about this subject as the author and will pardon

the authors inability to do it justice.


-----


### Appendix A

## Operators and Commutation Relations

####### A.1 ####### Harmonic Oscillators


a, a  = 1 (A.1)
 

a, a  a = a (A.2)
 

a  , a  a =  a  (A.3)
 

####### A.2 ####### Spin 1/2

[  + ,   ] =  z (A.4)

[   ,  z ] =  2   (A.5)

[  i ,  j ] = 2 i i , j , k  k (A.6)

Where i, j { x, y, z } and  i , j , k is the Levi-Cevita tensor ( if i = j then  i , j , k = 0 else k is the remaining

index and it is  i , j , k =  1 if the i, j, and k are cyclic or acyclic.)

####### A.3 ####### Jaynes-Cummings Operators

Note that the operator (  + a  a    , a  a ) used is not the dipole interaction operator itself but a

unitary operator which can be used to diagonalize it approximately to second order.

227


-----


APPENDIX A. OPERATORS AND COMMUTATION RELATIONS 228

######### A.3.1 ######### Interaction with Harmonic oscillator operators

 + a  a    , a  a =  + a + a    (A.7)


 + a  a    , a =   (A.8)
 +  +
 a  a    , a  =  (A.9)
 

######### A.3.2 ######### Interaction with Spin 1/2 Operators


 + a a    ,  z = 2  + a + a    (A.10)
 

 + a a     ,    =  z a  (A.11)
 
 


-----


### Appendix B

## Derivation of Dressed State Atom Picture

The Jaynes-Cummings Hamiltonian:


H JC =   r ( a  a + 1 / 2) +   a  z +  g ( a    + a + ) (B.1)

![SchusterThesis.pdf-231-0.png](SchusterThesis.pdf-231-0.png)

2

has the convenient property that it conserves excitation number, or more specifically it only connects

nearest atom and photon levels together. In matrix form the Hamiltonian can be represented by the

ground state and an infinite block diagonal matrix of 2x2 matrices of the form:


(0)
 r g
g (  r + )



2 

g 




![SchusterThesis.pdf-231-1.png](SchusterThesis.pdf-231-1.png)

 r + (  r + )


![SchusterThesis.pdf-231-2.png](SchusterThesis.pdf-231-2.png)

...


g n  n r ( n  1)  g r + (  n  r + )


![SchusterThesis.pdf-231-3.png](SchusterThesis.pdf-231-3.png)

![SchusterThesis.pdf-231-4.png](SchusterThesis.pdf-231-4.png)

(B.2)


where  a =  r + and n is the number of excitations (photons + 0 or 1 excitation in the atom).

Because of this simple form each block can be diagonalized directly (and independently). The

eigenvalues of the n th submatrix are as in Eq. 2.4:




E ,n =



![SchusterThesis.pdf-231-6.png](SchusterThesis.pdf-231-6.png)

4 ng 2 +  2 (B.3)

 
E g, 0 =
 2


( n  1)  r +  a 


![SchusterThesis.pdf-231-5.png](SchusterThesis.pdf-231-5.png)

![SchusterThesis.pdf-231-7.png](SchusterThesis.pdf-231-7.png)

229


-----


APPENDIX B. DERIVATION OF DRESSED STATE ATOM PICTURE 230

The corresponding eigenstates in raw form (unnormalized and no trig substitutions) are:


![SchusterThesis.pdf-232-1.png](SchusterThesis.pdf-232-1.png)


+


![SchusterThesis.pdf-232-2.png](SchusterThesis.pdf-232-2.png)

 



4 g 2 n +  2

2 g  n | g, n  + | e, n  1 


4 g 2 n +  2


| + , n  = A

![SchusterThesis.pdf-232-0.png](SchusterThesis.pdf-232-0.png)

| , n  = B


![SchusterThesis.pdf-232-3.png](SchusterThesis.pdf-232-3.png)

![SchusterThesis.pdf-232-5.png](SchusterThesis.pdf-232-5.png)

4 g 2 n +  2

2 g  n | g, n  + | e, n  1


(B.4)

(B.5)


4 g 2 n +  2


![SchusterThesis.pdf-232-4.png](SchusterThesis.pdf-232-4.png)

![SchusterThesis.pdf-232-6.png](SchusterThesis.pdf-232-6.png)

![SchusterThesis.pdf-232-7.png](SchusterThesis.pdf-232-7.png)

The square root terms have a very Pythagorean look to them and so one can try to introduce

an angle



1 2 g  n
 n = arctan

![SchusterThesis.pdf-232-9.png](SchusterThesis.pdf-232-9.png)

2 



(B.6)


![SchusterThesis.pdf-232-8.png](SchusterThesis.pdf-232-8.png)

![SchusterThesis.pdf-232-10.png](SchusterThesis.pdf-232-10.png)

With a bit of work (or the right line of Mathematica) one can arrive at the rather beautiful

solution for the eigenstates

, n = cos  n g, n sin  n e, n 1 (B.7)
|  |  |  

![SchusterThesis.pdf-232-11.png](SchusterThesis.pdf-232-11.png)

+ , n = sin  n g, n + cos  n e, n 1
|  |  |  

![SchusterThesis.pdf-232-12.png](SchusterThesis.pdf-232-12.png)

Because the qubit now has a photon component it can decay into the transmission line. This


![SchusterThesis.pdf-232-14.png](SchusterThesis.pdf-232-14.png)

corresponds to going from | + , n  to  , n  1 , which means that we have lost one excitation and

gone from a state which was mostly excited state qubit to mostly ground state qubit (see Fig. B.1).  



![SchusterThesis.pdf-232-13.png](SchusterThesis.pdf-232-13.png)

The decay can be modeled as a term that couples the photons inside the cavity to the transmission

line mode ( b and b  ), which looks like 1

H  =   b  a + a  b (B.8)
 

![SchusterThesis.pdf-232-15.png](SchusterThesis.pdf-232-15.png)

In this language the Fermi Golden Rule can be expressed as


![SchusterThesis.pdf-232-17.png](SchusterThesis.pdf-232-17.png)

![SchusterThesis.pdf-232-16.png](SchusterThesis.pdf-232-16.png)

![SchusterThesis.pdf-232-18.png](SchusterThesis.pdf-232-18.png)

Note that the b will not act if the transmission line is empty (as is assumed above). 2 The


  =
 




2
 , n  1  1 |   b  a + a  b | 0 | + , n  (B.9)
   
  2


expression can then be simplified to

![SchusterThesis.pdf-232-19.png](SchusterThesis.pdf-232-19.png)

1 Eq. B.8 is an approximation which is based on the coupling of a single mode cavity to a continuum of bath modes.
If the bath has frequency structure on the scale of  a more sophisticated treatment is necessary [Walls2006].
2 If amplifier noise or some other source populated the transmission line one could add this in by making n in the
b-mode be nonzero, which would give a rate to heat the qubit-cavity system.


-----


APPENDIX B. DERIVATION OF DRESSED STATE ATOM PICTURE 231

|e,n-1 



|e,n-2 

![SchusterThesis.pdf-233-0.png](SchusterThesis.pdf-233-0.png)

|e,1 

|e,0 


|g,n

|g,2

|g,1

|g,0


-g n-1 /  


|+,2

|+,1


|-,3

|-,2


|-,1 


|Col1| r|
|---|---|


![SchusterThesis.pdf-233-1.png](SchusterThesis.pdf-233-1.png)

Figure B.1: Radiative atom decay paths in presence of coherent cavity coupling. The net amplitude
for a path is found by multiplying the rate of each segment. In the green path, the small part of the
qubit excitation which lives in the cavity is emitted from the cavity leaving the photon number the
same but the atom decayed. At the same time as the purple path shows it is possible for the atom
to absorb a photon (hence the minus sign) from this decayed state, resulting in an ordinary photon
decay with no implications on the qubit state. These rates add coherently with the ns canceling

g 2

leaving only a net rate amplitude (black) g  k/ which gives the usual   =  decay rate.


k/ which gives the usual   = g



2  decay rate.



![SchusterThesis.pdf-233-2.png](SchusterThesis.pdf-233-2.png)

![SchusterThesis.pdf-233-3.png](SchusterThesis.pdf-233-3.png)

![SchusterThesis.pdf-233-4.png](SchusterThesis.pdf-233-4.png)

![SchusterThesis.pdf-233-5.png](SchusterThesis.pdf-233-5.png)

Expressing the eigenstates in the qubit/photon basis (rather than the  , excitation basis, it


  = 
 




2
 , n  1 a | + , n  (B.10)
 
 


is straight forward to evaluate this matrix element. Though it is not hard to evaluate the exact

expressions to gain a bit of intuition let us first use the approximate (to order g/ ) eigenstates



g  n

![SchusterThesis.pdf-233-7.png](SchusterThesis.pdf-233-7.png)
, n = g, n
|  |  


| e, n  1  (B.11)


![SchusterThesis.pdf-233-6.png](SchusterThesis.pdf-233-6.png)

![SchusterThesis.pdf-233-8.png](SchusterThesis.pdf-233-8.png)


g  n

![SchusterThesis.pdf-233-10.png](SchusterThesis.pdf-233-10.png)
+ , n =
|  


| g, n  + | e, n  1 


![SchusterThesis.pdf-233-9.png](SchusterThesis.pdf-233-9.png)

![SchusterThesis.pdf-233-11.png](SchusterThesis.pdf-233-11.png)

Substituting into eq. B.10 and remembering that a | n  =  n | n  1 


![SchusterThesis.pdf-233-12.png](SchusterThesis.pdf-233-12.png)


g  n 1

![SchusterThesis.pdf-233-13.png](SchusterThesis.pdf-233-13.png)
g, n 1 
  |  


g  n

![SchusterThesis.pdf-233-15.png](SchusterThesis.pdf-233-15.png)
e, n 2 a
  | 
 

![SchusterThesis.pdf-233-16.png](SchusterThesis.pdf-233-16.png)

  =   ng  n


g  n
e, n 2 a
  | 
 


| g, n  + | e, n  1 



  = 


(B.12)


![SchusterThesis.pdf-233-14.png](SchusterThesis.pdf-233-14.png)


g  n 1

![SchusterThesis.pdf-233-21.png](SchusterThesis.pdf-233-21.png)
n 1 

![SchusterThesis.pdf-233-20.png](SchusterThesis.pdf-233-20.png)
 


![SchusterThesis.pdf-233-18.png](SchusterThesis.pdf-233-18.png)

![SchusterThesis.pdf-233-17.png](SchusterThesis.pdf-233-17.png)

![SchusterThesis.pdf-233-19.png](SchusterThesis.pdf-233-19.png)

![SchusterThesis.pdf-233-22.png](SchusterThesis.pdf-233-22.png)

g
  =



2
 (B.13)



![SchusterThesis.pdf-233-23.png](SchusterThesis.pdf-233-23.png)

Note that due to the amazing properties of the harmonic oscillator that   does not depend on n

(to first order). This can be seen as the coherent interference between the two decay paths (see Fig.


-----


APPENDIX B. DERIVATION OF DRESSED STATE ATOM PICTURE 232

B.1), represented by the matrix elements inside eq. B.12. The expression using the full eigenstates

is


  =  (cos  n 1 g, n 1 sin  n 1 e, n 2 ) a (sin  n g, n + cos  n e, n 1 ) 2
|    |     | |  |   |


  =   n sin  n cos  n 1

![SchusterThesis.pdf-234-0.png](SchusterThesis.pdf-234-0.png)
 





2

![SchusterThesis.pdf-234-1.png](SchusterThesis.pdf-234-1.png)
n 1 sin  n 1 cos  n (B.14)
 




With these exact expressions we can also find the radiative decay in the resonant limit   0.


Substituting this into eq. B.6 gives  n / 4, substituting this result into eq. B.14, for n 2 yields
 



 n 




lim   = 

![SchusterThesis.pdf-234-2.png](SchusterThesis.pdf-234-2.png)
  0 4


![SchusterThesis.pdf-234-4.png](SchusterThesis.pdf-234-4.png)

![SchusterThesis.pdf-234-3.png](SchusterThesis.pdf-234-3.png)

When calculating the special case of n = 1, the unique ground state must be taken into account 1 .



2
n  1 (B.15)
  1 .


  n =1 =  g, 0 a + , 1 2 (B.16)

![SchusterThesis.pdf-234-5.png](SchusterThesis.pdf-234-5.png)
 |
  
  


lim   n =1 =  g, 0 a 1 ( g, 1 + e, 0
  0  |  2 |  | 





= / 2


![SchusterThesis.pdf-234-6.png](SchusterThesis.pdf-234-6.png)

![SchusterThesis.pdf-234-7.png](SchusterThesis.pdf-234-7.png)

![SchusterThesis.pdf-234-8.png](SchusterThesis.pdf-234-8.png)

1 In the dispersive limit to first order the uniqueness of the ground state can be neglected because the matrix
element for mixing is zero anyway, but in the resonant limit the mixing is by definition of order unity


-----


### Appendix C

## Mathematica Notebooks

####### C.1 ####### Cooper Pair Box

233


-----


### Appendix D

## Recipes

This Appendix will present recipes and descriptions of the fabrication process.

234


-----


APPENDIX D. RECIPES 235

1. Sonicate fresh wafer in NMP 60s

2. Sonicate wafer in Acetone 60s

3. Sonicate wafer in Methanol 60s

4. Sonicate wafer in DI water 60s

5. Blow dry with N 2 and then bake at 110  120s

6. Spin LOR5A at 4000 rpm for 60s

7. Bake at 195  C for 15 minutes

8. Spin S1808 at 4000 rpm for 60s

9. Bake at 115  C for 60s

10. Expose in hard contact mode for 3.3s at 9 . 3mW / cm 2 on 365nm line.

11. Develop in 300 mL of MF-319 for 140s (for  500 nm undercut)

Table D.1: This is an optical lithography recipe to achieve, resist bilayer profile of 800 nm of S1808
on top of 500 nm of LOR 5A with 500 nm undercut.

PMMA/MMA bilayer spinning recipe

1. Sonicate fresh wafer in NMP 60s

2. Sonicate wafer in Acetone 60s

3. Sonicate wafer in Methanol 60s

4. Do NOT sonicate wafer in DI water (PMMA is hydrophobic)

5. Blow dry with N 2 and then bake at 110  120s

6. Spin MMA EL13 at 4000 rpm for 60s

7. Bake at 170  C for 60s (under petri dish propped up on slides)

8. Spin PMMA 950k A3 at 4000 rpm for 60s

9. Bake at 170  C for 30min

Table D.2: When followed correctly this recipe should result in a PMMA-MMA bilayer with 
550 nm of MMA and  120 nm of PMMA on top.


-----


APPENDIX D. RECIPES 236

PMMA development recipe

1. Pour 30 mL of MIBK:IPA 1:3 at 25  C into small beaker

2. Pour 30 mL of isopropyl alcohol (IPA) at 25  C into small beaker

3. Using self-closing tweezers gently shake chip vertically in MIBK solution for 48s

4. Immediately put chip into IPA for 10s

5. Blow dry with N 2

Table D.3: This recipe is not very sensitive to any of the parameters. The developer should be
at room temperature but in my experience  a one or two degrees in temperature does not hurt.
To minimize fluctuations one can keep a store of MIBK solution in a hot water bath a few degrees
above room temperature. One should always be very consistent with the development time but if
one should leave the chip in for a few seconds to long in the developer it will probably still come out
(for > 100 nm feature at least). The isopropyl alcohol is used mainly as a stop to the development,
but will etch the resist, so dont just leave it in there.


-----


APPENDIX D. RECIPES 237

Niobium Sputtering Recipe

1. Load sample in Leaker sputter system on a stainless wafer holder, with a 3/64 thick, 2
diameter copper disk on the back of the wafer.

2. Check that the base pressure is about 2x10-8 Torr before deposition.

3. Turn on all cooling water supplies.

4. Presputter Nb from the 2 torus dc magnetron sputter gun for 2 minutes. Note that the
parameters should be argon=1.3 mTorr; 350 W.

5. Switch off the ion gauge;

6. Set conductance controller to 4.0;

7. Close the conductance controller switch;

8. Close the CHAM INTERLOCK valve;

9. Switch on station gas AR3;

10. Switch on the capacitance manometer;

11. Switch on the flow controller (FC) main;

12. Switch on FC channel 1;

13. Turn the capacitance manometer controller to AUTO;

14. Set pressure to 1.3 mTorr;

15. Set the 1 kW switch to gun E (Niobium);

16. Switch on the 1 kW power supply;

17. Fix the setpoint at 40 W;

18. Switch on OUTPUT to start plasma (light violet);

19. Increase the setpoint to about 350 W

20. Presputter for 2 minutes;

21. Decrease the setpoint to 40 W;

22. Set pressure to 0 mTorr;

23. Open the CHAM INTERLOCK valve.

24. Ion beam clean the wafer for 1.5 minutes.

25. Sputter Nb to desired thickness: Note that the parameters should be argon=1.3 mTorr and 350
W; rate=1.25 nm/s. Source to sample distance is approximately 3 inches. The Nb thickness
should be kept below 300 nm to reduce the probability of photoresist cracking or peeling during
the sputter deposition.

26. Close the CHAM INTERLOCK valve;

27. Set pressure to 1.3 mTorr;

28. Switch on OUTPUT to start plasma (light violet);

29. Increase the setpoint at 350 W;

30. Open shutter E (sputtering time 150 seconds for Nb thickness of 190 nm);

31 To shut down close shutter E;


-----


APPENDIX D. RECIPES 238

Electron Beam Evaporation Recipe

1. Pump out chamber to  3  10  7 . Takes about 2 hours.

2. Evaporate a few nanometers of 1  10  7 . titanium (not on the sample) to lower the pressure to 

3. Evaporate 30 nm aluminum at 0  from normal

4. Wait 2 min .

5. Put 85/15 Argon/Oxygen mix in at 3 Torr for 12 min .

6. Pump chamber down, should get to 5  10  7 in a few minutes.

7. Evaporate 100 nm aluminum at 32  from normal

8. Wait 2 min .

9. Put 70/30 Argon/Oxygen mix in at 3 Torr for 10 min .

10. Place sample in a vertical or slightly inverted holder, for 20 minutes in 50 mL of acetone at
70  C

11. Squirt sample with hot acetone from a syringe, this should take the whole metal film off in
one squirt.

12. Place beaker in sonicator, wait 30s for it to cool, then sonicate for 60s.

Table D.5: This is the deposition recipe for making tunnel junctions. It typically results in a critical
current density of approximately as 2  10  6 but they seem to age less consistently then when a longer pump down time is used. I  40 A / cm 2 . The junctions can be evaporated at pressures as high
have not systematically varied the length of time or pressure of the oxidation step, so I cannot say
how sensitive this parameter is, with any certainty, though others say that it is not very sensitive. A
wide degree of lift-off times and temperatures can be used. If it lifts off smoothly its probably fine.


-----