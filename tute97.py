import concurrent.futures
import requests

def DownloadFiles (url, name):
    print(f"Start Downloading {name}")
    response = requests.get(url)
    open(f"araiz-image/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://source.unsplash.com/random/1920x1080/?random"
    

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l = [i for i in range(30)]
        l2 = [url for i in range(30)]
        results = executor.map(DownloadFiles, l2, l)
        for r in results:
            print(r)


