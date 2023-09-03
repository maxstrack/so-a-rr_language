/*
 * Maximilian Strack
 * word creator for English to Zentil
 * 8/30/2023
 */

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
bool inArray(const std::string &value, const std::vector<std::string> &array) {
    return std::find(array.begin(), array.end(), value) != array.end();
}
int main() {
    std::cout << "Beginning World\n";
	//sorted via most reoccurring
	const char english[26] = {'e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z'};
	const std::string zentil[26] = {"a","z","eh","i","uh","rr","n","s","th","v","t","m","o","l","k","sh","f","veh","za","mi","zi","rreh","ke","irr","tho","so"};

	const std::vector<std::string> end2{"ed","er"};
	const std::vector<std::string> end3{"ion","ing"};
	const std::vector<std::vector<std::string>> endAll{end2,end3};

	const std::vector<std::string> search2{"ll","sh","th","oo","nn","tt","ee","rr", "tr"};
	const std::vector<std::string> search3{"ght"};
	const std::vector<std::vector<std::string>> searchAll{search2,search3};

	std::string engWord;
	std::string zenWord;
	std::ofstream myfile;

	myfile.open ("Dictionary.txt");
	while (1){
    	std::cout << "enter your word(-1 to exit)" << std::endl;
		std::cin >> engWord;
		if (engWord == "-1")
			break;
		myfile << engWord << "\t";

		// trim the ending depending on the endAll vector
		for (int i=2; i <= 3; ++i){
			if (engWord.length() > 4){
				std::string endWord= engWord.substr(engWord.length()-i,i);
		    	if (inArray(endWord, endAll[i-2]))
					engWord.resize(engWord.length()-i);
			}
		}

		// clears unwanted combinations
		for (int i=2; i <= 3; ++i){
			for (size_t j=0; j < searchAll[i-2].size(); ++j){
				size_t index = 0;
				while (index < engWord.length()){
        			index = engWord.find(searchAll[i-2][j], index);
        			if (index == std::string::npos)
            			break;
					engWord.erase(index+1,1);
        			index += i;
				}
			}
		}

		// convert
		for (size_t i=0; i < engWord.length(); ++i){
			for (int j=0; j < 26; ++j){
				if (engWord[i] == english[j])
    				zenWord += zentil[j] + "-";
			}
		}

		// print everything
    	std::cout << zenWord;
   		std::cout << "\n------------" << std::endl;
		myfile << zenWord; 
		myfile << "\n";
		zenWord.clear();
	}
	myfile.close();
    return 0;
}
