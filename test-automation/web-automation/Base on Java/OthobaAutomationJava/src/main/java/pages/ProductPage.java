package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class ProductPage {
    WebDriver driver;

    public ProductPage(WebDriver driver) {
        this.driver = driver;
    }

    // Locators
    By searchBox = By.id("search-box");
    By searchButton = By.id("search-submit");
    By productLink = By.xpath("//div[contains(@class, 'product-name')]");

    // Actions on Product Page
    public void searchProduct(String productName) {
        driver.findElement(searchBox).sendKeys(productName);
        driver.findElement(searchButton).click();
    }

    public void selectProduct() {
        driver.findElement(productLink).click();
    }
}
