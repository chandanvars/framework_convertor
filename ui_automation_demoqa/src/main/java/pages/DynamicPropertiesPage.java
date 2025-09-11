package pages;

import com.microsoft.playwright.Page;

public class DynamicPropertiesPage {
    private Page page;

    public DynamicPropertiesPage(Page page) {
        this.page = page;
    }

    public boolean isEnableAfterButtonClickable() {
        return page.locator("#enableAfter").isEnabled();
    }

    public String getColorChangeButtonColor() {
        return page.locator("#colorChange").evaluate("element => getComputedStyle(element).color").toString();
    }
}