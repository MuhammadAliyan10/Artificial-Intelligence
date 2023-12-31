num_of_pages = int(input("Enter the number of pages:"))
one_day = int(input("Enter the number of pages you read one day:"))
day_spend = int(input("Enter how many days you read it:"))

pages_left = num_of_pages - (one_day*day_spend)
pages_read = num_of_pages - pages_left
print(f"Total number of pages is {num_of_pages}, and you read {pages_read} pages and the number of pages left is {pages_left}")