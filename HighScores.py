import heapq


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return heapq.nlargest(3, scores)


def latest_after_top_three(scores):
    topthree = heapq.nlargest(3, scores)
    return topthree[-1]


def scores_after_top_three(scores):
    topthree = heapq.nlargest(3, scores)
    for element in topthree:
        if element in scores:
            scores.remove(element)
    return scores


scores = [30, 50, 20, 70]
print(scores_after_top_three(scores))
