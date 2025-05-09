class NonTerminal:
    def __init__(self, name):
        self.name = name
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def set_rules(self, rules):
        self.rules = rules

    def get_name(self):
        return self.name

    def get_rules(self):
        return self.rules

class CFG:
    def __init__(self, input_str):
        self.non_terminals = []
        self.terminals = []
        self.start_symbol = ""
        self.non_terminal_map = {}
        self.parse_input(input_str)

    def parse_input(self, input_str):
        nt_section, t_section, rule_section = input_str.strip().split("#")
        self.non_terminals = nt_section.split(";")
        self.terminals = t_section.split(";")

        for nt in self.non_terminals:
            self.non_terminal_map[nt] = NonTerminal(nt)

        rules = rule_section.split(";")
        for rule in rules:
            nt, productions = rule.split("/")
            for prod in productions.split(","):
                self.non_terminal_map[nt].add_rule(prod)

    def eliminate_left_recursion(self):
        nts = self.non_terminals
        for i in range(len(nts)):
            Ai = self.non_terminal_map[nts[i]]
            for j in range(i):
                Aj = self.non_terminal_map[nts[j]]
                self._substitute(Ai, Aj)
            self._eliminate_immediate(Ai)

    def _substitute(self, Ai, Aj):
        new_rules = []
        Aj_name = Aj.get_name()
        Aj_rules = Aj.get_rules()
        for rule in Ai.get_rules():
            if rule.startswith(Aj_name):
                suffix = rule[len(Aj_name):]
                for Aj_rule in Aj_rules:
                    new_rules.append(Aj_rule + suffix)
            else:
                new_rules.append(rule)
        Ai.set_rules(new_rules)

    def _eliminate_immediate(self, A):
        name = A.get_name()
        rules = A.get_rules()
        alpha = []
        beta = []

        for rule in rules:
            if rule.startswith(name):
                alpha.append(rule[len(name):])
            else:
                beta.append(rule)

        if not alpha:
            return

        new_name = name + "'"
        new_A_rules = []
        new_A_prime_rules = []

        for b in beta:
            new_A_rules.append(b + new_name)
        for a in alpha:
            new_A_prime_rules.append(a + new_name)
        new_A_prime_rules.append("e")

        A.set_rules(new_A_rules)
        new_A = NonTerminal(new_name)
        new_A.set_rules(new_A_prime_rules)

        self.non_terminals.append(new_name)
        self.non_terminal_map[new_name] = new_A

    def toString(self):
        # Non-terminals
        nts_str = ";".join(self.non_terminals)
        # Terminals
        ts_str = ";".join(self.terminals)
        # Rules
        rules_str = []
        for nt in self.non_terminals:
            rule_obj = self.non_terminal_map[nt]
            productions = ",".join(rule_obj.get_rules())
            rules_str.append(f"{nt}/{productions}")
        return f"{nts_str}#{ts_str}#{';'.join(rules_str)}"


if __name__ == "__main__":
    # Example input string
    # input_string = "S#a;b;c;d#S/Sa,Sb,c,d"
    input_string = "S;T;L#a;b;c;d;i#S/ScTi,La,Ti,b;T/aSb,LabS,i;L/SdL,Si"

    cfg = CFG(input_string)
    cfg.eliminate_left_recursion()
    print(cfg.toString())