
**Abstract**

###### Catching and Reversing a Quantum Jump Mid-Flight

Zlatko Kristev Minev

2018

A quantum system driven by a weak deterministic force while under strong continuous energy

measurement exhibits quantum jumps between its energy levels (Nagourney _et al._ , 1986,

Sauter _et al._ , 1986, Bergquist _et al._ , 1986). This celebrated phenomenon is emblematic of

the special nature of randomness in quantum physics. The times at which the jumps occur

are reputed to be fundamentally unpredictable. However, certain classical phenomena, like

tsunamis, while unpredictable in the long term, may possess a degree of predictability in the

short term, and in some cases it may be possible to prevent a disaster by detecting an advance

warning signal. Can there be, despite the indeterminism of quantum physics, a possibility

to know if a quantum jump is about to occur or not? In this dissertation, we answer this

question affirmatively by experimentally demonstrating that the completed jump from the

ground to an excited state of a superconducting artificial atom can be tracked, as it follows its

predictable flight, by monitoring the population of an auxiliary level coupled to the ground

state. Furthermore, the experimental results demonstrate that the jump when completed is

continuous, coherent, and deterministic. Exploiting these features, we catch and reverse a

quantum jump mid-flight, thus deterministically preventing its completion. This real-time

intervention is based on a particular lull period in the population of the auxiliary level, which

serves as our advance warning signal. Our results, which agree with theoretical predictions

essentially without adjustable parameters, support the modern quantum trajectory theory and

provide new ground for the exploration of real-time intervention techniques in the control of

quantum systems, such as early detection of error syndromes.


-----


#### Catching and Reversing a Quantum Jump Mid-Flight

######### A Dissertation Presented to the Faculty of the Graduate School of Yale University in Candidacy for the Degree of Doctor of Philosophy

 by Zlatko Kristev Minev

 Dissertation Director: Michel H. Devoret

 May 2018


-----


 2019 by Zlatko Kristev Minev

All rights reserved.

ii


-----


For those who gave the most but could see the least.

  
(April 11, 1925 - December 11, 2017)

&

  
(December 9, 1928 - February 2, 2016)

iii


-----


### Contents

**Contents** **iv**

**List of Figures** **vi**

**List of Tables** **viii**

**List of Symbols** **ix**

**Acknowledgments** **x**

**Overview** **1**

**1** **Introduction and main results** **3**
1.1 Principle of the experiment . . . . . . . . . . . . . . . . . . . . . . . . 4

1.2 Unconditioned monitoring of the quantum jumps . . . . . . . . . . . . . 8

1.3 Catching the quantum jump . . . . . . . . . . . . . . . . . . . . . . . . 9

1.4 Reversing the quantum jump . . . . . . . . . . . . . . . . . . . . . . . 13

1.5 Discussion of main results . . . . . . . . . . . . . . . . . . . . . . . . . 15

**2** **Quantum measurement theory** **17**
2.1 Prelude: from classical to quantum measurements . . . . . . . . . . . . 18

2.1.1 Classical measurement theory: basic concepts . . . . . . . . . . . 19

2.1.2 Classical toy model of system-environment interaction . . . . . . 26

2.1.3 Quantum toy model . . . . . . . . . . . . . . . . . . . . . . . . 30

2.2 Continuous quantum measurements: introduction to quantum trajectories
and stochastic calculus . . . . . . . . . . . . . . . . . . . . . . . . . . 36

2.2.1 Time-discrete model with flying spins . . . . . . . . . . . . . . . 37

2.2.2 Geometric representation of a continuous measurement: random
walk on a hyperbola . . . . . . . . . . . . . . . . . . . . . . . . 45

2.2.3 Continuum limit: Wiener noise and stochastic calculus . . . . . . 47

2.3 Quantum trajectory theory . . . . . . . . . . . . . . . . . . . . . . . . 50

2.3.1 Photodetection . . . . . . . . . . . . . . . . . . . . . . . . . . 51

2.3.2 Homodyne and heterodyne detection . . . . . . . . . . . . . . . 57

iv


-----


2.4 Further reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

**Theoretical description of quantum jumps** **65**
3.1 Fluorescence monitored by photon counts . . . . . . . . . . . . . . . . 66

3.1.1 Dehmelt electron-shelving scheme and quantum jumps . . . . . 66

3.1.2 Measurement-backaction effective force in the absence of the Dark
Rabi drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

3.1.3 Incoherent Bright drive and Dark drive off . . . . . . . . . . . . 86

3.2 Heterodyne monitoring of readout cavity coupled to three-level atom . . 90


3.2.1 Description of cQED experiment . . . . . . . . . . . . . . . . . 90

3.2.2 Simulation of Stochastic Schrdinger equation (SSE) . . . . . . 92

**Experimental methods** **95**
4.1 Sample design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

4.1.1 Energy-participation-ratio (EPR) approach . . . . . . . . . . . . 100

4.1.2 Calculation of the EPR . . . . . . . . . . . . . . . . . . . . . . 106

4.1.3 Calculation of Hamiltonian parameters with the EPR . . . . . . . 110

4.1.4 Calculation of dissipation budget with the EPR . . . . . . . . . 111

4.2 Sample fabrication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

4.3 Sample holder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

4.3.1 Material losses and selection . . . . . . . . . . . . . . . . . . . 118

4.3.2 Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

4.4 Cryogenic setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

4.4.1 Material selection . . . . . . . . . . . . . . . . . . . . . . . . . 124


4.4.2 Thermalization . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

4.4.3 Light and magnetic shielding . . . . . . . . . . . . . . . . . . . 128

4.5 Microwave setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

**Additional experimental results** **131**
5.1 Characterization of the system . . . . . . . . . . . . . . . . . . . . . . . 132

5.1.1 Measurement-induced relaxation _T_ 1 ( _n_ ) . . . . . . . . . . . . . . 133

5.2 Control of the three-level atom . . . . . . . . . . . . . . . . . . . . . . 136

5.2.1 Qubit pulses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136

5.2.2 Tomography of the three-level atom . . . . . . . . . . . . . . . . 137

5.2.3 Atom and cavity drives . . . . . . . . . . . . . . . . . . . . . . 140

5.3 Monitoring quantum jumps in real time . . . . . . . . . . . . . . . . . 140

5.3.1 IQ filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140


5.3.2 Unconditioned monitoring . . . . . . . . . . . . . . . . . . . . . 142

5.4 Catching and reversing the jump . . . . . . . . . . . . . . . . . . . . . 143

5.4.1 Experiment flow . . . . . . . . . . . . . . . . . . . . . . . . . . 143

5.5 Comparison between theory and experiment . . . . . . . . . . . . . . . 146

5.5.1 Simulated data sets . . . . . . . . . . . . . . . . . . . . . . . . 146

5.5.2 Error budget . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153


-----


5.6 Signal-to-noise ratio (SNR) and de-excitation measurement efficiency . . 154

**6** **Conclusions and perspectives** **162**
6.1 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162

6.2 Perspectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

**Bibliography** **172**

vi


-----


### List of Figures

**Introduction and overview** **3**

1.1 Principle of the experiment . . . . . . . . . . . . . . . . . . . . . . . . 6

1.2 Unconditioned monitoring of quantum jumps in the 3-level system . . . . 10


1.3 Catching the quantum jump mid-flight . . . . . . . . . . . . . . . . . . 11

1.4 Reversing the quantum jump mid-flight . . . . . . . . . . . . . . . . . . 14

**Quantum trajectory theory** **17**


2.1 Geometric representation of the state of a classical and quantum bit . . . 21

2.2 Classical toy model of the interaction between the system and environment 27

2.3 Homodyne monitoring of a quantum bit: time-discrete model . . . . . . 37

2.4 Circuit representation of the _n_ -th timestep of the quantum trajectory . . 41

2.5 Random walk on the measurement hyperbola. . . . . . . . . . . . . . . 47

2.6 Schematic representations of a photo, homodyne, and heterodyne detection schemes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

**Theoretical description of quantum jumps** **65**

3.1 : ideal photodetection theory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Conditional no-click evolution of the jump from _|_ G __ to _|_ D __ 72

3.2 Geometrical representation of a qutrit state with real coefficients: R -qutrit
sphere . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


3.3
Adiabatic solution for the no-click GD manifold trajectory of a superposition state measured with  DG = 0 . . . . . . . . . . . . . . . . . . . . 80


3.4 Geometrical representation of the no-click measurement-backaction force
for  BG = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82


3.5 Geometrical representation of the measurement-backaction force and a
no-click trajectory with  BG = 0 _._ 1 __ B . . . . . . . . . . . . . . . . . . . 84


**Experimental methods** **95**

vii


-----


4.1 Sample and chip layout . . . . . . . . . . . . . . . . . . . . . . . . . . 97

4.2 Darkmon energy-level diagram . . . . . . . . . . . . . . . . . . . . . . . 98

4.3 Effective circuit model of Darkmon system . . . . . . . . . . . . . . . . 100

4.4 Finite-element model of linearized Josephson junction . . . . . . . . . . 107

4.5 Finite-element simulation of a transmon device . . . . . . . . . . . . . . 109

4.6 Non-magnetic couplers and sampler holder . . . . . . . . . . . . . . . . 120

**Experimental results** **131**

5.1 Measurement-induced energy relaxation _T_ 1 ( _n_ ) . . . . . . . . . . . . . . 135

5.2 Control experiment: time-resolved tomogram of the free evolution of a DG
superposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

5.3 Mid-flight tomogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139


5.4 Waiting time to switch from a _|_ B __ to not- _|_ B __ state assignment result . . 142

5.5 Experiment flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144

5.6 Sampling of the Monte-Carlo simulation (courtesy of H.J. Carmichael) . 150

5.7 Comparison between simulation and experiment (courtesy of H.J. Carmichael)151

5.8 Coherence loss through sample to sample fluctuations (courtesy of H.J.
Carmichael) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

**Conclusions and perspectives** **162**

6.1 Four-level atom with two counter-steering measurements . . . . . . . . . 170

viii


-----


### List of Tables

**Quantum trajectory theory** **17**

2.1 Basic concepts of classical measurement theory . . . . . . . . . . . . . . 24

**Experimental results** **131**

5.1 Compilation of experimental parameters . . . . . . . . . . . . . . . . . . 134

5.2 Summary of timescales . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

5.3 Compilation of the simulation parameters . . . . . . . . . . . . . . . . . 149

5.4 Comparison between parameters extracted from the simulation and those
from the experiment. . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

ix


-----


### Acknowledgments

am delighted to take this opportunity to acknowledge the people I learned from

the most and those who supported me during my doctoral research at Yale. In this

## I

short Acknowledgements section, it is infeasible to properly thank everyone. I apologize

in advance for any potential shortcomings. This is particularly relevant for those I worked

with most closely during the initial years of my Ph.D., before I changed course by proposing

and carrying out the quantum jump project in the final two years. The product of these

two years constitutes the remainder of this Dissertation.

To set the stage for the acknowledgements below, let me first briefly recount the origin

and story of this work. In the summer of 2015, I traveled to Scotland to participate in

the Scottish Universities Summer School in Physics (SUSSP71) by partly self-funding my

participation. There I heard a cogent lecture by Howard J. Carmichael, which radically

changed the direction of my doctoral scientific inquiry. Howard presented his gedanken

experiment for catching and reversing a quantum jump mid-flight, which made the striking

prediction that the nature of quantum jumps could be continuous and coherent. The

discussion emphasized that a test of the conclusions remains infeasible, since the requisite

experimental conditions remain far out of reach of atomic physics (see Chap. 1). Excited

by the ideas, however, I brainstormed and ran simulations to find a possible realization of

the gedanken experiment, but in a different domain  superconducting quantum circuits.

Although much was unclear in the leap from the quantum optics to the superconducting

realm, I reached out to Howard and found him very receptive to my still developing ideas.


-----


After an initial rebuff of my proposed experiment on my return to Yale, I spent the fall

and early months of the next year developing the concepts and implementation in detail to

prove their validity, and the feasibility of the project. Following many lessons and in-depth

discussions with Michel, and the input of Howard and the people acknowledged below, the

experiment was successfully realized just short of two years later. The predictions were not

only experimentally confirmed but were further expanded to demonstrate the coherent,

continuous, and deterministic evolution of the quantum jump even in the absence of a

coherent drive on the jump transition.

Thus, first and foremost, I would like to express my deep and heartfelt gratitude to my

dissertation advisor, Michel H. Devoret . Michels reputation as a great mentor and

a brilliant physicist, agreed upon by all sources, notably preceded him as early as during

my undergraduate days at Berkeley. Since I joined Michels group, I have only developed

an ever-growing admiration for his breadth of knowledge and deep thinking. It has been a

privilege and a pleasure to learn from and work closely with Michel. I am endlessly thankful

for the countless hours and legions of lessons he so elegantly delivered on physics, writing,

aesthetics in science, and innumerable other subjects. I am especially grateful to him for

allowing me to take the unusual path of proposing and carrying out a complex, original

experiment with little relation to any other project in the lab or to my previous work. I

deeply appreciate this unique opportunity and I am especially thankful for his support,

trust, and belief in the ideas of a young graduate student. Michel also taught me how

to communicate science clearly and to follow the highest standards, to pay attention to

every detail, including font choices and color combinations. Michel continues to be my

role model for a scientist of the highest caliber. I will dearly miss our inspired, in-depth

conversations on science and beyond. Ill also miss the collaborative and knowledge-rich

environment of Michels Quantronics Laboratory (Qlab) on the fourth floor in

Becton.

xi


-----


As related above, it was my good fortune to meet Howard J. Carmichael at

SUSSP71, where I was inspired by his lecture on quantum jumps. It has been a pleasure

and a privilege to work with Howard, who also inspires me with his record of pathbreaking

advances in quantum optics theory and his seminal role in the foundation of quantum

trajectory theory [the term was coined by him in Carmichael (1993)]. His open reception

of my ideas since the beginning, his generosity with his time, and his continued support has

been beyond measure. I am endlessly grateful to Howard, as well as his student, Ricardo

Gutirrez-Juregui , whom I also had the pleasure of meeting at SUSSP71, for the

indispensable theoretical modeling of the final experimental results. The project greatly

benefitted from the discussions with and theoretical contributions of both Howard and

Ricardo. I am particularly indebted to Howard for his thoughtful edits and input in the

writing and revising of the paper we have submitted, and the enlightening lessons I picked

up along the way.

I deeply appreciate the theoretical discussions during the inception of the project with

Professor Mazyar Mirrahimi , which were of significant help in navigating the land-

scape of cascaded non-linear parametric processes in circuit quantum electrodynamics

(cQED), used in the readout of the atom. I am grateful to Mazyar for patiently accom-

modating the many questions I had. I also want to express my deep gratitude to Professor

Steven M. Girvin for the cQED and quantum trajectory discussions we had, for his

detailed reading and edits of this dissertation manuscript, and for his kind manner of teach-

ing and enlightening his students with countless deep insights, and warm encouragement.

I feel indebted to Professor Jack Harris , who advised me early on at Yale on a project

in optomechanics in his lab, and also provided careful and thoughtful comments on this

dissertation manuscript. Jack has always been inspirational and supportive of my efforts.

I also owe a debt to all the professors and senior scientists who taught me a great deal

of what I know, Rob Schoelkopf, Luigi Frunzio, Liang Jiang, Doug Stone ,

xii


-----


and those who significantly broadened my horizons, and improved my understanding of

physics: Daniel Prober, Leonid Glazmann, Peter Rakich, David DeMille,

Hui Cao, Yoram Alhassid, Paul Fleury, Sean E. Barrett .

During the quantum jump project, I had the pleasure of working very closely with

Shantanu Mundhada . Shantanu was instrumental to the success of the project by

contributing a great deal with his aid in fabrication and the initial DiTransmon design of

the device. Philip Reinhold had developed an outstanding Python platform for the

control of the FPGA, and helped me a great deal in debugging the control code. Shyam

Shankar aided in the fabrication of the device and provided general support to the lab

in his kind and patient manner. I appreciate the many fruitful discussions with Victor

V. Albert, Matti P. Silveri, and Nissim Ofek . Victor in particular addressed an

aspect of the Lindblad theoretical modeling regarding the waiting-time distribution. It was

Nissim and Yehan Liu who spearheaded the initial FPGA development. In later discus-

sions, I benefited from insightful conversations with Howard M. Wiseman, Klaus

Mlmer, Birgitta Whaley, Juan P. Garrahan, Ananda Roy, Joachim

Cohen, and Katarzyna Macieszczak.

In my earlier days at Yale, I learned much about low-temperature experimental physics

from Ioan Pop and Nick Masluk . I had the good fortune to work with them and

Archana Kamal (who inspired me with her dual mastery of experiment and theory)

on the development of a superinductance with a Josephson junction array (Masluk _et al._ ,

2012, Minev _et al._ , 2012). Ioan and I, after spending three months repairing nearly

every part of our dilution system, continued to work together for the next five years.

We demonstrated the first superconducting whispering-gallery mode resonators (WGMR),

which achieved the highest quality factors of planar or quasi-planar quantum structures

at the time (Minev _et al._ , 2013a). These led us to demonstrate the first multi-layer

(2.5D), flip-chip cQED architecture (Minev _et al._ , 2015b, 2016), which demonstrated the

xiii


-----


successful unification of the advantages of the planar (2D) and three-dimension (3D)

cQED architectures (Minev _et al._ , 2013b, 2014, 2015a, Serniak _et al._ , 2015). During the

later phase of this project, I had the pleasure of working with Kyle Serniak , whom I

thank for his many hours in the cleanroom. During these first years, I greatly benefited

from Ioans mentorship, his energetic and cheerful character, and the pleasure of wonderful

gatherings hosted by Cristina and him; additionally, our sailing lessons. While none of the

work described in this paragraph is featured in this Dissertation  as it could form an

orthogonal, independent dissertation  its results are detailed in the cited literature.

During the development of the 2.5D architecture, I came up with an alternative idea

for the quantization of black-box quantum circuits  the energy-participation ratio (EPR)

approach to the design of quantum Josephson circuits (Minev _et al._ , 2018). I am grateful

to Michel and to Zaki Leghtas for their support along the way for this unanticipated

project. More generally, I had the extreme pleasure of working closely with Zaki and learn-

ing a great deal of physics from him in lab and over countless dinners. During the EPR

project, I was privileged to coach a number of talented undergraduate students, whose en-

thusiasm and time I am thankful for: Dominic Kwok, Samuel Haig, Chris Pang,

Ike Swetlitz, Devin Cody, Antonio Martinez, and Lysander Christakis .

Overall, many students and post-docs in Qlab and RSL contributed to the success

of my time at Yale. I would like to thank them all. I have been fortunate to remain close

friends and colleagues with my incoming class, Kevin Chou, Eric Jin, Uri Vool,

Theresa Brecht , and Jacob Blumoff , and to learn dancing with Kevin. It has

been a particular pleasure to work more closely with Serge Rosenblum, Chan U Lei,

Zhixin Wang, Vladimir Sivak, Steven Touzard , and Evan Zalys-Geller .

As part of Qlab , I had the privilege to work, although more indirectly, with a number of

excellent postdoctoral researchers, including Michael Hatridge, Baleegh Abdo,

Ioannis Tsioutsios, Philippe Campagne-Ibarcq, Gijs de Lange, Angela

xiv


-----


Kou , and Alexander Grimm . I also had the pleasure to occasionally collaborate

with a number of the other graduate students in Qlab , including Anirudh Narla,

Clarke Smith, Nick Frattini, Jaya Venkatraman, Max Hays, Xu Xiao,

Alec Eickbusch, Spencer Diamond, Flavius Schackert, Katrina Sliwa,

and Kurtis Geerlings .

Our work was always mutually supported and very closely intertwined with that of

Rob Scholekopfs lab, and I thank Hanhee Paik, Gerhard Kirchmair, Luyan

Sun, Chen Wang, Reinier Heeres, Yiwen Chu, Brian Lester, and Vijay

Jain . There are also many graduate students in Robs group I would like to acknowl-

edge: Andrei Petrenko, Matthew Reagor, Brian Vlastakis, Eric Hol-

land, Matthew Reed, Adam Sears, Christopher Axline, Luke Burkhart,

Wolfgang Pfaff, Yvonne Gao, Lev Krayzman, Christopher Wang, Taek-

wan Yoon, Jacob Curtis , and Sal Elder . I benefited from a number of thoughtful

theoretical discussions with Linshu Li and William R Sweeney .

Our department would not run without the endless support and help provided to us

by Giselle M. DeVito, Maria P. Rao, Theresa Evangeliste , and Nuch

Graves , or that provided by Florian Carle and Racquel Miller for the Yale

Quantum Institute (YQI) .

My time at Yale would not be what it was without Open Labs , a science outreach

and careers pathways not-for-profit I founded in 2012, and the innumerable, wonderful

people who helped me develop it into a nation-wide organization that has reached over

3,000 young scholars and parents and coached more than several hundred graduate stu-

dents. In 2015, I had the good fortune to meet two of my best friends and kindred spirits,

Darryl Seligman and Sharif Kronemer . I am deeply grateful to Darryl for his

immeasurable effort in spearheading the expansion of Open Labs from Yale to Princeton,

Columbia, Penn, and Harvard, and to Sharif for further growing and shaping Open Labs

xv


-----


into a long-lasting sustainable organization. I would like to thank Maria Parente and

Claudia Merson for believing in my nascent idea of Open Labs and providing support

through Yale Pathways to Science . There are far too many other key people to

thank for their volunteer work with Open Labs, but I must acknowledge Jordan Feyn-

gold, Ian Weaver, Munazza Alam, Aida Behmard, Matt Grobis, Kirsten

Blancato, Nicole Melso, Shannon Leslie, Diane Yu, Lina Kroehling,

Christian Watkins, Arvin Kakekhani , and Charles Brown . More recently,

I wish to express my gratitude to Yale for recognizing me with the Yale-Jefferson Award

for Public Service and to the American Physical Society (APS) and National Science

Foundation (NSF) for supporting Open Labs with an outreach grant award.

Beyond the world of physics, I was fortunate to meet some of my best friends whose

support and good cheer I am deeply thankful for, including Rick Yang, Brian Ten-

nyson, Xiao Sun, Rasmus Kyng, Marius Constantin, Stafford Sheehan ,

and Luis J.P. Lorenzo . I am also very grateful to Olga Laur for her unstinting

support during the writing of this work. Finally, the people whose contributions are the

greatest yet the least directly visible are my family members. There are no words to

describe the incomparable debt I owe each of you, especially to my parents Lora and

Kris , and to those painfully no longer among us  my grandparents, Angelina and

Tzvetko , to whom I dedicate my dissertation. Your richness of knowledge, creativity

in science and art, and unconditional love remain a beacon of inspirational light. Thank

you!

 _If I have seen a little further, it is by standing on the shoulders of Giants._ 

- Isaac Newton, "Letter from Sir Isaac Newton to Robert Hooke,

Historical Society of Pennsylvania.

xvi


-----


### Overview

_Can there be, despite the indeterminism of quantum physics, a possibility to know_

_if a quantum jump is about to occur or not?_

Chapter 1 opens by introducing the notion of a quantum jump between discrete en-

ergy levels of a quantum system, a theoretical idea introduced by Bohr in 1913 (Bohr,

1913)  yet, one whose existence was experimentally observed only seven decades later

(Nagourney _et al._ , 1986, Sauter _et al._ , 1986, Bergquist _et al._ , 1986), in a single atomic

three-level system. Section 1.1 outlines our proposal to map out the dynamics of a quan-

tum jump from the ground, _|_ G __ , to an excited, _|_ D __ , state of a three-level superconducting

system. We propose a protocol to catch quantum jumps mid-flight and, further, to re-

verse them prior to their completion. The proposal critically hinges on achieving near

unit-measurement efficiency, as discussed, and experimentally demonstrated, in Sec. 1.2.

Building on this, the catch and reverse experimental protocols and measurement results

are presented in Sections 1.3 and 1.4. These results directly demonstrate that the answer

to the above-posed question can indeed be in the affirmative. Section 1.4 summarizes the

experimental results that demonstrate the deterministic prevention of the completion of

jumps; this experiment thereby precludes quantum jumps from occurring altogether. A

control experiment in which the feedback intervention does not exploit the deterministic

character of the completed jumps is presented. Before proceeding to the remainder of


-----


the thesis, Section 1.5 provides a brief discussion of the main results and their implica-

tions for the hundred-year-long debate on the nature and reality of quantum jumps. The

section concludes by providing an outlook for the implications of the results for future

experiments. The remaining chapters, whose individually aim is described in the following

paragraphs, provide further support to the main conclusions presented in Chapter 1 and

devoted special attention to explicating the theory and experimental methodology of the

work.

Chapter 2 develops the essential background needed to gain access to the core ideas

and results of quantum measurement theory and its formulation, which lead to the catch

and reverse theoretical prediction and modeling of the experiment. The basic notions of

the formalism are introduced in view of specific examples. Building on this background,

Chapter 3 develops the quantum trajectory description of the quantum jumps observed

in the three-level atom. The basic ideas as well as the rigorous, quantitative description

of the continuous, coherent, and deterministic evolution of a completed quantum jump

is presented. Finally, the realistic model of the experiment including known imperfections

is developed. Chapter 4 details the experimental methods, including our approach to

the design of the superconducting quantum devices developed in Minev _et al._ (2018).

Section 4.1.1 provides a nutshell introduction to this approach, referred to as the energy-

participation-ratio (EPR) approach and used to design and optimize both the dissipative

and Hamiltonian parameters of our circuit-quantum-electrodynamic (cQED) systems.

Chapter 5 presents the results of control experiments that further support the con-

clusions reached in Chapter 1. The comparison between the experimental results and

the predictions of the quantum trajectory theory developed in Chapter 3 is provided in

Sec. 5.5. Chapter 6 summarizes the results of this dissertation and discusses future re-

search directions.


-----


### Introduction and main results

If all this damned quantum jumping
were really to stay, I should be sorry I
ever got involved with quantum
theory.

Erwin Schrdinger
_Brit. J. Philos. Sci. III_ , 109 (1952)

Bohr conceived of quantum jumps Bohr (1913) in 1913, and while Einstein elevated their

hypothesis to the level of a quantitative rule with his AB coefficient theory (Einstein, 1916,

1917), Schrdinger strongly objected to their existence (Schrdinger, 1952). The nature

and existence of quantum jumps remained a subject of controversy for seven decades until

they were directly observed in a single system (Nagourney _et al._ , 1986, Sauter _et al._ , 1986,

Bergquist _et al._ , 1986). Since then, quantum jumps have been observed in a variety of

atomic (Basche _et al._ , 1995, Peil and Gabrielse, 1999, Gleyzes _et al._ , 2007, Guerlin _et al._ ,

2007) and solid-state (Jelezko _et al._ , 2002, Neumann _et al._ , 2010, Robledo _et al._ , 2011,

Vijay _et al._ , 2011, Hatridge _et al._ , 2013) systems. Recently, quantum jumps have been

recognized as an essential phenomenon in quantum feedback control (Delglise _et al._ ,

2008, Sayrin _et al._ , 2011), and in particular, for detecting and correcting decoherence-


-----


1.1. Principle of the experiment 4

induced errors in quantum information systems (Sun _et al._ , 2013, Ofek _et al._ , 2016).

Here, we focus on the canonical case of quantum jumps between two levels indirectly

monitored by a third  the case that corresponds to the original observation of quantum

jumps in atomic physics (Nagourney _et al._ , 1986, Sauter _et al._ , 1986, Bergquist _et al._ ,

1986), see the level diagram of Fig. 1.1a. A surprising prediction emerges according to

quantum trajectory theory (see Carmichael (1993), Porrati and Putterman (1987), Ruskov

_et al._ (2007) and Chapter 2): not only does the state of the system evolve continuously

during the jump between the ground _|_ G __ and excited _|_ D __ state, but it is predicted that

there is always a latency period prior to the jump, during which it is possible to acquire a

signal that warns of the imminent occurrence of the jump (see Chapter 3 for the theoretical

analysis and mathematical treatment). This advance warning signal consists of a rare,

particular lull in the excitation of the ancilla state _|_ B __ . The acquisition of this signal

requires the time-resolved detection of _every_ de-excitation of _|_ B __ . Instead, exploiting the

specific advantages of superconducting artificial atoms and their quantum-limited readout

chain, we designed an experiment that implements with maximum fidelity and minimum

latency the detection of the advance warning signal occurring before the quantum jump

(see rest of Fig. 1.1).

###### 1.1 ###### Principle of the experiment

First, we developed a superconducting artificial atom with the necessary V-shape level

structure (see Fig. 1.1a and Section 4.1). It consists, besides the ground level _|_ G __ , of one

protected, dark level _|_ D __  engineered to not couple to any dissipative environment or

any measurement apparatus  and one ancilla level _|_ B __ , whose occupation is monitored

at rate  . Quantum jumps between _|_ G __ and _|_ D __ are induced by a weak Rabi drive  DG

 although this drive might eventually be turned off during the jump, as explained later.


-----


1.1. Principle of the experiment 5

Since a direct measurement of the dark level is not possible, the jumps are monitored

using the Dehmelt shelving scheme (Nagourney _et al._ , 1986). Thus, the occupation of


_|_ G __ is linked to that of _|_ B __ by the strong Rabi drive  BG (  DG __  BG __  ). In the

atomic physics shelving scheme (Nagourney _et al._ , 1986, Sauter _et al._ , 1986, Bergquist

_et al._ , 1986), an excitation to _|_ B __ is recorded with a photodetector by detecting the

emitted photons from _|_ B __ as it cycles back to _|_ G __ . From the detection events  referred

to in the following as clicks  one infers the occupation of _|_ G __ . On the other hand,

from a prolonged absence of clicks (to be defined precisely in Chapter 3), one infers that

a quantum jump from _|_ G __ to _|_ D __ has occurred. Due to the poor collection efficiency

and dead-time of photon counters in atomic physics (Volz _et al._ , 2011), it is exceedingly

difficult to detect every individual click required to faithfully register the origin in time

of the advance warning signal. However, superconducting systems present the advantage

of high collection efficiencies (Vijay _et al._ , 2012, Rist _et al._ , 2013, Murch _et al._ , 2013a,

Weber _et al._ , 2014, Roch _et al._ , 2014, De Lange _et al._ , 2014, Campagne-Ibarcq _et al._ ,

2016b), as their microwave photons are emitted into one-dimensional waveguides and are

detected with the same detection efficiencies as optical photons. Furthermore, rather

than monitoring the direct fluorescence of the _|_ B __ state, we monitor its occupation by

dispersively coupling it to an ancilla readout cavity. This further improves the fidelity

of the detection of the de-excitation from _|_ B __ (effective collection efficiency of photons

emitted from _|_ B __ ).

The readout cavity, schematically depicted in Fig. 1.1a by an LC circuit, is resonant

at __ C = 8979 _._ 64 MHz and cooled to 15 mK. Its dispersive coupling to the atom results

in a conditional shift of its resonance frequency by __ B _/_ 2 __ = __ 5 _._ 08 __ 0 _._ 2 MHz ( __ D _/_ 2 __ =

__ 0 _._ 33 __ 0 _._ 08 MHz ) when the atom is in _|_ B __ ( _|_ D __ ), see Fig. 1.1c. The engineered large

asymmetry between __ B and __ D together with the cavity coupling rate to the output

waveguide, _/_ 2 __ = 3 _._ 62 __ 0 _._ 05 MHz , renders the cavity response markedly resolving for


-----


1.1. Principle of the experiment 6

|a|Col2|
|---|---|
|a Bright B||
| Dark D  BG  (t) DG Ground G||


![Mivev_Thesis.pdf-22-7.png](Mivev_Thesis.pdf-22-7.png)

![Mivev_Thesis.pdf-22-9.png](Mivev_Thesis.pdf-22-9.png)

![Mivev_Thesis.pdf-22-8.png](Mivev_Thesis.pdf-22-8.png)

![Mivev_Thesis.pdf-22-2.png](Mivev_Thesis.pdf-22-2.png)

![Mivev_Thesis.pdf-22-4.png](Mivev_Thesis.pdf-22-4.png)

![Mivev_Thesis.pdf-22-5.png](Mivev_Thesis.pdf-22-5.png)

![Mivev_Thesis.pdf-22-1.png](Mivev_Thesis.pdf-22-1.png)

![Mivev_Thesis.pdf-22-6.png](Mivev_Thesis.pdf-22-6.png)

![Mivev_Thesis.pdf-22-3.png](Mivev_Thesis.pdf-22-3.png)

![Mivev_Thesis.pdf-22-0.png](Mivev_Thesis.pdf-22-0.png)

**Figure 1.1** _|_ **Principle of the experiment. a,**
Three-level atom possessing a hidden transition (shaded region) between its ground _|_ G __ and dark _|_ D __ state, driven by Rabi
drive  DG ( _t_ ) . Quantum jumps between _|_ G __ and _|_ D __ are indirectly monitored by a stronger
Rabi drive  BG between _|_ G __ and the bright state _|_ B __ , whose occupancy is continuously
monitored at rate  by an auxiliary oscillator (LC circuit on right), itself measured in
reflection by continuous-wave microwave light (depicted in light blue). When the atom
is in _|_ B __ , the LC circuit resonance frequency shifts to a lower frequency than when the
atom is in _|_ G __ or _|_ D __ (effect schematically represented by switch). Therefore, the probe
tone performs a _|_ B __ /not- _|_ B __
measurement on the atom, and is blind to any superposition of _|_ G __ and _|_ D __ . **b,** The actual atom and LC oscillator used in the experiment is
a superconducting circuit consisting of two strongly-hybridized transmon qubits placed
inside a readout resonator cavity at 15 mK. Control signals for the atom and cavity are
supplied by a room-temperature field-programmable gate array (FPGA) controller. This
fast electronics monitors the reflected signal from the cavity, and after demodulation and
filtering, actuates the control signals. The amplifier chain includes circulators (curved
arrows) and amplifiers (triangles and trapezoids). **c,** Frequency landscape of atom and
cavity responses, overlaid with the control tones shown as vertical arrows. The cavity pull
__ of the atom is nearly identical for _|_ G __ and _|_ D __ , but markedly distinct for _|_ B __ . The BG
drive is bi-chromatic in order to address the bright transition independently of the cavity
state. **d,** Hierarchy of timescales involved in the experiment, which are required to span
5 orders of magnitude. Symbols explained in text, and summarized in Table 5.2.


-----


1.1. Principle of the experiment 7

_|_ B __ vs. not- _|_ B __ , yet non-resolving (Gambetta _et al._ , 2011, Rist _et al._ , 2013, Roch _et al._ ,

2014) for _|_ G __ vs. _|_ D __ , thus preventing information about the dark transition from reaching


the environment. When probing the cavity response at __ C __ __ B , the cavity either remains

empty, when the atom is in _|_ G __ or _|_ D __ , or fills with  _n_ = 5 __ 0 _._ 2 photons when the atom is

in _|_ B __ . This readout scheme yields a transduction of the _|_ B __ -occupancy signal with five-

fold amplification, which is an important advantage to overcome the noise of the following

amplification stages. To summarize, in this readout scheme, the cavity probe inquires: Is


the atom in _|_ B __ or not? The time needed to arrive at an answer with a confidence level

of 68% (signal-to-noise ratio of 1) is  __ 1 __ 1 _/_ ( __ _n_  ) = 8 _._ 8 ns for an ideal amplifier chain

(see Chapter 3).

Importantly, the engineered near-zero coupling between the cavity and the _|_ D __ state

protects the _|_ D __ state from harmful effects, including Purcell relaxation, photon shot-noise

dephasing, and the yet unexplained residual measurement-induced relaxation in supercon-

ducting qubits (Slichter _et al._ , 2016). We have measured the following coherence times for

the B state: energy relaxation _T_ 1 D = 116 5 __ s , Ramsey coherence _T_ D 2R = 120 5 __ s ,
_|_ __ __ __

and Hahn echo _T_ 2E D = 162 6 __ s . While protected, the D state is indirectly quantum-

__ _|_ __

non-demolition (QND) read out by the combination of the V-structure, the drive between

_|_ G __ and _|_ B __ , and the fast _|_ B __ -state monitoring. In practice, we can access the popula-

tion of _|_ D __ using an 80 ns unitary pre-rotation among the levels followed by a projective

measurement of _|_ B __ (see Chapter 5).

Once the state of the readout cavity is imprinted with information about the occupation

of _|_ B __ , photons leak through the cavity output port into a superconducting waveguide,

which is connected to the amplification chain, see Fig. 1.1b, where they are amplified

by a factor of 10 12 . The first stage of amplification is a quantum-limited Josephson

parametric converter (JPC) (Bergeal _et al._ , 2010), followed by a high-electron-mobility

transistor (HEMT) amplifier at 4 K. The overall quantum efficiency of the amplification


-----


1.2. Unconditioned monitoring of the quantum jumps 8

chain is __ = 0 _._ 33 __ 0 _._ 03 . At room temperature, the heterodyne signal is demodulated by

a home-built field-programmable gate array (FPGA) controller, with a 4 ns clock period

for logic operations. The measurement record consists of a time series of two quadrature

outcomes, _I_ rec and _Q_ rec , every 260 ns, which is the integration time _T_ int , from which the

FPGA controller estimates the state of the atom in real time. To reduce the influence of

noise, the controller applies a real-time, hysteretic IQ filter (see Section 5.3.1), and then,

from the estimated atom state, the control drives of the atom and readout cavity are

actuated, realizing feedback control.

###### 1.2 ###### Unconditioned monitoring of the quantum jumps

Having described the setup of the experiment, we proceed to report its results. The field

reflected out of the cavity is monitored in a free-running protocol, for which the atom is

subject to the continuous Rabi drives  BG and  DG , as depicted in Fig. 1.1. Figure 1.2a

shows a typical trace of the measurement record, displaying the quantum jumps of our

three-level artificial atom. For most of the duration of the record, _I_ rec switches rapidly

between a low and high value, corresponding to approximately 0 ( _|_ G __ or _|_ D __ ) and 5

( _|_ B __ ) photons in the cavity, respectively. The spike in _Q_ rec at _t_ = 210 __ s is recognized

by the FPGA logic as a short-lived excursion of the atom to a higher excited state (see

Section 5.3.1). The corresponding state of the atom, estimated by the FPGA controller,

is depicted by the color of the dots. A change from _|_ B __ to not- _|_ B __ is equivalent to a

click event, in that it corresponds to the emission of a photon from _|_ B __ to _|_ G __ , whose

occurrence time is shown by the vertical arrows in the inferred record d _N_ ( _t_ ) (top). We

could also indicate upward transitions from _|_ G __ to _|_ B __ , corresponding to photon absorption

events (not emphasized here), which would not be detectable in the atomic case.

In the record, the detection of clicks stops completely at _t_ = 45 __ s , which reveals a


-----


1.3. Catching the quantum jump 9

quantum jump from _|_ G __ to _|_ D __ . The state _|_ D __ survives for 90 __ s before the atom returns

to _|_ G __ at _t_ = 135 __ s , when the rapid switching between _|_ G __ and _|_ B __ resumes until a

second quantum jump to the dark state occurs at _t_ = 350 __ s . Thus, the record presents

jumps from _|_ G __ to _|_ D __ in the form of click interruptions.

In Fig. 1.2b, which is based on the continuous tracking of the quantum jumps for

3.2 s, a histogram of the time spent in not- _|_ B __ , __ not-B , is shown. The panel also shows

a fit of the histogram by a bi-exponential curve that models two interleaved Poisson

processes. This yields the average time the atom rests in _|_ G __ before an excitation to _|_ B __ ,

 __ BG 1 = 0 _._ 99 0 _._ 06 __ s , and the average time the atom stays up in D before returning to

__ _|_ __

G and being detected,  __ GD 1 = 30 _._ 8 0 _._ 4 __ s . The average time between two consecutive
_|_ __ __

G to D jumps is  __ DG 1 = 220 5 __ s . The corresponding rates depend on the atom
_|_ __ _|_ __ __

drive amplitudes (  DG and  BG ) and the measurement rate  (see Chapter 3). Crucially,

all the rates in the system must be distributed over a minimum of 5 orders of magnitude,

as shown in Fig. 1.2d.

###### 1.3 ###### Catching the quantum jump

Having observed the quantum jumps in the free-running protocol, we proceed to con-

ditionally actuate the system control tones in order to tomographically reconstruct the

time dynamics of the quantum jump from _|_ G __ to _|_ D __ , see Fig. 1.3a. Like previously, af-

ter initiating the atom in _|_ B __ , the FPGA controller continuously subjects the system to

the atom drives (  BG and  DG ) and to the readout tone ( R ). However, in the event

that the controller detects a single click followed by the complete absence of clicks for

a total time  _t_ catch , the controller suspends all system drives, thus freezing the system

evolution, and performs tomography, as explained in Section 5.2.2. Note that in each

realization, the tomography measurement yields a single +1 or -1 outcome, one bit of


-----


1.3. Catching the quantum jump 10


|Col1| BG|
|---|---|
|||
|||


![Mivev_Thesis.pdf-26-1.png](Mivev_Thesis.pdf-26-1.png)

![Mivev_Thesis.pdf-26-0.png](Mivev_Thesis.pdf-26-0.png)

Time-record position (  s)


 not-B (  s)


**Figure 1.2** _|_
**Unconditioned monitoring of quantum jumps in the 3-level system. a,** Typical measurement of integrated, with duration _T_ int _,_ quadratures _I_ rec and _Q_ rec
of signal reflected from readout cavity as a function of time. The color of the dots (see
legend) denotes the state of the atom estimated by a real-time filter implemented with
the FPGAs (see Section 5.3.1). On top, the vertical arrows indicate click events ( d _N_ )
corresponding to the inferred state changing from _|_ B __ to not- _|_ B __ . The symbol __ not-B
corresponds to the time spent in not- _|_ B __ , which is the time between two clicks minus the last
duration spent in _|_ B __ . An advance warning that a jump to _|_ D __ is occurring is triggered
when _no_ click has been observed for a duration  _t_ catch , which is chosen between 1 and
12 __ s at the start of the experiment. **b,** Log-log plot of the histogram of __ not-B (shaded
green) for 3.2 s of continuous data of the type of panel (a). Solid line is a bi-exponential
fit defining jump rates  BG = (0 _._ 99 __ 0 _._ 06 __ s) __ 1 and  GD = (30 _._ 8 __ 0 _._ 4 __ s) __ 1 .

information for a single density matrix component. We also introduce a division of the

duration  _t_ catch into two phases, one lasting  _t_ on during which  DG is left on and one

lasting  _t_ off =  _t_ catch __  _t_ on during which  DG is turned off. As we explain below, this

has the purpose of demonstrating that the evolution of the jump is not simply due to the

Rabi drive between _|_ G __ and _|_ D __ .

In Fig. 1.3b, we show the dynamics of the jump mapped out in the full presence of

the Rabi drive,  GD , by setting  _t_ off = 0 . From 3 _._ 4 __ 10 6 experimental realizations we

reconstruct, as a function of  _t_ catch , the quantum state, and present the evolution of the

jump from _|_ G __ to _|_ D __ as the normalized, conditional GD tomogram (see Section 5.2.2).

For  _t_ catch _<_ 2 __ s , the atom is predominantly detected in _|_ G __ ( _Z_ GD = __ 1 ), whereas for

 _t_ catch _>_ 10 __ s , it is predominantly detected in _|_ D __ ( _Z_ GD = +1 ). Imperfections, due

to excitations to higher levels, reduce the maximum observed value to _Z_ GD = +0 _._ 9 (see

Section 5.5).


-----


1.3. Catching the quantum jump 11

########## a ########## R ########## ...


dN( _t_


|>|...|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||B|...||||||
|Prep|...|||||Tomo.|
||...|t t on off|||||
||||||||
||||t catch||||


|Col1|Z GD X experiment GD theory Y GD t t = 0 mid off|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|t on Z X GD GD Y GD t t = t - t mid off catch on||||||||


Catch time  _t_ catch (  s)


**Figure 1.3** _|_ **Catching the quantum jump mid-flight. a,** The atom is initially
prepared in _|_ B __ . The readout tone ( R ) and atom Rabi drive  BG are turned on until the
catch condition is fulfilled, consisting of the detection of a click followed by the absence of
click detections for a total time  _t_ catch . The Rabi drive  DG starts with  BG , but can be
shut off prematurely, prior to the end of  _t_ catch . A tomography measurement is performed
after  _t_ catch . **b & c,** Conditional tomography revealing the continuous, coherent, and,
surprisingly, deterministic flight (when completed) of the quantum jump from _|_ G __ to _|_ D __ .
The error bars are smaller than the size of the dots. The mid-flight time  _t_ mid is defined
by _Z_ GD = 0 . The jump proceeds even when  DG is turned off at the beginning of the
flight (panel c),  _t_ on = 2 __ s . Data obtained from 6 _._ 8 __ 10 6 experimental realizations.
Solid lines: theoretical prediction (see Sec. 5.5). Dashed lines in panel c: theory curves for
the  _t_ on interval, reproduced from panel b. The data suggests that an advance-warning
signal of the jump can be provided by a no-click period for catch time  _t_ catch =  _t_ mid ,
at which half of the jumps will complete.


-----


1.3. Catching the quantum jump 12

For intermediate no-click times, between  _t_ catch = 2 __ s and  _t_ catch = 10 __ s , the

state of the atom evolves continuously and coherently from _|_ G __ to _|_ D __  the flight of the


quantum jump. The time of mid flight,  _t_ mid __ 3 _._ 95 __ s , is markedly shorter than the Rabi



2 BG __ 1 ln  2 BG

2  DG
 


period 2 _/_  DG = 50 __ s , and is given by the function  _t_ mid =  2 BG


BG + 1

 DG 


in which  DG enters logarithmically (see Section 3.1.1). The maximum coherence of


the superposition, corresponding to


_X_ GD 2 + _Y_ 2 GD , during the flight is 0 _._ 71 0 _._ 005 ,

__


quantitatively understood to be limited by several small imperfections (see Section 5.5).

Motivated by the exact quantum trajectory theory, we fit the experimental data with

the analytic form of the jump evolution, Z GD ( _t_ catch ) = _a_ + _b_ tanh( _t_ catch _/_ + _c_ ) ,

X GD ( _t_ catch ) = _a_ __ + _b_ __ sech( _t_ catch _/_ __ + _c_ __ ) , and Y GD ( _t_ catch ) = 0 . We compare the

fitted jump parameters ( _a, a_ __ _, b, b_ __ _, c, c_ __ _, , _ __ ) to those calculated from the theory and

numerical simulations using independently measured system characteristics (see Section

5.5).

By repeating the experiment with  _t_ on = 2 __ s , in Fig. 1.3c, we show that the jump

proceeds even if the GD drive is shut off at the beginning of the no-click period. The

jump remains coherent and only differs from the previous case in a minor renormalization

of the overall amplitude and timescale. The mid-flight time of the jump,  _t_ __ mid , is given

by an updated formula (see Chapter 3). The results demonstrate that the role of the Rabi

drive  DG is to initiate the jump and provide a reference for the phase of its evolution 1 .

Note that the  _t_ catch __  _t_ mid non-zero steady state value of _X_ GD in Fig. 1.3b is the

result of the competition between the Rabi drive  DG and the effect of the measurement

of _|_ B __ . This is confirmed in Fig. 1.3c, where  DG = 0 , and where there is no offset in

the steady state value.

1 A similar phase reference for a non-unitary, yet deterministic, evolution induced by measurement
was previously found in a different context in: N. Katz, M. Ansmann, R. C. Bialczak, E. Lucero, R.
McDermott, M. Neeley, M. Steffen, E. M. Weig, A. N. Cleland, J. M. Martinis, and A. N. Korotkov,
Science (New York, N.Y.) 312, 1498 (2006).


-----


1.4. Reversing the quantum jump 13

The results of Fig. 1.3 demonstrate that despite the unpredictability of the jumps from

_|_ G __ to _|_ D __ , they are preceded by an identical no-click record. While the jump starts at

a random time and can be prematurely interrupted by a click, the deterministic nature

of the flight comes as a surprise given the quantum fluctuations in the heterodyne record

_I_ rec during the jump  an island of predictability in a sea of uncertainty.

###### 1.4 ###### Reversing the quantum jump

In Fig. 1.4b, we show that by choosing  _t_ catch =  _t_ mid for the no-click period to serve

as an advance warning signal, we reverse the quantum jump 2 in the presence of  DG ; the

same result is found when  DG is off, see Section 3.1.3. The reverse pulse characteristics

are defined in Fig. 1.4a. For __ I = _/_ 2 , our feedback protocol succeeds in reversing the

jump to _|_ G __ with 83 _._ 1% __ 0 _._ 3% fidelity, while for __ I = 3 _/_ 2 , the protocol completes the

jump to _|_ D __ , with 82 _._ 0% __ 0 _._ 3% fidelity. In a control experiment, we repeat the protocol by

applying the reverse pulse at random times, rather than those determined by the advance

warning signal. Without the advance warning signal, the measured populations only reflect

those of the ensemble average.

In a final experiment, we programmed the controller with the optimal reverse pulse pa-

rameters _{_ __ _I_ ( _t_ catch ) _, _ _I_ ( _t_ catch ) _}_ , and as shown in Fig. 1.4c, we measured the success

of the reverse protocol as a function of the catch time,  _t_ catch . The closed/open dots

indicate the results for  DG on/off, while the solid curves are theory fits motivated by

the exact analytic expressions (see Chapter 3). The complementary red dots and curves

reproduce the open-loop results of Fig. 1.3 for comparison.

2 Reversal of quantum jumps have been theoretically considered in different contexts, see H. Mabuchi
and P. Zoller, Phys. Rev. Lett. 76, 3108 (1996) and R. Ruskov, A. Mizel, and A. N. Korotkov, Phys.
Rev. B 75, 220501(R) (2007).


-----


1.4. Reversing the quantum jump 14

########## a ########## b

######## Z ########  ######## DG ######## on


![Mivev_Thesis.pdf-30-0.png](Mivev_Thesis.pdf-30-0.png)

![Mivev_Thesis.pdf-30-3.png](Mivev_Thesis.pdf-30-3.png)

######## X


![Mivev_Thesis.pdf-30-1.png](Mivev_Thesis.pdf-30-1.png)

Reverse pulse angle  I

![Mivev_Thesis.pdf-30-2.png](Mivev_Thesis.pdf-30-2.png)

Catch and reverse duration  _t_ catch (  s)


_P_ G


**Figure 1.4** _|_ **Reversing the quantum jump mid-flight. a,** Bloch sphere of the
GD manifold, showing the axis X for the jump reversal, defined by the azimuthal angle
__ I . The angle of the intervention pulse is __ I . **b,** Success probabilities _P_ G (purple) and
_P_ D (orange) to reverse to _|_ G __ and complete to _|_ D __ the quantum jump mid-flight at
 _t_ catch =  _t_ mid , with __ I = _/_ 2 , in the presence of the Rabi drive  DG . The error bars
are smaller than the size of the dots. Black dots: success probability for _|_ G __ (closed dots)
and _|_ D __ (open dots) in a control experiment where intervention is applied at random
times along the record, rather than at  _t_ catch . **c,** Optimal success of reverse protocol
(purple) as a function of  _t_ catch . The FPGA controller is programmed with the optimal
_{_ __ _I_ ( _t_ catch ) _, _ _I_ ( _t_ catch ) _}_ . Closed and open dots correspond to  _t_ on =  _t_ catch and
 _t_ on = 2 __ s , respectively. Red points show the corresponding open-loop (no intervention)
results from Fig. 1.3b and c.


-----


1.5. Discussion of main results 15

###### 1.5 ###### Discussion of main results

From the experimental results of Fig. 1.2a one can infer, consistent with Bohrs initial

intuition and the original ion experiments, that quantum jumps are random and discrete.

Yet, the results of Fig. 1.3 support a contrary view, consistent with that of Schrdinger:

the evolution of the jump is coherent and continuous. Noting the difference in time scales

in the two figures, we interpret the coexistence of these seemingly opposed point of views

as a unification of the discreteness of countable events like jumps with the continuity of

the deterministic Schrdingers equation. Furthermore, although all 6 _._ 8 __ 10 6 recorded

jumps (Fig. 1.3) are entirely independent of one another and stochastic in their initiation

and termination, the tomographic measurements as a function of  _t_ catch explicitly show

that all jump evolutions follow an essentially identical, predetermined path in Hilbert space

 not a randomly chosen one  and, in this sense, they are deterministic. These results

are further corroborated by the reversal experiments shown in Fig. 1.4, which exploit the

continuous, coherent, and deterministic nature of the jump evolution and critically hinge

on priori knowledge of the Hilbert space path. With this knowledge ignored in the control

experiment of Fig. 1.4b, failure of the reversal is observed.

In conclusion (see Chapter 6 for an expanded discussion), these experiments revealing

the coherence of the jump, promote the view that a single quantum system under efficient,

continuous observation is characterized by a time-dependent state vector inferred from

the record of previous measurement outcomes, and whose meaning is that of an objective,

generalized degree of freedom. The knowledge of the system on short timescales is not

incompatible with an unpredictable switching behavior on long time scales. The excellent

agreement between experiment and theory including known experimental imperfections

(see Sec. 5.5) thus provides support to the modern quantum trajectory theory and its

reliability for predicting the performance of real-time intervention techniques in the control


-----


1.5. Discussion of main results 16

of single quantum systems.


-----


### Quantum measurement theory

In quantum physics, you dont see
what you get, you get what you see.

A.N. Korotkov
Private communication

his chapter provides a general background to the central ideas and results of quan-

tum measurement theory. It begins with a prelude, Section 2.1, where the ele-

## T

mentary notions of the measurement formalism are introduced. These are developed,

in Sections 2.1.1 and 2.1.2, within the framework of probability theory. For simplicity,

the initial discussion is concerned with measurements of classical systems. Section 2.1.3

extends the discussion to measurements of quantum systems, and it is seen that many

of the concepts developed in the classical setting directly carry over. The tack of this

approach makes it easy to discern the classical from the quantum aspects of measure-

ments. The ideas and results of Sec. 2.1 are extended to time-continuous measurements

in Sec. 2.2 by way of a specific example before generalizing to arbitrary systems. Specif-

ically, we construct a microscopic description of the homodyne monitoring of a qubit,

using only two-level ancillary systems. Although the time-discrete model is simple and

is readily solved, it contains sufficient generality to illustrate the principal ideas of con-

17


-----


2.1. Prelude: from classical to quantum measurements 18

tinuous quantum measurements. The concept of a stochastic path taken by the state

of a monitored quantum system over time, known as its _quantum trajectory_ , naturally

emerges from the discussion. A higher degree of mathematical rigor of the description

follows in Section. 2.2.3, which takes the continuous limit of our time-discrete model, thus

allowing the natural development of the basic notions of stochastic calculus; in particular,

the calculus of a Wiener process (Gaussian white noise) is mathematically formulated.

Finally, Section 2.3 generalizes the results of the former section to formulate the general

theory of quantum measurements and quantum trajectories. This framework sets the

stage for the description of the quantum jumps experiment presented in Chapter 3 (see

also 5). Suggestions for further reading on the formulation of quantum trajectory theory

are provided in Section 2.4.

###### 2.1 ###### Prelude: from classical to quantum measure-

 ments

This section provides an introduction to the basic concepts of measurement theory. Before

discussing a measurement of a quantum system, it is helpful to develop and to understand

the description of general, disturbing classical measurements. 1 One finds that the proba-

bilistic formulation of these greatly parallels that of quantum measurements. In this way,

it provides a closest approach to the quantum one from the simpler, classical framework.

Notably, many key ideas carry over  but, with a few modifications that prove profound

and lead to the departure of the quantum measurements from classical ones. For con-

creteness, throughout the discussion, we keep the simplest possible example in view as we

develop the theory, usually based on a classical or quantum bit. While self-contained and

1 For further reading on classical measurement theory, we suggest Refs. Wiseman and Milburn (2010)
and Jacobs (2014). Our notation closely follows that of Wisemans book.


-----


2.1. Prelude: from classical to quantum measurements 19

thorough, our discussion cannot hope to be exhaustive, and hence, for further reading, we

refer the reader to the references suggested in Section 2.4.

######### 2.1.1 ######### Classical measurement theory: basic concepts

Let us begin with the absolute minimum needed to discuss a measurement of a classical

system. Leading with the example of the simplest, smallest classical system, a bit, we

first establish the notions needed to describe the system and then the measurement.

**The simplest, smallest classical system  a bit.** The simplest, smallest classical

system is one that, at a given time, can be described by only one of two possible config-

urations. 2 A concrete, familiar example is that of a coin on a table, which is either heads

or tails. More generally, such a system with two possible configurations (a bit worth of

information) could represent any number of physical situations; for instance, the bit could

represent the tilt of a mechanical seesaw on a playground (the seesaw is tilted either to the

left or to the right), or, for instance, in a classical computer, it could represent the digital

logic bit corresponding to the thresholded voltage value at the output of a transistor (for

example, the two configuration could be that the voltage is less than five volts or not).

_Description of the system._ Continuing with the coin example, the configuration of the

coin is specified by a single property, corresponding to the binary question: Is the coin tails,

or not? Mathematically, this property can be specified by a variable, which we will denote

_S_ , and which takes only one of two _values._ 3 Specifically, in anticipation of the discussion

In some contexts, the term state is sometimes employed instead of the term configuration. However, within the context of classical measurement theory, the term state is typically reserved for probability distributions only, which will be introduced shortly. The motivation for this choice of terminology 2
is by analogy with quantum measurement theory, where the state of the system describes, in effect, a
probability distribution.
3 Of course, we could use a representation where the binary values _S_ can take are H for heads and
T for tails. We could then endow these symbols, H and T, with an algebraic structure. However, a
more familiar and systematic approach is to use ordinary, real numbers, as employed in the following.


-----


2.1. Prelude: from classical to quantum measurements 20

of a qubit, 4 let us choose to assign the value _S_ = 1 to correspond to the coin when it is

tails and _S_ = __ 1 for heads. 5 Analogously, a general classical system is described by its

_configuration_ , which is specified by a set of _variables,_ each of which describes an intrinsic

property of the system, such as a degree of freedom. These properties and variables are

known to have _objective, definite values_ for a classical system.

_From perfect to probabilistic measurements._ In principle, a perfect measurement of

a classical system can be performed to unambiguously obtain the values of the system

variables, even without disturbing the system. As such, an observer of the system can

perform measurements to determine the unambiguous configuration of the system. In this

case, the observer acquires complete information about the system, and learns everything

there is to know about it. If the system is also deterministic, then the observer has thus

additionally gained complete knowledge of the result of all possible future measurements

on the system. Under these conditions, the description of the system is exhaustive, and

there isnt much more to say about measurements. However, these ideal conditions are

often not met in practice. Measurements are often imperfect, ensembles of non-identical

system have to be considered, etc. These situations require a description of the system and

measurements that is inherently probabilistic. This description is the concern of classical

measurement theory. In the following, we first focus on the case of a probabilistic classical

system, whose description is somewhat analogous to that of an ensemble of quantum

systems.

**_Probabilistic bit system with perfect measurements._** For concreteness, consider

a coin that is prepared probabilistically, such as by a coin toss. Following the toss, an

4 We choose the values +1 and __ 1 , rather than 0 and 1 , in order to parallel the later discussion of
a quantum bit, and the outcome of the Pauli _Z_ measurement. For completeness, the values _S_ = 1 and
_S_ = __ 1 are analogous to the ground ( _|_ + _z_ __ ) and excited ( _|_ _z_ __ ) state of a qubit, respectively, which are
introduced in Sec. 2.1.3.
5 Note that at this stage, we assume no time dynamics of the system. This will be introduced in the
following.


-----


2.1. Prelude: from classical to quantum measurements 21


########## Classical bit

####### Z

########## 1

 p
 0

 -1


########## Quantum bit


![Mivev_Thesis.pdf-37-0.png](Mivev_Thesis.pdf-37-0.png)

![Mivev_Thesis.pdf-37-1.png](Mivev_Thesis.pdf-37-1.png)

![Mivev_Thesis.pdf-37-2.png](Mivev_Thesis.pdf-37-2.png)

**Figure 2.1** _|_ **Geometric representation of the state of a classical and quantum**
**bit. a,** State of a classical bit system represented as the one-dimensional probability
vector _p_ on the line segment Z between __ 1 and 1 (see Eq. (2.5) for the definition of Z).
**b,** State of quantum bit (qubit) represented as the three-dimensional Bloch vector. Unlike
the classical bit, the qubit has three observables (X, Y, and Z), which do not commute.
The quantum state of the qubit, __ , is bounded by the unit sphere. The surface of the
sphere contains all pure states, which can be parametrized by the angles __ and __ .

observer can perform a measurement of the coin variable _S_ , which yields a measurement

result. Formally, we should distinguish the measurement result obtained by the observer

from the actual value of the system property _S_ . For completeness, lets denote the variable

of the _measurement result_ of _S_ as _m_ _S_ . By analogy with _S_ , we could assign _m_ _S_ = __ 1

and _m_ _S_ = 1 to results that corresponds to heads and tails, respectively. The distinction

between the measurement result _m_ _S_ and system variable _S_ is crucial for imperfect and

quantum measurements. However, for simplicity, let us first proceed by assuming perfect,

classical measurements where there is no confusion between _S_ and _m_ _S_ , i.e, _m_ _S_ = _S_ . In

this case, _m_ _S_ is redundant, and for the following discussion there is no need to insist on

the distinction.

_State of the system  a probability distribution._ To describe the expected outcome

of a measurement on the system, we introduce the concept of the system _state_ . 6 The

6 For the following discussion, it suffices to adopt the point of view that the state of the system


-----


2.1. Prelude: from classical to quantum measurements 22

state describes the probability of a configuration to be the system state. In other words,

mathematically, the state is a probability distribution over all possible system configu-

rations, which form a space known as the _configuration space_ , denoted S ; for the bit,

S _{_ _S_ = 1 _, S_ = __ 1 _}_ . The probability for the coin be in the tails configuration, _S_ = 1 ,

is then written as Pr [ _S_ = 1] . More generally, the probability that the variable _S_ of the

system will have the value _s_ is Pr [ _S_ = _s_ ] ; for a bit, _s_ _{_ 1 _,_ __ 1 _}_ . 7 This description of

the classical system in terms of a probability distribution, Pr [ _S_ = _s_ ] , is analogous to the

density matrix description of a quantum system. 8 Motivated by the analogy, we express

the state of the coin bit as a vector of probabilities,


Pr [ _S_ = 1]

Pr [ _S_ = __ 1]


_._ (2.1)




_S_ __


Keeping in mind the constraint that a measurement always yields a result, one observes

that the sum of the probabilities must be one. Mathematically, the state vector _L_ 1 norm is



__
constrained, _S_ =
L1
 
    


_s_ Pr [ _S_ = _s_ ] = 1 , where L1 denotes the _L_ 1 norm. This property

_||_


is analogous to the unit-trace property of the density matrix of a quantum state. Using


this constrain, the state of the coin, Eq. (2.1), can be simplified to a single information

parameter _p_ , which denotes the bias of the coin,

1+ _p_


_,_ (2.2)




_S_ =


1 __ _p_


The bias parameter _p_ is a number between __ 1 and 1, 9 and, since it specifies the system


represents _subjective_ knowledge of the observer regarding the system.
7 In this section, we employ the convention that capital letters denote variables (typically, random
ones) and lower case letters denote values.
8 However, note that, as a probability, Pr [ _S_ = _s_ ] is a real and positive number between 0 and 1.
9 Mathematically, _p_ is a number in the convex hull defined by S .


-----


2.1. Prelude: from classical to quantum measurements 23

state, is a quantity of central importance. It can be viewed as the classical analog of

the Bloch vector of a quantum bit. In a sense, it represents a kind of one-dimensional

probability vector, which constitutes a geometric representation of the system state; see

Fig. 2.1a.

**Operations on the system.** An operation on the system results in a change of its

configuration. For the example of a coin, there are only two possible operations: i) the

coin is flipped (the logical negation operation, _not_ ) or ii) the coin is left as is (the _identity_

operation). Working within the framework of an ensemble of systems, an operation (one

that is applied to all systems in the ensemble) results in a change of the state of the

system that can be described by a linear map. The state of the system ensemble after

__ __
the operation, denoted _S_ __ , can then be written as _S_ __ = _U_ _S_ , where the linear map

is represented by a configuration-transition matrix, denoted _U_ . For the coin, the two

possible operations, the _identity_ and _not,_ take the following forms


and __ _x_ __




_,_ (2.3)




_I_ __


respectively. The bit-flip Pauli matrix is denoted __ _x_ .

**Perfect classical measurement of a system ensemble.** Consider the long-run av-

erage value a series of repeated measurements of the coin variable _S_ , for the example of

randomly prepared coins. The expected mean value of _S_ is the weighted average of the

results, defined as


E [ _S_ ] __


_s_ Pr [ _S_ = _s_ ] _,_ (2.4)


where E [ __ ] represents expectation value of and the sum is taken over all possible values

_s_ of _S_ . In matrix form, recalling Eq. (2.2), Eq. (2.4) simplifies to


-----


2.1. Prelude: from classical to quantum measurements 24

|Concept|Symbols|Definition / Description|
|---|---|---|



**Basic concepts**

|variable|S,E|Describes intrinsic property of system, has definite value independent of measurement apparatus|
|---|---|---|
|variable value|s, e|Specific value that a variable can take|
|probability|Pr [S = s]|Probability that variable S has value s|
|configuration|S , E , S, E { } { } { }|Set of all system variables|
|configuration space|S,E,J|Set of all possible system configurations|
|state|   S, E, J|Probability distribution on the configuration space, represented as a vector|
|expectation value|E [S]|Expected (mean) value of repeated measurements of S, see Eq. (2.4)|



**Table 2.1** _|_ **Basic concepts of classical measurement theory.**



__
E [ _S_ ] = __ _Z_ _S_ = _p ,_ (2.5)
L1
 

where _p_ is non-negative and we have introduced the measurement operator   __ _Z_ , associated

with the variable _S_ and given by the Pauli matrix


_._ (2.6)




__ _Z_
__


__ 1


The matrix formulation given by Eq. (2.5) for the expectation value of a classical mea-


surement bears marked resemblance to that employed with quantum systems. For a

measurement on a quantum bit, the expectation value of the _Z_ component of its spin

is given by Tr [ __ _z_ __ ] , where __ is the qubit density matrix,  __ _z_ is the Pauli Z operator,

represented by the matrix given in Eq. (2.6), and Tr [ __ ] denotes the trace function.


-----


2.1. Prelude: from classical to quantum measurements 25

**Composite system.** Extending the coin example, consider a composite system consist-

ing of two coins. The first coin is described by the variable _S_ , or in the ensemble situation,



__
by the state _S_ , defined over the configuration space S _{_ _S_ = 1 _, S_ = __ 1 _}_ . The second

1+ _p_ _E_



__
coin is similarly described by a single variable, _E_ , and a state _E_ =


, where _p_ _E_




1 _p_ _E_
__


is the coin bias. Its configuration space is E _{_ _E_ = 1 _, E_ = __ 1 _}_ . The configuration of


the composite system consists of the simultaneous specification of all variables, namely,

_S_ and _E_ . The set of all possible configurations of the composite system is

J = S __ E (2.7)

= 1 _S_ _,_ 1 _S_ 1 _E_ _,_ 1 _E_
_{_ __ _} {_ __ _}_

= 1 _S_ 1 _E_ _,_ 1 _S_ 1 _E_ _,_ 1 _S_ 1 _E_ _,_ 1 _S_ 1 _E_ _,_
_{_ __ __ __ __ _}_


where __ denotes the tensor product, and where, momentarily, we have used the notation

where 1 _S_ stands for _S_ = 1 . 10 The state of the composite system is a probability distri-

__
bution over J , which can be represented by a 4-dimensional probability vector, _J_ . When

the two subsystems are uncorrelated, the composite state is separable, and can be written

__ __ __
as a simple product of the states of the constituent subsystems, _J_ = _S_ __ _E_ . However,

when the subsystems are correlated, this is no longer possible. For concreteness, consider

the case where the two coins are prepared randomly but always the same, the correlated



__ 1
randomness of the two systems is described by the composite state _J_ = 2

 



,



1 _,_ 0 _,_ 0 _,_ 1

2 2


where  denotes the transposition operation. More generally, an operation that represents


an interaction between the two coins results in statistical correlations between them, and

thus renders the composite state inseparable. These features generally carry over to the

10 So that no confusion arises, we note that the dimension of the composite system space is not the
sum but is the product of the subsystem dimensions, i.e., dim J = dim S __ dim E , where dim represents
dimension of.


-----


2.1. Prelude: from classical to quantum measurements 26

description of composite quantum systems, but standard statistical correlations are re-

placed by entanglement. In the following subsection, Sec. 2.1.2, we explore the effect of

an interaction between the two coins.

######### 2.1.2 ######### Classical toy model of system-environment interaction

For a more general discussion of measurements, it is necessary to consider the interaction

of the system with another, which probes it and is often referred to as the _environment_ .

In this subsection, we consider the minimal limit of this model, where both the system

and environment are bits. Further, to introduce only the essentials for now, we consider

only the effect of a single interaction between the classical system and environment,

and discuss the effect of the interaction on the system transfer of information. In the

following subsection, Sec. 2.1.3, we consider the analogous quantum case, consisting of

the interaction between a system and environment, each of which is quantum bit. In

Sec. 2.2, we generalize the toy model to the time-continuous homodyne monitoring of a

quantum bit.

**Classical toy model.** Continuing with the example of two coins, we label one as the

system and the other as the environment. For definitiveness, consider the case where

the system coin belongs to Adam, who aims to employ it to communicate with Bob. To

achieve this, at time _t_ = 0 , Adam prepares his coin in the configuration _S_ (0) = _s_ _A_ ,

where _s_ _A_ is the bit value Adam hopes to communicate. He sends the coin flying to Bob,

who receives it at time _T_ , and measures it to obtain the value of _S_ ( _T_ ) . If the coin flies

undisturbed, _S_ ( _T_ ) = _S_ (0) , and Bob faithfully receives Adams bit.

However, during its flight, the coin unavoidably interacts with a second flying coin,

which belongs to an agent, Eve, who, at time _t_ = 0 , has prepared her coin in the

configuration _E_ (0) = _e_ , where _E_ is the variable describing her coin, and which is unknown


-----


2.1. Prelude: from classical to quantum measurements 27

![Mivev_Thesis.pdf-43-4.png](Mivev_Thesis.pdf-43-4.png)

![Mivev_Thesis.pdf-43-7.png](Mivev_Thesis.pdf-43-7.png)

![Mivev_Thesis.pdf-43-3.png](Mivev_Thesis.pdf-43-3.png)

![Mivev_Thesis.pdf-43-6.png](Mivev_Thesis.pdf-43-6.png)

![Mivev_Thesis.pdf-43-2.png](Mivev_Thesis.pdf-43-2.png)

![Mivev_Thesis.pdf-43-5.png](Mivev_Thesis.pdf-43-5.png)

_e_ _e_

**Environment** **System**


Eve


Adam


Bob

_S_ ( _T_ )

![Mivev_Thesis.pdf-43-1.png](Mivev_Thesis.pdf-43-1.png)

measure


![Mivev_Thesis.pdf-43-0.png](Mivev_Thesis.pdf-43-0.png)

**Figure 2.2** _|_ **Classical toy model of the interaction between the system and**
**environment.** Circuit of the interaction between the system, with agents Adam and Bob,
and the environment, with agent Eve. Vertical lines depict the bits of the system and
environment, initially prepared by Adam and Eve in the states _S_ (0) = _s_ _A_ and _E_ ( _T_ ) = _e_ ,
respectively. The two bits interact via a controlled-NOT (cNOT) gate. Bob measures the
system at time _T_ , obtaining the value _S_ ( _T_ ) . Brick wall depicts the lack of communication
between the agents of the system and environment.


-----


2.1. Prelude: from classical to quantum measurements 28

to Adam and Bob. For concreteness, suppose the interaction between the two coins is

described by the controlled-NOT (cNOT) gate,


cNOT __ _I_ __


(2.8)


+ __ _x_
__




=




where I and __ _x_ are defined according to Eq. (2.3). Matrices associated with operations

on the system (resp: environment) are placed to the left (resp: right) of the tensor

product. Given that Adam and Bob lack knowledge of Eves bit value, _e_ , but are aware

of the interaction, to what degree can they communicate, i.e., what is the effect of the

interaction on the value, _S_ ( _T_ ) , measured by Bob? More importantly, what action can Bob

undertake to undo the effect of the interaction, so as to obtain Adams bit, _S_ ( _T_ ) = _S_ (0) ?

**Evolution of the state, and Bobs information gain.** Employing the formalism

developed in Section 2.1.1, the initial state of the composite system, consisting of the two



__ __ __
coins, is described by the state vector _J_ (0) = _S_ (0) __ _E_ (0) _,_ where the initial states of


1+ _s_


1+ _p_ _E_



__
the system and environment are _S_ (0) =



__
and _E_ (0) =




_,_ respectively.




1 _s_ _A_
__


1 _p_ _E_
__


The variable _p_ _E_ denotes the bias of Eves coin, see Eq. (2.2). Following the interaction,



__ __
the composite system state is given by _J_ ( _T_ ) = cNOT _J_ (0) . The expected mean value

of Bobs measurement of _S_ ( _T_ ) , represented by the matrix _I_ __ __ _z_ , is given by, recalling

Eq. (2.5),



__
E [ _S_ ( _T_ )] = ( _I_ __ _z_ ) _J_ = _p_ _E_ _s_ _A_ _._ (2.9)
__ L1
 

To understand Eq. (2.9), consider three limiting cases: i) Eve always prepares her coin  

facing up, _e_ = 1 , corresponding to a maximal coin bias, _p_ _E_ = 1 . Since for _e_ = 1 the


-----


2.1. Prelude: from classical to quantum measurements 29

interaction with her coin has no effect on Adams coin, Bob faithfully receives Adams bit

every time, E [ _S_ ( _T_ )] = _s_ _A_ . ii) Eve always prepares her coin facing down, _e_ = __ 1 . Since

her coin bias is now _p_ _E_ = __ 1 , Bob always receives Adams coin flipped E [ _S_ ( _T_ )] = __ _s_ _A_ .

While inconvenient for Bob, by flipping each coin he receives (a deterministic action), he

could recover the bit. The effect of Eves coin is to change the encoding of the information,

but has not resulted in its loss. iii) Eve prepares her coin completely randomly, _p_ _E_ = 0 .

On average, Bob receives no information from Adam, E [ _S_ ( _T_ )] = 0 ! Eve has randomly

scrambled the encoding of the information for each of the realizations, which, from Bobs

point of view, results in the complete loss of the initial system information encoded by

Adam. More generally, for an arbitrary coin bias _p_ _E_ , the information shared between Adam

and Bob is characterized by the correlation between the initial and final configurations

of the system, which is given by the bias of Eves bit, E [ _S_ ( _T_ ) _S_ (0)] = _p_ _E_ , which can

be understood as the result of information transfer between the system and environment,

facilitated by the cNOT interaction, however, where the information propagating to the

system from the environment is random noise.

While the transfer of information between Adam and Bob is degraded by the influence

of the interaction with Eves bit, in principle no information has been erased, because

the cNOT interaction is reversible. For the case where _p_ _E_ = 0 , Adams bit, _s_ _A_ , is not

transferred to Bob at all; rather, it is encoded in the correlation between the system



__
and environment, E [ _S_ ( _T_ ) _E_ ( _T_ )] = ( __ _z_ __ _z_ ) _J_ = _s_ _A_ , which is inaccessible to Adam
L1
__

and Bob, who only have control over the system coin, and, hence, only access to   _S_ .

 

To summarize, the interaction between the system and a randomly prepared random

environment results in loss of information and injection of noise into the system, as far

as the system alone is concerned. Nevertheless, from the vantage point of the composite

system, no information is lost; rather, it is transferred into correlations between the system

and environment.


-----


2.1. Prelude: from classical to quantum measurements 30

**Recovering the information.** To recover Adams bit, Bob requires access to Eves

physical coin or knowledge of _e_ , the specific value of her coin for _each_ realization. First,

consider the latter case, where Bob learns _e_ . Recalling that cNOT 2 = _I_ __ _I_ , before Bob

performs a measurement, he can undo the interaction effect by preparing an ancillary,

third, coin with the value _e_ , by employing it to perform a second cNOT operation on his

coin, thus reversing the first. Applied to each realization, this procedure results in faithful

communication, E [ _S_ ( _T_ ) _S_ (0)] = 1 . Notably, Bob can also reverse the interaction effect

_after_ performing his measurement by essentially applying the second cNOT operation

virtually, i.e., when _e_ = 1 , _s_ _A_ = _s_ _B_ , while otherwise, _s_ _A_ = __ _s_ _B_ . We remark that any

operations performed by Eve on her coin after the system-environment interaction have

no consequences for Bob. To summarize, the examples highlights three distinct aspects

regarding the recovery of information in the classical setting:

1. Eves physical system was not required, only information about its initial configura-

tion, _E_ (0) = _e_ .

2. The effect of the interaction can be reversed _before_ or _after_ Bobs measurement.

3. Operations on Eves coin subsequent to the interaction have no consequences.

All three of these features break down in the quantum setting, as discussed in the following

subsection.

######### 2.1.3 ######### Quantum toy model

Rather than communicating with classical bits (coins), consider the situation where Adam

and Bob communicate with quantum bits (qubits), and Eve too employs a qubit. Before

proceeding, we briefly review the basic qubit concepts.


-----


2.1. Prelude: from classical to quantum measurements 31

**Quantum bit.** While the fundamental concept of classical information is the bit, which

represents the minimal classical system, the fundamental concept of quantum information

is the _quantum bit_ , or _qubit_ for short, which represents the minimal physical quantum


system. A qubit has two basis states, _|_ + _z_ __ and _|_ _z_ __ . A pure state of the qubit is described


by the state _|_ __ __ = cos __

in the range 0 __ __ 


+ _z_ + _e_ _i_ sin __

2

_|_ __

0 __ 2 __ 


_|_ + _z_ __ , where the angles __ and __ , which fall


in the range 0 __ __ __ __ and 0 __ __ __ 2 __ , define a point on the unit sphere, known as


the _Bloch sphere_ , see Fig. 2.1b. More generally, a statistical ensemble of pure states, a

_mixed_ qubit state is described by the density matrix



1
__ =



_I_ + _X_ __  _x_ + _Y_  __ _y_ + _Z_ __  _z_ _,_ (2.10)


where _X_ , _Y_ , _Z_ are real numbers parameterizing the state, given by the averages of the

Pauli operators, _X_ __ Tr [ __ _x_ __ ] , _et cetera_ , where Tr [ __ ] denotes the trace operation. The


matrix representation of the identity, _I_ , and Pauli  __ _x_ and  __ _z_ operators is given in Eqs. (2.3)


and (2.6), while that of Pauli operator Y is  __ _y_ =


__ _i_




The Bloch vector, ( _X, Y, Z_ ) , provides an important geometrical representation of the


, where _i_ is the unit imaginary.




state of the qubit, and as discussed in Sec. 2.1.1 is the analog of the coin bias _p_ . For a

pure state, the Bloch vector extends to the surface of the Bloch sphere, while for mixed

states, it lies in the interior. Notably, it admits the spherical parameterization:

_X_ = _r_ sin ( __ ) cos ( __ ) _,_

_Y_ = _r_ sin ( __ ) sin ( __ ) _,_

_Z_ = _r_ cos ( __ ) _,_ (2.11)


-----


2.1. Prelude: from classical to quantum measurements 32

where the angles __ and __ are defined as for pure states and _r_ is the length of the Bloch

vector, a number between 0 and 1. Notably, in the Bloch representation, mutually or-

thogonal state vectors are _not_ represented by orthogonal Bloch vectors, but rather, by

opposite Bloch vectors, which specify antipodal points on the sphere.

**Quantum toy model.** Returning to the toy model example of the interaction between

two systems (recall Fig. 2.2, which depicts the analogous classical model), we consider

the case where at time _t_ = 0 Adam prepares his qubit in the pure state _|_ __ (0) __ , with

corresponding Bloch vector components _X_ (0) , _Y_ (0) , and _Z_ (0) , while Eve prepares her


qubit in the pure state _|_ + _x_ __ , where _|_ + _x_ __ =



( + _z_ + + _z_ ) . Unlike in the classical toy
2

_|_ __ _|_ __


model, Adam has a choice regarding the encoding of his information  the orientation

of the Bloch vector, which has no classical analog. Both qubits are sent flying. A


controlled-NOT interaction occurs, described by the operator cNOT = _I_ _|_ + _z_ __ + _z_ _|_ +

__  _x_ _|_ _z_ __ _z_ _|_ , where operators on the left (resp., right) of the tensor product, denoted

__ , act on the system (resp., environment). Notably, the matrix representation of the

cNOT operator is the same that of the classical cNOT gate, given in Eq. (2.8). After the

interaction Bob receives the system qubit, at time _T_ .

**Effect of the interaction before the measurement.** Before the measurement, the

pure state of the composite system, _|_  ( _T_ ) __ = cNOT ( _|_ __ (0) _|_ + _x_ __ ) , is, in general, in-

separable  it cannot be written as a simple product of states of its component systems.

On a mathematical level, this result is the same as that for the classical model; however,

the interpretation and consequences are markedly distinct. Classically, the inseparability

represented statistical correlations between _definite_ configurations of the system and en-

vironment. For the quantum model, the inseparability represents entanglement between

the system and environment  the system cannot be fully described without considering

the environment. Generally, measurements of the entangled system are correlated with


-----


2.1. Prelude: from classical to quantum measurements 33

those of the environment, and the system alone cannot be represented by a pure state.

The consequences of the system-environment entanglement are at the heart of quantum

measurement theory.

Consider the reduced density matrix of the system qubit, found by taking the partial

trace over the environment, denoted Tr _E_ [ __ ] ,


_X_ (0)

_._ (2.12)

1






1
__ _S_ ( _T_ ) = Tr _E_ [  ( _T_ )  ( _T_ ) ] =
_|_ __ _|_ 2


_X_ (0)


Evidently, entanglement in the composite state, the result of the interaction between

the system and environment results in the loss of information from the point of view of

the system. Specifically, the _Y_ and _Z_ Bloch components prepared by Adam, _Y_ (0) and

_Z_ (0) , are absent in __ _S_ ( _T_ ) , despite the deterministic preparation of the ancilla in a _pure_

state _|_ + _x_ __ . However, if Adam chose to encode his information along the X component

of the Bloch vector, it would propagate to Bob undisturbed by the interaction with the

environment, and Bob could receive it by measuring _X_ . It is the _X_ component that is

preserved due to the choice of the interaction and initial pure state of the environment.

Analogously to the classical case, no information is truly lost, but rather, when viewed in

the broader context of the composite system, Adams initial _Y_ and _Z_ qubit components are

encoded in the YZ, __ _Y Z_ __ Tr [( __ _y_ __ __  _z_ ) __ ] = _Y_ (0) , and ZZ, __ _ZZ_ __ Tr [( __ _z_ __ __  _z_ ) __ ] =

_Z_ (0) , correlations between the system and environment, respectively.

**Recovering information before the measurement.** In the classical case, by learning

the initial configuration of the environment, _E_ (0) = _e_ , Bob could undo the effect of

the system-environment interaction and could recover the state sent by Adam before

performing the measurement. In the quantum case, this is not possible. Even though

Bob can know the initial state, _|_ + _x_ __ , of the environment and can clone it, by preparing a


-----


2.1. Prelude: from classical to quantum measurements 34


third ancilla qubit in the state _|_ + _x_ __ , he cannot use this ancilla to perform a second cNOT

2 
operation on the system so as to reverse (recall that cNOT = _I_ ) the cNOT performed

by the environment qubit. This is a profound consequence of the entanglement between

the system and environment, and has no classical analog. The only way to reverse the

interaction is to use the physical qubit of the environment to perform the second cNOT

operation  _no_ clone will suffice.

**Projective (von Neumann) measurement.** For a classical system described by a

state of maximal knowledge, the result of any measurement can be determined with

certainty. However, for a quantum system described by a state of maximal knowledge, a

pure state, the result of a measurement is _not_ , in general, determined. For definitiveness,

consider the description of a perfect projective (von Neumann) measurement performed

by Bob on the _Z_ component of his qubit spin, with the associated operator ( _observable_ )

__  _z_ . The measurement is described by the spectral decomposition of the observable,


__  _z_ =




_r_ _r_ __  _r_ =  __ 1 __ __  __ 1 , where _r_ is an eigenvalue, _r_ = 1 or _r_ = __ 1 , to which


corresponds a measurement result, and  __ _r_ is the projection operator onto the eigenstate


associated with _r_ ,  __ 1 = + _z_ + _z_ and  __ 1 = + _z_ + _z_ . The probability of obtaining an
_|_ __ _|_ __ _|_ __ _|_

outcome corresponding to the eigenvalue _r_ is

__ _r_ = Tr [ __ _r_ __ ] _._ (2.13)

According to the projection postulate of quantum mechanics, 11 the measurement leads to

the projection (or collapse) 12 of the system state into an eigenstate of the measurement

operator. Immediately after the measurement, conditioned on the result _r_ , the state of

11 Curiously, the modern formulation of the projection postulate is not precisely that of von Neumann
(von Neumann, 1932), but contains a correction due to Lders (Lders, 1951).
12 W. Heisenberg introduced the idea of wavefunction collapse in 1927 (Heisenberg, 1927).


-----


2.1. Prelude: from classical to quantum measurements 35

the system is


__  _r_ __ __  _r_
__ _r_ = _._ (2.14)

__ _r_

The evolution due to Eq. (2.14) is markedly non-linear in the state density, which appears in

the denominator, and represents a radical departure from the linear evolution encountered

with Schrdingers equation. Further, while a perfect measurement of a classical system

does _not_ alter its state, a perfect measurement of a quantum system, in general, _does_

alter its state. This non-linear disturbance has profound consequences.

Suppose, at time _T_ , Bob performs a _Z_ measurement of his qubit and obtains the


result _r_ = 1 , with probability, recalling Eqs. (2.12) and (2.13), __ 1 = Tr [ __ 1 __ _S_ ( _T_ )] = 1 2 .

Note that __ 1 is independent of _X_ (0) , _Y_ (0) , and _Z_ (0) . The system state after the


measurement is __ 1 =  __ 1 __ _S_ ( _T_ )  __ 1 _/_ Tr [ __ _S_ ( _T_ )  __ 1 ] =


state _|_ + _z_ __ . Notably, the potentially recoverable information encoded by Adam, _X_ (0) ,


, corresponding to the pure

 _X_ (0) ,


is irreversibly lost. From the point of view of the composite system, described by the

state _|_  ( _T_ ) __ , the measurement has projected the state onto the measurement basis,


according to the effect of the projector  __ 1 __ _I_ . The state of the composite system

after the measurement, _|_ + _z_ _|_ __ (0) __ , is pure and separable, i.e., the measurement has

disentangled the system and environment. In this toy model (and for this particular

measurement outcome), it just so happens that Adams state is completely teleported

to Eves qubit, a form of information transfer between the two systems. To understand

the situation a bit better, consider the alternative, where _r_ = __ 1 , with the associated


projector  __ 1 _I_ . The conditional state of the system after the measurement is again
__
__

obtained by employing Eq. (2.14), yielding _|_ + _z_ _|_ __ __ __ for the composite system, where

the state _|_ __ __ __ has the same Bloch vector as Adams initial state _|_ __ (0) __ but with the

_Y_ and _Z_ components flipped. This example illustrates the more general feature that a


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 36

measurement on either the system or environment disentangles the two, resulting in a

perfect correlation between the measurement on one and the state of the other. Further,

it tends to lead to a transfer of information between the two subsystems. We explore the

profound consequences of these features in the following section.

###### 2.2 ###### Continuous quantum measurements: introduc-

 tion to quantum trajectories and stochastic cal-

 culus

In this section, we consider a heuristic microscopic model of continuous quantum mea-

surements, which, although simple, contains sufficient generality to introduce the principal

ideas. Specifically, we model the homodyne measurement of a qubit by a sequence of in-

teractions with a chain of identically prepared ancilla qubits. A chain of ancillary systems

modeling the environment is known as a von Neumann chain (von Neumann, 1932).

While the evolution due to the interaction with each ancilla is unitary, deterministic,

the addition of a projective (von Neumann) measurement of each ancilla subsequent to

its interaction with the system results in the stochastic evolution of the quantum state

of the system  known as a _quantum trajectory_ (Carmichael, 1993). Due to the cor-

relation between the state of a measured ancilla and the resulting state of the system,

the measurement results allow faithful tracking of the state trajectory (Belavkin, 1987,

Carmichael, 1993, Gardiner _et al._ , 1992, Dalibard _et al._ , 1992, Korotkov, 1999). After

introducing the time-discrete version of the model, we take its continuum limit, which

allows us to introduce the fundamental concepts of stochastic calculus. Specifically, we

focus on introducing the Wiener noise process and obtaining the stochastic differential

equations (SDEs) that describe the homodyne monitoring of the qubit. Most of the results


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 37

**Environment**

|Z Measurement record|Col2|Col3|
|---|---|---|
||(t) S J(t)  t X t 0  r -1 1 1 -1 1 -1 -1 -1 ... n H n Y|||
||||


![Mivev_Thesis.pdf-53-0.png](Mivev_Thesis.pdf-53-0.png)

![Mivev_Thesis.pdf-53-8.png](Mivev_Thesis.pdf-53-8.png)

![Mivev_Thesis.pdf-53-10.png](Mivev_Thesis.pdf-53-10.png)

![Mivev_Thesis.pdf-53-12.png](Mivev_Thesis.pdf-53-12.png)

![Mivev_Thesis.pdf-53-14.png](Mivev_Thesis.pdf-53-14.png)

![Mivev_Thesis.pdf-53-7.png](Mivev_Thesis.pdf-53-7.png)

![Mivev_Thesis.pdf-53-9.png](Mivev_Thesis.pdf-53-9.png)

![Mivev_Thesis.pdf-53-11.png](Mivev_Thesis.pdf-53-11.png)

![Mivev_Thesis.pdf-53-13.png](Mivev_Thesis.pdf-53-13.png)

![Mivev_Thesis.pdf-53-2.png](Mivev_Thesis.pdf-53-2.png)

![Mivev_Thesis.pdf-53-4.png](Mivev_Thesis.pdf-53-4.png)

![Mivev_Thesis.pdf-53-3.png](Mivev_Thesis.pdf-53-3.png)

![Mivev_Thesis.pdf-53-5.png](Mivev_Thesis.pdf-53-5.png)

![Mivev_Thesis.pdf-53-6.png](Mivev_Thesis.pdf-53-6.png)

![Mivev_Thesis.pdf-53-1.png](Mivev_Thesis.pdf-53-1.png)

ancillas


measurement


**Figure 2.3** _|_ **Homodyne monitoring of a quantum bit: time-discrete model.**
The qubit, whose Bloch vector lies in the XZ plane, sequentially interacts with a chain
of ancilla qubits, which model the environment. At the beginning of each timestep, at
time _t_ , the system is in a pure state, __ ( _t_ ) _S_ . During the _n_ -th timestep, of length
_|_ __


 _t_ , the qubit interacts, subject to the Hamiltonian _H_ _n_ , with the _n_ -th ancilla, prepared
in _|_ + _x_ __ , whereafter, the Y component of its spin is projectively measured. The result
of the measurement, _r_ _n_ , which is either -1 or 1, is recorded and accumulated; in the
continuum limit,  _t_ __ 0 , it leads to the homodyne signal _J_ ( _t_ ) , a time-continuous
stochastic (Weiner) process.

derived in this section carry over with little modification to the following section, Sec. 2.3,

which establishes the general formulation of quantum measurement theory. Time-discrete

chain models have been discussed in Refs. Caves and Milburn (1987), Attal and Pautrat

(2006), Tilloy _et al._ (2015), Korotkov (2016), Bardet (2017).

######### 2.2.1 ######### Time-discrete model with flying spins

Time is discretized in small but finite bins of length  _t_ labeled by the integer _n_ , i.e., _t_ =

_n_  _t_ . During each timestep, a single spin of the environment, referred to as the _ancilla_ ,

interacts with the system for time  _t_ , see Fig. 2.3. For simplicity, assume each spin is

identically prepared in the state _|_ + _x_ __ . We employ the convention that the states _|_ _x_ __ ,

_|_ _y_ __ , and _|_ _z_ __ denote eigenstates of the Pauli X, Y, and Z operators, respectively. The


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 38

interaction between the _n_ -th ancilla and the system is described by the Hamiltonian


  __ _S_ ( _n_ )
_H_ _n_ __  _z_ __  _z_ _,_ (2.15)
__ 2 __

where __ is the strength of the interaction,  is Planks constant, and  __ _z_ _S_ and  __ _z_ ( _n_ ) denote

the Pauli Z operators of the system and ancilla, respectively. For the time being, we


assume that _H_ _n_ is the only generator of system evolution, and the system Hamiltonian


is zero, _H_ _S_ = 0 . Following the interaction, the ancilla is measured by a detector that

performs a projective measurement of the ancilla spin Y component, which yields the

measurement result _r_ _n_ = __ 1 or _r_ _n_ = 1 . The observer operating the measurement

apparatus keeps track of the sum total of the measurement results, the measurement


 _t_ _n_ _n_ __ =0 _r_ _n_ __ .




signal: _J_ _t_ __


Note two assumptions regarding the measurement: i) the ancilla qubits are undisturbed


during their flight from the system to the measurement apparatus, and ii) the measurement

apparatus performs a perfect measurement, and does not add technical noise. These

assumptions ensure no information is lost in the measurement, nor spurious noise is added

by it; i.e., the observer has perfect access to all information there is to know in the

environment, and is hence referred to as an _omniscient observer_ .

**Evolution of the composite system.** For simplicity, assume the state of the

system at time _t_ is pure and its Bloch vector lies in the XZ plane; i.e., it is described by

a single angle __ ( _t_ ) ,


__ ( _t_ )
__ ( _t_ ) _S_ = cos
_|_ __ 2



__ ( _t_ )
+ _z_ _S_ + sin
_|_ __ 2



cos __ ( _t_ )

2

sin __ ( _t_ )


_._ (2.16)




_|_ _z_ __ _S_ =


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 39

The state of the composite system at time _t_ , consisting of the _n_ -th ancilla and the system

qubit, is  ( _t_ ) = __ ( _t_ ) _S_ + _x_ _n_ , and for duration  _t_ evolves subject to the Hamiltonian
_|_ __ _|_ __ _|_ __

  
_H_ _n_ . The total evolution is given by the propagator _U_ ( _t, t_ +  _t_ ) = exp __ _i_ _H_ _n_  _t/_  ,
 

and the composite-system state after the interaction is


_|_  ( _t_ +  _t_ ) __ = _U_ ( _t, t_ +  _t_ ) _|_  ( _t_ ) __ _,_ (2.17)

Anticipating the ancilla Y measurement, we express _|_  ( _t_ +  _t_ ) __ in terms of the measure-

ment operator eigenstates. The measurement operator on the ancilla alone is the Pauli Y

( _n_ )
operator,  __ _y_ , with eigenstates _y_ _n_ and + _y_ _n_ , in terms of which,

_|_ __ _|_ __




 ( _t_ + d _t_ ) = __ 1 ( _t_ +  _t_ )
_|_ __ __







_y_ _n_ + __ +1 ( _t_ +  _t_ )
_S_ _|_ __





+ _y_ _n_ _,_ (2.18)
_S_ _|_ __


where the parameter __ __ __  _t_ characterizes the measurement strength and the un-



13 
normalized system states __ 1 ( _t_ +  _t_ )
__






are
_S_


cos __ ( _t_ )

2

sin __ ( _t_ )


cos _/_ 2 __ __

2

sin _/_ 2 __ __




__ 1 ( _t_ +  _t_ )
__




(2.19)


_S_ __


The state of the composite system following the interaction, Eq. (2.18), is not separable.

The interaction has entangled the system and environment, as discussed of Sec. 2.1.3.

**Projective (von Neumann) measurement of the ancilla.** The action of the mea-

surement apparatus on the composite system is described, recalling the discussion on

 
Pg. 34, by decomposing the measurement operator _Y_ _n_ = _I_ __ __  _y_ in terms of its eigenstate

 
projectors,  __ __ __ _I_ _S_ __ ( _|_ _y_ __ _y_ _|_ ) _n_ ; note, _Y_ =  __ + __ __  __ . According to the von Neumann

postulate, the projectors yield the probability for obtaining the results _r_ _n_ = __ 1 and _r_ _n_ = 1

13 By convention, a tilde will indicate an unnormalized state, with a norm less than one.


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 40

from the measurement,

__ _r_ ( _t_ ) = __  ( _t_ +  _t_ ) _|_  __ _r_ _|_  ( _t_ +  _t_ ) __


= 1


2 (1 __ _r_ _n_ sin ( __ ) cos ( __ ( _t_ ))) _,_ (2.20)


 
__ _r_ ( _t_ +  _t_ ) __ _r_ ( _t_ +  _t_ )

(1 _r_ _n_ sin (   __ ) cos ( __ ( _t_


as well as the state of the composite system immediately after the measurement, condi-

tioned on the result _r_ _n_ ,




_|_  _r_ ( _t_ +  _t_ ) __ = __ _r_ ( _t_ +  _t_ )




__ _r_ ( _t_ ) _,_ (2.21)



_y_ := _r_ _n_ _/_
_S_ _|_ __


where _|_ _y_ := _r_ __ _n_ denotes ancilla state _|_ + _y_ __ _n_ (resp., _|_ _y_ __ _n_ ) for _r_ = 1 (resp., _r_ = __ 1 ). The


measurement has transformed the entanglement between the system and environment,

evident in the non-separable state _|_  ( _t_ +  _t_ ) __ , Eq. (2.18), into a correlation between

the pure state of the system and environment after the measurement, evident in the

separable, non-entangled conditional state _|_  _r_ ( _t_ +  _t_ ) __ , Eq. (2.21). Assuming the ancilla

never interacts with the system again, it is unnecessary to retain it in the description of

the measurement; removing it from Eq. (2.21), we obtain the pure state of the system

alone at time _t_ +  _t_ :


cos __ _r_ ( _t_ +d _t_ )

2

sin __ _r_ ( _t_ +d _t_ )




__ _r_ ( _t_ +  _t_ )




_._ (2.22)




_|_ __ _r_ ( _t_ +  _t_ ) __ _S_ =


__ _r_ ( _t_ )



=
_S_


From the point of view of the observer, the entanglement is transformed by the mea-

surement into a classical correlation between the result _r_ _n_ and the final conditional state

of the system, __ _r_ ( _t_ +  _t_ ) _S_ . Figure 2.4 summarizes the steps of the model and the
_|_ __

conditional state update.


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 41

w/ omniscient observer


![Mivev_Thesis.pdf-57-0.png](Mivev_Thesis.pdf-57-0.png)

![Mivev_Thesis.pdf-57-1.png](Mivev_Thesis.pdf-57-1.png)

+ 


+  _t_ )

||Col2|Col3|
|---|---|---|
|n|H |S  z|
||||
|Y|||
||||


__ ( _t_ +  _t_ )

**Figure 2.4** _|_ **Circuit representation of the** _n_
**-th timestep of the quantum trajectory.** At time _t_ = _n_  _t_ , the system, described by the state __ ( _t_ ) _S_ , is subjected to

![Mivev_Thesis.pdf-57-2.png](Mivev_Thesis.pdf-57-2.png)
_|_ __


the system Hamiltonian _H_ _S_ and the interaction with the _n_ -th ancilla, characterized by
the parameter __ . Every ancilla is prepared in _|_ + _x_ __ . Following the interaction, the detector
projectively measures the Y component of the ancilla spin, yielding the result _r_ _n_ , which
provides the information necessary to update the state of the system. In the case of
the omniscient observer, characterized by unit quantum measurement efficiency, __ = 1 ,
at the end of the timestep, immediately after _t_ +  , the system state, __ _r_ ( _t_ +  _t_ ) _S_ ,
_|_ __
conditioned on the measurement result is pure. Contrast with Fig. 2.2.


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 42

**Solution for the conditional state update.** To explicitly solve Eq. (2.22) for the

updated angle of the qubit system conditioned on the measurement result _r_ _n_ , __ _r_ ( _t_ +  _t_ ) ,

one can use Eqs. (2.20) and (2.19), following trigonometric manipulation, to obtain,

without any approximations, an explicit relation (Devoret, M.H.) between the Bloch angle

at the start and end of the timestep:





(2.23)


![Mivev_Thesis.pdf-58-0.png](Mivev_Thesis.pdf-58-0.png)

In the following section, Sec. 2.2.2, this seemingly non-linear equation is transformed

into a linear equation by a hyperbolic transformation of the circular angle __ , and is solved

exactly. Nonetheless, for the continuum-limit discussion in Sec. 2.2.3, consider the solution

of Eq. (2.23) in the limit of weak interactions, __ __ 1 , to order __ :

d __ ( _t_ ) __ __ ( _t_ +  _t_ ) __ __ ( _t_ ) __ _r_ _n_ _X_ ( _t_ ) _,_ (2.24)

where we have defined the Bloch angle increment, d __ ( _t_ ) , and _X_ ( _t_ ) is the X component

of the Bloch vector, _X_ ( _t_ ) = sin ( __ ( _t_ )) .

**Interpretation and remarks.** The system measurement dynamics are described in

entirety by Eqs. (2.20), (2.22), and (2.24). To make the discussion more concrete, consider

the particular case where the system and ancilla do not interact, __ = 0 . The measurement

results are completely random, __ _r_ = 1 2 , uncorrelated with the system; similarly, the

system state is independent of the measurement results, _r_ _n_ ; in fact, there is no state

evolution, d __ ( _t_ ) = 0 . Consider the more interesting case of weak interactions, __ __ 1 .

Measurement results are correlated with the Z component of the system Bloch vector,


__ _r_ = 2 1 (1 _r_ _n_ _Z_ ( _t_ )) , where _Z_ ( _t_ ) = cos ( __ ( _t_ )) . Nonetheless, due to __ 1 , the two

__ __

measurement results still occur with nearly equal probability, and the record consists of


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 43

random noise, but with a slight bias that correlates it with _Z_ . Thus, the value of _Z_ can be

obtained from the instantaneous average of the measurement results, E [ _r_ _n_ ] = __ _Z_ . In

time, from the point of view of the observer, a long sequence of measurements gradually

results in the complete measurement of _Z_ , obtained from the noisy measurement record.


A peculiar feature of the weak interaction regime, __ __ 1 , is that amplitude of the noise is

essentially constant for all measurement strengths, its variance is Var [ _r_ _n_ ] = 1 __ ( _Z_ ) 2 __ 1 .

This origin of the randomness can be interpreted to be quantum in nature, since the system

and environment are in pure states at all times. Specifically, it is due to the incompatibility

(orthogonality) between the initial state of the ancilla, + _x_ _n_ , and the eigenstates, _y_ _n_ ,
_|_ __ _|_ __

of the measurement observable.

The random measurement result, _r_ _n_ , is correlated with a small kick on the state of

the system, described by Eq. (2.24). Conditioned on the result _r_ _n_ = 1 (resp., _r_ _n_ = __ 1 )

the system experiences a downward (resp., upward) kick corresponding to the circular


increment d __ ( _t_ ) = _r_ _n_ sgn ( _X_ ( _t_ ))


1 __ _Z_ ( _t_ ) , whose magnitude is largest for _Z_ = 0 , but


vanishing in the limit where _Z_ approaches __ 1 ; the sign function is denoted sgn . This

state-dependent nature of the back-action kicks leads to the eventual projection of the

state onto one of the eigenstate of the system observable,  __ _z_ , as discussed in Sec. 2.2.2.

The form of the backaction depends on the ancilla quantity being measured by the ap-

paratus; for example, a measurement of a quadrature other than the ancilla _Y_ quadrature

yields a different form of the measurement backaction. More generally, we emphasize that

no matter what ancilla quantity is measured, so long as the measurement is projective and

complete knowledge about the ancilla is obtained, the ancilla is collapsed onto a single

unique state. From this, it follows that the system cannot be entangled with the ancilla

and for this reason the system is left in a pure state.


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 44

**Generalized measurements.** By introducing an ancilla that interacts unitarily with the

system and is subsequently measured, we obtained evolution equations for the pure state

of the quantum system conditioned on the measurement result _r_ _n_ , and could otherwise

disregard the ancilla in the measurement description. The ancilla scheme realizes an

indirect measurement of the system, which gradually obtains information about the system

and disturbs it in a manner that is indescribable with the von Neumann formulation,

summarized by Eqs. (2.13) and (2.14). The example of this section belongs to a more

general class of measurements, referred to as _generalized measurements_ . A powerful

theorem by Neumark, see Sec. 9-6 of Ref. Peres (2002), proved that any generalized

measurement can be formulated essentially according to the scheme presented so far,

where an auxiliary quantum system is introduced, it interacts unitarily with the system,

and is subsequently projectively measured, in the traditional von Neumann sense. The

effect of the generalized measurement on the system can be completely described by


system operators, denoted _M_ _r_ , that are not in general Hermitian. For our example, the

14 
_measurement operator,_ _M_ _r_ _,_ follows directly from Eq. (2.21),




_y_ := _r_ _U_ ( _t, t_ +  _t_ ) + _x_
 
 


_M_ _r_ ( _t_ ) =


(2.25)


Note that _|_ + _x_ __ _n_ is the _initial_ ancilla state for the _n_ -th timestep, while _|_ _y_ := _r_ __ _n_ is the




_final_ ancilla state, follwing the projective measurement, while _U_ is the _composite_ system


propagator. Since _M_ _r_ in Eq. (2.25) is not Hermitian, it does not belong to the traditional


notion of an observable, and the outcomes _r_ _n_ are not the eigenvalues of _M_ _r_ , but serve

 
merely as labels. The measurement operators _M_ 1 and _M_ 1 , which are non-orthogonal
__



 
( _M_ 1 _M_ 1 = 0 ) link the system state with the set of measurement probabilities __ _r_ , and
__
__

 
formally, their operator set, _M_ _r_ __ _M_ _r_ : _r_ , constitutes a _positive-operator-valued measure_
 

14 The measurement operator is sometimes referred to as a Kraus operator.


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 45

(POVM) on the space of results, see Sec. 2.2.6 of Ref. Nielsen and Chuang (2010). In

general, the measurement operators generalize von Neumanns postulate in the following

way:

__ _r_ ( _t_ ) = Tr _M_  _r_ __ _M_  _r_ __ _,_ (2.26)
 

__ _r_ ( _t_ +  _t_ ) = _M_  _r_ __ ( _t_ ) _M_  _r_ __ _/_ _r_ ( _t_ ) _,_ (2.27)

where __ _r_ ( _t_ ) is the probability to obtain the measurement outcome _r_ and __ _r_ ( _t_ +  _t_ ) is the

state of the system immediately _after_ the measurement, conditioned on the result _r_ . Note

that technically, the generalized projection postulate does not introduce anything funda-

mentally new beyond von Neumanns postulate, since it follows from Neumarks theorem

that considering a larger quantum system with projective (von Neumann) measurements

and unitary operations is completely equivalent.

######### 2.2.2 ######### Geometric representation of a continuous measurement:

 random walk on a hyperbola

In this subsection, we present a geometric representation of the measurement dynamics.

Section 2.1.3 presented the geometric representation of the qubit state as a point on

the Bloch sphere, with coordinates _X_ , _Y_ , and _Z_ , or for a pure state, as a point on the

surface of the sphere, parameterized by the angles __ and __ , Eq. (2.11). For our qubit


example, _Y_ = 0 by assumption, hence its pure state, __ _S_ , can be represented on the
_|_ __

Bloch _circle_ , see Fig. 2.5a, parametrized by a single 15 circular angle __ : _X_ = sin ( __ ) and

_Z_ = cos ( __ ) . This geometric representation is particularly well suited to describing unitary

operations, which describe rotations in Hilbert space. For concreteness, consider the state

15 For simplicity, we have assumed that _X >_ 0 , which corresponds to the angle __ = 0 . Recall that
since 0 __ __ __ __ , the left half of the Bloch circle, _X <_ 0 , corresponds to angle __ = __ .


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 46



 1
evolution subject to the Rabi Hamiltonian _H_ _S_ = 2  __ __  _y_ , where, without assumptions on


the timestep,  _t_ , the effect of the propagator _U_ ( _t, t_ +  _t_ ) = exp __ _i_ _H_ _S_  _t/_  on the
 

state is given by the simple linear equation:

__ ( _t_ +  _t_ ) __ __ ( _t_ ) = __  _t ._ (2.28)

The complexity of Eq. (2.23) indicates that the circular representation is _not_ well suited

to describe the evolution due to the measurement. Rather, we show that a natural

representation for measurement dynamics is a hyperbolic one.

**Hyperbolic representation.** We map the Bloch circle onto the standard hyperbola

according to the equation _Z_ = cos ( __ ) = tanh __ , where __ is the hyperbolic angle, the

analogue of the circular angle __ , see Fig. 2.5a. In terms of the hyperbolic representation,

without any approximations, Eq. (2.23) is transformed into a simple linear equation,

analogous to that of Eq. (2.28),

__ _r_ ( _t_ +  _t_ ) __ __ ( _t_ ) = __ _r_ _n_ _ ,_ (2.29)

where __ _r_ ( _t_ +  _t_ ) is the hyperbolic angle of the system after the measurement, conditioned

on the result _r_ _n_ , __ ( _t_ ) is the hyperbolic angle before the interaction with the ancilla, and __ is

the hyperbolic increment, tanh ( __ ) = sin ( __ ) . In view of the Eq. (2.29), the measurement

backaction kicks are understood as hyperbolic rotations of a definite amplitude __ , but

random orientation _r_ _n_ . By iterating the calculation of Eq. (2.29) _N_ times, one can obtain

the stochastic path taken by the qubit state, its quantum trajectory, which, understood

in terms of the stochastic difference equation d __ _r_ ( _t_ ) __ __ _r_ ( _t_ +  _t_ ) __ __ ( _t_ ) = __ _r_ _n_ __ , is a

random walk on a hyperbola.

The circular and hyperbolic coordinate transformations together with Eqs. (2.28)


-----


![Mivev_Thesis.pdf-63-3.png](Mivev_Thesis.pdf-63-3.png)

![Mivev_Thesis.pdf-63-2.png](Mivev_Thesis.pdf-63-2.png)

![Mivev_Thesis.pdf-63-1.png](Mivev_Thesis.pdf-63-1.png)

hyperbola, with asymptotes defined by the lines _Z_ = __ _X_ . **b,** Histogram of quantum

![Mivev_Thesis.pdf-63-0.png](Mivev_Thesis.pdf-63-0.png)
trajectory densities obtained from simulations of the flying-spin model. All trajectories
(not shown here) begin with the initial state defined by the Bloch coordinates _X_ (0) = 1
and _Z_ (0) = 0 . The time axis is scaled in units of the measurement rate, __ .

and (2.29) can be employed to construct a finite-difference numerical scheme to cal-

culate the quantum trajectory of the qubit subject to homodyne monitoring. Notably,

since the difference equations were derived _without_ approximations, especially with regard

to the size of  _t_ , they guarantee a physical system state for all parameters and at all time,

features which offer some practical advantages for numerical simulations. In the following

subsection, Sec. 2.2.3, we construct the continuum limit of the model and formally derive

the differential equations for the quantum trajectory of the qubit.

######### 2.2.3 ######### Continuum limit: Wiener noise and stochastic calculus

In this section, we take the appropriate limit in which the measurement becomes continu-

ous. In this limit, the interaction time,  _t_ , becomes infinitely small while the measurement

strength, __ , becomes infinitely large. Since each short sequence of individual measure-


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 48

ments carries an infinitesimal amount of information in this limit, we coarse-grain the

measurement record in the following way. The evolution up to time _t_ is divided in _m_

intervals of total duration d _t_ , while each of these intervals is further subdivided in _l_ yet

smaller intervals, each of duration  _t_ ; i.e., _t_ = _n_  _t_ = _ml_  _t_ and d _t_ = _l_  _t_ . The inter-


action amplitude, __ , is chosen to be __ =

Subject to appropriate scaling, by a factor

to time _t_ is the measurement signal _J_ _t_ =


_/_  _t_ , where __ denotes the interaction rate.

 _t_ , the sum of all measurement results up


d _t_ , beginning at _t_ = _ml_  _t_ and ending at _t_ __ = ( _m_ + 1) _l_  _t_ , the signal changes by


 _t_ _m_ _m_ __ =0 _l_ _l_ __ =0 _r_ _m_ __ _l_ __ . During a time interval

= (  _m_ + 1)  _l_  _t_ , the signal changes by


d _J_ _t_ = _J_ ( _m_ +1) _l_  _t_ __ _J_ _ml_  _t_ =


( _m_ +1) _l_

_r_ _k_ _._ (2.30)
_k_ = _ml_




 _t_


Equation (2.30) is known as a _stochastic difference equation,_ because the difference in-

crement in the variable _J_ _t_ is a random variable. Assuming the state of the system does

not appreciably change over the time interval d _t_ , the measurement results, _r_ _k_ , are inde-

pendent and identically distributed binary random variables described by the probability


function __ [ _r_ _k_ ] = 1 2 (1 _r_ _k_ _Z_ ( _t_ )) _,_ recall Eq. (2.20), where __ =

__


__  _t_ . It follows that


the mean and variance of the measurement increment are


E [d _J_ _t_ ] = _l_


 _t_ E [ _r_ _k_ ] = __ __ _Z_ ( _t_ ) d _t ,_ (2.31)


Var [d _J_ _t_ ] = _l_  _t_ Var [ _r_ _k_ ] __ d _t ,_ (2.32)

respectively, while, according to the central limit theorem, all higher-order cumulants of

the probability distribution for d _J_ _t_ vanish in the limit of large _l_ . Working in this limit, and

employing Eqs. (2.31) and (2.32), the stochastic difference equation, Eq. (2.30), can be

taken to the continuum limit, 16

16 For completeness, we note that Eq. (2.33) is a special case of Eq. (2.58).


-----


2.2. Continuous quantum measurements: introduction to quantum trajectories and
stochastic calculus 49

d _J_ ( _t_ ) = __ __ _Z_ ( _t_ ) d _t_ + d _W_ ( _t_ ) _,_ (2.33)

where the infinitesimal term d _W_ ( _t_ ) represents Gaussian white noise, and is known as the

_Wiener increment_ . It obeys the following canonical relations and probability density:

E [d _W_ ( _t_ )] = 0 _,_ d _W_ ( _t_ ) d _t_ = 0 _,_ (2.34)


E d _W_ ( _t_ ) 2 = d _t ,_ __ (d _W_ ) = exp ( __ __ d 2 _W_ __ 2 d _/_ _t_ (2d _t_ )) _._ (2.35)
 

**Stochastic calculus.** Equation (2.33) is known as a _stochastic differential equation_

(SDE) because the infinitesimal differential is not completely determined, but is a random

variable. Notably, in obtaining this equation, we took the value of the function _Z_ ( _t_ ) at

the _beginning_ of the timestep d _t_ . In general, because the stochastic noise is not smooth

and not differentiable if we had taken the value of the function at the _end_ of the time-

interval d _t_ we would have obtained a different form of the SDE. By taking the value of the

function at the beginning of the timestep, the SDE we obtained is said to be in _It form_ ;

otherwise, it would have been in _Stratonovich form_ . The two forms are not equivalent

in a straightforward manner, but for our purposes, it will suffice to only consider the It

form; see Chapter 3 of Ref. Jacobs (2010) for an in-depth discussion. From Eqs. (2.34)

and (2.35) it follows that the SDE solution only depends on terms proportional to d _t,_ d _W,_

and d _W_ 2 _,_ while all other terms of the form d _t_ _p_ d _W_ _q_ are vanishing. Importantly, in an

unusual departure from the rules of differential calculus, in the continuum limit, one can

set d _W_ 2 = d _t_ , a result known as _It_ s _rule_ . We note that d _W_ ( _t_ ) is an idealized Gaussian

noise process in that it has a perfect delta function correlation in time, which implies its

Markovianity, but also that it has a white noise power spectral density, non-zero for _all_

frequencies.


-----


2.3. Quantum trajectory theory 50


**It SDE for the Bloch vector.** In our example, the Bloch vector of the qubit can



17 __
be parameterized by its Z component, _S_ ( _t_ ) =




1 __ _Z_ ( _t_ ) 2 _,_ 0 _, Z_ ( _t_ ) . Thus, it



suffices to derive an SDE for _Z_ ( _t_ ) , which is obtained from the system state, _|_ __ _J_ ( _t_ ) __ ,


conditioned on the measurement signal _J_ ( _t_ ) by taking the expectation value of  __ _z_ , _Z_ ( _t_ ) =

__ __ _J_ ( _t_ ) _|_ __  _z_ _|_ __ _J_ ( _t_ ) __ . The SDE is derived by first Taylor expanding _Z_ ( _t_ ) = cos ( __ ( _t_ )) to


first order in d _t_ , d _Z_ ( _t_ ) __


1 _Z_ ( _t_ ) 2 d __ ( _t_ ) 1 2 _Z_ ( _t_ ) d __ ( _t_ ) 2 , where we have retained
__ __


terms to second order in d __ ( _t_ ) . This is necessary because d __ ( _t_ ) , recalling Eq. (2.24), is

proportional to d _W_ , and d _W_ 2 = d _t_ . By summing _l_ times over the difference equation

and performing the same coarse graining employed to arrive at Eq. (2.33), we arrive at

the It form of the SDE for the Z component of the Bloch vector of a qubit subject to

heterodyne monitoring of  __ _z_ ,

![Mivev_Thesis.pdf-66-0.png](Mivev_Thesis.pdf-66-0.png)

Equation (2.36) is a non-linear diffusion equation with a state-dependent diffusion coef-

ficient, _D_ ( _Z_ ) = __ (1 __ _Z_ 2 ) 2 , which is maximized for _Z_ ( _t_ ) = 0 , but approaches zero for

_Z_ = __ 1 . Mathematically, it is for this reason, that in the limit _t_ __ , the system tends

to one of the pointer states ( _Z_ = __ 1 ) of the measurement, where diffusion vanishes, and

states cluster.

###### 2.3 ###### Quantum trajectory theory

The preceding sections introduced the general background required to develop quantum

trajectory theory. With the aid of specific examples, important overriding themes were

highlighted, which will carry us forward in this section, and play a key role in understanding

17 For simplicity, we have assumed _X_ ( _t_ ) _>_ 0 for all _t_ .


-----


2.3. Quantum trajectory theory 51

photon-counting, homodyne, and heterodyne measurements.

######### 2.3.1 ######### Photodetection

Photodetection is the minimal time-continuous measurement scheme  at each moment

in time, the detector records one of only two possible results: _r_ = 0 (no-click) or _r_ = 1

(click). As discussed in Sec. 2.2, the measurement result communicates some knowledge

about the system state and the unavoidable disturbance caused to it by the measurement

itself. 18 The information gain as well as the action of the disturbance are encoded in the


measurement operators, _M_ _r_ , recall Eq. (2.25). These operators, also known as Kraus


operators, generalize unitary evolution due to a system Hamiltonian, _H_ , so as to include


the effect of the measurement process. Microscopically, the measurement operators, _M_ _r_ ,

can be understood to describe the unitary interaction between the system and another,

auxiliary one, which is subsequently measured by a von Neumann measurement apparatus,

see discussion on Neumarks theorem in Sec. 2.2. In this section, we will only concern

ourselves with the system evolution subject to measurement, and will make no further

reference to the auxiliary system, other than to specify the system operator  _c_ that couples

the two. The minimal set of infinitesimal measurement operators, which corresponding

to the no-click ( _r_ = 0 ) and click ( _r_ = 1 ) evolution, are


1
_M_  0 (d _t_ ) =  1 _c_  __ _c_  + _i_ _H_  d _t ,_ (2.37)
__ 2
 


_M_ 1 (d _t_ ) =


_dt_ _c ,_  (2.38)



 
in units where  = 1 . One can verify that _M_ 0 (d _t_ ) and _M_ 1 (d _t_ ) form a positive-operator-

valued measure (POVM) on the space of results. Hence, they form a resolution of the

18 From an operational point of view, the state of the system is strictly speaking only _our_ knowledge
about the probabilities for outcomes of _future_ measurements of the system.


-----


2.3. Quantum trajectory theory 52

identity, _M_  0 __ (d _t_ )  _M_ 0 (d _t_ ) + _M_  1 __ (d _t_ )  _M_ 1 (d _t_ ) =  1 + (d _t_ 2 ) , guaranteeing that the law
_O_

of total probability is satisfied, i.e., a measurement yields an outcome with probability 1.

The probability for a specific outcome, _r_ = 0 or _r_ = 1 , is is given by the generalized


measurement postulate, Eq. (2.26), __ _r_ (d _t_ ) = _M_ _r_ __ (d _t_ )  _M_ _r_ (d _t_ ) ,


__ 0 (d _t_ ) = 1 __ d _t_ _c_  __ _c_  + _O_ d _t_ 2 _,_ (2.39)
   

__ 1 (d _t_ ) = d _t_ _c_  __ _c_  _._ (2.40)
 

We define the time-continuous photodetection measurement record to be the number of

photodetections up to time _t_ , denoted _N_ ( _t_ ) . It follows that the infinitesimal measurement

increment, denoted d _N_ ( _t_ ) , is a _point-process_ , also known as the _Poisson process_ , defined

by

d _N_ ( _t_ ) 2 = d _N_ ( _t_ ) _,_ (2.41)

E [d _N_ ( _t_ )] = __ 1 (d _t_ ) _,_ (2.42)

where E [ __ ] denotes the expectation value in the classical sense, see Sec. 2.1.1. In the

continuum limit, the detector photocurrent, _I_ ( _t_ ) = d _N_ ( _t_ ) _/_ d _t_ , consists of a series of

Dirac __ -functions at the times of the clicks.

**Stochastic master equation (SME) for ideal photodetection.** Ideal photodetec-

tion is the limit where the photodetector collects the entirety of the system output field

and adds no technical noise, i.e., the quantum measurement efficiency is one, __ = 1 .

According to the generalized projection postulate, Eq. (2.27), the state of the system

after a measurement at time _t_ conditioned on the measurement result _r_ = 0 or _r_ = 1 is


 
__ _r_ ( _t_ + d _t_ ) = _M_ _r_ (d _t_ ) __ ( _t_ ) _M_ _r_ __ (d _t_ ) _._ (2.43)

__ _r_ (d _t_ )


-----


2.3. Quantum trajectory theory 53

In the continuum limit, where the instantaneous measurement outcome is the photocur-

rent _I_ ( _t_ ) _,_ the two possible states, __ 0 ( _t_ + d _t_ ) and __ 1 ( _t_ + d _t_ ) , can be combined in a

single stochastic differential equation (SDE) for the posterior system state __ _I_ ( _t_ + d _t_ )

conditioned on _I_ ( _t_ ) , resulting in the state differential, in It form,

d __ _I_ ( _t_ ) = __ _I_ ( _t_ + d _t_ ) __ __ _I_ ( _t_ ) (2.44)

= d _N_ ( _t_ ) __ 1 ( _t_ + d _t_ ) __  1 + (1 __ d _N_ ( _t_ )) __ 0 ( _t_ + d _t_ ) __  1 _,_ (2.45)
   

which can be simplified by Taylor expanding the denominator of __ 0 ( _t_ + d _t_ ) , retaining

terms to order d _t_ , and employing the stochastic calculus rule 19

d _N_ ( _t_ ) d _t_ = 0 (2.46)

in order to obtain the _stochastic master equation_ (SME) for photodetection, in the

Schrdinger picture and in It form,

![Mivev_Thesis.pdf-69-0.png](Mivev_Thesis.pdf-69-0.png)

where the superoperators _G_ [ _c_ ] __ and _H_ [ _c_ ] __ are defined by


_c_  __ __ _c_ 
[ _c_ ] __
_G_ __ Tr [ _c_ __



_ ,_ (2.48)
Tr [ _c_ __ __ _c_  ] __


_H_ [ _c_ ] __ __ _c_  + __ _c_  __ __ Tr _c_  + __ _c_  __ __ (2.49)
 


= ( _c_ __ _c_  __ ) __ + __ _c_  __ __ _c_  __ _,_ (2.50)
  


19 Technically, d _N_ ( _t_ ) d _t_ is not strictly zero. However, because the mean of d _N_ is infinitesimal, d _N_ ( _t_
is negligible when compared with d _t_ , and so are all higher-order products containing both d _N_ and d _t_ .


-----


2.3. Quantum trajectory theory 54

The superoperator _G_ results in point-like discontinuous state evolution, while _H_ results in

smooth, continuous, but non-unitary evolution generated by the effective non-Hermitian

Hamiltonian



1
_H_  eff _H_  _i_ _c_  __ _c ._  (2.51)
__ __ 2

Notably, the trace terms in Eqs. (2.48) and (2.49) make the photodetection SME, Eq. (2.47),


_nonlinear_ in the state density, __ _I_ . The origin of the trace term in _H_ , namely Tr _c_  + __ _c_  __ ,

is the Taylor expansion of the denominator of Eq. (2.43), which gives the no-click prob-  

ability, __ 0 (d _t_ ) . As discussed in Sec. 2.2, the role of this term is to preserve the state

density trace for all time, Tr [ __ _I_ ( _t_ )] = 1 . The solution of the SME is a stochastic path

taken by the conditional state over time, known as a _quantum trajectory_ , a term coined

in Ref. _Carmichael (1993)._

**Stochastic Schrdinger equation (SSE) for photodetection.** For a system in a

pure state, __ _I_ ( _t_ ) = _|_ __ _I_ ( _t_ ) __ __ _I_ ( _t_ ) _|_ , the SME, Eq. (2.47), preserves the purity of the

state for all times. It follows that the state evolution is described by a type of Schrdinger

equation, known as the _stochastic Schrdinger equation_ (SSE),





(2.52)


![Mivev_Thesis.pdf-70-0.png](Mivev_Thesis.pdf-70-0.png)

which is nonlinear in the state _|_ __ _I_ ( _t_ ) __ . The non-linear terms contain the expectation value
_c_  __ _c_  ( _t_ ) = 1 __ _I_ ( _t_ ) _c_  __ _c_  __ _I_ ( _t_ ) , which gives the click probability __ 1 , see Eq. (2.40). Be-


cause these non-linear terms render analytic treatment of the equations particularly difficult


__ _I_ ( _t_ ) _c_  __ _c_  __ _I_ ( _t_ ) , which gives the click probability __ 1 , see Eq. (2.40). Be-

cause these non-linear terms render analytic treatment of the equations particularly difficult   

 


in general, a linear description of the state evolution is desired, and can be accomplished


as described next. The term 2 1 d _t_ _c_  __ _c_  ( _t_ ) __ _I_ ( _t_ ) , which updates the observers state-

_|_ __

of-knowledge in a non-linear way, mathematically, ensures the proper normalization of  

_|_ __ _I_ ( _t_ ) __ for all times; however, normalization need not be enforced for each infinitesimal


-----


2.3. Quantum trajectory theory 55

timestep d _t_ . Instead, it can manually be enforced for the no-click periods, _I_ ( _t_ ) = 0 ,




by first first solving for the un-normalized system state, denoted with a tilde, __ _I_ =0 ( _t_ )

  
then normalizing it, __ _I_ =0 ( _t_ ) = __ _I_ =0 ( _t_ ) _/_ __ _I_ =0 ( _t_ ) __ _I_ =0 ( _t_ ) , where the effective 
_|_ __ 



  
then normalizing it, _|_ __ _I_ =0 ( _t_ ) __ = __ _I_ =0 ( _t_ ) _/_ __ _I_ =0 ( _t_ ) __ _I_ =0 ( _t_ ) , where the effective


Schrdinger equation for __ _I_ =0 ( _t_ )  is 

 




Schrdinger equation for __ _I_ =0 ( _t_ ) is




 

![Mivev_Thesis.pdf-71-0.png](Mivev_Thesis.pdf-71-0.png)


where _H_ eff is the non-Hermitian Hamiltonian, Eq. (2.51). Since Eq. (2.53) is linear, it is



  
__ _I_ =0 ( _t_ ) = _H_ eff __ _I_ =0 ( _t_ ) _,_ (2.53)
 
 


generally easier to solve for the time-dynamics. Calculation of system averages still requires



  
normalizing __ _I_ =0 ( _t_ ) by its the state norm, __ _I_ ( _t_ ) __ _I_ ( _t_ ) , which gives the probability

of no-clicks occurring for duration  _t_ . We remark that Eq. (2.53) corresponds to tracking 

 

the sub-ensemble of quantum trajectories that contain no clicks, or mathematically, to


the repetitive application of the measurement operator _M_ 0 ; hence, in general, in the limit

_t_ __ , it leads to the decay of the norm to zero.

**Unconditioned evolution: master equation for photodetection.** By averaging

over all possible evolutions due to all measurement outcomes at each instant, one can ob-

tain the _unconditioned_ evolution of the quantum state, denoted __ ( _t_ + d _t_ ) , from Eq. (2.47).


Simplifying the average, __ ( _t_ + d _t_ ) =




_r_ __ _r_ __ _r_ ( _t_ + d _t_ ) ,


__ ( _t_ + d _t_ ) = _M_  0 (d _t_ ) __ _M_  0 __ (d _t_ ) +  _M_ 1 (d _t_ ) __ _M_  1 __ (d _t_ ) (2.54)



= __ ( _t_ ) __ _i_ _H, _ ( _t_ ) d _t_ + _D_ [ _c_ ] __ ( _t_ ) d _t ,_ (2.55)

where the superoperator _D_ is defined to be



1
[ _c_ ] __ _c_  _c_  __ _c, _  + _._ (2.56)
_D_ __ __ 2 _{_ _}_


-----


2.3. Quantum trajectory theory 56

Eq. (2.55) for the unconditioned state evolution is known as the _master equation,_ in

Lindblad form (Lindblad, 1976). 20 Unlike the SME, it is linear in the state density, __ , and

yields deterministic state evolution, since there are no stochastic increments, d _N_ or d _W_ .

Notably, the master equation is very general and makes no reference to photodetection,

other than specifying the system operator  _c_ subject to detection, although it does not

specify how. As will be evident from the following section, the same master equation is

obtained for heterodyne detection of  _c_ , see Sec. 2.3.2. The two SMEs corresponding to

the same master equation are known as _unravellings_ 21 of it. We note that the unravellings

of the master equation are not unique.

**Imperfect detection.** Imperfect conditions limit the observers access to informa-

tion regarding the system and generally result in excess noise. The effect of imperfections

can be modeled by considering an ideal photodetector that is, however, sensitive to only a

fraction __ of the system output field. This fraction, known as the _quantum measurement_

_efficiency_ , is a real number between zero and one, 0 __ __ __ 1 . Because of the loss of

information due to imperfect detection, over time, the system state will, in general, be-

come mixed, with purity less than one, 0 __ Tr [ __ 2 ] _<_ 1 . To account for the imperfections,

SME, Eq. (2.47), is be modified in the following way, see Sec. 4.8.1 of Ref. Wiseman and

Milburn (2010):


![Mivev_Thesis.pdf-72-0.png](Mivev_Thesis.pdf-72-0.png)

For a comprehensive summary of the properties of the master equation and Lindbladians, see Refs. Albert and Jiang (2014), Albert 20 _et al._ (2016).
21 The term unraveling was coined in Ref. Carmichael (1993).


-----


2.3. Quantum trajectory theory 57

where the jump probability for each timestep is obtained by also replacing  _c_ with __ __ _c_  in

Eq. (2.42), E [d _N_ ( _t_ )] = __ Tr _c_  __ _c_  d _t_ . Considering the two limits __ __ 0 and __ __ 1 ,

one can associate the Lindblad superoperator   _D_ with information loss, and _H_ and _G_ with

information gain due to the measurement.

######### 2.3.2 ######### Homodyne and heterodyne detection

The measurements described so far are not sensitive to the phase of the system output

field, but only its amplitude. In the following, we describe _dyne_ measurements _, homodyne_

or _heterodyne,_ which provide information about the phase and a qualitatively different

(diffusive) trajectory unraveling.

**Physical implementation.** Dyne detection is realized by mixing the system output

signal with a local-oscillator (LO) tone, see Fig. 2.6. For a system carrier frequency,

conventionally termed the radio frequency (RF), __ RF and LO frequency __ LO , the lower

sideband of the mixed-signal is at intermediate frequency (IF), __ IF = __ LO __ __ RF . In

homodyne detection, the LO is tuned in resonance with the system carrier, resulting in a

direct-current (DC) IF signal, __ IF = 0 , proportional to a quadrate of the RF signal that

depends on the LO phase. The IF signal is typically sampled and digitally processed. On

the other hand, in heterodyne detection, the LO frequency is significantly detuned from

the RF, __ IF __ 0 , resulting in a an oscillatory IF signal, which is demodulated to extract

the information-bearing _in-quadrature_ (I) and _out-of-quadrature_ (Q) components. Note

that the heterodyne measurement record consists of a series of not one but _two_ values,

I and Q. Heterodyne detection is equivalent to two concurrent homodyne detections with

LO phases 90 __ apart.

**Homodyne measurement record.** The homodyne measurement signal is mathemat-

ically described by a function, _J_ hom ( _t_ ) , that is real and continuous everywhere but differ-


-----


2.3. Quantum trajectory theory 58

**a)** **b)** **c)**


RF


LO RF IF


photodetector

|system|c|
|---|---|


![Mivev_Thesis.pdf-74-0.png](Mivev_Thesis.pdf-74-0.png)

hom


![Mivev_Thesis.pdf-74-1.png](Mivev_Thesis.pdf-74-1.png)

**Figure 2.6** Schematic representations of a (a) photo, (b) homodyne, and (c) heterodyne detection schemes. _|_ **a,** The system output field, proportional to the system
coupling operator  _c_ , is directly monitored with a photodetector, whose photocurrent _I_ ( _t_ )
is the measurement record. **b,** Optical balanced homodyne detection: system output
field, assumed with carrier frequency __ RF , is interfered on a 50:50 beam splitter with a
strong local oscillator (LO) tone at the carrier frequency, __ LO = __ RF
. The measurement record, _J_ hom ( _t_ ) , is obtained from the difference of the photodetector currents on
each output arm of the beamsplitter. **c,** Balanced heterodyne detection scheme (with
digital demodulation): LO frequency is detuned by an intermediate frequency value, __ IF _,_
where __ IF __ __ RF _, _ LO . The difference of the photodetector currents of each arm, which
oscillates at __ IF
, is digitally demodulated to obtain the in-phase [out-of-phase] quadrature Re _J_ het ( _t_ ) [ Im _J_ het ( _t_ ) ] by digitally mixing the signal with a reference one, cos ( __ IF _t_ )

[ sin ( __ IF _t_ ) ], and low-pass filtering the output to reject tones above __ IF . Digital panel
schematic inspired by Ref. (Campagne-Ibarcq _et al._ , 2016b).


-----


2.3. Quantum trajectory theory 59

entiable nowhere, see Sec. 2.2.3. The measurement signal gradually reveals information

about a system operator of the form  _c_ +  _c_ __ , where  _c_ is the operator coupled to the mea-


surement apparatus, which for the example of Sec. 2.2.3 is  _c_ = __ 2 __ __  _z_ . In It form, the
__

measurement increment is

d _J_ hom ( _t_ ) = _c_  +  _c_ __ ( _t_ ) d _t_ + d _W_ ( _t_ ) _,_ (2.58)
 

where d _W_ ( _t_ ) is the stochastic Wiener increment satisfying the canonical relations given

in Eqs. (2.34) and (2.35).

**Heterodyne measurement record.** The heterodyne measurement signal consists of

two functions: the in-phase, _J_ _I_ ( _t_ ) , and out-of-phase, _J_ _Q_ ( _t_ ) , quadrature functions, which


can be combined in a single complex function, _J_ het ( _t_ ) 1 2 ( _J_ _I_ ( _t_ ) + _iJ_ _Q_ ( _t_ )) , continuous
__

everywhere but differentiable nowhere. In heterodyne detection, _J_ het ( _t_ ) gradually reveals

information about a system operator  _c_ , which need not be Hermitian but which can be

decomposed into the sum of two Hermitian operators, corresponding to two observables,

know as the quadrature operators,

_I_  __ _c_  +  _c_ __ and _Q_  __ _i_ _c_  __ _c_  __ _,_ (2.59)
 


so that  _c_ = 1 2

where d _Z_ __


 
_I_ + _i_ _Q_ . The It form of the measurement increment is

d _J_ het ( _t_ ) = __ _c_  __ ( _t_ ) d _t_ + d _Z_ ( _t_ ) _,_ (2.60)

2 (d _W_ _I_ ( _t_ ) + _i_ d _W_ _Q_ ( _t_ )) is the complex Wiener increment, the sum of two


independent Wiener increments, d _W_ _I_ ( _t_ ) and d _W_ _Q_ ( _t_ ) , that satisfy E [d _W_ _I_ ( _t_ ) d _W_ _Q_ ( _t_ )] =

0 , so that d _Z_ ( _t_ ) __ d _Z_ ( _t_ ) = d _t_ and d _Z_ ( _t_ ) 2 = 0 . We note that d _Z_ is obtained by making


-----


2.3. Quantum trajectory theory 60

the substitution _e_ _i_ RF _t_ d _W_ __ d _Z_ in the heterodyne derivation.

For concreteness, consider the example of a qubit coupled to the environment where

an observer performs heterodyne detection of the qubit fluoresce (Campagne-Ibarcq _et al._ ,

2014, 2016b, Naghiloo _et al._ , 2016). The system-environment coupling is given by the

non-Hermitian operator  _c_ =  __ + _z_ _z_ , which is decomposed into the two Hermitian
__ _|_ __ _|_

  
quadrature operators _I_ =  __ _x_ and _Q_ = __ __  _y_ . Note the minus sign in _Q_ . The heterodyne


detection of  __ can be understood as a homodyne detection of the observable _I_ and a
__


concurrent homodyne detection of the observable _Q_ , each with efficiency __ = 1 _/_ 2 , see

below. Consider the example where the qubit is replaced by a cavity, the coupling operator

is  _c_ =  _a_ , where  _a_ is the annihilation operator, and the whose cavity output field is subject to



 
heterodyne monitoring, which reveals information about _I_ =  _a_ + _a_ __ and _Q_ = __ _i_ _a_  __ _a_  __

For a coherent state in the cavity, __ ( _t_ )  


For a coherent state in the cavity, _|_ __ ( _t_ ) __ , the measurement record gradually reveals its


complex amplitude, E [d _J_ het ( _t_ ) _/_ d _t_ ] = __ ( _t_ ) 2 1




**Measurement operators and the SME for perfect dyne detection.** At an instant


_I_  +  _i_ _Q_  __ ( _t_ ) = __ ( _t_ ) .
 




in time, the noisy heterodyne record, _J_ het ( _t_ ) , relates the measurement outcome to the

quantum trajectory evolution according to the action of the measurement operator (see

discussion on Pg. 44)



1
_M_  _J_ =  1 __ _i_ _H_  d _t_ __ 2 _c_  __ _c_  d _t_ + _J_ het __ ( _t_ )  _c_ d _t ._ (2.61)


The measurement operator for homodyne detection, also denoted _M_ _J_ , is obtained by

making the substitution _J_ het __ ( _t_ ) _J_ hom ( _t_ ) in Eq. (2.61). Notably, the non-orthogonal

__


set of measurement operators for dyne detection, _M_ _J_ : _J_ , is continuous, in contrast
   

with that of photodetection, which consists of two elements, _M_ 0 _,_ _M_ 1 _,_ since there are
 

only two possible measurement outcomes, click or no click. The system state conditioned

on the record at time _t_ , denoted __ _J_ , is obtained by employing the generalized measurement


-----


2.3. Quantum trajectory theory 61

postulate, Eq. (2.27),


__ _J_ ( _t_ + d _t_ ) = _M_  _J_ __ _J_ ( _t_ ) _M_  _J_ __


Equation (2.62) is simplified by Taylor expanding the denominator to order d _t_ and writing


_J_ _J_ _J_ _._ (2.62)

Tr _M_  _J_ __ _J_ ( _t_ ) _M_  _J_ __
 


the infinitesimal state change, in It form, d __ _J_ ( _t_ ) = __ _J_ ( _t_ + d _t_ ) __ __ _J_ ( _t_ ) , thus obtaining

the SME for perfect heterodyne detection, in the Schrdinger picture,

d __ _J_ ( _t_ ) = __ _i_ d _t_ [ _H,_  __ ] + d _t_ _D_ [ _c_ ] + d _Z_ __ ( _t_ ) _H_ [ _c_ ] __ _J_ ( _t_ ) _,_ (2.63)
 

where the superoperators _D_ and _H_ are defined in Eqs. (2.56) and (2.49), respectively.

Equation (2.63) has to be solved jointly with Eq. (2.60). The homodyne SME is obtained

by making the substitution d _Z_ __ ( _t_ ) __ d _W_ ( _t_ ) in Eq. (2.63).

**SME for imperfect measurements.** Measurement imperfections (see discussion on

Pg. 2.57) are primarily due to: i) losses associated with the propagation of the system

output field to the measurement apparatus, characterized by a quantum efficiency __ prop ,

and ii) finite detector efficiency, __ det . The measurement chain efficiency is given by the

product of those of it sub-components, __ = __ prop __ det , and is used to modify Eq. (2.60)

to account for imperfections by making the substitution  _c_ __ __ _c_  ,
__

d _J_ het ( _t_ ) = __ __ __ _c_  __ ( _t_ ) d _t_ + d _Z_ ( _t_ ) _._ (2.64)


Similarly, the homodyne measurement increment is d _J_ hom ( _t_ ) = __ __ _c_  +  _c_ __ ( _t_ ) d _t_ +

d _W_ ( _t_ ) . In Eq. (2.64), the effect of an efficiency less than one, _ <_  1 , is to reduce 

the measurement signal amplitude, __ _c_  __ , relative to the noise, d _Z_ , resulting in a degraded

signal-to-noise (SNR) ratio. In the extreme limit __ __ 0 , the measurement is entirely noise,


-----


2.3. Quantum trajectory theory 62

and the SNR is zero. Only in the limit __ __ 1 , as discussed in Sec. 2.2, can the noise

be interpreted as entirely due to quantum vacuum fluctuations. The trajectory evolution

associated with the noisy signal, _J_ het ( _t_ ) , is obtained by making the substitution  _c_ __ __ __ _c_ 

in the innovator, _H_ , term of the heterodyne SME, Eq. (2.63), which is responsible for

the information gain due to the measurement, thus obtaining the SME for finite-efficiency

heterodyne detection,

![Mivev_Thesis.pdf-78-0.png](Mivev_Thesis.pdf-78-0.png)

which upon the the substitution d _Z_ __ ( _t_ ) __ d _W_ ( _t_ ) becomes the SME for finite-efficiency

homodyne detection. Equations (2.65) and (2.64) have to be solved simultaneously.

**Qualitative comparison of dyne- vs. photo- detection trajectories.** In Sec. 2.3.1,

we considered the stochastic evolution of the conditional quantum state of a system sub-

ject to photodetection, a measurement scheme that results in one of two possible out-

comes, _r_ = 0 and _r_ = 1 , at each moment in time. The state evolution was marked by

two qualitatively distinct possibilities: i) smooth, continuous, deterministic-like evolution


due to the non-Hermitian Hamiltonian _H_ eff , associated with _r_ = 0 , or ii) discontinuous,

point-like, jumpy evolution due to the action of the superoperator term _G_ , associated with

the occasional outcome _r_ = 1 . Both the measurement record and the state evolution of

dyne detection are, in a sense, antithetic to those of dyne detection, which is charac-

terized by a (Gaussian-distributed) infinite continuum of possible measurement outcomes

and neither smooth nor jumpy state evolution. Rather, the evolution is _diffusive_ (Gisin

and Percival, 1992), a consequence of the Gaussian-distributed measurement outcomes.

While in photodetection, a click could result in a substantial amount of information about

the system being acquired at an instant in time, such an event is not possible with dyne


-----


2.4. Further reading 63

monitoring, where the noisy signal, _J_ ( _t_ ) , only _gradually_ reveals information about the

state of the system. It is only in this gradual sense that dyne measurements collapse the

system state to an eigenstate of the measurement operator, see discussion of Sec. 2.2.3.

###### 2.4 ###### Further reading

For further reading, we suggest the following books, and, where applicable, note sections

closely related to some of the topics discussed in more depth in this chapter:

-  Carmichael (1993) & Carmichael (1999)  The formulation of quantum trajectory

theory is presented; key terms, such as unraveling, are introduced. Section 17.2 of

Ref. Carmichael (1999) treats the example of a quantum bit subject to continuous

photodetection, comparing the state evolution in quantum measurement theory with

that of classical measurement theory.

-  Gardiner and Zoller (2004)  Chapter 3 provides a useful derivation of input-output

theory by treating the one-dimensional transmission line. Focus on the Heisenberg

formulation of quantum measurements.

-  Wiseman and Milburn (2010)  Classical measurement theory is introduced in

Chapter 2.

-  Jacobs (2010)  Introduction to _classical_ stochastic differential equations (SDE).

-  Girvin (2014)  Chapter 3 discusses quantum measurements in the context of

circuit quantum electrodynamics (cQED), which is introduced in the remainder of

the notes.

-  Steck (2017)  Lecture notes on quantum trajectories, SDE numerical methods,

and a number of related topics in quantum optics.


-----


2.4. Further reading 64

We conclude this chapter with an amusing quote by H. Mabuchi:

 _The quantum measurement problem refers to a set of people_ .

[the set who have a problem with the theory of quantum measurements] (Fuchs, 2003).


-----


### Theoretical description of quantum

 jumps

Photons, the quanta of light, are countable and discrete,
and one assumes they come and go in jumps. Einstein
proposed it so  though only as a pragmatic step ... Yet
the Schrdinger equation is deterministic and nothing
within its jurisdiction jumps. What then to make of this
unlikely marriage where the continuous is to somehow
cavort with the discrete.

H.J. Carmichael
New Zealand Science Review
Vol. 72 (2) 2015

his chapter presents the quantum trajectory description of the Dehmelt electron-

shelving scheme and the catch-and-reverse circuit quantum electrodynamics (cQED)

## T

experiment. Section 3.1 discusses quantum jumps in the three-level atom subject to flu-

orescence photodetection. The minimal idealized model with coherent Rabi drives is

considered in Section 3.1.1. To better conceptualize important aspects of the measure-

ment dynamics, Sec. 3.1.2 considers the simpler case of a three-level atom subject only

to measurement and no competing coherent dynamics; i.e., the Dark Rabi drive is zero,

65


-----


3.1. Fluorescence monitored by photon counts 66

 DG = 0 . The character of the unavoidable state-disturbance due to the back-action

of the measurement is examined in depth, and the notion of _measurement-backaction_

_effective force_ and its geometrical representation are introduced. Section 3.1.3 continues

the description of quantum jumps and considers the flight of the jump in the presence of

an incoherent Bright drive and the conditional interruption of  DG (  _t_ off ). Section 3.2

presents the trajectory description of the cQED experiment including all known imper-

fections. Section 3.2.2 discusses the Monte Carlo simulation of the linear Stochastic

Schrdinger equation (SSE), employed in the comparison between theoretical predictions

and experimental results, see Sec. 5.5.

###### 3.1 ###### Fluorescence monitored by photon counts

######### 3.1.1 ######### Dehmelt electron-shelving scheme and quantum jumps

As discussed in Chapter 1, the experiments with trapped ions (Nagourney _et al._ , 1986,

Sauter _et al._ , 1986, Bergquist _et al._ , 1986) monitor intermittent fluorescence from the

bright state _|_ B __ to track jumps between _|_ G __ and _|_ D __ (Cook and Kimble, 1985). In the

simplest three-level scheme (Bergquist _et al._ , 1986) and using coherent radiation to excite

both the BG and DG transitions, the master equation, Eq. (2.55), for the reduced density

operator __ of the three-level system, written in the interaction picture, is


d __ ( _t_ ) = ( _i_  ) __ 1 [  _H_ drive _, _ ( _t_ )] + __ B [ G B ] __ ( _t_ ) + __ D [ G G ] __ ( _t_ ) _,_ (3.1)

d _t_ _D_ _|_ __ _|_ _D_ _|_ __ _|_


where [ _c_ ] =  _c_  _c_ __ 2 1 _c_  __ _c,_  denotes the Lindblad superoperator, defined in Eq. (2.56),
_D_ __ __ __ _{_ _}_

__ B and __ D are radiative decay rates of the B and D level, respectively, and the drive


-----


3.1. Fluorescence monitored by photon counts 67

Hamiltonian is


  BG
_H_ drive = _i_ 



 DG
B G G B + _i_ 
_|_ __ _| |_ __ _|_ 2


_|_ D __ G _| |_ G __ D _|_ _,_ (3.2)


with  BG and  DG the Rabi drives.

**Quantum trajectory description.** The quantum trajectory description (Carmichael,

1993, Dalibard _et al._ , 1992, Dum _et al._ , 1992) unravels __ into an ensemble of pure states,

see Sec. 2.3.1, whose ket vectors evolve along stochastic paths conditioned on the clicks of

_imaginary_ photon detectors that monitor fluorescence from _|_ B __ and, much less frequently,

from _|_ D __ . Working in the limit of the omniscient observer, corresponding to unit quantum

measurement efficiency, __ = 1 , for both the B and D click records, denoted d _N_ B ( _t_ ) and

d _N_ D ( _t_ ) , respectively, see Eqs. (2.41) and (2.42), and corresponding to the quantum jump

operators  _c_ B = __ __ B _|_ G __ B _|_ and  _c_ D = __ __ D _|_ G __ D _|_ , respectively, the non-linear stochastic

Schrdinger equation (SSE) in It form, Eq. (2.52), is



 __ B
d _|_ __ _I_ ( _t_ ) __ =d _t_ __ _i_ _H_ +



B D

2 ( _|_ B __ B _|_ ( _t_ ) _|_ B __ B _|_ ) + __


2 ( _|_ D __ D _|_ ( _t_ ) _|_ D __ D _|_ ) _|_ __ _I_ ( _t_ ) __


G B
_|_ __ _|_  1

_|_ B __ B _|_ ( _t_ ) __


_|_ G __ B _|_


G D
_|_ __ _|_  1

_|_ D __ D _|_ ( _t_ ) __


+ d _N_ B ( _t_ )


+ d _N_ D ( _t_ )


_|_ G __ D _|_


(3.3)

The terms proportional to d _N_ B ( _t_ ) and d _N_ D ( _t_ ) reset the ket vector to _|_ G __ with instanta-

neous probability __ B _|_ B __ B _|_ ( _t_ ) d _t_ and __ D _|_ D __ D _|_ ( _t_ ) d _t_ , respectively, and correspond

to the state-disturbance due to the detection of a click on the B and D detectors, re-

spectively. Otherwise, when no click is observed on either detector, the state follows a

deterministic evolution as a coherent superposition, governed by the terms proportional

to d _t_ .


-----


3.1. Fluorescence monitored by photon counts 68

**Linear SSE and no-click evolution.** To describe the conditional no-click evolution,

as discussed on Pg. 55, it is analytically favorable to work with the linear form of the

SSE, obtained by suppressing the expectation value terms in Eq. (3.3), and defining the

_un-normalized_ quantum state,




__ ( _t_ catch ) = _c_ G ( _t_ catch ) _|_ G __ + _c_ B ( _t_ catch ) _|_ B __ + _c_ D ( _t_ catch ) _|_ D __ _,_ (3.4)



where  _t_ catch denotes the no-click duration. Immediately after a click, marked by  _t_ catch =




0 , the state __ ( _t_ catch ) is reset with the coefficients _c_ G ( _t_ catch ) = 1 and _c_ B ( _t_ catch ) =

_c_ D ( _t_ catch ) = 0  _._ Conditioned on no clicks, the evolution of the un-normalized state is



governed by the effective non-Hermitian Hamiltonian, see Eq. (2.51),


  __ B
_H_ eff = _H_ drive _i_ 
__ 2



B __ D

B B _i_ 
2 _|_ __ _| _ 2



D

D D _,_ (3.5)
2 _|_ __ _|_


and the Schrdinger-type equation




d __ ( _t_ catch )
_i_ 

d _t_ catch






 
= _H_ eff __ ( _t_ catch ) _._ (3.6)
d _t_ catch




decays as a function of  _t_ catch and gives the probability that the no-click evolution has



 
Due to the purely imaginary-valued terms in _H_ eff , the norm of the state __ ( _t_ catch )

decays as a function of  _t_ catch and gives the probability that the no-click evolution has 




continued without click interruptions for duration  _t_ catch . In the limit  _t_ catch __ 0 , the

norm of the ket approaches zero. The evolution of the state can be described by a matrix

equation for the state coefficients, using Eqs. (3.4), (3.5), and (3.6),


_c_ G

_c_ B

_c_ D


0  BG  DG
__ __

 BG __ B 0
__

 DG 0 __ D
__


_c_ G


d _t_ catch


= 1


_c_ B


(3.7)


_c_ D


-----


3.1. Fluorescence monitored by photon counts 69

In general this 3 __ 3 system does not have a closed solution in simple form, although there

is a particularly simple solution under conditions that produce intermittent fluorescence,

i.e., rare jumps from _|_ G __ to _|_ D __ [shelving in the dark state (Nagourney _et al._ , 1986)]

interspersed as intervals of fluorescence off in a background of fluorescence on. The

conditions follow naturally if _|_ D __ is a metastable state (Nagourney _et al._ , 1986, Sauter

_et al._ , 1986, Bergquist _et al._ , 1986) whose lifetime __ D __ 1 is extremely long on the scale of

the mean time,


__ BG =  2 BG _,_ (3.8)

__ B

between photon detector clicks for a weak  BG Rabi drive. Subject to ( DG _, _ D ) __

 2 BG _/_ B __ B , one way to solve Eq. (3.7) is to first adiabatically eliminate the fast time

__

dynamics of the B level, by setting the time derivative of the B coefficient to zero,


d _c_ B

= 0 _,_ (3.9)
d _t_ catch


Solving Eq. (3.9), _c_ B =  __ BG B _c_ G , allows one to eliminate the B level from the description


Solving Eq. (3.9), _c_ B =  BG


of the dynamics and to extract the effective GD dynamics, to obtain the un-normalized

state conditioned on the detection of no clicks,



 BG
G +
_|_ __ __ B




  2 BG
__ ( _t_ catch ) = exp
__ 2 __ B

 

 + exp


BG  _t_ catch

2 __ B


B
__ B _|_



__ D
exp __ 2



D  _t_ catch exp  2 BG

2 __ __ 2 __ B


BG  _t_ catch

2 __ B


__ B  D

 2 BG _|_ D __ _._ (3.10)




__ B  D

 2 BG





 
Note that __ ( _t_ catch ) has purely real coefficients, since _H_ eff has purely imaginary ones.

The Bloch vector components of the normalized GD manifold evolution conditioned on 




-----


3.1. Fluorescence monitored by photon counts 70

no-clicks are obtained by normalizing the state, Eq. (3.10),


Z GD ( _t_ catch ) = _W_ _W_ DG DG ( ( _t_ _t_ catch catch ) ) + __ _W_ _W_ DG DG __ __ 1 1 ( ( _t_ _t_ catch catch ) ) _,_ (3.11)


_W_ DG ( _t_ catch ) + _W_ DG __ 1 ( _t_ catch ) _,_ (3.12)


X GD ( _t_ catch )


Y GD ( _t_ catch ) = 0 _,_ (3.13)

where we have defined the ratio (Porrati and Putterman, 1987)



_c_ D ( _t_ catch )
_W_ DG ( _t_ catch ) _._ (3.14)
__ _c_ G ( _t_ catch )

Notably, as an alternative to the adiabatic method employed to solve Eq. (3.7), one can

instead directly write down the equation of motion for _W_ DG within the same approxima-


tions,
d _W_ DG


d _W_ DG  2 BG

=
d _t_ catch 2 __ B



 2 BG _W_ DG +  DG

2 __ B 2



DG

_,_ (3.15)
2


which, with the initial condition _W_ DG (0) = 0 , has the solution


 DG
_W_ DG ( _t_ catch ) =  2 BG _/_ B


exp  2 BG  _t_ catch

2 __ B




 DG
_W_ DG ( _t_ catch ) =


__ 1 _,_ (3.16)


and also yields the Bloch components, Eqs. (3.11), (3.12), and (3.13). The timescale of

the transition, the mid-flight time of the quantum jump,  _t_ mid , is found by setting the G

and D coefficients equal to each other, _c_ G ( _t_ mid ) = _c_ D ( _t_ mid ) _,_



__ 1 ln  2 BG _/_ B + 1 _._ (3.17)



![Mivev_Thesis.pdf-86-0.png](Mivev_Thesis.pdf-86-0.png)

For strong monitoring,  2 BG __ B __ 1  DG , the +1 in Eq. (3.17) can be dropped. Working

__

in this limit, Eqs. (3.11)(3.13) provide simple formulas for the continuous, deterministic,


For strong monitoring,  2 BG __ B __ 1  DG , the +1 in Eq. (3.17) can be dropped. Working

__


-----


3.1. Fluorescence monitored by photon counts 71

and coherent evolution of the completed quantum jump:


Z GD ( _t_ catch ) = tanh  2 BG

2 __ _B_




BG ( _t_ catch  _t_ mid ) _,_ (3.18)

2 __ _B_ __


X GD ( _t_ catch ) = sech  2 BG

2 __ _B_




BG ( _t_ catch  _t_ mid ) _,_ (3.19)

2 __ _B_ __


Y GD ( _t_ catch ) = 0 _._ (3.20)


These formulas, derived in the strong-monitoring limit, execute a perfect jump, Z GD ( __ ) =

1 , X GD ( __ ) = Y GD ( __ ) = 0 . Departures from the ideal limit can be transparently

analyzed by adopting an incoherent Bright drive, see Sec. 3.1.3. An elegant analysis of

the no-click evolution for arbitrary amplitude of the Dark Rabi drive can be found in

Refs. Ruskov _et al._ (2007) and Ruskov _et al._ (2009). For an interesting connection to of

the three-level intermittent dynamics to dynamical phase transitions, see Refs. Lesanovsky

_et al._ (2013) and Garrahan and Gu (2018).

**Remarks on the state evolution.** The evolution of the GD manifold Bloch vector

( _X_ GD ( _t_ catch ) _, Y_ GD ( _t_ catch ) _, Z_ GD ( _t_ catch ) ) conditioned on _no_ clicks, d _N_ ( _t_ catch ) =

0 , for duration  _t_ catch , is plotted in Fig. 3.1a. The partial tomogram visually shows that

the predicted evolution of the quantum jump from _|_ G __ to _|_ D __ is continuous and coherent,

_X_ GD 2 + _Y_ 2 GD + _Z_ GD 2 = 1 for all no-click times,  _t_ catch . The measurement record, d _N_ ,

and the predicted trajectory is identical for any two jumps from _|_ G __ to _|_ D __ . The time

axis has been scaled in units of the mean time, __ BG = ( 2 BG _/_ B ) __ 1 , between photon

detector clicks. This time can also be understood as the inverse of the information-gain

rate of the measurement about the G level. To expand on this, for definitiveness, consider

the situation where the atom is initialized in _|_ G __ , but this information is not shared with

the observer operating the photon detector. By measurement, how long does it take the

observer to statistically deduce that the atom is in _|_ G __ or not? The measurement drive


-----


3.1. Fluorescence monitored by photon counts 72

**a**

dN( _t_ )

1.0

0.5

0.0

-1.0

![Mivev_Thesis.pdf-88-0.png](Mivev_Thesis.pdf-88-0.png)

0 3 6 9 12 15

**b**

10 0

10 -1

10 -4

10 -5


10 -6


![Mivev_Thesis.pdf-88-1.png](Mivev_Thesis.pdf-88-1.png)

3 6 9 12 15

No-click time  _t_ catch ( __ BG )


**Figure 3.1** _|_ **Conditional no-click evolution of the jump from** _|_ G __ **to** _|_ D __ **: ideal**
**photodetection theory.** **a,** A typical quantum trajectory for a jump from _|_ G __ to
d _|_ D _N_ __ ( represented as the GD Bloch vector ( _t_ ) = 0 , for duration  _t_ catch . The Rabi drives are _X_ GD , _Y_ GD , _Z_  GD DG ), conditioned on = 10 __ 5 and  _no_ BG = 0 clicks, _._ 1
in units of the decay rate __ B . Time axis is scaled in units of the mean time between
detector clicks, __ BG = ( 2 BG _/_ B ) __ 1 . Time scale of the jump flight is the mid-flight time
 _t_ mid , defined by _Z_ GD = 0 . **b,** Log plot of the norm of the un-normalized no-click state,
 
__ ( _t_ catch ) __ ( _t_ catch ) , as a function of  _t_ catch , in units of __ BG . Parameters of the
 plot correspond to those of panel a.  




-----


3.1. Fluorescence monitored by photon counts 73

 BG is actuated and the observer monitors the detector for clicks. If the atom is in _|_ G __ _,_

on average, the detector records a click after time __ BG , and informs the observer that

the atom is definitively in _|_ G __ . Alternatively, if the atom was initialized in _|_ D __ _,_ no clicks

would be recorded. As the detector does not record a click for durations longer than __ BG ,

the observer becomes increasingly confident that the atom could not be in _|_ G __ since it

becomes exponentially unlikely that a click has not yet been observed, see Fig. 3.1b, and

the alternative conclusion, that the atom is in _|_ D __ , becomes increasingly likely. Although

this information-gain consideration is carried out from the point of view of the observer,

and with classical measurements would bear no consequence for the objective state of the

system, with quantum measurements the gain of information about the system by virtue of

a measurement is necessarily accompanied by a result-correlated state-disturbance (back-

action). In Hilbert space, the disturbance can be viewed as a _measurement-backaction_

_effective force_ , as discussed in the following subsection, Sec. 3.1.2.

**Probability of no-click record.** Fig. 3.1b shows a plot of the conditional no-click

state norm, __ __ ( _t_ catch ) _|_ __ ( _t_ catch ) __ , as a function of the no-click duration,  _t_ catch . The

norm initially decays exponentially with a time-constant __ BG , during which time, the atom

remains essentially in _|_ G __ , as indicated by the _Z_ GD Bloch component in panel a, which is

roughly equal to __ 1 . However, as the no-click duration approaches mid-flight time of the

jump,  _t_ catch __  _t_ mid , the decay of the norm slows down dramatically, since the atom

transitions from _|_ G __ to _|_ D __ , in which state one can stop expecting the rapid occurrence

of clicks. The quantum jump from _|_ G __ to _|_ D __ can be observed in the tomogram shown

in panel (a). For no-click duration  _t_ catch __  _t_ mid , the decay of the norm initially

appears flat, however, on longer time-scales (not shown) it is seen that it also follows an

exponential decay law with a much longer time constant, __ DG __ __ BG , corresponding to

the waiting-time for the jump back down, from _|_ D __ to _|_ G __ .


-----


3.1. Fluorescence monitored by photon counts 74

**Application of the photon counting model to the experiment.** The photon-

counting theory presented in this section provides the background to the experiment

along with a link to the original ion experiments. It captures a core set of the ideas,

even though the monitoring of _|_ B __ implemented in the experiment is diffusive  the op-

posite limit of the point-process description presented here, see Sec. 3.2. Nevertheless,

the photon-counting theory even provides a quantitative first approximation of the ex-

perimental results. For definitiveness, consider the flight of the quantum jump shown in

Fig. 1.3b. The measured mid-flight time,  _t_ mid = 3 _._ 95 __ s , is predicted, in a first approx-

imation, by Eq. (3.17). Using the (independently measured) values of the experimental

parameters, summarized in Table 5.1 (setting  BG equal to  B0 = 2 __ __ 1 _._ 2 MHz, the

BG drive when the atom is not in _|_ B __ ) and extracting the effective measurement rate of

_|_ B __ , __ B = 2 __ __ 9 _._ 0 MHz (which follows from Eq. (3.8) where  BG = 2 __ __ 1 _._ 01 MHz,

the average click rate on the BG transition), Eq. (3.17) predicts  _t_ mid __ 4 _._ 3 __ s  in

fair agreement with the observed value  _t_ mid = 3 _._ 95 __ s . The photodetection theory

presented in in Sec. 3.1.3 further improves the agreement. These calculations serve to

generally illustrate the theory and ideas of the experiment; the quantitative comparison

between theory and experiment is only presented in Sec. 5.5.

######### 3.1.2 ######### Measurement-backaction effective force in the absence

 of the Dark Rabi drive

While in Sec. 3.1.1 we considered the coherent dynamics of the three-level atom in the

presence of both unitary evolution, due to the Rabi drive  DG , and the competing non-

unitary state collapse, due to the measurement, in this subsection, we examine the simpler

case where only measurement dynamics are at play, i.e.,  DG = 0 . In this simpler situation,

some important features of the measurement, consisting of the Rabi drive  BG and the


-----


3.1. Fluorescence monitored by photon counts 75

monitoring of the B level at the rate __ B , are more easily discussed. In particular, we pay

attention to the notion of a _measurement-backaction effective force_ , the special force that

unavoidably disturbs of the quantum state due to the measurement.

For definitiveness, consider the situation where the three-level atom is prepared in an

initial superposition involving the G and D levels, _|_ __ (0) __ = _N_ ( _|_ G __ + __ _|_ D __ ) , where __ __ 1

and _N_ is the ket normalization factor; for simplicity, assume _|_ D __ is completely decoupled

form the environment, __ D = 0 . To measure the atom, only the Rabi drive  BG is turned

on. One of two qualitatively distinct measurement records is observed: either clicks are

recorded indefinitely or no clicks are ever recorded, which can qualitatively be understood

in view of the following considerations. When the BG drive is first turned on, some of

the initial population from the G level is transferred to the B level due to the steering

force of  BG . However, even as a tiny amount of population is deposited in _|_ B __ , the

strong coupling with the environment and the photodetector dampens the transfer and

quickly yields the detection of a click, with probability __ 1 (d _t_ ) = _c_  __ B _c_  B ( _t_ ) d _t_ , where
 

_c_  B = __ __ B _|_ G __ B _|_ is the jump operator. The click resets the atom to the ground state,

_|_ G __ . Once the atom is completely in _|_ G __ , the amplitude of _|_ D __ is zero, and since  DG = 0 ,

the atom can never transition to _|_ D __ subsequently. The remainder of the history proceeds

as described above, the atom remains predominantly in _|_ G __ and continues to fluoresce

though the partial excitation and subsequent relaxation of _|_ B __ , by means of  BG and

the detection, __ B , respectively. In this way, the Dehmelt electron scheme implements

a measurement with result _|_ G __ , occurring with an approximate probability 1 __ __ 2 . The

alternative set of trajectories, where no clicks are observed is quantitatively analyzed in

the following, and occur with approximate probability __ 2 .


-----


3.1. Fluorescence monitored by photon counts 76

**No-click trajectory.** The _normalized_ state of the three-level atom conditioned on no-

clicks, 1

_|_ __ _I_ =0 ( _t_ ) __ = _C_ G ( _t_ ) _|_ G __ + _C_ B ( _t_ ) _|_ B __ + _C_ D ( _t_ ) _|_ D __ _,_ (3.21)

evolves according to the non-linear Schrdinger equation, see Eq. (3.10),


d 1 1

d _t_ _|_ __ _I_ =0 ( _t_ ) __ = __ _i_ _H_  __ 2 _c_  __ B _c_  B + 2


_c_  __ B _c_  B ( _t_ ) __ _I_ =0 ( _t_ ) _,_ (3.22)
_|_ __


which in terms of the normalized state coefficients ( _C_ G _, C_ B , and _C_ D ) yields the set of

coupled non-linear equations,


d

_C_ B ( _t_ ) =1
d _t_ 2



__ B _C_ B ( _t_ ) 3 + 1
2 2



1

 BG _C_ G ( _t_ )
2 __ 2



__ B _C_ B ( _t_ ) _,_ (3.23)
2


d

_C_ G ( _t_ ) =1
d _t_ 2



__ B _C_ B ( _t_ ) 2 _C_ G ( _t_ ) 1
2 __ 2



 BG _C_ B ( _t_ ) _,_ (3.24)
2


d _C_ D ( _t_ ) =1 __ B _C_ B ( _t_ ) 2 _C_ D ( _t_ ) _,_ (3.25)

d _t_ 2


d

_C_ D ( _t_ ) =1
d _t_ 2


The measurement terms in Eqs. (3.23)-(3.25) associated with information gain are the

non-linear ones. As discussed in Sec. 2.3, they originate from the normalization term in

the conditional state update and give rise to non-unitary state dynamics, resulting in a

drastic departure from the usual Schrdinger equation. To analyze their effect and gain

some physical intuition, we introduce a graphical representation of the Hilbert space of

the three-level atom.

R **-qutrit sphere representation.** It follows from the real coefficients of Eqs. (3.23)-

(3.25) and the initial conditions that _C_ G _, C_ B _,_ and _C_ D are constrained to be real. Hence a

pure state of the atom admits a geometrical representation as a point on the unit sphere

defined by the state norm condition _C_ B 2 + _C_ G 2 + _C_ D 2 = 1 , see Fig. 3.2. We nickname

1 Notationally, we employ capital letters for the coefficients of the normalized sate, and lower-case
letters for those of the un-normalized state.


-----


3.1. Fluorescence monitored by photon counts 77

this representation the  R -qutrit sphere. Unlike the Bloch sphere representation where

orthogonal state vectors are represented by _antiparallel_ vectors, in the R -qutrit sphere

representation, orthogonal state vectors are actually represented by orthogonal vectors,

extending from the origin to the surface of the sphere. Notably, the sphere contains states

of the two-level sub-manifolds that are _not_ represented on the Bloch sphere, those with

a global phase. 2 The addition of the third level allows, in general, the observation of

the global phase because it can be measured relative to the phase of the third level. Con-

sequently, a Rabi rotation between two levels is no longer 2 __ periodic but 4 __ periodic.

Unitary evolution is represented by rotations on the sphere; for instance, the evolution

due to the Bright Rabi drive,  BG , is a rotation about the D axis, and the correspond-


ing infinitesimal-state-change vector field, d __ ( BG ) = 2 1 ( _C_ G B _C_ B G )  BG d _t_ , is
_|_ __ _|_ __ _|_ __

plotted on the surface of the sphere in Fig. 3.2. Note that the length of the vectors is

largest at the GB equator and approaches zero toward the D poles. The vector field repre-

sentation is useful in the analysis of the non-linear measurement-backaction effective force

due to the renormalization terms and we hope can provide a more intuitive understanding

of the interplay between the coherent Rabi and the stochastic measurement dynamics.

Before elaborating on the geometrical representation of the measurement dynamics, it is

useful to first algebraically solve Eqs. (3.23)-(3.25).

**Measurement-backaction force steers atom towards** _|_ D __ **.** Although there is no

Rabi drive or measurement directly applied to the Dark level, conditioned on not detecting

a click, according to Eq. (3.25), a force is nonetheless exerted by the B-level monitoring

that steers the atom toward the Dark level. Specifically, the rate of change of the D


level amplitude,


d d _t_ _C_ D , is given by an anti-damping term with a state-dependent rate


proportional to the B level population, _C_ B ( _t_ ) 2 , and measurement rate, __ B . Solving

2 The special unitary Lie group _SU_ (2) is not isomorphic to the special orthogonal Lie group _SO_ (3) ,
but is a double cover of it.


-----


![Mivev_Thesis.pdf-94-0.png](Mivev_Thesis.pdf-94-0.png)

![Mivev_Thesis.pdf-94-1.png](Mivev_Thesis.pdf-94-1.png)

_t_
_C_ D ( _t_ ) = _C_ D (0) exp

0




d _t_ __ 1 __ B _C_ B ( _t_ ) 2 _._ (3.26)

2



1
d _t_ __


In this sense, the renormalization of the conditional state amounts to a (non-unitary)

measurement-backaction force on _|_ D __ , which is linked to the population of _|_ B __ _._ To ex-

plicitly solve Eq. (3.26), we need to solve the remaining equations, Eqs. (3.23) and (3.24).

**Adiabatic elimination of the Bright state dynamics.** Because Eq. (3.23) is non-

linear, we consider the B level dynamics and their adiabatic elimination with greater care.


Eq. (3.23), contains both a damping, 1 2 __ B _C_ B , and an anti-damping, 1 2 __ B _C_ B3 , term.
__

These cancel out perfectly only if the atom is either entirely in _|_ B __ , _C_ B = __ 1 , or not

at all in _|_ B __ , _C_ B = 0 ; otherwise, _|_ _C_ B _|_ _<_ 1 , the damping dominates, steering _C_ B in


-----


3.1. Fluorescence monitored by photon counts 79

the direction of zero. In the extreme case, where  BG = 0 , one can explicitly solve the


B level dynamics, _C_ B ( _t_ ) 2 = 1 + _C_ B (0) __ 2 __ 1 exp ( __ B _t_ ) __ 1 _,_ which for small initial

2 1
populations, _C_ B (0) 1 rapidly decays to a stable zero equilibrium at a rate     2 __ B ,
__


_C_ B ( _t_ ) _C_ B (0) exp 2 1 __ B _t_ . Since __ B is the fastest timescale in the problem and the
__ __


B dynamics are convergent, we can adiabatically eliminate _C_ B by setting


d d _t_ _C_ B ( _t_ ) = 0 ;


solving the cubic equation, one finds three solution branches,



 2 __ BG B _C_ G ( _t_ ) + ( BG _/_ B ) 2

_O_
 2 


1  BG

2 __ B

__ __



 2 __ BG B _C_ G ( _t_ ) + ( BG _/_ B ) 2

_O_
 3 



_C_ B ( _t_ ) =


1  BG

2 __ B

__


(3.27)


__ BG B _C_ G ( _t_ ) + ( BG _/_ B ) 3

_O_
 


 BG


Operating the three-level atom in the limit where the _|_ B __ level is never appreciably popu-



  BG
lated, we employ the third solution branch, _C_ B ( _t_ ) = __ B _C_ G ( _t_ ) , in Eq. (3.24) to find the

effective equation of motion for the G level dynamics,

d _C_ G ( _t_ ) = __ __ BG 1 1 _C_ G ( _t_ ) 2 _C_ G ( _t_ ) _,_ (3.28)

d _t_ __ __
 

which are now completely decoupled from the other levels. In Eq. (3.28), we identify a

damping and an anti-damping term with a constant and G-population dependent, _C_ G 2 ,

rate, respectively. The scale of both terms is given by the parameter __ BG __ 1 =  2 BG _/_ 2 __ B ,

which is the expected rate of clicks when the atom is in _|_ G __ . By eliminating the B level,

we have obtained an explicit relation for the effective monitoring of the G level, which

occurs at a rate __ BG __ 1 , which can also be interpreted as the quantum Zeno rate (Misra and

Sudarshan, 1977, Gambetta _et al._ , 2008, Matsuzaki _et al._ , 2010, Vijay _et al._ , 2011, Slichter

_et al._ , 2016, Harrington _et al._ , 2017, Hacohen-Gourgy _et al._ , 2018). The numerator  2 BG

is proportional to the population transfer rate from _|_ G __ to _|_ B __ while the denominator


-----


3.1. Fluorescence monitored by photon counts 80

dN( _t_ )

1.0

0.0

-0.5

-1.0

![Mivev_Thesis.pdf-96-0.png](Mivev_Thesis.pdf-96-0.png)

0 2 4 6 8

########## No-click time ########## t ########## ( ##########  ########## BG ########## )

**Figure 3.3** _|_ **Adiabatic solution for the no-click GD manifold trajectory of a**
**superposition state measured with**  DG = 0 **.** Adiabatic-approximation (solid lines)
and numerical (dashed lines) solution for the partial tomogram of the GD manifold of the
no-click quantum trajectory of an initial superposition state where __ = 0 _._ 1 and = (1 + __ 2 ) __ 1 _/_ 2 . The Bright Rabi drive is _|_ __ (0)  BG __ = = 0 _N_ ( _._ 1 _|_ G , in units of __ + __ _|_ D __ ) ,
the decay rate __ B . Time axis scaled in units of _N_ __ BG = ( 2 BG _/_ BG ) __ 1 _._

__ B gives the rate of projection from _|_ B __ to _|_ G __ . Solving Eq. (3.28) and substituting its

solution in Eq. (3.26), one finds


_C_ G ( _t_ ) 2 = _p_ G


_p_ G + (1 __ G _p_ G ) _e_ 2 _t/_ BG _,_ (3.29)


_C_ D ( _t_ ) 2 = _p_ D _e_ _t/_ BG


_p_ D + (1 D __ _p_ D ) _e_ 2 _t/_ BG _,_ (3.30)


where _p_ G __ _C_ G (0) 2 and _p_ D __ _C_ D (0) 2 are the initial conditions. Note, for _p_ D = 0 , the

above solution for _C_ D is always zero. The evolution of the GD Bloch vector conditioned

on no clicks for the initial state _|_ __ (0) __ = _N_ ( _|_ G __ + __ _|_ D __ ) is obtained by substituting


-----


3.1. Fluorescence monitored by photon counts 81

Eq. (3.29) and (3.30) in Eqs. (3.11)-(3.13),

Z GD ( _t_ ) = tanh [ _t/_ BG + arctanh [Z GD (0)]] _,_ (3.31)

X GD ( _t_ ) = sech [ _t/_ BG + arctanh [Z GD (0)]] _,_ (3.32)

Y GD ( _t_ ) = 0 _._ (3.33)

We note that a few results of this subsection, especially Eqs. (3.31)-(3.33), bear resem-

blance to results from Sec. 3.1.1, yet we stress that the two situations are fundamentally

distinct, and the resemblance must be considered with care. For instance, we note that

the mid-flight time  _t_ mid cannot be recovered from the simpler situation considered here,

where no quantum jumps occur and there is no competition between unitary dynamics

due to  DG and the measurement.

In Fig. 3.3a, we plot the adiabatic-approximation solution to the non-linear Schrdinger

evolution, Eq. (3.22), for the GD manifold Bloch vector conditioned on no clicks, Eqs. (3.31)-

(3.33), obtained in the limit  BG __ __ _B_ . Overlaid (dashed lines) is the corresponding

numerically calculated solution to Eq. (3.22). Even for modest separation of timescales,

 BG _/_ B = 0 _._ 1 in the plot, the two solutions appear nearly indistinguishable. The initial

atom state, __ = 0 _._ 1 , is gradually projected to _|_ D __ on a timescale given by __ BG and evolves

in a characteristically non-unitary manner. Notably, the state remains pure at all times,

and in the limit _t_ __ __ BG remains essentially in _|_ D __ , indefinitely. Importantly, for times _t_

on the other of __ BG , the projection can (but need not) be interrupted by the detection of

a click, which would project the state to _|_ G __ , and occurs with total probability __ 1 __ __ 2 .

**Hilbert space representation of the measurement dynamics.** It is useful to con-

sider a geometric representation of the measurement dynamics and in particular of the

non-linear measurement-backaction force. For simplicity, first consider the measurement


-----


3.1. Fluorescence monitored by photon counts 82


Norm




![Mivev_Thesis.pdf-98-0.png](Mivev_Thesis.pdf-98-0.png)

1.0

0.5

0.0

-0.5

-1.0

|G || G|
|---|---|
|||
|D ||B  | |
|||

|Max  G |   =0 I  ||Col2| G|
|---|---|---|
|1.0 0.5 B D |  |  0.0 -0.5 -1.0|||
|1.0 0.5 0.0 -0.5 -1.0|||
||B D |  | ||
||||


-1.0 -0.5 0.0 0.5 1.0


_|_ B __ _|_ D __

-1.0 -0.5 0.0 0.5 1.0


**Figure** **3.4** _|_
**Geometrical representation of the no-click measurementbackaction force for**  BG = 0 **.** Shown are two projections of R -qutrit sphere overlaid
with the measurement-force vector field, d __ _I_ =0 , due to the monitoring of the B level


with the measurement-force vector field, d d _t_ __ _I_ =0 , due to the monitoring of the B level

_|_ __
with  BG = 0 . Color of density plot indicates the relative magnitude of the change,
Norm d d _t_ __ _I_ =0 .

_|_ __

 


d d _t_ __ _I_ =0

_|_ __


=0


-----


3.1. Fluorescence monitored by photon counts 83

force due only to the monitoring of the B level, in the absence of the Bright Rabi drive,

 BG = 0 . This force can be represented as a vector field on the surface of the R -qutrit

sphere, see Fig. 3.4. The vector field is calculated from Eqs. (3.31)-(3.33) for the change

in the state conditioned on detecting no clicks,


_C_ B 1
__

_C_ G


d

__ _I_ =0 = 1 __ B _C_ B
d _t_ _|_ __ 2


d

__ _I_ =0 = 1
d _t_ _|_ __ 2


(3.34)


_C_ D


The colormap in Fig. 3.4 depicts the relative magnitude of the change, Norm d d

which we note is only zero in two special cases: i) when the atom is B 


which we note is only zero in two special cases: i) when the atom is _ |_ B __ , corresponding


d d _t_ __ _I_ =0

_|_ __


to the points ( __ 1 _,_ 0 _,_ 0) _,_ and ii) when the atom is in a state involving exclusively _|_ G __ and

_|_ D __ but not _|_ B __ . The latter is special in that it corresponds to an entire manifold of states,

the GD equatorial circle, which can be visually recognized in Fig. 3.4 as the dark vertical

stripe at the center of the left panel and the dark circular perimeter of the disk in the

right panel. All other states, not covered under the latter two cases, are superpositions

involving _|_ B __ . From the vector field plot, it is evident that these states are guided by the

force away from the _|_ B __ poles and toward the GD equator. It is precisely this feature of

the measurement force that results in the gradual projection of the state conditioned on

no clicks  it is the unavoidable disturbance of the atom due to the information-gain of

the no-click measurement outcomes, which lead the observer to gradually learn that the

atom is not in _|_ D __ , thus resulting in the increased likelihood that it is in _|_ G __ or _|_ D __ . This

dynamics embody the message of the Chapter 2 epigraph, In quantum physics you dont

see what you get, you get what you see.

In Fig. 3.5, we plot the measurement vector field in the presence of the Bright Rabi


-----


3.1. Fluorescence monitored by photon counts 84


Norm




![Mivev_Thesis.pdf-100-0.png](Mivev_Thesis.pdf-100-0.png)

1.0

0.5

0.0

-0.5

-1.0

|G |  || G|
|---|---|
|||
|D | |B | |
|||

|Max  G |   =0 I  ||Col2| G|
|---|---|---|
|1.0 0.5 B |  0.0 -0.5 -1.0|||
|1.0 0.5 0.0 -0.5 -1.0|||
||B | ||
||||


-1.0 -0.5 0.0 0.5 1.0


_|_ D __

-1.0 -0.5 0.0 0.5 1.0


**Figure 3.5** _|_ **Geometrical representation of the measurement-backaction force**
**and a no-click trajectory with**  BG = 0 _._ 1 __ B **.** Two projections of the R -qutrit sphere
overlaid with the measurement-force vector field d __ _I_ =0 (blue arrows) and the path of


overlaid with the measurement-force vector field d d _t_ __ _I_ =0 (blue arrows) and the path of

_|_ __
the quantum trajectory from Fig. (3.3) (red arrows), depicting the gradual projection of
a superposition state to magnitude, Norm d d _t_ __ _|_ _I_ =0 D __ conditioned on no clicks. Density plot indicates relative field .

_|_ __

 


d d _t_ __ _I_ =0

_|_ __


=0


-----


3.1. Fluorescence monitored by photon counts 85

drive  BG ,


_C_ B 1
__

_C_ G


_C_ G


d

__ _I_ =0 = 1 __ B _C_ B
d _t_ _|_ __ 2


d

__ _I_ =0 = 1
d _t_ _|_ __ 2



1
+  BG

2


+ 1


_C_ B
__


(3.35)


_C_ D 0


with  BG = 0 _._ 1 __ B . The Bright Rabi drive, visually represented on the R -qutrit sphere in

Fig. 3.2, perturbs the measurement field, shown in Fig. 3.4, by linking the B and G levels

and lifting the degeneracy of the measurement, represented in GD equator. Visually, this is

evident in the tilt of the vertical dark stripe in the center of the left-panel colormap. In the

right panel, it is also evident that _|_ B __ is no longer an equilibrium point; the equilibrium has

been shifted in the direction of _|_ G __ by an amount proportional  BG _/_ B _,_ see Eq. (3.27),

and made metastable. The red arrows depict the path of the quantum trajectory in Hilbert

of the gradual projection of an initial superposition state of _|_ G __ and _|_ D __ , for the same

parameters as employed in Fig. (3.3), where __ = 0 _._ 1 . Initially, the state is quickly steered

in the direction of _|_ B __ by the force of  BG . However, as the state moves in the direction of

_|_ B __ , the motion is quickly opposed by the no-click measurement-backaction force, which

grows larger in amplitude in this direction. The two forces do not precisely cancel each

other out, because of the slight mismatch in angles. The net force, albeit small, steers

the atom towards the GD equator and with a slight tilt toward _|_ D __ . The opposition of the

 BG drive and the measurement back-action trap the state in the ridge where the two

forces nearly cancel each other out, the nearly vertical dark stripe in the left panel, and

the small angular mismatch slowly carries the state in the direction of _|_ D __ , an equilibirum

point, where all forces are zero.


-----


3.1. Fluorescence monitored by photon counts 86

######### 3.1.3 ######### Incoherent Bright drive and Dark drive off

In this section, we consider the case of quantum jumps in the three-level atom subject to

photodetection and an incoherent Bright drive, rather than a Rabi one, see Sec. 3.1.1. The

situation analyzed in this section is somewhat more analogous to the cQED experiment

where the Bright Rabi drive consists of a bi-chromatic tone that unconditionally addresses

the BG transition, independent of the population of the readout cavity, necessitated by

the dispersive pull of the readout cavity on the BG frequency. The bi-chromatic drive

effectively acts as an incoherent drive. The incoherent Bright drive photodetection theory

presented here sheds some further light on the dynamics of the quantum jump from _|_ G __


to _|_ D __ . Features such as the non-zero coherence, _X_ GD , and in the limit  _t_ catch __  _t_ mid

are discussed. 3

Replacing the coherent Rabi drive  BG by an incoherent drive  BG in the master

equation of the three-level atom in the interaction picture, Eq. (3.1) becomes


d __ = ( _i_  ) __ 1 [  _H_ drive _, _ ] +  BG [ B G ] __ + ( __ B +  BG ) [ G B ] __ + __ D [ G D ] _,_

d _t_ _D_ _|_ __ _|_ _D_ _|_ __ _|_ _D_ _|_ __ _|_

(3.36)

and Eq. (3.5) becomes


  DG
_H_ drive = _i_ 


_|_ D __ G _| |_ G __ D _|_ _._ (3.37)


The strong-monitoring assumption, __ BG __ 1 __ B , is also carried over from Sec. 3.1.1 by

__

assuming  BG __ __ B , i.e., the time between clicks in fluorescence is essentially the same


The strong-monitoring assumption, __ BG __ 1 __ B , is also carried over from Sec. 3.1.1 by

__


as the time separating photon absorptions from the incoherent drive, as absorption is


rapidly followed by fluorescence ( __ B +  BG __  BG ). This brings a useful simplification,

3 The following derivation is due to H.J. Carmichael and R. Gutierrez-Jauregui.


-----


3.1. Fluorescence monitored by photon counts 87

since, following each reset to _|_ G __ , the unnormalized state evolves in the GD-subspace,



D 

D D __ _,_ (3.38)
2 _|_ __ _|_
 






d __

  BG

_i_  = _H_ drive _i_ 

d _t_ catch __ 2

 





d __
_i_ 

d _t_






__ D
G G _i_ 
_|_ __ _| _ 2


thus replacing Eqs. (3.7) and (3.15) by the simpler 2 __ 2 system


_c_ G

_c_


 BG  DG
__ __

 DG __ D
__


_c_ G

_c_


= 1

2





_,_ (3.39)




d _t_ catch


and, in the limit __ D __  BG , the equation of motion for _W_ DG , defined in Eq. (3.14), is


d _W_ DG  BG

=
d _t_ catch 2


d _W_ DG



BG DG

_W_ DG + 
2 2



DG (1 + _W_ 2 DG ) _,_ (3.40)

2


with solution, for _W_ DG (0) = 0 ,


exp [( _V_ _V_ __ 1 ) DG  _t_ catch _/_ 2] 1
_W_ DG ( _t_ catch ) = _V_ __ _V_ __ 1 exp [( __ _V_ __ _V_ __ 1 ) DG  _t_ catch __ _/_ 2] _,_ (3.41)


where


 BG

 DG




2
__ 1 _._ (3.42)




1
_V_ =


 BG

 DG


In Ref. Ruskov _et al._ (2007), a general form of the Bloch vector equations for arbitrary

amplitude of the Rabi drive was found. Inversion of the condition _W_ DG ( _t_ mid ) = 1 gives

the characteristic time scale


 _t_ mid = 2 ( _V_ __ _V_ __ 1 ) DG __ 1 ln _V_ _V_ __ + 1 1 + 1

 


(3.43)


Although Eqs. (3.41) and (3.43) replace Eqs. (3.16) and (3.17), under strong monitoring,

 BG  DG , they revert to the latter with the substitution  2 BG _/_ 2 __ B  BG _/_ 2 ,; in
__ __


-----


3.1. Fluorescence monitored by photon counts 88

this way, Eqs. (3.11)(3.13) are recovered with the same substitution. More generally,

_W_ DG ( _t_ catch ) goes to infinity at finite  _t_ catch , changes sign, and returns from infinity

to settle on the steady value _W_ DG ( __ ) = __ _V_ . The singular behavior marks a trajectory

passing through the north pole of Bloch sphere. It yields the long-time solution


Z GD ( ) =
__


 DG
1 4
__  BG



2

 DG
_,_ X GD ( ) = 2 _,_ Y GD ( ) = 0 _,_ (3.44)
__ __  BG __



2

 DG
_,_ X GD ( ) = 2
__ __  BG



in contrast to the perfect jump of Eqs. (3.18)(3.20). The long-term coherence and

lower-than-one value of Z were observed in the experiments, see Fig. 1.3b. They can be

understood as the equilibrium point of the coherent Rabi drive  DG attempting to rotate

the state from _|_ D __ back to _|_ G __ perfectly balanced against the measurement-backaction

force of the no-click measurement steering the atom toward _|_ D __ , recall discussion of the

measurement vector field, see Figs. 3.4 and 3.5.

**Dark drive off.** Turing the Dark drive off shortly after a click demonstrates the con-

nection between the flight of a quantum jump and a projective measurement. From the

point of view of the trajectory equations, the only change is the setting of  DG to zero at

time  _t_ on on the right-hand side of Eqs. (3.15) and (3.40). Subsequently, _W_ DG ( _t_ catch )

continues its exponential growth at rate  2 BG _/_ 2 __ _B_ [Eq. (3.15)] or  BG _/_ 2 [Eq. (3.40)].

Equations (3.11)(3.13) for the GD Bloch components still hold, but now with


 _t_ mid =  2 BG _,_  BG

2 __ _B_ 2




__ 1
ln _W_ DG __ 2 ( _t_ on ) _._ (3.45)

 


which can provide an estimate of  _t_ __ mid , specifying the time at which _Z_ GD = 0 .

The evolution during  _t_ off , in the absence of  DG , in effect realizes a projective

measurement of whether the state of the atom is _|_ G __ or _|_ D __ , similar to the one analyzed


-----


3.1. Fluorescence monitored by photon counts 89

in Sec. 3.1.2, where the normalized state at  _t_ on is


__ ( _t_ on )
_|_ __


( _t_ on ) _c_ G ( _t_ on ) G + _c_ D ( _t_ on ) D
__ = _|_ __ _|_ __

( _t_ on ) ( _t_ on )
_N_ _N_



D on

_,_ (3.46)
( _t_ on )
_N_


with ( _t_ on ) = _c_ 2 G ( _t_ on )+ _c_ 2 D ( _t_ on ) the probability for the jump to reach  _t_ catch =  _t_ on
_N_

after a click reset to _|_ G __ at  _t_ catch = 0 . The probability for the jump to continue to

 _t_ catch _>_  _t_ on (given  _t_ on is reached) is then


( _t_ catch ) = _C_ D 2 ( _t_ on )

( _t_ on ) ( _t_ on
_N_ _N_



_C_ D 2 ( _t_ on ) G 2 ( _t_ on )

+ _C_
( _t_ on ) ( _t_ on
_N_ _N_


G 2 ( _t_ on ) exp  2 BG

( _t_ on ) __ __ B
_N_  


( _t_ catch )
_N_


BG _,_  BG

__ B


 _t_ catch


(3.47)


**Completed and aborted evolutions of the jump transition.** In this simple model,

the probability for the trajectory to complete  for the measurement to yield the result

_|_ D __  is obtained in the limit  _t_ catch __ , and, as expected, is equal to the probability

to occupy the state _|_ D __ at time  _t_ on ; i.e., the completion probability is _P_ D ( _t_ on ) =

_C_ D 2 ( _t_ on ) _/_ Norm( _t_ on ) . It is helpful to illustrate this idea with an example. Consider the

catch experiment of Fig. 1.3b in the absence of the Dark Rabi drive,  DG . From _Z_ GD , we

can estimate that out of all the trajectories that pass though the  _t_ on mark approximately

_P_ D ( _t_ on ) = (1 + _Z_ GD ( _t_ on )) _/_ 2 __ 8% fully complete without an interruption. On

the other hand, for those that pass the  _t_ __ mid mark, approximately 50% complete. It

follows from Eq. (3.47), that the probability of the evolution to complete increases the

further along the trajectory is. Although some of the jump evolutions abort at random,

importantly, every single jump evolution that completes, and is thus recorded as a jump,

follows _not_ a random but an identical path in Hilbert space, i.e., a deterministic one.

This path (of _any_ jump) is determined by Eq. (3.41), or, in the simpler model, by the

Eqs. (3.18)-(3.20) for the components of the GD Bloch vector.


-----


3.2. Heterodyne monitoring of readout cavity coupled to three-level atom 90

###### 3.2 ###### Heterodyne monitoring of readout cavity cou-

 pled to three-level atom

######### 3.2.1 ######### Description of cQED experiment

In Chapter 1, we described the cQED experiment involving a superconducting atom with

the necessary V-shape level structure (see Fig. 1.1a or Sec. 4.1) subject to heterodyne

monitoring of _|_ B __ by means a dispersively coupled readout cavity. The three-level atom

is formed form two heavily hybridized transmon modes, which are coupled by means of a

cross-Kerr interaction to the readout cavity in an asymmetric way, __ BC __ __ DC . In the

following, we present the quantum trajectory description of the heterodyne monitoring,

including imperfections.

**System Hamiltonian.** In the lab frame, the Hamiltonian of the system is, see also

Sec. 4.1,

   
_H_ lab = _H_ 0 + _H_ _I_ + _H_ _d_ ( _t_ ) _,_ (3.48)

where the Hamiltonian of the uncoupled three-level atom and cavity, is

_H_  0 =  __ DG _|_ D __ D _|_ +  __ BG _|_ B __ B _|_ +  __ _C_ _c_  __ _c ,_  (3.49)

where __ DG , __ BG , __ C are the Dark, Bright, and cavity mode frequency, respectively,  _c_ is

the cavity amplitude operator, the atom-cavity interaction Hamiltonian is

_H_  _I_ =  _c_ __ _c_  [  __ B _|_ B __ B _|_ +  __ D _|_ D __ D _|_ ] _,_ (3.50)


-----


3.2. Heterodyne monitoring of readout cavity coupled to three-level atom 91

where the shift of the cavity frequency conditioned on _|_ B __ ( _|_ D __ ) is __ B ( __ D ), and the

Hamiltonian of the atom Rabi drives and readout probe tone is



_i_ 

_H_ _d_ ( _t_ ) =
__ 2



_i_ ( __ C + R ) _t_ _i_ ( __ DG + DG ) _t_
_n_  _ce_  +  __ DG _e_ G D

_|_ __



_i_ BG _t_ _i_ ( __ BG + B1 ) _t_
+ __ B0 _e_ G B +  __ B1 _e_ G B + H _._ c _._ _,_ (3.51)

_|_ __ _|_ _|_ __ _|_


where  _n_ is the steady state number of photons in the cavity when driven resonantly,

 R ,  DG _,_ and  B1 are the drive detunings from the bare mode frequencies. The first

Bright Rabi tone,  B0 , addresses the Bright transition when the cavity is unpopulated,

while the second tone,  B0 , addresses the BG transition when the cavity is populated, see

frequency spectrum in Fig. 1.1c. Moving to the rotating frame at the drive frequencies,

defined by the ket transformation _|_ __ ( _t_ ) __ = _U_ ( _t_ ) _|_ __ lab ( _t_ ) __ , where _U_ ( _t_ ) = exp ( _u_ ( _t_ ) _/i_  )

and _u_ ( _t_ ) =  _t_ ( __ C +  R ) _a_ __ _a_ + __ BG _|_ B __ B _|_ + ( __ DG +  DG ) _|_ D __ D _|_ , the Hamiltonian

in the rotating frame is  

  
_H_ ( _t_ ) = _H_ R + _H_ drive ( _t_ ) _,_ (3.52)


where _H_ R is a time-independent Hamiltonian,



__
_H_  R =   R _c_  __ _c_  + _i_ 
__ 2


_n_  ( _c_ __ __ _c_  ) +  __ B _|_ B __ B _|_ + __ D _|_ D __ D _|_ _c_  __ _c,_  (3.53)




and _H_ drive is the time-dependent Hamiltonian of the atom Rabi drives,


  BG ( _t_
_H_ drive ( _t_ ) = _i_ 

2




B G  __ BG ( _t_ )
_|_ __ _| _ 2



 DG
G B + _i_ 
_|_ __ _|_ 2


( _|_ D __ G _| |_ G __ D _|_ ) _._

(3.54)


The bi-chromatic drive, which unselectively addresses the BG transition,  BG ( _t_ ) =  B0 +

 B1 exp( __ _i_  B1 _t_ ) replaces the Rabi drive  BG of Eq. (3.2).


-----


3.2. Heterodyne monitoring of readout cavity coupled to three-level atom 92

**Measurement record.** The readout cavity input-output coupling is given by the jump

operator __ __ _c_  . It follows from Eq. (2.64) that the heterodyne measurement-record incre-

ment is

d _J_ het ( _t_ ) = __ __ __ _c_  __ ( _t_ ) d _t_ + d _Z_ ( _t_ ) _,_ (3.55)

where d _Z_ is a complex Wiener increment, see discussion below Eq. (2.60), and __ is the

quantum efficiency of the readout and amplification chain. The record, d _J_ het ( _t_ ) , is scaled

 to units of (readout cavity photon number) 1 _/_ 2  and filtered to generate the simulated

quadratures _I_ rec and _Q_ rec of the measurement record:


__ 1 _/_ 2
Re(d _J_ het ) _,_ (3.56)





__ filter
_dI_ rec =
__ 2

__ filter
_dQ_ rec =
__ 2



__
_I_ rec _dt_ __
__ 2


__ 1 _/_ 2
Im(d _J_ het ) _,_ (3.57)





__
_Q_ rec _dt_ __
__ 2


where __ filter is the bandwidth of the amplifier chain. In practice, it is assured that __ filter

is the fastest rate in the problem, __ filter __ __ , so that its effect is largely negligible.

######### 3.2.2 ######### Simulation of Stochastic Schrdinger equation (SSE)

The quantum trajectory unraveling monitors the reflected probe with efficiency __ and ac-

counts for residual photon loss through random jumps. It follows that the linear stochastic

Schrdinger equation combines a continuous evolution (heterodyne readout channel),


1
d __ ( _t_ ) =
_|_ __ _i_ 




__
_H_  drive + _H_  R __ _i_  2 _c_  __ _c_  d _t_ + __ __ d _J_ het __ ( _t_ )  _c_ _|_ __ ( _t_ ) __ _,_ (3.58)



__
 
_H_ drive + _H_ R __ _i_ 


with the point-like process (photon loss),


_c_  __ _c_  __

_._ (3.59)
__ __
__  _|_  __ 

 


_|_ __ __ _c_  _|_ __ __ at rate (1 __ __ ) __


-----


3.2. Heterodyne monitoring of readout cavity coupled to three-level atom 93

Note that for perfect quantum efficiency, __ = 1 , the rate of the photon loss channel goes

to zero. We emphasize that expectation values are performed over the normalized state;

importantly, when calculating the measurement record increment d _J_ het __ ( _t_ ) , see Eq. (3.55),

__ _c_  __ ( _t_ ) = __ __ ( _t_ ) _|_ _c_  _|_ __ ( _t_ ) __ _/_ __ __ ( _t_ ) _|_ __ ( _t_ ) __ _._

**Independently measured imperfections.** To more realistically model the cQED ex-

periment, we need to account for the small experimental non-idealities associated with

the device performance; namely, the finite energy relaxation lifetime of the levels ( _T_ 1 ), the

finite dephasing time of the levels ( _T_ 2 __ ), which is generally smaller than the bound imposed

by the lifetime, _T_ 2 __ _< T_ 1 , and the finite temperature of the device ( _n_ th ). Specifically, we

supplement the stochastic Schrdinger equation by spontaneous and thermal jumps on

both the G to B and G to D transitions ( _n_ B th and _n_ D th ) and by pure dephasing of
_|_ __ _|_ __ _|_ __ _|_ __

the GB and GD coherences ( __ B __ and __ D __ ). With these processes included, the term


__ B
__ _i_ 



B ( _n_ B th + 1) + __ B __ B B + __ D

2 _|_ __ _|_ 2
 


D ( _n_ D th + 1) + __ D __ D D + __ B _n_ B th + __ D _n_ D th

2 _|_ __ _|_ 2


_| |_ G __ G _|_



  __
is added to the non-Hermitian Hamiltonian, _H_ drive + _H_ R _i_  2 _c_  __ _c_  , on the right-hand side
__



  __
is added to the non-Hermitian Hamiltonian, _H_ drive + _H_ R _i_  2
__


of Eq. (3.58), with the additional three point-processes:


_|_ __ _|_ G __ at rate __ B ( _n_ B th + 1) __ __ _|_ B __ __ __ B _|_ __ __


__ B __ __ _|_ __ B __ _|_ __ __ + __ D ( _n_ D th + 1) __ __ _|_ __ D __ __ _|_ __ D __ _|_ __


_,_ (3.60)
__ __ _|_ __ __


_|_ __ _|_ B __ at rate __ B _n_ B th __ __ _|_ G __ __ __ G _|_ __ __


__ G __ __ _|_ __ G __ _|_ __ __ + 2 __ B __ __ __ _|_ __ B __ __ _|_ __ B __ _|_ __ __


_,_ (3.61)
__ __ _|_ __ __


_|_ __ _|_ D __ at rate __ D _n_ D th __ __ _|_ G __ __ __ G _|_ __


__ G __ __ _|_ __ G __ _|_ __ __ + 2 __ D __ __ __ _|_ __ D __ __ _|_ __ D __ _|_ __ __


_._ (3.62)
__ __ _|_ __ __


In the simulation, the parameters __ B _,_ D , _n_ th B _,_ D , and __ B __ _,_ D are mapped to the independently

measured parameters _T_ B 1 _,_ D , _n_ G th _,_ D , and _T_ B 2R _,_ D listed in Table 5.1.


-----


3.2. Heterodyne monitoring of readout cavity coupled to three-level atom 94

**Leakage from the** **_GBD_** **-manifold.** Because the three-level atom is realized from

two transmon qubits, the three-state manifold, _{|_ G __ _,_ _|_ B __ _,_ _|_ D _}_ , is not strictly closed, and

transitions to higher excited states are sometimes observed. This imperfection is modeled

in the SSE simulation with the addition of the further term


__ FG
_i_ 
__ 2



FG FD

G G + __
2 _|_ __ _|_ 2



FD D D + __ GF + __ DF

2 _|_ __ _|_ 2


_|_ F __ F _|_


to the non-Hermitian Hamiltonian, and the associated additional random jumps,


__ G G __
__ F at rate __ FG __ _|_ __ _|_ __
_|_ _|_ __ __ __


G G __ __ D D __
__ _|_ __ + __ FD __ _|_ __ _|_ __

__ __ _|_ __ __ __ __ _|_ __ __


_,_ (3.63)
__ __ _|_ __ __


__ F F __
__ G at rate __ GF __ _|_ __ _|_
_|_ _|_ __ __ __


_,_ (3.64)
__ __ _|_ __ __


__ F F __
__ D at rate __ DF __ _|_ __ _|_ __
_|_ _|_ __ __ __


_,_ (3.65)
__ __ _|_ __ __


where _|_ F __ models the all higher level by a single catch-all higher excited state. The results

of the simulation are presented in Sec. 5.5.


-----


### Experimental methods

If I knew what I was doing, it
wouldnt be called research.

Albert Einstein
See Hawken _et al._ (2010)

he design of the superconducting three-level atom and readout cavity is presented

in Sec. 4.1. It was optimized subject to the constrains of the experiment (Hamil-

## T

tonian and dissipative) with the energy-participation ratio (EPR) approach, presented in

Sec. 4.1.1. The methodology of the finite-element numerical simulations employed to

engineer the electromagnetic (EM) properties of the distributed circuit is presented in

Secs. 4.1.2 and 4.1.3. Sample fabrication is discussed in Sec. 4.2, while design and as-

sembly of the sample holder are discussed in Sec. 4.3. Particular attention is paid to

material selection, a care continued in Sec. 4.4, where aspects of the cryogenic setup of

the experiment are discussed, including sample thermalization, surface preparation, light-

tightness, and magnetic shielding. The microwave setup of the experiment is discussed in

Sec. 4.5. For further information on experimental methods employed in circuit quantum

electrodynamics (cQED) experiments see Refs. Geerlings (2013), Reed (2013), Reagor

95


-----


4.1. Sample design 96

(2016), Brecht (2017).

###### 4.1 ###### Sample design

**Overview.** The superconducting artificial atom presented in Sec. 1.1, see Fig. 4.1a,

consists of two coupled transmon qubits (Koch _et al._ , 2007, Schreier _et al._ , 2008, Paik

_et al._ , 2011) fabricated on a 2.9 mm-by-7 mm double-side-polished c-plane sapphire wafer

with the Al/AlO x /Al bridge-free electron-beam lithography technique (Lecocq _et al._ , 2011,

Rigetti, 2009); for fabrication methodology, see Sec. 4.2. The first transmon (B) is

aligned with the electric field of the fundamental TE 101 mode of the aluminum rectangular

cavity (alloy 6061; dimensions: 5.08 mm by 35.5 mm by 17.8 mm), while the second

transmon (D) is oriented perpendicular to the first and positioned 170 __ m adjacent to it,

see Fig. 4.1b. The inductance of the Josephson junction of each transmon (nominally,

9 nH for both B and D), the placement and dimensions of each transmon, and the

geometry of the cavity were designed and optimized using finite-element electromagnetic

analysis and the energy-participation-ratio (EPR) method 1 , as discussed in Sec. 4.1.1.

**Hamiltonian and level diagram.** Under the rotating-wave approximation and in the

low-excitation limit, see Sec. 4.1.3, the effective Hamiltonian of the device, consisting of

the Dark, Bright, and cavity modes, is energy conserving,


_H/_  = __ D _n_  D +  __ B _n_  B +  __ C _n_  C



1
__ 2



1 1

__ D _n_  D _n_  D  1
2 __ __ 2



__ B _n_  B _n_  B  1
2 __


+ __ DB _n_  D _n_  B + __ DC _n_  D _n_  C + __ BC _n_  B _n_  C _,_ (4.1)

1 Z.K. Minev _et al._ , in preparation.


-----


4.1. Sample design 97

|a|b|
|---|---|
|||
|15 mm I-O coupler Al cavity||


![Mivev_Thesis.pdf-113-0.png](Mivev_Thesis.pdf-113-0.png)

![Mivev_Thesis.pdf-113-4.png](Mivev_Thesis.pdf-113-4.png)

![Mivev_Thesis.pdf-113-3.png](Mivev_Thesis.pdf-113-3.png)

![Mivev_Thesis.pdf-113-1.png](Mivev_Thesis.pdf-113-1.png)

![Mivev_Thesis.pdf-113-2.png](Mivev_Thesis.pdf-113-2.png)

**Figure 4.1** _|_ **Sample and chip layout. a,** Photograph of Darkmon chip ( 2 _._ 9 __ 7 mm,
sapphire) in the aluminum (Al) cavity, which serves as the sample holder, shown with upper
half removed. Green arrow points to location of the chip. Also visible: input-output ( _IO_ **)** SMA coupler and frequency tuning screw (right side). **b,** Not-to-scale schematic
representation of the Bright (vertical) and Dark (horizontal) transmon qubits. Vertical
blue arrow indicates the orientation of the electric field of the fundamental ( TE 101 ) cavity
mode.

where  _n_ D _,_ B _,_ C are the Dark, Bright, and cavity photon-number operators, __ D _,_ B are the

Dark and Bright qubit anharmonicities, also referred to as self-Kerr frequencies, __ DB is the

dispersive cross-Kerr frequency shift between the Dark and Bright modes, while __ DC _,_ BC

are the dispersive shifts between the cavity and the two transmons. The energy level

structure of the two-transmon composite system is schematically represented in Fig. 4.2.

When the anharmonicities, __ B and __ D _,_ are relatively large, typically in the range 100 to

300 MHz, see Table 5.1 for device parameters, the level structure becomes sufficiently

anharmonic and we can restrict our attention to the manifold of the four lowest energy

states, _{|_ _gg_ __ _,_ _|_ _eg_ __ _,_ _|_ _ge_ __ _,_ _|_ _ee_ _}_ , where the first (second) letter refers to the Dark (Bright)

transmon. When the two qubits are uncoupled, __ DB = 0 , the transitions among the levels

contain degeneracies, and _|_ _ge_ __ and _|_ _eg_ __ cannot be addressed individually. In the limit

where the coupling, __ DB , is large, in practice, on the order of 100 MHz, the degeneracy

is lifted, and the _|_ _ge_ __ and _|_ _eg_ __ states become independent, allowing us to further restrict

our attention to the three lowest-lying states. We label _|_ _gg_ __ simply as _|_ G __ , _|_ _eg_ __ as _|_ D __ ,

and _|_ _ge_ __ as _|_ B __ _._ In reference to the protected Dark state, _|_ D __ , which is engineered to be


-----


4.1. Sample design 98


![Mivev_Thesis.pdf-114-1.png](Mivev_Thesis.pdf-114-1.png)

![Mivev_Thesis.pdf-114-0.png](Mivev_Thesis.pdf-114-0.png)

######### g ######### g


######### e ######### g


**Figure 4.2** _|_ **Darkmon energy-level diagram.** Energy level diagram of the hybridized
Dark and Bright transmon qubits. Red (Blue) color denotes association with the Dark
(Bright) transmon, while grey denotes strong association with both transmons. The
strong non-linear, dispersive interactions in the circuit, self-Kerr ( __ B _,_ D ) and cross-Kerr
( __ DB ), allow the lowest-lying three levels to be isolated, and for the two qubit system to
be employed as a three-level one with a V-shape structure.

decoupled from the environment and readout cavity, we nickname the device Darkmon.

**Unique design constraints.** In addition to the required large transmon anharmonicity,

__ B , __ D , and cross-Kerr, __ DB _,_ frequencies, a few somewhat unique, decoherence related,

constraints were required, notably, at odds with the large couplings. First, catching and

reversing the quantum jump from _|_ G __ to _|_ D __ coherently and with high fidelity required five

orders of magnitude in timescales, see Table 5.2, thus imposing the constraint that the _|_ D __

level coherences be minimally at the 100 __ s level, both the energy-relaxation and dephasing


times, _T_ 1 D _, T_ D 2R 100 __ s . The regime of long energy relaxation, _T_ D 1 _,_ is accessible with the

__

state-of-the-art Purcell-filtered three-dimensional (3D) transmon qubits (Paik _et al._ , 2011,

Wang _et al._ , 2015, Dial _et al._ , 2016), but long quantum coherences, _T_ 2R D , are far more

difficult to achieve, and are generally obtained by decoupling the transmon qubit from

the readout cavity (Gambetta _et al._ , 2006, Rigetti _et al._ , 2012), thus making a tradeoff


-----


4.1. Sample design 99

between quantum coherence and the ability to perform a fast readout. In the quantum

jumps experiment, this tradeoff is not permissible, a fast readout of the _|_ D __ is required

simultaneously with long coherences.

To maximize the coherence properties of _|_ D __ , we designed the Dark transmon to

be decoupled from all dissipative environments, including the readout cavity and input-

output (I-O) coupler. Removing the coupling between _|_ D __ and the cavity is advantageous

in three important ways: it protects _|_ D __ from i) dephasing due to cavity photon shot noise

(Gambetta _et al._ , 2006, Wang _et al._ , 2019, 2018), ii) energy relaxation through the cavity

by means of the Purcell effect (Gambetta _et al._ , 2011, Srinivasan _et al._ , 2011, Diniz _et al._ ,

2013, Dumur _et al._ , 2015, Novikov _et al._ , 2015, Zhang _et al._ , 2017, Roy _et al._ , 2017), and

iii) measurement-induced energy relaxation (Boissonneault _et al._ , 2009, Slichter _et al._ ,

2016), see Fig. (5.1). Decoupling _|_ D __ might seem like a tradeoff at first, since _|_ D __ can no

longer be directly measured through the cavity. However, the strong coupling between the

Dark transmon and the Bright transmon, together with the special nature of the V-shape

level structure and the _|_ B __ /not- _|_ B __ dispersive readout, can be employed to nonetheless

achieve a fast and faithful readout, see Sec. 5.2.2. The associated challenge is that when

two transmon qubits are strongly coupled, the D level needs to remain otherwise isolated

and coherent at the same time that the B level is strongly coupled to the low-quality

(low-Q) cavity. The coupling between _|_ B __ and the cavity is necessitated to yield a large

dispersive shift, __ BC _,_ used to realize the _|_ B __ /not- _|_ B __ readout; however, this coupling is

accompanied by a degree of energy relaxation by means of the Purcell effect inherited

by _|_ B __ (Gambetta _et al._ , 2011). The dissipation in _|_ B __ can in turn be inherited by the

coupled state _|_ D __ , due to the hybridization between the two transmons, __ DB , if the design

is not carefully optimized.

On a conceptual level, the Darkmon device and the couplings among the levels can

be understood in terms of an effective circuit model, see Fig. 4.3, where each mode is


-----


4.1. Sample design 100

Dark Bright Readout Input-output

|L D|L B|Col3|Col4|
|---|---|---|---|


![Mivev_Thesis.pdf-116-1.png](Mivev_Thesis.pdf-116-1.png)

![Mivev_Thesis.pdf-116-0.png](Mivev_Thesis.pdf-116-0.png)

**Figure 4.3** _|_ **Effective circuit model of Darkmon system.** Dark and Bright
transmons represented as lumped-element junction-capacitor circuits, junction denoted
by cross, coupled an LC circuit representing the readout cavity. _L_ D _,_ B denote the Dark
and Bright Josephson inductances, corresponding to the horizontal and vertical junctions
in Fig. 4.1, respectively.

represented by a single LC oscillator, with the two qubits having the inductors replaced by

non-linear Josephson tunnel junctions. The Dark resonator is capacitively coupled to the

Bright one, which is capacitively coupled to the readout resonator, which is capacitively

coupled to the input-output transmission line. The Bright and readout resonators can be

seen to act as a two-pole filter shielding the Dark resonator from the dissipative effect of

the transmission line. While the model is conceptually useful to analyze the qualitative

behavior of the circuit, it cannot produce reliable quantitative results. Instead, engineering

the highly asymmetric set of couplings while isolating the _|_ D __ level was achieved by means

of an iterative search over the design geometry with the energy participation ratio (EPR)

approach. In the following, we briefly summarize the methodology.

######### 4.1.1 ######### Energy-participation-ratio (EPR) approach

The design of distributed circuits with the aim of obtaining a desired Hamiltonian and

set of environmental couplings has attracted a lot of interest (Nigg _et al._ , 2012, Bourassa

_et al._ , 2012, Solgun _et al._ , 2014, Solgun and DiVincenzo, 2015, Smith _et al._ , 2016), but a


-----


4.1. Sample design 101

general solution to this inverse problem appears to be out of reach. Instead, one applies a

search algorithm over the direct problem  a circuit is chosen, the non-linear mixing and

dissipation parameters are calculated, the circuit is modified, and the process is repeated

in search of the target parameters. A broadly-applicable approach based on the concept

of the energy-participation ratio (EPR) of the nonlinear elements (Josephson devices) in

the circuit allows the efficient calculation of the Hamiltonian. In the following, we briefly

outline the EPR procedure and finite-element methodology employed in the design of the

sample.

**Josephson tunnel junction**

**Non-linear, flux-controlled inductor.** From the point of view of circuit theory (Yurke

and Denker, 1984, Devoret, 1997, Girvin, 2014, Vool and Devoret, 2017), a Josephson

tunnel junction (Josephson, 1962) is a two-terminal, non-linear, flux-controlled, lumped-

element inductor, whose constitutive current-flux relationship is

_I_ ( _t_ ) = _I_ _c_ sin ( ( _t_ ) _/_ 0 ) _,_ (4.2)

where _I_ _c_ is the _critical current_ of the junction, a phenomenological parameter, __ 0 __  _/_ 2 _e_

is the _reduced flux quantum_ , and  ( _t_ ) is the _generalized flux_ across the junction, which

has the same dimension as magnetic flux,


_t_
 ( _t_ ) __ d _V_ ( __ ) _,_ (4.3)
 __

where _V_ is the _instantaneous voltage drop_ across the junction terminals. The differential


inductance presented by the junction is _L_ _J_ _/_ cos () _,_ where _L_ _J_ __ __ 0 _/I_ _c_ is known as the

_Josephson inductance_ . The quantity _E_ _J_ __ __ 0 _I_ _c_ is known as the _Josephson energy_ , see


-----


4.1. Sample design 102

Eq. (4.4). Since there are two Josephson junctions in the Darkmon device, we label the

junction variables with a subscript _j_ _{_ V _,_ H _}_ , where V and H denote the vertical and

horizontal junctions, respectively. From Eq. (4.2) it follows that the potential energy

function of the _j_ -th junction is a function of flux,

_E_ _j_ ( _j_ ) = _E_ _j_ (1 __ cos ( _j_ _/_ 0 )) _,_ (4.4)

where _E_ _j_ and  _j_ are the Josephson energy and generalized flux of the _j_ -th junction.

**Linear and non-linear contributions.** Dropping constant terms, the potential energy

of the Josephson junctions, Eq. (4.4), can conceptually be separated in two, corresponding

to terms associated with the linear-response and non-linear response of the junction, _E_ _j,_ lin

and _E_ _j,_ nl , respectively,

_E_ _j_ ( _j_ ) _E_ _j,_ lin ( _j_ ) + _E_ _j,_ nl ( _j_ ) _,_ (4.5)

where


_j,_ lin ( _j_ ) = _E_ _j_
_E_ 2


 _j_

__ 0




2
_,_ (4.6a)



_E_ _j,_ nl ( _j_ ) = _E_ _j_


_c_ _jp_

_p_ =3


 _j_

__ 0




__ 0


_p_
_,_ (4.6b)



where _c_ _jp_ are the _dimensionless_ coefficients of the Taylor series of _E_ _j_ ,


( __ 1) _p/_ 2+1


_p_ ! for even _p_


_._ (4.7)
for odd _p_


_c_ _jp_ =


-----


4.1. Sample design 103

**Distributed circuit with non-linear lumped elements**

Although electromagnetic (EM) structures are often classified as planar (Blais _et al._ ,

2004, Wallraff _et al._ , 2004, Barends _et al._ , 2013, Yan _et al._ , 2016) (2D), quasi-planar

(Minev _et al._ , 2013a, 2016, Brecht _et al._ , 2016, Rosenberg _et al._ , 2017) (2.5D), or three-

dimensional (Paik _et al._ , 2011, Rigetti _et al._ , 2012, Reagor _et al._ , 2016, Axline _et al._ , 2016)

(3D), it is possible to treat these classes on equal footing within the EPR framework. Aside

from the junctions, the distributed EM circuit of the readout cavity with the Darkmon chip

can be described by a quadratic Hamiltonian function, _H_ EM , that depends on the device

geometry and the material properties. Analytic treatment of this function is impractical,

but finite-element (FE) numerical simulations are adept at handling systems described by

quadratic energy functions and finding their eigenmodes (Louisell, 1973, Jin, 2014). The

Hamiltonian of the Josephson circuit, consisting of the EM and Josephson elements, is

_H_ = _H_ lin + _H_ nl _,_ (4.8)

where its quadratic part is


_H_ lin _H_ EM +


1 _E_ _j_ ( _j_ _/_ 0 ) 2 _,_ (4.9)
2


_j_ __ _J_


while its non-linear part, originating from the non-linearity of the Josephson junctions, is


nl
_H_ __


_j_ __ _J_


_E_ _j_ _c_ _jp_ ( _j_ _/_ 0 ) _p_ _,_ (4.10)
_p_ =3


where, for notational convenience, _J_ _{_ V _,_ H _}_ _._ The quadratic Hamiltonian, _H_ lin , corre-

sponds to the _linearized Josephson circuit_ (LJC), which can be numerically simulated with

FE EM methods to find its eigenfrequencies, __ _m_ , and modal field distributions, consisting


-----


4.1. Sample design 104

__ __
of the electric field, _E_ _m_ ( __ _r_ ) , and magnetic field, _H_ _m_ ( __ _r_ ) , eigenvectors over the simulation

domain, where __ _r_ is the spatial coordinate. For our device, we restrict our attention to the

lowest three eigenmodes, the Dark, Bright, and readout cavity modes, labeled D _,_ B , and

C , respectively; i.e., _m_ __ _M_ _{_ D _,_ B _,_ C _}_ . Quantizing _H_ lin , the quantum Hamiltonian of

the LJC can thus be expressed


 __ _m_ _a_  __ _m_ _a_  _m_ _,_ (4.11)
_m_ __ _M_


_H_ lin =


where  _a_ _m_ is the _m_ -th mode amplitude (annihilation operator). Importantly, the frequen-

cies __ _m_ should be seen as an intermediate parameter entering in the calculation of the

rest of the quantum Josephson Hamiltonian,


_H_ nl =


_j_ __ _J_



 _p_
_E_ _j_ _c_ _jp_ __ _j_ _._ (4.12)
_p_ =3


While _E_ _j_ and _c_ _jp_ are known from the fabrication of the circuit devices, the quantum



 
operators __ _j_ __  _j_ _/_ 0 remain to be expressed in terms of the mode amplitudes. It can


be shown that __ _j_ is a linear combination of the latter,


__ _mj_ _a_  __ _m_ +  _a_ _m_ _,_ (4.13)
_m_ __ _M_


__ _j_ =


where __ _mj_ are the dimensionless, _real_ -valued zero-point fluctuations (ZPF) of mode _m_ at


the position of the junction _j_ . Calculation of _H_ is now reduced to computing __ _mj_ . We

achieve this by employing the energy participation ratio.


-----


4.1. Sample design 105

**Energy participation ratio**

We define the EPR _p_ _mj_ of junction _j_ in eigenmode _m_ to be the fraction of the total

inductive energy that is stored in the junction,



Inductive energy stored in junction _j_
_p_ _mj_ (4.14a)
__ Inductive energy stored in mode _m_



_n_ _m_ : 1 2
= __ _|_

_n_


2 _E_ _j_  __ 2 _j_ : _n_ _m_

_|_ __


_n_ _m_ 1 2
__ _|_


_j_

_,_ (4.14b)

1 

2 _H_ lin _n_ _m_
_|_ __


where we have taken the normal-ordered (Gerry and Knight, 2005) expectation values

over the state _|_ _n_ _m_ __ , a Fock excitation in mode _m_ . The normal-ordering, denoted by : : ,

nulls the parasitic effect of vacuum-energy contributions.

__ __
The EPR _p_ _mj_ is computed from the FE eigenfield solutions _E_ _m_ ( __ _r_ ) and _H_ _m_ ( __ _r_ ) as

explained in Sec. 4.1.2. It is a bounded real number, 0 __ _p_ _mj_ __ 1 . For example, a

participation of 0 means that junction _j_ is not excited by mode _m_ , while a participation

of 1 means that it is the only inductive element excited by the mode. It can be shown

that the values __ 2 _mj_ and _p_ _mj_ are directly proportional to each other,

__ 2 _mj_ = _p_ _mj_  2 __ _E_ _m_ _j_ _._ (4.15)

![Mivev_Thesis.pdf-121-0.png](Mivev_Thesis.pdf-121-0.png)

Equation (4.15) constitutes the bridge between the classical solution of the LJC and the


quantum Hamiltonian _H_ of the full Josephson system, and, as detailed below, is very

useful for practical applications.

**Fundamental design constraints.** The ZPF __ _mj_ are not independent of each other,

since the EPRs are submitted to three types of constraints. These are of practical im-

portance, as they are useful guides in evaluating the performance of possible designs and

assessing their limitations. It is possible to show the EPRs obey one sum rule per junction


-----


4.1. Sample design 106

_j_ and one set of inequalities per mode _m_ ,

_p_ _mj_ = 1 _,_ (4.16a)
_m_  __ _M_


0 __


_j_ __ _J_ _p_ _mj_ __ 1 _._ (4.16b)


In practice, Eq. (4.16a) can be exploited only if _M_ contains the total number of relevant

modes of the system, otherwise the sum of the EPR is bounded by one, rather than equal

to one. The final fundamental EPR relation concerns the orthogonality of the EPRs.

Solving Eq. (4.15) explicitly for the ZPF,


__ _mj_ = _S_ _mj_


_p_ _mj_  _/_ 2 _E_ _j_ _,_ (4.17)


where _S_ _mj_ = +1 or _S_ _mj_ = __ 1 is the _EPR sign bit_ of Josephson device _j_ in mode _m_ . The

EPR sign bit encodes the relative current direction across the Josephson device. Specif-

ically, only the _relative_ value between _S_ _mj_ and _S_ _mj_ __ for _j_ __ = _j_ __ has physical significance.

The EPR sign bit _S_ _mj_ is calculated during the process of calculating _p_ _mj_ , from the field

__
solution _H_ ( __ _r_ ) , see Eq. (4.25). The EPRs obey the orthogonality relationship

_S_ _mj_ _S_ _mj_ __ __ _p_ _mj_ _p_ _mj_ __ = 0 _,_ (4.18)
_m_  __ _M_

valid when all relevant modes are considered.

######### 4.1.2 ######### Calculation of the EPR

**Modeling the Josephson junction.** In our device, as in most cQED experiments, the


physical dimensions of the Josephson junction ( __ 10 __ 7 m) are approximately 5 orders

of magnitude smaller than the wavelength of the modes of interest ( __ 10 __ 2 m), mak-


-----


4.1. Sample design 107

ing the junction geometry unimportant, other than its role in establishing the value of

the Josephson inductance _L_ _j_ . Similarly, the lead wires leading up to the junction from

the transmon pads are deep-sub-wavelength features, and it follows that, typically, their

geometry is also unimportant, and can be ignored altogether, aside from any kinetic in-

ductance contribution. In view of this, in the FE simulation, we model the _j_ -th junction

as a single, two-dimensional rectangular sheet, _S_ _j_ , see Fig. 4.4, acting as lumped-element

inductor with linear inductance _L_ _j_ , Eq. (4.6a). The sheet is assigned a surface-impedance

__
boundary condition that links the tangental electric field, _E_ _,_ to the tangental magnetic
__

__ __ __
field, _H_ , on the surface of the sheet, _E_ = _Z_ _S_ ( _n_ _H_ ) _,_ where  _n_ is the surface normal
__ __ __ __

vector and _Z_ _S_ is the complex surface impedance, which is calculated so that the total

not a quantum operator.

![Mivev_Thesis.pdf-123-1.png](Mivev_Thesis.pdf-123-1.png)

![Mivev_Thesis.pdf-123-2.png](Mivev_Thesis.pdf-123-2.png)

![Mivev_Thesis.pdf-123-0.png](Mivev_Thesis.pdf-123-0.png)

**Figure 4.4** _|_ **Finite-element model of linearized Josephson junction.** Not-to-scale
schematic representation of the finite-element model of the linearized Josephson junction
(location marked by cross) connected by wire leads (elevated brown trace) to two large
metal pads (dark rectangles). Since the geometry of the junction and leads is in deepsub-wavelength regime, it can typically be ignored, and the inductance presented by the
junction, _L_ _j_ , graphically represented by black inductor symbol with two open terminals,
can be modeled by a single lumped-element inductive sheet, _S_ _j_ , in the FE simulation,
depicted by light grey rectangle. Green background represents the substrate.

After the design geometry and boundary conditions are established, additional fine-

mesh operations on crucial features of interest, such as the junction rectangles, are applied


-----


4.1. Sample design 108

to speed up the solver convergence, which can be diagnosed by examining the parameters

__ _m_ and _p_ _mj_ as a function of adaptive pass number. At each pass, the FE solver provides

__ __
the modal frequencies, __ _m_ _,_ and the electric, _E_ max ( __ _r_ ) , and magnetic, _H_ max ( __ _r_ ) , phasors.

The electric field at a point __ _r_ in the volume of the device, _V_ , at time _t_ is

__ __ _j_ _m_ _t_
_E_ ( __ _r, t_ ) = Re _E_ max ( _x, y, z_ ) _e_ _._

The total magnetic and electric field energies of a mode can be computed from the

eigenfields (Pozar, 2011):


elec = Re
_E_ 4

1
mag = Re
_E_ 4


d _v_ _E_ __ max __ __ __ __ _E_ __ max _,_ (4.19)

d _v_ _H_ __ max __ __ __ __ _H_ __ max _,_ (4.20)


where the spatial integral is performed over total volume, _V_ , of the device, and __ __ __

( __ __ __ ) is the electric-permittivity (magnetic-permeability) tensor. While the magnetic and


where the spatial integral is performed over total volume, _V_ , of the device, and __ __


electric energies are typically equal on resonance (Pozar, 2011), when lumped elements

are included in the model, the more general equality is between the capacitive, _E_ cap _,_ and

inductive, _E_ ind _,_ energies, _E_ cap = _E_ ind _._ For our design, the capacitive energy is stored

entirely in the electric fields, _E_ cap = _E_ elec , but the inductive energy is stored both in

the magnetic fields and in the kinetic inductance of the Josephson junctions, _E_ mag =

_E_ ind + _E_ kin , where _E_ kin is the total energy stored in the kinetic inductors, _H H_ EM , see

Eq. (4.9); it follows,

_E_ cap = _E_ ind + _E_ kin _,_ (4.21)

which, for a single-junction device, implies that the EPR of the junction in mode _m_ is



elec mag
_p_ _m_ = _E_ _E_ _._ (4.22)

elec
_E_


-----


4.1. Sample design 109

For a device with multiple junctions, such as the Darkmon, it follows from Eq. (4.14a),

that the EPR of junction _j_ in mode _m_ is


_p_ _mj_ = 1 _L_ _j_ _I_ _mj_ 2 _/_ ind _,_ (4.23)

2 _E_

where _I_ _mj_ is the junction peak current, which can be calculated from the surface-current

__ _m_
density, _J_ _s_ , of the junction sheet _S_ _j_ ,



__ _m_
d _s_ _J_ _s_ _,_ (4.24)
_S_ _j_
 
 


_I_ _mj_ = _l_ _j_ __ 1
_|_ _|_


where _l_ _j_ is the length of the sheet, see Fig. 4.5.


max

![Mivev_Thesis.pdf-125-0.png](Mivev_Thesis.pdf-125-0.png)

![Mivev_Thesis.pdf-125-1.png](Mivev_Thesis.pdf-125-1.png)

![Mivev_Thesis.pdf-125-3.png](Mivev_Thesis.pdf-125-3.png)

0

![Mivev_Thesis.pdf-125-2.png](Mivev_Thesis.pdf-125-2.png)

**Figure 4.5** _|_ **Finite-element simulation of a transmon device.**
Plot of the surfacecurrent density, __ _J_ _S_
, of a transmon qubit mode, obtained with finite-element electromagnetic eigenmode simulation; red (blue) indicates maximum (minimum) current magnitude.
Josephson junction (center rectangle) is modeled by a single inductive sheet ( _S_ _j_ ) with
length _l_ _j_ , spanning the distance between the two transmon pads (dark rectangles). Green
background represents the transmon chip.

The calculation of the EPR sign bits, _S_ _mj_ _{_ 1 _,_ 1 _}_ , requires the definition of a

convention for the junction orientation, which is accomplished by supplementing the FE

model with a directed line, DL _j_ , along the length of the junction sheet _S_ _j_ . The actual

orientation of the line is irrelevant, so long as it spans the two terminals of the junction.


-----


4.1. Sample design 110

The sign of the current along the line can be used as the sign bit


_S_ _mj_ = sign



__ __ _m_
d _l_ _J_ _s_ _._ (4.25)
DL _j_ __


**Remarks.** The convergence of the EPR extracted from local field quantities, _I_ _mj_ _,_ can

be enhanced by renormalizing the EPRs so as to enforce the global condition given by


Eq. (4.21),




_j_ __ _J_ _p_ _mj_ = _E_ kin _/_ _E_ ind . The eigenmode simulation approach affords several


distinct advantages. No prior knowledge of the mode frequencies is required to execute


the simulation. The solver can be queried to solve for the _N_ -lowest eigenmodes. If only

information on modes above a particular frequency is desired, this cutoff frequency can

also be supplied to the solver. From a single mesh and simulation, the FE solver returns

_complete_ information for all modes of interest  the parameters __ _m_ , _p_ _mj_ _,_ and _S_ _mj_ of

the Hamiltonian and, as shown in Sec. 4.1.4, the dissipation budget. These features

play nicely into the iterative nature of the design optimization, and make the eigenmode

design-optimization process easy to automate, provided freely to the community in our

software package pyEPR. 2 In the optimization of the Drakmon device, the finite-element

software of choice was _Ansys high-frequency electromagnetic-field simulator (HFSS)_ .

######### 4.1.3 ######### Calculation of Hamiltonian parameters with the EPR

The quantities __ _m_ , _p_ _mj_ _,_ and _S_ _mj_ obtained from the FE eigenmode solution together with


Eqs. (4.13), and (4.15) completely specify _H_ nl , Eq. (4.12). The multitude of non-linear


interactions contained in _H_ nl mix the LJC modes. However, operating the Darkmon in the


 _p_
dispersive regime (Blais _et al._ , 2004, Koch _et al._ , 2007), defined by __ _k_ __ _m_ _E_ _j_ _c_ _jp_ __ _j_
__ __

 
for all _p_ __ 3 , we can restrict our attention to the leading order correction of _H_ nl to _H_ lin

to account for the device spectrum, see level diagram of Fig. 4.2. The leading-order

2 http://github.com/zlatko-minev/pyEPR


-----


4.1. Sample design 111

correction is given by the _p_ = 4 terms that survive the rotating-wave approximation

(RWA) (Carmichael, 1999, Gardiner and Zoller, 2004), representing energy-conserving


interactions. To leading order, in the RWA, after normal-ordering, _H_ nl reduces to the

effective Hamiltonian

__


_H_ 4 _/_  = __

__


 _m_ _a_  __ _m_ _a_  _m_ + __ _m_ _a_  __ _m_ 2 _a_  2 _m_ + 1

2 2

_m_  __ _M_ __


__ _mn_ _a_  __ _m_ _a_  _m_ _a_  __ _n_ _a_  _n_ _,_ (4.26)
_m_ = __ _n_


__


which when combined with _H_ lin , Eq. (4.11), yields Eq. (4.1). The Lamb shift,  _m_ =

2 1 _n_ __ _M_ __ _mn_ _,_ represents the dressing of the linear mode _m_ by the zero-point vacuum

energy of all  _M_ modes. From Eq. (4.26), it follows that the measured transition frequency

between _|_ G __ and _|_ B __ is __ BG = __ B __  B _,_ where __ B is the LJC Bright eigenmode frequency

and  B is the Bright mode Lamb shift; a similar conclusion holds for the GD transition.

The Kerr frequencies are found from the EPR,


__

__ _mn_ = __


__

_j_ __ _J_


__

 __ _m_ __ _n_

_p_ _mj_ _p_ _nj_ (4.27)
4 _E_ _j_


__

and __ _m_ = __ _mm_ _/_ 2 . Remarkably, from Eq. (4.27) it becomes evident that the EPRs are

essentially the only free parameters subject to optimization and design in engineering the

non-linear couplings, since the frequencies, __ _m_ , and Josephson energies, _E_ _j_ , are con-

strained to a narrow range due to practical considerations. Notably, Eq. (4.27) embodies

the structure of a spatial-mode overlap in the EPRs.

######### 4.1.4 ######### Calculation of dissipation budget with the EPR

In this subsection, we summarize the methodology employed in minimizing dissipation in

the Darkmon device. This is achieved by optimizing the geometry of the design (in parallel

with the Hamiltonian parameter optimization) with the aim of minimizing the susceptibility


-----


4.1. Sample design 112

of each mode to the various unavoidable material and inputoutput losses. For each

design variation, we compute the bound on the modal quality factors by constructing a

_dissipation budget_ , which consists of the loss expected due to each lossy element in the

design. By manipulating the geometry, the budget can be favorably altered, to a degree.

The calculation of the dissipation parameters is detailed in the following.


Losses can be classified as either _capacitive,_ proportional to the electric field intensity,
2 2

__ __
_E_ , or _inductive_ , proportional to the magnetic field intensity, _H_ . The total loss due to
    _l_

a material is proportional to its energy participation in the mode,    _p_  , a geometric quantity

   

related to the field distribution, and its intrinsic quality, _Q_ , a material property. The

intrinsic material quality, _Q_ , can typically only be bounded, while _p_ _l_ can be calculated

from the eigenfields. The total capacitive and inductive losses, characterized by _Q_ cap and

_Q_ ind _,_ respectively, sum together with the loss due to input-output coupling, _Q_ rad , and

give the upper bound on the quality factor of an EM mode, _Q_ total , (Zmuidzinas, 2012,

Geerlings, 2013, Reagor, 2016)


_Q_ total


_Q_ cap


_Q_ ind


_._ (4.28)
_Q_ rad


In the following, we explicate the calculation of each quantity. We note that the EPR treats

dissipation and Hamiltonian parameters on equal footing, and all quantities, Hamiltonian

and dissipative, are extracted from a single eigensolution.


**Capacitive losses.** Capacitive losses, proportional to the intensity of the electric field,
2

__
_E_ , can originate from bulk or surface of materials. Dielectrics, such as the substrate
 

of the Darkmon device, constitute the primary source of bulk loss (Martinis and Megrant,  

 

2014, Dial _et al._ , 2016, Kamal _et al._ , 2016), and, unfortunately, every surface in a de-

vice possesses a near-unavoidable, lossy, surface dielectric layer, possibly due to chemical

residues, condensation, dust, etc. (Martinis and Megrant, 2014, Wang _et al._ , 2015). Re-


-----


4.1. Sample design 113

gardless of the microscopic origin of the dielectric losses, the loss properties of the _l_ -th

dielectric are characterized by a catch-all quality factor _Q_ _l_ cap (or equivalently the inverse

of the loss tangent) and the EPR of the dielectric in the mode, _p_ _l_ cap  the fraction of

capacitive energy stored in dielectric element _l_ . For a bulk dielectric, the dissipative EPR

is given by


_p_ _l_ cap,bulk =


elec
_E_



Re
4


d _v_ _E_ __ max __ __ __ __ _E_ __ max _,_ (4.29)
_V_ _l_


where the integral is carried over the volume of the _l_ -th dielectric element, namely _V_ _l_ .

The dissipative EPR of a surface dielectric, _p_ _l_ cap _,_ surf , can be approximated by


_t_ _l_ __ _l_

4 Re



__
d _s_ _E_ max _,_ (4.30)
surf _l_
 
 


_p_ _l_ cap,surf =


elec
_E_


where the surface layer thickness is _t_ _l_ , and its dielectric permittivity is __ _l_ . The total capaci-


tive loss in the mode is the EPR-weighted sum of the individual contributions (Zmuidzinas,

2012, Geerlings, 2013),


_Q_ cap


_p_ _l_ cap

_Q_ _l_ cap _._ (4.31)


**Inductive losses.** Electric currents flowing in metals or metal-metal seams can result in

inductive losses. The bound on the mode inductive-loss quality factor _Q_ ind is a weighted

sum of the intrinsic material quality _Q_ _l_ ind of each lossy inductive element _l_ , analogous to

Eq. (4.31),


_Q_ ind


_p_ _l_ ind

_Q_ _l_ _,_ (4.32)
ind


where _p_ _l_ ind is the inductive-loss EPR of element _l_ . For a metal surface, this can be

calculated from the eigenfield solutions,


__ 0 __ _l_

4 Re



__
d _s_ _H_ max _,_ __ _,_ (4.33)
surf _l_
 
 


_p_ _l_ ind,surf =


mag
_E_


-----


4.2. Sample fabrication 114

where __ 0 is the metal skin depth at __ _m_ , and __ _l_ is the magnetic permeability of the surface

(typically, __ _l_ = __ 0 ). In the case of superconductors _p_ _l_ ind,surf is the kinetic inductance frac-

tion (Gao, 2008, Zmuidzinas, 2012), commonly denoted __ . Normal metals typically have

an inductive quality factor _Q_ _l_ ind,surf of approximately one (Pozar, 2011). Bulk supercon-

ducting aluminum has been measured to have an inductive quality factor _Q_ ind,surf bounded

to be better than a few thousand (Reagor _et al._ , 2013). Meanwhile, the bound on the

quality of thin-film Al has been measured to be better than 10 5 (Minev _et al._ , 2013a).

**Seam losses.** A distinct loss mechanisms occurs at the seam of two metals (Brecht

_et al._ , 2015). For instance, a common source of such loss is the seam used in supercon-

ducting cavities. In the FE model, the seam can be modeled by a line, denoted seam _l_ ,

between the two mating metallic surfaces. The seam inductive participation is


__ 0 _t_ _l_ __ _l_



__
d _l_ _H_ max _,_ __ _,_ (4.34)
seam _l_
 
 


_p_ _l_ ind,seam =


Re


mag
_E_


where the seam thickness is denoted _t_ _l_ , its magnetic permeability __ _l_ , and its the penetra-


tion depth __ 0 . It is convenient to recast the seam loss contribution



__ __
seam _J_ _s_ _l_ _dl_
__

0 vol  _H_ max  2

 _|_  _|_


_p_ _l_ ind,seam

_Q_ seam


vol _H_ max 2 _dV_ _,_ (4.35)

_|_ _|_


_g_ seam


__


in terms of a seam admittance _g_ seam , which is defined in Ref. Brecht _et al._ (2015).

###### 4.2 ###### Sample fabrication

Samples were fabricated on 430 __ m thick, double-side-polished, c-plane sapphire wafers,

grown with the edge-defined film-fed growth (EFG) technique, with the bridge-free junc-

tion fabrication method, see Refs. Lecocq _et al._ (2011), Pop _et al._ (2012), Pop (2011),


-----


4.2. Sample fabrication 115

Reagor (2016). We defined the sample pattern, both large and fine structures, with

a 100 kV electron-beam pattern generator ( _Raith EBPG 5000+_ ) in a single step on a

PMAA/MAA resist bilayer. In the following, we describe each step of the fabrication

process in detail, and we hope that by adding some additional information about each

step and motivation behind it, a reader who is new to the subject will benefit.

**Cleaning the wafer.** First, the sapphire wafer is solvent cleaned under a chemical hood

in a two-step _N_ -Methyl-2-pyrrolidone (NMP) process. The solvent removes dust, organic

residues, and oils on the wafer surface. For our samples, we heated the wafer to 90 __ C

for 10 minutes in an NMP bath, then sonicated it in the bath for another 10 minutes.

After removing the wafer from the bath, if it is left out to dry on its own, the NMP would

evaporate quickly and leave undesirable residue behind. Instead, we rinsed the wafer in

an acetone bath, followed by a methanol one, before finally blow drying it with filtered

nitrogen gas. Methanol has low evaporation pressure and under the blow drying tends to

take away the residues, rather than simply evaporating and leaving residues behind. An

acid should not be used to clean the sapphire wafer, since the wafer is costly and already

polished.

**Spinning the positive resist bi-layer.** The copolymer resist ( _Microchem EL-13_ ) is

spun onto the cleaned wafer at 2,000 revolutions per minute (r.p.m.) for 100 seconds,

then, it is baked for 5 minutes at 200 __ C. The PMMA resist ( _Microchem A-4_ ) is spun

on top of the first at 2000 r.p.m. for 100 seconds. The wafer is baked at 200 __ C for

15 minutes, yielding a thickness of about 200 nm. It is worth noting why PMMA is the

resist of choice: it offers high, nm-sized resolution, simplicity and ease of handling, no

sensitivity to white light, nor shelf or film life issues, and is easily dissolved, qualities that

make it the ideal resist for this type of nanofabrication.

Before proceeding to patterning, fabrication on sapphire requires an extra step: the


-----


4.2. Sample fabrication 116

anti-charging layer. Whereas most silicon substrates are conducive enough to prevent

electron beam deflection during the e-beam writing, sapphire substrates are not. The

buildup of charge is mitigated by depositing a thin (10 nm) anti-charging layer of gold on

the wafer. In terms of metals, gold is an excellent choice, as it is inert, does not have

an oxide, and has notably high electrical conductivity. Alternatively, we have also used

aluminum for the anti-charging layer (13 nm thick).

**Writing and developing the pattern.** Both large and fine structures, including the

Josephson tunnel junction are patterned in a single step with the 100 kV EBPG, following

which, the gold layer is removed by submerging the wafer in a potassium-iodide/iodine

etch solution for 10 seconds. Next, the wafer is rinsed in water and the resist is developed

in a 3:1 IPA:water mixture at 6 __ C for 2 minutes. After development, the pattern is

inspected under an optical microscope.

**Plasma cleaning, deposition, and oxidation.** The wafer is loaded in the electron-

beam evaporation system, a multi-chamber _Plassys UMS300 UHV_ . To prepare the surfaces

for deposition and reduce the amount of aging of the Josephson junction, the exposed

sample surfaces are subjected to a 1 minute of oxygen-argon plasma cleaning, under a

pressure of 3 __ 10 __ 3 mbar. In this procedure, the etch removed 30 nm from the upper

resist layer; however, ideally, one would use a shorter duration and larger pressure (Pop

_et al._ , 2012), which was not available. Next, the sample is transferred from the load-lock

to the deposition chamber, where an automated titanium sweep is performed to absorb

residual gases in the deposition chamber. At an angle of 19 degrees, 20 nm of Aluminum

is deposited onto the sample, following which, the sample is transferred to the oxidation

chamber, where it is exposed to a 3:17 oxygen:argon mixture for 10 minutes at 100 Torr.

This forms an approximately 1 nm thick aluminum oxide layer, the insulating barrier of

the Al/Al O x /Al Josephson tunnel junctions. The sample is returned to the deposition


-----


4.2. Sample fabrication 117

chamber, where the second and final layer of aluminum (30 nm) is deposited at an angle

of __ 19 degrees. Next, rather than directly removing the sample from the evaporation

system and allowing the exposed aluminum surfaces to uncontrollably oxidize in air, the

surfaces are passivated with a final oxidation step at 50 Torr for 10 minutes. The aluminum

forms a self-limiting oxide capping layer.

**Liftoff.** The sample is placed in a heated bath of NMP solvent at 70 __ C for two hours.

It is then sonicated for 1 minute, while still in the NMP, following which, the NMP is

cleaned with acetone, methanol, IPA, and, finally, a dry nitrogen blow gun. The solvent

lifts off the unwanted metal from the wafer by dissolving the resist underneath it, thus

leaving the bath full of aluminum flakes. Note that NMP cant be heated much above

100 __ C, since that will likely damage the Al/Al O x /Al junctions.

**Dicing.** A protective coating of optical resist ( _SC1827_ ) is spun at 1,500 r.p.m. for

120 seconds and baked at 90 __ C for 5 minutes. The sample is loaded in the dicer ( _ADT_

_ProVecturs 7100_ ), which then is calibrated, aligned, and which then performs the dicing.

The diced chips are cleaned with acetone, methanol, and dry nitrogen, and are stored

until they ready to be mounted in the sample holder.

**Sample selection.** The diced chips are cleaned (NMP, Acetone, methanol, nitrogen air)

and visually examined under an optical microscope where the normal-state resistance, _R_ _N_ ,

of their Josephson junctions is measured. This is performed under an optical microscope

( _Copra Optical Inc. SMZ800_ ) with probe needles ( _Quater-Research H-20242_ ) lowered

to contact the transmon pads on either side of the junction, taking care to properly

ground all object in contact with the sample and to minimize unavoidable scratching

of the pad during the probing. The measurement of _R_ _N_ provides a good estimate of

the junction Josephson energy, _E_ _J_ , by an extrapolation from room temperature to the

operating sample temperature, at approximately 15 mK, using the Ambegaokar-Baratoff


-----


4.3. Sample holder 118

relation (Ambegaokar and Baratoff, 1963),



1
_E_ _J_ =


(2 _h_ _e_  ) 2 _R_ _N_ __ 1 _,_ (4.36)


_h_ 


where  is the superconducting gap of aluminum. The chip closest matching the Joseph-

son energies, _E_ _J_ , of the EPR-designed vertical and horizontal junctions is selected for

mounting in the sample holder.

###### 4.3 ###### Sample holder

In this section, we describe the methodology used in the design of the sample holder

and readout cavity, while paying special attention to the motivation underlying the design

choices. The boundary conditions of the readout cavity, depicted in Fig. 1.1, are formed

from the superconducting inner walls of the chip sample holder, composed of two main

halves, see Fig. 4.6c, and based on the ideas presented in Ref. Paik _et al._ (2011). Before

a discussion on the design geometry, we focus on the selection of its materials.

######### 4.3.1 ######### Material losses and selection

**Readout cavity considerations.** The inner walls of the sample holder establish the

boundary conditions of the readout cavity mode, and hence have a large inductive, _p_ _l_ ind,surf ,

and dielectric, _p_ _l_ cap,surf _,_ surface-loss participation ratio, see Sec. 4.1.4. It follows that the

material quality of the cavity inner walls is important in determining the readout quality

factor, _Q_ R . However, since this mode is purposefully made low-Q, by coupling it strongly

to the input-output ( _I-O_ ) couplers, the importance of the sample-wall material is greatly

reduced, and could in principle be rather lossy. For instance, in some designs, copper,

which has an inductive quality factor of unity, _Q_ = 1 , has been used, thus limiting _Q_ R to


-----


4.3. Sample holder 119

several thousand. Under these conditions, a fraction of the readout cavity signal is lost to

the walls of the cavity, rather than to the _I-O_ couplers. Nonetheless, the _I-O_ coupling is

engineered to be larger still, so that most of the signal in the readout cavity makes it to

the amplifier chain, and a high quantum measurement efficiency, __ , can still be obtained.

**Qubit mode considerations.** However, the Bright and Dark qubit modes, while pre-

dominantly spatially localized to the sapphire substrate region, have a small fraction of

their fields extending to the inner walls of the readout cavity. Although the lossy energy

participation ratios, _p_ _l_ ind,surf and _p_ _l_ cap,surf , are exponentially small (  10 __ 5 ), so that the


cavity walls participate on the part-per-million level, a normal-metal wall ( _Q_ _l_ ind 1 ) could

__


limit the qubit quality factors significantly, making lifetimes on the order of _T_ 1 D 100 __

__


out of reach. For this reason, we employ a low-loss superconducting material for the


sample holder, and clean its surfaces with care, see discussion on Pg. 127. Specifically,

we machined the readout cavity from 6061 aluminum alloy, which is typically found in

the construction of aircraft structures. Notably, it is a good superconductor, and due to

its hardened structure offers a machining advantage over regular aluminum, which is too

soft.

We remark that in other experiments, involving high-Q storage mode cavities, the

cavities are often machined from high-purity 4N (99.99% pure) aluminum (or sometimes,

5N), which is very soft, and thus difficult to machine. Further, the machining forms deep

cracks ( __ 100 __ m ), where machining oils and dirt seep in, and hence, the surfaces require

a more involved chemical etch process to remove about 150 __ m of the surface; see the

dissertation of M. Reagor (Reagor, 2016).

**Non-magnetic input-output couplers.** It has been recognized that commercial flange-

based _I-O_ couplers contain magnetic ferrite impurities with fields at the ten milligauss

level, which although small, due to the close spatial proximity of the coupler to the thin-


-----


4.3. Sample holder 120

![Mivev_Thesis.pdf-136-0.png](Mivev_Thesis.pdf-136-0.png)

**Figure 4.6** _|_ **Non-magnetic couplers and sampler holder. a/b,** Photograph of
two generations of custom-made, non-magnetic, _SubMiniature version A_
(SMA), inputoutput ( _I-O_ ) pin couplers. **c,** Photograph of disassembled sample holder, inside walls
forms boundary condition for the readout cavity mode. Three machined grooves on the
mating surfaces of the two halves provide placement slots for samples. Mating surface of
lower-half has groove encircling the inside cavity, employed with an indium wire to seal the
two halves. Large through holes visible on the mating surfaces provide means to fasten
sample holder and attach it to a cold finger in the dilution refrigerator. Small hole visible
on the interior back wall of the lower half allows for screw-tuning of the readout cavity
frequency.

film superconducting pads of the transmon, as well as the Josephson junction, could

introduce vortices in the films, and it is suspected, generally degrade the superconduc-

tor performance. To achieve better control of the electromagnetic environment and to

reduce potential losses due to magnetic impurities, we employed custom-made pins from

non-magnetic materials, such as copper and brass.

Panels (a) and (b) of Fig. 4.6 show two generations of non-magnetic, _SubMiniature_

_version A_ (SMA) pin-couplers. The first generation, see panel (a), was made in-house from

a standard, SMA copper cable with two female connectors. After testing the quality of

the cable, by checking its insertion loss with a vector network analyzer (VNA), the cable

was cut in two, partially stripped (external shielding and teflon) to expose the center

conductor, which serves as the pin inside the readout cavity, and soldered (non-magnetic

solder) to a custom copper flange. The flange can then be mounted to the outside


-----


4.3. Sample holder 121

surface of the readout cavity, see panel (c), by non-magnetic, brass or aluminum, screws.

Panel (b) shows a second generation of non-magnetic couplers, made from beryllium-

copper, and custom-ordered, courtesy of Christopher Axline. In general, components

used with the sample holder, placed inside the enclosing magnetic shielding, were tested

for magnetic compatibility with a magnetometer inside a magnetically shielded box at

room-temperature.

**Sample-holder seam.** To enclose the Darkmon chip in the sample holder, the sample

holder is designed as two separate halves, see Fig. 4.6c. As discussed in Sec. 4.1.4,

the placement of the seam in the design is important, as it determines the seam-loss

participation ratio, _p_ _l_ ind,seam . The seam in placed at the minimum of the current field

profile of the readout cavity mode. No perfect symmetry exists in the design; it is broken

by the _I-O_ couplers and the sample chip, so even at this location, the participation is not

strictly zero for either the readout cavity or qubit modes. For this reason, it is important

that the seam quality is as high as possible. In the following, we remark on seam properties

at the microscopic level, and the use of an indium seal for improved electrical contact.

_Seam quality at the microscopic level._ Even under high pressure, applied by the

fastening action of the sample holder screws, see Fig. 4.6c, the mating faces of the two

halves of the sample holder do not join well at the atomic level. Three interface regions

can be identified: i) _metal-to-metal regions_ , the rarest, where aluminum atoms from both

halves are in physical contact, allowing superconducting current to flow undisturbed, ii)

_semi-conducting regions_ , more common, where contaminants, typically dielectric, result

in resistive conductance, and iii) _non-conducting regions,_ typically, the most common,

where electrical flow is altogether prohibited, for either the region is a vacuum gap or is

dominated by a thick non-conductive film of oxides, sulphides, etc. The physical contact

area is typically less than a tenth of the area of the mating surfaces.


-----


4.3. Sample holder 122

_Higher-quality seam._ To create a seam with higher electrical conductivity, one can

first increase the force applied to form the bond to fracture the native oxide layer of the

mating surfaces and to yield a greater physical contact area, region (i). However, this

method is rather limited in applicability with our design, because the constraint of non-

magnetic screws excludes nearly all hard-material screws, including stainless steel ones, due

to magnetic impurities. The soft screws we use, aluminum and brass, lack the impurities

needed to make them withstand larger forces, and tend to break and strip easily. Mostly,

we relied on a soft-metal seal, a thin wire gasket placed in a small groove in one of the

mating faces. A number of materials metals are conventionally used as soft-metal seals,

such as copper, aluminum, indium, etc. The seal of choice in the cQED community is

indium, typically used in cryogenic hermetic seals and low-temperature solder with melting

point of 47 C, since it remains soft and malleable even at cryogenic temperatures and is

a superconductor. The indium gasket has been observed to increase the internal quality

factor of a superconducting cavity by several orders of magnitude and its estimated seam

conductance is _g_ seam  10 6 _/_ m (Brecht, 2017). In our experiment, we used an un-greased

99.99% indium wire of 0.020 in. diameter to form the seam gasket.

######### 4.3.2 ######### Assembly

After the surfaces of the machined sample holder are cleaned, see discussion on Pg. 127,

the Darkmon chip selected from the diced wafer, Sec. 4.2, is cleaned (NMP, Acetone,

methanol, nitrogen air) and, under an optical microscope, is immediately placed in the

central groove of the sample holder, see Fig. 4.1a. The groove is designed to be larger

(at minimum 5%) than the dimensions of the chip to account for the differential ther-

mal contraction between aluminum and sapphire (mostly, the aluminum contracts) and

machining tolerances. The precision of the dicing saw ( _ADT ProVecturs 7100_ ) is high,


-----


4.4. Cryogenic setup 123

several microns when recently calibrated, and the chip will not exceed the diced margin by

more than a few microns, but it can fall quite short of that, because, unlike silicon, when

sapphire is diced, it shatters around the edges, much like glass, and forms a jagged edge.

For this reason, when placed in the groove, the chip can rattle about, and requires an-

choring, accomplished by placing four small bits of indium on its four corners and pressing

them down to fill the corner circular pockets machined in the groove, see Fig. 4.6c. To

minimize contamination during the mounting, the chip is placed face down in the groove,

although, we note that even dust on the back side of the chip can contribute to loss in

the qubit modes, though, its participation ratio will be far smaller than if it were on the

front face.

When the sample is well anchored, the indium gasket is laid down in the gasket

groove, as visible in Fig. 4.1a, and the top half of the sample holder is mounted on

top, fastened tightly with even-pressure to allow the indium to distribute evenly. For

the screws, we used aircraft-alloy 7075 ( _McMaster_ / _Fastener Express_ ), with less than

1% iron impurities. These screws, as discussed earlier, are rather soft, and to achieve

a higher compression between the two halves at cryogenic temperatures, we used the

screws with molybdenum washers, which provide differential contraction  the linear

thermal contraction for molybdenum (aluminum) between room temperature and 4 K is

0.095% (0.415%). Molybdenum is compatible with the non-magnetic requirement. After

10 minutes, the indium seal relaxes, and the screws can be further tightened, with even

pressure.

###### 4.4 ###### Cryogenic setup

The embedding environment of the sample is nearly as important as the properties of the

sample itself in achieving long-coherences and desired performance. For this reason, in


-----


4.4. Cryogenic setup 124

this section, we focus on a few notable aspects of the cryogenic setup, and pay particular

attention to motivations. For the most part, our cryogenic setup is rather standard in

the field of cQED. For a more general discussion of low-temperature cryogenics, see

Refs. Ventura and Risegari (2010) and Pobell (2013).

######### 4.4.1 ######### Material selection

As already emphasized, the material selection of components used in the setup is of prime

importance. For this reason, we feel it worthwhile to note a few overriding principles,

corroborated by experience, employed when selecting materials for the cryogenic setup of a

cQED experiment, which have to be compatible with operation at milikelvin temperatures

and high vacuum ( _<_ 10 __ 1 Pa).

**Tested and well-understood cryogenic materials.** In the cryogenic setup of our ex-

periment, we employed only materials that have been exhaustively studied, characterized,

and established in regular laboratory use. There are only a handful suitable for cQED

experiments, which, in the solid-state, can classified as: i) ambient-pressure supercon-

ductors: aluminum, niobium, indium, titanium, tin, molybdenum, and niobium-titanium

(NbTi), ii) normal metals: copper, brass, gold, beryllium, stainless steel, and iii) dielectrics:

silicon, sapphire, quartz, nylon, Teflon, Stycast, poly(methyl methacrylate) (PMMA). The

listed materials are the most common ones; for material properties, see Refs. Ventura and

Risegari (2010) and Pobell (2013).

**Simplicity and homogeneity.** The simplest and smallest number of materials were

employed in the cryogenic setup. The Darkmon sample (including _I-O_ pins, seam gaskets,

screws, _et cetera_ ) consisted of essentially three types of atoms  aluminum, oxygen, and

indium. Beyond the materials employed in the sample holder, the properties of commercial

components were found to vary among manufacturers, for instance, the residual magnetic


-----


4.4. Cryogenic setup 125

impurity levels measured in screws and SMA connectors, barrels, adapters, _et cetera_ varied

across manufacturers. For this reason, prior to use in the setup, all components were

screened with a magnetometer, especially when employed inside magnetically shielded

compartments.

**Aluminum.** Chief among the materials employed was aluminum (Al), and hence, we

pay special attention to its properties. From a structural standpoint, Al is light-weight,

having one-third the density and stiffness of steel and copper. However, unlike steel, it

is free of magnetic impurities and has 59% of the thermal and electrical conductivity of

copper at room temperature. Importantly, when aluminum oxidizes, it forms a protective

coating of amorphous aluminum oxide ( AlO x ) that is thermodynamically favored to self

limit growth to a thickness of merely one nanometer. The AlO x layer is special in that it

has one of the highest hardness coefficients of all oxides, even greater than glass, making it

an excellent (unavoidable) encapsulation layer, rendering Al highly resistant to corrosion,

but also making the formation of a very-conductive Al-Al seam difficult, as discussed on

Pg. 121, and resulting in a surface dielectric layer with a loss tangent, see Sec. 4.1.4.

######### 4.4.2 ######### Thermalization

The design and implementation of a high-thermal-conductivity link between the Darkmon

sample and the main source of cooling power in the dilution refrigerator, the mixing

chamber pot, is crucial to take undesired heat away from the sample. At low temperatures,

the task is complicated since the rate limiting factor in the heat transfer becomes the

_contact thermal resistance,_ _R_ C _,_ found at the interface of two mating surfaces, intricately

dependent upon on the interface properties and difficult to control. The temperature


-----


4.4. Cryogenic setup 126

discontinuity,  _T_ , across two mating surfaces is



_R_ C
 _T_ =



_Q ,_ (4.37)




where _A_ is the surface area and _Q_ is the power flowing through the surface. It is seen

that to minimize  _T_ once can increase the contact area, _A_ , or decrease the geometry-

independent resistance, _R_ C _._ In the following, we describe the thermal link setup of the

sample and briefly outline the strategies employed to minimize _R_ _C_ across the various

interfaces.

**Gold plating and welding.** The sample was mounted on a cold-finger attached to

the mezzanine mixing-chamber plate. The plate is _gold plated_ ( __ 5 _m_ by electroplating)

to achieve higher thermal conductivity. As a soft metal, gold allows for a larger real

surface-area contact, and due to its chemical inertness, also provides protection from

oxidation of the surface, which keeps _R_ C low across multiple uses and over time. The

cold finger is not gold-plated, due to the cost and long-lead time of the process. It is

machined from two oxygen-free high-thermal-conductivity (OFHC) copper blocks, which

are _welded together_ to minimize the number of contact joints, essentially eliminating _R_ C

altogether. Of course, the bulk thermal resistance of the OFHC copper block remains,

but it is rather small and the cross-sectional area of the cold-finger block is rather large,

providing a good thermal link.

**Pressure and differential contraction.** The sample is fixed to the cold finger

with aluminum screws. The cold finger is mounted on the mezzanine mixing-chamber

plate with stainless steel screws, which allow greater pressure. To maximize the pressure

across all joints, _molybdenum washers_ were used everywhere to provide further differential-

contraction pressure, see discussion on Pg. 123.

**Thermal straps.** The cold finger thermalization link contains several unavoidable


-----


4.4. Cryogenic setup 127

joins, an issue that can be circumvented to a degree with the use of a flexible heat strap

(also known as _thermal braid_ ). Directly mounted on the sample was a small copper block

welded to a thick OFHC copper heat strap (models _P6-501_ and _P7-501_ from _TAI_ ) that

extended to the mixing chamber plate without interruption. The strap has the advantage

of being durable, flexible, and reusable.

**Surface preparation.** The physical and chemical condition of the surfaces forming

the contact determine _R_ C . When a component is machined, the stresses applied to

the surface create dislocations and riddle the surface with extremely narrow (order of a

few nanometers) but deep (hundreds of nanometers) cracks, into which machining oils

seep. The cracks and oil residues degrade the surface quality, visually, electrically, and

thermally. For this reason, all surfaces involved in forming a thermal link were prepared in

the following way. First, they were cleaned abrasively with scotch bright, buffing, and fine

sandpaper, removing the top surface layer and resulting in a shiny mirror finish. Second,

the mating component was cleaned chemically. Typically, by sonication in an anionic

detergent solution ( _Alconox 1%_ ), followed by acetone, then IPA, and finally blow dried

with dry nitrogen air. For more aggressive cleaning, we used a powerful oxidizing agent,

nitric acid ( HNO 3 ), to etch the surface. The acid and oxidized impurities were then

washed away with deionized water, followed by an acetone and isopropanol (IPA) bath,

and finally a nitrogen blow dry. The components were then mounted immediately, before

a substantial oxide layer could form. For previously treated components that required

remounting, the mating surface was cleaned with blue solder flux, which has a high

concentration of nitric acid, immediately prior to mounting.


-----


4.4. Cryogenic setup 128

######### 4.4.3 ######### Light and magnetic shielding

The quality factor of superconducting microwave aluminum resonators (and qubits) is

known to strongly depend on the quality of the infrared and magnetic shielding of the

embedding environment (Barends _et al._ , 2011, Wang _et al._ , 2014, Kreikebaum _et al._ ,

2016). Stray infrared light that is absorbed by a superconductor creates quasiparticles,

which reduces the overall quality factor of the superconducting surface. This effect is

especially pronounced in aluminum, whose superconducting gap is rather low, __ 88 GHz

(Barends _et al._ , 2011, de Visser _et al._ , 2011). The effect of stray light can be largely

mitigated with multistage infrared shielding. Magnetic fields at the surface of the super-

conductor can suppress the superconducting gap and introduce vortices, which generally

reduce the inductive surface quality, although, under certain conditions, the vortices can

act as quasiparticle traps, and can result in overall higher quality (Wang _et al._ , 2014, Vool

_et al._ , 2014).

**Light shielding.** Black-body radiation from warmer stages in the dilution refrigerator

was blocked by reflective thermal shields enclosing the mixing chamber space and special

care with taken to prevent line-of-sight leaks through screw holes, _et cetera_ . However,

_low frequency_ photons are more difficult to shield against, and several further strategies

were employed to make a light-tight sample space for the Darkmon device. In addition

to the indium seal between the two metal halves of the sample holder, the sample holder

was wrapped in three layers of aluminized mylar foil, secured with copper tape. In some

cooldowns, the inside of the magnetic shield housing the sample (see below) was lined with

infrared absorbing epoxy (Barends _et al._ , 2011, Rigetti _et al._ , 2012). Coaxial thermalization

and infrared filters (teflon replaced by _Eccosorb CR-110_ as the dielectric) were used on

the input and output lines of the sample.


-----


4.5. Microwave setup 129

**Magnetic shielding.** A high-magnetic-permeability, __ -metal ( _Amumetal A4K_ ) can en-

closed an aluminum superconducting cylinder which housed the sample. In this config-

uration, the __ -metal shield allows the superconducting shield to cool through its critical

temperature in a lower magnetic field, lowering the possibility of vortex trapping. Both

shields were thermally anchored to the mixing-chamber base plate by thermal straps, while

the __ -metal shield was also anchored to the cold-finger by direct contact. Components

employed within the can were tested for magnetic impurities with a magnetometer. Special

care was taken to avoid markings and paint that could be magnetic; paint on components,

such as directional couplers, was stripped with a solvent bath (typically, Acetone).

###### 4.5 ###### Microwave setup

**Room temperature.** The control tones depicted in Fig. 1.1 were each generated from

individual microwave generators (  D and  B0 : _Agilent N5183A_ ; readout cavity tone R

and  B1 : _Vaunix LabBrick LMS-103-13_ and LMS-802-13, respectively). To achieve IQ

control, the generated tones were mixed ( _Marki Microwave Mixers IQ-0618LXP_ for the

cavity and _IQ-0307LXP_ for  B0 _,_  B1 , and  D ) with intermediate-frequency (IF) signals

synthesized by the 16 bit digital-to-analog converters (DACs) of the integrated FPGA

controller system ( _Innovative Integration VPXI-ePC_ ). Prior to mixing, each analog output

was filtered by a 50  low pass filter ( _Mini-Circuits BLP-300+_ ) and attenuated by a

minimum of 10 dB. The radio-frequency (RF) output was amplified at room temperature

( _MiniCircuits ZVA-183-S+_ ) and filtered by _Mini-Circuits_ coaxial bandpass filters. The

output signal was further pulse modulated by the FPGA with high-isolation SPST switches

( _Analog Device HMC-C019_ ), which provided additional 80 dB isolation when the control

drives were turned off. The signals were subsequently routed to the input lines of the

refrigerator.


-----


4.5. Microwave setup 130

At room temperature, following the cryogenic high-electron mobility amplifier (HEMT;

_Low Noise Factory LNF-LNC7_10A_ ), the signal were amplified by 28 dB ( _Miteq AFS3-_

_00101200-35-ULN_ ) before being mixed down ( _Marki image reject double-balanced mixer_

_IRW-0618_ ) to an intermediate frequency (IF) of 50 MHz, where they were band-pass

filtered ( _Mini-Circuits SIF-50+_ ) and further amplified by a cascaded preamplifier ( _Stan-_

_ford Research Systems SR445A_ ), before finally digitization by the FPGA analog-to-digital

converters (ADC).

**Cryogenic.** The experiments were carried out in a cryogen-free dilution refrigerator

( _Oxford Triton 200_ ). Our input-output cryogenic setup is nearly identical to that de-

scribed in Ofek _et al._ (2016) and Minev _et al._ (2016), aside from the differences ev-

ident in the schematic of our setup (see Figs. 1.1b) Notably, for the output lines be-

tween the sample and the HEMT, we employed low-loss superconducting cables ( _CoaxCo_

_Ltd. SC-086/50-NbTi-NbTi PTFE_ ). The input line had a 12 GHz low-pass filter ( _K&L_

_6L250-12000/T26000-OP/O_ ) and the output line had two broadband isolators ( _Quinstar_

_CWJ1019-K414_ ), providing a total of 36 dB of reverse isolation between the HEMT and

the JPC. Since the experiment spanned more than a dozen cool-downs, we note that

regular retightening of all cryogenic SMA connectors and screws was observed to yield

overall better performance.


-----


### Additional experimental results

A strong claim of violation [of Bells
inequality] should be supported by at
least a 5 sigma deviation.

Alain Aspect
Rosenthal Lecture, 2018

his chapter presents experimental results and control experiments that support the

main experimental results and conclusions presented in Chapter 1. The charac-

## T

terization of the Hamiltonian parameters, coherence properties, and other non-idealities

of the two-transmon, one-readout-cavity device employed in the experiment is discussed

in Sec. 5.1. The calibration of the tomography and control pulses and relevant control

experiments are discussed in Sec. 5.2. A summary of the drive amplitudes and frequencies

can be found in Sec. 5.2.3. Details of the experimental flow of the catch and reverse

protocol with regard to the FPGA controller are discussed in Sec. 5.4. A comparison be-

tween the predictions of the quantum trajectory description of the experiment developed

in Chapter 3 and the main experimental results is presented in Sec. 5.5.

131


-----


5.1. Characterization of the system 132

###### 5.1 ###### Characterization of the system

In this section, we describe the characterization of the Hamiltonian and coherence pa-

rameters of the two-transmon, one-readout-cavity device employed in the experiment. In

reference to the protected Dark level, which is engineered to be decoupled from the en-

vironment and readout cavity, we nickname the device Darkmon. The low-excitation

manifold of the Darkmon device is well described by the approximate dispersive Hamilto-

nian, see Sec. 4.1,



1
_H/_   = __ B  _b_ __  _b_
__ 2



1 __ B  _b_ __ 2  _b_ 2 + __ D _d_  __  _d_ 1

2 __ 2



 _b_ __  _b_ __ B  _b_ __ 2  _b_ 2 + __ D _d_  __  _d_ __ D  _d_ __ 2  _d_ 2 __ DB  _b_ __  _b_ _d_  __  _d_ (5.1)
__ 2 __ 2 __

__ C + __ B  _b_ __  _b_ + __ D _d_  __  _d_ _c_  __ _c ,_ 



 
where __ D _,_ B _,_ C are the Dark, Bright, and cavity mode frequencies, _d_ , _b,_  _c_ are the respective

mode amplitude (annihilation) operators, __ D ( __ B ) is the Dark (Bright) transmon anhar-

monicity, __ D ( __ B ) is the dispersive shift between the Dark (Bright) transmon and the

readout cavity, and __ DB is the dispersive shift between the two qubits. The Dark, _|_ D __ ,


and Bright, _|_ B __ _,_ states correspond to a single excitation in the Dark and Bright transmon

 
modes, _d_ __ _|_ 0 __ and _b_ __ _|_ 0 __ , respectively; see Fig. 4.2 for a level diagram of the low-energy

manifold.

The readout cavity frequency was spectroscopically measured in reflection (Geerlings,

2013), __ C _/_ 2 __ = 8979 _._ 640 MHz, and the extracted cavity linewidth agreed well with an

independent measurement of the energy-relaxation rate of the cavity extracted from a

time-domain ring-down measurement, _/_ 2 __ = 3 _._ 62 __ 0 _._ 05 MHz _._ The cavity was observed

to be well over-coupled; i.e., the coupling quality factor, _Q_ _c_ , dominated the internal quality

factor, _Q_ _i_ ; making it difficult to precisely extract _Q_ _i_ _._ The frequency and anharmonicity of

the B transmon were __ B _/_ 2 __ = 5570 _._ 349 MHz and __ B _/_ 2 __ = 195 MHz , respectively, mea-


-----


5.1. Characterization of the system 133

sured with two-tone pulsed spectroscopy (Geerlings, 2013, Reagor, 2016). The frequency

and anharmonicity of the D transmon, __ D _/_ 2 __ = 4845 _._ 255 MHz and __ D _/_ 2 __ = 152 MHz ,

respectively, were measured in a modified two-tone spectroscopy sequence, where the _|_ G __

level was mapped to the _|_ B __ level at the end of the spectroscopy sequence, before the

readout, with __ -pulse on the BG transition. In a similar two-tone spectroscopy experi-

ment, which included a pre-rotation on either the BG or DG transition, and a measurement

rotation after the probe tone is turned off but before the readout tone is actuated, the

cross-Kerr coupling between the two qubits was measured to be __ DB _/_ 2 __ = 61 __ 2 MHz . In

a standard energy-relaxation experiment (Geerlings, 2013), the _|_ B __ lifetime was measured

to be _T_ 1 B = 28 2 __ s , which we believe is limited by the Purcell effect with the readout

__

cavity mode, based on a finite-element calculation, see Sec. 4.1.2. The Ramsey coherence

time of B was _T_ 2 R _,_ B = 18 1 __ s , possibly limited by photon shot noise (Gambetta
_|_ __ __

_et al._ , 2006, Rigetti _et al._ , 2012). The measured Hamiltonian and coherence parameters

of the device are summarized in Table 5.1, where the drive parameters employed in the

experiment can also be found.

######### 5.1.1 ######### Measurement-induced relaxation ######### T ######### 1 ######### ( ######### n ######### )

It has been established in the superconducting qubit community (Boissonneault _et al._ ,

2009, Slichter _et al._ , 2012, Sank _et al._ , 2016, Slichter _et al._ , 2016) that as a function of

the number of photons circulating in the readout cavity,  _n,_ the energy-relaxation time, _T_ 1 ,

of a dispersively coupled qubit is degraded. In Fig. 5.1, we show a measurement of the

_T_ 1 lifetime of the _|_ B __ and _|_ D __ states as a function of the readout drive strength, in units

of the number of circulating photons,  _n_ , when the drive is resonant; the measurement

protocol is explained in the figure caption. As typically observed in cQED experiments,

the Bright level, which is directly coupled to the readout cavity, exhibits a large parasitic


-----


5.1. Characterization of the system 134

|Readout cavity|BG transition|DG transition|
|---|---|---|



**Mode frequencies and non-linear parameters**

| /2 = 8979.640 MHz C| /2 = 5570.349 MHz  /2 = 4845.255 MHz BG DG  /2 = 5.08 0.2 MHz  /2 = 0.33 0.08 MHz B   D    /2 = 195 2 MHz  /2 = 152 2 MHz B  D   /2 = 61 2 MHz DB |
|---|---|



**Coherence related parameters**

|/2= 3.62 0.05 MHz   = 0.33 0.03  T = 260.0 ns int nC 0.0017 0.0002 th  |T 1B = 28 2 s  T 2B = 18 1 s R  T 2B = 25 2 s E  nB 0.01 0.005 th  |T 1D = 116 5 s  T 2D = 120 5 s R  T 2D = 162 6 s E  nD 0.05 0.01 th  |
|---|---|---|



**Drive amplitude and detuning parameters**

|n = 5.0 0.2   =  R B| /2 = 1.20 0.01 MHz B0   /2 = 0.60 0.01 MHz B1   /2 = 30.0 MHz B1 | /2 = 20 2 kHz DG   /2 = 275.0 kHz DG |
|---|---|---|



**Table 5.1** _|_ **Compilation of experimental parameters.**


-----


5.1. Characterization of the system 135

|Col1|Bright B Dark D|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||


Readout drive strength _n_

**Figure 5.1** rate ( _T_ 1 __ 1 ) of _|_ **Measurement-induced energy relaxation** B (blue dots) and D (red dots) as a function of _T_ 1 (  _n_ _n_ ) , measured with the **.** Energy relaxation

_|_ __ _|_ __
following protocol: after the atom is prepared in either _|_ B __ or _|_ D __ , the readout tone ( R ) is
turned on for duration _t_ read with amplitude  _n_ (corresponding to the number of steady-state
photons in the readout cavity when excited on resonance), whereafter, the population of
the initial state is measured. As in all other experiments, the readout drive is applied at
the _|_ B __ cavity frequency ( __ C __ __ B ). The relaxation rates are extracted from exponential 7
The solids lines are guides to the eye: blue line indicates the rapid degradation of fits of the population decay as a function of _t_ read , from 1 _._ 3 __ 10 experimental realizations. _T_ 1 B as
a function of the readout strength, while the red line indicates the nearly constants _T_ 1 D
of the protected dark level.

measurement-induced energy relaxation, _T_ 1 B ( _n_ )  its lifetime suffers more than an order

of magnitude degradation. On the other hand, perhaps surprisingly, the lifetime, _T_ 1 D _,_ of

the Dark state, _|_ D __ , remains essentially unaffected, even at very large drive strengths,

_n_  __ 50 . In this sense, the Dark level is protected from the _T_ 1 ( _n_ ) parasitic effect.


guide
for eye


-----


5.2. Control of the three-level atom 136

###### 5.2 ###### Control of the three-level atom

######### 5.2.1 ######### Qubit pulses

The implementation of precise and coherent manipulation of the three-level atom is im-

portant for the tomographic reconstruction of the flight of the quantum jump as well the

ability to faithfully reverse it. One of the main sources of pulse infidelity is typically deco-

herence, but the rather long coherence time of the Darkmon device relative to the duration

of the pulses employed in the experiment make it largely unimportant, and instead, place

emphasis on the technical details of pulse generation and Hamiltonian non-idealities, such

as leakage to higher excited states.

Mitigation of main technical non-idealities. The effect of the zero-order hold of the

FPGA digital-to-analog converter (DAC) was mitigated by installing a 270 MHz low pass

filter ( _Mini-Circuits BLP-300+_ ) on each of the analog output channels, see Sec. 4.5. All

microwave tones were generated with single-sideband IQ-controlled modulation at a base

intermediate frequency (IF) of 50 MHz, and the lower radio-frequency (RF) sideband was

used for the control tones (detuned 50 MHz below the local oscillator (LO) frequency).

The IQ mixers were calibrated with a four stage iterative routine to minimize carrier

leakage, by tuning the DC offsets of the I and Q channels, and to suppress the RF

image, by minimizing the quadrature skew and IQ gain imbalance. The LO leakage could

typically be suppressed to __ 70 dB relative to the RF tone. Spurious intermodulation

tones generated by higher-order non-linear terms present in the mixers [i.e., third-order

intercept-point (IP3) products] were generally negligible as the mixers were not typically

driven near saturation, but bandpass filters were installed on the RF outputs of all mixers

to nonetheless suppress any spurious tones. Excess noise from the following RF amplifier

( _MiniCircuits ZVA-183-S+_ ) was suppressed by 80 dB when the control drives were turned


-----


5.2. Control of the three-level atom 137

off by use of a high-isolation SPST switch ( _Analog Device HMC-C019_ ).

The pulses applied to the Dark and Bright transition were calibrated with a combination

of Rabi, derivative removal via adiabatic gate (DRAG) (Chow _et al._ , 2010), _All-XY_ (Reed,

2013), and amplitude pulse train sequences (Bylander _et al._ , 2011). Pulse timings and

delays, especially between the analog channels and the SPST switch digital markers,

were calibrated with a wide-bandwidth oscilloscope with ultra-low jitter ( _Keysight 86100D_

_Infiniium DCA-X_ ). The alignment was verified by performing a Gaussian qubit __ pulse on

the GB transition and varying the delay between the rise of the SPST digital marker and

the signal on the analog IQ pair playing the pulse.

######### 5.2.2 ######### Tomography of the three-level atom

At the end of each experimental realization, we performed one of 15 rotation sequences

on the atom that transferred information about one component of the density matrix,

__  _a_ , to the population of _|_ B __ , which was measured with a 600 ns square pulse on the

readout cavity. Pulses were calibrated as discussed in Sec. 5.2.1. The readout signal was

demodulated with the appropriate digital filter function required to realize temporal mode

matching (Eichler _et al._ , 2012). To remove the effect of potential systematic offset errors

in the readout signal, we subtracted the measurement results of operator components of

__  _a_ and their opposites. From the measurement results of this protocol, we reconstructed

the density matrix  __ _a_ , and subsequently parametrized it the useful form


_N_ 2 (1 _Z_ GD )

__

2 ( _X_ GD _iY_ GD )

__


2 ( _X_ GD + _iY_ GD ) _R_ BG + _iI_ BG

_N_ 2 (1 + _Z_ GD ) _R_ BD + _iI_ BD


__  _a_ =


(5.2)


_R_ BG _iI_ BG _R_ BD _iI_ BD 1 _N_
__ __ __


-----


5.2. Control of the three-level atom 138

where _X_ GD _, Y_ GD _,_ and _Z_ GD are the Bloch vector components of the GD manifold, _N_ is

the total population of the _|_ G __ and _|_ D __ states, while _R_ BG _, R_ BD _, I_ BG and _I_ BD are the

coherences associated with _|_ B __ , relative to the GD manifold. The measured population

in _|_ B __ , 1 __ _N_ , remains below 0.03 during the quantum jump, see Fig. 5.3. Tomographic

reconstruction was calibrated and verified by preparing Clifford states, accounting for the

readout fidelity of 97%.

**Control experiment.** In Fig. 5.2, we show the results of a control experiment where we

verified the Ramsey coherence ( _T_ 2R D ) and energy relaxation ( _T_ D 1 ) times of the DG transition

with our tomography method. Solid lines are fitted theoretical curves for the free evolution


of the prepared initial state


2 ( D G ) . The _T_ D 2R = 119 _._ 2 __ s value gained from the

_|_ _|_ __


simultaneous fit of _X_ DG ( _t_ ) and _Y_ DG ( _t_ ) matches the lifetime independently obtained from

a standard _T_ 2R measurement. Similarly, the value of _T_ 1 D = 115 _._ 4 __ s extracted from an

exponential fit of _Z_ DG ( _t_ ) matches the value obtained from a standard _T_ 1 measurement.

We note that our tomography procedure is well calibrated and skew-free, as evident in

the zero steady-state values of _X_ DG and _Y_ DG . The steady state _Z_ DG corresponds to the

thermal population of the dark state _n_ D th . It has recently been shown that residual thermal

populations in cQED systems can be significantly reduced by properly thermalizing the

input-output lines (Yeh _et al._ , 2017, Wang _et al._ , 2019).

**Mid-flight tomogram.** In the presence of the coherent Rabi drive  DG (corresponding

to catch parameter  _t_ off = 0 ), the complete tomogram of the three-level atom was

reconstructed, and a slice at the mid-flight time,  _t_ mid , is shown in Fig. 5.3. All imaginary

components of the reconstructed conditional density matrix, __ c , are negligibly small, less

than 0.007, as expected, see Sec. 5.5, for well-calibrated tomographic phase control. The

population of the _|_ B __ state, 0.023, is nearly negligible as well, as it is conditioned away

by the IQ filter, see Sec. 5.3.1.


-----


5.2. Control of the three-level atom 139

![Mivev_Thesis.pdf-155-0.png](Mivev_Thesis.pdf-155-0.png)

![Mivev_Thesis.pdf-155-1.png](Mivev_Thesis.pdf-155-1.png)

Time from start to tomography (  s)


**Figure 5.2** **of a DG superposition.** _|_ **Control experiment: time-resolved tomogram of the free evolution** The atom is prepared in __ 1 2 ( D G ) and tomography is

_|_ _|_ __
performed after a varied delay. Dots: reconstructed conditional GD tomogram ( _X_ DG _, Y_ DG ,
and _Z_ DG ) and population in DG manifold, _N_ , see Eq. (5.2). Solid lines: theoretical fits.

**a** **b**
Re  c ( _t_ mid ) Im  c ( _t_ mid )

![Mivev_Thesis.pdf-155-2.png](Mivev_Thesis.pdf-155-2.png)

![Mivev_Thesis.pdf-155-3.png](Mivev_Thesis.pdf-155-3.png)

**Figure 5.3** _|_ **Mid-flight tomogram.** The plots show the real (a) and imaginary
(b) parts of the conditional density matrix, __ c , at the mid flight of the quantum jump
(  _t_ catch =  _t_ mid ), in the presence of the Rabi drive from _|_ G __ to _|_ D __ (  _t_ off = 0 ). The
population of the _|_ B __ state is 0.023, and the magnitude of all imaginary components is
less than 0.007.


-----


5.3. Monitoring quantum jumps in real time 140

######### 5.2.3 ######### Atom and cavity drives

In all experiments, unless noted otherwise, the following drive parameters were used: The

DG Rabi drive,  DG , was applied 275 kHz below __ D to account for the Stark shift of the

cavity. The BG drive,  BG , was realized as a bi-chromatic tone in order to unselectively

address the BG transition, which was broadened and Stark shifted due to the coupling

between _|_ B __ and the readout cavity. Specifically, we addressed transitions from _|_ G __ to

_|_ B __ with a Rabi drive  B0 _/_ 2 __ = 1 _._ 20 __ 0 _._ 01 MHz at frequency __ BG , whereas transitions

from _|_ B __ to _|_ G __ were addressed with a Rabi drive  B1 _/_ 2 __ = 0 _._ 60 __ 0 _._ 01 MHz tuned

30 MHz below __ BG . This bi-chromatic scheme provided the ability to tune the up-click

and down-click rates independently, but otherwise essentially functioned as an incoherent

broad-band source. In Table 5.2, we summarize the hierarchy of timescales established by

the drive amplitudes and frequencies as well as the relevant decoherence properties of the

atom.

###### 5.3 ###### Monitoring quantum jumps in real time

######### 5.3.1 ######### IQ filter

To mitigate the effects of imperfections in the atom readout scheme in extracting a

_|_ B __ /not- _|_ B __ result, we applied a two-point, hysteretic IQ filter, implemented on the FPGA

controller in real time. The filter is realized by comparing the present quadrature record

values _I_ rec _, Q_ rec , with three thresholds ( _I_ B _, I_ B  _,_ and _Q_ B ) in the following way:
_{_ _}_


-----


5.3. Monitoring quantum jumps in real time 141

**Symbol** **Value** **Description**

 __ 1 __ 8 _._ 8 ns Effective measurement time of _|_ B __ , approximately given
by 1 _/_ _n_  , where  _n_ = 5 __ 0 _._ 2 in the main experiment


__ __ 1 44 _._ 0 __ 0 _._ 06 ns Readout cavity lifetime

_T_ int 260.0 ns Integration time of the measurement record, set in the
controller at the beginning of the experiment


 __ BG 1 0 _._ 99 0 _._ 06 __ s Average time the atom rests in G before an excitation
__ _|_ __
to _|_ B __ , see Fig. 1.2b

 _t_ mid 3 _._ 95 __ s No-click duration for reaching _Z_ GD = 0 in the flight of
the quantum jump from _|_ G __ to _|_ D __ , in the full presence
of  DG , see Fig. 1.3b


 __ GD 1 30 _._ 8 0 _._ 4 __ s Average time the atom stays in D before returning to
__ _|_ __
_|_ G __ and being detected, see Fig. 1.2b

_T_ 1 D 116 5 __ s Energy relaxation time of D
__ _|_ __


_T_ 2R D 120 5 __ s Ramsey coherence time of D
__ _|_


_T_ 2E D 162 6 __ s Echo coherence time of D
__ _|_ __


 __ DG 1 220 5 __ s Average time between two consecutive G to D jumps
__ _|_ __ _|_ __


**Table 5.2** _|_ **Summary of timescales.** List of the characteristic timescales involved
in the catch and reverse experiment. The Hamiltonian parameters of the system are
summarized in Sec. 5.1.

The filter and thresholds were selected to provide a best estimate of the time of a click,

operationally understood as a change in the filter output from _|_ B __ to not- _|_ B __ . The _I_ B and

_I_ B  thresholds were chosen 1.5 standard deviations away from the I-quadrature mean of

the _|_ B __ and not- _|_ B __ distributions, respectively. The _Q_ B threshold was chosen 3 standard

deviations away from the Q-quadrature mean. Higher excited states of the atom were

selected out by _Q_ rec values exceeding the _Q_ B threshold.


-----


5.3. Monitoring quantum jumps in real time 142


![Mivev_Thesis.pdf-158-0.png](Mivev_Thesis.pdf-158-0.png)

#######  ####### B ####### ( #######  ####### s)

**Figure 5.4** _|_ **Waiting time to switch from a** _|_ B __ **to not-** _|_ B __ **state assignment**
**result.**
Semi-log plot of the histogram (shaded green) of the duration of times corresponding to _|_ B __ -measurement results, __ B , for 3.2 s of continuous data of the type shown
in Fig. 1.2a. Solid line is an exponential fit, which yields a 4 _._ 2 __ 0 _._ 03 __ s time constant.

######### 5.3.2 ######### Unconditioned monitoring

In Sec. 1.2, we described a protocol for the unconditioned monitoring of the quantum

jumps where the atom is subject to the continuous Rabi drives  BG and  DG , as depicted

in Fig. 1.1. From the continuous tracking of the quantum jumps, over 3.2 s. of data,

we histogrammed the times, __ not-B , spent in not- _|_ B __ , Fig. 1.2b. In Fig. 5.4, we show

the complimentary histogram for the times, __ B _,_ spent in _|_ B __ , which is unlike the latter,

in that it follows a single exponential decay law. This single Poisson process character

follows from the fact that the _|_ B __ measurement result collapses the atom to a single state,

_|_ B __ , unlike the not- _|_ B __ result. The average time spent in _|_ B __ , extracted from the fit, is

__  B = 4 _._ 2 __ 0 _._ 03 __ s .


-----


5.4. Catching and reversing the jump 143

###### 5.4 ###### Catching and reversing the jump

######### 5.4.1 ######### Experiment flow

Figure 5.5a shows a flowchart representation of steps involved in the catch and reverse

protocol. In the following, we describe each block in the diagram in the order in which it

would be executed.

**Start:** internal memory registers are set to zero (Ofek _et al._ , 2016, Liu, 2016), including

the no-click counter cnt, defined below.

**Prepare B:** controller deterministically prepares the atom in _|_ B __ , a maximally conser-

vative initial state, with measurement-based feedback (Rist _et al._ , 2012a).

**Initialize:** controller turns on the atom (  BG and  DG ) and cavity drives ( R ) and begins

demodulation.

**Monitor and catch**  _t_ on **:** with all drives on (  BG _,_  DG , and R ), the controller actively

monitors the cavity output signal until it detects no-clicks for duration  _t_ on , as described

in panel (b), whereafter, the controller proceeds to monitor and catch  _t_ off  in the

case that  _t_ off _>_ 0 ; otherwise, for  _t_ off = 0 , the controller proceeds to tomography

(feedback pulse) for the catch (reverse) protocol.

**Monitor and catch**  _t_ off **:** with the Rabi drive  DG off, while keeping the drives  BG

and R on, the controller continues to monitor the output signal. The controller exits the

routine only if it detects a click, proceeding to the declare B step of the monitor and

catch  _t_ on  routine, or if no further clicks are detected for the pre-defined duration  _t_ off ,

proceeding to tomography (feedback pulse) for the catch (reverse) protocol.

**Feedback pulse:** with all the continuous drives turned off, the controller performs a

pulse on the DG transition of the atom, defined by the two angles _{_ __ _I_ ( _t_ catch ) _, _ _I_ ( _t_ catch ) _}_ .


-----


5.4. Catching and reversing the jump 144


![Mivev_Thesis.pdf-160-0.png](Mivev_Thesis.pdf-160-0.png)

![Mivev_Thesis.pdf-160-1.png](Mivev_Thesis.pdf-160-1.png)

![Mivev_Thesis.pdf-160-2.png](Mivev_Thesis.pdf-160-2.png)

**Figure 5.5** _|_ **Experiment flow.** See text for detailed description.


-----


5.4. Catching and reversing the jump 145

**Tomography:** controller performs next-in-order tomography sequence (see Sec. 5.2.2)

while the demodulator finishes processing the final data in its pipeline.

**Advance tomo.:** tomography sequence counter is incremented, and after a 50 __ s delay,

the next realization of the experiment is started.

**Logic and timing of catch subroutines**

**Monitor and catch**  _t_ on **.** Figure 5.5b shows a concurrent-programming flowchart

representation of the monitor and catch  _t_ on  routine. Displayed are the master and

demodulator modules of the controller. The demodulator outputs a pair of 16 bit signed

integers, _{_ _I_ rec _, Q_ rec _}_ , every _T_ int = 260 ns, which is routed to the master module, as

depicted by the large left-pointing arrow. The master module implements the IQ filter

(see Sec. 5.3.1) and tracks the number of consecutive not- _|_ B __ measurement results with

the counter cnt. The counter thus keeps track of the no-click time elapsed since the last

click, which is understood as a change in the measurement result from _|_ B __ to not- _|_ B __ .

When the counter reaches the critical value _N_ on , corresponding to  _t_ on , the master and

demodulator modules synchronously exit the current routine, see the T* branch of the

declare not-B decision block. Until this condition is fulfilled (F*), the two modules

proceed within the current routine as depicted by the black flowlines.

To minimize latency and maximize computation throughput, the master and demod-

ulator were designed to be independent sequential processes running concurrently on the

FPGA controller, communicating strictly through synchronous message passing, which im-

posed stringent synchronization and execution time constraints. All master inter-module

logic was constrained to run at a 260 ns cycle, the start of which necessarily was imposed

to coincide with a receive & stream record operation, here, denoted by the stopwatch.

In other words, this imposed the algorithmic constraint that all flowchart paths staring


-----


5.5. Comparison between theory and experiment 146

at a stopwatch and ending in a stopwatch, itself or other, were constrained to a 260 ns

execution timing. A second key timing constraint was imposed by the time required to

propagate signals between the different FPGA cards, which corresponded to a minimum

branching-instruction duration of 76 ns.

**Monitor and catch**  _t_ off **.** Figure 5.5c shows a concurrent-programming flowchart

representation of the master module of the monitor and catch  _t_ off  routine. The

corresponding demodulation-module flowchart is identical to that shown of panel (b);

hence, it is not shown. This routine functions in following manner: If a _|_ B __ outcome

is detected, the controller jumps to the declare B block of the monitor & catch  _t_ on

routine; otherwise, when only not- _|_ B __ outcomes are observed, and the counter reaches

the critical value _N_ off , corresponding to  _t_ catch =  _t_ on +  _t_ off , the controller exits the

routine.

###### 5.5 ###### Comparison between theory and experiment

In this section, we present the comparison between the results of the quantum jumps

experiment and the predictions of the quantum trajectory theory of the experiment de-

veloped in Chapter 3. The results agree with the theoretical predictions, accounting for

known imperfections, essentially without adjustable parameters. Simulation plots courtesy

of H.J. Carmichael.

######### 5.5.1 ######### Simulated data sets

**Independently measured parameters.** The parameters used in the Monte Carlo sim-

ulation described in Sec. 3.2.2 are listed in Table 5.3. Nearly all are set to the value at

the center of the range quoted in Table 5.1, with three exceptions: i) _T_ 1 B and _T_ D 1 are set


-----


5.5. Comparison between theory and experiment 147

to lower values in response to the photon number dependence of the readout displayed in

Fig. 5.1, ii)  DG _/_ 2 __ is set higher, but still falls inside the experimental error bars, and iii)

_n_ C th = 0 . Notably, of the three exceptions, only  DG _/_ 2 __ has a noticeable effect on the

comparison between simulated and experimental data sets.

**Leakage from the** **_GBD_** **-manifold.** As discussed in Sec. 4.1, see Fig. 4.2, the Dark-

mon system has higher excited states, which are generally unimportant, but do contribute

a small imperfection that needs to be considered to qualitatively account for the results.

As discussed in Sec. 3.2.2, we model the effect of leakage from the GBD manifold by

adding a single additional higher-excited state level, denoted _|_ F __ _._ The additional random

jumps to state _|_ F __ are governed by four parameters that are not independently measured;

they serve as fitting parameters, required to bring the simulation into agreement with the

asymptotic behavior of Z( _t_ catch ) , which, without leakage to _|_ F __ , settles to a value higher

than is measured in the experiment. The evolution of the X( _t_ catch ) is largely unaffected

by the assignment of these parameters, where any change that does occur can be offset

by adjusting  DG _/_ 2 __ while staying within the experimental error bars.

**Ensemble average.** Simulated data sets are computed as an ensemble average by sam-

pling an ongoing Monte Carlo simulation, numerically implementing the model outlined in

Eqs. (3.58)(3.65). Quadratures _I_ rec and _Q_ rec are computed from Eqs. (3.56) and (3.57),

digitized with integration time _T_ int = 260ns , and then, as in the experiment, a hysteric

filter is used to locate click events (  _t_ catch = 0 ) corresponding to an inferred change

of state from _|_ B __ to not- _|_ B __ . During the subsequent sampling interval (  _t_ catch __ 0 ), the

four quantities

Z _j_ GD _,_ X _j_ GD _,_ Y GD _j_ _,_ P _j_ BB ( _t_ catch ) = Z rec GD _,_ X rec GD _,_ Y GD rec _,_ P rec BB ( _t_ _j_ +  _t_ catch ) _,_ (5.3)


-----


5.5. Comparison between theory and experiment 148

with _t_ _j_ is the click time and


Z rec GD ( _t_ ) = __ D _|_ __ ( _t_ ) __ __ ( _t_ ) _|_ D __ G _|_ __ ( _t_ ) __ __ ( _t_ ) _|_ G __


_,_ (5.4)
__ __ ( _t_ ) _|_ __ ( _t_ ) __


X rec GD ( _t_ ) + _i_ Y GD rec ( _t_ ) = 2 __ D _|_ __ ( _t_ ) __ __ ( _t_ ) _|_ G __


_,_ (5.5)
__ __ ( _t_ ) _|_ __ ( _t_ ) __


P rec BB ( _t_ ) = __ B _|_ __ ( _t_ ) __ __ ( _t_ ) _|_ B


_,_ (5.6)
__ __ ( _t_ ) _|_ __ ( _t_ ) __


are computed, and running sums of each are updated. The sample terminates when the

measurement record indicates a change of state from not- _|_ B __ back to _|_ B __ . Finally, for

comparison with the experiment, Bloch vector components are recovered from the average

over sample intervals via the formula


_N_ _j_ ( _t_ catch ) Z _j_ GD _,_ X _j_ GD _,_ Y GD _j_ ( _t_ catch )

_N_  ( _t_ catch )  _N_ _j_ ( _t_ catch ) _P_ BB _j_  ( _t_ catch


_j_ GD GD GD

_N_ ( _t_ catch ) _N_ _j_ ( _t_ catch ) _P_ BB _j_ ( _t_ catch ) _,_ (5.7)
__




Z GD _,_ X GD _,_ Y GD ( _t_ catch ) =


where _N_ ( _t_ catch ) is the number of sample intervals that extend up to, or beyond, the


time  _t_ catch . The simulation and sampling procedure is illustrated in Fig. 5.6, and a

comparison between the experiment and the simulation is provided in Fig. 5.7.

The simulated and measured Bloch vector components are fit with expressions moti-

vated by Eqs. (3.18)-(3.20) and (3.44), modified to account for the effect of non-idealities

in the experiment,

Z GD ( _t_ catch ) = _a_ + _b_ tanh( _t_ catch _/_ + _c_ ) _,_ (5.8)

X GD ( _t_ catch ) = _a_ __ + _b_ __ sech( _t_ catch _/_ __ + _c_ __ ) _,_ (5.9)

Y GD ( _t_ catch ) = 0 _._ (5.10)

The fit parameters ( _a, a_ __ _, b, b_ __ _, c, c_ __ _, , _ __ ) for the simulated and experimental data shown


-----


5.5. Comparison between theory and experiment 149

|Readout cavity|BG transition|DG transition|
|---|---|---|



**Non-linear parameters**

|Col1| /2 = 5.08 MHz B | /2 = 0.33 MHz D |
|---|---|---|



**Coherence related parameters**

|/2= 3.62MHz  = 0.33 T = 260.0 ns int nC = 0 th|T 1B = 15 s T 2B = 18 s R nB = 0.01 th|T 1D = 105 s T 2D = 120 s R nD = 0.05 th|
|---|---|---|



**Drive amplitude and detuning parameters**

|n = 5.0  =  R B| /2 = 1.20 MHz B0  /2 = 0.60 MHz B1  /2 = 30.0 MHz B1 | /2 = 21.6 kHz DG  /2 = 274.5 kHz DG |
|---|---|---|



**Table 5.3** _|_ **Compilation of the simulation parameters.**

in Fig. 5.7 are compared in Table 5.4. As imposed by Eq. (3.44), in the absence of  DG

(turned off at time  _t_ on = 2 __ s ) _a_ __ , the offset of X GD , is strictly enforced to be zero. The

extracted simulation and experiment parameters are found to agree at the percent level.


-----


5.5. Comparison between theory and experiment 150

########## a ########## j
 Z GD


-1


![Mivev_Thesis.pdf-166-0.png](Mivev_Thesis.pdf-166-0.png)

![Mivev_Thesis.pdf-166-2.png](Mivev_Thesis.pdf-166-2.png)

![Mivev_Thesis.pdf-166-1.png](Mivev_Thesis.pdf-166-1.png)

204 208 212 216

Time-record position (  s)


**Figure 5.6** _|_ **Sampling of the Monte-Carlo simulation. a,** Simulated measurement
quadrature _I_ rec and correlated trajectory computed from Eqs. (5.4) and (5.5). Three
sample intervals are shown. The earliest corresponds to leakage from the GBD-manifold,
where a jump from _|_ G __ to _|_ F __ is followed by a jump from _|_ F __ to _|_ D __ . The second and third
sample intervals correspond to direct transitions from _|_ G __ to _|_ D __ , which are continuously
monitored and the object of the experiment. **b,** Expanded view of the shaded region of
the second sample interval in panel (a). The evolution is continuous but not smooth, due
to backaction noise from the continuously monitored readout. This feature is in sharp
contrast to the perfect no-click readout upon which the simple theory of Sec. 3.1 is
based. Figure courtesy of H.J. Carmichael.


-----


5.5. Comparison between theory and experiment 151

########## a ########## 1.0

 0.0

 -0.5

 -1.0

![Mivev_Thesis.pdf-167-0.png](Mivev_Thesis.pdf-167-0.png) 0 2 4 6 8 10 12

 b 1.0

 0.5

 0.0

 -0.5

 -1.0

|Z GD X GD|Col2|
|---|---|
|||
|Y GD||

 0 2 4 6 8 10 12
 Catch time  t catch (  s)

**Figure 5.7** _|_ **Comparison between simulation and experiment. a,** Simulated data
set obtained with Rabi drive  DG turned on for the entire  _t_ catch ; parameters taken from
Table 5.3 and leakage from the GBD-manifold included with ( __ FG _, _ FD ) _/_ 2 __ = 0 _._ 38kHz
and ( __ GF _, _ DF ) _/_ 2 __ = 11 _._ 24kHz . **b,** Simulated data set obtained with Rabi drive  DG
turned off at time  _t_ on = 2 __ s ; parameters taken from Table 5.3 and leakage from
the GBD-manifold included with __ FG _/_ 2 __ = 0 _._ 217kHz , __ FD _/_ 2 __ = 4 _._ 34kHz , __ GF _/_ 2 __ =
11 _._ 08kHz , and __ DF _/_ 2 __ = 15 _._ 88kHz . When leakage from the GBD-manifold is omitted,
the Z GD curve rises more sharply and settles to a value that is 10% (20%) higher in panel
(a) (panel (b)). Figure courtesy of H.J. Carmichael.


-----


5.5. Comparison between theory and experiment 152

**(a)** In presence of  DG

![Mivev_Thesis.pdf-168-0.png](Mivev_Thesis.pdf-168-0.png)

**(b)** In absence of  DG

![Mivev_Thesis.pdf-168-1.png](Mivev_Thesis.pdf-168-1.png)

**Table 5.4** _|_ **Comparison between parameters extracted from the simulation**
**and those from the experiment** . **a,** Parameters obtained from fits of the simulated and
measured data for the catch protocol in the presence of the Rabi drive  DG throughout
the entire duration of the quantum jump, data shown in Fig. 5.7a. **b,** Parameters obtained
from fits of the simulated and measured data for the catch protocol in the absence of the
 DG during the flight of the quantum jump for  _t_ on = 2 __ s , data shown in Fig. 5.7b.


-----


5.5. Comparison between theory and experiment 153

######### 5.5.2 ######### Error budget

In this section, we examine the effect of the various imperfections and dissipation channels

on the fidelity of the catch protocol.

**Imperfections.** The various imperfections are expected to reduce the maximum coher-

ence recovered in the measurement of X GD ( _t_ catch ) . They include:

1. Readout errors when inferring _|_ B __ to not- _|_ B __ transitions and the reverse. Such

errors affect the assignment of  _t_ catch , which can be either too short or too long

to correlate correctly with the true state of the system.

2. Leaks from the GBD-manifold to higher excited states. Importantly, these errors

mimic a _|_ B __ to not- _|_ B __ transition, as in the first sample interval of Fig. 5.6, but

the anticipated coherent evolution within the GBD-manifold does not occur. In this

manner, the excitations to higher states lead to false detections.

3. Thermal jumps from _|_ G __ to _|_ D __ . Such incoherent transitions contribute in a similar

way to Z GD ( _t_ catch ) , while making no contribution to the measured coherence.

4. Direct dephasing of the DG-coherence, _T_ 2R D .

5. Partial distinguishability of _|_ G __ and _|_ D __ . The readout cavity is not entirely empty

of photons when the state is not- _|_ B __ , in which case the cross-Kerr interaction

__ D _|_ D __ D _|_ _c_  __ _c_  shifts the  DG Rabi drive from resonance; hence, backaction noise is

transferred from the photon number to X GD ( _t_ catch ) .

**Budget for lost coherence.** The maximum coherence reported in the experiment is

0 _._ 71 __ 0 _._ 005 . In the simulation it is a little lower at 0.69. By removing the imperfections

from the simulation, one by one, we can assign a fraction of the total coherence loss to


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 154

each. Readout errors are eliminated by identifying transitions between _|_ B __ and not- _|_ B __ in

the ket _|_ __ __ rather than from the simulated measurement record; all other imperfections

are turned off by setting some parameter to zero. The largest coherence loss comes from

readout errors, whose elimination raises the X GD ( _t_ catch ) maximum by 0.09. The next

largest comes from leakage to higher excited states, which raises the maximum by a further

0.06. Setting __ D to zero adds a further 0.04, and thermal transitions and pure dephasing

together add 0.02. Figure 5.8 illustrates the change in the distribution of X _j_ GD ( _t_ catch )

samples underlying the recovery of coherence. The removal of the finger pointing to the

left in panel (a) is mainly brought about by the elimination of readout errors, while the

reduced line of zero coherence marks the elimination of leakage to higher excited states.

Aside from these two largest changes, there is also a sharpening of the distribution, at

a given  _t_ catch , when moving from panel (a) to panel (b). Having addressed the five

listed imperfections, a further 10% loss remains unaccounted for, i.e., the distribution of

panel (b) is not a line passing through X _j_ GD ( _t_ mid ) = 1 . The final 10% is explained

by the heterodyne detection backaction noise, a function of the drive and measurement

parameters, displayed in panel (b) of Fig. 5.6.

###### 5.6 ###### Signal-to-noise ratio (SNR) and de-excitation

 measurement efficiency

The catch protocol hinges on the efficient detection of de-excitations from _|_ B __ to _|_ G __ ,

as discussed in more detail in Chapter 3. In atomic physics, de-excitations are typically

monitored by a _direct_ detection method, employing a photodetector. Alternatively, de-

excitations can be monitored by an _indirect_ method, as done in our experiment. In this

section, we discuss the efficiency of both methods. For the indirect method, using simple


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 155

analytics, we estimate the _total_ efficiency of time-continuous, uninterrupted monitoring

of de-excitations from _|_ B __ to _|_ G __ to be __ eff _,_ clk = 0 _._ 90 __ 0 _._ 01 for the parameters of our

experiment, with integration time _T_ int = 0 _._ 26 __ s . The simple analysis of this section

complements the numerical one of the previous section, Sec. 5.5.2.

_Direct monitoring method in atomic physics._ The direct method monitors for a _|_ B __ de-

excitation by collecting and absorbing the photon radiated in the de-excitation. The _total_

measurement efficiency of this method is limited by i) collection efficiency  the fraction

of emitted photons collected by the detector in its own input spatial modes (for instance, as

determined by the solid angle)  typically falls in the range 0.1 - 50%, (Volz _et al._ , 2011)

ii) the efficiency of detecting the absorption of a single photon, which falls in the range

1 - 90%, (Eisaman _et al._ , 2011) and iii) non-idealities of the photodetector apparatus,

including its dead time, dark counts, jitter, etc. (Eisaman _et al._ , 2011) The combination of

these inefficiencies presents an almost insurmountable challenge in experimental atomic

physics for realizing continuous, time-resolved detection of nearly every single photon

emitted by the three-level atom, required to faithfully catch the jump.

_Direct monitoring method with superconducting circuits._ While technologically very

different, the direct monitoring method with superconducting circuits is conceptually simi-

lar to atomic method but can readily achieve high collection efficiencies (Katz _et al._ , 2008,

Vijay _et al._ , 2011, Rist _et al._ , 2012a, Vijay _et al._ , 2012, Hatridge _et al._ , 2013, Murch _et al._ ,

2013b, De Lange _et al._ , 2014, Roch _et al._ , 2014, Weber _et al._ , 2014, Campagne-Ibarcq

_et al._ , 2014, Macklin _et al._ , 2015, Campagne-Ibarcq _et al._ , 2016b,a, Hacohen-Gourgy

_et al._ , 2016, Naghiloo _et al._ , 2016, White _et al._ , 2016, Ficheux _et al._ , 2018, Naghiloo

_et al._ , 2017, Tan _et al._ , 2017, Hacohen-Gourgy _et al._ , 2018, Heinsoo _et al._ , 2018, Bultink

_et al._ , 2018). However, the energy of the emitted microwave photon is exceedingly small

 23 __ eV , about a part per 100,000 of the energy of a single optical photon  which

essentially forbids the direct detection of the photon with near-unit efficiency. This is be-


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 156

cause the propagating photon is unavoidably subjected to significant loss, added spurious

noise, amplifier non-idealities, etc. In our experiment, these imperfections reduce the full

measurement/amplification chain efficiency from its ideal value (Hatridge _et al._ , 2013,

Macklin _et al._ , 2015, Bultink _et al._ , 2018) of 1 to a modest __ = 0 _._ 33 __ 0 _._ 03 , correspond-

ing to the direct detection of approximately only one out of every three single photons 

insufficient for the catch protocol.

**Indirect monitoring method with superconducting circuits**

Alternatively, the indirect monitoring method couples the atom to an ancillary degree of

freedom, which is itself monitored in place of the atom. In our experiment, the atom is

strongly, dispersively coupled to the ancillary readout cavity. The cavity scatters a probe

tone, whose phase shift constitutes the readout signal, as discussed in Chapter 3. Since

the probe tone can carry itself many photons, this scheme increases the signal-to-noise

ratio ( SNR ) and, hence, the total efficiency ( __ eff _,_ clk ) of detecting a _|_ B __ de-excitation. Note

that the efficiency __ eff _,_ clk should not be confused with the efficiency of a photodetector or

the efficiency __ of the measurement/amplification chain, since __ eff _,_ clk includes the effect of

all readout imperfections and non-idealities, state discrimination and assignment errors,

etc. see below. In the remainder of this section, we estimate the SNR and efficiency

__ eff _,_ clk of the experiment.

_SNR of the indirect (dispersive) method._ The output of the measurement and am-

plification chain monitoring the readout cavity is proportional to the complex hetero-

dyne measurement record __ ( _t_ ) , which obeys the It stochastic differential equation, see

Eq. (3.55), 1



__ ( _t_ ) _a_  __ ( _t_ )
d __ ( _t_ ) = __ __ __ _|_ _|_ __

__ ( _t_ ) __ ( _t_ )



d _t_ + d _Z_ ( _t_ ) _,_ (5.11)
__ __ ( _t_ ) _|_ __ ( _t_ ) __


1 Since the bandwidth of the measurement chain, __ filter , is significantly larger than that, __ , of the
readout cavity, __ filter __ __ , we can neglect the effect of __ filter for simplicity of discussion, see Eqs. (3.56)
and (3.57).


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 157

where  _a_ is the cavity amplitude operator in the Schrdinger picture, __ is the total mea-

surement efficiency of the amplification chain  again, not to be confused with the

de-excitation measurement efficiency, __ eff _,_ clk  and d _Z_ is the complex Wiener process

increment, defined below Eq. (5.11). A somewhat counterintuitive property of Eq. (5.11)

is that the heterodyne record increment d __ ( _t_ ) is stochastic and noisy even when __ = 1 ,

the case of ideal measurement in which no signal is lost  the stochastic term, d _Z_ , rep-

resents pure quantum vacuum fluctuations, which are inherent in the case of heterodyne

detection (Carmichael, 1993, Plenio and Knight, 1998, Wiseman and Milburn, 2010). Due

to the unavoidable presence of these fluctuations, only an infinitesimal amount of infor-

mation about the system can be extracted from d __ at an instant of time. Finite amount

of information is extracted by integrating d __ for a finite duration _T_ int ,


_T_ int
_s_ __ _I_ rec + _iQ_ rec __ 0



d __ ( _t_ ) _,_ (5.12)


where _I_ rec and _Q_ rec are the in- and out-of-phase quadrature components of one segment

of the record. What does _s_ correspond to? Its value depends on d __ , which depends on

the state of the cavity, _|_ __ __ , which itself depends on the occupation of _|_ B __  and therefore

_s_ contains the occupation of _|_ B __ . A de-excitation of _|_ B __ to _|_ G __ can thus be detected by

monitoring _s_ , whose value is different for the two states, since the cavity is generally in

the coherent state _|_ __ B __ or _|_ __ G __ when the atom is in _|_ B __ or _|_ G __ , respectively. For the

moment, assuming the atom and cavity do not change states during the course of the

measurement duration _T_ int , the stochastic integral in Eq. (5.12) explicitly evaluates to



1

_s_ B _,_ G = __ __ Re [ __ B _,_ G ] _T_ int + 1 __ 2 _W_ _I_ ( _T_ int ) + _i_ __ __ __ Im [ __ B _,_ G ] _T_ int + __
  



_W_ _Q_ ( _T_ int ) _,_
2

(5.13)


where _W_ _I,Q_ denote independent Wiener processes, obeying the conventional rules, E [ _W_ ( _t_ )] =


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 158

0 and Var [ _W_ ( _t_ )] = _t_ 2 . Equation (5.13) shows that the distribution of the stochastic vari-

able _s_ is a Gaussian blob in the IQ plane centered at  _s_ B _,_ G __ E [ _s_ B _,_ G ] = __ _T_ int __ B _,_ G with


width determined by the variance __ B 2 _,_ G Var [ _s_ B _,_ G ] = 1 2

__


2 _T_ int . We can thus define the


SNR of the experiment by comparing the distance between the two pointer distributions


to their width,


_s_  B _s_  G
SNR __
__ __ B + __ G


(5.14)


where the B (resp., G) subscript denotes signals conditioned on the atom being in _|_ B __

(resp., _|_ G __ ). In terms of _|_ __ B __ and _|_ __ G __ ,


SNR = 1 _T_ int __ B __ G 2 _,_ (5.15)

2 _|_ __ _|_

which can be expressed in terms of the parameters of the experiment, summarized in


Table 5.1,



1
SNR = _T_ int

2


2
_n ,_  (5.16)



SNR = 1


cos arctan


2 __ BG


Holding other parameters fixed, according to Eq. (5.16), the SNR can be increased ar-

bitrarily by increasing  _n_ , which can be readily done by increasing the amplitude of the

cavity probe tone. A higher SNR for _s_ corresponds to a higher SNR for measuring an

atom de-excitation, since _s_ is a proxy of the _|_ B __ population. Thus, the indirect cavity

monitoring can overcome the typical degradation in SNR imposed by the inefficiencies

and non-idealities of the measurement chain, __ . In practice, the SNR increase with  _n_

is bounded from above, since with sufficiently high  _n_ spurious non-linear effects become

significant (Boissonneault _et al._ , 2008, 2009, Minev _et al._ , 2013a, Sank _et al._ , 2016, Khezri

_et al._ , 2016, Bultink _et al._ , 2016, Khezri and Korotkov, 2017, Walter _et al._ , 2017, Les-

canne _et al._ , 2019, Verney _et al._ , 2019, Serniak _et al._ , 2018). The cavity and non-linear

coupling to the atom serve in effect as a rudimentary embedded pre-amplifier at the site


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 159

of the atom, which transduces with amplification the de-excitation signal before its SNR

is degraded during propagation and further processing.

_Discrimination efficiency of the indirect method._ While the SNR provides a basic

characterization of the measurement, it is useful to convert it to a number between 0 and

1, which is called the discrimination efficiency, __ disc . It quantifies the degree to which the

two Gaussian distributions of _s_ are distinguishable (Gambetta _et al._ , 2007),



1
__ disc = erfc

2


SNR


(5.17)


where erfc denotes the complementary error function. Equation (5.17) shows that in-

creasing the SNR by separating the _s_ B and _s_ G distributions far beyond their spread, __ B _/_ G ,

provides only marginal gain as __ disc saturates to 1. Next, we calculate the SNR and __ disc

for the parameters of the experiment and discuss corrections due to readout non-idealities.

_A first comparison to the experiment._ A first estimate of the SNR and __ disc of the

experiment are provided by Eqs. (5.16) and (5.17). Using the parameters of the experi-

ment, summarized in Table 5.1, from these two equations, we find SNR = 4 _._ 3 __ 0 _._ 6 and

__ disc = 0 _._ 98 __ 0 _._ 007 . Using data from the experiment, in particular, a second long IQ

record trace, represented by a short segment in Fig. 2a, we find the SNR of the jumps

experiment, by fitting the histogram of the trace with a bi-Gaussian distribution, to be

SNR = 3 _._ 8 __ 0 _._ 4 , corresponding to __ disc = 0 _._ 96 __ 0 _._ 01 . The measured values are slightly

lower than the analytics predict due to readout imperfections not included in the calcu-

lation so far, such as state transitions during _T_ int , cavity transient dynamics, additional

pointer-state distributions, etc.

_Effective click detection efficiency._ The dominant next-order error is due to atom state

transitions during the measurement window, _T_ int , which contributes an assignment error

of approximately 1 __ __ asg = 1 __ exp ( _T_ int _/_ B ) = 0 _._ 06 __ 0 _._ 001 to the detection of a _|_ B __


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 160

de-excitation. Combining __ disc with __ asg , we obtain the total efficiency for detecting _|_ B __

de-excitations __ eff _,_ clk = __ disc __ asg = 0 _._ 90 __ 0 _._ 01 , consistent with the total readout efficiency

of 0 _._ 91 that is independently estimated using the trajectory numerics, see Sec. 5.5.2.


-----


5.6. Signal-to-noise ratio (SNR) and de-excitation measurement efficiency 161

########## a
 1.0

 0.5


########## X ########## GD

_j_
########## X ########## GD


########## 0.0

 -1.0

 1.0

 0.5

 0.0

 -1.0


0.050
0.040
0.030
0.020
0.015
0.010
0.0075
0.0050
0.0025


![Mivev_Thesis.pdf-177-0.png](Mivev_Thesis.pdf-177-0.png)

########## 0 ########## 2 ########## 4 ########## 6 ########## 8 ########## 10 ########## 12
 Catch time  t catch (  s)

**Figure 5.8** **Coherence loss through sample to sample fluctuations. a,** Contour
###### | ###### j
plot of the distribution of X GD ( _t_ catch ) samples corresponding to the simulated data set
displayed in panel (a) of Fig. 5.7. **b,** Same as panel (a) but with transitions between _|_ B __
and not- and with changed parameters: _|_ B __ identified in the ket ( _|_ __ __ FG __ _, _ rather than from the simulated measurement record, FD _, _ GF _, _ DF ) _/_ 2 __ = 0 , _n_ B th = _n_ D th = 0 , _T_ D 2 = 2 _T_ D 1 ,
and __ D _/_ 2 __ = 0 . Figure courtesy of H.J. Carmichael.


-----


### Conclusions and perspectives

Technological forecasting is even
harder than weather forecasting.

Rolf Landauer

###### 6.1 ###### Conclusions

In conclusion, we experimentally demonstrated that, despite the fundamental indetermin-

ism of quantum physics in the context of the monitoring of the evolution of a system,

it is possible to detect an advance warning that signals the occurrence of an event, the

quantum jump from the ground state ( _|_ G __ ) to the excited state ( _|_ D __ ) of a three-level

superconducting atom, prior to its complete occurrence (Sec. 1.3). While the quantum

jump begins at a random time and can be prematurely interrupted by a click, a quantum

jumps that completes follows a _continuous_ , _deterministic_ , and _coherent_ flight, which

comes as a surprise in view of standard textbooks on quantum mechanics. The special

nature of the transition was exploited to catch the jump and reverse it to the ground state,

_|_ G __ . Additionally, the state of the atom was tomographically reconstructed, __ _c_ , as a func-

162


-----


6.1. Conclusions 163

tion of the duration of the catch signal,  _t_ catch , from 6 _._ 8 __ 10 6 individual experimental

realizations, each catching a single jump occurring at a random time. At the mid-flight

time of the quantum jump,  _t_ mid , the atom was observed to be in coherent superposi-

tion of _|_ G __ (equivalent to no jump) and _|_ D __ (equivalent to a jump), with state purity

Tr [ __ 2 _c_ ] = 0 _._ 75 0 _._ 004 . Even when conditionally turning off the Rabi drive between G

__ _|_ __

and _|_ D __ ,  DG , at the beginning of the jump,  _t_ on = 2 __ s , the flight of the quantum jump

was observed to nonetheless proceed in coherent, deterministic, and essentially identical

manner, despite the absence of the coherent Rabi drive. This demonstrated that the role

of  DG is to initiate the jump and set its phase but is otherwise unimportant, and that the

dynamics of the flight are (essentially) entirely governed by the measurement-backaction

force due to the measurement, discussed in Chapter 3.

The jump coherence and deterministic-like character (any two jumps take the same

gradual flight) provide a small island of predictability in a sea of uncertainty that was

exploited, see Sec. 1.4, to reverse the quantum jump to the ground state, thus precluding

its occurrence. When applied at the mid-flight time,  _t_ mid , the protocol succeeded in

reversing the jump to _|_ G __ with 82 _._ 0% __ 0 _._ 3% fidelity. Remarkably, under ideal conditions,

every jump that would complete is detected by the warning signal and reversed, thus

eliminating _all_ quantum jumps from _|_ G __ to _|_ D __ , and preventing the atom from ever

reaching _|_ D __ . Jumps that would not complete and are reversed by the protocol meet their

fate faster by the warning-based intervention.

In Sec. 5.5, we showed that the experimental results agree essentially without ad-

justable parameters with the theory predictions, accounting for known experimental im-

perfections, such as finite quantum measurement efficiency, __ , temperature, _n_ th _,_ dephas-

ing mechanisms, _T_ 1 and _T_ 2 , etc. The agreement testifies for the validity, reliability, and

predictive power of quantum trajectory theory and suggests its critical role in the practical

development of real-time feedback techniques for quantum system control.


-----


6.2. Perspectives 164

On a technological level, we developed a three-level superconducting atom with distinct

features of interest. By decoupling one of the states, _|_ D __ , from both the readout cavity

and the environment, we demonstrated a protected qubit design with notable quantum

coherence, _T_ 2R D = 120 5 __ s , importantly, _without_ sacrificing measurement efficiency or

__

speed, as typically necessitated when decoupling a level, see Sec. 4.1. Integral to the

implementation was the design optimization with the energy participation ratio (EPR)

approach, as described in Sec. 4.1. In Sec. 5.1.1, we demonstrated the ability to populate

the readout cavity with a large number of photons without degrading the coherence

properties of _|_ D __ due to measurement-induced relaxation, _T_ 1 ( _n_ ) .

###### 6.2 ###### Perspectives

In the following, we discuss a few possible research directions that build on the catch and

reverse experiment and the development of the Darkmon system, listed in ascending order

of difficulty.

**Fundamental tests.** The Darkmon three-level atom is a particularly versatile platform

for fundamental tests in quantum physics. Two unique aspects of the _|_ B __ /not- _|_ B __ mea-

surement are important for fundamental tests: i) it is information-asymmetric, and ii) its

is degenerate. For definitiveness, consider the situation where a measurement is performed

on the atom prepared in an unknown initial state. At first, the observer has no knowledge

of the system, i..e, zero bits of information. Performing a measurement and obtaining

a B outcome, the observer learns that the measurement has projected the atom in the

definite, pure state _|_ B __ , and now posses complete knowledge of the system, and has thus

gained _I_ = ln 2 3 __ 1 _._ 6 bits of information, although the initial state remains unknown.

In contrast, in obtaining a not-B outcome, only _I_ = ln 2 (3 _/_ 2) __ 0 _._ 6 bits of information

are gained, since the atom could still be in _|_ G __ or _|_ D __ . The measurement has left behind


-----


6.2. Perspectives 165

1 bit of the initial-state information. Importantly, the _|_ B __ /not- _|_ B __ measurement does not

disturb this bit, and preserves its quantum coherence. Since it leaves behind a manifold

of states untouched, it is known as _degenerate measurement._

_Contextuality._  Degenerate measurements are required to perform tests of Kochen-

Specker contextuality (Kochen and Specker, 1967), which reveals an essential aspect of

the nonclassical nature of quantum measurements and constrains hidden variable theories;

it can be viewed as a complement to Bells theorem. It follows from the degenerate

measurement requirement that a qutrit is the simplest system in which contextuality can

be observed, and the Darkmon system with its notable control and coherence properties

could prove a well-suited testbed for rigorous tests (Mermin, 1993, Klyachko _et al._ , 2008,

Yu and Oh, 2012, Szangolies, 2015).

_Wavefunction collapse and the arrow of time._  There is a growing interest in the

community to experimentally investigate the dynamics of the wavefunction collapse

(Katz _et al._ , 2006, 2008, Murch _et al._ , 2013b, Hatridge _et al._ , 2013, Weber _et al._ , 2014,

Campagne-Ibarcq _et al._ , 2014, 2016b, Jordan _et al._ , 2016, Naghiloo _et al._ , 2016, Tan _et al._ ,

2017, Harrington _et al._ , 2017) and associated fundamental questions. An interesting

research direction is to investigate the emergence of the apparent irreversibility of the

collapse, which, it is argued, yields the arrow of time in quantum physics. Recently,

theoretical work has emerged that suggests ways in which quantum trajectory experiments

can begin to probe this outstanding question regarding the origin of the arrow of time with

the tools of quantum trajectory theory (Dressel _et al._ , 2017, Jordan _et al._ , 2017). Focus so

far has been almost exclusively on two level systems, but important fundamental features

in quantum physics, such as Kochen-Specker contextuality, only emerge in systems of

larger than two dimension. The arrow of time is an especially interesting direction in view

of the results presented here, where we reverse quantum jumps prior to their complete

occurrence. We believe the Darkmon system and its degenerate measurement could offer


-----


6.2. Perspectives 166

a unique vantage point on the problem.

_Thermodynamics._  In a related research direction, the Darkmon system could be

employed to probe the emergence of thermodynamics in continuously monitored systems,

a question of active research in the community. Specifically, understanding (and formulat-

ing) the fundamental laws of thermodynamics in the quantum domain, as well as notions

such as work, heat, and Maxwells demon, with applications to heat engines, are under

investigation and can be explored with quantum trajectories in the multi-level system

(Alonso _et al._ , 2016, Naghiloo _et al._ , 2017, Elouard _et al._ , 2017, Cottet _et al._ , 2017).

**Protected qubit with faithful readout.** Technologically, pursuing further the ideas

demonstrated with the Darkmon system could lead to improved qubit coherences and

measurement capabilities within the cQED architecture with the aim of addressing the

third and fourth DiVincenzo criteria for practical quantum computation (DiVincenzo,

2000) .

In the development of fast and high-fidelity superconducting qubit readout, a number

of non-linear process have been employed (Cooper _et al._ , 2004, Astafiev _et al._ , 2004,

Siddiqi _et al._ , 2006, Lupacu _et al._ , 2006, Mallet _et al._ , 2009, Reed _et al._ , 2010), but

the linear dispersive readout, by means of a low-Q cavity (Wallraff _et al._ , 2005, Blais

_et al._ , 2004, Johnson _et al._ , 2012, Rist _et al._ , 2012b), is adopted most widely. While the

cavity inhibits the spontaneous relaxation of the qubit, it introduces three additional loss

mechanisms: i) energy relaxation ( _T_ 1 ) due to the Purcell effect (Esteve _et al._ , 1986, Koch

_et al._ , 2007, Neeley _et al._ , 2008), ii) qubit dephasing ( _T_ __ ) due to the photon shot noise

of the readout cavity (Blais _et al._ , 2004, Schuster _et al._ , 2005, Gambetta _et al._ , 2006,

Schuster _et al._ , 2007, Gambetta _et al._ , 2008, Sears _et al._ , 2012, Rigetti _et al._ , 2012),

often dominated by residual thermal population, _n_ th , and iii) measurement-induced qubit

energy relaxation ( _T_ 1 ( _n_ ) ) (Boissonneault _et al._ , 2009, Slichter _et al._ , 2012, Sank _et al._ ,


-----


6.2. Perspectives 167

2016, Slichter _et al._ , 2016). In contrast, the GD qubit in the Darkmon device is decoupled

from all three dissipation channels, while still benefiting from the cavity properties, and

not sacrificing the ability to perform a fast readout or to monitor the atom continuously.

Practically advantageous is that the design is hardware-efficient (simple) in the sense that

it does not require additional control gates, such as fast-flux lines or DC gates, or other

high-power pump tones.

An interesting idea to pursue further stems from the use of the readout cavity in the

catch and reverse experiment to provide amplification (and transduction) of the _|_ B __ signal

_prior to_ its transmission to the following quantum-limited amplifier. Reducing losses in

the transmission, __ , is an outstanding challenge in the field. However, a strategy to

overcome this problem is indicated by the design: the addition of a built-in gain element

at the site of the sample that provides sufficient amplification to overcome transmission

losses and whose coupling to the readout signal can be tuned independently of the gain

(in the experiment, by means of  BG ). First, we note that direct monitoring of the _|_ B __

signal, by means of fluorescence detection, would have prohibited the faithful execution

of the catch and reverse protocol, since a large number of the click signals would have

been lost in transmission, due to __ . In contrast, in the experiment, the _|_ B __ /not- _|_ B __ signal

was effectively amplified fivefold (with frequency transduction) by the readout scheme by

use of the large disperse shift, __ BC __ __ _C_ , and the cavity probe tone,  _n_ . In contrast

to the usual dispersive readout scheme, where the use of a large probe signal,  _n,_ results

in degradation of the signal-to-noise ratio and qubit coherence due to the _T_ 1 ( _n_ ) effect,

the _|_ D __ level was shown to be essentially immune to this, see Sec. 5.1.1. This could

provide the ability to use strong pump tones to activate interesting non-linear interactions

(Mundhada _et al._ , 2017, 2018) without harming _|_ D __ , and to implement a gain element or


to couple _|_ B __ to the readout cavity in a dissipation engineered manner. A specific form of

the latter would realize a coupling term proportional to _|_ G __ B _|_ _a_  +  _a_ __ , where  _a_ is the
 


-----


6.2. Perspectives 168

cavity annihilation operator that would operate as follows: if the atom is not-in- _|_ B __ , the

cavity is empty, otherwise, as  BG steers the atom from _|_ G __ to _|_ B __ , the cavity fills with

_n_  __ 1 photons and activates a strong dissipation channel of _|_ B __ that repopulates _|_ G __

before _|_ B __ is ever appreciably populated. Similar-in-spirit dissipation channels have been

realized, e.g., with the double-drive reset-of-population (DDROP) protocol (Geerlings

_et al._ , 2013). If sufficient gain is achieved, no quantum-limited amplifier is required, and

the scheme would simplify the setup and transmission losses, __ .

**Distillation and single-photon detector.** The degenerate measurement of the Dark-

mon atom, perhaps employed with the lowest four levels, could make it an interesting

candidate for magic-state and entanglement distillation protocols (Bennett _et al._ , 1996,

Bravyi and Kitaev, 2005). Interestingly, the detection of a quantum jump from _|_ G __ to

_|_ D __ can be viewed as the absorption and detection of a photon from the input-output

transmission line. In this sense, the three-level monitoring scheme implements a pho-

todetection apparatus for single flying microwave photons in cQED. The device could

be optimized with this goal in mind to address the outstanding challenge of detecting

itinerant microwave photons with high efficiency (Chen _et al._ , 2011, Fan _et al._ , 2014,

Inomata _et al._ , 2016, Narla _et al._ , 2016). In contrast to previous work on this subject,

which focused on operating detectors in a time-gated mode, the Darkmon scheme affords

the advantage of time-resolved, time-continuous photodetection with gain. It is possible

these advantages can be exploited for catching and releasing flying Fock states (Kalb

_et al._ , 2017, Campagne-Ibarcq _et al._ , 2017).

**Stochastic drive,**  DG **, and reversal.** Realizable with the current device, one could

catch and reverse the quantum jump from _|_ G __ to _|_ D __ in the presence of a stochastic

drive from _|_ G __ to _|_ D __ ,  DG ( _t_ ) . The stochastic drive more realistically models the effect

of the environment and breaks the feature of identical jumps; i.e., any two jumps no


-----


6.2. Perspectives 169

longer look identical. The phase of the mid-flight superposition between _|_ G __ and _|_ D __ is

determined by the details of the stochastic  DG phase during the initial period of the


jump,  _t_ catch __  _t_ mid _._ Nonetheless, our prediction is that if the phase fluctuations of

 DG at the beginning of the jump are known, one could still successfully reverse the jump

mid-flight with the appropriate coherent intervention. This could be implemented by

generating  DG with the FPGA controller, on the fly, and having the controller calculate

the correct intervention angles, _{_ __ _I_ ( _t_ catch ) _, _ _I_ ( _t_ catch ) _}_ . The reverse could be studied

as a function of the bandwidth of the noisy signal,  DG (practically, this could be made as

large as 25 MHz), thus exploring the crossover from jump dynamics due to deterministic

forces and those of the environment, perhaps shedding further light on decoherence and

measurement irreversibility.

**Phase-agnostic reversal and quantum error correction.** Calculation of the angles,

_{_ __ _I_ ( _t_ catch ) _, _ _I_ ( _t_ catch ) _}_ , becomes increasingly difficult for larger noise bandwidths. An

alternative strategy is to implement a phase-agnostic reversal. This could be achieved with

dissipation engineering (Poyatos _et al._ , 1996) to conditionally dynamically cool to atom

the ground state. Practical cooling protocols have been experimentally demonstrated in

cQED (Valenzuela _et al._ , 2006, Grajcar _et al._ , 2008, Murch _et al._ , 2012, Geerlings _et al._ ,

2013, Liu _et al._ , 2016).

Instead of dissipation engineering, the jump could be reversed by means of a measurement-

backaction force due to another measurement. This will likely have to be probabilistic,

unless adaptive measurements (Wiseman, 1995, Jacobs, 2003) or measured-based quan-

tum steering is employed (Schrdinger, 1935, Murch _et al._ , 2013b, Wiseman _et al._ , 2007).

Specifically, we propose to investigate a four-level scheme that builds on the Darkmon,

see Fig. 6.1. The ground state, _|_ G __ , is monitored though a Bright state, _|_ B 1 __ , by means

of Rabi drive,  B1 ( _t_ ) , and the photodetection of _|_ B 1 __ at rate  _._ Similarly, the Dark level,


-----


6.2. Perspectives 170

![Mivev_Thesis.pdf-186-0.png](Mivev_Thesis.pdf-186-0.png)

![Mivev_Thesis.pdf-186-1.png](Mivev_Thesis.pdf-186-1.png)

**Figure 6.1** _|_ **Four-level atom with two counter-steering measurements.** Sketch
of a modified Darkmon atom consisting of four levels: ground, _|_ G __ , Dark, _|_ D __ , a first
Bright, _|_ B 1 __ , and a second Bright, _|_ B 2 __ . Both Bright levels are monitored at rate  ,
while controlled-actuated Rabi drives  B1 ( _t_ ) and  B1 ( _t_ ) turn on the effective monitoring
of _|_ G __ and _|_ D __ _,_ respectively. A potentially stochastic Rabi drive  DG ( _t_ ) links _|_ G __ and
_|_ D __ .

_|_ D __ , is monitored by coupling it with a Rabi drive  B2 ( _t_ ) to a second Bright state, _|_ B 2 __ ,

monitored at rate  _._ Conditioned on no clicks, the _|_ G __ measurement steers the atom

toward _|_ D __ _,_ see Chapter 3. In contrast, conditioned on no clicks, the _|_ D __ measurement

steers the atom toward _|_ G __ . Both forces are phase agnostic. Since they oppose each other,

one can be used to undo the effect of the other with proper conditioning and control of

the Rabi drives. If _|_ G __ is measured subject to the Dark Rabi drive  DG from _|_ G __ to _|_ D __ ,

which could be deterministic or stochastic, while  B2 = 0 , the protocol demonstrated in

Chapter 1 is implemented. When the signal warning of the occurrence of the quantum

jump from _|_ G __ to _|_ D __ is detected,  B1 is shut off. If the catch time is set to  _t_ mid , the

state of the GD superposition is known to be on the GD equator, but its phase may be

unknown. If  B2 is turned on and the record is conditioned on no clicks, the jump should

be reversed, no matter what the superposition phase is. More generally, the opposition

of the two counter-steering no-click measurements offers a unique testbed for studying

non-commuting simultaneous measurements, a topic of rising interest in the field (Jordan

and Bttiker, 2005, Ruskov _et al._ , 2010, Hacohen-Gourgy _et al._ , 2016, Perarnau-Llobet

and Nieuwenhuizen, 2017, Atalaya _et al._ , 2017, Lewalle _et al._ , 2017, Patti _et al._ , 2017,


-----


6.2. Perspectives 171

Ficheux _et al._ , 2018, Chantasri _et al._ , 2018).

Quantum jumps are intimately involved in the detection and correction of errors in

quantum information systems (Sun _et al._ , 2013, Ofek _et al._ , 2016). A controller con-

tinuously monitors an error syndrome, often parity, such as that of a cavity state (Ofek

_et al._ , 2016, Cohen _et al._ , 2017) or multi-qubit stabilizer (Huembeli and Nigg, 2017), and

detects jumps in the measurement record, which signal the occurrence of an error. The

error needs to corrected. Catch and reversing the quantum jump of an error syndrome

prior to its occurrence could prevent the error from manifesting fully. A research direction

that could be explored is to couple the GD transition to the parity operator of a long-lived

quantum-memory cavity (Kirchmair _et al._ , 2013) that encodes a logical quantum state

(Cochrane _et al._ , 1999, Mirrahimi _et al._ , 2014, Leghtas _et al._ , 2015, Michael _et al._ , 2016,

Li _et al._ , 2017, Touzard _et al._ , 2018). The parity bit of the cavity state would be contin-

uously mapped onto the GD manifold. The state _|_ G __ would indicate _no_ error, while _|_ D __

would indicate that an error has occurred. If the noise process driving the parity bit flips

has sufficiently narrow bandwidth, it may be possible to extend the catch and reverse pro-

tocol to intervene in the occurrence of the parity-bit error. By monitoring the _|_ B __ /not- _|_ B __

measurement record as discussed in Chapter 1, the controller would detect the advance-

warning signal and immediately perform a phase-agnostic reversal of the jump to prevent

the error. Applications of the jump reversal protocol to quantum error correction schemes

present an interesting and open direction for theoretical and experimental research.

**Closing statement.** We hope the catch and reverse experiment offers a new vantage

point on the state-disturbing nature of measurements and the interplay between deter-

ministic forces and the necessarily-stochastic ones due to quantum measurements. More

generally, we hope it could provide a conceptually simple but striking illustration to help

write operationally-based, rather than postulate-based, textbooks for quantum mechanics.


-----