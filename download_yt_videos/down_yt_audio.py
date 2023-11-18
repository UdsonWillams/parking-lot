import yt_dlp


def download_video_audio(url: list):
    ydl_opts = {
        "format": "bestaudio[ext=mp3]/best",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        # ydl.sanitize_info makes the info json-serializable
        dict_infos: dict = ydl.sanitize_info(info, True)

    video_name: dict = dict_infos.get("title")
    print(f"O VIDEO: {video_name} FOI BAIXADO!")


def main():
    print(("-" * 20) + "Baixar o audio de videos do youtube!" + ("-" * 20))
    url = str(input("\n\nLINK do video: "))
    download_video_audio(url)


if __name__ == "__main__":
    main()
