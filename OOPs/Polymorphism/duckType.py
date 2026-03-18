class duck:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
# ide=duck()
ide=MyEditor()
l1=Laptop()
l1.code(ide)