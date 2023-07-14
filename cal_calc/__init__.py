from cal_calc.models import Day, Product

days: list[Day] = []
products: list[Product] = []
def get_last_product_id() -> int: return len(products)
