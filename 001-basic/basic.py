import time

class Track:
    def __init__(self, size):
        self.size = size
        self.notes = [0] * size
        
    def get(self, idx):
        return self.notes[idx]

    def put(self, idx, note):
        self.notes[idx] = note

    def __str__(self):
        return " ".join([str(n) for n in self.notes])

class BasicSequencer:
    def __init__(self, track_count, track_size, view = None):
        self.track_count = track_count
        self.track_size = track_size
        self.tracks = []

        self.cur_step = 0

        for i in range(track_count):
            self.tracks.append(Track(self.track_size))

        self.view = view

    def update_view(self):
        if self.view:
            self.view.update([t.notes[:] for t in self.tracks], self.cur_step)

    def step(self):
        self.cur_step = (self.cur_step + 1) % self.track_size
        return self

    def get_step(self):
        return self.cur_step

    def get_cur_notes(self):
        return [t.get(self.cur_step) for t in self.tracks]

    def get_note(self, track, idx):
        return self.tracks[track].get(idx)

    def put_note(self, track, idx, note):
        self.tracks[track].put(idx, note)
        return self
            
class PhysicalSequencer:
    def __init__(self, sequencer, track_count, track_size):
        self.sequencer = sequencer
        self.track_count = track_count
        self.track_size = track_size
        self.note_cursor = 0

    def cursor_left(self):
        if self.note_cursor == 0:
            self.note_cursor = self.track_size - 1
        else:
            self.note_cursor = self.note_cursor - 1

    def cursor_right(self):
        self.note_cursor = (self.note_cursor + 1) % (self.track_size)

    def toggle_tx(self, track):
        n = self.sequencer.get_note(track, self.note_cursor)
        if n == 0:
            self.sequencer.put_note(track, self.note_cursor, 1)
        else:
            self.sequencer.put_note(track, self.note_cursor, 0)

    def toggle_t0(self):
        self.toggle_tx(0)
        
        
    def toggle_t1(self):
        self.toggle_tx(1)

    def __str__(self):
        ts = []
        for t in self.tracks:
            ts.append(t)

        return "\n".join(ts)

class SequencerView:
    def __init__(self):
        self.tracks = []
        self.cur_pos = 0

    def update(self, tracks, cur_pos):
        self.tracks = tracks
        self.cur_pos = cur_pos

    
