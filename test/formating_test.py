import logger as l

print("----------test start----------")

print("\ntesting tabs spacing")
l.set_verbosity(0)
l.log_deb("debug", tabs = 1)
l.log_inf("message", tabs = 2)
l.log_warn("warning", tabs = 3)
l.log_err("error", tabs = 4)

print("\ntesting global tabs spacing")
l.set_verbosity(0)
l.set_global_tabs(1)
l.log_deb("debug", tabs = 1)
l.log_inf("message", tabs = 2)
l.log_warn("warning", tabs = 3)
l.log_err("error", tabs = 4)

print("\n----------test end----------")
