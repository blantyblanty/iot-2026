
class Candidate:
    """Кандидат на місцевих виборах: прізвище та кількість голосів."""

    def __init__(self, surname="", votes=0):
        self._surname = surname
        self._votes = votes

    def __del__(self):
        # Деструктор
        print(f"[Деструктор] Об'єкт Candidate '{self._surname}' знищено")

    # --- функції доступу ---
    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname

    def get_votes(self):
        return self._votes

    def set_votes(self, votes):
        if votes < 0:
            raise ValueError("Кількість голосів не може бути від'ємною")
        self._votes = votes

    # --- виведення ---
    def show(self, total_votes):
        percent = self._votes / total_votes * 100 if total_votes > 0 else 0.0
        print(f"{self._surname:<20} {self._votes:>8} {percent:>9.2f}%")


class Elections:
    """Вибори: набір кандидатів, підрахунок відсотків і переможця."""

    def __init__(self, candidates=None):
        self._candidates = list(candidates) if candidates else []

    def __del__(self):
        print("[Деструктор] Об'єкт Elections знищено")

    # --- функції доступу ---
    def get_candidates(self):
        return self._candidates

    def add_candidate(self, candidate):
        self._candidates.append(candidate)

    def remove_candidate(self, surname):
        for c in self._candidates:
            if c.get_surname() == surname:
                self._candidates.remove(c)
                return True
        return False

    def total_votes(self):
        return sum(c.get_votes() for c in self._candidates)

    def get_winner(self):
        """Повертає кандидата з найбільшою кількістю голосів
        (або None, якщо кандидатів немає)."""
        if not self._candidates:
            return None
        return max(self._candidates, key=lambda c: c.get_votes())

    def get_winners(self):
        """Усі кандидати з максимальною кількістю голосів (на випадок нічиєї)."""
        winner = self.get_winner()
        if winner is None:
            return []
        top = winner.get_votes()
        return [c for c in self._candidates if c.get_votes() == top]

    # --- виведення ---
    def show_results(self):
        total = self.total_votes()
        print(f"{'Прізвище':<20} {'Голосів':>8} {'Відсоток':>10}")
        print("-" * 40)
        for c in self._candidates:
            c.show(total)
        print("-" * 40)
        print(f"{'Всього голосів:':<20} {total:>8}")

    def show_winner(self):
        winners = self.get_winners()
        if not winners:
            print("Кандидатів немає")
        elif len(winners) == 1:
            w = winners[0]
            print(f"Переможець виборів: {w.get_surname()} ({w.get_votes()} голосів)")
        else:
            names = ", ".join(w.get_surname() for w in winners)
            print(f"Нічия між кандидатами: {names} "
                  f"({winners[0].get_votes()} голосів)")


def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Число має бути невід'ємним.")
                continue
            return value
        except ValueError:
            print("Введіть ціле число.")


def main():
    CANDIDATES_COUNT = 5
    elections = Elections()

    print(f"Введіть дані {CANDIDATES_COUNT} кандидатів:")
    for i in range(1, CANDIDATES_COUNT + 1):
        surname = input(f"Кандидат {i}, прізвище: ").strip()
        votes = read_int(f"Кандидат {i}, кількість голосів: ")
        elections.add_candidate(Candidate(surname, votes))

    print("\nРезультати виборів:")
    elections.show_results()
    print()
    elections.show_winner()
    

if __name__ == "__main__":
    main()