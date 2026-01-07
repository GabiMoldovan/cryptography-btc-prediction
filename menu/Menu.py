from service.CSVService import CSVService
from service.DailyReportService import DailyReportService
from service.PredictionService import PredictionService


class Menu:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        self.__daily_report_service = DailyReportService()
        self.__csv_service = CSVService()
        self.__prediction_service = PredictionService()
        self._initialized = True

    @staticmethod
    def print_array_of_daily_reports(daily_reports):
        for daily_report in daily_reports:
            print(daily_report.toString())


    def menu(self):
        while True:
            print("=" * 60)
            print("Project Cryptography BTC Prediction Menu")
            print("=" * 60)
            print("0. Parse CSV files to store BTC values (deletes old values)")
            print("1. Show BTC values for a year [2020-2025]")
            print("2. Run prediction model for year 2026")
            print("3. Exit")
            option = input("Select an option: ")

            if option == "0":
                self.__daily_report_service.delete_everything_from_database()
                self.__csv_service.parse_csvs()

            elif option == "1":
                year = int(input("Enter year: "))
                results =  self.__daily_report_service.get_annual_report(year)
                self.print_array_of_daily_reports(results)


            elif option == "2":
                print("Running prediction model for 2026...")
                try:
                    predictions_df = self.__prediction_service.generate_predictions_for_2026()
                    print("\nPrediction completed successfully!")
                    print(f"Generated {len(predictions_df)} daily predictions for 2026.")
                except Exception as e:
                    print(f"Error during prediction: {e}")

            elif option == "3":
                exit()
