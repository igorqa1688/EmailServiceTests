# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EmailServiceGrpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x45mailServiceGrpc.proto\x12\x10\x45mailServiceGrpc\"D\n\x10SendEmailRequest\x12\x11\n\trecipient\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0f\n\x07subject\x18\x03 \x01(\t\"$\n\x11SendEmailResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32h\n\x10\x45mailServiceGrpc\x12T\n\tSendEmail\x12\".EmailServiceGrpc.SendEmailRequest\x1a#.EmailServiceGrpc.SendEmailResponseB\x13\xaa\x02\x10\x45mailServiceGrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EmailServiceGrpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\020EmailServiceGrpc'
  _globals['_SENDEMAILREQUEST']._serialized_start=44
  _globals['_SENDEMAILREQUEST']._serialized_end=112
  _globals['_SENDEMAILRESPONSE']._serialized_start=114
  _globals['_SENDEMAILRESPONSE']._serialized_end=150
  _globals['_EMAILSERVICEGRPC']._serialized_start=152
  _globals['_EMAILSERVICEGRPC']._serialized_end=256
# @@protoc_insertion_point(module_scope)
