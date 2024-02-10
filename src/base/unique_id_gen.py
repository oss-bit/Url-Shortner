import logging
import time

# logging configurations
loger = logging.getLogger(__name__)
loger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formater)
loger.addHandler(handler)

LAST_TIMESTAMP = -1
MACHINE_BIT = 5
DATACENTER_BITS = 5
SEQUENCE_NUM = 0
SEQUENCE_BIT = 12
SEQUENCE_MASK = (1<< SEQUENCE_BIT) - 1

# MAX BITs are used to deal with machine or datacenter bit overflows
MAX_MACHINE_BITS = (1<<MACHINE_BIT) - 1
MAX_DATACENTER_BITS = (1<< DATACENTER_BITS) - 1

#shifts acts as right padding when combining all snowflake elements
MACHINE_BITS_SHIFT = SEQUENCE_BIT
DATACENTER_BITS_SHIFT = MACHINE_BIT + SEQUENCE_BIT
TIMESTAMP_LEFT_SHIFT = DATACENTER_BITS + MACHINE_BIT + SEQUENCE_BIT

EPOCH =  time.mktime((2023,12,14,0,0,0,0,0,0)) # returns the number of seconds between the data and unix epoch

# returns the current time
def get_timestamp() -> int:
    timestamp = int(time.time()*1000) # converts the time to miliseconds
    return timestamp


def wait_miliseconds(last:int) -> int:
    timestamp = get_timestamp()
    while timestamp <= last:
        timestamp = get_timestamp()
    return timestamp

def snowflake(machine_id:int=0, datacenter_id:int = 0, epoch:int  = None) -> int:
    global LAST_TIMESTAMP
    if epoch is None:
        epoch = EPOCH
    
    machine_id &= MAX_MACHINE_BITS
    datacenter_id &= MAX_DATACENTER_BITS
    
    timestamp = get_timestamp()
    if timestamp < LAST_TIMESTAMP:
        loger.critical("clock moved backwards")
        raise ValueError("clock moved backwards")
    
    if timestamp == LAST_TIMESTAMP:
        SEQUENCE_NUM = (SEQUENCE_NUM +1) & SEQUENCE_MASK
        if SEQUENCE_NUM == 0:
            timestamp = wait_miliseconds(LAST_TIMESTAMP)
    else:
        SEQUENCE_NUM = 0
    LAST_TIMESTAMP = timestamp
    timestamp -=int(epoch*1000)
    return (
        (timestamp<<TIMESTAMP_LEFT_SHIFT)|
        (datacenter_id<<DATACENTER_BITS_SHIFT)|
        (machine_id<<MACHINE_BITS_SHIFT)|
        (SEQUENCE_NUM)
    )

if __name__ == "__main__":
    uuid = snowflake()
    print(uuid)