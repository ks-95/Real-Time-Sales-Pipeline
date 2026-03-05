import duckdb
import time
import os

# Connect to database
con = duckdb.connect()

print("--- Real-Time Analytics Dashboard Starting ---")
print("Watching 'live_stream.json' for changes...\n")

while True:
    if os.path.exists("live_stream.json"):
        try:
            #  query json file 
            query = """
                SELECT 
                    count(*) as total_sales,
                    round(sum(price), 2) as total_revenue,
                    product,
                    count(*) as product_count
                FROM read_json_auto('live_stream.json')
                GROUP BY product
                ORDER BY total_revenue DESC
                LIMIT 5;
            """
            
            # show result
            result = con.execute(query).df()
            
            # clear terminl for dashboard
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"--- Dashboard Update: {time.strftime('%H:%M:%S')} ---")
            print(result.to_string(index=False))
            print("\n(Press Ctrl+C to stop)")
            
        except Exception as e:
            print(f"Waiting for more data{e}")
    else:
        print("Waiting for 'live_stream.json' to be created by the producer")
        
    time.sleep(2) #refresh
