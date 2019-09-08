========================
Python bridge for IceNLP
========================


.. image:: https://img.shields.io/pypi/v/icenlp_bridge.svg
        :target: https://pypi.python.org/pypi/icenlp_bridge

.. image:: https://img.shields.io/travis/sverrirab/icenlp_bridge.svg
        :target: https://travis-ci.org/sverrirab/icenlp_bridge

.. image:: https://readthedocs.org/projects/icenlp-bridge/badge/?version=latest
        :target: https://icenlp-bridge.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Simplify using IceNLP (Icelandic NLP library written in Java)


* Free software: Apache Software License 2.0
* Documentation: https://icenlp-bridge.readthedocs.io.


Features
--------

* Run Icelandic NLP from python using a local IceNLP server and this library


Example
-------

Start the local IceNLP server.  For example using docker:

``docker run -it --rm -p 1234:1234 sverrirab/icenlp``

Install locally using:

``pip install icenlp_bridge``

Your code might look like this:

>>> from icenlp_bridge import parse
>>> print(parse('Vá hvað þetta var einfalt!'))


``[InjP Vá au ] {*SUBJ [NP hvað fshen ] } {*SUBJ> [NP þetta fahen ] } [VPb var sfg3eþ ] {*COMP< [AP einfalt lhensf ] } ! !``


You can also pipe files into icenlp_bridge

``cat texti.txt | python -m icenlp_bridge``

For connection options see `python -m icenlp_bridge --help` and `init` documentation.

Credits
-------

This package is built on the excellent IceNLP_ library.  Information on the docker image can be found on DockerHub_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _IceNLP: https://github.com/hrafnl/icenlp
.. _DockerHub: https://cloud.docker.com/repository/docker/sverrirab/icenlp
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
