# Student number: KSKTAN003
# Student name: Craig Kaseke
# Date: 7 March 2025
# Last modified: 7 March 2025
#
# Program Description:
# This program classifies an organism based on user responses to a series of yes/no questions.
# It follows a decision tree to determine whether the organism is a vertebrate or invertebrate
# and further categorizes it into specific groups such as mammals, birds, reptiles, fish, insects, etc.
# The classification is based on key characteristics such as backbone presence, warm-bloodedness,
# scales, fur, number of legs, and body segmentation.
#

print('Welcome to the Biology Expert\n')
print('-' * 80)
print('Answer the following questions by selecting from among the options.\n')

organism_classification = ''

has_backbone = input('Does the organism have a backbone? (yes/no): ').strip().lower()

if has_backbone == 'yes':  # Vertebrate
    is_warm_blooded = input('Is it warm-blooded? (yes/no): ').strip().lower()

    if is_warm_blooded == 'yes':  # Endotherm
        has_feathers = input('Does it have feathers? (yes/no): ').strip().lower()
        if has_feathers == 'yes':
            organism_classification = 'Bird'
        else:
            has_fur = input('Does it have fur? (yes/no): ').strip().lower()
            if has_fur == 'yes':
                organism_classification = 'Mammal'
            else:
                organism_classification = 'Other Vertebrate' 
    else:  # Ectotherm
        has_scales = input('Does it have scales? (yes/no): ').strip().lower()
        if has_scales == 'yes':
            lives_in_water = input('Does it live in water? (yes/no): ').strip().lower()
            if lives_in_water == 'yes':
                organism_classification = 'Fish'
            else:
                organism_classification = 'Reptile'
        else:
            organism_classification = 'Amphibian'
else:  # Invertebrate
    has_exoskeleton = input('Does it have an exoskeleton? (yes/no): ').strip().lower()
    if has_exoskeleton == 'yes':
        has_six_legs = input('Does it have six legs? (yes/no): ').strip().lower()
        if has_six_legs == 'yes':
            organism_classification = 'Insect'
        else:
            has_eight_legs = input('Does it have eight legs? (yes/no): ').strip().lower()
            if has_eight_legs == 'yes':
                organism_classification = 'Arachnid'
            else:
                organism_classification = 'Crustacean'
    else:
        segmented_body = input('Does it have a segmented body? (yes/no): ').strip().lower()
        if segmented_body == 'yes':
            organism_classification = 'Annelid (e.g., Earthworm)'
        else:
            has_shell = input('Does it have a shell? (yes/no): ').strip().lower()
            if has_shell == 'yes':
                organism_classification = 'Snail or Clam'
            else:
                organism_classification = 'Octopus or Squid'

print(f'It is a {organism_classification}.')
