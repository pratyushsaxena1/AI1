import concurrent.futures
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout.strip().split('\n')[-1]
    except subprocess.CalledProcessError as e:
        return f"Error: {e}\nCommand: {e.cmd}"

def main():
    num_runs = 10
    commands = [
        f"python '5 Saxena Pratyush unit_4_blue_1.py' 'BEST' 'RANDOM'" for _ in range(num_runs)
    ]
    commands.extend([
        f"python '5 Saxena Pratyush unit_4_blue_1.py' 'BEST' 'AGGRESSIVE'" for _ in range(num_runs)
    ])
    commands.extend([
        f"python '5 Saxena Pratyush unit_4_blue_1.py' 'RANDOM' 'BEST'" for _ in range(num_runs)
    ])
    commands.extend([
        f"python '5 Saxena Pratyush unit_4_blue_1.py' 'AGGRESSIVE' 'BEST'" for _ in range(num_runs)
    ])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(run_command, commands))

    print(results[0])
    print(results[1])
    print(results[2])
    print(results[3])
    print(results[4])
    print(results[5])
    print(results[6])
    print(results[7])
    print(results[8])
    print(results[9])

    # Add a blank line between the two sets of prints

    print()

    print(results[10])
    print(results[11])
    print(results[12])
    print(results[13])
    print(results[14])
    print(results[15])
    print(results[16])
    print(results[17])
    print(results[18])
    print(results[19])

    # Add another blank line

    print()

    print(results[20])
    print(results[21])
    print(results[22])
    print(results[23])
    print(results[24])
    print(results[25])
    print(results[26])
    print(results[27])
    print(results[28])
    print(results[29])

    # Add one more blank line

    print()

    print(results[30])
    print(results[31])
    print(results[32])
    print(results[33])
    print(results[34])
    print(results[35])
    print(results[36])
    print(results[37])
    print(results[38])
    print(results[39])


if __name__ == "__main__":
    main()