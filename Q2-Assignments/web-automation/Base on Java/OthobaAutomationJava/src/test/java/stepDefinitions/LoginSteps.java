//package stepDefinitions;
//
//import org.openqa.selenium.WebDriver;
//import io.cucumber.java.en.*;
//import pages.LoginPage;
//import utils.DriverManager;
//
//public class LoginSteps {
//    WebDriver driver = WebDriver.getDriver();
//    LoginPage loginPage = new LoginPage(driver);
//
//    @Given("user is on login page")
//    public void user_is_on_login_page() {
//        driver.get("https://www.othoba.com/login");
//    }
//
//    @When("user enters valid username and password")
//    public void user_enters_valid_username_and_password() {
//        loginPage.enterUsername("01706257588");
//        loginPage.enterPassword("Othoba4Beats@");
//    }
//
//    @When("clicks on login button")
//    public void clicks_on_login_button() {
//        loginPage.clickLogin();
//    }
//
//    @Then("user is navigated to the homepage")
//    public void user_is_navigated_to_the_homepage() {
//        // Assert the homepage URL or any other verification
//    }
//}
package stepDefinitions;

import org.openqa.selenium.WebDriver;
import io.cucumber.java.en.*;
import pages.LoginPage;
import utils.DriverManager;

public class LoginSteps {
    WebDriver driver = DriverManager.getDriver();  // Corrected to call getDriver() on DriverManager
    LoginPage loginPage = new LoginPage(driver);

    @Given("user is on login page")
    public void user_is_on_login_page() {
        driver.get("https://www.othoba.com/login");
    }

    @When("user enters valid username and password")
    public void user_enters_valid_username_and_password() {
        loginPage.enterUsername("01706257588");
        loginPage.enterPassword("Othoba4Beats@");
    }

    @When("clicks on login button")
    public void clicks_on_login_button() {
        loginPage.clickLogin();
    }

    @Then("user is navigated to the homepage")
    public void user_is_navigated_to_the_homepage() {
        // Assert the homepage URL or any other verification
    }
}
