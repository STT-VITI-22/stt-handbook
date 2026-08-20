# What is gRPC?

![Overhead view of intersecting roads](https://assets.ibm.com/is/image/ibm/dji_20240709173523_0088_d_r?ts=1734375440031&dpr=off)

## What is gRPC?

gRPC is an open source, language agnostic and cross-platform remote procedure call (RPC) framework that uses HTTP/2 transport layer protocol. It is a specific implementation of RPC, initially developed by Google and is now managed by the Cloud Native Computing Foundation (CNCF).

RPC, or remote procedure call, is a communication model for client/server interaction that enables remote calls to appear and function as local calls. It’s an older technique, dating back conceptually to the 1970s, with initial applications seen in pioneering computing projects such as the ARPANET and Xerox PARC.

In an RPC, the client interacts with a representation of the server, which appears local but is in fact an intermediary. This intermediary is commonly referred to as a stub, which handles the marshalling and unmarshalling data (that is, converting data into a suitable format for transmission and converting the results received from the server back to the original format). Because it is an architectural style for client/server communication, it’s commonly used in [API design.](https://www.ibm.com/topics/api-design)

There are many different implementations of RPC frameworks, including XML-RPC and JSON-RPC. These implementations use HTTP as their transport protocol, differing mostly in format type. Dating back to the 1990s and 2000s, these implementations showcased RPC’s strengths: they simplified development, abstract [network](https://www.ibm.com/think/topics/networking) communication complexities, are lightweight, relatively simple to use and are human readable.

However, many modern environments—particularly those that use microservices architectures, polyglot environments and systems with high data loads—require a faster, high-performance framework to connect distributed applications. Ideally, this framework facilitates more efficient, real-time data transfer between services running across different environments and data centers.

gRPC was developed to meet this need, offering low [latency](https://www.ibm.com/think/topics/latency) and high throughput through data serialization and its use the HTTP/2 protocol, bidirectional streaming capabilities, code generation and more.

gRPC was initially released in 2015, the same year as the release of HTTP/2. It addresses the limitations with older RPC implementations primarily through its use of Protocol Buffers, or Protobuf, its interface definition language (IDL). Protobuf serializes and encodes structured data into binary. This makes data more compact, enabling faster transmission and higher performance.

Protobuf also allows changes to data fields without disrupting code. This helps reduce errors and enable real-time data sharing and processing. These features make APIs built with gRPC a strong option for modern, distributed environments, microservices architectures, streaming applications and for connecting [Internet of Things](https://www.ibm.com/think/topics/internet-of-things) systems and devices.

It would make sense if gRPC stood for “Google Remote Procedure Call.” But the gRPC team at grpc.io cheekily claims that it stands for “gRPC Remote Procedure Call.” Its [GitHub notes](https://grpc.github.io/grpc/core/md_doc_g_stands_for.html) that the “g” stands for something different with each version (ranging from “gregarious” to “goose” to “Guadalupe River Park Conservancy”). In any case, Google developed gRPC and released as an open source project in 2015.

![3D design of balls rolling on a track](https://assets.ibm.com/is/image/ibm/trailv2_1200x1200?ts=1746554193743&dpr=off)

### The latest AI News + Insights

Discover expertly curated insights and news on AI, cloud and more in the weekly Think Newsletter.

[Subscribe today](https://www.ibm.com/us-en/forms/news-mkt-52954)

## gRPC features

gRPC presents a modern, updated version of RPC, with support for modern languages and additional features and optimizations. Features include:

* An interface design language (IDL) called Protocol Buffers
* Use of HTTP/2 for data transmission
* Bidirectional streaming
* Code generation
* Four method types
* Integration with TLS-based security
* Interceptor support for logging, tracing, authentication and more

### Protocol Buffers

Protocol Buffers, commonly known as Protobuf, is a cross-platform data format developed by Google that is used to serialize structured data. In effect it serves as a powerful intermediary between the client and server that serializes requests into binary code for transmission.

This mechanism is flexible and efficient, enabling programming language agnosticism, reduced message size and faster parsing and transmission all at the same time. An application that uses Java can communicate with one that uses Python because the request is converted into the lingua franca of binary. Though not readable by humans, binary is faster to transmit and decode with computers than a text-based format such as JSON.

Essentially, developers create a text file with the suffix ".proto" that contains all the information about data structure. This information is schema-based, meaning that it defines parameters, methods and possible outputs—a description of the structure of the data. For example, you might have an entry for “user,” which notes that this data will include “name,” “email address” and “favorite pizza topping.”

According to the [Protobuf documentation](https://protobuf.dev/), it’s like XML, “but smaller, faster and simpler. You define how you want your data to be structured once, then you can use specially generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.” As a middleman, Protobuf enables the installation of various authentication and security measures as well.

Developers can use a compiler, called Protoc, to generate code in any of several supported languages, including C#, C++, Dart, Go, Java, Kotlin, Node.js, Objective-C, PHP, Python and Ruby. This code serves many functions: it typically includes classes or modules, handles serializing into binary and deserializing from binary and abstracts away data exchange complexities. Developers needn’t worry about network packaging, marshalling, updating for compatibility and implementation; Protobuf handles it all.

Protobuf’s schema-based design allows developers to add new data fields to existing structures without breaking the entire system. It also greatly reduces the effort needed to update, maintain and handle tedious API-related tasks, such as adjusting the prior code after adding new data fields. That said, .proto files can take some time and effort to set up in the first place.

### HTTP/2

HTTP/2 is a transport protocol—a method that computers and servers use to exchange information—that uses a binary format to send messages, reduces TCP connections and uses header compression, all of which help make it faster and more efficient than its predecessor (HTTP/1.1). It also enables multiplexing, or the ability to send multiple concurrent streams on a single connection; gRPC uses what are called channels to enable multiple streams over those multiple connections. Messages are sent as HTTP/2 data frames, each of which might contain multiple gRPC messages.

### Bidirectional streaming

gRPC offers bidirectional streaming, in which both the client and server can independently send messages in a read/write stream. This method allows for all kinds of flexibility: a server and client can exchange responses sequentially, or a server can wait until all the client’s messages have been received before responding. This feature can be adjusted according to specific applications.

### Code generation

gRPC uses a compiler tool called protoc to automatically generate both client and server code in various languages based on service definitions and message structures defined in a .proto file. Plug-ins can be used to extend support [many more](https://github.com/protocolbuffers/protobuf/blob/main/docs/third_party.md) languages.  
  
Protoc generates data access classes in the language defined in the proto definition. These classes provide simple accessors for fields such as [name], as well as methods for serializing and parsing the structure to and from raw bytes.1

### Methods

gRPC supports four different method types for data transmission: Unary, client-side streaming, server-side streaming and bidirectional streaming.

### TLS-based security

gRPC has built-in integration with TLS (transport layer security), which encrypts data exchanges between client and server and enables users to help secure connections.

### Interceptor support

gRPC supports pluggable authentication, tracing, logging, metrics, load balancing, health checking and more.

## gRPC method types

gRPC has four different types of methods, which denote how a message is sent and received by a gRPC client and gRPC server. Those types are:

**Unary**: A simple call in which a client sends a single request and a server replies with a single response.

**Server-side streaming**: A call in which a client sends one request, but the server replies with multiple responses.

**Client-side streaming:** A call in which a client sends multiple requests and a server replies with a single response. The server can opt to wait for the entire stream of client requests to cease before processing and responding.

**Bidirectional streaming**: The client and server both send multiple calls back and forth concurrently, enabling real-time communication.

What is Apache Kafka?

### What is Apache Kafka?

In this video, you will learn what Apache Kafka is, how it works and the core concepts behind building real-time event streaming applications.

[Explore Confluent](https://www.confluent.io/?utm_campaign=tm.ibm_cd.data-leaders-tofu-page-video&utm_source=ibm&utm_medium=ibmweb)

## gRPC vs. REST

Both gRPC and [REST](https://www.ibm.com/think/topics/rest-apis) are architectural styles that are commonly used in API design. They have many similarities; both follow a client/server architecture, rely on HTTP-based communication, are stateless and language-agnostic. But they also differ in key ways that make each ideal for different use cases.

**Data format:** REST APIs use plain-text formats such as JSON and XML. gRPC uses Protobuf to encode data into binary.

**Communication pattern:** gRPC supports four methods: unary, server streaming, client streaming and bidirectional streaming. REST uses a unary system of request and response.

**Code generation:** gRPC offers built-in code generation; REST does not, though there are plug-ins available.

**Design pattern:** gRPC has a service-oriented design, in which callable server operations are defined as services or functions. In REST, design is oriented around resources, in which HTTP methods are used to access server resources through [endpoints](https://www.ibm.com/think/topics/api-endpoint) defined by URLs.

**Protocol:** gRPC uses HTTP/2, whereas REST relies on HTTP/1.1.

**Coupling:** gRPC’s client and server are tightly coupled, meaning that both the client and server must have access to the same middleware proto file. Any change in one requires a change in the other. REST is loosely coupled. This independence means that changes in one component do not affect the other.

## What is gRPC used for?

gRPC is often used for complex APIs that connect multiple services in a distributed environment. Its real-time streaming capability and high-performance make gRPC a good fit for several use cases including [microservices](https://www.ibm.com/think/topics/microservices), streaming and connecting Internet of Things clients.

### Microservices

Due to its high-performance, low latency, ability to handle large data volumes and real-time, bidirectional streaming capability, gRPC is often used to create APIs for microservices.

Because gRPC is language agnostic, it can enable communication between services written in different programming languages. In addition, Protobuf definitions provide a strongly typed schema that helps safeguard the microservice data integrity.

### Streaming

gRPC’s bidirectional streaming capabilities mean that it can concurrently stream data in both directions between client and server over a single network connection. This capability makes gRPC ideal for ongoing processes such as video conferencing or when a user wants to use part of a dataset while other data is being transferred.

### Internet of Things

The Internet of Things refers to a network of connected devices or clients. IoT devices—also known as “smart objects”—can include simple “smart home” devices such as smart thermostats, wearables such as smartwatches and RFID-enabled clothing and complex industrial machinery and transportation systems.2 gRPC APIs are often used to facilitate the consistent data exchange between these devices.

### Cloud

With its bidirectional streaming support and microservices-friendly capabilities (and its status as a CNCF project), gRPC is increasingly used for [cloud-native](https://www.ibm.com/think/topics/cloud-native) APIs.

### Generation of client libraries

gRPC is used to generate client libraries in many different programming languages. These libraries are generated based on the service definition provided in .proto files; once the service is defined, gRPC automatically generates client code in a chosen programming language.

This capability simplifies work for developers, enabling them to focus on application logic rather than low-level communication code.

## Benefits of gRPC

gRPC offers many benefits for organizations and developers building APIs with high-performance requirements. Those benefits include:

**Faster and more efficient transmission:** There are several factors that contribute to gRPC’s high-performance. For one, Protobuf serialization reduces message size and smaller packages can be transmitted more quickly. Binary is also more efficiently parsed than plain-text formats like JSON or XML.

In addition, gRPC uses HTTP/2, which is faster and more efficient than HTTP/1.1, further reducing latency and bandwidth usage.

**Greater portability:** Because gRPC uses protocol buffers (a language- and platform-agnostic serialization mechanism) to describe data structures and RPC interfaces, it can be used to enable communication between services written in various languages across different platforms.

**Reduced runtime errors:** Protobuf provides strong typing, meaning that it enforces a firm, explicitly defined data structure. Strong typing promotes consistency and earlier error detection, reducing the chance of errors at runtime.

**Flexible customization:** Built-in support for middleware enables customization and the addition of features, such as security and authentication measures or analytics tools.

## Challenges of gRPC

While gRPC has many advantages, it is not without its challenges. In some cases—for instance, public facing APIs with simple data sources where ease of use is a primary consideration—the complexity introduced by gRPC might be unnecessary. Challenges of gRPC include:

**Complexity:**Defining message structures and services in .proto files, as gRPC requires, can be more challenging than working with text-based formats such as XML and JSON.

**Ease of use:**gRPC, protocol buffers and HTTP/2 can present a steep learning curve for developers used to working with REST.

**Debugging:**It can be difficult to inspect, debug and log gRPC applications because the binary format is not human-readable. There are tools that can convert binary, but they require an extra step, compared with XML or JSON.

**Recency and support:**gRPC is not as old as other popular architectural styles like REST and does not have as large of a community or as much plug-in and documentation support. As a newer framework, there are fewer tools (such as security scanner tools) available for gRPC compared to some more established styles.

**Browser limitations:**Because web browsers do not natively support the gRPC protocol, it is not possible to directly call a gRPC service from a browser-based application One way to work around this issue is by using a proxy such as gRPC-Web. gRPC-Web essentially acts as a translation layer between a browser’s HTTP and gRPC protocol.

The web application initiates a gRPC call using the gRPC-Web JavaScript client library to send a gRPC request that has been adapted for browser compatibility. The request is sent to a proxy server that converts the request into a standard gRPC request and forwards it to the gRPC backend server. The gRPC server processes the request, sends back a response to the proxy server and the proxy once again converts the response into gRPC-Web format before passing back to the client.

