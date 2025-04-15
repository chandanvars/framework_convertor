package pages;

import com.microsoft.playwright.Page;
import playwright.PlaywrightManager;

public class HomePage {
    private Page page;

    public HomePage() {
        this.page = PlaywrightManager.getPage();
    }

    public void clickOnElementsCard() {
        page.locator("//h5[text()='Elements']").click();
    }
}