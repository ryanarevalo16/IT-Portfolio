# IT Help Desk Analytics Dashboard

## Overview

This project simulates a help desk reporting system using Python. It analyzes support tickets and generates metrics commonly used by IT teams to monitor performance and service levels.

## Features

- Total ticket count
- Open vs closed ticket tracking
- Average resolution time
- SLA compliance reporting
- Overdue ticket detection
- Ticket category analysis
- Automated chart generation

## Technologies Used

- Python
- pandas
- matplotlib

## Files

- `tickets.csv` - sample help desk ticket data
- `helpdesk_report.py` - reporting and analytics script
- `ticket_status_pie.png` - ticket status visualization
- `ticket_categories_bar.png` - category breakdown chart

## Example Insights

- Tracks ticket volume
- Measures resolution performance
- Identifies overdue support requests
- Monitors SLA compliance

## How to Run

```bash
pip install -r requirements.txt
python3 helpdesk_report.py
