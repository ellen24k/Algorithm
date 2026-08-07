import heapq # 기본은 최소힙

def solution(jobs):
    jobs.sort(key= lambda x: -x[0]) # pop 성능을 위해 요청 시간을 기준으로 내림차순 정렬
    print("jobs:",jobs)

    time = 0
    processable = 0 # 하드디스크가 작업을 수행할 수 있는 상태가 되는 시각
    job_heap = []
    until_finished = []

    while(len(job_heap) > 0 or len(jobs) > 0):
        while (len(jobs) > 0 and time == jobs[-1][0]): # 작업이 요청된 시간에
            req_time , processing_time = jobs.pop()
            heapq.heappush(job_heap, (processing_time, req_time)) # 실행 시간을 기준으로 힙에 넣는다
            # print("time",time,"job_heap",job_heap)

        if time >= processable: # 디스크가 작업을 수행할 수 있으면
            if len(job_heap) > 0:
                processing_time, req_time = heapq.heappop(job_heap)
                processable = processing_time + time
                until_finished.append(time + processing_time - req_time)
                # print("pop:",processing_time, req_time,"time:",time,"until:",until_finished)

        time += 1

    answer = sum(until_finished)//len(until_finished)
    return answer