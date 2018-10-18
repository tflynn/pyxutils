# pyxutils - Python utilities 

Misc python utilities focused on internals.


*paths*

Get (absolute) package path

::

  from pyxutils import paths
  paths.get_package_path(package_name='pyxutils')



Get (abolute) data path - default is <package dir>/data

::

  from pyxutils import paths
  paths.get_data_path(file_name='gettysburg.txt', package_name='pyxutils')
  

