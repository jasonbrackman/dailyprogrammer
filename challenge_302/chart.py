class Chart:
    horizontal_x = 0
    horizontal_y = 10
    vertical_x = 0
    vertical_y = 4

    records = list()

    def __init__(self):
        pass

    def set_table_bounds(self, hx, hy, vx, vy):
        self.horizontal_x = hx
        self.horizontal_y = hy
        self.vertical_x = vx
        self.vertical_y = vy

    def display(self):

        indent = len(str(self.vertical_y + 1))
        self._print_rows(indent)
        self._print_horizontal_label(indent)

    def _print_rows(self, indent):
        for height in reversed(range(self.vertical_x, self.vertical_y + 1)):
            components = list()

            # ensure left label is rjustified by the maximum number length
            components.append('{}'.format(height).rjust(indent))

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
        labels.insert(0, (indent-1) * ' ')

        print(' '.join(labels))

    def _convert(self, list_):
        return [int(item) for item in list_]


class BarChart(Chart):

    def __init__(self, text):
        super().__init__()

        bounds, count, *records = text.split('\n')
        bounds = [int(bound) for bound in bounds.split()]

        self.set_table_bounds(*bounds)
        self.count = int(count)
        self.records = [self._convert(records[index].split())for index in range(self.count)]


class HistogramChart(Chart):
    bar_width = 0

    def __init__(self, text):
        super().__init__()

        bounds, bar_width, count, *records = text.split('\n')
        bounds = [int(bound) for bound in bounds.split()]

        self.set_table_bounds(*bounds)

        self.bar_width = int(bar_width)
        self.count = int(count)
        self.records = [self._convert(records[index].split()) for index in range(self.count)]

    def get_bucket_average(self):
        current = 1

        buckets = {current: []}
        for index, record in enumerate(self.records, 1):
            buckets[current].append(record[1])
            if index % self.bar_width == 0 and index < len(self.records):
                current += 1
                buckets[current] = list()

        buckets = [int(sum(values)/self.bar_width) for _, values in buckets.items()]

        return buckets

    def _print_rows(self, indent):
        buckets = self.get_bucket_average()

        for height in reversed(range(self.vertical_x, self.vertical_y + 1)):
            components = ['{}'.format(height).rjust(indent)]
            for bucket in buckets:
                mark = '*' if bucket >= height else ' '
                pad = len(str(self.horizontal_y)) + 1
                components.append(int(self.bar_width * pad - 1) * mark + ' ')

            print(''.join(components))

    def _print_horizontal_label(self, indent):
        pad = len(str(self.horizontal_y))
        labels = [str(record[0]).zfill(pad) for record in self.records]
        labels.insert(0, (indent-1) * ' ')
        print(' '.join(labels))
