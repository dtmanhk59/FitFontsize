import pdfplumber

class Pdf2Box:
  def __init__(self, file_name):
    with pdfplumber.open(file_name) as reader:
      for page in reader.pages:
        print(page)


def test_Pdf2Box__init__():
  file_name = "./pdf-test.pdf"
  pdf2box = Pdf2Box(file_name)


if __name__ == "__main__":
  test_Pdf2Box__init__()