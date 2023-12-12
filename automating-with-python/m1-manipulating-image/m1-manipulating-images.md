### **Distributed Systems**

- **Nature**: Distributed systems consist of software components working together on separate servers or nodes, often interconnected by a shared network.
- **Goal**: These systems aim to distribute tasks and functions across multiple components to avoid bottlenecks and single points of failure.

### **Characteristics**

1. **Resource Sharing**: Hardware, software, and data can be shared across the system.
2. **Error Detection**: Facilitates the identification of errors and inefficiencies.
3. **Transparency**: Nodes can interact and communicate seamlessly.
4. **Simultaneous Processing**: Multiple machines can process the same function concurrently.
5. **Scalability**: Adding more machines increases computation and processing power.
6. **Heterogeneity**: Systems often comprise asynchronous nodes with various operating systems, middleware, and hardware, allowing for expansion and new component integration.

### **Advantages**

1. **Flexibility**: Tuning server characteristics to specific components (e.g., more memory/CPU for application servers).
2. **Large Volume Handling**: Running multiple component copies for fault tolerance and traffic management.
3. **Redundancy of Nodes**: Provides backup nodes in case of failures.
4. **Fault Tolerance**: Improves dependability by reducing single points of failure risks.

### **Disadvantages**

1. **Increased Complexity**: More challenging in design, administration, and understanding.
2. **Extra Work for Component Discovery**: Components must locate each other, adding complexity.
3. **New Problem Introduction**: Network issues can introduce new failure points.
4. **Potential Delays**: Network-induced delays can affect performance.
5. **Increased Costs**: Scalability can lead to higher expenses.

### **Design Considerations**

- **Early Awareness**: Incorporate distributed systems architecture from the beginning for scalable applications.
- **Discovery Mechanisms**: Implement methods for component discovery (configuration files, service catalogs, service meshes).
- **Simplicity Balance**: Avoid overcomplication to prevent fragility and maintenance challenges.

---

**NALSD**, Non-Abstract Large System Design, is a framework developed by Google to guide the design and evaluation of large-scale systems. It's particularly focused on practicality and real-world application in the context of site reliability engineering (SRE). Here's a detailed breakdown of its key aspects:

### **Characteristics of NALSD**

1. **Technical Design (Phase 1)**:
    - **Iterative Process**: Involves multiple rounds of design, refinement, prototypes, feasibility studies, and stakeholder feedback.
    - **Key Questions**:
        - "Is it possible?" Assessing the basic feasibility of the design.
        - "Can we do better?" Optimizing for efficiency, simplicity, and cost.
2. **Scaling Up (Phase 2)**:
    - **Scalability Assessment**: Evaluating the system's performance under increased load and scalability to accommodate growth without losing performance.
    - **Key Questions**:
        - "Is it feasible at scale?" Determining if the system can handle increased demand.
        - "Is it resilient?" Ensuring system stability despite component failures.
        - "Can we make improvements?" Identifying potential enhancements or modifications.

### **Three Goals of NALSD**

1. **Capacity Planning**:
    - Focus on correctly sizing each component and planning for growth.
    - Involves monitoring, performance analysis, and predicting growth trends.
2. **Component Isolation**:
    - Emphasizes designing system elements for simplicity, modularity, and independence.
    - Follows the principle of doing one thing well, leading to specialized, clear-purpose components.
3. **Graceful Degradation**:
    - Ensuring parts of the system remain functional even if other parts fail.
    - For instance, a web application might switch to a read-only mode if a database server fails.

### **Google’s NALSD Workbook**

- Created by Google's SRE team, this workbook provides insights, best practices, and guidelines for designing and building scalable and reliable systems.
- A valuable resource for engineers and developers to learn and improve their skills in system design.

### **Key Takeaways**

- **NALSD's Focus**: It emphasizes practical, tangible aspects of large system design, particularly suitable for SREs.
- **Design Phases**: Involves both a rigorous design process (Phase 1) and a thorough evaluation of scalability and resilience (Phase 2).
- **Goals**: Aims to achieve efficient capacity planning, clear component isolation, and robustness through graceful degradation.

The NALSD approach is essential for managing the complexities of modern, large-scale systems, ensuring they are not only well-designed but also prepared to handle the dynamic challenges of real-world applications. The emphasis on practicality over theoretical concepts makes it particularly valuable in the rapidly evolving field of technology.

Workbook: <https://static.googleusercontent.com/media/sre.google/en//static/pdf/nalsd-workbook-letter.pdf>

---

## What is an API?

Application Programming Interfaces (APIs) facilitate communication between different software components. They are provided by libraries in programming languages as **external** or **public** functions, classes, and methods, which can be used by other software, potentially written in different programming languages.

### Special Attributes of an API

- **Internal/Private Functions**: These are functions, classes, and methods in a library not meant for direct use in your code. They support public functions.
- **Stability and Consistency**: An API remains stable even if the library's internal code changes, ensuring consistent parameters and results.
- **Promise of Stability**: An API is like a promise that even with internal code changes, the interface for using the functions remains consistent.

### Breaking Changes

- **Library Authors and Changes**: Authors can improve and change the code behind the API but should not alter how functions are called or the results they provide. Changes to the API that could break dependent code are known as **breaking changes**.
- **Communicating Breaking Changes**: Library authors need a plan to communicate any breaking changes to users. [Semantic Versioning](https://semver.org/#summary) suggests that breaking changes should be reserved for major version increments.

### Semantic Versioning (SemVer)

- **Version Format**: A semantic version number has the format `MAJOR.MINOR.PATCH`.
- **Version Increment Rules**:
  - **MAJOR**: Incremented for incompatible API changes.
  - **MINOR**: Incremented for backward-compatible functionality additions.
  - **PATCH**: Incremented for backward-compatible bug fixes.
- **Pre-release and Build Metadata**: Identified with hyphens and plus signs respectively. They are not considered in precedence rules.
- **Deprecating Functionality**: When deprecating part of an API, update documentation and issue a new minor release before completely removing the functionality in a new major release&#8203;``【oaicite:2】``&#8203;.
- **Version String Size Limit**: No explicit limit, but it's recommended to use good judgment, considering possible limits imposed by specific systems&#8203;``【oaicite:1】``&#8203;.
- **Semantic Version Tagging**: Prefixing a version with "v" (e.g., "v1.2.3") is common but not part of the semantic version. The semantic version would be "1.2.3"&#8203;``【oaicite:0】``&#8203;.

### Choosing a Library

- **Understanding the API**: Familiarize with how functions are called, the inputs they expect, and the outputs they return.

# Generate and Manage Containers

## Generating Image Containers

To build a container image, you need a Dockerfile with instructions for Docker to package your application with all its dependencies.

## Choosing a Base Image

Select a base image wisely as it provides the operating system inside the container. Some popular base images include:

- [Debian](https://hub.docker.com/_/debian)
- [Ubuntu](https://hub.docker.com/_/ubuntu)
- [Alpine Linux](https://hub.docker.com/_/alpine)
- [Python](https://hub.docker.com/_/python/)

## Creating a Dockerfile

A Dockerfile in your project directory will list steps to generate your container image. Here’s a sample for a Python Flask app:

```Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 4000
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]
```

## **Build a Docker Image**

Use **`docker build`** to build your Docker image:

```bash
docker build -t myname/myapp:1.0 .

```

## **Manage Images**

To start a container:

```bash

docker run -p 4000:4000 myname/myapp:1.0

```

To see images on your system:

```bash

docker image ls -a

```

Remove unused images:

```bash
docker image prune

```

Push your image to a repository:

```bash
docker image push myname/myapp:1.0

```

### **Requirements File**

Your project should have a **`requirements.txt`**:

```text
flask
pymysql
Flask-SQLAlchemy
```

### **Pro Tip**

Docker images are built from layers. Clean up at the end of commands that create temporary files to avoid large layers.

## **Key Takeaways**

Containerization benefits development, deployment, and application management, enhancing efficiency and scalability.

This guide encapsulates the essentials of building and managing Docker images, from creating a Dockerfile to choosing a base image and managing built images.
