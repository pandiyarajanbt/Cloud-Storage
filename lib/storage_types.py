from enum import Enum

class StorageType(Enum):
    PERSONAL = 'personal'
    SHARED = 'shared'
    BACKUP = 'backup'
    MEDIUM = 'medium'
    DATABASE = 'database'
    ARCHIVE = 'archive'

class StorageStatus(Enum):
    ACTIVE = 'active'
    SUSPENDED = 'suspended'
    FULL = 'full'
    DELETED = 'deleted'

class StorageNodeType(Enum):
    HDD = 'HDD'
    SSD = 'SSD'
    NVME = 'NVME'
    HYBRID = 'Hybrid'
    OBJECT = 'Object'
    BLOCK = 'Block'
    COLD = 'Cold'

class StorageNodeStatus(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    MAINTENANCE = 'maintenance'
    FULL = 'full'
    DEGRADED = 'degraded'
    FAILED = 'failed'

class StorageNodeTier(Enum):
    HOT = 'hot'
    WARM = 'warm'
    COLD = 'cold'
