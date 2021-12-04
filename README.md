# B_field

## Introduction

### ELF: Extremely Low Frequency

Low frequency electromagnetic fields, commonly referred to as ELF (Extremely Low Frequency), are emitted at frequencies between 0 Hz and 3000 Hz.
The main artificial sources of ELF fields are the transmission and distribution systems of electricity (power lines) consisting of:

- _power lines_ with different voltage levels, in which alternating electric current flows at a frequency of 50 Hz;
- _substations and electrical transformer cabins_, to transfer electricity between power lines at different voltages.

### Characteristics of power lines

The main characteristics of a power line are the operating voltage (kV) and the carried electric current (A). On the basis of the operating voltage, the power lines are divided into:

- Very High Voltage lines (AAT - 220 kV and 380 kV),
- High Voltage lines (AT - from 40 kV to 150 kV),
- Medium Voltage lines (MT - from 1 kV to 40 kV)
- Low Voltage lines (BT- 380 V and 220 V).

In this project, only AAT, AT and MT power lines will be considered.

### Assessment of human exposure: ARPA

The ascertained effects of low-frequency sources on the human body are essentially related to the intensity of the magnetic field B, which unlike the electric one is not shielded from obstacles such as walls and vegetation. For this reason the magnetic field is more important than the electric one for the protection of the population.

According to the [Legge Quadro 36/01][3], [**ARPA**][2] plays a technical role of support to the public authorities responsible for the health and environmental control and surveillance activity.
The [D.P.C.M. 08.07.2003][3] "Fissazione dei limiti di esposizione, dei valori di attenzione e degli obiettivi di qualità per la protezione della popolazione dalle esposizioni ai campi elettrici e magnetici alla frequenza di rete (50 Hz) generati dagli elettrodotti" establishes three threshold values that apply to different situations:
- _limite di esposizione_ (100 µT) applies to all areas accessible by the population;
- _valore di attenzione_ (10 µT), calculated as the median of the B values over 24 hours, applies to playgrounds, schools and places with daily human presence greater than 4 hours;
- _obiettivo di qualità_ (3 µT), calculated as the median of the B values over 24 hours, is applied in the design of new playgrounds, schools and places with daily human presence greater than 4 hours and in the design of new power lines near these settlements.

The assessment of human exposure to low-frequency electric and magnetic fields is carried out by Arpae in order to assess the impact of the sources on the territory and compare the levels with the limits set by the legislation for the protection of human health. Models and measurements are used in order to verify the compatibility of the territory with the constraint of the buffer zones of the power lines (DPA).

### Distanza di prima approssimazione (DPA)

The magnetic induction field levels generated by the power lines in the area are evaluated through the _DPA (distanza di prima approssimazione)_. That is, the maximum extension of the isoline at 3 µT (or 10 µT) projected to the ground.\
Typically the distances are taken from the axis of the power line considered.

----------------------------

## The project

The code calculates the magnetic induction field values B generated by high (AT) and medium (MT) voltage power lines and the corresponding DPA. In particular, it has 4 main functions available both for _single triads_ and _double triads_:
- B value (µT) in a given "point of interest" of coordinates _(xp, yp)_;
- B values (µT) in a 2D grid having the "point of interest" _(xp, yp)_ in its center;
- graphical representation of the mentioned 2D grid of B values (having the "point of interest" _(xp, yp)_ in its center);
- estimate of the so-called DPA (_distanza di prima approssimazione_) for the given configuration at \'lim_val\' µT from the cables' center of gravity abscissa. Suggested lim_values: 3 or 10 µT [D.P.C.M. 08.07.2003][3].

Power lines can be _overhead_ or _underground_. The active conductors, i.e. under voltage and traversed by current, are normally three in number, forming a three-phase _triad_ in which the voltage on the individual conductors is the same, but is out of phase by 120°. Some power lines consist of two triads, and are therefore called _double triads_ (doppia terna). The double triad can be _optimized_ or _non-optimized_. There is an optimized double triad when the pairs of conductors at equal height have different phases and concordant currents or vice versa. The non-optimized double triplet, on the other hand, is when the pairs of conductors at equal height have both the same or different phases and currents.

To perform the calculation, using phasors, it is necessary to provide the current circulating on the line (A), the phase (°) and the spatial configuration of the conductors (m) in a plane orthogonal to the direction of the current. The given point where the magnetic induction field will be calculated lies in this plane.
These data can be found in the "[Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]" (published by E-Distribuzione), where some usual configurations are exemplified.

As a reference, a spatial coordinate system must be assumed. Its origin _must_ be placed:
- on the ground, in the center of the trellis' base in case of overhead power lines;
- on the ground, right above the middle line in case of underground power lines (the cables' depth will have negative values).

Moreover, the current phases are usually indicated with integer numbers referring to the numbers on a clock face, where positive angles have counterclockwise orientation starting from 3 o'clock as zero angle. Examples:
- 4 - 330°
- 8 - 210°
- 12 - 90°

### Normalized computational model

The calculation methods are described in the two technical standards:
- **CEI 106-11** (Guida per la determinazione delle fasce di rispetto per gli elettrodotti secondo le disposizioni del DPCM 8 luglio 2003 - Linee elettriche aeree e in cavo);
- **CEI 211-4** (Guida ai metodi di calcolo dei campi elettrici e magnetici generati da linee e da stazioni elettriche).

The normalized model for calculating the magnetic induction field B produced in a cross section of an overhead or underground power line is a two-dimensional model that applies the law of Biot-Savart to determine the magnetic induction due to each conductor carried by current and therefore the law of superposition of the effects to determine the total magnetic induction, obviously taking into account the phases of the currents, supposedly symmetrical and balanced.

The following schematizations of the line are assumed:
1. all conductors are considered straight, horizontal, of infinite length and parallel to each other;
2. the currents are considered to be concentrated in the central axes of the overhead conductors or cables;
3. the currents induced respectively in the guard cables for overhead lines and in the shields for underground lines are not considered as their effect on magnetic induction is considered negligible;
4. the ground is considered perfectly transparent from the magnetic point of view and therefore the images of the conductors with respect to the ground are neglected, which at 50 Hz are at very high depths.

The calculation algorithm considers the following steps:
1. the effective values and phases of the sinusoidal currents on the conductors are represented by phasors (complex numbers): _Ii_ is the phasor of the current _i_, on conductor i;
2. with reference to a generic point of coordinates _(xp, yp)_ on the plane orthogonal to the conductors, the phasors of the spatial components of the total magnetic induction _Bx_ and _By_ are calculated through the formulas reported here;

![Formula5_x](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Formula5_x.gif "B_x")         ![Formula5_y](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Formula5_y.gif "B_y")         ![Formula5_z](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Formula5_z.gif "B_z")

3. the effective value of magnetic induction B is obtained with the formula:

![Formula_4](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Formula4.gif)

----------------------------

## Installation

In order to install the application _B\_field_ you first need to clone the repository [ELFproject](https://github.com/ElenaFusillo/ELFproject) and then use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.
The --editable option is necessary only during the code development in order not to have to reinstall the package at each code modification.

```bash
git clone https://github.com/ElenaFusillo/ELFproject
cd ELFproject
pip install --editable B_field
```

All the code in this readme must be executed inside a python environment, thus it could be necessary to add `py -m` or `python -m` before the instructions shown.

## Usage

### Input

Once installed, B_field can be exploited through the command line with `B_field <subcommand>`.\
To explore the inputs needed by the subcommands, the command line help can be used via `B_field <subcommand> -h` or `B_field <subcommand> --help`.

**These inputs are mandatory in number and order. Default configuration files can be found in the config_args folder.**

There are two main subcommands, that are:
- _single_, in case only one triad of cables is considered;
- _double_, in case a double triad of cables is considered.

#### single

Inputs can be provided individually:

```python
B_field single <xp>, <yp>, <diam_cables>, <I>, <ph_1_deg>, <x1>, <y1>, <ph_2_deg>, <x2>, <y2>, <ph_3_deg>, <x3>, <y3> -point -bidim -graph -dpa <lim_val>
```
or through a configuration file where all the input needed must be listed in order (as the _--help_ shows):

```python
B_field single @<single_arguments.txt> -point -bidim -graph -dpa <lim_val>
```

The **@** simbol indicates the input from a configuration file.

#### double

Similarly to the previous case, inputs can be provided individually:

```python
B_field double <xp>, <yp>, <diam_cables>, <A_I>, <A_ph_1_deg>, <A_x1>, <A_y1>, <A_ph_2_deg>, <A_x2>, <A_y2>, <A_ph_3_deg>, <A_x3>, <A_y3>, <B_I>, <B_ph_1_deg>, <B_x1>, <B_y1>, <B_ph_2_deg>, <B_x2>, <B_y2>, <B_ph_3_deg>, <B_x3>, <B_y3> -point -bidim -graph -dpa <lim_val>
```
or through a configuration file where all the input needed must be listed in order (as the _--help_ shows):

```python
B_field double @<double_arguments.txt> -point -bidim -graph -dpa <lim_val>
```

The **@** simbol indicates the input from a configuration file.

#### Optional arguments

As it can be seen in the previus bash scripts, the command line interface requires also one or more optional arguments. The optional arguments accept a long form and short form, moreover they can be chained together. They are:
- _-point_ / _-p_ :  it calculates the point estimate (µT) of the magnetic induction B in the point of interest (_xp_, _yp_) generated by the given single/double triad;
- _-bidim_ / _-b_ : it calculates the 2D estimate (µT) of the magnetic induction B in a 2D grid having at its center the point of interest (_xp_, _yp_);
- _-graph_ / _-g_ : it returns a graphical representation of the 2D estimate of the magnetic induction B around (_xp_, _yp_) - i.e. the result of the _-bidim_ optional argument;
- _-dpa_ lim_val / _-d_ lim_val : it returns the estimate (m) of the DPA (distanza di prima approssimazione) for the given configuration at 'lim_val' µT from the cables' center of gravity abscissa. Suggested lim_values: 3, 10 µT.

### Output

Once all the positional input arguments and one or more optional input arguments are provided, the code calculates what it was requested to. The results are given either in microTesla (µT) or in meters (m), according to the optional argument provided.

----------------------------

## Examples

#### single

Configuration A1 of the [Linea Guida ENEL][1], single triad:

```bash
B_field single @./examples/Argom_Bsingle.txt -point -bidim -graph -dpa 3

In point of coordinates ( -20.5 , 1.0 ), the magnetic induction is  2.99  microTesla.


------Grid of B field values (microTesla)------
----Point of interest in the matrix center-----

 [[2.46 2.57 2.69 2.82 2.95 3.1  3.25 3.42 3.6  3.8  4.01 4.24 4.49]
 [2.44 2.55 2.67 2.79 2.92 3.06 3.22 3.38 3.56 3.75 3.95 4.18 4.42]
 [2.42 2.53 2.64 2.76 2.89 3.03 3.18 3.34 3.51 3.69 3.89 4.11 4.35]
 [2.39 2.5  2.61 2.73 2.85 2.99 3.13 3.29 3.46 3.64 3.83 4.04 4.27]
 [2.37 2.47 2.58 2.69 2.82 2.95 3.09 3.24 3.4  3.58 3.76 3.96 4.18]
 [2.34 2.44 2.54 2.66 2.78 2.9  3.04 3.19 3.34 3.51 3.69 3.89 4.1 ]
 [2.31 2.41 2.51 2.62 2.74 2.86 2.99 3.13 3.28 3.45 3.62 3.81 4.01]
 [2.28 2.37 2.47 2.58 2.69 2.81 2.94 3.08 3.22 3.38 3.54 3.72 3.91]
 [2.25 2.34 2.44 2.54 2.65 2.76 2.89 3.02 3.16 3.31 3.47 3.64 3.82]
 [2.22 2.3  2.4  2.5  2.6  2.71 2.83 2.96 3.09 3.24 3.39 3.55 3.72]
 [2.18 2.27 2.36 2.45 2.56 2.66 2.78 2.9  3.03 3.16 3.31 3.46 3.63]
 [2.15 2.23 2.32 2.41 2.51 2.61 2.72 2.84 2.96 3.09 3.23 3.38 3.53]
 [2.11 2.19 2.28 2.37 2.46 2.56 2.66 2.78 2.89 3.02 3.15 3.29 3.44]]


The value of the DPA (Distanza di Prima Approssimazione) is  22.0  meters from the cables' center of gravity abscissa.
```

The result of the _-graph_ optional arguments is the following.

![Graph_single](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Example_single_graph.jpeg "Graph_single")

#### double

Configuration A9 of the [Linea Guida ENEL][1], non-optimized balanced double triad:

```bash
B_field double @./examples/Argom_Bdouble.txt -point -bidim -graph -dpa 3

In point of coordinates ( -5.0 , 1.0 ), the magnetic induction is  21.95  microTesla.


------Grid of B field values (microTesla)------
----Point of interest in the matrix center-----

 [[31.64 34.74 38.22 42.08 46.19 50.21 53.49 55.03 53.84 49.71 43.43 36.22 29.06]
 [28.9  31.34 33.97 36.72 39.42 41.82 43.49 43.93 42.77 39.94 35.8  30.96 25.97]
 [26.4  28.31 30.29 32.26 34.07 35.55 36.44 36.48 35.51 33.52 30.72 27.42 23.99]
 [24.13 25.64 27.14 28.57 29.83 30.78 31.28 31.2  30.45 29.06 27.14 24.89 22.54]
 [22.11 23.31 24.47 25.53 26.44 27.09 27.4  27.3  26.75 25.78 24.47 22.93 21.34]
 [20.32 21.28 22.19 23.01 23.68 24.15 24.37 24.3  23.92 23.26 22.36 21.32 20.25]
 [18.74 19.52 20.25 20.89 21.41 21.77 21.95 21.92 21.67 21.23 20.63 19.93 19.21]
 [17.34 17.98 18.57 19.09 19.51 19.81 19.97 19.97 19.83 19.54 19.15 18.68 18.2 ]
 [16.09 16.63 17.13 17.56 17.91 18.16 18.31 18.35 18.27 18.1  17.85 17.55 17.24]
 [14.99 15.44 15.86 16.23 16.53 16.75 16.9  16.96 16.94 16.85 16.69 16.51 16.31]
 [14.   14.39 14.75 15.07 15.33 15.54 15.68 15.76 15.77 15.73 15.65 15.54 15.42]
 [13.11 13.45 13.77 14.04 14.28 14.47 14.61 14.69 14.74 14.74 14.7  14.65 14.58]
 [12.31 12.61 12.89 13.13 13.35 13.52 13.66 13.75 13.81 13.84 13.84 13.82 13.78]]

The value of the DPA (Distanza di Prima Approssimazione) is  32.0  meters from the cables' center of gravity abscissa.
```

The result of the _-graph_ optional arguments is the following.

![Graph_double](https://github.com/ElenaFusillo/ELFproject/blob/main/images/Example_double_graph.jpeg "Graph_double")


----------------------------

## Test routines

Tests are stored inside _test_calculations.py_ and _test_cli.py_ files, with the support of all the fixtures needeed contained in _conftest.py_.
In order to perform the tests, it is just necessary to invoke the _pytest_ module:

```bash
pytest
============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: C:\Users\Elena\Documents\ELFproject
plugins: hypothesis-6.24.0
collected 8 items

test_calculations.py ......                                              [ 75%]
test_cli.py ..                                                           [100%]

============================== 8 passed in 0.05s ==============================
```

__TODO__ UPDATE THE TESTS AND CHANGE THIS SECTION

----------------------------

## External links

Here are a few useful links:

- [Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]
- [Arpae - campi elettromagnetici a bassa frequenza (ELF)][2]
- [Normativa nazionale campi elettromagnetici a bassa frequenza][3]
- [Normativa regionale campi elettromagnetici a bassa frequenza](https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/normativa/normativa-regionale/normativa-regionale-cem-a-bassa-frequenza)

[1]:https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/connessione_alla_rete/regole_tecniche/LineaGuidaDPA.pdf
[2]:https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/scopri-di-piu/campi-elettromagnetici-a-bassa-frequenza
[3]:https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/normativa/normativa-nazionale/normativa-nazionale-campi-elettromagnetici-a-bassa-frequenza

## Contacts
-----------

**Author:**

Elena Fusillo\
efusillo@arpae.it\
Arpae, Agenzia regionale per la prevenzione, l'ambiente e l'energia dell'Emilia Romagna\
Via Guido Alberoni, 17\
48121 Ravenna (RA), Italy

## License
[CC0 1.0 UNIVERSAL](https://creativecommons.org/publicdomain/zero/1.0/legalcode)
