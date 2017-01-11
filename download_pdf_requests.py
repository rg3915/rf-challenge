import requests


def main():
    download_file('http://www.bcb.gov.br/pec/GCI/PORT/readout/R20160324.pdf')


def download_file(download_url):
    with open("R20160324.pdf", 'wb') as book:
        a = requests.get(download_url)
        for block in a.iter_content(chunk_size=1024):
            if not block:
                break

            book.write(block)


if __name__ == "__main__":
    main()
