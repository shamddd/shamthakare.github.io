import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="recovery-eval", description="State-Matched Reasoning Evaluation Framework")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("register-states", help="Register recovery and control states")
    subparsers.add_parser("match", help="Perform deterministic covariate state matching")
    subparsers.add_parser("verify", help="Execute AST / sandbox verifiers")
    subparsers.add_parser("analyze", help="Compute paired continuation contrasts")
    subparsers.add_parser("audit", help="Audit dataset exposure and provenance")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    print(f"Executing command: {args.command}")

if __name__ == "__main__":
    main()
