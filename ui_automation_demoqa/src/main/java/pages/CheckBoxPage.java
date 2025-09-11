package pages;

import com.microsoft.playwright.Page;

public class CheckBoxPage {
    private Page page;

    public CheckBoxPage(Page page) {
        this.page = page;
    }

    public void expandAll() {
        page.locator(".rct-collapse.rct-collapse-btn").click();
    }

    public void selectHomeCheckBox() {
        page.locator(".rct-icon.rct-icon-uncheck").click();
    }

    public boolean isResultDisplayed() {
        return page.locator("#result").isVisible();
    }
}