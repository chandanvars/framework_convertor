package pages;

import com.microsoft.playwright.Page;

public class WebTablePage {
    private Page page;

    public WebTablePage(Page page) {
        this.page = page;
    }

    public void clickAddButton() {
        page.locator("#addNewRecordButton").click();
    }

    public void enterFirstName(String firstName) {
        page.locator("#firstName").fill(firstName);
    }

    public void enterLastName(String lastName) {
        page.locator("#lastName").fill(lastName);
    }

    public void enterEmail(String email) {
        page.locator("#userEmail").fill(email);
    }

    public void enterAge(String age) {
        page.locator("#age").fill(age);
    }

    public void enterSalary(String salary) {
        page.locator("#salary").fill(salary);
    }

    public void enterDepartment(String department) {
        page.locator("#department").fill(department);
    }

    public void clickSubmitButton() {
        page.locator("#submit").click();
    }

    public boolean isTableRowDisplayed() {
        return page.locator(".rt-tr-group").isVisible();
    }
}