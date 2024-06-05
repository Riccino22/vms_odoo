from odoo import fields, api, models

class Word(models.Model):
    _name = 'vms.word'
    
    name = fields.Char("Word")
    translation = fields.Char("Translation", compute="_translate_word")

    @api.onchange("name")
    def _translate_word(self):
        for record in self:
            record.translation = "Mine"
            