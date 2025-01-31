# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kuscia/proto/api/v1alpha1/datamesh/domaindatasource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kuscia.proto.api.v1alpha1 import common_pb2 as kuscia_dot_proto_dot_api_dot_v1alpha1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9kuscia/proto/api/v1alpha1/datamesh/domaindatasource.proto\x12\"kuscia.proto.api.v1alpha1.datamesh\x1a&kuscia/proto/api/v1alpha1/common.proto\"o\n\x1cQueryDomainDataSourceRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12\x15\n\rdatasource_id\x18\x02 \x01(\t\"\x96\x01\n\x1dQueryDomainDataSourceResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\x12\x42\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x34.kuscia.proto.api.v1alpha1.datamesh.DomainDataSource\"\xc2\x01\n\x10\x44omainDataSource\x12\x15\n\rdatasource_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12@\n\x04info\x18\x05 \x01(\x0b\x32\x32.kuscia.proto.api.v1alpha1.datamesh.DataSourceInfo\x12\x10\n\x08info_key\x18\x06 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ss_directly\x18\x07 \x01(\x08\"\xec\x01\n\x0e\x44\x61taSourceInfo\x12H\n\x07localfs\x18\x01 \x01(\x0b\x32\x37.kuscia.proto.api.v1alpha1.datamesh.LocalDataSourceInfo\x12\x42\n\x03oss\x18\x02 \x01(\x0b\x32\x35.kuscia.proto.api.v1alpha1.datamesh.OssDataSourceInfo\x12L\n\x08\x64\x61tabase\x18\x03 \x01(\x0b\x32:.kuscia.proto.api.v1alpha1.datamesh.DatabaseDataSourceInfo\"#\n\x13LocalDataSourceInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\"\xb3\x01\n\x11OssDataSourceInfo\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x15\n\raccess_key_id\x18\x04 \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_key_secret\x18\x05 \x01(\t\x12\x13\n\x0bvirtualhost\x18\x06 \x01(\x08\x12\x0f\n\x07version\x18\x07 \x01(\t\x12\x14\n\x0cstorage_type\x18\x08 \x01(\t\"\\\n\x16\x44\x61tabaseDataSourceInfo\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x04 \x01(\t2\xb8\x01\n\x17\x44omainDataSourceService\x12\x9c\x01\n\x15QueryDomainDataSource\x12@.kuscia.proto.api.v1alpha1.datamesh.QueryDomainDataSourceRequest\x1a\x41.kuscia.proto.api.v1alpha1.datamesh.QueryDomainDataSourceResponseB\\\n org.secretflow.v1alpha1.datameshZ8github.com/secretflow/kuscia/proto/api/v1alpha1/datameshb\x06proto3')



_QUERYDOMAINDATASOURCEREQUEST = DESCRIPTOR.message_types_by_name['QueryDomainDataSourceRequest']
_QUERYDOMAINDATASOURCERESPONSE = DESCRIPTOR.message_types_by_name['QueryDomainDataSourceResponse']
_DOMAINDATASOURCE = DESCRIPTOR.message_types_by_name['DomainDataSource']
_DATASOURCEINFO = DESCRIPTOR.message_types_by_name['DataSourceInfo']
_LOCALDATASOURCEINFO = DESCRIPTOR.message_types_by_name['LocalDataSourceInfo']
_OSSDATASOURCEINFO = DESCRIPTOR.message_types_by_name['OssDataSourceInfo']
_DATABASEDATASOURCEINFO = DESCRIPTOR.message_types_by_name['DatabaseDataSourceInfo']
QueryDomainDataSourceRequest = _reflection.GeneratedProtocolMessageType('QueryDomainDataSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDOMAINDATASOURCEREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.QueryDomainDataSourceRequest)
  })
_sym_db.RegisterMessage(QueryDomainDataSourceRequest)

QueryDomainDataSourceResponse = _reflection.GeneratedProtocolMessageType('QueryDomainDataSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDOMAINDATASOURCERESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.QueryDomainDataSourceResponse)
  })
_sym_db.RegisterMessage(QueryDomainDataSourceResponse)

DomainDataSource = _reflection.GeneratedProtocolMessageType('DomainDataSource', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINDATASOURCE,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.DomainDataSource)
  })
_sym_db.RegisterMessage(DomainDataSource)

DataSourceInfo = _reflection.GeneratedProtocolMessageType('DataSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATASOURCEINFO,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.DataSourceInfo)
  })
_sym_db.RegisterMessage(DataSourceInfo)

LocalDataSourceInfo = _reflection.GeneratedProtocolMessageType('LocalDataSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOCALDATASOURCEINFO,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.LocalDataSourceInfo)
  })
_sym_db.RegisterMessage(LocalDataSourceInfo)

OssDataSourceInfo = _reflection.GeneratedProtocolMessageType('OssDataSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _OSSDATASOURCEINFO,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.OssDataSourceInfo)
  })
_sym_db.RegisterMessage(OssDataSourceInfo)

DatabaseDataSourceInfo = _reflection.GeneratedProtocolMessageType('DatabaseDataSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEDATASOURCEINFO,
  '__module__' : 'kuscia.proto.api.v1alpha1.datamesh.domaindatasource_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.datamesh.DatabaseDataSourceInfo)
  })
_sym_db.RegisterMessage(DatabaseDataSourceInfo)

_DOMAINDATASOURCESERVICE = DESCRIPTOR.services_by_name['DomainDataSourceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n org.secretflow.v1alpha1.datameshZ8github.com/secretflow/kuscia/proto/api/v1alpha1/datamesh'
  _QUERYDOMAINDATASOURCEREQUEST._serialized_start=137
  _QUERYDOMAINDATASOURCEREQUEST._serialized_end=248
  _QUERYDOMAINDATASOURCERESPONSE._serialized_start=251
  _QUERYDOMAINDATASOURCERESPONSE._serialized_end=401
  _DOMAINDATASOURCE._serialized_start=404
  _DOMAINDATASOURCE._serialized_end=598
  _DATASOURCEINFO._serialized_start=601
  _DATASOURCEINFO._serialized_end=837
  _LOCALDATASOURCEINFO._serialized_start=839
  _LOCALDATASOURCEINFO._serialized_end=874
  _OSSDATASOURCEINFO._serialized_start=877
  _OSSDATASOURCEINFO._serialized_end=1056
  _DATABASEDATASOURCEINFO._serialized_start=1058
  _DATABASEDATASOURCEINFO._serialized_end=1150
  _DOMAINDATASOURCESERVICE._serialized_start=1153
  _DOMAINDATASOURCESERVICE._serialized_end=1337
# @@protoc_insertion_point(module_scope)
