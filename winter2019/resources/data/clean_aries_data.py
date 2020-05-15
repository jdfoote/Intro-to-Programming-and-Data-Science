import csv

with open('./aries_crash_data_2018.csv', 'r') as fh:
    f = csv.DictReader(fh)
    to_keep = ["INDIVIDUAL_MR_RECORD",
            "PERSONTYPEDESCR",
            "GENDERCDE",
            "AGE_GRP",
            "INJNATUREDESCR",
            "RESULTDRUGIND",
            "COLLDTE",
            "COLLISION_TIME",
            "COLLISION_TIME_AM_PM",
            "CITYDESCR",
            "INJUREDNMB",
            "DEADNMB",
            "WEATHERDESCR",
            "PRIMARYFACTORDESCR"]

    with open('./aries_crash_data_2018_filtered.csv', 'w') as out:
        o = csv.writer(out)
        o.writerow(to_keep)
        for row in f:
            result = [row[x] for x in to_keep]
            o.writerow(result)
