# pyutils - Python utilities 

Misc python utilities focused on internals.


*paths*

Get (absolute) package path

::

  from pyutils import paths
  paths.get_package_path(package_name='pyutils')



Get (abolute) data path - default is <package dir>/data

::

  from pyutils import paths
  paths.get_data_path(file_name='gettysburg.txt', package_name='pyutils')
  

