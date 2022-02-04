# PyFrenchConjugations
Just a file that fetches french conjugations from www.wordreference.com.

# Usage:
```py
frc = FrenchConjugation('va')
print(frc.okay())
print(frc.get_indicatif_pronouns())
print(frc.indicatif_present())
print(frc.indicatif_imparfait())
print(frc.indicatif_passe_simple())
print(frc.indicatif_futur_simple())
print(frc.get_compound_pronouns())
print(frc.compound_passe_compose())
print(frc.compound_plus_que_parfait())
print(frc.compound_passe_anterieur())
print(frc.compound_futur_anterieur())
print(frc.get_subjonctif_pronouns())
print(frc.subjonctif_present())
print(frc.subjonctif_imparfait())
print(frc.subjonctif_passe())
print(frc.subjonctif_plus_que_parfait())
print(frc.get_conditionnel_pronouns())
print(frc.conditionnel_present())
print(frc.conditionnel_passe1())
print(frc.conditionnel_passe2())
print(frc.get_imperatif_pronouns())
print(frc.imperatif_present())
print(frc.imperatif_passe())
```

Output:
```
True
["je/j'", 'tu', 'il, elle, on', 'nous', 'vous', 'ils, elles']
['vais', 'vas', 'va', 'allons', 'allez', 'vont']
['allais', 'allais', 'allait', 'allions', 'alliez', 'allaient']
['allai', 'allas', 'alla', 'allâmes', 'allâtes', 'allèrent']
['irai', 'iras', 'ira', 'irons', 'irez', 'iront']
["je/j'", 'tu', 'il, elle, on', 'nous', 'vous', 'ils, elles']
['suis allé(e)', 'es allé(e)', 'est allé(e)', 'sommes allé(e)s', 'êtes allé(e)(s)', 'sont allé(e)s']
['étais allé(e)', 'étais allé(e)', 'était allé(e)', 'étions allé(e)s', 'étiez allé(e)(s)', 'étaient allé(e)s']
['fus allé(e)', 'fus allé(e)', 'fut allé(e)', 'fûmes allé(e)s', 'fûtes allé(e)(s)', 'furent allé(e)s']
['serai allé(e)', 'seras allé(e)', 'sera allé(e)', 'serons allé(e)s', 'serez allé(e)(s)', 'seront allé(e)s']
["que je/j'", 'que tu', "qu'il, elle, on", 'que nous', 'que vous', "qu'ils, elles"]
['aille', 'ailles', 'aille', 'allions', 'alliez', 'aillent']
['allasse', 'allasses', 'allât', 'allassions', 'allassiez', 'allassent']
['sois allé(e)', 'sois allé(e)', 'soit allé(e)', 'soyons allé(e)s', 'soyez allé(e)(s)', 'soient allé(e)s']
['fusse allé(e)', 'fusses allé(e)', 'fût allé(e)', 'fussions allé(e)s', 'fussiez allé(e)(s)', 'fussent allé(e)s']
["je/j'", 'tu', 'il, elle, on', 'nous', 'vous', 'ils, elles']
['irais', 'irais', 'irait', 'irions', 'iriez', 'iraient']
['serais allé(e)', 'serais allé(e)', 'serait allé(e)', 'serions allé(e)s', 'seriez allé(e)(s)', 'seraient allé(e)s']
['fusse allé(e)', 'fusses allé(e)', 'fût allé(e)', 'fussions allé(e)s', 'fussiez allé(e)(s)', 'fussent allé(e)s']
['–', 'tu', '–', 'nous', 'vous', '–']
['–', 'va !', '–', 'allons !', 'allez !', '–']
['–', 'ois allé(e) !', '–', 'oyons allé(e)s !', 'oyez allé(e)(s) !', '–']
```
