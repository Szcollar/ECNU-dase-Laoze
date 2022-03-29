def jaccard(stra,strb):
    straSet = set(stra)
    strbSet = set(strb)
    Union = strbSet | straSet
    Intersection = straSet & strbSet
    return len(Intersection)/len(Union)

