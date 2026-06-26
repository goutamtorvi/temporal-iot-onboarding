import asyncio
from temporalio.client import Client

from workflows import DeviceOnboardingWorkflow

async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        DeviceOnboardingWorkflow.run,
        "device-123",
        id="device-onboarding-device-123",
        task_queue="iot-onboarding-task-queue",
    )

    print(result)

if __name__ == "__main__":
    asyncio.run(main())