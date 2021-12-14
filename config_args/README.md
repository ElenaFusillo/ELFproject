## Configuration files: CLI arguments

### Legend

- **A/M**: stands for Alta Tensione (AT) or Media Tensione (MT)
- **Number**: stands for the corresponding configuration inside [Linea Guida ENEL per l'applicazione del punto 5.1.3 dell'Allegato al DM 29.05.08][1]
- **OH/UG**: stands for OverHead or UnderGround power line
- **single/double**: stands for the number of triads in the configuration


### Order of the arguments

As can be seen via the help in the command line, the arguments' order is slightly different between the _single_ and _double_ option.

#### single

1. **xp**: Abscissa (m) of the point of interest
2. **yp**: Ordinate (m) of the point of interest
3. **diam_cables**: Diameter (mm) of the cables used
4. **current**: Current (A) - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line
5. **ph_1_deg**: Initial phase (deg) - cable 1
6. **x1**: Abscissa (m) of the first cable (1)
7. **y1**:Ordinate (m) of the first cable (1)
8. **ph_2_deg**: Initial phase (deg) - cable 2
9. **x2**: Abscissa (m) of the first cable (2)
10. **y2**:Ordinate (m) of the first cable (2)
11. **ph_3_deg**: Initial phase (deg) - cable 3
12. **x3**: Abscissa (m) of the first cable (3)
13. **y3**:Ordinate (m) of the first cable (3)

#### double

1. **xp**: Abscissa (m) of the point of interest
2. **yp**: Ordinate (m) of the point of interest
3. **diam_cables**: Diameter (mm) of the cables used
4. **A_current**: Current (A) of triad A - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line A
5. **A_ph_1_deg**: Initial phase (deg) - cable 1A
6. **A_x1**: Abscissa (m) of the first cable (1A)
7. **A_y1**: Ordinate (m) of the first cable (1A)
8. **A_ph_2_deg**: Initial phase (deg) - cable 2A
9. **A_x2**: Abscissa (m) of the first cable (2A)
10. **A_y2**: Ordinate (m) of the first cable (2A)
11. **A_ph_3_deg**: Initial phase (deg) - cable 3A
12. **A_x3**: Abscissa (m) of the first cable (3A)
13. **A_y3**: Ordinate (m) of the first cable (3A)
14. **B_current**: Current (A) of triad B - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line B
15. **B_ph_1_deg**: Initial phase (deg) - cable 1B
16. **B_x1**: Abscissa (m) of the first cable (1B)
17. **B_y1**: Ordinate (m) of the first cable (1B)
18. **B_ph_2_deg**: Initial phase (deg) - cable 2B
19. **B_x2**: Abscissa (m) of the second cable (2B)
20. **B_y2**: Ordinate (m) of the second cable (2B)
21. **B_ph_3_deg**: Initial phase (deg) - cable 3B
22. **B_x3**: Abscissa (m) of the third cable (3B)
23. **B_y3**: Ordinate (m) of the third cable (3B)



[1]:https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/connessione_alla_rete/regole_tecniche/LineaGuidaDPA.pdf