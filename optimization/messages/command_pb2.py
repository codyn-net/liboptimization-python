# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import optimization.messages.task_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='optimization/messages/command.proto',
  package='optimization.messages.command',
  serialized_pb='\n#optimization/messages/command.proto\x12\x1doptimization.messages.command\x1a optimization/messages/task.proto\"\x19\n\x0bKillCommand\x12\n\n\x02id\x18\x01 \x02(\r\"2\n\x12SetPriorityCommand\x12\n\n\x02id\x18\x01 \x02(\r\x12\x10\n\x08priority\x18\x02 \x02(\x01\"$\n\x13\x41uthenticateCommand\x12\r\n\x05token\x18\x01 \x01(\t\"\r\n\x0bListCommand\"\x19\n\x0bInfoCommand\x12\n\n\x02id\x18\x01 \x02(\r\"\x1d\n\x0fProgressCommand\x12\n\n\x02id\x18\x01 \x02(\r\"\r\n\x0bIdleCommand\"\xff\x03\n\x07\x43ommand\x12\x38\n\x04type\x18\x01 \x02(\x0e\x32*.optimization.messages.command.CommandType\x12\x38\n\x04list\x18\x02 \x01(\x0b\x32*.optimization.messages.command.ListCommand\x12\x38\n\x04info\x18\x03 \x01(\x0b\x32*.optimization.messages.command.InfoCommand\x12\x38\n\x04kill\x18\x04 \x01(\x0b\x32*.optimization.messages.command.KillCommand\x12\x46\n\x0bsetpriority\x18\x05 \x01(\x0b\x32\x31.optimization.messages.command.SetPriorityCommand\x12H\n\x0c\x61uthenticate\x18\x06 \x01(\x0b\x32\x32.optimization.messages.command.AuthenticateCommand\x12@\n\x08progress\x18\x07 \x01(\x0b\x32..optimization.messages.command.ProgressCommand\x12\x38\n\x04idle\x18\x08 \x01(\x0b\x32*.optimization.messages.command.IdleCommand\"\xb2\x01\n\x03Job\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04user\x18\x03 \x02(\t\x12\x10\n\x08priority\x18\x04 \x02(\x01\x12\x0f\n\x07started\x18\x05 \x02(\x04\x12\x12\n\nlastupdate\x18\x06 \x02(\x04\x12\x10\n\x08progress\x18\x07 \x02(\x01\x12\x14\n\x0ctaskssuccess\x18\x08 \x02(\r\x12\x13\n\x0btasksfailed\x18\t \x02(\r\x12\x0f\n\x07runtime\x18\n \x02(\x01\"?\n\x0cInfoResponse\x12/\n\x03job\x18\x01 \x02(\x0b\x32\".optimization.messages.command.Job\"@\n\x0cListResponse\x12\x30\n\x04jobs\x18\x01 \x03(\x0b\x32\".optimization.messages.command.Job\")\n\x14\x41uthenticateResponse\x12\x11\n\tchallenge\x18\x01 \x02(\t\"\x0e\n\x0cKillResponse\"\x15\n\x13SetPriorityResponse\"\x88\x01\n\x10ProgressResponse\x12?\n\tfitnesses\x18\x01 \x03(\x0b\x32,.optimization.messages.task.Identify.Fitness\x12\x33\n\x05items\x18\x02 \x03(\x0b\x32$.optimization.messages.task.Progress\"\x1f\n\x0cIdleResponse\x12\x0f\n\x07seconds\x18\x01 \x02(\x04\"\xa8\x04\n\x08Response\x12\x38\n\x04type\x18\x01 \x02(\x0e\x32*.optimization.messages.command.CommandType\x12\x0e\n\x06status\x18\x02 \x02(\x08\x12\x0f\n\x07message\x18\x03 \x02(\t\x12\x39\n\x04list\x18\x04 \x01(\x0b\x32+.optimization.messages.command.ListResponse\x12\x39\n\x04info\x18\x05 \x01(\x0b\x32+.optimization.messages.command.InfoResponse\x12\x39\n\x04kill\x18\x06 \x01(\x0b\x32+.optimization.messages.command.KillResponse\x12G\n\x0bsetpriority\x18\x07 \x01(\x0b\x32\x32.optimization.messages.command.SetPriorityResponse\x12I\n\x0c\x61uthenticate\x18\x08 \x01(\x0b\x32\x33.optimization.messages.command.AuthenticateResponse\x12\x41\n\x08progress\x18\t \x01(\x0b\x32/.optimization.messages.command.ProgressResponse\x12\x39\n\x04idle\x18\n \x01(\x0b\x32+.optimization.messages.command.IdleResponse*w\n\x0b\x43ommandType\x12\x08\n\x04List\x10\x00\x12\x08\n\x04Info\x10\x01\x12\x08\n\x04Kill\x10\x02\x12\x0f\n\x0bSetPriority\x10\x03\x12\x10\n\x0c\x41uthenticate\x10\x04\x12\x0c\n\x08Progress\x10\x05\x12\x08\n\x04Idle\x10\x06\x12\x0f\n\x0bNumCommands\x10\x07')

_COMMANDTYPE = descriptor.EnumDescriptor(
  name='CommandType',
  full_name='optimization.messages.command.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='List', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Info', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Kill', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SetPriority', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Authenticate', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Progress', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Idle', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NumCommands', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1944,
  serialized_end=2063,
)


List = 0
Info = 1
Kill = 2
SetPriority = 3
Authenticate = 4
Progress = 5
Idle = 6
NumCommands = 7



_KILLCOMMAND = descriptor.Descriptor(
  name='KillCommand',
  full_name='optimization.messages.command.KillCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='optimization.messages.command.KillCommand.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  serialized_start=104,
  serialized_end=129,
)


_SETPRIORITYCOMMAND = descriptor.Descriptor(
  name='SetPriorityCommand',
  full_name='optimization.messages.command.SetPriorityCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='optimization.messages.command.SetPriorityCommand.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priority', full_name='optimization.messages.command.SetPriorityCommand.priority', index=1,
      number=2, type=1, cpp_type=5, label=2,
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
  extension_ranges=[],
  serialized_start=131,
  serialized_end=181,
)


_AUTHENTICATECOMMAND = descriptor.Descriptor(
  name='AuthenticateCommand',
  full_name='optimization.messages.command.AuthenticateCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='token', full_name='optimization.messages.command.AuthenticateCommand.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=183,
  serialized_end=219,
)


_LISTCOMMAND = descriptor.Descriptor(
  name='ListCommand',
  full_name='optimization.messages.command.ListCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=221,
  serialized_end=234,
)


_INFOCOMMAND = descriptor.Descriptor(
  name='InfoCommand',
  full_name='optimization.messages.command.InfoCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='optimization.messages.command.InfoCommand.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  serialized_start=236,
  serialized_end=261,
)


_PROGRESSCOMMAND = descriptor.Descriptor(
  name='ProgressCommand',
  full_name='optimization.messages.command.ProgressCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='optimization.messages.command.ProgressCommand.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  serialized_start=263,
  serialized_end=292,
)


_IDLECOMMAND = descriptor.Descriptor(
  name='IdleCommand',
  full_name='optimization.messages.command.IdleCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=294,
  serialized_end=307,
)


_COMMAND = descriptor.Descriptor(
  name='Command',
  full_name='optimization.messages.command.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='optimization.messages.command.Command.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='list', full_name='optimization.messages.command.Command.list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='info', full_name='optimization.messages.command.Command.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill', full_name='optimization.messages.command.Command.kill', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='setpriority', full_name='optimization.messages.command.Command.setpriority', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='authenticate', full_name='optimization.messages.command.Command.authenticate', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='progress', full_name='optimization.messages.command.Command.progress', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='idle', full_name='optimization.messages.command.Command.idle', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=310,
  serialized_end=821,
)


_JOB = descriptor.Descriptor(
  name='Job',
  full_name='optimization.messages.command.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='optimization.messages.command.Job.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='optimization.messages.command.Job.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='optimization.messages.command.Job.user', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priority', full_name='optimization.messages.command.Job.priority', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='started', full_name='optimization.messages.command.Job.started', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastupdate', full_name='optimization.messages.command.Job.lastupdate', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='progress', full_name='optimization.messages.command.Job.progress', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taskssuccess', full_name='optimization.messages.command.Job.taskssuccess', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tasksfailed', full_name='optimization.messages.command.Job.tasksfailed', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='runtime', full_name='optimization.messages.command.Job.runtime', index=9,
      number=10, type=1, cpp_type=5, label=2,
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
  extension_ranges=[],
  serialized_start=824,
  serialized_end=1002,
)


_INFORESPONSE = descriptor.Descriptor(
  name='InfoResponse',
  full_name='optimization.messages.command.InfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='job', full_name='optimization.messages.command.InfoResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=1004,
  serialized_end=1067,
)


_LISTRESPONSE = descriptor.Descriptor(
  name='ListResponse',
  full_name='optimization.messages.command.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='jobs', full_name='optimization.messages.command.ListResponse.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1069,
  serialized_end=1133,
)


_AUTHENTICATERESPONSE = descriptor.Descriptor(
  name='AuthenticateResponse',
  full_name='optimization.messages.command.AuthenticateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='challenge', full_name='optimization.messages.command.AuthenticateResponse.challenge', index=0,
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
  serialized_start=1135,
  serialized_end=1176,
)


_KILLRESPONSE = descriptor.Descriptor(
  name='KillResponse',
  full_name='optimization.messages.command.KillResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1178,
  serialized_end=1192,
)


_SETPRIORITYRESPONSE = descriptor.Descriptor(
  name='SetPriorityResponse',
  full_name='optimization.messages.command.SetPriorityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1194,
  serialized_end=1215,
)


_PROGRESSRESPONSE = descriptor.Descriptor(
  name='ProgressResponse',
  full_name='optimization.messages.command.ProgressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fitnesses', full_name='optimization.messages.command.ProgressResponse.fitnesses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='optimization.messages.command.ProgressResponse.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1218,
  serialized_end=1354,
)


_IDLERESPONSE = descriptor.Descriptor(
  name='IdleResponse',
  full_name='optimization.messages.command.IdleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seconds', full_name='optimization.messages.command.IdleResponse.seconds', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  extension_ranges=[],
  serialized_start=1356,
  serialized_end=1387,
)


_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='optimization.messages.command.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='optimization.messages.command.Response.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='optimization.messages.command.Response.status', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='optimization.messages.command.Response.message', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='list', full_name='optimization.messages.command.Response.list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='info', full_name='optimization.messages.command.Response.info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill', full_name='optimization.messages.command.Response.kill', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='setpriority', full_name='optimization.messages.command.Response.setpriority', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='authenticate', full_name='optimization.messages.command.Response.authenticate', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='progress', full_name='optimization.messages.command.Response.progress', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='idle', full_name='optimization.messages.command.Response.idle', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=1390,
  serialized_end=1942,
)

_COMMAND.fields_by_name['type'].enum_type = _COMMANDTYPE
_COMMAND.fields_by_name['list'].message_type = _LISTCOMMAND
_COMMAND.fields_by_name['info'].message_type = _INFOCOMMAND
_COMMAND.fields_by_name['kill'].message_type = _KILLCOMMAND
_COMMAND.fields_by_name['setpriority'].message_type = _SETPRIORITYCOMMAND
_COMMAND.fields_by_name['authenticate'].message_type = _AUTHENTICATECOMMAND
_COMMAND.fields_by_name['progress'].message_type = _PROGRESSCOMMAND
_COMMAND.fields_by_name['idle'].message_type = _IDLECOMMAND
_INFORESPONSE.fields_by_name['job'].message_type = _JOB
_LISTRESPONSE.fields_by_name['jobs'].message_type = _JOB
_PROGRESSRESPONSE.fields_by_name['fitnesses'].message_type = optimization.messages.task_pb2._IDENTIFY_FITNESS
_PROGRESSRESPONSE.fields_by_name['items'].message_type = optimization.messages.task_pb2._PROGRESS
_RESPONSE.fields_by_name['type'].enum_type = _COMMANDTYPE
_RESPONSE.fields_by_name['list'].message_type = _LISTRESPONSE
_RESPONSE.fields_by_name['info'].message_type = _INFORESPONSE
_RESPONSE.fields_by_name['kill'].message_type = _KILLRESPONSE
_RESPONSE.fields_by_name['setpriority'].message_type = _SETPRIORITYRESPONSE
_RESPONSE.fields_by_name['authenticate'].message_type = _AUTHENTICATERESPONSE
_RESPONSE.fields_by_name['progress'].message_type = _PROGRESSRESPONSE
_RESPONSE.fields_by_name['idle'].message_type = _IDLERESPONSE
DESCRIPTOR.message_types_by_name['KillCommand'] = _KILLCOMMAND
DESCRIPTOR.message_types_by_name['SetPriorityCommand'] = _SETPRIORITYCOMMAND
DESCRIPTOR.message_types_by_name['AuthenticateCommand'] = _AUTHENTICATECOMMAND
DESCRIPTOR.message_types_by_name['ListCommand'] = _LISTCOMMAND
DESCRIPTOR.message_types_by_name['InfoCommand'] = _INFOCOMMAND
DESCRIPTOR.message_types_by_name['ProgressCommand'] = _PROGRESSCOMMAND
DESCRIPTOR.message_types_by_name['IdleCommand'] = _IDLECOMMAND
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['InfoResponse'] = _INFORESPONSE
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['AuthenticateResponse'] = _AUTHENTICATERESPONSE
DESCRIPTOR.message_types_by_name['KillResponse'] = _KILLRESPONSE
DESCRIPTOR.message_types_by_name['SetPriorityResponse'] = _SETPRIORITYRESPONSE
DESCRIPTOR.message_types_by_name['ProgressResponse'] = _PROGRESSRESPONSE
DESCRIPTOR.message_types_by_name['IdleResponse'] = _IDLERESPONSE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class KillCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KILLCOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.KillCommand)

class SetPriorityCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETPRIORITYCOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.SetPriorityCommand)

class AuthenticateCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHENTICATECOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.AuthenticateCommand)

class ListCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTCOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.ListCommand)

class InfoCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INFOCOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.InfoCommand)

class ProgressCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROGRESSCOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.ProgressCommand)

class IdleCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDLECOMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.IdleCommand)

class Command(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMAND
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.Command)

class Job(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOB
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.Job)

class InfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INFORESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.InfoResponse)

class ListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.ListResponse)

class AuthenticateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHENTICATERESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.AuthenticateResponse)

class KillResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KILLRESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.KillResponse)

class SetPriorityResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETPRIORITYRESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.SetPriorityResponse)

class ProgressResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROGRESSRESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.ProgressResponse)

class IdleResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDLERESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.IdleResponse)

class Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE
  
  # @@protoc_insertion_point(class_scope:optimization.messages.command.Response)

# @@protoc_insertion_point(module_scope)
