"""
    Use the builders for creating Database thrift object.
    Some arguments are optional when creating a thrift object.
    Check Builder constructor for more information.
"""

from hive_metastore_client.builders import DatabaseBuilder
from hive_metastore_client import HiveMetastoreClient

HIVE_HOST = "host.docker.internal"
HIVE_PORT = 9083

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Delete database from thrift table object
    hive_client.drop_database(name="database_name", deleteData=True, cascade=True)
