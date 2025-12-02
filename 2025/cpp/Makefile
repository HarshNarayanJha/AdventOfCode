CXX = clang++
BUILD_DIR = bin
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic -O2

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

%: %.cpp $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $< -o $(BUILD_DIR)/$@
	$(BUILD_DIR)/$@

.PHONY: clean $(BUILD_DIR)

clean:
	rm -r -I $(BUILD_DIR)
