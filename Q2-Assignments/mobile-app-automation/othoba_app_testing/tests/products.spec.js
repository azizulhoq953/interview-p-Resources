// Filename: test/products.spec.js

import { remote } from 'webdriverio';

describe('Product Module', () => {
    let driver;

    before(async () => {
        driver = await remote({
            logLevel: 'info',
            runner: 'local',
            path: '/',
            port: 4723,
            capabilities: {
                platformName: 'Android',
                'appium:deviceName': 'Realme C33',
                'appium:platformVersion': '13',
                'appium:app': '/data/app/~~MueMXAedlBErmyC0h6EAcw==/com.othoba.android-WTZYHzM67VU_ysbgvet3Yw==/base.apk',
                'appium:automationName': 'UiAutomator2',
            },
            services: ['appium'],
        });

        // Perform login
        await driver.$('~Username').setValue('01706257588'); // Replace with actual accessibility ID
        await driver.$('~Password').setValue('Othoba4Beats@'); // Replace with actual accessibility ID
        await driver.$('~LoginButton').click(); // Replace with actual accessibility ID
        await driver.pause(5000); // Wait for login to complete
    });

    it('should create a product', async () => {
        await driver.$('~Add Product').click(); // Replace with actual accessibility ID
        await driver.$('~ProductName').setValue('Test Product'); // Replace with actual accessibility ID
        await driver.$('~ProductPrice').setValue('100'); // Replace with actual accessibility ID
        await driver.$('~SaveButton').click(); // Replace with actual accessibility ID

        // Verify the product is added
        const productList = await driver.$('~ProductList').getText(); // Replace with actual accessibility ID
        expect(productList).toContain('Test Product');
    });

    after(async () => {
        await driver.deleteSession();
    });
});
