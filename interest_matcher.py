from csp import Constraint, CSP
from typing import Dict, List, Optional, TypeVar

V = TypeVar('V')  # variable type


D = TypeVar('D')  # domain type


class InterestConstraint(Constraint[str, str]):
    def __init__(self, p1: str, p2: str) -> None:
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str]) -> bool:

        print(assignment, self.p1, self.p2, domains)

        return True


if __name__ == "__main__":
    variables: List[str] = ['Eric Schmidt',
                            'Kris Bharat', 'Lars Bak']

    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = list(filter(lambda x: x != variable, variables))

    csp: CSP[str, str] = CSP(variables, domains)

    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)
