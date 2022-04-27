cmd = ""
count = 10
def on_data_received():
    global cmd
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    basic.show_string(cmd)
    if cmd == "0":
        basic.show_number(0)
    elif cmd == "1":
        basic.show_arrow(1)
    elif cmd == "2":
        basic.show_arrow(2)
    elif cmd == "3":
        basic.show_arrow(3)
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

def on_forever():
    global count
    if count == 10:
        serial.write_string("!1:TEMP:" + ("" + str(input.temperature())) + "#")
    if count == 5:
        serial.write_string("!1:LIGHT:" + ("" + str(input.light_level())) + "#")
    count += -1
    if count == 0:
        count = 10
    basic.pause(1000)
basic.forever(on_forever)
