

class appconfig(object):
    pass

def parse(params:list):

    arg = appconfig()

    action =  params.pop(0)
    if action is None:
        raise Exception("Action not defined")

    datafile =  params.pop(0)
    if datafile is None:
        raise Exception("Datafile not defined")

    setattr(arg,'action',action)
    setattr(arg,'datafile',datafile)
    setattr(arg,'params',params)

    return arg