from pyluach import dates, parshios

JWT_SECRET_KEY = "my_secret_key_is_invisble_123456"

PARSHIOT_HEB_TO_ENG_SORTED = {
    'אחרי מות': 'achrei_mot',
    'אמור': 'emor',
    'בא': 'bo',
    'בלק': 'balak',
    'במדבר': 'bamidbar',
    'בהר': 'behar',
    'בחוקותי': 'bechukotai',
    'בהעלותך': 'behaalotcha',
    'בראשית': 'bereshit',
    'בשלח': 'beshalach',
    'חיי שרה': 'chayei_sara',
    'חקת': 'chukat',
    'דברים': 'devarim',
    'עקב': 'eikev',
    'האזינו': 'haazinu',
    'קדושים': 'kedoshim',
    'כי תבא': 'ki_tavo',
    'כי תצא': 'ki_teitzei',
    'כי תשא': 'ki_tisa',
    'קרח': 'korach',
    'לך לך': 'lech_lecha',
    'מסעי': 'masei',
    'מטות': 'matot',
    'מצורע': 'metzora',
    'מקץ': 'miketz',
    'משפטים': 'mishpatim',
    'נשא': 'nasso',
    'נצבים': 'nitzavim',
    'נח': 'noach',
    'פקודי': 'pekudei',
    'פינחס': 'pinchas',
    'ראה': "reeh",
    'שמות': 'shemot',
    'שלח': 'shlach',
    'שמיני': 'shmini',
    'שופטים': 'shoftim',
    'תזריע': 'tazria',
    'תרומה': 'terumah',
    'תצוה': 'tetzaveh',
    'תולדות': 'toldot',
    'צו': 'tzav',
    'וארא': 'vaera',
    'ואתחנן': 'vaetchanan',
    'ויחי': 'vayechi',
    'וילך': 'vayelech',
    'וישב': 'vayeshev',
    'ויצא': 'vayetzei',
    'וירא': 'vayera',
    'ויגש': 'vayigash',
    'ויקרא': 'vayikra',
    'וישלח': 'vayishlach',
    'ויקהל': 'vayakhel',
    'וזאת הברכה': 'vezot_haberachah',
    'יתרו': 'yitro'
}
def get_current_parsha():
    today = dates.HebrewDate.today()
    parsha = parshios.getparsha_string(today, israel=True, hebrew=True)
    #print (PARSHIOT_HEB_TO_ENG_SORTED[parsha])
    return PARSHIOT_HEB_TO_ENG_SORTED[parsha]

#get_current_parsha()