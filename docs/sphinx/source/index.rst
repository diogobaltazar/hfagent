.. Your Project documentation master file, created by
   sphinx-quickstart on Thu Oct 14 2023.

Welcome to Your Project's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   contributing/contributing

docker run --rm -it -p 8000:8000 --network hfagent --name hfagent-docs ghcr.io/diogobaltazar/hfagent-docs:0.0.0 /bin/bash
sphinx-autobuild sphinx/source sphinx/build --host 0.0.0.0