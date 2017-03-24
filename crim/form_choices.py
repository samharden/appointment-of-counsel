CRIM_CASETYPE_CHOICES = (
    ('dui', ("DUI")),
    ('battery', ("Battery")),
    ('marijuanaposs', ("Marijuana Possession")),
    ('petit-theft', ("Petit Theft")),
    ('dwlsr', ("Driving While License Suspended")),
)
CRIM_STATE_CHOICES = (
    ('fl', ("Florida")),
)

CRIM_COUNTY_CHOICES = (
    ('hillsb', ("Hillsborough")),
    ('pinell', ("Pinellas")),
    # ('orange', ("Orange")),
)
CRIM_JUDGE_CHOICES_HILLSB = (
    ('conrad', ("Conrad")),
    ('farr', ("Farr")),

    ('jeske', ("Jeske")),
    ('lefler', ("Lefler")),
    ('mcneil', ("McNeil")),
    ('myers', ("Myers")),
    ('taylor', ("Taylor")),
    ('notsure', ("Not Sure")),
)
CRIM_JUDGE_CHOICES_PINELL = (
    ('bedinghaus', ("Bedinghaus")),
    ('carballo', ("Carballo")),
    ('dittmer', ("Dittmer")),
    ('horrox', ("Horrox")),
    ('levine', ("Levine")),
    ('mckyton', ("McKyton")),
    ('overton', ("Overton")),
    ('pierce', ("Pierce")),
    ('notsure', ("Not Sure")),
)
YN_CHOICES = (
    ('yes', ("Look my case up by my name.")),
    ('no', ("Browse by judge.")),
)
