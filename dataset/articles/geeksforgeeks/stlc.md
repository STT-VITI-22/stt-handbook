# Software Testing Life Cycle (STLC)

The Software Testing Life Cycle (STLC) is a structured process that defines the steps involved in testing a software product. It ensures that the application meets quality standards and user expectations. STLC is an essential part of the Software Development Life Cycle (SDLC) and guides QA teams in testing activities.

* Provides a systematic approach to plan, execute, and manage testing
* Helps in early detection of defects and improves software quality
* Ensures complete test coverage and proper reporting of results

## ****Phases of STLC****

There are six major phases of the Software Testing Life Cycle (STLC) that we are discussing here in detail.

![image](https://media.geeksforgeeks.org/wp-content/uploads/20250929170953952296/image.png)

Phases of STLC

## ****1. Requirement Analysis****

[Requirement Analysis](https://www.geeksforgeeks.org/software-engineering/activities-involved-in-software-requirement-analysis/) is the first phase where the QA/testing team understands what needs to be tested.

* Review the Software Requirements Document (SRD) and related documents
* Interview stakeholders to gather additional information
* Identify ambiguities, inconsistencies, or missing requirements
* Review non-functional requirements such as performance, security, usability, and compliance
* Identify potential risks or challenges that may impact testing

## 2. Test Planning

[Test Planning](https://www.geeksforgeeks.org/software-testing/test-plan-software-testing/) is the most crucial phase where the overall test strategy and plan are created. The major activities carried out during the Test Planning phase include:

* Define testing objectives, scope, and priorities
* Develop a test strategy, including selection of manual or automated testing techniques
* Identify required testing environments, tools, and resources
* Define entry and exit criteria for each phase
* Estimate time, cost, and resource requirements
* Identify test deliverables and key milestones
* Assign roles and responsibilities to the testing team
* Incorporate risk-based testing to prioritize critical functionalities
* Review and approve the test plan

## 3. Test Case Development

The [Test Case Development](https://www.geeksforgeeks.org/software-testing/test-case/) phase testers design detailed test cases and prepare the necessary test data. The main activities performed during the Test Case Development phase in include:

* Identifying the test cases that will be developed
* Writing test cases that are clear, concise and easy to understand
* Creating test data and test scenarios that will be used in the test cases
* Identifying the expected results for each test case
* Reviewing and validating the test cases
* Updating the requirement traceability matrix (RTM) to map requirements to test cases

## 4. Test Environment Setup

[Test Environment Setup](https://www.geeksforgeeks.org/software-testing/test-environment-a-beginners-guide/) defines the hardware, software and network conditions under which testing will be executed. The activities involved in the Test Environment Setup phase include:

* Install and configure required software, tools and databases.
* Set up servers, browsers, operating systems and devices.
* Prepare access credentials and permissions.
* Validate the environment before test execution.
* Test environments can be physical, virtual, or cloud-based. For Agile/DevOps environments, ensure integration with CI/CD pipelines and test automation tools.

## ****5. Test Execution****

In [Test Execution](https://www.geeksforgeeks.org/software-testing/test-execution-for-software-testing/) phase prepared test cases are executed in the defined environment. The activities performed during the Test Execution phase include:

* Run manual or automated test cases.
* Log defects with details like severity and priority.
* Retest fixed defects (defect retesting).
* Perform regression testing if required.
* Collect and analyze test results.
* Document and share test reports.

## 6. Test Closure

[Test Closure](https://www.geeksforgeeks.org/software-testing/test-closure-in-software-testing/) is the final phase where testing activities are completed and documented. The final activities carried out during the Test Closure phase include:

* Prepare a Test Summary Report (test cases executed, pass/fail count, defects found/resolved).
* Ensure all defects are tracked and closed.
* Clean up the test environment.
* Archive test cases, data and reports.
* Conduct a retrospective for lessons learned.
* Share knowledge with stakeholders.

## STLC vs SDLC

| Aspect | SDLC (Software Development Life Cycle) | STLC (Software Testing Life Cycle) |
| --- | --- | --- |
| ****Definition**** | A process that defines all phases of software development, from requirements gathering to deployment and maintenance. | A process that defines all phases of software testing, from requirement analysis to test closure. |
| ****Focus**** | Focuses on building the software. | Focuses on verifying and validating the software. |
| ****Phases**** | Requirement gathering, Design, Development, Testing, Deployment, Maintenance. | Requirement analysis, Test planning, Test case development, Test environment setup, Test execution, Test closure. |
| ****Performed By**** | Developers, business analysts, project managers, QA team (partly). | QA/testing team primarily. |
| ****Deliverables**** | Software product, design documents, user manuals, deployment package. | Test plan, test cases, defect reports, test summary, closure report. |
| ****Objective**** | To deliver a working software product that meets user requirements. | To ensure the product is defect-free and high quality before release. |
| ****Relation**** | Covers the entire lifecycle of the software. | Part of SDLC, focused only on testing. |


