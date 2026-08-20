# What are microservices?

Published 23 September 2021

![A laptop rests atop a server, surrounded by other servers.](https://assets.ibm.com/is/image/ibm/adobestock_912021577?ts=1782334768172&dpr=off "Laptop in futuristic server room with blue lights")

## Microservices defined

Microservices, or microservices architecture, is a [cloud-native](https://www.ibm.com/think/topics/cloud-native) architectural approach in which a single application is composed of many loosely coupled and independently deployable smaller components or services.

Microservices typically:

* Have their own technology stack, inclusive of the database and data management model.
* Communicate with one another over a combination of [representational state transfer (REST) APIs](https://www.ibm.com/think/topics/rest-apis), event streaming and [message brokers](https://www.ibm.com/think/topics/message-brokers).
* Are organized by business capability, with the line separating services often referred to as a bounded context.

While much of the discussion about microservices has revolved around architectural definitions and characteristics, their value can be more commonly understood through fairly simple business and organizational benefits:

* Code can be updated more easily—new features or functionality can be added without touching the entire application.
* Teams can use different stacks and different programming languages for different components.
* Components can be scaled independently of one another, reducing the waste and cost associated with having to scale entire applications because a single feature might be facing too much load.

### What microservices are not

Microservices might also be understood in contrast with two preceding application architectures: monolithic architecture and [service-oriented architecture (SOA)](https://www.ibm.com/think/topics/soa).

The difference between microservices and monolithic architecture is that microservices compose a single application from many smaller, loosely coupled services as opposed to the monolithic approach of a large, tightly coupled application.

[The differences between microservices and SOA](https://www.ibm.com/think/topics/soa-vs-microservices) can be a bit less clear. While technical contrasts can be drawn between microservices and SOA, especially around the role of the [enterprise service bus](https://www.ibm.com/think/topics/esb), it’s easier to consider the difference as one of scope. SOA was an enterprise-wide effort to standardize the way all web services in an organization talk to and integrate with each other, whereas microservices architecture is application-specific.

.

## How microservices benefit the organization

Microservices are likely to be at least as popular with executives and project leaders as with developers. This is one of the more unusual characteristics of microservices because architectural enthusiasm is typically reserved for software development teams. The reason for this is that microservices better reflect the way many business leaders want to structure and run their teams and development processes.

Put another way, microservices are an architectural model that better facilitates a wanted operational model. In a 2021 [IBM survey of over 1,200 developers and IT executives](https://www.ibm.com/account/reg/signup?formid=urx-49970), 87% of microservices users agreed that microservices adoption is worth the expense and effort.

Here are just a few of the enterprise benefits of microservices:

### Independently deployable

Perhaps the single most important characteristic of microservices is that because the services are smaller and independently deployable, it no longer requires an act of Congress to change a line of code or add a new feature in an application.

Microservices promise organizations an antidote to the visceral frustrations associated with small changes taking huge amounts of time. It doesn’t require a Ph.D. in computer science to see or understand the value of an approach that better facilitates speed and agility.

But speed isn’t the only value of designing services this way. A common emerging organizational model is to bring together cross-functional teams around a business problem, service or product. The microservices model fits neatly with this trend. The model enables an organization to create small, cross-functional teams around one service or a collection of services and have them operate in an agile fashion.

Microservices’ loose coupling also builds a degree of fault isolation and better resilience into applications. And the small size of the services, combined with their clear boundaries and communication patterns, makes it easier for new team members to understand the code base and contribute to it quickly—a clear benefit in terms of both speed and employee morale.

### Right tool for the job

In traditional n-tier architecture patterns, an application typically shares a common stack, with a large, [relational database](https://www.ibm.com/think/topics/relational-databases) supporting the entire application. This approach has several obvious drawbacks—the most significant of which is that every component of an application must share a common stack, data model and database even if there is a clear, better tool for the job for certain elements. It makes for bad architecture, and it’s frustrating for developers who are constantly aware that a better, more efficient way to build these components is available.

By contrast, in a microservices model, components are deployed independently and communicate over some combination of REST, event streaming and message brokers—so it’s possible for the stack of every individual service to be optimized for that service. Technology changes constantly, and an application composed of multiple, smaller services is much easier and less expensive to evolve with more desirable technology as it becomes available.

### Precise scaling

With microservices, individual services can be individually deployed—but they can be individually scaled, as well. The resulting benefit is obvious: done correctly, microservices require less infrastructure than monolithic applications because they enable precise scaling of only the components that require it, instead of the entire application in the case of monolithic applications.

### There are challenges to microservices, too:

Microservices’ significant benefits come with significant challenges. Moving from monolith to microservices means a lot more management complexity - a lot more services, created by a lot more teams, deployed in a lot more places. Problems in one service can cause, or be caused by, problems in other services. Logging data (used for monitoring and problem resolution) is more voluminous, and can be inconsistent across services. New versions can cause compatibility with an earlier version issues. Applications involve more network connections, which means more opportunities for latency and connectivity issues. A DevOps approach can address many of these issues, but DevOps adoption has challenges of its own.

Nevertheless, these challenges aren’t stopping nonadopters from adopting microservices—or adopters from deepening their microservices commitments. The aforementioned [IBM survey data](https://www.ibm.com/account/reg/signup?formid=urx-49970) reveals that 56% of current non-users are likely or very likely to adopt microservices within the following two years. Consequently, 78% of current microservices users will likely increase the time, money and effort they’ve invested in microservices.

IBM DevOps

## Microservices both enable and require DevOps

Microservices architecture is often described as optimized for DevOps and [continuous integration](https://www.ibm.com/think/topics/continuous-integration) or [continuous delivery](https://www.ibm.com/think/topics/continuous-delivery), and in the context of small services that can be deployed frequently, it’s easy to understand why.

But another way of looking at the relationship between microservices and DevOps is that microservices architectures require DevOps to be successful. While monolithic applications have a range of drawbacks that have been discussed earlier in this article, they have the benefit of not being a complex distributed system with multiple moving parts and independent tech stacks. In contrast, given the massive increase in complexity, moving parts and dependencies that come with microservices, it would be unwise to approach microservices without significant investments in deployment, monitoring and lifecycle automation.

Rosalind Radcliffe provides a deeper dive on DevOps in the video:

## Key enabling tools and technologies

While just about any modern tool or language can be used in a microservices architecture, there are a handful of core tools that have become essential and borderline definitional to microservices:

### Containers, Docker and Kubernetes

One of the key elements of a microservice is that it’s small. There is no arbitrary amount of code that determines whether something is or isn’t a microservice, but “micro” is right there in the name.

When [Docker](https://www.ibm.com/think/topics/docker) ushered in the modern container era in 2013, it also introduced the compute model that would become most closely associated with microservices. Because individual [containers](https://www.ibm.com/think/topics/containers) don’t have the overhead of their own operating system, they are smaller and lighter weight than traditional [virtual machines](https://www.ibm.com/think/topics/virtual-machines) and can spin up and down more quickly, making them a perfect match for the smaller and lighter weight services found within microservices architectures.

With the proliferation of services and containers, orchestrating and managing large groups of containers quickly became one of the critical challenges. [Kubernetes](https://www.ibm.com/think/topics/kubernetes), an open source [container orchestration](https://www.ibm.com/think/topics/container-orchestration) platform, has emerged as one of the most popular orchestration solutions because it does that job so well.

### API gateways

Microservices often communicate through API, especially when first establishing their state. While it’s true that clients and services can communicate with one another directly, API gateways are often a useful intermediary layer, especially as the number of services in an application grows over time. An [API gateway](https://www.ibm.com/products/api-connect/api-gateway) acts as a reverse proxy for clients by routing requests, fanning out requests across multiple services, and providing additional security and authentication.

There are multiple technologies that can be used to implement API gateways. Among these technologies are [API management platforms](https://www.ibm.com/products/api-connect), but if the microservices architecture is being implemented using containers and Kubernetes, the gateway is typically implemented using Ingress or, more recently, [Istio](https://www.ibm.com/think/topics/istio).

### Messaging and event streaming

While best practice might be to design stateless services, the state nonetheless exists and services need to be aware of it. And while an API call is often an effective way of initially establishing state for a specific service, it’s not an effective way of staying up to date. A constant polling, “are we there yet?” approach to keeping services current isn’t practical.

Instead, it is necessary to couple state-establishing API calls with messaging or event streaming so that services can broadcast changes in state. This way, other interested parties can listen for those changes and adjust accordingly. This job is likely best suited to a general-purpose message broker, but there are cases where an event streaming platform, such as [Apache Kafka](https://www.ibm.com/think/topics/apache-kafka), might be a good fit. And by combining microservices with [event-driven architecture](https://www.ibm.com/think/topics/event-driven-architecture) developers can build distributed, highly scalable, fault tolerant and extensible systems that can consume and process large amounts of events or information in real time.

### Serverless

[Serverless](https://www.ibm.com/think/topics/serverless) architectures take some of the core cloud and microservices patterns to their logical conclusion. In the case of serverless, the unit of execution is not just a small service, but a function, which can often be just a few lines of code. The line separating a serverless function from a microservice is a blurry one, but functions are commonly understood to be even smaller than a microservice.

Where serverless architectures and [functions-as-a-service](https://www.ibm.com/think/topics/faas) platforms share affinity with microservices is that they are both interested in creating smaller units of deployment and scaling precisely with demand.

## Microservices and cloud services

Microservices are not necessarily exclusively relevant to [cloud computing](https://www.ibm.com/think/topics/cloud-computing). However, there are a few important reasons why they so frequently go together—reasons that go beyond microservices being a popular architectural style for new applications and the cloud being a popular hosting destination for new applications.

Among the primary benefits of microservices architecture are the usage and cost benefits associated with deploying and scaling components individually. While these benefits would still be present to some extent with on-premises infrastructure, the combination of small, independently scalable components coupled with on-demand, pay-per-use infrastructure is where real cost optimizations can be found.

Secondly, and perhaps more importantly, another primary benefit of microservices is that each individual component can adopt the stack best suited to its specific job. Stack proliferation can lead to serious complexity and overhead when you manage it yourself but using the supporting stack as cloud services can dramatically minimize management challenges. Put another way, while it’s not impossible to roll your own microservices infrastructure, it’s not advisable, especially when just starting out.

## Common patterns

Within [microservices](https://developer.ibm.com/tutorials/cl-ibm-cloud-microservices-in-action-part-1-trs/?mhsrc=ibmsearch_a&mhq=microservices) architectures, there are many common and useful design, communication and integration patterns that help address some of the more common challenges and opportunities, including:

### Backend-for-frontend (BFF) pattern

This pattern inserts a layer between the user experience and the resources that the experience calls on. For example, an app used on a desktop will have different screen size, display and performance limits than a mobile device. The BFF pattern allows developers to create and support one backend type per user interface using the best options for that interface, rather than trying to support a generic backend that works with any interface but may negatively impact frontend performance.

### Entity and aggregate patterns

An entity is an object distinguished by its identity. For example, on an e-commerce site, a product object might be distinguished by product name, type and price. An aggregate is a collection of related entities that should be treated as one unit. So, for the e-commerce site, an order would be a collection (aggregate) of products (entities) ordered by a buyer. These patterns are used to classify data in meaningful ways.

### Service discovery patterns

These help applications and services find each other. In a microservices architecture, service instances change dynamically due to scaling, upgrades, service failure and even service termination. These patterns provide discovery mechanisms to cope with this transience. [Load balancing](https://www.ibm.com/think/topics/load-balancing) can use service discovery patterns by using health checks and service failures as triggers to rebalance traffic.

### Adapter microservices patterns

Think of adapter patterns in the way you think of plug adapters that you use when you travel to another country. The purpose of adapter patterns is to help translate relationships between classes or objects that are otherwise incompatible. An application that relies on third-party APIs might need to use an adapter pattern to ensure the application and the APIs can communicate.

### Strangler application pattern

These patterns help manage refactoring a monolithic application into microservices applications. The colorful name refers to how a vine (microservices) slowly and over time overtakes and strangles a tree (a monolithic application).

## Antipatterns

While there are many patterns for doing microservices well, there are an equally significant number of patterns that can quickly get any development team into trouble. Some of these—rephrased as microservices “don’ts”—are as follows:

### Don’t build microservices

Stated more accurately, don’t start with microservices. Microservices are a way to manage complexity once applications have gotten too large and unwieldy to be updated and maintained easily. Only when you feel the pain and complexity of the monolith begin to sneak in is it worth considering how you might refactor that application into smaller services. Until you feel that pain, you don’t even really have a monolith that needs refactoring.

### Don’t do microservices without DevOps or cloud services

Building out microservices means building out distributed systems, and distributed systems are hard—and they are especially hard if you make choices that make it even harder. Attempting to do microservices without either proper deployment and monitoring automation, or managed cloud services to support your now sprawling, heterogenous infrastructure, is asking for a lot of unnecessary trouble. Save yourself the trouble so you can spend your time worrying about state.

### Don’t make too many microservices by making them too small

If you go too far with the “micro” in microservices, you could easily find yourself with overhead and complexity that outweighs the overall gains of a microservice architecture. It’s better to lean toward larger services and then only break them apart when they start to develop characteristics that microservices solve for—namely that it’s becoming hard and slow to deploy changes, a common data model is becoming overly complex, or that different parts of the service have different load/scale requirements.

### Don’t turn microservices into SOA

Microservices and SOA are often conflated with one another, given that at their most basic level, they are both interested in building reusable individual components that can be consumed by other applications. The difference between microservices and SOA is that microservices projects typically involve refactoring an application so it’s easier to manage, whereas SOA is concerned with changing the way IT services work enterprise-wide. A microservices project that morphs into an SOA project will likely buckle under its own weight.

### Don’t try to be Netflix

Netflix was one of the early pioneers of microservices architecture when building and managing an application that accounted for one-third of all Internet traffic—a kind of perfect storm that required them to build lots of custom code and services that are unnecessary for the average application. You’re much better off starting with a pace you can handle, avoiding complexity, and using as many off-the-shelf tools as you possible.

