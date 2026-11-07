def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    paras = markdown.split("\n\n")
    for para in paras:
        block = para.strip()
        if block != "":
            blocks.append(block)
        else: continue
    return blocks