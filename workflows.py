from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
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


@workflow.defn
class DeviceOnboardingWorkflow:
    def __init__(self):
        self.status = "Not started"
        self.human_approved = False

    @workflow.run
    async def run(self, device_id: str) -> str:
        try:
            self.status = "Registering device"
            await workflow.execute_activity(
                register_device,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Validating certificate"
            await workflow.execute_activity(
                validate_certificate,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Running AI install photo validation"
            result = await workflow.execute_activity(
                validate_install_photo,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            if result["confidence"] < 90:
                self.status = "Waiting for human approval"
                await workflow.wait_condition(
                    lambda: self.human_approved,
                    timeout=timedelta(minutes=2),
                )

            self.status = "Configuring MQTT"
            await workflow.execute_activity(
                configure_mqtt,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Pushing OTA firmware"
            await workflow.execute_activity(
                push_firmware,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Verifying telemetry"
            await workflow.execute_activity(
                verify_telemetry,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Notifying customer"
            await workflow.execute_activity(
                notify_customer,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )

            self.status = "Completed"
            return f"Device {device_id} successfully onboarded"

        except Exception:
            self.status = "Rolling back"
            await workflow.execute_activity(
                rollback_device,
                device_id,
                start_to_close_timeout=timedelta(seconds=10),
            )
            raise

    @workflow.signal
    async def approve_installation(self):
        self.human_approved = True

    @workflow.query
    def get_status(self) -> str:
        return self.status