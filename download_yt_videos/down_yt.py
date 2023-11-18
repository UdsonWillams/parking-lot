import types

import yt_dlp

consts = types.SimpleNamespace()
consts.UM_VIDEO: int = 1
consts.LISTA_DE_VIDEOS: int = 2
consts.PLAYLIST_DE_VIDEOS: int = 3
# Deixei os valores acima mais por aprendizado.


def download_one_video(url: list):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]",
        # "writeinfojson": True, # retorna valores do video em json
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # ydl.sanitize_info makes the info json-serializable
        dict_infos: dict = ydl.sanitize_info(info, True)
        # Desse jeito as infos de formato do video são retornadas \/
        # print(ydl.list_formats(dict_infos))

    video_name: dict = dict_infos.get("title")
    print(f"O VIDEO: {video_name} FOI BAIXADO!")


def main():
    print(("-" * 20) + "Baixar videos do youtube!" + ("-" * 20))
    url = str(input("\n\nLINK do video: "))
    download_one_video(url)


if __name__ == "__main__":
    main()
