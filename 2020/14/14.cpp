#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <regex>
#include <bitset>

void getData(std::vector<std::string>& outData, std::string fileName){
    std::fstream newfile;
    newfile.open(fileName, std::ios::in);       //open a file to perform read operation using file object
    if (newfile.is_open()){                     //checking whether the file is open
        std::string tp;
        while(std::getline(newfile, tp)){       //read data from file object and put it into string.
            outData.push_back(tp);              //print the data of the string
        }
        newfile.close();                        //close the file object.
    }
}

std::string applyMask(const std::string& data, const std::string& mask){
    int iData = std::stoi(data);
    std::string sDataBin = std::bitset< 36 >(iData).to_string();

    for(int i = 0; i < mask.size(); i++){
        if(mask[i] != 'X'){ sDataBin[i] = mask[i]; }
    }

    return sDataBin;
}

int main(){
    typedef std::vector<std::string>        vStr;

    vStr                                    myData;
    std::string                             fileName = "input.txt";
    std::map<std::string, std::string>      mem;
    std::string                             mask = "000000000000000000000000000000000000";
    std::string                             index;
    std::regex                              regex("\\d+");
    std::smatch                             m;

    getData(myData, fileName);

    for(auto line: myData){
        if(line.substr(0, 4) == "mask"){
            mask = line.substr(7, line.size()-1);
        }
        else{
            std::string::const_iterator searchStart(line.cbegin());
            int i = 0;
            while (std::regex_search(searchStart, line.cend(), m, regex)) {
                if(!i%2){ index = m.str(0);}
                else{
                    mem[index] = applyMask(m.str(0), mask);
                }
                searchStart = m.suffix().first;
                i++;
            }
        }
    }

    long long int sum = 0;
    for (auto const& [key, val] : mem){
        sum += std::stoll(val, nullptr, 2);
    }
    std::cout << "Sum of memory: " << sum << std::endl;

    return 0;
}