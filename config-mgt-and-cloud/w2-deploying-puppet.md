# Deploying Puppet

## Deploying Puppet Locally

### Applying Rules Locally

**Declarative Language:**

- Puppet uses a declarative language, meaning you declare the desired state, not the steps to achieve it.
- This is different from procedural languages like Python or C, where you specify the exact sequence of steps to accomplish a task.

**Idempotency:**

- Idempotency means that an action can be performed repeatedly without changing the system's state after the first execution, with no unintended side effects.
- Most Puppet resources are designed to be idempotent, ensuring consistent results with multiple runs.
- An exception is the **`exec`** resource, which can be non-idempotent if not carefully handled.

**Test and Repair Paradigm:**

- Configuration management tools like Puppet follow the test and repair paradigm.
- Puppet tests whether the desired configuration is already in place and only takes action when necessary to achieve the desired state.

**Statelessness:**

- Puppet is stateless, meaning each Puppet run is independent of previous and future runs.
- During each run, the Puppet agent collects current facts, the master generates rules based on these facts, and the agent applies those rules.