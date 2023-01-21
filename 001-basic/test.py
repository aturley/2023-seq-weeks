import pytest
import basic

def test_track_init():
    t = basic.Track(16)
    assert t.size == 16
    assert len(t.notes) == 16

def test_track_put_get():
    t = basic.Track(16)
    for x in range(0, 16, 2):
        t.put(x, 1)

    for x in range(16):
        assert t.get(x) == ((x + 1) % 2)

def test_basic_sequencer_init():
    bs = basic.BasicSequencer(2, 16)
    assert len(bs.tracks) == 2
    assert len(bs.tracks[0].notes) == 16
    assert len(bs.tracks[1].notes) == 16

def test_basic_sequencer_step():
    bs = basic.BasicSequencer(2, 16)

    for x in range(0, 100):
        assert bs.get_step() == (x % 16)
        bs.step()

def test_basic_sequencer_step():
    bs = basic.BasicSequencer(2, 16)

    for x in range(0, 100):
        assert bs.cur_step == (x % 16)
        bs.step()

def test_basic_sequencer_put_note_get_note():
    bs = basic.BasicSequencer(2, 16)

    for t in range(2):
        for x in range(0, 16, 2):
            bs.put_note(t, x, t + 5)

    for x in range(16):
        assert bs.get_note(0, x) == bs.get_cur_notes()[0]
        assert bs.get_note(1, x) == bs.get_cur_notes()[1]

        bs.step()

def test_physical_sequencer_init():
    bs = basic.BasicSequencer(2, 16)
    ps = basic.PhysicalSequencer(bs, 2, 16)

def test_write_song():
    bs = basic.BasicSequencer(2, 16)
    ps = basic.PhysicalSequencer(bs, 2, 16)

    ps.cursor_right()
    # p = 1
    ps.toggle_t0()
    assert str(ps.sequencer.tracks[0]) == "0 1 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    assert str(ps.sequencer.tracks[1]) == "0 0 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    
    ps.cursor_right()
    # p = 2
    ps.toggle_t1()
    assert str(ps.sequencer.tracks[0]) == "0 1 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    assert str(ps.sequencer.tracks[1]) == "0 0 1 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"

    ps.cursor_left()
    # p = 1
    ps.toggle_t1()
    assert str(ps.sequencer.tracks[0]) == "0 1 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    assert str(ps.sequencer.tracks[1]) == "0 1 1 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"

    ps.cursor_left()
    # p = 0
    ps.toggle_t0()
    assert str(ps.sequencer.tracks[0]) == "1 1 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    assert str(ps.sequencer.tracks[1]) == "0 1 1 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"

    ps.cursor_left()
    # p = 15
    ps.toggle_t1()
    assert str(ps.sequencer.tracks[0]) == "1 1 0 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 0"
    assert str(ps.sequencer.tracks[1]) == "0 1 1 0" " 0 0 0 0" " 0 0 0 0" " 0 0 0 1"



    
