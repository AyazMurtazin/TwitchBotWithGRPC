# TwitchBotWithGRPC

<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Stream messages with Twitchio and gRPC</h3>

  <p align="center">
    Redirect chat stream from Twitchio Bot using gRPC Server
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The "Redirect Chat Stream from Twitchio Bot using gRPC Server" project aims to facilitate the redirection of chat messages from a Twitchio bot to a gRPC server for further processing or analysis. Twitchio is a Python library for building Twitch chat bots, and gRPC is a high-performance RPC (Remote Procedure Call) framework that allows communication between different services.

In this project, we leverage the capabilities of Twitchio to create a Twitch chat bot that listens to messages in a Twitch channel. Instead of processing these messages directly within the bot, we establish a gRPC server that receives the chat messages from the bot and forwards them to another service for analysis or storage. This architecture enables scalable and modular design, allowing the bot to focus on its primary responsibilities while offloading message processing to external services.

The main components of the project include:

* Twitchio Bot: We create a Twitchio bot using Python and configure it to join a specific Twitch channel. The bot listens to chat messages in real-time and captures them for further processing.
* gRPC Server: We implement a gRPC server using Python, which acts as an intermediary between the Twitchio bot and external services. The server receives chat messages from the bot and provides an interface for clients to consume the message stream.





### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [![gRPC](https://img.shields.io/badge/gRPC-1.63.0-brightgreen.svg)](https://grpc.io)
* [![Twitchio](https://img.shields.io/badge/Twitchio-2.9.1-purple.svg)](https://github.com/TwitchIO/TwitchIO)
* [![Redis](https://img.shields.io/badge/Redis-6.0.16-red.svg)](https://redis.io)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

To install Redis on Ubuntu, you can follow these steps:
* redis
  ```sh
  sudo apt install redis-server
  ```

You need to generate Python files from .proto
  ```sh
  make grpc
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

2. Clone the repo
3. Install Dependencies

    Ensure that you have Python and pip installed on your system. Then, install the required dependencies for your project, including Twitchio and gRPC:

    ```sh
    pip install -r requirements.txt
    ```

4. Set Up Twitch API Credentials

    Obtain your Twitch API credentials, including the TMI token and client ID. You may need to register an application on the Twitch Developer Portal to obtain these credentials.

5. Configure Environment Variables

    Create a .env file in your project directory and add your Twitch API credentials as environment variables:

    ```.env
    TMI_TOKEN=your_tmi_token
    CLIENT_ID=your_client_id
    BOT_NICK = your_bot_nick
    BOT_PREFIX = !
    ```
6. Start the gRPC Server
    
    Start the gRPC server that will handle chat message redirection:

    ```sh
    python3 Server.py
    ```
7. Start the example Client
    
    ```sh
    python3 Client.py
    ```
    Then input a channel name you would like to get messages from.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.





<!-- CONTACT -->
## Contact

Project Link: [https://github.com/AyazMurtazin/TwitchBotWithGRPC](https://github.com/AyazMurtazin/TwitchBotWithGRPC)