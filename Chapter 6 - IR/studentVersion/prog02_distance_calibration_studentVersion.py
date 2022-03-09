# importald be a LED es MCP3008 klasszokat
# a raspberry_functions_studentVersion modulbol importald be a read_2column_files es az interpolate1d fuggvenyeket


ir = # inicializalj egy LEDet a GPIO 2es pinre
mcp = # inicializald az ADC konvertert a 7es csatornaval

calib_file = # add meg a feszultseg tavolsag kalibralas fajl nevet sztring formaban (ha kell az utvonalat is)
volt, distance = # a read_2column_files fuggvennyel olvasd ki a kalibracios ertekeket, figyelj a bemeneti parameterekre

# kapcsold be a LEDet

while True:
    current_voltage = # olvasd ki az ADC konverteren mert feszultseget
    current_distance = # az interpolate1d fuggvennyel interpolald a mert feszultseget, hogy megbecsuld a tavolsagot
    # nyomtasd ki a tavolsagot a kepernyore valami kisero szoveggel