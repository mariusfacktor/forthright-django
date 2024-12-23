
from rest_framework.decorators import api_view
from django.http import HttpResponse


from forthright_server import g_exported_functions_dict


@api_view(['PUT'])
def get_data(request):

    global g_exported_functions_dict

    data = request.body
    unserialized = unserialize_arguments_server(data)


    function_name = unserialized[0]
    input_kwargs = unserialized[1]
    input_args = unserialized[2:]

    try:
        outputs = g_exported_functions_dict[function_name](*input_args, **input_kwargs)
    except KeyError:
        raise KeyError('forthright: %s() not found. Use forthright_server.export_functions(%s)' %(function_name, function_name))


    outputs_serialized = serialize_arguments(outputs)

    return HttpResponse(outputs_serialized, content_type='application/octet-stream')




