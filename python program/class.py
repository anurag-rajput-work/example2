class parent:
    def play(self):
        print("he is playing ")
class child(parent):
    # def play(self):
    #     print("he is playing out door games ")
        super().play()
a =  child()
a.play()