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
