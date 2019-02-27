def sliding_window(segments, MINLEN, MINCNT):
    d = {}
    for sublen in range(MINLEN, int(len(segments) / MINCNT)):
        for i in range(0, len(segments) - sublen):
            sub = segments[i:i + sublen]
            cnt = segments.count(sub)
            if cnt >= MINCNT and sub not in d:
                d[sub] = cnt
    return d