import sonpy

def main():
    snt = sonpy.sonnet()
    snt.setSonnetInstallationPath('C:\\Program Files\\Sonnet Software\\18.53\\bin')
    snt.setSonnetFilePath(".")
    snt.setSonnetFile("example3.son")
    snt.readProject()
    # Give the project file a new name to not overwrite the original
    snt.setSonnetFile("example3_new.son")

    snt.addPort(15.0, 9.225)
    snt.addPoly([(5, 5), (6, 5), (6, 6), (5, 6), (5, 5)], "Metal1")

    snt.setFrequencySweep(f1=4, f2=6)
    snt.setOutput(filename="example3.csv", partype="S", parform="RI")
    snt.printProject()  # Not actually required, also called from runSimulationStatusMonitor()
    snt.runSimulationStatusMonitor()
    # Sonnet should now open, run the simulation and save the data to example3.csv

if __name__ == "__main__":
    main()
