# Define variables
PROTO_DIR := protos
PROTO_FILES := $(wildcard $(PROTO_DIR)/*.proto)
GRPC_PYTHON_OUT := .
PROTOBUF_PYTHON_OUT := .

# Define targets
.PHONY: all grpc

# Target to generate gRPC Python files
grpc:
	@echo "Generating gRPC Python files from .proto files..."
	@mkdir -p $(GRPC_PYTHON_OUT)
	@python3 -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(GRPC_PYTHON_OUT) --grpc_python_out=$(GRPC_PYTHON_OUT) $(PROTO_FILES)

# Target to build everything
all: grpc