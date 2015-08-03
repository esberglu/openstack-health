from django.conf.urls import patterns, include, url

from .results import ResultsView
from .timeline import TimelineView
from .aggregate import AggregateResultsView

from .api import (TempestRunTreeEndpoint,
                  TempestRunRawEndpoint,
                  TempestRunDetailsEndpoint)


urlpatterns = patterns('',
    url(r'^results_(?P<run_id>\d+).html$',
        ResultsView.as_view(),
        name='tempest_results'),
    url(r'^timeline_(?P<run_id>\d+).html$',
        TimelineView.as_view(),
        name='tempest_timeline'),

    url(r'^api_tree_(?P<run_id>\d+).json$',
        TempestRunTreeEndpoint.as_view(),
        name='tempest_api_tree'),
    url(r'^api_raw_(?P<run_id>\d+).json$',
        TempestRunRawEndpoint.as_view(),
        name='tempest_api_raw'),
    url(r'^api_details_(?P<run_id>\d+).json$',
        TempestRunDetailsEndpoint.as_view()),
    url(r'^api_details_(?P<run_id>\d+)_(?P<test_name>[^/]+).json$',
        TempestRunDetailsEndpoint.as_view()),

    url(r'^aggregate.html$',
        AggregateResultsView.as_view(),
        name='tempest_aggregate_results'),
)
