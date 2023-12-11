# Managing Cloud Instances at Scale

## Building Software for the Cloud

### Storing Data in the Cloud

#### Understanding Cloud Storage Solutions

- **Factors to Consider**: Data volume, type, location, access patterns, frequency of change, and budget.
- **Storage Types**: Traditional (block storage) and newer technologies (object or blob storage).

#### Block Storage

- **Characteristics**: Resembles physical storage, managed by the OS as if a physical drive.
- **Virtual Disks**: Allow easy data movement, attachment to different machines, and snapshot creation.
- **Types**: Persistent (for long-lived instances) and ephemeral (for temporary instances).

#### Shared File Systems

- **Purpose**: Share data across instances via network file system protocols.
- **Deployment**: Utilized in Platform as a Service (PaaS) models.

#### Object (Blob) Storage

- **Function**: Stores objects in storage buckets, accessed by unique names.
- **Usage**: Ideal for storing application data like files, photos, and videos.

#### Cloud-Based Databases

- **Types**: SQL (relational) and NoSQL (scalable, distributed).
- **Choice**: Based on application requirements and existing data models.

#### Selecting a Storage Class

- **Performance Factors**: Throughput, IOPS (Input/Output Operations Per Second), and latency.
- **Storage Classes**: Different classes offered at varying prices, based on performance and access frequency.
- **Hot vs. Cold Storage**: Hot for frequently accessed data, cold for infrequently accessed data.

#### Hot and Cold Storage Considerations

- **Performance**: Hot storage typically faster, often using SSDs.
- **Data Lifecycle Management**: Moving data from hot to cold storage based on access patterns.

#### Conclusion

- **Complexity**: Storage in the cloud involves various considerations and options.
- **Further Learning**: Additional resources provided for deeper understanding.

### Load Balancing

#### The Role of Load Balancing

- **Purpose**: Distributes requests across multiple instances of a service.
- **Applications**: Useful for scaling, geographical distribution, and backup instances.

#### Round Robin DNS

- **Method**: Distributes tasks evenly among a group, like serving cookies at a party.
- **DNS Protocol**: Translates URLs into a rotating list of IP addresses for load distribution.
- **Limitations**: Lack of control over which server clients connect to and issues with DNS caching.

#### Dedicated Load Balancers

- **Function**: Act as a proxy between clients and servers, directing requests based on set rules.
- **Complexity**: Can range from simple to complex, depending on service requirements.

#### Features of Load Balancers

- **Sticky Sessions**: Ensures all requests from the same client go to the same server.
- **Health Checks**: Monitors the health of backend servers and excludes unhealthy ones from the pool.

#### Auto Scaling with Load Balancers

- **Integration**: Adding new machines to a server pool becomes straightforward.
- **Automatic Adjustment**: Auto scaling feature adjusts the number of instances based on load.

#### Geo DNS and GeoIP

- **Purpose**: Directs clients to geographically closest load balancers.
- **Implementation**: Configurations in DNS servers respond with IPs based on the client's location.

#### Content Delivery Networks (CDNs)

- **Goal**: Bring content closer to the user for faster access.
- **Mechanism**: Caches content in servers near the user's location, speeding up repeated access.

#### Upcoming Topics

- Strategies for deploying changes safely to cloud services.

### Change Management

#### Embracing Change

- **Need for Change**: Essential for fixing bugs and improving features.
- **Controlled Change**: Implementing changes in a safe and managed way through change management.

#### Testing and Continuous Integration (CI)

- **Testing**: Ensuring thorough testing through unit and integration tests.
- **CI Systems**: Automatically building and testing code for each change, even during reviews.

#### Continuous Deployment (CD)

- **Automatic Deployment**: Deploying builds only when tests pass.
- **Environment-Based Rules**: Configuring CD to push changes to different environments based on criteria.

#### Different Environments

- **Production (Prod)**: The real environment seen by users.
- **Test Environment**: For verifying changes work correctly before affecting users.
- **Development (Dev) and Pre-Prod**: Additional stages for testing changes before release.

#### Deployment Strategies

- **A/B Testing**: Comparing two sets of code/configuration (A and B) in production.
- **Load Balancer Utilization**: Directing different percentages of requests to A/B configurations.
- **Monitoring**: Essential to identify which configuration performs better.

#### Handling Production Issues

- **Learning from Failure**: Using post-mortems to understand and prevent future failures.
- **Improving Systems**: Incorporating learnings into tests, CI/CD, and health checks.

#### Conclusion

- **Accepting IT Challenges**: Recognizing that issues may occur despite precautions.
- **Growth and Confidence**: Refining change management systems and skills over time for safer and quicker changes.

### Understanding Limitations

### Handling Cloud Service Challenges

#### Designing Fault-Tolerant Applications

- **Importance**: Ensuring applications handle unexpected events, like instance crashes, without issues.
- **Fault Tolerance**: Applications should continue operating smoothly despite individual machine failures.

#### Dealing with Quotas and Limits

- **Operation Limits**: Restrictions on the number of certain operations within a time period (e.g., blob writes).
- **Rate Limits**: Enforced on expensive API calls to prevent system overload.
- **Utilization Limits**: Caps on the total amount of resources you can provision.
- **Strategy**: Modify operations to fit limits or request quota increases from the cloud provider.

#### Managing Auto-Scaling and Budgets

- **Auto Scaling**: Automatically adds/removes instances based on traffic but can lead to high costs.
- **Quotas and Budgets**: Setting quotas to control costs; important for services with tight budgets.

#### Monitoring and Alerting

- **Vital for Management**: Essential for tracking system behavior, especially around quotas and demand spikes.
- **Response**: Enables timely decisions on quota adjustments or other actions.

#### Dependency on Platform as a Service (PaaS)

- **Upgrade Cycles**: Limited control over software version updates provided by cloud services.
- **Communication**: Cloud providers usually inform about changes proactively.
- **Testing New Versions**: Setting up environments to test beta or prerelease versions.

---

## Monitoring and Alerting

### Getting Started with Monitoring

#### Introduction to Monitoring

- **Purpose**: Monitoring provides insights into the history and current status of a system.
- **Metrics**: Key indicators of service performance, both generic and service-specific.

#### Monitoring Web Services

- **Example**: Analyzing HTTP response codes to gauge web server performance.
- **Types of Metrics**: Vary based on the nature of the service (e-commerce, mail servers, etc.).

#### Choosing Relevant Metrics

- **Selection Process**: Identify metrics critical to understanding your specific service.
- **Storage**: Metrics are stored in monitoring systems for analysis.

#### Monitoring Systems

- **Provider-Specific**: AWS Cloudwatch, Google Stack Driver, Azure Metrics.
- **Cross-Vendor Systems**: Prometheus, Datadog, Nagios.
- **Data Collection**: Utilize either a pull model (monitoring system queries service) or a push model (service sends metrics).

#### Using Dashboards

- **Functionality**: Visualize the progression of metrics over time.
- **Analysis**: Compare current data against historical data to identify trends or issues.

#### Whitebox vs. Blackbox Monitoring

- **Whitebox Monitoring**: Internal system monitoring, tracking metrics like storage usage and request processing time.
- **Blackbox Monitoring**: External system checks, assessing service responsiveness and global performance.

#### Importance of Alerting

- **Automation**: Avoids the need for constant manual monitoring.
- **Critical for Reliability**: Alerts notify when something is wrong in the system.


### Getting Alerts When Things Go Wrong

### Monitoring and Alerting: Detecting and Addressing Problems

#### Importance of Automated Alerting

- **Need for Automation**: Services must be set up to work unattended and handle problems as they arise.
- **Proactive Detection**: Automated alerting helps detect issues before users are impacted.

#### Basic Alerting Approach

- **Periodic Checks**: Using tools like cron with scripts to monitor health and send alerts.
- **Monitoring System**: Configures periodic evaluation of metrics to identify and raise alerts.

#### Raising Effective Alerts

- **Types of Alerts**: Immediate attention (pages) and non-immediate attention (bugs/tickets).
- **Pages**: Urgent issues that might require immediate action, often received via SMS, calls, or apps.
- **Bugs/Tickets**: Less urgent issues, addressed during regular work hours.

#### Actionability of Alerts

- **Actionable Alerts**: Alerts should prompt a necessary action; non-actionable alerts are just noise.
- **Example**: Adjusting alerting criteria for a cron job to avoid unnecessary noise.

#### Configuring Alerts

- **Metrics Selection**: Identifying which metrics are important for the service.
- **Alert Configuration**: Determining when to raise alerts based on those metrics.
- **Types of Situations**: Deciding which situations warrant pages and which should create bugs or tickets.

#### Decision Making for Alerts

- **Team Discussion**: Necessary to decide which alerts are important and how to handle them.
- **Impact on Work**: Well-configured alerts allow focusing on tasks without constant service monitoring.

#### Upcoming Topics

- Criteria for deciding when to raise alerts and strategies for responding to them.

### Service-level Objectives

### Basic Monitoring in GCP

---

## Troubleshooting and Debugging

### What to Do When You Can't be Physcially There
