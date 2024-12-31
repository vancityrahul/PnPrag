from setuptools import find_packages , setup
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(filename : str) -> List[str] :
	req = []
	with open(filename) as f:
		req = f.readlines()
		req = [ _.replace("\n","") for _ in req]
		if HYPHEN_E_DOT in req:
			req.remove(HYPHEN_E_DOT)
	return req

setup(
	name="PnPrag",
	version="0.0.1",
	author="anmol-rahul",
	author_email="None",
	packages=find_packages(),
	install_requires = get_requirements("requirements.txt")
)