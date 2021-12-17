.. |badge-doc| image:: https://readthedocs.org/projects/coalition/badge/?version=latest
   :target: http://coalition.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |badge-version| image:: https://badge.fury.io/gh/MercenariesEngineering%2Fcoalition.svg
   :target: https://badge.fury.io/gh/MercenariesEngineering%2Fcoalition

.. |badge-coverage| image:: https://coveralls.io/repos/github/MercenariesEngineering/coalition/badge.svg?branch=development
   :target: https://coveralls.io/github/MercenariesEngineering/coalition?branch=development

.. |badge-tests| image:: https://travis-ci.org/MercenariesEngineering/coalition.svg?branch=master

|badge-doc| |badge-version| |badge-coverage| |badge-tests|

`Full online documentation is available on ReadTheDocs <http://coalition.readthedocs.io/en/latest/>`_.

Coalition
=========

**Coalition** is a lightweight open source **job manager** client-server application whose role is to control **job execution in a set of computers**. One computer acts as a **server** coordinating the list of jobs to be done. A set of physical (or virtual, eg. in the cloud) computers acting as **workers** is deployed, raising the global grid system ressources.

The server waits for incoming connections from workers requesting jobs. The server then assigns a job to a worker according to simple **affinity rules**. After the worker finishes the job, it informs the server of the job's execution status and asks for a new job.

*Coalition* should not be used on the public Internet but on **private LANs**, **cloud VLANs** or **VPNs** for security reasons.

*Coalition* has been successfully used in production notably for **renderfarms**.

*Coalition* provides:

- **Broadcast discovery** for workers to find the server without configuration;
- A **RESTfull Python API** based on `Twisted matrix <https://twistedmatrix.com>`_ for program-to-program communication;
- **Cloud ready** configurations to manage starting/termination of workers in the cloud;
- A **Web interface** for humans to control jobs, workers, affinities and to view status and logs;
- A **Database** interface for SQLlite and MySQL;
- A **Logging** system;
- An **Email notification** system;
- An **Access Control List** when connected to an **LDAP** server;
- **Unittests** of critical code parts;
- **Source code** and **documentation** on `the development platform <https://github.com/MercenariesEngineering/coalition>`_.

The current stable versions are 3.8 and 3.10.

The development version is |current-version|.

.. |current-version| include:: version

