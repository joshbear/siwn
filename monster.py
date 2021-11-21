import utils

def new_monster(prose=True):
    # file = 'monster.yaml'
    prose_desc = ''
    itemized_desc = ''
    monster_gen = utils.FeatureGenerator('monster')
    hunt = monster_gen.get_list_option('hunt')
    form = monster_gen.get_list_option('form')
    body = monster_gen.get_list_option('body')
    survival = monster_gen.get_list_option('survival')
    characteristics, special_feature = monster_gen.get_categorical_option('characteristics')

    if prose:
        prose_desc += 'You are approached by a ' + characteristics.lower() + ' creature. '
        prose_desc += ('It has a generally ' + form.lower() + ' form that is '
                       + body.lower() + '. ')
        prose_desc += 'The most striking feature is it\'s ' + special_feature.lower() + '. '
        prose_desc += 'To hunt, ' + hunt.lower() + '. '
        prose_desc += 'You suspect that it has survived because ' + survival.lower() + '.'
        return prose_desc
    else:
        itemized_desc += 'Creature type:   ' + characteristics + '\n'
        itemized_desc += 'Form:            ' + form + '\n'
        itemized_desc += 'Body:            ' + body + '\n'
        itemized_desc += 'Notable feature: ' + special_feature + '\n'
        itemized_desc += 'Hunting habits:  ' + hunt + '\n'
        itemized_desc += 'Survival:        ' + survival + '\n'
        print(itemized_desc)
        return itemized_desc
