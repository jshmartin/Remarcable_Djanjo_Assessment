from django.db import models

# Create your models here.
class Category(models.Model):
    """
    product category (e.g. "Electronics", "Housewares","Clothing").

    - no FKey; referenced by Product via FKey
    - unique set to true; prevents dupes which can get confusing and messy
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Display name of the category (must be unique)",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

        def __str__(self) -> str:
            return self.name
        
class Tag(models.Model):
    """
    a label that can be applied to products (e.g. "new", "featured", "sale")

    - no FKey; referenced by Product
    - unique set to true; prevents dupes of tags which can get confusing and messy
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="short label for tag (must be unique)",
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

        def __str__(self) -> str:
            return self.name  
        
class Product(models.Model):

    name = models.CharField(
        max_length=150,
        help_text="Full name of the product.",
    )

    description = models.CharField(
        max_length=255,
        help_text="Description of the product.",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        help_text="The single category this product belongs to. (REQUIRED)",
    )
 
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="products",
        help_text="Zero or more tags applied to this product.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp set once when the product is first created.",
    )
 
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp updated automatically every time changes to product is saved.",
    )
 
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]
 
    def __str__(self) -> str:
        return self.name