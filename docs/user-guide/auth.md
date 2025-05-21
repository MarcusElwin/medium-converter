# Authentication

Medium Converter can access articles behind Medium's paywall by using authentication cookies from your browser.

## Browser Cookies

By default, Medium Converter attempts to extract cookies from your browser to authenticate requests to Medium. This allows you to access articles that would normally require a Medium membership if you're already logged in.

### Supported Browsers

Medium Converter supports extracting cookies from the following browsers:

- Chrome/Chromium
- Firefox
- Safari (macOS only)
- Edge
- Opera
- Brave

### Using Browser Cookies

#### Command Line

```bash
# Enabled by default
medium convert https://medium.com/example-article

# Explicitly enable
medium convert https://medium.com/example-article --use-cookies

# Disable
medium convert https://medium.com/example-article --no-cookies
```

#### Python API

```python
from medium_converter import convert_article

# Enabled by default
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown"
)

# Explicitly enable
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    use_cookies=True
)

# Disable
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    use_cookies=False
)
```

## Manual Cookie Configuration

If automatic cookie extraction doesn't work, you can manually specify cookies:

### Environment Variables

```bash
export MEDIUM_SID=your_sid_cookie
export MEDIUM_UID=your_uid_cookie
```

### Configuration File

In `~/.medium-converter/config.toml`:

```toml
[auth]
sid = "your_sid_cookie"
uid = "your_uid_cookie"
```

### Python API

```python
from medium_converter import convert_article
from medium_converter.core.auth import get_medium_cookies

# Create a custom cookie dictionary
cookies = {
    "sid": "your_sid_cookie",
    "uid": "your_uid_cookie"
}

await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    cookies=cookies
)
```

## Finding Your Cookies Manually

If you need to manually find your Medium cookies:

1. Log in to Medium in your browser
2. Open DevTools (F12 or Right-click > Inspect)
3. Go to the Application tab (Chrome) or Storage tab (Firefox)
4. Select Cookies in the left sidebar
5. Select the medium.com domain
6. Look for `sid` and `uid` cookies

## Limitations

- Cookie authentication only works if you have an active Medium membership
- Cookies expire after a certain period (usually a few weeks)
- Some browsers store cookies in an encrypted format that may not be accessible
- Corporate security policies might prevent accessing cookies