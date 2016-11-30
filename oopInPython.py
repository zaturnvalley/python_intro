class Program():
  # init method is a special method that
  # always runs, default
  def __init__(self, *args, **kwargs):
    # modifying language itself, stored in init
    self.lang = input("What Language?: ")
    self.version = float(input("Version?: "))
    self.skill = input("What skill level?: ")
  
  def upgrade(self):
    new_version = input("What version?: ")
    print("We have updated the version for", self.lang) 
    self.version = new_version

p1 = Program()
# p2 = Program()