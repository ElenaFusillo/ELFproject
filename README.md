# B_field

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
The [D.P.C.M. 08.07.2003][3] "Fissazione dei limiti di esposizione, dei valori di attenzione e degli obiettivi di qualità per la protezione della popolazione dalle esposizioni ai campi elettrici e magnetici alla frequenza di rete (50 Hz) generati dagli elettrodotti" establishes three values that apply to different situations:
- _limite di esposizione_ (100 µT) applies to all areas accessible by the population;
- _valore di attenzione_ (10 µT), calculated as the median of the B values over 24 hours, applies to playgrounds, schools and places with daily human presence greater than 4 hours;
- _obiettivo di qualità_ (3 µT), calculated as the median of the B values over 24 hours, is applied in the design of new playgrounds, schools and places with daily human presence greater than 4 hours and in the design of new power lines near these settlements.

The assessment of human exposure to low-frequency electric and magnetic fields is carried out by Arpae in order to assess the impact of the sources on the territory and compare the levels with the limits set by the legislation for the protection of human health. Models and measurements are used in order to verify the compatibility of the territory with the constraint of the buffer zones of the power lines (DPA).

### Distanza di prima approssimazione

The magnetic induction field levels generated by the power lines in the area are evaluated through the DPA (distanza di prima approssimazione). That is, the maximum extension of the isoline at 3 µT projected to the ground. All distances are to be understood as distances from the axis of the power line considered.

----------------------------

The code calculates the magnetic induction field values B generated by high (AT) and medium (MT) voltage power lines, both overhead and underground. 

Power lines can be overhead or underground, indeed. The active conductors, i.e. under voltage and traversed by current, are normally three in number, forming a three-phase triad in which the voltage on the individual conductors is the same, but is out of phase by 120°. Some power lines consist of two triads, and are therefore called double triads (doppia terna). The double triad can be optimized or not optimized.

To perform the calculation, using phasors, it is necessary to provide the current circulating on the line, the phase and the spatial configuration of the conductors in a plane orthogonal to the direction of the current.
These data can be found in the "[Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]" (published by E-Distribuzione).

As a reference, a coordinate system must be assumed. For simplicity, its origin can be placed:
- on the ground, in the center of the trellis' base in case of overhead power lines;
- on the ground, right above the middle line in case of underground power lines.

The calculation methods are described in the two technical standards:
- CEI 106-11 (Guida per la determinazione delle fasce di rispetto per gli elettrodotti secondo le disposizioni del DPCM 8 luglio 2003 - Linee elettriche aeree e in cavo);
- CEI 211-4 (Guida ai metodi di calcolo dei campi elettrici e magnetici generati da linee e da stazioni elettriche).

----------------------------

Furthermore, the code estimates the so-called DPA (_distanza di prima approssimazione_) with reference to the limits indicated in the [D.P.C.M. 08.07.2003][3] and graphically represents the results.

----------------------------


## Installation

In order to install the application _B\_field_ you first need to clone the repository [ELFproject](https://github.com/ElenaFusillo/ELFproject) and then use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.
The --editable option is necessary only during the code development in order not to have to reinstall the package at each code modification.

```bash
git clone https://github.com/ElenaFusillo/ELFproject
cd ELFproject
pip install --editable B_field
```

The previous code must be executed inside a python environment, thus sometimes it could be necessary to add `py -m` before the pip instructions.

## Usage

Once installed, B_field can be exploited through the command line with `B_field <subcommand>`.
There are two main commands, that are:

### single

In case only one triad of cables is considered, the command to use will be

```python
B_field single <single_arguments.txt>
```
where `<single_arguments.txt>` is the configuration file where all the input needed are listed in order. The module's help is useful to know the specific order of these input, via `B_field -h`.

### double

In case a double triad of cables is considered, the command to use will be

```python
B_field double <double_arguments.txt>
```
where `<double_arguments.txt>` is the configuration file where all the input needed are listed in order.

----------------------------
#show the expected output,  inline the smallest example, links to examples more complicated
#istruzioni per eseguire i test? necessario
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
Elena Fusillo
efusillo@arpae.it
Arpae, Agenzia regionale per la prevenzione, l'ambiente e l'energia dell'Emilia Romagna
Via Guido Alberoni, 17
48121 Ravenna (RA), Italy

## License
[CC0 1.0 UNIVERSAL](https://creativecommons.org/publicdomain/zero/1.0/legalcode)
