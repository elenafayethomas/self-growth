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
