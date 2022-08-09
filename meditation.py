
import routine


class Meditation(object):

    def __init__(self, name, routines):
        self.name = name
        self.routines = routines

    def as_html(self):
        routines_formatted = ''.join([routine.as_html() for routine in self.routines])
        html = f"""
            <p><b>{self.name}</b></p>
            <p>Make sure you try clearing out your mind before beginning. Try this video: <a href="https://www.youtube.com/watch?v=ez3GgRqhNvA">Decompress</a>!</p>
            <ul>
                {routines_formatted}
            </ul>"""

        return html

    def __str__(self):
        return self.as_html()

TotalMeditation = Meditation(
    name= "Total Meditation",
    routines=[
        routine.FullMeditationRoutine,
    ] 
)