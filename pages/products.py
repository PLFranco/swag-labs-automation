from playwright.sync_api import expect, Page

class SwagLabsProductListings:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.inventory_list = page.locator('.inventory_list')
        self.inventory_items = page.locator('.inventory_item')
        self.dropdown_option = page.get_by_role("combobox")
        self.selected_option = None
    
    def load_state(self) -> None:
        self.page.wait_for_load_state("networkidle")
        
    def verify_inventory_list(self) -> None:
        expect(self.inventory_list).to_be_visible(timeout=5000)
        expect(self.inventory_list.locator(self.inventory_items)).to_have_count(6)
        
             
    def verify_all_product_details(self) -> None:
        for item in self.inventory_items.all():
            expect(item.locator('.inventory_item_name')).to_be_visible()
            expect(item.locator('.inventory_item_price')).to_be_visible()
            expect(item.locator('img.inventory_item_img')).to_be_visible()
            expect(item.locator('.btn_inventory')).to_be_visible()
            expect(item.locator('.inventory_item_desc')).to_be_visible()

    def verify_product_count(self) -> None:
        expected_count = 6
        expect(self.inventory_items).to_have_count(expected_count)

    def get_option(self, option: str) -> None:
        self.dropdown_option.select_option(option)
        self.selected_option = option
    
    def get_product_names(self) -> list:
        return self.page.locator('.inventory_item_name').all_text_contents()

  
