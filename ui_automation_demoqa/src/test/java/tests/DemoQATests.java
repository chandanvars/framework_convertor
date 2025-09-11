package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.*;
import utils.DataProviderUtil;

public class DemoQATests extends BaseTest {

    @Test(dataProvider = "textBoxDataProvider", dataProviderClass = DataProviderUtil.class)
    public void testTextBox(String fullName, String email, String currentAddress, String permanentAddress) {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        TextBoxPage textBoxPage = new TextBoxPage(page);
        textBoxPage.enterFullName(fullName);
        textBoxPage.enterEmail(email);
        textBoxPage.enterCurrentAddress(currentAddress);
        textBoxPage.enterPermanentAddress(permanentAddress);
        textBoxPage.clickSubmit();

        Assert.assertTrue(textBoxPage.isOutputSectionDisplayed(), "Output section is not displayed");
    }

    @Test
    public void testButtonClick() {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        ButtonsPage buttonsPage = new ButtonsPage(page);
        buttonsPage.doubleClickButton();

        Assert.assertEquals(buttonsPage.getDoubleClickMessage(), "You have done a double click", "Double click message is incorrect");
    }

    @Test
    public void testCheckBox() {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        CheckBoxPage checkBoxPage = new CheckBoxPage(page);
        checkBoxPage.expandAll();
        checkBoxPage.selectHomeCheckBox();

        Assert.assertTrue(checkBoxPage.isResultDisplayed(), "Result section is not displayed");
    }

    @Test
    public void testRadioButton() {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        RadioButtonPage radioButtonPage = new RadioButtonPage(page);
        radioButtonPage.selectYesRadioButton();

        Assert.assertEquals(radioButtonPage.getSuccessMessage(), "Yes", "Radio button selection message is incorrect");
    }

    @Test
    public void testAlert() {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        AlertsPage alertsPage = new AlertsPage(page);
        alertsPage.clickAlertButton();

        String alertText = alertsPage.getAlertText();
        alertsPage.acceptAlert();

        Assert.assertEquals(alertText, "This is a test alert", "Alert text is incorrect");
    }

    @Test
    public void testWebTable() {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        WebTablePage webTablePage = new WebTablePage(page);
        webTablePage.clickAddButton();
        webTablePage.enterFirstName("John");
        webTablePage.enterLastName("Doe");
        webTablePage.enterEmail("john.doe@example.com");
        webTablePage.enterAge("30");
        webTablePage.enterSalary("1000");
        webTablePage.enterDepartment("IT");
        webTablePage.clickSubmitButton();

        Assert.assertTrue(webTablePage.isTableRowDisplayed(), "New table row is not displayed");
    }

    @Test
    public void testDynamicProperties() throws InterruptedException {
        HomePage homePage = new HomePage(page);
        homePage.clickOnElementsCard();

        DynamicPropertiesPage dynamicPropertiesPage = new DynamicPropertiesPage(page);
        Thread.sleep(5000); // Wait for 5 seconds for the button to become clickable

        Assert.assertTrue(dynamicPropertiesPage.isEnableAfterButtonClickable(), "Button is not clickable after 5 seconds");
    }
}