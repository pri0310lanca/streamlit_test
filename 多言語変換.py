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

#webブラウザ設定
st.set_page_config(
     page_title="多言語翻訳放送プロトタイプ",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded",
 )

#音声入力選択
red =st.sidebar.radio("Choice",["リアルタイム放送","音声データ選択"]) 
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
if red == "リアルタイム放送":
    def Translate_ja_to_en(word):
        # from googletrans import Translator
        translator  = Translator()
        word2 = translator.translate(word, src='ja', dest=selected_item)
        text = word2.text
        #st.write(text)
        return text
    # 音声合成定義
    def TextToSpeech_pyttsx3(ph):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[1].id)
        engine.say(ph)
        engine.runAndWait()
    #リアルタイム音声翻訳
    #音声入力　テキスト出力 音声出力
    def record():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("何かお話しして下さい。")
            st.sidebar.subheader("何かお話しして下さい。")
            audio = r.listen(source)
            try:
                result = r.recognize_google(audio, language='ja-JP')
                print(result)
                st.sidebar.subheader(result)
            except Exception:
                st.sidebar.subheader("音声検知できませんでした")               
                print("音声検知できませんでした")
            else:
                # word1 = input("翻訳する言葉を入力して！")
                word1 = result
                word2 = Translate_ja_to_en(word1)
                print(word2)
                st.header(word2)
                TextToSpeech_pyttsx3(word2)
    st.warning("「録音」ボタンを押して放送してください")
    if st.button("録音"):
        record()
    st.success("------translate text-----")

if red == "音声データ選択":
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
        # 音声合成の定義
        def TextToSpeech_pyttsx3(ph):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty("voice", voices[0].id)
            engine.say(ph)
            engine.runAndWait()
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
        st.sidebar.subheader("日本語認識")
        st.sidebar.subheader(result)
        st.header(word2)
        #選択言語の音声出力
        TextToSpeech_pyttsx3(word2)

