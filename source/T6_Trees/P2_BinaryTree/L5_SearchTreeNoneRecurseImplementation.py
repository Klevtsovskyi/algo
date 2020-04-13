from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree


class SearchTree(BinaryTree):
    """ Клас - Бінарне дерево пошуку.

     Реалізує структуру даних, у якій вставка та пошук елементів здійснюється
     (в середньому) за логарифмічний час. """

    def search(self, key):
        """ Метод, що реалізує пошук елемента item у бінарному дереві
            Не рекурсивна реалізація

        :param key: Шуканий елемент
        :return: Вузол з ключем key якщо такий елемент міститься у дереві
        та None - якщо елемент не знайдений.
        """
        node = self   # починаємо з кореня
        while node is not None:
            if node.mKey == key:   # якщо ключ поточного вузла збігається з шуканим,
                return node        # повертаємо знайдений вузол
            elif node.mKey > key:  # випадок: шуканий елемент може міститися у лівому піддереві
                node = node.mLeftChild  # рухаємося вниз до лівого нащадка
            else:                  # випадок: шуканий елемент може міститися у правому піддереві
                node = node.mRightChild # рухаємося вниз до правого нащадка
        # якщо опустилися по дереву до листка, то дерево не містить шуканого елемента
        return None

    def insert(self, key):
        """ Метод, що реалізує вставку елемента у бінарне дерево
            Не рекурсивна реалізація

        :param key: ключ, що необхідно вставити
        """

        node = self         # починаємо з кореня
        while True:
            if node.mKey == key:       # якщо ключ поточного вузла збігається з шуканим,
                break                  # вставка не потрібна
            elif node.mKey > key:      # якщо елемент для вставки має міститися у лівому піддереві
                if node.hasLeft():     # якщо дерево має лівого нащадка
                    node = node.mLeftChild  # рухаємося вниз до лівого нащадка
                else:                  # якщо дерево не має лівого нащадка
                    node.setLeft(key)  # додаємо key у ролі лівого нащадка
                    break
            elif node.mKey < key:      # якщо елемент для вставки має міститися у правому піддереві
                if node.hasRight():    # якщо дерево має правого нащадка
                    node = node.mRightChild # рухаємося вниз до правого нащадка
                else:                  # якщо дерево не має правого нащадка
                    node.setRight(key) # додаємо key у ролі правого нащадка
                    break

    def addItems(self, *items):
        """ Додає послідовність елементів у дерево пошуку

        :param items: Послідовність елементів, що додаються у дерево пошуку
        :return: None
        """
        for item in items:
            self.insert(item)


if __name__ == "__main__":
    t = SearchTree(9999999999999)
    t.addItems(12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16, 16)

    print(t)

    print(t.search(10))
    print(t.search(5))
    print(t.search(21))
    print(t.search(111))

    print()


