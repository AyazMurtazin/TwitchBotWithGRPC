import grpc
import asyncio
import chat_listener_pb2
import chat_listener_pb2_grpc


async def stream_messages():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = chat_listener_pb2_grpc.TwitchChatStub(channel)
        request = chat_listener_pb2.ChannelRequest(channel_name=input("Input channel name:"))

        try:
            async for message in stub.StreamMessages(request):
                print(message.message)
        except grpc.aio.AioRpcError as e:
            print(f"Error streaming messages: {e}")


async def main():
    await stream_messages()

if __name__ == '__main__':
    asyncio.run(main())