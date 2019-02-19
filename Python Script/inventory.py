stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def display_inventory(inventory):
	print('Inventory'.center(20,'='))
	item_total=0
	for k,v in inventory.items():
		print(' '+k.title().ljust(15,'.')+ ' '+str(v).ljust(3))
		item_total+=v
	print('Total numner of items: '+str(item_total))

def addToInventry(inventory,loot):
	for item in loot:
		if item in inventory:
			inventory[item]+=1
		else:
			inventory.setdefault(item,1)
	
	return inventory



if __name__ == '__main__':
	print('Before Loot')
	display_inventory(stuff)
	print()
	print('Loot')
	dragonLoot=['gold coin','dagger','gold coin','ruby']
	print (dragonLoot)
	print()
	print('After the Loot')
	inv=addToInventry(stuff,dragonLoot)
	display_inventory(inv)
