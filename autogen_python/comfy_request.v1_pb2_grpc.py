# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from comfy_request import v1_pb2 as comfy__request_dot_v1__pb2
from google import empty_pb2 as google_dot_empty__pb2


class ComfyStub(object):
    """====== Service Definitions ======

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Run = channel.unary_unary(
                '/comfy_request.v1.Comfy/Run',
                request_serializer=comfy__request_dot_v1__pb2.ComfyRequest.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.JobSnapshot.FromString,
                )
        self.RunSync = channel.unary_stream(
                '/comfy_request.v1.Comfy/RunSync',
                request_serializer=comfy__request_dot_v1__pb2.ComfyRequest.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.JobOutput.FromString,
                )
        self.GetJob = channel.unary_unary(
                '/comfy_request.v1.Comfy/GetJob',
                request_serializer=comfy__request_dot_v1__pb2.JobId.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.JobSnapshot.FromString,
                )
        self.GetNodeDefinitions = channel.unary_unary(
                '/comfy_request.v1.Comfy/GetNodeDefinitions',
                request_serializer=comfy__request_dot_v1__pb2.NodeDefRequest.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.NodeDefs.FromString,
                )
        self.GetModelCatalog = channel.unary_unary(
                '/comfy_request.v1.Comfy/GetModelCatalog',
                request_serializer=comfy__request_dot_v1__pb2.ModelCatalogRequest.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.ModelCatalog.FromString,
                )
        self.SyncLocalFiles = channel.unary_stream(
                '/comfy_request.v1.Comfy/SyncLocalFiles',
                request_serializer=google_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=comfy__request_dot_v1__pb2.LocalFiles.FromString,
                )


class ComfyServicer(object):
    """====== Service Definitions ======

    """

    def Run(self, request, context):
        """Queue a workflow and receive the job id.
        Results can be retrieved from the graph-id or via a webhook callback.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunSync(self, request, context):
        """Queue a workflow and await its outputs (synchronous)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJob(self, request, context):
        """Looks up the most current job state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodeDefinitions(self, request, context):
        """Cancels a specific job (regardless if it's running or queued)
        This is a combination of 'delete' and 'interrupt' from ComfyUI.
        rpc CancelJob (JobId) returns (google.protobuf.Empty) {};

        Cancels all queued (pending) jobs in a given session-id that this user created
        ComfyUI calls this 'clear'
        rpc PurgeSessionQueue (SessionId) returns (google.protobuf.Empty) {};

        Returns a list of outputs from a given user
        rpc GetUserHistory (UserId) returns (UserHistory) {};

        Removes the JobOutputs from memory for a given user
        rpc ClearUserHistory (UserId) returns (google.protobuf.Empty) {};

        Gets the definitions of all nodes supported by this server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModelCatalog(self, request, context):
        """Get models, grouped by architecture
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncLocalFiles(self, request, context):
        """Streams updates to local-files in realtime.
        This is only used when running Comfy Creator with local files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComfyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=comfy__request_dot_v1__pb2.ComfyRequest.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.JobSnapshot.SerializeToString,
            ),
            'RunSync': grpc.unary_stream_rpc_method_handler(
                    servicer.RunSync,
                    request_deserializer=comfy__request_dot_v1__pb2.ComfyRequest.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.JobOutput.SerializeToString,
            ),
            'GetJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJob,
                    request_deserializer=comfy__request_dot_v1__pb2.JobId.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.JobSnapshot.SerializeToString,
            ),
            'GetNodeDefinitions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodeDefinitions,
                    request_deserializer=comfy__request_dot_v1__pb2.NodeDefRequest.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.NodeDefs.SerializeToString,
            ),
            'GetModelCatalog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModelCatalog,
                    request_deserializer=comfy__request_dot_v1__pb2.ModelCatalogRequest.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.ModelCatalog.SerializeToString,
            ),
            'SyncLocalFiles': grpc.unary_stream_rpc_method_handler(
                    servicer.SyncLocalFiles,
                    request_deserializer=google_dot_empty__pb2.Empty.FromString,
                    response_serializer=comfy__request_dot_v1__pb2.LocalFiles.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'comfy_request.v1.Comfy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Comfy(object):
    """====== Service Definitions ======

    """

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comfy_request.v1.Comfy/Run',
            comfy__request_dot_v1__pb2.ComfyRequest.SerializeToString,
            comfy__request_dot_v1__pb2.JobSnapshot.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunSync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/comfy_request.v1.Comfy/RunSync',
            comfy__request_dot_v1__pb2.ComfyRequest.SerializeToString,
            comfy__request_dot_v1__pb2.JobOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comfy_request.v1.Comfy/GetJob',
            comfy__request_dot_v1__pb2.JobId.SerializeToString,
            comfy__request_dot_v1__pb2.JobSnapshot.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNodeDefinitions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comfy_request.v1.Comfy/GetNodeDefinitions',
            comfy__request_dot_v1__pb2.NodeDefRequest.SerializeToString,
            comfy__request_dot_v1__pb2.NodeDefs.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetModelCatalog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comfy_request.v1.Comfy/GetModelCatalog',
            comfy__request_dot_v1__pb2.ModelCatalogRequest.SerializeToString,
            comfy__request_dot_v1__pb2.ModelCatalog.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyncLocalFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/comfy_request.v1.Comfy/SyncLocalFiles',
            google_dot_empty__pb2.Empty.SerializeToString,
            comfy__request_dot_v1__pb2.LocalFiles.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
