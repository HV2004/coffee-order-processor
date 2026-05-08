class Service:
    def __init__(self,reader,writer,validator,processor):
        self.reader = reader
        self.writer = writer
        self.validator = validator
        self.processor = processor

    def execute(self,input_file,output_file):
        orders = self.reader.read(input_file)
        processed_rows = []
        valid_orders = []
        for o in orders:
            if not self.validator.validate(o):
                continue
            valid_orders.append(o)
            processed = self.processor.process(o)
            processed_rows.append(processed)

        self.writer.write(output_file,processed_rows)
        return valid_orders

