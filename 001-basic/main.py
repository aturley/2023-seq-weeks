import basic
import debouncer
import scroll_view
import picoscroll as scroll
from machine import Timer
from machine import Pin

def main():
    scroll.init()

    sv = basic.SequencerView()
    bs = basic.BasicSequencer(2, 16, sv)
    ps = basic.PhysicalSequencer(bs, 2, 16)

    pa = Pin(12, Pin.IN, Pin.PULL_UP)
    pb = Pin(13, Pin.IN, Pin.PULL_UP)
    px = Pin(14, Pin.IN, Pin.PULL_UP)
    py = Pin(15, Pin.IN, Pin.PULL_UP)

    

    debouncer_a = debouncer.Debouncer()
    debouncer_b = debouncer.Debouncer()
    debouncer_x = debouncer.Debouncer()
    debouncer_y = debouncer.Debouncer()

    rled = Pin(6, Pin.OUT, Pin.PULL_UP)
    gled = Pin(7, Pin.OUT, Pin.PULL_UP)

    rled.high()
    gled.high()
    
    def cycle(t):
        bs.step()

        notes = bs.get_cur_notes()
        for (led, n) in [(rled, notes[0]), (gled, notes[1])]:
            if not n:
                led.high()
            else:
                led.low()
        
        bs.update_view()
        scroll_view.draw_view_to_scroll(sv, scroll)
        scroll.update()

    def button_handler(debouncer, action):
        if debouncer.down():
            action()
            bs.update_view()
            scroll_view.draw_view_to_scroll(sv, scroll)
            scroll.update()

    def button_handler_a(pin):
        button_handler(debouncer_a, ps.cursor_left)

    def button_handler_b(pin):
        button_handler(debouncer_b, ps.cursor_right)

    def button_handler_x(pin):
        button_handler(debouncer_x, ps.toggle_t0)

    def button_handler_y(pin):
        button_handler(debouncer_y, ps.toggle_t1)

    pa.irq(trigger = Pin.IRQ_FALLING, handler = button_handler_a)
    pb.irq(trigger = Pin.IRQ_FALLING, handler = button_handler_b)
    px.irq(trigger = Pin.IRQ_FALLING, handler = button_handler_x)
    py.irq(trigger = Pin.IRQ_FALLING, handler = button_handler_y)

    tim = Timer()

    tim.init(period=500, callback=cycle)
    
