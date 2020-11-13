from django.contrib import admin
from .models import Post
# Register your models here.


"""Though it does the work, we can customize the way data is displayed in the administration panel according to our convenience. Open the admin.py file again and replace it with the code below."""

#This will make our admin dashboard more efficient. Now if you visit the post list, you will see more details about the Post.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

"""Note that I have added a few posts for testing.

The list_display attribute does what its name suggests display the properties mentioned in the tuple in the post list for each post.

If you notice at the right, there is a filter which is filtering the post depending on their Status this is done by the list_filter method.

And now we have a search bar at the top of the list, which will search the database from the search_fields attributes. The last attribute prepopulated_fields populates the slug, now if you create a post the slug will automatically be filled based upon your title.

Now that our database model is complete we need to create the necessary views, URLs, and templates so we can display the information on our web application.

"""