import csv

from django.apps import apps
from django.core.management.base import BaseCommand

"""python manage.py loadfile --path "./static/data/genre.csv"""
""" --model_name "Genre"""


class Command(BaseCommand):
    help = "Creating model objects according the file path specified"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")
        parser.add_argument("--model_name", type=str, help="model name")

    # noqa: C901
    def handle(self, *args, **options):  # noqa: C901
        file_path = options["path"]
        _model = apps.get_model("reviews", options["model_name"])
        with open(file_path, "r", encoding="utf8") as csv_file:
            reader = csv.reader(csv_file, delimiter=";", quotechar="|")
            header = next(reader)
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                opts = _model._meta
                other_fields = [
                    field for field in opts.get_fields() if field.many_to_one
                ]
                id = _object_dict.get("id")
                try:
                    obj = _model.objects.get(pk=id)
                    print("запись уже существует!", obj)
                    continue
                except _model.DoesNotExist:
                    try:
                        if other_fields:
                            for field in other_fields:
                                print(field.name)
                                rel_model = opts.get_field(
                                    field.name
                                ).related_model
                                print(rel_model)
                                try:
                                    rel_obj = rel_model.objects.get(
                                        id=_object_dict.get(field.name)
                                    )
                                except rel_model.DoesNotExist:
                                    rel_obj = rel_model.objects.create(
                                        id=_object_dict.get(field.name)
                                    )

                                _object_dict.update({field.name: rel_obj})
                    except _model.DoesNotExist:
                        pass
                    obj = _model.objects.create(**_object_dict)
                    print("создали запись")
                except _model.MultipleObjectsReturned:
                    print("неуникальный ключx`", id)
                    pass
