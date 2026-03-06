
class SaveName:
    def input_name(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def no_update(self):
        self.input_name('Nice try!\nEnter your name:')

    def save_name_to_file(self):
        new_name = self.input_name('Congratulations!\nEnter your name:')
        filename = "scores.txt"
        try:
            scores = []
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(" ", 1)
                    name, score = parts[0], int(parts[1])
                    scores.append((name, score))
        except:
            scores = []
        found = False
        for i, (name, score) in enumerate(scores):
            if name == new_name:
                scores[i] = (name, score + 1)
                found = True
                break
        if not found:
            scores.append((new_name, 1))
        scores.sort(reverse=True, key=lambda x: x[1])
        with open(filename, 'w') as file:
            for name, score in scores:
                file.write(name + ' ' + str(score))
