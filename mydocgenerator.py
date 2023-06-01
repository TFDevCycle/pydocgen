import argparse
from generateDoc import startgenerate

def main():
    parser = argparse.ArgumentParser(description='Generate HTML documentation for Python modules, classes, and methods.')

    startgenerate()

if __name__ == '__main__':
    main()
