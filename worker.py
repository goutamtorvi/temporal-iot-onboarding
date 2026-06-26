import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from workflows import DeviceOnboardingWorkflow
from activities import (
    register_device,
    validate_certificate,
    validate_install_photo,
    configure_mqtt,
    push_firmware,
    verify_telemetry,
    notify_customer,
    rollback_device,
)

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="iot-onboarding-task-queue",
        workflows=[DeviceOnboardingWorkflow],
        activities=[
            register_device,
            validate_certificate,
            validate_install_photo,
            configure_mqtt,
            push_firmware,
            verify_telemetry,
            notify_customer,
            rollback_device,
        ],
    )

    print("Worker started...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())