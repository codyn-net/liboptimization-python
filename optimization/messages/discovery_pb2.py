# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='optimization/messages/discovery.proto',
  package='optimization.messages.discovery',
  serialized_pb='\n%optimization/messages/discovery.proto\x12\x1foptimization.messages.discovery\"\x1e\n\x08Greeting\x12\x12\n\nconnection\x18\x01 \x02(\t\"\x1c\n\x06Wakeup\x12\x12\n\nconnection\x18\x01 \x02(\t\"\xfd\x01\n\tDiscovery\x12=\n\x04type\x18\x01 \x02(\x0e\x32/.optimization.messages.discovery.Discovery.Type\x12;\n\x08greeting\x18\x02 \x01(\x0b\x32).optimization.messages.discovery.Greeting\x12\x37\n\x06wakeup\x18\x03 \x01(\x0b\x32\'.optimization.messages.discovery.Wakeup\x12\x11\n\tnamespace\x18\x04 \x01(\t\"(\n\x04Type\x12\x10\n\x0cTypeGreeting\x10\x00\x12\x0e\n\nTypeWakeup\x10\x01')



_DISCOVERY_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='optimization.messages.discovery.Discovery.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TypeGreeting', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TypeWakeup', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=350,
  serialized_end=390,
)


_GREETING = descriptor.Descriptor(
  name='Greeting',
  full_name='optimization.messages.discovery.Greeting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='connection', full_name='optimization.messages.discovery.Greeting.connection', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=74,
  serialized_end=104,
)


_WAKEUP = descriptor.Descriptor(
  name='Wakeup',
  full_name='optimization.messages.discovery.Wakeup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='connection', full_name='optimization.messages.discovery.Wakeup.connection', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=106,
  serialized_end=134,
)


_DISCOVERY = descriptor.Descriptor(
  name='Discovery',
  full_name='optimization.messages.discovery.Discovery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='optimization.messages.discovery.Discovery.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='greeting', full_name='optimization.messages.discovery.Discovery.greeting', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wakeup', full_name='optimization.messages.discovery.Discovery.wakeup', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='namespace', full_name='optimization.messages.discovery.Discovery.namespace', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DISCOVERY_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=137,
  serialized_end=390,
)

_DISCOVERY.fields_by_name['type'].enum_type = _DISCOVERY_TYPE
_DISCOVERY.fields_by_name['greeting'].message_type = _GREETING
_DISCOVERY.fields_by_name['wakeup'].message_type = _WAKEUP
_DISCOVERY_TYPE.containing_type = _DISCOVERY;
DESCRIPTOR.message_types_by_name['Greeting'] = _GREETING
DESCRIPTOR.message_types_by_name['Wakeup'] = _WAKEUP
DESCRIPTOR.message_types_by_name['Discovery'] = _DISCOVERY

class Greeting(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GREETING
  
  # @@protoc_insertion_point(class_scope:optimization.messages.discovery.Greeting)

class Wakeup(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WAKEUP
  
  # @@protoc_insertion_point(class_scope:optimization.messages.discovery.Wakeup)

class Discovery(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DISCOVERY
  
  # @@protoc_insertion_point(class_scope:optimization.messages.discovery.Discovery)

# @@protoc_insertion_point(module_scope)
