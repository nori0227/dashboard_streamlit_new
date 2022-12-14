# dashboard_streamlit

## HHA 507 Assignment 10

### Analysis of FIFA Worldcup 2022 Players Stats and Playing time

##### pip3 install streamlit

##### Create a VM in AZURE, copy the IP address and open in terminal (AZURE preffered - Public IP 52.255.181.59):
1. sudo apt-get update
2. sudo apt install python3-pip
3. git clone ###
4. touch player_playingtime.py
5. nano player_playingtime.py
6. streamlit run player_playingtime.py
7. obtained two datasets, added a title, headers, captions and performed a barchart to get the number of players receiving yellow cards and linechart analysis to get the number of players drawing goals
8. Add inbound port rule in Neworking : 8501

## important command to run for streamlit to work
pyenv install 3.10.0  
On remote machine, installation after doing  Install streamlit -> pip3 install streamlit 
Go to .bashrc file -> `nano ~/.bashrc` 
in the nano text editor, type "export PATH="$HOME/.local/bin:$PATH" to the very last line - save / exit 
source ~/.bashrc
pip3 install jinja2 --upgrade

# Important website
https://docs.streamlit.io/library/get-started/create-an-app 
