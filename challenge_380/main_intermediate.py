import time
import string

morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
smorse_map = dict(zip(morse, string.ascii_lowercase))


def recursive_track(text, track=None):
    if track is None:
        track = []

    # base case
    if len(track) == 26:
        return track

    # Lets try all the different letter possibilities for this position
    for i in range(4, 0, -1):
        item = smorse_map.get(text[:i], None)
        if item and item not in track:
            track.append(item)
            if recursive_track(text[i:], track=track) is not None:
                return track
            track.pop()


def main():
    # simple example -- solved in 0.000 seconds
    t = ".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----.."

    # More complex -- solved in 0.200 seconds
    t = "------.-...-..--.-...-.-..-.-..-...---.--...-.-....---..-...-.-......--..---.-.---"

    t1 = time.monotonic()
    result = recursive_track(t, track=[])
    t2 = time.monotonic()
    print(f"[{t2 - t1:.6f} Seconds] {''.join(result)}")

    with open(r'./data/smorse2_bonus.txt', 'rt') as handle:
        lines = handle.readlines()

    num = 1_000
    t1 = time.monotonic()
    for line in lines[:num]:
        recursive_track(line, track=[])
        # print(''.join(result))
    t2 = time.monotonic()
    print(f"[{(t2 - t1) / num:.6f} Seconds] Avg of {num} iterations.")


if __name__ == "__main__":
    main()
