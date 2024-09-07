import argparse
import task_manager

if __name__ == "__main__":
    print("Test")

    parser = argparse.ArgumentParser(description='Process file requests')
    parser.add_argument('file_path', type=str, help="Must be a valid xml file")
    parser.add_argument('limit', type=int, help='Limit the number of requests')
    args = parser.parse_args()

    
    my_instance_class = task_manager.TaskManager()
    my_instance_class.file_path = args.file_path
    my_instance_class.http_request_limit = args.limit
    my_instance_class.start()

