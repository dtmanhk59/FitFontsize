import pdfplumber


def pt2px(pt, dpi):
    return int(float(pt) * dpi / 72)


def pdf_to_boxes(file_name, dpi):
  boxes = []
  with pdfplumber.open(file_name) as pdf:
    for page_number, page in enumerate(pdf.pages):
      for char in page.chars:
        text = char['text']
        font_name = char['fontname']
        x = pt2px(char['x0'], dpi)
        y = pt2px(char['top'], dpi)
        w = pt2px(char['width'], dpi)
        h = pt2px(char['height'], dpi)
        if text.strip() != "":
          boxes.append([text, x, y, w, h, font_name, page_number])
  return boxes


def boxes_to_network(boxes):
  pass


if __name__ == "__main__":
  boxes = pdf_to_boxes("pdf-test.pdf", 300)
  for box in boxes:
    print(box)
