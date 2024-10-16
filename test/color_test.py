import logger as l

print("----------test start----------")

i = 0
print(f"\ntesting with nocolor: ")
l.set_nocolor(True)
l.set_verbosity(0)
l.log_deb("debug")
l.log_inf("message")
l.log_warn("warning")
l.log_err("error")

print(f"\n----------test end----------")
