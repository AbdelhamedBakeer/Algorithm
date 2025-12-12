import heapq
from dataclasses import dataclass, field

# ========== Patient Class ==========
@dataclass(order=True)
class Patient:
    priority: tuple = field(init=False, repr=False)
    severity: int
    service_time: int
    arrival_time: int
    name: str = field(compare=False)

    def __post_init__(self):
        # ترتيب الأولوية داخل الـ Priority Queue
        self.priority = (-self.severity, self.arrival_time, self.service_time)


# ========== Hospital Priority System ==========
class EmergencyPrioritySystem:
    def __init__(self):
        self.queue = []
        self.time = 0
        self.log = []

    def add_patient(self, patient: Patient):
        heapq.heappush(self.queue, patient)

    def process_patients(self):
        while self.queue:
            patient = heapq.heappop(self.queue)

            start_time = max(self.time, patient.arrival_time)
            finish_time = start_time + patient.service_time

            self.log.append({
                "name": patient.name,
                "arrival": patient.arrival_time,
                "severity": patient.severity,
                "service": patient.service_time,
                "start": start_time,
                "finish": finish_time
            })

            self.time = finish_time

    def print_table(self):
        print("\n=====Emergency Patient Priority Schedule =====\n")
        print("{:<12} {:<10} {:<10} {:<10} {:<10} {:<10}"
              .format("Name", "Arrival", "Severity", "Service", "Start", "Finish"))

        for row in self.log:
            print("{:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                row["name"], row["arrival"], row["severity"],
                row["service"], row["start"], row["finish"]
            ))


# ========== Example Run ==========
if __name__ == "__main__":
    system = EmergencyPrioritySystem()

    print("Enter the number of patients:")
    n = int(input("Number of patients:"))

    for i in range(n):
        print(f"\n Patient data number{i+1}:")
        name = input("name: ")
        severity = int(input("Danger level (1-10):"))
        service = int(input("Duration of examination: "))
        arrival = int(input("Arrival time:"))

        p = Patient(name=name, severity=severity, service_time=service, arrival_time=arrival)
        system.add_patient(p)

    system.process_patients()
    system.print_table()
