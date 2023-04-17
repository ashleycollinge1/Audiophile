# Workflows

Describe what you want to happen, so we can work on what we need to do to achieve it.

## Importing music from a local import folder (drag music files into it)
* Music copied to the import folder should import automatically.
* Music will be deleted from the import folder once it's been successfully imported, and moved
to a different directory (Library).
* Once imported the files will be placed in to a folder structure like this: Artist > Album > Tracks

1. Users copies/moves music into the import folder.
2. Scan for files and do the following for each file found:
    1. Using metadata, the filename, and any folder structure, to get the below information:
        * Artist Name
        * Album Name
        * Track Name
        Use pythonmutagen to extract the tags from the audio files, example from a FLAC I downloaded:

        >>> import mutagen
        >>> from mutagen.flac import FLAC

        >>> a = FLAC('216-limahl-never_ending_story.flac')
        >>> a.tags
        [('Language', 'English'), ('TRACKNUMBER', '16'), ('Artist', 'Limahl'), ('Title', 'Never Ending Story'), ('Rip Date', '2022-07-04'), ('Date', '2008'), ('Retail Date', '2008-00-00'), ('Media', 'CD'), ('Encoded By', '.:WRE:.'), ('Supplier', '.:WRE:.'), ('Encoder', 'FLAC 1.3.1'), ('Ripping Tool', 'EAC'), ('Release Type', 'Retail'), ('Genre', 'Pop'), ('Catalog', '2646852'), ('ORGANIZATION', 'EMI'), ('Album', '101 80s Hits'), ('Album Artist', 'VA')]
    2. Create a new folder inside the main Library folder, for the Album, and put the tracks inside the folder. Save the folder for the album, and each individual track to the DB. Each track should be named 000-artist-track_name.ext
    3. 
    4. Delete the tracks and associated folders from the import folder