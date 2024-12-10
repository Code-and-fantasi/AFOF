Traceback (most recent call last):
  File "/usr/bin/pip", line 11, in <module>
    load_entry_point('pip==21.1.3', 'console_scripts', 'pip')()
  File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 489, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 2852, in load_entry_point
    return ep.load()
  File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 2443, in load
    return self.resolve()
  File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 2449, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "/usr/lib/python2.7/site-packages/pip/__init__.py", line 1, in <module>
    from typing import List, Optional
ImportError: No module named typing
