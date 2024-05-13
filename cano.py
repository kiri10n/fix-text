import re

def line_up(batch):
    batch = re.sub("\r?\n", " ", batch)
    return batch

def main():
    input = "./input.txt"
    out = "./output.txt"

    with open(file=input, mode="r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

        removed_text = "".join(map(line_up, lines))
    
    with open(file=out, mode="w", encoding="utf-8") as output_file:
        output_file.write(removed_text)

if __name__ == "__main__":
    main()