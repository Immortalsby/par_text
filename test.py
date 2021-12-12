
from deep_translator import DeepL
#translated = GoogleTranslator(source='fr', target='zh-CN').translate("amour")
translated = DeepL(api_key="94001194-c302-dea6-9fda-02a577bb4b3f:fx",
source='french', target='chinese',use_free_api=True).translate("amour", return_all=True)
print(translated)