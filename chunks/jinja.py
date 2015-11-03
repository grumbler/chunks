# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import jinja2

from .templatetags.chunks import CACHE_PREFIX, Chunk, cache


def get_chunk(key_name, cache_time=0):
    try:
        cache_key = CACHE_PREFIX + key_name
        c = cache.get(cache_key)
        if c is None:
            c = Chunk.objects.get(key=key_name)
            cache.set(cache_key, c, int(cache_time))
        content = c.content
    except Chunk.DoesNotExist:
        content = ''
    return jinja2.Markup(content)
