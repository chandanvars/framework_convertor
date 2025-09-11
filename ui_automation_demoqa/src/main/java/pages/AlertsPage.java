package pages;

import com.microsoft.playwright.Page;

public class AlertsPage {
    private Page page;
    private String alertText;

    public AlertsPage(Page page) {
        this.page = page;
    }

    public void clickAlertButton() {
        // Setup alert handler to capture alert text
        page.onDialog(dialog -> {
            alertText = dialog.message();
            dialog.accept();
        });
        page.locator("#alertButton").click();
    }

    public String getAlertText() {
        return alertText;
    }

    public void acceptAlert() {
        // Alert is already accepted in the dialog handler
        // This method is kept for compatibility with the test
    }

    public void dismissAlert() {
        page.onDialog(dialog -> dialog.dismiss());
    }
}