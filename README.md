
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
- `trial-betterproto`
  - use `poetry`
  - use `betterproto` rather than default `protoc`+plugins

# Presentation Slides
- [Google Slides (Internal access only)](https://docs.google.com/presentation/d/1a8gHWwjPL0DS4docXKngc9zdWtMsI2dIf1dYiWbOn88/edit?usp=sharing)
- [Markdown version](./gRPC-python.md)

# Develop

## Step 1: Create a virutalenv and install dependencies

`poetry install`

## Step 2: Generate python types and classes based on account.proto

In `./account_server/account_server` and `./account_client/account_client`, use the following command to generate `account/__init__.py`:

```bash
poetry run python -m grpc_tools.protoc \
  -I ../../protos \
  --python_betterproto_out=. \
  ../../protos/account.proto
```

Rerun this step if you've made changes to the protobuf `account.proto`.

## Step 3: Implement server and client code

The server code lives under `./account_server`, and the stub (client) lives under `./account_client`. 

They can be updated independently of each other in the case of new field or features added in contract.


## Step 4: Start server and client

```bash
poetry run python account_[server|client].py
```
