from builder import Builder


class Director():
    def __init__(self, builder: Builder) -> None:
        self.builder: Builder = builder

    def construct(self) -> None:
        self.builder.make_title('Greeting')
        self.builder.make_string('朝から昼にかけて')
        self.builder.make_items(['おはようございます', 'こんにちは'])

        self.builder.make_string('夜に')
        self.builder.make_items(['こんばんは', 'おやすみなさい', 'さようなら'])
        self.builder.close()
