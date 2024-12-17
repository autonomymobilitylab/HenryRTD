Read The Docs documentation for Henry
======================================

This repository is generated into Read The Docs documentation at https://henrydocs.readthedocs.io.

Contributing
------------

Add any new documentation pages to ``docs/sources/`` in `ReST format (.rst) <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
and add the name of page to the table of contents at ``docs/sources/index.rst``.

Add new images to ``docs/source/images`` and if you have for example drawio versions add them to ``docs/source/images_source``.

Readthedocs handles the rest, rebuilding the page when changes are pushed here.

Note that the documentation is public! Do not store sensitive information here.

ReadTheDocs ReST syntax tips
----------------------------

* Use \``double backticks\`` for ``inline code snippets`` or ``file names``.

  * For code, you can also use \:code:\`code snippet\`. Highlighting is supported for bash and Python with \:bash:\`code snippet\`.

* For code blocks, see the `Sphinx documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_.
* Hyperlinks without a label work as is, but you can also add a label like this: ```link text <https://example.com>`_``. Note the space between the text and the link, and the trailing underscore.
* Use \*single asterisks\* for *italics* and \*\*double asterisks\*\* for **bold text**.
* Bulleted lists are created with a \* at the beginning of each line, and numbered lists with the number followed by a period. Lists can be nested by indenting with spaces.

  * For nested lists, add a newline before and after the nested portion, and line up the bullet for the nested list with the start of the text for the parent. Otherwise, ReST might think it is a definition and makes the parent bold. See the source of this file for an example. 

* The title for a page is underlined with ``=`` and sections with ``-``.
* Tags for sections can be added with ``.. _section-name:`` above the title of a section, and then linked to with ``:ref:`section-name```. For linking to another page, use ``:doc:`page name```.
* To separate paragraphs, add a blank line between them.

Setup
-----

A webhook for notifying Readthedocs of any pushed changes has been configured for this repo in Github with the URL and secret from the Integrations page in Readthedocs (instructions `here <https://docs.readthedocs.io/en/stable/guides/setup/git-repo-manual.html#manual-integration-setup>`_).

The Readthedocs account is managed by Eelis.