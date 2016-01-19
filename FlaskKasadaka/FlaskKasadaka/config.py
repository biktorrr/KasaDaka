#Change these variables according to your installation

#Sparql endpoint
sparqlURL = "http://127.0.0.1:3020/sparql/"

#default language
defaultLanguage = "en"
#audio files location
audioURLbase = "http://127.0.0.1/audio/"

#debug mode
debug=False

##DO NOT EDIT BELOW THIS line



class LanguageVars(object):
	"""This class is used to process languages.
	By default the default language from the config is used. 
	"""
    audioURL = audioURLbase + defaultLanguage + "/"
    audioInterfaceURL = audioURLbase + defaultLanguage + "/interface/"
    language = defaultLanguage

    def replaceVoicelabels(self,inputQuery,
    voicelabelToReplace = "speakle:voicelabel_en",
    voicelabelReplacement = "speakle:voicelabel_"):
		"""replaces the speakle voicelabels in a string
		"""
        return inputQuery.replace(voicelabelToReplace,voicelabelReplacement+self.language)

    def __init__(self,languageInit):
		"""Initializes language object from lang string, or from many arguments, including a string
		"""
        if type(languageInit) is not str and 'lang' in languageInit:
             self.audioURL = audioURLbase + languageInit['lang'] + "/"
             self.audioInterfaceURL = audioURLbase + languageInit['lang'] + "/interface/"
             self.language = languageInit['lang']
        elif type(languageInit) is str:
            self.audioURL = audioURLbase + languageInit + "/"
            self.audioInterfaceURL = audioURLbase + languageInit + "/interface/"
            self.language = languageInit

    def __str__(self):
        return language
