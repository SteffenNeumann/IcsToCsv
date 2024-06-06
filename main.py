import csv
from ics import Calendar
def ics_to_csv(ics_file, csv_file):
    with open(ics_file, 'r') as ics:
        calendar = Calendar(ics.read())
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['start_datetime', 'end_datetime', 'summary', 'description', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for event in calendar.events:
            writer.writerow({
                'start_datetime': event.begin.to('local').format('YYYY-MM-DD HH:mm:ss'),
                'end_datetime': event.end.to('local').format('YYYY-MM-DD HH:mm:ss'),
                'summary': event.name,
                'description': event.description,
                'location': event.location
            })
if __name__ == "__main__":
    ics_file = 'dein_dateiname.ics'
    csv_file = 'output.csv'
    ics_to_csv(ics_file, csv_file)
    print(f"Die Daten wurden erfolgreich von {ics_file} nach {csv_file} konvertiert.")
