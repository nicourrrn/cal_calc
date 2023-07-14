from cal_calc.repos import AbstractBaseRepo, repos_entry 
from cal_calc.models import *

repo: AbstractBaseRepo

entries = [f'{i}) {name}' for i, name in enumerate(repos_entry.keys())]
repo_name = list(repos_entry.keys())[int(input( 
    f"Change your repo: {' '.join(entries)}\n>>>"))]
repo = repos_entry[repo_name]()

data: AbstractBaseRepo.Data = repo.loads()
products = data.products
days = data.days

menu = """Menu:
1) Print all
"""

try:
    while True:
        break 
    print(days, products)
except KeyboardInterrupt:
    print("Bye!")
except:
    print("Panic!!!")

