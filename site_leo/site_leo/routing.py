from channels.routing import ProtocolTypeRouter, URLRouter
import site_leo.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(site_leo.routing.websocket_urlpatterns),
})
