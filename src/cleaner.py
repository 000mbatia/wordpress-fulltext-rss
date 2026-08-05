from bs4 import BeautifulSoup


def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove the like/dislike widget
    for widget in soup.select(".pld-like-dislike-wrap"):
        widget.decompose()

    # Fix lazy-loaded images
    for img in soup.find_all("img"):
        if img.get("data-src"):
            img["src"] = img["data-src"]

        # Remove unnecessary attributes
        for attr in [
            "loading",
            "decoding",
            "data-src",
            "data-srcset",
            "data-sizes",
            "sizes",
            "srcset",
        ]:
            img.attrs.pop(attr, None)

    return str(soup)