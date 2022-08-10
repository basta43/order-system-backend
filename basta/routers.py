from rest_framework.routers import DefaultRouter


from products.viewsets import ProductGenericViewSet, ProductViewSet

router = DefaultRouter()
router.register('product-abc', ProductGenericViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
