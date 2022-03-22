# gRPC

![](https://grpc.io/img/landing-2.svg)

- Binary Payloads
- Polyglot services
- Protocol Buffer (Protobuf) contracts

# Protobuf
- Interface Definition Language
  - Language and platform neutral
- Acts as contract between gRPC server (server) and stub (client)
- Code generation
- Automatic serialisation and deserialisation of binary payloads

# gRPC vs REST

| gRPC                                                                                                                           | REST                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| HTTP/2<br><ul><li>Unary</li><li>Server or client streaming</li><li>Bidirectional communication</li></ul>                       | HTTP/1<br><ul><li>Unary request/response</li></ul>                                                                            |
| No out-of-the-box browser support                                                                                              | Well supported by browsers                                                                                                    |
| “API Contract” using Protobuf<br><ul><li>Binary and highly compressed<br>Automatically converted into protobuf types</li></ul> | Commonly JSON<br><ul><li>Human-readable text</li><li>Requires manual serialisation and deserialisation into objects</li></ul> |
| Native code generation                                                                                                         | Requires third party tools e.g. OpenAPI                                                                                       |

# Code generation
- The [protoc](https://github.com/protocolbuffers/protobuf) (protobuf) cli tool
- In Python, use pip package `grcpio-tools` to
  - Generate both protobuf types and grpc stub definitions
  - Generate mypy type hints
    - With plugin [mypy-protobuf](https://github.com/nipunn1313/mypy-protobuf)
    - Google’s [in-house type hint generator](https://github.com/protocolbuffers/protobuf/issues/2638#issuecomment-1035238525) (to be released March/April 2022)

# Demo

# Final Thoughts
✅
- Plays well in a polyglot environment
- Generated code using Protobuf contracts
- Append-style contract means migrations won’t break things
- Efficient protobuf serialisation from binary payload

❌
- Takes some getting used to
- Looks weird in non-CamelCase languages like Python
- Used at major establishments, but open source tools sometimes lack maturity

# Useful Links
- [Performance best practices with gRPC](https://docs.microsoft.com/en-us/aspnet/core/grpc/performance?view=aspnetcore-6.0#:~:text=A%20gRPC%20channel%20uses%20a,complete%20before%20they%20are%20sent.)
- [How to implement a gRPC client and server in TypeScript](https://medium.com/blokur/how-to-implement-a-grpc-client-and-server-in-typescript-fa3ac807855e)
- [Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3)
- [Python gRPC examples](https://github.com/grpc/grpc/tree/master/examples/python)
