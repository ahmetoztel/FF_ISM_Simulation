import numpy as np
import random
import matplotlib.pyplot as plt


def ffism_fism_simulation():
    replications = int(input("Enter the number of replications: "))
    DSS = []

    for w in range(replications):
        z = random.randint(5, 20)  # Number of experts
        x = random.randint(10, 30)  # Number of factors

        # Initialize matrices
        rndmat = np.zeros((x, x, z), dtype=int)
        FFExpert = np.zeros((x, x, z), dtype=object)
        FExpert = np.zeros((x, x, z), dtype=object)
        FFDec = np.zeros((x, x), dtype=object)
        FDec = np.zeros((x, x), dtype=object)
        FFCrispDec = np.zeros((x, x))
        FCrispDec = np.zeros((x, x))
        FIRM = np.zeros((x, x), dtype=int)
        FFIRM = np.zeros((x, x), dtype=int)

        # Fill rndmat and initialize FFExpert and FExpert
        for t in range(z):
            for i in range(x):
                for j in range(x):
                    rndmat[i, j, t] = random.randint(0, 4) if i != j else 4

                    # Fuzzy expert opinions
                    FExpert[i, j, t] = {
                        0: {"Le": 0, "Mi": 0, "Ri": 0.25},
                        1: {"Le": 0, "Mi": 0.25, "Ri": 0.5},
                        2: {"Le": 0.25, "Mi": 0.5, "Ri": 0.75},
                        3: {"Le": 0.5, "Mi": 0.75, "Ri": 1.0},
                        4: {"Le": 0.75, "Mi": 1.0, "Ri": 1.0},
                    }[rndmat[i, j, t]]

                    # Fermatian Fuzzy expert opinions
                    FFExpert[i, j, t] = {
                        0: {"Mf": 0.0, "NMf": 1.0},
                        1: {"Mf": 0.1, "NMf": 0.8},
                        2: {"Mf": 0.4, "NMf": 0.5},
                        3: {"Mf": 0.7, "NMf": 0.2},
                        4: {"Mf": 0.9, "NMf": 0.1},
                    }[rndmat[i, j, t]]

        # Aggregate expert decisions
        for i in range(x):
            for j in range(x):
                Fl, Fm, Fr = 0, 0, 0
                Mf_sum, NMf_sum = 0, 0

                for t in range(z):
                    Fl += FExpert[i, j, t]["Le"]
                    Fm += FExpert[i, j, t]["Mi"]
                    Fr += FExpert[i, j, t]["Ri"]

                    Mf_sum += FFExpert[i, j, t]["Mf"]
                    NMf_sum += FFExpert[i, j, t]["NMf"]

                FDec[i, j] = {"Le": Fl / z, "Mi": Fm / z, "Ri": Fr / z}
                FCrispDec[i, j] = (FDec[i, j]["Le"] + 2 * FDec[i, j]["Mi"] + FDec[i, j]["Ri"]) / 4

                FFDec[i, j] = {"Mf": Mf_sum / z, "NMf": NMf_sum / z}
                FFCrispDec[i, j] = (1 + 2 * (FFDec[i, j]["Mf"] ** 3) - (FFDec[i, j]["NMf"] ** 3)) / 3

        # Compute thresholds
        FFThreshold = np.sum(FFCrispDec) / (x * x)
        FuzzyThreshold = np.sum(FCrispDec) / (x * x)

        # Generate binary reachability matrices
        FFIRM = (FFCrispDec >= FFThreshold).astype(int)
        FIRM = (FCrispDec >= FuzzyThreshold).astype(int)
        np.fill_diagonal(FFIRM, 1)
        np.fill_diagonal(FIRM, 1)

        # Compute Dice-Sørensen similarity
        JaccA = np.sum(FFIRM)
        JaccB = np.sum(FIRM)
        Joint = np.sum(np.logical_and(FFIRM, FIRM))
        DSS.append(2 * Joint / (JaccA + JaccB))

    # Calculate average DSS and standard error
    AveDSS = np.mean(DSS)
    SE = np.std(DSS, ddof=1)

    # Visualization
    plt.boxplot(DSS, vert=True, patch_artist=True, showmeans=True, meanline=True)
    plt.title("Dice-Sørensen Similarity: FFISM vs. FISM")
    plt.ylabel("DSS")
    plt.xticks([1], ["Simulation Results"])
    for i, value in enumerate(DSS):
        plt.scatter(1, value, alpha=0.6, color="blue", label="Data Points" if i == 0 else "")
    plt.text(1.1, np.mean(DSS), f"Mean: {np.mean(DSS):.2f}", color="red")
    plt.text(1.1, np.mean(DSS) - np.std(DSS), f"SD: {np.std(DSS, ddof=1):.2f}", color="green")
    plt.text(1.1, min(DSS), f"Replications: {len(DSS)}", color="blue")
    plt.legend()
    plt.show()

    return AveDSS, SE


# Example usage
average_dss, standard_error = ffism_fism_simulation()
print(f"Average DSS: {average_dss}")
print(f"Standard Error: {standard_error}")
