
# The following functions will be moved to the different files
# if their complexity will be growing

# All functions have arguments parameter. Its point is that
# in mgmt_parse, we get user's input, if its first part is one of the
# commands described in MGMTOperationsConfiguration.COMMANDS_MAPPING
# we can just call the function mapped to the name with the rest of the arguments
# provided in user's input without any additional ifs and logic

def mgmt_chmod(arguments=None):
    ...


def mgmt_exit(arguments=None):
    ...


def mgmt_help(arguments=None):
    ...


def list_databases(arguments=None):
    ...


class MGMTOperationsConfiguration:
    COMMANDS_MAPPING = {
        "chmod": mgmt_chmod,
        "exit": mgmt_exit,
        "help": mgmt_help,
        "list_databases": list_databases
    }
