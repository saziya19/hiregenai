echo " BUILD START"
python3.11.3 -m pip install -r requirement
python3.11.3 mange.py collectstatic --noiniput -clear
echo " BUILD END"