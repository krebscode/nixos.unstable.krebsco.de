`unstable@2016-09-24``
####################################################
:date: 2016-09-24 09:41
:modified: 2016-09-24 09:41
:author: mic92
:tags:  b9df84cd

Nix-Container with IPs break
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because `b9df84cd` refactored the syntax of the nix expression,
building container with private network broke.

This [pull request](https://github.com/NixOS/nixpkgs/pull/18915) fix it.
