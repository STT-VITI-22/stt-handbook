# Agile Laws | Boehm's Curve

“

The earlier you catch a defect in the software development lifecycle, the cheaper it is to fix it.

Barry Boehm



![Boehm's Curve](https://agilelaws.com/images/laws/boehms-curve.png)

Defects caught during the requirements or design phase cost significantly less to fix than those found during coding, testing, or post-release. This principle is central to modern software development practices, particularly Agile, where early feedback and defect prevention are key.

To address Boehm's Curve effectively, Agile teams adopt a "Shift-left" approach - moving activities like testing, validation, and quality assurance earlier in the development lifecycle. Together, Boehm's Curve and shifting left drive Agile teams to proactively identify and resolve issues as soon as possible, reducing rework and cost.

## How This Works in Agile Teams

Agile methodologies emphasize simplicity, efficiency, and delivering value quickly. Applying Occam's Razor in an Agile context encourages teams to:

1. Iterative Development:
   * Agile breaks work into small, incremental cycles (Sprints), allowing teams to develop, test, and refine features continuously. This enables early detection of defects.
2. Collaborative Design and Validation:
   * Agile teams leverage automation for continuous integration and testing, catching regressions early. This embodies the shift-left mindset, where testing occurs throughout development rather than at the end.
3. Automation and CI/CD:
   * Agile teams focus on building what is necessary right now rather than trying to predict future needs. This reduces waste and allows teams to pivot when requirements inevitably change.
4. Test-Driven Practices:
   * Approaches like Test-Driven Development (TDD) and Behavior-Driven Development (BDD) align with both Boehm's Curve and shifting left by ensuring defects are prevented or detected during coding, not after.

## Scenario

An Agile team is woring on an e-commerce platform:

* During Backlog Refinement, the Product Owner specifies that the system should apply discounts for bulk orders.
* The team collaboratively writes acceptance criteria and translates them into test cases (shifting left).
* Developers write unit tests while implementing the feature and run them continuously through an automated pipeline.
* During a Daily Scrum, a tester raises a question about edge cases, "What happens if a bulk discount overlaps with a flash sale?" This prompts immediate clarification and a code adjustment.
* An automated integration test catches a logic error in the discount calculation before the feature is finalized.

By detecting and addressing these issues early, the team avoids costly rework or customer-facing defects after release.

## Summary

Boehm's Curve underscores the high cost of late defect detection, while shifting left focuses on preventing and identifying defects early. Agile teams naturally embrace these principles by working iteratively, fostering collaboration, and integrating testing throughout the development cycle. By doing so:

* Reduce the cost and complexity of fixing defects.
* Deliver higher-quality software faster.
* Minimize risks to customers and the organization.

Agile teams thrive by embedding Boehm's Curve and shifting left into their workflows, ensuring that quality and cost-effectiveness go hand in hand.