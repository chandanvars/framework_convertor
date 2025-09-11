package base;

import com.microsoft.playwright.Browser;
import com.microsoft.playwright.Page;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import utils.PlaywrightFactory;

public class BaseTest {
    protected Browser browser;
    protected Page page;

    @BeforeMethod
    public void setUp() {
        browser = PlaywrightFactory.createBrowser();
        page = browser.newPage();
        page.setDefaultTimeout(10000);
        page.navigate("https://demoqa.com/");
    }

    @AfterMethod
    public void tearDown() {
        if (page != null) {
            page.close();
        }
        PlaywrightFactory.closeBrowser();
    }
}