import pandas as pd
from django.core.management.base import BaseCommand
from itinerary.models import Activity, District

class Command(BaseCommand):
    help = 'Import activity data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'itinerary/csvdata/activities.csv'

        # Read CSV file
        df = pd.read_csv(file_path)

        activities_to_create = []  # List to store Activity objects for bulk insert

        for _, row in df.iterrows():
            # Ensure the district exists
            district, _ = District.objects.get_or_create(name=row['District'])

            # Create Activity object (DO NOT check for duplicates)
            activities_to_create.append(Activity(
                district=district,
                name=row['Place'],
                category=row['Category']
            ))

        # Bulk insert all activities at once (More Efficient)
        Activity.objects.bulk_create(activities_to_create)

        self.stdout.write(self.style.SUCCESS('Successfully imported all activity data, including duplicates!'))
