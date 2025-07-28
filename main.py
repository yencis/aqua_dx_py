from src.mai2.music.search import MusicSearch
from src.game.game import get_summary
from src.types import Game
from src.mai2.mai2 import get_ratings, view_rating_play, view_recent_score, get_maimai_summary, get_maimai_user_card

import inspect

# card = card_ops.get_user_card("uencis")
# print(card_ops.get_game_card(card, "mai2"))

# with open("test.json") as f:
#     j = json.load(f)
#     print(j)
#     x = RecentScore.model_validate(j)
#     print(x)

# ms = MusicSearch()
# summary = get_summary("uencis", Game.MAI2)
# # # print(len(summary.recent))
# # # print(get_rating(0.224, 100700, 13.9))
# ratings_15, ratings_35 = get_ratings(summary)
# print([view_rating_play(p, ms) for p in ratings_15])
# print([view_recent_score(r, ms) for r in summary.recent])

print(get_maimai_user_card("uencis"))

# i_s = ImageSearch()
# img_url = i_s.get_image_url("111234")
# response = requests.get(img_url)
# print(response, img_url)
# with open("image.png", "wb") as f:
#     f.write(response.content)


# response = requests.post(API_ENDPOINT+"game/mai2/user-summary?username=uencis", json={'username': 'uencis'})
# print(response.json())

# def yield_after_time():
#     for i in range(2):
#         time.sleep(2)
#         yield 8
#
#
# def return_after_secs(secs: int):
#     time.sleep(secs)
#     return f"Slept for {str(secs)} seconds"
#
#
# with ThreadPoolExecutor(max_workers=4) as executor:
#     futures = {executor.submit(return_after_secs, seconds): seconds for seconds in [6,4,6,8,8]}
#     for future in as_completed(futures):
#         seconds = futures[future]
#         try:
#             data = future.result()
#         except Exception as e:
#             print("Exception! %s", e)
#         else:
#             print(data)
#     print("All done")

# class NoTitle(GenerateJsonSchema):
#     def field_title_should_be_set(self, schema):
#         return False
#
#     def default_schema(self, schema):
#         return self.generate_inner(schema['schema'])
#
#
# x = Song.model_json_schema(schema_generator=NoTitle)
#
# print({'properties': x["properties"]})