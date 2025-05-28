import argparse
from pathlib import Path
import pandas as pd
from src.views import index
from src.reports import spend_by_category
from src.services import (
    simple_search,
    investment_bank,
    phone_search,
    people_transfer_search
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Coursework 1 CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Парсер для команды index
    index_parser = subparsers.add_parser('index', help='Show index page with transactions')
    index_parser.add_argument(
        "--datetime",
        default="2023-12-15 15:30:00",
        help="Datetime 'YYYY-MM-DD HH:MM:SS'"
    )
    index_parser.add_argument(
        "--file",
        default=str(Path(__file__).resolve().parent.parent / "data" / "operations.xlsx"),
        help="Path to transactions file"
    )

    # Парсер для команды report
    report_parser = subparsers.add_parser('report', help='Generate spending report')
    report_parser.add_argument(
        "--file",
        default=str(Path(__file__).resolve().parent.parent / "data" / "transactions.xlsx"),
        help="Path to transactions file"
    )
    report_parser.add_argument(
        "--category",
        default="Супермаркеты",
        help="Spending category"
    )

    # Парсеры для сервисов
    subparsers.add_parser('simple_search', help='Simple search service')
    subparsers.add_parser('investment_bank', help='Investment bank service')
    subparsers.add_parser('phone_search', help='Phone number search service')
    subparsers.add_parser('people_transfer', help='People transfer service')

    args = parser.parse_args()

    if args.command == 'index':
        print(index(args.datetime, args.file))
    elif args.command == 'report':
        if Path(args.file).exists():
            df = pd.read_excel(args.file)
            print(spend_by_category(df, category=args.category))
        else:
            print("Нет файла с транзакциями, пропускаем отчёт.")
    elif args.command == 'simple_search':
        print(simple_search())
    elif args.command == 'investment_bank':
        print(investment_bank())
    elif args.command == 'phone_search':
        print(phone_search())
    elif args.command == 'people_transfer':
        print(people_transfer_search())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
