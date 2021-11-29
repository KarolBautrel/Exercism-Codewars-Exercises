def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False


print(is_criticality_balanced(750, 600))


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    Efficiency = (generated_power/theoretical_max_power)*100
    if Efficiency >= 80:
        return "green"
    elif Efficiency < 80 and Efficiency >= 60:
        return"orange"
    elif Efficiency < 60 and Efficiency >= 30:
        return"red"
    elif Efficiency < 30:
        return"black"


print(reactor_efficiency(200, 50, 15000))


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    balance = temperature * neutrons_produced_per_second
    if balance < (threshold*0.9):
        return "LOW"
    elif threshold*0.9 <= balance <= threshold * 1.1:
        return "NORMAL"
    else:
        return "DANGER"


print(fail_safe(temperature=10, neutrons_produced_per_second=1101, threshold=10000))
