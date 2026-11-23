#Basic chunking without overlap......

import time
def chunks(chunk_size,data):
    
    data = data2.split()
    start = 0
    end = chunk_size
    chunks_list = []
    i = 0
    
    while start < len(data):
        chunks_list.append(" ".join(data[start:end]))
        start = end 
        if(len(data)-end < chunk_size):
            end = end+len(data)-end
        else:
            end += chunk_size
            
        print(f"[Chunk - {i+1} ]")
        print(f"{chunks_list[i]}",flush = True)
        print()
        time.sleep(1)
        i += 1
    
     

time_start = time.perf_counter()
with open("virat_data.txt", "r") as data1:
    data2 = data1.read()

chunks(data = data2,chunk_size = 100)
time_end = time.perf_counter()
print(f"Time taken to execute the code : {(time_end-time_start):.2f} seconds")



