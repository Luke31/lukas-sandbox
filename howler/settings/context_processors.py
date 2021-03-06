from django.conf import settings


def global_settings(request):
    http_start = 'http://'
    es_host = ''.join((settings.ES_HOSTS[0], ':', str(settings.ES_DEFAULT_PORT)))
    kibana_host = ''.join((settings.ES_HOSTS[0], ':', '5601'))
    dashboard_main = '/goto/bc0525132fd567e59cd41318099b547a'
    dashboard_irc_main = '/goto/b84358b29112e62fc484fa1af1bed080'
    return {
        'http_es_settings': ''.join(
            (http_start, es_host, '/', settings.ES_SUPPORTED_INDEX_PREFIX['email'].format('*'), '/_settings?pretty')),
        'http_es_indices': ''.join(
            (http_start, es_host, '/_cat/indices?v')),
        'http_kibana': ''.join(
            (http_start, kibana_host)),
        'http_kibana_dashboard': ''.join(
            (http_start, kibana_host, dashboard_main)),
        'http_kibana_irc_dashboard': ''.join(
            (http_start, kibana_host, dashboard_irc_main)),
        'http_kuromoji_analyze_test': ''.join(
            (http_start, es_host, '/', settings.ES_SUPPORTED_INDEX_PREFIX['email'].format('ja'), '/_analyze?pretty=true&analyzer=kuromoji_custom')),
        'http_kuromoji_analyze_test_irc': ''.join(
            (http_start, es_host, '/', settings.ES_SUPPORTED_INDEX_PREFIX['irc'].format(''),
             '/_analyze?pretty=true&analyzer=kuromoji_custom')),
    }
