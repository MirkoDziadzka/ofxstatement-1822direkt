~~~~~~~~~~~~~~~~~~~~~~~
ofxstatement-1822direkt
~~~~~~~~~~~~~~~~~~~~~~~

`ofxstatement`_ plugin to support 1822direkt.com bank statements

`ofxstatement`_ is a tool
to convert proprietary bank statement to OFX format, suitable for
importing to GnuCash. Plugin for `ofxstatement`_ parses a particular
proprietary bank statement format and produces common data structure,
that is then formatted into an OFX file.

This project provides an `ofxstatement`_ plugin for the German bank
1822direkt.com

.. _ofxstatement: https://github.com/kedder/ofxstatement

1822direkt used to provide OFX downloads but canceld this without
warning last weekend.  Shame on them.

Using `ofxstatement`_ and this plugin, I  successfully converted the
standard CSV statements (the first of the two available) to OFX and
import this into my banking software.


Requirements
============

You need python 3.x to run this as ofxstament seems to requires python3

Setup
=====

Check if plugin is installed:

 $ ofxstatement list-plugins

 germany_1822direkt

Edit config (add your account id here)

 $ ofxstatement edit-config

 [1822direkt]

 plugin = germany_1822direkt

 account = 12345678



