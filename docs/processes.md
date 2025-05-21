# Processes

## Contribution Guidelines

Contribution guidelines are important for both open source projects and for projects that span a company. GitHub have [guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) on how to write a `CONTRIBUTING.md` file with some good examples from projects such as [Ruby on Rails](https://github.com/rails/rails/blob/main/CONTRIBUTING.md) or the [Open Government](https://github.com/opengovernment/opengovernment/blob/master/CONTRIBUTING.md).

From having written contribution guidelines, it is best to keep them brief whilst providing links to more information. This is to allow for quick onboarding for people unfamiliar to the project whilst allowing people to have more in depth information on design guidelines, testing, and so on, if required.

## Architectural Decision Records (ADRs)

https://github.com/joelparkerhenderson/architecture-decision-record

ADRs should be concise and clear, using a templated format. They should provide context, a decision and the consequences of making that decision. Some examples of "good" ADR practices are:

* Rationale: Explain the reasons for doing the particular AD. This can include the context (see below), pros and cons of various potential choices, feature comparisons, cost/benefit discussions, and more.

* Specific: Each ADR should be about one Architectural Decision (AD), not multiple ADs.

* Timestamps: Identify when each item in the ADR is written. This is especially important for aspects that may change over time, such as costs, schedules, scaling, and the like.

* Immutable: Don't alter existing information in an ADR. Instead, amend the ADR by adding new information, or supersede the ADR by creating a new ADR.

