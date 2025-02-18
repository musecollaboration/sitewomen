from django.template.defaultfilters import first, last

menu = list(map(str.strip, input().split(";")))

print(first(menu), last(menu))
