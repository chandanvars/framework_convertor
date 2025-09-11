package pages;

import com.microsoft.playwright.Page;

public class HomePage {
    private Page page;

    public HomePage(Page page) {
        this.page = page;
    }

    public void clickOnElementsCard() {
        page.locator("//h5[text()='Elements']").click();
    }
}