# Scripting

## Shell

### Operators

There are two similar logical operators in shell scripting. `;` and `&&`. The difference is this:

```shell
# if ./tnp/folder does *not* exist the rm command will still run
# this will delete everything at the top-level folder
# this is bad :)
cd ./tnp/folder; rm -rf ./

# will only run the second command if the first succeeds
cd ./tnp/folder && rm -rf ./ 
```

A [discussion](https://stackoverflow.com/questions/6152659/bash-sh-difference-between-and) on the topic.

## Python

### Nesting Functions

Article [link](https://colinsblog.net/2023-08-05-nesting-functions/).

Function nesting is useful for scoping functions and maintaining logical flow of a program. In the example below the `format_country_name` function is only used within the `format_names` function.

```python
def format_names(names: list):
    def format_country_name(name: str) -> str:
        if name in EXCEPTIONS:
            return EXCEPTIONS[name]

        _name = unidecode(name.lower())
        matches = re.findall(
            "'|\,|\-|\.|\([a-zA-Z0-9_,'-. ]+\)|\[[a-zA-Z0-9_,'-. ]+\]", _name
        )

        if len(matches) > 0:
            matches.reverse()  # performs reverse on the original list. Has no return value
            for match in matches:
                _name = "{0} {1}".format(
                    re.sub("[\[\]\(\),'-.]", "", match), _name.replace(match, "")
                )

        return "_".join(_name.upper().split())

    formatted = []
    for name in names:
        formatted.append(format_country_name(name))

    return formatted
```

### Character Encoding

Encodings [link](https://docs.python.org/3/library/codecs.html#standard-encodings).

Acceted characters, `ó`, `é` etc., can be normalised to their ASCII (plain letter) counterparts. This can be done using the [unidecode](https://pypi.org/project/Unidecode/) module.
