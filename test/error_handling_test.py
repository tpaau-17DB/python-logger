import logger as l
from logger.logger import set_global_tabs

print("----------test start----------")

print("trying to set verbosity to an incorrect value")
l.set_verbosity(-1)
l.set_verbosity(4)
l.set_verbosity("a")

print("\nattempting to set PRINT_DATETIME to an incorrect value")
l.set_print_datetime(1)
l.set_print_datetime("a")

print("\nattempting to set datetime format to an incorrect value")
l.set_datetime_format(5)
l.set_datetime_format(True)

print("\nattempting to set global tabs to an incorrect value")
l.set_global_tabs("a")

print("----------test end----------")
