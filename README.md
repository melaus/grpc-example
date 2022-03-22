
# Introduction
This is a repo created for an internal presentation to demonstrate some high level concepts of gRPC in Python.

This repo contains:
- An [account protobuf](./protos/account.proto)
- A Python gRPC server implementation of `account.proto`
- A Python gRPC stub (client) implementation of `account.proto`

We implement two RPC methods to demonstrate:
- `GetAccount` - a unary connection (like a REST GET request/response)
- `StreamIndustryIds`  - a client-side streaming connection (streams responses as an iterator from server)

There are three branches:
- `main` 
  - original implementation
- `01-update-server-with-new-fields` 
  - add a new field to `GetAccountResponse` and update server to return the new field
  - client should continue to work
- `02-update-client-to-use-new-contract` 
  - update client to implement new contract

# Presentation Slides
- [Google Slides (Internal access only)](https://docs.google.com/presentation/d/1a8gHWwjPL0DS4docXKngc9zdWtMsI2dIf1dYiWbOn88/edit?usp=sharing)
- [Markdown version](./gRPC-python.md)

# Develop

## Step 1: Create a virutalenv and install dependencies

Use your favourite tool to create virtual environment and install dependencies in `requirements.txt`.

## Step 2: Generate python types and classes based on account.proto

In `./account_server/account_server` and `./account_client/account_client`, use the following command to generate three files:
- `account_pb2.py`
  - contains the generated message types and enums defined in the protobuf file 
- `account_pb2_grpc.py`
  - contains the generated service servicer (server) and stub (stub) abstract classes to be implemented
- `account_pb2.pyi`
  - contains mypy types using the plugin [`mypy_protobuf`](https://github.com/nipunn1313/mypy-protobuf)

```bash
python -m grpc_tools.protoc \
  -I ../../protos \
  --plugin=protoc-en-mypy=/Users/alanlau/.pyenv/shims/protoc-gen-mypy \
  --mypy_out=. \
  --python_out=. \
  --grpc_python_out=. \
  ../../protos/account.proto
```

Rerun this step if you've made changes to the protobuf `account.proto`.

## Step 3: Implement server and client code

The server code lives under `./account_server`, and the stub (client) lives under `./account_client`. 

They can be updated independently of each other in the case of new field or features added in contract.


## Step 4: Start server and client

```bash
python account_[server|client].py
```
