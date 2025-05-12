# Concepts

## Cardinality

https://chronosphere.io/learn/what-is-high-cardinality/

In observability terms, cardinality is the number of dimensions a single metric has. The higher the number of dimensions the higher the cardinality. For example, having time as a cardinality is infinite because there are an infinite number of combinations that are possible. Low cardinality is often ideal to help reduce data storage costs and improve query times.

Low cardinality can be achieved by reducing the number of possible combinations. This could be done by constraining time fields to be specific days in a week. Bucketing values into broader categories can also help to reduce the number of labels that have associated cardinalities.

## Terraform Providers

https://www.hashicorp.com/en/blog/writing-custom-terraform-providers

New Relic user example: https://github.com/newrelic/terraform-provider-newrelic/blob/main/newrelic/resource_newrelic_user_management.go

## Hexagonal Architecture

Talk from Alistair Cockburn: https://www.youtube.com/watch?v=k0ykTxw7s0Y

Ports & Adapters/Interactors

Should always describe what ports are used *for*

* Driving ports: outputs (test harness)
* Driven ports: inputs (database, devices, receivers)

## TypeScript Modules

https://www.typescriptlang.org/docs/handbook/2/modules.html

JavaScript has (too many) ways of creating code modules. The newest method are ES modules (ESM) and the older method is CommonJS. ESM uses the `import` and `export` keywords. Like so:

```typescript
// @filename: sum.ts
export function sum(a: number, b: number) {
    return a + b
}

// @filename: main.ts
import { sum } from './sum'

sum(2, 4)
```

Aliases can also be used when importing:

```typescript
import { sum as add } from './sum'

add(2, 4)
```

Namespaces can also be flattened, much like in Python:

```typescript
import * as math from  './sum'

math.sum(2, 4)
```

Types can also be exported. This is useful so bundlers, such as [esbuild](https://esbuild.github.io/), know what can be discarded.

```typescript
// @filename: animals.ts
export type Cat = {
    age: number
    breed: string
    name: string
    isFluffy: boolean
}

// @filename: main.ts
import { type Cat } from './animals'
```

For using ESM with CommonJS set the compiler flag `esModuleInterop` to be true in `tsconfig.json`.

## Python Literals

Allows for type checking in Python. Available in the `typing` module. [Link](https://docs.python.org/3/library/typing.html#typing.Literal).

```python
type Mode = Literal["r", "rb", "w", "wb"]

def open_helper(file: str, mode: Mode) -> str:
    ...
```
