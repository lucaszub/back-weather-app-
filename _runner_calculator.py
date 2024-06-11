from datetime import datetime
from app.utils.date_difference_calculator import DateDifferenceCalculator 
from database_singleton import DatabaseSingleton
from sqlalchemy import func
from model.temperature import Temperature

class TemperatureStatsCalculator:
    def __init__(self, start_date_str, end_date_str):
        self.start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        self.session = DatabaseSingleton().session

    def calculate_stats(self, granularity):
        if granularity == 'jour':
            return self._calculate_daily_stats()
        elif granularity == 'mois':
            return self._calculate_monthly_stats()
        elif granularity == 'trimestre':
            return self._calculate_quarterly_stats()
        elif granularity == 'année':
            return self._calculate_yearly_stats()

    def _calculate_daily_stats(self):
        return self.session.query(
            Temperature.year,
            Temperature.month,
            Temperature.day,
            func.round(func.avg(Temperature.temperature_moyenne), 1).label('avg_temp'),
            func.min(Temperature.temperature_minimale).label('min_temp'),
            func.max(Temperature.temperature_maximale).label('max_temp')
        ).filter(
            (Temperature.year >= self.start_date.year) &
            (Temperature.year <= self.end_date.year) &
            (Temperature.month >= self.start_date.month) &
            (Temperature.month <= self.end_date.month)
        ).group_by(
            Temperature.year,
            Temperature.month,
            Temperature.day
        ).all()

    def _calculate_monthly_stats(self):
        return self.session.query(
            Temperature.year,
            Temperature.month,
            func.round(func.avg(Temperature.temperature_moyenne), 1).label('avg_temp'),
            func.round(func.min(Temperature.temperature_minimale), 1).label('min_temp'),
            func.round(func.max(Temperature.temperature_maximale), 1).label('max_temp')
        ).filter(
            (Temperature.year >= self.start_date.year) &
            (Temperature.year <= self.end_date.year) &
            (Temperature.month >= self.start_date.month) &
            (Temperature.month <= self.end_date.month)
        ).group_by(
            Temperature.year,
            Temperature.month
        ).all()

    def _calculate_quarterly_stats(self):
        return self.session.query(
            Temperature.year,
            ((Temperature.month - 1) // 3 + 1).label('quarter'),
            func.round(func.avg(Temperature.temperature_moyenne), 1).label('avg_temp'),
            func.round(func.min(Temperature.temperature_minimale), 1).label('min_temp'),
            func.round(func.max(Temperature.temperature_maximale), 1).label('max_temp')
        ).filter(
            (Temperature.year >= self.start_date.year) &
            (Temperature.year <= self.end_date.year)
        ).group_by(
            Temperature.year,
            'quarter'
        ).all()

    def _calculate_yearly_stats(self):
        return self.session.query(
            Temperature.year,
            func.round(func.avg(Temperature.temperature_moyenne), 1).label('avg_temp'),
            func.round(func.min(Temperature.temperature_minimale), 1).label('min_temp'),
            func.round(func.max(Temperature.temperature_maximale), 1).label('max_temp')
        ).filter(
            (Temperature.year >= self.start_date.year) &
            (Temperature.year <= self.end_date.year)
        ).group_by(
            Temperature.year
        ).all()

if __name__ == "__main__":
    start_date_str = '2020-02-07'
    end_date_str = '2022-08-03'
    
    calculator = DateDifferenceCalculator(start_date_str, end_date_str)
    granularity = calculator.determine_granularity()
    
    Temperature_calculator = TemperatureStatsCalculator(start_date_str, end_date_str)
    stats = Temperature_calculator.calculate_stats(granularity)

    # Affichage des statistiques
    print("Statistiques:")
    for stat in stats:
        print(stat)
