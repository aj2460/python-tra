#separate a list with comma and a space and add 'and' before the last item

def sepateList(list):
	return ', '.join(list[:-1]) + ' and ' + list[-1]

spam=['apples','bananas','tofu','cats']

print(sepateList(spam))