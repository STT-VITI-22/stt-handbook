# What is GitOps

Published 02 November 2021

Updated 22 June 2026

![3D rendering of abstract pattern sphere against blue background](https://assets.ibm.com/is/image/ibm/adobestock_1163885541?ts=1782133601127&dpr=off "Abstract 3D Pixelated Sphere on Gradient Background")

By
[Ashok Iyengar](https://www.ibm.com/think/author/ashok-iyengar.html)

## GitOps defined

GitOps is a [DevOps](https://www.ibm.com/think/topics/devops) practice that uses Git as the single source of truth where the desired configuration state is stored.

The focus is on operations automation, driven from Git repositories.
Although it is in the title, Git is not the only repository that can be
used. It is the interfaces provided by Git that automate operations.
GitOps ends up using information extracted from build metadata to
determine which packages to build triggered by a particular code change:

![Figure 1. GitOps overview.](https://assets.ibm.com/is/image/ibm/screen-shot-2021-11-01-at-1-49-36-pm?ts=1782133601869&dpr=off)

Figure 1. GitOps overview.

At its core, the GitOps model uses the controller pattern. This is further aided by the operator pattern from a [Kubernetes](https://www.ibm.com/think/topics/kubernetes) or OpenShift perspective, wherein operators are software extensions that use [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to manage applications and their components.

We would be amiss not to mention Argo CD, a GitOps tool that helps with GitOps workflows. Argo CD is an open-source declarative tool for the [continuous integration](https://www.ibm.com/think/topics/continuous-integration) and [continuous deployment](https://www.ibm.com/think/topics/continuous-deployment) (CI/CD) of applications. Implemented as a Kubernetes controller, Argo CD continuously monitors running application definitions and configurations, comparing the current, live state on the cluster against the desired state defined in a Git repository.

But GitOps is not a single product, plugin or platform. GitOps workflows help teams manage IT infrastructure through processes they already use in application development. To borrow from a GitLab blog, GitOps requires three core components: **GitOps = IaC + PRs or MRs + CI/CD**

* **IaC**: [Infrastructure as Code (IaC)](https://www.ibm.com/think/topics/infrastructure-as-code) is the practice of keeping all infrastructure configuration stored as code. GitOps uses a Git repository as the single source of truth for infrastructure definitions. Git tracks all code management changes.
* **PRs or MRs**: GitOps uses pull requests (PRs) or merge requests (MRs) as the change mechanism for all infrastructure updates. This is where teams can collaborate via reviews and comments and where formal approvals take place.
* **CI/CD**: GitOps automates infrastructure updates using a Git workflow with continuous integration (CI) and continuous delivery (CD). When new code is merged, the CI/CD pipeline enacts the change in the environment. Any configuration drift, such as manual changes or errors, is overwritten by GitOps automation so the environment converges on the desired state defined in Git, thus providing continuous operations (CO):

GitOps has been around for a few years now, but it has gained traction recently because of [containers](https://www.ibm.com/think/topics/containers) and the complexity surrounding the consistent deployment and management of container runtime environments.

What is the problem that GitOps is attempting to solve? Well, it automates software operations so that enterprises can get better at software engineering. It enables application teams to release more frequently and operate [cloud-native applications](https://www.ibm.com/think/topics/cloud-native) more effectively.

## The latest tech news, backed by expert insights

Stay up to date on the most important—and intriguing—industry trends on AI, automation, data and beyond with the Think newsletter. See the [IBM Privacy Statement](https://www.ibm.com/us-en/privacy).

## Thank you! You are subscribed.

![Figure 2. CI/CD/CO](https://assets.ibm.com/is/image/ibm/screen-shot-2021-11-01-at-1-50-04-pm?ts=1782133602822&dpr=off)

Figure 2. CI/CD/CO

## GitOps in Red Hat OpenShift

Red Hat OpenShift operators simplify the installation and automated orchestration of complex workloads. They help encode human operational logic to manage services running as Kubernetes-native applications, making day-2 operations easier. The operator is a piece of software running in a pod on the cluster, interacting with the Kubernetes API server. An OpenShift operator is essentially a custom controller and can be, in effect, an application-specific controller.

IBM DevOps

### 6 observability myths in AIOps uncovered

In this video, IBM Vice President Chris Farrell challenges six common myths about observability, unpacking them one by one to clarify what organizations really need to achieve deeper operational insight and smarter decision-making.

[Explore DevOps](https://www.ibm.com/solutions/devops)

## GitOps operator

Red Hat OpenShift makes it easy for developers wanting to use GitOps by providing the necessary operators. Once deployed, they can then be viewed under the Installed Operators section in the OpenShift Console. The Red Hat OpenShift GitOps operator is the upstream operator for ArgoCD, and the Red Hat OpenShift Pipelines operator, which also gets deployed, is the upstream operator for Tekton. See Figure 3:

![Figure 3. GitOps-related operators in Red Hat OpenShift.](https://assets.ibm.com/is/image/ibm/screen-shot-2021-11-01-at-4-14-05-pm?ts=1782133604021&dpr=off)

Figure 3. GitOps-related operators in Red Hat OpenShift.

The operators and related APIs can then be used to kick off one or more GitOps pipelines that can deploy to different environments pulling the desired configuration outcome from Git. Environments could be the usual dev, test and prod but can also span geographical environments like the enterprise cloud, telco network or edge computing nodes.

The deployment resources are classified into three areas: infrastructure, services and applications. These areas make it easy to separate and manage the deployment of related resources:

* **Infrastructure** is where the required namespaces and storage units are defined.
* **Services** is where the various operators needed to set up the instances are described.
* **Applications** is where the application to be deployed are enumerated.

## GitOps in edge computing

### Cloud/enterprise data center

Edge computing is seeing the proliferation of OpenShift or Kubernetes clusters in most IT centers. It has the potential to reach a massive scale of hundreds to thousands of deployments per customer. The result is that enterprise IT departments must manage multiple independent or cooperative container runtime clusters running on-prem and/or on public clouds.

Ensuring clusters have the same desired state — rolling out a change and rolling back a change on multiple clouds — is a major benefit that GitOps provides to edge- and IoT-based businesses.

### Network edge

The GitOps paradigm is applicable at the network edge since one of the major challenges Communication Service Providers (CSPs) face is looking for orchestration, automation and management of their networks. While 5G is a boon to consumers, software-defined networks (SDNs), network slicing with different bandwidths and faster deployment have created challenges for the telco providers.

An automated deployment pipeline is one way that CSPs can bring services to customers faster. Having a central repository and a declarative approach to provisioning container infrastructure means faster time to market for new features and change requests. Such a paradigm will help the provisioning of VNFs (Virtual Network Functions) and CNFs (Cloud-Native Network Functions) at the network edge. Containerization of network components makes it possible to manage such functions. Lastly, because all configuration activity is logged and stored in Git, the ability to track changes is critical for compliance and audit purposes. There are a couple of related blogs from WeaveWorks in the references:

![Figure 4. GitOps in edge computing.](https://assets.ibm.com/is/image/ibm/screen-shot-2021-11-01-at-1-50-43-pm?ts=1782133605528&dpr=off)

Figure 4. GitOps in edge computing.

### Enterprise edge

GitOps allows organizations to deploy to multiple targets simultaneously. It allows for the rollout of fine-grained deployments. This would be extremely useful when deploying applications to hundreds and tens of thousands of edge nodes, which come in different shapes and form factors and use varied communication protocols — especially if the edge nodes are small Eedge clusters using an Intel NUC or NVIDIA Jetson.

The GitOps framework can be beneficial in deploying applications and using the Git repository as the single source of truth. [ITOps](https://www.ibm.com/think/topics/it-operations) teams look for autonomous application deployment, management and operations of edge nodes, which is facilitated with the use of Red Hat OpenShift operators.

### Device edge (or far edge)

The benefit of GitOps is obvious at the network edge and the
enterprise edge. The far edge devices present a different challenge
because the storage and compute capacity of some of these devices is not
large enough to host GitOps services and run applications.

The
release of lightweight Kubernetes distributions, such as K3s and K0s,
are meant for IoT and edge use cases. The ability to deploy a
lightweight Kubernetes distribution on an edge device allows us to run a
GitOps tool like Argo CD. The device(s) will then be able to adopt the
pull model of polling a Git repository for the desired state and
synchronizing it to the live state of the cluster.

