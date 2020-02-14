# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import image_pb2 as image__pb2


class ImageTestStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Analyse = channel.stream_stream(
        '/ImageTest/Analyse',
        request_serializer=image__pb2.MsgRequest.SerializeToString,
        response_deserializer=image__pb2.MsgReply.FromString,
        )


class ImageTestServicer(object):
  """The greeting service definition.
  """

  def Analyse(self, request_iterator, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImageTestServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Analyse': grpc.stream_stream_rpc_method_handler(
          servicer.Analyse,
          request_deserializer=image__pb2.MsgRequest.FromString,
          response_serializer=image__pb2.MsgReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ImageTest', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
