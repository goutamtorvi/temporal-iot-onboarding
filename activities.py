from temporalio import activity
import random


@activity.defn
async def register_device(device_id: str) -> str:
    return f"Device {device_id} registered"


@activity.defn
async def validate_certificate(device_id: str) -> str:
    return f"Certificate validated for {device_id}"


@activity.defn
async def validate_install_photo(device_id: str) -> dict:
    # Mock AI confidence score
    confidence = random.randint(70, 99)
    return {"device_id": device_id, "confidence": confidence}


@activity.defn
async def configure_mqtt(device_id: str) -> str:
    return f"MQTT topics configured for {device_id}"


@activity.defn
async def push_firmware(device_id: str) -> str:
    return f"Firmware pushed to {device_id}"


@activity.defn
async def verify_telemetry(device_id: str) -> str:
    return f"Telemetry verified for {device_id}"


@activity.defn
async def notify_customer(device_id: str) -> str:
    return f"Customer notified: {device_id} onboarding complete"


@activity.defn
async def rollback_device(device_id: str) -> str:
    return f"Rollback completed for {device_id}"