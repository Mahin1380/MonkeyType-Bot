import nodriver as uc
import asyncio
import time


async def main():
    """
    Main function for the test
    """
    # Start the browser
    browser = await uc.start()
    
    # Navigate to the website
    page = await browser.get("https://monkeytype.com/")

    # Wait for 5 seconds
    await asyncio.sleep(5)

    # Accept the cookies
    cookies_ = await page.select("#cookiesModal > div.modal > div.main > div.buttons > button.active.acceptAll")

    await cookies_.click()

    # Get all the words on the page
    words = await page.select_all("#words > div")

    # Get the active word
    activity = await page.select("#words > div.word.active")

    # Loop through all the words and get the text and put them in a list
    elements = [word.text_all.strip().replace(" ", "") for word in words]
    # Click on the active word
    await activity.click()

    # Get the start time
    start = time.time()
    # Loop through all the words and type them
    for word in elements:
        # Loop through each character in the word
        for char in word:
            # Get the time elapsed
            end = time.time() - start
            # If the time elapsed is greater than 30 seconds, break the loop
            if end >= 30:
                break
            else:
                # Send the character to the active word
                await activity.send_keys(char)
                # Wait for 0.1 seconds
                await asyncio.sleep(0.1)
        # If the time elapsed is greater than 30 seconds, break the loop
        if end >= 30:
            break
        # Send a space to the active word
        await activity.send_keys(" ")
        # Wait for 0.1 seconds
        await asyncio.sleep(0.1)

            
    # Wait for 5 seconds
    await asyncio.sleep(5)

    # Close the page
    await page.close()

if __name__ == "__main__":
    uc.loop().run_until_complete(main())