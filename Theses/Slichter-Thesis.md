
###### Quantum Jumps and Measurement Backaction in a Superconducting Qubit

 by

 Daniel Huber Slichter

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

Professor John Clarke

Professor Dmitry Budker

Professor Birgitta Whaley

Fall 2011


-----


###### Abstract

 Quantum Jumps and Measurement Backaction in a Superconducting Qubit

 by

 Daniel Huber Slichter

 Doctor of Philosophy in Physics

 University of California, Berkeley

 Professor Irfan Siddiqi, Chair

Real-time monitoring of a quantum state provides powerful tools for studying the

backaction of quantum measurement and performing quantum feedback. Historically, this
monitoring capability has been the exclusive province of atomic and optical physics. This
thesis describes the implementation of the first such high-fidelity readout scheme in a solid
state circuit, a superconducting quantum bit (qubit) coupled to a microwave cavity in the
circuit quantum electrodynamics (circuit QED) architecture. The qubit-state-dependent
resonance frequency of the cavity is probed with a microwave drive tone, and the resulting
signal amplified using a fast, ultralow-noise superconducting parametric amplifier. This
arrangement enables the observation of quantum jumps between the qubit states in real
time.

The ability to monitor the qubit continuously with high fidelity and resolve quan-

tum jumps can be used to investigate the backaction of the measurement process on the
qubit. This thesis examines the quantum Zeno eectwhere strong measurement inhibits
the evolution of a quantum systemas well as the transition to non-ideal measurement with
increasing measurement strength in the circuit QED architecture, a phenomenon shown to
be due to the upconversion of low-frequency dephasing noise. These data allow probes of
universal flux noise in previously inaccessible frequency ranges. The work presented here
opens the door for quantum feedback and error correction in solid-state quantum systems
using continuous weak measurement.


-----


###### Quantum Jumps and Measurement Backaction in a Superconducting Qubit

 Copyright 2011

 by

 Daniel Huber Slichter


-----


###### For my family


-----


ii

# Contents

**List of Figures** **v**

**List of Symbols and Abbreviations** **viii**

**1** **Introduction** **1**

1.1 Superconducting qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.2 Quantum jumps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1.3 Superconducting parametric amplifiers . . . . . . . . . . . . . . . . . . . . . 5

1.4 Thesis overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

1.5 Summary of key results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

**2** **Superconducting qubits and circuit quantum electrodynamics** **8**

2.1 Qubits and quantum information . . . . . . . . . . . . . . . . . . . . . . . . 8

2.1.1 Quantization of an electrical circuit . . . . . . . . . . . . . . . . . . 10

2.1.2 Superconducting qubits . . . . . . . . . . . . . . . . . . . . . . . . . 11

2.1.3 The transmon qubit . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

2.2 Quantum non-demolition measurement . . . . . . . . . . . . . . . . . . . . . 18

2.3 Circuit quantum electrodynamics . . . . . . . . . . . . . . . . . . . . . . . . 19

2.3.1 The Jaynes-Cummings Hamiltonian . . . . . . . . . . . . . . . . . . 21

2.3.2 The dispersive approximation . . . . . . . . . . . . . . . . . . . . . . 23

2.3.3 Transmon dispersive shift . . . . . . . . . . . . . . . . . . . . . . . . 25

2.3.4 Measurement rate and readout signal-to-noise ratio . . . . . . . . . . 27

**3** **Amplification and the quantum limit** **30**

3.1 Amplification and noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

3.2 Quantum limits on amplifiers . . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.2.1 Phase-sensitive and phase-preserving amplifiers . . . . . . . . . . . . 36

3.3 Parametric amplification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

3.3.1 Brief history of parametric amplification . . . . . . . . . . . . . . . . 38

3.4 The Lumped Josephson Parametric Amplifier (LJPA) . . . . . . . . . . . . 39

3.4.1 Mathematical description . . . . . . . . . . . . . . . . . . . . . . . . 41

3.4.2 Theoretical gain and bandwidth . . . . . . . . . . . . . . . . . . . . 43

3.4.3 Physical description of operation . . . . . . . . . . . . . . . . . . . . 45

3.4.4 Saturated regime operation . . . . . . . . . . . . . . . . . . . . . . . 51


-----


iii

**Sample fabrication** **54**

4.1 Electron-beam lithography . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

4.1.1 Resist selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

4.1.2 Cold development . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

4.2 Thin-film deposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

4.2.1 Oxygen plasma cleaning . . . . . . . . . . . . . . . . . . . . . . . . . 62

4.2.2 Ground plane fabrication . . . . . . . . . . . . . . . . . . . . . . . . 63

4.3 Sample design and parameters . . . . . . . . . . . . . . . . . . . . . . . . . 65

4.3.1 Transmons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

4.3.2 Paramps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

**Experimental apparatus** **68**

5.1 Sample boxes and launches . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

5.2 Fridge wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70

5.2.1 Low-frequency wiring . . . . . . . . . . . . . . . . . . . . . . . . . . 70

5.2.2 Microwave wiring and switches . . . . . . . . . . . . . . . . . . . . . 72

5.2.3 Microwave roach motel filters . . . . . . . . . . . . . . . . . . . . . 76

5.2.4 Hot/cold load setup . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

5.3 Room temperature electronics . . . . . . . . . . . . . . . . . . . . . . . . . . 80

5.3.1 Pulse and tone generation . . . . . . . . . . . . . . . . . . . . . . . . 80

5.3.2 Variable attenuators . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

5.3.3 Demodulation and digitization . . . . . . . . . . . . . . . . . . . . . 82

**Calibration experiments** **84**

6.1 Paramp sample packaging . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

6.2 Paramp biasing procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

6.3 Paramp performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

6.3.1 Paramp gain . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

6.3.2 Noise performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

6.3.3 Saturated regime operation . . . . . . . . . . . . . . . . . . . . . . . 93

6.4 Calibration of the qubit/cavity system . . . . . . . . . . . . . . . . . . . . . 94

6.4.1 Qubit and cavity spectroscopy . . . . . . . . . . . . . . . . . . . . . 94

6.4.2 Rabi, Ramsey, _T_ 1 , and tomography . . . . . . . . . . . . . . . . . . . 97

6.4.3 Photon number and ac Stark shift . . . . . . . . . . . . . . . . . . . 101

**Quantum jumps** **104**

7.1 What are quantum jumps? . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

7.2 Historical background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

7.3 Experimental design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

7.4 Observation of quantum jumps . . . . . . . . . . . . . . . . . . . . . . . . . 109

7.4.1 Jumps without a paramp . . . . . . . . . . . . . . . . . . . . . . . . 115

7.4.2 Three-level jumps . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116

7.5 Signal-to-noise ratio and fidelity . . . . . . . . . . . . . . . . . . . . . . . . . 118

7.5.1 Theoretical SNR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119

7.5.2 Experimental measurements of SNR . . . . . . . . . . . . . . . . . . 122


-----


iv

7.5.3 Measurement fidelity . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

**8** **Measurement backaction** **126**

8.1 Automated qubit state extraction . . . . . . . . . . . . . . . . . . . . . . . . 126

8.1.1 Determining the qubit state . . . . . . . . . . . . . . . . . . . . . . . 127

8.1.2 Jump time distribution . . . . . . . . . . . . . . . . . . . . . . . . . 131

8.1.3 Maximum likelihood estimation . . . . . . . . . . . . . . . . . . . . . 134

8.1.4 Tests of the extraction algorithm . . . . . . . . . . . . . . . . . . . . 141

8.2 Measurement-induced state mixing . . . . . . . . . . . . . . . . . . . . . . . 144

8.2.1 Dressed dephasing theory . . . . . . . . . . . . . . . . . . . . . . . . 144

8.2.2 Experimental scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

8.2.3 State mixing with added flux tones . . . . . . . . . . . . . . . . . . . 148

8.2.4 Flux noise measurements . . . . . . . . . . . . . . . . . . . . . . . . 152

8.3 Quantum Zeno eect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154

**9** **Conclusions and outlook** **161**

9.1 Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

9.1.1 Quantum feedback and error correction . . . . . . . . . . . . . . . . 161

9.1.2 Single microwave photon source and detector . . . . . . . . . . . . . 162

9.1.3 Improved qubits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162

9.1.4 Parametric amplifier development . . . . . . . . . . . . . . . . . . . 163

9.2 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

**Bibliography** **166**

**A Microwave roach motel filters** **182**

A.1 Design and modeling of roach filters . . . . . . . . . . . . . . . . . . . . . . 182

A.2 Millikelvin filter performance . . . . . . . . . . . . . . . . . . . . . . . . . . 185

**B Fabrication recipes** **189**

B.1 Resist Spinning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189

B.2 E-beam lithography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189

B.3 Resist Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191

B.4 Thin film deposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191

B.5 Silicon nitride deposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192

**C Experimental schematics** **193**


-----


# List of Figures

1.1 The quantronium qubit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1.2 The first observation of quantum jumps. . . . . . . . . . . . . . . . . . . . . 4

2.1 Quantum two-level systems. . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.2 Energy levels of quantized oscillators. . . . . . . . . . . . . . . . . . . . . . 12

2.3 Generalized superconducting qubit. . . . . . . . . . . . . . . . . . . . . . . . 14

2.4 Schematic of transmon qubit. . . . . . . . . . . . . . . . . . . . . . . . . . . 15

2.5 Energy structure of the Cooper pair box and transmon qubits. . . . . . . . 17

2.6 Schematic of cavity QED. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

2.7 Schematic of circuit QED. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.8 Avoided crossing from the Jaynes-Cummings Hamiltonian. . . . . . . . . . . 22

2.9 Principle of circuit QED readout. . . . . . . . . . . . . . . . . . . . . . . . . 24

2.10 Readout signal and noise in the IQ plane. . . . . . . . . . . . . . . . . . . . 29

3.1 Amplification process. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

3.2 Nonlinear resonance response. . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3.3 Schematic of the LJPA. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

3.4 Nonlinear resonance solutions. . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.5 Theoretical gain and bandwidth. . . . . . . . . . . . . . . . . . . . . . . . . 44

3.6 Paramp transfer function: reflected phase vs. pump amplitude. . . . . . . . 46

3.7 Phase-sensitive amplification in the IQ plane. . . . . . . . . . . . . . . . . . 47

3.8 Phase-preserving amplification in the IQ plane. . . . . . . . . . . . . . . . . 49

3.9 Amplification and noise for a detuned signal. . . . . . . . . . . . . . . . . . 50

3.10 Saturated regime amplification. . . . . . . . . . . . . . . . . . . . . . . . . . 52

4.1 Tools of the fab trade. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

4.2 Resist mask troubleshooting. . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4.3 Double-angle evaporation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

4.4 SlichTECH e-beam evaporator and NRC thermal evaporator. . . . . . . . . 61

4.5 O 2 plasma cleaning to remove the black veil of death. . . . . . . . . . . . 63

4.6 Measured loss tangent of microlab SiN _x_ . . . . . . . . . . . . . . . . . . . . . 64

4.7 Transmon samples. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

4.8 Paramp sample. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

5.1 Sample boxes and launches. . . . . . . . . . . . . . . . . . . . . . . . . . . . 69


-----


vi

5.2 VeriCold dilution refrigerator and sample boxes. . . . . . . . . . . . . . . . 71

5.3 Flux bias noise from a Keithley sourcemeter. . . . . . . . . . . . . . . . . . 72

5.4 Circulators and microwave switches. . . . . . . . . . . . . . . . . . . . . . . 75

5.5 Microwave roach motel filters. . . . . . . . . . . . . . . . . . . . . . . . . 77

5.6 Hot/cold load setup for calibrating noise temperature. . . . . . . . . . . . . 79

6.1 Paramp sample box. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

6.2 Typical paramp tuning with flux. . . . . . . . . . . . . . . . . . . . . . . . . 86

6.3 Paramp transfer function. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87

6.4 Paramp phase response. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

6.5 Paramp gain and bandwidth. . . . . . . . . . . . . . . . . . . . . . . . . . . 90

6.6 Unusual gain profile. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

6.7 Paramp noise measurement scheme. . . . . . . . . . . . . . . . . . . . . . . 92

6.8 System noise temperature with paramp. . . . . . . . . . . . . . . . . . . . . 93

6.9 Saturated regime paramp response. . . . . . . . . . . . . . . . . . . . . . . . 94

6.10 Avoided crossing of qubit and resonator. . . . . . . . . . . . . . . . . . . . . 95

6.11 Qubit punchout calibration. . . . . . . . . . . . . . . . . . . . . . . . . . . 96

6.12 Qubit coherence measurments: Rabi, Ramsey and _T_ 1 . . . . . . . . . . . . . 98

6.13 Purcell eect. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

6.14 Quantum state tomography. . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

6.15 ac Stark shift and photon number calibration. . . . . . . . . . . . . . . . . . 102

7.1 Base temperature apparatus. . . . . . . . . . . . . . . . . . . . . . . . . . . 108

7.2 Overview of experimental setup. . . . . . . . . . . . . . . . . . . . . . . . . 109

7.3 Individual measurement traces. . . . . . . . . . . . . . . . . . . . . . . . . . 110

7.4 Jumps with varied state preparation. . . . . . . . . . . . . . . . . . . . . . . 111

7.5 Histograms of many individual traces. . . . . . . . . . . . . . . . . . . . . . 113

7.6 Jump times and population decay. . . . . . . . . . . . . . . . . . . . . . . . 114

7.7 Jumps with simultaneous readout and excitation. . . . . . . . . . . . . . . . 114

7.8 Quantum jumps with and without paramp. . . . . . . . . . . . . . . . . . . 116

7.9 Three-level jumps. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

7.10 Paramp biasing for three-level jumps. . . . . . . . . . . . . . . . . . . . . . 118

7.11 Readout signal cartoon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

7.12 Readout SNR. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

8.1 Optimal smoothing of time traces. . . . . . . . . . . . . . . . . . . . . . . . 128

8.2 Hysteretic data thresholding. . . . . . . . . . . . . . . . . . . . . . . . . . . 129

8.3 Automated qubit state determination. . . . . . . . . . . . . . . . . . . . . . 131

8.4 State diagram for finite bandwidth detection. . . . . . . . . . . . . . . . . . 132

8.5 Expected dwell time distributions. . . . . . . . . . . . . . . . . . . . . . . . 133

8.6 Log-likelihood in parameter space. . . . . . . . . . . . . . . . . . . . . . . . 140

8.7 Performance of automated state extraction algorithm. . . . . . . . . . . . . 143

8.8 Spurious qubit state mixing. . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

8.9 Transmon qubit and resonator with fast flux line. . . . . . . . . . . . . . . . 147

8.10 Spurious excitation and qubit spectroscopy. . . . . . . . . . . . . . . . . . . 149


-----


vii

8.11 Spurious excitation with coherent fast flux tone. . . . . . . . . . . . . . . . 150

8.12 Qubit population with no fast flux tone. . . . . . . . . . . . . . . . . . . . . 151

8.13 Qubit population with added noise. . . . . . . . . . . . . . . . . . . . . . . . 153

8.14 Spectral density of flux noise vs frequency. . . . . . . . . . . . . . . . . . . . 154

8.15 Quantum Zeno eect. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

9.1 Preliminary TWPA performance. . . . . . . . . . . . . . . . . . . . . . . . . 164

A.1 Roach filter stripline geometry. . . . . . . . . . . . . . . . . . . . . . . . . . 183

A.2 Permittivity and permeability of Eccosorb MFS-117. . . . . . . . . . . . . . 184

A.3 Millikelvin S-parameters of roach filters. . . . . . . . . . . . . . . . . . . . . 185

A.4 Thermalization measurement setup. . . . . . . . . . . . . . . . . . . . . . . 186

A.5 Thermalization measurement. . . . . . . . . . . . . . . . . . . . . . . . . . . 187

C.1 Fast flux noise generation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193

C.2 Typical room temperature wiring. . . . . . . . . . . . . . . . . . . . . . . . 194

C.3 Fridge wiring for Chapter 7 experiments. . . . . . . . . . . . . . . . . . . . . 195

C.4 Fridge wiring for Chapter 8 experiments. . . . . . . . . . . . . . . . . . . . . 196


-----


viii

# List of Symbols and Abbreviations

_a,_   _a_ __ photon/harmonic oscillator annihilation and creation operators

_A_ _s_ _||_ _, A_ _s_ _?_ in-phase and quadrature amplitudes of LJPA input signal

_A_ 0 _, A_ pump unmodulated and modulated LJPA pump amplitude

_B_ noise bandwidth

_B_ det detection bandwidth

_B_ LJPA instantaneous half-width half-maximum bandwidth of LJPA

_C_ capacitance

_C_ _B_ transmon shunt capacitance

_C_ cav readout cavity capacitance

_C_ _g_ transmon gate capacitance

_C_ _J_ junction capacitance

_C_  total transmon capacitance

_e_ elementary charge

_E_ _C_ charging energy _e_ 2 _/_ 2 _C_ 

_E_ _J_ Josephson energy ~ _I_ 0 _/_ 2 _e_

_E_ _m_ _, E_ _i_ energy of _m_ th or _i_ th transmon level


_E_ 01 transmon qubit energy _E_ 1 _E_ 0
__

_f_ dimensionless LJPA signal detuning frequency _f_ =

2 _Q_ ( _!_ _s_ _/!_ _p_ 0 )

_f_ _q_ qubit frequency

_f_ _'_ dephasing noise in control parameter


-----


ix

_f_ 3dB filter 3 dB corner frequency

_F_ single-shot measurement fidelity

_g_ qubit-cavity coupling strength (taken to be _g_ 01 if no subscript
is specified)

_g_ _ij_ qubit-cavity coupling strength for transitions between qubit
states _|_ _i_ _i_ and _|_ _j_ _i_

_G_ amplifier power gain

_G_ _s_ _, G_ _i_ signal and idler power gain of parametric amplifier

_H_ cav readout cavity Hamiltonian

_H_ int interaction Hamiltonian

_H_ meter meter Hamiltonian

_H_ qubit _, H_ _q_ qubit Hamiltonian

~ reduced Plancks constant

_|_ _i_ _i_ _i_ th eigenstate of transmon qubit

_|_ 0 _i_ _,_ _|_ 1 _i_ _,_ _|_ 2 _i_ lowest three transmon eigenstates

_I_ current

_I_ _c_ critical current of a two-junction SQUID

_I_ _d_ paramp drive current

_I_ 0 critical current of a Josephson junction

_k_ LJPA bandwidth scaling factor

_k_ _B_ Boltzmanns constant

_K_ _i_ multilevel Kerr shift

_L_ inductance

_L_ log-likelihood function

_L_ _J_ Josephson inductance

_L_ _J_ 0 zero-current Josephson inductance

_L_ likelihood function

_m_ mass

_n_  Cooper pair number operator


-----


_n_ _g_ gate charge Cooper pair oset for transmon and Cooper pair
box

_n_  mean cavity photon occupation

_n_ cens number of censored observations

_n_ crit mathematical limit of dispersive approximation _n_ crit =

 2 _/_ 4 _g_ 2

_n_  _e_ mean cavity photon occupation, excited state

_n_  _g_ mean cavity photon occupation, ground state

_n_  res mean cavity photon occupation, driven on resonance

_p_  momentum operator

_P_ _c_ critical power for bifurcation of the LJPA

_P_  fast flux excitation power

_p_ _i_ generalized Hamiltonian momentum

_P_ out power output from reflection geometry resonator

_P_ rad power radiated from resonator

_Q,_ _Q_  capacitor charge, capacitor charge operator

_Q_ resonator quality factor

_Q_ int _, Q_ ext internal and external resonator quality factors

_q_ _i_ generalized Hamiltonian coordinate

_R_ _n_ normal state resistance of tunnel junction

_S_ ( _!_ ) noise power spectral density

_S_ _!_ _q_ ( _!_ ) power spectral density of qubit frequency fluctuations



1 _/_ 2
_S_  ( _!_ ) flux noise amplitude spectral density

_S_ _i_ multilevel ac Stark shift

_s_ _hi_ _, s_ _lo_
high and low voltage states for qubit state extraction algorithm

SNR meas measured signal-to-noise ratio

_T_ temperature

_T_ e _, T_ _s_ eective temperature of source impedance


-----


xi

_T_ _H_ _, T_ _L_ temperature of hot and cold loads for noise calibration

_T_ _n_ _, T_ _n,i_ amplifier noise temperature

_T_ sys system noise temperature of amplification chain

_T_ 1 qubit relaxation time

_T_ 2 qubit dephasing time

_T_ _'_ qubit pure dephasing time

_U_ energy stored in a Josephson junction

_V_ voltage

_V_ _C_ voltage across a capacitor

_V_ _d_ drive voltage

_V_ _e,t_ _, V_ _g,t_
output voltages from transmission mode cavity for qubit excited and ground states

_V_ _g_ gate voltage for transmon and Cooper pair box

_V_ _h_ _, V_ _l_ _, V_ _mid_
hysteretic threshold voltages for automated qubit state extraction algorithm

_V_ in _, V_ out voltages of incoming and outgoing waves from LJPA

_V_ _J_ voltage across Josephson junction

_V_ _L_ voltage across an inductor

_V_ out _,_ r output voltage from reflection mode cavity

_V_ _s_ signal voltage

_V_ sig _,_ _r_ _, V_ sig _,_ _t_
readout signal voltage in reflection and transmission geometries


_V_


rms 0 zero-point voltage of the readout cavity _V_ 0


rms 0 =


~ _!_ cav _/_ 2 _C_


_x_  position operator

_Y_ Y-factor of hot/cold load test

_Z_ resonator impedance

_Z_ 0 microwave shunt impedance for LJPA

__ qubit anharmonicity

_, _ _|_ 0 _i_ _, _ _|_ 1 _i_ _, _ _|_ 2 _i_ complex cavity amplitude and its value corresponding to
qubit states _|_ 0 _i_ , _|_ 1 _i_ , and _|_ 2 _i_


-----


xii

__ transmon capacitance ratio __ = _C_ _g_ _/C_ 

__ resultant vector between readout cavity pointer states

__ phase dierence across Josephson junction

__  phase operator (conjugate to number operator  _n_ )

__ _, _ quadrature amplitudes for solutions of driven LJPA
_||_ _?_

tan __ dielectric loss tangent

( _T_ ) temperature-dependent superconducting gap

 qubit cavity detuning (angular frequency): = _!_ _q_ _!_ cav ,
__
equivalent to  0


 _i_ qubit-cavity detuning (angular frequency) for _i_ th
qubit transition  _i_ = ( _!_ _i_ +1 __ _!_ _i_ ) __ _!_ cav

__ purc Purcell relaxation rate __ purc = _g_ 2 _/_  2

__ _q_ ac-Stark-broadened qubit linewidth

 _,_  qubit state transition rates
_"_ _#_

 _"#_ _,_ DD qubit dressed dephasing transition rates

 _A_ _,_  _B_ transition rates between states _A_ and _B_
of a Poissonian twolevel system

 _d_ measurement-induced dephasing rate

 det _,_   det detection bandwidth and its maximum likelihood estimate

 dn _,_   dn
rate of downward state transitions and its maximum likelihood estimate

 jump total rate of qubit state transitions

 _m_ measurement rate

 Rabi Rabi decay rate

 up _,_   up rate of upward state transitions and its maximum likelihood
estimate

 1 qubit relaxation rate

 2 qubit dephasing rate

 _'_ qubit low-frequency pure dephasing rate

__ solution for small signal perturbation on LJPA drive


-----


xiii

__ parameterization variable for jump time probability distribution __ =  up +  dn +  det

__ _i_ ratio of coupling to detuning for _i_ th transmon level __ _i_ =
_g_ _i,i_ +1 _/_  _i_

__ cavity linewidth (angular frequency)

__ flux-to-qubit-frequency transfer coefficient

__ density matrix


__ dimensionless LJPA drive amplitude __ = _Q_ 0 2 _/_ 8

__ max drive amplitude for maximum LJPA gain at zero detuning

__  _x_ _,_  __ _y_ _,_  __ _z_ Pauli operators for qubit


__  + _,_  __ __ qubit raising and lowering operators

_,_ __  parameter of statistical distribution and its maximum likelihood estimate


__ up

2

parameterization variable for jump time probability distribution, __ up = __ __ 4 up  det


__ dn

2

parameterization variable for jump time probability distribution __ dn = __ __ 4 dn  det

__ cavity pull p

 _,_   branch flux, branch flux operator

 app applied magnetic flux

 0 flux quantum _h/_ 2 _e_

__ 1/2 of linear dispersive shift (angular frequency)

__ _ij_ transmon partial dispersive shift (angular frequency)

__ 01 transmon lamb shift (angular frequency)

_|_ _i_ general qubit state

_!_ _c_ critical frequency for bifurcation of the LJPA

_!_ cav bare cavity resonant frequency

_!_  cav qubit-state-dependent cavity resonant frequency

_!_ _d_ drive frequency

_!_  fast flux excitation frequency


-----


xiv

_!_ _i_ frequency of _i_ th transmon state _E_ _i_ _/_ ~

_!_ _ij_ frequency of splitting between _i_ th and _j_ th transmon states

_!_  _ij_ Lamb-shifted frequency of splitting between _i_ th and _j_ th
transmon states

_!_ _p_ pump frequency

_!_ _p_ 0 LJPA linear resonant frequency

_!_ _q_ qubit frequency

_!_ ro readout frequency

_!_ _s_ signal detuning frequency from pump

_!_ sig _, !_ id signal and idler frequencies

 dimensionless drive detuning for LJPA = 2 _Q_ (1 _!_ _d_ _/!_ _p_ 0 )
__

 Rabi _,_  Rabi frequency, Rabi frequency at zero detuning

CPB Cooper pair box

DD dressed dephasing

JC Jaynes-Cummings

LJPA lumped Josephson parametric amplifier

QED quantum electrodynamics

SNR signal-to-noise ratio

SQUID superconducting quantum interference device

TWPA traveling wave parametric amplifier


-----


xv

###### Acknowledgments

There are many people who played a role in the success of this thesis, and I would

like to acknowledge and thank them.

I would first like to thank my advisor, Prof. Irfan Siddiqi. Irfan has taught me

an enormous amount, on topics such as the inner workings of dilution refrigerators, the
nuances of microwave electronics and measurements, how to give a successful talk, and the
virtues of patience and perseverance when dealing with complex experiments. Irfan created
a warm and collegial atmosphere in QNL which made it a pleasure to work there, and I
always felt I could come to him with scientific questions and have an interesting discussion.
He personally taught me to fabricate samples and understand microwave techniques, back
when the lab was very first starting. I am very grateful for the support Irfan has given
me over my graduate career. I would like to thank him as well as the rest of my thesis
committee for their extensive and thoughtful comments on this document.

I have been fortunate to work with a number of excellent graduate students and

postdocs in my time at Berkeley, and they have enriched my experience enormously. I would
like to especially thank Dr. R. Vijay and Dr. Ofer Naaman, the two postdocs with whom
I worked during my time in QNL. The work in this thesis was carried out in very close
collaboration with Vijay, who taught me a great deal about the subtleties of microwave
experiments and the fine points of quantum measurement theory. I have enjoyed our many
sessions together discussing outlandish experimental ideas and doping out the meaning of
confusing or unexpected results. He has been a superb collaborator as well as a dear friend.
I worked with Dr. Ofer Naaman during the earlier stages of my career at QNL. Ofer did
the wiring in our dilution fridge and taught me about all of the various pitfalls associated
with this difficult activity. Ofer helped me a great deal developing and measuring the

roach filters. In addition to Vijay and Ofer, my work at UC Berkeley has been done in the
company of many other hardworking and lively physicists, from whom I learned a great deal
about physics and life. I would like to especially thank Kater Murch, Andy Schmidt, Eli
Levenson-Falk, Ned Henry, Natania Antler, Steve Weber, Chris Macklin, Michael Hatridge,
Sarah Busch, Jed Johnson, and Emile Hoskinson. The work in this thesis was done with
the help of numerous collaborators at other institutions as well. I would like to thank Dr.
Joe Aumentado at NIST for his enthusiastic assistance with the design of the SlichTECH
evaporator, a project I could not have completed by myself. Dr. Jay Gambetta, Prof.

Rob Schoelkopf, Prof. Michel Devoret, and Prof. Steve Girvin have all provided insightful
comments and lively discussion on issues related to understanding quantum jumps. Dr.
Gambetta, Prof. Alexandre Blais and Maxime Boissonneault have also been very helpful
in collaborating with us on the dressed dephasing work.

I would like to thank several of my past advisors and mentors, who have been

instrumental in bringing me to this point. Prof. Jene Golovchenko at Harvard took me in
to his freshman seminar on experimental physics, where I first learned about the joys and
frustrations of trying to do an experiment nobody else has done before. He later hired me
on as an undergraduate research assistant in his lab, where I learned a great deal about
carbon nanotubes, DNA sequencing, and electron microscopy. Prof. J.C. Campuzano at
the University of Illinois-Chicago hired me to work in his lab when I was between college
and graduate school, trying to decide if I wanted to purse physics further. He gave me an


-----


xvi

enormous boost of confidence, and taught me a lot about ultra-high-vacuum techniques.
Prof. John Clarke at UC Berkeley first introduced me to the world of superconducting
devices, and sparked my interest in high-sensitivity measurements. I will always look back
fondly on my excellent first-year graduate quantum mechanics class, taught with great __ _elan_

by Prof. Robert Littlejohn.

I am deeply grateful to the Fannie and John Hertz Foundation for the graduate

fellowship they awarded me, and to Ray Sidney for endowing that fellowship. The Hertz
Fellowship was a crucial aspect of my success in graduate school; beyond the simple monetary considerations, the Hertz community provided me with encouragement and support,
while opening doors to a wide range of experiences and fields of scientific endeavor. I have
made many lasting friendships with Hertz fellows and alumni, and I am very grateful to the
Foundation for giving me the opportunities it has.

I doubt I would have made it this far without the help of the physics sta, who

work tirelessly to keep everything running smoothly in the department. Special thanks go
to Anne Takizawa, Donna Sakima, and Claudia Trujillo in the student services office, as
well as Anthony Vitan, Eleanor Crump, and Katalin Markus in support services. These
people happily helped me with problems large and small, and I am very thankful to them.

I have been lucky to have a great group of friends here in Berkeley, both from my

incoming physics cohort and elsewhere. I want to thank them for making me laugh and
keeping me sane for the past six and a half years. I will always have fond memories of
Wednesday night dinners, Bay to Breakers, skiing in Tahoe, Big Sur trips, and many other
fun adventures we shared.

Finally, I would like to thank my family, without whom I never would have made it

this far. Mom, Dad, Sumner, Bill, Jacob, Ann, David, and YolandaI have always felt your
unwavering love and support, and it has given me great strength and confidence. Thank
you for your advice, your encouragement, and your enthusiasm for my work. I love you,
and dedicate my thesis to all of you.


-----


## Chapter 1

# Introduction

In the past 30 years, it has become possible to isolate and interrogate individ-

ual quantum systems, allowing a wide variety of experiments on fundamental aspects of
quantum mechanics. Many of these experiments were initially conceived of as _Gedankenexperiments_ in the early days of quantum mechanics, when the technology did not exist to
carry them out in a laboratory. Questions of entanglement, spooky action at a distance,
and the nature of quantum measurement have since transitioned from the realm of theory
into the realm of experiment.

Experiments on the fundamentals of quantum mechanics require controllable quan-

tum systems to use as test beds. Perhaps the simplest quantum system, familiar to any
student of elementary quantum mechanics, is the quantum two-state system, called a quantum bit or qubit for short. The terminology comes from the word bit, used to described
a classical two-state system. A bit could be a flipped coin (heads or tails), a switch (on or
o), or a small magnetic domain on a hard disk (aligned up or down). Crucially, a classical
bit can be in only one of its two possible states at any given time.

In contrast, a qubit can exist in either of its two eigenstates, or in a superposition

of those two eigenstates. In addition, if one has several coupled qubits, it is possible to form
an entangled state of the qubits which cannot be written as a simple product of individual qubit states. Using _n_ classical bits, one can represent just a single _n_ -bit configuration
out of the 2 _n_ possible configurations. By contrast, _n_
_n_
qubits can be placed in an entangled superposition state of all 2 possible configurations with varying complex amplitudes,
a state which can contain exponentially more information than the classical _n_ -bit state.
The enormous dimensionality of the Hilbert space for entangled qubits could theoretically
be harnessed to build a quantum computer capable of solving certain classes of problems
exponentially faster than any classical computer [1]. Such a system could also be used as
a large-scale quantum simulator to study problems in many-body physics or to probe the
quantum-classical boundary [2, 3].

There are a number of physical realizations of quantum two state systems: a spin-

1/2 particle in a magnetic field, two electronic levels of an atom, or two polarizations of
a photon, for example. In this thesis, we are study the quantum properties of engineered
qubits made from superconducting electrical circuits.


-----


#### 1.1 #### Superconducting qubits

Superconducting qubits [4, 5] are quantum two-level systems realized in an electri-

cal circuit by exploiting macroscopic quantum degrees of freedom. The notion that macroscopic variables could behave according to the rules of quantum mechanics was first put
forward in the 1980s by Leggett [6], and subsequent experimental tests demonstrated the
quantum behavior of the macroscopic phase degree of freedom of a Josephson junction [7].
This laid the groundwork for constructing qubits from superconducting Josephson circuits.
In 1999, the research group at NEC in Japan observed coherent oscillations between two
states of definite Cooper pair number on a submicron superconducting island [8], a design
called the Cooper pair box [9]. The oscillations displayed coherence times on the order of 1
ns.

In subsequent years, many dierent superconducting qubit designs have been de-

veloped. Qubits based on macroscopic states of the phase of a Josephson junction [10] or
the circulating currents in a superconducting loop [11], called phase and flux qubits
respectively, came on the scene. An improved Cooper pair box design called the quantronium qubit (shown in Figure 1.1) exhibited reduced sensitivity to environmental noise and
dramatically increased coherence times [12]. A further modified version of the Cooper pair
box, called the transmon qubit, ushered in a new era of reliable qubits with greatly reduced
sensitivity to charge noise [13]. Other new designs promising reduced sensitivity to various
types of noise, rich energy structures, and other exotic features have arrived on the scene
in the past few years, among them the fluxonium qubit [14], the capacitively shunted flux
qubit [15], the tunable coupling qubit [16], and the 3D transmon qubit [17]. In the twelve
years since the original NEC experiments, coherence times have improved by more than
four orders of magnitude; the 3D transmon design currently boasts typical coherence times
approaching 50 __ s.

As the coherence times of superconducting qubits improved, it became possible to

entangle them and use them to perform quantum algorithms. Several groups have performed
experiments demonstrating entanglement among multiple superconducting qubits [18, 19,
20] and violations of Bells inequality [21, 22, 23], providing strong evidence of the inherently
quantum nature of superconducting qubits. Superconducting qubits are easy to manipulate,
tunable, and can be mass produced, opening avenues for creating large-scale engineered
quantum systems. Work is underway to build scalable architectures for implementing a
quantum computer using superconducting circuits [22, 24, 25].

Although superconducting qubit technology has advanced by leaps and bounds

in the past decade, it still lags many competing model quantum systems, such as trapped
ions, on issues of measurement. Until the work presented in this thesis, there had been
no measurement system for superconducting qubits which allowed continuous high-fidelity
monitoring of the qubit state. Without this capability, it had been difficult or impossible
to study the dynamics of superconducting qubits under measurement. In particular, it

was impossible to observe one of the most basic manifestations of the eects of quantum
measurement, namely quantum jumps.


-----


![SlichterThesis.pdf-21-0.png](SlichterThesis.pdf-21-0.png)

Figure 1.1: The quantronium qubit.

This false color image shows a quantronium qubit, a modified Cooper pair box whose qubit
energy can be tuned to a noise-insensitive sweet spot. The Cooper pair box is shown in
red, with qubit control implemented by applying voltages to the gate electrode (blue) and
magnetic fluxes to the qubit loop (yellow). A large Josephson junction used for readout is
shown in green.

#### 1.2 #### Quantum jumps

The notion that quantum systems can evolve by jumping abruptly between

eigenstates was first proposed by Bohr almost a century ago in 1913 [26]. For three quarters
of a century, the concept of quantum jumps remained a purely theoretical curiosity, and
a subject of substantial debate. By the early 1980s, though, advances in atomic physics
allowed for the trapping and cooling of single ions [27, 28], perhaps giving a chance to settle
the question of quantum jumps experimentally. Only a few years later, in 1986, three groups
simultaneously reported the observation of quantum jumps between the electronic states of
individual trapped ions [29, 30, 31]. Data from [29] are shown in Figure 1.2.

Since that time, quantum jumps have been observed in a variety of other systems,

starting with the electronic states of single molecules embedded in a crystal [32]. It was
found that single electrons in cyclotron orbits undergo quantum jumps between Landau
levels [33], and that single microwave photons are suddenly created and annihilated by
thermal processes inside a Fabry-Perot cavity [34]. In solid state systems, quantum jumps
have been observed in a microscopic defect in a Josephson junction [35], while more recently,
work showed that the state of a single nuclear spin in a diamond NV center undergoes
quantum jumps [36], as does the electronic state of an electron in an indium gallium arsenide
quantum dot [37]. Quantum jumps from spin flips of a single trapped proton in a magnetic
field were also reported recently, paving the way for precision tests of matter-antimatter
asymmetry [38].

The observation of quantum jumps requires a quantum non-demolition (QND)

measurement scheme, that is, one which leaves the system in an eigenstate of the measured


-----


![SlichterThesis.pdf-22-0.png](SlichterThesis.pdf-22-0.png)

Figure 1.2: The first observation of quantum jumps.

This figure shows quantum jumps between two electronic states of a single Ba + ion as
determined from the fluorescence of a fast cycling transition between one of the two jump
states and a third state. Note the horizontal time axis. Figure adapted from ref. [29].

observable [39], thus allowing repeated measurements. One must also be able to perform the
measurements on a timescale much faster than that of the qubit dynamics in order to resolve
the jumps. All of the previous quantum jump experiments mentioned above have used

microscopic quantum degrees of freedom with long relaxation times ( __ ms to s), enabling
the observation of quantum jumps even with low-bandwidth measurement techniques.


Superconducting qubits typically have much shorter relaxation times ( __ __ s) on ac-

count of strong coupling to their environment, so the observation of quantum jumps requires
substantially higher measurement bandwidth than in previous quantum jump experiments.
Fortunately, a technique capable of continuous, high-bandwidth readout of a superconducting qubit has been developed. The technique is known as circuit quantum electrodynamics
(circuit QED), and involves dispersively coupling the qubit to a microwave cavity [40].
Circuit QED was developed in direct analogy to the techniques of cavity quantum electrodynamics (cavity QED), a technique used in optics to explore the coupling between atoms
and the electromagnetic field in a Fabry-Perot cavity. In the dispersive regime, where the
frequency of the qubit and the cavity are far detuned relative to the strength of their coupling, the resonant frequency of the cavity depends on the state of the qubit. Probing

the cavity frequency implements a continuous, high visibility QND measurement whose
bandwidth is only limited by the cavity linewidth [41].

Despite successfully demonstrating QND measurement with several kinds of su-

perconducting qubits [14, 42, 43], circuit QED implementations with linear cavities have
typically suered from low single-shot fidelity 1 , precluding the observation of quantum
jumps. This is primarily due to inefficient amplification of the readout photons leaving the
cavity carrying information about the qubit state. The noise added by state-of-the-art cryogenic semiconductor microwave amplifiers is considerably larger than the signal from the
cavity, necessitating repeated state preparation/measurement experiments to resolve the

1 Single-shot fidelity describes the ability to resolve the qubit state faithfully in a single experiment.


-----


qubit state [44]. Using a stronger readout tone to detect the cavity frequency can induce
qubit state mixing [45], thus limiting the fidelity.

Other high fidelity readout schemes exist for superconducting qubits, but they

are not suitable for observing quantum jumps. Latching readouts based on the dynamical
bifurcation of a nonlinear oscillator can provide the desired QND measurement [46, 47], but
the averaging time required to distinguish the qubit state is sufficiently long compared to the
qubit relaxation time that one cannot resolve quantum jump events. Hysteretic switching
readouts involving current-biased Josephson junctions transitioning to the voltage state can
have fidelities better than 90%, but they either destroy the qubit state [48] or again require
too long a reset time for use in measuring quantum jumps [49].

The single-shot fidelity problems of linear cavity circuit QED could be alleviated

if the added noise of the following amplifiers were considerably lower, but no commercial
solution to this problem currently exists. We instead turn to a class of amplifiers called
superconducting parametric amplifiers, long a topic of research but recently the subject of
redoubled eorts driven by the need for low noise amplification of quantum signals.

#### 1.3 #### Superconducting parametric amplifiers

Parametric amplifiers achieve gain by varying a parameter of the amplifier system

harmonically in time. The energy used to vary the parameter is called the pump. The
modulation of the system parameters at the pump frequency causes some of the pump
energy to be transferred into other frequency modes, amplifying signals present in those
modes. Because parametric amplification can occur without any dissipation, it has the

potential to have quantum-limited noise performance [50].

Superconducting parametric amplifiers based on the nonlinear Josephson induc-

tance were first demonstrated in 1975 [51]. A number of superconducting parametric amplifier designs followed in the 1980s and 1990s [52, 53, 54, 55, 56], but they tended to be
plagued by spurious noise rise and were not used broadly in applications. However, the
rapid progress in solid-state quantum measurement and quantum information of the past
decade has renewed interest in superconducting parametric amplifiers. A number of recent
results [57, 58, 59, 60] have demonstrated quantum-limited noise performance and high gain
using new amplifier designs.

One of the main limiting factors on the use of parametric amplifiers has been their

signal bandwidth, which was typically of order 1 MHz or less. The most recent designs,
including the one discussed in this thesis, have instantaneous bandwidth on the order of
10 MHz or greater, making them suitable for amplifying qubit readout signals [59, 60, 61].
The key is to lower the quality factor _Q_ of the amplifier resonator, which allows larger
bandwidth without sacrificing gain.

With this large bandwidth, quantum-limited noise, and high gain, we finally have

the device we need to amplify the circuit QED readout signal. The stage is set for continuous
monitoring of the state of a superconducting qubit and the observation of quantum jumps.


-----


#### 1.4 #### Thesis overview

The thesis begins with a brief introduction to superconducting qubits in Chapter

2, giving some information on the quantization of electrical circuits and the Hamiltonian
for our qubit of choice (the transmon) and its solutions. It then describes the circuit QED
system, how this system can be used to realize a QND measurement of the qubit state, and
how the readout signal manifests itself.

Chapter 3 discusses basic ideas of amplification and noise, including a derivation

of the quantum limit for the noise performance of an amplifier. The chapter goes on to
describe some basic features of parametric amplification, followed by some detailed theory
of our particular realization of superconducting parametric amplifier, called the Lumped
Josephson Parametric Amplifier or LJPA. We provide mathematical expressions for the
performance as well as a physical description of the amplification mechanism.

To close the first half of the thesis, Chapters 4 and 5 give details on the fabrication

of the qubit and amplifier samples, as well as the experimental methods used to interrogate
the samples.

The second half of the thesis, Chapters 6 to 8, consists of experimental results.

First, we detail the experimental performance of the LJPA in Chapter 6, describing the
procedures for correctly biasing the amplifier and giving measurements of its gain and noise.
We also present a series of tests and calibrations used to determine important properties
of the qubit/cavity system such as the qubit energy structure and coherence times, the
qubit-cavity coupling, and the measurement strength.

In Chapter 7, we present some theoretical and historical background on quantum

jumps before detailing the experiments carried out to observe them in a superconducting
qubit. The chapter contains information on a variety of test experiments used to demonstrate that the jumps seen are in fact those of the superconducting qubit, and closes with a
discussion of the signal-to-noise ratio and measurement fidelity achieved with our readout
technique.

The penultimate chapter, Chapter 8, describes the experiments done to examine

measurement backaction. It begins with a description of the automated qubit state extraction algorithm used to process individual time trace data into useful ensemble metrics. The
phenomenon of spurious qubit state mixing during measurement is detailed and a theoretical framework is presented to explain this behavior. We then show experimental data
supporting the theory, finding that flux noise well below the qubit Larmor frequency is the
root cause of the observed spurious state mixing. The experiment allows us to measure the
spectral density of flux noise at frequencies around 1 GHz. Finally, we show data illustrating
the quantum Zeno eect, where the presence of strong measurement inhibits the evolution
of the qubit.

After discussions of potential future work and extensions of the thesis, including

quantum error correction and feedback, single-photon sources and detectors, and improved
qubits and parametric amplifiers, we give some brief conclusions in Chapter 9.


-----


#### 1.5 #### Summary of key results

The work presented in this thesis represents the first observation of quantum jumps

in a macroscopic quantum degree of freedom, a superconducting qubit [62]. It provides
further evidence of the quantum nature of superconducting qubits, which had been shown
previously through entanglement and violation of Bells inequality. A variety of tests show
that the observed jumps are indeed quantum jumps of the qubit. The experiment relies
crucially on the high bandwidth and quantum-limited noise performance of the LJPA.

With the capability to perform continuous qubit state monitoring, we look at qubit

dynamics during measurement using state extraction from many single-shot time traces. We
develop mathematical methods to estimate the qubit state accurately from individual measurement traces and retrieve both single-shot and ensemble dynamics in presence of noise
and bandwidth limitations. Using these methods, we examine the backaction of measurement in two phenomena. The first phenomenon, spurious qubit state mixing, is found to
result from the upconversion of low-frequency flux noise to noise at the qubit frequency due
to the presence of measurement photons. We use the measurements of spurious excitation
to estimate the flux noise power spectral density at frequencies around 1 GHz, a region
previously inaccessible to experiments, and show that the spectrum of flux noise appears to
obey a 1 _/f_ __ power law over 11 decades in frequency. The second phenomenon displaying
measurement backaction is the quantum Zeno eect, where the presence of strong measurement inhibits qubit state evolution. We show that our qubit system exhibits quantum Zeno
behavior with scalings roughly commensurate with those predicted by theory.


-----


## Chapter 2

# Superconducting qubits and circuit quantum electrodynamics

This chapter is intended to give an introduction to superconducting qubits, in

particular the transmon qubit, and to describe basic principles and phenomena of circuit
quantum electrodynamics (circuit QED). We will demonstrate how circuit QED can be
used to measure the state of a qubit, and how to extract the theoretical parameters of a
qubit-cavity system from experimental measurements.

Superconducting qubits and circuit QED have been the subjects of a great deal

of work in recent years, and there are a number of excellent sources for finding information
in greater detail than presented here. For more on superconducting qubits, the reader is
directed to several recent review articles by Siddiqi [4], Clarke and Wilhelm [5], and You
and Nori [63]. A nice introduction to circuit QED is presented in Dave Schusters thesis

[64], and subsequent theses from the Yale group detail various extensions to multiple qubits
and microwave quantum optics.

#### 2.1 #### Qubits and quantum information

A qubit, short for quantum bit, is a quantum two-state system. This terminology

comes from the word bit, used to described a classical two-state system and commonly
used in information theory and computer science. A bit could be a flipped coin (heads or
tails), a switch (on or o), or a small magnetic domain on a hard disk (aligned up or down).
A bit can be in only one of its two possible states at any given time. A series of _n_ classical
bits has 2 _n_ possible configurations, but can only be in one of those configurations at a given
time.

Qubits, on the other hand, can exist in either of its two eigenstates, or in a su-

perposition of those two eigenstates. In addition, if one has multiple coupled qubits, it is
possible to form states which cannot be written as product states of the individual qubits.
For example, given two qubits labeled _a_ and _b_ , the two-qubit state


_|_  + _i_ =


_|_ 0 _i_ _a_ _|_ 0 _i_ _b_ + _|_ 1 _i_ _a_ _|_ 1 _i_ _b_


(2.1)


-----


Energy


Energy Energy

![SlichterThesis.pdf-27-8.png](SlichterThesis.pdf-27-8.png)

![SlichterThesis.pdf-27-9.png](SlichterThesis.pdf-27-9.png)

![SlichterThesis.pdf-27-6.png](SlichterThesis.pdf-27-6.png)

![SlichterThesis.pdf-27-7.png](SlichterThesis.pdf-27-7.png)

![SlichterThesis.pdf-27-2.png](SlichterThesis.pdf-27-2.png)

![SlichterThesis.pdf-27-10.png](SlichterThesis.pdf-27-10.png)

![SlichterThesis.pdf-27-4.png](SlichterThesis.pdf-27-4.png)

![SlichterThesis.pdf-27-5.png](SlichterThesis.pdf-27-5.png)

Figure 2.1: Quantum two-level systems.


 z

![SlichterThesis.pdf-27-11.png](SlichterThesis.pdf-27-11.png)

![SlichterThesis.pdf-27-0.png](SlichterThesis.pdf-27-0.png)

spin 1/2


![SlichterThesis.pdf-27-1.png](SlichterThesis.pdf-27-1.png)

![SlichterThesis.pdf-27-3.png](SlichterThesis.pdf-27-3.png)

The canonical qubit is a spin-1/2 particle in a magnetic field, with the energy level spacing
given by the Zeeman splitting. Any quantum two-state system can be mapped on to this
model. Systems with more than two quantum states can act as qubits if they are restricted
to be in a two-level subspace. In this way, qubits can be realized using two electronic energy
levels of a single atom or two energy levels of a quantized electrical circuit.

cannot be written as a product of states of _a_ and _b_ in isolation. This type of non-separable
state is called an entangled state 1 . Given _n_
_n_
qubits, one can create entangled states consisting of linear combinations of all 2 possible _n_ -bit configurations, with a dierent complex
amplitude for each of the 2 _n_ terms. Such a state can contain exponentially more information
than a classical _n_ -bit state. By realizing a computer relying on qubits rather than classical
bits, it may be possible to harness this exponentially large state space to carry out certain
computations at speeds far exceeding that of even the most powerful classical computer [1].
Quantum computers have been theoretically shown to provide an exponential speedup for
the prime factorization of large numbers [65], as well as a quadratic speedup for search on
unsorted data [66].

Qubits are also interesting because they are one of the simplest test beds for

studying the behavior of quantum systems. The classic example of a quantum two-state
system, a spin-1/2 particle in a magnetic field, is a ubiquitous pedagogical tool in quantum
mechanics textbooks. Many of the unexpected features of quantum mechanics are first laid
out for students in _Gedankenexperiments_ involving a Stern-Gerlach apparatus and a beam
of spin-1/2 particles. However, for decades such experiments were destined to remain purely
theoretical.

In the past 30 years, it has become possible to isolate and interrogate individual

quantum systems, allowing a wide variety of experiments on fundamental aspects of quantum mechanics. A great variety of quantum two-level systems have been used as test beds
in these eorts. Three examples are shown in Figure 2.1: a spin-1/2 particle in a magnetic
field, two electronic levels of an atom, and two macroscopic quantum states of an electrical
circuit. It is on this third type of qubit that this thesis will focus. In the next sections, we
describe how an electrical circuit can be thought of as a qubit.


1 The particular entangled state _|_  + _i_ given here is a type of maximally entangled two-qubit state called

a Bell state.


-----


10

###### 2.1.1 ###### Quantization of an electrical circuit

If we would like to make a qubit from an electrical circuit, we must describe

the circuit in quantum mechanical terms. In this section, we will demonstrate how to

quantize an electrical circuit using the example of an LC resonator, one of the simplest
electrical circuits. The classical variables used to describe the classical LC resonator will
be transformed into operators in the quantum version. This derivation and its attendant
methods are described in thorough and rigorous detail in refs. [67, 68].

In a lossless parallel LC resonator, the voltages across the inductor and capacitor

are equal, by Kirchos laws. The voltage can be expressed either in terms of the inductance
or the capacitance (we adopt the sign convention that the positive current direction and
positive voltage direction across a component are opposite, and choose relative voltage
orientations such that _V_ _L_ = _V_ _C_ ):

_V_ _C_ = _Q/C, V_ _L_ = _L_ _I._  (2.2)


Here _Q_ is the charge on the capacitor and _I_ is the current through the inductor, which
because of our choice of sign convention is given by _I_ = __ _Q_  , where the dot denotes dier-

entiation with respect to time. For reasons that will become clear, we choose to define a
quantity for the inductor called the branch flux , which is given by the time integral of
the voltage across the inductor:


Z _t_ _1_


 =


_V_ ( _t_ _0_ ) _dt_ _0_ = _LI._ (2.3)


This voltage integral uses the boundary condition that all voltages and currents are zero at
time _t_ = _1_ . We can write the energy stored in the LC resonant circuit as:



1
_E_ =



1 _LI_ 2 + 1

2 2


2 _CV_ _C_ 2


_C_ 2 _,_ (2.4)


which we can express as a Hamiltonian using the branch flux defined above, giving the form



 2
_H_ =



 2 2

+ _Q_
2 _L_ 2



_._ (2.5)
2 _C_


A Hamiltonian is parameterized by generalized coordinates _q_ _i_ and momenta _p_ _i_ , which are
said to be canonical if they obey the relation given by the Hamilton equations:


_@H_

_@q_ _i_

_@H_

_@p_ _i_


= _p_  _i_ (2.6)
__

=  _q_ _i_ _._ (2.7)


Applying these expressions to (2.5), we can see that the branch flux  and charge _Q_ act as
canonical coordinate and momentum variables respectively:


_@H_

=  _/L_ = _I_ = _Q_  (2.8)
_@_  __


-----


11


_@H_

= _Q/C_ = _L_  _I_ =   _,_ (2.9)
_@Q_


_@H_


where we have used the relations from (2.2) and (2.3). Since  and _Q_ are canonical variables,
we can quantize them by converting them to quantum mechanical operators  and  _Q_  , which

will obey the commutation relation

[   _,_ _Q_  ] = _i_ ~ _._ (2.10)

Having quantized the Hamiltonian of this LC resonator, we can map it to the Hamiltonian
of a particle moving in a harmonic potential, which is given by


_p_ 
_H_ =


_p_  2 + 1

2 _m_ 2



_m!_ 2 _x_  2 _._ (2.11)
2


If we take equation (2.5) and make the correspondences _Q_  _!_  _p_ ,   _!_  _x_ , _m_ _!_ _C_ , and


1 _/_


_LC_ _!_ _!_ , we find that it maps directly on to equation (2.11), showing that an LC


circuit can be quantized as a harmonic oscillator. It is usual to express the Hamiltonian of
a quantum harmonic oscillator in terms of dimensionless annihilation and creation operators:



1
_H_ = ~ _!_ ( _a_ __ _a_  + ) _,_ (2.12)

2



1
_H_ = ~ _!_ ( _a_ __ _a_  +


where the annihilation operator is given by


_a_  =


2 ~ _Z_


(  +  _iZ_ _Q_  ) _,_ (2.13)


using the definition of the resonator impedance _Z_ =


_L/C_ . The expected value of the LC


circuits energy is just equal to the number of photons at the resonant frequency multiplied
by the energy per photon, plus a half-photon zero-point term. Our model is for a lossless
LC circuit in isolation, whereas a real physical system will be coupled to other degrees
of freedom and sources of dissipation. We can model dissipation in a natural way using
input-output theory by coupling the LC circuit to an external continuum bath of harmonic
oscillator modes. We will not discuss this here, but instead direct the reader to references

[69] and [70], both of which give clear and detailed accounts on the subject.

###### 2.1.2 ###### Superconducting qubits

Having shown how to quantize an electrical circuit, we can now examine how to

make an electrical circuit into a qubit 2 . A harmonic oscillator at low temperatures such that
~ states _!_ __ 3 _k_ . If we could change the state back and forth between the ground state and first _B_ _T_ will be primarily in the ground state, with little to no population in its excited
excited state by applying radiation at frequency _!_ , we would have a qubit. Unfortunately,
the states of a harmonic oscillator are all evenly spaced in energy, so any radiation that

2 A somewhat more detailed description of the following arguments can be found in ref. [71].
3 Technically, we mean that the density matrix of the harmonic oscillator is such that the probability of

measuring it to be in a state other than the ground state is very small.


-----


12

![SlichterThesis.pdf-30-2.png](SlichterThesis.pdf-30-2.png)

Flux (  )



![SlichterThesis.pdf-30-7.png](SlichterThesis.pdf-30-7.png)

![SlichterThesis.pdf-30-6.png](SlichterThesis.pdf-30-6.png)

![SlichterThesis.pdf-30-5.png](SlichterThesis.pdf-30-5.png)

![SlichterThesis.pdf-30-0.png](SlichterThesis.pdf-30-0.png)

![SlichterThesis.pdf-30-1.png](SlichterThesis.pdf-30-1.png)

![SlichterThesis.pdf-30-4.png](SlichterThesis.pdf-30-4.png)

Flux (  )


![SlichterThesis.pdf-30-3.png](SlichterThesis.pdf-30-3.png)

Figure 2.2: Energy levels of quantized oscillators.

Panel (a) shows the potential (black) as a function of branch flux for a lossless harmonic
oscillator. The energy levels (red and blue) are equally spaced. If we add loss to the

harmonic oscillator, the levels broaden as shown in (b). An anharmonic oscillator with a
non-parabolic potential, such as the softening potential in (c), has unequally spaced energy
levels. The potential and energy levels of a harmonic oscillator with the same lowest-

level energy spacing are shown as dashed lines to highlight the uneven level spacing of the
anharmonic oscillator.

drives a transition between the ground and first excited states would also drive transitions
between all of the other levels as well, as shown in Figure 2.2(a). This means that the
harmonic oscillator is unsuitable for use as a qubit; we require instead an electrical circuit
with uneven spacing between energy levels, an anharmonic oscillator.

We should also consider the presence of dissipation. Real electrical circuits have

loss, which we have so far ignored in our calculations. Loss causes decay of the quantum
state of the circuit, so we would like to be able to minimize it. In circuit language, loss
occurs in the presence of a real (rather than an imaginary) shunt impedance, such as a
resistance. One way to create circuits with low loss is to make them from superconducting
elements, which have zero resistance in the limit of zero frequency.

We have determined that in order to make a qubit out of an electrical circuit,

we should create an anharmonic (nonlinear) oscillator which operates at low temperature
( ) and with low loss. One would ideally make such a circuit using superconductors. Fortunately, a lossless nonlinear circuit element exists for superconductors: the ~ _!_ __ _k_ _B_ _T_
Josephson junction. A Josephson junction is composed of two superconductors coupled by
a weak link, in our case a thin insulating barrier . The junction can support a dissipationless supercurrent of any magnitude up to a certain limit called the critical current, which 4
depends on the geometry of the junction and on the superconducting material. We can
describe the behavior of a Josephson junction with a pair of constitutive relations known
as the Josephson relations [72]:

_I_ = _I_ 0 sin __ (2.14)

4 A Josephson weak link can also be made using a superconducting constriction or a layer of non-

superconducting metal [72].


-----




_V_ =

2 __




_V_ =


13

_._  (2.15)


Here _I_ is the supercurrent through the Josephson junction, _I_ 0 is the critical current, _V_ is the
voltage across the junction,  0 is the flux quantum _h/_ 2 _e_ , and __ is the dierence between the
phases of the superconducting order parameter on each side of the junction. Even though
__ depends on the behavior of many individual electrons, it has been shown experimentally
to behave as a single macroscopic quantum degree of freedom [7].

If we combine the two Josephson relations, we find the junction has a relation

between the voltage and the time derivative of the current, in other words, an inductance.
The Josephson inductance is given by


 0
_L_ _J_ =


 0 _L_ _J_ 0

2 _I_ 0 cos __ __ cos



_,_ (2.16)
cos __


defining _L_ _J_ 0 __  0 _/_ 2 _I_ 0 as the Josephson inductance in the absence of supercurrent flow.
We can use (2.14) and trigonometric identities to express the Josephson inductance as


_L_ _J_ 0
_L_ _J_ = (2.17)

1 ( _I/I_ 0 ) 2 _._
__

This form highlights the dependence of the Josephson inductance on the current in the p
junction. This nonlinear inductance can be harnessed to make an anharmonic oscillator.

One can construct a tunable Josephson inductance using a superconducting loop

interrupted by two junctions. This configuration is called a dc Superconducting QUantum
Interference Device, or dc SQUID [73]. This nomenclature exists for historical reasons;

there is nothing intrinsically low-frequency about a dc SQUID, which can happily exhibit
dynamics at tens of GHz. In the presence of a magnetic flux inside the SQUID loop, a
circulating current is set up which reduces the eective critical current of the SQUID. In
the limit where the loop inductance _L_ is much smaller than the Josephson inductances _L_ _J_ 0
of the individual junctions, the critical current _I_ _c_ of the SQUID can be expressed in terms
of the applied magnetic flux bias  app as [73]


__  app

 0





_,_ (2.18)






_I_ _c_ ( app ) = 2 _I_ 0


 cos



where _I_ 0
is the critical current of one junction (the two junctions are assumed to be identical). The SQUID thus behaves as though it were a single junction with a flux-tunable
critical current, allowing us to tune the Josephson inductance _in situ_ by applying an external
magnetic field.


A tunnel junction also has some capacitance in parallel with its inductance (one

can think of a junction as a parallel plate capacitor, with the insulating tunnel barrier
serving as the dielectric). As a result, a Josephson junction by itself is already a nonlinear
oscillator. We can choose to shunt the junction with additional linear capacitance and/or
inductance, as shown in Figure 2.3, to change the properties of this nonlinear oscillator
to some desired regime. All superconducting qubits can be modeled in this way, as a

junction with capacitance and nonlinear inductance shunted by external capacitance and/or


-----


14


|Col1|L ,C J J C|C|
|---|---|---|
||||


Figure 2.3: Generalized superconducting qubit.

The generalized equivalent circuit for a superconducting qubit consists of a Josephson junction, with its capacitance _C_ _J_ and nonlinear Josephson inductance _L_ _J_ , shunted by additional
linear inductance _L_ and capacitance _C_ . The various types of superconducting qubits are

inductance. Charge, phase, and flux qubits, as well as variants such as the transmon,

fluxonium, and capacitively shunted flux qubit, can all be seen as dierent limits of this
protean circuit.

To find the energy levels of a qubit, we need to write down its Hamiltonian. We

can write down an energy associated with the junction, assuming __ = 0 at time _t_ = _1_
and integrating the power in the junction over time until we are at phase __ at time _t_ . The
power is just _IV_ , so our energy is


Z _t_ _1_


_U_ =


_I_ ( _t_ _0_ ) _V_ ( _t_ _0_ ) _dt_ _0_ _,_ (2.19)


or substituting in the Josephson relations,


Z _t_ _1_


_I_ 0  0


_U_ =


0  0

sin _ @_
2 __ _@t_


_@t_ _0_ _dt_ _0_ _._ (2.20)


If we define the Josephson energy scale _E_ _J_ =  0 _I_ 0 _/_ 2 __ = ~ _I_ 0 _/_ 2 _e_ , we can rewrite the energy
in the junction as:

_U_ = _E_ _J_ (1 cos __ ) _._ (2.21)
__

Since __ is a macroscopic quantum degree of freedom, we can turn this expression into a
quantum Hamiltonian by replacing __ with the operator __  .

###### 2.1.3 ###### The transmon qubit

We now examine the specific case of the transmon qubit, which is a nonlinear

LC resonator consisting of a Josephson junction shunted by an external capacitor (this is
the universal qubit circuit shown above with the linear inductance removed, or taken to
be _L_ _! 1_ ). A full, detailed account of the transmon qubit is found in ref. [13]. The
transmon is depicted in Figure 2.4. We can write down its Hamiltonian in terms of the


-----


15


|Col1|Z|
|---|---|


![SlichterThesis.pdf-33-0.png](SlichterThesis.pdf-33-0.png)

Figure 2.4: Schematic of transmon qubit.

The transmon qubit consists of a SQUID loop, characterized by a Josephson energy _E_ _J_ and
a parallel junction capacitance _C_ _J_ , shunted by an external capacitance _C_ _B_ and coupled to
the external circuit voltage _V_ _g_ and shunt impedance _Z_ through a coupling capacitance _C_ _g_ .
The value of _E_ _J_ can be tuned by applying a magnetic flux bias to the SQUID loop.

energy scales _E_ _J_ = ~ _I_ _c_ _/_ 2 _e_ , where _I_ _c_ is the flux-dependent critical current of the SQUID
given in equation (2.18), and _E_ _C_ = _e_ 2 _/_ 2 _C_  , where _C_  is the total capacitance shunting
the Josephson inductance. In both cases, we use the convention that _e_ is the elementary
charge; the reader should be aware that some references use the convention that _e_ is the
Cooper pair charge, twice the elementary charge. The shunt capacitance _C_  is given by
_C_  = _C_ _J_ + _C_ _B_ + _C_ _g_ , where _C_ _J_ is the junction capacitance, _C_ _B_ is the external capacitance
shunting the junction and _C_ _g_ is the coupling capacitance to the external circuit. Using
these definitions, the Hamiltonian can be written as

_H_ = 4 _E_ _C_ ( _n_ __ _n_ _g_ ) 2 __ _E_ _J_ cos _,_  (2.22)

where we have left out the constant oset term from (2.21). The two operators here are

_n_  , the number of Cooper pairs transferred through the junction, and __  , the junction phase,


while _n_ _g_ is a parameter representing a voltage bias _V_ _g_ from the external circuit in units of
Cooper pairs ( _V_ _g_ = 2 _en_ _g_ _/C_ _g_ ). Note that the flux bias in the SQUID loop is implicit in the
definition of _E_ _J_ .

The operators  _n_ and __  are canonically conjugate, analogous to _Q_  and  for the 

harmonic oscillator circuit described above, with the commutation relation

[ _,_   _n_ ] = _i_ (2.23)

The relationship between __  and  _n_ is very interesting; each operator can be expanded as a

Fourier series in the basis of the other operator. The fact that  _n_ , representing the number

of Cooper pairs tunneling through the junction, is constrained to have integer values causes
__  to be a periodic function; it is therefore the discreteness of the Cooper pairs tunneling
through the junction which gives rise to the nonlinearity of the Josephson junction. These
ideas are presented in more detail in [68].

The Hamiltonian (2.22) can be solved exactly in the phase basis representation


-----


16


(where  _n_ = _i_ _@_
__ _@_


then given by [13]


_@_ _@_ __  ) in terms of Mathieu functions, as detailed in [74] 5 . The eigenenergies are


_E_ _m_ ( _n_ _g_ ) = _E_ _C_ _a_ 2[ _n_ _g_ + _k_ ( _m,n_ _g_ )] ( _E_ _J_ _/_ 2 _E_ _C_ ) _,_ (2.24)
__

where _a_ _r_ ( _q_ ) is Mathieus characteristic value, _m_ 0 _,_ 1 _,_ 2 _, ..._ is the index of the eigenstates,
_2 {_ _}_
and _k_ ( _m, n_ _g_ ) is a function for appropriately sorting eigenvalues:


_k_ ( _m, n_ _g_ ) =



[int(2 _n_ _g_ + _`/_ 2)mod 2] __

_`_ = __ 1


int( _n_ _g_ ) + _`_ ( 1) _m_ [( _m_ + 1)div 2]
__


(2.25)


In this expression, int( is the modulo operation, and _a_ div _b_ is the integer quotient of _x_ ) rounds to the integer closest to _a_ and _b_ . Mathieus characteristic value _x_ , _a_ mod _b_ _a_ _r_ ( _q_ ) is
implemented as a built-in Mathematica function, making the eigenenergies straightforward
to evaluate.

These solutions are general for this circuit, regardless of the values of _E_ _J_ and


_E_ _C_ ; it is the particular choice of _E_ _J_ and _E_ _C_ that determines the type of qubit which the
circuit represents. We plot the energy spectrum versus _n_ _g_ in Figure 2.5 for several values
of the ratio _E_ _J_ _/E_ _C_ . The qubit transition energy is the simply the energy spacing between
the two lowest-lying levels. In the limit _E_ _J_ _E_ _C_ , this circuit is called a split Cooper
__

pair box qubit [74], and the eigenenergies of the Hamiltonian, shown in Figure 2.5(a), are
essentially those of the charge eigenstates (parabolic with _n_ _g_ ), with the tunnel coupling _E_ _J_
lifting the degeneracy where the levels intersect. The energy levels of the Cooper pair box
depend strongly on _n_ _g_ , so noise in _n_ _g_ caused by the motion of charged defects in the qubit
substrate (known as charge noise) is problematic for qubit coherence [64]. At special charge
bias values where _n_ _g_ is a half-integer, the qubit energy splitting _E_ 01 = _E_ 1 __ _E_ 0 is insensitive
to _n_ _g_ (and thus charge noise) to first order. This bias point is called the charge sweet
spot.

The transmon qubit sidesteps the problem of charge noise by expanding this


charge sweet spot. In the transmon limit _E_ _J_ _E_ _C_ , usually reached by making _C_ _B_
__

large, the energy levels of (2.22) become very flat with respect to _n_ _g_ , as seen in Figure
2.5(d). The charge dispersion of the transmon levels actually decreases exponentially in
the ratio _E_ _J_ _/E_ _C_ , so that by the time one reaches _E_ _J_ _/E_ _C_ = 100 the ground state energy
varies by less than a part in 10 __ 8 over the whole range of _n_ _g_ , giving us a charge sweet
spot everywhere. The remarkable feature of this reduced sensitivity to charge noise with
increasing _E_ _J_ _/E_ _C_ is that it is not accompanied by a decrease in coupling to charge-based
external control fields (this phenomenon is described extensively in [13]), aording us a
qubit which we can control with capacitively coupled excitations but which does not suer
from charge-noise-related decoherence. Another nice feature of the transmon is that the
external shunting capacitor _C_ _B_ can be designed to have very low loss, improving the qubit
relaxation time. Transmon qubits hold the current record for the longest typical qubit relaxation times ( _T_ 1 = 20 __ 60 __ s), with correspondingly long dephasing times ( _T_ 2 = 6 __ 20
__ s) [17]; only one other qubit sample in history, a Cooper pair box, has shown a longer
reported relaxation time of 200 __ s [75].

5 The reader should be aware that ref. [74] uses a dierent convention for _E_ _C_ , which diers from ours by

a factor of 4.


-----


17

(a) E J /E C =1 (b) E J /E C =5

2.5


![SlichterThesis.pdf-35-0.png](SlichterThesis.pdf-35-0.png)

![SlichterThesis.pdf-35-1.png](SlichterThesis.pdf-35-1.png)

-2 -1


_n_ _g_


1.5

1

0.5

0

-2 -1 0 1 2

_n_ _g_


(c) E J /E C =10 (d) E J /E C =50

2

1.5


1.5

0.5


![SlichterThesis.pdf-35-2.png](SlichterThesis.pdf-35-2.png)

![SlichterThesis.pdf-35-3.png](SlichterThesis.pdf-35-3.png)

-2 -1


_n_ _g_


0.5

0

-2 -1 0 1 2

_n_ _g_


Figure 2.5: Energy structure of the Cooper pair box and transmon qubits.

This figure shows the lowest three energy levels of equation (2.24) as a function of the ratio
_E_ _J_ _/E_ _C_ and the charge bias _n_ _g_ . The energies are normalized to the value of _E_ 01 = _E_ 1 __ _E_ 0
at the degeneracy point _n_ _g_ = 1 _/_ 2. For _E_ _J_ _/E_ _C_ = 1, the levels are close approximations to
those of the uncoupled charge eigenstates (black dotted lines), with degeneracies lifted by
the tunnel coupling _E_ _J_ . This is the energy structure of the Cooper pair box. As _E_ _J_ _/E_ _C_
becomes larger, the energy levels become flatter with respect to _n_ _g_ and exhibit reduced
anharmonicity. By _E_ _J_ _/E_ _C_ = 50, we are in the transmon regime, where the energy levels
are essentially independent of _n_ _g_ . The eigenstates here are a linear combination of many
uncoupled charge states. Adapted from ref. [13].

The price we pay for insensitivity to charge noise is reduced qubit anharmonicity.


The Cooper pair box levels in Figure 2.5(a) are very anharmonic, but the transmon levels
in (d) are almost equally spaced. As a rough rule of thumb, the qubit frequency of a

transmon is given by _p_ 8 _E_ _J_ _E_ _C_ __ _E_ _C_ , while the anharmonicity is about equal to _E_ _C_ [13].
The reduced anharmonicity of the transmon has two major impacts. First, it means that
we cannot perform qubit state manipulations too quickly, lest we accidentally excite higher
energy levels. This problem can be ameliorated somewhat through the use of specially

shaped qubit pulses [76]. The second impact is that the higher levels of the transmon must
be accounted for when calculating readout parameters such as dispersive shifts. We will
discuss and quantify this in detail in section 2.3.3.


-----


18

#### 2.2 #### Quantum non-demolition measurement

Having described our quantum systems of interest, superconducting qubits, we

need to develop a method to measure their quantum states. For this we will use circuit
quantum electrodynamics, or circuit QED, described in the next section. Before we delve
into circuit QED, though, we need to examine the notion of quantum measurement and
understand what it is we seek in a measurement technique.

Quantum measurement is a process by which the information in a quantum state

is mapped to the state of a macroscopic meter which can then be read out classically. We
can describe this in terms of a Hamiltonian for a qubit, meter, and their interaction:

_H_ = _H_ qubit + _H_ meter + _H_ int _._ (2.26)

Ideally one would like to be able to turn the interaction on and o(i.e. be able to make
_H_ int = 0 when desired). When the interaction is o, the qubit can undergo free quantum
evolution, and then when the interaction is turned on at the desired point the information
in the qubit will be mapped into the meter where we can access it.

The textbook quantum measurement simply projects the state of the system under

measurement into one of the eigenstates of the measured observable with probabilities given
by the state of the system before measurement. This sort of idealized measurement is

known as a projective quantum non-demolition or QND measurement [39, 77]. A projective
QND measurement leaves the system in the measured eigenstate after it has completed,
such that repeated measurements will give identical results (modulo the evolution of the
quantum system between measurements). One can compare to a non-QND measurement,
where the quantum system is left in a state other than the measured eigenstate upon
completion of the measurement; here, the result of a subsequent measurement may or may
not be correlated with the result of the first measurement 6 . QND measurement need not
be projective; it is possible to make a weak QND measurement, where one receives only
partial information about the measured observable and the system is only nudged somewhat
towards the corresponding eigenstate. Projective QND measurement can be thought of as
a limit of many sequential weak QND measurements [50].

Whenever quantum measurement occurs, it is accompanied by backaction on the

quantum system under study. The very act of projecting the system into an eigenstate
of the measured observable is a form of backaction, but it is one that we desire during
measurement. However, the act of projecting into an eigenstate of one observable means
that information in the eigenstates of non-commuting observables is necessarily lost, a
dierent sort of backaction. If we envision the case of a repeated Stern-Gerlach experiment, a
measurement of _S_ _z_ on the beam of atoms will scramble the values of _S_ _x_ and _S_ _y_ , which do not
commute with _S_ _z_ . Repeated measurements of _S_ _z_ will give the same result, but if we measure
_S_ _z_ , then _S_ _x_ , then _S_ _z_ again, the information about _S_ _z_ will have been scrambled by the

6 We note that there is vocal opposition to the terminology of QND from some quarters [78], with

the contention that any quantum measurement can more straightforwardly be described as a perfect measurement combined with some specified or unknown measurement backaction. We employ the QND

terminology in this thesis because it is prevalently used, but the reader should be aware of the controversy
surrounding this terminology.


-----


19

backaction of the intervening _S_ _x_ measurement and the results of the two _S_ _z_ measurements
will be uncorrelated.

A QND measurement is one where all backaction (aside from projection) occurs in

observables other than the one we are measuring. This means that the mechanism by which
we couple to and measure the qubit must not disturb the states of our measured observable.
We can express this mathematically in terms of commutation relations. A measurement of
the observable A is QND if and only if:

[ _H_ qubit _, A_ ] = 0 (2.27)

and

[ _H_ int _, A_ ] = 0 _._ (2.28)

We also note that, trivially,

[ _H_ meter _, A_ ] = 0 (2.29)

because _A_ represents a qubit degree of freedom, which by definition commutes with all
meter degrees of freedom. All terms involving both qubit and meter degrees of freedom are
part of _H_ int by definition.

One can think of these criteria in terms of the time evolution of the quantum state.


From the time-dependent Schr odinger equation, the quantum state _|_ _i_ of the qubit evolves


in time according to



_iHt/_ ~
_|_ ( _t_ ) _i_ = _e_ _|_ (0) _i_ _._ (2.30)


If _|_ (0) _i_ is an eigenstate of _H_ , the time evolution operator _e_ _iHt/_ ~ just becomes a c-number
phase factor and does not cause any state transitions. If A commutes with _H_ , any eigenstate
of _A_ will also be unaected by the time evolution operator (modulo a phase factor) and so
repeated measurements of A will give the same result. The commutation relations above
simply state that neither the time evolution dynamics of the qubit nor those of the qubitmeter interaction will couple dierent eigenstates of _A_ , so once the qubit state has collapsed
it will remain there. Because the time evolution operator does not mix eigenstates of _A_ , we
say that _A_ is a constant of the motion.


#### 2.3 #### Circuit quantum electrodynamics

The method we choose to couple our superconducting qubits to the outside world

is called circuit quantum electrodynamics, or circuit QED. Circuit QED is an extension to
microwave circuits of the techniques of cavity QED used in atomic physics. In cavity QED,
an atom is coupled to the electromagnetic field inside a Fabry-Perot cavity. One of the
mirrors of the cavity is made slightly transparent so that photons may occasionally escape.
As a simplification, we look at just one atomic transition and treat the atom as a quantum
two-level system. Because the interaction between light and atoms is typically weak, the
cavity has the eect of amplifying the interaction strength by allowing a photon bouncing
back and forth inside many chances to interact with the atom before the photon leaves the
cavity. The cavity QED system is characterized by the coupling strength _g_ between the
atomic transition and the electromagnetic field in the cavity, the rate __ at which photons


-----


20

![SlichterThesis.pdf-38-0.png](SlichterThesis.pdf-38-0.png)

Figure 2.6: Schematic of cavity QED.

A two-level atom (circle) interacts with the electromagnetic field inside a Fabry-Perot cavity
with a strength _g_ . Photons leave the cavity at rate __ , and the atom decays into unobserved
channels with a rate __ .

escape the cavity, and the rate __ at which the atom decays into modes other than the cavity
mode. A typical cavity QED system is shown schematically in Figure 2.6.

The Yale group has pioneered the application of these ideas to electrical circuits

[40, 41]. In circuit QED, the atom is replaced by a superconducting qubit, while the cavity
is replaced by a superconducting resonator (a harmonic oscillator of the type discussed in
section 2.1.1). The coupling capacitance between the qubit and the resonator sets _g_ , while
the coupling capacitance between the resonator and the microwave environment sets __ .
Figure 2.7 shows a schematic of the circuit QED system with a transmon qubit.

Circuit QED has proven to be a very successful qubit measurement technique. It

has been shown experimentally to give a unit visibility readout of the qubit state (that
is, one where the qubit state is mapped into the readout signal perfectly) [44]. The circuit
QED architecture has been used to couple qubits together and perform quantum algorithms

[79, 80, 19, 22, 81, 24, 25], to prepare and detect quantum states of the microwave photon
field [82, 83, 84], and to perform multi-qubit error correction protocols [24, 85, 86].

The following sections give an outline of the salient features of circuit QED relevant

to the quantum jump experiments to be presented later, but are by no means an exhaustive
survey of the rich and varied topics which fall under the aegis of circuit QED. For those
seeking additional information, Dave Schusters thesis gives a very thorough description
of circuit QED, including for the transmon qubit [64], and Lev Bishops thesis adds more
theoretical detail [87]. Other Yale theses contain further details of circuit QED relevant to
control of photons [88] and coupling and manipulation of multiple qubits [89], topics which
are not directly addressed in this thesis.


-----


21


![SlichterThesis.pdf-39-0.png](SlichterThesis.pdf-39-0.png)

![SlichterThesis.pdf-39-1.png](SlichterThesis.pdf-39-1.png)

![SlichterThesis.pdf-39-2.png](SlichterThesis.pdf-39-2.png)

![SlichterThesis.pdf-39-3.png](SlichterThesis.pdf-39-3.png)

feed line


microwave
qubit (transmon) readout cavity


Figure 2.7: Schematic of circuit QED.

In circuit QED, we use a qubit (here a transmon) in place of an atom and a linear superconducting resonator as the readout cavity, in analogy to the cavity QED system in Figure
2.6. The qubit/cavity coupling _g_ is set by one pair of coupling capacitors, while the cavity
linewidth __ is set by another pair of capacitors. In this schematic, the cavity is probed in
reflection geometry with dierential excitation, but it is also possible to use transmission
geometry and/or single-ended excitation.

###### 2.3.1 ###### The Jaynes-Cummings Hamiltonian

The circuit QED Hamiltonian consists of three terms: a qubit term, a cavity term,

and a coupling or interaction term. Schematically, we can write it in the form

_H_ = _H_ _q_ + _H_ cav + _H_ int _._ (2.31)


The _H_ _q_ term is a classic Zeeman term of the form 1 2 ~ _!_ _q_ __  _z_ , where ~ _!_ _q_ is the qubit energy

splitting and  __ _z_ is one of the Pauli matrices. The _H_ cav term expresses the energy of

the electromagnetic field in the cavity in harmonic oscillator form using annihilation and
creation operators  _a_ and  _a_ __ . The uncoupled (or bare) cavity resonant frequency is _!_ cav _/_ 2 __ .

The _H_ int term represents a dipole coupling between the qubit and the electromagnetic field
in the cavity, characterized by the strength _g_ . Combining these expressions, we have the
total Hamiltonian:



1
_H_ =



1 1

~ _!_ _q_ __  _z_ + ~ _!_ cav ( _a_ __ _a_  +
2



) + ~ _g_ ( _a_ +  _a_ __ )( __ + +  __ ) _,_ (2.32)
2 __


where  __ + and  __ are qubit raising and lowering operators given by
__


multiply out the products in parenthesis in the _H_ int term, we get four terms with  _a_ or  _a_ __



1 2 ( __ _x_ _i_ __  _y_ ). If we

__


times __ + or __ , the qubit lowering and raising operators. Since we are in the limit where
__
the qubit and cavity energies are large compared to the available thermal energy, we invoke
the rotating wave approximation, meaning that we discard any terms which do not conserve
energy 7 . For example, the term  _a_ __ __ + does not conserve energy, because it adds a quantum

7 In some other systems, notably trapped ions, the energy scales are such that one cannot make the

rotating wave approximation and all four terms must be kept. The energy non-conserving terms of this


-----


22

![SlichterThesis.pdf-40-1.png](SlichterThesis.pdf-40-1.png)

![SlichterThesis.pdf-40-2.png](SlichterThesis.pdf-40-2.png)

![SlichterThesis.pdf-40-0.png](SlichterThesis.pdf-40-0.png)

Qubit frequency


Figure 2.8: Avoided crossing from the Jaynes-Cummings Hamiltonian.

The eigenstates of the Jaynes-Cummings Hamiltonian change as the qubit frequency is swept
through the cavity frequency. When qubit and cavity are far detuned, the eigenenergies
(solid lines) are similar to the uncoupled eigenenergies of the qubit (red dotted line) and
cavity (green dotted line), and the corresponding eigenstates are primarily qubit-like or
photon-like, respectively (the color of the solid lines indicates the qubit/photon nature of
the eigenstates). For _!_ _q_ = _!_ cav , the qubit-cavity coupling _g_ lifts the degeneracy and gives
rise to an avoided level crossing. The eigenstates here are equal superpositions of qubit and
photon states.

of energy to both the cavity and the qubit. After making the rotating wave approximation,
our Hamiltonian becomes:



1
_H_ JC =



1 1

~ _!_ _q_ __  _z_ + ~ _!_ cav ( _a_ __ _a_  +
2 2



) + ~ _g_ ( _a_ __  + +  _a_ __ __  ) _._ (2.33)
2 __


The expression in (2.33) is known as the Jaynes-Cummings (JC) Hamiltonian, and has been
used extensively in quantum optics since its development in the 1960s [70]. The interaction
term couples the qubit and cavity states by allowing them to exchange quanta of energy.
Figure 2.8 shows a cartoon of the energy spectrum of (2.33) as one tunes _!_ _q_ from below
_!_ cav to above _!_ cav . The dotted lines indicate the values of the qubit and cavity (photon)
eigenenergies in the absence of coupling, while the solid lines give the eigenvalues of the JC
Hamiltonian. The qubit and cavity maintain their individual character when far detuned
but become mixed as their frequencies become closer.

In the resonant limit, where _!_ _q_ = _!_ cav , the degeneracy of the uncoupled spec-

tra of the qubit and cavity is lifted by the presence of the coupling term in (2.33). The

Hamiltonian are the basis for sideband cooling techniques used to bring individual trapped ions to their
motional ground states [90].


-----


23

eigenstates of the system are then equal-weighted linear combinations of qubit and cavity
eigenstates, sometimes referred to whimsically as phobit and quton states because of
their hybridized nature, which dier in energy by 2 . A quantum of energy will be resonantly swapped back and forth between qubit and cavity continuously at a rate 2 _g_ _g_ . This
eect is known as vacuum Rabi oscillation, and the splitting between the eigenstates of the
JC Hamiltonian is known as the vacuum Rabi splitting.

When _!_ _q_ and _!_ cav are detuned from each other by an amount much larger than

the coupling _g_ , the eigenstates of the JC Hamiltonian are approximately product states of
qubit and cavity. This is known as the dispersive regime, and is the subject of the next
section.

###### 2.3.2 ###### The dispersive approximation


When the qubit and cavity are detuned from each other by an amount  __

_!_ _q_ _!_ cav _g_ , we are in the dispersive regime. Unlike the resonant limit shown above,
__ __
in the dispersive limit no energy is exchanged between the qubit and the cavity, and the
eigenstates of the system are well approximated by product states of the qubit and cavity.
If we examine (2.33) in the interaction picture, we can perform a perturbation expansion
in the small parameter _g/_ to yield the dispersive approximation to the Jaynes-Cummings
Hamiltonian:



1
_H_ disp = ~

2



1
_H_ disp =



_g_ 2
_!_ _q_ +



1
__  _z_ + ~ _!_ cav ( _a_ __ _a_  +



1 _g_ 2

) + ~
2 


_a_  __ _a_  __  _z_ _._ (2.34)



There are again three terms, corresponding to the qubit, the cavity, and their interaction
respectively. We note that the dispersive approximation has caused a shift in the qubit
frequency of _g_ 2 _/_ ; this is the Lamb shift, caused by the interaction of the qubit with the
zero-point energy of the cavity field. In addition, the interaction term has now taken on a
new form which allows us to make a QND measurement of the qubit state  __ _z_ using the cavity

as the meter. This can be seen because our desired observable  __ _z_ and the Hamiltonian obey

the necessary commutation relations from (2.27) and (2.28):

[ _H_ _q_ _,_  __ _z_ ] = 0 (2.35)

[ _H_ int _,_  __ _z_ ] = 0 _._ (2.36)

We have established that (2.34) satisfies the conditions to give a QND measurement of the
qubit, but it is not immediately evident how the measurement manifests itself. However, a
simple rearrangement of terms highlights the eect of the qubit on the meter state:



1
_H_ disp = ~ _!_ _q_ __  _z_ + ~

2



1
_H_ disp =



_g_ 2
_!_ cav + __  _z_





1
( _a_ __ _a_  + ) _._ (2.37)

2



1
( _a_ __ _a_  +


We see that the cavity resonant frequency now depends on  __ _z_ , so probing the resonant

frequency of the cavity will allow us to determine the state of the qubit. The shift between
the two eective cavity frequencies  _!_ cav ( 0 ) and  _!_ cav ( 1 ) corresponding to the two qubit
_|_ _i_ _|_ _i_


-----


24



|2|(a) |
|---|---|

|2| (b)|
|---|---|


 d

Frequency


 d

Frequency


Figure 2.9: Principle of circuit QED readout.

In the dispersive approximation, the cavity resonance frequency depends on the state of
the qubit. Depending on whether the qubit is in the ground or excited state, the cavity
frequency is shifted by an amount 2 __ . If we probe the cavity with a drive tone at an

appropriate frequency, this qubit-induced cavity shift manifests itself as a change in the
cavity phase reponse (left, for either reflection or transmission geometry) or amplitude
response (right, only for transmission geometry).


states _|_ 0 _i_ and _|_ 1 _i_ is called the dispersive shift and denoted 2 __ . For the dispersive JC

Hamiltonian with a two-state qubit as in (2.37), we have



_g_ 2
__ = _._ (2.38)




Figure 2.9 shows how to use the dispersive shift to read out the state of the qubit. In either
reflection or transmission geometry one can look at the phase shift of the cavity response,
which changes rapidly as one goes through resonance as shown in part (a). If the dispersive
shift 2 __ is of the order of the cavity linewidth __ , there will be an appreciable dierence in
the phase shift of the cavity output signal between the two qubit states if we drive at an
appropriate frequency, labeled _!_ _d_ . In transmission geometry, the cavity resonant frequency
can also be probed by looking at the transmitted amplitude, as shown in part (b). If we
look at the complex amplitude of the output signal in the IQ plane, we find that the optimal
choice of _!_ _d_ to maximize the output signal is halfway between  _!_ cav ( _|_ 0 _i_ ) and  _!_ cav ( _|_ 1 _i_ ), with

2 __ = __ [91].

If we group the terms in (2.34) in yet another way, we can look at the interaction

term not as a shift of the cavity frequency but as a shift of the qubit frequency:



1
_H_ disp = ~

2



1
_H_ disp =



2 _g_ 2 _g_ 2
_!_ _q_ + _a_  __ _a_  +

 



1
__  _z_ + ~ _!_ cav ( _a_ __ _a_  + ) (2.39)

2



1
__  _z_ + ~ _!_ cav ( _a_ __ _a_  +


This arrangement shows that the qubit frequency will be shifted by the presence of photons
in the cavity, a phenomenon known as the ac Stark eect. We can use the ac Stark eect to
calibrate the average cavity photon occupation  _n_ = _h_ _a_  __ _a_  _i_ for a given value of the readout


-----


25

drive power [42, 92]. This is a crucial part of the calibration of a circuit QED experiment,
and will be discussed in further detail in sections 2.3.3 and 6.4.3.

The dispersive approximation breaks down mathematically when the average cav-

ity photon occupation  _n_ becomes larger than a critical value _n_ crit =  2 _/_ 4 _g_ 2 , but numerical

simulations of the full Jaynes-Cummings Hamiltonian show that many of the predictions of
the dispersive approximation continue to be reasonable for  _n > n_ crit [92].

The eigenstates of the qubit in the dispersive JC Hamiltonian are primarily uncou-

pled qubit states, but they do have a small photonic component. This photonic component
gives rise to the Purcell eect, discussed experimentally in section 6.4.2. The Purcell eect
gives a qubit relaxation rate __ purc = _g_ 2 _/_  2 , which can be thought of as the photonic part
of the qubit eigenstate escaping from the cavity. A detailed derivation of the eigenstates of
the dispersive JC Hamiltonian and the resulting Purcell eect can be found in [64]. For a
multilevel system such as the transmon, the problem of diagonalizing _H_ disp exactly becomes
more difficult and one must resort to numerical methods [13].

###### 2.3.3 ###### Transmon dispersive shift

Because the transmon has many levels with relatively low anharmonicity, we need

to account for their eects in the dispersive approximation as well. For the transmon qubit,
the expression for the dispersive shift __ given in (2.38) is not accurate. We must instead
define the dispersive shift in terms of partial dispersive shifts between neighboring transmon
states, which tend to cancel each other and reduce __ from the value for a true two-level
system.

We will denote the transmon eigenenergies are given by (2.24) with a single sub-

script, as ~ _!_ _i_ . The energy dierence between any two transmon levels _|_ _i_ _i_ and _|_ _j_ _i_ is denoted
with two subscripts, as ~ _!_ _ij_ . The dipole coupling strength _g_ between the cavity and the
transmon levels now depends on which two transmon states are being coupled, so it receives
two subscripts as well and becomes _g_ _ij_ . These couplings are given by:


~ _g_ _ij_ = 2 _eV_ rms 0 _i_ _n_  _j_ (2.40)

_h_ _|_ _|_ _i_


where __ = _C_ _g_ _/C_  is the ratio of the gate capacitance to the total capacitance of the
transmon, _V_ 0 = ~ _!_ cav _/_ 2 _C_ cav is the RMS zero-point voltage of the cavity, and  _n_ is


rms 0 =


~ _!_ cav _/_ 2 _C_ cav is the RMS zero-point voltage of the cavity, and  _n_ is


the charge operator from the transmon Hamiltonian in equation (2.22). To a reasonable
approximation, the values of the coupling strengths are given by [13]:


_E_ _J_

8 _E_ _C_




1 _/_



_i_ + 1


~ _g_ _i,i_ +1 2 _eV_ rms 0
__


~ _g_ _i,i_ +1 __ 2 _eV_ 0


(2.41)


The coupling elements between non-neighboring states tend to zero at large _E_ _J_ _/E_ _C_ :

_g_ _ij_ 0 for _i_ _j_ _>_ 1 as _E_ _J_ _/E_ _c_ _._ (2.42)
_!_ _|_ __ _|_ _! 1_


The expressions above are only approximate, and any precise calculations should use values of _g_ _ij_ computed using the exact numerical values of the matrix elements _h_ _i_ _|_ _n_  _|_ _j_ _i_ . For

notational simplicity, subsequent experimental parts of this thesis drop the subscripts on _g_
using _g_ to mean _g_ 01 .


-----


26

Given expressions for _g_ _ij_ , we can write down a generalized Jaynes-Cummings

Hamiltonian for a multilevel system with _M_ levels denoted by _|_ _i_ _i_ . This Hamiltonian takes
the form [13, 93]:


_M_ __ 1

_i_ =0

X


_M_ __ 2

_i_ =0

X


_H_ = ~ _!_ cav



1
_a_  __ _a_  +


~ _!_ _i_ _|_ _i_ _ih_ _i_ _|_ +


~ _g_ _i,i_ +1


_a_  __ _|_ _i_ _ih_ _i_ + 1 _|_ +  _a_ _|_ _i_ + 1 _ih_ _i_


(2.43)


A quick check shows that this is just a natural generalization of equation (2.33), with
the interaction term swapping single quanta back and forth between qubit and cavity. If
we take the dispersive limit with an expansion to second order in __ _i_ = _g_ _i,i_ +1 _/_  _i_ , where
 _i_ = ( _!_ _i_ +1 __ _!_ _i_ ) __ _!_ cav , we can derive an expression for the eective dispersive shift __ :

__ = __ 01 __ 12 _/_ 2 _,_ (2.44)
__

where __ _ij_ are the partial dispersive shifts given by:


__ _ij_
__


_g_ _ij_ 2

_!_ _j_ _!_ _i_ _!_ cav
__ __


(2.45)


Using the approximate expressions above for _g_ _ij_ and defining the qubit anharmonicity __ =
_!_ 12 __ _!_ 01 __ _E_ _C_ _/_ ~ , we calculate the dispersive shift as [13]:



_g_ 2
__ =


 0


01


 0 + __


(2.46)


In the regime where the qubit is detuned far from the cavity such that  0 __ , we
_|_ _| |_ _|_
find that the dispersive shift is substantially reduced from the typical value given in (2.38)
by the presence of the higher transmon levels. For notational simplicity, the experimental
parts of this thesis drop the subscript on , using to mean  0 .

For improved accuracy in calculating the dispersive shift, which is a crucial cali-

bration element for our system, we expand the generalized Jaynes-Cummings Hamiltonian
(2.43) to fourth order in __ _i_ , which gives us [93]:


_H_ disp = _H_  0 +


_M_ __ 1

_i_ =0

X


~ _S_ _i_ _|_ _i_ _ih_ _i_ _|_ _a_  __ _a_  +


_M_ __ 1

_i_ =0

X


~ _K_ _i_ _|_ _i_ _ih_ _i_ _|_ ( _a_ __ _a_  ) 2 (2.47)


We use the shorthand _H_  0 to refer to the uncoupled qubit and cavity terms in the Hamil-

tonian, including the Lamb shifts. The _S_ _i_ represent ac Stark shifts of the type described
above, while the _K_ _i_ are shifts arising from the Kerr nonlinearity (terms of the form  _n_ 2 )

which appears in our fourth order dispersive expansion. The overall dispersive shift of the
transmon will be given by:

2 __ = ( _S_ 1 _S_ 0 ) + ( _K_ 1 _K_ 0 ) _n._ (2.48)
__ __

For the ac Stark shift, the total shift in qubit frequency due to the cavity (known as the
cavity pull) is given by

__ = 2 __ _n_  = ( _S_ 1 _S_ 0 ) _n_ + ( _K_ 1 _K_ 0 ) _n_ 2 _._ (2.49)
__ __


-----


27

We can write out analytical expressions for the _S_ _i_ and _K_ _i_ , which take the form [93]:


_S_ _i_ = [ __ _i_ __ 1 (1 __ __ _i_



2 _i_ ) __ _i_ (1 __ 2 _i_

__ __



2 _i_ __ 1 ) __ 2 __ _i_ __ 1 __ 2 _i_


_i_ __ 1 ]


+ 1


9 __ _i_ __ 2 __ 2 _i_



2 _i_ __ 1 __ 3 __ _i_ __ 1 __ 2 _i_



2 _i_ __ 2 __ __ _i_ __ 2 _i_


(2.50)

(2.51)


_i_ +1


+ 3 __ _i_ +1 __ 2 _i_



(2)
_g_ _i_
__



(2)
__



(2)
3 _g_ _i_
__ __



(2) (2)

_i_ __ 2 __ _i_ __


_i_ __ 2



1
_K_ _i_ =


3 __ _i_ __ 2 __ 2 _i_



2 _i_ __ 1 __ __ _i_ __ 1 __ 2 _i_



2 _i_ __ 2 + __ _i_ __ 2 _i_



2 _i_ +1 3 __ _i_ +1 __ 2 _i_

__


+ ( __ _i_ __ __ _i_ __ 1 )( __ 2 _i_



2 _i_ + __ _i_



2 _i_ __ 1 ) + _g_ _i_ (2)



(2)
__



(2)
_g_ _i_
__ __



(2) (2)

_i_ __ 2 __ _i_ __


_i_ __ 2


where we use the shorthand notation __ _i_ = _g_ _i,i_ +1 _/_  _i_ , __ _i_ = _g_ _i,i_ 2 +1 _/_  _i_ , _g_ _i_ (2)


_i,i_ 2 +1 _/_  _i_ , _g_ _i_ (2)


= __ _i_ __ _i_ +1 ( _i_ +1
__



(2)
 _i_ ) and __



(2)
= _g_ _i_
__


_/_ ( _i_ +1 +  _i_ ), and take __ _i_ = __ _i_ = 0 for all _i_ _62_ [0 _, M_ __ 2].


###### 2.3.4 ###### Measurement rate and readout signal-to-noise ratio

In section 2.3.2, we established that the circuit QED architecture can be used

to make a QND measurement of the state of the qubit when operated in the dispersive
regime, with _|_  _| _ _g_ . The information about the qubit state manifests itself as a shift
in the resonant frequency of the cavity, which we can probe by driving the cavity with a
microwave tone and looking at its response. We will now examine the nature and strength
of the signal mathematically.

When driven with a microwave tone, the electromagnetic field inside the cavity

will be characterized by a complex amplitude __ which depends on the cavity linewidth, the
strength of the drive, and the drive detuning. The photon occupation of the cavity  _n_ is the

square modulus of this amplitude _|_ __ _|_ 2 , while arg( __ ) gives the phase of the field. Because
the cavity resonant frequency depends on the qubit state, in general the complex amplitude
__ will as well. For a given drive power and frequency, there will be two amplitudes __ _|_ 0 _i_
and __ 1 corresponding to the qubit being in state 0 or 1 respectively. We call these the
_|_ _i_ _|_ _i_ _|_ _i_
pointer states, since they indicate the state of the qubit. The pointer states are coherent
states of the microwave field, and as such are characterized by noise (uncertainty) in both
amplitude and phase. We can average the readout signal in time to reduce this uncertainty,
assuming the qubit does not change state.

The measurement of the state of the qubit depends on the vector dierence between

the pointer states __ 0 and __ 1 , which we call __ . The value of __ depends on the relationship
_|_ _i_ _|_ _i_
between the dispersive shift 2 __ and the cavity linewidth __ , as well as the frequency and
power of the cavity drive tone. If __ = 0, the pointer states are independent of the qubit
state; we can record the readout signal to our hearts content and never know what the
state of the qubit was. As _|_ __ _|_ becomes larger and larger, it is easier and easier to determine
the qubit state from the pointer states in a given amount of time. We can characterize this
eect in terms of a measurement rate  _m_ [91]:

 _m_ ( _t_ ) = __ __ ( _t_ ) 2 _,_ (2.52)
_|_ _|_


-----


28


where __ is the cavity linewidth. The measurement rate parameterizes the strength of the
measurement; since the readout signal is continuous in time,  _m_ tells us how rapidly we
accumulate information about the state of the qubit. As one might expect,  _m_ depends
both on our ability to resolve the pointer states and on the rate at which photons leave
the cavity carrying information about the qubit. Figure 2.10(a) and (b) show two possible
cases, one with weak measurement (a) and another with stronger measurement (b). Note
that the amplitude of the pointer states is the same for both cases, but that their relative
phase shift is dierent (due a dierent ratio of __ to __ ). For a given cavity drive power,
__ is maximized when the drive frequency is midway between  _!_ cav ( 0 ) and  _!_ cav ( 1 ), with
_|_ _|_ _|_ _i_ _|_ _i_

2 __ = __ [91].

As we saw in our two alternate associative groupings of the dispersive JC Hamil-

tonian, the qubit-cavity interaction can be thought of as shifting either the cavity frequency
or the qubit frequency. If the qubit state aects the cavity frequency (i.e. _|_ __ _| 6_ = 0), then the
photons in the cavity will aect the qubit frequency through the ac Stark shift. Because
the readout cavity photon state is a coherent state, there are fluctuations in the cavity
photon occupation  _n_ . As a result, there are fluctuations in the ac-Stark-shifted qubit fre-

quency, which gives rise to dephasing. This is the measurement induced dephasing which is
a necessary consequence of any quantum measurement; as one projects to an eigenstate of
the measured observable, the phase information of a superposition state must be lost. The
measurement-induced dephasing rate  _d_ is related to the measurement rate by:


 _d_  _m_ (2.53)
__

This relationship means that we cannot acquire information about the qubit state faster
than we cause it to dephase. A detailed theoretical treatment of measurement-induced

dephasing is given in refs. [50] and [92]. The reader is warned that these references use
conventions for  _d_ that dier by a factor of 2. The convention in the above expression is
that of [50].

Given a certain measurement rate  _m_ at which we accumulate information about

the qubit state, we can ask what our readout signal-to-noise ratio (SNR) will be. This
topic will be discussed in more detail in section 7.5.1, and is covered extensively in ref. [94]
(although the reader should be careful as some of the conventions used in that paper are
dierent from in this thesis).

In general, the signal to noise ratio will be proportional to __  _m_ , where __ is a

measure of our efficiency in detecting the readout signal with our amplification chain. For
a state-of-the-art commercial low-noise microwave amplifier, __ __ 1, and we find that the
noise added by our amplification chain severely limits our ability to resolve the pointer
states. Figure 2.10 (c) and (d) show this eect schematically. When the pointer states exit
the cavity, as seen in part (c), they each have some quantum noise but are still readily
distinguishable from each other. If one includes the eects of added noise from the postamplification chain, shown in part (d), the noise has become so large that it drowns out
the signal from the pointer states and we cannot distinguish them anymore. The circuit
QED readout signal is giving us a projective QND measurement of the qubit state, but
the noise added by post-amplification prevents us from distinguishing the readout pointer
states reliably. In order to observe the qubit dynamics using the circuit QED architecture,
we will have to use amplifiers which add less noise to the readout signal.


-----


29

![SlichterThesis.pdf-47-0.png](SlichterThesis.pdf-47-0.png)

Figure 2.10: Readout signal and noise in the IQ plane.

Parts (a) and (b) show the readout pointer states for weak and strong measurements,
respectively. Part (c) shows the eects of noise on our ability to resolve the pointer states
given high efficiency __ __ 1 of our amplification chain. The colored circles correspond to
the uncertainty in the output signal amplitude. Part (d) shows the pointer states in the
presence of the noise typically added by state of the art amplifiers, where __ __ 1. It is not
possible to resolve the pointer states cleanly in this instance.


-----


30

## Chapter 3

# Amplification and the quantum limit

The circuit QED formulation and techniques mentioned in the previous chapter

have been widely used for the readout of superconducting qubits. However, typical circuit
QED implementations have poor single-shot readout fidelity because of noise added by
following amplifiers. These amplifiers are necessary to make the signal large enough to

measure at room temperature. In this chapter, we delve into the theory of amplification and
noise and show that the ultimate noise performance of an amplifier is limited by quantum
mechanics. We will then describe the theory and operating principles of the parametric
amplifier we developed to improve the noise performance of circuit QED readout.

For a thorough, mathematically detailed treatment of general ideas of quantum

noise and amplification, the reader is directed to the excellent review by Clerk and coworkers [50]. Some of the derivations in this chapter follow those presented in that reference.
For an excellent general reference on classical noise and amplification, we recommend the
book by Motchenbacher and Connelly [95].

#### 3.1 #### Amplification and noise

Experiments with quantum mechanical systems inevitably deal with very low-level

probe and readout signals. Such signals cannot be too strong, lest they destroy the quantum
eects we are trying to observe. However, the typical data recording or measurement

apparatus of experimental physics, sitting at room temperature, adds thermal noise to all
incoming signals, so much so that signals of the level used to probe quantum eects are
lost in the noise. What we need is a method for increasing the power of the low-level

quantum signals until they are large enough to lay our grubby, classical hands on, in
the famous words of Carlton Caves [96]. This is what we mean by amplification: it is

a method to increase the power of a signal. Unfortunately, this power gain comes with a
price, namely the addition of noise beyond that of the original signal, as shown in Figure 3.1.
This added noise is an inevitable consequence of amplification which arises from quantum
mechanical constraints; this will be discussed in detail in the next section. The type of
amplification one typically thinks of in physics is linear amplification, which means that the


-----


31

amplified

input

signal

![SlichterThesis.pdf-49-0.png](SlichterThesis.pdf-49-0.png)

###### +

input

noise

![SlichterThesis.pdf-49-1.png](SlichterThesis.pdf-49-1.png)

###### +

|+|G,T n|
|---|---|


added

amplifier

noise

![SlichterThesis.pdf-49-2.png](SlichterThesis.pdf-49-2.png)

Figure 3.1: Amplification process.


input

signal

input

noise


A linear amplifier takes an input signal and its associated noise and outputs copies of these
inputs with an amplitude increased by _p_ _G_ , where _G_ is the power gain of the amplifier. The

amplifier also adds additional noise to the output signal, the amount of which is characterized by the amplifier noise temperature _T_ _n_ .


A linear amplifier takes an input signal and its associated noise and outputs copies of these
inputs with an amplitude increased by _p_ _G_ , where _G_ is the power gain of the amplifier. The


output signal is linearly related to the input signal (for example, multiplied by some fixed
amplitude gain _p_ _G_ ). We will deal primarily with linear amplification in this chapter, since

it is straightforward to treat mathematically 1 .


output signal is linearly related to the input signal (for example, multiplied by some fixed
amplitude gain _p_ _G_ ). We will deal primarily with linear amplification in this chapter, since


As discussed above, noise is intimately tied to amplification. Noise is typically

characterized by a power spectral density _S_ ( _!_ ), the intensity of noise at a given frequency
_!_ , found by taking the Fourier transform of the time-domain noise trace 2 . The power

spectral density _S_ ( _!_ ) can also be equivalently parameterized in terms of the amplitude
spectral density _S_ 1 _/_ 2 ( _!_ ) of noise in quantities such as voltage, current, or flux.

Classical electronic noise occurs due to the thermal fluctuations of charge carriers,


and is often referred to as Johnson or Nyquist noise, after the men who discovered and
explained it, respectively [97, 98]. Johnson/Nyquist noise has a spectral density which is
independent of frequency (noise which is frequency-independent in this way is referred to as
white noise). A resistor at temperature _T_ with resistance _R_ will exhibit voltage noise with
a spectral density of _p_ 4 _k_ _B_ _TR_ V _/_ _p_ Hz and current noise with spectral density 4 _k_ _B_ _T/R_


A _/_


Hz[95]. If we multiply these expressions, we find that the total noise power in a resistor


Hz and current noise with spectral density


4 _k_ _B_ _T/R_


in a given bandwidth _B_ is given by _P_ = 4 _k_ _B_ _TB_ . In the case where the resistor is connected
to an impedance-matched load, the voltage noise occurs across the parallel resistance _R/_ 2
and the current noise through the series resistance 2 _R_ . Assigning half of the dissipated
power to the source impedance and half to the load impedance, and we recover the famous
expression for noise power dissipated in a matched load [95]:

_P_ = _k_ _B_ _TB._ (3.1)

1 Amplification need not be linear to be useful, and indeed the experimental work presented in later

chapters involves amplification which is not necessarily linear.


2 More technically, one can define the power spectral density in terms of the autocorrelation function of


R _1_


_1_ _h_ _V_ ( _t_ ) _V_ (0) _i_ _e_ _i!t_ _dt_ [50, 95].


the noise signal. As an example, for a voltage signal _V_ ( _t_ ), we find _S_ ( _!_ ) =


-----


32

We can rewrite this equation in terms of the power spectral density (the noise power per
unit bandwidth) as

_S_ ( _!_ ) = _k_ _B_ _T._ (3.2)

This expression shows that the thermal noise dissipated in a matched load is white and
is linearly dependent on temperature. At very high frequencies and/or very low temperatures, however, quantum mechanical eects change this simple relationship. Accounting
for quantum eects using the fluctuation-dissipation theorem [99], the result for the noise
power spectral density 3 becomes [50]:



~ _!_
_S_ ( _!_ ) = 2 coth


~ _!_

2 _k_ _B_ _T_





~ _!_
_S_ ( _!_ ) =


(3.3)


Lets examine a few limits of equation (3.3). First, in the high-temperature classical limit
where ~ _!_ __ _k_ _B_ _T_ , we use the approximation coth _x_ __ 1 _/x_ for small _x_ and find _S_ ( _!_ ) __ _k_ _B_ _T_
reproducing the original classical result. In the low temperature limit ~ _!_ __ _k_ _B_ _T_ , the coth
term goes to 1 and we find that



~ _!_
_S_ ( _!_ ) =



_._ (3.4)
2


This term is recognizable as the zero-point energy of the electromagnetic field; we have
rediscovered the result that even at zero temperature there will still be quantum fluctuations
of the electromagnetic field at the level of half a photon per unit bandwidth. Since our qubits
and readout operate in this low-temperature limit where ~ _!_ __ _k_ _B_ _T_ , the noise on a circuit
QED output signal will be made up of quantum fluctuations.

Given the nice relationship in (3.2), it is convenient to parameterize the noise

spectral density in terms of an eective temperature _T_ e , which is defined as

_T_ e = _S_ ( _!_ ) _/k_ _B_ _._ (3.5)

In the classical (high temperature) regime, we find that _T_ e = _T_
, the true physical temperature. However, at sufficiently low temperatures we must use the full quantum mechanical
expression (3.3) and the relationship becomes more complicated. At temperatures low

enough that (3.4) applies, the eective temperature saturates to the value



~ _!_
_T_ e =

2 _k_ _B_


(3.6)


For a qubit experiment with readout frequencies of 6 GHz we have _T_ e = 144 mK, even
though the physical temperature might approach 30 mK.


3 In general, the spectral density of quantum noise is not symmetric in frequency: _S_ ( _!_ ) _6_ = _S_ ( __ _!_ ). The

expression in (3.3) is the symmetrized or classical noise spectral density, which is the average of the quantum
noise spectral densities at frequencies . The asymmetry of quantum noise spectra arises mathematically from the fact that the two quadratures of a signal do not commute with each other and thus their _!_ and __ _!_
cross-correlation is non-zero. We can also understand it heuristically by considering noise as coming from
absorption or emission of photons coming from a thermal bath, corresponding to noise at positive or negative
frequencies respectively. The density of final states for absorption and emission processes are dierent when
_|_ _!_ _|_ & _k_ _B_ _T/_ ~ , so the emission and absorption rates (and thus the amount of noise at _!_ versus __ _!_ ) will be
dierent. Further details are provided in ref. [50].


-----


33

The noise on the input signal is only part of the full story, however, since we must

also account for the noise added by the amplifier itself. Lets take a microwave amplifier
connected to a matched source impedance of eective temperature _T_ _s_ . We can express the
noise added by the amplifier in terms of an amplifier noise temperature _T_ _n_ , which is defined
as follows. For an amplifier with gain _G_ and an eective source temperature _T_ _s_ , the noise
power at the output is given by

_P_ _n,_ out = _Gk_ _B_ ( _T_ _s_ + _T_ _n_ ) _B._ (3.7)

By measuring the output noise power and knowing _T_ _s_ , we can extract the value of _T_ _n_ . The
noise temperature is not a real temperature (although it may be correlated with the physical
temperature of the amplifier for many devices), but rather is a convenient shorthand way of
expressing the amount of noise added by the amplifier. Looking at equation (3.7), we can
see that using an amplifier with noise temperature _T_ _n_ is equivalent to raising the eective
source temperature by _T_ _n_ and then amplifying using a fictitious noiseless amplifier with the
same gain _G_ .

Often the signal of interest is so small that we must use several amplifiers in series

to achieve sufficient gain; this is the case with circuit QED readout signals. In such a setup,
it is essential to know how the noise temperature of each amplifier will aect the noise
properties of the final output signal. We can write this down mathematically if we assume
that each of the amplifiers in series (lets say there are _k_ of them) has a gain _G_ _i_ and noise
temperature _T_ _n,i_ . The noise power after the first amplifier stage is given by equation (3.7),
and this serves as the input noise of the second amplifier stage. We add the contribution of
the second amplifier and find that its output noise is

_P_ _n,_ out = _G_ 2 [ _G_ 1 _k_ _B_ ( _T_ _s_ + _T_ _n_ 1 ) _B_ + _k_ _B_ _T_ _n_ 2 _B_ ] _._ (3.8)

After the third stage, we have


_P_ _n,_ out = _G_ 3


_G_ 2 [ _G_ 1 _k_ _B_ ( _T_ _s_ + _T_ _n_ 1 ) _B_ + _k_ _B_ _T_ _n_ 2 _B_ ] + _k_ _B_ _T_ _n_ 3 _B_


(3.9)


and so forth through all the stages. At the final output, we would like to calculate the
equivalent input noise, which we do by dividing out the total gain _G_ 1 _G_ 2 _G_ _k_ . We then
_  _
divide by _k_ _B_ _B_ and subtract the original eective source temperature _T_ _s_ to give the noise
temperature _T_ sys for the whole amplifier system :



_T_ _n_ 2
_T_ sys = _T_ _n_ 1 +

_G_ 1


_T_ _n_ 3

_G_ 1 _G_


_T_ _nk_
+ +
_  _ _G_ 1 _G_ 2 _  _ _G_ _k_ __ 1


_T_ _nk_
+ +
_  _ _G_ 1 _G_ 2


(3.10)


For large gains _G_ _i_ 1 and for noise temperatures such that _T_ _n,i_ _T_ _n,i_ +1 _/G_ _i_ , we find
__ __
that the overall system noise temperature depends primarily on the noise temperature of
the first-stage amplifier. In other words, as long as the output noise from any given stage
is much larger than the input noise of the next stage, the noise of this next stage will
contribute little to the overall _T_ sys .

For circuit QED experiments, we need several stages of amplification. State-of-the-

art cryogenic semiconductor microwave amplifiers have noise temperatures around 3 K and
power gains on the order of 10 3 __ 10 4 , or 30 __ 40 dB (gain for microwave amplifiers is usually


-----


34


quoted in logarithmic units (dB), with the relationship between linear and logarithmic power
gains given by _G_ dB = 10 log 10 _G_ linear ). This means that as long as the next amplifier in
the chain has _T_ _n_ __ 3 _,_ 000 _K_ , the value of _T_ sys is set by the cryogenic amplifier. If we

would like to reduce the system noise temperature further, we need an amplifier with noise
temperature well below 3 K and enough gain to overwhelm the input noise of the cryogenic
semiconductor amplifier. If we make an amplifier with _T_ _n_ 150 mK (one which adds half
__
a photon of noise at 6 GHz), it should ideally have a power gain of at least 100 (20 dB in
log units) to ensure that it is the primary contribution to the system noise temperature.

#### 3.2 #### Quantum limits on amplifiers

In the previous section, we alluded to the fact that quantum mechanics sets limits

on the noise temperature of a linear amplifier. We will now derive this result theoretically and examine its consequences. At the source of all quantum noise constraints is the
quantum mechanical notion of commuting and non-commuting operators. Qualitatively,
quantum noise limits arise when we wish to know the value of two non-commuting observables simultaneously. Our knowledge of non-commuting observables is limited by the
Heisenberg uncertainty principle, which in eect makes our estimates of the observed values
noisy.

Lets take the canonical example of a harmonic oscillator, described by the position

operator  _x_ and the momentum operator  _p_ , which do not commute with each other. Quantum

mechanics dictates that there will exist a relationship between the position and momentum
uncertainties  _x_ and  _p_ given by

 _x_  _p_ __ ~ _/_ 2 (3.11)

Any measurement of position will disturb the value of momentum and vice versa,

with the amount of disturbance depending on the precision of the measurement of the other
observable. If one would like to know both the position and the momentum simultaneously,
the uncertainty relationship (3.11) limits the total precision of the combined measurement.
Even when the harmonic oscillator is in its lowest energy state there is some spread in the
values of position and momentum, an eect called the zero-point motion of the oscillator.
In a heuristic sense, one can think of the zero-point motion as a fundamental quantummechanical noise obscuring our knowledge of the exact position and momentum of the
oscillator [39].

The Hamiltonian for the electromagnetic field at a given frequency is isomorphic to

that of a harmonic oscillator, with the roles of position and momentum mapped into the two
quadrature amplitudes, or alternatively the amplitude and phase. We usually characterize
the electromagnetic field in terms of the creation and annihilation operators  _a_ __ and  _a_ , which

obey the commutation relation [ _a,_  _a_ __ ] = 1.

Since these operators do not commute, it will be impossible to know their values

simultaneously with arbitrary precision, just as in the case of position and momentum for
the harmonic oscillator. However, if we want to amplify an electromagnetic wave faithfully,
in general we need to know the value of both operators simultaneously (equivalent to
saying we need to know both the amplitude and phase of a signal simultaneously) so we can


-----


35

make an enlarged copy at the amplifier output. Heuristically, we can say that the amplifier
adds noise because it cannot copy and enlarge both quadratures of the input signal at the
same time without being a bit uncertain about what the true value of the input signal is.
As a result, the output signal is never a perfect copy of the input, but rather a slightly
noisier copy. This way of looking at added noise suggests that we could potentially amplify
without adding noise if we only care about one quadrature; this is in fact the case and will
be discussed in section 3.2.1.

We can examine this in a more mathematically rigorous way in the following

derivation, which is due to Haus and Mullen [100] and was expanded by Caves [96]. We
take an amplifier whose input and output can be described by a set of bosonic modes,
photons for example. A classical input signal _E_ ( _t_ ) at frequency _!_ takes the general form


_ae_ __ _i!t_ + _a_ __ _e_ _i!t_




_E_ ( _t_ ) _/_


(3.12)


where _a_ and its complex conjugate _a_ __ characterize the two quadrature amplitudes (or the
amplitude and phase) of the signal. For quantum mechanical signals, we must convert


these complex amplitudes to operators _a_ _!_  _a_ and _a_ __ _!_  _a_ __ , the annihilation and creation

operators for the electromagnetic field at the input. We would like to map this input


these complex amplitudes to operators _a_ _!_  _a_ and _a_ __ _!_  _a_ __ , the annihilation and creation


signal to an output signal which is also a state of the electromagnetic field. We described
the output field in terms of output annihilation and creation operators  _b_ and  _b_ __ . These

operators all obey the standard commutation relations:

[ _a,_  _a_ __ ] = 1 _,_ [  _b,_  _b_ __ ] = 1 _._ (3.13)


We would like the output of our amplifier to be a copy of the input with some power gain
_G_ . We would like both quadratures of the input signal to be amplified with the same gain,
so we have the relationship


_b_ =


_G_ _a,_   _b_ __ =


_G_ _a_  __ _._ (3.14)


Unfortunately, these expressions clearly violate the commutation relations in (3.13). We
have to introduce a second term _F_  to satisfy the commutation relations, changing (3.14) to


_b_ =


_G_ _a_  + _F_  _,_  _b_ __ =


_G_ _a_  __ + _F_  __ _._ (3.15)


This operator _F_  represents noise added by the amplifier, which should be uncorrelated with


the input signal  _a_ . As a result, we can take [ _F_  _,_  _a_ ] = 0 and [ _F_  _,_  _a_ __ ] = 0. Since _F_  is a random


noise, we take the expectation values _h_ _Fi_  = _h_ _F_  _a_  _i_ = _h_ _F_  _a_  __ _i_ = 0 as well. If we now insist


that  _b_ satisfy the commutation relations in (3.13), we find that:



[ _F_  _,_ _F_  __ ] = 1 __ _G._ (3.16)

We would now like to determine the mean-square fluctuations of the output signal, given
by ( _b_ ) 2 . This can be expressed as


( _b_ ) 2 = 1  _b,_  _b_ __  _b_ 2 _,_ (3.17)

2 _h{_ _}i |h_ _i|_


-----


36


where _{_  _b,_  _b_ __ _}_ =  _b_  _b_ __ +  _b_ __  _b_ . An identical formula holds for ( _a_ ) 2 . Using a series of useful


commutator and anticommutator relations presented in [96], as well as the relations between


_F_  and  _a_ presented above, we can write the expression for ( _b_ ) 2 as:


( _b_ ) 2 = _G_ ( _a_ ) 2 + 1  _,_  __ _._ (3.18)

2 _h{_ _F_ _F_ _}i_


( _b_ ) 2 = _G_ ( _a_ ) 2 + 1


Using another identity from [96] and recalling that _h_ _Fi_  = 0, we can rewrite this as an

inequality:


Using another identity from [96] and recalling that _h_ _Fi_  = 0, we can rewrite this as an


( _b_ ) 2 _G_ ( _a_ ) 2 + 1 [  _,_  __ ]
__ 2 _|h_ _F_ _F_ _i|_


( _b_ ) 2 _G_ ( _a_ ) 2 + 1
__ 2


(3.19)


_G_ ( _a_ ) 2 + _|_ _G_ __ 1 _|_
__ 2


In the limit of large gain, we have _G_ __ _G_ __ 1. Dividing the output noise by the gain _G_ to
get the noise referred to the input, we find


( _b_ ) 2 _/G_ ( _a_ ) 2 + 1 _._ (3.20)
__ 2

We have recovered the result that phase-preserving amplification must add at least half a
quantum of noise, referred to the input. In the no-amplification limit _G_ = 1, we find that
the amplifier is not required to add noise. Looking at (3.16), we can see that for _G >_ 1 it
is possible to write a model for the added noise as


_F_  =


_G_ __ 1 _d_  __ _,_ _F_  __ =


_G_ __ 1 _d ._  (3.21)


This formulation represents a single additional input mode _d_  which is amplified by _G_ __ 1.

One can readily check that the noise inequality in (3.20) becomes an equality in this case,
and the amplifiers added noise represents just the vacuum fluctuations of the input mode


This formulation represents a single additional input mode _d_  which is amplified by _G_ __ 1.


_d_ , which is required to maintain the commutation relations and still achieve gain. This
additional mode represents the idler mode in a parametric amplifier, to be discussed in
section 3.3.

###### 3.2.1 ###### Phase-sensitive and phase-preserving amplifiers


The above derivation is dependent on the fact that we wish to amplify both  _a_

and  _a_ __ in the same way, in other words, that we wish to amplify both quadratures of the

4
input signal with the same gain. This type of amplification is often referred to as phasepreserving amplification , since the amplified signal contains the information from both
quadratures of the input signal and maintains phase and amplitude relationships.

There are certain situations in which one might only be interested in one quadra-

ture of the signal, without caring what happens to the other quadrature. Amplification of
just one quadrature of a signal is referred to as phase-sensitive amplification, since the
output signal depends on the relative phase of the input signal. We might suspect that this

4 It is also occasionally called phase-insensitive amplification, a nomenclature we avoid here because it

is so similar to phase-sensitive.


-----


37

allows us to amplify without adding noise, since the single quadrature we amplify commutes
with itself.

Phase-sensitive amplification is equivalent to amplifying  _a_ without regard to what

happens to information in  _a_ __ . Given this flexibility, we can write down an analogue to

equation (3.14) where we amplify one quadrature but deamplify the other 5 :


_b_ =


_G_ _a,_   _b_ __ =


_a_  __ _._ (3.22)


We can see by inspection that these definitions of  _b_ and  _b_ __ satisfy the commutation

relations in (3.13), and so we have no need to introduce extra modes and their associated
noise into the output signal. As a result, we find that the output noise referred to the input is
( ; we have accomplished noiseless amplification! For general signals, phasesensitive amplification is not appropriate because we typically care about the information _b_ ) 2 _/G_ = ( _a_ ) 2
in the deamplified quadrature. However, for some signals, including qubit readout signals
as will be detailed in later sections, we can profitably employ phase-sensitive amplification
and benefit from its superior noise performance.

#### 3.3 #### Parametric amplification

Having talked about amplification in general, we narrow our focus to a specific and

basic type known as parametric amplification. The principle of parametric amplification
is simple: gain is achieved by varying a parameter of the amplifier system harmonically in
time. The energy used to vary the parameter is called the pump. The modulation of the
system parameters at the pump frequency causes some of the pump energy to be transferred
into another frequency mode, chosen to be the signal frequency (additional pump power
is sent to another mode, called the idler). In this way, the signal achieves power gain and
amplification. Detailed mathematical derivations of parametric amplification can be found
in refs. [101, 102], among many others.

The classic example of parametric amplification is a child on a swing. Even when

nobody is around to push him or her, a child can still swing to great heights just by
pumping his or her legs. Whenever the child reaches the maximum swing excursion, he
or she changes leg position from bent to outstretched or vice-versa. The direction is chosen
to raise the childs center of gravity, which changes the eective length of the swing. This
is the parameter of the oscillator (the swing) which is modulated. The energy from the
childs pumping is, appropriately, the pump, which is at twice the natural frequency of
the swing. The energy from this pump is transferred into the two degenerate normal modes
of the swing ( _e_ __ _i!t_ ) and causes the amplitude of the swings oscillations to increase.

In a parametric amplifier, often called a paramp for short, the pump couples

two frequency modes together and transfers energy to both of them. These modes are

called the signal and the idler. The frequencies of the signal, idler, and pump are related

5 This operation is also called squeezing, because it takes a coherent state input, which has equal width in

both quadratures in the IQ plane, and squeezes it into a more elliptical state with dierent widths along
its two principal axes but the same phase space area as the initial coherent state. Squeezed states are of
interest in quantum optics [70], and phase-sensitive amplification is a typical way of generating them.


-----


38

in a specific way depending on the exact nature of the system. The two most common
types of parametric amplifiers are called three-wave or four-wave amplifiers. In a threewave amplifier, the relationship between the pump frequency _!_ _p_ and the signal and idler
frequencies _!_ sig and _!_ id is given by

_!_ _p_ = _!_ sig + _!_ id _,_ (3.23)

while for a four-wave amplifier the relationship is

_!_ _p_ + _!_ _p_ = _!_ sig + _!_ id _._ (3.24)

Thinking in the context of quantum mechanics, one need only multiply these equations by
~ to realize that they represent expressions of energy conservation 6 . This also suggests the
reason for the names three-wave and four-wave; a three-wave amplifier turns a pump
photon into a signal photon plus an idler photon, while a four-wave amplifier turns two pump
photons into a signal photon plus an idler photon. This fact is codified mathematically by
the so-called Manley-Rowe relations, which can be derived from the completely classical
theory of coupled oscillator modes and state that, in a parametric amplifier, the power in a
given mode divided by the frequency of that mode is constant across all modes [101].

It is possible to have a parametric amplifier where _!_ sig = _!_ id ; such an amplifier

is called a degenerate parametric amplifier, because the frequencies of the signal and idler
modes are degenerate. A degenerate parametric amplifier is necessarily phase-sensitive; the
pump serves as a reference clock for incoming signals, and signals which are not in phase
with the pump will not be amplified. For a parametric amplifier to be phase-preserving, we
require that _!_ sig = _!_ id . This dovetails nicely with the description of quantum noise limits
_6_
in the previous section, where we showed that a phase-preserving amplifier must have at
least one additional input mode (which we recognize to be the idler) in order to satisfy
the constraints of photon commutation relations, while a phase-sensitive amplifier does not
require an additional input mode (which we recognize as the signal and idler being at the
same frequency).

###### 3.3.1 ###### Brief history of parametric amplification

Parametric amplification has been known and used for a long time [103]. The

idea that a parametrically driven system exhibits energy transfer between coupled modes
was noted by Faraday in 1831 and Lord Rayleigh in the 1880s, who considered oscillations
of mechanical systems in their calculations. Almost a century ago, the first circuit-based
parametric amplifiers were developed to amplify and transmit radio signals [104]. These
amplifiers relied on parametric modulation of the inductance of a resonant circuit by periodic
saturation of the inductors iron core. Just a few years later, though, high power vacuum
tubes became available and took over the market for power amplification of radio signals. It
was not until the late 1940s and early 1950s, after the development of radar and microwave
electronics during World War II led to a need for high-frequency, low-noise amplifiers, that
parametric amplification returned to the scene. Transistors were still a new technology, and

6 It also gives an idea of why the idler must exist; if not for the idler, the only way energy conservation can

be satisfied is to have _!_ _p_ be a multiple of _!_ sig , which as we shall see represents phase-sensitive amplification.


-----


39

early transistors did not function well as amplifiers at microwave frequencies. Parametric
amplifiers using varactor diodes, which operate as voltage-dependent capacitors in certain
bias regimes, became a topic of substantial research interest because they had superior
gain and noise performance at microwave frequencies. In the 1970s, the technology of

heterostructure transistors became sufficiently advanced that transistor amplifiers could
once again compete with parametric amplifiers at microwave frequencies, and in the ensuing
years transistor amplifiers have become the dominant technology for amplifying microwave
signals.

Work on microwave-frequency parametric amplifiers has continued despite the

dominance of the transistor. For example, the traveling-wave tube amplifier (TWTA) uses
parametric modulation of a high-voltage beam of electrons to amplify microwave signals to
very large powers, up to 70 dBm (10 kW). TWTAs are widely used for satellite communications [105]. The first superconducting parametric amplifiers, based on the nonlinear
Josephson inductance, were demonstrated in 1975 [51]. A variety of superconducting parametric amplifier designs followed in the 1980s and 1990s [52, 53, 54, 55, 56], but they tended
to be plagued by spurious noise rise and were not used broadly in applications.

Optical-frequency parametric amplifiers employing nonlinear optical fibers were

also demonstrated in the mid-1970s, and development work continues to the present day.
The performance of these fiber amplifiers has improved in recent years and may someday
be competitive for use in fiber-optic repeaters [106]. Optical parametric amplifiers have also
been used extensively in quantum squeezing experiments [70].

The rapid progress in solid-state quantum measurement and quantum information

of the past decade has renewed interest in superconducting parametric amplifiers. A number
of recent results [57, 58, 59, 60, 107, 108, 109, 110, 111] have demonstrated quantum-limited
noise performance, gains in excess of 30 dB, and quantum squeezing of the microwave vacuum. These properties make superconducting parametric amplifiers attractive candidates
for improving qubit readout.

#### 3.4 #### The Lumped Josephson Parametric Amplifier (LJPA)

The work in this thesis relies on a particular implementation of superconduct-

ing parametric amplifier called the Lumped Josephson Parametric Amplifier (LJPA) 7 . The
LJPA is a nonlinear microwave resonator consisting of a two Josephson junctions in a small
SQUID loop, shunted by a capacitance (the equivalent circuit diagram is shown in Figure
3.3). This is the same basic circuit as the transmon qubit described in Chapter 2, with the
exception that the critical current of the LJPA junctions is much higher than that of the
transmon junctions. In particular, the critical current is large enough that there are many
energy levels in the potential well defined by _E_ _J_ , so we can treat the LJPA as a classical
nonlinear oscillator rather than a quantum one. In the zero-voltage state, the two-junction
SQUID loop acts like a single Josephson junction with a flux-tunable critical current, allowing us to tune the resonant frequency of the LJPA over an octave in frequency, from 4-8

7 The lumped in the name comes from the fact that the circuit is sufficiently small to be treated as a

lumped element at microwave frequencies.


-----


![SlichterThesis.pdf-58-0.png](SlichterThesis.pdf-58-0.png)

![SlichterThesis.pdf-58-1.png](SlichterThesis.pdf-58-1.png)

##### Pump frequency


40

#####  ##### p ##### 0


Figure 3.2: Nonlinear resonance response.

The response of the LJPA resonance is linear for low drive powers, but moves to lower
frequency as the drive power increases, eventually becoming bistable for certain bias parameters. The LJPA can be used as a paramp when biased into the region labeled paramp
by a strong drive tone.

GHz. The fact that one can use this design of lumped Josephson resonator as a paramp
was first noted in R. Vijays thesis [108].

The response of the nonlinear LJPA resonance is shown in cartoon form in Figure


3.2. At low drive power, the resonance is linear, with a resonant frequency _!_ _p_ 0 =


1 _/L_ _J_ 0 _C_ ,


where is the shunt capacitance. As the drive power increases, the resonance bends to lower frequencies, a consequence _L_ _J_ 0 is the Josephson inductance in the absence of driving and _C_
of the particular type of nonlinearity exhibited by the Josephson junctions, and sharpens.
The diagram shows a critical point ( _!_ _c_ _, P_ _c_ ), beyond which the system becomes bistable for
some bias parameters. This bistable regime has been accessed in the Josephson bifurcation
amplifier (JBA)essentially the same circuit as the LJPA for high-fidelity qubit readout

[46, 108].

For parametric amplification, we bias the LJPA into the region labeled paramp

with a strong drive tone that functions as the pump. The pump modulates the nonlinear
Josephson inductance _L_ _J_ . Since _L_ _J_ is an even function of the current through the junctions,
_L_ _J_ is modulated at twice the pump frequency, and the LJPA acts like a four-wave parametric
amplifier. Accordingly, the signal and idler frequencies are symmetric around the pump
frequency.


-----


41


|Col1|C Z 0|
|---|---|


Figure 3.3: Schematic of the LJPA.

The LJPA consists of a SQUID loop, modeled as a single Josephson junction with fluxdependent critical current _I_ 0 , shunted by a capacitance _C_ and an real impedance _Z_ 0 . We
can study the dynamics of the system mathematically by adding a drive current _I_ ( _t_ ).

###### 3.4.1 ###### Mathematical description

A schematic diagram of the LJPA circuit is shown in Figure 3.3. We treat the

SQUID loop as a junction with critical current _I_ 0 , shunted by a capacitance _C_ and the
impedance _Z_ 0 of the microwave environment 8 . We apply a current _I_ ( _t_ ) to the circuit from
an external source. Using the Josephson relations and Kirchos laws, we can describe the
behavior of this circuit with the following dierential equation:


_d_ 2 __ ( _t_ )



 0
_C_

2 __



 0
_C_


__ ( _t_ ) + 1

_dt_ 2 _Z_


 0
2 __


_d_ ( _t_ )

+ _I_ 0 sin( __ ( _t_ )) = _I_ ( _t_ ) _._ (3.25)
_dt_


_d_ ( _t_


_Z_


Lets take our externally applied current to be a sinusoidal pump tone of the form _I_ ( _t_ ) =
_I_ _d_ cos( _!_ _d_ _t_ ), with _I_ _d_ _< I_ 0 , and replace the sin __ term with its Taylor expansion, keeping only
the first nonlinear term. The resulting equation, known as the Duffing equation, greatly
simplifies the algebra while accurately reproducing the dynamics of the system [112], and
is given by


_d_ 2 __ ( _t_


__ ( _t_ ) _d_ ( _t_ )

+ 2
_dt_ 2 _dt_



__ ( _t_ ) 3
__ ( _t_ )
__ 6


2 __

_I_ _d_ cos( _!_ _d_ _t_ ) _,_ (3.26)
 0 _C_


2 __


_dt_ + _!_ _p_ 2


_p_ 0


where _!_ _p_ 0 =


2 _I_ 0 _/_  0 _C_ is the oscillators resonant frequency (or plasma frequency) at


low drive amplitude and  = 1 _/_ 2 _Z_ 0 _C_ is the damping rate of the oscillation amplitude. We
can solve this equation using an ansatz of the form

__ ( _t_ ) = __ 0 cos( _!_ _d_ _t_ __ __ ) _._ (3.27)


To make it easier to solve equation (3.26), it is useful to parameterize the ansatz as a pair
of quadrature amplitudes __ and __ , with __ 0 2 = __ 2 + __ 2 and tan __ = __ _/_ . Our ansatz then
_||_ _?_ _||_ _?_ _?_ _||_


takes the form


0 2 = __ 2



2 + __ 2

_||_



2 and tan __ = __ _/_ . Our ansatz then

_?_ _?_ _||_


__ ( _t_ ) = __ cos( _!_ _d_ _t_ ) + __ sin( _!_ _d_ _t_ ) _,_ (3.28)
_||_ _?_

8 We use dierential excitation with a 180 __ hybrid for our paramps as described in sections 5.1 and 6.1,

so in our case _Z_ 0 = 100 .


-----


42

|Col1|0.01 0.02 I/I 0.03 d 0 0.04 0.05 0.06|
|---|---|



4 0 -4 -8

Detuning  = 2 _Q_ (1-  d / p0 )


180

135

90

45


1.50

1.25

1.00

0.75

0.50

0.25

0.00

|Col1|0.01 0.02 I d/I 0 0.03 0.04 0.05 0.06|
|---|---|


4 0 -4 -8

Detuning  = 2 _Q_ (1-  d / p0 )


Figure 3.4: Nonlinear resonance solutions.

We plot solutions for equation (3.26) in terms of the parameters __ 0 and __ defined in equation
(3.27). At low drive strengths, the response is linear. As the drive amplitude increases, the
resonance moves to lower frequencies and finally becomes bistable. The vertical dashed line
and three circles highlight the three solutions (of which the middle solution represents an
unstable state) in the bistable regime.

and we can solve for the values of __ and __ by plugging into equation (3.26). We make the
_||_ _?_
rotating wave approximation, replacing terms oscillating at 2 _!_ _d_ and 3 _!_ _d_ with their averages,
to yield two coupled cubic equations


__ + __
__ _||_ _?_



_Q_
 __


8 ( __ 2



2 + __ 2

_||_



2 )

_?_


= 0 (3.29)


and


__ + __
_?_ _||_



_Q_
 __


8 ( __ 2



2 + __ 2

_||_



2 )

_?_


= _QI_ _d_ _/I_ 0 _,_ (3.30)


where = 2 _Q_ (1 _!_ _d_ _/!_ _p_ 0 ) is the dimensionless detuning of the drive from the resonant
__
frequency and _Q_ = _!_ _p_ 0 _Z_ 0 _C_ is the quality factor of the resonator.

Since these equations are cubic, we expect in general that there will be three


solutions for _{_ __ _||_ _, _ _?_ _}_ and thus for _{_ __ 0 _, _ _}_ . For  _>_


3, there exist some ranges of _I_ _d_ for


which there are three distinct real solutions; this is the bistable regime, and the largest and
smallest values of __ 0 are the stable states. For  _<_ _p_ 3, where the paramp regime falls, only


3, where the paramp regime falls, only


one real-valued solution exists for __ 0 _, _ .
_{_ _}_

Figure 3.4 shows a family of solutions for __ 0 and __ at dierent values of _I_ _d_ as


one real-valued solution exists for __ 0 _, _ .
_{_ _}_


a function of the dimensionless detuning . As shown qualitatively in Figure 3.2, the


resonance moves to lower frequency with increasing drive power, finally becoming bistable
at some bias values. The response is single-valued for  _<_ _p_ 3, as well as for  _p_ 3 at


3, as well as for  __


3 at


sufficiently low or high drive amplitude. The curve for _I_ _d_ _/I_ 0 = 0 _._ 04, with a steepened but
single-valued response, represents the paramp regime. We note that the amplitude __ 0 . 0 _._ 8
for the paramp regime, so our use of the Duffing approximation sin __ __ __ __ __ 3 _/_ 6 is accurate
to better than 0 _._ 4%.


-----


43

###### 3.4.2 ###### Theoretical gain and bandwidth

Now we add a small signal slightly detuned from the pump tone to characterize

the gain and bandwidth of the amplifier. A detailed derivation of these results has been
presented in several theses [108, 109], so we will give only a brief sketch. We take the signal
to have the form _I_ _s_ ( _t_ ) = _I_ _s_ cos( _!_ _d_ _t_ + _!_ _s_ _t_ ), where _!_ _s_ __ _!_ _d_ and _I_ _s_ __ _I_ _d_ . In this case, we
can treat the signal as a small perturbation on the strong pump, and we predict that the
solution to (3.26) will be of the form

__ ( _t_ ) = __ 0 cos( _!_ _d_ _t_ __ __ ) + __ ( _t_ ) _,_ (3.31)

where __ ( _t_ ) represents the response due to the presence of the weak signal. Plugging this into
equation (3.26) and using the fact that __ ( _t_ ) = __ 0 cos( _!_ _d_ _t_ __ __ ) is a solution in the absence of
a signal tone, we get a dierential equation for __ of the form


_d_ 2 __ ( _t_ )



2 __ ( _t_ ) _d_ ( _t_

+ 2
_dt_ 2 _dt_


1 __ 0 2
__ 4


0 2 __ 0

4 __


2 __

_I_ _s_ cos( _!_ _d_ _t_ + _!_ _s_ _t_ ) _._ (3.32)
 0 _C_


2 __


_dt_ + __ ( _t_ ) _!_ _p_ 2


_p_ 0



cos(2 _!_ _d_ _t_ 2 __ )
4 __


The left-hand side of this equation is that of a parametrically driven harmonic oscillator
whose resonant frequency is being modulated at 2 _!_ _d_ 9 . We can use input-output theory

[69] to write down the voltage amplitudes of incoming and outgoing waves in our reflection
geometry in terms of the input signal amplitude _V_ _s_ = _I_ _s_ _Z_ 0 and _V_ _J_ = ( 0 _/_ 2 __ ) _d/dt_ , the
voltage across the junction. This gives us two equations:


_V_ _s_ ( _t_ ) = 2 _V_ in ( _t_ ) (3.33)


_V_ out ( _t_ ) = _V_ _J_ ( _t_ ) _V_ in ( _t_ ) _._ (3.34)
__

We can take the Fourier transform of equation (3.32) and solve for the relationship between
_V_ in ( _t_ ) and _V_ out ( _t_ ) in the frequency domain, which makes the analysis simple because our
signal is harmonic. The parametric driving gives rise to a coupling between the modes at
_!_ . We recognize this second mode as the idler frequency in our fourwave parametric amplifier. The gain is defined as the ratio of the power in signal and idler _d_ + _!_ _s_ and _!_ _d_ __ _!_ _s_
output modes to that in the input mode, and depends on the signal frequency and pump
parameters. We can write down closed-form expressions for this gain, which we call _G_ _s_ for
the signal (or direct) gain and _G_ _i_ for the idler (or trans) gain 10 :


and


4 __ 2
_G_ _s_ ( _f_ ) = 1 + [( __ 2 __ ) 2 __ __ 2 + 1] 2 __ 2 _f_ 2 [( __ 2 __ ) 2 __ __ 2 __ 1] (3.35)


where we have introduced the notation __ = _Q_ 2


_G_ _i_ ( _f_ ) = _G_ _s_ ( _f_ ) 1 _,_ (3.36)
__


0 2 _/_ 8 to characterize the drive amplitude 11


9 The fact that the modulation is at 2 _!_ _d_ while the pump frequency is at _!_ _d_ arises because the Josephson


inductance is an even function of __ , so a drive at _!_ _d_ modulates the Josephson inductance and thus the
resonant frequency of the oscillator at 2 _!_ _d_ .


10 We have dropped an _f_ 4 term in the denominator of this expression, which has a negligible eect, to


highlight the Lorentzian shape of the gain profile. This _f_ 4 term is not dropped in the gain expressions given
in refs. [61] and [108]. We also note that there are typographical errors in the expressions for _G_ _s_ and _f_
given in [61], which have been corrected here.


-----


44

_6_


25

20

15

10

_6_


![SlichterThesis.pdf-62-0.png](SlichterThesis.pdf-62-0.png)

-4 -3 -2 -1 0 1 2 3 4

Signal detuning _f_

Figure 3.5: Theoretical gain and bandwidth.

_6_


These curves show the gain and bandwidth of the LJPA for varying values of the pump
drive strength __ at a pump detuning = 0 _._ 98 _p_ 3. Note that the bandwidth is given in

units of the reduced signal detuning _f_ , indicating that a lower _Q_ paramp resonator will
give correspondingly broader absolute instantaneous bandwidth. We can trade gain for

additional bandwidth by driving at _> _ max .

and defined the dimensionless signal-pump detuning frequency _f_ = 2 _Q_ ( _!_ _s_ _/!_ _p_ 0 ). A quick
check of these equations shows that, in the limit of no pump ( __ _!_ 0), we recover _G_ _s_ = 1
and _G_ _i_ = 0, as we would expect for the case of no amplification. For large gain, we have
_G_ _s_ _G_ _i_ , again as expected. In the limit of small signal detuning _f_ 0, we can optimize
__ _!_
the gain with respect to the pump amplitude, yielding a value for __ which maximizes the
gain:

_6_


__ max =

_6_


1 +  2

_6_


(3.37)

_6_


Figure 3.5 shows the value of _G_ _s_ ( _f_ ) for several dierent values of the drive amplitude __ .
The bandwidth is a monotonically increasing function of __ , while the gain reaches a peak
at __ max and then decreases at higher drive amplitudes. For signal detunings _f_ _6_ = 0, the
maximum gain may come for __ = _6_ __ max . We can calculate the drive current amplitude _I_ _d_ at
__ max , which is given by the expression


_6_

_I_ 2


_6_

_d_ 2 = 16 _I_ 0


_6_

0 2 )(2

3 _Q_ 3 (1 + 


_6_

1 +  2 __


_6_

3) _._ (3.38)


_6_

This gives us a scale for a typical pump power we might expect to use for amplification. For
typical amplifier parameters _I_ 0 3 4 __ A, _Q_ 20 25,  _p_ 3, we find that the pump
__ __ 12 __ __ __


_6_

3, we find that the pump


_6_

power should be around -90 to -95 dBm 12 . This in turn sets a scale for the strength of the
input signals, since we require that _I_ _s_ __ _I_ _d_ in our analysis.


_6_

11 Note that in ref. [108] the notation __ is used for what we call __ .
12 The units dBm, commonly used in microwave frequency applications, are absolute logarithmic power


_6_

units, defined as _P_ dBm = 10 log 10 _P_ mW , where _P_ mW is the power in milliwatts.


-----


45


In the _f_ _!_ 0 limit, we can use the expression for __ max to derive an expression for

the maximum gain:


_G_ max = 1 +


(3.39)
1 +  2 _._


This expression diverges for =


3; in practice, however, higher order eects will cause


3 + 7 2 __ 4


3


the gain to remain finite. At the maximum gain point, we can substitute the value of __ max
into (3.35), re-expressing the frequency-dependent gain as:


_G_ max
_G_ _s_ ( _f_ ) __ 1 + _f_ 2 ( _kG_ max ) _,_ (3.40)

where _k_ is a constant of order unity given by the expression


1 +  2 )



(3 2
_k_ = __ __


_._ (3.41)
1 +  2


In the limit  _!_


3, we find _k_ 3 4
_!_



3 4 . Equation (3.40) highlights the Lorentzian nature of


the gain profile, and gives us a relation between the gain and the bandwidth of the amplifier;
using the definition of _f_ , we can write the half-width half-maximum bandwidth _B_ LJPA as


_!_ _p_ 0
_B_ LJPA = 4 _Q_ _p_ _kG_ max


_!_ _p_ 0
_B_ LJPA =


(3.42)


This expression shows that the gain-bandwidth product 13 is constant for the LJPA, and
is given by _B_ LJPA _p_ _G_ max = _!_ _p_ 0 _/_ 4 _Q_ _p_ _k_ . We can see that using a low- _Q_ resonator as our


_p_ _G_ max = _!_ _p_ 0 _/_ 4 _Q_


_k_ . We can see that using a low- _Q_ resonator as our


paramp increases the gain-bandwidth product.

###### 3.4.3 ###### Physical description of operation

It is helpful to have a physical understanding of the mechanism of amplification,

beyond just the math, which is what we hope to provide in this section. All amplifiers have
a transfer function which relates the input quantity to the output quantity. For a field-eect
transistor, for example, the transfer function is the transconductance, which relates the gate
voltage to the source-drain current. To make a useful transistor amplifier, one constructs
and biases a circuit in such a way that a small change in gate voltage will give rise to a
large change in source-drain current. A dc SQUID amplifier has a flux-to-voltage transfer
function _V_  , allowing small flux signals to be converted into larger voltage signals. When
the flux and SQUID current are correctly biased, small changes in flux eect large changes
in voltage.

For the LJPA, the transfer function is the change in the phase of the reflected

pump tone with respect to the pump amplitude; note that this is not the same as the
phase __ of __ ( _t_ ), though the two are related. As we increase the amplitude of the pump
and sweep through resonance, the phase of the reflected pump changes rapidly. The phase
changes about 60 __ __ 90 __ over a very small range in pump amplitude, with the overall phase
shift across the resonance equal to about 180 __ . This phase shift is a manifestation of the


-----


46

![SlichterThesis.pdf-64-0.png](SlichterThesis.pdf-64-0.png)

0.02 0.04 0.06 0.08 0.10

Drive current (I _d_ /I 0 )


180

90

0

-90

-180


Figure 3.6: Paramp transfer function: reflected phase vs. pump amplitude.


We show three theoretical traces of the phase of the reflected pump tone as a function of the
dimensionless detuning for _Q_ = 20. These traces can be thought of as vertical linecuts of
Fig 3.2 in the paramp regime, with = _p_ 3 corresponding to the critical point.

nonlinearity of the LJPA; a linear resonator shows no phase response with changes in drive
amplitude.

Figure 3.6 shows three sample theoretical traces of the reflected phase of the


paramp for three dierent values of the dimensionless detuning . As  _!_


3, in other


words, as the pump frequency approaches the bifurcation point, the phase response steepens. The physical mechanism by which gain occurs can be understood using this transfer
function. When the pump amplitude is chosen so that we are biased on the steepest part
of the transfer function, any small modulations of the pump amplitude will lead to modulations of its reflected phase. The transfer function is approximately linear over a small
range of pump amplitudes, so we will have a linear relation between the reflected pump
phase and its amplitude. The theoretical power gain when biased at the steepest part of
the transfer function is given by equation (3.39) and is 10, 70, and 10 4 for the blue, green,
and red traces respectively.


We consider first the case where our signal is at the same frequency as the pump;

this is the doubly-degenerate mode of operation (so named because signal and pump frequencies are degenerate, and we have four-wave mixing) and will give us phase-sensitive
amplification, as described in section 3.2.1. If the signal is in phase with the pump, they
will add coherently and the eective pump amplitude will be changed slightly. This is shown
schematically in the IQ plane in Figure 3.7(a). Any shifts in the amplitude of the signal
will cause shifts of the same magnitude in the eective pump amplitude. These amplitude
shifts move us left and right along the paramp transfer function, shown in cartoon form in
Figure 3.7(b), giving rise to phase shifts in the reflected pump tone. We plot the reflected


13 The gain-bandwidth product is defined in terms of amplitude gain, not power gain; the amplitude gain

is _p_ _G_ max .


-----


47


(a) Q (b) (c)


+90



-90

|Signal in phase|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||


![SlichterThesis.pdf-65-0.png](SlichterThesis.pdf-65-0.png)

Pump power

![SlichterThesis.pdf-65-1.png](SlichterThesis.pdf-65-1.png)

(d) Q (e) (f)


+90


|Q (f)|Col2|
|---|---|
|(f) Q UTPUT reflected pump||
|||


![SlichterThesis.pdf-65-2.png](SlichterThesis.pdf-65-2.png)

Pump power


INPUT

signal


-90

|Q|Col2|
|---|---|
|Q pump||
|||


Figure 3.7: Phase-sensitive amplification in the IQ plane.

Parts (a-c) treat a signal in phase with the pump. A signal (green) in phase with the pump
(red) will add or subtract coherently with it, modulating its amplitude slightly (light red
arrows). Note that we exaggerate the magnitude of the signal relative to the pump in parts
(a) and (d) for clarity. If the pump is biased at the steep part of the transfer function,
as seen in part (b), this pump amplitude modulation will lead to a phase modulation on
the reflected pump. Sketching the output signal in the IQ plane in (c), we note that the
vector dierence between output states (the phase-shifted reflected pump) is much larger
than that between input signal states, meaning we have achieved power gain. In parts (d-f),
the signal is in quadrature with the pump. As a result, the amplitude of the vector sum
of the signal and pump (light red arrows) is the same to first order as the original pump
amplitude. This means that the signal only makes a very small modulation of the reflected
pump phase, as seen in (e), and the vector dierence between output states shown in (f)
is smaller than that of the input signal. This represents de-amplification of the quadrature
signal.


-----


48

pump in the IQ plane in part (c). For sufficiently small signal amplitudes, there will be a
linear relation between the signal amplitude and the reflected pump phase.

How does this represent amplification? The output signal is the phase shift on

the reflected pump tone, which is much stronger than the input signal. The information
carried in the amplitude of the input signal has been mapped linearly to the phase of the
much stronger reflected pump. In the IQ plane, we see the vector dierence between the
output states is larger than the vector dierence between the input states. This represents
power gain and thus is amplification by our definition. To reconstruct the original signal
from the amplified one, we can simply extract the phase of the output signal and use the
linear mapping between input amplitude and output phase to determine what the original
signal was.

The phase-sensitive nature of this method can be seen if one considers a signal in

quadrature with the pump tone. Such a signal will leave the pump amplitude unchanged
to first order. This can be seen in Figure 3.7(d), where the vector sum of the signal and
pump in the IQ plane has essentially the same magnitude as the original pump vector. As
a result, the pump amplitude moves very little along the transfer function, seen in part (e),
and thus the phase of the reflected pump changes very little. The signal ends up actually
being de-amplified; the vector dierence between output states in the IQ plane is less than
that between the input signals.

Now lets consider the case where there is input noise in addition to the signal (we

know that we will always have at least have quantum zero-point fluctuations, no matter
what the signal is). Noise at the signal frequency will modulate the pump amplitude in
exactly the same way as the signal does: in-phase noise will lead to noise on the reflected
pump phase, while quadrature noise will be de-amplified. Since the amplifier treats the
input signal and input noise on the same footing, we will have the same gain for signal and
noise; in particular, no quadrature noise will be amplified. This means that the signal-tonoise ratio is preserved by the amplifier, which can only happen if the amplifier itself adds
no noise (see Figure 3.1). We can see therefore from transfer function arguments why the
phase-sensitive mode of the LJPA paramp should give noiseless amplification.

Phase-sensitive amplification is unfortunately only useful when one knows the

phase of the incoming signal. This is not the case for arbitrary signals, but for a circuit
QED readout signal one can control the phase of the readout tone relative to the paramp
pump and thus ensure that the readout signal lies in the amplified quadrature. We utilize
phase-sensitive amplification in the quantum jump experiments detailed in Chapters 7 and
8 because of its superior noise performance.

Phase-preserving amplification is more broadly applicable than phase-sensitive am-

plification, although we pay for this with decreased noise performance. We can understand
the mechanism for phase-preserving amplification using the same idea of the transfer function. Here we have an input signal at frequency _!_ _d_ + _!_ _s_ . For maximum amplification to
occur, we require _!_ _s_ __ _!_ _d_ _/Q_ _p_ _G_ _s_ (the signal detuning must be small compared to the
linewidth of the paramp resonance divided by the amplitude gain; compare with equation
(3.42)). This criterion is roughly equivalent to _f_ _p_ _G_ _s_ , which is the bandwidth criterion
__
for high gain seen in equation (3.40). Physically, this constraint means that _!_ _s_ is sufficiently
slow that the pump amplitude can respond to modulation at that frequency.


-----


49

![SlichterThesis.pdf-67-0.png](SlichterThesis.pdf-67-0.png)

Pump power



+90

-90


|a)|Q|
|---|---|
|NPUT  s|Q  pump s I|
|signal||


Figure 3.8: Phase-preserving amplification in the IQ plane.

In phase-preserving mode, the input appears as a small signal rotating at frequency _!_ _s_ in
the IQ plane frame rotating at _!_ _d_ . This signal introduces a sinusoidal modulation on the
pump amplitude, which becomes a sinusoidal phase modulation of the reflected pump as
shown in (b). Since the signal amplitude is much smaller than the pump amplitude, the
reflected pump exhibits a double-sideband phase modulation. These two sidebands are the
signal and the idler of the paramp.

If we look in the IQ plane in the frame rotating at _!_ _d_ , the signal looks like a small

vector rotating at _!_ _s_ , as shown in Figure 3.8. As is evident from the picture, this signal
will modulate the pump amplitude at frequency _!_ _s_ as well. We can parameterize the input
signal in the rotating frame in terms of two time-varying amplitudes, one in phase with the
pump ( _A_ _s_ _||_ ) and one in quadrature with the pump ( _A_ _s_ _?_ ),

_A_ _s_ _||_ ( _t_ ) = _A_ _s_ ( _t_ ) cos( _!_ _s_ _t_ + __ _s_ ( _t_ )) (3.43)

_A_ _s_ _?_ ( _t_ ) = _A_ _s_ ( _t_ ) sin( _!_ _s_ _t_ + __ _s_ ( _t_ )) _,_ (3.44)

where _A_ _s_ ( _t_ ) is the amplitude of the input signal and __ _s_ ( _t_ ) is its phase 14 . In this way we have
decomposed the signal at _!_ _d_ + _!_ _s_ into two quadrature signals at frequency _!_ _d_ , each of which
will undergo phase-sensitive amplification as described previously. The quadrature _A_ _s_ _||_ ( _t_ )
will modulate the pump amplitude (since it is in phase with the pump) and be amplified,
while _A_ _s_ _?_ ( _t_ ) will not modulate the pump amplitude (since it is in quadrature with the
pump) and thus be de-amplified. However, since _A_ _s_ _||_ ( _t_ ) contains information on both the
amplitude _A_ _s_ ( _t_ ) and phase __ _s_ ( _t_ ) of the input signal, we will get both amplitude and phase
information on the output signal, realizing phase-preserving amplification. If we assume
for a moment that _A_ _s_ and __ _s_ are constant, we will have a sinusoidal modulation of pump
amplitude from _A_ _s_ _||_ ( _t_ ), which will result in a sinusoidal phase modulation of the reflected
pump, as shown in Figure 3.8(b).

14 An input signal of the form _A_ _s_ ( _t_ ) cos( _!_ _d_ _t_ + _!_ _s_ _t_ + __ _s_ ( _t_ )) can be re-expressed as _A_ _s_ ( _t_ ) cos( _!_ _d_ _t_ ) cos( _!_ _s_ _t_ +

__ _s_ ( _t_ )) _A_ _s_ ( _t_ ) sin( _!_ _d_ _t_ ) sin( _!_ _s_ _t_ + __ _s_ ( _t_
)) using trigonometric identities. We can rewrite this as the two quadratures of a signal at __ _!_ _d_ as _A_ _s_ _||_ ( _t_ ) cos( _!_ _d_ _t_ ) __ _A_ _s_ _?_ ( _t_ ) sin( _!_ _d_ _t_ ), where the quadrature amplitudes are as given in
equations (3.43) and (3.43). The minus sign can be eliminated by the choice of reference phase.


-----


50


SNR= S

N

|SNR|Col2|Col3|
|---|---|---|
||||


![SlichterThesis.pdf-68-0.png](SlichterThesis.pdf-68-0.png)


![SlichterThesis.pdf-68-1.png](SlichterThesis.pdf-68-1.png)

![SlichterThesis.pdf-68-5.png](SlichterThesis.pdf-68-5.png)


2N


![SlichterThesis.pdf-68-8.png](SlichterThesis.pdf-68-8.png)

![SlichterThesis.pdf-68-4.png](SlichterThesis.pdf-68-4.png)

![SlichterThesis.pdf-68-2.png](SlichterThesis.pdf-68-2.png)

![SlichterThesis.pdf-68-3.png](SlichterThesis.pdf-68-3.png)

![SlichterThesis.pdf-68-7.png](SlichterThesis.pdf-68-7.png)

![SlichterThesis.pdf-68-6.png](SlichterThesis.pdf-68-6.png)

S
N


 d -  s  d  d +  s

|G i S SNR= N|Col2|Col3|
|---|---|---|
||||



Figure 3.9: Amplification and noise for a detuned signal.

The top portion of this figure shows the input pump (green) and single-sideband input
signal (blue) in addition to the input noise floor (red) composed of quantum zero-point
fluctuations. The phase-preserving parametric amplification process gives both direct gain
(vertical arrows) and trans gain (diagonal arrows) at the signal and idler frequencies. The
output signal is a double-sideband signal, where each sideband has half the signal-to-noise
ratio (SNR) of the original input signal because of the presence of additional amplified
vacuum fluctuations from the idler input. This is the realization of the quantum limit on
phase-preserving amplification derived in section 3.2.


The quadrature _A_ _s_ _||_ ( _t_ ) and its noise will be amplified with the same gain (and noise


on _A_ _s_ _?_ ( _t_ ) will be de-amplified), so one might guess that this is again noiseless amplification
as in the phase-sensitive case. However, we have neglected to consider vacuum fluctuations
at the idler frequency _!_ _d_ _!_ _s_ . This noise will also modulate the pump amplitude at
__


frequency _!_ _s_ (in a counter-rotating sense relative to the signal) and be amplified. Thus
the output signal will have an additional ~ ( _!_ _d_ __ _!_ _s_ ) _/_ 2 of added noise referred to the input
and the amplification process is no longer noiseless, in keeping with the quantum limits on
phase-preserving amplifiers described in section 3.2.


We can see this eect more clearly by thinking in terms of the frequency spectrum.

The quadrature _A_ _s_ ( _t_ ) modulates the initial amplitude _A_ 0 of the pump, and the modulated
_||_


-----


51

amplitude _A_ pump is given by


_A_ pump =


( _A_ 0 + _A_ _s_ ( _t_ )
_||_


cos( _!_ _d_ _t_ )


(3.45)


= _A_ 0 cos( _!_ _d_ _t_ ) + _A_ _s_ ( _t_ ) cos( _!_ _s_ _t_ + __ _s_ ( _t_ )) cos( _!_ _d_ _t_ ) _._


Using trigonometric identities, we can rewrite this as:






1
_A_ pump = _A_ 0 cos( _!_ _d_ _t_ ) + _A_ _s_ ( _t_ )

2



1
_A_ pump = _A_ 0 cos( _!_ _d_ _t_ ) +


cos


_!_ _d_ _t_ + _!_ _s_ _t_ + __ _s_ ( _t_ )


+ cos


_!_ _d_ _t_ _!_ _s_ _t_ __ _s_ ( _t_ )
__ __


_._ (3.46)


Recalling that _A_ 0 __ _A_ _s_ , we can see that this is the equation for a carrier tone at _!_ _d_ with
two smaller sidebands detuned by _!_ _s_ . Since the pump amplitude is linearly mapped into
__
the phase of the output signal, we should see two sidebands at _!_ _d_ _!_ _s_ on the output signal

15 __
as well . These represent the signal and the idler of the paramp, as described in section
3.3. We note that the pump amplitude contains information on both the amplitude _A_ _s_ ( _t_ )
and phase __ _s_ ( _t_ ) of the input signal, meaning that the output signal will also contain this
information. The maintenance of both input amplitude and input phase information on the
output signal demonstrates that this is phase-preserving amplification of the input signal.


Figure 3.9 draws the frequency spectrum of the input (top) and output (bottom),

showing the pump, signal, and idler. The arrows in between show both the direct gain
_G_ _s_ (signal to signal and idler to idler) and the trans gain _G_ _i_ (signal to idler and idler to
signal). In the high gain regime, _G_ _s_ _G_ _i_ , as seen from equation (3.36). The signal (blue
__
arrows) and its noise (red arrows) are amplified with the same direct gain, but noise (red
arrows) from the idler frequency is mixed in by the trans gain and degrades the overall
signal-to-noise ratio. If the input noise at both signal and idler frequencies is just due to
quantum zero-point fluctuations, this process adds half a photon of noise (referred to the
input) to the amplified signal, the minimum required by quantum mechanics. In the limit
of no amplification _G_ _s_ = 1 and _G_ _i_ = 0, so the amplifier simply reflects the signal without
adding any noise or creating an idler.

###### 3.4.4 ###### Saturated regime operation

The above results are derived for the small-signal regime, where we assume we are

always in the linear region of the transfer function. When the signal amplitude becomes
large enough that we leave the linear transfer region, the output signal is no longer linearly
related to the input signal, a phenomenon called saturation. In an op-amp, saturation can
occur when one attempts to drive the output signal past the voltage supplies, causing it to
rail. In the LJPA, saturation occurs when the signal modulates the pump amplitude far
enough that the slope of the transfer function starts to flatten out 16 .

15 The output signal shows phase modulation, not amplitude modulation. However, given a harmonic input

signal small enough to remain in the linear regime of the transfer function, the output phase modulation
has the same frequency spectrum as the pump amplitude modulation.

16 The range of signal powers over which the amplifier behaves linearly is called its dynamic range; the

dynamic range of the LJPA is set by the width in pump amplitude of the linear part of the transfer function.
Alternatively, one can think about dynamic range and paramp saturation in terms of pump depletion. The
process of parametric amplification transfers energy from the pump to the signal and the idler. If the power
of the output signal becomes large enough, the transfer of power from pump to signal becomes significant
enough to deplete (reduce the power of) the pump. When the pump starts to become depleted, there is less
pump energy to transfer into signal and idler tones and so the gain is decreased.


-----


52

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||



Pump power



+90


+90


-90


-90


![SlichterThesis.pdf-70-0.png](SlichterThesis.pdf-70-0.png)

Pump power


Figure 3.10: Saturated regime amplification.

A large-amplitude sinusoidal signal modulating the pump amplitude is not faithfully reproduced in the output signal. The extrema of the sinusoid are flattened and reduced in
amplitude. However, a square wave signal (one which modulates the pump between two
dierent amplitudes) will give rise to a square wave output signal. The eective square
wave transfer function (dashed purple line) has a reduced slope compared to the original
transfer function, indicating the reduced gain that typifies amplifier saturation.

The eects of saturation on sinusoidal and square wave modulations are shown in

Figure 3.10. For signals which give a sinusoidal pump modulation, the output signal in the
saturated regime will be a distorted sinusoid with flattened peaks. This distortion renders
the amplifier much less useful. However, if the signal is a square wave which modulates
the pump amplitude between two specific values, the output signal will also be a square
wave, with a one-to-one mapping between output phase and pump amplitude. In this way,
input signals which switch between two states are faithfully amplified even in the saturated
regime. This is fortuitous, because we get exactly this type of signal from circuit QED
qubit readout. By choosing the pump bias properly, we can use the paramp to amplify
qubit readout signals even though the power from the readout signal exceeds the dynamic
range of the paramp.

Lets examine the behavior of a square wave signal undergoing phase-sensitive

amplification in the saturated regime. The output signal is the phase shift on the reflected
pump; however, once we have saturated the paramp, this will always be __ 180 __ , no matter
the input signal strength. With the output signal fixed, increases in the input signal must
correspond to decreases in gain of the same amount. This reduction in gain with increasing
signal amplitude is a hallmark of a saturated amplifier. If one draws an eective paramp
transfer function (shown in Figure 3.10(b) as a purple dashed line), one sees that the eective
transfer function is less steep than the original one, indicating reduced gain.

The noise performance is also degraded in the saturated regime. When the paramp

saturates, the amplitude of the output signal no longer grows with increasing input signal
amplitude. Noise on the input signal continues to be amplified, although the noise gain
decreases gradually as the paramp moves farther into the saturated regime. As a result,
the output signal-to-noise ratio (SNR) plateaus and grows only sub-linearly with increasing
input SNR; the output signal is fixed, while the output noise is slowly decreasing. When


-----


53

the paramp is deeply saturated, the output SNR will be considerably lower than the input
SNR. Thus the amplification process degrades the SNR, which we can think of in terms of
the amplifier adding noise. The farther we go into the saturated regime, the greater the
SNR degradation, and thus the higher the noise temperature of the paramp. It is important
to note, however, that the output SNR is still a monotonically increasing function of input
SNR.


-----


54

## Chapter 4

# Sample fabrication

This chapter describes the fabrication techniques used to make superconducting

qubits, resonators, and parametric amplifiers. The methods for making these devices are
straightforward, but achieving reliable and high-quality results requires attention to detail,
a great deal of patience, and sometimes a bit of luck. We detail a few tricks used for

successful sample fabrication, to save the reader the trouble of rediscovering them. Further
specifics of recipes will be presented in Appendix B.

#### 4.1 #### Electron-beam lithography

All of the samples described in this thesis were made with electron-beam lithog-

raphy, a standard technique for fabricating very high resolution features. Electron-beam
lithography allows structures to be defined by first coating the substrate of interest with
some form of resist, then selectively damaging (exposing) the resist in certain desired regions
using a finely focused beam of high-speed electrons. The exposed resist is then washed away
by a chemical developer, leaving a patterned mask of resist on the surface. The samples
described in this thesis are made by depositing thin films of aluminum or niobium on top
of this mask, which serves as a sort of stencil. The mask is then chemically dissolved, with
the metal on top of the mask lifting o to leave behind metal on the substrate in the
pattern defined by the electron beam exposure.

The focused electron beam used for lithography comes from a scanning electron

microscope (SEM), a modified FEI Nova NanoSEM depicted in Figure 4.1. This microscope uses a field emission tip as the electron source, so the electrons come from a smaller
region than with a hot filament emitter. This allows the beam to be more finely focused
than with a filament SEM, giving better resolution for both imaging and lithography. The
imaging resolution has been measured to be __ 1.2 nm, and the system is capable of reliably
making 20 nm lithographic features. The SEM is be turned over to remote control by a
computer running Nanometer Pattern Generation System (NPGS) software during lithography. NPGS can control the position of the beam, its focus, the magnification, and even
the position of the sample stage, allowing the e-beam writing process to be fully automated
for samples from small test structures to entire wafers of ground planes.

For optimal resolution, the electron beam should have the highest possible accel-


-----


55


![SlichterThesis.pdf-73-1.png](SlichterThesis.pdf-73-1.png)

![SlichterThesis.pdf-73-0.png](SlichterThesis.pdf-73-0.png)

![SlichterThesis.pdf-73-2.png](SlichterThesis.pdf-73-2.png)

Figure 4.1: Tools of the fab trade.

The scanning electron microscope in (a) has been modified to allow remote control by NPGS
pattern generation software, allowing it to be used to for e-beam lithography in addition
to imaging. The electron source is a field emission tip, giving very high resolution. Part
(b) shows a sample holder for lithography, showing gold standard, Faraday cup, and spring
clips for holding the sample. The cold developer setup is seen in (c), consisting of a beaker
of ice-water slush in an insulating jacket with a smaller beaker of developer resting inside.

erating voltage; we use 30 kV, the maximum for our system. Dedicated e-beam writers in
the UC Berkeley Nanolab and the Lawrence Berkeley Lab Molecular Foundry can run at
50 kV or 100 kV, but this is not necessary to achieve suitable resolution for qubit samples.
Higher accelerating voltages are useful because they minimize the spread of the electron
beam as it scatters oof atoms in the resist and the substrate [113]. Due to this scattering,
very fine (10-20 nm) features should be made on the thinnest possible resist stack. Another
essential element for good lithography is careful optimization of the electron beam profile
by adjusting the focus, stigmation, and lens alignment. For this purpose, our sample holder
includes a viewing standard containing gold balls on a graphite substrate, which allows very
precise beam optimization before lithography. In addition, drops of a colloidal solution of
100 nm and 40 nm diameter gold balls are added on the substrate surface itself, to allow final focusing and correction for any tilt in the substrate relative to the beam axis. To ensure
fine lithography, one needs to write above a certain minimum SEM magnification setting
(about 1300x) so that the fine scan coils will be used instead of the coarse scan coils. This
eect is show in Figure 4.2(c) and (d). Finally, it is important to know the beam current
accurately to be able to give the correct dose. To do this, the sample holder includes a
Faraday cup, made by covering a small hole drilled in the holder with a single-hole TEM
grid glued down with carbon paint. We measure the current by steering the beam into the
Faraday cup and reading out the current on a picoammeter connected to the microscope
stage.


-----


56

###### 4.1.1 ###### Resist selection

All samples in this thesis were fabricated using a bilayer resist stack, consisting

of a thick ( __ 1 __ m), softer underlayer resist topped with a thinner ( __ 300 nm), harder
resist layer. The bilayer resist stack is used for several reasons. First, it is required to
create the freestanding bridge structures necessary to fabricate junctions using double-angle
evaporation (described in detail in section 4.2). Secondly, the bilayer resist stack allows for
the creation of undercut, where holes patterned in the developed resist are larger next to
the substrate than at the top of the resist stack; this aids in liftoby reducing the chance
that metal films will stick to the walls of the resist or form a continuous coat between the
substrate and the top surface of the resist stack.

The standard resists used to fabricate superconducting qubits in the past are

poly(methylmethacrylate) (PMMA) in anisole solvent as the top resist layer and methyl
methacrylate/methacrylic acid copolymer (MMA) in ethyl lactate solvent as the underlayer.
The resists and solvents are chosen so that the MMA is not soluble in the PMMA solvent
(anisole), which allows the PMMA to be spin-coated on top of the MMA layer without
disturbing or damaging it. PMMA and MMA are available in dierent concentrations, which
yield dierent final thicknesses after spinning. Detailed spin and bake recipes are given in
Appendix B. The PMMA/MMA resist stack is developed in a single step using a mixture
of isopropanol (IPA) and methyl isobutyl ketone (MIBK) in a ratio of 1:3 MIBK:IPA (other
groups have used other ratios, such as 1:7 MIBK:IPA, or even IPA/water mixtures [114]).
Because MMA is more sensitive to e-beam irradiation than PMMA, it is exposed at a lower
dose, so electrons scattered to the side (proximity dosing) during writing create a natural
undercut in the MMA underlayer. MMA is also more easily solved in the developer solution,
which further contributes to the undercut. With the ability to realize features smaller

than 50 nm, and sufficient undercut to perform double-angle evaporation, PMMA/MMA
is suitable for making a variety of superconducting devices such as qubits, resonators, and
paramps.

There are some drawbacks to the PMMA/MMA resist stack, however, which led us

to investigate alternatives. In some masks, more undercut is required than occurs naturally
in the MMA layer. Sometimes it is possible to achieve additional undercut by writing undercut boxes, low-dose features intended to expose the MMA layer without fully exposing
the PMMA above it. However, there are limitations to this method. In particular, if the
size of the feature in the top PMMA layer is relatively small (a small area qubit junction,
for example), the developer can only enter and leave through this small PMMA hole. If
one needs a large adjacent undercut area, it is often difficult to get enough developer flow
through the PMMA hole to remove all the MMA from the undercut region, and one ends up
with an improperly developed sample, as seen in Figure 4.2(a) and (b). The problem can be
solved by developing for a longer time, but unfortunately the PMMA will be overdeveloped
as a result, resulting in poorly defined features and potentially causing collapse of small
bridges.

The solution to the undercut conundrum is to use orthogonal resists, i.e. resists

where dierent developers are required for each of the two layers, and neither one is developed by the others developer. In this way, one can write a pattern in the top layer and
low-dose undercut boxes for the bottom layer, develop the top for a short time so it comes


-----


57


![SlichterThesis.pdf-75-1.png](SlichterThesis.pdf-75-1.png)

![SlichterThesis.pdf-75-0.png](SlichterThesis.pdf-75-0.png)

![SlichterThesis.pdf-75-2.png](SlichterThesis.pdf-75-2.png)

![SlichterThesis.pdf-75-4.png](SlichterThesis.pdf-75-4.png)

![SlichterThesis.pdf-75-5.png](SlichterThesis.pdf-75-5.png)

![SlichterThesis.pdf-75-3.png](SlichterThesis.pdf-75-3.png)

Figure 4.2: Resist mask troubleshooting.

Part (a) shows insufficient underlayer development due to small top layer features. This
problem is solved by using orthogonal resists and developing the underlayer for a longer
time. Part (b) gives an example of overdevelopment and resist pulling breaking resist
bridges. Both (a) and (b) are PMMA/PMGI bilayers. In part (c), the resist appears to
have a development or focus issue, but this is actually due to writing with coarse scan coils
(mag _<_ 1300x). The same mask is written under the same conditions in part (d), except
this time at a sufficiently high magnification, and shows much better feature resolution.
Part (e) shows a properly exposed mask with a double-angle evaporated junction. Note
the freestanding resist bridge and the undercut, described further in section 4.2. All the
masks in (a)-(e) were coated with a few nm of sputtered gold or evaporated aluminum after
development to improve contrast and reduce charging while imaging. Part (f) is a detailed
view of transmon qubit junctions after liftoand post-ashing. The two shifted shadows,
characteristic of double-angle evaporation, are clearly visible, the first one thin and the
second one thicker.

out nicely, and then let the sample sit in the developer for the bottom layer as long as it
needs to for the undercut to be fully developed. This technique was reported by Cord and
coworkers [115] using poly(methylglutarimide) (PMGI) as an underlayer and PMMA as the
top layer. We tried this combination initially for making flux qubit samples, but the desired
features did not come out reliably because the PMGI underlayer appeared to be too soft, or


-----


58

else too prone to swelling and/or contracting during development. Because the flux qubit
mask at the time involved tiny bridges ( __ 150 nm across) for junctions, and these bridges
were connected to freestanding islands 100 __ m long and 20 __ m wide (the qubit loops),
even very small fractional shifts due to expansion or contraction of the underlayer during
development could cause bridge breaking (see Figure 4.2). This resist pulling problem
might be solved by trying a dierent PMGI developer (we used CD-30, an aqueous alkaline
salt developer used for photoresists; others have used IPA/water developer [116]). However,
even without swelling eects, the surface tension of the water in the developer was large
enough to cause pulling on freestanding features during the post-development blow-dry
stage. PMGI is also more complicated in that it doesnt lift oin acetone like PMMA and
MMA do, but requires its own liftostep in heated n-methylpyrrolidone (NMP).

We then tried a second combination of orthogonal resists, returning to MMA as the

underlayer and using ZEP-520A resist as the orthogonal top layer. ZEP is a relatively new
high-resolution positive resist which uses anisole as a solvent (allowing it to be orthogonal to
MMA for spinning) but uses n-amyl acetate (xylene can also be used) as developer and is not
developed by 1:3 MIBK:IPA solution for low exposure doses (at higher doses this no longer
holds [117]). ZEP thus provides the desired orthogonality to an MMA underlayer; ZEP
also lifts oin acetone, making liftoagain a single-step process. The primary difficulty
with ZEP is that features with nearby undercut boxes are often distorted, because ZEP is
exposed with a lower dose than PMMA and so undercut boxes would overexpose the ZEP
layer. To solve this issue, we turned to cold development.

###### 4.1.2 ###### Cold development

Most groups working on superconducting qubits have used room-temperature de-

velopment for their lithography, and it has worked fine. However, it has been shown that
developing resists at lower temperatures can lead to improved resolution, allowing sub-10
nm features [118, 119, 120]. The theory for cold development is as follows. Electron-beam
resist is composed of long-chain linear polymers, which are cut into shorter pieces (chain
scission) by the electrons in the beam used to expose the resist. The shorter pieces dissolve
much more easily in the developer than the longer ones, and so areas where the resist has
been exposed to the beam are washed away [121]. However, longer uncut polymers can also
be dissolved into the developer, albeit at a considerably slower rate than the cut pieces,
allowing development to occur in areas where the resist has not been exposed. Since the
dissolving process is thermally activated, developing at lower temperature exponentially
reduces the rate at which unexposed resist is developed [122]. The contrast of the resist is
increased as a result, giving sharper edges and finer features, even for resists with initially
shorter polymer chains [123]. However, the dose must be correspondingly higher because the
developer can only remove shorter and shorter pieces of resist as the temperature goes down.
The higher doses also improve resolution by reducing dose variation due to shot noise in
the beam current [124]. As the dose continues to increase, however, the cut polymer pieces
start to reattach in a spiderweb or dendritic pattern, an eect known as cross-linking.
The cross-linked polymer pieces, owing to their complex shape, are very insoluble in the
developer and will not develop.

Since cross-linking ruins lithographic patterns, one cannot simply keep developing


-----


59

at lower and lower temperatures, and there is an optimal temperature where the benefits
of higher dose and reduced development thermal activation are balanced by the onset of
cross-linking. For PMMA developed in 1:3 MIBK:IPA, this optimal temperature is about
-15 __ C [120]. We designed a rig to develop resist at this temperature, which enabled us
to fabricate superconducting nanobridge junctions for use as magnetometers and amplifiers

[125, 59]. The system uses an immersion chiller to cool a bath of isopropanol in a Dewar
flask to the appropriate temperature; a magnetic stirring rod circulates the isopropanol and
keeps the temperature uniform. The beaker of developer is immersed in the isopropanol
bath and held in place by a special bracket.

For ZEP, cold development at the temperature of an ice water bath (1-2 __ C) is

sufficient for a substantial improvement in resolution and edge quality [126]. Importantly for
our processes, the cold development also pushes the ZEP dose sufficiently high that undercut
boxes written for the MMA underlayer (which is still developed at room temperature, using
an orthogonal developer) do not overexpose the ZEP top layer. The beaker of developer
simply sits in a holder in an ice water bath, which does not require temperature control.
With this arrangement, we perform a rapid cold develop of the ZEP layer, followed by a
room temperature MMA develop which can be made as long as necessary to achieve the
desired undercut.

#### 4.2 #### Thin-film deposition

After the resist mask has been developed, it is metallized to form the supercon-

ducting circuit structures. There are several standard methods for depositing metal films at
our disposal, thermal evaporation, e-beam evaporation, and sputtering. All three methods
are performed in vacuum. Thermal and e-beam evaporation both melt the material to be
deposited, which then evaporates and coats the substrate. In thermal evaporation, the material is held in a tungsten boat or coil which is heated by current flow until the material
inside melts. E-beam evaporation works by steering a beam of high-voltage electrons generated by thermionic emission into the target material, which is locally heated and melts. In
contrast with the melting-based evaporation techniques, sputtering involves hitting a target with high speed ions (often from an Ar plasma), physically ejecting atoms of the target
material, which settle on all surfaces in the chamber including the substrate. Sputtering
does not involve melting the target, which makes it suitable for depositing a broader variety
of materials than evaporation. Evaporation methods are directional, sending material in a
straight line from target to substrate, while sputtering is non-directional, creating a cloud
of target particles which settle on all surfaces, both horizontal and vertical.

The devices in this thesis are made of aluminum and niobium on intrinsic silicon

substrates. Aluminum can be deposited by any of the three techniques above, while niobium
must be sputtered because its melting point is too high for efficient evaporation deposition.
The junction fabrication techniques used in our samples require directional deposition, so
the junctions are made using evaporated aluminum. It is possible to make junctions using
only sputtering (allowing for the use of niobium junctions), but the process involves several
lithographic steps and will not be discussed in detail. We do use sputtered niobium for
ground planes for the paramp samples, as will be described in further detail in section


-----


60


ee -

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PMMA|||||||||||||
|MMA|||||||||||||
|Si substrate|||||||||||||



E-beam exposure

|Col1|O2|Col3|Col4|O2|Col6|
|---|---|---|---|---|---|
|PMMA||||||
|MMA||||||
|Si substrate||||||



Oxidation


|Al Al|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|PMMA||||||
|MMA||||||
|Si substrate||||||


1st angle evaporation

Josephson junction

![SlichterThesis.pdf-78-0.png](SlichterThesis.pdf-78-0.png)

Liftoff


|PMMA|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|MMA|||||
|Si substrate|||||


Development

|Al Al|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|PMMA|||||
|MMA|||||
|Si substrate|||||



2nd angle evaporation


Figure 4.3: Double-angle evaporation.

Using a bilayer resist, one can fabricate Al-AlOx-Al Josephson junctions by performing
double-angle evaporation, sometimes called the Dolan bridge technique. The layers are

labeled as PMMA, MMA, and Si substrate, but in general they could be any suitable
bilayer stack on a substrate. First, a bilayer resist stack is exposed using electron beam
lithography (top left) so that a thin bridge is left unexposed. The resist is then developed
chemically (top center), washing away the exposed top layer and underlayer and leaving a
freestanding bridge, seen here end-on. Note the scooped out undercut. Next, the sample
is placed in an evaporator and aluminum is deposited at an angle (top right), forming
two regions on the substrate disconnected from each other by the shadow of the bridge.
The sample is then exposed to an Ar/O 2 gas mixture, causing an oxide layer (yellow) to
grow on the deposited aluminum (bottom left). A second evaporation is performed at a
dierent angle (bottom center), such that the aluminum overlaps features on both sides of
the original bridge shadow. Finally, the resist is lifted o(bottom right), leaving behind
the circuit. The desired Josephson junction is formed by the Al-AlOx-Al tunnel barrier
between the two bridge shadows, while several spurious Josephson junctions are formed by
Al-AlOx-Al barriers elsewhere. As long as the areas (and thus the critical currents) of the
spurious junctions are much larger than that of the intended junction, they will not aect
the device behavior.

4.2.2.

Aluminum Josephson junctions are most simply made using the double-angle de-

position technique [127], detailed in Figure 4.3. This method requires a freestanding bridge
of top-layer resist separating two exposed areas with no resist. By evaporating aluminum
at an angle from the substrate normal and perpendicular to the length of the bridge, a


-----


61


![SlichterThesis.pdf-79-3.png](SlichterThesis.pdf-79-3.png)

![SlichterThesis.pdf-79-0.png](SlichterThesis.pdf-79-0.png)

![SlichterThesis.pdf-79-2.png](SlichterThesis.pdf-79-2.png)

Figure 4.4: SlichTECH e-beam evaporator and NRC thermal evaporator.

![SlichterThesis.pdf-79-1.png](SlichterThesis.pdf-79-1.png)

The SlichTECH evaporator is shown in part (a), with its vacuum chamber and electronic
control rack. Part (b) shows a detail view of the two-axis controllable sample stage with
the load lock open. The vacuum control panel and turbo pump controller are shown in
(c); the system can be controlled either manually or by computer. The old NRC thermal
evaporator is seen in (d), with all manual valves. The NRC evaporator is durable but has
inaccurate and often sticky angle control, angle-dependent thickness variations, and poorer
base pressure and cycle time due to its single-chamber design.

shifted shadow of aluminum is deposited on the substrate. One can then let a controlled
amount of O 2 gas (we use a mixture of Ar and O 2 ) into the vacuum chamber, which causes
a layer of aluminum oxide to form on the deposited aluminum. By controlling the exposure
time and O 2 pressure, one can control the thickness of the oxide and thus the transparency
of the tunnel junction to be formed. Finally, a second layer of aluminum is evaporated at
a dierent angle (often the negative of the first angle), in such a way that the deposited
film bridges the gap in the first aluminum layer formed by the bridge shadow. The bridge
shadow thus defines one edge of the junction in the bottom layer and the other edge of the
junction in the top layer, and the angles determine the amount of overlap between layers
(the junction area). Double angle evaporation can be used to make junctions of various
sizes ranging from 100 nm or less on a side up to about 4 __ m by 1 __ m. Junctions larger
than this are difficult to make because they require a very long freestanding bridge, which
is difficult to achieve reliably, and so are typically made using dierent methods.

As part of the fabrication work, we designed, built, and commissioned a new

evaporator system with angle control and oxidation capabilities to use for device fabrication.
The evaporator was christened the SlichTECH evaporator, in homage to Joe Aumentados
JoeTEK system which was the inspiration for the design. The SlichTECH is an e-beam
evaporation system with a load lock for fast sample cycling and improved base pressure,
precisely controllable oxidation pressure, two-axis angle control for the sample, and an Ar
ion mill for cleaning surfaces and removing native oxides. It was built to replace an old NRC


-----


62

thermal evaporation system, which had relatively poor base pressure, unreliable thickness
monitoring, and somewhat inaccurate angle and oxidation capabilities. Photos of the two
systems are shown in Figure 4.4. The SlichTECH allows improved sample throughput and
parameter control, and is automated for use with computer control.

###### 4.2.1 ###### Oxygen plasma cleaning

One of the great frustrations of junction fabrication is the tendency of junction

critical currents to decrease over time after fabrication (a phenomenon known as aging).
Some amount of junction aging is unavoidable, because the oxide barrier in the tunnel
junction has some ability to diuse, and because water and oxygen from room air can
migrate into the barrier and change its transparency. Good junctions will age by 10%

or less before reaching a steady state; oftentimes, though, junctions can age by 50-100%,
making qubit fabrication very difficult . In addition, we often observe substantial run-torun variation in junction critical currents where the fabrication, evaporation, and oxidation 1
parameters were nominally the same. Both this variation and excessive aging present major
headaches for getting good samples.

We tried several techniques to combat aging, such as performing controlled sample

post-oxidations in vacuum before venting the chamber and designing junctions where the
tunnel barrier is overlapped on three sides by aluminum to reduce exposure to air. These
methods all met with limited success. Aging can be improved somewhat by using junctions
with a lower critical current density (thicker tunnel barrier), but for many applications there
is not a great deal of freedom on this axis. However, we eventually determined that the best
method for controlling junction aging was to perform a brief (10-20 second) O 2 plasma clean
at low power ( __ 10 W at 100 kHz) after development and before evaporation. The theory is
that any remaining resist residue on the substrate which was not removed by the developer
may contribute to aging, and that the plasma cleaning removes this without damaging the
mask. The oxygen plasma is generated by a capacitively coupled parallel plate source, and
this means that the plasma etching is directional, preferentially etching vertically. Junctions
made with this pre-ash technique tend to show consistent aging of about 10% or less. In
addition, the run-to-run variation in critical currents is greatly reduced, suggesting that
resist residue on the substrate (and perhaps outgassing from that resist) was a cause of
absolute variability as well as excessive aging. Recent work in other groups agrees with the
hypothesis of leftover resist residue and our observation that pre-ashing improves junction
aging and variability [129, 130].

We can also perform oxygen plasma cleaning after the liftostep, dubbed post-

ashing. This cleans the substrate surface of any remaining resist residue not removed

chemically, which may be a source of loss in qubits and resonators. Post-ashing also has
been successful at removing the black veil of death [64], theorized to be an aluminum or
aluminum oxide film that collapses from the resist sidewalls onto the device and may be
a source of dielectric loss. Before and after pictures of post-ashed samples are shown in
Figure 4.5. There has been anectodal evidence from our lab that both pre- and post-ashing

1 Flux qubits are particularly sensitive to aging, as the frequency of a three-junction flux qubit depends

exponentially on the critical current of the small qubit junction [128].


-----


63


![SlichterThesis.pdf-81-0.png](SlichterThesis.pdf-81-0.png)

![SlichterThesis.pdf-81-1.png](SlichterThesis.pdf-81-1.png)

![SlichterThesis.pdf-81-3.png](SlichterThesis.pdf-81-3.png)

![SlichterThesis.pdf-81-2.png](SlichterThesis.pdf-81-2.png)

Figure 4.5: O 2 plasma cleaning to remove the black veil of death.

Our 100 kHz parallel plate O 2 plasma ashing system (a) is used for pre- and post-ashing
of samples. Many samples show pieces of black film after lifto, nicknamed the black veil
of death by the Yale group. Part (b) shows black veil of death lying on the fingers of a
transmon capacitor. The film may be a source of dielectric loss and decoherence in qubits
and resonators. A brief oxygen plasma cleaning appears to remove the black veil of death
without aecting the critical currents of junctions on the sample, as seen in the before (c)
and after (d) pictures of transmon junctions.

improve the internal _Q_ of resonators, which should correlate with improved qubit coherence
times. We have not yet done systematic tests with qubits to study this eect, but anecdotal
evidence from our group suggests that post-ashing can improve _T_ 1 and _T_ 2 noticeably in
transmon qubits.

###### 4.2.2 ###### Ground plane fabrication

The paramps require large capacitance (several pF), which we realize using two

parallel plate capacitors in series. Each capacitor consists of an evaporated aluminum top
plate, a sputtered niobium bottom plate, and a thin-film silicon nitride (SiN _x_ ) dielectric in
between. The two capacitors share a common niobium bottom plate, which we refer to as
a ground plane 2 , thus forming two capacitors in series. This design eliminates the need for
vias through the dielectric layer and simplifies fabrication.

The niobium ground planes are fabricated by electron beam lithography and sput-

tering in a liftoprocess. The e-beam lithography is done in a standard PMMA/MMA
bilayer, which gives a substantial natural undercut. When sputtered, this resist profile

gives rise to a slow, smooth slope at the edge of the ground plane, rising from the surface
of the substrate to the __ 250 nm thickness of the ground plane over about 3-5 __ m. This
gentle shoulder is important to ensure continuity of the silicon nitride and aluminum

2 This capacitor style was initially used in the original JBA designs at Yale [108], and the terminology

comes from the fact that under dierential excitation of the resonator, the niobium bottom plate is a virtual
ground.


-----


64

![SlichterThesis.pdf-82-0.png](SlichterThesis.pdf-82-0.png)

10 3 10 4 10 5 10 6 10 7 10 8

Cavity photon occupation (photons)


10 -3


10 -4


Figure 4.6: Measured loss tangent of microlab SiN _x_ .

Loss tangent of microlab-grown silicon nitride capacitor dielectric extracted from resonator
data. The loss tangent decreases with increasing power, consistent with loss from two-level
systems [131]. At very high powers, the loss tangent starts to increase again, perhaps from
higher order eects such as local heating or quasiparticle generation.

layers deposited on top, preventing shorts to ground through the nitride and open circuit
breaks in the aluminum. Too thick a layer of niobium or too high a dose on the resist mask
can cause niobium to climb the resist sidewalls or connect over the top of the resist, ruining
the needed shoulder and making liftodifficult.

After the niobium ground planes have been fabricated, they are coated with SiN _x_

by plasma enhanced chemical vapor deposition (PECVD). We use the oxford2 machine in
the UC Berkeley Microlab (now the Nanolab) to deposit a SiN _x_ layer between 120 and
180 nm thick with a relative dielectric constant of about 6.75. Thinner layers may not
provide full coverage to prevent shorts, while thicker layers may give rise to too much stray
inductance in the capacitor. We use SiN _x_ because its loss properties are superior to SiO 2

[132]. Nitride recipe details are provided in Appendix B.

The large capacitors made using these ground planes have fairly mediocre loss


properties due to defects in the SiN _x_ dielectric. We made some linear resonators to test the
loss tangent tan __ of the nitride as a function of power. The results are shown in Figure 4.6.
At low power tan __ __ 10 __ 3 , improving to tan __ __ 10 __ 4 as the excitation power increases.
This power dependence is expected if the loss is due to two-level defects in the dielectric

[131]. The substantial loss tangent means that we cant use the parallel plate capacitors as
part of a qubit, but they are suitable for use in paramps, which have a very low external _Q_
and operate at higher power. The Maryland group have reported low power loss tangents
of 2 _._ 5 __ 10 __ 5 in high stress nitride [133], more than an order of magnitude better than ours.

Recently, our group has developed a method for making ground planes with a

single-crystal silicon dielectric using silicon-on-insulator (SOI) wafers. The loss tangent of
these SOI caps is about 5 __ 10 __ 6 at single photon powers [134], making them suitable not


-----


65

just for paramps but also perhaps for qubits. We are currently working to develop transmon
and phase qubits using SOI cap shunting capacitances in the hopes of improving coherence
times.

#### 4.3 #### Sample design and parameters

The design process for qubit/cavity and paramp samples involves extensive com-

puter simulation. The primary tool in our arsenal is AWRs Microwave Office (MWO),
which provides a suite of capabilities for simulating the behavior of microwave circuits. Every design starts with layout of capacitor and inductor designs for cavity and qubit, which
we simulate using Microwave Offices AXIEM electromagnetic (E-M) simulator. AXIEM
does not require a conducting bounding box, giving more freedom in the circuit design for
simulation, and runs considerably faster than the other MWO E-M solvers. AXIEM does
a good job of capturing unexpected features such as spurious resonances, so its good to
simulate as much of the circuit as possible to catch potential issues. For most designs, one
can efficiently simulate the entire qubit/cavity circuit with input/output coupling and surrounding launch structures and get accurate values for the external quality factor _Q_ ext and
resonant frequency _!_ cav . To estimate the qubit-cavity coupling _g_ , a SPICE extraction can
be performed to extract the cavity capacitance (usually accurate to about 10%). Once a
MWO design has the desired parameters, it can be exported directly into NPGS for lithography. Fast flux line couplings are usually estimated using FastHenry, an older, standalone
program which gives estimates of mutual inductances.

###### 4.3.1 ###### Transmons

The energy structure of a transmon qubit is determined by the critical current of its

Josephson junctions and the capacitance shunting them, as described in section 2.1.3. Using
AXIEM, we are able to get a reasonable estimate for the shunting capacitance for a given
design. We can then determine the junction critical current for a desired qubit frequency
using Mathematica. Room temperature resistance measurements on co-fabricated witness
junctions give us an estimate of the critical current of fabricated qubit junctions using the
Ambegoakar-Baratorelations [72]



__ ( _T_ )
_I_ 0 =

2 _eR_ _n_


( _T_ )

2 _k_ _B_ _T_





__ ( _T_ )
_I_ 0 =


tanh


2 _k_ _B_ _T_


(4.1)


where _I_ 0 is the critical current, ( _T_ ) is the temperature-dependent superconducting gap,
_R_ _n_ is the normal-state junction resistance, _T_ is the temperature, and _e_ is the elementary
charge. The room-temperature junction resistance is a close approximation to _R_ _n_ . Since we
operate at 20-50 mK, _T_ __ _T_ _c_ (the superconducting transition temperature) and therefore
( _T_ ) (0) and the tanh term 1. Substituting these into (4.1) gives _I_ 0 __ (0) _/_ 2 _eR_ _n_
__ __ __
For aluminum, (0) = 170 meV.


Table 4.1 gives a listing of the transmon samples used in the quantum jump ex-

periments. The values of _E_ _J_ , _E_ _C_ , and coherence times are all quoted at a single operating
point which optimizes coherence while still allowing single-shot readout. All of the samples
have _E_ _J_ _/E_ _C_ 1 and so are well in the transmon regime.
__


-----


66

![SlichterThesis.pdf-84-0.png](SlichterThesis.pdf-84-0.png)

Figure 4.7: Transmon samples.

Optical images of three transmon samples and readout cavities. Panel (a) shows a reflection
geometry cavity with capacitive coupling to the microwave feedlines, while panels (b) and
(c) are transmission geometry cavities with inductive feedline coupling. The cavities and
transmons in (b) and (c) have wider traces and greater spacing between traces compared to
(a), which is intended to help reduce capacitive losses. The sample in (c) also has a weakly
coupled fast flux line, used for the experiments described in Chapter 8. The inset shows a
detail view of the fast flux line and the qubit loop.

Figure 4.7 shows optical images of several dierent designs for the transmon and

its readout cavity, corresponding to the three samples listed in Table 4.1. The first sample,
TF051310b, is the initial sample in which quantum jumps were observed and is pictured in
part (a). It uses a capacitively coupled cavity in reflection geometry. To improve coherence
times, we modified the design to have wider traces and larger gaps between traces, a technique we adopted from the Devoret group at Yale. The newer cavities, pictured in (b) and
(c), operate in transmission and are inductively coupled to the microwave feedlines (rather
than capacitively coupled). Spurious cross-coupling between the input and output feedlines
gives the cavity resonance a Fano lineshape in this design, but this does not degrade per-

|Sample name|E (GHz) E (MHz) T (s) T (s) J C 1 2|Sample design|
|---|---|---|
|TF051310b TF021111d TF042811b|11.4 280 0.29 0.4 14.0 231 1.27 0.4 15.0 235 0.91 1.35|Fig. 4.7(a) Fig. 4.7(b) Fig. 4.7(c)|



Table 4.1: List of transmon samples.

This table gives parameters for all the samples used in quantum jump experiments. All
values are quoted at the best measured qubit operating point.


-----


67

![SlichterThesis.pdf-85-0.png](SlichterThesis.pdf-85-0.png)

Figure 4.8: Paramp sample.

Panels (a) and (b) are optical micrographs of a typical paramp sample, showing the two large
parallel plate capacitors formed by the Al top plate and Nb ground plane with intervening
SiN _x_ dielectric, as well as the small SQUID loop. The slow sloping apron at the edge
of the Nb ground plane can be seen in (b) as the few- __ m-wide purple region to the right
of the dark line. This slow slope allows the SiN _x_ and Al to transition onto the ground
plane without breaking. The SQUID loop and junctions are shown in greater detail in the
scanning electron micrograph in (c).

formance. For the samples used to study measurement backaction in Chapter 8, we added
a weakly-coupled fast flux line as seen in (c).

###### 4.3.2 ###### Paramps


Paramp design is also relatively straightforward. The paramp has _Q_ __ 20 to

give large bandwidth, which in turn sets the capacitance through the relationship _Q_ =
_!Z_ 0 _C_ , where _!_ is the resonant frequency and _Z_ 0 is the microwave impedance of the launch
(typically 100 for the dierential launch used in our experiments and described in section
5.1). The capacitance can be estimated using the standard parallel plate formula _C_ =

_A_ 0 __ _r_ _/d_ , where _A_ is the area of the capacitor plate, _d_ is the dielectric thickness (measured
in the Nanolab using interferometry), __ 0 is the permittivity of free space, and __ _r_ is the relative
permittivity of the dielectric (experimentally, 6.75 for our SiN _x_ ). Once the capacitance has
been determined, the resonant frequency is then set by the Josephson inductance of the
SQUID junctions _L_ _J_ =  0 _/_ 2 _I_ _c_ , where _I_ _c_ is the flux-dependent SQUID critical current.
For a typical paramp sample, _C_ 6 pF and _I_ _c_ ( = 0) 4 __ A.
__ __


-----


68

## Chapter 5

# Experimental apparatus

All the experiments in this thesis were carried out in a VeriCold dry dilution

refrigerator with a base temperature of 30 - 50 mK. These low temperatures are required
so that the thermal energy _k_ _B_ _T_ is well below the qubit energy splitting ~ _!_ _q_ and the energy
of the readout photons ~ _!_ ro . We use a variety of microwave components, both inside and
outside the fridge, to manipulate our qubit and readout signals. The VeriCold fridge has
five temperature stages, each with a large gold-plated copper plate with tapped holes for
mounting components and experimental samples. The two warmest temperature stages are
nominally at 70 K and 4 K 1 and are cooled by a two-stage pulse tube refrigerator. The
next three stages are the still, a plate between the continuous and discrete heat exchangers,
and the mixing chamber. The base temperature of the fridge on delivery was around 11
mK, but due to changes in the mix balance and the heat load of the fridge wiring, the base
temperature for these experiments is somewhat higher.

#### 5.1 #### Sample boxes and launches

We use our own customized microwave launches to connect the paramp and qubit

samples to the microwave cabling in the fridge. For the paramps (and initially the qubit/cavity
samples as well), we use a modified 6 GHz microstrip 180 __ rat-race hybrid [135] to convert
single-ended microwave signals on the lines into dierential excitations at the sample. The
circuit design, christened the Bollywood launch because of a resemblance to a Bollywood
dancer, is detailed in Michael Hatridges Ph.D. thesis [136]. Because of its dierential output, the Bollywood presents a 100 impedance (rather than 50 ) to the sample, which
helps with the simultaneous optimization of paramp dynamic range and stability. The initial
quantum jump experiments were performed with a Bollywood launch for the qubit/cavity
sample as well. However, the Bollywood is unshielded, and we discovered that the qubits
on the Bollywood launch suered from spurious radiative coupling as a result.

For subsequent qubit experiments, we used two dierent styles of enclosed sample

boxes. The first style (A) uses edge-launch connectors (Southwest Microwave 292-04A-5)

1 The original pulse tube began to fail around the time of the initial quantum jump experiments, and

these stages had temperatures closer to 85 K and 6 K respectively. A retrofit with a new pulse tube has
since brought the temperatures back down to 55 K and 4 K.


-----


69


![SlichterThesis.pdf-87-0.png](SlichterThesis.pdf-87-0.png)

![SlichterThesis.pdf-87-1.png](SlichterThesis.pdf-87-1.png)

![SlichterThesis.pdf-87-3.png](SlichterThesis.pdf-87-3.png)

![SlichterThesis.pdf-87-2.png](SlichterThesis.pdf-87-2.png)

Figure 5.1: Sample boxes and launches.

Panel (a) shows Bollywood launches with samples and flux bias coils. Panel (b) shows a
type A box with Southwest Microwave connectors and a bias coil. The newer type B
box with bulkhead connectors and a third port for a fast flux line is seen in panels (c) and
(d), with the latter showing the box closed and with a flux bias coil underneath.

on a microwave circuit board and has a clamshell-like lid which can be screwed down on top
to enclose the sample. This provides considerably more shielding than the open Bollywood,
but the lid does not make tight contact on all surfaces of the edge-launch connectors and
so some stray radiation could still enter. The second style of enclosed sample box (B)
is a milled-out copper block with a flat lid which makes a very good flush seal (this seal
can be augmented with indium wire or foil if desired). The microwave circuit board inside
is held down by screws, and signals are launched by SMA bulkhead connectors designed
for this application (AEP/Radiall 9308-9113-001). Both styles A and B use circuit boards
with grounded CPW microwave traces and vias connecting the top and bottom grounds; a
recessed square was milled partway through the board to accommodate the sample chips
flush with the board surface. Versions of the style B sample box and board were also made
with an additional SMA connector for launching fast flux signals, as used in the experiments
in Chapter 8. Photographs of Bollywood, A-style, and B-style launches are shown in
Figure 5.1.

The qubit and paramp samples boxes and launches are placed inside fully enclosed

superconducting aluminum shields, with dc wires, coaxial cables, and thermalization straps


-----


70

penetrating the shield through long, narrow holes. This design helps shield environmental
noise and reduces trapped flux in the devices by shielding static magnetic fields. Each superconducting shield is surrounded by a Cryoperm can to keep the shield itself from trapping
magnetic flux as it cools through _T_ _c_ . We also place a three-layer mu-metal shield around
the outside of the dilution fridge during cooldown and operation to reduce external static
and low-frequency magnetic fields at the samples. With this shielding, the primary source
of static magnetic fields at the samples is from the permanent magnets in the microwave circulators at base temperature; we try to keep the circulators far from the samples to reduce
flux trapping. We also discovered that the superconducting shield boxes mediate spurious
radiative coupling between samples inside them, especially those on Bollywood launches.
To combat this eect, we put the paramps (which are biased with strong microwave tones)
in a separate superconducting shield from the qubit samples, and use enclosed qubit sample
boxes as described above.

#### 5.2 #### Fridge wiring

The experiments in this thesis require extensive electrical wiring and components

inside the dilution refrigerator. Microwave-frequency signals are sent over coaxial lines,

while low-frequency signals (e.g. for flux biasing) are sent via filtered twisted pairs. We
use a number of microwave switches on the base stage, allowing us to try various dierent
experiments in a single cooldown without the increased heat load and decreased space that
come with adding more microwave lines. We have also implemented a setup for calibrating
amplifier noise performance. Complete schematics of the fridge wiring can be found in

Appendix C.

###### 5.2.1 ###### Low-frequency wiring

The fridge has two sets of 16 filtered low-frequency lines, one set for low-current

applications with manganin wires and another set for high-current applications with Cu
wires from room temperature to 4 K and superconducting CuNi-clad NbTi wires from 4
K to base temperature. In this thesis, these low-frequency lines are used to establish a dc
magnetic flux bias in the paramp SQUID loop or the qubit loop, and to operate the hot-cold
load switch described in section 5.2.4.

Both the manganin and the Cu/superconducting lines are well shielded and are


filtered in several stages. All signals pass through a series of LC __ filters (with __ 1 MHz
cutofrequency) at room temperature, enter the fridge through a hermetic LEMO connector, and continue to further LC filters at 4 K; the signals are carried on twisted-pair
looms (Oxford Instruments A8-311, A8-312, A8-313) inside a flexible stainless steel bellows
for shielding. Below the 4 K filter, the wires are broken out into eight channels, each with
two twisted pairs. Each channels wires are carried inside a separate braided shield with
four-pin Reichenbach connectors. Each twisted pair passes through three further stages
of Cu powder filters [7] at 700 mK, 100 mK, and 30 mK. The Cu powder filters remove
high-frequency noise from __ MHz to __ THz.

We use o-chip superconducting coils made of CuNi- or Cu-clad NbTi wire wound


-----


71


70 K

4 K

![SlichterThesis.pdf-89-2.png](SlichterThesis.pdf-89-2.png)

700 mK (c)

100 mK

30 mK

![SlichterThesis.pdf-89-1.png](SlichterThesis.pdf-89-1.png)

![SlichterThesis.pdf-89-0.png](SlichterThesis.pdf-89-0.png)

Figure 5.2: VeriCold dilution refrigerator and sample boxes.

Panel (a) is a photograph of the VeriCold fridge, fully wired, with each of the stages labeled
by its temperature during operation. The bottom plate is about 25 cm in diameter, ample
room for multiple experiments. Panel (b) shows several B-style sample boxes mounted to
a copper cold finger and connected to captive microwave cables through an aluminum lid.
This assembly slides into an aluminum box which screws to the lid to create a continuous
superconducting shield. A Cryoperm shield is then placed around the entire assembly to
minimize flux trapping. The assembled shielded box can be seen at left in part (c), with
the captive microwave cables connected to the microwave switches visible at right.

on Cu bobbins (see figure 5.1) to provide dc flux bias for the paramp and qubit. The coils
have 240 turns, and can operate at currents up to __ 15 mA before the mixing chamber plate
starts to heat up due to dissipation in the contact resistance of the Reichenbach connectors.
The current per flux quantum varies depending on the size of the loop and the sample-coil
distance, but generally runs between 5 and 50 mA/ 0 . This is a relatively weak coupling,
the lines are well-filtered, and the superconducting coil acts as a giant LC filter, so generally
one does not have to be too concerned about flux noise arising from current noise in the
coil. However, the paramp is also a very sensitive magnetometer, so it is still important
to be careful, as we discovered on one occasion. When biasing a paramp into the gain


-----


72

![SlichterThesis.pdf-90-0.png](SlichterThesis.pdf-90-0.png)

-200 -150 -100 -50 0 50 100 150 200

Detuning from paramp pump (kHz)

Figure 5.3: Flux bias noise from a Keithley sourcemeter.


-30

-40

-50

-60

-70

-80

-90


These traces show the output frequency spectrum of a paramp biased in the high-gain
regime using a Keithley 2400 sourcemeter to generate the current in the flux bias coil. Note
many spectral noise components and how they decrease as the Keithleys output range is
increased. With a low pass filter ( _f_ 3dB = 0 _._ 7 Hz) on the Keithley output (black trace), the
noise is totally removed (green trace shows same range without filter).

regime, we saw unexpected jumping on the output trace. After extensive debugging, we
determined that the jumping was due to the paramp amplifying noise from the Keithley
2400 sourcemeter used to establish the dc flux bias. The paramp was acting as a noise
sensor, detecting many sharp harmonics in the spectrum of the Keithley output, as shown
in Figure 5.3. We found that changing ranges on the Keithley (while outputting the same
current) changed the noise output, and we finally solved the problem by putting a big RC
lowpass filter with _f_ 3dB = 0 _._ 7 Hz on the Keithleys output. The lesson is to filter all dc
signals carefully, even for microwave circuits.

###### 5.2.2 ###### Microwave wiring and switches

The experiments in this thesis are carried out at millikelvin temperatures and

microwave frequencies. This combination presents a challenge, because the high bandwidth
coaxial lines needed for the microwave signals also admit thermal noise over a very broad
band. Black body radiation from 300 K and 4 K have substantial spectral weight in the
microwave regime which must be eliminated before they reach the qubit. Stray black

body radiation can cause loss and decoherence in superconducting qubits and resonators

[137, 138]. To remove black body radiation from input signals and thermalize them to the
base temperature, the coaxial input lines are attenuated in several stages with broadband
NiCr attenuators (XMA 2782-6051-10, -20). The attenuation values for each temperature
stage are chosen to reduce input black body radiation from the next higher stage to a level


-----


73

below that of the current stage. Attenuation, like gain, is typically expressed in logarithmic
dB units in microwave circuits, with the conversion between linear and dB units given by
_A_ dB = 10 log 10 _A_ linear . In addition to the attenuators, we include low-pass and high-pass
reactive filters on microwave injection lines to prevent undesired out-of-band noise from
reaching our devices. Above the 10-20 GHz range, though, these filters no longer function
eectively and the attenuators and intrinsic loss of the coaxial cables must do the job alone.
Fortunately, it appears that these are sufficient to thermalize microwave input lines [137].

Its also important to consider the heat load from microwave cables. Unlike low-

frequency wires, which can be made very thin to reduce their thermal conductivity, coaxial
cables must be of a certain size and geometry. As a result, the thermal conductivity needs
to be reduced by an appropriate choice of materials [139]. The coaxial cables between

stages (Micro-Coax UT-085B-SS, Coax Co. SC-219/50-SS-SS, SC-219/50-CN-CN, and SC219/50-SCN-CN) are made of stainless steel, beryllium-copper alloy, or copper-nickel alloy,
which have low thermal conductivity. The tradeofor this reduced thermal conductivity
is reduced electrical conductivity and therefore increased cable loss for signals. This is not
problematic on injection lines, which are already heavily attenuated, but can be frustrating
on output lines carrying weak signals from an experiment to the amplifiers. For cables
between points on the same temperature stage thermal conductivity is not an issue, and we
use tin-plated copper cables (Micro-Coax UT-085-TP) to minimize loss.

We use a cryogenic high electron mobility transistor (HEMT) amplifier (Low Noise

Factory LNF-LNC4 8A) as our initial amplification stage (not counting the paramp). The
HEMT amplifier operates over the 4-8 GHz band with a noise temperature of 2.6 K, equivalent to 9 photons of added noise at 6 GHz. This is currently the lowest noise commercially
available amplifier in this frequency range. The HEMT is anchored to the 4 K plate of the
fridge; unfortunately, it cannot be run at a colder stage due to its power dissipation of 4
mW. Because of this constraint on the HEMTs location, cable losses between the experiment and the HEMT (about 7 dB) significantly degrade the system noise temperature. We

2
eliminated this problem by using superconducting Nb coaxial cables (Coax Co. SC-219/50Nb-Nb), which have very low loss and very low thermal conductivity , to bring signals from
the mixing chamber stage to the HEMT on the 4 K plate.

Our experiments rely on the ability to control the direction of propagation of

microwave signals. For this, we use cryogenic 3-port circulators (Pamtech CTH1368K18).
Circulators are passive devices which direct incident microwaves to a specific output port
while preventing them from reaching any other ports. In a 3-port circulator, incoming

signals are directed to output ports in the pattern 1 _!_ 2 _,_ 2 _!_ 3 _,_ 3 _!_ 1, while propagation
does not occur in the reverse directions 1 _6!_ 3 _,_ 3 _6!_ 2 _,_ 2 _6!_ 1. We can use this to separate the
input and output signals from a reflection measurement, for example: signals enter at port 1,
are directed out port 2, interact with the device under test (a paramp or resonator), reflect

2 The Weidemann-Franz law, which states that the electrical conductivity and thermal conductivity are

directly proportional to each other, holds for most materials at temperatures below __ 10K. This is because
electronic thermal conductivity is dominant over lattice thermal conductivity at these temperatures. In

superconductors, the Cooper pairs have zero entropy and cannot carry heat, so only unpaired electrons can
be involved in heat transport. The number of unpaired electrons decreases exponentially with temperature
below _T_ _c_ , so at temperatures well below _T_ _c_ superconductors are simultaneously good thermal insulators and
excellent electrical conductors.


-----


74

back into port 2, and are directed out port 3. One can also make an isolator, essentially
a microwave one-way valve, by terminating one port of the circulator with a matched 50
load. Isolators allow signals out of a sensitive qubit experiment while protecting it from
noise or signals which might propagate back down the output lines and cause undesired
eects.

As is often the case, the experimental realization of a circulator cannot quite

match its Platonic ideal. Real circulators have finite reverse isolation (the ratio of signal
which propagates in the allowed versus the forbidden direction), in our case about 20 dB.
To get larger isolations, we use must use several circulators in series. Each circulator

also has an insertion loss of about 0.5 dB, so we pay for the isolation they provide with
decreased signal. In addition, real circulators have a finite bandwidth, usually an octave for
commercial devices. For the experiments in this thesis, the circulators operate in the 4-8
GHz band. Outside of this band, the circulators are reflective. The Pamtech circulators are
unique in that they operate well at low temperatures; in fact, their bandwidth, isolation, and
return loss are worse at room temperature than at cryogenic temperatures. Since Pamtech is
currently the only source of cryo-compatible circulators, non-Pamtech circulators should not
be used at low temperatures because they may not function properly. Because circulators
employ permanent magnets to break time reversal symmetry (thus allowing non-reciprocal
behavior), one should take care in placing them to minimize the eect of their magnetic
fields on qubit and paramp samples.

In addition to circulators, we can also achieve directionalityat the expense of

attenuationwith directional couplers, which weakly cross-couple signals between two lines
with a preferred direction of propagation for the coupled signals. As with circulators, the
directionality is not perfect, and the directivity (ratio of preferred versus opposite direction
propagation) is finite, usually about 30 dB. In addition, only a small fraction of the original
signal gets coupled to the new line, giving an eective attenuation of typically 10 or 20 dB.
However, because of their small size, broad bandwidth, and because they dont generate
magnetic fields, directional couplers (Krytar 104020020 and similar) find many uses in our
experiments, primarily for coupling in paramp pump tones.

We can multiplex several samples on a single input and output line using microwave

switches and/or splitters at base temperature. The exact configuration of switches and
splitters depends on the number of samples in the cooldown and whether they are measured
in transmission or reflection. For a setup with all reflection samples, a single switch can
be used for multiplexing. We use latching 3-pole and 6-pole single-throw switches (Radiall
R573423300 and R573423600), which are slightly modified from their stock configuration to
allow reliable operation at cryogenic temperatures. For samples in transmission, we need to
multiplex both the input signal and the output signal. We accomplish this either by using
one switch on the input and one on the output, or by using a four-way splitter (Anaren
44020) on the input. The isolation between switch channels is about 80 dB and the on-o
ratio is better than 90 dB, so there is no issue with crosstalk from other samples coming
through on the output. In addition, we use a latching DPDT transfer switch (Radiall

R577433000) on the output line to switch the paramp and some of its attendant circulators
into or out of the amplification chain. This method gives us improved noise temperature
when we cant or dont want to use the paramp, and lets us control for the eects of the


-----


75


![SlichterThesis.pdf-93-1.png](SlichterThesis.pdf-93-1.png)

![SlichterThesis.pdf-93-2.png](SlichterThesis.pdf-93-2.png)

![SlichterThesis.pdf-93-0.png](SlichterThesis.pdf-93-0.png)

Figure 5.4: Circulators and microwave switches.

Several cryogenic 3-port circulators can be seen in (a), attached to a copper cold finger
to ensure thermalization. Part (b) shows a cryo-compatible fast GaAs microwave switch
(Hittite) on a circuit board. Three latching microwave switches (Radiall) attached to a
copper cold finger are shown in panel (c). The large bundle of red, green, and blue wires
carries control pulses from a superconducting loom to the switches.

paramp on the readout trace without having to temperature-cycle the fridge. The Radiall
switches are shown mounted to the fridge in Figure 5.4(c).

Each switching operation of these Radiall switches dissipates a small amount of

heat, warming the mixing chamber stage by a few tens of mK, but the fridge recovers fully
to base temperature within around 10-15 minutes. Care must be taken to make a highthermal-conductivity connection between the copper finger inside superconducting sample
shields and the mixing chamber plate, or else the copper finger may take considerably
longer to re-equilibrate after a switch is thrown. Since the switches are latching, and we
only seldom operate them (usually they remain in a fixed configuration for days or weeks
at a time), this brief heating does not aect the behavior of the samples.

For some purposes, such as the hot-cold load measurement mentioned in Section

5.2.4 and the filter thermalization measurements in Section 5.2.3 and Appendix A, we need
a microwave switch that can be switched back and forth at kHz or higher frequencies, much
faster than the mechanical Radiall switches can operate. For this we use solid state GaAs
switches from Hittite Microwave (HMC 547 and HMC 194). These Hittite switches dissipate
as little as 10 __ W when in use and have nominal switching times of 5-25 ns. The switching


-----


76

rate is limited in our experiment by the bandwidth of the filtered manganin low-frequency
lines used for the control signals, but this could be easily addressed if faster switching was
required. The main drawback of the Hittite switches is their insertion loss, which is around
2-3 dB at low temperature, so we only use them when the Radiall switches wont do. Figure
5.4(b) shows a Hittite switch on a microwave board mounted to the mixing chamber plate.

###### 5.2.3 ###### Microwave roach motel filters

The standard combination of attenuators and reactive filters used to thermalize

injection lines and reject out-of-band signals (as described in the previous section) works
well for most applications. However, there are some drawbacks which create a need for a new
type of filter. First, it is impossible to pass substantial dc currents (more than a few tens
of __ A) through a microwave injection line at base temperature given the large attenuation
values needed for thermalization. This is an issue for fast flux bias lines, which require the
high bandwidth of a coaxial line but must be able to pass __ mA of current. One can replace
the attenuators with low-pass filters, allowing dc current to pass through while removing
the higher-frequency black body radiation propagating down the line. The problem here
is that all reactive low-pass filters are re-entrantwith stopband attenuation decreasing
to near zero at sufficiently high frequency (usually 20-40 GHz)and will allow most black
body radiation through [140]. Furthermore, reactive filters are reflective in their stopband,
so out-of-band photons are not dissipated (as in an attenuator) but rather bounce around
in the lines, perhaps finding another route into the experiment. This reflective behavior
arises because the impedance of reactive filters is very far from 50 in their stopband; this
presents yet another problem, because the qubit doesnt see a well-controlled impedance
looking out into the fast flux line.

What we need for fast flux lines is a low-pass filter with low loss at dc and a

stopband extending to hundreds of GHz/THz frequencies. The filter should present a

matched 50 impedance in both passband and stopband, and should thermalize down
to mK temperatures. We developed a suitable filter, which we christened the microwave
roach motel or roach filter 3 . The roach filter is simply a stretch of lossy transmission line,
an idea which has been around for quite some time [141, 142]. Lossy, impedance-matched
transmission line filters for qubit experiments have been developed before [143, 144, 145],
but these filters are fragile, difficult to fabricate, and/or have too low a corner frequency.
The roach filter is a simple stripline [135, 146] with a magnetically loaded silicone dielectric
(Emerson & Cuming Eccosorb MFS-117) inside a connectorized copper box, shown in Figure
5.5(a). The design is based on one originally used at Yale [108, 147], and was independently
developed and published by Dan Santavicca and Dan Prober at Yale [148]. Roach filters
are simple and quick to build and their electrical properties are robust to minor fabrication
variations. By varying the length of the lossy stripline, one can change the filter cuto
frequency _f_ 3dB between a few hundred MHz and about 1.5 GHz. It should be possible to
make higher cutofrequencies through careful engineering of the copper box and perhaps
by using dierent types of Eccosorb.

3 The name derives from the impedance matching in the filters stopband, which means stopband signals

are admitted to the filter and dissipated inside rather than being reflected. This is analogous to the roach
motel style of cockroach trap, where the roaches check in, but they dont check out.


-----


77



-5

-10

-15

-20

-25

|VLFX-1350 1.3 GHz roach|Col2|
|---|---|
|||


![SlichterThesis.pdf-95-0.png](SlichterThesis.pdf-95-0.png)

![SlichterThesis.pdf-95-1.png](SlichterThesis.pdf-95-1.png)

10 20 30 40

Frequency (GHz)


10 20 30 40


10 20 30 40

Frequency (GHz)


![SlichterThesis.pdf-95-2.png](SlichterThesis.pdf-95-2.png)

Figure 5.5: Microwave roach motel filters.

Part (a) shows a roach filter with _f_ 3dB = 1 _._ 3 GHz. The copper strip center conductor is
sandwiched between two pieces of Eccosorb (the top piece has been removed here) and then
a lid is screwed on. The two graphs show a comparison of filter attenuation (b) and reflection
(c) between a 1.3 GHz roach and a Mini-circuits VLFX-1350 reactive filter. The VLFX has
a steeper stopband transition, but its attenuation wanes with increasing frequency to be
only 10 dB at 40 GHz. By contrast, the roach filters attenuation is at the network analyzers
noise floor at all frequencies above 20 GHz. In the stopband, the VLFX is very reflective,
but the roach filter maintains its impedance match, with less than 10 dB reflection below
10 GHz and less than 6 dB reflection at 40 GHz.

The insertion loss of the roach filters reaches the noise floor of network analyzer

measurements at around 15-20 GHz and remains there until at least 40 GHz, while the
return loss is better than 10 dB below 10 GHz and better than 6 dB out to 40 GHz, as
shown in Figure 5.5(b) and (c). This compares favorably with the parameters of commercial
broadband high-attenuation reactive filters, such as the Mini-circuits VLFX-1350, which has
a similar 3 dB corner frequency but becomes re-entrant in its stopband to the point where
it only attenuates by 10 dB at 35 GHz. Based on absorption coefficient measurements

reported in the literature [149, 150, 151], we expect the Eccosorb dielectric to remain lossy
to THz frequencies.

The big remaining question is whether the Eccosorb dielectric works at dilution

fridge temperatures. Eccosorb has been used extensively in the astrophysics community as a
cryogenic black-body emitter for calibration loads in cosmic microwave background studies

[149, 151, 152, 153, 154]. However, these studies were all carried out at temperatures above
1 K, so it was not known whether Eccosorb would thermalize properly and retain its loss
characteristics at millikelvin temperatures. We performed experiments at 50 mK showing
that the transmission and reflection properties of the roach filters were essentially unchanged
from room temperature, and found that the black body noise power emitted by a roach filter
in its stopband is equivalent to that emitted by a thermally anchored NiCr attenuator at the
same temperature [155]. Details of the experiments and results are presented in Appendix
A. With these data, we can confidently use roach filters on fast flux lines, knowing that they


-----


78

will present a well-thermalized, matched impedance to the experiment and will protect the
qubit from black body radiation from higher temperatures.

###### 5.2.4 ###### Hot/cold load setup

To calibrate the system noise temperature of our amplification chain, we use the

noise emitted by two 50 microwave loads at dierent known temperatures; we refer to this
as a hot/cold load setup. By measuring the total output noise of the amplification chain
with each of the two loads, we can extract the noise added by the amplifiers and calculate
an eective system noise temperature, a technique known as a Y-factor measurement. The
method can be seen mathematically as follows: assign the hot and cold loads each known
noise temperatures _T_ _H_ and _T_ _L_ . If the amplification chain has gain _G_ and system noise
temperature _T_ sys referred to the plane of the hot and cold loads, then the output noise
power _P_ out _,H_ and _P_ out _,L_ are given by:

_P_ out _,H_ = _k_ _B_ ( _T_ _H_ + _T_ sys ) _BG_ (5.1)

_P_ out _,L_ = _k_ _B_ ( _T_ _L_ + _T_ sys ) _BG_ (5.2)


Using these two quantities, we can define the Y-factor _Y_ _P_ out _,H_ _/P_ out _,L_ . Substi-
__

tuting in the previous results then yields:



_T_ _H_ + _T_ sys
_Y_ =

_T_ _L_ + _T_ sys


(5.3)


This quantity is a nice one to measure as it is independent of the gain _G_ , which

may be difficult to measure with high precision. Rearranging terms to solve for _T_ sys , we
find that



_T_ _H_ _Y T_ _L_
_T_ sys = __


In the above analysis, we have assumed that _G_ and _B_ are identical for the mea-


(5.4)
_Y_ __ 1


surements of _P_ out _,H_ and _P_ out _,L_ . This is certainly true for _B_ , which can be defined with
precision by a spectrum analyzer. However, drifts in typical microwave amplification chains, so that if we wait long times between measuring _G_ is subject to slow 1 _/f_ _P_ out _,H_ and
_P_ out _,L_ we may not be able to assume _G_ is the same. To address the problem of gain drifts,
we switch rapidly back and forth between the hot and cold loads and detect the output
noise power synchronously. The detected Y-factor will then only depend on variations in _G_
on timescales faster than the switching period.

Our experimental setup can be seen in Figure 5.6. We use 50 terminations on the

4 K plate and the mixing chamber plate as our hot and cold loads. The noise from the hot
load is sent to the mixing chamber plate through a Nb coax to minimize attenuation, which
lets us better estimate the noise at base temperature from the hot load. We chop back and
forth between the hot and cold loads at 100 Hz using a Hittite GaAs switch (as described in
Section 5.2.2) and detect the output noise power synchronously using a spectrum analyzer.
We put the spectrum analyzer in zero span time sweep mode, so that we see a square wave


-----


79

spectrum analyzer

|Col1|Col2|
|---|---|


![SlichterThesis.pdf-97-0.png](SlichterThesis.pdf-97-0.png)

Figure 5.6: Hot/cold load setup for calibrating noise temperature.

Matched 50 loads on the 4 K plate and mixing chamber plate serve as hot and cold loads
for determining system noise temperature. A GaAs switch chops back and forth between
hot and cold loads at 100 Hz, and the output noise power is synchronously detected on a
spectrum analyzer operating in zero span time sweep mode. The hot load is connected to
the mixing chamber plate by a Nb coax to reduce cable loss and give a higher and more
accurately calibrated value of _T_ _H,_ e .

in time from switching between the output noise of the hot and cold loads. The Y-factor
is simply the ratio of the powers at the high and low parts of this square wave; we can
ignore the absolute power level (as long as it is high compared to the spectrum analyzer
noise floor).

As I alluded to in the previous paragraph, we need to be careful in calibrating

_T_ _H_ and _T_ _L_ in order to determine _T_ sys accurately. We know the physical temperatures of
the hot and cold loads very accurately, because they are well thermally anchored to the
4 K and mixing chamber plates, whose temperatures we know from the calibrated fridge
thermometry. However, there is attenuation between the loads and the reference plane

of the measurement. An attenuation _A_ (in linear power units) between the hot load and
the reference plane will reduce the noise at the reference plane to an eective noise _T_ _H,_ e
according to

_T_ _H,_ e = _T_ _H_ (1 _A_ ) + _T_ att _A,_ (5.5)
__

where _T_ att is the noise temperature of the attenuation. This eect has a substantial con-


-----


80

tribution in our setup because the Hittite switch has 2-3 dB of attenuation; in order to
determine _T_ _H,_ e , we have to take separate calibration measurements of the Hittite switch
insertion loss at base temperature (done on a dierent fridge cooldown). We have found
that the attenuation can vary rapidly across the 4-8 GHz band by as much as 1 dB. As long
as _T_ att = _T_ _L_ , we need not apply the correction for the cold load.

I have so far been talking of the noise temperatures _T_ _H_ and _T_ _L_ of the hot and

cold loads as being related to their physical temperatures. This is true in most regimes, but
when we get to temperatures where ~ _!_ __ _k_ _B_ _T_ , as is the case in our experiment, we need to
look at the full quantum treatment. The symmetrized quantum power spectral density of
noise from a matched microwave load can be determined using the fluctuation-dissipation
theorem, and is given by [50]:



~ _!_
_S_ ( _!_ ) = 2 coth


~ _!_

2 _k_ _B_ _T_





~ _!_
_S_ ( _!_ ) =


(5.6)


We can define an equivalent noise temperature ) by Boltzmanns constant. At high temperatures ( _k_ _B_ _T_ __ ~ _!_ ), equation (5.6) reduces to the classic expression _T_ equiv by dividing _S_ ( _!_
for Johnson noise, _S_ ( _!_ ) = _k_ _B_ _T_ and we get _T_ equiv = _T_ . For our hot load, we are in this
regime and so _T_ _H_ is accurately given by the physical temperature of the 4 K plate.


the value of the quantum zero point fluctuations _S_ ( _!_ ) = 1


However, for _k_ _B_ _T_ __ ~ _!_ we find that the noise power spectral density saturates to 1 _!_



1 ~ _!_

2 ~ _!_ , and we have _T_ equiv = 2 _k_


2 _k_ _B_ , no


longer related to the physical temperature. For _!/_ 2 __ = 6 GHz, we have _T_ equiv 145 mK.
__
It is this _T_ equiv , and not the physical temperature, that we must use for _T_ _L_ in our Y-factor
expression. The value of _T_ att is also given by _T_ equiv and not the physical temperature of
the attenuation. After these corrections, we can modify equation (5.4) for the system noise
temperature to read


_T_ sys =



~ _!_

[ _T_ _H_ (1 _A_ ) + 2 _k_
__



~ _!_ _!_

2 _k_ _B_ _A_ ] _Y_ ~ 2 _k_

__


2 _k_ _B_


_B_ _B_ _,_ (5.7)

_Y_ __ 1


where _T_ _H_ is the physical temperature of the hot load on the 4 K plate, _A_ is the attenuation
of the Hittite switch, _Y_ is the Y-factor, and _!/_ 2 __ is the frequency at which we are measuring
the system noise temperature.


#### 5.3 #### Room temperature electronics

Our experiments also rely on precise generation and manipulation of microwave

and RF signals using room temperature electronics. Schematics of typical room-temperature
electronics setups can be found in Chapter 7 and Appendix C.

###### 5.3.1 ###### Pulse and tone generation

We generate our readout and qubit manipulation pulses, as well as our paramp

pump tone, using commercial synthesized microwave generators (Agilent 8257C, 8257D).
These generators have excellent phase stability, which is important to keep the relative
phase between the paramp pump, the readout signal, and the local oscillator (LO) of the


-----


81

demodulation circuit from drifting while operating the paramp in phase-sensitive mode. For
less stable generators, the eect can be mitigated by splitting the output of one generator
and using it for readout, pump, and demod LO; however, this is more technically demanding,
as one then needs good methods for controlling the amplitudes of these signals independently
over disparate ranges without impacting the others.

We shape our readout and qubit pulses by applying shaped pulse envelopes to the

IF port(s) of a microwave mixer. Qubit pulses are shaped using the internal IQ mixer of an
Agilent 8267C generator, using a 1 GS/s arbitrary waveform generator or arb (Tektronix
AWG520) to provide the pulse envelope shape. Readout pulses are shaped using a Marki
M10310MB mixer, using either a 50 MS/s arb (Agilent AG33220A) or the AWG520 to create
the envelope pulse. For both readout and qubit pulses, carrier feedthrough is an issue; we
dont want microwaves impinging on the arbitrary waveform generator outputs (from which
the carrier might reflect and be passed to the mixer output), nor do we want leakage to find
its way down to the qubit and aect its state. We can solve the first problem by putting
roach filters with 800 MHz corner frequencies (see section 5.2.3) on the lines between the
arbs and the mixers. The second problem is solved by experimentally determining the dc
oset voltage (usually a few tens of mV) at which the carrier feedthrough from LO to RF
ports is lowest, and using that as the o voltage for the arb output. For the Marki

M10310MB mixer, careful optimization of this oset voltage gives an on/oratio of 39
dB, which for typical experimental parameters means the readout cavity photon population
from leakage is below that due to thermal excitations at the base temperature. The osets
of the internal IQ mixer in the Agilent 8267C generator can be nulled using front panel
controls to give an on/oratio of 60 dB. If a better on/oratio is needed for either pulse
type, a Marki IQ-0307LXP IQ mixer can be used for pulse shaping; it can be nulled (using
two channels of oset optimization) to better than 70 dB on/oratio.

Because of the low anharmonicity of the transmon, it is important that the spectral

content of qubit pulses not be too broad [76]. For applications requiring very fast qubit
pulses, the pulse-shaping techniques described in [76] can compensate for eects of low
anharmonicity, but the experiments in this thesis do not require such advanced methods.
We use qubit pulses of a minimum 10 ns duration, with the pulse envelopes from the
AWG520 shaped by convolution with a Gaussian filter in software. The readout pulse

shapes are naturally filtered by the 20 ns rise time of the slower AG33220A arb, and dont
typically need additional software waveform shaping.

###### 5.3.2 ###### Variable attenuators

In addition to time-domain shaping of readout pulses, we need to be able to control

their amplitude accurately over at least two orders in magnitude, ranging from very weak
to very strong measurement. For pulses shaped with a mixer, this can be accomplished by
changing the amplitude of the pulse envelope sent to the IF port (because mixers require
a certain fixed LO power to operate, we cannot vary the output amplitude at the RF
port simply by varying the LO amplitude). However, reducing the amplitude of the pulse
envelope on the IF port has the undesired side eect of reducing the mixers on/oratio
by the same amount. One way around this problem is to have the mixer shape pulses with
full amplitude IF pulse envelopes and then to attenuate the pulse after the mixer, thereby


-----


82

preserving the on/oratio while also giving control over the amplitude of the output pulse.
Because we would like fine-grained, repeatable values of readout pulse amplitude, we opted
to use digital variable attenuators.

We used two types of digital attenuators in our experiments, a Hittite HMC425

and a Vaunix Lab Brick LDA-602. The Hittite attenuator can be set to give any attenuation
between 0 and 31.5 dB in 0.5 dB steps. The attenuator came on a connectorized microwaveoptimized demonstration board, and we controlled and powered it using a USB digital
I/O board (National Instruments USB-6501). For some experiments, though, the Hittite
attenuator did not provide sufficient dynamic range for controlling readout powers, and so
we switched to using the Lab Brick attenuator, which can be set to any attenuation between
0 and 63 dB in 0.5 dB steps. The attenuation at a given setting appears to be very stable,
with less than 0.01 dB of variation over the course of an hour. The Lab Brick attenuator
is only speced to work to 6 GHz, but we tested it on a network analyzer and found that
it works admirably to 10 GHz and beyond, with the caveat that as the frequency rises
above 7 GHz the maximum attenuation saturates to a value less than the rated 63 dB. This
maximum attenuation value changes steadily with frequency from 63 dB at 7 GHz to 43
dB for frequencies above 12 GHz. One additional wrinkle with the Lab Brick attenuators is
that they appear to emit digital switching noise at low frequencies, potentially aecting the
experiment. To combat this, we use inner-outer dc blocks on both sides of the attenuator,
as well as a high pass filter (Mini-Circuits VHF-3800+) on the output.

###### 5.3.3 ###### Demodulation and digitization

The readout signals returning from the fridge carry information about the qubit

state as a phase modulation on a roughly 6 GHz carrier. To strip the carrier and just keep
track of the phase modulation (whose bandwidth is only __ 5-10 MHz, set by the readout
cavity linewidth _/_ 2 __ ), we perform homodyne detection by mixing the readout signal with
a local oscillator at the same frequency. We demodulate using an IQ mixer (Marki IQ0307LXP), giving us information about both the amplitude and the phase of the readout
signal. For qubit readout, we expect there to be two steady amplitude/phase combinations
in the readout signal (corresponding to the two qubit states), with their vector dierence
defining a line in the I-Q plane (see Figure 2.10, e.g.). By shifting the relative phase of the
LO and the readout signal, we can align this line with either the I or Q output quadratures,
so that all the qubit state information in the demodulated output signal lies only in one of
the two output quadratures. This makes post-processing simple, as we dont have to turn
every I-Q pair into an amplitude-phase pair in software to see changes in the qubit state.
To accomplish the desired phase shift, we use a phase shifter (Sage 6705-15) on the readout
signal right before the mixer.

After demodulation, the signal at the I and Q ports of the mixer is still quite small

( __ __ V-mV), too small for the resolution of our digitizer card. We boost the amplitude of
each output using an ultra-low-noise OPA847 op-amp configured for noninverting voltage
gain of 40 with 100 MHz 3 dB bandwidth. The OPA847s are each on their own circuit
board (Texas Instruments DEM-OPA-SO-1B) configured for optimal high-frequency performance, including 50 input and output impedance matching. Both the IQ mixer and
the OPA847 following amplifier boards are contained in a metal shielding box with SMA


-----


83

bulkhead connectors for all signals. The OPA847s are run odual power supplies with __ 5
V regulators inside the shield box.

After post-amplification by the OPA847s, the demodulated I and Q signals are

filtered to reduce noise bandwidth. We use either commercial filters (Mini-Circuits SLP10.7+) or simple homemade single-pole RC filters (to give a slower rollo), both with cuto
frequencies in the 5-10 MHz range. After filtering to remove excess noise, the signals are
digitized by an 8-bit 2-channel 1 GS/s digitizer (Alazar ATS9870). The digitizer is typically
run at 100 MS/s (10 ns per point), which gives a suitably large Nyquist bandwidth of 50
MHz to prevent aliasing. The data from each measurement trace are sent to LabVIEW
using asynchronous direct memory access, which allows very high data throughput rates.
LabVIEW collects the raw data from each of the two channels and saves it to disk as an array
of unsigned 8-bit binary numbers. The digitizer is a PCI Express card, capable of nominal
data throughput of 1.4 GB/s, but the process of sending the data through LabVIEW slows
down the transfer rate considerably. However, we are able to acquire and save data to the
hard drive at a maximum rate of roughly 100 MB/s, corresponding to a roughly 50% duty
cycle for data acquisition. We use eSATA hard drives for data storage in order to keep up
with this throughput.


-----


84

## Chapter 6

# Calibration experiments

This chapter details the experimental realization of the lumped Josephson para-

metric amplifier (LJPA), or paramp, described in Chapter 3. It also details the calibration
procedures for the transmon qubit and its readout cavity.

The paramp is essential to the work presented in subsequent chapters, so it is

important that we understand its behavior experimentally. We discuss the techniques for
testing and biasing the paramp to its operating points. We also present measurements of
amplifier gain, bandwidth, and noise. The data shown in this chapter are taken from several
dierent paramp samples at a variety of operating frequencies, and are selected to provide
representative examples of paramp behavior. We tested and used five dierent paramp

samples over the course of the work presented in this thesis, and all five samples displayed
very similar gain, noise performance, and tunability.

The techniques for calibrating the qubit-cavity system are general, and we will

only sketch them. These calibration methods are used for all the qubit samples in this
thesis at every bias point to which they are tuned.

#### 6.1 #### Paramp sample packaging

The paramp is a low- _Q_ nonlinear microwave resonator measured in reflection.

We use Bollywood 180 __ hybrid microwave board (see Chapter 5) to launch signals to our
paramp. The Bollywood turns incoming single-ended microwave signals into a dierential
excitation and presents a 100 impedance to the paramp. The paramp is directly coupled
to the launch, with no on-chip coupling capacitors, so this impedance sets the _Q_ of the
paramp resonance. The dierential excitation means that the ground plane used in the splitgeometry paramp capacitors is a true virtual ground and so will not radiate. The launch is
designed so that the sample is glued directly to a copper surface to aid in thermalization.

The paramp requires a flux bias for tuning, which we generate using an o-chip

superconducting coil wound on a copper bobbin. The coil generates fields of up to a few mT
at the paramp. The paramp amplifies microwave signals but also acts as a very sensitive
low-frequency magnetometerexhibiting some of the highest flux sensitivity seen to date
experimentally [59]so it is very important to shield it from external magnetic fields. We
place the paramp and its flux bias coil inside a superconducting aluminum box to reduce


-----


85

![SlichterThesis.pdf-103-0.png](SlichterThesis.pdf-103-0.png)

Figure 6.1: Paramp sample box.

The paramp is mounted on a Bollywood launch attached to a copper cold finger as shown
in (a). A superconducting coil beneath the sample is used for flux bias. The system is
fully enclosed in a superconducting aluminum shield, pictured in (b). Microwave signals, dc
current for flux bias, and copper thermalization straps penetrate the shield through highaspect ratio holes in the lid. A cryoperm shield, seen in (c), is used to reduce flux trapping
in the aluminum shield as it cools through _T_ _c_ .

coupling to external fields. The aluminum box is placed inside a Cryoperm can to reduce flux
trapping in the box and sample as they cool through _T_ _c_ . The microwave line and coil wires
enter the aluminum box through high-aspect-ratio holes to maintain shielding eectiveness.
One must be careful to filter the leads to the flux bias coil at very low frequency to prevent
noise pickup. Further details of the sample boxes and coil filtering are in sections 5.1 and
5.2.1. Figure 6.1 shows an image of the sample box with Bollywood launch, flux bias coil,
thermalization straps, and shields.

#### 6.2 #### Paramp biasing procedure

Upon reaching base temperature, we do some initial tests and then adjust the


paramp bias parameters to give the desired gain. One of the advantages of the LJPA paramp
is its wide frequency tunability; typical samples can be tuned to provide gain anywhere in
the 4-8 GHz band by tuning with a magnetic field. The first test we usually complete is to
check that the paramp resonance can be tuned into the desired frequency range. Figure 6.2
shows the phase response of a typical paramp as a function of flux bias, measured in terms
of current through the flux bias coil. The periodic response comes from tuning through
several flux quanta; a flux quantum typically corresponds to a few mA of coil current in our
setup. Since the flux sensitivity of the paramp can be as low as 10 __ 8  0 _/_ _p_ Hz, the current


noise on the flux bias coil must be no more than a few pA


Hz. This typically requires


substantial filtering when using a digital current source (see section 5.2.1 for further details).

The astute reader will notice a number of horizontal bands in this figure, indicating

variations in reflected phase with frequency that do not depend on flux bias. The bands


-----


86

![SlichterThesis.pdf-104-3.png](SlichterThesis.pdf-104-3.png)

![SlichterThesis.pdf-104-0.png](SlichterThesis.pdf-104-0.png)

![SlichterThesis.pdf-104-2.png](SlichterThesis.pdf-104-2.png)

![SlichterThesis.pdf-104-1.png](SlichterThesis.pdf-104-1.png)

-3.0 -2.0 -1.0 0.0 1.0 2.0 3.0

Coil current (mA)

Figure 6.2: Typical paramp tuning with flux.


8.0

7.5

7.0

6.5

6.0

5.5

5.0

4.5

4.0


This plot shows the reflected phase of the paramp as a function of applied magnetic flux,
parameterized in terms of the current in the flux bias coil. The yellow band which signifies
the paramps resonant frequency tunes between 4 and 7 GHz in this scan and repeats over
several flux quanta. The ripple-like horizontal banding is due to interference eects from
the biasing circuit, and the large phase excursions above 7.5 GHz are due to the circulators
in the output chain. A small spurious resonance in the launch board is visible at 6.5 GHz,
but does not aect the performance of the paramp.

appear to be periodic in frequency. These bands are small-amplitude ripples in the reflected
phase caused by interference eects arising from the finite directivity of the directional
coupler used to bias the paramp. The directional coupler sends the pump tone from the
side port almost entirely towards the paramp, but a small fraction, usually about 20 dB
lower in power, is coupled in the direction away from the paramp. This leakage interferes
with the reflected signal from the paramp and causes small phase and/or magnitude shifts,
depending on the relative phase between the two signals. As the frequency changes, the
relative phase will change as well. The frequency periodicity of these phase modulations
given by _v/_ 2 _`_ , where _v_ is the group velocity of microwaves on the coaxial line and _`_ is the
length of line between the directional coupler and the paramp. We typically would like
to increase the spacing between these phase wiggles so that the phase response of the
paramp is locally flat in frequency; this entails putting the directional coupler as close to
the paramp as is practical. In addition to the small phase modulations, there are two other
horizontal features in Figure 6.2. The first is a small spurious environmental resonance at
6.5 GHz. This is atypical, but did not aect the performance of the paramp. The second is
the slow phase rolloabove about 7.25 GHz; this is caused by the circulators on the output
amplification chain, which display this sort of phase response near the edge of their band.

Once we have determined that the paramp tunes properly with flux, we can choose

a rough flux bias for our frequency of interest. This is done using a vector network analyzer
in frequency sweep mode, looking at the reflected phase of the paramp and tuning the flux


-----


87


90

60

30

0

-30

-60

-90

![SlichterThesis.pdf-105-0.png](SlichterThesis.pdf-105-0.png)

-102 -101 -100 -99 -98 -97 -96 -95 -94

Power at paramp (dBm)

Figure 6.3: Paramp transfer function.


We show four linecuts of the paramp reflected phase versus pump power. These curves
represent the transfer function of the amplifier, which maps an amplitude modulation on an
incident signal to a phase modulation of the reflected pump. The red curve is in the bistable
regime and shows an abrupt phase jump. The green, blue, and purple curves are cuts in the
paramp regime with decreasing paramp gain. The steepness of the transfer function gives
the gain, while the width in power gives the dynamic range. The phase shift as one goes
through the resonance in the power direction is about 180 __ . The curves have been shifted
vertically to show the similarity in their overall phase shifts. The shape of these curves
compares well with the theoretically calculated ones in Figure 3.6.

until the steepest part of the phase response is at the desired frequency. Since the frequency
of this steepest phase response is a function of pump power as well as flux bias, we perform
this search at powers roughly equivalent to a typical pump power during operation, about
-95 dBm at the paramp.

With the flux roughly tuned up, we switch from a frequency sweep to an upward

power sweep at our desired pump frequency, centered around our estimated pump power.
This shows us the response of the pump phase with pump power, which is the transfer
function of our paramp 1 . Figure 6.3 shows some sample traces of this transfer function. If
the phase response has a discontinuity, we are in the bistable regime and we tune the flux
to decrease the resonant frequency of the paramp until the phase response becomes smooth
and continuous. If there is little or no slope in the phase response, we tune the flux to
increase the resonant frequency. The gain is directly related to the steepness of the phase
response curve, as described in Chapter 3. The dynamic range is proportional to the width
of the phase response in power.


We note that the reflected phase changes by __ 180 __ as we go through the paramp

resonance. One typically thinks of resonators measured in reflection having 360 __ of phase

1 The fact that there is any phase response with power is evidence of the nonlinearity of the paramp. A

linear resonator exhibits no change in phase response with drive amplitude. Thus, as would be expected,
the transfer function of our paramp requires nonlinearity to exist.


-----


88

![SlichterThesis.pdf-106-0.png](SlichterThesis.pdf-106-0.png)

![SlichterThesis.pdf-106-3.png](SlichterThesis.pdf-106-3.png)

![SlichterThesis.pdf-106-1.png](SlichterThesis.pdf-106-1.png)

5.50 5.60 5.70 5.80 5.90 6.00

Frequency (GHz)


-95



-98

-101

-104

-107

-110

-113

-116


-92

-95

-98

-101

-104

-107

-110

-113

-116

|Col1|paramp regime 180 Reflected 135 90 45 phase 0 -45 (degrees) -90 -135 -180|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
||180 Reflected 135 90 45 phase 0 -45 (degrees) -90 -135 -180|||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||


![SlichterThesis.pdf-106-4.png](SlichterThesis.pdf-106-4.png)

![SlichterThesis.pdf-106-2.png](SlichterThesis.pdf-106-2.png)

7.25 7.35 7.45 7.55 7.65

Frequency (GHz)


Figure 6.4: Paramp phase response.

These two plots show the reflected phase of the paramp as a function of pump power and
frequency. The plots are made by interleaving increasing and decreasing power sweep data
so that regions of bistability appear toothed. The region of bias parameter space useful
for parametric amplification, which occurs near but not inside the bistable region, is labeled.
Part (a) shows a fairly well-behaved paramp response, similar to theory. Part (b) shows the
paramp response in the presence of embedding circuit impedance fluctuations, which cause
non-monotonic behavior of the resonance in the paramp and bistable regimes. One must
be more careful when choosing a paramp bias point in this situation.

shift as one crosses the resonance. However, this only holds true if we sweep through the
resonance in frequency. In our case, we are sweeping in power and not frequency, and thus
the phase shift is not necessarily 360 __ ; a purely linear resonator would show no phase shift
in power, for example.

It is useful to make a map of the phase response of the paramp with respect to

pump power and frequency. This shows the regions of bistability and the regions of paramp
gain, and helps diagnose any issues with the paramp bias. Two sample phase response plots
are shown in Figure 6.4. The data for these plots is taken by sweeping the excitation power
both upwards and downwards and then interleaving the up and down sweep directions as
we step in frequency. At low powers, the resonance is essentially linear and independent
of power. As the power increases, the resonance bends to lower frequency and sharpens,
eventually becoming bistable beyond a the critical point at ( _!_ _c_ _, P_ _c_ ). The bistable region
is readily evident from the toothed eect caused by interleaving the up and down sweep
traces. One should always check that the chosen paramp bias point is not in or near a
region of bistability or the paramp will not function as desired.

At the bias point in Figure 6.4 (b), the width in power of the bistable region does

not grow smoothly as we go to lower frequencies (as is expected theoretically), but instead


-----


89

grows and shrinks non-monotonically. This eect is due to variations in the impedance of the
embedding circuit, in our case the Bollywood launch, likely due to spurious resonances. The
embedding circuit impedance shunts the paramp resonator and directly sets its _Q_ , which
in turn sets the frequency and power of the critical point ( _!_ _c_ _, P_ _c_ ). If the embedding circuit
impedance changes with frequency, then the detuning from the critical point _!_ __ _!_ _c_ and
thus the width in power of the bistable region will vary non-monotonically with frequency
as well [108, 156].

The same impedance variations which aect the region of bistability also aect

the paramp gain; in their presence, the gain when biased in the paramp regime is no longer
necessarily a monotonic function of the flux bias or pump frequency. This is one reason
it is helpful to take 2D phase response plots, because they help identify the best paramp
bias points in a reliable way. For example, flux tuning may increase, then decrease, then
increase the gain again, so if one does not search thoroughly it is possible to miss finding
the optimal bias point. If the impedance variation is very pronounced, the gain profile can
have strange behavior, as detailed in section 6.3.1. In truly extreme cases we have observed
two subregions of bistability separated by a monostable region. Using the 2D plot can help
to avoid accidentally biasing in such a regime, which might be unsuitable for paramp use
because of the proximity of bistable regions on both sides.

#### 6.3 #### Paramp performance

Having found a suitable flux bias for operation, we can now optimize the paramps

properties for our desired application. To do this, we use a directional coupler to combine
test signals from the vector network analyzer with a pump tone from a separate microwave
generator. The network analyzer is used to calibrate the gain and bandwidth of the amplifier
as a function of pump power and frequency. We determine the paramp noise performance
with a spectrum analyzer, using the network analyzer as a CW signal source.

###### 6.3.1 ###### Paramp gain

We first take a network analyzer frequency sweep over the frequency range of

interest with the paramp pump oto calibrate the loop gain of the system in the absence
of the paramp pump. All further traces are then taken dividing out this loop gain so

that with the paramp pump on, the normalized network analyzer traces now give a direct
measurement of the paramp gain. We then explore the phase space of pump power, and to
a lesser extent fine-tuning of the flux bias, to optimize the gain and bandwidth as desired.
Typically, we get around 20 dB of gain with 10-15 MHz full 3dB bandwidth.

Initially we use a very small signal power, usually around -140 dBm at the sample,

to ensure we are not exceeding the dynamic range of the paramp. However, it is important
to know when the paramp starts to saturate, so we can find its 1 dB compression point (the
point at which gain is reduced by 1 dB from nominal, a standard measure of saturation onset
in microwave amplifiers) by increasing the signal power and measuring the gain. Typical
values for the input signal power at the 1 dB compression point are around -135 to -130
dBm when biased in the high-gain regime. Figure 6.5 shows three sample gain traces at


-----


90


30

21
18
15
12

9
6
3
0

![SlichterThesis.pdf-108-0.png](SlichterThesis.pdf-108-0.png)

-30 -20 -10 0 10 20 30

Signal detuning from pump (MHz)

Figure 6.5: Paramp gain and bandwidth.


This figure shows three typical gain traces with identical pump power of -100 dBm and
varying signal power as indicated in the legend. As the signal power increases, the paramp
saturates and the gain is reduced.

21

15


12


![SlichterThesis.pdf-108-1.png](SlichterThesis.pdf-108-1.png)

5.82 5.84 5.86 5.88 5.90 5.92 5.94

Frequency (GHz)

Figure 6.6: Unusual gain profile.

This paramp sample suered from substantial impedance variations in the embedding circuit, and has a very unusual gain response as a result. The pump is clearly visible at 5.82
GHz, while the main gain peak shows up 60 MHz detuned (a second symmetrical gain peak
occurs at - 60 MHz detuning, not shown).

dierent signal powers. For the lowest power signals, we have around 26 dB of gain with 10
MHz full bandwidth; as the signal power increases, the gain is reduced due to saturation,
although the bandwidth remains substantial.

The embedding circuit impedance variations mentioned in the preceding section


-----


91

can produce some strange eects, including a double-humped gain profile at large detunings, with gain comparable to or greater than in the central peak at optimal bias. The
impedance variations are on frequency scales smaller than resonator linewidth, so we end
up coupling a low- _Q_ mode at the pump frequency with higher- _Q_ modes detuned to either
side. Because gain increases with _Q_ , these impedance variations depress the central peak
gain while increasing the gain detuned to the sides. Figure 6.6 shows such a bias point,
with the maximum gain occurring 60 MHz detuned from the pump (sharp needle). This
bias point was used successfully in some experiments, despite its unusual shape.

###### 6.3.2 ###### Noise performance

Once we have chosen a satisfactory gain point, we can check the noise performance

of the amplifier. For the HEMT amplifier at 4 K, we used a hot-cold load technique described
in section 5.2.4 to determine system noise temperature. Unfortunately, we cannot do this
with the paramp. The thermal noise power _k_ _B_ _TB_ in a 20 MHz band from a 4 K hot load
is about -120 dBm, so exposing the paramp to noise from the hot load will saturate it and
lead to an inaccurate noise assessment.

To get around this difficulty, we use the method of signal-to-noise ratio (SNR)

improvement, detailed in Figure 6.7. First, we measure the system noise temperature _T_ sys
with the paramp ousing the standard hot-cold load method. This noise temperature is
calibrated to the reference plane of the 6-way switch used to change between the hot-cold
load and the qubit/cavity samples of interest. We can then inject a signal, again with the
paramp o, and measure the ratio of the signal peak to the surrounding noise floor using
a spectrum analyzer. This is then repeated with the paramp pump on. Since the signal
has the same amplitude at the reference plane in both cases, the improvement in SNR from
turning the paramp on must be due to a reduction in the system noise. We can simply
divide the value of _T_ sys measured with the paramp oby the SNR improvement (in linear
power units) to give the value of _T_ sys with the paramp on.

Because the attenuation of the cold fridge injection lines is difficult to calibrate

accurately, we use a qubit and cavity to calibrate the power of our input signal at base
temperature. We know that the power radiated from a cavity in transmission is given by
_P_ rad =  _n_ ~ _!_ , where  _n_ is the cavity photon occupation, _!_ is the signal frequency, and __ is

the cavity linewidth. The value of  _n_ can be extracted very precisely using the ac Stark shift,

as discussed in sections 2.3.3 and 6.4.3, while _!_ is set by the signal generator and __ is easily
measured independently. This precise calibration of the power at base temperature can be
used to perform an independent check on the extracted noise temperature without requiring
the measurement from the hot-cold load. Because we know the precise signal power both
at base temperature and at room temperature, we can extract the overall gain _G_ of the
amplification chain between the reference plane and the spectrum analyzer. We can then
take the noise power spectral density measured at the spectrum analyzer and divide by _G_
to find the noise power spectral density at the reference plane at base temperature; the
noise power spectral density can be converted into a noise temperature by dividing by _k_ _B_ .

These methods require us to resolve the height of the signal peak above the noise

floor, which means that the signal and pump must be at dierent frequencies. As a consequence, we can only extract the noise temperature in phase-preserving amplification mode.


-----


92


spectrum analyzer
readout

![SlichterThesis.pdf-110-0.png](SlichterThesis.pdf-110-0.png)

Figure 6.7: Paramp noise measurement scheme.

This experimental setup allows us to calibrate the system noise temperature _T_ sys with the
paramp on by measuring the improvement in signal-to-noise ratio over when the paramp is
o. We know _T_ sys with the paramp ofrom using a hot-cold load. We then inject a signal
of known amplitude and look at the ratio of signal peak to noise floor at the output using
a spectrum analyzer. When we turn the paramp on and o, we see this ratio change and
can deduce the reduction in _T_ sys when the paramp is on. The qubit and cavity are used to
provide an accurate calibration of signal power using the ac Stark shift.

There is not an analogous procedure for measuring noise temperature in phase-sensitive
mode, but we can make a rough estimate by substracting from the noise temperature estimated in the phase-preserving mode. ~ _!/_ 2 _k_ _B_

The system noise temperature we extract is shown in Figure 6.8 as a function of


signal power. For small signals, where the amplifier is not saturated, our _T_ sys approaches
the standard quantum limit for phase-preserving amplification of . The noise temperature appears to be consistently slightly higher than the quantum limit, which can ~ _!/_ 2 _k_ _B_
be attributed to loss between the reference plane and the paramp, primarily due to the
circulators. As the signal power increases, the amplifier starts to saturate and the noise
performance degrades accordingly. This knee occurs at powers which correspond roughly
to cavity photon occupations  _n_ __ 1 __ 2 in a typical circuit QED setup. Even with a signal

power 10 __ 15 dB above the level where the paramp starts to saturate, the value of _T_ sys is
still considerably lower than that without the paramp, which is _T_ sys 7 K with minimal
__
circulators, a state-of-the-art HEMT, and superconducting coaxial cables between the base
stage and HEMT stage (see section 5.2.2 for details).


-----


93


3.0

2.5

2.0

1.5

1.0

0.5


0.0

![SlichterThesis.pdf-111-0.png](SlichterThesis.pdf-111-0.png)

-145 -140 -135 -130 -125 -120 -115

Signal power at paramp (dBm)

Figure 6.8: System noise temperature with paramp.

The system noise temperature with the paramp on is shown here as a function of the signal
power. For low power signals, the noise is almost at the quantum limit. As the signal power
increases and the paramp saturates, the noise temperature degrades, but even deep into
the saturated regime it is still considerably better than the best value achieved without the
paramp of _T_ sys 7 K.
__

###### 6.3.3 ###### Saturated regime operation

Because most signals of interest (e.g. from a qubit readout cavity) are of high

enough power that the paramp is no longer in the linear gain regime, it is helpful to understand the behavior of the paramp in the saturated regime as well. Here we use the
paramp not as a linear amplifier in the traditional sense, but rather as a continuous digital
detector. One could imagine an op-amp configured to have very large closed-loop gain; its
output would always be railed high or low, depending on the input signal, but would change
rapidly to follow that input signal. If the signal of interest only has two values, as is the
case with the readout signal from a qubit, then such an instrument could be very useful as
an amplifier even though its output is not a linear function of its input. The principle of
saturated regime operation for the paramp is explained in more detail in section 3.4.4.

Figure 6.9 shows the measured average phase of the reflected paramp pump as a

function of pump power, where the input signal comes from a qubit in a cavity (for power
calibration purposes). The paramp is operating in phase-sensitive mode. We prepare the
qubit either in the ground (blue, open circles) or excited (red, filled circles) states; the
resulting pointer states which form the paramp input signal are approximately 180 __ phase
shifted from each other. In part (a), the signal power is about -132 dBm, while in part (b)
it is about -118 dBm. In both cases, we can see that there is a range of pump powers for
which there is a large dierence in the output phase shift signal depending on the phase


-----


94



+90


+90


0

-90


0


|Col1|Col2|Col3|
|---|---|---|
|P = -132 dBm sig|||
|P = -132 dBm sig|||
||||

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|P = -118 dBm sig||||
|||||


-94.2 -94.0 -93.8

Pump power (dBm)


-94.2 -94.0 -93.8

Pump power (dBm)


Figure 6.9: Saturated regime paramp response.

These curves show the average reflected phase of the pump in phase-sensitive mode as a
function of pump power. We use two input signals of the same amplitude but approximately
180 __ out of phase with each other (red and blue traces/circles), both for for weak signals
(a) at the edge of the linear regime and strong signals (b) deep in the saturated regime. In
both instances we can find a value of the pump bias which gives clearly distinguished values
of the reflected pump phase depending on the input signal.

of the input signal. The amplifier is already starting to saturate in part (a), while in part
(b) it is well into the saturated regime; the increase in the input signal amplitude has not
brought about a correspondingly large increase in output phase shift. If we set the pump
power at the point denoted by the dashed vertical line, the reflected paramp phase will
swing almost 180 __ depending on the two-state input signal. In this regime, we can use the
paramp as a continuous digital detector.

#### 6.4 #### Calibration of the qubit/cavity system

We perform a number of tests and calibrations on our qubit/cavity system to

extract the relevant experimental parameters, assess the coherence properties of the qubit,
and calibrate the measurement strength. This section gives a brief overview of a standard
set of calibrations performed on each sample at each qubit bias point.

###### 6.4.1 ###### Qubit and cavity spectroscopy

Our first task is to extract the parameters _E_ _J_ and _E_ _C_ of the qubit, _!_ cav and __ of

the cavity, and the coupling _g_ . Note that for simplicity we will use the notation _g_ and 
to refer to the quantities denoted _g_ 01 and  0 , respectively, in section 2.3.3.

The cavity frequency can be seen almost immediately in a network analyzer mea-


surement, and we use this rough frequency to set the measurement tone for qubit spectroscopy. Here we turn on a weak measurement tone, with the power chosen to give  _n_ __ 1,

and examine the cavity response in the presence of a weak qubit spectroscopy tone which
is swept in frequency. The output signal will change when the qubit spectroscopy tone is
at the frequency of the qubit line. We use this method to extract the qubit energy splitting


-----


95

|Col1|2g 0 transmission Relative -10 -20 -30 cavity -40 (dB) -50|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||0 transmission Relative -10 -20 -30 cavity -40 (dB) -50||
||||||||
||||||||


![SlichterThesis.pdf-113-0.png](SlichterThesis.pdf-113-0.png)

![SlichterThesis.pdf-113-1.png](SlichterThesis.pdf-113-1.png)

![SlichterThesis.pdf-113-3.png](SlichterThesis.pdf-113-3.png)

![SlichterThesis.pdf-113-2.png](SlichterThesis.pdf-113-2.png)

Flux bias coil current (mA)

Figure 6.10: Avoided crossing of qubit and resonator.

This plot shows the magnitude response of a cavity measured in transmission as a transmon
qubit is tuned through the cavity frequency. We see the expected avoided crossing with a
splitting given by 2 _g_ . The transmon line can be seen in this cavity measurement because the
eigenstates of the Jaynes-Cummings Hamiltonian are a superposition of cavity and qubit
states; as the qubit detunes farther from the cavity, the photonic part of the eigenstate is
reduced and so the line weakens.


_!_ 01 . If we turn up the power of the qubit spectroscopy tone, we can excite two-photon
transitions between transmon states _|_ 0 _i_ and _|_ 2 _i_ ; the cavity will show a response when the
spectroscopy tone is at frequency _!_ 02 _/_ 2. We can repeat this process to perform three-photon
spectroscopy of the 0 _!_ 3 transition as well 2 .

There are two methods for calibrating _g_ . One method is to measure the cavity

response as we tune the transmon frequency through the cavity frequency; this will give us
an avoided crossing as shown in Figure 6.10. We can see the relatively broad, horizontal
resonator line hybridizing with the narrow qubit line as the system enters the resonant
limit. At the point of narrowest approach between the two lines, they are separated by a
frequency of 2 _g_ .

A superior way to calibrate _g_ is what we call the punchout method, which is

a measurement of the Lamb shift. For small cavity photon occupation  _n_ , the bare cavity

frequency is dressed by the presence of the qubit in its ground state, which shifts the cavity
resonant frequency by an amount



_g_ 2
__ 01 = __ _._ (6.1)
__ 

2 Technically, the spectroscopic values measured are the Lamb shifted qubit transition frequencies  _!_ _ij_ and

not the true uncoupled qubit transition frequencies _!_ _ij_ . For sufficiently large , this does not have much
eect on the calibrations described in this section. However, for maximum precision one should correct for
the Lamb shifts on the spectroscopic frequencies, which is done self-consistently using progressively finer
estimates of _E_ _J_ , _E_ _C_ , and the _g_ _ij_ .


-----


96

|Col1|180 Reflected 135 90 45 phase 0 -45 (degrees) -90  -135 01 -180|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||180 Reflected 135 90 45 phase 0 -45 (degrees) -90 -135 -180|||||
|||||||


![SlichterThesis.pdf-114-1.png](SlichterThesis.pdf-114-1.png)

![SlichterThesis.pdf-114-0.png](SlichterThesis.pdf-114-0.png)

5.90 5.91 5.92 5.93 5.94 5.95

Frequency (GHz)


-10

-20

-30

-40

-50

-60


Figure 6.11: Qubit punchout calibration.

This plot of cavity phase response versus drive power shows the punchout calibration
method. At low powers, the cavity frequency is dressed by the qubit. As the power increases, the cavity becomes nonlinear due the presence of the qubit, until finally the qubit
is punched out and the cavity shows its bare frequency _!_ cav . The dierence between the
bare and dressed cavity frequencies is the Lamb shift __ 01 , which gives us _g_ by equation
(6.1). In our qubit experiments, we always operate with sufficiently low readout power that
the cavity remains linear.

As we drive the cavity at higher and higher powers, the cavity inherits the nonlinearity
of the qubit and the cavity resonance shifts. Finally, at very high photon numbers there
are so many quanta of excitation in cavity and qubit that the cavity behaves classically
and no longer shows the eects of the qubits presence [157]. In this regime, we simply see
a response at the bare cavity frequency _!_ cav ; the qubit has been punched out. Figure
6.11 shows this eect, with the cavity response changing from the dressed frequency at low
power to the bare frequency at high power.

We take linecuts of the vector cavity response both at low powers (well below the

punchout threshold) and at high powers (above the punchout threshold) and fit the real
part of the cavity response to a Lorentzian function to extract the resonant frequency and
linewidth for both cases. The resonant frequency with the qubit punched out is just _!_ cav ,
and the dierence between the resonant frequencies with and without punchout gives us
the Lamb shift shown in (6.1). Using our knowledge of _!_ 01 from qubit spectroscopy (which
we must also correct for the Lamb shift by an amount identical to what is measured from
the punchout), we can extract the value of _g_ . We find that the linewidth __ is the same at
both high and low powers.


-----


97

This punchout technique is straightforward and has the advantage that one does


not require an avoided crossing between qubit and cavity to calibrate _g_ . If one exists, we
can use it as a less-trusted cross-check of the extracted value of _g_ . We also note that if
we prepare the qubit in state _|_ 1 _i_ and perform a punchout, the power threshold at which
the punchout occurs is dierent than if the qubit is in state _|_ 0 _i_ . This eect has been

used experimentally to provide a high-fidelity single shot readout [158] (albeit one which
is not QND) and can be well explained theoretically by numerical diagonalization of the
generalized Jaynes-Cummings Hamiltonian for a multilevel system [93].

Armed with measurements of the first three transmon frequencies, _!_ cav , and _g_ , we

can use Mathematica to solve for the qubit energy scales _E_ _J_ and _E_ _C_ . If we know _E_ _J_ and
_E_ _C_ , we can determine all of the _g_ _ij_ for higher levels numerically and solve for the dispersive
shift __ ( _n_ ) using the expressions given at the end of section 2.3.3. Since the estimates of _E_ _J_


and _E_ _C_ depend on the accuracy of our knowledge of the Lamb shifts and thus on the _g_ _ij_ ,
we can perform this procedure iteratively for increased accuracy if desired. Generally, such
a procedure is not needed if we are well into the dispersive regime _|_  _| _ _g_ .

To calibrate the qubits sensitivity to flux, we can perform qubit spectroscopy as a

function of flux bias in the external coil and then fit the resulting spectrum to the theoretical
energy spectrum of the qubit. We fix the value of _E_ _C_ to be the one extracted by the method
above at a given bias point, allowing the maximum _E_ _J_ and the flux periodicity to vary until
the fit is optimized. One does not need to be able to sweep through a full flux quantum to
yield an accurate fit.

###### 6.4.2 ###### Rabi, Ramsey, ###### T ###### 1 ###### , and tomography

Once we have established the qubit and cavity frequencies, we can proceed to

examine the qubit coherence, characterized in terms of the relaxation time _T_ 1 and the
dephasing time _T_ 2 . We measure these coherence times using several standard methods


known from nuclear magnetic resonance and atomic physics. All of these measurements
are ensemble measurements, requiring many repetitions of a given experiment. The delay
time between repetitions is chosen to ensure that the qubit has relaxed back to the thermal
ground state (which is _|_ 0 _i_ , since we operate with ~ _!_ _q_ __ _k_ _B_ _T_ ) before the next repetition.

Typically we start by measuring Rabi oscillations of the qubit. We send a pulse

at the qubit frequency of varying duration and then measure the state of the qubit after
the pulse has stopped. We repeat this experiment a number of times for each value of the
Rabi pulse duration and average the results from each pulse duration together, giving us
decaying sinusoidal Rabi oscillations as shown in Figure 6.12(d). The frequency of these
Rabi oscillations depends on the amplitude of the Rabi drive and on the detuning of the
Rabi drive from the qubit frequency  _!_ as follows:


 Rabi =


 2 + ( _!_ ) 2 _,_ (6.2)


where is the Rabi frequency at zero detuning.

We can use Rabi oscillations for several purposes. First, they provide a probe of

the qubit frequency, which can be found by fixing the amplitude of the Rabi drive tone and
varying its frequency until we minimize the frequency of the Rabi oscillations. Secondly,


-----


98

![SlichterThesis.pdf-116-2.png](SlichterThesis.pdf-116-2.png)

readout

![SlichterThesis.pdf-116-5.png](SlichterThesis.pdf-116-5.png)

500 1000 1500 2000

T 1 delay  (ns)


(a) (b)  /2  /2 (c)


 /2


 /2


 _q_




 _q_

 _ro_


 _q_

 _ro_


![SlichterThesis.pdf-116-0.png](SlichterThesis.pdf-116-0.png)

![SlichterThesis.pdf-116-1.png](SlichterThesis.pdf-116-1.png)

readout


readout


(d) (e) (f)


160

140

120

100


160

140

120

100


160

140

120

100


![SlichterThesis.pdf-116-3.png](SlichterThesis.pdf-116-3.png)

![SlichterThesis.pdf-116-4.png](SlichterThesis.pdf-116-4.png)

500 1000 1500 2000

Rabi duration  (ns)


500 1000 1500 2000

Ramsey delay  (ns)


Figure 6.12: Qubit coherence measurments: Rabi, Ramsey and _T_ 1 .

Parts (a), (b), and (c) show timing diagrams for the Rabi, Ramsey, and _T_ 1 experiments
respectively. The red trace indicates pulses at the qubit frequency _!_ _q_ , while the black

indicates pulses at _!_ ro
, the readout frequency. Panels (d), (e), and (f) show typical experimental Rabi, Ramsey, and _T_ 1 traces. Each data point (red circles) represents the average
measured voltage of 3 __ 10 4 identical experiments for a given value of __ . The excited state
corresponds to higher digitizer voltage and the ground state corresponds to lower digitizer
voltage. These data do not have an absolute calibration to qubit state probability, and
such a calibration is not strictly required to extract the information we need about the
qubit frequency, coherence, and pulse coupling. If desired, though, one can perform such a
calibration using the methods described in [44]. The blue lines are fits to a sine wave with
an exponentially decaying envelope in parts (d) and (e), and a fit to a decay exponential in
(f). These data were taken with the paramp on to speed data acquisition.

Rabi oscillations give us a calibration for the pulse duration and amplitude required to make
a pulse that takes _|_ 0 _i_ to _|_ 1 _i_ , called a __ pulse because it corresponds to a rotation of the
Bloch vector by __ .

The decay of Rabi oscillations can also provide a useful probe of qubit dephasing.


Rabi oscillations are an ensemble measurement, and their decay results from noise-induced
variations in the Rabi frequency, which causes individual measurements to have dierent
phases at longer times. We can quantify this eect and relate the Rabi decay envelope to
the qubit relaxation and dephasing times. The expression for the Rabi decay rate  Rabi is
given by [159]:



3 cos 2 __
 Rabi = __


 1 +  __ cos 2 __ + 1  __ sin 2 _,_ (6.3)

2


 1 +  __ cos 2 __ + 1


where  1 = 1 _/T_ 1 ,  __ = 1 _/T_ 2 __ 1 _/_ 2 _T_ 1 is the low-frequency dephasing rate, and  __ =


-----


99

_S_ _!_ _q_ ( Rabi ), where _S_ _!_ _q_ ( _!_ ) is the power spectral density of qubit frequency fluctuations
at frequency _!_ . We can alternately define  __ = _S_ _!_ _q_ ( _!_ _!_ 0). The angle __ is defined in
terms of the Rabi frequency and detuning by cos __ =  _!/_  Rabi and sin __ =  _/_  Rabi .

Depending on the Rabi detuning, one can use the Rabi decay as a probe of the qubit

noise. The envelope of the Rabi oscillations can also change from exponential to Gaussian
depending on the spectrum of the noise; the expression in (6.3) is valid for the case of
exponential decay, where the noise spectrum is not singular at low frequencies [159, 160].

We can also probe the qubit by measuring Ramsey fringes, giving us information

about the qubit frequency and dephasing time _T_ 2 . We send two _/_ 2 pulses to the qubit with
a varying time delay between the pulses, then measure the state of the qubit. We repeat
this experiment many times for each value of the time delay and plot the average measured
qubit state versus time delay. If the frequency of the qubit drive is detuned from the true
qubit frequency, the plot will show oscillations called Ramsey fringes. A typical Ramsey
fringe is shown in Figure 6.12(e). The decay envelope of the Ramsey fringes with delay
time is exponential, with a time constant given by the dephasing time _T_ 2 . The frequency of
oscillations is equal to the detuning between the qubit drive frequency and the true qubit
frequency. Because of this feature, Ramsey fringes are a very precise way to measure the
qubit frequency. We can measure low-frequency fluctuations in the qubit frequency, caused
for example by flux noise, by taking a series of Ramsey fringes to extract the qubit frequency
as a function of time. Ramsey fringes are a more sensitive way to extract the qubit frequency
than Rabi oscillations, since for small detunings the Ramsey frequency depends linearly on
the detuning, while the Rabi frequency has a only a quadratic detuning dependence.

Having calibrated the qubit frequency and the __ pulse amplitude using Rabi and

Ramsey experiments (sometimes applied iteratively to refine the extracted values), we measure the relaxation time _T_ 1 of the qubit. To do this, we prepare the qubit in the excited
state with a __ pulse, wait for a variable amount of time, and then measure the qubit state.
This is repeated many times for each value of the wait time, allowing us to see the ensemble
decay of the qubit state. The excited state population decays exponentially in time with
time constant _T_ 1 , as seen in Figure 6.12(f).

For Rabi, Ramsey, and _T_ 1 experiments, we use curve fitting to extract the coher-

ence parameters of the qubit, the qubit frequency, and the Rabi drive coupling relating the
amplitude of the Rabi drive to the zero-detuning Rabi frequency. These data can in turn
give us information about the coupling of the qubit to its environment and the amount of
environmental noise the qubit sees.

Because the qubit eigenstates of the Jaynes-Cummings Hamiltonian in the dis-

persive regime have a small photonic part, there is a possibility for the qubit to decay by
the emission of its photonic component from the cavity. This phenomenon is known as the
Purcell eect, and sets a limit on the _T_ 1 of a qubit coupled to a cavity. The rate at which
the qubit decays due to the Purcell eect is



 2
__ purc = __ _g_ 2 _._ (6.4)

We can observe this eect experimentally by measuring the _T_ 1 of the qubit as a function of
its detuning from the cavity, thus changing __ purc . The results of such a measurement are


-----


100

|0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||measured T 1 Purcell T 1 Q=11,500 Purcell T plus Q=11,500 1|||||
|||||||



4.0 4.5 5.0 5.5 6.0

Qubit frequency (GHz)

Figure 6.13: Purcell eect.


600
500
400

300

200


100

80
70
60


The red dots show the fitted value of _T_ 1 (see Figure 6.12(f) for a sample fit) as a function
of qubit frequency with _!_ cav = 5 _._ 923 GHz. The dotted blue line gives the theoretical

prediction for the Purcell _T_ 1 from (6.4), the dashed blue line shows a line representing a _Q_
for qubit oscillations of 11,500 due to other loss mechanisms, and the solid blue line shows
the combined eects of these two types of decay.

shown in Figure 6.13. The red dots are measured values of _T_ 1 , while the blue line shows the
expected _T_ 1 based on the Purcell eect in combination with qubit decay from an unknown
additional channel giving a _Q_ of 11,500 for the qubit. This phenomenological limiting _Q_
has been reported in other transmons and is likely due to dielectric loss in the transmon
capacitors [43].

When the readout cavity has multiple modes, the Purcell decay rate becomes more

complicated than the simple expression given above. In general, the presence of higher
cavity modes makes __ purc considerably higher for _!_ _q_ _> !_ cav , while reducing it slightly for
_!_ _q_ _< !_ cav . This multi-mode Purcell eect has been theoretically modeled and agrees well
with experimental measurements including the eects of an intrinsic qubit _Q_ [43]. To avoid
the multi-mode Purcell eect, we make our resonators in a lumped geometry that has no
higher harmonics below 20 GHz.

We can also perform quantum state tomography on the qubit to determine the

location of the qubit state on the Bloch sphere [161]. We prepare a desired state, apply a
rotation of a given angle about a given axis in the x-y plane, and the measure the qubit
state. We repeat this process many times for each of a number of dierent choices of rotation
axis and angle. Each axis/angle pair is equivalent to measuring a dierent projection of the
qubit state (thus the use of the term tomography), so by choosing a variety of axis/angle
combinations we can reconstruct the full density matrix of the measured ensemble 3 . This
technique can be extended to characterize the density matrices of multiple qubits [20, 162]

3 Technically, one need only perform four rotations, such as a _/_ 2 x rotation, a _/_ 2 y rotation, a __ rotation

about either x or y, and an identity (null) rotation, to be able to extract the full density matrix.


-----


101


-1

-2

2

1

0

-1

-2


-1

-2

2

1

0

-1

-2


![SlichterThesis.pdf-119-8.png](SlichterThesis.pdf-119-8.png)

![SlichterThesis.pdf-119-7.png](SlichterThesis.pdf-119-7.png)

![SlichterThesis.pdf-119-0.png](SlichterThesis.pdf-119-0.png)

![SlichterThesis.pdf-119-1.png](SlichterThesis.pdf-119-1.png)

-2 -1 0 1 2
X amplitude ( pulses)

![SlichterThesis.pdf-119-6.png](SlichterThesis.pdf-119-6.png)

![SlichterThesis.pdf-119-3.png](SlichterThesis.pdf-119-3.png)

-2 -1 0 1 2
X amplitude ( pulses)


-2 -1 0 1 2
X amplitude ( pulses) 0.2

![SlichterThesis.pdf-119-9.png](SlichterThesis.pdf-119-9.png)

![SlichterThesis.pdf-119-2.png](SlichterThesis.pdf-119-2.png)

![SlichterThesis.pdf-119-5.png](SlichterThesis.pdf-119-5.png)

![SlichterThesis.pdf-119-4.png](SlichterThesis.pdf-119-4.png)

-2 -1 0 1 2

X amplitude ( pulses)


Figure 6.14: Quantum state tomography.


These four panels show quantum state tomography of a transmon qubit for each of four
quantum states, 0 , 1 , _p_ 1 2 ( 0 + 1 ), and _p_ 1 2 ( 0 + _i_ 1 ). The tomograpy for the two
_|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_ _|_ _i_



( 0 + 1 ), and
2

_|_ _i_ _|_ _i_



( 0 + _i_ 1 ). The tomograpy for the two
2

_|_ _i_ _|_ _i_


eigenstates ( _|_ 0 _i_ and _|_ 1 _i_ ) show no angular dependence, while that for the two superposition
states show strong angular dependence. This angular dependence is a signature of phase
coherence of the prepared superposition states. The extreme values of _P_ ( _|_ 1 _i_ ), the probability
to measure _|_ 1 _i_ after the tomographic rotation, are close to 0 and 1 in all four instances,
showing we can prepare a pure quantum state.


and or of states of the microwave field [82].

Figure 6.14 shows quantum state tomography of a qubit prepared in four dierent

states, the ground state, excited state, and two equal superposition states which dier
by a phase factor of _e_ _i/_ 2 . The horizontal and vertical axes represent the magnitude of
rotation in the x and y axes, respectively, while the color scale indicates the probability
of measuring the qubit in the excited state after the rotation. For the ground and excited
states, the tomography has no angular dependence. Any radial linecut from the center just
shows a Rabi oscillation. For the superposition states, however, there is a strong angular
dependence. We see no radial dependence when rotating around an axis parallel to the
state vector, but we do if we rotate around an axis perpendicular to the state vector. The
two superposition state images show that we can prepare superposition states of arbitrary
and well-defined phase.

###### 6.4.3 ###### Photon number and ac Stark shift

The strength of our measurement depends on the average cavity photon occupation

_n_  . As described in section 2.3.3, we can calibrate this in an elegant way using the ac Stark


-----


102

![SlichterThesis.pdf-120-0.png](SlichterThesis.pdf-120-0.png)

-75 -70 -65 -60 -55 -50 -45 -40

Nominal room temp. readout power (dBm)


(a) (b)


100

10

1

0.1


-40

-45

-50

-55

-60

-65

-70

-75


0.01


![SlichterThesis.pdf-120-2.png](SlichterThesis.pdf-120-2.png)

![SlichterThesis.pdf-120-1.png](SlichterThesis.pdf-120-1.png)

4.80 4.90 5.00 5.10

Qubit spectroscopy frequency (GHz)


Figure 6.15: ac Stark shift and photon number calibration.

Part (a) shows qubit spectroscopy in the presence of readout photons as a function of
readout power. The qubit line shifts in frequency and broadens in response to the ac Stark
shift and associated dephasing. The green circles show the qubit frequencies at each readout
power extracted from curve fits. Part (b) shows the cavity photon occupation  _n_ calculated

from the ac-Stark-shifted frequencies found in part (a). The occasional steps seen in

the photon number are due imperfections in the digital attenuator used to set the readout
power.

shift. The ac Stark shift dictates that the qubit frequency will depend on  _n_ , with the

shift between the qubit frequency in the absence of photons and in the presence of photons
(known as the cavity pull), given by

__ = ( _S_ 1 _S_ 0 ) _n_ + ( _K_ 1 _K_ 0 ) _n_ 2 _,_ (6.5)
__ __

where the _S_ _i_ and _K_ _i_ are described in section 2.3.3. The values of the _S_ _i_ and _K_ _i_ depend on
the transmon _E_ _J_ and _E_ _C_ , as well as the bare cavity frequency _!_ cav and the qubit-cavity
coupling _g_ . All four of these parameters are extracted from spectroscopic data as described
in section 6.4.1.

We can make an experimental measurement of __ using qubit spectroscopy. We

turn on the readout cavity drive, wait several microseconds, and then turn on a weak qubit
spectroscopy pulse lasting for several more microseconds while the cavity drive is still on.
We step the frequency of the qubit spectroscopy and look for dierences between the cavity
responses before and during the spectroscopy pulse. We repeat this for a range of cavity
drive powers set by changing the attenuation of a digital variable attenuator of the type
discussed in section 5.3.2. The digital attenuator enables us to return to a given drive power
in a repeatable fashion.

The resulting spectrum is shown in Figure 6.15(a). The light regions show regions

where the qubit did not respond to the spectroscopy tone, while the dark regions show the


-----


103

regions where it did. As the cavity drive power increases, the qubit line shifts to lower and
lower frequencies and becomes broader. The frequency shift is downward (as oppose to upwards) because the qubit frequency is below that of the cavity for this sample. The increase
in qubit linewidth with increasing readout power is a manifestation of the measurementinduced dephasing of the qubit [42]. We can perform curve fits on the spectroscopy response
at each value of cavity drive power to determine the qubit center frequency and linewidth.
The extracted values of the qubit frequency are overlaid on part (a) as green circles.

We can use equation (6.5) to calculate the value of  _n_ at a given cavity power using

these extracted qubit frequencies. Figure 6.15(b) plots the value of  _n_ found by this method

against the nominal room temperature cavity readout power. As we expect, the signal is
quite linear for small  _n_ , deviating slightly as  _n_ becomes large. This is in keeping with the

expected theoretical relationship between the drive power and the cavity occupation, which
begins to increase nonlinearly for very strong cavity drive [93].

It is important to note that this method for calibrating the photon number is only

useful for calibrating the photon number  _n_ _g_ when the qubit is in the ground state. In

general, the value of  _n_ will depend on the cavity drive frequency and the qubit state as well


as the cavity drive power. If we bias the cavity at a point midway between  _!_ cav ( 0 ) and
_|_ _i_

_!_  cav ( 1 ), however, the photon occupation will be the same in both states for low  _n_ .
_|_ _i_


-----


104

## Chapter 7

# Quantum jumps

This chapter details the experimental observation of quantum jumps in a super-

conducting qubit. We begin by laying out some historical background on the theory and
observation of quantum jumps, then proceed to describe the experimental method. We then
describe the experimental results and provide evidence that we are indeed seeing quantum
jumps of the qubit. The chapter concludes by examining the fidelity of qubit readout using
this technique. This chapter will be concerned primarily with the initial quantum jump
experiments, while details of subsequent quantum jump experiments used to examine measurement non-idealities and the quantum Zeno eect will be presented along with those
data in Chapter 8.

#### 7.1 #### What are quantum jumps?

According to the postulates of quantum mechanics, the act of measurement col-

lapses the state of a quantum system into an eigenstate _|_ _k_ _i_ of the measured observable _A_  :

_A_  _k_ = _a_ _k_ _k_ (7.1)
_|_ _i_ _|_ _i_

_6_


If the measurement is quantum non-demolition, then the state _|_ _i_ of the system immediately
after the measurement is given by system will evolve according to the time-dependent Schr _|_ _i_ = _|_ _k_ _i_ . In the absence of further measurement, the odinger equation _i_ ~ _@_ =  _H_

_6_


_@t_ _@_ =  _H_

_|_ _i_ _|_ _i_

_6_


In many cases (such as in our qubit experiments) the measured observable _A_  is the energy,

_6_


so _|_ _k_ _i_ is an eigenstate of _H_  . In this case, _|_ _i_ will remain unchanged by time evolution

(except for a phase factor).

_6_


so _|_ _k_ _i_ is an eigenstate of _H_  . In this case, _|_ _i_ will remain unchanged by time evolution

_6_


Now consider the case where environmental noise or an applied drive enters as a

perturbation to the Hamiltonian. This perturbation will in general give rise to non-zero
matrix elements between the eigenstates of the unperturbed Hamiltonian, so that the time
evolution of _|_ _i_ is no longer simply a phase factor. In general, we can write that at a time
__ after the measurement,

_6_


( __ ) = _c_ _k_ ( __ ) _k_ +
_|_ _i_ _|_ _i_

_6_


_k_ _0_ = _6_ _k_


_c_ _k_ _0_ ( __ ) _k_ _0_ _,_ (7.2)
_|_ _i_

_6_


-----


105

_6_


where _c_ _k_ _0_ (0) = __ _kk_ _0_ . If we perform a second QND measurement at time __ , we will again
collapse the quantum system to one of its eigenstates. If __ is small, in the sense that

_c_ _k_ ( __ ) _c_ _k_ _0_ ( __ ) for _k_ _0_ = _k_ , then the measurement will collapse the system to _k_ again
_|_ _| |_ _|_ _6_ _|_ _i_
with high probability. We can repeat this process of measuring at time intervals of __ and
will generally get a sequence of results showing collapse to state often (with probability 1 _c_ _k_ ( __ ) 2 per measurement) the system will instead collapse to _|_ _k_ _i_ . However, every so
_|_ _|_
a dierent state _|_ _k_ _0_ _i 6_ = _|_ _k_ _i_ . Repeated measurements will then show state _|_ _k_ _0_ _i_ for a period
of time, until the system is projected to a dierent state again, and so on. When we see a
change between repeated measurements showing _|_ _k_ _i_ and repeated measurements showing
_|_ _k_ _0_ _i_ , we say that a quantum jump has occurred. This is the classic interpretation of quantum
jumps, due to Cook [163].

As seen from this definition, the observation of quantum jumps requires a method

for performing quantum non-demolition measurements on the system in question at a rate
considerably faster than the systems free evolution. The definition given uses discrete measurements at fixed points in time, but in our experiments the measurement is continuous
(in the sense the readout cavity is being continuously irradiated with microwaves). In this
instance, instead of a time between discrete projective measurements, we have a measurement rate  _m_ at which information about the qubit state can be determined [50]. The
measurement time can be taken to be 1 _/_  _m_ and then the quantum jump formulation for
discrete measurements applies [91].

#### 7.2 #### Historical background

This notion that quantum systems evolve instantaneously by jumping between

eigenstates was first proposed by Bohr in 1913 [26]. For three quarters of a century, the
concept of quantum jumps remained a purely theoretical curiosity, and a subject of substantial debate. Schr odinger wrote a lengthy piece denying their existence in 1952, com-

menting that the notion of monitoring the state of a single quantum particle was ludicrous
and that quantum jumps are the modern equivalent of epicycles, fudge factors used by
the Greeks to reconcile astronomical observations of retrograde planetary motion with the
geocentric theory of the universe [164, 165]. By the early 1980s, though, advances in atomic
physics allowed for the trapping and cooling of single ions [27, 28], raising the possibility
that the question of quantum jumps might be settled experimentally. A few years later, in
1986, three groups simultaneously reported the observation of quantum jumps between the
electronic states of individual trapped ions [29, 30, 31]. Since that time, quantum jumps
have been observed in a variety of other systems, beginning with the electronic states of
single terrylene molecules embedded in a crystal [32]. Single electrons in cyclotron orbits
are seen to undergo quantum jumps between Landau levels [33], and single microwave photons are suddenly created and annihilated by thermal processes inside a Fabry-Perot cavity

[34]. In solid state systems, quantum jumps have been observed in a microscopic defect in a
Josephson junction [35], while more recently, work showed that the state of a single nuclear
spin in a diamond NV center undergoes quantum jumps [36], as does the electronic state
of an electron in an indium gallium arsenide quantum dot [37]. Quantum jumps from spin
flips of a single trapped proton in a magnetic field were reported recently as well, paving


-----


106

the way for precision test of matter-antimatter asymmetry [38].

All of these experiments observed quantum jumps in microscopic quantum degrees

of freedom (single atoms, molecules, electrons, protons, or photons) with long ( __ ms to s)
relaxation times, both in isolation and as part of a larger solid state system. The paper
of Yu _et al._ claims that their quantum jumps are of the qubit-TLS system, and thus are
macroscopic quantum jumps [35]. However, we maintain that their observed jumps must be
attributed purely to the microscopic TLS defect (or to some other unknown mechanism),
with the qubit functioning solely as a measurement apparatus, for several reasons. First, the
observation of quantum jumps requires multiple QND measurements of the quantum system
under study before it changes state. In the work by Yu _et al._ , measurements were made
every 10 ms, while they report a qubit _T_ 1 of 600 ns. Secondly, their measurement technique
is not QND because it causes the phase qubit to transition to the voltage state 1 with each
measurement, at which point there is no qubit anymore. Since the measurement completely
destroys the phase qubit, it cannot hold quantum information between measurements, so
any quantum state information must be held solely in the TLS defect. Finally, the reported
quantum jump lifetimes are of the order of seconds, much longer than those any reported
superconducting qubit. The jumping dynamics observed by Yu _et al._ must be purely those
of the TLS defect (or of some other part of the experiment), with the phase qubit serving
merely as a readout element.

The work presented in this chapter represents the first observation of quantum

jumps in a superconducting qubit, which a macroscopic quantum system [62]. It provides
a further confirmation of the quantum nature of superconducting qubits, which had been
shown previously through entanglement and violation of Bells inequality [18, 19, 20, 21, 22,
23, 166]. Our readout method gives the ability to monitor continuously with high fidelity
to observe single-shot qubit dynamics. Because the relaxation time of superconducting

qubits is much shorter ( __ __ s) than that of the other systems in which jumps have been
observed, the experiment relies crucially on the high bandwidth and quantum-limited noise
performance of the paramp.

#### 7.3 #### Experimental design

Quantum jumps occur whenever strong projective measurements are performed

at a rate much faster than the natural evolution dynamics of the qubit state. In circuit
QED, quantum jumps occur from the action of the readout photons in the cavity (given
a sufficient number of photons  _n_ and a nonzero dispersive shift 2 __ ). The readout photons

become strongly entangled with the qubit state; if we then measure the phase of the photons,
the qubit state also collapses to the corresponding eigenstate. The difficulty in observing
these jumps comes because the number of readout photons is necessarily small, so the signal
is drowned by the noise added in the amplification chain. The solution to this problem is the
introduction of the superconducting parametric amplifier (paramp) described in Chapters
3 and 6, which lowers the noise temperature of the amplification chain enough to enable
continuous high-fidelity readout. No matter the qubit or readout cavity design, all of the
quantum jump experiments in this thesis make use of a paramp for this purpose.

1 For a detailed explanation of this phase qubit readout method, see refs. [48] and [71].


-----


107

The basic experimental setup (on which a few variations will be discussed in this

and later chapters) is shown in Figure 7.1. The key ingredients are a qubit coupled to a
readout cavity in a circuit QED architecture and a paramp to amplify the readout signal.
This particular setup was used for the initial quantum jump experiments. We implement the
readout cavity as a quasi-lumped-element linear resonator consisting of a meander inductor
of L = 1.25 nH (orange) in parallel with finger capacitors of C = 575 fF (blue) [167]. We
chose this design over the traditional transmission line resonators used in most circuit QED
experiments to this point for several reasons. First, the lumped element cavity doesnt have
higher harmonic modes and so should not suer from the multi-mode Purcell eect [43],
where higher cavity modes cause additional qubit relaxation. Second, the smaller footprint
of the lumped-element cavity allows more cavities to be placed on a single chip, which may
help with scaling up to multi-cavity designs. The qubit is a transmon (described in detail in
section 2.1.3 and in [13]) which is capacitively coupled to the cavity; the qubit parameters
at the operating point are _E_ _J_ = 11 _._ 4 GHz and _E_ _C_ = 280 MHz, with a qubit frequency of
4.753 GHz. The coupling strength between the qubit and the cavity is _g/_ 2 __ = 109 MHz.
The cavity has a bare resonant frequency _!_ cav = 5 _._ 923 GHz with a linewidth _/_ 2 __ = 4 _._ 9
MHz. For this experiment, the dispersive shift 2 _/_ 2 __ = 4 _._ 4 MHz. Since 2 __ __ __ , there will
be about a 180 __ phase shift between the reflected readout cavity signals corresponding to
the two qubit states. We use the ac Stark shift for a multilevel qubit to calibrate the cavity
photon occupation, as described in sections 2.3.3 and 6.4.3.

The experiment proceeds as shown by the arrows in the figure. Readout photons

at 5.932 GHz from the input port are directed through a circulator into the readout cavity,
where they interact with the qubit and acquire a phase shift depending on the qubit state.
The readout photons then leave the cavity and travel to the paramp through a series of
three circulators, which isolate the readout cavity and qubit from the strong pump tone
used the bias the paramp to its gain point 2 . The readout photons then combine with

the paramp pump, also at 5.932 GHz, which enters through the -20 dB weakly coupled
port of a directional coupler. We adjust the phase of the pump beforehand so that the
readout photons and pump interfere either constructively or destructively, depending on
the phase shift of the readout photons (and thus on the qubit state). Since the readout
photons corresponding to the two qubit states are about 180 __ phase shifted from each
other, this interference between readout signal and pump results in a modulation of the
pump amplitude and thus a large phase modulation of the reflected pump, as described in
section 3.4.3. By mapping the readout phase shift signal (carried by a few photons) onto
the phase shift of the reflected pump (carried by hundreds of photons), we have eectively
amplified the readout signal (specifically, this realizes a phase-sensitive amplification as
described in Chapter 3). The amplified signal is reflected out of the paramp and directed
through a circulator to further cryogenic and room temperature amplification stages. The
amplified signal is then mixed down to zero frequency (converting the phase shift signal
into a quadrature voltage signal) and digitized. By shifting the relative phase of the local
oscillator, we can put the entire readout signal into one quadrature. Experimental details

2 The pump power is about -90 to -95 dBm at the paramp, so three circulators (each with about 20 dB of

isolation) will reduce the pump leakage to about -150 dBm at the readout cavity, a power which corresponds
to a cavity occupation of roughly 0.01 photons. This power is too small to aect the qubit in any significant
way.


-----


108

![SlichterThesis.pdf-126-2.png](SlichterThesis.pdf-126-2.png)

![SlichterThesis.pdf-126-0.png](SlichterThesis.pdf-126-0.png)

![SlichterThesis.pdf-126-1.png](SlichterThesis.pdf-126-1.png)

Figure 7.1: Base temperature apparatus.


![SlichterThesis.pdf-126-3.png](SlichterThesis.pdf-126-3.png)

![SlichterThesis.pdf-126-4.png](SlichterThesis.pdf-126-4.png)

Readout cavity


Readout photons enter the from the input port (black arrow) and are directed through a
circulator into the readout cavity, where they interact with the qubit and acquire a phase
shift that depends on the qubit state. Upon leaving the cavity, the readout photons (purple
arrows), now carrying information about the qubit state in their phase, travel through three
microwave circulators, which isolate the qubit from the strong pump tone used to bias the
paramp. The readout photons combine with the paramp pump (green arrow) which enters
from the weakly coupled port of a directional coupler and interact in the parametric amplifier
so that the phase of the readout photons is encoded in the phase of the reflected pump tone
which forms the output signal (red arrow). Since the pump has many more photons than
the initial readout signal, this eects an amplification of the readout signal. The output
is directed on to further cryogenic and room-temperature amplification stages (not shown)
and then is mixed down to zero frequency (converting the phase shift signal into a voltage
signal) and digitized. Both the readout cavity and paramp are excited using Bollywood
180 __ hybrids, which turn the single-ended input signals into dierential ones. The false
color images show the qubit/cavity sample in the upper left and the paramp sample in the
lower right. The cavity consists of a meander inductor (orange) shunted by an interdigital
capacitor (blue); input signals are coupled in through the interdigital capacitors at the top
and bottom. The transmon qubit (yellow) is capacitively coupled to the cavity. The inset
view shows the qubit loop. The paramp sample consists of a SQUID loop (pink) with

Josephson junctions (black) shunted by two capacitors in series formed by Al top layers
(cyan) on a Nb ground plane (brown) coated with SiN _x_ dielectric.


-----


109

|||
|---|---|


![SlichterThesis.pdf-127-0.png](SlichterThesis.pdf-127-0.png)

Figure 7.2: Overview of experimental setup.


paramp

pump


paramp


qubit

excitation


qubit


pulse

shaping


pulse


readout

generator


readout


Qubit and readout pulses are formed by mixing the output of microwave generators with
pulse envelope shapes made by an arbitrary waveform generator. The readout power is set
using a variable attenuator, and both qubit and readout pulses are combined and sent to
the INPUT port of the experiment by a heavily attenuated input line. The paramp pump
is supplied to the DRIVE port from a separate generator. After interacting with the qubit
(see Figure 7.1), the amplified signal from the paramp leaves the OUTPUT port, is further
amplified by a cryogenic HEMT and low-noise room-temperature microwave amplifiers, and
is then mixed down to zero frequency with an IQ mixer. A phase shifter is used to adjust
relative phase and put the information all in one quadrature of the mixer output. The
mixer output is amplified, low-pass filtered at 11 MHz, and digitized at 100 MS/s.

are in Chapter 5, while details of the amplification mechanism are presented in Chapter 3.
Fully detailed diagrams of the experimental setup can be found in Appendix C.

#### 7.4 #### Observation of quantum jumps

Using this experimental apparatus, we can look at individual time traces of the

mixed-down voltage signal and see quantum jumps of the qubit state. In these traces,

dierent dc voltage levels correspond to dierent phases of the readout signal, which in
turn correspond to dierent qubit states. We prepare the qubit in either the excited state
or ground state before the readout turns on by applying an appropriate microwave pulse, as
shown in Figure 7.3(a) 3 . In this instance, we prepared two traces in the excited state with


3 Before these pulses are applied, the qubit is initialized in the thermal ground state (which is _|_ 0 _i_ to a

good approximation since ~ _!_ _q_ __ _k_ _B_ _T_ ) by letting it equilibrate for a period of 50 or 100 __ s, much longer
than the qubit _T_ 1 .


-----


110


###### (a) ###### (,2) ###### (b)


(,2)


0.8

0.4

0.0

-0.4

|Col1|1 ||
|---|---|
||0 ||


![SlichterThesis.pdf-128-0.png](SlichterThesis.pdf-128-0.png)

![SlichterThesis.pdf-128-1.png](SlichterThesis.pdf-128-1.png)

![SlichterThesis.pdf-128-2.png](SlichterThesis.pdf-128-2.png)

![SlichterThesis.pdf-128-3.png](SlichterThesis.pdf-128-3.png)

-150 -100 -50 0 50 100

_t_ (ns)


200 400 600 800

_t_ (ns)


200 400 600 800


Figure 7.3: Individual measurement traces.

Part (a) shows the timing diagram for the data traces in (b). The qubit is prepared in
either the excited or ground state with a __ pulse or a 2 __ pulse, respectively (red). The
readout is then energized (black) and the internal cavity amplitude (purple) rises, eecting
a measurement. We select time _t_ = 0 to be two cavity time constants after the readout is
first energized. Part (b) shows three individual time traces, two prepared with a __ pulse
(red and green) and one prepared with a 2 __ pulse (blue). Data points are recorded every
10 ns. When the readout turns on (grey background), the excited state and ground state
traces separate and settle to dierent voltages. As the measurement continues, the excited
state traces decay stochastically to the ground state with an abrupt quantum jump. The
qubit states are easily resolved from each other at all times during readout.

a __ pulse (red and green) and one in the ground state with a 2 __ pulse (blue). Figure 7.3(b)
shows what happens during the subsequent readout. When the readout is o, the voltage
is the same level for all state preparations (this level is not quite 0 V, due to osets in the
mixer and its following amplifiers). However, as the readout turns on (grey background), the
ground and excited state traces separate to the point where they can be clearly distinguished
at any given time point (data points are taken every 10 ns). The dotted line in the figure
shows a discrimination threshold for determining the state of the qubit based on statistics
from many traces. As we know from ensemble measurements, the qubit will relax from
the excited state to the ground state with a characteristic time constant _T_ 1 . However, the
continuous measurement forces the qubit to remain in an energy eigenstate. As a result,
the qubit transitions stochastically to the ground state with an abrupt quantum jump, as
can be seen in the red and green traces in Figure 7.3(b). No jump is evident in the blue
trace because it began in the ground state.

There are many possible things which may cause a measurement trace to jump

between two stable states in an experiment. For example, the paramp is bistable for some
bias values, a fact utilized for bifurcation readout in the past [46]. To ensure that the jumps
we are seeing are truly quantum jumps of the qubit, we must perform some checks. The


-----


111

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||||-0.5 0 0.5 1.0 Digitizer voltage (V)|||||
|||||||||||


![SlichterThesis.pdf-129-5.png](SlichterThesis.pdf-129-5.png)

![SlichterThesis.pdf-129-4.png](SlichterThesis.pdf-129-4.png)

![SlichterThesis.pdf-129-3.png](SlichterThesis.pdf-129-3.png)

![SlichterThesis.pdf-129-2.png](SlichterThesis.pdf-129-2.png)

![SlichterThesis.pdf-129-6.png](SlichterThesis.pdf-129-6.png)

![SlichterThesis.pdf-129-1.png](SlichterThesis.pdf-129-1.png)

200 400 600 800 1000

Time (ns)


(a) (b)


2

3/2



/2


0.4

0.2

0.0

-0.2


![SlichterThesis.pdf-129-0.png](SlichterThesis.pdf-129-0.png)

Qubit pulse amplitude ( pulses)


Figure 7.4: Jumps with varied state preparation.

Part (a) shows Rabi oscillations of the qubit as a function of the qubit excitation pulse
amplitude. The data plotted are the average voltages of 10 4 traces in the 10 ns interval
starting at _t_ = 40 ns (as defined in Fig. 7.3(a)), where fidelity was optimal. Part (b)

shows a color plot of 30 individual time traces for each of 5 initial qubit state preparations,
corresponding to the circled points in (a). The white color represents the excited state,
while the blue indicates ground state. After a __ pulse, the qubit is primarily in the excited
state at the start of the readout and jumps down stochastically in time. After no pulse
or a 2 __ pulse, the qubit starts out in the ground state and stays there. Preparations of
equal excited and ground state populations with a _/_ 2 or 3 _/_ 2 pulse show some traces in
the excited state and some in the ground state at the start of the readout, in a fraction
about midway between the 0 pulse and __ pulse populations. The observed dwell times in
the excited state are independent of state preparation.

simplest check is to prepare the qubit in dierent states to see if the measurement trace
is correlated appropriately to the state preparation. Figure 7.4 shows data from such a
test, where we prepared the qubit with pulses varying between 0 and __ 5 __ . In part (a), we
sweep the amplitude of the qubit excitation pulse and measure the average voltage across
10 4 traces for a 10 ns interval where the readout fidelity is maximized. This average voltage
signal undergoes Rabi oscillations between ground and excited states as the excitation power
is increased; this tends to rule out the idea that the qubit excitation pulse itself is causing
the jumps. Part (b) shows a color plot of 30 individual time traces (running horizontally)
for each of the five bias points circled in part (a); blue represents low voltage and white
high voltage. We find that the trace voltages correlate with the prepared qubit state;


when preparing _|_ 0 _i_ (either with no pulse or with a 2 __ pulse), we see blue at the start of
measurement, while preparing _|_ 1 _i_ gives us mostly white at the start. When we prepare an
equal superposition of _|_ 0 _i_ and _|_ 1 _i_ , we see both blue and white in similar proportions.

There are a few details to note about this figure. First, even when we prepare


-----


112

_|_ 1 _i_ with a __ pulse, we measure _|_ 0 _i_ (blue) at the start of the traces a fair amount of the
time. This loss of fidelity is due to the qubit relaxing before the readout can ring up, and
will be discussed in more detail in section 7.5. We see the same eect after a _/_ 2 pulse;
here, the fraction of traces measured as _|_ 1 _i_ (white) at the start of the readout is somewhat
below half, and is about halfway between what we get when preparing _|_ 0 _i_ and _|_ 1 _i_ . A second
important feature is that the typical high and low voltages measured after a _/_ 2 pulse are
the same as for other state preparations; only the fraction of traces showing high voltage
versus low voltage changes. This means that the oscillations in average voltage seen in part
(a) are due to changes in the fraction of traces showing high versus low voltage ( _|_ 0 _i_ versus
_|_ 1 _i_ ), not due to changes in the typical readout voltage levels. Finally, the typical lifetime
of the excited state traces before decay appears to be independent of the qubit preparation
pulse, as expected if the jumps represent _T_ 1 decay of the qubit. We will examine the decay
times in more detail shortly.

To see the robustly bimodal nature of the readout voltages more clearly, we can


histogram many individual time traces. Figure 7.5 shows histograms of voltage versus


time; each panel represents 2 __ 10 4 individual traces for a given qubit state preparation.
The voltage signal is well separated once the readout has rung up, and we can identify a
threshold voltage for distinguishing between ground and excited states that is independent
of qubit state preparation. Since the histogram represents many identical trials of the same
experiment, we can talk about an ensemble qubit population in this instance. The excited
state population decreases in time but remains at the same mean voltage, indicating that
the individual traces decay with discrete jumps from _|_ 1 _i_ to _|_ 0 _i_ rather than slowly evolving
to _|_ 0 _i_ . We can also see the initial ground and excited state populations are correlated


appropriately to the prepared qubit state. Finally, we see a small but noticeable excited
state population at large times and when preparing the ground state. This is simply a
steady-state thermal population of the qubit.


We have successfully checked that the jumps we observe are between two dierent

voltages which are independent of qubit state preparation, but that the fraction of traces
observed at a given voltage is well correlated to the qubit state preparation. This suggests
that the jumps are indeed due to the qubit. However, we should also check that the

jumps occur at appropriate times. Individual quantum jumps happen stochastically, but
the distribution of times at which they occur is well understood [168]. For jumps from decay
events, the time _t_ jump when each jump occurs follows an exponential distribution with the
time constant given by the qubit _T_ 1 4 .

We can find _t_ jump for each data trace by detecting when the voltage goes below

the _t_ jump _|_ 0 for 2 _i_ _/_ _|_ 1 _i_ discrimination threshold. In Figure 7.6(a), we histogram the extracted values of __ 10 4 traces. The times follow an exponential distribution with time constant
__ jump = 310 ns, which is within the fitting error of the independently measured qubit
_T_ 1 of 320 ns. This correspondence again strongly suggests that the jumps we are seeing
are those of the qubit. In part (b) of the figure, we show a 3D version of Figure 7.5(c),
highlighting the exponential decay of the excited state population (nearer peak) with time,
and the corresponding growth of the ground state population (far peak). The excited

4 For very strong measurement, the time constant may be dierent due to the quantum Zeno eect, which

we will discuss in the next chapter


-----


113

![SlichterThesis.pdf-131-6.png](SlichterThesis.pdf-131-6.png)

![SlichterThesis.pdf-131-1.png](SlichterThesis.pdf-131-1.png)

200 400 600 800

_t_ (ns)

![SlichterThesis.pdf-131-4.png](SlichterThesis.pdf-131-4.png)

![SlichterThesis.pdf-131-3.png](SlichterThesis.pdf-131-3.png)

200 400 600 800


(a) 1.0 (b)


(a) 1.0 (b)


1.0

0.5

0.0

-0.5

-1.0

1.0

0.5

0.0

-0.5

-1.0


0.5

0.0

-0.5

-1.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||0 80 Count||||||
|||||||||
||||||||0 80 Count|
|||||||||


![SlichterThesis.pdf-131-7.png](SlichterThesis.pdf-131-7.png)

![SlichterThesis.pdf-131-0.png](SlichterThesis.pdf-131-0.png)

200 400 600 800

_t_ (ns)



0.5

0.0

-0.5

-1.0


![SlichterThesis.pdf-131-5.png](SlichterThesis.pdf-131-5.png)

![SlichterThesis.pdf-131-2.png](SlichterThesis.pdf-131-2.png)

200 400 600 800


_t_ (ns) _t_ (ns)

Figure 7.5: Histograms of many individual traces.

These color plots show histograms of the readout signal voltage as a function of time for
2 __ 10 4 individual readout traces. The four panels correspond to four dierent qubit state
preparations; (a) no pulse, (b) _/_ 2 pulse, (c) __ pulse, and (d) 2 __ pulse. We can draw a clean
discrimination threshold (dotted white line) between ground and excited state voltages. The
relative fraction of traces in ground versus excited states depends on the state preparation.
As we go farther into the readout, the excited state population decays back to the ground
state with quantum jumps, reflected in the unchanging mean voltages but changing weights
of the ground and excited state parts of the histogram. The grayed-out region shows

the voltage transients during qubit excitation and readout ring-up, before we consider the
readout to be on at _t_ = 0 ns.

state population, as measured by the histogram weight at voltages above the discrimination
threshold, decays exponentially with a time constant of __ = 290 ns, which again correlates
well with both __ jump and _T_ 1 .

We make a brief comment here on determination of decay time constants. For

the data in Figure 7.6(a), we did a least-squares fit of a curve to a histogram. This is
an acceptable way to estimate the decay time constant, but note that for such a fit to be
correct one must weight each bin by its standard deviation (given by the square root of
the bin occupation). However, this method is not optimal because it uses coarse histogram
bins, rather than the more fine-grained information about individual jump times which
we have access to. A more robust and accurate way of estimating a parameter such as a


-----


114


(a) (b)

2000 Voltage


(a) (b)


1500

1000

500


![SlichterThesis.pdf-132-0.png](SlichterThesis.pdf-132-0.png)

250 500 750 1000 1250

| =310 ns jump|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


_t_ jump (ns)


![SlichterThesis.pdf-132-4.png](SlichterThesis.pdf-132-4.png)

![SlichterThesis.pdf-132-1.png](SlichterThesis.pdf-132-1.png)

Figure 7.6: Jump times and population decay.

In part (a), we show a histogram of values of _t_ jump extracted from 2 __ 10 4 traces prepared
with a __ pulse. Fitting the decay times to an exponential distribution (blue line) yields a
time constant __ jump = 310 ns. This is within fitting error of the independently measured
qubit _T_ 1 of 320 ns. Part (b) shows the data from Figure 7.5(c) as a 3D plot, allowing us to
see more clearly the exponential decay of the excited state population and corresponding
rise in ground state population with time.



0.4

0.2

0.0

-0.2

-0.4

-0.6

![SlichterThesis.pdf-132-2.png](SlichterThesis.pdf-132-2.png)

-2 0 2 4 6 8 10

Time (s)


![SlichterThesis.pdf-132-6.png](SlichterThesis.pdf-132-6.png)

qubit

|bit|Col2|
|---|---|
|||
|dout||



-3 0 3 6 9 12

Time (s)


![SlichterThesis.pdf-132-5.png](SlichterThesis.pdf-132-5.png)

![SlichterThesis.pdf-132-3.png](SlichterThesis.pdf-132-3.png)

-2 0 2 4 6 8 10

Time (s)


-2 0 2 4 6 8 10


Figure 7.7: Jumps with simultaneous readout and excitation.

Part (a) shows a timing diagram with simultaneous readout and qubit excitation. Part (b)
shows 60 individual time traces. The qubit is usually in the ground state when the qubit
excitation tone is o, and then jumps stochastically back and forth between ground and
excited states when the excitation tone is on. Once the excitation turns oagain at 8 __ s,
we see essentially no more jumps up to the excited state. Part (c) shows one individual
time trace with repeated jumps between ground and excited states.


-----


115

decay constant is to use maximum likelihood estimation, which will be discussed in the next
chapter. The maximum likelihood estimate for __ jump is 296 ns, again consistent with the
measured qubit _T_ 1 . Maximum likelihood estimation will be described in detail in the next
chapter.

Finally, we can look at quantum jumps in the presence of a simultaneous qubit

excitation tone (we set the frequency of this tone to the appropriately ac-Stark-shifted qubit
frequency). The qubit excitation should cause the qubit state to evolve in time, but the
measurement pins the qubit in an eigenstate. Under these two competing influences, we
expect the qubit to jump back and forth between the ground and excited states. This

is just what we see experimentally, as shown in Figure 7.7. With just the readout tone
on initially, the qubit is primarily in the ground state (with the occasional jump visible).
However, when the qubit excitation tone is on as well, we see frequent jumps back and
forth between the ground and excited states. With very weak measurement, we would

see Rabi oscillations of the qubit if we averaged many of these traces together. However,
because of the strong measurement the qubit is rapidly dephased and the up/down jumps
from multiple traces do not average together to give Rabi oscillations. This transition from
smooth qubit state evolution to jump-like evolution has been seen in ensemble measurements
in the frequency domain by the Saclay group [23], and we have reproduced these results.
As the measurement grows stronger, causing a transition to the jumping regime, it actually
inhibits qubit evolution, a phenomenon known as the quantum Zeno eect [169]. We show
measurements of the quantum Zeno eect in the next chapter.

###### 7.4.1 ###### Jumps without a paramp

The jumps we observe correlate well with the qubit state preparation and excited


state lifetime, suggesting that they are indeed quantum jumps of the qubit. However, since
we know that the paramp can also exhibit bistability, it would be nice to see quantum
jumps without the paramp present. This is quite difficult to do, as the noise performance
of the HEMT amplifier is much worse than that of the paramp. However, we were able to
reduce the system noise temperature to 7 K by using a Nb coaxial cable to transmit the
output signal between the mixing chamber plate and the 4 K plate (details are in Chapter
5). With this reduced noise temperature, we could look for jumps both with and without
the paramp in the circuit.

Data from this experiment 5 are shown in Figure 7.8. We turn on the readout and

apply a __ pulse to the qubit (at the ac-Stark-shifted qubit frequency) after a 3 __ s delay, as
shown in part (a). We did this for a strong measurement power,  _n_ = 60, both (b) with the

paramp on and (c) with the paramp oand switched out of the circuit. While the data
without the paramp are much noisier, one can see that both data sets look similar. With
the readout on, there is some spurious excited state population at all times (more details
in Chapter 8). When the __ pulse occurs, a majority of the traces show a transition to the
excited state, with subsequent relaxation to the ground state (the __ pulse efficiency is low
due to the strong measurement). The ground and excited state populations as a function

5 These data we obtained with a dierent qubit sample (TF021111d) than the data in the previous section.

This sample has a transmission-mode cavity (so qubit pulses are filtered by the cavity and do not impinge
on the paramp) and a longer _T_ 1 of 1.27 __ s.


-----


116



200


With paramp (c) Without paramp


200

150

100

50


(a)

qubit

![SlichterThesis.pdf-134-0.png](SlichterThesis.pdf-134-0.png)

![SlichterThesis.pdf-134-1.png](SlichterThesis.pdf-134-1.png)

3 s


150

100

50

|Col1|With paramp|Col3|Col4|Col5|
|---|---|---|---|---|
||Digitizer voltage|||Digitizer voltage|
||||||
||||||
||||||
||||||

|Col1|Without paramp|Col3|Col4|p|
|---|---|---|---|---|
||Digitizer voltage|||Digitizer voltage|
||||||
||||||
||||||
||||||


![SlichterThesis.pdf-134-4.png](SlichterThesis.pdf-134-4.png)

![SlichterThesis.pdf-134-5.png](SlichterThesis.pdf-134-5.png)

![SlichterThesis.pdf-134-3.png](SlichterThesis.pdf-134-3.png)

![SlichterThesis.pdf-134-2.png](SlichterThesis.pdf-134-2.png)

Time (s)


Time (s)


Figure 7.8: Quantum jumps with and without paramp.

Part (a) shows the timing diagram for parts (b) and (c); the readout is turned on, and
the qubit is excited with a __ pulse at the ac-Stark-shifted qubit frequency 3 __ s into the
readout. Parts (b) and (c) show 200 individual time traces with readout power  _n_ = 60; part

(b) shows data taken using the paramp, while the data in (c) we taken with the paramp o
and removed from the circuit. The jump timescales and behavior in (c) are commensurate
with those in (b), albeit with considerably more noise.

of time, as well as the excited state lifetimes, appear to be commensurate between the two
data sets. We conclude that the jumps are not due to the presence of the paramp, but that
the paramp merely serves to improve our noise performance.

###### 7.4.2 ###### Three-level jumps

Our quantum jump readout allows us to distinguish between ground and excited


states, but the must take into account that the transmon qubit is really a multilevel system.
We can attempt to make measurements to distinguish between _|_ 0 _i_ , _|_ 1 _i_ , and _|_ 2 _i_ , which can
work because the low anharmonicity of the transmon means that the qubit-state-dependent
cavity frequencies  _!_ cav ( 0 ),  _!_ cav ( 1 ), and  _!_ cav ( 2 ) are roughly evenly spaced. If we choose
_|_ _i_ _|_ _i_ _|_ _i_


our readout frequency to be _!_ ro _!_  cav ( 1 ), we should be able to see three dierent phase
__ _|_ _i_ 6


shifts, corresponding to the three dierent qubit states 6 . Such a measurement would let us
observe the qubit dynamics outside the _{|_ 0 _i_ _,_ _|_ 1 _i}_ subspace. It would also be another strong
piece of evidence that these really are quantum jumps of the qubit and not a spurious
experimental bistability, since we would see tristable as well as bistable readout traces.


Figure 7.9(a) shows three individual time traces 7 from a measurement with simul-


6 Note that for the measurements discussed earlier in this chapter, we have chosen a readout frequency


fairly close to  _!_ cav ( 0 ).

7 These data we obtained with qubit sample TF042811b. _|_ _i_


-----


117

(a) (b)


1.5

1.0

0.5

0.0

-0.5

-1.0


100

80

60

40

20


![SlichterThesis.pdf-135-0.png](SlichterThesis.pdf-135-0.png)

![SlichterThesis.pdf-135-1.png](SlichterThesis.pdf-135-1.png)

8 10 12 14 16

Time (s)


-1.0 -0.5 0.0 0.5 1.0 1.5

Digitizer Voltage (V)


Figure 7.9: Three-level jumps.

Part (a) shows three individual time traces from a measurement with simultaneous strong
driving of the 0 _!_ 1 transition. The signal exhibits three stable voltages, corresponding
to the qubit states _|_ 0 _i_ , _|_ 1 _i_ , and _|_ 2 _i_ , with clear discrimination thresholds. Most relaxation
events occur one level at a time, with the qubit stepping down the energy ladder. Part
(b) shows a histogram of the voltages of 10 4 individual time traces at all time points, again
showing the tristability of the readout signal and the discrimination thresholds.

taneous strong driving of the 0 _!_ 1 transition. The traces jump back and forth between
three stable levels, corresponding to the qubit states state is populated due to spurious transitions arising from measurement non-idealities (more details _|_ 0 _i_ , _|_ 1 _i_ , and _|_ 2 _i_ . The _|_ 2 _i_
in Chapter 8). We can verify which voltage corresponds to each state by preparing the
qubit state in one of the three states before the readout with either no pulse, a pulse at
_!_ 01 , or a pulse at _!_ 02 _/_ 2, and noting the voltage when the readout turns on. We observe
that the decay transitions tend to occur stepwise, going one level at a time. In part (b),
we histogram the voltages for all time points across 10 4 of these traces. The histogram
clearly shows the three stable voltage levels, as well as discrimination thresholds for state
determination.

When operating the paramp in phase sensitive mode, we can rotate the phase

of the pump generator to change the phase of the amplified signal quadrature. In this

experiment, there are three dierent readout pointer states depending on the state of the
qubit. By simply varying the quadrature we amplify, we can change the output signal

so that it distinguishes between _|_ 0 _i_ and _{|_ 1 _i_ _,_ _|_ 2 _i}_ or individually between _|_ 0 _i_ , _|_ 1 _i_ ,and _|_ 2 _i_ .
Figure 7.10(a) shows a cartoon of this process, where each qubit state corresponds to one
of three complex readout amplitudes __ _|_ 0 _i_ , __ _|_ 1 _i_ , and __ _|_ 2 _i_ . The signal into the paramp is just
the projection of these complex amplitudes onto the amplified quadrature of the paramp.
Two example quadratures are shown, one which distinguishes all three states and another
which just distinguishes two.

Even though the paramp is in the saturated regime, we can choose a bias point so

that the middle of the three readout states (corresponding to _|_ 1 _i_ in the data shown above)
is right on the steep part of the paramp transfer function, with the other two readout
states are on the two saturated ends of the transfer function. This configuration is shown
schematically in Figure 7.10(b). In this way, we can make a continuous three-state detector,


-----


118

Pump power


+90


![SlichterThesis.pdf-136-1.png](SlichterThesis.pdf-136-1.png)

![SlichterThesis.pdf-136-3.png](SlichterThesis.pdf-136-3.png)

-90


![SlichterThesis.pdf-136-2.png](SlichterThesis.pdf-136-2.png)


![SlichterThesis.pdf-136-0.png](SlichterThesis.pdf-136-0.png)

quadrature


Input signal

(quadrature projection amplitude)

|Q (a)|Col2|
|---|---|
|(a) Q|I 2-state quadr 3-state paramp|
|||


Figure 7.10: Paramp biasing for three-level jumps.


Part (a) shows the complex amplitudes __ 0 , __ 1 , and __ 2 of the readout pointer states in
_|_ _i_ _|_ _i_ _|_ _i_
the IQ plane. The projection of these states onto the amplified quadrature of the paramp is
dierent depending on the quadrature chosen; one can choose this quadrature to distinguish
between either _|_ 0 _i_ and _{|_ 1 _i_ _,_ _|_ 2 _i}_ or between all three states individually. The paramp

quadratures are shown displaced from the origin for clarity. Part (b) shows the paramp
transfer function, whose output, shown in red, can distinguish between three input values,
shown in blue, even in the saturated regime. To distinguish the three inputs efficiently,
the middle value to be amplified should be biased near the middle of the paramp transfer
function.

at the expense of the signal-to-noise ratio for discriminating between states _|_ 0 _i_ and _|_ 1 _i_ . If
all we care about is whether the qubit is in the ground state or an excited state, we can
usually improve our state discrimination by operation in the two-state rather than threestate regime.

#### 7.5 #### Signal-to-noise ratio and fidelity

Having established that the jumps we see are indeed quantum jumps of the qubit,

we can now try to quantify how well our technique lets us know the qubit state. We can
look at two figures of merit for our measurement technique. The first is our ability to

discriminate between the readout pointer states at a given time point, which we refer to as
the signal-to-noise ratio (SNR). The second is our ability to prepare the qubit in a desired
state and then obtain a measurement result corresponding to that state, which we refer to
as the single-shot fidelity _F_ . The SNR obviously enters into the fidelity; if we are unable to
distinguish between our two readout pointer states, we will be unable to measure the qubit
state reliably.

If the SNR is poor enough to be the main limit on fidelity (as is the case in typical

circuit QED experiments), averaging in time will improve fidelity, but only until we reach
the limits set by _T_ 1 decay or errors in qubit state preparation [94]. In our quantum jump


-----


119

experiments, the SNR is sufficiently high that the ability to distinguish between readout
pointer states should not be the limiting factor on our total fidelity. We will describe this
in more detail in section 7.5.3.

###### 7.5.1 ###### Theoretical SNR

We now present calculations of the expected SNR for resolving readout pointer

states. The signal depends on the dierence between the two coherent states coming from
the readout cavity corresponding to the two qubit states. To extract the signal, we need
to know the amplitude of these states and the angle between them. The noise comes from
standard noise theory as detailed in Chapter 3.


For a readout cavity with an average photon occupation  _n_ res when driven on

resonance, the power radiating out of the cavity is given by _P_ rad =  _n_ res ~ _!_ , where _!_ is the


readout frequency and __ is the cavity linewidth. When the cavity is driven in the reflection
geometry, the steady state incident power is the same as the steady state reflected power
which forms the output. This output power is _P_ out = _P_ rad _/_ 4, where the factor of four arises
due to the interference between the incident and radiated signals [135]. Assuming that the
internal loss of the cavity is small (in the sense that _Q_ int __ _Q_ ext ), _P_ out is actually the same
at all bias frequencies, not just the resonance frequency. This power corresponds to a peak
voltage amplitude 2 _V_ out _,_ r through the relation _|_ _V_ out _,_ r _|_ = _p_ 2 _p_ 50 _P_ out , where we have used the


fact that _P_ = _V_ 2


rms 2 _/R_ , and that the amplitude of a sinusoidal signal is


2 _p_ 50 _P_ out , where we have used the


2 times its RMS


value. Substituting for _P_ out gives


_V_ out _,_ r =
_|_ _|_


25 _n_ res ~ _!._ (7.3)


Depending on the qubit state, this output voltage will have one of two phases. The readout
signal changes between two points in the IQ plane corresponding to these two phases with
the given amplitude _V_ out _,_ r . Thus the peak amplitude of the readout signal is given by half
_|_ _|_
the vector dierence between _V_ out _,_ r with one phase and _V_ out _,_ r with the other phase. We can
calculate the magnitude of this vector dierence, giving


_V_ sig _,_ _r_ = _V_ out _,_ r sin
_|_ _|_ _|_ _|_



__ = 1

2 2



_V_ out _,_ r
2 _|_


2 __ 2 cos _,_ (7.4)


where the _r_ subscript indicates reflection geometry. This result is derived from simple

trigonometric arguments. We can substitute in the expression in (7.3) to give:


_V_ sig _,_ _r_ =
_|_ _|_


12 _._ 5 __ _n_  res ~ _!_ (1 __ cos __ ) _._ (7.5)


The signal is maximized for __ = __ , which is achieved when the dispersive shift 2 __ is equal
to __ , with the readout frequency set halfway between  _!_ cav ( 0 ) and  _!_ cav ( 1 ). The signal at
_|_ _i_ _|_ _i_

this optimal bias point is


The signal is maximized for __ = __ , which is achieved when the dispersive shift 2 __ is equal
to __ , with the readout frequency set halfway between  _!_ cav ( 0 ) and  _!_ cav ( 1 ). The signal at
_|_ _i_ _|_ _i_


_V_ sig _,_ _r_ =
_|_ _|_


25 _n_ res ~ _!._ (7.6)


Having solved for the signal in reflection geometry, we turn to an asymmetric transmission
geometry with the signal exiting from the strongly coupled port. With the same caveat of
low internal cavity loss, we find that the power radiated from the cavity is again _P_ rad =


-----


120


(a)



_V_ out _V_ _e_

|Q|V out|
|---|---|
|||
|||
|| V out|


![SlichterThesis.pdf-138-0.png](SlichterThesis.pdf-138-0.png)

![SlichterThesis.pdf-138-1.png](SlichterThesis.pdf-138-1.png)

Figure 7.11: Readout signal cartoon.

The signal to the paramp in reflection (a) and transmission (b) geometries is determined
by the vector dierence between the two pointer states in the IQ plane. The amplitudes of
these pointer states are given by equations (7.3), (7.7), and (7.8). The signal amplitude is
half the peak-to-peak excursion, and thus half of the vector dierence between the pointer
states.

_n_  ~ _!_ . However, in transmission there is no interference between incoming and outgoing
waves, so _P_ rad = _P_ out . Furthermore, _P_ rad depends on  _n_ , which decreases as we move away

from the cavity resonance frequency (assuming a fixed cavity drive power). This means that
both the phase and amplitude of the output signal may change depending on the qubit state.
In analogy with equation (7.3), we can write the peak voltage amplitudes corresponding to
the ground and excited states as


100 _n_ _g_ ~ _!_ (7.7)

100 _n_ _e_ ~ _!,_ (7.8)


_V_ _g,t_ =
_|_ _|_


_V_ _e,t_ =
_|_ _|_


where  _n_ _g_ and  _n_ _e_ are the ground and excited state cavity photon occupations, respectively.


The output signal is again half of the vector dierence between _V_ _g,t_ and _V_ _e,t_ in the IQ plane.
Using the law of cosines, we can express the signal amplitude as



1
_V_ sig _,_ _t_ =
_|_ _|_


_V_ _g,t_ 2 + _V_ _e,t_ 2 2 _V_ _g,t_ _V_ _e,t_ cos _,_ (7.9)
_|_ _|_ _|_ _|_ __ _|_ _||_ _|_


where here the _t_ subscript indicates transmission geometry. If we substitute in the results
from equations (7.7) and (7.8), this becomes


25 __ ~ _!_ ( _n_ _g_ +  _n_ _e_ __ 2 _n_  _g_ _n_  _e_ cos __ ) _._ (7.10)

__ = _/_ 2, corresponding to p __ = 2 __ and readout


_V_ sig _,_ _t_ =
_|_ _|_


We find that this signal is maximized when __ = _/_ 2, corresponding to __ = 2 __ and readout
frequency midway between  _!_ cav ( 0 ) and  _!_ cav ( 1 ). These are the same parameters for which
_|_ _i_ _|_ _i_


the signal was maximized in reflection geometry 8 . At this bias point,  _n_ _g_ =  _n_ _e_ = 1


2 _n_  res . If


8 It is not immediately evident that equation (7.10) is maximized for __ = _/_ 2, but arises because  _n_ _g_ and

_n_  _e_ are not independent of __ . However, it should not be surprising that the same relation between __ and __
gives the maximum signal for both reflection and transmission. The proof is left as an exercise to the reader.
Hint: draw pictures in the IQ plane.


-----


121

we substitute in this relationship, equation(7.10) reduces to


_V_ sig _,_ _t_ =
_|_ _|_


25 _n_ res ~ _!,_ (7.11)


which is exactly the same result for maximum signal in the reflection case given in equation
(7.6). We see that in both transmission and reflection, the output signal is maximized when
2 __ = __ ; this is why we aim for this regime with our sample bias parameters.

Having derived expressions for the signal, we now examine the noise. The intrinsic


noise floor is set by quantum fluctuations and can be expressed as a noise temperature
_T_ _Q_ = ~ _!/_ 2 _k_ _B_ . The corresponding voltage noise is given by _V_ _Q_ = 50 _k_ _B_ _T_ _Q_ _B_ , where _B_ is

the noise bandwidth. The noise bandwidth is set by our integration time; the longer we

p

average the readout signal, the lower the noise bandwidth and thus the lower the noise. In
practice, _B_ is eectively given by the bandwidth of the filters on the demodulated signal (see
section 5.3.3). However, the paramp bandwidth also plays a role, because the noise on the
output signal consists primarily of amplified paramp output noise. If the paramp bandwidth
is smaller than the demod filter bandwidth, then _B_ will depend on both 9 . When setting _B_
to minimize noise, we must also consider the bandwidth of our desired signal, which is given
by the cavity amplitude response rate _/_ 2. If we make _B_ larger than the signal bandwidth,
we introduce unnecessary noise, while if we make _B_ smaller we will begin to lose signal 10 .

If our amplification chain has a system noise temperature _T_ sys , then the eective

voltage noise referred to the input of the chain is given by


_V_ sys =


50 _k_ _B_ ( _T_ _Q_ + _T_ sys ) _B,_ (7.12)


combining both the intrinsic quantum noise and the noise added by amplification. We

can now derive the theoretically expected signal-to-noise ratio. In the case of noiseless

amplification (paramp in phase-sensitive mode), we have _T_ sys = 0. If we maximize the signal
(which involves both having __ = 2 __ and choosing the amplified quadrature of the paramp
appropriately), its amplitude is given by the expressions in equations (7.6) and (7.11). We
then calculate the maximum achievable signal to noise ratio given a noise bandwidth _B_ :


SNR max = _V_ sig _/V_ sys =


25 _n_ res ~ _!/_ 50 _k_ _B_ ( ~ _!/_ 2 _k_ _B_ ) _B_ =


_n_  res _/B ._ (7.13)


This is a pleasing result; the maximum SNR is just the square root of the photon flux out of
the cavity on resonance divided by the noise bandwidth (which depends on the integration
time). We can also derive expressions for the SNR in reflection or transmission for arbitrary
__ and  _n_ (assuming noiseless amplification) using (7.5), (7.10), and (7.12):


SNR _r_ =


_n_  res __ (1 cos __ ) _/_ 2 _B_ (7.14)
__


__ ( _n_ _g_ +  _n_ _e_ __ 2 _n_  _g_ _n_  _e_ cos __ ) _/B ._ (7.15)

p


SNR _t_ =


9 Ref. [95] gives methods for calculating _B_ given the demod filter and/or paramp frequency response.


10 In this section, we assume that the signal and noise are filtered with a boxcar frequency response. The

question of optimal filtering of the readout signal to give maximum information about the qubit state is
complex, and will be considered further in section 7.5.3.


-----


122


![SlichterThesis.pdf-140-0.png](SlichterThesis.pdf-140-0.png)

|2|2  g| e|
|---|---|---|


 _g_  _e_


Figure 7.12: Readout SNR.

The black circles are a voltage histogram of 2 __ 10 4 readout traces at _t_ = 200 ns, taken
from a linecut of Figure 7.5(c). The blue and red curves are Gaussian fits to the ground
and excited state peaks, respectively. The means ( __ _g_ _, _ _e_ ) and standard deviations ( __ _g_ _, _ _e_ )
of each fit are shown. The data are slightly above the fits in the region around V=0.25 V;
this eect is due to traces making a transition between excited and ground states.

As would be expected, increasing the cavity photon occupation makes the SNR go up,
as does decreasing the noise bandwidth (increasing the integration time). One should be
careful to note that __ is an angular frequency, while _B_ is not. For the qubit described in
section 7.3, measured in reflection with _/_ 2 __ = 4 _._ 9 MHz, __ = 155 __ and _B_ __ 15 MHz 11 , we
get a theoretical maximum SNR 1 _._ 4 _p_ _n_  res .
__

###### 7.5.2 ###### Experimental measurements of SNR

The SNR can be improved by increasing  _n_ res , but in practice higher order eects

start to reduce the dispersive shift [93] and cause qubit state mixing (see Chapter 8 for
details), setting a practical upper bound on  _n_ res for our measurement. In our initial exper-

iment, we used a maximum photon occupation of  _n_ res = 47. For this level of excitation, we


compute an optimal SNR __ 9 _._ 6.


We can compare this number with the SNR we achieve experimentally. Figure


7.12 shows a voltage histogram of 2 __ 10 4 individual traces for  _n_ res = 47; the data are


from a vertical linecut of Figure 7.5 (c) at _t_ = 200 ns. There are two clearly resolved peaks,
corresponding to the qubit in ground (negative voltage) and excited (positive voltage) states.
We can fit each peak to a Gaussian function (blue and red lines) and extract the means
( __ _g_ _, _ _e_ ) and standard deviations ( __ _g_ _, _ _e_ ) for each fit. Note that the widths of the two peaks
are dierent because the paramp is not linear for this high level of excitation. We define
the measured SNR as


SNR meas = _|_ __ _g_ __ __ _e_ _|_ _/_ ( __ _g_ + __ _e_ ) _._ (7.16)

This definition of SNR is consistent with the analytical expressions given in the previous

11 This value of the noise bandwidth was determined from the frequency response of the filter on the

demodulated signal, as well as the bandwidth of the paramp.


-----


123


section 12 . For the data shown SNR meas 3 _._ 75, a factor of 2.6 smaller than the ideal
__


case. This implies that 8 K and the added noise is not zero. Nevertheless, this is an improvement of more than an order of magnitude in noise temperature _T_ sys __ 5 _._ 6 _T_ _Q_ = 0 _._
over a typical state-of-the-art microwave amplification chain using cryogenic semiconductor amplifiers, where _T_ sys 10 30 K. The experimental parameters give a signal power
__ __
_P_ out =  _n_ res ~ _!/_ 4 = __ 118 _._ 5 dBm. The extracted value of _T_ sys is commensurate with the


values measured for similar paramp input powers as presented in Chapter 6.


For the data in Figure 7.12, the paramp is deeply in the saturated regime. In

the linear regime, the output SNR grows linearly with the input SNR from the cavity; the
output signal grows, while the output noise stays constant. When the paramp saturates, the
amplitude of the output signal no longer grows with increasing input signal amplitude. Input
noise continues to be amplified, although the noise gain decreases gradually as the paramp
moves farther into the saturated regime. As a result, the output SNR plateaus and grows
only sub-linearly with increasing input SNR; the output signal is fixed, while the output
noise is slowly decreasing. Thus when the paramp is deeply saturated, the output SNR
will be considerably lower than the input SNR. This is another way of understanding the
increase in paramp noise temperature in the saturated regime (see discussions in Chapters
3 and 6). It is important to note, however, that the output SNR is still a monotonically
increasing function of input SNR, so that operation in the saturated regime is advantageous
for maximizing readout fidelity. Improving the dynamic range of the paramp will prevent
saturation and should allow further improvements in SNR.

###### 7.5.3 ###### Measurement fidelity

Having determined our experimentally achieved SNR, we turn to the examine our

overall qubit measurement fidelity. We prepare the qubit in either the ground or the excited
state and then measure its state. By taking a number of measurements, we can find an
ensemble probability to measure the qubit in the ground state when it was prepared in
the excited state, denoted _P_ ( _s_ 0 _|_ _q_ _|_ 1 _i_ ), and a corresponding probability _P_ ( _s_ 1 _|_ _q_ _|_ 0 _i_ ) to measure
excited state when the qubit was prepared in the ground state. The total fidelity is defined
by subtracting these errors:

_F_ = 1 __ _P_ ( _s_ 0 _|_ _q_ _|_ 1 _i_ ) __ _P_ ( _s_ 1 _|_ _q_ _|_ 0 _i_ ) (7.17)

These probabilities are determined by the probability of the qubit actually being in the
desired state _|_ _i_ _i_ when measured, which we term the state-specific process fidelity _F_ _|_ _i_ _i_ , and
our ability to determine the qubit state from the readout signal, which we call the readout
efficiency __ ro . _F_ _i_ depends on the quality of our ground state initialization and qubit gates,
_|_ _i_
as well as on qubit excitation and decay rates and the delay time between state preparation
and readout; the theoretical expression has a complicated form. The circuit QED readout
method has been shown experimentally to map the qubit state to the phase of the readout
signal with unit efficiency [44], in which case the readout efficiency is just our ability to
distinguish between the two states of the readout signal at a given time point. This is

12 We checked that these definitions are consistent by creating simulated noisy readout traces (with signal

and noise amplitudes as given by the expressions in the previous section) and extracting SNR meas .


-----


124


determined by the SNR, and for the definition of SNR given in the preceding sections is
__ ro = erf(SNR _/_ _p_ 2) [94]. This formula implicitly assumes an eective signal averaging time

of 1 _/B_ , where _B_ is the noise bandwidth that enters into the SNR. Because __ ro is so high
in our experiment (almost always above 95% and typically above 99%), and because the
_T_ 1 of our qubit is relatively short, averaging further in time does not improve the overall
fidelity. The eects on readout fidelity of averaging or filtering a continuous readout signal
have been studied carefully by Gambetta and co-workers in the Yale group [94]. They set
limits on the achievable fidelity for a given signal-to-noise ratio and qubit decay time. The
reader is cautioned that they define their signal-to-noise ratio _r_ _sn_ dierently from how we
define our SNR. The conversion is given by _r_ _sn_ = _T_ 1 _B_ (SNR) 2 in the case of simple average
filtering (the relation is more complex or even not analytical in the case of other filters).
Our experimental value SNR meas = 3 _._ 75 given in the previous section translates to a value
_r_ _sn_ = 45 for the signal-to-noise ratio definition in [94].

For the qubit sample presented in this chapter, our single-shot fidelity was around

70%, which is within the error bars of the theoretically predicted value. The 30% fidelity loss
is almost entirely due to _T_ 1 decay. Using a dierent sample 13 with longer _T_ 1 = 910 ns and

_n_  = 80 photons, we achieved our best single-shot fidelity of 81 __ 2%, which agrees well with
the theoretically predicted value of 82 __ 3%. The individual error probabilities for equation
(7.17) are found experimentally to be _P_ ex ( _s_ 0 _|_ _q_ _|_ 1 _i_ ) = 0 _._ 17 __ 0 _._ 02 and _P_ ex ( _s_ 1 _|_ _q_ _|_ 0 _i_ ) = 0 _._ 015 __
0 _._ 004. These numbers are very close to the theoretically predicted values _P_ th ( _s_ 0 _|_ _q_ _|_ 1 _i_ ) =
0 _._ 16 __ 0 _._ 03 and _P_ th ( _s_ 1 _|_ _q_ _|_ 0 _i_ ) = 0 _._ 018 __ 0 _._ 01. The loss of fidelity (both theoretically and
experimentally) is primarily due to _T_ 1 decay and to the thermal excited state population of
the qubit. The good agreement between theoretical and experimental fidelity values means
that our assumption of perfect mapping between qubit state and readout photon state is
reasonable.

Although these fidelity numbers are not quite as high as some achieved in other

superconducting systems [47, 48], the fidelity as quoted above does not fully capture the
power of our measurement technique. The switching phase qubit readout [48] has better
than 90% fidelity and is very rapid (readout takes a few ns). However, the readout is

not QND because the qubit junction switches to the voltage state if state _|_ 1 _i_ is measured,
thereby destroying the qubit. The latching bifurcation readout used in [47] is QND and
has 86% fidelity (which can be increased to 92% with the use of an additional shelving
qubit state), but measurements can only be made once every 250 ns. This is too slow to
resolve quantum jumps when the qubit lifetime is of order __ 1 __ s. In addition, use of the
shelving state to increase fidelity takes the qubit out of the _{|_ 0 _i_ _,_ _|_ 1 _i}_ manifold and so
continuous qubit dynamics cannot be observed.

In contrast, our ability to determine the qubit state when the readout is on is

limited only by __ ro and the rate _/_ 2 at which the readout signal amplitude responds to
changes in the qubit state. We can perform continuous monitoring of the qubit state with
error rates in qubit state determination at any given point in time of around 2-4%, depending
on averaging and readout strength. This enables studies of qubit dynamics (such as those
presented in this chapter and the next) which are not possible using the other readout
methods described in the previous paragraph.

13 Sample TF042811b: see Chapter 4.


-----


125

Since our fidelity is essentially set by _T_ 1 decay between state preparation and

readout, we could improve the fidelity by reducing this delay time and/or increasing _T_ 1 .
It is possible to prepare transmon qubit states with better than 99% efficiency [76, 170],
and the recent development of transmon qubits with very long lifetimes [17] should reduce
losses from decay. Using optimized state preparation pulses with a qubit with _T_ 1 = 10 __ s,
we expect a fidelity above 95% given the same pulse timing and SNR as were used in the
experiments above.


-----


126

## Chapter 8

# Measurement backaction

With the ability to perform continuous monitoring and see quantum jumps, we

have a powerful tool for probing the dynamics of our qubit. As with all things quantum,
the act of measurement is bound to aect the system under study. This chapter looks

at the backaction of the circuit QED measurement technique. We first present a method
for efficient automated analysis of individual qubit measurement traces, and then use this
method to study the behavior of the qubit during measurement. We observe and describe
two forms of measurement backaction, spurious qubit state mixing and the quantum Zeno
eect.

#### 8.1 #### Automated qubit state extraction

The techniques for continuous monitoring of the qubit state presented in the pre-

vious chapter let us observe the dynamics of the qubit with high accuracy in a single time
trace. We can now study ensemble behavior (for example decay times, as shown in Figure
7.6) by extracting the behavior in individual time traces and looking at ensemble statistics
of the extracted parameters. This allows us to see eects and quantify behavior in ways
which are much harder or impossible to do using the traditional method of averaging together many time traces and then extracting parameters from the average. However, the
disadvantage of this ability to extract the qubit dynamics from individual time traces is
that we need to save and process tens of thousands of individual time traces, rather than
just a single averaged time trace, at each experimental bias point.

With data sets of many gigabytes for typical experiments, we need a reliable

automated method for analyzing individual time traces and determining ensemble behavior
of interest. We devised a suitable algorithm to determine the qubit state as a function of
time during a measurement trace, noting when jumps occur and how long the qubit remains
in each state before jumping. The algorithm also aggregates this information over many
traces with identical experimental parameters and determines ensemble qubit behavior such
as excited state population and excitation and decay rates. With only a small amount ( __
10 parameters) of human input at the very beginning of operation, the extraction algorithm
can run unattended for days and achieve accurate results processing tens of gigabytes of
data over a wide range of experimental parameters. The algorithm currently only works for


-----


127

analyzing jumps between two qubit states. It could be extended to analyze jumps between
three states (for data such as that shown in section 7.4.2), but because of the substantial
work involved this capability has not been implemented yet.

###### 8.1.1 ###### Determining the qubit state

The first task, from which all others follow, is the extraction of the qubit state as

a function of time in each individual measurement trace. We accomplish this by removing
noise in a controlled way to boost the SNR, then performing level detection to determine
the initial state and the positions of all transitions between states.

The noise power in the signal is determined by the noise bandwidth _B_ , typically


set by the 10-15 MHz cutofrequencies of the filters between the demod box and the Alazar
card (see section 5.3.3). The value of _B_ sets the SNR as described in the previous chapter.
However, the qubit usually remains in a given state longer than 1 _/B_ , suggesting that we
can filter the recorded signal in software to further reduce _B_ and improve our SNR without
losing too much information about the qubit state. For an automated system, we need to
have an algorithmic way of determining the optimal level of filtering for a given data set.

For each set of time traces (usually 10 4 traces, recorded over a period of about 0.1-1

sec, and corresponding to one particular experimental bias point), we histogram the voltages
of all the data points during readout (typically __ 10 7 total points) 1 . We then smooth the
histogram slightly and take its derivative, using the zero-crossings to find the locations of
the two peaks corresponding to ground and excited state voltages, as well as the location of
the minimum between them, which serves as the state discrimination threshold 2 . The height
of this minimum is an indicator of the SNR; lower height indicates that the peaks are better
resolved. To optimize the SNR, we apply a filter to the individual time traces, repeat this
histogram/derivative procedure, and find the height of the minimum again. If the minimum
is decreased relative to what it was before the last round of filtering, we have improved the
SNR. We can repeat this procedure until the SNR is no longer improved (i.e. the inter-peak
minimum is no longer decreased) by additional filtering, at which point we have determined
the optimal filtering. Further filtering (overfiltering) means that the noise bandwidth _B_
has become low enough that we are losing substantial signal information. We show three
sample histogramsunfiltered, optimally filtered, and overfilteredin Figure 8.1.

There are several ways one could perform this filtering. Because we have a great

deal of data to process, fast execution time is important, so we filter using a simple, speedy
boxcar smoothing function (a moving average) [171]. The boxcar width can be chosen as
desired at the start of extraction. The algorithm uses successive applications of the boxcar
smoothing function at each iteration, so that optimizing the SNR means optimizing the
number of passes of boxcar smoothing applied to the raw data traces. One could in principle

1 Raw data traces typically have dead spots at the beginning and end, before the readout has turned on

and after it has turned o. We use only data taken while the readout is on in our automated analysis. We
specify the data range of interest by giving the algorithm turn-on and turn-otimes for the readout signal,
which are chosen to be consistent throughout a given experiment.

2 For traces with initially poor SNR, the two peaks may overlap so much that there is no minimum

between them, especially if one peak is much higher than the other. In this case, the algorithm performs its
iterative filtering until a minimum appears, or until a maximum number of filtering operations is reached.
Once the minimum appears, the algorithm proceeds as described.


-----


128


**(a)** **(b)** **(c)**

350


**(a)** **(b)** **(c)**


500

400

300

200

100

0

![SlichterThesis.pdf-146-1.png](SlichterThesis.pdf-146-1.png)

-2.0 -1.0 0.0 1.0

Digitizer voltage (V)


800

600

400

200

0

![SlichterThesis.pdf-146-2.png](SlichterThesis.pdf-146-2.png)

-2.0 -1.0 0.0 1.0

Digitizer voltage (V)


300

250

200

150

100

50

0

![SlichterThesis.pdf-146-0.png](SlichterThesis.pdf-146-0.png)

-2.0


-1.0 0.0 1.0

Digitizer voltage (V)


Figure 8.1: Optimal smoothing of time traces.

We show histograms of 10 7 data points from 10 4 traces at a given experimental bias point.
Part (a) shows a histogram of the original data, with a measured SNR of 2.1. Part (b)
is a histogram of the same data after the individual traces have been optimally smoothed.
The measured SNR has now increased to 3.4. Part (c) shows the eects of oversmoothing.
There are now a number of data points which do not fall into either of the Gaussian peaks;
these points correspond to state transitions which have been smeared out in time by the
smoothing process. Because of this smearing, our ability to estimate the transition times
(and to see short-duration dwell events in a given state) is degraded.


Figure 8.1: Optimal smoothing of time traces.


use any form of filtering, for example a software Chebyshev or Butterworth filter with a
variable cutofrequency. In this case, finding the optimal filtering would amount to finding
the filter cutofrequency and/or order which maximizes SNR. However, performance testing
of the automatic extraction algorithm show that it produces quite accurate results using
just simple boxcar smoothing (details are given in section 8.1.4).

We note that any filtering process will remove some signal information as well.

The boxcar smoothing described above hurts our ability to resolve jumps with very short
duration because the filtering has removed the high-frequency components of the signal 3 .
Because such missed events are short, their absence has little eect on our determination
of ensemble qubit population. We have to be more careful of this phenomenon when estimating transition rates, but the methods described in section 8.1.2 compensate for missed
short events.

Once we have performed our optimal smoothing, we need to determine a voltage

threshold for discriminating between the qubit states. Rather than one threshold, we use
two dierent thresholds with hysteretic Schmitt trigger behavior [172]. This method

allows us to eliminate spurious event counts caused by noise on the individual traces as
they pass through the threshold. To choose our thresholds, we perform Gaussian fits on
the histogram to determine the means __ _h_ and __ _l_ and standard deviations __ _h_ and __ _l_ of
the high and low voltage peaks respectively. We also calculate the signal to noise ratio

3 The cavity linewidth __ sets a limit on our ability to see very fast qubit dynamics, but added filtering

can exacerbate this eect.


-----


129

|id|Col2|Col3|
|---|---|---|
||||
||||
||||



Time



V _h_

V _mid_

V _l_

|(a) counts 2 Histogram l  l|voltage 2 Digitizer h  h|
|---|---|


V _l_ V _mid_ V _h_

Digitizer voltage

Figure 8.2: Hysteretic data thresholding.

Part (a) shows a cartoon histogram of the voltages in a data set (grey bars) with Gaussian
fits to the high and low voltage peaks (red and blue lines). The means and standard deviations __ _h_ and __ _l_ of the fits are shown. We choose the hysteretic threshold voltages __ _h_ and __ _l_
_V_ as described in the text. Part (b) shows a cartoon of a trace being analyzed using the hysteretic thresholding method. State changes (blue circles) are only registered for _h_ and _V_ _l_
upward transitions through _V_ _h_ from the low-voltage state or downward transitions through
_V_ _l_ from the high-voltage state. This method rejects spurious level-crossings of _V_ _mid_ which
do not reach the appropriate hysteretic threshold.


SNR = ( of the midpoint voltage __ _h_ __ __ _l_ ) _/_ ( __ _h_ + __ _V_ _l_ ), as in section 7.5.2. The two thresholds _mid_ = ( __ _h_ + __ _l_ ) _/_ 2 at voltages given by _V_ _V_ _h,l_ _h_ = and _V_ _mid_ _V_ _l_ sit on either side __ _h,l_ 2 _/_ ( __ _h_ __ _l_ ).
__ __


_h,l_ 2 _/_ ( __ _h_ __ _l_ ).

__


These thresholds are shown schematically in Figure 8.2(a). The data are taken in such a
way that __ _h_ __ _l_ , so we can write these thresholds approximately as _V_ _mid_ __ _h,l_ _/_ (2 SNR),
__ __ __
which gives some intuition as to the choice; for an SNR of 1 we choose thresholds midway
between _V_ _mid_ and the __ _h,l_ , with the width of the hysteretic region diminishing as SNR
improves. Unlike the method described in [172], we do not perform iterative analysis to
refine these thresholds, but simply use the initial starting values. Empirically, this has not
degraded the algorithms performance.


The optimal smoothing and threshold determination steps are performed anew

with each set of time traces to be analyzed. This is done because slow phase drifts in

the paramp pump can cause the voltage levels to drift up and down with time; they are
constant over the __ 1 second interval to take a given data set, but separate data sets taken
several minutes apart can have mean levels sufficiently dierent to aect the analysis. In
addition, changing experimental bias parameters may cause the qubit to jump up and down
at very dierent rates or change the intrinsic SNR, both of which can aect the optimal
number of smoothing operations. As a result, redoing the optimal smoothing and threshold
determinations for each data set greatly improves the robustness of the state extraction
algorithm.


-----


130

With thresholds established, we can now proceed to determine the state of the

qubit as a function of time during each individual time trace. We use the nomenclature _s_ _hi_
and _s_ _lo_ to refer to the voltage state of the signal, with up meaning a transition from _s_ _lo_
to _s_ _hi_ and down meaning a transition in the opposite direction. The algorithm deals only
with _s_ _hi_ and _s_ _lo_ ; the experimenter must note which voltage state ( _s_ _hi_ or _s_ _lo_ ) corresponds
to which qubit state ( _|_ 0 _i_ or _|_ 1 _i_ ). This mapping is usually obvious from the data. All the
data for a given experiment are taken with the same mapping between the voltage state
and qubit state to avoid confusion.

The algorithm records the voltage state as a function of time during each trace, as

well as the durations of all dwell periods in _s_ _lo_ and _s_ _hi_ . The first step is to determine the
initial state of the qubit in the readout trace. Starting from _t_ = 0 at the beginning of the
trace, we look for the first level crossing of _V_ _mid_ and find the mean voltage of the data points
up until that first crossing. If the mean is above _V_ _mid_ , the initial state is _s_ _hi_ , if below, its
_s_ _lo_ . We then go back to the start of the trace and look for transitions through the hysteretic
thresholds, as shown in Figure 8.2(b). If the initial state is _s_ _lo_ , we look for upward-rising
level crossings of _V_ _h_ , while for _s_ _hi_ we look for downward-falling level crossings of _V_ _l_ . If a
crossing is found, we note the dwell time since the last state change, change the current
state in the extracted time record appropriately, and then repeat the process of looking for
level crossings. This continues until the end of the measurement trace is reached. In some
cases, there are many transitions during a readout trace, while in others there may be none
at all. Either way, for every trace one dwell time is cut short by the end of the readout.
We record these dwell times but mark them as censored [173]. We can use such censored
data points in our extraction of qubit transition rates, but we must handle them dierently
from non-censored data, as will be described in section 8.1.3.

Figure 8.3 shows the performance of the state extraction algorithm for 100 individ-

ual time traces. The left panel shows the raw input data, the middle panel shows the same
data after optimal smoothing, and the right panel shows the extracted qubit state. The
extracted state trace accurately reproduces the features visible in the raw data, although it
occasionally misses events with short dwell times. The raw SNR of the data shown is 2.1.

As can be seen (and will be quantified in section 8.1.4), this method for extracting

the qubit state works very well. We should mention that there are a number of other

methods for extracting state information from noisy telegraph signals such as our jump
data. One of our collaborators has successfully used hidden Markov models [174] to perform
state extraction with low-SNR tunneling data from quantum dots [175]. This work shows
the hidden Markov method to be more accurate in extracting rates than non-hysteretic
thresholding and cumulative sum testing [176] (another popular jump-finding algorithm),
but the advantage over level-finding disappears for data with reasonable SNR. Another
option related to cumulative sum testing is edge detection [177], which finds transitions
in a data set and can be used when the mean voltages for _s_ _hi_ and _s_ _lo_ vary significantly
within a given data set. These other methods are all more computationally intensive and
algorithmically complex than the hysteretic level-finding described above, so we chose not
to pursue them in light of the already high accuracy of the simple method.


-----


131

|Col1|shi slo Extracted state|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||


![SlichterThesis.pdf-149-4.png](SlichterThesis.pdf-149-4.png)

4 6 8 10

Time (s)


(a) (b) (c)


100


100


![SlichterThesis.pdf-149-3.png](SlichterThesis.pdf-149-3.png)

![SlichterThesis.pdf-149-1.png](SlichterThesis.pdf-149-1.png)

80

60

40

20


80

60

40

20


100

80

60

40

20

|Col1|-2 -1 0 1 2 Dig. voltage (V)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||

|Col1|-1 0 1 Dig. voltage (V)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||


![SlichterThesis.pdf-149-0.png](SlichterThesis.pdf-149-0.png)

![SlichterThesis.pdf-149-2.png](SlichterThesis.pdf-149-2.png)

10


10


Time (s)


Time (s)


Figure 8.3: Automated qubit state determination.

Panel (a) shows the raw data from 100 individual time traces with an SNR of 2.1. Panel (b)
shows the same data after optimal smoothing, which has increased the SNR to 3.4. Panel
(c) shows the qubit state as determined by the automated state extraction algorithm. The
extracted state traces accurately reproduce the behavior seen in the raw data. These data
are from the same data set used to make the histograms in Figure 8.1.

###### 8.1.2 ###### Jump time distribution

The decay events of a qubit are exponentially distributed in time with a time

constant _T_ 1 (alternatively, we can parameterize the distribution in terms of a decay rate
 1 = 1 _/T_ 1 ). In an ensemble of exponentially distributed decay times, most decays occur at
short times, with fewer and fewer occurring in a given interval as time progresses. However,
in our extracted data we see very few decays at short times. This is a result of the limited
bandwidth of the experiment _B_ det , set by the readout cavity linewidth __ , the paramp
bandwidth, and the filtering and smoothing of the demodulated readout signal. The readout
signal shows little or no response to events where the qubit jumps and then jumps back in
a time less than 1 _/B_ det , and we dont detect them with our extraction algorithm. On its
__
face, this does not seem to be a problem for estimating the decay rate  1 ; we might just
simply fit the events we do observe to an exponential and get our answer.

The problem here is a subtle one. Imagine we have two dwell times __ 1 and __ 3 in

_s_ _lo_ , separated by a dwell __ 2 in _s_ _hi_ so short that the readout signal does not register it. What
were actually two dwell times in _s_ _lo_ of length __ 1 and __ 3 are seen in the readout record as a
single dwell time of length __ 1 + __ 2 + __ 3 . This spurious combining of separate events skews
the distribution of observed dwell times to longer times. The overall statistics may still look
reasonably exponential, but an exponential fit will give us a time constant longer than the
true one. The fractional error in the estimated time constant can be as much as 20-30% for
our experimental parameters.

A solution to this problem for a Poissonian two level system (such as a qubit) was

developed by Naaman and Aumentado [178]. They create a model of the qubit and readout


-----


132



|A*|Col2|B*|
|---|---|---|
|A B||A B|
||||
||||


Figure 8.4: State diagram for finite bandwidth detection.

This figure shows a system state diagram for finite bandwidth detection. The qubit is in
either state _A_ or _B_ (circles), while the readout is in state _A_ __ or _B_ __ . For each qubit/readout
state, the likelihood of transitioning to a dierent qubit/readout state is determined by the
rates  _A_ ,  _B_ , and  det as indicated. Adapted from ref. [178].

where the states of the the qubit (denoted _A_ and _B_ ) are allowed to be independent of the
states of the readout (denoted _A_ __ and _B_ __ ). A diagram of this model, adapted from their
paper, is shown in Figure 8.4. For each readout state, the qubit can be in either state _A_ or
_B_ . Transitions occur between _A_ and _B_ with rates  _A_ and  _B_ . However, when the qubit and
readout disagree, i.e. states ( _B, A_ __ ) and ( _A, B_ __ ), the readout can also make a transition
(to ( _B, B_ __ ) or ( _A, A_ __ ), respectively) with rate  det . We assume that the readout does not
change states unless the qubit has changed states (no false positives).

To take an example, imagine the readout record has just made a transition to _A_ __ ,


so the system will is in ( _A, A_ __ ). After some time, a qubit transition will occur and we go
from ( _A, A_ __ ) to ( _B, A_ __ ). As we wait for the readout to register by transitioning to ( _B, B_ __ ),
there is some probability that the qubit will change states again and return to ( _A, A_ __ ). If
so, this is a missed event. It is possible for several such cycles to occur before a transition
to ( _B, B_ __ ) occurs. At this point, the cycle repeats itself. The important point to note is
that the readout record gives us access to transition rates between _A_ __ and _B_ __ , but NOT to
rates between _A_ and _B_ . However, we can write down analytic expressions relating the two
to allow us to determine  _A_ and  _B_ , the true qubit transition rates.

If we are in readout state _A_ __ , we can write down rate equations for the probabilities

of being in qubit states _A_ and _B_ respectively:

_P_  _A_ = __  _A_ _P_ _A_ +  _B_ _P_ _B_ _,_ (8.1)

_P_  _B_ = __ ( _B_ +  det ) _P_ _B_ +  _A_ _P_ _A_ _._ (8.2)

The probability density for transitioning to readout state _B_ __ at time _t_ after arriving in _A_ __

is given by _P_ _B_ ( _t_ ) det . Solving equations (8.1) and (8.2) for _P_ _B_ and using the boundary
conditions 4 _P_ _A_ (0) = 1 and _P_ _B_ (0) = 0, we come up with an analytical formula for the

4 These boundary conditions are simply the statement that the readout never makes a transition to state

_A_ __ when the qubit is in state _B_ .


-----


133

|Col1|Exponential = 50 = 10 = 4 = 2 =|
|---|---|
|||
|||
|||
|||
|||



3 4 5 6

Time (  A )


0.0

-0.5

-1.0

-1.5

-2.0

-2.5

-3.0


Figure 8.5: Expected dwell time distributions.

We plot an exponential probability distribution function (PDF) with rate  _A_ as well as
_h_ ( _t_ ) for various values of  det with  _A_ =  _B_ . On these semi-log axes, exponential decay
appears as a straight line with slope proportional to decay rate. The time axis is in units
of __ _A_ = 1 _/_  _A_ . For  det __  _A_ , the behavior of _h_ ( _t_ ) closely approximates the exponential.
However, for smaller  det the long-time exponential tail of _h_ ( _t_ ) has a shallower slope than the
exponential. The slope is 98%, 90%, 76%, 59%, and 38% of the true  _A_ slope, respectively,
for the 5 curves with decreasing  det . The probability of observing short dwell time events
decreases with  det as expected.

distribution of dwell times in state _A_ __ :


_h_ ( _t_ ) = 2  _A_  det _e_ __ _t/_ 2 sinh

__


_t_

2





2
_h_ ( _t_ ) =


(8.3)


where __ =  _A_ +  _B_ +  det and __ =


__ 2 4 _A_  det . Examining the _t_ dependence of this
__


function, we note that the sinh term tends to reduce the probability of seeing short-time
events, as we expect. The overall behavior can be slightly difficult to glean by inspection,
so several dierent curves of _h_ ( _t_ ) for varying values of  det are plotted on semi-log axes in
Figure 8.5. We set  _A_ =  _B_ and vary  det ; a curve plotting an exponential decay with
rate  _A_ is shown for comparison. While the sinh term reduces the probability of seeing
short-duration events, at long times _h_ ( _t_ ) looks exponential again. However, the rate of this
long-time exponential behavior is substantially dierent from  _A_ , with the eect growing
worse as  det decreases. This is the eect we noted at the start of this section; now that we
have the form of _h_ ( _t_ ), though, we can use it to extract the true  _A_ .


The expression for _h_ ( _t_ ) is properly normalized to be a probability distribution


_1_

0

R


function (PDF), with


0 _h_ ( _t_ ) _dt_ = 1. We can also define a survival function _s_ ( _t_ ), which is


the probability of an event occurring at any point after time _t_ , expressed mathematically
as _s_ ( _t_ ) = _1_ _h_ ( _t_ _0_ ) _dt_ _0_ . The functional form of _s_ ( _t_ ) is:


_1_

_t_

R


_h_ ( _t_ _0_ ) _dt_ _0_ . The functional form of _s_ ( _t_ ) is:


_t_

2




_t_

2








_e_ __ _t/_ 2
_s_ ( _t_ ) =


__ sinh


+ __ cosh


(8.4)


-----


134

The reason for our interest in _s_ ( _t_ ) will become clear in the next section.

###### 8.1.3 ###### Maximum likelihood estimation

One of the classic problems of statistics is to determine the shape of a probabil-

ity distribution given a random set of observations drawn from that distribution. In the
case where the distribution is known to have a specific parameterized functional form, the
problem becomes the estimation of the parameters which characterize the distribution. For

5
example, an exponential distribution is characterized by a single parameter, the time constant __ , while a normal or Gaussian distribution is characterized by two parameters, the
mean __ and standard deviation __ . In our case, we are interested in estimating the qubit
transition rates  _A_ and  _B_ (for which we must also estimate  det ) given a set of observed
qubit state dwell times.

Of the many statistical methods used for parameter estimation, the technique

known as maximum likelihood estimation is generally the most robust method for generating
unbiased parameter estimates if we know the functional form of the underlying distribution.
Maximum likelihood estimation is relatively simple to understand. Let _X_ be a random
variable from a distribution _p_ ( _, X_ ) characterized by a parameter __ . If we are given a set
of observations _x_ _i_ drawn from this distribution with _i_ = 1 _,_ 2 _, ..., n_ , we can write down
_{_ _}_ _{_ _}_
the probability of receiving this particular set of observations, which is just the product of
each of the individual observation probabilities. This total probability for a particular set
of observations is called the likelihood function and denoted with _L_ :


_L_ =


_p_ ( _, x_ _i_ ) _._ (8.5)

_i_ =1


The value of the likelihood function depends on the parameter __ . The maximum likelihood
principle says simply that the best estimate for __ , called the maximum likelihood estimate
or MLE and denoted __  , is the one for which the likelihood function is largest.

Maximum likelihood estimation has a number of nice properties, which are enu-

merated and rigorously proven in standard statistics books [179, 180, 181], and which we
touch on briefly here. First, maximum likelihood estimators are called invariant, meaning that they are independent of the particular parameterization of the distribution. In
other words, if __  is the MLE of the parameter __ for a given distribution, then the MLE

of a parameter __ __ = _g_ ( __ ) (where _g_ is an arbitrary function) is just __  __ = _g_ ( __  ) 6 . Second,


maximum likelihood estimates are unbiased, meaning that in the limit of a large number
of data points the MLE __  tends to the true value of the parameter __ . Third, the maximum

likelihood estimate is asymptotically normal, meaning that for large _n_ , the value of __  will


be normally distributed about the true parameter value __ with a variance __ __ 2 _/n_ which can

5 One can equivalently parameterize an exponential distribution with a rate constant __ = 1 _/_ ; in either

case, though, only one parameter is required.

6 For example, the exponential distribution can be parameterized in terms of a time constant __ or a rate

constant __ = 1 _/_ ; the invariance of the maximum likelihood estimator means that it does not matter which
parameterization we use.


-----


135

be explicitly calculated 7 . The property of asymptotic normality allows us to put confidence
intervals on maximum likelihood parameter estimates given sufficiently large data sets. Finally, the maximum likelihood estimator is what is known as a uniformly minimum variance
unbiased estimator. This means that of all the possible unbiased estimation methods for
a parameter __ of a distribution, maximum likelihood estimation always has the smallest
uncertainty in the final estimate __  .

_6_


The actual process of maximum likelihood estimation just involves solving for the

value of __  which maximizes equation (8.5). A maximum will occur at a point where

_6_


_@_
_L_ = 0 (8.6)

_@_

_6_


Note that equation (8.6) represents a necessary, but not sufficient, condition for maximization. Because the derivative will be zero at both minima and maxima, and because there
may be several maxima, in general we may need to check the values of _L_ at each extreme
point to find which one is the global maximum. In addition, maxima may lie on the boundaries of the parameter space in places where _@_ _L_ = 0, so it important to check boundary _6_


_@_ _L_ = 0, so it important to check boundary

_6_



_6_

cases as well.



_6_

To solve for __  , we can simply solve equation (8.6). As a practical matter, though,

the problem of maximizing _L_ is generally solved by instead maximizing the log-likelihood
function _L_ = ln :
_L_ _n_



_6_

_L_ =



_6_

ln[ _p_ ( _, x_ _i_ )] (8.7)

_i_ =1



_6_

Since ln( _x_ ) is a monotonic function of _x_ , the value of __ which maximizes _L_ will also maximize
_L_ , so we can use either formulation of the problem. However, the math of maximizing
_L_ is typically much simpler, since it is a sum of terms instead of a product. There is

another practical reason for using _L_ instead of _L_ , related to the constraints of numerical
calculations. For large data point were 0.5 (a high estimate in most cases!) and _n_ , _L_ rapidly becomes incredibly small. If the probability for each _n_ = 10 4 , we find _L_ = 2 __ 10 _,_ 000 ,
a number so small that it cannot be represented as a standard double precision floatingpoint number. Since _L_ sums numbers rather than multiplying them, the log-likelihood

function is much better behaved with large numbers of data points; in the above example,
_L_ = 10 4 ln(0 _._ 5) __ 6930, a much more tractable number. In general, if there are enough
data points to yield reasonable parameter estimates, one typically has to use _L_ .

Many probability distributions have multiple parameters, which we can express by

writing __ as a vector __ _~_ with _K_ components, one for each parameter. In this case, maximizing

_L_ requires finding extreme points in multidimensional space, with derivatives with respect
to each parameter __ _k_ satisfying



_6_

_@L_

_@_ _k_



_6_

= 0 _, k_ = _{_ 1 _,_ 2 _,_ _  _ _, K_ _}_ _._ (8.8)



_6_

7 The value of __ __ 2 is the inverse of the Fisher information ( __ ), given by ( __ ) = _E_ __ _@_ _@_ ln _p_ ( _, X_ ) 2 =

_1_ _1_ _@_ _@_ ln _p_ ( _, x_ ) 2 _p_ ( _, x_ ) _dx_ . The notation _E_ __ denotes the conditional expectation value over _I_ _I_  _X_ with respect 

to _p_ ( _, X_ ) for a given __ [181].

R  



_6_

_@_




_6_

7 The value of __



_6_

__ 2 is the inverse of the Fisher information ( __ ), given by ( __ ) = _E_ __

_I_ _I_



_6_

_@_ _@_ ln _p_ ( _, X_ )



_6_

_@_




_6_

_@_

2 _p_ ( _, x_ ) _dx_ . The notation _E_ __ denotes the conditional expectation value over _X_ with respect

__ [181].





_6_

to _p_ ( _, X_ ) for a given __ [181].



_6_

_1_



_6_

_@_ _@_ ln _p_ ( _, x_ )


-----


136

We will use the notation of __ _~_ to maintain full generality, and because it applies to our case

of interest.

It is instructive to demonstrate how maximum likelihood estimation works on a


specific probability distribution. Lets take the example of an exponential distribution with
random variable _T_ and decay time parameter __ , given by _p_ ( _, T_ ) = __ 1 _e_ __ _T/_ . Given a set of

observations _t_ _i_ , we construct the likelihood function:
_{_ _}_


_L_ =


_i_ =1



_e_ __ _t_ _i_ _/_ _._ (8.9)
__


Taking the log of of _L_ gives us the log-likelihood function, which takes the nice form:


_L_ =


_i_ =1



_t_ _i_ 1
( ln __ ) = _n_ ln __
__ __ __ __ __ __


_t_ _i_ _._ (8.10)

_i_ =1


Next we take the derivative of _L_ with respect to __ , which gives:


_@L_ _n_

=
_@_ __ __


+ 1

__


+ 1


_t_ _i_ _._ (8.11)

_i_ =1


The extreme points of _L_ will occur when _@L_



_@L_ _@_ = 0. Setting the above expression equal to 0


and factoring out 1 _/_ 2 leaves us with:


__ 2


__ _n_ +


_i_ =1


_t_


= 0 _._ (8.12)


One solution to this equation is __ = _1_ , which is a non-physical solution. The other solution
is the maximum, and gives us the MLE  __ for __ :



1
__  =


_t_ _i_ _._ (8.13)

_i_ =1


The result we get is that  __ is the sum of all observed times divided by the number of

observations, in other words the mean observed decay time. This is a simple, clean result
which makes intuitive sense 8 .

If we have only a certain window in which we can observe events, for example

the finite duration of a qubit readout pulse, we may have some data which is censored.
Censoring broadly refers to observations where we do not know the exact observed value,
merely a range in which it lies. Censored data is common in the statistics subfields of

survival analysis and reliability analysis, and methods for using censored data are very well
developed [173].

Our quantum jump data exhibit right censoring, which is when we know that the

value of the censored data point is greater than or equal to a known value. Considering the


8 For a Gaussian distribution, the estimator  __ of the mean is simply the mean of the observed data points,

and the estimator  __ 2 of the variance is the variance of the observed data points. These simple cases are nice

checks, but dont fully showcase the power of maximum likelihood estimation for non-intuitive cases.


-----


137

case of a readout pulse, the qubit is in a given state when the readout turns o, but does
not necessarily decay right then. All we can know about the dwell time of the qubit in that
state is that it was at least as long as what we observed during readout. However, despite
the fact that we have incomplete information about this data point, we can still make use
of it.

We can modify equation (8.5) to account for right censoring by introducing the


variables __ _i_ and the function _P_ ( _,X > x_ _~_ ). The __ _i_ are variables which take either the value 0

(if the _i_ th observation is uncensored) or 1 (if the _i_ th observation is censored). The function
_P_ ( _,X > x_ _~_ ) is the survival function, given by integrating the PDF _p_ ( _,X_ _~_ ) over all values of

_X_ greater than a specific one _x_ :


_1_

_x_

Z


_P_ ( _, X > x_ _~_ ) =


_p_ ( _, x_ _~_ _0_ ) _dx_ _0_ _._ (8.14)


Armed with these definitions, we construct the likelihood function as before by multiplying
together the probabilities of each individual observation. For uncensored observations,


we use the same probability as before, _p_ ( _,x_ _~_ _i_ ). For censored observations, however, the

probability is now the survival function _P_ ( _,X > x_ _~_ _i_ ). We need to construct a likelihood

function that is able to represent either one of these cases based on whether a given data
point is censored or not. A suitable function takes the form:


_L_ =


_p_ ( _,x_ _~_ _i_ ) 1 __ __ _i_ _P_ ( _,X > x_ _~_ _i_ ) __ _i_ _._ (8.15)

_i_ =1


If __ _i_ = 0 for a given _i_ (an uncensored data point), the second factor is just 1 and so we
just recover the original probability _p_ ( _, x_ _~_ _i_ ). If __ _i_ = 1, the first factor becomes one and

the probability for that point is then given by _P_ ( _,X > x_ _~_ _i_ ), as desired. The corresponding


If __ _i_ = 0 for a given _i_ (an uncensored data point), the second factor is just 1 and so we
just recover the original probability _p_ ( _, x_ _~_ _i_ ). If __ _i_ = 1, the first factor becomes one and


log-likelihood function is then:


_L_ = ln _L_ =


_i_ =1


(1 __ __ _i_ ) ln[ _p_ ( _,x_ _~_ _i_ )] + __ _i_ ln[ _P_ ( _,X > x_ _~_ _i_ )]


(8.16)


This log-likelihood function allows us to use all data points, both censored and uncensored,
to estimate the parameters. Lets return to the example of the exponential distribution, but
this time allow data points to be censored. First, we must calculate the survival function
for the exponential distribution, which is given by _P_ ( _, T > t_ ) = _1_ 1 _e_ __ _t_ _0_ _/_ _dt_ _0_ = _e_ __ _t/_ . We


_1_

_t_

R


can then write down the likelihood function:


1 _t_ _0_ _/_ _t/_
__ _e_ __ _dt_ _0_ = _e_ __ . We


_L_ =


_i_ =1


1 _e_ __ _t_ _i_ _/_

__




1 __ __ _i_




_e_ __ _t_ _i/_ __ _i_ _._ (8.17)




Taking the logarithm gives us the log-likelihood function:


_L_ =


_i_ =1



_t_
(1 __ _i_ )( ln __
__ __ __ __



_t_ _i_ _t_ _i_

) + __ _i_ ( __
__ __


__


= __ ln __ ( _n_ __


_i_



1
__ _i_ )
__ __


_t_ _i_ _._ (8.18)

_i_ =1


-----


138

To find the maximum, we take the derivative of _L_ with respect to __ :


_@L_


_@L_ 1

=
_@_ __ __



( _n_
__ __


_i_ =1



1
__ _i_ ) + __ 2



1
__ _i_ ) +


_t_ _i_ _._ (8.19)

_i_ =1


A maximum will occur when _@L_


_@_ = 0. We set the above derivate equal to zero and factor


out 1 _/_ 2 as before, giving us:


__ 2


__ __ ( _n_ __


_i_ =1


__ _i_ ) +


_i_ =1


_t_


= 0 _._ (8.20)


Again we ignore the pathological __ = solution. This equation contains the term __ _i_ ,
_1_
which we recognize to be simply the total number of censored data points _n_ cens . Using the

P
definition
_n_

__ _i_ = _n_ cens _,_ (8.21)

_i_ =1

X

we substitute in to equation (8.20) to get our MLE  __ , which is given by


__  =


_n_ _n_ cens
__


_t_ _i_ _._ (8.22)

_i_ =1


Our result is almost as simple as the result for  __ in the case without censoring. The MLE

for __ is the sum of all of the individual observed times divided by the total number of
uncensored observations. In this way, the estimate uses both censored and uncensored data
(because all the _t_ _i_ are included), giving us more information than if we just used uncensored
observations. While simple, equation (8.22) is not intuitive, and begins to demonstrate the
power of maximum likelihood estimation.

We are interested in determining the rate of transitions between the two qubit


states, which we can do using the model described in section 8.1.2. There we derived a
probability distribution function _h_ ( _t_ ) and survival function _s_ ( _t_ ), defined in equations (8.3)
and (8.4), for the observed jump times, given some underlying rate parameters. To keep our
notation consistent with that used for the qubit state extraction, we make the identification
between states _A_ _$_ _s_ _lo_ and _B_ _$_ _s_ _hi_ , with  _A_ _$_  up and  _B_ _$_  dn .

Our task is now to find the true values of  up and  dn , for which we will use

maximum likelihood estimation. We are given two sets of observations, the dwell times _t_ _i_
_{_ _}_
in _s_ _lo_ and the dwell times _{_ _t_ _j_ _}_ in _s_ _hi_ , as well as lists _{_ __ _i_ _}_ and _{_ __ _j_ _}_ of censoring variables for
each. The parameters  up ,  dn , and  det are the same for both sets of observations, so we
should construct our likelihood function to enable us to use both data sets simultaneously
to optimize all three parameter values. If there are _n_ _lo_ observed dwell times in _s_ _lo_ and _n_ _hi_
in _s_ _hi_ , we can write:

_n_ _lo_


_L_ =


_i_ =1


_h_ ( up _,_  dn _,_  det ; _t_ _i_ ) 1 __ __ _i_ _s_ ( up _,_  dn _,_  det ; _t_ _i_ ) __ _i_


(8.23)

_h_ ( dn _,_  up _,_  det ; _t_ _j_ ) 1 __ __ _j_ _s_ ( dn _,_  up _,_  det ; _t_ _j_ ) __ _j_


_n_ _hi_


_j_ =1


-----


139

where we explicitly write out the dependence of _h_ and _s_ on the three  parameters. This
likelihood function is constructed by multiplying together the individual likelihood functions
for each set of observations to give a joint likelihood for maximization. In this way, we use
all of the data in a single estimation. Importantly, note that the order of  up and  dn is
interchanged for the _t_ _j_ relative to the _t_ _i_ . This is because the rate of leaving _s_ _lo_ is the same
as the rate of leaving _s_ _hi_ with the  up and  dn interchanged, as is clear from the symmetry
of the model.

Given this rather large likelihood function, we make the log-likelihood function _L_ ,

which takes the form:

_n_ _lo_


_L_ =


(1 __ __ _i_ ) ln[ _h_ ( up _,_  dn _,_  det ; _t_ _i_ )] + __ _i_ ln[ _s_ ( up _,_  dn _,_  det ; _t_ _i_ )]


_i_ =1


_n_ _hi_

_j_ =1


(8.24)

(1 __ __ _j_ ) ln[ _h_ ( dn _,_  up _,_  det ; _t_ _j_ )] + __ _j_ ln[ _s_ ( dn _,_  up _,_  det ; _t_ _j_ )]


Already this is beginning to look considerably more complicated than the case of the simple
exponential distribution! We now plug in the functional forms for _h_ ( _t_ ) and _s_ ( _t_ ) which are
shown in equations (8.3) and (8.4). We must be careful, because they are parameterized
in terms of the variables __ and __ , which are combinations of the three gammas. While
__ =  up +  dn +  det is invariant under a swap of  up and  dn , __ is not. We therefore must
define two dierent values, __ up = __ 2 4 up  det and __ dn = __ 2 4 dn  det to be used in


__ 2 __ 4 up  det and __ dn =


__ 2 __ 4 dn  det to be used in


the appropriate cases. Note that the use of __ and __ is simply a change of variables used
to make the algebra easier; they do not represent additional parameters to be maximized,
because each is fully specified by the three gammas 9 .


We can write out the first line of equation (8.24) using the full definitions of _h_ ( _t_ )

and _s_ ( _t_ ). This substitution gives us:


_n_ _lo_

_i_ =1


2 up  dn

__ up





_t_ _i_
__ 2 + ln



_t_ _i_
__


__ up _t_ _i_

2







(1 __ _i_ )
__

_n_ _lo_

+ __ _i_

_i_ =1

X


ln


sinh



_t_ _i_
ln( __ up ) + ln
__ __ 2



_t_ _i_
ln( __ up )
__ __


__ up _t_

2




__ up _t_ _i_

2




 (8.25)


__ sinh


+ __ up cosh


The second line of equation (8.24) is the same, except we interchange every __ up for __ dn , _n_ _lo_
for _n_ _hi_ , and _i_ for _j_ . This gives us:


_n_ _hi_

_j_ =1


2 dn  up

__ dn





_t_ _j_
__ 2 + ln



_t_ _j_
__


__ dn _t_ _j_

2







(1 __ _j_ )
__

_n_ _hi_

+ __ _j_

_j_ =1

X


ln


sinh



_t_ _j_
ln( __ dn ) + ln
__ __ 2



_t_
ln( __ dn )
__ __


__ dn _t_ _j_

2




__ dn _t_

2




 (8.26)


__ sinh


+ __ dn cosh


9 Recall as well that the invariance property of maximum likelihood estimation means that we are free to

choose among these dierent parameterizations when describing our probability density without aecting
the outcome of the maximum likelihood estimation.


-----


140

![SlichterThesis.pdf-158-0.png](SlichterThesis.pdf-158-0.png)

![SlichterThesis.pdf-158-2.png](SlichterThesis.pdf-158-2.png)

![SlichterThesis.pdf-158-1.png](SlichterThesis.pdf-158-1.png)

100 200 300 400 500 600 700 800

#####  ##### up ##### (ns)

Figure 8.6: Log-likelihood in parameter space.


1600

1400

1200

1000

800

600

400

200


This is a color plot of the log-likelihood function _L_ in equation (8.24) as a function of
__ up = 1 _/_  up and __ dn = 1 _/_  dn , with  det = 0 _._ 01 ns __ 1 , using dwell times extracted from 10 3

measurement traces. The likelihood is maximized for this value of  det at the point marked
by the red circle. The function _L_ actually exists in three dimensions, and so we must search
in  det as well to determine the true maximum likelihood. The function is smooth and
well-behaved except at the boundaries, where it diverges.


Looking at the expressions in (8.25) and (8.26), it is readily apparent that we wont be able
to solve analytically to determine the maximum likelihood parameter estimates   up ,   dn

or   det . We instead resort to numerical optimization. By providing a reasonable initial


guess for our parameters, we can use numerical methods to hill climb to a maximum
of _L_ in parameter space and determine   up ,   dn , and   det in this way. Figure 8.6 shows

the numerical value of _L_ for a real data set with 10 3 traces. The function is smooth and
well-behaved, except near the boundaries  = 0 where it diverges. The maximum likelihood
point is marked in red.

There are a number of methods in the literature for performing multidimensional

numerical optimizations of this kind [182, 183]. However, some of the best methods are
notoriously finicky about the shape of the function to be optimized and the quality of the
initial guess. We chose one which seemed to provide sufficient robustness, a quasi-Newton
method with a double-dogleg trust-region search [182] as implemented by Igor [171]. The
whole trick of numerical optimization schemes, aside from making a good initial guess, is to
select a good direction to search in parameter space and an appropriate step length along
that direction. The simplest method along these lines, called gradient descent 10 , involves

10 All optimization methods can search for either a minimum or a maximum; one need simply negate the

function being optimized to turn its maxima into minima and vice versa. Much of the optimization literature


-----


141

following the gradient some distance to choose the next point, the following the gradient
from there, and so on. Gradient descent is almost never used, because in the case of flat,
shallow minima it takes a very long time to converge and is thus computationally inefficient.
Methods like gradient descent, which follow the derivative exactly, are referred to as Newton
methods.

In the 1960s and 1970s, a class of methods called quasi-Newton methods arose.

Quasi-Newton methods follow a modified prescription for finding the search direction, combining gradient information with information from the Hessian matrix, or an approximation
to the Hessian matrix, which contains information on the second derivatives of the function. As a result, quasi-Newton methods have much more rapid convergence than simple
gradient descent. One of the most popular quasi-Newton methods is the Broyden-FletcherGoldfarb-Shanno (BFGS) method, which provides a technique for continuously updating
an approximation to the Hessian matrix at each search point, making it computationally
efficient. However, the BFGS method requires that the Hessian matrix always be positivedefinite, which is equivalent to the statement that the concavity of the optimized function
must have the same sign everywhere. If this is not the case, as appears to be the case
with our optimization problem, the BFGS method fails. The double-dogleg trust-region
method uses a hybrid approach, combining some of the robustness of gradient descent with
the efficiency of quasi-Newton Hessian-based step direction selection, and employing trustregion techniques to restrict step size in a more robust way [182]. There are many other
possible optimization routines available, and the interested reader is encouraged to consult
references [182] and [183] to begin his or her explorations.

To perform the optimization, we need to give some initial guesses about the values

of the parameters. We can provide rough estimates for the values of  up and  dn by

assuming an exponential distribution and using equation (8.22) to determine __ up = 1 _/_  up
and __ dn = 1 _/_  dn . A reasonable initial guess for  det might be __ , the cavity linewidth, which
sets the rate at which information leaves the readout resonator.

There are a few other technical considerations for the numerical optimization re-

lated to floating point arithmetic. The log-likelihood function _L_ has various terms of the
form ln(sinh( _x_ )) or ln( _a_ sinh( _x_ ) + _b_ cosh( _x_ )), as seen in equations (8.25) and (8.26). For
sufficiently large values of _x_ , sinh( _x_ ) and cosh( _x_ ) will return a NaN (Not a Number) in
floating point arithmetic, so ln(sinh( _x_ )) and ln(sinh( _x_ )) will evaluate as NaNs as well.
These NaNs turn the entire value of to a NaN and thus are fatal to the optimization procedure. The solution is to recognize that for _L_ _x_ __ 1, ln(sinh( _x_ )) __ _x_ __ ln 2 and
ln( _a_ sinh( _x_ )+ _b_ cosh( _x_ )) __ _x_ +ln( _a_ + _b_ ) __ ln 2. When performing the sum to compute _L_ , we
simply check the value of fractional errors below 10 _x_ __ 18 and use these alternative forms if for any given term). _x_ __ 20 (a cutowhich gives

###### 8.1.4 ###### Tests of the extraction algorithm

To test the performance of the automated extraction algorithm, we made a series

of simulated data traces with known parameters. By running these through the automated

is written for minimization problems, where one descends into a minimum, thus the nomenclature. We
will use descent, even though it should strictly be ascent in our case, because they are made equivalent
by just choosing to minimize __ _L_ rather than maximizing _L_ .


-----


142

extraction algorithm, we could see how well the extracted qubit state tracked the nominal
qubit state, and gauge the quality of the estimates both for ensemble qubit population
across many time traces and for qubit transition rates.

In order for this test to be accurate, we need the simulated data traces to be as

similar to real data as possible. This means modeling the limited measurement bandwidth,
adding noise, and using a wide variety of realistic qubit transition rates. To generate

simulated data, we specify qubit excitation and relaxation rates  and  , the cavity
_"_ _#_
bandwidth __ , the noise bandwidth _B_ , the initial excited state fraction, the signal-to-noise
ratio, the duration of each trace, and the number of traces. We match the sampling rate in
time (100 MS/s) to that of our real data.

First, we make a series of noiseless time traces, representing the state of the qubit.

These are formed by stringing together random dwell times drawn from exponential distributions with decay rates  and  until we reach the time limit for the trace. The initial
_"_ _#_
state is chosen randomly, with a specified probability for being in the ground state initially.
After making these noiseless time traces, we convert the sharp transitions between states
to rising or falling exponentials with a time constant 2 _/_ , which models the behavior of the
cavity output signal when the qubit state changes.

We generate Gaussian white noise at the data sampling frequency and then filter

it to be in the bandwidth _B_ , which is set to be equivalent to the bandwidth of the filters on
the output of the demodulation circuit (see section 5.3.3). The filter rollois set to match
that of the physical filters used in the experiment. We then histogram the filtered noise to
determine its standard deviation.

With both signal and noise in hand, we add them together, scaling their relative

values to give the desired signal-to-noise ratio (as defined in section 7.5.2). The absolute
scaling of the combined trace is then set to match typical values of real data. The real data,
in raw form, are 8-bit unsigned integers (integers in the range 0-255), with a dierence in the
mean high and low levels of around 70-100, so this is the scaling we apply to our simulated
data. Finally, we turn the scaled simulated data into 8-bit unsigned integers, rounding o
all data points to the nearest integer.

For each simulated data trace, we have access to the exact set of dwell times in the


high and low excited states. Using these, we perform maximum likelihood estimation using
equation (8.22) to give best-case estimates   and   if the qubit state is perfectly known.
_"_ _#_

We also calculate the qubit ensemble population as a function of time, as well as the mean
and median steady-state qubit population. These are our benchmarks for comparing the
performance of the automated qubit extraction algorithm.

Figure 8.7 shows the results of state extraction algorithm tests for simulated data


with either a nominal SNR of 3 (equivalent to the SNR of real data with  _n_ __ 30) or a


nominal SNR of 1.6 (equivalent to the SNR of real data with  _n_ __ 3). These SNR values


are quoted for the raw data, before any smoothing. The simulated data are generated for
a variety of possible excitation and relaxation rates  and  corresponding to typical
_"_ _#_
observed experimental values. We test our state extraction algorithms estimates of the
steady state qubit population (top two panels), the qubit relaxation time 1 _/_  (middle
_#_
two panels), and the qubit excitation time 1 _/_  (bottom two panels). Each plotted point
_"_
represents the mean percentage error of the extracted estimate (as compared to the true


-----


143


SNR=3 steady state qubit population SNR=1.6

50000
25000
10000


SNR=3 steady state qubit population SNR=1.6


50000
25000
10000

6000
4500
3000
1750
1000

600
350

50000
25000
10000

6000
4500
3000
1750
1000

600
350

50000
25000
10000

6000
4500
3000
1750
1000

600
350


6000
4500
3000
1750
1000

600
350

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|10 Extraction 5 0 error -5 (%) -10|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|10 Extraction 5 0 error -5 (%) -10|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||


![SlichterThesis.pdf-161-1.png](SlichterThesis.pdf-161-1.png)

![SlichterThesis.pdf-161-0.png](SlichterThesis.pdf-161-0.png)

1/   (ns)


1/   (ns)


relaxation time 1/  

50000

20 25000

10000


6000
4500
3000
1750
1000

600
350

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Extraction 20 10 0 error -10 -20 (%)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Extraction 20 10 0 error -10 -20 (%)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||


![SlichterThesis.pdf-161-2.png](SlichterThesis.pdf-161-2.png)

![SlichterThesis.pdf-161-3.png](SlichterThesis.pdf-161-3.png)

1/   (ns)


1/   (ns)


excitation time 1/  

50000

20 25000

10000


6000
4500
3000
1750
1000

600
350

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Extraction 20 10 0 error -10 -20 (%)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Extraction 20 10 0 error -10 -20 (%)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||


![SlichterThesis.pdf-161-5.png](SlichterThesis.pdf-161-5.png)

![SlichterThesis.pdf-161-4.png](SlichterThesis.pdf-161-4.png)

1/   (ns)


1/   (ns)


Figure 8.7: Performance of automated state extraction algorithm.

These six panels show the percentage error in the estimates provided by the automated
state extraction algorithm for the steady state qubit population (top two panels), the qubit
relaxation time (middle two panels), and the qubit excitation time (bottom two panels).
The left column is from simulated data with nominal SNR=3, while the right column is for
simulated data with nominal SNR=1.6; these SNRs are quoted before any smoothing by
the state extraction algorithm.


-----


144

value) for 10 dierent sets of simulated data generated with nominally identical values of
 ,  , and SNR. Each simulated data set consists of 10 4 traces of 1750 points each, the
_"_ _#_
same size as the experimental data sets we use later in this chapter.

We find that the algorithm estimates the steady state qubit population quite ac-

curately, with a typical fractional error less than 5% even for the low SNR data. The

population estimates are least accurate for simulated data with   . However, in this
_"_ __ _#_
regime the actual steady state excited population of the qubit is quite small (  _/_  ),
__ _"_ _#_
so the absolute error in the qubit state population remains low even though the fractional
error has increased.


The fractional error of the qubit transition rate estimates   and   is not as
_"_ _#_

low as that for the population estimates, but is essentially always better than 20% and
is typically better than 10%, even for the low SNR case. The performance is worst when
one or both of the transition rates is very fast, (causing us to miss a greater fraction of
events due to our finite measurement bandwidth and limiting our ability to reduce the noise
bandwidth _B_ to improve the SNR), or when the rates are very disparate. Our estimates
of the excitation rate  are on the whole better than our estimates of  because  is
_"_ _#_ _"_
typically much slower, and so we have fewer missed events. In all cases, improving the
nominal SNR gives a more reliable estimate of the transition rates.

Overall, the performance of the automated qubit state extraction algorithm is good

enough for use in our experimental analyses. Because the population estimates are more
accurate than the rate estimates, we use population estimates when possible.

#### 8.2 #### Measurement-induced state mixing

During the course of our quantum jump measurements, we saw that the qubit

would occasionally jump up to the excited state during measurement without any applied
qubit pulse. This phenomenon became more and more visible as we increased the readout
cavity occupation  _n_ . It has been known for some time through ensemble measurements [64]

that something limits the fidelity and QND nature of circuit QED readout at high photon
numbers. With our continuous monitoring capabilities and automated jump extraction

techniques, we can quantify this behavior for the first time and attempt to discover its
origin.

Figure 8.8 shows two typical sets of measurement time traces with the qubit ini-

tially in the ground state. As the cavity photon occupation  _n_ increases, the qubit is more

and more likely to be randomly excited during the measurement. This appears to be an
eect caused during readout pulse itself, since the qubit is in the ground state at the start
of readout, no matter the value of  _n_ .

###### 8.2.1 ###### Dressed dephasing theory

One candidate theory to explain this phenomenon is the dressed dephasing theory

[45, 184]. The dressed dephasing theory predicts that noise at the qubit-cavity detuning
frequency = _!_ _q_ __ _!_ ro will be mixed with readout photons to cause qubit transitions. The
noise couples to the qubit through some control parameter (flux or charge, for example)


-----

|Digitizer voltage|Col2|Col3|Col4|Digitizer voltage|
|---|---|---|---|---|
||||||

|Digitizer voltage|Col2|Col3|Col4|Digitizer voltage|
|---|---|---|---|---|
||||||


![SlichterThesis.pdf-163-10.png](SlichterThesis.pdf-163-10.png)

![SlichterThesis.pdf-163-11.png](SlichterThesis.pdf-163-11.png)

![SlichterThesis.pdf-163-7.png](SlichterThesis.pdf-163-7.png)

![SlichterThesis.pdf-163-8.png](SlichterThesis.pdf-163-8.png)

![SlichterThesis.pdf-163-9.png](SlichterThesis.pdf-163-9.png)

![SlichterThesis.pdf-163-0.png](SlichterThesis.pdf-163-0.png)

![SlichterThesis.pdf-163-1.png](SlichterThesis.pdf-163-1.png)

![SlichterThesis.pdf-163-2.png](SlichterThesis.pdf-163-2.png)

![SlichterThesis.pdf-163-3.png](SlichterThesis.pdf-163-3.png)

![SlichterThesis.pdf-163-4.png](SlichterThesis.pdf-163-4.png)

![SlichterThesis.pdf-163-5.png](SlichterThesis.pdf-163-5.png)

![SlichterThesis.pdf-163-6.png](SlichterThesis.pdf-163-6.png)

0.0 0.5 1.0 1.5 2.0

Time (s)


145

Digitizer voltage

0.0 0.5 1.0 1.5 2.0

Time (s)


Figure 8.8: Spurious qubit state mixing.

We show two sets of measurement traces taken with the qubit nominally in the ground state
for  _n_ = 5 (left) and  _n_ = 46 (right). Some of the traces are spuriously excited during the

measurement. The eect appears to be measurement-induced because it becomes stronger
with increasing  _n_ , and because the spurious excited state population is not apparent when

the measurement starts.

that enters in the qubit Hamiltonian. This is modeled as a perturbation

_H_ _'_ = ~ _f_ _'_ ( _t_ ) __ _z_ _,_ (8.27)

where __ characterizes the strength of the coupling between the noise and the qubit (e.g. if
_f_ _'_ ( _t_ ) is a flux noise, as in the case of the transmon, __ is a flux-to-qubit-frequency transfer
function). The low frequency components of _f_ _'_ ( _t_ ) are responsible for qubit dephasing.

However, the frequency spectrum of _f_ _'_ ( _t_ ) can extend out to arbitrarily high frequencies, so
that this dephasing noise can have components at the detuning frequency . When this
dephasing noise is dressed by the presence of readout photons (thus the name dressed
dephasing), it can give rise to transitions between the qubit states. The rate for transitions
up and down is given by [45, 184]



2
 _"_ _#_ _,_ DD = 4 _g_  2 __ 2 _S_ ( __ ) _n,_ (8.28)

where _g_ is the qubit-cavity coupling,  _n_ is the cavity photon occupation, and _S_ () is the


power spectral density of _f_ _'_ ( _t_ ) at the detuning frequency . Once the system has reached
steady state, we expect a spurious excited state population to exist. Using the principle of
detailed balance, we can express this in terms of __  _z_ as
_h_ _i_


__  _z_ = 1 +  _"_ _,_ DD
_h_ _i_ __  1 + 


 1 +  _,_ DD
_#_


(8.29)


-----


146

Here  1 = 1 _/T_ 1 is the intrinsic qubit decay rate, including the Purcell eect. In the case of
a symmetric noise spectrum where _S_ () = _S_ ( ), we have  _,_ DD =  _,_ DD . Furthermore,
__ _#_ _"_
in most cases the spurious excitation and relaxation rates are much slower than  1 . Using
these two ideas, we can rewrite equation (8.29) as:


__  _z_ = 1 +  _"_ _,_ DD
_h_ _i_ __  1 +  _,_ DD

_"_


1 +  _"_ _,_ DD
__  1


1 +  _"_ _,_ DD
__  1


(8.30)


The fractional excited state population of the qubit is given by (1+ __  _z_ ) _/_ 2, which
_h_ _i_

means that it is directly proportional to  _"_ _,_ DD . This in turn implies that the fractional
excited state population we observe in steady state should be directly proportional to the
cavity photon occupation  _n_ and the spectral density of flux noise at the detuning frequency


The fractional excited state population of the qubit is given by (1+ __  _z_ ) _/_ 2, which
_h_ _i_


_S_ ( __ ).


We now set out to perform experimental tests of the dressed dephasing theory


by intentionally injecting signals and/or noise into the qubit loop. There are three main
avenues we pursue. First, we apply flux signals to the qubit at dierent frequencies and see
if the qubit responds to noise at all frequencies or just near . This establishes whether or
not the notion of mixing between flux noise at and readout photons to generate qubit
transitions is accurate. Second, we apply broadband noise with a known component at 
and see if the steady state qubit population scales linearly with _S_ () and  _n_ as predicted.


Finally, if these two tests support the dressed dephasing theory, we can use measurements
of the qubit behavior with and without added noise to measure the power spectral density
of flux noise at the detuning frequency , which is of order __ 1 GHz. Flux noise in

superconducting devices has never been measured in this frequency range before.

###### 8.2.2 ###### Experimental scheme

The experiment is similar to that presented in the previous chapter. We use a

transmon qubit with _E_ _J_ ( = 0)=20.3 GHz and _E_ _C_ =231 MHz, capacitively coupled to a
superconducting quasi-lumped-element resonator consisting of a meander inductor (L=3.68
nH) in parallel with an interdigital capacitor (C=175 fF). The qubit/cavity sample is shown
in Figure 8.9(a). Unlike the sample in the previous chapter, this resonator has asymmetric
coupling and is operated in transmission, with excitations entering from the weakly coupled
port via a heavily attenuated injection line and leaving through the strongly coupled port
towards the amplifiers 11 . The qubit state is manipulated by applying microwave signals
through the weakly coupled port of the resonator. In addition, while the sample in the
previous chapter was on a Bollywood launch, this sample was in an enclosed, shielded type
B sample box with bulkhead SMA connectors (see section 5.1 for more details). Qubit
coherence times are better in this sample, varying monotonically depending on the qubit
frequency from _T_ 1 =290 ns and _T_ 2 =550 ns at _f_ _q_ =5.705 GHz to _T_ 1 =910 ns and _T_ 2 =1.35
__ s at _f_ _q_ =5.075 GHz. These numbers represent _T_ 1 values about a factor of two below the
Purcell limit, and pure dephasing times _T_ _'_ much longer than _T_ 1 . The readout cavity has

11 This design has the additional advantage that the cavity serves as a filter for the qubit pulses, substan-

tially reducing their power at the paramp relative to the reflection geometry. The paramp does not appear
to be aected by the presence of qubit pulses in either geometry since they are very far detuned from the
pump, but its nice to control this variable nonetheless.


-----


147




![SlichterThesis.pdf-165-0.png](SlichterThesis.pdf-165-0.png)

![SlichterThesis.pdf-165-2.png](SlichterThesis.pdf-165-2.png)

![SlichterThesis.pdf-165-1.png](SlichterThesis.pdf-165-1.png)

Figure 8.9: Transmon qubit and resonator with fast flux line.

Part (a) shows a photograph of the qubit/cavity sample with input port (left), output port
(right), and fast flux port (top). Part (b) depicts the experimental setup, similar to the
previous chapter. Readout photons enter the cavity via the weakly coupled input port (grey
arrow, 1), interact with the qubit, and acquire a phase shift which depends on the qubit
state. The readout signal then leaves the cavity via the strongly coupled port (purple arrow,
2), passes through several circulators, and combines with the paramp pump tone (green
arrow, 3). The readout and pump interact in the paramp and the amplified readout

signal (red arrow, 4) is reflected to the output port. The readout signal then is further
amplified, mixed down to zero frequency (converting the phase shift signal into a voltage
signal), and digitized. Noise or coherent tones can be injected into the qubit loop via a
weakly coupled fast flux line with a bandwidth of 2.2 GHz. Grey dashed lines indicate flux
coupling.

a bare frequency of 6.2724 GHz with a linewidth _/_ 2 __ = 7 MHz and a coupling to the
qubit _g/_ 2 __ = 106 MHz. The cavity frequency is Lamb-shifted up by roughly 10-20 MHz
depending on the qubit bias point.

For each qubit bias point, the dispersive shift 2 __ is calculated using an expression


that accounts for the higher excited states of the transmon qubit and includes corrections
for the Kerr nonlinearity [93], as described in section 2.3.3. We use the dispersive shift
information to calibrate the number of photons in the readout cavity using the ac Stark shift

[42] (see section 6.4.3) and to set the frequency _!_ ro _/_ 2 __ to use for readout photons. We select
a readout frequency halfway between the cavity resonant frequencies corresponding to the
qubit in the ground and first excited states _!_ ro = 1 2 [ _!_ cav ( 0 )+ _!_ cav ( 1 )] =  _!_ cav ( 0 )+ __ . This



1 2 [ _!_ cav ( 0 )+ _!_ cav ( 1 )] =  _!_ cav ( 0 )+ __ . This

_|_ _i_ _|_ _i_ _|_ _i_


choice of readout frequency means that the cavity photon occupation  _n_ is the same whether


the qubit is in state _|_ 0 _i_ or _|_ 1 _i_ , simplifying the analysis of the dependence of transition rates
on  _n_ .

The experimental setup, shown in Figure 8.9(b), is similar to that presented in

the previous chapter. Photons enter the readout cavity, where they acquire a phase shift
that depends on the state of the qubit. These readout photons leave the cavity through the


-----


148

strongly coupled port and pass through four microwave circulators, which isolate the qubit
from the paramp pump. The paramp amplifies the signal, which is then further amplified
by cryogenic and room temperature amplifiers (not shown) and finally mixed down to zero
frequency and digitized. Detailed experimental schematics are shown in Appendix C.

This sample also has a weakly coupled fast flux line, which allows modulation of

the qubit Hamiltonian by noise or coherent signals. The fast flux line has a bandwidth of 2.2
GHz, defined by a reactive VLFX-1350 filter at 700 mK and three lossy impedance-matched
roach filters (see section 5.2.3 and Appendix A for more details) at 4 K, 100 mK, and 50
mK. The roach filters thermalize the line and prevent any high frequency signals in the
re-entrant part of the VLFX filters passband from reaching the qubit. Because the roach
filters have no loss at dc, we can pass substantial ( __ mA) dc currents without causing too
much dissipation on the cold stages and heating the fridge. A 20 dB attenuator at the 4 K
stage provides some low-frequency thermalization.

We calibrate the coupling of the fast flux line to the qubit loop by extracting the

flux-to-qubit-frequency transfer function at the qubit operating point from spectroscopy 12 .
We then measure the qubit frequency using Ramsey fringes and watch the frequency change
as a function of applied dc current through the fast flux line. Combining the frequencyto-flux and current-to-frequency transfer functions gives us a calibration of the flux in the
qubit loop as a function of the current in the fast flux line at base temperature. We can
then use the measured frequency-dependent attenuation of the fast flux line to convert
room-temperature power into a flux in the qubit loop. The coupling is sufficiently weak
(180 mA/ 0 ) that noise from the 50 impedance of the fast flux line should not be the
dominant source of flux noise in the qubit loop for frequencies at or below _!_ _q_ _/_ 2 __ 13 .

The measurement protocol consists of readout pulses lasting 17.5 __ s occurring

every 100 __ s. The long delay ensures that the qubit will fully relax to its thermal ground
state (1.5% excited state population, corresponding to a qubit temperature of 62 mK)
between measurement runs. We take 10 4 individual time traces for each combination of
experimental parameters. The measurement traces are then analyzed using the automated
state extraction algorithm described in section 8.1. All fast flux excitations, both coherent
tones and noise, are applied continuously (not pulsed) independent of whether the readout
is on or o.

###### 8.2.3 ###### State mixing with added flux tones

To test the dressed dephasing theory, we first would like to determine if signals at


the detuning frequency can be mixed with readout photons to cause state transitions, as
postulated. We do this by injecting a continuous microwave tone into the fast flux line of
frequency _!_  ( _n_ ), where we note that depends on  _n_ due to the ac Stark shift [42].
__

This tone produces a small flux oscillation in the qubit loop; the power _P_  of the tone was

12 In this particular sample, we were unable to tune the qubit through a full flux quantum due to weak

coupling to our external coil, so we took spectroscopy over a partial range and fit it to the theoretical
expression for qubit frequency versus flux to get the desired transfer function.


10 __ 12  0 _/_


13 12 The equivalent flux noise in the qubit loop due to quantum fluctuations in the fast flux line is 3 __


Hz at the qubit frequency, several orders of magnitude below the value of the intrinsic flux noise


we extract in section 8.2.4.


-----


149

12

_6_


0.4

0.3

0.2

0.1

_6_


10

_6_


0.0

|spectroscopy excited state population|Col2|
|---|---|


1180 1200 1220 1240 1260 1280

Fast flux frequency/spectroscopy detuning frequency (MHz)

Figure 8.10: Spurious excitation and qubit spectroscopy.

We plot the qubit excited state population (black diamonds) versus the frequency of fast
flux excitation for a fast flux signal of 625 __  0 RMS and a readout cavity occupation  _n_ = 12.

For comparison, we plot independently measured qubit spectroscopy (red line), with the
spectroscopic frequency given in terms of the detuning from the cavity frequency ( _n_ ).

The spectroscopic qubit line has been shifted and broadened by the ac Stark eect. Note
that spurious excitation of the qubit occurs primarily in regions where the frequency of the
fast-flux excitation signal is commensurate with .

varied to produce RMS flux excitations of up to 625 __  0 , corresponding to qubit frequency
fluctuations of 2-4 MHz RMS (depending on qubit bias point). These fluctuations are much
smaller than the ac-Stark-broadened qubit linewidth __ _q_ ( _n_ ) _/_ 2 __ for the values of  _n_ studied.

For each value of  _n_ , we stepped the frequency of the coherent tone through a range from

_6_


_!_  _<_ ( _n_ ) __ _q_ ( _n_ ) to _!_  _>_ ( _n_ ) + __ _q_ ( _n_ ) and stepped _P_  through ten values linearly
_|_ _| _ _|_ _|_

spaced over a factor of 40 in power, as well as a control where _P_  =0. The qubit is detuned
by about 1.2 GHz at our operating point, with _!_ _q_ _/_ 2 __ = 5 _._ 075 GHz.

Figure 8.10 shows the extracted steady state qubit population as a function of

fast flux frequency _!_  for a cavity readout occupation  _n_ of 12 photons and an RMS flux

excitation of 650 __  0 . We observe that spurious excitation occurs primarily in regions

where the frequency of the fast flux tone is commensurate with the detuning frequency
( _n_ ) between the cavity frequency and the ac-Stark-shifted qubit line, which is measured

independently by spectroscopy as described in section 6.4.3.

_6_


A larger plot of experimental results is shown in Figure 8.11. When _P_  = 0, qubit
_6_


_6_

state mixing occurs as long as _!_ 
is within roughly a qubit linewidth of the detuning frequency, and is most noticeable when _!_  = ( _n_ ) . The eect grows stronger with increasing
_|_ _|_


_6_

_P_  . Figure 8.11(f) shows the same bias parameters as Figure 8.11(e), except it displays
the qubit population at the start of the readout as opposed to the steady state population.
This initial excited population is much lower than the steady state excited population and
is essentially independent of _!_  and  _n_ , indicating that the spurious excitation observed in


_6_

(a)-(e) is caused by the presence of readout photons and does not occur when the readout


-----


150


**(a)** **(b)** **(c)**

|0.00 0.25 0.50 Excited state fraction|Col2|Col3|Col4|0. E|Col6|Col7|Col8|Col9|0.50 ction|
|---|---|---|---|---|---|---|---|---|---|
||||||00 xcite|0.2 d sta|5 te f|ra||
|||||||||||


![SlichterThesis.pdf-168-6.png](SlichterThesis.pdf-168-6.png)

![SlichterThesis.pdf-168-8.png](SlichterThesis.pdf-168-8.png)

![SlichterThesis.pdf-168-5.png](SlichterThesis.pdf-168-5.png)

![SlichterThesis.pdf-168-7.png](SlichterThesis.pdf-168-7.png)

![SlichterThesis.pdf-168-0.png](SlichterThesis.pdf-168-0.png)

![SlichterThesis.pdf-168-1.png](SlichterThesis.pdf-168-1.png)

Cavity photon occupation


Cavity photon occupation


Cavity photon occupation

![SlichterThesis.pdf-168-11.png](SlichterThesis.pdf-168-11.png)

![SlichterThesis.pdf-168-3.png](SlichterThesis.pdf-168-3.png)

Cavity photon occupation


**(d)** **(e)** **(f)**


![SlichterThesis.pdf-168-10.png](SlichterThesis.pdf-168-10.png)

![SlichterThesis.pdf-168-9.png](SlichterThesis.pdf-168-9.png)

![SlichterThesis.pdf-168-2.png](SlichterThesis.pdf-168-2.png)

![SlichterThesis.pdf-168-4.png](SlichterThesis.pdf-168-4.png)

Cavity photon occupation


Cavity photon occupation


Figure 8.11: Spurious excitation with coherent fast flux tone.

Parts (a)-(e) show the qubit steady state population during measurement with a coherent
microwave tone applied to the fast flux line. Each panel is for a dierent value of _P_  ,

corresponding to RMS added fluxes of 0 __  0 (a), 230 __  0 (b), 370 __  0 (c), 470 __  0 (d), and
550 __  0 (e). The population data are shown as a function of _!_  and of the cavity photon
occupation  _n_ . The black xs denote the qubit-cavity detuning frequency ( _n_ ) as determined


independently by qubit spectroscopy. The qubit remains primarily in the ground state, even
for large fast flux excitations, except when _!_  ( _n_ ) (within about one qubit linewidth
__

__ _q_ ; note that __ _q_ grows with  _n_ ). The excited state fraction also grows with increasing _P_ 


Part (f) shows the qubit population measured 40 ns after the readout has turned on (the
earliest time point at which we could reliably extract qubit population) with the same _P_ 
as part (e). The qubit is primarily in the ground state even when _!_  ( _n_ ), showing
__

that the excited state population in (e) developed during the measurement and did not
exist before the measurement turned on. There is a small ( __ 10%) excited state population
visible, which does not track with the measured ( _n_ ) as in the other panels. We theorize

this may be the result of mixing between the fast flux tone and the cavity photons in the
very early stages of readout, or potentially of mixing between a residual thermal cavity
population and the fast flux signal when the measurement is o. The vertical color scale is
the same for all panels.


-----


151


0.1

0.01


5 6 7 8

|Col1|Col2|fq = 5.732 GHz fq = 5.582 GHz fq = 5.355 GHz fq = 5.057 GHz|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||


10


5 6 7 8


Cavity photon occupation n

Figure 8.12: Qubit population with no fast flux tone.

This figure plots the steady-state excited state population of the qubit in the absence of
fast flux tones as a function of  _n_ for four dierent qubit frequencies. The higher qubit


frequencies correspond to smaller detunings but also reduced qubit sensitivity to flux __ .
The excited state population has a roughly linear dependence on  _n_ until  _n_ __ 20, at which

point it increases rapidly. The data are plotted on log-log axes to show the large range of
qubit populations and  _n_ .

is o. This fact suggests that the applied flux signals at the detuning frequency are mixing
with readout photons to cause qubit transitions. The small excited state population visible
in Figure 8.11(f) does not track with the measured ( _n_ ) as in the other panels, and may

arise from mixing between the fast flux tone and the cavity photons in the very early stages
of readout (since  _n_ is lower during cavity ring-up than in steady state, the qubit frequency

is shifted less and is smaller), or possibly from mixing between a residual thermal cavity
population and the fast flux signal when the measurement was o.

In the absence of a fast flux tone, we can still observe some spurious qubit exci-

tation with increasing  _n_ , as seen in Figure 8.12. The eect is about 1% additional excited


population per 10 photons cavity occupation, increasing more rapidly at higher photon
numbers (up to __ 10% total for  _n_ __ 40). Since there is no applied fast flux tone, the

dressed dephasing theory postulates that the spurious excitation is due to intrinsic flux
noise at ( _n_ ) in the qubit being upconverted by measurement photons. If so, this repre-

sents a limit on measurement fidelityeven with quantum-limited post-amplificationby
giving a penalty for increasing  _n_ . It would also suggest a route to optimizing measurement

fidelity by addressing sources of low-frequency noise in the qubit.


-----


152

###### 8.2.4 ###### Flux noise measurements

Having determined that signals at ( _n_ ) cause spurious excitation, we can use the

the qubit as a spectrometer to measure flux noise at  14 . To test the qubits response to
noise, we applied flux noise to the qubit loop through the fast flux line and examining spurious excitation during measurement. The noise was generated by amplifying the Johnson
noise of a room-temperature 50 termination, which was then sent to the fast flux line
through a computer controlled attenuator, allowing the strength of the added noise to be
varied (detailed diagrams of the noise generation setup are in Appendix C. The experiment
was performed both with full-spectrum white noise from 10 MHz to 2.2 GHz and with noise
filtered to lie in the range 180 MHz - 2.2 GHz; the steady state qubit populations were
essentially identical between these two types of applied flux noise, suggesting again that
only noise components near ( _n_ ) are responsible for spurious excitation.

Figure 8.13(a) shows the steady state qubit excited population as a function of

cavity photon occupation  _n_ and the spectral density of added flux noise at the detuning



1 _/_ 2
frequency _S_


 (( _n_ )). As anticipated, the qubit excited state population increases with



1 _/_ 2
both  _n_ and _S_



1 _/_ 2 1 _/_

 (( _n_ )). The scaling is roughly linear in  _n_ and quadratic in _S_ 


 (( _n_ )), as


predicted by the dressed dephasing theory. To ensure that the added noise is not causing
excitation in the absence of measurement, we also examined the initial qubit population at
the start of measurement from the same data set, shown in Figure 8.13(b). As expected,
the excited state population at the start of the measurement corresponds to the thermal

1 _/_ 2
population, and is independent of  _n_ and _S_ (( _n_ )).


 (( _n_ )).


If we attribute all spurious excitation to upconverted flux noise, we can extrapolate


these data back to a value of the added flux noise where there is no excitation above the
thermal population, yielding an estimate of the intrinsic flux noise at the detuning frequency.

1 _/_ 2
Using this method, we extract a flux noise spectral density _S_ = 0 _._ 005 0 _._ 002 __  _/_ _p_ Hz at


= 0 _._ 005 0 _._ 002 __  0 _/_
__


Hz at


690 MHz. We can test whether this number agrees with the dressed dephasing expressions
(8.28) and (8.30) by inserting our experimental parameters _g_ , ,  1 , __ , and the slope of the
excited state population versus  _n_ . This latter quantity is determined by fitting a line to the


data in Figure 8.12. Using the extracted numbers, we find that the dressed dephasing theory

1 _/_ 2
predicts a flux noise spectral density _S_ = 0 _._ 004 0 _._ 001 __  _/_ _p_ Hz, in good agreement


= 0 _._ 004 0 _._ 001 __  0 _/_
__


Hz, in good agreement


with our experimentally extracted number.


We can perform cross-checks on this noise level by using Ramsey and Rabi exper-

iments (detailed in section 6.4.2) to measure flux noise in dierent frequency ranges. First,
we measured Ramsey fringes at a rate of one per second for an hour, then fit each fringe
to extract the qubit frequency. We then translated noise in the qubit frequency into an
eective flux noise using the flux-to-qubit-frequency transfer coefficient __ , allowing us to
extract a flux noise spectral density for frequencies below 0.5 Hz. Second, we performed
Rabi oscillations with a zero-detuning Rabi drive tone for several Rabi drive amplitudes.
Each drive amplitude yielded to a dierent Rabi frequency  Rabi , and we extracted the

14 Since the transmon qubit does not couple to charge noise, flux noise should be the main source of

qubit dephasing in our experiment. In this section, we will quote noise on the qubit frequency in terms of
an equivalent flux noise. In principle, the observed spurious excitation could also be due to critical current
noise. Recent experiments suggest, however, that critical current noise in transmon junctions is much weaker
than had previously been supposed [17], and flux noise should be the dominant source of dephasing.


-----


153



(a)

Excited state

population

(steady state)

(b)

Excited state

population


0.3

0.2

0.1

0.0

|20 15 10 5 0 0.02 Added flux noise 0.01|Col2|
|---|---|



0.3

0.2


0.00

|20 15 10 5 0 0.02 Added flux noise 0.01|Col2|
|---|---|



0.00


(start of readout)


0.1

0.0


Figure 8.13: Qubit population with added noise.

Part (a) shows the qubit steady state population as a function of added flux noise and
the number of measurement photons  _n_ in the readout cavity. Part (b) shows the qubit

population immediately after the readout has fully energized. A thermal population of

1.5% is visible, and is equivalent for all values of added flux noise and  _n_ .

decay rate  Rabi for each  Rabi . We used this decay rate to obtain a spectral density of
qubit frequency fluctuations _S_ _!_ _q_ at  Rabi using the relation



3
 Rabi =



3

 1 + 1
4 2



 __ _,_ (8.31)
2


where  1 = 1 _/T_ 1 and  __ = _S_ _!_ _q_ ( Rabi ) [159]. Converting _S_ _!_ _q_ ( Rabi ) to an eective flux
noise gives us data for frequencies between 1 and 20 MHz. These methods are also discussed
in section 6.4.2.

The flux noise values extracted by these methods, as well as those calculated from

our spurious excitation data, are shown in Figure 8.14. We fit the Ramsey data to a 1 _/f_ __


power law [160, 185] to yield the red trend line shown. This fit agrees well with the extracted
values from both Rabi decay and from the spurious excitation data, representing a power
law for flux noise that appears to hold over 11 orders of magnitude in frequency. The fit

1 _/_ 2
coefficients give __ = 0 _._ 58 0 _._ 04 and _S_  (1 Hz) = 1 _._ 4 0 _._ 1 __  0 _/_ _p_ Hz, both of which agree
__ __


 (1 Hz) = 1 _._ 4 0 _._ 1 __  0 _/_

__


Hz, both of which agree


with typical values reported in the literature [185, 186, 187, 188, 189]. We note that other

1 _/_ 2
recent work produced a similar _S_ (1 Hz) but found __ = 0 _._ 9 1 _._ 0 [160, 190]; sample-to-


 (1 Hz) but found __ = 0 _._ 9 1 _._ 0 [160, 190]; sample-to-

__


sample variation in __ of this magnitude has been noted elsewhere [185, 189].


-----


154


10 -5

10 -6

10 -7

10 -8

10 -9

|-5 10 ) ( -6 10 0.01 0.1 Frequency (Hz) Ramsey data Ramsey fit + 95% conf. band Rabi data Spurious excitation data|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||


![SlichterThesis.pdf-172-0.png](SlichterThesis.pdf-172-0.png)

![SlichterThesis.pdf-172-1.png](SlichterThesis.pdf-172-1.png)

![SlichterThesis.pdf-172-2.png](SlichterThesis.pdf-172-2.png)

![SlichterThesis.pdf-172-3.png](SlichterThesis.pdf-172-3.png)

![SlichterThesis.pdf-172-4.png](SlichterThesis.pdf-172-4.png)

10


-2
10


10


10


10


10


10

10


10


Frequency (Hz)

Figure 8.14: Spectral density of flux noise vs frequency.

We plot eective flux noise extracted from Ramsey fringes (black), Rabi oscillation decay
(red triangles), and our measurements of spurious excitation (blue squares). The red line
is a fit to the Ramsey fringe data using a 1 _/f_ __ power law, with the grey shaded area
representing the 95% confidence interval on the fitted value of __ = 0 _._ 58. The inset view
shows a detail of the Ramsey fringe data and fit line.

The correspondence of the low-frequency fit to the extracted flux noise at ( _n_ )

suggests that the universal low-frequency flux noise [191] causes not only qubit dephasing
but also reduces the QND character of circuit QED measurement, in quantitative agreement with the proposed dressed dephasing theory [45, 184]. Further work to improve

low-frequency dephasing noise, such as is being carried out by many groups including ours,
may therefore also provide a route to improved qubit readout fidelity. As _T_ 1 values grow
increasingly longer, the eects of measurement non-idealities like dressed dephasing become
more and more important.

#### 8.3 #### Quantum Zeno eect

The process of quantum measurement forces a quantum system into an eigenstate

of the measured observable. This measurement backaction gives rise to a number of unusual phenomena, including the quantum jumps described in the previous chapter. One
of the most famous examples of measurement backaction is the quantum Zeno eect. The
quantum Zeno eect [169] pertains to the competition between quantum state evolution
and projective measurement; the first tries to change the state of the quantum system of
interest, while the second forces it into an eigenstate. The presence of measurement actually


-----


155

slows the evolution of the quantum system.

The quantum Zeno eect was first observed experimentally in 1990 using an ensem-

ble of trapped ions [192]. Since that time, it has also been seen in single trapped ions [193],
molecules [194], cold atoms [195], photons [196], and the polarization of light [197, 198].
In 2000, the anti-Zeno eect, where a quantum system can decay faster in the presence of
measurement than without, was proposed [199]. A recent theoretical paper looked at the
Zeno eect in the classical limit, as ~ _!_ 0, and found that it vanishes to all orders in ~

[200]. This means that the Zeno eect is truly quantum mechanical, and provides evidence
for the quantum mechanical nature of systems in which it is observed.

The basic theory of the quantum Zeno eect is rather straightforward, the classic


example being a qubit undergoing Rabi oscillations while being periodically measured. We
can write a simple model for the qubits behavior, after Cook [163], using density matrix
formalism. For a qubit undergoing Rabi oscillations at frequency from an on-resonance
drive, we can write the time evolution of the density matrix __ in the rotating frame as
follows:



1
__  00 =
__ 2



_i_ ( __ 01 __ 10 ) (8.32)
2 __



1
__  11 = _i_ ( __ 01 __ 10 ) (8.33)

2 __



1
__  11 =



1
__  01 = _i_ ( __ 11 __ 00 ) _._ (8.34)

2 __



1
__  01 =


Lets say that at time _t_ = 0 we make a measurement of the qubit, projecting it into
the state _|_ 1 _i_ . This sets boundary conditions for equations (8.32)-(8.34) at _t_ = 0, namely
__ 00 = __ 01 = __ 10 = 0 and __ 11 = 1. We can then write down explicit solutions for the

components of the density matrix as a function of time.

__ 00 ( _t_ ) = sin 2 ( _t/_ 2) (8.35)

__ 11 ( _t_ ) = cos 2 ( _t/_ 2) (8.36)



_i_
__ 01 ( _t_ ) = sin( _t_ ) _._ (8.37)

2

The probability _P_ _|_ 0 _i_ ( __ ) or _P_ _|_ 1 _i_ ( __ ) for a subsequent measurement at time __ to find the qubit
in either state 0 or 1 is simply given by __ 00 ( __ ) and __ 11 ( __ ) respectively. Lets consider
_|_ _i_ _|_ _i_
the case when another measurement is made a very short time (a small fraction of a Rabi
period) after the first one, so that the qubit will not have strayed far from being in the state
_|_ 1 _i_ . Mathematically, we can write this by saying  __ __ 1, allowing us to Taylor expand
equations (8.35)-(8.37). We then write the density matrix components as:


__ 00 ( __ ) ( _/_ 2) 2 =  2 __ 2
__ 4


(8.38)

(8.39)


__ 11 ( __ )
__


1 1 ( _/_ 2) 2
__ 2



1
1
__ 2


2



1 ( _/_ 2) 2 = 1  2 __ 2
__ __ __ 4


-----


156



_i_  __
__ 01 ( __ ) _._ (8.40)
__ 2



_i_  __
__ 01 ( __ )
__ 2


The probability for us to observe a qubit state change _P_ sc ( __ ) when we measure at time __ is
_P_ _|_ 0 _i_ ( __ ) = __ 00 ( __ ), or alternatively 1 __ _P_ _|_ 1 _i_ ( __ ) = 1 __ __ 11 ( __ ). We note that in the case where
we do not measure between time 0 and __ , this probability is just given by

_P_ sc ( __ ) =  2 __ 2 _/_ 4 _,_ (8.41)

which increases quadratically with the time __ . Now we can ask what happens if we perform
multiple measurements within the time __ . Lets imagine we perform _N_ measurements evenly
distributed in time; the time between measurements will be _/N_ . To find the probability
_P_ sc ( __ ) of a state change, we need to determine the probability that the qubit will have
remained in state _|_ 1 _i_ throughout all the measurements. We can write down the probability
for the qubit to be in state _|_ 1 _i_ after one such measurement using equation (8.39), which
gives:



 2 ( _/N_ ) 2
_P_ _|_ 1 _i_ ( _/N_ ) = 1 __ 4


(8.42)


Every time a measurement occurs, the qubit is projected back into either _|_ 0 _i_ or _|_ 1 _i_ . As long
as the qubit is projected back into _|_ 1 _i_ each time, the probability in equation (8.42) only
depends on the time _/N_ since the last measurement and not the overall time since _t_ = 0.
The case where the qubit is projected back to _|_ 1 _i_ each time is the one we are interested
in, because we would like to know the probability that the qubit has remained in state _|_ 1 _i_
throughout all the measurements. Because the probability for each interval is the same, we
can write that the total probability to remain in _|_ 1 _i_ given _N_ measurements in time __ is just
the product of the individual probabilities to remain in _|_ 1 _i_ at each interval:


_P_ _|_ 1 _i_ ( _, N_ ) =


_P_ _|_ 1 _i_ ( _/N_ )


 _N_ =



 2 ( _/N_ ) 2
1
__ 4


_N_



(8.43)

(8.44)


Recalling that  __ __ 1, we can expand this form out to give:



 2 __ 2
_P_ _|_ 1 _i_ ( _, N_ ) __ 1 __ 4 _N_



2 __ 2  2 __

= 1
4 _N_ __ 4 _f_


4 _f_ _m_


where _f_ _m_ = _N/_ is the frequency at which measurements are made. We can then find the
probability of state change in the time __ , which is just 1 __ _P_ _|_ 1 _i_ ( _, N_ ):



 2 __
_P_ sc ( _, f_ _m_ ) =

4 _f_ _m_


(8.45)


Lets compare this result with equation (8.41). In the absence of measurement, _P_ sc ( __ ) __ 2 ,
_/_
showing a quadratic dependence of the qubit evolution on time. By contrast, _P_ sc ( _, f_ _m_ ) __
_/_
in the presence of repeated measurements, exhibiting linear rather than quadratic scaling
behavior in time. Furthermore, we notice that the act of repeated measurement actually
decreases the probability of changing states, eectively slowing down the qubit evolution.


-----


157

The stronger (i.e. more frequent) the measurement, the more the qubit evolution is inhibited; this is most readily apparent from the form in equation (8.44). This phenomenon of
inhibition of qubit evolution through repeated measurement is the quantum Zeno eect. In
the limit where becomes infinitesimal, we can talk about the probability of changing states per unit time __ _!_ __ __ , in other words a rate  jump of quantum jumps between states.
Using (8.45) we find

 jump =  2 _/_ 4 _f_ _m_ (8.46)

The model derived above is fairly simplistic, and we must take a little bit of care interpreting
its results. If we carry equation (8.45) out to the limit of infinitely fast measurement, the
transition probability would drop to zero and we would expect to see the qubit frozen
in state _|_ 1 _i_ . This is referred to in the literature as the quantum Zeno paradox, as distinct
from the quantum Zeno eect (which is merely a slowing of qubit evolution). The quantum
Zeno paradox is not realizable in real systems which exhibit radiative or radioactive decay
because at the very short time scales required for the measurement, the energy uncertainty
is so large that the system couples to channels outside the subspace of interest [199, 201].

In our experiments, we have continuous rather than pulsed measurement. However,

the Zeno eect should still hold theoretically in this instance [202], with the time between
individual pulsed measurements replaced by an eective measurement time defined by the
measurement rate  _m_ . If we take __ =1 _/_  _m_ , we have  jump =  2 _/_ 4 _m_ . The model above
also does not account for qubit relaxation processes.

Gambetta and co-workers [91] were able to derive approximate results for the Zeno

eect in the case of a continuous circuit QED measurement. Their analytical expression
only holds in the weak measurement regime, and takes the form


 2
 jump = _,_ (8.47)

2( 2 +  _d_ )


where  2 = 1


2  1 +  _'_ ( 1 = 1 _/T_ 1 and  _'_ is the low-frequency dephasing rate) and  _d_ is


the measurement-induced dephasing rate. The measurement rate  _m_ is given by 1



1 2  _d_ in the


ideal case 15 , so in the limit of low intrinsic decoherence ( 2 0) this expression reduces to
_!_
the same one given in the previous paragraph derived from the simplistic theory.


In the strong measurement regime, one cannot rid the qubit stochastic master


equation used to derive equation (8.47) of cavity eects, and so there is no analytical
formula presented for  jump with strong measurement in [91] . However, the results of full
numerical simulations of the qubit/cavity system seems to suggest a scaling  jump ,

2 _/_
rather than the  jump  of the simple analytical form.
_/_

While the quantum Zeno eect is traditionally described in the time domain, the

expression in (8.47) gives a hint that we can think about it in the frequency domain as well
for our experiment. The qubit linewidth is set by the dephasing; normally, in the absence
of measurement, the qubit linewidth is given by  2 . As can be seen in circuit QED ac
Stark shift data, the presence of measurement photons broadens the qubit line [42]. One
can think of this in terms of the action of the measurement-induced dephasing  _d_ , which

15 We remind the reader that there are two conventions for the relationship between  _m_ and  _d_ which

dier by a factor of two. We use the convention of [91] and [92] here because the expression in (8.47) uses
this convention.


-----


158

with strong measurement is considerably larger than the intrinsic dephasing  _'_ and so sets
the qubit linewidth. As described above, the measurement-induced dephasing is intimately
tied to the measurement rate.

When a qubit undergoes Rabi oscillations, a set of sidebands appear on the qubit

line in the frequency domain, with the distance between the central peak and the sidebands
given by the Rabi frequency. The qubit line and two Rabi sidebands are sometimes referred
to as the Mollow triplet in atomic and optical physics [203]. The presence of the sidebands
is an indication in the frequency domain of the qubits time domain oscillations. Qualitatively, the quantum Zeno eect occurs when the qubit linewidth becomes so broadened by
measurement that one can no longer resolve the Rabi sidebands separately from the main
peak. Mathematically, this can be expressed roughly as  _d_ 2. If we use the relations
__
 _d_ = 2 _m_ __ 1 _/_ , this gives us the rough criterion  __ __ 1, which we note is the essentially
same criterion of fast measurement repeat rate used in equation (8.39) for our derivation
of the simple case of the quantum Zeno eect.

The slowing and eventual disappearance of coherent Rabi oscillations under in-


creasingly strong measurement, an indication of the quantum Zeno eect, has been observed
experimentally by the Saclay group [23]. We have duplicated these results and found that
Rabi oscillations in our qubit/cavity system tend to be suppressed by measurement for
cavity photon occupations  _n_ & 1. Above this value of  _n_ , we should be in the Zeno regime.

For  _n_ & 3, we are able to use our automated jump extraction algorithm to deter-


mine the excitation and relaxation rates of the qubit directly from the individual measurement traces. Our protocol consists of turning on the readout, waiting 3 __ s, and then turning
on a qubit drive tone at the center frequency of the ac-Stark-shifted qubit line _!_ _q_ ( _n_ ). We

leave the qubit drive tone on for 10 __ s. This experiment is repeated 10 4 times each (at
a 100 __ s repetition rate) for a range of values of both  _n_ and qubit drive amplitude. The

measurement setup and qubit sample are the same as were presented in the previous section
on measurement-induced state mixing. We use our automated jump extraction algorithm
to analyze the data. We only analyze data taken while both readout and qubit drive tones
were on, because the rates will dier from when the qubit drive is o. The time in the data
traces before the qubit drive turns on can be separately analyzed to calibrate the amount
of measurement-induced state mixing if we would like to subtract othis eect.

The extracted jump rates are plotted in Figure 8.15. Because the actual  jump


values vary over several orders of magnitude depending on the experimental bias parameters,
we plot scaled values rather than absolute values. We use , the Rabi frequency in the
absence of measurement, as our scaling factor. In part (a), we plot the rate of excitation
from the ground state  (the total  jump =  +  ) as a function of and _p_ _n_  . Because
_"_ _"_ _#_


there is no _T_ 1 contribution to  , the rate should be just that given by the na ve Zeno
_"_


theory, with  =  2 _/_  _m_ . We plot the scaled quantity  2 _/_  on the vertical axis; the use
of the scaling factor  _"_ 2 allows us to readily compare qubit excitation rates which vary over _"_
more than two orders of magnitude as we change and  _n_ , and show that these rates obey


the scaling in (8.47). The data show the quantity  2 _/_  to be more or less independent of
, as suggested by the simple Zeno theory. In addition, we see that  _"_ 2 _/_  increases with
_"_
increasing photon number  _n_ . This demonstrates the quantum Zeno eect; for a given Rabi

drive strength, increasing the measurement strength decreases the rate at which the qubit


-----


159

2

0

|8 6 4 (MHz) 2|8 6 4|
|---|---|



2

0

|8 6 4 (MHz) 2|8 6 4|
|---|---|



Figure 8.15: Quantum Zeno eect.


8x10 8

6

(s -1 )

4

10


![SlichterThesis.pdf-177-0.png](SlichterThesis.pdf-177-0.png)

Part (a) plots the scaled quantity  2 _/_  . For a given value of , this quantity increases
_"_
with increasing  _n_ , showing that  decreases with  _n_ as expected for the quantum Zeno
_"_


eect. The use of the scaling factor  2 lets us readily compare the values of  , which
vary by more than two orders of magnitude in the plotted data. We expect  2 _/_  _"_ to be
_"_
independent of , and this appears to be more or less the case. Part (b) shows plots the
scaled quantity  _/_ ( +  ) for same data set. Since these rates now include the eects
of _T_ 1 decay, we choose the scaling factor (rather than  _"_ _#_ 2 ) as suggested by numerical
simulations of the Zeno eect including decoherence eects given in [91]. Again, for a given
the rate  jump =  +  decreases for increasing  _n_ , showing a slowing of the qubit
_"_ _#_


transition rates with increasing measurement strength.


-----


160

changes state. Based on the simple theory we expect to see a linear dependence on  _m_
and thus on  _n_ , but we instead find a sublinear trend. In addition, the behavior appears to

saturate at very high measurement strengths.


Part (b) shows the same data set, but now plots  jump =  +  . We scale the
_"_ _#_


vertical axis as  _/_ ( +  ), based on the roughly linear (and not quadratic) dependence
_"_ _#_
of  jump on observed in the full numerical simulations in ref. [91], which account for
decay processes as well as the applied qubit drive. Again, we see that the scaled quantity
 _/_ ( +  ) appears to be essentially independent of , but increases with  _n_ , showing that
_"_ _#_


increased measurement strength slows the qubit evolution as expected from the Zeno eect.


Our data clearly show that continuous measurement inhibits qubit state evolution,

demonstrating the quantum Zeno eect. Because the Zeno eect has no classical analogue,
this observation also serves as further confirmation of the quantum mechanical nature of
superconducting qubits.


-----


161

## Chapter 9

# Conclusions and outlook

#### 9.1 #### Future work

The ability to perform continuous qubit state monitoring should enable us to im-

plement quantum feedback and error correction and to create heralded single microwave
photon sources and detectors. These eorts may also be furthered by improving the performance of the qubit and the paramp in subsequent designs.

###### 9.1.1 ###### Quantum feedback and error correction

One potential application of the qubit measurement technology demonstrated in

this thesis is to quantum feedback and error correction. All quantum systems eventually
decohere, albeit at widely varying rates. If we seek to combine these in quantum computers
or quantum simulators where the quantum state of each constituent element cannot be
allowed to decohere, we quickly run into difficulties.

One method for addressing the problem of decoherence is quantum error correction,

where a decoherence-free logical qubit is constructed from an assembly of imperfect physical
qubits [1, 204, 205]. The logical quantum state is stored in a subspace of the multi-qubit
Hilbert space which is protected against decoherence. By making appropriately designed
measurements of the multi-qubit state, one can check for and fix state errors in any of the
physical qubits without actually measuring (and thus aecting) the logical quantum state.
As long as the error rate for each physical qubit is not too high, this technique could in
principle be used to store a logical quantum state indefinitely.

In a simple example, one can entangle three qubits, with two of the qubits serving

as ancillae, and correct for a phase flip or bit flip error in any of the qubits by performing
state-conditional gate operations. At the end, the error has been moved to the states of
the ancilla qubits and the primary qubit recovers to its initially prepared state. One can
then reset the ancillae, re-entangle them with the primary qubit, and repeat. This errorcorrecting three-qubit gate, known as the Tooli gate, has recently been implemented with
trapped ions [206] and superconducting qubits [24, 85, 86].

One could also perform a similar three-qubit error correction protocol based on

measurement, where several fast, high-fidelity projective QND measurements of the pairwise


-----


162

parity of the three-qubit state are performed (these measurements do not aect the encoded
logical qubit state). The resulting information is used to send a sequence of appropriate
pulses to correct any errors in the physical qubits. We could potentially implement the
necessary fast, high-fidelity, QND parity measurements using a scheme like the one described
in this thesis.

Our fast, high-fidelity measurement capabilities could also be used for quantum

feedback, performing weak measurements on the quantum system and using the resulting
information to stabilize a desired quantum state. In one such proposal, periodic weak

measurement of the state of a microwave photon field in a Fabry-Perot cavity is used to feed
back and stabilize Fock states of the field [207]. This proposal was recently demonstrated in
the one of the first experiments showing stabilization of a quantum state through feedback

[208]. Other proposals have shown the possibility of using continuous weak measurement
and feedback to stabilize dierent states on the Bloch sphere [209]. Because the circuit
QED/LJPA combination detailed in this thesis has excellent noise performance, particularly
in the small-signal regime, it should be possible to implement this type of state stabilization
feedback in a superconducting qubit.

One might also use continuous weak measurement techniques to stabilize qubit

dynamics, for example Rabi oscillations. A continuous weak measurement on a qubit undergoing Rabi oscillations can be used to feed back and lock the Rabi oscillations to a
desired frequency [210]. This could allow Rabi oscillations of a qubit to persist for times
much longer than those set by the intrinsic dephasing of the qubit.

###### 9.1.2 ###### Single microwave photon source and detector

The qubit/cavity system with following paramp can also function as a heralded

single photon source and/or detector. The decay of the qubit corresponds to the emission
of a photon at the qubit frequency, which could potentially be directed into a particular
channel and used in quantum optics experiments. The timing of the photon emission is
accessible to the experimenter because we observe a quantum jump at that point. The
time of absorption of a single resonant microwave photon by a qubit could be determined
in a similar manner. Such heralded single-photon emitters and detectors could be used to
demonstrate quantum eects such as antibunching of microwave photons [211].

###### 9.1.3 ###### Improved qubits

Great strides have been made recently in the eort to improve the coherence times

of superconducting qubits, with the 3D transmon design demonstrating coherence times
reliably longer than 20 __ s [17]. Such long-lived qubits would be useful for extensions of the
quantum jump experiments presented in this thesis for a variety of reasons. First, the longer
coherence time would allow for improved single-shot fidelity. Secondly, the longer coherence
times would allow more subtle measurement backaction eects to become apparent. We
could harness this to make further measurements of flux noise and explore the behavior of
flux noise at high frequencies for a variety of qubit parameters and designs.

In addition, the ability to make single-junction versus SQUID-loop transmon

qubits in the 3D transmon configuration could potentially be used to reduce the eects


-----


163

of spurious qubit state mixing by preventing flux noise from causing noise on the qubit
frequency. This could point the way to improving the QND nature of circuit QED readout
at high readout power.

Although the circuit QED techniques used in this thesis were applied to the readout

of a superconducting qubit, circuit QED coupling and readout have also been successfully
used with other solid state quantum systems such as lateral quantum dots and electron
spin ensembles [212, 213, 214]. The addition of a following paramp, as described in this
thesis, could enable fast, high-fidelity QND state monitoring for these and other solid state
quantum systems coupled to a superconducting readout cavity.

###### 9.1.4 ###### Parametric amplifier development

The LJPA used to amplify the quantum jump signal has excellent gain and noise

properties but suers from limited dynamic range. Improvements in the dynamic range of
the amplifier could pave the way for use in a much broader range of quantum information
experiments. One potential method for improving dynamic range would be to use arrays of
SQUIDs rather than just a single SQUID; the array would have the same inductance as our
current single-SQUID design but would have a considerably higher critical current, which in
turn would increase the pump power and the dynamic range. However, there are potential
difficulties with such an arrangement because the array would have multiple normal modes
and might not be stable to phase slips when driven into the paramp regime.

Another possibility for improving dynamic range would be to use nulling feedback

to keep the pump power in the linear regime of the transfer function. Such feedback would
work in a similar way to the classic flux-locked loop used to extend the dynamic range
of the dc SQUID amplifier. The tradeoin such a system would be reduced amplifier

bandwidth, but this issue could potentially be ameliorated by the use of fast electronics or
cryogenic components to make the feedback loop. Modern dc SQUID amplifiers can operate
in flux-locked loop configurations with 20 MHz of bandwidth using fast feedback electronics

[215].

A dierent approach to the dynamic range and bandwidth problem would be to

develop a new type of superconducting parametric amplifier. One potential design, called
the traveling wave parametric amplifier or TWPA, uses a nonlinear transmission line loaded
with Josephson junctions to create a transmission-mode microwave amplifier analogous to an
optical fiber parametric amplifier. Because the TWPA does not have resonant structures, it
should be inherently broadband and tunable over a wide frequency range simply by changing
the pump frequency. Initial theoretical calculations suggest that the TWPA could achieve
close to 1 GHz of instantaneous bandwidth with a 6 GHz pump and gains on the order
of 15-20 dB. The dynamic range of the TWPA should be considerably larger than than of
the LJPA, with saturation occurring at powers at least 20 dB higher than for the LJPA.
These features might allow for the frequency multiplexing of a number of dierent qubit
readout signals on a single amplifier channel, aiding in the scalability of quantum computing
architectures based on superconducting qubits read out with parametric amplifiers. In

addition, the fact that the TWPA is a transmission amplifier, and that the pump can
be very far detuned from the amplified signals, may reduce the need for bulky, expensive
microwave circulators between the readout cavity and the amplifier.


-----


164

(a) (b)


20

15

5

0

-5

-10

-15

-20

![SlichterThesis.pdf-182-0.png](SlichterThesis.pdf-182-0.png)

3.0 4.0 5.0 6.0 7.0

Frequency (GHz)


-40

-45

-50

-55

-60

-65

-70

-75


![SlichterThesis.pdf-182-1.png](SlichterThesis.pdf-182-1.png)

5.85 5.90 5.95 6.00 6.05 6.10 6.15

Frequency (GHz)


Figure 9.1: Preliminary TWPA performance.

Part (a) shows the gain of the TWPA relative to a microwave through with the pump on
and o. The pump frequency is 4.8 GHz. Part (b) shows the output spectrum of a TWPA
and a microwave through with a pump at 6 GHz and small signal detuned by 100 MHz.
The TWPA shows both signal and idler gain, with a signal gain of 9 dB and an output
signal-to-noise improvement of 4 dB relative to the through.

Some preliminary gain and noise data from a TWPA prototype are shown in Figure

9.1. The TWPA has about 10 dB of gain relative to a microwave through, with more than
500 MHz of instantaneous 3 dB bandwidth. The noise performance is analyzed in part (b);
the TWPA shows both direct and trans gain and gives a signal-to-noise ratio improvement
of about 4 dB over a microwave through. The TWPA fabrication process is complex, and
is currently under development.

#### 9.2 #### Conclusions

This thesis showed the first observation of quantum jumps in a superconducting

qubit, a macroscopic quantum system. The work described harnessed the combination

of projective QND readout oered by the circuit QED architecture and fast, quantumlimited amplification enabled by a superconducting parametric amplifier, the LJPA. The
resulting observation of quantum jumps brings quantum measurement capabilities to solid
state quantum systems which had previously been the exclusive domain of atomic and
optical physics. The ability to perform continuous high-fidelity qubit monitoring points the
way to quantum error correction and feedback in solid state systems.

The continuous high-fidelity monitoring capabilities demonstrated here allow the

quantification of measurement backaction in superconducting qubits. They show the perhaps surprising result that low-frequency noise is the culprit in measurement-induced qubit
state mixing at high readout powers in circuit QED, a problem that has limited the fidelity
of circuit QED readout. This points the way for to the unification of several disparate


-----


165

research directions in the superconducting qubit community, namely the quest to maximize
readout fidelity and the quest to understand and reduce the sources of universal flux noise.
We also observe the quantum Zeno eect.

One way forward is to use the techniques described in this thesis to enable quantum

error correction. This pursuit is one of the major goals in contemporary experimental

quantum information research. The successful implementation of quantum error correction
to create long-lived logical qubits would be an important breakthrough in the quest to
build quantum computers and quantum simulators. We hope that some of the work in this
thesis can contribute to this and other research eorts in the future, helping to advance our
capabilities and knowledge as we explore the fascinating quantum world.


-----


166

## Appendix A

# Microwave roach motel filters

#### A.1 #### Design and modeling of roach filters

The roach filters are implemented as a length of lossy stripline transmission line

in a copper box. The center trace of the stripline is a piece of copper tape cut to the

appropriate width, while the dielectric is a magnetically loaded silicone rubber microwave
absorber, Emerson & Cuming Eccosorb MFS-117. We seek to impedance-match the filters
to the 50 microwave environment, which is accomplished by choosing the width of the
stripline center conductor. The impedance _Z_ is related to the capacitance _C_ _`_ and inductance
_L_ _`_ per unit length of the transmission line as [135]


_Z_ =


_L_
_C_


_p_ _L_ _`_ _C_ _`_

_C_ _`_


_v_ _p_ _C_ _`_


(A.1)


where _v_ _p_ is the phase velocity of the TEM mode propagating down the stripline. We can
express this phase velocity in terms of the permittivity _"_ and permeability __ of the dielectric
as:

1
_v_ _p_ = _p_ _"._ (A.2)

We note that these are the absolute (not the relative) permittivity and permeability, and
that in general they are complex and frequency-dependent. We can write them in terms of
their real parts _"_ _0_ and __ _0_ and their imaginary parts _"_ _00_ and __ _00_ as

_"_ ( _!_ ) = _"_ _0_ ( _!_ ) + _i"_ _00_ ( _!_ ) (A.3)

__ ( _!_ ) = __ _0_ ( _!_ ) + _i_ _00_ ( _!_ ) _._ (A.4)

To determine the impedance, all that remains is to calculate the capacitance per unit length
_C_ _`_ . We can solve for this in the electrostatic approximation, giving [135]


_C_ _`_ = _W_ e


_n_ =1
_n_ odd


( _n_ ) 2 _"_ cosh( _nb/_ 2 _a_ )

_,_ (A.5)
2 _a_ sin( _nW_ e _/_ 2 _a_ ) sinh( _nb/_ 2 _a_ )


-----


167

![SlichterThesis.pdf-201-0.png](SlichterThesis.pdf-201-0.png)

Figure A.1: Roach filter stripline geometry.

This figure shows a cross-section of a roach filter stripline with box width _a_ and height _b_
and center strip width _W_ and thickness _T_ . The Eccosorb dielectric is characterized by the
real and imaginary parts of the permittivity and permeability _"_ _0_ , _"_ _00_ , __ _0_ , and __ _00_ .

where _a_ is the width of the box, _b_ is its depth, and _W_ e is the eective width of the center
strip. The sum in (A.5) is over odd values of _n_ only. Although it is nominally a sum over all
odd values of _n_ , in practice one can truncate the sum at _n_ __ 10 3 __ 10 4 without impacting
the result. The eective strip width _W_ e is given by [146]



_T_
_W_ e = _W_ +


ln(2 _b/T_ ) + 1


(A.6)


where _W_ and _T_ are the width and thickness of the strip, respectively. Figure A.1 shows
the cross-section of a roach filter stripline with dimensions labeled.

With these expressions, we can write down an expression for the impedance of the

roach filter in terms of its cross-sectional geometry and the permittivity and permeability
of the Eccosorb dielectric:


_p_ _"_
_W_ e


2 _a_ sin( _nW_ e _/_ 2 _a_ ) sinh( _nb/_ 2 _a_ )

_._ (A.7)
( _n_ ) 2 _"_ cosh( _nb/_ 2 _a_ )


_Z_ =


2 _a_ sin( _nW_ e _/_ 2 _a_ ) sinh( _nb/_ 2 _a_ )


_n_ =1
_n_ odd


The values of _"_ and __ for Eccosorb MFS-117 have been measured at various frequencies
by the manufacturer and are presented in the data sheet [216]. These values change substantially with frequency, so the impedance of the filter will vary with frequency as well.
However, by choosing the geometry appropriately it is possible to keep the impedance in
the range 50 __ 7 out to 18 GHz.

Figure A.2 plots the real and imaginary parts of _"_ and __ (in units of the vacuum


The values of _"_ and __ for Eccosorb MFS-117 have been measured at various frequencies
by the manufacturer and are presented in the data sheet [216]. These values change substantially with frequency, so the impedance of the filter will vary with frequency as well.
However, by choosing the geometry appropriately it is possible to keep the impedance in
the range 50 __ 7 out to 18 GHz.


permittivity and permability _"_ 0 and __ 0 , respectively) as a function of frequency. We see
that the loss is a combination of dielectric loss and magnetic loss at low frequencies, but
that magnetic loss dominates as we move to higher frequencies. The magnetic loss tangent
__ _00_ _/_ _0_ is greater than 1 above 8 GHz.


-----


164

5.0

4.5


45

40

35

30

25

20

15

10


4.0

3.5

3.0

2.5

2.0

1.5


1.0

0.5

0.0


![SlichterThesis.pdf-202-0.png](SlichterThesis.pdf-202-0.png)

Figure A.2: Permittivity and permeability of Eccosorb MFS-117.

This figure plots the real and imaginary parts of the permittivity and permeability _"_ _0_ , _"_ _00_ ,
__ _0_ , and __ _00_ as a function of frequency in units of _"_ 0 and __ 0 . The magnetic loss tangent __ _00_ _/_ _0_

increases with frequency; this is the primary loss mechanism for Eccosorb.

The filter boxes are milled from oxygen-free high-conductivity copper, and consist

of a cavity with holes at the ends for connecting to SMA bulkhead connectors designed for
launching to microstrip (AEP/Radiall 9308-9113-001). Matching copper lids screw down
on top to seal the cavity and finish the filter. The impedance depends on the cross-sectional
dimensions of the cavity and the center trace as described above, while the filter cuto
frequency _f_ 3dB depends on the length of the cavity [148]. Our standard roach fiter has
_f_ 3dB = 1 _._ 3 GHz using a cavity 9.5 mm long, 8.9 mm wide, and 4.1 mm deep, with a stripline
center conductor 1.35 mm wide and 50 __ m thick. One can decrease the cutofrequency
by making a longer cavity, however making the cavity shorter to raise the cutofrequency
tends to give rise to re-entrant behavior above 30 GHz due to direct coupling between the
pins of the SMA launches. We are working to develop roach filters using FIRAM microwave
absorber material [217, 218] instead of Eccosorb; the FIRAM has lower loss, allowing higher
cutofrequencies. FIRAM is a carbon-loaded silicone rubber which shows dielectric loss
instead of magnetic loss, and has been shown to be lossy to THz frequencies. However, its
performance at millikelvin temperatures has not yet been tested.

The stripline is fabricated by cutting a piece of Eccosorb with a razor blade which

will fit snugly in the copper box with no gaps. This Eccosorb is then cut in half and one half
is placed in the box. A piece of copper tape cut to the correct dimensions with a razor blade
is used for the center conductor; we remove the sticky backing of the tape with acetone to
facilitate filter assembly. The tape is soldered to the SMA launch pins and the second half
of the Eccosorb is placed on top. The lid of the box is then screwed on and the filter is
complete.


-----


165

(a) (b)


-20

-40

-60

-80


-10

-20

-30


![SlichterThesis.pdf-203-0.png](SlichterThesis.pdf-203-0.png)

![SlichterThesis.pdf-203-1.png](SlichterThesis.pdf-203-1.png)

10 15 20 25 30 35

Frequency (GHz)


1.3 1.4 1.5 1.6 1.7

Frequency (GHz)


Figure A.3: Millikelvin S-parameters of roach filters.

Part (a) shows the filter attenuation _S_ 21 at 300 K and 50 mK, along with the noise floor of
_|_ _|_
the measurement. The noise floor rises with frequency due to attenuation in the cryogenic
coaxial lines. Part (b) shows the reflection _S_ 11 at 25 mK from an open circuit (bold red),
_|_ _|_
a 50 termination (black), a 70-mm-long roach filter with the opposite end open-circuited
(empty blue circles), and a standard 9.5-mm-long roach (at 50 mK) connected to a 50 
load (filled blue circles).

#### A.2 #### Millikelvin filter performance

We measured the characteristics of roach filters at dilution fridge temperatures,

which we reported in ref. [155]. Measurements of the transmission and reflection properties
of several roach filters are shown in Figure A.3. We found that the frequency-dependent loss
of the roach filters was essentially unchanged between room temperature and 50 mK, and
that in both cases the attenuation of the filter was below the noise floor of our measurement
at frequencies above 15 GHz. In addition, we found that the filters remained impedancematched at low temperatures, with return loss better than 10 dB.

We also examined the thermalization of a 70-mm-long roach filter at millikelvin

temperatures by measuring the noise power emitted in the filter stopband. A direct measurement of the Johnson noise emitted from the filter is hampered by 1 _/f_ drifts in the gain
and system noise temperature of the measurement chain, which limit the maximum integration time. These drifts limit our maximum measurement resolution to approximately
150 mK for a direct noise measurement.

To circumvent this problem, we used a dierential measurement technique analo-

gous to a Dicke radiometer, shown schematically in Figure A.4. We used a Hittite switch
(see section 5.2.2) located on the mixing chamber stage of our refrigerator to chop between
our filter and a 40 dB NiCr attenuator, both anchored to the mixing chamber plate. The
noise from both sources was amplified, bandpass filtered, and then detected with a zero-bias
Schottky diode. The dierence in noise power emission between the filter and the attenua-


-----


166


T =25-500mK HEMT
bath switch


Hittite


switch


@4K


f=1.5 GHz
B=75 MHz


10dB
@1K

20dB
@4K


amplifier detector


amplifier


![SlichterThesis.pdf-204-0.png](SlichterThesis.pdf-204-0.png)

Figure A.4: Thermalization measurement setup.

We measure the noise power emitted by a 70-mm-long roach filter and a NiCr attenuator
anchored to the mixing chamber stage of a dilution fridge. A Hittite switch is used to chop
back and forth between the filter and the attenuator in a Dicke radiometer configuration.
The noise emitted by each is amplified, bandpass filtered, and detected with a zero-bias
Schottky diode used as a power detector. The noise power signal is measured synchronously
with a lock-in amplifier. An external generator is used to provide a calibration signal

tor was measured synchronously with a lock-in amplifier. A signal generator connected to
the attenuator was used for calibrating the absolute noise power.

This radiometric technique allows us to compare the noise radiated from the filter

to that of a NiCr attenuator, which is believed to thermalize well at millikelvin temperatures.
To quantify the temperature dierence between the filter and the attenuator, we set the
calibration generator power _P_ cal = __ 135 dBm and measured the in-phase quadrature of the
lock-in signal


_V_ lockin = _Gk_ _B_ _B_ ( _T_ atten __ _T_ filter ) _,_ (A.8)

where is the gain of the measurement chain, __ is the power to voltage rectification ratio of the diode, _B_ = 75 MHz is the bandwidth of the bandpass filter on the output, and _G_
_T_ atten and _T_ filter are the noise temperatures of the attenuator and filter respectively. To
extract the temperature dierence, we used two independent calibration procedures. First,
after each data point acquisition, five calibration points with dierent values of _P_ cal ranging
from -63 dBm to -78 dBm were recorded. In this case, the lock-in signal is

_V_ lockin = _G_ [ _AP_ cal + _k_ _B_ _B_ ( _T_ atten __ _T_ filter )] (A.9)

where _A_ = __ 76 dB is the attenuation of the stainless steel coaxial input line and associated
attenuators (measured independently at room temperature). This room temperature value
of _A_ is accurate to within a few dB when the fridge is cold. Given _A_ and _P_ cal , we can
find  _T_ __ _T_ atten __ _T_ filter from the _V_ lockin = 0 intercept of (A.9), independent of the system
gain. As a crosscheck, we connected the Hittite switch to the NiCr attenuator, varied the
attenuator temperature from 200 mK to 600 mK, and recorded the diode output voltage.


-----


167

![SlichterThesis.pdf-205-0.png](SlichterThesis.pdf-205-0.png)

![SlichterThesis.pdf-205-1.png](SlichterThesis.pdf-205-1.png)

0 10 20 30 40

Time (hrs)

Figure A.5: Thermalization measurement.

The noise temperature dierence  _T_ between the filter and the attenuator as a function
of time is shown in the top panel. The bottom panel shows the temperature of the mixing
chamber stage on the same time axis. The long tick marks on the horizontal axis denote
the times when the refrigerator temperature was changed. At temperatures above 150 mK,
each temperature step is accompanied by a spike in  _T_ ; the inset shows an expanded view
of one such  _T_ spike. The time of the temperature change is shown with a dotted line.

This yielded the product _G_ which can also be used to obtain  _T_ from _V_ lockin using (A.8).
These two methods yield values of  _T_ that agree to within 30%. The first calibration

procedure is carried out for every data point, while the latter was performed only once for
the entire measurement. However, the close agreement of these two calibrations indicates a
high degree of immunity to 1 _/f_ noise. Additionally, we measured the insertion loss of both
channels of the Hittite switch and calculate the eects of transmission imbalance and noise
emission to be negligible.

In Figure A.5, we plot the measured  _T_ as a function of time, together with the

temperature of the thermal bath as it is varied between 25 mK and 500 mK. The data
indicate that the attenuator and the filter have temperatures within a few millikelvin of
each other down to 25 mK. At high temperatures ( _>_ 150 mK), the measured temperature
dierence between the attenuator and the filter is within the experimental uncertainty, and
each temperature step is accompanied by a spike in  _T_ : a sharp increase followed by a
slower decrease, shown in the figure inset. We interpret this as the attenuator rapidly

thermalizing to the new bath temperature, followed by the filter equilibrating with a longer
time constant. Note that the spike polarity is reversed when we step the temperature

downwards. Below 150 mK, the filter appears to be slightly colder than the attenuator,
even after several hours of measurement.

These data show that the roach filters maintain both their loss and reflection

characteristics at base temperature, and that they thermalize as well as a NiCr attenuator
even down to millikelvin temperatures. This makes the roach filters very useful for low-


-----


168

temperature applications requiring low loss at dc but high loss at microwave frequencies
(such as the thermalization of a fast flux line), and for applications requiring a microwave
stopband that extends to very high frequencies (such as measurements of loss in high- _Q_
resonators).


-----


169

## Appendix B

# Fabrication recipes

#### B.1 #### Resist Spinning

This recipe gives the standard MMA/ZEP bilayer, with about 250-300 nm of ZEP

and 1 __ m of MMA. Other work has used longer bake times for the MMA layer, but we
found that 5 minutes is sufficient.

1. Procure substrate (wafer or chip) and place on spinner chuck, checking alignment

carefully.

2. Coat substrate with MMA/MAA EL-13 resist.

3. Spin at 3000 rpm for 60 sec.

4. Remove substrate and bake on 180 __ C hot plate for 5 min.

5. Return substrate to spinner chuck, aligning carefully.

6. Coat substrate with ZEP-520A7 resist.

7. Spin at 3000 rpm for 60 sec.

8. Remove substrate and bake on 200 __ C hot plate for 3 min.

9. Remove from hot plate and heat sink to cool substrate. Put resist-coated substrate

in a dark place until ready for use.

#### B.2 #### E-beam lithography


Typical doses for the ZEP/MMA bilayer with ice-water-bath development are 210

__ C/cm 2 for fine features written at small currents (e.g. junctions), 240-270 __ C/cm 2 for
coarser features written with larger currents (e.g. resonators), and 50-60 __ C/cm 2 for resist
undercut boxes. ZEP resist is available from the Nippon Zeon Corp.; all other resists in this
thesis were purchased from Micro-Chem Corp. Gold colloid and spring clips for lithography
can be purchased from Ted Pella. Faraday cup parts and gold standards can be purchased


-----


170

from EB Sciences. The NPGS website (http://www.jcnabity.com/) has a listing of vendors
for electron beam lithography supplies.

1. Spin resist on a full wafer or smaller sample, then dice as appropriate.

2. Mount the sample on an SEM stub. The wafer should be held down with spring clips.

3. Put a toothpick in the bottle of gold colloid and let it sit there for a minute or two.

Remove the toothpick and put a small drop of colloid at each corner of the sample.
Allow the drops to dry completely.

4. Place the SEM stub in the SEM, pump down, and turn on the beam.

5. Using the computer controls, move around until you find the Faraday cup. Focus on

the edge of the Faraday cup, link the stage Z to the focal distance, and zoom in to
the Faraday cup hole so the picture is black.

6. Make a notation of the beam current on all spot sizes to be used for lithography.

7. Zoom out and move to the gold standard. Focus, link the stage Z, and adjust the

stage height until the working distance is 10 mm.

8. Adjust the focus and astigmatism until the image is as clean as you can make it.

Adjust the lens alignment using the modulator. Link the Z of the stage to the focal
distance.

9. In NPGS, select Direct Stage Control and skip rotation correction. This prepares

the system to accept dynamic focus correction points.

10. Zoom back out to low magnification and find a corner of the sample. Find where the

gold colloid was deposited and zoom in on that area. Manually adjust the stage Z
until the image comes into good focus.

11. Find an isolated gold ball sitting on the resist (not on a piece of debris) and focus on

it. Optimize the focus with the computer controls.

12. Make a new point on the stage map for your location, then add the focus point to

NPGS dynamic focus correction list.

13. Move to another corner, then repeat steps 11 and 12. Do this for all drops of colloid

placed on the sample.

14. Accept the dynamic focus points in NPGS, then hit Beam O and ensure the

electrostatic beam blanker is set to External.

15. Check to make sure the doses, beam currents, magnifications, and spot sizes are

correct in the NPGS run file.

16. Set the SEM scan mode to External.

17. Using the stage map, move to the desired location to begin lithography.

18. Use the NPGS program to perform lithography.


-----


171

#### B.3 #### Resist Development

1. Fill the bath beaker with ice, then add water to make slush. Place the beaker inside

its thermal insulation jacket.

2. Pour n-amyl acetate into the small developer beaker and place this beaker in its holder

inside the bath beaker. Ensure that the developer is steady and no water gets in the
beaker. Place the lid on the bath beaker to reduce condensation in the developer.

3. Wait 5 minutes for developer to cool.

4. Using tweezers, plunge the sample into the cold n-amyl acetate and agitate gently for

60 seconds.

5. Remove sample and blow dry immediately. DO NOT rinse (this may cause overde-

veloping). Blow dry for at least 15 seconds to warm the sample so no condensation
forms on its surface.

6. Using tweezers, plunge the sample into a beaker of room-temperature 1:3 MIBK:IPA

and agitate gently for 4 minutes (large undercut features) or 1 minute (small undercut
features).

7. Remove the sample and plunge it into a beaker of isopropanol, agitating gently for 15

seconds.

8. Remove sample and blow dry.

#### B.4 #### Thin film deposition

Typical evaporation parameters for qubit samples are layers of 20-30 nm for the

first evaporation and 70-90 nm for the second evaporation, with angles of __ 18 __ , __ 30 __ , or
__ 5 __ _/_ + 30 __ , depending on the design. Typical oxidation parameters are 10 Torr of 5% O 2
in Ar for 10 minutes. Paramp samples have evaporation thicknesses of 60 and 80 nm for
the two layers at angles of __ 30 __ . Oxidation parameters are typically 8 Torr of 5% O 2 in Ar
for 8 minutes.

1. Place the sample in the evaporator, taking care to align the sample axis appropriately

to the stage rotation axis.


2. Close the load lock and pump down. Once the load lock pressure is below 1 __ 10 6

Torr, open the load lock gate valve and allow the cryo pump to pump on the load lock
as well.

3. Allow at least 4 hours, or preferably overnight, for the load lock to be pumped by the

cryo pump.

4. Fill and flush the oxidation volume with ArO 2 three times, with a fill pressure of 100

Torr.


-----


172

5. Fill the oxidation volume to the correct pressure of ArO 2 .

6. Allow the chamber to return to base pressure.

7. Set the stage to the first angle and turn on the e-gun.

8. Slowly turn up the e-gun current until a rate appears, then continue until it settles.

Pre-evaporate 50-60 nm of aluminum.

9. Open the shutter and deposit the desired thickness of aluminum.

10. Turn the e-gun down slowly until it is o. Close the load-lock gate valve and the

turbo gate valve.

11. Open the oxidation volume to the load lock and allow the oxidation to proceed for

the desired time.

12. Turn on the turbo pump and its backing pump 25 seconds before oxidation is to

complete, then open the turbo gate valve at the completion time. Allow the load lock
to pump out to below 5 __ 10 7 Torr.

13. Open the load lock gate and allow the load lock to pump down.

14. Set the stage to the second angle for evaporation and turn on the e-gun.

15. Slowly turn up the e-gun current until a rate appears, then continue until it settles.

Pre-evaporate 50-60 nm of aluminum.

16. Open the shutter and deposit the desired thickness of aluminum.

17. Turn the e-gun down slowly until it is o. Return the sample stage to an angle of 0 __ .

18. Close gate valves, vent load lock, and remove sample.

#### B.5 #### Silicon nitride deposition

The silicon nitride for the paramp capacitors is deposited on top of the Nb ground

planes and Si substrate using plasma-enhanced chemical vapor deposition (PECVD). We
use the oxford2 machine in the UC Berkeley Nanolab for this purpose. Deposition is performed at 350 __ C substrate temperature with 100 W of RF power, using 100 sccm of 10%
SiH 4 /90% Ar and 30 sccm NH 3 as precursor gases. The deposition rate is roughly 15-20
nm/minute, and we grow between 120 and 180 nm of nitride depending on the desired
specific capacitance.


-----


173

## Appendix C

# Experimental schematics

These schematic diagrams show the arrangement of components used for our ex-

periments. Filters and splitters not labeled with the name of a manufacturer are from

Mini-circuits. Figure C.1 shows the setup used to generate broadband white noise for the
experiments in section 8.2.4. Figure C.2 shows a typical room temperature experimental
setup, including qubit and readout pulse generation, paramp pump generation, demodulation, and digitization. Coherent fast flux tones, if desired, are applied with a dierent
generator (not shown).

Figures C.3 and C.4 show the wiring arrangement inside the fridge for the ex-

periments performed in Chapters 7 and 8, respectively. These figures do not show the

low-frequency wiring. The current for flux biasing of the qubit and paramp samples is sent
to the flux bias coils via filtered low-frequency superconducting lines (copper above 4 K).
The voltage signals used to operate the Hittite switch are sent via filtered low-frequency
manganin lines. The signals to operate the Radiall switches are sent on unshielded superconducting looms (copper above 4K).


Mini-circuits

ZX60-8008E-S+


Miteq

AFS3-00100800-32-LN

50 


Mini-circuits

ZKL-2

to fast flux

injection line

|Col1|10 dB|Col3|10 dB|VLF-2250+|
|---|---|---|---|---|
||10 dB||10 dB|VLF-2250+|
|LabBrick LDA-602 Miteq (0-63 dB) AFS4-00100800-14-10P-4|||||


Figure C.1: Fast flux noise generation.

Circuit for generating broadband white noise 10 MHz - 2.5 GHz from amplified Johnson
noise of a 50 termination. The strength and frequency spectrum of noise at the output
can be characterized using a spectrum analyzer. This circuit was used to generate flux noise
for dressed dephasing experiments in Chapter 8.


-----


174

to paramp pump

injection line

to qubit/cavity


from network

analyzer


from network


(paramp


Agilent
8257C


pump)


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||


![SlichterThesis.pdf-212-0.png](SlichterThesis.pdf-212-0.png)

Figure C.2: Typical room temperature wiring.

Typical room temperature wiring for quantum jump experiments. A network analyzer

(not shown) is connected to the directional couplers as labeled to perform paramp tune-up
without needing to change the circuit. After tune-up, the network analyzer is removed and
replaced with 50 terminations. The room temperature circulators are all from DiTom,
model D3I4080. The small unlabeled squares represent inner-outer DC blocks (Inmet 8039).


-----


175


70 K

4 K

700 mK

(still)

100 mK

30 mK

(mixing

chamber)

|Col1|Col2|
|---|---|
|||


|qubit/cavity injection line|Col2|out lin|put e|Col5|Col6|paramp injection line|Col8|
|---|---|---|---|---|---|---|---|
|dB 20 50 ||HEMT||||VHF-3800 20 dB||
|||||||||
|||||||||
|||||||||
|ng chamber to 4K|VHF-3800 10 dB|||||||
|Nb coax cable mixi|10 dB|||||||
|50  dB dB 20 20 Hittite HMC547 to other . PARAMP samples . . Krytar qubit/cavity 104020020 sample Radiall||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|qubit/cav sampl||||||||


switch


Radiall


Not shown: flux bias coils for qubit and paramp (filtered low-freq. superconducting lines)
control lines for switches (superconducting for Radiall, manganin for Hittite)

Figure C.3: Fridge wiring for Chapter 7 experiments.


-----


176






chamber)


70 K

4 K

700 mK

(still)

100 mK

30 mK

(mixing


|cavity ction ne|fast flux injection line|output line|Col4|paramp injection line|Col6|
|---|---|---|---|---|---|
|20 dB|roach filter 1.3 GHz 20 dB|HEMT LNF-LNC4_8A 50 ||VHF-3800 20 dB||
|||||||
|||||||
|||||||
|||||||
|VHF-3800 10 dB|||ng chamber to 4K ing chamber to 4K|||
|10 dB|roach filter VLFX-1350 1.3 GHz||Nb coax cable mixi Nb coax cable mix|||
|naren 4020||||||
|||||||
|||||||


![SlichterThesis.pdf-214-0.png](SlichterThesis.pdf-214-0.png)

Figure C.4: Fridge wiring for Chapter 8 experiments.


-----

