class Service:
    def __init__(self,reader,writer,validator,processor):
        self.reader = reader
        self.writer = writer
        self.validator = validator
        self.processor = processor

    def execute(self,input_file,output_file):
        orders = self.reader.read(input_file)
        processed_rows = []
        for o in orders:
            if not self.validator.validate(o):
                continue
            processed = self.processor.process(o)
            processed_rows.append(processed)

        self.writer.write(output_file,processed_rows)

