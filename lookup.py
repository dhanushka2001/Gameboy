class Lookup:
    def __init__(self):
        self.highscore = {"HS1":["NUL",0],"HS2":["NUL",0],"HS3":["NUL",0],"HS4":["NUL",0],"HS5":["NUL",0]}
        with open("highscore.txt", "r") as f:
            lines = f.readlines()
            reader = []
            for line in lines:
                reader.append(line.split(" "))

            for x in reader:
                ID, name, score = x
                self.highscore[ID] = [name, int(score.rstrip())]

    def get_highscore(self):
        return self.highscore

    def write_out(self):
        with open("highscore.txt", "w") as x:
            for id, values in self.highscore.items():
                x.write(str(id) + " " + values[0] + " " + str(values[1]) + "\n")

    def add_name(self, name, score):
        if len(self.highscore) > 4:
            y = min(self.highscore.items(), key=(lambda k: k[1][1]))
            self.highscore[y[0]] = [name.upper(), score]
        else:
            self.highscore[len(self.highscore) + 1] = [name.upper(), score]
        self.write_out()