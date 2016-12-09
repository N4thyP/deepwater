# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf import meta_graph_pb2 as tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='deepwater',
  syntax='proto3',
  serialized_pb=_b('\n\rservice.proto\x12\tdeepwater\x1a)tensorflow/core/protobuf/meta_graph.proto\"\xbf\x01\n\nParamValue\x12\x0b\n\x01s\x18\x02 \x01(\x0cH\x00\x12\x0b\n\x01i\x18\x03 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01\x62\x18\x05 \x01(\x08H\x00\x12/\n\x04list\x18\x01 \x01(\x0b\x32\x1f.deepwater.ParamValue.ListValueH\x00\x1a\x43\n\tListValue\x12\t\n\x01s\x18\x02 \x03(\x0c\x12\r\n\x01i\x18\x03 \x03(\x03\x42\x02\x10\x01\x12\r\n\x01\x66\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\r\n\x01\x62\x18\x05 \x03(\x08\x42\x02\x10\x01\x42\x07\n\x05value\"\x8d\x01\n\x0eNetworkRequest\x12\x35\n\x06params\x18\x01 \x03(\x0b\x32%.deepwater.NetworkRequest.ParamsEntry\x1a\x44\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.deepwater.ParamValue:\x02\x38\x01\"_\n\x0fNetworkResponse\x12)\n\x07network\x18\x01 \x01(\x0b\x32\x18.tensorflow.MetaGraphDef\x12!\n\x06status\x18\x02 \x01(\x0b\x32\x11.deepwater.Status\"\r\n\x0bPingRequest\"\x08\n\x06Status2\x87\x01\n\x07Service\x12\x33\n\x04Ping\x12\x16.deepwater.PingRequest\x1a\x11.deepwater.Status\"\x00\x12G\n\x0c\x42uildNetwork\x12\x19.deepwater.NetworkRequest\x1a\x1a.deepwater.NetworkResponse\"\x00\x42!\n\x10\x61i.h2o.deepwaterB\x0bGRPCServiceP\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMVALUE_LISTVALUE = _descriptor.Descriptor(
  name='ListValue',
  full_name='deepwater.ParamValue.ListValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='deepwater.ParamValue.ListValue.s', index=0,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i', full_name='deepwater.ParamValue.ListValue.i', index=1,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='f', full_name='deepwater.ParamValue.ListValue.f', index=2,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='b', full_name='deepwater.ParamValue.ListValue.b', index=3,
      number=5, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=187,
  serialized_end=254,
)

_PARAMVALUE = _descriptor.Descriptor(
  name='ParamValue',
  full_name='deepwater.ParamValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='deepwater.ParamValue.s', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i', full_name='deepwater.ParamValue.i', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f', full_name='deepwater.ParamValue.f', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='deepwater.ParamValue.b', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='deepwater.ParamValue.list', index=4,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PARAMVALUE_LISTVALUE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='deepwater.ParamValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=263,
)


_NETWORKREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='deepwater.NetworkRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='deepwater.NetworkRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='deepwater.NetworkRequest.ParamsEntry.value', index=1,
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
  serialized_start=339,
  serialized_end=407,
)

_NETWORKREQUEST = _descriptor.Descriptor(
  name='NetworkRequest',
  full_name='deepwater.NetworkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='deepwater.NetworkRequest.params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NETWORKREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=407,
)


_NETWORKRESPONSE = _descriptor.Descriptor(
  name='NetworkResponse',
  full_name='deepwater.NetworkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='deepwater.NetworkResponse.network', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='deepwater.NetworkResponse.status', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=504,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='deepwater.PingRequest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=519,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='deepwater.Status',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=529,
)

_PARAMVALUE_LISTVALUE.containing_type = _PARAMVALUE
_PARAMVALUE.fields_by_name['list'].message_type = _PARAMVALUE_LISTVALUE
_PARAMVALUE.oneofs_by_name['value'].fields.append(
  _PARAMVALUE.fields_by_name['s'])
_PARAMVALUE.fields_by_name['s'].containing_oneof = _PARAMVALUE.oneofs_by_name['value']
_PARAMVALUE.oneofs_by_name['value'].fields.append(
  _PARAMVALUE.fields_by_name['i'])
_PARAMVALUE.fields_by_name['i'].containing_oneof = _PARAMVALUE.oneofs_by_name['value']
_PARAMVALUE.oneofs_by_name['value'].fields.append(
  _PARAMVALUE.fields_by_name['f'])
_PARAMVALUE.fields_by_name['f'].containing_oneof = _PARAMVALUE.oneofs_by_name['value']
_PARAMVALUE.oneofs_by_name['value'].fields.append(
  _PARAMVALUE.fields_by_name['b'])
_PARAMVALUE.fields_by_name['b'].containing_oneof = _PARAMVALUE.oneofs_by_name['value']
_PARAMVALUE.oneofs_by_name['value'].fields.append(
  _PARAMVALUE.fields_by_name['list'])
_PARAMVALUE.fields_by_name['list'].containing_oneof = _PARAMVALUE.oneofs_by_name['value']
_NETWORKREQUEST_PARAMSENTRY.fields_by_name['value'].message_type = _PARAMVALUE
_NETWORKREQUEST_PARAMSENTRY.containing_type = _NETWORKREQUEST
_NETWORKREQUEST.fields_by_name['params'].message_type = _NETWORKREQUEST_PARAMSENTRY
_NETWORKRESPONSE.fields_by_name['network'].message_type = tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2._METAGRAPHDEF
_NETWORKRESPONSE.fields_by_name['status'].message_type = _STATUS
DESCRIPTOR.message_types_by_name['ParamValue'] = _PARAMVALUE
DESCRIPTOR.message_types_by_name['NetworkRequest'] = _NETWORKREQUEST
DESCRIPTOR.message_types_by_name['NetworkResponse'] = _NETWORKRESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS

ParamValue = _reflection.GeneratedProtocolMessageType('ParamValue', (_message.Message,), dict(

  ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), dict(
    DESCRIPTOR = _PARAMVALUE_LISTVALUE,
    __module__ = 'service_pb2'
    # @@protoc_insertion_point(class_scope:deepwater.ParamValue.ListValue)
    ))
  ,
  DESCRIPTOR = _PARAMVALUE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:deepwater.ParamValue)
  ))
_sym_db.RegisterMessage(ParamValue)
_sym_db.RegisterMessage(ParamValue.ListValue)

NetworkRequest = _reflection.GeneratedProtocolMessageType('NetworkRequest', (_message.Message,), dict(

  ParamsEntry = _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _NETWORKREQUEST_PARAMSENTRY,
    __module__ = 'service_pb2'
    # @@protoc_insertion_point(class_scope:deepwater.NetworkRequest.ParamsEntry)
    ))
  ,
  DESCRIPTOR = _NETWORKREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:deepwater.NetworkRequest)
  ))
_sym_db.RegisterMessage(NetworkRequest)
_sym_db.RegisterMessage(NetworkRequest.ParamsEntry)

NetworkResponse = _reflection.GeneratedProtocolMessageType('NetworkResponse', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:deepwater.NetworkResponse)
  ))
_sym_db.RegisterMessage(NetworkResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:deepwater.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:deepwater.Status)
  ))
_sym_db.RegisterMessage(Status)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020ai.h2o.deepwaterB\013GRPCServiceP\001'))
_PARAMVALUE_LISTVALUE.fields_by_name['i'].has_options = True
_PARAMVALUE_LISTVALUE.fields_by_name['i']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_PARAMVALUE_LISTVALUE.fields_by_name['f'].has_options = True
_PARAMVALUE_LISTVALUE.fields_by_name['f']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_PARAMVALUE_LISTVALUE.fields_by_name['b'].has_options = True
_PARAMVALUE_LISTVALUE.fields_by_name['b']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_NETWORKREQUEST_PARAMSENTRY.has_options = True
_NETWORKREQUEST_PARAMSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/deepwater.Service/Ping',
        request_serializer=PingRequest.SerializeToString,
        response_deserializer=Status.FromString,
        )
    self.BuildNetwork = channel.unary_unary(
        '/deepwater.Service/BuildNetwork',
        request_serializer=NetworkRequest.SerializeToString,
        response_deserializer=NetworkResponse.FromString,
        )


class ServiceServicer(object):

  def Ping(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BuildNetwork(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=PingRequest.FromString,
          response_serializer=Status.SerializeToString,
      ),
      'BuildNetwork': grpc.unary_unary_rpc_method_handler(
          servicer.BuildNetwork,
          request_deserializer=NetworkRequest.FromString,
          response_serializer=NetworkResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'deepwater.Service', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaServiceServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Ping(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def BuildNetwork(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaServiceStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Ping(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Ping.future = None
  def BuildNetwork(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  BuildNetwork.future = None


def beta_create_Service_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('deepwater.Service', 'BuildNetwork'): NetworkRequest.FromString,
    ('deepwater.Service', 'Ping'): PingRequest.FromString,
  }
  response_serializers = {
    ('deepwater.Service', 'BuildNetwork'): NetworkResponse.SerializeToString,
    ('deepwater.Service', 'Ping'): Status.SerializeToString,
  }
  method_implementations = {
    ('deepwater.Service', 'BuildNetwork'): face_utilities.unary_unary_inline(servicer.BuildNetwork),
    ('deepwater.Service', 'Ping'): face_utilities.unary_unary_inline(servicer.Ping),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Service_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('deepwater.Service', 'BuildNetwork'): NetworkRequest.SerializeToString,
    ('deepwater.Service', 'Ping'): PingRequest.SerializeToString,
  }
  response_deserializers = {
    ('deepwater.Service', 'BuildNetwork'): NetworkResponse.FromString,
    ('deepwater.Service', 'Ping'): Status.FromString,
  }
  cardinalities = {
    'BuildNetwork': cardinality.Cardinality.UNARY_UNARY,
    'Ping': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'deepwater.Service', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)