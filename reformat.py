import sys

if len(sys.argv) < 2:
    print('Provide a file path as an argument.')
    sys.exit()

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    links = f.read().split(',')

links = [link.strip() for link in links]
sorted_links = sorted(set(links))

with open('sorted_links.txt', 'w') as f:
    for link in sorted_links:
        f.write(link + '\n')
        
print('Links sorted and saved to sorted_links.txt')
