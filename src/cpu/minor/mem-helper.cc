#include "base/logging.hh"
#include "cpu/minor/mem-helper.hh"
#include <string>
#include <sstream>
#include <stdexcept>
#include <iostream>

static bool _once = false;
int32_t MemHelper::retrieveEffectiveAddr(const std::string &disassembledInst) {
    int32_t offset = 0;

    _once = true;

    try {
        // Find the offset in the disassembled string
        size_t offsetStart = disassembledInst.find('#');
        if (offsetStart != std::string::npos) {
            size_t offsetEnd = disassembledInst.find_first_of(" ,]", offsetStart);
            if (offsetEnd != std::string::npos) {
                // Extract and parse the offset
                std::string offsetStr = disassembledInst.substr(offsetStart + 1, offsetEnd - offsetStart - 1);
                offset = std::stoi(offsetStr);
            } 
            else {
                fatal("Failed to parse offset: No valid delimiter found.");
            }
        } 
        /*else {
            warn("Failed to parse offset: '#' not found in disassembly.");
            warn("Disassembled instruction: %s", disassembledInst);
        }*/
    } 
    catch (const std::exception &e) {
        fatal("Failed to parse the offset: %s", e.what());
    }

    return offset;
}

