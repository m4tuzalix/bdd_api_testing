from lib.pages.api_get import Api_GET
from lib.pages.api_post import Api_POST
from lib.pages.api_delete import Api_DELETE
from lib.pages.api_patch import Api_PATCH

def before_tag(context, tag):
     url = "http://192.168.99.100:8080/apps/" #// please change the adress
     if tag == "api_GET":
          context.method = Api_GET(url)
     elif tag == "api_POST":
          context.method = Api_POST(url)
     elif tag == "api_DELETE":
          context.method = Api_DELETE(url)
     elif tag == "api_PATCH":
          context.method = Api_PATCH(url)

def after_all(context):
     print("Finished testing. All error have been reported in bug-reports folder")
