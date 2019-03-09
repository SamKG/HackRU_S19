import json
import os
import sys

import app.cli
import app.formats as formats
import app.twitch as twitch


def draw_progress(current: float, end: float, description: str = 'Downloading'):
    sys.stdout.write('[{}] {}%\r'.format(description, '%.2f' % min(current * 10 / end * 10, 100.00)))
    sys.stdout.flush()


def download_multiple_formats():
    pass


def download(video_id: str, format_name: str) -> str:
    if app.cli.arguments.verbose:
        print('Downloading {} initialized'.format(format_name))

    # Get Video
    video: twitch.Video = twitch.Video(video_id)

    # Format video comments and output
    lines, output = formats.use(format_name, video)

    sys.stderr.write(repr(list(map(lambda a:a[0], lines))))

    return output
