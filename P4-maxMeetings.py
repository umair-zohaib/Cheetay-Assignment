def maxMeetings(S, F, N):
    slots = []
    for i in range(0, N):
        slots.append((S[i], F[i], i))

    slots.sort(key=lambda x: x[1])
    meet_count = 0

    if slots:
        meet_ends = slots[0][1]
        meet_count = 1
        for i in range(1, N):
            if slots[i][0] > meet_ends:
                meet_ends = slots[i][1]
                meet_count += 1
    return meet_count

