# SonPy

_Python interface for Sonnet._

Sonnet is a commercial (with a free version) EDA software for high-frequency RF/MW electromagnetic analysis. It is focused on 2.5D planar structures, like PCBs or chips.

SonPy is a Python module that lets the user manipulate and simulate Sonnet Software projects through Python. Please see the documentation in SonPy.pdf for more information.

**NOTE:** SonPy does not work properly with current Sonnet versions. I forked the latest version to fix at least a few of these issues for myself. The new `example3.py` works with the current Sonnet version (18.53), but a lot of work still needs to be done. Anyone is welcome to contribute.

**NOTE:** I am also planing to make SonPy more usable without importing a GDSII file by implementing functions to create those structures (addPoly is already there). This allows the better usage with the free version, as the free version is missing `gds.exe` to import GDSII files.

## Changelog

**Master (2022-05-19)**
Functionality/fixes added since the fork of version 1.1:

* changed a few things to make SonPy work with the current version of Sonnet (18.53), this includes so far:
    - Removed gds_stream/gds_object in favour of lay_name for Polygon
    -  Fixed coordinate translation, the box seems to be the relevant reference, not the polygons
* added the function addPoly to add polygons to the project

**Version 1.1 (2018-09-16)**

Functionality to handle brick layers added.

* added self.bricks = [] to Geo class
* added Brick class
* added section to readProject to initialize BRI and BRA definitions
* added section to printProject to print BRI and BRA material initiations
* added parameter to setTlayer to match defined brick to brick material
* made necessary additions to set tlayer parameters appropriate if brick material defined
* wrote addBrick function which takes in erel, loss_tan, cond, and brick name
