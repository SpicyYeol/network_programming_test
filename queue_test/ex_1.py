import queue
fifo_q = queue.Queue() #FIFO 큐 생성
data = ['Hello', 'World', 'Victory', 'Korea']
for value in data:
    fifo_q.put(value) #큐에 저장
while not fifo_q.empty(): #큐에 저장된 값이 있는지 확인
    print(fifo_q.get()) #저장된 데이터를 인출하여 출력
