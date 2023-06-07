echo " BUILD START"
python3.11 -m pip install -r requirement
python3.11 mange.py collectstatic --noiniput -clear
echo " BUILD END"
