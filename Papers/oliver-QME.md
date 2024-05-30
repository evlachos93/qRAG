
# Error mitigation via stabilizer measurement emulation

A. Greene, 1 M. Kjaergaard, 1 M. E. Schwartz, 2 G. O. Samach, 1, 2 A. Bengtsson, 1, 3 C. McNally, 1 M. OKeeffe, 2

D. K. Kim, 2 M. Marvian, 1, 4 A. Melville, 2 B. M. Niedzielski, 2 A. Veps al ainen, 1 R. Winik, 1 J. Yoder, 2

D. Rosenberg, 2 S. Lloyd, 1, 4 T. P. Orlando, 1 I. Marvian, 5 S. Gustavsson, 1 and W. D. Oliver 1, 2, 6, 7

1 _Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
2 _MIT Lincoln Laboratory, Lexington, MA 02421, USA_
3 _Microtechnology and Nanoscience, Chalmers University of Technology, G_ _oteborg, SE-412 96, Sweden_
4 _Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
5 _Departments of Physics & Electrical and Computer Engineering, Duke University, Durham, NC 27708, USA_
6 _Department of Physics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
7 _Department of Electrical Engineering & Computer Science,_
_Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
(Dated: February 12, 2021)

Dynamical decoupling (DD) is a widely-used quantum control technique that takes advantage
of temporal symmetries in order to partially suppress quantum errors without the need resourceintensive error detection and correction protocols. This and other open-loop error mitigation techniques are critical for quantum information processing in the era of Noisy Intermediate-Scale Quantum technology. However, despite its utility, dynamical decoupling does not address errors which
occur at unstructured times during a circuit, including certain commonly-encountered noise mechanisms such as cross-talk and imperfectly calibrated control pulses. Here, we introduce and demonstrate an alternative technique  quantum measurement emulation (QME)  that effectively
emulates the measurement of stabilizer operators via stochastic gate application, leading to a firstorder insensitivity to coherent errors. The QME protocol enables error suppression based on the
stabilizer code formalism without the need for costly measurements and feedback, and it is particularly well-suited to discrete coherent errors that are challenging for DD to address.


# **INTRODUCTION**

Over the past few years, impressive strides have been
made in the field of quantum computing. Quantum advantage has been reported [1] and there is now an ecosystem of cloud-based quantum processors and companies
interested in using them [25]. However, high error rates
continue to limit circuit depth such that solving realworld problems with todays quantum computers remains
a challenge [6, 7]. Errors in quantum devices can be
grouped into two categories: incoherent (stochastsic) and
coherent (deterministic). Although coherent errors do
not reduce the purity of a qubit state, they are surprisingly pernicious. For small errors, infidelity grows linearly with incoherent errors and quadratically with coherent errors [8]. As quantum processors grow in complexity and computational power, control signal crosstalk and coherent errors from spectator qubits become increasingly problematic for gate performance and increasingly challenging to characterize [9]. Unlike incoherent
errors, they compound each other in unpredictable ways

[10] that lead to substantially worse performance than
predicted by randomized benchmarking techniques.
Feedback-based quantum error correction (QEC) is designed to suppress the high error rates in quantum hardware, and attaining QEC is a long-term goal of the quantum computation community [1115]. QEC works by
making error detection measurements that are carefully
designed to preserve quantum information, and then performing restorative gates on the system conditioned on


the error pattern observed in order to return the processor to an error-free state. However, performing feedback is an enormous technical challenge. Compared to
other operations on todays superconducting qubit quantum processors, readout has the highest error rate by
an order of magnitude [1, 16, 17]. Readout is also the
longest operation on these processors by up to two orders of magnitude [17, 18], so teams working to get a
feedback operation below the threshold for fault-tolerant
computation must wrestle with a substantial incoherent
error as well as a relatively low assignment fidelity [19].
It thus behooves us to get as much mileage as we can
out of error reduction techniques which do not utilize
feedback ( _i. e._ feed-forward error mitigation), especially
in the era of Noisy Intermediate-Scale Quantum (NISQ)
technology [20].
Dynamical decoupling (DD) is the primary feedforward control technique in use today [2125]. It takes
advantage of temporal symmetries in the structure of the
noise in order to reverse errors, and is highly effective
against low frequency incoherent noise. The canonical
example of such a technique is the Hahn echo, pioneered
in the context of magnetic resonance imaging [26]. However, most sources of coherent error (such as imperfectly
calibrated gates and cross-talk) are discrete events with
no inherent temporal symmetry to exploit.
Randomized compiling [27, 28] is a promising new feedforward control technique that specifically addresses coherent errors from complex gates by inserting stochastically chosen high-fidelity gates to make those errors inco-


-----


Measurement Quantum Measurement Emulation

|0 1|Col2|
|---|---|


|0 QMEz 1|Z|
|---|---|



Ensemble Average: Ensemble Average:

**d**


herent. A twirling gate _T_ _k_ , drawn uniformly at random
from the group generated by Pauli gates and the phase
gate, is inserted before each error-prone gate _G_ _k_
. To preserve the original computation, _G_ _k_
is followed by a correction gate _T_ _c_ _k_ calculated such that _T_ _c_ _k_ _G_ _k_ _T_ _k_ = _G_ _k_ . This
renders coherent errors incoherent, which reduces error
rates and lowers the gate fidelity threshold required for
fault-tolerant quantum computation.
In this work, we introduce a related feed-forward
control technique for addressing coherent errors, which
uses stochastic gates but requires no classical precomputation. Previous work on stabilizer codes has
shown that errors can be reduced simply by measuring the stabilizers, even without feedback [2933] . We
take this a step further and investigate the effects of
simulating the quantum channel of measurement via
the stochastic application of single-qubit gates, which is
faster than real measurement by more than an order of
magnitude. We find that this technique leads to an improvement in circuit performance. This quantum measurement emulation ( QME ) technique extends naturally
from the stabilizer code formalism and is particularly
well-suited for discrete coherent errors that are challenging for dynamical decoupling to address.

# **OPERATING PRINCIPLE OF EMULATING A**
**QUANTUM MEASUREMENT CHANNEL**

Consider the measurement of a state __ along the _z_
axis in an experiment without feedback, described by the
Kraus operators _P_ 0 _z_ = 0 0 and _P_ _z_ 1 = 1 1 :

_|_ __ _|_ _|_ __ _|_


![oliver_QuantumMEasurementEmulation.pdf-1-0.png](oliver_QuantumMEasurementEmulation.pdf-1-0.png)

![oliver_QuantumMEasurementEmulation.pdf-1-1.png](oliver_QuantumMEasurementEmulation.pdf-1-1.png)


Full state tomography

Full state tomography

Varying _z_
initial state ( )

|Q|MEz Full s Z tomog|
|---|---|


![oliver_QuantumMEasurementEmulation.pdf-1-2.png](oliver_QuantumMEasurementEmulation.pdf-1-2.png)

![oliver_QuantumMEasurementEmulation.pdf-1-3.png](oliver_QuantumMEasurementEmulation.pdf-1-3.png)

FIG. 1. **Emulated dephasing channel a** Diagram depicting
_z_ -axis measurement as a dephasing channel. The measurement
projects the quantum state onto the _z_ -axis and reduces the length
of the Bloch vector. **b** Stochastic gate application can create the
same quantum channel as _z_ -axis measurement. **c** Various qubit
initial states reconstructed with state tomography (grey squares),
plotted with projection after _z_ -axis measurement (orange x). **d**
State tomography data of qubit __ , plotted after applying 1 (grey
squares), Pauli _Z_ gate (blue triangles) and QME _Z_ (green circles)
for varying initial states. We see that QME _Z_ implements the same
channel as _z_ -axis measurement.

matrix __ as performing a measurement in the _z_ basis.
We call this stochastic operation _quantum measurement_
_emulation_ :


_z_ ( __ ) : __
_M_ __


_P_ _i_ _z_ _P_ _z_ _i_
_i_ =0 _,_ 1


__ 11 __ 12
__ 21 __ 22



= __ 11 0
0 __ 22
 


(1)


_z_
_M_


The same quantum channel (i.e. mapping) is implemented by


QME _Z_


with _p_ = 1 2

with _p_ = 1


(3)

|Col1|1|Col3|
|---|---|---|
||||
||Z||
||||


For an intuitive picture, consider a vector on the Bloch
sphere. Fig 1a visualizes the effect of _z_ -axis measurement
when performed on an ensemble of identically prepared
experiments. In Fig 1b, we see how applying the QME
operation has the same outcome  when the 1 and _Z_
- components cancel and leave only the projection on the branches are averaged together, their _x_ - and _y_ _z_ -axis.
We experimentally demonstrate the equality of these
two quantum channels using superconducting transmon
qubits. (For more information on the device, see [35]).
We prepare the qubit in an arbitrarily chosen initial state
and plot a tomographic reconstruction of the state after
either doing nothing (grey square), applying a Z gate
(blue triangle), or after stochastically applying a _Z_ gate
with p = 0.5 (green circle). We repeat these measure-



1
_z_ ( __ ) : __
_D_ __



1

1 __ 1 + 1
2



_ZZ_
2


__ 11 __ 12
__ 21 __ 22



= __ 11 0
0 __ 22
 


(2)


_z_
_D_


which is the dephasing operator [34]. Equation (2) provides an operational interpretation of the act of measurement: the state is dephased in the basis of the measurement. Equation (2) can also be interpreted as a probabilistic application of either the identity operation ( 1 ) or
a Pauli _Z_ operation.
Taken together this observation implies that when averaging over an ensemble of identically prepared qubits,
applying a _Z_ gate with probability 0.5 (and otherwise
doing nothing) has the same effect on the qubits density


QME


-----


ments for a variety of input states. As expected from
Equation (2), the probabilistic application of _Z_ and 1
gates effectively projects the qubit state onto the _z_ -axis,
with some small deviations due to measurement errors.
To highlight the effective equivalence between this and
actual _z_ -basis measurement, we prepare the same initial
states and plot __ _Z_ __ (Fig 1c).
The equivalence we have described between _z_ ( __ ) and
_M_
_z_ ( __ ) can be generalized to measurement along any axis,
_D_
including those in a multi-qubit basis. The observable for
an _n_ -qubit measurement along a multi-qubit axis __
_n_
corresponds to a unitary __ _SU_ (2 ). Measurement along __
_S_ __
is performed by replacing the projectors in Equation (1)
with the projectors for the 1 eigenstates of __
. Consequently, the generalized dephasing channel is given by: __ _S_


Initial state

State after coherent error

State after ensemble QME _Z_
Coherent error, R _x_ ( __ )

Trace distance, _T_ ( _, _ initial )

Bell state Rotation
prep. error


![oliver_QuantumMEasurementEmulation.pdf-2-0.png](oliver_QuantumMEasurementEmulation.pdf-2-0.png)

Rotation
error


![oliver_QuantumMEasurementEmulation.pdf-2-1.png](oliver_QuantumMEasurementEmulation.pdf-2-1.png)

0.8

0.6

0.4



1
__ ( __ ) : __
_D_ __ 2



1 1 __ _n_ __ 1 __ _n_ + 1

2


2 _S_ __ __ _S_ __ __ (4)


This implies that a quantum measurement emulation of
any Pauli operator can be performed with the stochastic
application of single-qubit gates. As an example, we show
below how the quantum channel for __ _ZZ_ __ measurement
can be emulated using single-qubit _Z_ gates.

with _p_ = 1


![oliver_QuantumMEasurementEmulation.pdf-2-2.png](oliver_QuantumMEasurementEmulation.pdf-2-2.png)

![oliver_QuantumMEasurementEmulation.pdf-2-3.png](oliver_QuantumMEasurementEmulation.pdf-2-3.png)

Rotation error, __ (rad) Rotation error, __ (rad)


0.8 1.6


0.4 0.8


FIG. 2. **QME** **for Error Mitigation** **a** Diagram depicting
QME as an error mitigation technique. After the initial state is
prepared (white circle), a coherent error rotates the state away
(grey square). Applying QME _Z_
projects that error into an incoherent error, pushing the qubit state back to the -axis (green circle). Notice that after performing QME , the trace distance to the _z_
initial state is greatly reduced. **b** Qubit is prepared in the _|_ 0 __ state
and subjected to coherent errors of increasing strength. We plot
the trace distance with (grey squares) and without (green circles)
QME , overlaid with theoretical values from simulations performed
using the measured initial state and no free parameters. **c** Qubits
are prepared in _|_ 0 __ = __ 1 2 ( _|_ 00 __ + _|_ 11 __ ) in a simple code stabilized

by _ZZ_ , subjected to a small _R_ _x_ ( __ ) __ _R_ _x_ ( __ ) coherent error and plot
the trace distance to the initially prepared state with (green circles)
and without (grey squares) QME _ZZ_ for increasing error strength __ .
In both of these examples, QME provides a first-order insensitivity
to __ . (In these plots, 1 _T_ ( _, _ _initial_ ) has been normalized to 1 in
__
order to account for state preparation and measurement (SPAM)
errors.)


FIG. 2. **QME** **for Error Mitigation** **a** Diagram depicting
QME as an error mitigation technique. After the initial state is
prepared (white circle), a coherent error rotates the state away
(grey square). Applying QME _Z_
projects that error into an incoherent error, pushing the qubit state back to the -axis (green circle). Notice that after performing QME , the trace distance to the _z_
initial state is greatly reduced. **b** Qubit is prepared in the _|_ 0 __ state
and subjected to coherent errors of increasing strength. We plot
the trace distance with (grey squares) and without (green circles)
QME , overlaid with theoretical values from simulations performed
using the measured initial state and no free parameters. **c** Qubits
are prepared in _|_ 0 __ = __ 1 2 ( _|_ 00 __ + _|_ 11 __ ) in a simple code stabilized

|Col1|1|Col3|
|---|---|---|
||||

|Col1|1|Col3|
|---|---|---|
||||



(5)

|Col1|QME ZZ|Col3|
|---|---|---|
||||
||||


with _p =_ 1 2

|Col1|Z|Col3|
|---|---|---|
||||


|Col1|Z|Col3|
|---|---|---|
||||



for a logical qubit. Stabilizer codes are designed such
that stabilizer measurements do not corrupt the quantum information stored in the logical qubit, and the measurement results can be used as a parity check for error
detection or error correction. In this case, performing
QME __ emulates a stabilizer measurement which can be
used to mitigate coherent errors which rotate the state
outside of the codespace.

# **USING** **QME** **TO MITIGATE COHERENT**
**ROTATION ERRORS**

After a coherent error has occurred, applying the appropriate will project the qubit onto the measurement axis, effectively converting the coherent error into QME
an incoherent error. Fig. 2a shows a qubit initially in the
_|_ state (white) which is subjected to a coherent rotation error 0 __ _R_ _x_ ( __ ) (grey). When QME is performed along
the _z_ -axis (denoted QME _Z_ ), the qubit state is projected
onto the , the coherent error which rotated the qubit state on the surface of the Bloch sphere _z_ -axis. After QME


is now manifest as an incoherent error which shortens
the length of the vector along the measurement axis.
After applying QME _Z_ the trace distance between the
initial and measured states is only second order in the
size of the original perturbation. Here, trace distance
_T_ ( _, _ ) = 2 1 __ __ 1 is a more sensitive metric than fi

__ __ __
delity  trace distance measures the maximum distinguishability between states, whereas fidelity measures the
distinguishability along the axis of the qubit state.


is now manifest as an incoherent error which shortens
the length of the vector along the measurement axis.
After applying QME _Z_ the trace distance between the
initial and measured states is only second order in the
size of the original perturbation. Here, trace distance
_T_ ( _, _ ) = 1 __ __ is a more sensitive metric than fi


To demonstrate QME as a state stabilization technique,
state and induce coherent errors of increasing strength (Fig 2b). We plot we prepare the qubit in the _|_ 0 __
1 ) with (grey squares) and without (green circles) __ _T_ QME ( _, _ (Fig. 2b and 2d), overlayed with theoretical


-----


Bell state


values from simulations performed using the measured
initial state and no free parameters. For small values of
the error strength __ , the corrected trace distance curve
is nearly flat, indicating a first-order insensitivity to coherent errors.
to reduce the effects of deleterious coherent errors, one must know the axis along which to To use QME
measure. In the single-qubit case, this corresponds to
knowing the axis of the ideal qubit state  in which
case, the qubit can only store classical information. Stabilizer codes, on the other hand, are carefully designed
so that parity measurements may be performed without
is applied within the framework of a stabilizer code, coherent disrupting the quantum information. When QME
errors that would have moved information outside of the
codespace are projected into incoherent errors. This both
reduces the trace distance and prevents the build-up of
coherent errors.
To demonstrate the power of stabilizer measurement
emulation, we use a simple code consisting of Bell states
and stabilized by _ZZ_ , with  1 = __ 1 2 00 + 11 and

_|_ __ _|_ __
 0 = __ 1 2 00 11 . To mitigate coherent errors for this  

_|_ _|_ __ 


prep. Cell 1 Cell 2 Cell _N_

...

![oliver_QuantumMEasurementEmulation.pdf-3-0.png](oliver_QuantumMEasurementEmulation.pdf-3-0.png)

![oliver_QuantumMEasurementEmulation.pdf-3-1.png](oliver_QuantumMEasurementEmulation.pdf-3-1.png)

**c**

Trace distance State fidelity


__ ( _N_


![oliver_QuantumMEasurementEmulation.pdf-3-2.png](oliver_QuantumMEasurementEmulation.pdf-3-2.png)

![oliver_QuantumMEasurementEmulation.pdf-3-3.png](oliver_QuantumMEasurementEmulation.pdf-3-3.png)

Number of cells ( _N_ )


10 15 0 5 10 15


Number of cells ( _N_


FIG. 3. **QME** **for Mitigating Coherent Two-Qubit Errors**
**in a Sequence of CZ Gates** . **a** Circuit used to test QME in the
context of a computation, consisting of a sequence of 1 operations,
each decomposed into two CZ gates. QME _XX_ is added after every
CZ pair. This circuit is run increasing the length of the sequence,
and state tomography is used to reconstruct the trace distance and
fidelity to the initially prepared state. The experiment is performed
with a CZ gate with an intentionally introduced coherent error ( **b** )
and with a high fidelity CZ gate ( **c** ). To generate the theory curves
we model the circuit with amplitude-damping and phase-damping
channels, as well as single- and two-qubit over-rotations in the CZ
gates. The amplitude (phase) damping constants are determined
from measured _T_ 1 ( _T_ 2 ) times, and the over-rotation angles are fit
to the data. (In these plots, 1 _T_ ( _, _ _initial_ ) has been normalized
__
to 1 in order to account for SPAM errors.)

in the form of an QME _XX_ inserted between every pair of
CZ gates.
Executing the circuit without QME results in the steep
plunge and revival that is the hallmark of the accumulation of coherent errors, seen in both the trace distance
and the fidelity. The device used in this experiment has
CZ gates with an average fidelity of 0.997 (measured via
interleaved Clifford randomized benchmarking). Nevertheless, after 10 steps (20 gates) the output fidelity is
nearly 0.5  a clear demonstration of the deleterious accumulation of coherent errors. Adding QME leads to a
smooth monotonic decay, which indicates that the coherent error has been made incoherent. Though adding
QME increases the circuit depth, it results in a substantial improvement in circuit performance.

# **OUTLOOK**

We have demonstrated a new feed-forward control
technique for mitigating coherent errors in quantum information processing which is tailored to discrete coherent errors. By using stochastically-applied single-qubit
gates to emulate quantum measurement along the appropriate axis, coherent errors can be made incoherent.
Unlike randomized compiling, QME does not require the


and stabilized by _ZZ_ , with  1 = __ 1 2 00 + 11 and

_|_ __ _|_ __
 0 = __ 1 2 00 11 . To mitigate coherent errors for this 

_|_ _|_ __ 
code, we will apply QME _ZZ_ as outlined n Eq. 5; namely,

 

we apply identity gates or simultaneous  _Z_ gates on both


 0 = __ 1 2 00 11 . To mitigate coherent errors for this

_|_ _|_ __
code, we will apply QME _ZZ_ as outlined n Eq. 5; namely,
we apply identity gates or simultaneous  _Z_ gates on both
qubits with 50% probability. Note that extending QME
to multiple qubits does not consume more time or require more complicated gates: with _p_ = 0 _._ 5 we perform
an identity operation, and with _p_ = 0 _._ 5 we apply a _Z_
gate to each qubit. As with the state stabilization experiment, we apply a coherent error of varying strength
(now an _R_ _x_ ( __ ) _R_ _x_ ( __
) error), either do nothing or apply QME , and measure the resulting trace distance to the __
initial state with a state tomography measurement (Fig
2b, 2c). Here too, applying QME leads to a distinctly
smaller error. Though this plot demonstrates improved
performance specifically for an _R_ _x_ ( __ ) _R_ _x_ ( __ ) error, that
__
particular error was chosen arbitrarily; any error that rotates the state outside of the  0 _,_  1 manifold will behave
similarly.
   
 

# **USING** **QME** **TO MITIGATE COHERENT**
**ERRORS FROM 2QB GATES**


Two-qubit gates are the dominant source of coherent
errors in all current generation quantum processors, so
we explore the effects of QME in a circuit comprised of
a sequence of CZ gates (Fig. 3a). For this experiment
we use a different code, stabilized by _XX_ , with  1 =
__ 1 2 _|_ 00 __ + _|_ 11 __ and  0 = __ 1 2 _|_ 01 __ + _|_ 10 __ . ( CZ is not a  

2 



00 + 11 and  0
2

_|_ __ _|_ __





01 + 10 . ( CZ is not a
2

_|_ __ _|_ __

2


logical operation in this code, but CZ 2 = 1 __ 1 is a logical
operation in every code.) To set a performance baseline,
we prepare the  0 state, apply _N_ CZ pairs and record
the trace distance (state fidelity) to the initial state as
 
shown in Fig3b(c). We then introduce error mitigation 


-----


computation of correction gates needed in randomized
compiling, with the trade-off that it only protects against
errors that rotate the qubit out of the logical codespace.
QME also offers protection against coherent errors that
might have occurred during twirling gates. We show how
can be used in the context of stabilizer codes to improve circuit performance in terms of both trace distance QME
and fidelity. This still holds in arbitrarily generated circuits where simple dynamical decoupling schemes do not
offer an advantage. QME is a promising addition to the
collection of quantum computing control techniques.

# **Acknowledgments:** AG acknowledges funding from
the 2019 Google US/Canada PhD Fellowship in Quantum Computing. MK acknowledges support from the
Carlsberg Foundation during part of this work. IM acknowledges funding from NSF grant FET-1910859. This
research was funded in part by the U.S. Army Research
Office Grant W911NF-18-1-0411 and the Assistant
Secretary of Defense for Research & Engineering under
Air Force Contract No. FA8721-05-C-0002. Opinions,
interpretations, conclusions, and recommendations are
those of the authors and are not necessarily endorsed by
the United States Government.

The authors declare no competing interests. **Competing interests:**




-----


# Supplementary material for Error mitigation via stabilizer measurement emulation

A. Greene, 1 M. Kjaergaard, 1 M. E. Schwartz, 2 G. O. Samach, 1, 2 A. Bengtsson, 1, 3 C. McNally, 1 M. OKeeffe, 2

D. K. Kim, 2 M. Marvian, 1, 4 A. Melville, 2 B. M. Niedzielski, 2 A. Veps al ainen, 1 R. Winik, 1 J. Yoder, 2

D. Rosenberg, 2 S. Lloyd, 1, 4 T. P. Orlando, 1 I. Marvian, 5 S. Gustavsson, 1 and W. D. Oliver 1, 2, 6, 7

1 _Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
2 _MIT Lincoln Laboratory, Lexington, MA 02421, USA_
3 _Microtechnology and Nanoscience, Chalmers University of Technology, G_ _oteborg, SE-412 96, Sweden_
4 _Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
5 _Departments of Physics & Electrical and Computer Engineering, Duke University, Durham, NC 27708, USA_
6 _Department of Physics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA_
7 _Department of Electrical Engineering & Computer Science,_
_Massachusetts Institute of Technology, Cambridge, MA 02139, USA_

## **DEVICE**

![oliver_QuantumMEasurementEmulation.pdf-5-0.png](oliver_QuantumMEasurementEmulation.pdf-5-0.png)

Supplementary Figure 1.

The device used for these measurements is the same used for [34]. As shown in the SEM image in Supplementary
Figure 1, this chip has three asymmetric xmon-style transmon qubits with individual microwave and flux control
lines. All experiments in this paper were performed with the two leftmost qubits; their properties are reported in
Table I. Interleaved randomized benchmarking data for single- (two-) qubit gates are shown in Supplementary Figure
2 (3).

1 See M. K. _et al. arXiv:2001.08838_ (2020) for details

|Parameter|Qubit 1 (, target)|Qubit 2 (, instruction)|
|---|---|---|
|Idling frequency,  /2 i Anharmonicity, /2 Coupling strength, g/2 Readout resonator frequency, f /2 i Junction asymmetry|4.748 GHz 4.225 GHz 175 MHz 190 MHz 10.6 MHz 7.251 GHz 7.285 GHz 1:5 1:10||
|Relaxation time at idling point, T 1 Coherence time at idling point, T 2R Effective relaxation time undergoing CZ trajectory, Te1 1 Effective coherence time undergoing CZ trajectory, Te2R 1|23 s 13 s 17 s 5 s|39 s 25 s (same as idling) (same as idling)|
|Single-qubit gate fidelity, t 1 1qb Single-qubit gate time, t 1qb Two-qubit gate fidelity, t 1 CZ Two-qubit gate time, t CZ| 0.999  0.999 30 ns 30 ns 0.997 60 ns||



TABLE I. Parameters of the two qubits used in this work.


-----


## **STATE STABILIZATION ALONG AN ARBITRARY AXIS**


Wait(t)


H+

H+ =


![oliver_QuantumMEasurementEmulation.pdf-6-0.png](oliver_QuantumMEasurementEmulation.pdf-6-0.png)

![oliver_QuantumMEasurementEmulation.pdf-6-1.png](oliver_QuantumMEasurementEmulation.pdf-6-1.png)

![oliver_QuantumMEasurementEmulation.pdf-6-2.png](oliver_QuantumMEasurementEmulation.pdf-6-2.png)

R _x_ ( __ ) QME _x_

![oliver_QuantumMEasurementEmulation.pdf-6-3.png](oliver_QuantumMEasurementEmulation.pdf-6-3.png)

## /4 ## /2

![oliver_QuantumMEasurementEmulation.pdf-6-6.png](oliver_QuantumMEasurementEmulation.pdf-6-6.png)
 Angle (rad)


R _z_ ( __ ) QME

![oliver_QuantumMEasurementEmulation.pdf-6-5.png](oliver_QuantumMEasurementEmulation.pdf-6-5.png)

## 20 ## 40

![oliver_QuantumMEasurementEmulation.pdf-6-8.png](oliver_QuantumMEasurementEmulation.pdf-6-8.png)
 Time ( s)



_-3_
_Z_ _4_



__
_X_ _2_


_3_


![oliver_QuantumMEasurementEmulation.pdf-6-4.png](oliver_QuantumMEasurementEmulation.pdf-6-4.png)

## 0.75
 0.5
 0.25


## /4 ## /2

![oliver_QuantumMEasurementEmulation.pdf-6-7.png](oliver_QuantumMEasurementEmulation.pdf-6-7.png)
 Angle (rad)


Supplementary Figure 2.


In the main text, Equation 1 and Equation 2 describe how the quantum channel for measuring the expectation
value of an arbitrary unitary operator _S_ _v_ can be performed by stochastically applying _S_ _v_ . Figure 1 demonstrates
this equivalence for a measurement along the _z_ -axis. Here, we show similar data for emulated measurement along the
_x_ -axis (Supplementary Figure 4a) and along the _x_ + 2 _y_ -axis (Suppementary Figure 4b).

## **ERROR MITIGATION**

In Figure 2 of the main text, we demonstrate QME as an error mitigation technique using an intentionally applied
__ _x_ __ __ _x_ over-rotation error of varying strength. In Figure we show that QME leads to first-order insensitivity to a
variety of transversal errors.


( ) __


QME _H_


-----


![oliver_QuantumMEasurementEmulation.pdf-7-0.png](oliver_QuantumMEasurementEmulation.pdf-7-0.png)

![oliver_QuantumMEasurementEmulation.pdf-7-1.png](oliver_QuantumMEasurementEmulation.pdf-7-1.png)

![oliver_QuantumMEasurementEmulation.pdf-7-2.png](oliver_QuantumMEasurementEmulation.pdf-7-2.png)

Supplementary Figure 3.

## **SIMULATIONS**

All theory curves used in this paper were generated by simulating the described circuit in `QuTiP` , using the initial __
as measured by state tomography. In Fig 3 and Fig 4, the nonidealities in the CZ gates were captured by representing
each CZ gate as the composition of the ideal operation with a CPHASE( __ ) over-rotation, single-qubit _Z_ over-rotations
_R_ _Z_ ( __ 1 ) __ _R_ _Z_ ( __ 2 ) and a leakage channel parameterized by leakage rate _lambda_ . The parameters _, _ 1 _, _ 2 and __ were
fit to the state tomography data taken at each step of the circuit. The simulations for Fig. 3 and Fig. 4 also included
decoherence, in the form of amplitude-damping and dephasing channels added after each gate in the circuit. The
decay rates for these channels were determined by measured coherence times (shown in Table I) and the duration of
the preceding gate (30n single-qubit gates and 60ns two-qubit gates, with a 5ns gap between pulses).
Our state tomography analysis does not discriminate between _|_ 1 __ and _|_ 2 __ , so leakage from _|_ 11 __ to _|_ 20 __ looks like
incoherent population transfer to _|_ 10 __ . Accordingly, we used the following Kraus operators used to model leakage:


1 0 0
0 1 0
0 0 1
0 0 0


0 0 0 0
0 0 0 0
0 0 __ __ 0

0 0 0


_L_ 1 _,_ ( _t_ ) =


0 0
0 0
0 0



_,_ _L_ 2 _,lambda_ ( _t_ ) =

0

1 __ 
__ 




(1)


The channel that composes amplitude damping and dephasing is given by:


q _k_ ( _t_ ) : __ q _k_
_E_ __


_i_ =1 _,_ 2
_j_ =1 _,_ 2 _,_ 3


_A_ _i,_  1 ( _t_ ) _D_ _j,_  __ ( _t_ ) __ q _k_ _D_ _j,_ __  __ ( _t_ ) _A_ __ _i,_  1 ( _t_ ) _,_ (2)


where _A_ _i,_  1 ( _t_ ) is the amplitude damping process (with  1 = 1 _/T_ 1 ), and _D_ _j,_  __ ( _t_ ) is the dephasing process ( __ =
1 _/T_ 2R __ 1 _/_ 2 _T_ 1 ),  1 _,_ q _k_ and  _,_ q _k_ are the appropriate coherence parameters for qubit _k_ , and _t_ is the time of the


-----


preceeding single- or two-qubit gate on that qubit. The amplitude damping and dephasing Kraus operators are given
by:


_A_ 1 _,_  1 ( _t_ ) =

_A_ 2 _,_  1 ( _t_ ) =

_D_ 1 _,_  __ ( _t_ ) =

_D_ 2 _,_  __ ( _t_ ) =

_D_ 3 _,_  __ ( _t_ ) =


(3)

(4)

(5)

(6)

(7)


0 _e_ __  1 _,_ q _k_ _t/_ 2

0 __ 1 __ _e_ __  1 _,_ q _k_ _t_


_e_ __  _,_ q _k_ _t/_ 2 0
0 _e_ __  _,_ q _k_ _t/_ 2


 __


1 __ _e_ __  _,_ q _k_ _t_ 0
0 0

0
__ 1 __ _e_ __  _,_ q _k_ _t_


-----

