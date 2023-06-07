echo " BUILD START"
python3.9 -m pip install -r requirement
python3.9 mange.py collectstatic --noiniput -clear
echo " BUILD END"
