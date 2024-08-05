from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200,  # CharField - nechtagacha harf qabul qilishi
                             unique=True,  # yagona yakka
                             verbose_name='Nomlanishi')  # Perevodini chiqarishi

    def __str__(self):
        return self.title

    class Meta:  # Adminkada korinishiga javob beradi
        verbose_name = 'Category'  # Birlikda
        verbose_name_plural = 'Categories'  # Koplikda


class Article(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Kino nomi')
    content = models.TextField(verbose_name='Tarifi')  # TextField - xoxlagancha tekst qoshiladi
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Rasm')  # ImageField - rasm qoshish uchun modelkada
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Qoshilgan vaqti')  # DateTimeField - yaratilgan vaqtini chiqaradi
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Yangilangan vaqti')  # DateTimeField - Yangilangan vaqtini chiqaradi
    publish = models.BooleanField(default=True,
                                  verbose_name='Chop etish')  # BooleanField - Chop etish yoki qimaslig vazifani bajaradi
    views = models.IntegerField(default=0,
                                verbose_name='Korganlar soni')  # IntegerField - Son sanash uchun xizmat qiladi
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Kategoriya')  # ForeignKey - Qaysi modelka berilsa ichida shunga qarashli boladi
    video = models.CharField(max_length=500, default='', verbose_name='Video')

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBhIIBwgVCgkXDQoREAwNDRsUChAWIBIWIiAdHx8YHSggGBolGxUfITEhJSkrLi4uFx8zODMsNygtLisBCgoKBQUFDgUFDisZExkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAMgA3wMBIgACEQEDEQH/xAAbAAEBAQADAQEAAAAAAAAAAAAABQcDBAYBAv/EADoQAQABAwADCwoGAwEAAAAAAAABAgMEBQYREhMWFyExVFWRktEiMjQ1UWFzdLKzBxRBQlKBFTNxI//EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDYgAAAAAAAAAAAAAAAAAAAAAAAAACQkAAAAAAAAAAAAAAAAAAAAAAAAAAAkJAAAAAAAAAAAAAAAAAAAAAAAAAAAJCQAAAAAAAAAAAAAAAAAAAAAAAAAACQkAAAAAAAAAE3TOladFU29uNXfrrubimi3s3Uzs2/qCkIPCDK6gyO7T4nCDL6gyO7T4gvCDwgy+oMju0+Jwgy+oMju0+ILwg8IMvqDI7tPicIMvqDI7tPiC8IPCDL6gyO7T4nCDK6gyO7T4gvDo6H0jRpXBjKt25t0zVcjcVedExOx3gAAAAAACQkAAAAAAAABB1l9PwfnafoleQdZfT8H52n6JBeAAHHTetVXps03Im5EUzNET5URPNthyA47123Yt75eri3bjnqqnZTD842Vj5VG7xr1N2jm20VRNLxf4nzk73Z3O38r/6bdnm7v9Nv9Jn4cfmf83O9bd43qrfP4+7+9oNNfJ5n18nmBD1L9Rx8bK+5K6hal+o4+NlfcldAAAAAAAJCQAAAAAAAAEHWX0/B+dp+iV5B1l9PwfnafokF553WzWa3oWxvNiYuZsxyU89NEe2fA1s1mtaGsbzYmLmbMclP7aI9s+DK8i/dyb83r9c3LkztmqqfKmQdvE0vm4ukv8hbvzORuttVVU7d37Yn3NV1e05jabw99tTuLscly1M+VTPgxx29GaQydGZkZWJXuLkTzftqj2T7gbVes28i3vd+3Fy3PPTXG2mXFbtYejceardujGsxG6qmmmKaY98uhoTWHD0ro+crdxaqpp23aKp8z3/8eD1u1nr0xd/LYtU0YUTyRzVXJ9s+73A93oTWTA0zfrsY9W5uUzVspr5N8p/lCxPMwvHv3ca/F6xXNu5E7YqpnyolqequstvTVjer0xbzKaeWj9tce2PAHLqX6jj42V9yV1C1L9RR8XK+5K6AAAAAAASEgAAAAAAAAPJ/iBlXMHHx8qz/ALKciqY2x5O3cS9Yk6w6Es6cx6bN+7VbimvdRNERy8mz9QZBkX7uTfm9frm5cmds1VTtqmXG0bi8wem3Oyk4vMHptzspBnI0bi8wem3Oyk4vMHptzspBnUV1UxMU1bImNkxE88PjRuLzB6bc7KTi8wem3OykGcuTHv3Ma9F6xXNu5E7YqpnZVEtC4vMHptzspOLzB6bc7KQU9RK5r1bt11ctU3MiZ78vQOjoXRtvROj6cO1XNyiJqmKqvO5Z2u8AAAAAAASEgAAAAAAAAAAAAAAAAAAAAAAAAAAEhIAAAAAAAAAAAAAAAAAAAAAAAAAABISAAAAAAAAAAAAAAAAAAAAAAAAAAASEgAAAAAAAAAAAAAAAAAAAAAAAAAAEhIAAAAAAAAAAAAAAAAAAAAAAAAAABIA//9k="

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
