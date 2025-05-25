# Website-Blocker

A simple Python tool to block or unblock websites on your computer by editing the system's `hosts` file. Useful for staying focused, preventing distractions, or limiting access to certain sites.

## What it Does:
When you open a website like `facebook.com`, your system looks up its IP address using something called **DNS**. But **before** doing that, your system checks a local file called the **`hosts` file**.

This project modifies that file to **redirect websites to your own computer (127.0.0.1)** — making the websites completely unreachable.

