import streamlit as st
import speech_recognition as sr
import speech_recognition
from googletrans import Translator
import pyttsx3
#import requests
#from gtts import gTTS
#from janome.tokenizer import Tokenizer
#import pykakasi
#import pygame
from mutagen.mp3 import MP3 as mp3
from time import sleep
import streamlit.components.v1 as stc
import base64
from gtts import gTTS
import urllib.request
import ffmpeg
import pathlib
import wave
import subprocess
import soundfile as sf
from urllib.request import urlopen
from shutil import copyfileobj
import requests
#webブラウザ設定
st.set_page_config(
     page_title="多言語翻訳放送プロトタイプ",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded",
 )

#音声入力選択
red =st.sidebar.radio("モードセレクト",["業務放送（デモ）","デバイス音声データ翻訳"]) 
#HTML表示UI設定
st.title("多言語翻訳放送プロトタイプ")
st.subheader("with googletrans")

#翻訳言語選択
selected_item = st.sidebar.selectbox('Select langage', ['afrikaans', 'albanian', 'amharic','arabic','armenian','azerbaijani','basque','belarusian','bengali','bosnian',\
                                                     'bulgarian','bengali','bosnian','bulgarian','catalan','cebuano','chichewa','zh-CN','zh-TW',\
                                                        'corsican','croatian','czech','danish','dutch ','english','esperanto','estonian '\
                                                            ,'filipino','finnish','french','galician','georgian','german','greek ','gujarati','haitian_creole',\
                                                                'hausa','hawaiian','hebrew ','hindi','hmong','hungarian','icelandic','igbo','indonesian','irish',\
                                                                    'italian','japanese','javanese','kannada','kazakh','khmer','korean','kurdish_kurmanji','kyrgyz',\
                                                                        'lao ','latin','latvian','lithuanian','luxembourgish','macedonian','malagasy','malay',\
                                                                            'malayalam','maltese','maori','marathi','mongolian','myanmar_burmese','nepali','norwegian',\
                                                                                'odia','pashto','persian','polish','portuguese','punjabi','romanian','russian'\
                                                                                    ,'samoan','scots_gaelic','serbian','sesotho','shona','sindhi','sinhala','slovak',\
                                                                                        'slovenian','somali','spanish','sundanese','swahili','swedish','tajik','tamil',\
                                                                                            'telugu','thai','turkish','ukrainian','urdu','uyghur','uzbek','vietnamese',\
                                                                                                'welsh','xhosa','yiddish','yoruba','zulu'])
st.sidebar.subheader(selected_item)
st.sidebar.subheader("-------CAUTION------")
st.sidebar.text("中国語（簡体）= you select zh-CN")
st.sidebar.text("中国語（繁体）= you select zh-TW")
st.sidebar.subheader("--------------------")
st.sidebar.subheader("")
st.sidebar.subheader("langage list (total:105) ")
st.sidebar.text('afrikaans')
st.sidebar.text('albanian')
st.sidebar.text('amharic')
st.sidebar.text('arabic')
st.sidebar.text('armenian')
st.sidebar.text('azerbaijani')
st.sidebar.text('basque')
st.sidebar.text('belarusian')
st.sidebar.text('bengali')
st.sidebar.text('bosnian')
st.sidebar.text('bulgarian')
st.sidebar.text('catalan')
st.sidebar.text('cebuano')
st.sidebar.text('chichewa')
st.sidebar.text('chinese (simplified)')
st.sidebar.text('chinese (traditional)')
st.sidebar.text('corsican')
st.sidebar.text('croatian')
st.sidebar.text('czech')
st.sidebar.text('danish')
st.sidebar.text('dutch')
st.sidebar.text('english')
st.sidebar.text('esperanto')
st.sidebar.text('estonian')
st.sidebar.text('filipino')
st.sidebar.text('finnish')
st.sidebar.text('french')
st.sidebar.text('frisian')
st.sidebar.text('galician')
st.sidebar.text('georgian')
st.sidebar.text('german')
st.sidebar.text('greek')
st.sidebar.text('gujarati')
st.sidebar.text('haitian creole')
st.sidebar.text('hausa')
st.sidebar.text('hawaiian')
st.sidebar.text('hebrew')
st.sidebar.text('hindi')
st.sidebar.text('hmong')
st.sidebar.text('hungarian')
st.sidebar.text('icelandic')
st.sidebar.text('igbo')
st.sidebar.text('indonesian')
st.sidebar.text('irish')
st.sidebar.text('italian')
st.sidebar.text('japanese')
st.sidebar.text('javanese')
st.sidebar.text('kannada')
st.sidebar.text('kazakh')
st.sidebar.text('khmer')
st.sidebar.text('korean')
st.sidebar.text('kurdish (kurmanji)')
st.sidebar.text('kyrgyz')
st.sidebar.text('lao')
st.sidebar.text('latin')
st.sidebar.text('latvian')
st.sidebar.text('lithuanian')
st.sidebar.text('luxembourgish')
st.sidebar.text('macedonian')
st.sidebar.text('malagasy')
st.sidebar.text('malay')
st.sidebar.text('malayalam')
st.sidebar.text('maltese')
st.sidebar.text('maori')
st.sidebar.text('marathi')
st.sidebar.text('mongolian')
st.sidebar.text('myanmar (burmese)')
st.sidebar.text('nepali')
st.sidebar.text('norwegian')
st.sidebar.text('odia')
st.sidebar.text('pashto')
st.sidebar.text('persian')
st.sidebar.text('polish')
st.sidebar.text('portuguese')
st.sidebar.text('punjabi')
st.sidebar.text('romanian')
st.sidebar.text('russian')
st.sidebar.text('samoan')
st.sidebar.text('scots gaelic')
st.sidebar.text('serbian')
st.sidebar.text('sesotho')
st.sidebar.text('shona')
st.sidebar.text('sindhi')
st.sidebar.text('sinhala')
st.sidebar.text('slovak')
st.sidebar.text('slovenian')
st.sidebar.text('somali')
st.sidebar.text('spanish')
st.sidebar.text('sundanese')
st.sidebar.text('swahili')
st.sidebar.text('swedish')
st.sidebar.text('tajik')
st.sidebar.text('tamil')
st.sidebar.text('telugu')
st.sidebar.text('thai')
st.sidebar.text('turkish')
st.sidebar.text('ukrainian')
st.sidebar.text('urdu')
st.sidebar.text('uyghur')
st.sidebar.text('uzbek')
st.sidebar.text('vietnamese')
st.sidebar.text('welsh')
st.sidebar.text('xhosa')
st.sidebar.text('yiddish')
st.sidebar.text('yoruba')
st.sidebar.text('zulu')
afrikaans = "af";albanian ="sq";amharic ="am";arabic = "ar";armenian = "hy";azerbaijani = "az";basque = "eu";belarusian = "be";bengali = "bn";bosnian = "bs"
bulgarian = "bg";catalan = "ca";cebuano = "ceb";chichewa = "ny";#chinese = "zh-cn";#traditional = "tw"\;
corsican = "co";croatian = "hr";czech = "cs"
danish = "da";dutch = "nl";english = "en";esperanto = "eo";estonian = "et";filipino = "tl";finnish = "fi";french = "fr";frisian = "fy";galician = "gl"
georgian = "ka";german = "de";greek = "el";gujarati = "gu";haitian_creole ="ht";hausa = "ha";hawaiian = "haw";hebrew = "iw";hindi = "hi";hmong = "hmn"
hungarian = "hu";icelandic = "is";igbo = "ig";indonesian = "id";irish = "ga";italian = "it";japanese = "ja";javanese = "jw";kannada = "kn";kazakh = "kk"
khmer = "km";korean = "ko";kurdish_kurmanji ="ku";kyrgyz = "ky";lao = "lo";latin = "la";latvian = "lv";lithuanian = "lt";luxembourgish = "lb";macedonian = "mk"
malagasy = "mg";malay = "ms";malayalam = "ml";maltese = "mt"
maori = "mi";marathi = "mr";mongolian = "mn";myanmar_burmese = "my";nepali = "ne";norwegian = "no";odia = "or";pashto = "ps";persian = "fa";polish = "pl"
portuguese = "pt";punjabi = "pa";romanian = "ro";russian = "ru";samoan = "sm";scots_gaelic = "gd";serbian = "sr";sesotho = "st";shona = "sn";sindhi = "sd"
sinhala = "si";slovak = "sk";slovenian = "sl";somali = "so";spanish = "es";sundanese = "su";swahili = "sw";swedish = "sv";tajik = "tg";tamil = "ta";telugu = "te"
thai = "th";turkish = "tr";ukrainian = "uk";urdu = "ur";uyghur = "ug";uzbek = "uz";vietnamese = "vi";welsh = "cy";xhosa = "xh";yiddish = "yi";yoruba = "yo";zulu = "zu"

# 翻訳定義 （リアルタイム） 
if red == "業務放送（デモ）":
    submit_btn = st.button("業務放送（デモ）翻訳START")
    if submit_btn:
        #githubのURL指定（録音データをこのディレクトリに格納する.pyを作成予定）
        url = "https://github.com/pri0310lanca/streamlit_test/raw/main/isshoniganbattemiyou_01.wav"
        response = requests.get(url)
        #get 成功の場合、下で200のコードを返す
        #print(response.status_code)
        file = open("audio_file","rb")
        #下で日本語を読み込む
        #audio_bytes = file.read()
        #ここでダウンロードしたファイルを再wav化
        wf = wave.open("audio_file","rb")

        # wavファイルを日本語に翻訳
        r = speech_recognition.Recognizer()
        # （file）で相対パスを指定。GUIファイルと連携
        with speech_recognition.AudioFile("audio_file") as source:
            audio = r.record(source)
            result = r.recognize_google(audio, language="ja-JP")
        file.close()
        wf.close()

        # 翻訳（日本語から外国語）の定義    
        def Translate_ja_to_en(word):
            # from googletrans import Translator
            translator  = Translator()
            word2 = translator.translate(word, src='ja', dest=selected_item)
            text = word2.text
            return text
        word1 = result
        word2 = Translate_ja_to_en(word1)
        print(r.recognize_google(audio, language='ja-JP'))
        st.text("---日本語テキスト---")
        st.subheader(result)
        st.text("---翻訳テキスト---")
        st.header(word2)

        #選択言語の音声出力(streamlittest)
        tts_en = gTTS(word2,
                lang = "en"
                )
        tts_en.save('word2.mp3')
        audio_file = open('word2.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
        audio_file.close()
        sample_rate = 44100  # 44100 samples per second
        seconds = 2  # Note duration of 2 seconds
        frequency_la = 440  # Our played note will be 440 Hz

    st.success("------translate success-----")

if red == "デバイス音声データ翻訳":
    # 音声ファイルをアップロードする
    audio_file = st.file_uploader("音声ファイルをアップロードしてください", type=["mp3", "wav"])
    submit_btn = st.button("送信")
    if submit_btn:
        st.write("音声ファイルを送信しました")
        # wavファイルを日本語に翻訳
        r = speech_recognition.Recognizer()
        # （file）で相対パスを指定。GUIファイルと連携
        with speech_recognition.AudioFile(audio_file) as source:
            audio = r.record(source)
            result = r.recognize_google(audio, language="ja-JP")

        # 翻訳（日本語から外国語）の定義    
        def Translate_ja_to_en(word):
            # from googletrans import Translator
            translator  = Translator()
            word2 = translator.translate(word, src='ja', dest=selected_item)
            text = word2.text
            return text
        word1 = result
        word2 = Translate_ja_to_en(word1)
        print(r.recognize_google(audio, language='ja-JP'))
        st.text("---日本語テキスト---")
        st.subheader(result)
        st.text("---翻訳テキスト---")
        st.header(word2)

        #選択言語の音声出力(streamlittest)
        tts_en = gTTS(word2,
                lang = "en"
                )
        tts_en.save('word2.mp3')
        audio_file = open('word2.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/ogg')

        sample_rate = 44100  # 44100 samples per second
        seconds = 2  # Note duration of 2 seconds
        frequency_la = 440  # Our played note will be 440 Hz
        st.success("------translate success-----")
