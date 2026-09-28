from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait


# ============================================================
# ============================================================
#
#                   EDITABLE SETTINGS
#
# Change values in this section when tuning the robot.
#
# ============================================================
# ============================================================


# ============================================================
# PORTS
# ============================================================

LEFT_MOTOR_PORT = Port.A
RIGHT_MOTOR_PORT = Port.B

ULTRASONIC_PORT = Port.C
COLOR_SENSOR_PORT = Port.D
CAMERA_MOTOR_PORT = Port.F


# ============================================================
# YELLOW OBSTACLE BEHAVIOR
# ============================================================
#
# 0 = turn LEFT
# 1 = turn RIGHT

YELLOW_DIRECTION = 1


# ============================================================
# CAMERA SETTINGS
# ============================================================

CAMERA_FORWARD = -95
CAMERA_DOWN = -135

# degrees per second
CAMERA_SPEED = 80

# Wait after moving camera before reading color.
# milliseconds
CAMERA_SETTLE_TIME = 300

# Wait after returning camera downward.
CAMERA_DOWN_SETTLE_TIME = 150


# ============================================================
# ULTRASONIC SETTINGS
# ============================================================

# FIRST detection distance.
#
# As soon as an obstacle is within this range, obstacle handling
# takes priority over line searching/recovery.
#
# 100 mm = 10 cm
OBSTACLE_DETECTION_DISTANCE = 100

# FINAL distance for color checking.
#
# After the 10 cm detection triggers, the robot drives STRAIGHT
# toward the obstacle until this distance is reached.
#
# Kept at your current calibrated value:
# 50 mm = 5 cm
OBSTACLE_DISTANCE = 50

# Speed used only while approaching from the first detection
# distance to the final 5 cm color-check distance.
#
# Kept separate so you can make the final approach slower/faster
# without changing normal FORWARD_SPEED.
OBSTACLE_APPROACH_SPEED = 100

# After handling an obstacle, the ultrasonic sensor must
# see at least this much free space before it can trigger again.
#
# Prevents detecting the same obstacle twice.
OBSTACLE_REARM_DISTANCE = 100


# ============================================================
# NORMAL FORWARD MOVEMENT
# ============================================================

# degrees per second
FORWARD_SPEED = 170


# ============================================================
# LINE DETECTION
# ============================================================
#
# Calibration:
#
# BLACK approximately = 0
# WHITE approximately = 16
#
#
# <= LINE_FOUND_MAX
# definitely black
#
# between LINE_FOUND_MAX and LINE_LOST_MIN
# uncertain / edge -> continue straight
#
# >= LINE_LOST_MIN
# probably white / outside line

LINE_FOUND_MAX = 5

LINE_LOST_MIN = 10


# Number of consecutive WHITE readings before declaring
# that the robot has actually lost the line.
#
# Higher = more resistant to random readings,
# but reacts more slowly.
LINE_LOST_CONFIRMATIONS = 3


# Number of consecutive BLACK readings required during
# line searching before considering the line found.
LINE_FOUND_CONFIRMATIONS = 2


# ============================================================
# LINE SEARCH / RECOVERY
# ============================================================

# Rotation speed while searching for lost line.
SEARCH_SPEED = 150

# How long to search the first direction.
# milliseconds
SEARCH_SWEEP_TIME = 1000

# When sweeping to the other side, multiply the first sweep.
#
# 2.0 means:
#
# left 550ms
# then right 1100ms
#
# so it crosses the original heading and searches the
# opposite side.
SEARCH_OPPOSITE_MULTIPLIER = 2


# How long to rotate back toward approximately the original
# heading if neither direction finds the line.
SEARCH_RETURN_TIME = 550


# Back up slightly before another search attempt.
SEARCH_BACKUP_SPEED = 100
SEARCH_BACKUP_TIME = 500


# Maximum number of complete search attempts.
SEARCH_ATTEMPTS = 3


# Direction tried first when the robot has no previous
# information.
#
# Change to:
# "LEFT"
# or
# "RIGHT"

DEFAULT_SEARCH_DIRECTION = "LEFT"


# ============================================================
# OBSTACLE BACKUP
# ============================================================

# Speed while moving backward after reading obstacle.
BACKUP_SPEED = 150

# milliseconds
BACKUP_TIME = 1000


# ============================================================
# OBSTACLE TURNING
# ============================================================
#
# Previous test:
#
# TURN_SPEED = 200
# ~1500 ms
#
# gave approximately 90 degrees.
#
# Keep LEFT and RIGHT separate so they can be tuned
# individually.

TURN_SPEED = 200

LEFT_TURN_TIME = 2000
RIGHT_TURN_TIME = 2000


# ============================================================
# FORWARD MOVEMENT AFTER TURN
# ============================================================
#
# After rotating around the obstacle, move forward briefly.
#
# Normal line checking will then resume.
#
# If the sensor is outside the line, the recovery system
# automatically searches for it.

POST_TURN_SPEED = 120
POST_TURN_FORWARD_TIME = 250


# ============================================================
# OBSTACLE COLOR DETECTION
# ============================================================
#
# REAL CALIBRATION AT ~50 mm:
#
# RED
# H = 345-347
# S = 87-88
# V = 5-7
#
# YELLOW
# H = 32
# S = 68
# V = 10
#
# GREEN
# H = 140
# S = 51
# V = 4
#
#
# We deliberately give H considerable tolerance because
# classroom lighting may change.
#
# Brightness/value is NOT used strictly because lighting
# strongly affects V.


# ---------------------------
# RED
# ---------------------------

RED_HUE_CENTER = 346

# Red accepts roughly:
#
# 321 -> 360
# 0   -> 11
#
# because Hue wraps around at 360.
RED_HUE_TOLERANCE = 25


# ---------------------------
# YELLOW
# ---------------------------

YELLOW_HUE_CENTER = 32

# roughly 12 -> 52
YELLOW_HUE_TOLERANCE = 20


# ---------------------------
# GREEN
# ---------------------------

GREEN_HUE_CENTER = 140

# roughly 110 -> 170
GREEN_HUE_TOLERANCE = 30


# ---------------------------
# General HSV safety limits
# ---------------------------
#
# Kept deliberately low because:
#
# GREEN V = 4
# RED V = 5-7
# YELLOW V = 10
#
# Do NOT put V back to 5 or the green obstacle would
# be rejected.

COLOR_MIN_SATURATION = 25
COLOR_MIN_VALUE = 2


# Number of readings per obstacle.
COLOR_SAMPLES = 9

# Delay between readings.
# milliseconds
COLOR_SAMPLE_DELAY = 40


# Minimum number of matching samples required.
#
# With 9 samples:
# 5 means at least a majority.
COLOR_MIN_VALID_VOTES = 5


# If a batch fails, try again before giving up.
COLOR_READ_RETRIES = 3

# Wait between failed color-reading attempts.
COLOR_RETRY_DELAY = 200


# ============================================================
# MAIN LOOP
# ============================================================

# Delay between normal sensor checks.
# milliseconds
MAIN_LOOP_DELAY = 10


# ============================================================
# DEBUG OUTPUT
# ============================================================
#
# True:
# print useful information
#
# False:
# quieter during final testing

DEBUG_PRINT = True


# ============================================================
# ============================================================
#
#                  END OF SETTINGS
#
# Normally you should not need to edit below this point.
#
# ============================================================
# ============================================================


# ============================================================
# HARDWARE INITIALIZATION
# ============================================================

hub = InventorHub()

left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)

ultrasonic = UltrasonicSensor(ULTRASONIC_PORT)
color_sensor = ColorSensor(COLOR_SENSOR_PORT)

camera_motor = Motor(CAMERA_MOTOR_PORT)


# ============================================================
# DEBUG
# ============================================================

def debug(*items):

    if DEBUG_PRINT:
        print(*items)


# ============================================================
# BASIC ROBOT MOVEMENT
# ============================================================

def stop_robot():

    left_motor.brake()
    right_motor.brake()


def move_forward(speed=FORWARD_SPEED):

    # Experimentally confirmed:
    #
    # A negative
    # B positive
    #
    # = forward

    left_motor.run(-speed)
    right_motor.run(speed)


def move_backward(speed=BACKUP_SPEED):

    # Experimentally confirmed:
    #
    # A positive
    # B negative
    #
    # = backward

    left_motor.run(speed)
    right_motor.run(-speed)


def rotate_left(speed=TURN_SPEED):

    # Experimentally confirmed:
    #
    # A positive
    # B positive
    #
    # = counter-clockwise
    # = LEFT

    left_motor.run(speed)
    right_motor.run(speed)


def rotate_right(speed=TURN_SPEED):

    # Experimentally confirmed:
    #
    # A negative
    # B negative
    #
    # = clockwise
    # = RIGHT

    left_motor.run(-speed)
    right_motor.run(-speed)


# ============================================================
# CAMERA MOVEMENT
# ============================================================

def camera_down():

    camera_motor.run_target(
        CAMERA_SPEED,
        CAMERA_DOWN,
        then=Stop.HOLD
    )

    wait(CAMERA_DOWN_SETTLE_TIME)


def camera_forward():

    camera_motor.run_target(
        CAMERA_SPEED,
        CAMERA_FORWARD,
        then=Stop.HOLD
    )

    wait(CAMERA_SETTLE_TIME)


# ============================================================
# LINE DETECTION
# ============================================================

def definitely_on_black():

    reflection = color_sensor.reflection()

    return reflection <= LINE_FOUND_MAX


def definitely_off_line():

    reflection = color_sensor.reflection()

    return reflection >= LINE_LOST_MIN


# ============================================================
# HUE CALCULATION
# ============================================================

def hue_distance(hue1, hue2):
    """
    Returns shortest distance between two hues.

    Example:

    RED center = 346

    hue = 350
    distance = 4

    hue = 2

    normal difference would be 344,
    but because hue wraps around at 360,
    actual distance is only 16.
    """

    difference = abs(hue1 - hue2)

    return min(
        difference,
        360 - difference
    )


# ============================================================
# HSV COLOR CLASSIFIER
# ============================================================

def classify_hsv(h, s, v):
    """
    Detect obstacle color.

    Hue is the main measurement.

    Saturation and brightness limits are intentionally
    forgiving so changes in room lighting do not easily
    break detection.
    """

    # Reject extremely weak readings.

    if s < COLOR_MIN_SATURATION:
        return "UNKNOWN"

    if v < COLOR_MIN_VALUE:
        return "UNKNOWN"


    # Calculate distance from each calibrated hue.

    red_distance = hue_distance(
        h,
        RED_HUE_CENTER
    )

    yellow_distance = hue_distance(
        h,
        YELLOW_HUE_CENTER
    )

    green_distance = hue_distance(
        h,
        GREEN_HUE_CENTER
    )


    # Store all acceptable candidates.

    candidates = []


    if red_distance <= RED_HUE_TOLERANCE:

        candidates.append(
            ("RED", red_distance)
        )


    if yellow_distance <= YELLOW_HUE_TOLERANCE:

        candidates.append(
            ("YELLOW", yellow_distance)
        )


    if green_distance <= GREEN_HUE_TOLERANCE:

        candidates.append(
            ("GREEN", green_distance)
        )


    # Nothing matched.

    if len(candidates) == 0:

        return "UNKNOWN"


    # If more than one range somehow overlaps,
    # select whichever calibrated hue is closest.

    best_color = candidates[0][0]
    best_distance = candidates[0][1]

    for candidate in candidates:

        color = candidate[0]
        distance = candidate[1]

        if distance < best_distance:

            best_color = color
            best_distance = distance


    return best_color


# ============================================================
# OBSTACLE COLOR READING
# ============================================================

def detect_obstacle_color():

    for attempt in range(COLOR_READ_RETRIES):

        red_count = 0
        yellow_count = 0
        green_count = 0
        unknown_count = 0


        debug("")
        debug(
            "Color reading attempt:",
            attempt + 1,
            "/",
            COLOR_READ_RETRIES
        )


        # ====================================================
        # TAKE MULTIPLE READINGS
        # ====================================================

        for i in range(COLOR_SAMPLES):

            hsv = color_sensor.hsv()

            result = classify_hsv(
                hsv.h,
                hsv.s,
                hsv.v
            )


            debug(
                i + 1,
                result,
                "H:", hsv.h,
                "S:", hsv.s,
                "V:", hsv.v
            )


            if result == "RED":

                red_count += 1


            elif result == "YELLOW":

                yellow_count += 1


            elif result == "GREEN":

                green_count += 1


            else:

                unknown_count += 1


            wait(COLOR_SAMPLE_DELAY)


        # ====================================================
        # DISPLAY VOTES
        # ====================================================

        debug("")
        debug("Votes:")
        debug("RED:", red_count)
        debug("YELLOW:", yellow_count)
        debug("GREEN:", green_count)
        debug("UNKNOWN:", unknown_count)


        # ====================================================
        # FIND HIGHEST VOTE
        # ====================================================

        highest_count = max(
            red_count,
            yellow_count,
            green_count
        )


        # Must have enough valid votes.

        if highest_count >= COLOR_MIN_VALID_VOTES:


            # RED

            if (
                red_count == highest_count
                and
                red_count > yellow_count
                and
                red_count > green_count
            ):

                return "RED"


            # YELLOW

            if (
                yellow_count == highest_count
                and
                yellow_count > red_count
                and
                yellow_count > green_count
            ):

                return "YELLOW"


            # GREEN

            if (
                green_count == highest_count
                and
                green_count > red_count
                and
                green_count > yellow_count
            ):

                return "GREEN"


        # ====================================================
        # FAILED THIS BATCH
        # ====================================================

        debug(
            "No reliable color detected.",
            "Trying again..."
        )

        wait(COLOR_RETRY_DELAY)


    return "UNKNOWN"


# ============================================================
# FIXED OBSTACLE TURNS
# ============================================================

def turn_left():

    debug("Turning LEFT")

    rotate_left(TURN_SPEED)

    wait(LEFT_TURN_TIME)

    stop_robot()


def turn_right():

    debug("Turning RIGHT")

    rotate_right(TURN_SPEED)

    wait(RIGHT_TURN_TIME)

    stop_robot()


# ============================================================
# SEARCH FOR BLACK LINE
# ============================================================

def search_one_direction(
    direction,
    duration,
    check_obstacle=True
):
    """
    Rotate slowly while looking for black.

    Returns:

    "FOUND"
    "OBSTACLE"
    "NOT_FOUND"
    """

    if direction == "LEFT":

        rotate_left(SEARCH_SPEED)

    else:

        rotate_right(SEARCH_SPEED)


    elapsed = 0
    black_count = 0


    while elapsed < duration:


        # ====================================================
        # ULTRASONIC CHECK
        # ====================================================

        if check_obstacle:

            distance = ultrasonic.distance()

            if distance <= OBSTACLE_DETECTION_DISTANCE:

                # Obstacle priority is higher than line recovery.
                # Stop searching immediately, then the obstacle
                # handler will approach straight to 5 cm.
                stop_robot()

                return "OBSTACLE"


        # ====================================================
        # BLACK LINE CHECK
        # ====================================================

        if definitely_on_black():

            black_count += 1


            if (
                black_count
                >= LINE_FOUND_CONFIRMATIONS
            ):

                stop_robot()

                debug(
                    "Black line found while searching",
                    direction
                )

                return "FOUND"


        else:

            black_count = 0


        wait(MAIN_LOOP_DELAY)

        elapsed += MAIN_LOOP_DELAY


    stop_robot()

    return "NOT_FOUND"


# ============================================================
# RECOVER LOST LINE
# ============================================================

def recover_line(
    preferred_direction=DEFAULT_SEARCH_DIRECTION,
    check_obstacle=True
):
    """
    Search strategy:

    1. Try preferred direction.
    2. If not found, sweep across to opposite side.
    3. Return approximately to center.
    4. Back up slightly.
    5. Repeat.
    """


    debug("")
    debug("==============================")
    debug("LINE LOST")
    debug("==============================")


    if preferred_direction == "LEFT":

        opposite_direction = "RIGHT"

    else:

        opposite_direction = "LEFT"


    for attempt in range(SEARCH_ATTEMPTS):


        debug(
            "Search attempt:",
            attempt + 1,
            "/",
            SEARCH_ATTEMPTS
        )


        # ====================================================
        # SEARCH PREFERRED SIDE
        # ====================================================

        result = search_one_direction(
            preferred_direction,
            SEARCH_SWEEP_TIME,
            check_obstacle
        )


        if result == "FOUND":

            return (
                "FOUND",
                preferred_direction
            )


        if result == "OBSTACLE":

            return (
                "OBSTACLE",
                None
            )


        # ====================================================
        # SEARCH OPPOSITE SIDE
        # ====================================================

        opposite_time = int(
            SEARCH_SWEEP_TIME
            * SEARCH_OPPOSITE_MULTIPLIER
        )


        result = search_one_direction(
            opposite_direction,
            opposite_time,
            check_obstacle
        )


        if result == "FOUND":

            return (
                "FOUND",
                opposite_direction
            )


        if result == "OBSTACLE":

            return (
                "OBSTACLE",
                None
            )


        # ====================================================
        # RETURN APPROXIMATELY TO CENTER
        # ====================================================

        if preferred_direction == "LEFT":

            rotate_left(SEARCH_SPEED)

        else:

            rotate_right(SEARCH_SPEED)


        wait(SEARCH_RETURN_TIME)

        stop_robot()


        # ====================================================
        # BACK UP SLIGHTLY
        # ====================================================

        debug(
            "Line not found.",
            "Backing up..."
        )


        move_backward(
            SEARCH_BACKUP_SPEED
        )

        wait(
            SEARCH_BACKUP_TIME
        )

        stop_robot()

        wait(100)


    debug("")
    debug("BLACK LINE NOT FOUND")

    return (
        "FAILED",
        None
    )


# ============================================================
# DETERMINE TURN DIRECTION
# ============================================================

def get_turn_direction(obstacle_color):


    if obstacle_color == "RED":

        return "LEFT"


    if obstacle_color == "GREEN":

        return "RIGHT"


    if obstacle_color == "YELLOW":

        if YELLOW_DIRECTION == 1:

            return "RIGHT"

        else:

            return "LEFT"


    return None


# ============================================================
# APPROACH OBSTACLE
# ============================================================

def approach_obstacle():
    """
    After the obstacle is first detected at 10 cm, ignore the
    line-searching logic and drive STRAIGHT until the robot is
    at the calibrated 5 cm color-reading distance.
    """

    distance = ultrasonic.distance()

    debug(
        "Obstacle entered detection zone:",
        distance,
        "mm"
    )

    # If we are already at 5 cm or closer, do not move forward.
    if distance <= OBSTACLE_DISTANCE:

        stop_robot()

        debug(
            "Already at color-check distance:",
            distance,
            "mm"
        )

        return distance


    debug(
        "Approaching obstacle straight until",
        OBSTACLE_DISTANCE,
        "mm..."
    )

    move_forward(OBSTACLE_APPROACH_SPEED)

    while True:

        distance = ultrasonic.distance()

        if distance <= OBSTACLE_DISTANCE:

            stop_robot()

            debug(
                "Final obstacle distance:",
                distance,
                "mm"
            )

            return distance

        wait(MAIN_LOOP_DELAY)


# ============================================================
# HANDLE OBSTACLE
# ============================================================

def handle_obstacle():


    stop_robot()


    debug("")
    debug("==============================")
    debug("OBSTACLE DETECTED")
    debug("==============================")


    debug(
        "First detection distance:",
        ultrasonic.distance(),
        "mm"
    )


    # ========================================================
    # 1. APPROACH STRAIGHT TO COLOR-CHECK DISTANCE
    # ========================================================
    #
    # IMPORTANT:
    # While doing this, line searching/recovery is NOT allowed
    # to turn the robot left or right. Obstacle handling has
    # priority once the ultrasonic sensor sees it at 10 cm.

    approach_obstacle()

    wait(100)


    # ========================================================
    # 2. CAMERA FORWARD
    # ========================================================

    debug("Camera -> FORWARD")

    camera_forward()


    # ========================================================
    # 3. READ COLOR
    # ========================================================

    obstacle_color = detect_obstacle_color()


    debug("")
    debug(
        "Detected color:",
        obstacle_color
    )


    # ========================================================
    # 4. CAMERA DOWN
    # ========================================================

    debug("Camera -> DOWN")

    camera_down()


    # ========================================================
    # 5. COLOR FAILED
    # ========================================================

    if obstacle_color == "UNKNOWN":

        debug("")
        debug(
            "ERROR:",
            "Could not identify obstacle."
        )

        stop_robot()

        while True:

            wait(100)


    # ========================================================
    # 6. DECIDE DIRECTION
    # ========================================================

    direction = get_turn_direction(
        obstacle_color
    )


    debug(
        "Decision:",
        direction
    )


    # ========================================================
    # 7. BACK AWAY FROM OBSTACLE
    # ========================================================

    debug("Backing up...")


    move_backward(
        BACKUP_SPEED
    )

    wait(
        BACKUP_TIME
    )

    stop_robot()

    wait(100)


    # ========================================================
    # 8. TURN
    # ========================================================

    if direction == "LEFT":

        turn_left()

    else:

        turn_right()


    wait(100)


    # ========================================================
    # 9. GO FORWARD AGAIN
    # ========================================================

    debug(
        "Moving forward after turn..."
    )


    move_forward(
        POST_TURN_SPEED
    )

    wait(
        POST_TURN_FORWARD_TIME
    )

    stop_robot()


    debug(
        "Obstacle handling finished."
    )

    debug("")


    return direction


# ============================================================
# STARTUP
# ============================================================

debug("")
debug("==============================")
debug("ROBOT STARTING")
debug("==============================")


debug(
    "Yellow direction:",
    YELLOW_DIRECTION
)


debug(
    "Obstacle first-detection distance:",
    OBSTACLE_DETECTION_DISTANCE,
    "mm"
)

debug(
    "Obstacle color-check distance:",
    OBSTACLE_DISTANCE,
    "mm"
)


debug(
    "Camera -> DOWN"
)


camera_down()


debug(
    "Camera angle:",
    camera_motor.angle()
)


wait(500)


# ============================================================
# MAIN STATE VARIABLES
# ============================================================

obstacle_armed = True

preferred_search_direction = (
    DEFAULT_SEARCH_DIRECTION
)

lost_line_count = 0


# ============================================================
# MAIN LOOP
# ============================================================

while True:


    # ========================================================
    # ALWAYS CHECK ULTRASONIC
    # ========================================================

    distance = ultrasonic.distance()


    # ========================================================
    # OBSTACLE DETECTED WITHIN 10 CM
    # ========================================================
    #
    # This check happens BEFORE line detection. Once triggered,
    # obstacle handling takes priority and the robot drives
    # straight to 5 cm instead of starting a line recovery turn.

    if (
        obstacle_armed
        and
        distance <= OBSTACLE_DETECTION_DISTANCE
    ):


        stop_robot()


        direction = handle_obstacle()


        # After an obstacle, try searching in the direction
        # we just turned if the line is subsequently lost.

        preferred_search_direction = (
            direction
        )


        # Prevent same obstacle from immediately
        # triggering again.

        obstacle_armed = False


        lost_line_count = 0


        continue


    # ========================================================
    # RE-ARM ULTRASONIC
    # ========================================================

    if not obstacle_armed:


        if (
            distance
            >= OBSTACLE_REARM_DISTANCE
        ):


            obstacle_armed = True


            debug(
                "Obstacle detector re-armed."
            )


    # ========================================================
    # READ FLOOR
    # ========================================================

    reflection = (
        color_sensor.reflection()
    )


    # ========================================================
    # CHECK WHETHER LINE IS LOST
    # ========================================================

    if (
        reflection
        >= LINE_LOST_MIN
    ):


        lost_line_count += 1


    else:


        # Black or uncertain/edge.
        #
        # Continue straight.

        lost_line_count = 0


    # ========================================================
    # LINE REALLY LOST
    # ========================================================

    if (
        lost_line_count
        >= LINE_LOST_CONFIRMATIONS
    ):


        stop_robot()


        result, found_direction = recover_line(
            preferred_search_direction,
            check_obstacle=obstacle_armed
        )


        # ====================================================
        # OBSTACLE FOUND WHILE SEARCHING
        # ====================================================

        if result == "OBSTACLE":


            direction = handle_obstacle()


            preferred_search_direction = (
                direction
            )


            obstacle_armed = False


        # ====================================================
        # LINE RECOVERY FAILED
        # ====================================================

        elif result == "FAILED":


            debug("")
            debug(
                "ERROR:",
                "Unable to recover black line."
            )


            stop_robot()


            while True:

                wait(100)


        # ====================================================
        # LINE FOUND
        # ====================================================

        elif result == "FOUND":


            # Remember which side successfully found the line.
            #
            # Next time, try this direction first.

            preferred_search_direction = (
                found_direction
            )


            debug(
                "Line recovered."
            )


        lost_line_count = 0


        continue


    # ========================================================
    # NORMAL BEHAVIOR
    # ========================================================
    #
    # If the robot has NOT confirmed that it has left
    # the line, simply drive straight.
    #
    # No constant left/right correction.

    move_forward(
        FORWARD_SPEED
    )


    wait(
        MAIN_LOOP_DELAY
    )