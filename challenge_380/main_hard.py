import time
import string

morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
smorse_map = dict(zip(morse, string.ascii_lowercase))


def recursive_track(text, track=None):
    if track is None:
        track = []

    # base case
    if not text:
        return track
    else:
        # Lets try all the different letter possibilities for this position
        for i in range(1, 5):
            chunk = text[:i]
            if chunk in smorse_map:
                item = smorse_map[chunk]
                if item not in track:
                    track.append(item)
                    result = recursive_track(text[i:], track=track)
                    if result is not None:
                        return track
                    track.pop()


if __name__ == "__main__":
    start = time.time()
    t = ".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----.."
    print(f"[{(start-time.time()) / 1_000}] {''.join(recursive_track(t, track=[]))}")

    # with open(r'./data/smorse2_bonus.txt', 'rt') as handle:
    #     for line in handle.readlines():
    #         print(''.join(recursive_track(line.strip(), track=[])))
