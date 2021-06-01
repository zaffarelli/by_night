from django.http import JsonResponse
from storytelling.models.stories import Story
import json


def display_storytelling(request):
    all = Story.objects.all()
    all_stories = []
    settings = {}
    selected_story = None
    for s in all:
        if s.is_current:
            all_stories.append(s.toJSON())
            selected_story = s
    settings_json = json.dumps(settings, sort_keys=True, indent=4)
    places_json = json.dumps(selected_story.all_places, sort_keys=True, indent=4)
    scenes_json = json.dumps(selected_story.all_scenes, sort_keys=True, indent=4)
    data = {'story': selected_story.toJSON(), 'end_time': selected_story.story_end_time, 'places': places_json, 'scenes': scenes_json}
    data_json = json.dumps(data, sort_keys=True, indent=4)
    answer = {'data': data_json, 'settings': settings_json}
    return JsonResponse(answer)

