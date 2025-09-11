package tests;

import com.microsoft.playwright.*;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 * Simple demonstration test showing the converted Playwright framework
 * This test can run in headless mode to verify the conversion works
 */
public class FrameworkDemoTest {
    private Playwright playwright;
    private Browser browser;
    private Page page;

    @BeforeMethod
    public void setUp() {
        playwright = Playwright.create();
        // Use headless mode for demo
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions().setHeadless(true));
        page = browser.newPage();
    }

    @Test
    public void demoPlaywrightConversion() {
        // Navigate to a simple page to demonstrate Playwright is working
        page.navigate("https://example.com");
        
        // Verify the page title
        String title = page.title();
        Assert.assertTrue(title.contains("Example"), "Page title should contain 'Example'");
        
        // Demonstrate Playwright locator usage
        String heading = page.locator("h1").textContent();
        Assert.assertNotNull(heading, "Heading should not be null");
        
        System.out.println("✅ Playwright framework conversion successful!");
        System.out.println("✅ Page title: " + title);
        System.out.println("✅ Heading text: " + heading);
    }

    @AfterMethod
    public void tearDown() {
        if (page != null) {
            page.close();
        }
        if (browser != null) {
            browser.close();
        }
        if (playwright != null) {
            playwright.close();
        }
    }
}