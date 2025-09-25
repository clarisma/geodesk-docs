from bs4 import BeautifulSoup
from pathlib import Path

def expand_includes(soup, include_path):
    for include in soup.find_all("doc-include"):
        file = include.get("file")
        if not file:
            raise ValueError("<include> tag missing 'file' attribute")
        path = include_path / file
        if not path.is_file():
            raise FileNotFoundError(f"Include not found: {path}")
        content = path.read_text(encoding="utf-8")
        # Parse the included content so HTML fragments remain as markup
        fragment = BeautifulSoup(content, soup.builder.name)
        expand_includes(fragment, include_path)
        # Insert parsed fragment nodes after <include>, then remove the tag
        # (reverse to keep original order when using insert_after)
        for node in reversed(fragment.contents):
            include.insert_after(node)
        include.decompose()

def process_command(soup):
    for command in soup.find_all("doc-command"):
        print(f"Command: {command.get('name')}")
        for option in command.find_all("doc-option"):
            name = option.get("name")
            short = option.get("short")
            value = option.get("value")
            print(f"Option: {name}")

            header = soup.new_tag("h3")
            header['id'] = "option_" + name

            if short:
                e = soup.new_tag("code")
                e.append("-" + short)
                header.append(e)
                header.append(", ")
            e = soup.new_tag("code")
            e.append("--" + name)
            header.append(e)

            if value:
                header.append(" ")
                e = soup.new_tag("var")
                e.append("<" + value + ">")
                header.append(e)

            div = soup.new_tag("div")
            div["markdown"]	= "1"
            for child in list(option.contents):
                div.append(child)
                print(child)

            option.replace_with(header)
            header.insert_after(div)
        command.unwrap()

def process(soup, include_path):
    expand_includes(soup, include_path)
    process_command(soup)
    

def process_all(src_path, dest_path, include_path):
    count = 0
    for src in src_path.rglob("*.md"):
        rel = src.relative_to(src_path)
        dst = dest_path / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        process(soup, include_path)
        dst.write_text(str(soup), encoding="utf-8")
        count += 1

    print(f"Processed {count} file(s).")

if __name__ == "__main__":
    root = Path("c:\\dev\\geodesk-docs-v2")
    process_all(root / "_source\\gol", root / "_crap", root / "_include")



