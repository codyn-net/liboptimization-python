# All the messages
PROTO_MESSAGES = task command discovery monitor

# The temporary directory to fetch the proto files in
FETCH_DIR = .fetch-proto

PROTO_DIR = $(FETCH_DIR)/optimization/messages

# The fetched .proto files for each message
PROTO_FILES = $(foreach i,$(PROTO_MESSAGES),$(PROTO_DIR)/$(i).proto)

# The go version of the proto files in messages/
PROTO_PY_FILES = $(foreach i,$(PROTO_MESSAGES),liboptimization/messages/$(i)_pb2.py)

# The url where to fetch the proto files from
FETCH_REPOSITORY = https://ponyo.epfl.ch/gitlab/optimization/liboptimization.git

REPOSITORY_DIR = $(FETCH_DIR)/liboptimization

PROTO_SOURCE_DIR = $(REPOSITORY_DIR)/optimization/messages

PROTO_SOURCE_FILES = $(foreach i,$(PROTO_MESSAGES),$(PROTO_SOURCE_DIR)/$(i).proto)

all:
	@echo "Use the update-proto target to update the go protobuf files."

.proto-files.stamp:
	@mkdir -p $(dir $(PROTO_FILES)) || exit 1;				\
	if [ ! -d $(FETCH_DIR)/liboptimization ]; then 				\
		mkdir -p $(FETCH_DIR) || exit 1; 				\
		git clone $(FETCH_REPOSITORY) $(REPOSITORY_DIR); 		\
	else 									\
		(cd $(REPOSITORY_DIR) && git fetch && git reset --hard origin/master); \
	fi; 									\
	cp $(PROTO_SOURCE_FILES) $(PROTO_DIR)/; 				\
	touch .proto-files.stamp

update-proto: $(PROTO_PY_FILES)

clean-proto:
	@rm -rf messages/* $(FETCH_DIR)

$(PROTO_FILES): .proto-files.stamp

$(PROTO_PY_FILES): $(PROTO_FILES)
	@echo "[GEN] $(notdir $@)"; \
	pname=$(basename $(basename $(notdir $@)));				\
	protoc --python_out=$(FETCH_DIR) -I$(FETCH_DIR) $(PROTO_DIR)/$${pname%_pb2}.proto; \
	cp $(PROTO_DIR)/$${pname}.py optimization/messages/;

.PHONY : clean-proto update-proto all
