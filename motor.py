def close()
    import uln2003
    s1 = Stepper(HALF_STEP, microbit.pin16, microbit.pin15, microbit.pin14, microbit.pin13, delay=5)
    s1.step(100)

def open()
    import uln2003
    s1 = Stepper(HALF_STEP, microbit.pin16, microbit.pin15, microbit.pin14, microbit.pin13, delay=5)
    s1.step(100,-1)