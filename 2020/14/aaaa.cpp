#include <iostream>
#include <regex>

int main() {
    std::string s = "mem[53867] = 1949039";
    std::cout << s <<"\n";
    std::regex regex("\\d+");
    std::smatch m;
    regex_search(s, m, regex);
    std::cout << "match: " << m.str() << std::endl;
    return 0;
}