Collect Case Western Reserve University Bearing Data in Python3
============================================

Notice
---------

This repository only modified the code so that the repository below can be used in Python3.  
original => https://github.com/Litchiware/cwru  

Usage
---------

```python
  import cwru_py3 as cwru
  data = cwru.CWRU("12DriveEndFault", "1797", 384)
```

Then, you can use ``data.X_train``, ``data.y_train``, ``data.X_test``, ``data.y_test``, ``data.labels``, ``data.nclasses`` to train and evaluate your data driven fault diagnostic algrithms.

Not have a local copy of CWRU Bearing data on your machine?
Don't be worry, These ``.mat`` files required by your code will be automatically downloaded from `Case Western Reserve University Bearing Data Center`_, renamed properly with their corresponding class, stored in ``(Your Work Directory)/Datasets/CWRU`` directory to avoid downloading in future.

Arguments
---------

The constructor of class ``cwru.CWRU`` has three arguments:

* **exp**: experiment, supporting ``"12DriveEndFault", "12FanEndFault", "48DriveEndFault"``
* **rpm**: rpm during testing
* **length**: length of the signal slice, namely ``X_train.shape[1]``

Install
-------

Install by pip:

  $ pip install cwru_py3

Or install manually:

  $ python setup.py install

Test
----

You can run unit test by:

  $ python -m unittest discover

.. _Case Western Reserve University Bearing Data Center: https://csegroups.case.edu/bearingdatacenter/pages/download-data-file 
