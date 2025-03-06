# Tools

## isort

A Python package, [isort](https://pycqa.github.io/isort/) sorts Python packages in a file, or files. Especially useful when there are lots of dependencies for one file. Some examples of good, and bad, practice of imports are [below](#module-import-practices). There's also a good [article](https://realpython.com/python-import/) by [RealPython](https://realpython.com/) on the topic.

### Usage

```shell
isort fileone.py filetwo.py
```

All files:

```shell
isort .
```

Glob:

```shell
isort **/*.py
```

Get the diff before applying changes:

```shell
isort somefile.py --diff
```

### Module Import Practices

```python
# bad: unclear which module the imports belong to, never do this
from somemodule import *

# good: but depends on the nesting of the module, for example:
# somemodule.submodule.subsubmodule.some_file.some_func is gnarly
import somemodule

# good: though need to be careful if using uncommon abbreviations, could reduce clarity of code
import somemodule as somemod

# good: helps with nesting, though the top level namespace is lost so could reduce clarity
from somemodule import submodule
```

## Git

To debug what is going wrong with a Git command, use `GIT_TRACE`. `GIT_CURL_VERBOSE` can also be used for more details. For example:

```shell
GIT_TRACE=1 git commit -m "fix: bug in code"
```

For `GIT_CURL_VERBOSE`:

```shell
GIT_CURL_VERBOSE=1 GIT_TRACE=1 git pull
```

More details are available in Git's [docs](https://git-scm.com/book/ms/v2/Git-Internals-Environment-Variables).
