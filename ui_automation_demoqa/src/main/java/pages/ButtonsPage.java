package pages;

import com.microsoft.playwright.Page;

public class ButtonsPage {
    private Page page;

    public ButtonsPage(Page page) {
        this.page = page;
    }

    public void doubleClickButton() {
        page.locator("#doubleClickBtn").dblclick();
    }

    public String getDoubleClickMessage() {
        return page.locator("#doubleClickMessage").textContent();
    }
}