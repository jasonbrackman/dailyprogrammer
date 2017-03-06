
class Histogram():
    horizontal_x = 0
    horizontal_y = 10
    vertical_x = 0
    vertical_y = 4
    count = 0
    records = list()

    def __init__(self):
        pass

    def create(self, hx, hy, vx, vy):
        self.horizontal_x = hx
        self.horizontal_y = hy
        self.vertical_x = vx
        self.vertical_y = vy

    def number_of_records(self, count):
        self.count = count

    def record(self, interval_start, interval_end, frequency):
        self.records.append([interval_start, interval_end, frequency])

    def display(self):

        indent = len(str(self.vertical_y + 1))

        for height in reversed(range(self.vertical_x, self.vertical_y+1)):

            self._print_row(height, indent)

        self._print_horizontal_label(indent)

    def _print_row(self, height, indent):
        components = list()
        components.append('{}'.format(height).rjust(indent))
        components.append((indent - 1) * ' ')

        for record in self.records:

            start, end, frequency = record
            tab = len(str(start)) * ' '
            mark = '.' if height <= frequency else ' '

            components.append('{}{}'.format(tab, mark))

        print(''.join(components))

    def _print_horizontal_label(self, indent):

        start = self.horizontal_x
        end = self.horizontal_y + 1
        step = self.records[0][1] - self.records[0][0]
        labels = [str(width) for width in range(start, end, step)]

        indent += 1

        print(indent * ' ', end='')
        print(' '.join(labels))


test = Histogram()
test.create(80, 130, 1, 10)
test.number_of_records(5)
test.record(80, 90, 1)
test.record(90, 100, 5)
test.record(100, 110, 7)
test.record(110, 120, 6)
test.record(120, 130, 2)
test.display()
