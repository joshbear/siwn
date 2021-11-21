import yaml
import random

# with open('monster.yaml', 'r') as file:
#     feature_roll = yaml.safe_load(file)

# print(feature_roll)

class FeatureGenerator:
    feature_roll = None

    def __init__(self, source):
        with open(source + '.yaml', 'r') as file:
            self.feature_roll = yaml.safe_load(file)

    def get_list_option(self, feature):
        if feature in self.feature_roll:
            options = self.feature_roll[feature]
        else:
            print('No such feature: ' + feature)
            return

        weighted_options = []
        odds_name = feature + '_odds'

        if odds_name in self.feature_roll:
            odds = self.feature_roll[odds_name]
        else:
            odds = []
            for option in options:
                odds.append(1)

        if len(odds) != len(options):
            print('List of odds does not match that of the hunt options.',
                  ' Therefore, all options will be given equal weight.')
            odds = []
            for option in options:
                odds.append(1)

        for option, odd in zip(options, odds):
            for i in range(odd):
                weighted_options.append(option)

        return random.choice(weighted_options)


    def get_categorical_option(self, feature):
        if feature in self.feature_roll:
            categories = self.feature_roll[feature]
        else:
            print('No such feature: ' + feature)
            return

        selection = random.choice(categories)
        category, options = list(selection.items())[0]
        return category, random.choice(options)
