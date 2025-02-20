with open("inputs.txt", "r") as f:
    val1 = float(f.readline())
    val2 = float(f.readline())

    with open("outputs.txt", "w") as of:
        txt = f"{val1} + {val2} = {val1 + val2}"
        of.write(txt + "\n")

        txt = f"{val1} - {val2} = {val1 - val2}"
        of.write(txt + "\n")

        txt = f"{val1} * {val2} = {val1 * val2}"
        of.write(txt + "\n")

        txt = f"{val1} / {val2} = {val1 / val2}"
        of.write(txt + "\n")

        txt = f"{val1} // {val2} = {val1 // val2}"
        of.write(txt + "\n")

        txt = f"{val1} ** {val2} = {val1 ** val2}"
        of.write(txt + "\n")

        txt = f"{val1} % {val2} = {val1 % val2}"
        of.write(txt + "\n")

print("Output generated!")
