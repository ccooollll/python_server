from app import logger

in_memory_store = []

def save_version(version):
    logger.info(f"Saving version: {version}")
    in_memory_store.append(version)
    # make the version unique
    in_memory_store[:] = list(set(in_memory_store))

def versions():
    # Return the list of saved versions
    logger.info("Retrieving saved versions")
    return in_memory_store

def ping(data):
    logger.info(f"Ping received with data: {data}")
    version = data.get("version", "unknown")
    response = {
        "status": "success",
        "message": "Ping received",
        "data": data
    }
    save_version(version)
    return response