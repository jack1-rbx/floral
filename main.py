import webview

if __name__ == "__main__":
    webview.create_window(
        "Floral Radio",
        "https://floralradio.uk/",
        width=1200,
        height=800,
        resizable=True
    )
    webview.start()
