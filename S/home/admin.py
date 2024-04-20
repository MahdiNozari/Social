from django.contrib import admin
from .models import Post,Comment,Vote


class PostAdmin(admin.ModelAdmin):
    list_display = ('user','slug','updated')
    search_fields = ('slug','body')
    list_filter = ('updated','slug')
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','created','is_reply')
    raw_id_fields = ('user','post','reply')
admin.site.register(Comment,CommentAdmin)

admin.site.register(Vote)