from matplotlib import pyplot as plt
from matplotlib_venn import venn3


class MakeVenn3(object):

    def __init__(self, set_list_1, set_list_2, set_list_3):
        self.set_list_1 = set_list_1
        self.set_list_2 = set_list_2
        self.set_list_3 = set_list_3
        self.label_1 = input('first label ?')
        self.label_2 = input('second label ?')
        self.label_3 = input('third label ?')

    def set_list_1_2(self):
        set_list_1_2 = []
        for i in self.set_list_1:
            for j in self.set_list_2:
                if i == j:
                    set_list_1_2.append(i)

        return set_list_1_2

    def set_list_1_3(self):
        set_list_1_3 = []
        for i in self.set_list_1:
            for j in self.set_list_3:
                if i == j:
                    set_list_1_3.append(i)

        return set_list_1_3

    def set_list_2_3(self):
        set_list_2_3 = []
        for i in self.set_list_2:
            for j in self.set_list_3:
                if i == j:
                    set_list_2_3.append(i)

        return set_list_2_3

    def set_list_1_2_3(self):
        set_list_1_2_3 = []
        for i in self.set_list_1_2():
            for j in self.set_list_1_3():
                if i == j:
                    set_list_1_2_3.append(i)

        return set_list_1_2_3

    def make_venn3(self):

        venn3(
            subsets=(
                len(self.set_list_1) - len(self.set_list_1_2()) - len(self.set_list_1_3()) + len(self.set_list_1_2_3()),
                len(self.set_list_2) - len(self.set_list_2_3()) - len(self.set_list_1_2()) + len(self.set_list_1_2_3()),
                len(self.set_list_1_2()) - len(self.set_list_1_2_3()),
                len(self.set_list_3) - len(self.set_list_1_3()) - len(self.set_list_2_3()) + len(self.set_list_1_2_3()),
                len(self.set_list_1_3()) - len(self.set_list_1_2_3()),
                len(self.set_list_2_3()) - len(self.set_list_1_2_3()),
                len(self.set_list_1_2_3())
            ),
            set_labels=(self.label_1, self.label_2, self.label_3)
        )

        plt.show()
