package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import pages.*;
import playwright.PlaywrightManager;
import utils.DataProviderUtil;

public class DemoQATests {

    @Test(dataProvider = "textBoxDataProvider", dataProviderClass = DataProviderUtil.class)
    public void testTextBox(String fullName, String email, String currentAddress, String permanentAddress) {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        TextBoxPage textBoxPage = new TextBoxPage();
        textBoxPage.enterFullName(fullName);
        textBoxPage.enterEmail(email);
        textBoxPage.enterCurrentAddress(currentAddress);
        textBoxPage.enterPermanentAddress(permanentAddress);
        textBoxPage.clickSubmit();

        Assert.assertTrue(textBoxPage.isOutputSectionDisplayed(), "Output section is not displayed");
        PlaywrightManager.close();
    }

    @Test
    public void testButtonClick() {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        ButtonsPage buttonsPage = new ButtonsPage();
        buttonsPage.doubleClickButton();

        Assert.assertEquals(buttonsPage.getDoubleClickMessage(), "You have done a double click", "Double click message is incorrect");
        PlaywrightManager.close();
    }

    @Test
    public void testCheckBox() {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        CheckBoxPage checkBoxPage = new CheckBoxPage();
        checkBoxPage.expandAll();
        checkBoxPage.selectHomeCheckBox();

        Assert.assertTrue(checkBoxPage.isResultDisplayed(), "Result section is not displayed");
        PlaywrightManager.close();
    }

    @Test
    public void testRadioButton() {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        RadioButtonPage radioButtonPage = new RadioButtonPage();
        radioButtonPage.selectYesRadioButton();

        Assert.assertEquals(radioButtonPage.getSuccessMessage(), "Yes", "Radio button selection message is incorrect");
        PlaywrightManager.close();
    }

    @Test
    public void testAlert() {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        AlertsPage alertsPage = new AlertsPage();
        alertsPage.clickAlertButton();

        String alertText = alertsPage.getAlertText();
        alertsPage.acceptAlert();

        Assert.assertEquals(alertText, "This is a test alert", "Alert text is incorrect");
        PlaywrightManager.close();
    }

    @Test
    public void testWebTable() {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        WebTablePage webTablePage = new WebTablePage();
        webTablePage.clickAddButton();
        webTablePage.enterFirstName("John");
        webTablePage.enterLastName("Doe");
        webTablePage.enterEmail("john.doe@example.com");
        webTablePage.enterAge("30");
        webTablePage.enterSalary("1000");
        webTablePage.enterDepartment("IT");
        webTablePage.clickSubmitButton();

        Assert.assertTrue(webTablePage.isTableRowDisplayed(), "New table row is not displayed");
        PlaywrightManager.close();
    }

    @Test
    public void testDynamicProperties() throws InterruptedException {
        PlaywrightManager.initialize();
        HomePage homePage = new HomePage();
        homePage.clickOnElementsCard();

        DynamicPropertiesPage dynamicPropertiesPage = new DynamicPropertiesPage();
        Thread.sleep(5000); // Wait for 5 seconds for the button to become clickable

        Assert.assertTrue(dynamicPropertiesPage.isEnableAfterButtonClickable(), "Button is not clickable after 5 seconds");
        PlaywrightManager.close();
    }
}