package Activities1;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Activity1 {

	public static void main(String[] args) {
		WebDriverManager.firefoxdriver().setup();
		WebDriver driver=new FirefoxDriver();
		driver.get(" https://v1.training-support.net");
		System.out.println("Title of the Home page is :"+driver.getTitle());
		driver.findElement(By.id("about-link")).click();
		System.out.println("Title of the new page is :"+driver.getTitle());
		driver.close();
	}

}
