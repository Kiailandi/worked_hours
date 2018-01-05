from datetime import datetime
import json

def convert_s_to_hms(worked_seconds):
    hours, remainder = divmod(worked_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (hours, minutes, seconds)

def convert_hm_to_s(worked_hours, worked_minutes):
    return worked_hours * 3600 + worked_minutes *60

def main():
    configfile = open('config.json', 'r')
    config = json.load(configfile)
    configfile.close()

    inputfile = open(config["input_file"])

    worked_seconds = 0
    FMT = config["time_format"]

    for line in inputfile:
        tmp1 = line.split(config["date_separator"])
        tmp2 = tmp1[1].split(config["time_separator"])
        tdelta = datetime.strptime(tmp2[1].rstrip(), FMT) - datetime.strptime(tmp2[0].rstrip(), FMT)
        worked_seconds = worked_seconds + tdelta.seconds
        print ("Date: " + tmp1[0].rstrip())
        print ("Start: " + tmp2[0].rstrip())
        print ("End: " + tmp2[1].rstrip())
        hours, minutes, seconds = convert_s_to_hms(tdelta.seconds)
        print('You worked: ' + str(hours) + " hours and " + str(minutes) + " miutes \n")

    inputfile.close()

    hours, minutes, seconds = convert_s_to_hms(worked_seconds)

    print('You worked: ' + str(hours) + " hours and " + str(minutes) + " miutes in total.")
    print("Which is like " + str(int(hours / config["hours_day_fulltime"])) + " days of full time work.\n")

    if config["stage"]["active"]:
        stage = config["stage"]
        stage_hours = stage["CFU_needed"] * stage["CFU_hours"]
        if stage_hours > hours:
            missing_hours, missing_minutes, missing_seconds = convert_s_to_hms(convert_hm_to_s(stage_hours, 0) - worked_seconds)
            print("You still need to work " + str(missing_hours) + " hours and " + str(missing_minutes) +
                  " minutes to finish the stage (" + str(stage_hours) + " hours total).")
            print("Which is like " + str(int(missing_hours / config["hours_day_fulltime"])) + " days of full time work.")
        else:
            print("You finished your stage!")
    else:
        print("You earned: " + config["currency_simbol"] + str(hours * config["hour_pay"] + minutes / 30 * config["hour_pay"] / 2) + ".")

if __name__ == "__main__":
    main()