import pdfplumber

class TextBox:
  def __init__(self, char):
    if len(char['text'].strip()) != 0:
      self.text = char['text']
      self.x = float(char['x0'])
      self.y = float(char['y0'])
      self.width = float(char['width'])
      self.height = float(char['height'])
      self.font_name = char['fontname']
      self.font_size = float(char['size'])
      self.page_number = char['page_number']


class Pdf2Box:
  def __init__(self, file_name):
    with pdfplumber.open(file_name) as reader:
      for page in reader.pages:
        for char in page.chars:
          text_box = TextBox(char)
          print(text_box.__dict__)


def test_Pdf2Box__init__():
  file_name = "./pdf-test.pdf"
  pdf2box = Pdf2Box(file_name)


if __name__ == "__main__":
  test_Pdf2Box__init__()