from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support import expected_conditions as EC

class FrenchConjugation:
    def __init__(self, word):
        url = 'https://www.wordreference.com/conj/FrVerbs.aspx?v={}'.format(word)

        # Setting up a headless browser.
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

        # Run the browser.
        self.browser.implicitly_wait(5)
        self.browser.get(url)

    def __del__(self):
        try:
            self.browser.quit()
        except:
            print('Destructor Error')

    def __parse_response_output__(self, response):
        response = response.split('\n')
        response = response[1:7]
        return response

    def __get_response__(self, xpath1, func_name):
        response = None
        
        try:
            response = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, xpath1))).text
            response = self.__parse_response_output__(response)

        except:
            print('Error in function: {}'.format(func_name))
            
        return response

    def __get_two_response__(self, xpath1, xpath2, func_name):
        if self.has_note() and xpath2 != None:
            return self.__get_response__(xpath2, func_name)

        if xpath1 != None:
            return self.__get_response__(xpath1, func_name)

        return None

    # ------------------------------------------------------------------------------------------------------------------

    def okay(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/h3'))).text
        except:
            return False
        finally:
            return True

    def has_note(self):
        try:
            response = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[1]'))).text

            if 'In constructions where the past participle of ' in response:
                return True
        except:
            return False

    # ------------------------------------------------------------------------------------------------------------------
    def get_indicatif_pronouns(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[1]', func_name)

        je = response[0].split(' ')[0]
        tu = response[1].split(' ')[0]
        il_elle_on = ' '.join(response[2].split(' ')[0:3])
        nous = response[3].split(' ')[0]
        vous = response[4].split(' ')[0]
        ils_elles = ' '.join(response[5].split(' ')[0:2])

        return [je, tu, il_elle_on, nous, vous, ils_elles]

    def indicatif_present(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[1]', 'indicatif_present')
        pronouns = self.get_indicatif_pronouns()

        i: int
        for i in range(len(pronouns)):
            response[i] = response[i].replace(pronouns[i], '')[1:]

        return response

    def indicatif_imparfait(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[2]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[2]', 'indicatif_imparfait')
    
    def indicatif_passe_simple(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[3]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[3]', 'indicatif_passe_simple')

    def indicatif_futur_simple(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[4]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[4]', 'indicatif_futur_simple')
    
    # ------------------------------------------------------------------------------------------------------------------
    def get_compound_pronouns(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[1]', 'get_compound_pronouns')

        je = response[0].split(' ')[0]
        tu = response[1].split(' ')[0]
        il_elle_on = ' '.join(response[2].split(' ')[0:3])
        nous = response[3].split(' ')[0]
        vous = response[4].split(' ')[0]
        ils_elles = ' '.join(response[5].split(' ')[0:2])

        return [je, tu, il_elle_on, nous, vous, ils_elles]

    def compound_passe_compose(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[1]', 'compound_present')
        pronouns = self.get_compound_pronouns()

        i: int
        for i in range(len(pronouns)):
            response[i] = response[i].replace(pronouns[i], '')[1:]

        return response

    def compound_plus_que_parfait(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[2]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[2]', 'plus_que_parfait')

    def compound_passe_anterieur(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[3]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[3]', 'passe_anterior')

    def compound_futur_anterieur(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/table[4]','/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[4]',  'futur_anterieur')

    # ------------------------------------------------------------------------------------------------------------------
    def get_subjonctif_pronouns(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[1]', 'get_subjonctif_pronouns')

        je = ' '.join(response[0].split(' ')[0:2])
        tu = ' '.join(response[1].split(' ')[0:2])
        il_elle_on = ' '.join(response[2].split(' ')[0:3])
        nous = ' '.join(response[3].split(' ')[0:2])
        vous = ' '.join(response[4].split(' ')[0:2])
        ils_elles = ' '.join(response[5].split(' ')[0:2])

        return [je, tu, il_elle_on, nous, vous, ils_elles]

    def subjonctif_present(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[1]', 'subjonctif_present')
        pronouns = self.get_subjonctif_pronouns()

        i: int
        for i in range(len(pronouns)):
            response[i] = response[i].replace(pronouns[i], '')[1:]

        return response

    def subjonctif_imparfait(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[2]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[2]', 'subjonctif_imparfait')

    def subjonctif_passe(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[3]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[3]', 'subjonctif_passe_simple')

    def subjonctif_plus_que_parfait(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[4]/table[4]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[4]', 'subjonctif_plus_que_parfait')

    # ------------------------------------------------------------------------------------------------------------------
    
    def get_conditionnel_pronouns(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[1]', 'get_conditionnel_pronouns')

        je = response[0].split(' ')[0]
        tu = response[1].split(' ')[0]
        il_elle_on = ' '.join(response[2].split(' ')[0:3])
        nous = response[3].split(' ')[0]
        vous = response[4].split(' ')[0]
        ils_elles = ' '.join(response[5].split(' ')[0:2])

        return [je, tu, il_elle_on, nous, vous, ils_elles]

    def conditionnel_present(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[1]', 'conditionnel_present')
        pronouns = self.get_conditionnel_pronouns()

        i: int
        for i in range(len(pronouns)):
            response[i] = response[i].replace(pronouns[i], '')[1:]

        return response

    def conditionnel_passe1(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[2]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[2]', 'conditionnel_passe1')

    def conditionnel_passe2(self):
        return self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[5]/table[3]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[3]', 'conditionnel_passe2')
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def get_imperatif_pronouns(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[7]/table[1]', 'get_subjonctif_pronouns')
       
        je = response[0].split(' ')[0].replace('(', '').replace(')', '')
        tu = response[1].split(' ')[0].replace('(', '').replace(')', '')
        il_elle_on =  response[2].split(' ')[0].replace('(', '').replace(')', '')
        nous =  response[3].split(' ')[0].replace('(', '').replace(')', '')
        vous = response[4].split(' ')[0].replace('(', '').replace(')', '')
        ils_elles = response[5].split(' ')[0].replace('(', '').replace(')', '')

        return [je, tu, il_elle_on, nous, vous, ils_elles]

    def imperatif_present(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[1]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[7]/table[1]', 'imperatif_present')
        pronouns = self.get_imperatif_pronouns()

        i: int
        for i in range(len(pronouns)):
            if response[i] != '–':
                response[i] = response[i].replace(pronouns[i], '')[1:][2:]

        return response

    def imperatif_passe(self):
        response = self.__get_two_response__('/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[6]/table[2]', '/html/body/div[1]/div[4]/table/tbody/tr/td/table/tbody/tr/td[2]/div[7]/table[2]', 'imperatif_passe')
        pronouns = self.get_imperatif_pronouns()

        i: int
        for i in range(len(pronouns)):
            if response[i] != '–':
                response[i] = response[i].replace(pronouns[i], '')[1:]

        return response

# frc = FrenchConjugation('va')
# print(frc.okay())
# print(frc.get_indicatif_pronouns())
# print(frc.indicatif_present())
# print(frc.indicatif_imparfait())
# print(frc.indicatif_passe_simple())
# print(frc.indicatif_futur_simple())
# print(frc.get_compound_pronouns())
# print(frc.compound_passe_compose())
# print(frc.compound_plus_que_parfait())
# print(frc.compound_passe_anterieur())
# print(frc.compound_futur_anterieur())
# print(frc.get_subjonctif_pronouns())
# print(frc.subjonctif_present())
# print(frc.subjonctif_imparfait())
# print(frc.subjonctif_passe())
# print(frc.subjonctif_plus_que_parfait())
# print(frc.get_conditionnel_pronouns())
# print(frc.conditionnel_present())
# print(frc.conditionnel_passe1())
# print(frc.conditionnel_passe2())
# print(frc.get_imperatif_pronouns())
# print(frc.imperatif_present())
# print(frc.imperatif_passe())
