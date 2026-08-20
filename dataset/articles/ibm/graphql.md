# What is GraphQL?

Published 05 November 2024

![3D rendering of abstract pattern sphere against blue background](https://assets.ibm.com/is/image/ibm/adobestock_1163885541?ts=1782338819700&dpr=off "Abstract 3D Pixelated Sphere on Gradient Background")

## GraphQL defined

GraphQL is an open-source query language and server-side runtime that specifies how clients should interact with [application programming interfaces](https://www.ibm.com/think/topics/api) (APIs).

GraphQL offers an efficient, more flexible alternative to [representational state transfer (REST) and RESTful APIs](https://www.ibm.com/think/topics/rest-apis) and solves for some limitations of REST. For example, providing the ability to more accurately target resources with a single query.

GraphQL uses an intuitive syntax that enables clients to send a single GraphQL query to an API and receive exactly the data needed (instead of accessing complex [endpoints](https://www.ibm.com/think/topics/api-endpoint) with lots of parameters.) This more efficient data fetching can improve system performance and ease-of-use for developers.

It makes GraphQL particularly useful for building APIs in complex environments with rapidly changing front-end requirements. Neither REST nor GraphQL APIs are inherently superior; they’re different tools that are suited to different tasks.

In the early 2010s, Facebook was experiencing massive growth and transformation. But a growing user base and increasingly complex mobile app environment rendered its existing RESTful approach—which required multiple round trips to different API endpoints to fetch all necessary query data—unsustainable.

REST APIs were ill-equipped to handle complex, data-driven user interfaces and frequently encountered [latency](https://www.ibm.com/think/topics/latency) issues and data inefficiencies, especially for mobile users with limited or expensive data plans.

In response to these challenges, Facebook engineers developed GraphQL (along with single-page application platform React), releasing it as an [open source](https://www.ibm.com/think/topics/open-source) solution in 2015. Ultimately, Facebook moved the service to the GraphQL Foundation, which comprises member companies like AWS, Gatsby, Intuit and IBM, in 2018.

## What are GraphQL APIs and how do they work?

A GraphQL architecture’s declarative data-fetching features revolve around several key components and processes, each playing a unique role in data handling and processing.  
  
They include:

* **Schemas**
* **Resolvers**
* **Queries**
* **Mutations**

### Schemas

GraphQL relies on a strong type system where all data types are recorded in the GraphQL schema definition language (SDL). Typed schemas dictate the types of data that can be queried in the API and the relationships between the types and the operations available to the user.  
  
In other words, they define the capabilities of the API and the shape of the data clients can interact with. The configuration of this schema ultimately determines how the API can be used. As queries come in, the schema is used for request validation and the GraphQL API only executes the validated queries.

### Resolvers

Each field in a schema is backed by a resolver that populates data and determines the response to a set of fields. Resolvers—which can retrieve data from a database, a [cloud](https://www.ibm.com/think/topics/cloud-computing) service or virtually any other source—provide instructions for turning a GraphQL operation (for example, a query, mutation or subscription) into data.

When a query field starts, the system generates a call to the corresponding resolver to produce the next value. If a field produces a scalar value (for example, a string or number), the execution completes. If a field produces an object value, the query contains more fields for that object. This process continues until only scalar fields are left.

Resolvers also facilitate data formatting and help the system stitch together information from various data sources.

### Queries

A data query is the request made by the client to the GraphQL server; it specifies what data the client wants to fetch. Queries are defined in the query type, which is a special object in the code that defines the top level entry point for every request that clients can execute against the server. Each query type also defines the name and return type for each entry point.

When a query comes in, GraphQL validates it against the schema definitions and—assuming the query is valid—runs it. The structure of a query typically mirrors the structure of the response data, making data requirements explicit and predictable.

### Mutations

Mutations are GraphQL operations that create, update or delete data on the server. They are analogous to the POST, PUT, PATCH and DELETE operations in RESTful APIs. While users can access some queries without [authentication](https://www.ibm.com/think/topics/authentication), mutations always require authentication (for instance, by using an API token.)

Similar to how a queries work, GraphQL mutations are validated against the schema and its definitions. Once the mutation is validated and started, the server returns a JSON response.

## GraphQL vs. REST APIs

Though [GraphQL APIs have emerged](https://www.ibm.com/think/insights/seven-key-insights-on-graphql-trends) as a more efficient and flexible alternative, REST has long been long the standard for API architectures. REST is a structured architectural style for networked hypermedia applications, designed to use a cacheable, stateless, client/server communication protocol (usually HTTP).   
  
Making the choice between [GraphQL vs. REST](https://www.ibm.com/think/topics/graphql-vs-rest-api) is mostly about determining which tool is best for the job at hand. Both GraphQL and REST enable clients to communicate with servers and request data, but there are key differences that explain the proliferation of GraphQL systems.

Data retrieval

[REST APIs are designed](https://www.ibm.com/think/topics/api-design) around resources (for example, any type of object, data or service accessible to the client) and work by having different endpoints (URLs) for each resource. They use a fixed data structure to determine the shape and size of resources they provide to clients.

When the client requests a resource, the server sends back a complete dataset with all the data associated with that resource. If a client only needs a subset of the data, it still receives all the data (over-fetching); if the client needs data that spans multiple resources, it often must make multiple API calls due to inadequate data retrieval from the initial request (under-fetching).

GraphQL, however, uses a single endpoint that provides a complete and understandable description of the data. GraphQL queries can access resource properties and follow references between resources. This enables the client to get all the data it needs from a single API request payload and avoid over-fetching and under-fetching issues.

Versioning

In a RESTful architecture, changing the structure of the data often requires teams to version the API to prevent system errors and service disruptions for the user.  
  
This means developers must create a new endpoint every time they change the structure, resulting in multiple API versions and complicating the maintenance process.

GraphQL eliminates the need for versioning because clients can specify their requirements in the query. If new fields are added to the server, clients that don't need those fields won't be affected. Conversely, if fields are deprecated, clients can continue to request them until they update their queries.

Error handling

REST APIs use HTTP status codes to indicate the status/success of a request. Each status code has a specific meaning. A successful request returns a 200 status code, while a client error might return a 400 status code and a server error might return a 500 status code.

GraphQL handles errors differently. Every request, regardless of whether it resulted in an error, returns a 200 OK status code. The errors are not communicated by using HTTP status codes; rather, the system communicates errors in the response body along with the data.  
  
This approach requires clients to parse the response body to determine whether the request was successful, which can make [debugging](https://www.ibm.com/think/topics/debugging) GraphQL APIs a bit challenging.

Real-time data

REST doesn't have built-in support for real-time updates. If a web or mobile application needs real-time functions with a REST API, developers must usually implement techniques like long-polling (where the client repeatedly polls the server for new data), server-sent events and WebSockets, which can add complexity to the application.

However, GraphQL includes built-in support for real-time updates by using subscriptions. Subscriptions maintain a steady connection to the server, allowing the server to push updates to the client whenever specific events happen and enabling clients to stay on top of relevant API data.

Tools and ecosystem

The REST ecosystem is well established with a wide range of tools, libraries, frameworks and tutorials available to developers. However, working with REST APIs often requires teams to navigate several endpoints and understand the unique conventions and patterns of each API.

GraphQL is relatively new, but the GraphQL ecosystem has grown tremendously since its introduction, with various tools and libraries available for both frontend and backend service development.  
  
Tools such as GraphiQL, Apollo Studio and GraphQL Playground provide powerful in-browser integrated development environments (IDEs) for exploring and testing GraphQL APIs. Furthermore, GraphQL has strong support for code generation, which can simplify client-side development.

Caching

REST APIs rely on HTTP caching mechanisms like ETags and last-modified headers. While effective, caching strategies can be complex to implement and might not consistently optimize performance for all use cases.

GraphQL APIs can be more challenging to cache due to the dynamic nature of the queries. However, the use of persisted queries, response caching and server-side caching can mitigate these challenges and provide efficient caching strategies for GraphQL architectures.

## GraphQL federation

Since GraphQL’s transition to the GraphQL Foundation, developers have created implementations for various programming languages, including JavaScript, Python, Ruby and PHP, among others. GraphQL APIs have been adopted by myriad businesses, such as Github, Pinterest, PayPal, Shopify, Airbnb and more, enabling more clients to streamline data specification, reduce excessive or inadequate network data transmission and improve overall data-fetching capabilities.1

What’s more, enterprises and developers are pushing for open federation of GraphQL architectures. In its current iteration, [GraphQL federation](https://www.ibm.com/think/topics/graphql-federation) takes separate GraphQL services and aggregates them into a single GraphQL API, which serves as the entry point to all underlying backend data and facilitates single-request data fetching. However, federation implementation is exclusive to a single vendor.

As a response, GraphQL proponents advocate for democratized federation, which facilitates data aggregation from both GraphQL APIs and non-GraphQL APIs instead of GraphQL-exclusive aggregation.2

