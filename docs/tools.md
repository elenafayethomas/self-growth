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

### Debugging

To debug what is going wrong with a Git command, use `GIT_TRACE`. `GIT_CURL_VERBOSE` can also be used for more details. For example:

```shell
GIT_TRACE=1 git commit -m "fix: bug in code"
```

For `GIT_CURL_VERBOSE`:

```shell
GIT_CURL_VERBOSE=1 GIT_TRACE=1 git pull
```

More details are available in Git's [docs](https://git-scm.com/book/ms/v2/Git-Internals-Environment-Variables).

### Branches

To get all remote branches, run `git branch -r`. To then prune all branches without a remote, run `git remote prune origin`.

There is a [script](../scripts/git-prune.sh) to remove local branches that were created from remote branches in the scripts folder. This is a bit more specific in its use case.

### Configuration

[Link](https://blog.gitbutler.com/how-git-core-devs-configure-git/).

## AWS Lambda

### Logging

To format logs in AWS lambda: https://docs.powertools.aws.dev/lambda/typescript/latest/core/logger/#custom-log-formatter. This can be as basic as the `serviceName`, but many other fields can be added for log enrichment. An example:

```typescript
import { LogFormatter, Logger, LogItem } from "@aws-lambda-powertools/logger"
import { LogAttributes } from "@aws-lambda-powertools/logger/lib/cjs/types/Log"
import { UnformattedAttributes } from "@aws-lambda-powertools/logger/lib/cjs/types/Logger"

/**
 * Custom log formatter that sets all fields. This includes `service`, which is required for log partitions to work
 * @see https://docs.powertools.aws.dev/lambda/typescript/latest/core/logger/#custom-log-formatter
 */
class MyServiceLogFormatter extends LogFormatter {
  formatAttributes(attributes: UnformattedAttributes, additionalLogAttributes: LogAttributes): LogItem {
    const baseAttributes: LogAttributes = {
      logLevel: attributes.logLevel,
      message: attributes.message,
      service: attributes.serviceName,
      awsRequestId: attributes.lambdaContext?.awsRequestId,
      function: {
        name: attributes.lambdaContext?.functionName,
        arn: attributes.lambdaContext?.invokedFunctionArn,
        memoryLimitInMB: attributes.lambdaContext?.memoryLimitInMB,
        version: attributes.lambdaContext?.functionVersion,
        coldStart: attributes.lambdaContext?.coldStart,
      },
      timestamp: this.formatTimestamp(attributes.timestamp),
      logger: {
        sampleRateValue: attributes.sampleRateValue,
      },
      awsRegion: attributes.awsRegion,
    }

    const logItem = new LogItem({ attributes: baseAttributes })
      .addAttributes(additionalLogAttributes)
    
    return logItem
  }
}

export const logger = new Logger({
  logFormatter: new MyServiceLogFormatter(),
})
```

## Podman

Daemonless Docker.

### Links

* Installing on WSL: [link](https://dev.to/bowmanjd/using-podman-on-windows-subsystem-for-linux-wsl-58ji).
* CLI reference: [link](https://docs.podman.io/en/stable/markdown/podman-container.1.html).
* Buildpack with Podman: [link](https://buildpacks.io/docs/for-app-developers/how-to/special-cases/build-on-podman/).
* Fixing `docker.io` not being recognised as a registry by Podman: [link](https://github.com/containers/podman/issues/16096).
