import argparse

def parser_args():
    parser = argparse.ArgumentParser(description="Bu gostermelik program")
    parser.add_argument('--batch_size', type=str, required=True, help="batch_size sagla")
    return parser.parse_args()

def main():
    args = parser_args()

    print(f"batch_size:{args.batch_size}")

if __name__ == '__main__':
    main()


