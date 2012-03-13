"""This module contains models used in malconstrict."""


class Anime(object):
    """Model that representes an Anime object."""
    def __init__(self):
        self.id = None
        self.title = None
        self.other_titles = None
        self.rank = None
        self.popularity_rank = None
        self.image_url = None
        self.type = None
        self.episodes = None
        self.status = None
        self.classification = None
        self.members_score = None
        self.members_count = None
        self.favorited_count = None
        self.synopsis = None
        self.genres = None
        self.tags = None
        self.manga_adaptations = None
        self.prequels = None
        self.sequels = None
        self.side_stories = None
        self.watched_status = None
        self.watched_episodes = None
        self.score = None


class Manga(object):
    """Model that represents a Manga object."""
    def __init__(self):
        self.id = None
        self.title = None
        self.other_titles = None
        self.rank = None
        self.popularity_rank = None
        self.image_url = None
        self.type = None
        self.chapters = None
        self.volumes = None
        self.status = None
        self.classification = None
        self.members_score = None
        self.members_count = None
        self.favorited_count = None
        self.synopsis = None
        self.genres = None
        self.tags = None
        self.anime_adaptations = None
        self.related_manga = None
        self.read_status = None
        self.chapters_read = None
        self.volumes_read = None
        self.score = None


class AnimeList(object):
    """Model that represents an AnimeList object."""
    def __init__(self):
        self.anime = None
        self.statistics = None


class MangaList(object):
    """Model that represents an MangaList object."""
    def __init__(self):
        self.manga = None
