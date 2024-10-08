import requests
from config import CHECK_Q , MIN_PAGE, IS_WEEKLY, CONTEST_ID,THRESHOLD
from helper import get_page_ranking,get_contest_details,get_user_submission
import hashlib
import random
import time

GLOBAL_HASH_CODE = {}
GLOBAL_HASH = {}

CHECK_Q_ID = None




def main():
    global CHECK_Q_ID,GLOBAL_HASH,GLOBAL_HASH_CODE
    curr_page = MIN_PAGE
    page_details = get_contest_details(IS_WEEKLY,CONTEST_ID);
    page_details = page_details.json()
    while True:
        res = get_page_ranking(IS_WEEKLY,CONTEST_ID,curr_page)
        curr_page+=1;
        res = res.json()
        if(not CHECK_Q_ID):
            CHECK_Q_ID = str(page_details['questions'][CHECK_Q]['question_id'])
        is_no_one_attempted = True
        for each in res['total_rank']:
            try:
                submission_data = each['submissions'][CHECK_Q_ID]
                submission_id = submission_data['submission_id']
                is_no_one_attempted = False
                is_china_server = each['data_region'] == "CN"
                # time.sleep(0.3)
                submission = get_user_submission(submission_id,is_china_server);
                # print("submission",submission.text);
                submission = submission.json()['code']
                submission = submission.replace("\n", " ")
                hashed_ = hashlib.sha256(submission.encode()).hexdigest()
                print(hashed_)
                if(hashed_ not in GLOBAL_HASH):
                    GLOBAL_HASH[hashed_] = 0;
                GLOBAL_HASH[hashed_]+=1;
                if(GLOBAL_HASH[hashed_] > THRESHOLD):
                    GLOBAL_HASH_CODE[hashed_] = submission
                if(random.randint(0,50) == 4):
                    print(GLOBAL_HASH_CODE,"\n\n\n\n\n\n\n")
            except Exception as e:
                print("some error occured",str(e));
                time.sleep(2);
        print("Repeated Answers after complete page query",GLOBAL_HASH_CODE);
        time.sleep(5);

        if(is_no_one_attempted):
            break; 
    print("COMPLETE REPEATED CODES",GLOBAL_HASH_CODE)


if __name__ == "__main__":
    main()