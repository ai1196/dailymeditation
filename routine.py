import random
import itertools
import meditationvideos


class MeditationRoutine(object):
    def __init__(self, name, instructions, meditations):
        self.name = name
        self.instructions = instructions
        self.meditations = meditations

        self.meditations_for_routine = []

    def get_meditations(self):
        if not self.meditations_for_routine:
            self.meditations_for_routine.append(random.choice(self.meditations))
            
        return self.meditations_for_routine

    def as_html(self):
        meditations_formatted = ''.join(
            [f"<li>{meditation}</li>" for meditation in self.get_meditations()])
        return f"""
            <li><b>{self.name}</b> {self.instructions.rstrip(".")}:
                <ul>
                    {meditations_formatted}
                </ul>
            </li>"""

    def __str__(self):
        return self.as_html()

class SuperMeditationRoutine(MeditationRoutine):

    def __init__(self, name, instructions, meditation_groups):
        _unused_meditation = itertools.chain.from_iterable(meditation_groups)
        super().__init__(name, instructions, _unused_meditation)
        self.meditations_groups = meditation_groups

    def get_meditations(self):
        if not self.meditations_for_routine:
            for meditation_group in self.meditations_groups:
                self.meditations_for_routine.append(random.choice(meditation_group))

        return self.meditations_for_routine

FullMeditationRoutine = SuperMeditationRoutine(
    name="Full Meditation Routine",
    instructions="Get Zen.",
    meditation_groups=[
        [
            meditationvideos.Monday1,
            meditationvideos.Monday3,
        ], [
            meditationvideos.Monday2,
        ]
    ]
)

TotalMeditationRoutine = MeditationRoutine(
    name="Total Meditation Routine",
    instructions="Find your Inner Peace!",
    meditations=[
            meditationvideos.Tuesday1,
            meditationvideos.Tuesday2,
    ]
)
