# Concepts

## Cardinality

https://chronosphere.io/learn/what-is-high-cardinality/

In observability terms, cardinality is the number of dimensions a single metric has. The higher the number of dimensions the higher the cardinality. For example, having time as a cardinality is infinite because there are an infinite number of combinations that are possible. Low cardinality is often ideal to help reduce data storage costs and improve query times.

Low cardinality can be achieved by reducing the number of possible combinations. This could be done by constraining time fields to be specific days in a week. Bucketing values into broader categories can also help to reduce the number of labels that have associated cardinalities.
