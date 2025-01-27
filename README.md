

# MonkeyType Typing Automation

This project automates typing on the **MonkeyType** website using **nodriver** and **asyncio**. It types words from a list of elements, simulating user typing, and stops after 30 seconds.

## Features
- Automates the typing of words in the **MonkeyType** typing game.
- Simulates typing character-by-character with customizable typing speed.
- Stops typing automatically after 30 seconds.

## Prerequisites
Before running the code, ensure you have the following installed:

- **Python 3.7+**
- **nodriver**: For browser automation
- **asyncio**: For asynchronous operations

You can install `nodriver` with:
```bash
pip install nodriver
```

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install nodriver asyncio
   ```

## Usage

1. **Run the Script**:
   Simply execute the script:
   ```bash
   python monkeytype_typing_automation.py
   ```

2. **How It Works**:
   - The script opens the MonkeyType website.
   - It waits for the cookies banner to appear and accepts the cookies.
   - The script gathers the list of words to be typed.
   - It types each word character-by-character with a small delay between each character.
   - After typing each word, it simulates pressing the spacebar.
   - The script stops typing automatically after 30 seconds or once all words are typed.

## Code Breakdown

### 1. Browser Initialization:
The code uses **nodriver** to start the browser and open the **MonkeyType** website.

```python
browser = await uc.start()
page = await browser.get("https://monkeytype.com/")
```

### 2. Cookie Acceptance:
The script waits for the cookie consent modal and clicks the "Accept All" button.

```python
cookies_ = await page.select("#cookiesModal > div.modal > div.main > div.buttons > button.active.acceptAll")
await cookies_.click()
```

### 3. Word Collection:
The script collects all words to be typed from the page.

```python
words = await page.select_all("#words > div.word")
elements = [word.text_all.strip().replace(" ", "") for word in words]
```

### 4. Typing Simulation:
The script types each word by simulating key presses with the `send_keys` method.

```python
for word in elements:
    for char in word:
        await activity.send_keys(char)
        await asyncio.sleep(0.1)  # Typing speed delay
```

### 5. Timer for Stopping:
The script tracks elapsed time using `time.time()` and stops typing after 30 seconds.

```python
start = time.time()  # Start timer before typing
elapsed_time = time.time() - start
if elapsed_time >= 30:
    break  # Stop typing after 30 seconds
```

## Customization

- **Typing Speed**: Adjust the typing speed by changing the `await asyncio.sleep(0.1)` delay inside the `for char in word` loop.
- **Timer Duration**: Change the `30` value in the `if elapsed_time >= 30:` line to customize the time limit.

## License
This project is licensed under the Apache 2.0 License.
