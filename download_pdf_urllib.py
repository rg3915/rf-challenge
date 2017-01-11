from urllib.request import urlopen

def main():
    download_file('http://www.bcb.gov.br/pec/GCI/PORT/readout/R20161230.pdf')


def download_file(download_url):
    response = urlopen(download_url)
    file = open("R20161230.pdf", 'wb')
    file.write(response.read())
    file.close()
    print('Completed')


if __name__ == "__main__":
    main()
