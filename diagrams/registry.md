# Реестр схем

Обновляется командой `python registry.py` (и автоматически в конце `build_lesson.py`). Руками не править.

Всего схем: **41**, из них пересобираются скриптом: **32**, заморожены: **9**. Уроков: **6**. Дата: 2026-11-21.

## lesson_39

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `01_group_by_hair.excalidraw` | 82 | 0 | 968 × 759 | да | 1. GROUP BY hair — один признак |
| `02_group_by_hair_eye.excalidraw` | 85 | 6 | 852 × 875 | да | 2. GROUP BY hair, eye — два признака |

Исходники (архив, не пересобираются):

| файл | эл. | размер, px | о чём |
|---|---|---|---|
| `_source/group_by.excalidraw` | 40 | 1749 × 977 | GROUP BY |
| `_source/group_by_v2.excalidraw` | 135 | 1970 × 960 | GROUP BY: как строки собираются в группы |
| `_source/group_by_v3.excalidraw` | 131 | 1930 × 870 | GROUP BY: как строки разбредаются по группам |

## lesson_40

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `00_map.excalidraw` | 39 | 5 | 1288 × 651 | да | Занятие 40: связи между таблицами |
| `01_pk.excalidraw` | 64 | 4 | 980 × 553 | да | 1. Первичный ключ |
| `02_fk_o2m.excalidraw` | 59 | 3 | 853 × 623 | да | 2. Внешний ключ и связь «один ко многим» |
| `03_o2o.excalidraw` | 51 | 1 | 930 × 475 | да | 3. Связь «один к одному» |
| `04_m2m.excalidraw` | 68 | 6 | 853 × 521 | да | 4. Связь «многие ко многим» |
| `05_join_o2m.excalidraw` | 88 | 3 | 1006 × 757 | да | 5. JOIN по внешнему ключу |
| `06_join_m2m.excalidraw` | 97 | 6 | 966 × 753 | да | 6. JOIN через связку |

Исходники (архив, не пересобираются):

| файл | эл. | размер, px | о чём |
|---|---|---|---|
| `_source/sql_relationships.excalidraw` | 156 | 3004 × 5540 | 1. Пояснения первичного ключа |
| `_source/sql_relationships_v2.excalidraw` | 267 | 2093 × 1101 | Связи между таблицами: одна запись — одна ссылка |

## lesson_41

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `00_map.excalidraw` | 39 | 5 | 1307 × 655 | **нет** | Занятие 41: типы JOIN в SQLite |
| `01_inner.excalidraw` | 99 | 3 | 1239 × 675 | **нет** | 1. JOIN — остаются только пары |
| `02_left.excalidraw` | 103 | 4 | 1239 × 706 | **нет** | 2. LEFT JOIN — остаются все книги |
| `03_right.excalidraw` | 103 | 4 | 1303 × 706 | **нет** | 3. RIGHT JOIN — остаются все авторы |
| `04_full.excalidraw` | 107 | 3 | 1303 × 740 | **нет** | 4. FULL OUTER JOIN — остаётся всё |
| `05_cross.excalidraw` | 112 | 0 | 1139 × 853 | **нет** | 5. CROSS JOIN — каждая с каждой |
| `06_natural.excalidraw` | 123 | 3 | 1333 × 792 | **нет** | 6. NATURAL JOIN — соединение по именам |

## lesson_42

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `00_map.excalidraw` | 47 | 0 | 1150 × 745 | да | Оконные функции: карта занятия |
| `01_groupby_loses_rows.excalidraw` | 75 | 3 | 1012 × 744 | да | 1. Почему GROUP BY не хватает |
| `02_over_partition.excalidraw` | 88 | 0 | 1168 × 590 | да | 2. OVER (PARTITION BY): строки остаются |
| `03_over_empty.excalidraw` | 80 | 0 | 1244 × 606 | да | 3. OVER () без PARTITION: окно — вся таблица |
| `04_two_windows.excalidraw` | 84 | 0 | 1282 × 666 | да | 4. Два окна в одном запросе |
| `05_count_by_eye.excalidraw` | 91 | 0 | 1181 × 684 | да | 5. Окно как «сколько нас» |
| `06_running_total.excalidraw` | 83 | 0 | 1067 × 689 | да | 6. Нарастающий итог: ORDER BY внутри OVER |
| `07_ranks.excalidraw` | 95 | 0 | 1246 × 748 | да | 7. Ранги: три функции на одних данных |
| `08_top_per_group.excalidraw` | 112 | 0 | 1206 × 822 | да | 8. Топ в каждой группе |
| `09_lag_lead.excalidraw` | 75 | 0 | 1252 × 606 | да | 9. LAG и LEAD: сосед сверху и сосед снизу |

## lesson_44

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `01_why_catalog.excalidraw` | 59 | 0 | 860 × 800 | да | 1. Почему категория не живёт в каждом посте |
| `02_catalog_o2m.excalidraw` | 91 | 3 | 935 × 763 | да | 2. Справочник и внешний ключ: «один ко многим» |
| `03_declared_vs_works.excalidraw` | 70 | 0 | 1200 × 609 | да | 3. REFERENCES объявляет связь, а проверяет её — соединение |
| `04_delete_modes.excalidraw` | 131 | 0 | 1255 × 812 | да | 4. Один DELETE — три разных исхода |
| `05_join_result.excalidraw` | 87 | 3 | 920 × 836 | да | 5. Как получается строка ответа |
| `06_join_defaults.excalidraw` | 164 | 9 | 1163 × 787 | да | 6. JOIN по умолчанию, LEFT и OUTER |
| `07_join_rest.excalidraw` | 107 | 3 | 864 × 781 | да | 7. RIGHT JOIN и CROSS JOIN |
| `1.excalidraw` | 47 | 4 | 1651 × 1928 | **нет** | content |

Исходники (архив, не пересобираются):

| файл | эл. | размер, px | о чём |
|---|---|---|---|
| `_source/05_join_types_v1.excalidraw` | 117 | 1150 × 753 | 5. Пять JOIN на одних данных |

## lesson_45

| файл | эл. | стрелок | размер, px | скрипт | о чём |
|---|---|---|---|---|---|
| `01_junction_structure.excalidraw` | 73 | 2 | 976 × 744 | да | 1. Из чего состоит таблица пар |
| `02_many_to_many.excalidraw` | 108 | 5 | 1100 × 696 | да | 2. Многие ко многим: таблица пар |
| `03_cascade.excalidraw` | 109 | 3 | 1120 × 721 | да | 3. Каскад: пара уходит вместе с постом или тегом |
| `04_two_joins.excalidraw` | 173 | 3 | 1232 × 887 | да | 4. Два JOIN: три таблицы и выдача |
| `05_group_concat.excalidraw` | 163 | 4 | 1232 × 881 | да | 5. GROUP BY: одна строка на пост |
| `06_site_query.excalidraw` | 202 | 5 | 1129 × 837 | да | 6. Три JOIN: категория и теги для страницы сайта |
| `1.excalidraw` | 25 | 2 | 1122 × 282 | **нет** | posts_hashtags |

## Требуют скриптов

Эти файлы сделаны разовыми скриптами и правятся только вручную:

* `lesson_41/00_map.excalidraw`
* `lesson_41/01_inner.excalidraw`
* `lesson_41/02_left.excalidraw`
* `lesson_41/03_right.excalidraw`
* `lesson_41/04_full.excalidraw`
* `lesson_41/05_cross.excalidraw`
* `lesson_41/06_natural.excalidraw`
* `lesson_44/1.excalidraw`
* `lesson_45/1.excalidraw`

Чтобы пересобрать: `cp -r _template <урок>` → данные в `data.py` → скрипт на `blocks.py` → `python build_lesson.py <урок>`.
