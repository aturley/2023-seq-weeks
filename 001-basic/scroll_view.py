def draw_view_to_scroll(view, scroll):
    ba = bytearray();
    for i in range(len(view.tracks[0])):
        ba.append(((view.tracks[0][i] > 0) << 1) + ((view.tracks[1][i] > 0) << 2))

    scroll.show_bitmap_1d(ba, 16, 0)
    scroll.set_pixel(view.cur_pos, 3, 32)

