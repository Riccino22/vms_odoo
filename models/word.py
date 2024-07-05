from odoo import fields, api, models
from odoo.exceptions import ValidationError
from . import defs

class Word(models.Model):
    _name = 'vms.word'
    
    name = fields.Char("Word")
    translation = fields.Char("Translation", compute="_translate_word")
    definition = fields.Text("Definition", compute="_translate_word")
    examples = fields.Text("Examples", compute="_translate_word")
    category = fields.Char("Category", compute="_translate_word")
    synonyms = fields.Char("Synonyms", compute="_translate_word")
    language = fields.Selection([
    ('mandarin', 'Mandarin'),
    ('spanish', 'Spanish'),
    ('english', 'English'),
    ('hindi', 'Hindi'),
    ('arabic', 'Arabic'),
    ('bengali', 'Bengali'),
    ('portuguese', 'Portuguese'),
    ('russian', 'Russian'),
    ('japanese', 'Japanese'),
    ('western_punjabi', 'Western Punjabi'),
    ('marathi', 'Marathi'),
    ('telugu', 'Telugu'),
    ('wu_chinese', 'Wu Chinese'),
    ('turkish', 'Turkish'),
    ('korean', 'Korean'),
    ('french', 'French'),
    ('german', 'German'),
    ('vietnamese', 'Vietnamese'),
    ('tamil', 'Tamil'),
    ('urdu', 'Urdu'),
    ('javanese', 'Javanese'),
    ('italian', 'Italian'),
    ('egyptian_arabic', 'Egyptian Arabic'),
    ('gujarati', 'Gujarati'),
    ('iranian_persian', 'Iranian Persian'),
    ('bhojpuri', 'Bhojpuri'),
    ('southern_min', 'Southern Min'),
    ('haitian_creole', 'Haitian Creole'),
    ('hungarian', 'Hungarian'),
    ('malay', 'Malay')
], string='Language')

    print("-----------------------------------------------")
    @api.onchange("name")
    def _translate_word(self):
        for record in self:
            if record.name != False:
                word_data = defs.translate_with_llm(record.name, record.language)
                if word_data["translation"] and word_data["definition"] != "False":
                    record.definition = word_data["definition"]
                    record.translation = word_data["translation"]
                    record.category = word_data["category"]
                    record.synonyms = word_data["synonyms"]
                                    
                    examples = ""
                    for example in word_data["examples"]:
                        examples += f"- {example}\n"
                    record.examples = examples
                else:
                    raise ValidationError("The word or phrase can't be proccessed")
