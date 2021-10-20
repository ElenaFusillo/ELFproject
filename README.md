# B_field

Low frequency electromagnetic fields, commonly referred to as ELF (Extremely Low Frequency), are emitted at frequencies between 0 Hz and 3000 Hz.
The main artificial sources of ELF fields are the transmission and distribution systems of electricity (power lines) consisting of:

- **power lines** with different voltage levels (very high, high, medium, low), in which alternating electric current flows at a frequency of 50 Hz;
- **substations and electrical transformer cabins**, to transfer electricity between power lines at different voltages.


### Characteristics of power lines

The main characteristics of a power line are the operating voltage, measured in kilovolts (kV) and the current carried, which is expressed in Ampére (A).
The operating voltages of power lines in Italy are:

- 0.4 and 15 kV, for low and medium voltage;
- 132, 220 and 380 kV for high and very high voltage.

The intensity of the _electric field_ generated depends on the operating voltage, which is constant within the line, and increases as the line voltage increases. In space, the intensity of the electric field decreases as the distance from the line and the height of the conductors increase.
The electric field has the characteristic of being easily shielded from objects such as wood, metal, but also trees and buildings.
The unit of measurement of the electric field is the Volt/meter (V/m).

The intensity of the _magnetic field_, on the other hand, depends proportionally on the circulating current. This current varies over time depending on the energy demands. On average it can take values from a few amps to a thousand amps, depending on the power line. The intensity of the magnetic field also decreases, in space, as the distance from the line and the height of the conductors increase. Unlike the electric field, however, the magnetic field cannot be shielded from most commonly used materials.
The unit of measurement of the magnetic field is the microTesla (µT).

Power lines can be overhead or underground. The active conductors, i.e. under voltage and traversed by current, are normally three in number, forming a three-phase triad in which the voltage on the individual conductors is the same, but is out of phase by 120°. Some power lines consist of two triads, and are therefore called double triads. The double triad can be optimized or not optimized.


### Assessment of human exposure: ARPAE

The assessment of human exposure to low-frequency electric and magnetic fields is carried out by Arpae in order to assess the impact of the sources on the territory and compare the levels with the limits set by the legislation for the protection of human health.

This evaluation is made by means of measurements (monitoring, source control, response to complaints and requests from local and regional authorities) or simulations. The latter, which involve the use of forecasting models, are particularly important in the preventive phase, such as in VIA (valutazioni di impatto ambientale) and in the authorization procedures for power lines.


----------------------------

The code calculates the magnetic induction field values B generated by high (AT) and medium (MT) voltage power lines, both overhead and underground. 

To perform the calculation, using phasors, it is necessary to provide the current circulating on the line, the phase and the spatial configuration of the conductors in a plane orthogonal to the direction of the current.
These data can be found in the "[Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]" (published by E-Distribuzione).

As a reference, a coordinate system must be assumed. For simplicity, its origin can be placed:
- on the ground, in the center of the trellis' base in case of overhead power lines;
- on the ground, right above the middle line in case of underground power lines.

The calculation methods are described in the two technical standards:
- CEI 106-11 (Guida per la determinazione delle fasce di rispetto per gli elettrodotti secondo le disposizioni del DPCM 8 luglio 2003 - Linee elettriche aeree e in cavo);
- CEI 211-4 (Guida ai metodi di calcolo dei campi elettrici e magnetici generati da linee e da stazioni elettriche).


Furthermore, the code estimates the so-called DPA (_distanza di prima approssimazione_) with reference to the limits indicated in the D.P.C.M. 08/07/2003 and graphically represents the results.

This is because for the purposes of assessing the exposure of the population, and therefore urban planning, only the magnetic induction field B and not the electric field E is considered as the only indicator.


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
where `<single_arguments.txt>` is the configuration file where all the input needed are listed in order.
The module's help is useful to know the specific order of these input, via `B_field -h`.

### double


#show the expected output,  inline the smallest example, links to examples more complicated
#istruzioni per eseguire i test? necessario


## External links

Here are a few useful links:

- [Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]
- [Arpae - campi elettromagnetici a bassa frequenza (ELF)](https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/scopri-di-piu/campi-elettromagnetici-a-bassa-frequenza)
- [Normativa nazionale campi elettromagnetici a bassa frequenza](https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/normativa/normativa-nazionale/normativa-nazionale-campi-elettromagnetici-a-bassa-frequenza)
- [Normativa regionale campi elettromagnetici a bassa frequenza](https://www.arpae.it/it/temi-ambientali/campi-elettromagnetici/normativa/normativa-regionale/normativa-regionale-cem-a-bassa-frequenza)

[1]:https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/connessione_alla_rete/regole_tecniche/LineaGuidaDPA.pdf

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