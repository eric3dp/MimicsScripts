import pkgutil

#dynamically load plugin modules and packages
for finder, name, ispkg in pkgutil.iter_modules(['trimatic/plugins']) :
    print('importing trimatic.plugins.{0}'.format(name))
    exec('from trimatic.plugins.{0} import *'.format(name))
