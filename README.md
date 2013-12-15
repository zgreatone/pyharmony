pyharmony
=======

Python library for progarmmatically using a Logitech Harmony Link or Ultimate Hub.

A fork of (pyharmony)[https://github.com/petele/pyharmony] with the intent to:
- Make pip/setup.py installable.
- Unify improvments made in other forks.
- Configurable for Harmony Link/Hub differences.
- Better practices for project layout.
- Better error handling!

Original readme follows:

pyharmony
=========

Python library for connecting to and controlling the Logitech Harmony Link

Protocol
--------

As the harmony protocol is being worked out, notes are in PROTOCOL.md.

Status
------

* Authentication to Logitech's web service working.
* Authentication to harmony device working.
* Querying for entire device information
* Sending a simple command to harmony device working.

Usage
-----

To query your device's configuration state:

    PYTHONPATH="." python harmony --email user@example.com --password pass \
        --harmony_ip 192.168.0.1 show_config

For full argument information on the command-line tool:

    PYTHONPATH="." python harmony

TODO
----

* Figure out how to detect when the session token expires so we can get a new
  one.
* Figure out a good way of sending commands based on sync state.
* Is it possible to update device configuration?
