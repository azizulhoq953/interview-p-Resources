package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class CartPage {
    WebDriver driver;

    public CartPage(WebDriver driver) {
        this.driver = driver;
    }

    // Locators
    By addToCartButton = By.id("add-to-cart");
    By viewCartButton = By.id("view-cart");

    // Actions on Cart Page
    public void addToCart() {
        driver.findElement(addToCartButton).click();
    }

    public void viewCart() {
        driver.findElement(viewCartButton).click();
    }
}
