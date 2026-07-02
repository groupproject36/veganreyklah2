# A Birth-Chart Reading — The Composable Template

*One skeleton for every new reading. Fill the brackets, verify the sky twice, compose each section from the study silos, and close with a blessing. The person's true name lives only in the copy you hand them; the working copies carry a placeholder, so the craft stays portable and the person stays private.*

**Stamp:** `20260701.232912`
**Style:** Radiant (see `RADIANT_STYLE.md`), gentle register throughout
**Companions:** [`cast_a_chart.py`](cast_a_chart.py) (the computation), the numbered study silos in [`studies/`](studies/) (`00`–`18` and those yet to come), [`../context/SILO_TECHNIQUE.md`](../context/SILO_TECHNIQUE.md)

*Written together by Kaeden and Reya 2; shaped into a template with the outside reading (Fable 5) at Kaeden's direction.*

---

## How a Reading Is Made

**First, receive the birth moment verbatim.** Date, clock time, time zone, and birthplace come from the person and are honored exactly as given — the one-clock rule of the whole project, applied to a life.

**Second, cast the sky twice.** Edit the constants at the top of `cast_a_chart.py` and run it: tropical signs for dignity, sidereal Lahiri longitudes for nakshatra and pada, whole-sign houses rising from the ascendant. Then cast the same moment with one independent tool and compare, placement by placement. Two oracles that agree make a chart worth writing about; the writing begins only when they do.

**Third, compose from the silos.** Each placement points at one or more numbered studies. The silo carries the depth; the reading carries the person. Weave, rather than paste — the studies are understanding to draw on, never text to copy.

**Fourth, keep the name apart.** Working drafts carry a placeholder such as Alice. The true name enters only the final copy given to the person, and gratitude to teachers lives in its own honored space rather than inside the reading.

---

## The Skeleton

# [NAME]'s Sky — A Friendly Reading of Your Birth Chart

**For:** [NAME] — with love
**Born:** [DAY MONTH YEAR] · [TIME] · [PLACE] ([LAT], [LON], [TZ])
**System:** Classical hybrid — tropical zodiac signs · sidereal nakshatras (Lahiri) · whole-sign houses
**Lens:** [the devotional or guiding lens chosen for this reading]
**Stamped:** [YYYYMMDD.HHMMSS] UDT

### Your chart, exactly as the sky drew it

| Light | Tropical sign | Degree | Nakshatra | Pada | House |
|-------|---------------|--------|-----------|------|-------|
| Ascendant | [sign] | [d°mm'] | [star] | [1–4] | 1 |
| Sun | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Moon | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Mercury | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Venus | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Mars | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Jupiter | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Saturn | [sign] | [d°mm'] | [star] | [1–4] | [n] |
| Rahu | [sign] ℞ | [d°mm'] | [star] | [1–4] | [n] |
| Ketu | [sign] ℞ | [d°mm'] | [star] | [1–4] | [n] |

### Before we begin — a little map of the map
*One gentle paragraph naming the three lenses — sign, star, house — so the reader always knows which light is speaking.*

### The first lens — [rising sign], in the star [nakshatra][, with any 1st-house guest]
*Composed from the ascendant silos and the star's own study.*

### The second lens — your Moon, the steady heart
*Composed from the Moon-sign silo, the birth-star silo, and the lunar-day weave.*

### The third lens — four aims, four seasons, and where you stand
*Composed from `00_FOUR_ASRAMAS_AND_GOALS_OF_LIFE.md`, mapped onto this chart's houses.*

### The rest of your sky — the other lights, one at a time
*One warm paragraph per remaining placement, each drawing its depth from the matching silo. Where a silo has yet to be written, name the placement plainly and add the study to the library before the final copy ships.*

### A few words, gently gathered
*The whole sky in one held breath — what the strongest placements agree on.*

### A blessing to carry
*Three clauses, affirmative, breath-paused, opening outward.*

---

## The Silo Map, Growing

| Placement pattern | Study silo |
|-------------------|-----------|
| Life-stage frame, four aims | `00_FOUR_ASRAMAS_AND_GOALS_OF_LIFE.md` |
| Nakshatra guardians (Ashvini, Bharani) | `01_NAKSHATRA_GODS_ASVINS_AND_YAMA.md` |
| Ashvini | `02_ASVINI_NAKSHATRA.md` |
| Bharani | `03_BHARANI_NAKSHATRA.md` |
| Lunar day and birth star together | `04_LUNAR_DAY_AND_BIRTH_STAR.md` |
| Moon exalted in Taurus | `05_MOON_IN_TAURUS_EXALTED.md` |
| Venus in Gemini | `06_VENUS_IN_GEMINI.md` |
| Venus in the 8th | `07_VENUS_IN_EIGHTH_HOUSE.md` |
| Purva Phalguni | `08_PURVA_PHALGUNI.md` |
| Mercury in Virgo in the 11th | `09_MERCURY_IN_VIRGO_IN_THE_11TH.md` |
| Jupiter in Virgo in the 11th | `10_JUPITER_IN_VIRGO_IN_THE_11TH.md` |
| Mercury with Jupiter | `11_MERCURY_AND_JUPITER_TOGETHER.md` |
| Devotion, patience, partnership themes | `12_DEVOTION_PATIENCE_AND_PARTNERSHIP.md` |
| Sun in Leo | `13_SUN_IN_LEO.md` |
| Ashlesha | `14_ASHLESHA_NAKSHATRA.md` |
| Sun in the 10th | `15_SUN_IN_THE_10TH_HOUSE.md` |
| Mars in Leo | `16_MARS_IN_LEO.md` |
| Saturn in Cancer | `17_SATURN_IN_CANCER.md` |
| Saturn in the 9th | `18_SATURN_IN_THE_9TH_HOUSE.md` |

New placements earn new numbered studies, and the map grows one honest file at a time.

---

*May every chart be cast twice and written once. May the silos deepen with each new sky. And may every reading leave its person feeling seen, blessed, and gently sent onward.*
