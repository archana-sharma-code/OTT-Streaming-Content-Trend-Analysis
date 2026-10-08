# OTT Streaming Content Analysis - SQL Query Output

Source: netflix_titles.csv (8,807 rows) + amazon_prime_titles.csv (9,668 rows) combined into `content_library` (17,475 rows).
Engine: SQLite (MySQL functions emulated).

## QUERY 1: Content Count by Platform and Type
(4 rows)

| platform     | type    |   total_titles |   percentage |
|:-------------|:--------|---------------:|-------------:|
| Amazon Prime | TV Show |           1854 |        19.18 |
| Amazon Prime | Movie   |           7814 |        80.82 |
| Netflix      | TV Show |           2676 |        30.38 |
| Netflix      | Movie   |           6131 |        69.62 |

## QUERY 2: Top 10 Most Common Genres
(10 rows)

| genre                  |   count |
|:-----------------------|--------:|
| Drama                  |    3687 |
| International Movies   |    2752 |
| Dramas                 |    2427 |
| Comedy                 |    2099 |
| Comedies               |    1674 |
| Action                 |    1657 |
| Suspense               |    1501 |
| International TV Shows |    1351 |
| Kids                   |    1085 |
| Documentary            |     993 |

## QUERY 3: Content Rating Distribution by Platform
(41 rows)

| platform     | rating   |   title_count |   percentage |
|:-------------|:---------|--------------:|-------------:|
| Amazon Prime | 13+      |          2117 |        22.69 |
| Amazon Prime | 16+      |          1547 |        16.58 |
| Amazon Prime | ALL      |          1268 |        13.59 |
| Amazon Prime | 18+      |          1243 |        13.32 |
| Amazon Prime | R        |          1010 |        10.82 |
| Amazon Prime | PG-13    |           393 |         4.21 |
| Amazon Prime | 7+       |           385 |         4.13 |
| Amazon Prime | PG       |           253 |         2.71 |
| Amazon Prime | NR       |           223 |         2.39 |
| Amazon Prime | TV-14    |           208 |         2.23 |
| Amazon Prime | TV-PG    |           169 |         1.81 |
| Amazon Prime | TV-NR    |           105 |         1.13 |
| Amazon Prime | G        |            93 |         1    |
| Amazon Prime | TV-G     |            81 |         0.87 |
| Amazon Prime | TV-MA    |            77 |         0.83 |
| Amazon Prime | TV-Y     |            74 |         0.79 |
| Amazon Prime | TV-Y7    |            39 |         0.42 |
| Amazon Prime | UNRATED  |            33 |         0.35 |
| Amazon Prime | AGES_18_ |             3 |         0.03 |
| Amazon Prime | NC-17    |             3 |         0.03 |
| Amazon Prime | NOT_RATE |             3 |         0.03 |
| Amazon Prime | AGES_16_ |             2 |         0.02 |
| Amazon Prime | 16       |             1 |         0.01 |
| Amazon Prime | ALL_AGES |             1 |         0.01 |
| Netflix      | TV-MA    |          3207 |        36.43 |
| Netflix      | TV-14    |          2160 |        24.54 |
| Netflix      | TV-PG    |           863 |         9.8  |
| Netflix      | R        |           799 |         9.08 |
| Netflix      | PG-13    |           490 |         5.57 |
| Netflix      | TV-Y7    |           334 |         3.79 |
| Netflix      | TV-Y     |           307 |         3.49 |
| Netflix      | PG       |           287 |         3.26 |
| Netflix      | TV-G     |           220 |         2.5  |
| Netflix      | NR       |            80 |         0.91 |
| Netflix      | G        |            41 |         0.47 |
| Netflix      | TV-Y7-FV |             6 |         0.07 |
| Netflix      | NC-17    |             3 |         0.03 |
| Netflix      | UR       |             3 |         0.03 |
| Netflix      | 66 min   |             1 |         0.01 |
| Netflix      | 74 min   |             1 |         0.01 |
| Netflix      | 84 min   |             1 |         0.01 |

## QUERY 4: Content Release Trends by Year and Platform
(24 rows)

|   release_year | platform     |   titles_released |
|---------------:|:-------------|------------------:|
|           2021 | Amazon Prime |              1442 |
|           2021 | Netflix      |               592 |
|           2020 | Amazon Prime |               962 |
|           2020 | Netflix      |               953 |
|           2019 | Amazon Prime |               929 |
|           2019 | Netflix      |              1030 |
|           2018 | Amazon Prime |               623 |
|           2018 | Netflix      |              1147 |
|           2017 | Amazon Prime |               562 |
|           2017 | Netflix      |              1032 |
|           2016 | Amazon Prime |               521 |
|           2016 | Netflix      |               902 |
|           2015 | Amazon Prime |               378 |
|           2015 | Netflix      |               560 |
|           2014 | Amazon Prime |               391 |
|           2014 | Netflix      |               352 |
|           2013 | Amazon Prime |               289 |
|           2013 | Netflix      |               288 |
|           2012 | Amazon Prime |               252 |
|           2012 | Netflix      |               237 |
|           2011 | Amazon Prime |               252 |
|           2011 | Netflix      |               185 |
|           2010 | Amazon Prime |               186 |
|           2010 | Netflix      |               194 |

## QUERY 5: Top 10 Countries by Content Production
(10 rows)

| country        |   total_titles |   platforms_available |
|:---------------|---------------:|----------------------:|
| United States  |           3071 |                     2 |
| India          |           1201 |                     2 |
| United Kingdom |            447 |                     2 |
| Japan          |            247 |                     2 |
| South Korea    |            199 |                     1 |
| Canada         |            197 |                     2 |
| Spain          |            153 |                     2 |
| France         |            127 |                     2 |
| Mexico         |            112 |                     2 |
| Egypt          |            107 |                     2 |

## QUERY 6a: Average Movie Duration (minutes)
(2 rows)

| platform     |   avg_duration_minutes |   min_duration |   max_duration |
|:-------------|-----------------------:|---------------:|---------------:|
| Amazon Prime |                91.3119 |              0 |            601 |
| Netflix      |                99.5772 |              3 |            312 |

## QUERY 6b: Average TV Show Seasons
(2 rows)

| platform     |   avg_seasons |   min_seasons |   max_seasons |
|:-------------|--------------:|--------------:|--------------:|
| Amazon Prime |       1.7233  |             1 |            29 |
| Netflix      |       1.76495 |             1 |            17 |

## QUERY 7: Genre Analysis by Release Year (2015+)
(456 rows)

|   release_year | genre                        |   title_count |
|---------------:|:-----------------------------|--------------:|
|           2021 | Drama                        |           592 |
|           2021 | Suspense                     |           285 |
|           2021 | Action                       |           262 |
|           2021 | Comedy                       |           259 |
|           2021 | Horror                       |           227 |
|           2021 | Kids                         |           170 |
|           2021 | International TV Shows       |           149 |
|           2021 | Romance                      |           144 |
|           2021 | International Movies         |           141 |
|           2021 | Animation                    |           117 |
|           2021 | Dramas                       |            92 |
|           2021 | Science Fiction              |            86 |
|           2021 | TV Dramas                    |            83 |
|           2021 | Documentary                  |            81 |
|           2021 | TV Comedies                  |            72 |
|           2021 | Comedies                     |            70 |
|           2021 | Special Interest             |            58 |
|           2021 | Docuseries                   |            57 |
|           2021 | Documentaries                |            53 |
|           2021 | Crime TV Shows               |            47 |
|           2021 | Reality TV                   |            44 |
|           2021 | Kids' TV                     |            44 |
|           2021 | Children & Family Movies     |            40 |
|           2021 | and Culture                  |            39 |
|           2021 | Entertainment                |            39 |
|           2021 | Arts                         |            39 |
|           2021 | Sports                       |            38 |
|           2021 | Action & Adventure           |            37 |
|           2021 | Thrillers                    |            33 |
|           2021 | TV Shows                     |            33 |
|           2021 | Spanish-Language TV Shows    |            32 |
|           2021 | Romantic TV Shows            |            32 |
|           2021 | TV Action & Adventure        |            28 |
|           2021 | Romantic Movies              |            25 |
|           2021 | Unscripted                   |            23 |
|           2021 | Anime Series                 |            23 |
|           2021 | Horror Movies                |            20 |
|           2021 | Music & Musicals             |            19 |
|           2021 | British TV Shows             |            17 |
|           2021 | Arthouse                     |            17 |
|           2021 | Independent Movies           |            16 |
|           2021 | Sports Movies                |            15 |
|           2021 | TV Sci-Fi & Fantasy          |            14 |
|           2021 | TV Mysteries                 |            14 |
|           2021 | Music Videos and Concerts    |            13 |
|           2021 | LGBTQ                        |            13 |
|           2021 | Stand-Up Comedy              |            12 |
|           2021 | Young Adult Audience         |            11 |
|           2021 | Western                      |            11 |
|           2021 | TV Horror                    |            10 |
|           2021 | Science & Nature TV          |            10 |
|           2021 | TV Thrillers                 |             9 |
|           2021 | Anime                        |             9 |
|           2021 | Teen TV Shows                |             8 |
|           2021 | LGBTQ Movies                 |             8 |
|           2021 | International                |             8 |
|           2021 | Stand-Up Comedy & Talk Shows |             7 |
|           2021 | Anime Features               |             6 |
|           2021 | Talk Show and Variety        |             4 |
|           2021 | Movies                       |             4 |
|           2021 | Korean TV Shows              |             4 |
|           2021 | Adventure                    |             4 |
|           2021 | Fantasy                      |             3 |
|           2020 | Drama                        |           361 |
|           2020 | International Movies         |           239 |
|           2020 | International TV Shows       |           214 |
|           2020 | Comedy                       |           199 |
|           2020 | Dramas                       |           195 |
|           2020 | Suspense                     |           164 |
|           2020 | Kids                         |           154 |
|           2020 | Action                       |           150 |
|           2020 | Comedies                     |           133 |
|           2020 | TV Dramas                    |           127 |
|           2020 | Documentary                  |           117 |
|           2020 | TV Comedies                  |           105 |
|           2020 | Special Interest             |            88 |
|           2020 | Crime TV Shows               |            87 |
|           2020 | Children & Family Movies     |            83 |
|           2020 | Horror                       |            80 |
|           2020 | Documentaries                |            77 |
|           2020 | Docuseries                   |            74 |
|           2020 | Romance                      |            71 |
|           2020 | Animation                    |            71 |
|           2020 | Kids' TV                     |            63 |
|           2020 | Romantic Movies              |            61 |
|           2020 | Reality TV                   |            55 |
|           2020 | Science Fiction              |            52 |
|           2020 | Romantic TV Shows            |            46 |
|           2020 | Independent Movies           |            46 |
|           2020 | Action & Adventure           |            46 |
|           2020 | Thrillers                    |            45 |
|           2020 | and Culture                  |            41 |
|           2020 | Stand-Up Comedy              |            41 |
|           2020 | Entertainment                |            41 |
|           2020 | Arts                         |            41 |
|           2020 | Music & Musicals             |            37 |
|           2020 | British TV Shows             |            33 |
|           2020 | TV Action & Adventure        |            32 |
|           2020 | Horror Movies                |            29 |
|           2020 | Spanish-Language TV Shows    |            28 |
|           2020 | TV Mysteries                 |            27 |
|           2020 | LGBTQ                        |            23 |
|           2020 | International                |            21 |
|           2020 | Anime Series                 |            21 |
|           2020 | TV Shows                     |            19 |
|           2020 | TV Sci-Fi & Fantasy          |            19 |
|           2020 | Sports                       |            19 |
|           2020 | TV Horror                    |            17 |
|           2020 | Sports Movies                |            17 |
|           2020 | LGBTQ Movies                 |            17 |
|           2020 | Korean TV Shows              |            17 |
|           2020 | Arthouse                     |            17 |
|           2020 | Adventure                    |            16 |
|           2020 | Science & Nature TV          |            15 |
|           2020 | Unscripted                   |            14 |
|           2020 | Teen TV Shows                |            11 |
|           2020 | Young Adult Audience         |             9 |
|           2020 | Fitness                      |             9 |
|           2020 | Faith and Spirituality       |             9 |
|           2020 | Talk Show and Variety        |             8 |
|           2020 | TV Thrillers                 |             7 |
|           2020 | Stand-Up Comedy & Talk Shows |             7 |
|           2020 | Music Videos and Concerts    |             7 |
|           2020 | Faith & Spirituality         |             5 |
|           2020 | Western                      |             4 |
|           2020 | Historical                   |             4 |
|           2020 | Fantasy                      |             4 |
|           2020 | Classic & Cult TV            |             3 |
|           2020 | Anime Features               |             3 |
|           2020 | Anime                        |             3 |
|           2019 | International Movies         |           282 |
|           2019 | Drama                        |           275 |
|           2019 | Dramas                       |           243 |
|           2019 | Kids                         |           205 |
|           2019 | International TV Shows       |           201 |
|           2019 | Comedy                       |           177 |
|           2019 | Comedies                     |           159 |
|           2019 | Action                       |           143 |
|           2019 | TV Dramas                    |           133 |
|           2019 | Special Interest             |           114 |
|           2019 | Documentary                  |           114 |
|           2019 | Suspense                     |           105 |
|           2019 | Documentaries                |           104 |
|           2019 | Crime TV Shows               |            92 |
|           2019 | International                |            88 |
|           2019 | Animation                    |            87 |
|           2019 | Children & Family Movies     |            82 |
|           2019 | Independent Movies           |            76 |
|           2019 | TV Comedies                  |            75 |
|           2019 | Thrillers                    |            71 |
|           2019 | Romantic Movies              |            64 |
|           2019 | Horror                       |            64 |
|           2019 | Kids' TV                     |            59 |
|           2019 | Romance                      |            50 |
|           2019 | Stand-Up Comedy              |            49 |
|           2019 | and Culture                  |            48 |
|           2019 | Romantic TV Shows            |            48 |
|           2019 | Music & Musicals             |            48 |
|           2019 | Entertainment                |            48 |
|           2019 | Arts                         |            48 |
|           2019 | TV Shows                     |            47 |
|           2019 | Docuseries                   |            47 |
|           2019 | Action & Adventure           |            44 |
|           2019 | Reality TV                   |            42 |
|           2019 | TV Action & Adventure        |            35 |
|           2019 | Horror Movies                |            34 |
|           2019 | Spanish-Language TV Shows    |            31 |
|           2019 | British TV Shows             |            26 |
|           2019 | Adventure                    |            26 |
|           2019 | Sports Movies                |            25 |
|           2019 | Science Fiction              |            24 |
|           2019 | Sci-Fi & Fantasy             |            20 |
|           2019 | Sports                       |            19 |
|           2019 | Korean TV Shows              |            19 |
|           2019 | Fitness                      |            18 |
|           2019 | Anime Series                 |            18 |
|           2019 | TV Thrillers                 |            16 |
|           2019 | TV Mysteries                 |            16 |
|           2019 | TV Horror                    |            16 |
|           2019 | Young Adult Audience         |            14 |
|           2019 | Teen TV Shows                |            14 |
|           2019 | TV Sci-Fi & Fantasy          |            14 |
|           2019 | LGBTQ Movies                 |            13 |
|           2019 | LGBTQ                        |            13 |
|           2019 | Arthouse                     |            12 |
|           2019 | Unscripted                   |            10 |
|           2019 | Faith and Spirituality       |             9 |
|           2019 | Western                      |             8 |
|           2019 | Stand-Up Comedy & Talk Shows |             8 |
|           2019 | Science & Nature TV          |             8 |
|           2019 | Faith & Spirituality         |             8 |
|           2019 | Anime Features               |             6 |
|           2019 | Music Videos and Concerts    |             5 |
|           2019 | Historical                   |             5 |
|           2019 | Fantasy                      |             4 |
|           2019 | Classic & Cult TV            |             3 |
|           2019 | Anime                        |             3 |
|           2018 | International Movies         |           340 |
|           2018 | Dramas                       |           304 |
|           2018 | Drama                        |           224 |
|           2018 | International TV Shows       |           190 |
|           2018 | Comedies                     |           178 |
|           2018 | Independent Movies           |           131 |
|           2018 | Documentaries                |           120 |
|           2018 | Comedy                       |           115 |
|           2018 | TV Dramas                    |           109 |
|           2018 | Action                       |            98 |
|           2018 | Suspense                     |            96 |
|           2018 | Documentary                  |            88 |
|           2018 | Thrillers                    |            83 |
|           2018 | TV Comedies                  |            82 |
|           2018 | Action & Adventure           |            81 |
|           2018 | Crime TV Shows               |            79 |
|           2018 | International                |            69 |
|           2018 | Children & Family Movies     |            69 |
|           2018 | Special Interest             |            68 |
|           2018 | Kids                         |            67 |
|           2018 | Romantic Movies              |            64 |
|           2018 | Kids' TV                     |            64 |
|           2018 | Docuseries                   |            61 |
|           2018 | Stand-Up Comedy              |            59 |
|           2018 | Horror                       |            52 |
|           2018 | Horror Movies                |            51 |
|           2018 | Music & Musicals             |            43 |
|           2018 | Sci-Fi & Fantasy             |            42 |
|           2018 | and Culture                  |            41 |
|           2018 | Entertainment                |            41 |
|           2018 | Arts                         |            41 |
|           2018 | TV Shows                     |            39 |
|           2018 | Romantic TV Shows            |            39 |
|           2018 | British TV Shows             |            37 |
|           2018 | Reality TV                   |            36 |
|           2018 | Animation                    |            35 |
|           2018 | Romance                      |            32 |
|           2018 | Science Fiction              |            31 |
|           2018 | TV Action & Adventure        |            28 |
|           2018 | Sports Movies                |            27 |
|           2018 | Spanish-Language TV Shows    |            27 |
|           2018 | Anime Series                 |            24 |
|           2018 | Adventure                    |            21 |
|           2018 | Korean TV Shows              |            18 |
|           2018 | Unscripted                   |            16 |
|           2018 | Stand-Up Comedy & Talk Shows |            16 |
|           2018 | Sports                       |            16 |
|           2018 | TV Mysteries                 |            15 |
|           2018 | Fitness                      |            15 |
|           2018 | Faith & Spirituality         |            15 |
|           2018 | Science & Nature TV          |            14 |
|           2018 | LGBTQ Movies                 |            13 |
|           2018 | TV Horror                    |            11 |
|           2018 | Music Videos and Concerts    |            11 |
|           2018 | Movies                       |             9 |
|           2018 | Arthouse                     |             9 |
|           2018 | Teen TV Shows                |             8 |
|           2018 | LGBTQ                        |             8 |
|           2018 | Anime Features               |             8 |
|           2018 | TV Thrillers                 |             7 |
|           2018 | TV Sci-Fi & Fantasy          |             7 |
|           2018 | Young Adult Audience         |             6 |
|           2018 | Fantasy                      |             6 |
|           2018 | Faith and Spirituality       |             6 |
|           2018 | Western                      |             4 |
|           2018 | Anime                        |             3 |
|           2017 | International Movies         |           328 |
|           2017 | Dramas                       |           285 |
|           2017 | Drama                        |           199 |
|           2017 | Documentaries                |           172 |
|           2017 | Comedies                     |           164 |
|           2017 | International TV Shows       |           136 |
|           2017 | Independent Movies           |           113 |
|           2017 | Comedy                       |           106 |
|           2017 | Documentary                  |            89 |
|           2017 | Action & Adventure           |            89 |
|           2017 | Special Interest             |            81 |
|           2017 | TV Dramas                    |            77 |
|           2017 | Action                       |            76 |
|           2017 | Suspense                     |            74 |
|           2017 | Thrillers                    |            68 |
|           2017 | Kids                         |            67 |
|           2017 | Romantic Movies              |            64 |
|           2017 | Stand-Up Comedy              |            58 |
|           2017 | TV Comedies                  |            57 |
|           2017 | Children & Family Movies     |            55 |
|           2017 | Crime TV Shows               |            54 |
|           2017 | Kids' TV                     |            53 |
|           2017 | Horror Movies                |            47 |
|           2017 | International                |            41 |
|           2017 | Docuseries                   |            39 |
|           2017 | Horror                       |            36 |
|           2017 | British TV Shows             |            34 |
|           2017 | TV Shows                     |            33 |
|           2017 | Music & Musicals             |            33 |
|           2017 | Animation                    |            32 |
|           2017 | Romantic TV Shows            |            30 |
|           2017 | Sports Movies                |            29 |
|           2017 | Korean TV Shows              |            25 |
|           2017 | and Culture                  |            24 |
|           2017 | Entertainment                |            24 |
|           2017 | Arts                         |            24 |
|           2017 | Sci-Fi & Fantasy             |            23 |
|           2017 | Anime                        |            22 |
|           2017 | Romance                      |            21 |
|           2017 | Science Fiction              |            19 |
|           2017 | Fitness                      |            17 |
|           2017 | LGBTQ Movies                 |            16 |
|           2017 | Sports                       |            15 |
|           2017 | Reality TV                   |            15 |
|           2017 | Music Videos and Concerts    |            14 |
|           2017 | Adventure                    |            14 |
|           2017 | Spanish-Language TV Shows    |            12 |
|           2017 | Unscripted                   |            11 |
|           2017 | Stand-Up Comedy & Talk Shows |            10 |
|           2017 | Faith and Spirituality       |            10 |
|           2017 | Faith & Spirituality         |            10 |
|           2017 | Anime Series                 |            10 |
|           2017 | TV Mysteries                 |             9 |
|           2017 | Young Adult Audience         |             8 |
|           2017 | TV Action & Adventure        |             8 |
|           2017 | LGBTQ                        |             8 |
|           2017 | Science & Nature TV          |             7 |
|           2017 | Historical                   |             6 |
|           2017 | Anime Features               |             6 |
|           2017 | Teen TV Shows                |             5 |
|           2017 | Movies                       |             5 |
|           2017 | Fantasy                      |             5 |
|           2017 | TV Sci-Fi & Fantasy          |             4 |
|           2017 | TV Horror                    |             4 |
|           2017 | Military and War             |             4 |
|           2017 | TV Thrillers                 |             3 |
|           2017 | Arthouse                     |             3 |
|           2016 | International Movies         |           305 |
|           2016 | Dramas                       |           265 |
|           2016 | Drama                        |           153 |
|           2016 | Comedies                     |           150 |
|           2016 | Documentaries                |           137 |
|           2016 | International TV Shows       |           133 |
|           2016 | Comedy                       |           107 |
|           2016 | Special Interest             |           103 |
|           2016 | Independent Movies           |           101 |
|           2016 | Suspense                     |            87 |
|           2016 | Action & Adventure           |            80 |
|           2016 | Documentary                  |            79 |
|           2016 | TV Dramas                    |            73 |
|           2016 | Thrillers                    |            72 |
|           2016 | Kids                         |            59 |
|           2016 | Action                       |            52 |
|           2016 | TV Comedies                  |            47 |
|           2016 | Romantic TV Shows            |            46 |
|           2016 | Kids' TV                     |            46 |
|           2016 | Children & Family Movies     |            45 |
|           2016 | Romantic Movies              |            41 |
|           2016 | Crime TV Shows               |            39 |
|           2016 | Stand-Up Comedy              |            37 |
|           2016 | Horror                       |            37 |
|           2016 | Docuseries                   |            36 |
|           2016 | Sports Movies                |            32 |
|           2016 | Horror Movies                |            32 |
|           2016 | and Culture                  |            31 |
|           2016 | Entertainment                |            31 |
|           2016 | Arts                         |            31 |
|           2016 | British TV Shows             |            30 |
|           2016 | Music & Musicals             |            27 |
|           2016 | Animation                    |            27 |
|           2016 | Korean TV Shows              |            26 |
|           2016 | Reality TV                   |            24 |
|           2016 | Romance                      |            23 |
|           2016 | International                |            23 |
|           2016 | Sci-Fi & Fantasy             |            22 |
|           2016 | Science Fiction              |            19 |
|           2016 | Fitness                      |            18 |
|           2016 | Spanish-Language TV Shows    |            17 |
|           2016 | TV Shows                     |            16 |
|           2016 | Science & Nature TV          |            16 |
|           2016 | Unscripted                   |            15 |
|           2016 | Arthouse                     |            14 |
|           2016 | Adventure                    |            12 |
|           2016 | Anime Series                 |            11 |
|           2016 | TV Action & Adventure        |             9 |
|           2016 | LGBTQ Movies                 |             9 |
|           2016 | LGBTQ                        |             9 |
|           2016 | Anime                        |             9 |
|           2016 | TV Mysteries                 |             7 |
|           2016 | Sports                       |             7 |
|           2016 | Music Videos and Concerts    |             7 |
|           2016 | Movies                       |             6 |
|           2016 | Young Adult Audience         |             5 |
|           2016 | Teen TV Shows                |             5 |
|           2016 | Historical                   |             5 |
|           2016 | Faith and Spirituality       |             5 |
|           2016 | Anime Features               |             5 |
|           2016 | TV Sci-Fi & Fantasy          |             4 |
|           2016 | TV Horror                    |             4 |
|           2016 | Western                      |             3 |
|           2016 | TV Thrillers                 |             3 |
|           2016 | Faith & Spirituality         |             3 |
|           2015 | International Movies         |           210 |
|           2015 | Dramas                       |           180 |
|           2015 | Drama                        |           116 |
|           2015 | Comedy                       |            94 |
|           2015 | Comedies                     |            94 |
|           2015 | International TV Shows       |            93 |
|           2015 | Documentaries                |            67 |
|           2015 | Kids                         |            66 |
|           2015 | Independent Movies           |            65 |
|           2015 | Action                       |            63 |
|           2015 | Suspense                     |            62 |
|           2015 | Special Interest             |            59 |
|           2015 | Documentary                  |            55 |
|           2015 | Action & Adventure           |            53 |
|           2015 | TV Dramas                    |            50 |
|           2015 | Romantic Movies              |            40 |
|           2015 | TV Comedies                  |            37 |
|           2015 | Animation                    |            37 |
|           2015 | Romantic TV Shows            |            34 |
|           2015 | Thrillers                    |            32 |
|           2015 | Horror                       |            26 |
|           2015 | Crime TV Shows               |            25 |
|           2015 | and Culture                  |            24 |
|           2015 | Music & Musicals             |            24 |
|           2015 | Kids' TV                     |            24 |
|           2015 | Entertainment                |            24 |
|           2015 | Arts                         |            24 |
|           2015 | Children & Family Movies     |            23 |
|           2015 | Romance                      |            22 |
|           2015 | British TV Shows             |            22 |
|           2015 | Docuseries                   |            21 |
|           2015 | Horror Movies                |            20 |
|           2015 | Stand-Up Comedy              |            17 |
|           2015 | Sci-Fi & Fantasy             |            16 |
|           2015 | Sports Movies                |            15 |
|           2015 | Korean TV Shows              |            15 |
|           2015 | Reality TV                   |            12 |
|           2015 | TV Shows                     |            11 |
|           2015 | Science Fiction              |            11 |
|           2015 | LGBTQ Movies                 |            11 |
|           2015 | Anime Series                 |            11 |
|           2015 | Adventure                    |            10 |
|           2015 | TV Thrillers                 |             8 |
|           2015 | TV Horror                    |             8 |
|           2015 | Spanish-Language TV Shows    |             8 |
|           2015 | Movies                       |             8 |
|           2015 | Unscripted                   |             7 |
|           2015 | Science & Nature TV          |             7 |
|           2015 | TV Mysteries                 |             6 |
|           2015 | International                |             6 |
|           2015 | Faith and Spirituality       |             6 |
|           2015 | TV Sci-Fi & Fantasy          |             5 |
|           2015 | TV Action & Adventure        |             5 |
|           2015 | Sports                       |             5 |
|           2015 | Music Videos and Concerts    |             5 |
|           2015 | LGBTQ                        |             5 |
|           2015 | Western                      |             4 |
|           2015 | Teen TV Shows                |             4 |
|           2015 | Faith & Spirituality         |             4 |
|           2015 | Stand-Up Comedy & Talk Shows |             3 |
|           2015 | Anime                        |             3 |

## QUERY 8a: Netflix Top 10 Countries
(10 rows)

| country        |   netflix_titles |   percentage |
|:---------------|-----------------:|-------------:|
| United States  |             2818 |        35.33 |
| India          |              972 |        12.19 |
| United Kingdom |              419 |         5.25 |
| Japan          |              245 |         3.07 |
| South Korea    |              199 |         2.49 |
| Canada         |              181 |         2.27 |
| Spain          |              145 |         1.82 |
| France         |              124 |         1.55 |
| Mexico         |              110 |         1.38 |
| Egypt          |              106 |         1.33 |

## QUERY 8b: Amazon Prime Top 10 Countries
(10 rows)

| country                       |   prime_titles |   percentage |
|:------------------------------|---------------:|-------------:|
| United States                 |            253 |        37.65 |
| India                         |            229 |        34.08 |
| United Kingdom                |             28 |         4.17 |
| Canada                        |             16 |         2.38 |
| United Kingdom, United States |             12 |         1.79 |
| Italy                         |              8 |         1.19 |
| Spain                         |              8 |         1.19 |
| Canada, United States         |              7 |         1.04 |
| United States, United Kingdom |              6 |         0.89 |
| Germany                       |              5 |         0.74 |

## QUERY 9: Content Added Over Time
(15 rows)

|   year_added | platform     |   titles_added |
|-------------:|:-------------|---------------:|
|         2021 | Amazon Prime |            155 |
|         2021 | Netflix      |           1498 |
|         2020 | Netflix      |           1879 |
|         2019 | Netflix      |           2016 |
|         2018 | Netflix      |           1649 |
|         2017 | Netflix      |           1188 |
|         2016 | Netflix      |            429 |
|         2015 | Netflix      |             82 |
|         2014 | Netflix      |             24 |
|         2013 | Netflix      |             11 |
|         2012 | Netflix      |              3 |
|         2011 | Netflix      |             13 |
|         2010 | Netflix      |              1 |
|         2009 | Netflix      |              2 |
|         2008 | Netflix      |              2 |

## QUERY 10: Rating Distribution by Country
(373 rows)

| country                                                       | rating   |   title_count |
|:--------------------------------------------------------------|:---------|--------------:|
| Argentina                                                     | TV-MA    |            39 |
| Argentina                                                     | TV-14    |             7 |
| Argentina                                                     | TV-PG    |             3 |
| Argentina                                                     | TV-Y     |             2 |
| Argentina                                                     | TV-G     |             2 |
| Argentina                                                     | NR       |             2 |
| Argentina, Spain                                              | TV-MA    |             7 |
| Australia                                                     | TV-MA    |            36 |
| Australia                                                     | TV-PG    |            13 |
| Australia                                                     | TV-14    |            11 |
| Australia                                                     | TV-Y     |             8 |
| Australia                                                     | TV-Y7    |             4 |
| Australia                                                     | TV-G     |             4 |
| Australia                                                     | R        |             4 |
| Australia                                                     | PG       |             4 |
| Australia                                                     | 13+      |             3 |
| Australia, Canada                                             | TV-Y     |             2 |
| Australia, United States                                      | TV-14    |             4 |
| Australia, United States                                      | R        |             3 |
| Australia, United States                                      | PG-13    |             2 |
| Australia, United States                                      | PG       |             2 |
| Austria                                                       | TV-MA    |             3 |
| Belgium                                                       | TV-MA    |             6 |
| Belgium                                                       | TV-14    |             2 |
| Belgium, Netherlands                                          | TV-MA    |             2 |
| Brazil                                                        | TV-MA    |            50 |
| Brazil                                                        | TV-14    |            10 |
| Brazil                                                        | TV-PG    |             6 |
| Brazil                                                        | TV-Y     |             3 |
| Brazil                                                        | TV-G     |             3 |
| Brazil                                                        | PG       |             2 |
| Brazil                                                        | NR       |             2 |
| Brazil, France                                                | TV-MA    |             2 |
| Bulgaria, United States                                       | R        |             3 |
| Canada                                                        | TV-MA    |            61 |
| Canada                                                        | TV-14    |            26 |
| Canada                                                        | TV-PG    |            22 |
| Canada                                                        | R        |            18 |
| Canada                                                        | TV-Y     |            17 |
| Canada                                                        | TV-G     |            14 |
| Canada                                                        | TV-Y7    |             9 |
| Canada                                                        | PG       |             8 |
| Canada                                                        | 13+      |             7 |
| Canada                                                        | PG-13    |             3 |
| Canada                                                        | NR       |             2 |
| Canada                                                        | 18+      |             2 |
| Canada                                                        | 16+      |             2 |
| Canada, Australia                                             | TV-Y7    |             2 |
| Canada, India                                                 | TV-14    |             2 |
| Canada, United States                                         | TV-MA    |            17 |
| Canada, United States                                         | R        |            14 |
| Canada, United States                                         | TV-14    |             5 |
| Canada, United States                                         | TV-Y     |             3 |
| Canada, United States                                         | TV-PG    |             3 |
| Canada, United States                                         | TV-Y7    |             2 |
| Canada, United States                                         | PG       |             2 |
| Canada, United States, United Kingdom                         | R        |             2 |
| Chile                                                         | TV-MA    |            10 |
| Chile                                                         | TV-14    |             3 |
| China                                                         | TV-14    |            40 |
| China                                                         | TV-MA    |            15 |
| China                                                         | TV-PG    |             6 |
| China                                                         | TV-G     |             3 |
| China, Hong Kong                                              | TV-MA    |             6 |
| China, Hong Kong                                              | TV-14    |             5 |
| China, United Kingdom                                         | TV-Y     |             3 |
| China, United States, United Kingdom                          | PG       |             3 |
| Colombia                                                      | TV-MA    |            26 |
| Colombia                                                      | TV-14    |             9 |
| Colombia, Mexico, United States                               | TV-14    |             2 |
| Czech Republic, United States                                 | TV-14    |             2 |
| Denmark                                                       | TV-MA    |             9 |
| Denmark, United States                                        | TV-MA    |             3 |
| Egypt                                                         | TV-14    |            72 |
| Egypt                                                         | TV-MA    |            29 |
| Egypt                                                         | TV-PG    |             4 |
| Egypt, France                                                 | TV-14    |             2 |
| France                                                        | TV-MA    |            80 |
| France                                                        | TV-14    |            21 |
| France                                                        | TV-Y     |            10 |
| France                                                        | TV-Y7    |             3 |
| France                                                        | TV-PG    |             3 |
| France                                                        | TV-G     |             2 |
| France                                                        | R        |             2 |
| France                                                        | PG-13    |             2 |
| France, Belgium                                               | TV-MA    |            19 |
| France, Belgium                                               | PG       |             3 |
| France, Belgium                                               | R        |             2 |
| France, Egypt                                                 | TV-MA    |             2 |
| France, United States                                         | TV-MA    |             3 |
| France, United States                                         | R        |             3 |
| France, United States                                         | TV-14    |             2 |
| France, United States                                         | PG-13    |             2 |
| Germany                                                       | TV-MA    |            42 |
| Germany                                                       | TV-14    |            12 |
| Germany                                                       | TV-PG    |             4 |
| Germany                                                       | R        |             4 |
| Germany                                                       | TV-G     |             3 |
| Germany                                                       | 13+      |             2 |
| Germany, Canada, United States, France, United Kingdom        | R        |             2 |
| Germany, Czech Republic                                       | TV-MA    |             2 |
| Germany, United States                                        | PG-13    |             5 |
| Germany, United States                                        | R        |             3 |
| Germany, United States                                        | TV-MA    |             2 |
| Germany, United States                                        | PG       |             2 |
| Ghana                                                         | TV-MA    |             2 |
| Hong Kong                                                     | TV-14    |            25 |
| Hong Kong                                                     | TV-MA    |            18 |
| Hong Kong                                                     | R        |             6 |
| Hong Kong                                                     | TV-PG    |             3 |
| Hong Kong, China                                              | TV-MA    |             7 |
| Hong Kong, China                                              | TV-14    |             5 |
| Hong Kong, China                                              | R        |             3 |
| Hong Kong, United States                                      | R        |             3 |
| Hungary                                                       | TV-MA    |             3 |
| Iceland                                                       | TV-MA    |             5 |
| India                                                         | TV-14    |           550 |
| India                                                         | TV-MA    |           248 |
| India                                                         | TV-PG    |           134 |
| India                                                         | 13+      |           105 |
| India                                                         | ALL      |            46 |
| India                                                         | 16+      |            39 |
| India                                                         | 18+      |            20 |
| India                                                         | TV-Y7    |            14 |
| India                                                         | NR       |            14 |
| India                                                         | TV-G     |             9 |
| India                                                         | PG-13    |             7 |
| India                                                         | TV-Y     |             5 |
| India                                                         | 7+       |             4 |
| India                                                         | PG       |             3 |
| India, France                                                 | TV-MA    |             3 |
| India, Soviet Union                                           | TV-14    |             2 |
| India, United States                                          | TV-14    |             5 |
| India, United States                                          | 13+      |             4 |
| India, United States                                          | TV-MA    |             3 |
| Indonesia                                                     | TV-14    |            35 |
| Indonesia                                                     | TV-PG    |            20 |
| Indonesia                                                     | TV-MA    |            14 |
| Indonesia                                                     | TV-G     |             8 |
| Indonesia                                                     | R        |             2 |
| Iran, France                                                  | PG-13    |             2 |
| Ireland                                                       | TV-MA    |             7 |
| Ireland                                                       | R        |             2 |
| Israel                                                        | TV-MA    |             9 |
| Israel                                                        | TV-PG    |             2 |
| Israel                                                        | TV-14    |             2 |
| Israel, United States                                         | TV-MA    |             2 |
| Italy                                                         | TV-MA    |            30 |
| Italy                                                         | TV-14    |             7 |
| Italy                                                         | 13+      |             4 |
| Italy                                                         | TV-Y7    |             3 |
| Italy, France                                                 | TV-MA    |             2 |
| Japan                                                         | TV-14    |            91 |
| Japan                                                         | TV-MA    |            87 |
| Japan                                                         | TV-PG    |            39 |
| Japan                                                         | TV-Y7    |            17 |
| Japan                                                         | PG       |             4 |
| Japan                                                         | PG-13    |             3 |
| Japan                                                         | TV-Y     |             2 |
| Japan, United States                                          | TV-MA    |             4 |
| Japan, United States                                          | TV-14    |             3 |
| Japan, United States                                          | TV-PG    |             2 |
| Kuwait                                                        | TV-14    |             3 |
| Kuwait                                                        | TV-PG    |             2 |
| Lebanon                                                       | TV-14    |             8 |
| Lebanon                                                       | TV-MA    |             7 |
| Lebanon, Canada, France                                       | TV-14    |             2 |
| Malaysia                                                      | TV-PG    |             8 |
| Malaysia                                                      | TV-14    |             8 |
| Malaysia                                                      | TV-MA    |             3 |
| Malaysia                                                      | TV-Y7    |             2 |
| Mexico                                                        | TV-MA    |            78 |
| Mexico                                                        | TV-14    |            13 |
| Mexico                                                        | TV-PG    |             6 |
| Mexico                                                        | R        |             4 |
| Mexico                                                        | NR       |             4 |
| Mexico                                                        | TV-Y7    |             3 |
| Mexico                                                        | TV-G     |             2 |
| Mexico, Spain                                                 | TV-MA    |             3 |
| Mexico, United States                                         | TV-MA    |             5 |
| Mexico, United States                                         | TV-PG    |             3 |
| Mexico, United States                                         | R        |             2 |
| Netherlands                                                   | TV-MA    |            10 |
| Netherlands                                                   | TV-14    |             4 |
| Netherlands                                                   | TV-Y     |             2 |
| Netherlands                                                   | TV-G     |             2 |
| New Zealand                                                   | TV-MA    |             7 |
| New Zealand                                                   | TV-14    |             2 |
| New Zealand, United States                                    | PG-13    |             2 |
| Nigeria                                                       | TV-14    |            43 |
| Nigeria                                                       | TV-MA    |            41 |
| Nigeria                                                       | TV-PG    |             9 |
| Norway                                                        | TV-MA    |             7 |
| Norway                                                        | TV-PG    |             2 |
| Norway, Iceland, United States                                | R        |             2 |
| Pakistan                                                      | TV-14    |            11 |
| Pakistan                                                      | TV-PG    |             5 |
| Pakistan                                                      | TV-MA    |             2 |
| Peru                                                          | TV-MA    |             2 |
| Philippines                                                   | TV-14    |            34 |
| Philippines                                                   | TV-MA    |            28 |
| Philippines                                                   | TV-PG    |             8 |
| Philippines                                                   | TV-G     |             4 |
| Poland                                                        | TV-MA    |            21 |
| Poland                                                        | TV-14    |             2 |
| Poland, United States                                         | TV-MA    |             4 |
| Portugal, Spain                                               | TV-MA    |             2 |
| Romania                                                       | TV-MA    |             4 |
| Russia                                                        | TV-MA    |             7 |
| Russia                                                        | TV-Y     |             3 |
| Russia                                                        | TV-14    |             3 |
| Russia                                                        | TV-Y7    |             2 |
| Saudi Arabia                                                  | TV-14    |             7 |
| Singapore                                                     | TV-14    |            15 |
| Singapore                                                     | TV-MA    |             5 |
| Singapore                                                     | TV-PG    |             2 |
| Singapore, United States                                      | TV-MA    |             2 |
| South Africa                                                  | TV-MA    |            20 |
| South Africa                                                  | TV-14    |             5 |
| South Africa                                                  | TV-PG    |             4 |
| South Africa, United States                                   | PG-13    |             3 |
| South Korea                                                   | TV-MA    |            85 |
| South Korea                                                   | TV-14    |            83 |
| South Korea                                                   | TV-PG    |            16 |
| South Korea                                                   | TV-Y7    |             7 |
| South Korea                                                   | TV-Y     |             4 |
| South Korea                                                   | NR       |             3 |
| South Korea, United States                                    | TV-Y7    |             2 |
| South Korea, United States                                    | TV-MA    |             2 |
| Spain                                                         | TV-MA    |           120 |
| Spain                                                         | TV-14    |            13 |
| Spain                                                         | TV-PG    |             5 |
| Spain                                                         | 16+      |             3 |
| Spain                                                         | TV-Y     |             2 |
| Spain                                                         | TV-G     |             2 |
| Spain                                                         | R        |             2 |
| Spain                                                         | 13+      |             2 |
| Spain, Argentina                                              | TV-MA    |             3 |
| Spain, France                                                 | TV-MA    |             5 |
| Spain, Germany                                                | TV-MA    |             3 |
| Sweden                                                        | TV-MA    |            13 |
| Sweden, United States                                         | TV-14    |             2 |
| Switzerland                                                   | TV-MA    |             2 |
| Taiwan                                                        | TV-14    |            39 |
| Taiwan                                                        | TV-MA    |            34 |
| Taiwan                                                        | TV-PG    |             8 |
| Thailand                                                      | TV-MA    |            40 |
| Thailand                                                      | TV-14    |            16 |
| Thailand                                                      | TV-PG    |             4 |
| Turkey                                                        | TV-MA    |            63 |
| Turkey                                                        | TV-14    |            31 |
| Turkey                                                        | TV-PG    |             9 |
| United Arab Emirates                                          | TV-14    |            10 |
| United Arab Emirates                                          | TV-PG    |             3 |
| United Kingdom                                                | TV-MA    |           177 |
| United Kingdom                                                | TV-PG    |            75 |
| United Kingdom                                                | TV-14    |            72 |
| United Kingdom                                                | R        |            35 |
| United Kingdom                                                | TV-G     |            23 |
| United Kingdom                                                | TV-Y     |            19 |
| United Kingdom                                                | 16+      |            11 |
| United Kingdom                                                | PG-13    |            10 |
| United Kingdom                                                | NR       |             6 |
| United Kingdom                                                | TV-Y7    |             5 |
| United Kingdom                                                | 13+      |             5 |
| United Kingdom                                                | 18+      |             3 |
| United Kingdom                                                | PG       |             2 |
| United Kingdom,                                               | TV-MA    |             2 |
| United Kingdom, Canada, United States                         | R        |             5 |
| United Kingdom, Canada, United States                         | TV-Y7    |             2 |
| United Kingdom, France                                        | R        |             2 |
| United Kingdom, France                                        | PG-13    |             2 |
| United Kingdom, France, United States                         | R        |             2 |
| United Kingdom, Japan, United States                          | R        |             2 |
| United Kingdom, United States                                 | R        |            26 |
| United Kingdom, United States                                 | PG-13    |            21 |
| United Kingdom, United States                                 | TV-MA    |            16 |
| United Kingdom, United States                                 | PG       |             8 |
| United Kingdom, United States                                 | TV-14    |             5 |
| United Kingdom, United States                                 | TV-PG    |             3 |
| United Kingdom, United States                                 | 16+      |             3 |
| United Kingdom, United States                                 | G        |             2 |
| United Kingdom, United States, Australia                      | R        |             3 |
| United Kingdom, United States, Spain, Germany, Greece, Canada | TV-PG    |             4 |
| United States                                                 | TV-MA    |           931 |
| United States                                                 | R        |           504 |
| United States                                                 | TV-14    |           406 |
| United States                                                 | PG-13    |           323 |
| United States                                                 | TV-PG    |           251 |
| United States                                                 | PG       |           176 |
| United States                                                 | TV-Y7    |           101 |
| United States                                                 | TV-Y     |            87 |
| United States                                                 | TV-G     |            82 |
| United States                                                 | 13+      |            38 |
| United States                                                 | NR       |            37 |
| United States                                                 | 16+      |            36 |
| United States                                                 | 18+      |            34 |
| United States                                                 | G        |            30 |
| United States                                                 | ALL      |            15 |
| United States                                                 | 7+       |             7 |
| United States, Argentina                                      | TV-MA    |             2 |
| United States, Australia                                      | PG       |             4 |
| United States, Australia                                      | PG-13    |             3 |
| United States, Australia                                      | R        |             2 |
| United States, Bulgaria                                       | R        |             3 |
| United States, Canada                                         | TV-Y     |            16 |
| United States, Canada                                         | R        |            15 |
| United States, Canada                                         | PG       |            10 |
| United States, Canada                                         | TV-Y7    |             9 |
| United States, Canada                                         | PG-13    |             9 |
| United States, Canada                                         | TV-MA    |             8 |
| United States, Canada                                         | TV-14    |             5 |
| United States, Canada                                         | TV-PG    |             3 |
| United States, Canada                                         | TV-G     |             2 |
| United States, Chile                                          | R        |             2 |
| United States, China                                          | PG       |             3 |
| United States, China                                          | R        |             2 |
| United States, China                                          | PG-13    |             2 |
| United States, China                                          | 13+      |             2 |
| United States, Colombia                                       | TV-MA    |             3 |
| United States, Czech Republic                                 | TV-MA    |             3 |
| United States, Czech Republic                                 | PG       |             2 |
| United States, France                                         | R        |             6 |
| United States, France                                         | PG-13    |             4 |
| United States, France                                         | TV-Y     |             2 |
| United States, France                                         | PG       |             2 |
| United States, France                                         | 13+      |             2 |
| United States, France, Japan                                  | TV-Y7    |             4 |
| United States, France, Japan                                  | PG       |             2 |
| United States, Germany                                        | PG-13    |             9 |
| United States, Germany                                        | R        |             7 |
| United States, Germany                                        | PG       |             2 |
| United States, Germany, Canada                                | R        |             2 |
| United States, Greece                                         | PG-13    |             2 |
| United States, India                                          | PG-13    |             3 |
| United States, India                                          | TV-MA    |             2 |
| United States, India                                          | TV-14    |             2 |
| United States, India                                          | 13+      |             2 |
| United States, Ireland                                        | TV-MA    |             2 |
| United States, Ireland                                        | PG       |             2 |
| United States, Italy                                          | R        |             2 |
| United States, Japan                                          | TV-MA    |             5 |
| United States, Japan                                          | TV-14    |             4 |
| United States, Japan                                          | TV-Y7    |             2 |
| United States, Japan                                          | TV-PG    |             2 |
| United States, Japan                                          | R        |             2 |
| United States, Japan                                          | PG-13    |             2 |
| United States, Japan, Canada                                  | TV-Y7    |             2 |
| United States, Mexico                                         | R        |             4 |
| United States, Mexico                                         | TV-14    |             3 |
| United States, Mexico                                         | TV-PG    |             2 |
| United States, Mexico                                         | TV-MA    |             2 |
| United States, New Zealand                                    | TV-Y7    |             2 |
| United States, Nigeria                                        | TV-MA    |             2 |
| United States, Russia                                         | R        |             2 |
| United States, South Africa                                   | PG-13    |             2 |
| United States, Spain                                          | TV-MA    |             2 |
| United States, Sweden, Norway                                 | R        |             2 |
| United States, Thailand                                       | R        |             3 |
| United States, United Arab Emirates                           | PG-13    |             3 |
| United States, United Kingdom                                 | R        |            17 |
| United States, United Kingdom                                 | PG-13    |             9 |
| United States, United Kingdom                                 | PG       |             8 |
| United States, United Kingdom                                 | TV-MA    |             6 |
| United States, United Kingdom                                 | TV-PG    |             5 |
| United States, United Kingdom                                 | TV-14    |             5 |
| United States, United Kingdom, Australia                      | PG-13    |             3 |
| United States, United Kingdom, France                         | R        |             2 |
| United States, United Kingdom, France                         | PG-13    |             2 |
| United States, United Kingdom, Germany                        | R        |             2 |
| Uruguay                                                       | TV-PG    |             2 |
| Vietnam                                                       | TV-MA    |             3 |
| Vietnam                                                       | TV-14    |             3 |
