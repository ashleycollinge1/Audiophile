"""

"""

import mutagen
from mutagen.flac import FLAC

test_ogg_file = mutagen.File("11. The Way It Is.ogg")

if isinstance(test_ogg_file) == 'mutagen.flac.FLAC':
    print('FLAC file')
