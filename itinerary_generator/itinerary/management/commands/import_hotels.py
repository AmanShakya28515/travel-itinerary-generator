import pandas as pd
from django.core.management.base import BaseCommand
from itinerary.models import Hotel, District

class Command(BaseCommand):
    help = 'Import hotel data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'itinerary/csvdata/hotels.csv'

        # Read the CSV file
        df = pd.read_csv(file_path)

        hotels_to_create = []  # List to store Hotel objects for bulk insert

        for _, row in df.iterrows():
            # Ensure the district exists
            district, _ = District.objects.get_or_create(name=row['District'])

            # Create Hotel object (DO NOT check for duplicates)
            hotels_to_create.append(Hotel(
                district=district,
                name=row['Hotel Name'],
                budget_category=row['Budget Category'],
                price_range=row['Price Range (NPR)'],
                hotel_type=row['Hotel Type']
            ))

        # Bulk insert all hotels at once (Much Faster)
        Hotel.objects.bulk_create(hotels_to_create)

        self.stdout.write(self.style.SUCCESS('Successfully imported all hotel data, including duplicates!'))
