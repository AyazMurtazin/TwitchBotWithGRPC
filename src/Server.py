import grpc
import asyncio
import chat_listener_pb2
import chat_listener_pb2_grpc
import redis
import subprocess

# Initialize Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)
process = None
# gRPC service definition

            
class ChatServicer(chat_listener_pb2_grpc.TwitchChatServicer):

    async def StreamMessages(self, request, context):
        process = subprocess.Popen(['python3', 'TwitchBot.py', request.channel_name])
        try:
            async for message in self._get_messages_from_redis(request.channel_name):
                print(f"Received message: {message.message}")
                yield message
        except:
            process.terminate()
            print("Client disconnected")

    async def _get_messages_from_redis(self, channel_name):
        while True:
            message = redis_client.blpop(channel_name, timeout=30)
            if message:
                yield chat_listener_pb2.MessageResponse(message=message[1].decode())
        

# gRPC server setup
async def serve():
    server = grpc.aio.server()
    chat_listener_pb2_grpc.add_TwitchChatServicer_to_server(
        ChatServicer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    await server.start()
    print(f'Server listening on {listen_addr}')
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())
