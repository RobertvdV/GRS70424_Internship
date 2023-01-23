import json
import matplotlib.colors as mcolors

colors = [color[4:] for color in mcolors.TABLEAU_COLORS.keys()]
colors.extend([color for color in mcolors.CSS4_COLORS.keys()])
colors.extend(
    [
        'whitish', 'bluish', 'reddish', 'greenish', 'backish', 'greyish',
        'backish', 'purplish', 'yellowish', 'orangish', 'brownish', 'pinkish'
    ]
)

traits_dict = {
    'Life Form':
    [
        'Tree', 'Shrub', 'Bush', 'Ficus', 'Strangler', 'Liana', 'Parasitic', 'Palm', 'Herbaceous'
    ],
    'Trunk':
    [
        'Trunk', 'Straight', 'Flared', 'Foothills', 'Silt', 'Aerial'
    ],
    'Root':
    [
        'Root', 'Straight', 'Flared', 'Foothills', 'Silt', 'Aerial'
    ],
    'Latex':
    [
        'Latex'
    ],
    'Phyllotaxis': # Leaf Position
    [
        'Phyllotaxis', 'Alternate', 'Whorled', 'Whorls', 'Opposite'
    ],
    'Leaf Composition':
    [
        'Palmate', 'Pinnate', 'Entire', 'Bi-pinnate'
    ],
    'Crown':
    [
        'Crown'
    ],
    'Stem':
    [
        'Stem', 'Circular', 'Square'
    ],
    'Bark':
    [
        'Bark'
    ],
    'Bark Colour':
    [
        'Bark'
    ],
    'Leaf Shape':
    [
        'Simple', 'Bifoliate', 'Trifoliate', 'Digitized', 'Paripinnate', 'Unipinnate', 'Imperipinnate', 
        'Alternate', 'Bipinnate', 'Pinnate', 'Elliptic', 'Elongate', 'Ovate', 'Round', 'Obovate', 'Lanceolate',
        'Kidney-shaped', 'Heart-shaped', 'Spathulate'
    ],
    'Petiole':
    [
        'Petiole', 'Sessile', 'Petiolated', 'Canaliculate', 'Glands', 'Glandular', 
    'Winged' 'Wings', 'Hairs', 'Hair', 'Translucent'
    ],
    'Leaf Colour':
    [
        'Leaf Colour', 'Leaf Color'
    ],
    'Leaf Blade':
    [
        'Leaf Blade', 'Linear', 'Lanceolate', 'Elliptical', 'Obovate', 'Obtriangular', 
        'Obtriangular', 'Asymmetrical', 'Orbicular', 'Bilobed', 'Lobed', 'Lobes', 'Lobe'
    ],
    'Leaf Base':
    [
        'Leaf Base', 'Rounded', 'Cordate', 'Glands'
    ],
    'Leaf Margin':
    [
        'Margin', 'Smooth', 'Wavy', 'Crenate', 'Toothed', 'Teeth', 'Crenate', 'Serrate'
    ],
    'Leaf Apex':
    [
        'Apex', 'Acuminate', 'Apiculate', 'Mucronate', 'Rounded', 'Emarginated'
    ],
    'Leaf side':
    [
        'Glabrous', 'Pubescent', 'Salt Crystals', 'Scales', 'Woolly', 'Powdery'
    ],
    'Leaf glands':
    [
        'Glands', 'Gland', 'Translucent'
    ],
    'Rachis':
    [
        'Rachis', 'Winged'
    ],
    'Vein':
    [
        'Vein'
    ],
    'Tendril':
    [
        'Tendril'
    ],
    'Spine':
    [
        'Spine', 'Prickle', 'Spines', 'Prickles'
    ],
    'Thornes':
    [
        'Thorn', 'Thornes'
    ],
    'Blade Colour':
    [
        'Blade'
    ],
    'Fruit':
    [
        'Drupe', 'Berry', 'Capsule', 'Pod', 'Follicle', 'Achene', 'Winged', 'Follicle',
        'Pod', 'Nutlet', 'Fruit'
    ],
    'Fruit Shape':
    [
        'locular', 'Globose', 'Flattened', 'Elongate', 'Obovoid', 'Ovate', 'Twisted',
        'Curved', 'Pyriform', 'Ovoid'
    ],
    'Fruit Colour':
    [
        'Fruit'
    ],
    'Inflorescences':
    [
        'Inflorescences', 'Inflorescence', 'Sessile', 'Panicle', 'Flower head', 'Cyme', 'Glomerule', 
        'Fascicle', 'Umbel', 'Corymb', 'Rootlet', 'Spike', 'Dichasium', 'Fascicle',
        'Globose', 'Raceme', 'Fascicle', 'Umbel'
    ],
    'Sexuality':
    [
        'Sexuality', 'Axillary', 'Terminal'
    ],
    'Flower Colour':
    [
        'Flower colour', 'Flower color', 'Flower', 'Flowers'
    ],
    'Flower Shape':
    [
        'Flower shape', 'Petalled', 'Petal', 'Petals', 'Tubular', 'Apetal', 'Butterfly-shaped', 'Shaped', 'Flower', 'Flowers'
    ],
    'Sepal Shape':
    [
        'Sepal', 'Sepals', 'Connate'
    ],
    'Petal Shape':
    [
        'Petal', 'Petals', 'Tepals', 'Tepal', 'Tubular'
    ],
    'Aril Colour':
    [
        'Aril'
    ],
    'Seed Colour':
    [
        'Seed', 
    ],
    'Conspicuousness':
    [
        'Conspicuousness', 'Cryptic', 'Inconspicuous', 'Conspicuous'
    ]
}

with open('../../data/supportive/trait_dictionary.json', 'w') as f:
    json.dump(traits_dict, f)
with open('../../data/supportive/colour_list.json', 'w') as f:
    json.dump(colors, f)
