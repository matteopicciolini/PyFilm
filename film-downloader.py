import requests
import m3u8
from urllib.parse import urljoin
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def download_segment(segment_info):
    url = urljoin(base_url, segment_info["uri"])
    r = requests.get(url)
    return r.content


#insert master link here
url = ""

r = requests.get(url)
m3u8_master = m3u8.loads(r.text)
playlist_url = m3u8_master.data["playlists"][0]["uri"]
r = requests.get(playlist_url)
playlist = m3u8.loads(r.text)
base_url = urljoin(url, playlist_url)

output_file = "video.ts"

with ThreadPoolExecutor() as executor, open(output_file, "wb") as f:
    # Usa tqdm per visualizzare una barra di avanzamento
    segment_infos = playlist.data["segments"]
    futures = [executor.submit(download_segment, segment) for segment in segment_infos]

    for future in tqdm(futures, total=len(segment_infos), desc="Downloading segments"):
        f.write(future.result())
