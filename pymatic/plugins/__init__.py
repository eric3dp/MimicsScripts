import pkgutil

#dynamically load plugin modules and packages
for finder, name, ispkg in pkgutil.iter_modules(['pymatic/plugins']) :
    print('importing pymatic.plugins.{0}'.format(name))
    exec('from pymatic.plugins.{0} import *'.format(name))
