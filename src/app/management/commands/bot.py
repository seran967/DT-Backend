from django.core.management.base import BaseCommand

from app.internal.bot import run_bot


class Command(BaseCommand):
    help = "Run telegram bot"

    def handle(self, *args, **options):
        run_bot()
