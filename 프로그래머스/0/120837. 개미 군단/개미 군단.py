def solution(hp):
    general = int(hp/5)
    soldier = int((hp-general*5)/3)
    ant = int(hp-general*5-soldier*3)
    answer = general + soldier + ant
    return answer