from lib.music import *
import pytest

# Tests for __init__
def test_object_is_set_up_with_empty_list():
    music = MusicTracker()
    assert music.tracks == []

# Tests for add
"""Test adding a track and make sure the list of tracks
is updated"""
def test_add_track_and_list_updated():
    music = MusicTracker()
    music.add('Nirvana', 'Smells Like Teen Spirit')
    assert music.tracks == [ ('Nirvana', 'Smells Like Teen Spirit') ]


"""Test adding multiple tracks to make sure list is
updated with both and it doesn't overwrite"""
def test_add_multiple_tracks_make_sure_list_updated():
    music = MusicTracker()
    music.add('Nirvana', 'Smells Like Teen Spirit')
    music.add('The Beatles', 'Scream and Shout')
    assert music.tracks == [ 
        ('Nirvana', 'Smells Like Teen Spirit'),
        ('The Beatles', 'Scream and Shout'), ]


"""Test add() without adding title and song as empty string"""
def test_add_with_empty_strings():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.add('', '')
    assert str(e.value) == "Artist of song can't be empty"


# Tests for list_tracks
def test_list_tracks_with_one_track_should_by_only_thing_listed():
    music = MusicTracker()
    music.add('Nirvana', 'Smells Like Teen Spirit')
    result = music.list_tracks()
    assert result == 'Nirvana: Smells Like Teen Spirit'


"""Test adding multiple tracks and then listing them
to make sure they are all listed"""
def test_list_tracks_for_multiple_adds_returns_all():
    music = MusicTracker()
    music.add('Nirvana', 'Smells Like Teen Spirit')
    music.add('The Beatles', 'Scream and Shout')
    music.add('Pearl Jam', 'Alive')
    result = music.list_tracks()
    assert result == 'Nirvana: Smells Like Teen Spirit\nThe Beatles: Scream and Shout\nPearl Jam: Alive'


"""Test when list tracks is called and no tracks have been added
should raise error"""
def test_list_tracks_when_no_tracks_have_been_added():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.list_tracks()
    assert str(e.value) == "No tracks have been added yet"



