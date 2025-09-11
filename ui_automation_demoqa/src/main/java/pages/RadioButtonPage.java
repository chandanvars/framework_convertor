package pages;

import com.microsoft.playwright.Page;

public class RadioButtonPage {
    private Page page;

    public RadioButtonPage(Page page) {
        this.page = page;
    }

    public void selectYesRadioButton() {
        page.locator("//label[@for='yesRadio']").click();
    }

    public String getSuccessMessage() {
        return page.locator(".text-success").textContent();
    }
}