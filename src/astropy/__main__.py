import argparse
import logging
import sys

# Logger
log = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='output debug log messages to stderr')

    # Parse
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(format='%(relativeCreated)d ms [%(levelname)s:%(name)s] %(message)s',
                            level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=logging.INFO)

    log.debug(f'args: {args}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
