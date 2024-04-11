from store.schemas.product import ProductOut
from store.usecases.product import product_usecase
from tests.conftest import product_id


async def test_usescases_create_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"



async def test_usescases_get_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"
    