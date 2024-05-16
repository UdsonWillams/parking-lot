from datetime import (
    datetime,
    timedelta,
)

hours_per_day = 8

if __name__ == "__main__":
    # markeup hours
    work_entrance = "11:37"
    pre_lunch = "12:23"
    post_lunch = "13:50"

    today = datetime.now().date().strftime("%m/%d/%Y")
    work_entrance = datetime.strptime(f"{today} {work_entrance}", "%m/%d/%Y %H:%M")
    final_time = work_entrance + timedelta(hours=hours_per_day)

    pre_lunch_time = datetime.strptime(f"{today} {pre_lunch}", "%m/%d/%Y %H:%M")
    post_lunch_time = datetime.strptime(f"{today} {post_lunch}", "%m/%d/%Y %H:%M")

    diference = post_lunch_time - timedelta(
        hours=pre_lunch_time.hour, minutes=pre_lunch_time.minute
    )
    final_time = final_time + timedelta(hours=diference.hour, minutes=diference.minute)

    print(f"A hora de sair são as: {final_time.time()}")
