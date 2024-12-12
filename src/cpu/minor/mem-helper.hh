#ifndef MEM_HELPER_HH
#define MEM_HELPER_HH

#include "base/types.hh" // For Addr
#include <string>

class MemHelper {
  public:
    // Static method to retrieve the effective address
    static int32_t retrieveEffectiveAddr(const std::string &disassembledInst);
};

#endif // MEM_HELPER_HH

