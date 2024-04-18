class Predicate:
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __str__(self):
        return f"{self.name}/{self.arity}"

class Term:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Atom:
    def __init__(self, predicate, terms):
        self.predicate = predicate
        self.terms = terms

    def __str__(self):
        return f"{self.predicate.name}({', '.join(str(term) for term in self.terms)})"

class KnowledgeBase:
    def __init__(self):
        self.facts = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def query(self, atom):
        return any(isinstance(fact, Atom) and fact.predicate.name == atom.predicate.name
                   and all(term1.name == term2.name for term1, term2 in zip(fact.terms, atom.terms))
                   for fact in self.facts)

if __name__ == "__main__":
    kb = KnowledgeBase()
    pred_name = input("Enter predicate name: ")
    pred_arity = int(input("Enter predicate arity: "))
    predicate = Predicate(pred_name, pred_arity)
    terms = [Term(input(f"Enter term {i+1}: ")) for i in range(pred_arity)]
    atom = Atom(predicate, terms)
    kb.add_fact(atom)
    query_pred_name = input("Enter predicate name to query: ")
    query_pred_arity = int(input("Enter predicate arity: "))
    query_terms = [Term(input(f"Enter term {i+1}: ")) for i in range(query_pred_arity)]
    query_atom = Atom(Predicate(query_pred_name, query_pred_arity), query_terms)
    result = kb.query(query_atom)
    print(f"Query result: {result}")
