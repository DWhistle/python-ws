from collections import namedtuple

EMPTY_STRING = ''
VIDEO_REQUIRED_FIELDS = {'id', 'uploader', 'uploader_id', 'uploader_url',
                         'channel_id', 'channel_url', 'upload_date',
                         'license', 'creator', 'title', 'alt_title',
                         'thumbnail', 'description', 'categories', 'tags', 'ext'}

_LevelsEnum = namedtuple('PRIVACY_LEVELS', 'private, public, unlisted')
PRIVACY_LEVELS = _LevelsEnum('private', 'public', 'unlisted')

YOUTUBE_CATEGORIES = {'Film & Animation': 1, 'Autos & Vehicles': 2, 'Music': 10, 'Pets & Animals': 15, 'Sports': 17,
                      'Short Movies': 18, 'Travel & Events': 19, 'Gaming': 20, 'Videoblogging': 21,
                      'People & Blogs': 22, 'Comedy': 34, 'Entertainment': 24, 'News & Politics': 25,
                      'Howto & Style': 26, 'Education': 27, 'Science & Technology': 28, 'Movies': 30,
                      'Anime/Animation': 31, 'Action/Adventure': 32, 'Classics': 33, 'Documentary': 35, 'Drama': 36,
                      'Family': 37, 'Foreign': 38, 'Horror': 39, 'Sci-Fi/Fantasy': 40, 'Thriller': 41, 'Shorts': 42,
                      'Shows': 43, 'Trailers': 44}
ENTERTAINMENT_CATEGORY = 24

POSSIBLE_VIDEO_FORMATS = {".webm", ".mp4", ".avi", ".mkv"}
