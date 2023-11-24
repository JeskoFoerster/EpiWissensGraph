class Example_note:
    # __inti__ set the member variables
    def __init__(self):
        self.EXAMPLE_DESCRIPTION = "This is the Example Text"
        self.EXAMPLE_TITLE = "Example Title"

    # both geter methods return the value of the member variable
    def get_description(self):
        return self.EXAMPLE_DESCRIPTION

    def get_title(self):
        return self.EXAMPLE_TITLE
