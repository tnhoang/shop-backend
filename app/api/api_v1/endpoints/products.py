from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_products():
    return [
        {"title": "Monstera DK Var", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Deliociosa", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Borsigniana", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Variegata", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Adansonii", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Pinnatipartita", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Dubia", "rating": 3, "ratingCount": 210, "price": 40},
        {"title": "Monstera Siltepecana", "rating": 3, "ratingCount": 210, "price": 40},
    ]
