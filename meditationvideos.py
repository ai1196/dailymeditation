class Meditation(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def as_html(self):
        return f"{self.name} (<a href=\"{self.url}\">example<\a>)"
    
    def __str__(self):
        return self.as_html()

Monday1 = Meditation(
    "Monday Part 1",
    "https://www.youtube.com/watch?v=D3SvzgXLtro")

Monday2 = Meditation(
    "Monday Part 2",
    "https://www.youtube.com/watch?v=t2nmbIk9umw")

Monday3 = Meditation(
    "Monday Part 3",
    "https://www.youtube.com/watch?v=xcfzR8JhA6k")

Tuesday1 = Meditation(
    "Tuesday Part 1",
    "https://www.youtube.com/watch?v=3Y2kASh6ZVc")

Tuesday2 = Meditation(
    "Tuesday Part 2",
    "https://www.youtube.com/watch?v=dza092wAp-8")

Wednesday1 = Meditation(
    "Wednesday Part 1",
    "https://www.youtube.com/watch?v=q57JIsSlYZA")

Wednesday2 = Meditation(
    "Wednesday Part 2",
    "https://www.youtube.com/watch?v=Wzt5KPgzRXg")

Thursday1 = Meditation(
    "Thursday Part 1",
    "https://www.youtube.com/watch?v=u4E9g1RNKiM")

Thursday2 = Meditation(
    "Monday Part 2",
    "https://www.youtube.com/watch?v=P6QtCUG5m-Y")

Friday1 = Meditation(
    "Friday Part 1",
    "https://www.youtube.com/watch?v=N8_VxisNF9U")

Friday2 = Meditation(
    "Friday Part 2",
    "https://www.youtube.com/watch?v=xiaiKmWuDWM")

Saturday1 = Meditation(
    "Saturday Part 1",
    "https://www.youtube.com/watch?v=_WUbwFHFxdA")

Saturday2 = Meditation(
    "Saturday Part 2",
    "https://www.youtube.com/watch?v=Q2ySOyy-xw0")

Sunday1 = Meditation(
    "Saturday Part 1",
    "https://www.youtube.com/watch?v=EBmdHKJ-X8c")

Sunday2 = Meditation(
    "Sunday Part 2",
    "https://www.youtube.com/watch?v=zjoBumC6RtI")