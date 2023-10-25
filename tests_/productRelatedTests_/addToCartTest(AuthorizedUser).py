from tests_.baseTestWithLogin import BaseTestWithLogin
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.productRelatedPages_.searchResultPage import SearchResultPage
from pages_.productRelatedPages_.productDetailsPage import ProductDetailsPage
from testData_.data import searchTextData


class AddToCartTest(BaseTestWithLogin):
    def test_add_product_to_cart(self):
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.fill_search_field_and_apply(searchTextData["validText"])
        # self.navigationBarObj.click_search_button()

        self.searchResultPageObj = SearchResultPage(self.driver)
        self.searchResultPageObj.open_first_product()

        self.initialCartProductsQuantity = self.navigationBarObj.get_cart_products_quantity()
        self.productDetailsPageObj = ProductDetailsPage(self.driver)
        self.productDetailsPageObj.click_add_to_cart_button()
        self.updatedCartProductsQuantity = self.navigationBarObj.get_cart_products_quantity()

        self.productDetailsPageObj.validate_add_to_cart_confirmation_message()
        self.productDetailsPageObj.check_add_to_cart_confirmation_checkbox_icon_existence()
        self.assertGreater(self.updatedCartProductsQuantity, self.initialCartProductsQuantity, f"Quantity has not increased. Initial:{self.initialCartProductsQuantity}, Updated:{self.updatedCartProductsQuantity}")
