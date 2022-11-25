from django.http import HttpResponse


# Create your views here.
def main(request):
    server_host = request.META['HTTP_HOST']
    browser_info = request.META['HTTP_USER_AGENT']
    ip_adress = request.META['REMOTE_ADDR']
    return HttpResponse(f"""Server host: {server_host}<br>
                            Browser info: {browser_info}<br>
                            IP address: {ip_adress}
                        """)


def error_page(request):
    return HttpResponse("Произошла ошибка", status=400, reason='Incorrect data')


def user_info(request, login='Kirill', post_name='django project', post_number='1'):
    return HttpResponse(f"""Login: {login}<br>
                            Post name: {post_name}<br>
                            Post number: {post_number}<br>
                        """)
