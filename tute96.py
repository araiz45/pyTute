import multiprocessing
import requests

def DownloadFiles (url, name):
    print(f"Start Downloading {name}")
    response = requests.get(url)
    open(f"araiz-image/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://source.unsplash.com/random/1920x1080/?random"

    pros = []
    for i in range(50):
        p = multiprocessing.Process(target=DownloadFiles, args=[url, i])
        p.start()
        pros.append(p) 


    for p in pros:
        p.join()