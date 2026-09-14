def markdown_to_blocks(mardown: str) -> list[str]:
    blocks = mardown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks