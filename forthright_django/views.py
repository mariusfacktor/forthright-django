
from rest_framework.decorators import api_view
from django.http import HttpResponse
import pickle
import inspect


'''
# Hold on to the name of the module which instantiated the forthright_server object
# because this is where the class definition should be located when unserializing custom objects
g_caller_module_name = ''

g_exported_functions_dict = {}

# https://stackoverflow.com/questions/50465106/attributeerror-when-reading-a-pickle-file
class MyCustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):

        # If there's a custom object in the bytes_stream, 
        # change the module name to the name of the module that instantiated this forthright_server object
        # because that's where the class should be defined

        global g_caller_module_name

        module_name = g_caller_module_name
        return super().find_class(module_name, name)


def serialize_arguments(*args):

    args_tuple = tuple(args)
    args_serialized = pickle.dumps(args_tuple)

    return args_serialized

def unserialize_arguments_server(args_serialized):

    import io
    bytes_stream = io.BytesIO(args_serialized)

    unpickler = MyCustomUnpickler(bytes_stream)
    args_tuple = unpickler.load()

    return args_tuple



class forthright_server:
    def __init__(self):
        self.exported_functions_dict = {}

        # Get module name of caller
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        module_name = module.__name__

        global g_caller_module_name
        g_caller_module_name = module_name


    def export_functions(self, *funcs):

        global g_exported_functions_dict

        for func in funcs:
            self.exported_functions_dict[func.__name__] = func

        g_exported_functions_dict = self.exported_functions_dict
'''


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




