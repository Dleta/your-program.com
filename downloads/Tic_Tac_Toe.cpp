//
//  Created by Delta on 28.02.22.
//

#include <iostream>

#define RESET   "\033[0m"
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */


using namespace std;



string fields[9] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
bool winner = false;
string turn = "X";

void clear(){
    system("clear");
}

void getGridInfo(int x){

    string fieldData =  fields[x];

    if (fieldData == "X"){
        cout << BOLDRED << "X" << RESET;
    }else if (fieldData == "O"){
        cout << BOLDBLUE << "O" << RESET;
    }else{
        cout << BOLDGREEN << fieldData << RESET;
    }
    
}

void printGrid(){
    cout << "\n";
    cout << "  ";
    getGridInfo(0);
    cout << "  |  ";
    getGridInfo(1);
    cout << "  |  ";
    getGridInfo(2);
    cout << "\n";
    cout << "-----------------\n";
    cout << "  ";
    getGridInfo(3);
    cout << "  |  ";
    getGridInfo(4);
    cout << "  |  ";
    getGridInfo(5);
    cout << "\n";
    cout << "-----------------\n";
    cout << "  ";
    getGridInfo(6);
    cout << "  |  ";
    getGridInfo(7);
    cout << "  |  ";
    getGridInfo(8);
    cout << "\n";
    cout << "\n";
}

void playerAction(){
    int chosenfield;
    cout << "Player " << turn << " choose a field: ";
    cin >> chosenfield;
    chosenfield = chosenfield -1;

    if (fields[chosenfield] == "X"){
        cout << "\n This field is taken by a player please choose another one\n";
        playerAction();
    }else if (fields[chosenfield] == "O")
    {
        cout << "\nThis field is taken by a player please choose another one\n";
        playerAction();
    }else if (chosenfield == 1  || 2 || 3 || 4 || 5 || 6 || 7 || 8 || 9){
        fields[chosenfield] = turn;

    }else{
        cout << "pleas enter a number of the grid\n";
        playerAction();
    }
}

void checkForWinner(){
    if (fields[0] == "X"  &&  fields[1] == "X" && fields[2] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[0] == "O"  &&  fields[1] == "O" && fields[2] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[3] == "X"  &&  fields[4] == "X" && fields[5] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[3] == "O"  &&  fields[4] == "O" && fields[5] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[6] == "X"  &&  fields[7] == "X" && fields[8] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[6] == "O"  &&  fields[7] == "O" && fields[8] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[0] == "X"  &&  fields[3] == "X" && fields[6] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[0] == "O"  &&  fields[3] == "O" && fields[6] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[1] == "X"  &&  fields[4] == "X" && fields[7] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[1] == "O"  &&  fields[4] == "O" && fields[7] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[2] == "X"  &&  fields[5] == "X" && fields[8] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[2] == "O"  &&  fields[5] == "O" && fields[8] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[0] == "X"  &&  fields[4] == "X" && fields[8] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[0] == "O"  &&  fields[4] == "O" && fields[8] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[2] == "X"  &&  fields[4] == "X" && fields[6] == "X"){
        system("clear");
        printGrid();
        winner = true;
    }else if (fields[2] == "O"  &&  fields[4] == "O" && fields[6] == "O"){
        system("clear");
        printGrid();
        winner = true;
    }
}

void announceWinner(){
    if (turn == "X")
    {
        cout << BOLDRED << "**********************************\n";
        cout << "******* " << BOLDWHITE <<turn << " is the winner.  " << BOLDRED << "********\n";
        cout << "**********************************\n";
        cout << RESET << "\n";
    }else if (turn == "O")
    {
        cout << BOLDBLUE << "**********************************";
        cout << "*******" << BOLDWHITE <<turn << "  is the winner.  " << BOLDBLUE << "********";
        cout << "**********************************\n";
        cout << RESET << "\n";
    }
    
    
}


int main(int argc, const char * argv[]) {

    while (winner == false)
    {
        if (winner == false){
            turn = "X";
            printGrid();
            playerAction();
            checkForWinner();
        }else if (winner == true){
            announceWinner();
        }else{
            return 0;
        }
        
        if (winner == false){
            turn = "O";
            printGrid();
            playerAction();
            checkForWinner();
        }else if (winner == true){
            announceWinner();
        }else{
            return 0;
        }

    }
    return 0;
}
