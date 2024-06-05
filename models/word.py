from odoo import fields, api, models
from . import defs

class Word(models.Model):
    _name = 'vms.word'
    
    name = fields.Char("Word")
    translation = fields.Char("Translation", compute="_translate_word")
    definition = fields.Text("Definition", compute="_translate_word")
    print("-----------------------------------------------")
    @api.onchange("name")
    def _translate_word(self):
        for record in self:
            word_data = defs.translate_with_llm(record.name)
            record.definition = word_data["definition"]
            record.translation = word_data["translation"]
            print(word_data["examples"])