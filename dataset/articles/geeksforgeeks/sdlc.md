# Software Development Life Cycle (SDLC)

The Software Development Life Cycle (SDLC) is a structured process used to plan, design, develop, test, deploy, and maintain software. It ensures a systematic workflow and helps align software development with business goals and user requirements.

* Provides a clear and organized framework for managing development phases
* Helps in early detection of defects, reducing overall cost and time
* Ensures high-quality software delivery that meets user expectations

![software_development_life_cycle](https://media.geeksforgeeks.org/wp-content/uploads/20260402141628481400/software_development_life_cycle.webp)

## Stages of the Software Development Life Cycle

The Software Development Life Cycle (SDLC) typically consists of six or seven stages, depending on the development model used.

### Stage 1: Planning & Feasibility Analysis

This stage determines whether the project is technically, financially, and operationally feasible.

* ****Activities:**** Feasibility analysis, cost estimation, scheduling, resource planning
* ****Output:**** Project Plan, Feasibility Report
* ****Key Roles:**** Project Managers, Senior Engineers, Stakeholders

![stage_1_planning_and_requirement_analysis](https://media.geeksforgeeks.org/wp-content/uploads/20260402141244395100/stage_1_planning_and_requirement_analysis.webp)

stage-1

### Stage 2: Requirement Specification (SRS)

In this stage, detailed functional and non-functional requirements are documented clearly and approved by stakeholders.

* ****Activities:**** Requirement gathering, validation, documentation
* ****Output:**** Software Requirement Specification (SRS)
* ****Key Roles:**** Business Analysts, Product Owners

![stage_2_defining_requirements](https://media.geeksforgeeks.org/wp-content/uploads/20260402141311916001/stage_2_defining_requirements.webp)

Stage-2

### Stage 3: System Design

In this stage, the approved requirements are transformed into a technical blueprint for implementation.

* ****High-Level Design (HLD): Defines system architecture, technology stack, database design, and major modules.****
* ****Low-Level Design (LLD):**** Specifies component logic, APIs, data structures, and workflows.
* ****Output:**** Design Document Specification (DDS)

![stage_3_designing_architecture](https://media.geeksforgeeks.org/wp-content/uploads/20260402141334253101/stage_3_designing_architecture.webp)

Stage-3

### Stage 4: Development (Coding)

Developers build the software based on the approved design.

* ****Activities:**** Coding, code reviews, unit testing, version control management
* ****Tools:**** IDEs, version control systems, debuggers
* ****Output:**** Source code, executable application
* ****Key Roles:**** Frontend, Backend, Full Stack Developers

![stage_4_developing_product](https://media.geeksforgeeks.org/wp-content/uploads/20260402141356502809/stage_4_developing_product.webp)

Stage-4

### Stage 5: Testing

Testing ensures the software meets requirements and is free from defects before release.

****Types of Testing include:****

* ****Unit Testing****: Verifies individual components
* ****Integration Testing****: Ensures modules work together
* ****System Testing:**** Validates the complete system
* ****User Acceptance Testing (UAT)****: Confirms business requirements are met

****Output: T****est cases, defect reports, and quality metrics.

![stage_5_product_testing_and_integration](https://media.geeksforgeeks.org/wp-content/uploads/20260402141414537006/stage_5_product_testing_and_integration.webp)

Stage-5

### Stage 6: Deployment

The tested software is released to users.

* ****Activities:**** Production setup, deployment, smoke testing
* ****Modern Approach:**** Continuous Integration and Continuous Deployment (CI/CD) pipelines for faster and reliable releases
* ****Output:**** Live application
* ****Key Roles:**** DevOps Engineers, Release Managers

![stage_6_deployment_and_maintenance_of_products](https://media.geeksforgeeks.org/wp-content/uploads/20260402141439650124/stage_6_deployment_and_maintenance_of_products.webp)

Stage-6

### Stage 7: Maintenance

Post-deployment support ensures long-term usability.

* ****Activities:**** Bug fixes, performance tuning, updates, feature enhancements
* ****Output:**** Patches, updates, new versions
* ****Key Roles:**** Support Engineers, Developers

## Software Development Life Cycle Models

Software Development Models are structured frameworks that guide the planning, execution, and delivery of software projects. They define the sequence of development stages, such as requirements, design, coding, testing, and deployment.

### Common Models

* [Waterfall Model](https://www.geeksforgeeks.org/software-engineering/waterfall-model/)
* [Agile Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-agile-development-models/)
* [V-Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-sdlc-v-model/)
* [Spiral Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-spiral-model/)
* [Incremental Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-incremental-process-model/)
* [RAD Model](https://www.geeksforgeeks.org/software-engineering/software-engineering-rapid-application-development-model-rad/)

## Importance of SDLC

* Provides a clear and organized development framework.
* Improves planning, cost control, and project management.
* Ensures better quality through defined testing phases.
* Helps deliver software that meets user and business needs.

## Embedding Security into the SDLC

Security is integrated throughout the Software Development Life Cycle using a DevSecOps approach. It is built into every stage, from design to deployment, ensuring continuous protection.

* Vulnerabilities are identified and fixed early in the development process.
* Automated security checks are integrated into build and CI/CD pipelines.
* Security becomes a shared responsibility across development, testing, and operations teams.

Embedding security into the SDLC reduces risks, improves software resilience, and enables the delivery of safer applications.

## Common SDLC Mistakes Teams Make

Even experienced teams misuse SDLC by focusing on form over substance. Some frequent mistakes include:

* ****Treating documentation as the goal:**** Producing SRS and design documents without validating assumptions with real users.
* ****Late or inadequate testing:**** Testing is rushed or reduced due to time pressure, increasing post-release defects.
* ****Ignoring non-functional requirements:**** Performance, security, and scalability are considered too late.
* ****Poor communication between teams:**** Gaps between business, development, and QA lead to misaligned outcomes.
* ****Skipping feedback loops:**** Limited iteration and user feedback cause issues to surface only after deployment.
* ****Overengineering early:**** Designing overly complex solutions before validating core functionality.

Avoiding these mistakes requires continuous collaboration, early validation, and a mindset that values outcomes over processes.

## Real Life Example of SDLC

Banking Application Development using SDLC:

* ****Planning & Analysis:**** Identify banking features such as account management, fund transfers, and security requirements****.****
* ****Design****: Create UI designs, system architecture, databases, and technology stack.
* ****Development****: Implement frontend interfaces, backend services, and APIs.
* ****Testing:**** Conduct functional, performance, and security testing.
* ****Deployment & Maintenance****: Release the application and continuously monitor, fix defects, and add enhancements.

## Reasons for Project Failure Despite Following SDLC

Following SDLC does not automatically guarantee project success. Many projects fail because teams treat SDLC as a checklist rather than a decision-making framework.

* ****Poor requirement clarity:**** Requirements are documented but not deeply understood, leading to incorrect assumptions and rework.
* ****Weak stakeholder involvement:**** Limited feedback from users or business teams results in solutions that don’t solve real problems.
* ****Rigid execution:**** Teams follow the process mechanically and resist adapting to changing business or technical realities.
* ****Underestimated complexity:**** Risks related to scalability, integration, or performance are identified too late.
* ****Lack of ownership:**** Roles exist on paper, but accountability for outcomes is unclear.

SDLC provides structure, but success depends on how thoughtfully it is applied, not just whether it is followed.

