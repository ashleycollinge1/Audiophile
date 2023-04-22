import mutagen
from mutagen.flac import *
from pydoc import locate

#test_ogg_file = mutagen.File("501-belinda_carlisle-heaven_is_a_place_on_earth.flac")

#print(type(test_ogg_file))

#if isinstance(test_ogg_file, locate('mutagen.flac.FLAC')):
    #print('FLAC file')

# We want to get the file and determine what type of file it is, so we can use the correct
# class from mutagen, so regardless of type of file, if mutagen supports it, we can support it
# but we don't want to be writing an if statement for every type of file [Langford Method]

#FLAC_file = mutagen.flac.FLAC("501-belinda_carlisle-heaven_is_a_place_on_earth.flac")
#print(FLAC_file.tags)

def fullname(o):
    """
    Provides the full class name of the passed variable, o
    """
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__ # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__

# create generic 'file' class from mutagen and use it on our audio file
generic_file = mutagen.File("501-belinda_carlisle-heaven_is_a_place_on_earth.flac")
print("FileName:", "501-belinda_carlisle-heaven_is_a_place_on_earth.flac")
# using the fullname function we get the full name of the class being used, which
# tells us the type of audio file we're dealing with. we can then create a new instance
# of the correct type to make sure we get all the details we can i.e.
# FLAC files use: mutagen.flac.FLAC
file_type_class = fullname(generic_file)
print("File Type: ", file_type_class)
# create a new instance of the correct class of mutagen we need to get the correct details
new_class = locate(file_type_class)
# use the new class with the audio file
audio_file = new_class("501-belinda_carlisle-heaven_is_a_place_on_earth.flac")
# access attributes of the class, below printing the tags i.e.
# track number, title, artist, date, media, encoder, genre, organisation, album, album artist
print("Tags: ", audio_file.tags)

# there's a lot more information we can use mutagen to get out of the audio files before
# moving on to any other method of gaining metadata
