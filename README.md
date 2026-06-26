# Temporal IoT Device Onboarding Workflow

## Overview

This project demonstrates how Temporal can orchestrate a long-running IoT device onboarding process. The workflow models the lifecycle of a battery-powered sensor from registration through activation using Temporal's durable workflows.

The use case is based on a real-world IoT platform where customers self-install sensors across multiple sites. Device onboarding requires coordination across several distributed systems including device management, certificate validation, AI-powered installation verification, MQTT provisioning, OTA firmware updates, telemetry validation, and customer notifications.

---

## Business Problem

Traditional orchestration of IoT onboarding is challenging because:

* Multiple distributed systems must coordinate.
* External services may fail or be temporarily unavailable.
* Human intervention may be required.
* Device installation can take minutes or days.
* Workflows must survive application crashes.
* Operators need complete visibility into workflow state.

Implementing this with REST calls, cron jobs, or message queues often leads to complex retry logic, duplicated processing, and lost state.

Temporal solves these problems by providing durable workflow execution.

---

# Workflow

1. Register Device
2. Validate Device Certificate
3. Run AI Installation Photo Validation
4. Wait for Human Approval (if AI confidence is low)
5. Configure MQTT Topics
6. Push OTA Firmware
7. Verify Telemetry
8. Notify Customer

---

# Temporal Features Demonstrated

| Feature           | Usage                           |
| ----------------- | ------------------------------- |
| Workflow          | Device onboarding lifecycle     |
| Activities        | External service calls          |
| Retry Policy      | Recover from transient failures |
| Signal            | Human approval                  |
| Query             | Current onboarding status       |
| Timeout           | Approval waiting period         |
| Compensation      | Rollback after failure          |
| Durable Execution | Survives worker restarts        |

---

# Why Temporal?

Temporal is a strong fit because it provides:

* Durable execution
* Automatic retries
* Human-in-the-loop orchestration
* Long-running workflow support
* Complete execution history
* Built-in observability
* Deterministic workflow execution

without requiring custom orchestration code.

---

# Running

Command Line:

temporal server start-dev

python worker.py

python starter.py

Open the Temporal UI:

http://localhost:8233

---

# Future Enhancements

* Fleet onboarding using Child Workflows
* Parallel provisioning
* Automatic firmware rollback
* Multi-region deployment
* Device health monitoring
* Kafka integration
* AWS IoT Core integration
* Real AI image validation
