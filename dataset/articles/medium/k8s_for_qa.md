# Kubernetes for QA

Application development is changing. Some years ago, every project was a monolithic application. Nowadays, organizations are moving their business logic to the cloud and disassembling those monoliths into systems made up of loosely coupled microservices. There are a large number of reasons to do this — agility, reliability, scalability, and more. Testers must adapt to the new situation! It makes no sense to apply the same techniques and use the same tools in such a different scenario. In order to keep up-to-date and contribute to the team’s goals in terms of efficiency and quality, testers need to learn how to leverage Kubernetes’ potential for QA.

## What is Kubernetes?

Kubernetes (also known as K8s or just the Kube) is a very powerful automation tool for containerized applications. Containers are lightweight, virtually isolated environments where microservices can run, along with their dependencies and scripts. Containerization is key for [cloud-native development](https://napptive.com/introduction-to-cloud-native-development) because it contributes to the [Twelve-Factor App](https://12factor.net/) model, but it would fall short without an orchestrating tool.

In a cloud-native environment, multiple replicas of multiple microservices are scheduled in a series of machines on the cloud to ensure availability at all times. Some containers crash over time. Demand asks for horizontal scaling. The only way to efficiently manage such a large number of services is by using a tool that automates the operations — like Kubernetes.

## Leveraging Kubernetes for QA

Here you have three significant ways in which Kubernetes can help with software testing, [according to SauceLabs](https://saucelabs.com/blog/what-does-kubernetes-mean-for-software-testing):

## CI/CD Automation

Being an automating tool, Kubernetes fits perfectly in a CI/CD pipeline. You can package your automated tests and run them as part of a build pipeline against your deployment containers to get consistent results. In addition, you can [tag](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) tests depending on different parameters and run them in parallel using [jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/), reducing time costs.

## Ephemeral QA Environments

When using containers, you can run your tests in an exact copy of the production environment, with the added peace of mind of knowing you are the only one accessing to that instance. You can perform aggressive tests that could potentially ruin the environment because in case you do, you just have to destroy it and spin up a new one. Plus, the resulting logs reflect only all your activity.

## Shift-Left Testing

In cloud-native development, QA and Dev teams work closely from the early stages of development. Bugs need to be detected and fixed right away, so tests have to offer instant and detailed feedback. Kubernetes offer to both developers and testers the possibility of accessing a shared cluster for debugging and testing. This way, when a tester logs an issue, the developer can access all the necessary information and try to fix it right away and with confidence.

## Benefits of Kubernetes for testers

Summing up the previous section, we could say that Kubernetes brings to the QA table the following benefits:

* Cheap disposable environments, even production-like ones.
* Decreased dependence on shared environments, opening opportunities for more aggressive testing.
* Direct access to detailed logs — even logs that only contain data from your tests.
* The ability to get to a complicated failure state quickly.
* Unambiguous communication with developers.
* Instant feedback.

## QA tools for cloud-native development

At the beginning of the article, we mentioned that the development paradigm is changing, and that’s why QA needs to adapt. Traditional testing techniques no longer make sense, but which new ways of testing do we have? Ajit Singh at [Mindfire Solutions](https://www.mindfiresolutions.com/blog/2020/06/kubernetes-for-quality-assurance/) has summed them up in the following four:

## A/B testing

Kubernetes Canary Deployment easily allows having different release versions of software running at the same time. According to the configured percentages, a portion of the users is served the new version while the rest still access the current stable one. This provides valuable insights into the performance of new features before making them available to all users.

## Chaos engineering

This method consists of provoking problems in a system — like simulating a hardware failure or an increased load on a service — in order to check its performance and stability. This lets testers understand how it will behave in case of failure or unexpected situations. [Chaos Mesh](https://chaos-mesh.org/) is a well-known platform for this kind of test.

## Consumer-driven contract testing (CDC)

This methodology is used to check individual services of a system before deploying them. By making API calls, the tester can check if the responses comply to what a consumer of this service would expect from them. You can use [Pactflow](https://pactflow.io/) to implement CDC testing.

## Helm Tests

[Helm](https://helm.sh/) is a tool that lets you define, install and upgrade applications by using charts. A chart is a directory tree that may be packaged into a versionable archive to be deployed or shared. It may contain tests to validate that it worked as expected when it was installed. For example, you can use Helm tests to assert that your services are load-balancing correctly or that your credentials work.

## What you should know of Kubernetes as a tester

Finally, it is worth noting that, as a tester, you don’t need to be an expert on Kubernetes. [Citing Glenn Buckholz, Technical Manager at Coveros](https://techbeacon.com/app-dev-testing/testers-guide-leveraging-kubernetes), “as a cross-functional team member who specializes in testing, you probably only need to know the following:

* How to start Kubernetes in a virtual machine
* How to find the logs of each component in the GUI or the command line
* How to access the GUI
* How to tell which version of which components of the software are running
* How to update just one component of your application
* How to read the important parts of the YAML specification”

Probably, the main takeaway of the whole article is this — In this fast-evolving environment, nothing is too fixed except the necessity of multidisciplinary teams to work together.

