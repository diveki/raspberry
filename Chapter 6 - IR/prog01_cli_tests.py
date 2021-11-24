from gpiozero import LED, MCP3008

# inicializaljunk egy LEDet

ir = LED(2)

# teszteljuk, ki be kapcsolassal, villogassal a mukodeset
ir.on()
ir.off()
ir.blink()
ir.off()

# inicializaljuk az adc-t

mcp = MCP3008(channel=7)
print(mcp.voltage)

while True:
    print(mcp.voltage)