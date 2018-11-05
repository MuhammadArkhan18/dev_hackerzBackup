clear
sleep 1
echo "-------------------------------------------------------"
echo "|        H A C K E R Z   I P   B A C K U P            |"
echo "-------------------------------------------------------"
sleep 1
echo "-------------------------------------------------------"
echo "|       {*} = Root       |      {-} = No Root         |"
echo "-------------------------------------------------------"
sleep 2
echo ""
echo ""
sleep 1
echo "\033[0;31m""Author : ""\033[1;34m""VrozAnims2003"
sleep 1
echo "\033[0;31m""Team : ""\033[1;33m""United guilds of Cyber Arts"
sleep 1
echo "\033[0;31m""Version : ""\033[1;37m""1.0"
sleep 2
echo ""
echo ""
sleep 1
echo "\033[1;32m""Main Menu:"
echo "\033[0;32m""[01] Update Hackerz's Data {*}"
echo "\033[0;32m""[02] Backup Hackerz's ip(s) {-}"
echo "\033[0;32m""[03] Export ip to text mode (Backup First!) {-}"
echo "\033[1;31m""[00] Exit"
sleep 1
echo ""
echo "\033[1;37m""Select Number: "
read choice

if [ $choice = 1 ]
then
clear
sh configure.sh
sh main.sh
fi

if [ $choice = 2 ]
then
clear
sleep 2
echo "\033[1;35m""---------------------"
echo "\033[1;35m""| B A C K U P   I P |"
echo "\033[1;35m""---------------------"
sleep 2
echo ""
sleep 1
python data/1.py
read paus
sh main.sh
fi

if [ $choice = 3 ]
then
clear
sleep 2
echo "\033[1;35m""---------------------"
echo "\033[1;35m""| E X P O R T   I P |"
echo "\033[1;35m""---------------------"
sleep 2
echo "\033[1;37m"
sleep 1
python data/2.py
read paus
sh main.sh
fi

if [ $choice = 0 ]
then
echo ""
echo ""
sleep 1
echo "~Please wait"
sleep 2
echo "[*]Closing Program.."
sleep 2
clear
fi
