# What is software testing?

Published 09 July 2025

Updated 22 June 2026

![Abstract 3D render with a sphere and a torus](https://assets.ibm.com/is/image/ibm/adobestock_463710214?ts=1782132078941&dpr=off "Abstract blue sphere in spiral structure")

## Software testing, defined

Software testing is the process of evaluating and verifying that a software product or application functions correctly, securely and efficiently according to its specific requirements.

The primary benefits of robust testing include delivering high-quality software by identifying bugs and improving performance.

Today, software testing is deeply embedded in modern development practices, driven by Agile transformation, [DevOps](https://www.ibm.com/think/topics/devops) and [continuous integration/continuous delivery (CI/CD)](https://www.ibm.com/think/topics/ci-cd-pipeline) pipelines. Testing is no longer a final step before release—it begins at the design planning phase and continues after deployment.

This testing approach supports faster releases and reduces risk in rapidly changing [IT infrastructure environments.](https://www.ibm.com/think/topics/infrastructure) Practices like [shift-left testing](https://www.ibm.com/think/topics/shift-left-testing)—where testing begins earlier in the development cycle—help teams uncover issues sooner. Shift-right testing, focused on monitoring and validation in production, enables teams to adapt to real-world usage more quickly.

Modern software testing strategies continue to evolve in tandem with advances in [automation](https://www.ibm.com/think/topics/automation), [artificial intelligence (AI)](https://www.ibm.com/think/topics/artificial-intelligence) and [cloud-native](https://www.ibm.com/think/topics/cloud-native) architectures, such as [microservices](https://www.ibm.com/think/topics/microservices). As software grows more complex and release cycles accelerate, intelligent testing has become increasingly prevalent.

In a report from Fortune Business Insights, the global AI-enabled testing market size was valued at USD 856.7 million in 2024. It is projected to grow from USD 1,010.9 million in 2025 to USD 3,824.0 million by 2032, exhibiting a compound annual growth rate (CAGR) of 20.9% during the forecast period.1

.

## History of software testing

Software testing began alongside the development of software engineering, which emerged just after World War II. Computer scientist Tom Kilburn is credited with writing the first piece of software, which debuted on 21 June 1948, at the University of Manchester in England. It performed mathematical calculations through basic machine code instructions.

This shift marked the beginning of a broader view of testing, one that emphasized quality assurance as a critical focus. It became an integral part of the [software development lifecycle (SDLC)](https://www.ibm.com/think/topics/sdlc)—the structured process that teams use to create high-quality, cost-effective and secure software.

The 1990s and early 2000s saw the rise of automated testing, along with new practices like [test-driven development (TDD)](https://www.ibm.com/think/topics/test-driven-development). During this period, modular programming techniques like object-oriented programming (OOP), which organized software into modules, also gained popularity. This modular design made it easier to write focused tests for small parts of code, known as unit tests. The expansion of mobile and web applications further demanded new testing strategies, including performance, usability and security testing.

In the last decade, advances in [Agile methodologies](https://developer.ibm.com/articles/agile-method-everything-you-need-to-know/) and DevOps have fundamentally changed how teams build and deliver software. Testing has become continuous, automated and integrated into every phase of development and deployment. Many of today’s organizations leverage proprietary and [open source](https://www.ibm.com/think/topics/open-source) automation tools and [continuous testing](https://www.ibm.com/think/topics/continuous-testing) platforms (for example, Katalon Studio, Playwright, Selenium) to achieve quality assurance. These tools also help them gain velocity, scalability and customer trust.

IBM DevOps

## Why is software testing important?

In today’s interconnected world, the consequences of software defects are more severe than ever. Late delivery or software defects can damage a brand’s reputation, resulting in frustrated and dissatisfied customers. In extreme cases, a bug or defect can degrade interconnected systems or cause serious malfunctions.

Consider the incident involving Delta Air Lines in July 2024. A flawed software update from cybersecurity firm CrowdStrike led to widespread system crashes across Microsoft Windows platforms. Delta experienced the most severe operational impact among US airlines, with thousands of flight cancellations and estimated losses exceeding USD 500 million.2 This event highlights the vital importance of thorough testing, particularly when integrating third-party software into [mission-critical](https://www.ibm.com/think/topics/mission-critical-applications) systems.

Although testing itself incurs costs, companies can save millions of dollars per year in development and support by implementing effective testing techniques and QA processes. Early software testing identifies issues before a product is released to the market. The sooner development teams receive test feedback, the sooner they can address critical issues, such as:

* Architectural flaws

* Poor design decisions

* Invalid or incorrect functionality

* Security vulnerabilities

* Scalability issues

When development leaves ample room for testing, it improves software reliability, and high-quality applications are delivered with fewer errors. A system that meets or exceeds customer expectations can lead to increased sales, greater market share and improved [user experiences](https://www.ibm.com/think/topics/user-experience).

## Manual versus automated testing

Software testing falls primarily into two broad categories:

* Manual testing

* Automated testing

### Manual testing

Manual testing is the process where testers execute test cases manually without the assistance of automation tools. Testers perform actions like clicking buttons, entering text and verifying outputs, simulating how an end user would interact with the software.

Manual testing is typically used for exploratory testing, usability testing, and when the application is small enough that automating it might not be necessary.

### Automated testing

Automated testing uses scripts and tools to execute tests on software automatically. This fundamental approach is beneficial for repetitive testing tasks and for larger systems where executing the same tests multiple times is necessary.

Automated testing ensures that software can be tested more quickly and consistently. It also reduces human error and improves testing efficiency over time.

## Levels of software testing

In general, software testing occurs at four different levels—or stages—within the [software development](https://www.ibm.com/think/topics/software-development) lifecycle, each focusing on specific parts of the application:

* Unit testing

* Integration testing

* System testing

* Acceptance testing

Unit testing

[Unit testing](https://www.ibm.com/think/topics/unit-testing) validates that each software unit runs as expected. A unit is the smallest testable component of an application.

Integration testing

[Integration testing](https://www.ibm.com/think/topics/integration-testing) ensures that software components or functions work together effectively.

System testing

[System testing](https://www.ibm.com/think/topics/system-testing) entails the end-to-end performance of an entire system. This phase includes aspects of functional testing, nonfunctional testing, interface testing, stress testing and recovery testing.

Acceptance testing

Acceptance testing verifies whether the whole system works as intended.

## Types of software testing

There are many different types of software testing that fall under the levels discussed earlier, and they can typically be divided into two main categories:

* [**Functional testing**](https://www.ibm.com/think/topics/functional-testing) verifies whether a software application behaves according to specified requirements.

* **Nonfunctional testing** assesses how the software performs under various conditions, such as load, stress or across different environments.

The following lists outline common testing types within each category.

### Functional testing types

* **White-box testing:** White-box testing involves testing based on knowledge of the internal structure, logic and functions of the software being tested.

* **Black-box testing:** In black-box testing, a tester does not have any information about the internal workings of the software system.

* **Ad hoc testing:** In ad hoc testing, testers try to break or find bugs in an application without following predefined tests or documentation.

* **API testing:** [API (application programming interface)](https://www.ibm.com/think/topics/api) testing verifies that the interfaces between software components function correctly and reliably. [API testing](https://www.ibm.com/think/topics/api-testing) is an essential part of [API management](https://www.ibm.com/think/topics/application-performance-management), the software and processes that support an API’s lifecycle.

* **Exploratory testing:** Exploratory testing helps software testers uncover hard-to-predict scenarios and situations that can lead to software errors.

* **Regression testing:** [Regression testing](https://www.ibm.com/think/topics/regression-testing) checks whether new features break or degrade existing functionality. It ensures that recent changes haven’t introduced new defects.

* **Sanity testing:** Sanity testing evaluates whether specific functionalities work as expected. Testers can use it to verify menus, functions and commands at the surface level when there is no time for a full regression test.

* **Smoke testing:** Smoke testing is a preliminary software testing process that checks whether the basic functions of an application work correctly. It helps ensure that the build is stable enough for further testing.

* **User acceptance testing (UAT):** User acceptance testing (UAT) is a specific type of acceptance testing performed by the end users to confirm the system meets their needs and works in real-world scenarios.

### Nonfunctional testing types

* **Recovery testing:** Recovery testing verifies how the software responds and recovers from failures, ensuring that data and processes are restored correctly.

* **Performance testing:** Performance testing refers to how the software runs under different [workloads](https://www.ibm.com/think/topics/workload).

* **Load testing:** Load testing—a type of performance testing— evaluates performance under real-life [load balancing](https://www.ibm.com/think/topics/load-balancing) conditions.

* **Stress testing:** Stress testing examines the amount of strain the system can withstand before it fails.

* **Security testing:** Security testing validates whether software is open to hackers or other malicious types of vulnerabilities.

* **Usability testing:** Usability testing validates how well a customer can use a system’s user interface to complete a task efficiently and intuitively.

* **Compatibility testing:** Compatibility testing checks whether a software application functions as expected across various devices, [operating systems](https://www.ibm.com/think/topics/operating-systems), browsers and [network](https://www.ibm.com/think/topics/networking) environments.

## Software testing best practices

## The future of software testing

As the pace of software development accelerates and systems become increasingly complex, software testing continues to evolve in tandem. Here are some key trends shaping the future of testing.

### Low-code and no-code testing

As [low-code](https://www.ibm.com/think/topics/low-code) and [no-code](https://www.ibm.com/think/topics/no-code) platforms continue to gain popularity, new software testing tools are emerging that cater to nontechnical users. These tools simplify testing processes, enabling business users to easily create and run tests on applications they build. This capability speeds up the time to market without requiring technical expertise.

### IoT and edge testing

The rapid expansion of [Internet of Things (IoT)](https://www.ibm.com/think/topics/internet-of-things) devices presents unique challenges in terms of testing connectivity, security and performance in real-world conditions. As more devices rely on [edge computing](https://www.ibm.com/think/topics/edge-computing), testing tools must simulate diverse environments to ensure that software can perform reliably under varied network conditions.

### 5G and ultralow latency testing

Since the rollout of [5G](https://www.ibm.com/think/topics/5g), applications that require ultralow [latency](https://www.ibm.com/think/topics/latency), such as autonomous vehicles and remote healthcare, need specialized testing. Validating performance under high-speed, low-latency conditions has become crucial for mobile and edge-based apps.

### AI-driven predictive and self-healing systems

Self-healing systems powered by AI detect and automatically fix minor issues, reducing downtime. Predictive testing, driven by [machine learning (ML)](https://www.ibm.com/think/topics/machine-learning), enables teams to anticipate potential failures and address them before they disrupt production, which in turn makes software more resilient and reliable.

