package pages;

import com.microsoft.playwright.Page;

public class TextBoxPage {
    private Page page;

    public TextBoxPage(Page page) {
        this.page = page;
    }

    public void enterFullName(String fullName) {
        page.locator("#userName").fill(fullName);
    }

    public void enterEmail(String email) {
        page.locator("#userEmail").fill(email);
    }

    public void enterCurrentAddress(String currentAddress) {
        page.locator("#currentAddress").fill(currentAddress);
    }

    public void enterPermanentAddress(String permanentAddress) {
        page.locator("#permanentAddress").fill(permanentAddress);
    }

    public void clickSubmit() {
        page.locator("#submit").click();
    }

    public boolean isOutputSectionDisplayed() {
        return page.locator("#output").isVisible();
    }
}