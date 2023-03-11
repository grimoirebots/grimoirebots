from django.conf import settings
from rest_framework import serializers
from collections import OrderedDict

from .models import Order, Projects, Setup


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ['id', 'order']

    def to_representation(self, instance):
        """GrimoireLab representation."""
        ret = super().to_representation(instance)

        # Remove empty values
        ret = OrderedDict((k, v) for k, v in ret.items() if v not in [None, [], '', {}])
        ret['meta'] = {
            'title': instance.order.title
        }
        ret.move_to_end('meta', False)

        ret_sup = OrderedDict()
        ret_sup[instance.order.id.__str__()] = ret

        return ret_sup


class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setup
        exclude = ['id', 'order']

    def to_representation(self, instance):
        """GrimoireLab representation."""
        ret = OrderedDict()

        ret['general'] = {
            'short_name': instance.order.title,
            'update': False,
            'min_update_delay': 1000,
            'debug': True,
            'logs_dir': '/home/grimoire/logs',
            'bulk_size': 1000,
            'scroll_size': 1000,
            'aliases_file': '/home/grimoire/aliases.json',
        }

        ret['projects'] = {
            'projects_file': '/home/grimoire/conf/projects.json',
        }

        ret['es_collection'] = {
            'url': f'https://{settings.OPENSEARCH["USER"]}:{settings.OPENSEARCH["PASSWORD"]}@{settings.OPENSEARCH["HOST"]}:{settings.OPENSEARCH["PORT"]}',
        }

        ret['es_enrichment'] = {
            'url': f'https://{settings.OPENSEARCH["USER"]}:{settings.OPENSEARCH["PASSWORD"]}@{settings.OPENSEARCH["HOST"]}:{settings.OPENSEARCH["PORT"]}',
            'autorefresh': False,
        }

        ret['phases'] = {
            'collection': True,
            'enrichment': True,
            'identities': False,
            'panels': False,
        }

        ret['git'] = {
            'raw_index': 'git_demo_raw',
            'enriched_index': 'git_demo_enriched',
            'latest-items': True,
            'studies': '[enrich_demography:git, enrich_areas_of_code:git, enrich_onion:git]',
        }

        ret['enrich_demography:git'] = {}

        ret['enrich_areas_of_code:git'] = {
            'in_index': 'git_demo_raw',
            'out_index': 'git-aoc_demo_enriched',
        }

        ret['enrich_onion:git'] = {
            'in_index': 'git_demo_enriched',
            'out_index': 'git-onion_demo_enriched',
            'contribs_field': 'hash',
        }

        return ret
