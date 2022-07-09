jobs = [int(el) for el in input().split(", ")]
index_of_job_of_interest = int(input())

jobs_as_states = list(enumerate(jobs))

time_cycles = 0

for job in sorted(jobs_as_states, key=lambda x: (x[1], x[0])):
    index_of_job, time_for_job = job
    time_cycles += time_for_job
    if index_of_job == index_of_job_of_interest:
        break

print(time_cycles)
