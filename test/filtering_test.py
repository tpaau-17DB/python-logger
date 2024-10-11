import logger as l

print("----------test start----------")

i = 0
s = 0
while i < 4:
    print(f"\ntesting for verbosity == {i}")
    l.set_verbosity(i)

    if s == 0:
        l.log_deb("debug")
        l.log_inf("message")
        l.log_warn("warning")
        l.log_err("error")
    elif s == 1:
        l.log_deb("debug", override_prior=True)
        l.log_inf("message", override_prior=True)
        l.log_warn("warning", override_prior=True)
        l.log_err("error", override_prior=True)

    i += 1
    if i == 4 and s == 0:
        i = 0
        s = 1
        print("\ntesting all over again for override_prior as True")

print("----------test end----------")
