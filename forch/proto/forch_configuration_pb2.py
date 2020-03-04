# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/forch_configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/forch_configuration.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n%forch/proto/forch_configuration.proto\"v\n\x0b\x46orchConfig\x12\x19\n\x04site\x18\x01 \x01(\x0b\x32\x0b.SiteConfig\x12+\n\rorchestration\x18\x02 \x01(\x0b\x32\x14.OrchestrationConfig\x12\x1f\n\x07process\x18\x03 \x01(\x0b\x32\x0e.ProcessConfig\"\xc3\x01\n\nSiteConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x0b\x63ontrollers\x18\x02 \x03(\x0b\x32\x1c.SiteConfig.ControllersEntry\x1aJ\n\x10\x43ontrollersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.SiteConfig.Controller:\x02\x38\x01\x1a(\n\nController\x12\x0c\n\x04\x66qdn\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xa6\x04\n\x13OrchestrationConfig\x12\x1e\n\x16structural_config_file\x18\x01 \x01(\t\x12\x1e\n\x16\x62\x65havioral_config_file\x18\x02 \x01(\t\x12\x1f\n\x17static_device_placement\x18\x03 \x01(\t\x12\x1e\n\x16static_device_behavior\x18\x04 \x01(\t\x12\x1b\n\x13segments_vlans_file\x18\x05 \x01(\t\x12\x1e\n\x16\x66\x61ucetize_interval_sec\x18\x06 \x01(\x05\x12\x34\n\x0b\x61uth_config\x18\x07 \x01(\x0b\x32\x1f.OrchestrationConfig.AuthConfig\x1a\xc6\x01\n\nAuthConfig\x12\x34\n\x0bradius_info\x18\x01 \x01(\x0b\x32\x1f.OrchestrationConfig.RadiusInfo\x12\x15\n\rheartbeat_sec\x18\x02 \x01(\x05\x12\x1a\n\x12max_radius_backoff\x18\x03 \x01(\x05\x12\x19\n\x11query_timeout_sec\x18\x04 \x01(\x05\x12\x1a\n\x12reject_timeout_sec\x18\x05 \x01(\x05\x12\x18\n\x10\x61uth_timeout_sec\x18\x06 \x01(\x05\x1aR\n\nRadiusInfo\x12\x11\n\tserver_ip\x18\x01 \x01(\t\x12\x13\n\x0bserver_port\x18\x02 \x01(\x05\x12\x1c\n\x14radius_secret_helper\x18\x03 \x01(\t\"\x8b\x03\n\rProcessConfig\x12\x19\n\x11scan_interval_sec\x18\x01 \x01(\x05\x12\x12\n\ncheck_vrrp\x18\x02 \x01(\x08\x12\x30\n\tprocesses\x18\x03 \x03(\x0b\x32\x1d.ProcessConfig.ProcessesEntry\x12\x34\n\x0b\x63onnections\x18\x04 \x03(\x0b\x32\x1f.ProcessConfig.ConnectionsEntry\x1aH\n\x0eProcessesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.ProcessConfig.Process:\x02\x38\x01\x1aM\n\x10\x43onnectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.ProcessConfig.Connection:\x02\x38\x01\x1a\'\n\x07Process\x12\r\n\x05regex\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x1a!\n\nConnection\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORCHCONFIG = _descriptor.Descriptor(
  name='ForchConfig',
  full_name='ForchConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='site', full_name='ForchConfig.site', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orchestration', full_name='ForchConfig.orchestration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process', full_name='ForchConfig.process', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=159,
)


_SITECONFIG_CONTROLLERSENTRY = _descriptor.Descriptor(
  name='ControllersEntry',
  full_name='SiteConfig.ControllersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SiteConfig.ControllersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SiteConfig.ControllersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=315,
)

_SITECONFIG_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='SiteConfig.Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fqdn', full_name='SiteConfig.Controller.fqdn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='SiteConfig.Controller.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=357,
)

_SITECONFIG = _descriptor.Descriptor(
  name='SiteConfig',
  full_name='SiteConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SiteConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controllers', full_name='SiteConfig.controllers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SITECONFIG_CONTROLLERSENTRY, _SITECONFIG_CONTROLLER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=357,
)


_ORCHESTRATIONCONFIG_AUTHCONFIG = _descriptor.Descriptor(
  name='AuthConfig',
  full_name='OrchestrationConfig.AuthConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius_info', full_name='OrchestrationConfig.AuthConfig.radius_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heartbeat_sec', full_name='OrchestrationConfig.AuthConfig.heartbeat_sec', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_radius_backoff', full_name='OrchestrationConfig.AuthConfig.max_radius_backoff', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_timeout_sec', full_name='OrchestrationConfig.AuthConfig.query_timeout_sec', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reject_timeout_sec', full_name='OrchestrationConfig.AuthConfig.reject_timeout_sec', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_timeout_sec', full_name='OrchestrationConfig.AuthConfig.auth_timeout_sec', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=826,
)

_ORCHESTRATIONCONFIG_RADIUSINFO = _descriptor.Descriptor(
  name='RadiusInfo',
  full_name='OrchestrationConfig.RadiusInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_ip', full_name='OrchestrationConfig.RadiusInfo.server_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_port', full_name='OrchestrationConfig.RadiusInfo.server_port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radius_secret_helper', full_name='OrchestrationConfig.RadiusInfo.radius_secret_helper', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=910,
)

_ORCHESTRATIONCONFIG = _descriptor.Descriptor(
  name='OrchestrationConfig',
  full_name='OrchestrationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='structural_config_file', full_name='OrchestrationConfig.structural_config_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='behavioral_config_file', full_name='OrchestrationConfig.behavioral_config_file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_device_placement', full_name='OrchestrationConfig.static_device_placement', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_device_behavior', full_name='OrchestrationConfig.static_device_behavior', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segments_vlans_file', full_name='OrchestrationConfig.segments_vlans_file', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faucetize_interval_sec', full_name='OrchestrationConfig.faucetize_interval_sec', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_config', full_name='OrchestrationConfig.auth_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ORCHESTRATIONCONFIG_AUTHCONFIG, _ORCHESTRATIONCONFIG_RADIUSINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=910,
)


_PROCESSCONFIG_PROCESSESENTRY = _descriptor.Descriptor(
  name='ProcessesEntry',
  full_name='ProcessConfig.ProcessesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ProcessConfig.ProcessesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ProcessConfig.ProcessesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1081,
  serialized_end=1153,
)

_PROCESSCONFIG_CONNECTIONSENTRY = _descriptor.Descriptor(
  name='ConnectionsEntry',
  full_name='ProcessConfig.ConnectionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ProcessConfig.ConnectionsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ProcessConfig.ConnectionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1155,
  serialized_end=1232,
)

_PROCESSCONFIG_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='ProcessConfig.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regex', full_name='ProcessConfig.Process.regex', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='ProcessConfig.Process.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=1273,
)

_PROCESSCONFIG_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='ProcessConfig.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='ProcessConfig.Connection.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1275,
  serialized_end=1308,
)

_PROCESSCONFIG = _descriptor.Descriptor(
  name='ProcessConfig',
  full_name='ProcessConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_interval_sec', full_name='ProcessConfig.scan_interval_sec', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_vrrp', full_name='ProcessConfig.check_vrrp', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processes', full_name='ProcessConfig.processes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='ProcessConfig.connections', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROCESSCONFIG_PROCESSESENTRY, _PROCESSCONFIG_CONNECTIONSENTRY, _PROCESSCONFIG_PROCESS, _PROCESSCONFIG_CONNECTION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=913,
  serialized_end=1308,
)

_FORCHCONFIG.fields_by_name['site'].message_type = _SITECONFIG
_FORCHCONFIG.fields_by_name['orchestration'].message_type = _ORCHESTRATIONCONFIG
_FORCHCONFIG.fields_by_name['process'].message_type = _PROCESSCONFIG
_SITECONFIG_CONTROLLERSENTRY.fields_by_name['value'].message_type = _SITECONFIG_CONTROLLER
_SITECONFIG_CONTROLLERSENTRY.containing_type = _SITECONFIG
_SITECONFIG_CONTROLLER.containing_type = _SITECONFIG
_SITECONFIG.fields_by_name['controllers'].message_type = _SITECONFIG_CONTROLLERSENTRY
_ORCHESTRATIONCONFIG_AUTHCONFIG.fields_by_name['radius_info'].message_type = _ORCHESTRATIONCONFIG_RADIUSINFO
_ORCHESTRATIONCONFIG_AUTHCONFIG.containing_type = _ORCHESTRATIONCONFIG
_ORCHESTRATIONCONFIG_RADIUSINFO.containing_type = _ORCHESTRATIONCONFIG
_ORCHESTRATIONCONFIG.fields_by_name['auth_config'].message_type = _ORCHESTRATIONCONFIG_AUTHCONFIG
_PROCESSCONFIG_PROCESSESENTRY.fields_by_name['value'].message_type = _PROCESSCONFIG_PROCESS
_PROCESSCONFIG_PROCESSESENTRY.containing_type = _PROCESSCONFIG
_PROCESSCONFIG_CONNECTIONSENTRY.fields_by_name['value'].message_type = _PROCESSCONFIG_CONNECTION
_PROCESSCONFIG_CONNECTIONSENTRY.containing_type = _PROCESSCONFIG
_PROCESSCONFIG_PROCESS.containing_type = _PROCESSCONFIG
_PROCESSCONFIG_CONNECTION.containing_type = _PROCESSCONFIG
_PROCESSCONFIG.fields_by_name['processes'].message_type = _PROCESSCONFIG_PROCESSESENTRY
_PROCESSCONFIG.fields_by_name['connections'].message_type = _PROCESSCONFIG_CONNECTIONSENTRY
DESCRIPTOR.message_types_by_name['ForchConfig'] = _FORCHCONFIG
DESCRIPTOR.message_types_by_name['SiteConfig'] = _SITECONFIG
DESCRIPTOR.message_types_by_name['OrchestrationConfig'] = _ORCHESTRATIONCONFIG
DESCRIPTOR.message_types_by_name['ProcessConfig'] = _PROCESSCONFIG

ForchConfig = _reflection.GeneratedProtocolMessageType('ForchConfig', (_message.Message,), dict(
  DESCRIPTOR = _FORCHCONFIG,
  __module__ = 'forch.proto.forch_configuration_pb2'
  # @@protoc_insertion_point(class_scope:ForchConfig)
  ))
_sym_db.RegisterMessage(ForchConfig)

SiteConfig = _reflection.GeneratedProtocolMessageType('SiteConfig', (_message.Message,), dict(

  ControllersEntry = _reflection.GeneratedProtocolMessageType('ControllersEntry', (_message.Message,), dict(
    DESCRIPTOR = _SITECONFIG_CONTROLLERSENTRY,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:SiteConfig.ControllersEntry)
    ))
  ,

  Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), dict(
    DESCRIPTOR = _SITECONFIG_CONTROLLER,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:SiteConfig.Controller)
    ))
  ,
  DESCRIPTOR = _SITECONFIG,
  __module__ = 'forch.proto.forch_configuration_pb2'
  # @@protoc_insertion_point(class_scope:SiteConfig)
  ))
_sym_db.RegisterMessage(SiteConfig)
_sym_db.RegisterMessage(SiteConfig.ControllersEntry)
_sym_db.RegisterMessage(SiteConfig.Controller)

OrchestrationConfig = _reflection.GeneratedProtocolMessageType('OrchestrationConfig', (_message.Message,), dict(

  AuthConfig = _reflection.GeneratedProtocolMessageType('AuthConfig', (_message.Message,), dict(
    DESCRIPTOR = _ORCHESTRATIONCONFIG_AUTHCONFIG,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:OrchestrationConfig.AuthConfig)
    ))
  ,

  RadiusInfo = _reflection.GeneratedProtocolMessageType('RadiusInfo', (_message.Message,), dict(
    DESCRIPTOR = _ORCHESTRATIONCONFIG_RADIUSINFO,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:OrchestrationConfig.RadiusInfo)
    ))
  ,
  DESCRIPTOR = _ORCHESTRATIONCONFIG,
  __module__ = 'forch.proto.forch_configuration_pb2'
  # @@protoc_insertion_point(class_scope:OrchestrationConfig)
  ))
_sym_db.RegisterMessage(OrchestrationConfig)
_sym_db.RegisterMessage(OrchestrationConfig.AuthConfig)
_sym_db.RegisterMessage(OrchestrationConfig.RadiusInfo)

ProcessConfig = _reflection.GeneratedProtocolMessageType('ProcessConfig', (_message.Message,), dict(

  ProcessesEntry = _reflection.GeneratedProtocolMessageType('ProcessesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROCESSCONFIG_PROCESSESENTRY,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:ProcessConfig.ProcessesEntry)
    ))
  ,

  ConnectionsEntry = _reflection.GeneratedProtocolMessageType('ConnectionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROCESSCONFIG_CONNECTIONSENTRY,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:ProcessConfig.ConnectionsEntry)
    ))
  ,

  Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), dict(
    DESCRIPTOR = _PROCESSCONFIG_PROCESS,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:ProcessConfig.Process)
    ))
  ,

  Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), dict(
    DESCRIPTOR = _PROCESSCONFIG_CONNECTION,
    __module__ = 'forch.proto.forch_configuration_pb2'
    # @@protoc_insertion_point(class_scope:ProcessConfig.Connection)
    ))
  ,
  DESCRIPTOR = _PROCESSCONFIG,
  __module__ = 'forch.proto.forch_configuration_pb2'
  # @@protoc_insertion_point(class_scope:ProcessConfig)
  ))
_sym_db.RegisterMessage(ProcessConfig)
_sym_db.RegisterMessage(ProcessConfig.ProcessesEntry)
_sym_db.RegisterMessage(ProcessConfig.ConnectionsEntry)
_sym_db.RegisterMessage(ProcessConfig.Process)
_sym_db.RegisterMessage(ProcessConfig.Connection)


_SITECONFIG_CONTROLLERSENTRY.has_options = True
_SITECONFIG_CONTROLLERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PROCESSCONFIG_PROCESSESENTRY.has_options = True
_PROCESSCONFIG_PROCESSESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PROCESSCONFIG_CONNECTIONSENTRY.has_options = True
_PROCESSCONFIG_CONNECTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
