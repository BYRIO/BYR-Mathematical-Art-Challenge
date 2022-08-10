ifeq ($(OS),Windows_NT)
	CXX = clang++
	TARGET = render.exe
	RM = del
else
	CXX = g++
	TARGET = render
	RM = rm
endif

render: 
	$(CXX) -O2 -std=c++14 -o $(TARGET) main.cpp

.PHONY: clean

clean:
	$(RM) $(TARGET)