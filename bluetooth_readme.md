Suru ma available devices haru herna 

bluetoothctl 
hanne
ani tespaxi tya hco5 ko mac address dekhauxa 
pair hciokomac_address hanne

pair sucessful vanepaxi 

trust hco5komacaddress hanne

mero ma yo garda vako thena tei vayera pi ko screen nai kholera duiso gareko jo jo jasari gara 
pi ko screen ma bluetooth wala icon dekhinxa tya gayera pailei hco5 dekhaxa vane tesma click gara natra add device vanne ma click gara ani pair gara pin magxa pin hane paxi pair hunxa 
pailei bluetoothctl bata pair vako thyo vane paila remove garnu prxa ani balla pair hunxa

pair vaye paxi bluetoothctl khuleko wala terminal tessae xoddeu ani naya terminal kholera 

sudo rfcomm bind hco5 hco5ko_mac_address 

yo hane paxi bind hunxa 

bind vayo ki nai herna lai 

pi ko file manager kholera 

/dev ma hera rfcomm0 vanne file xa ki nai xa vane vayo 

tyo file herna lai terminal mai pani 

cd /dev
ani 
ls -a
garda dekhaunu parne ho 

bind vae sakepaxi chai aba yo code chalaune ho 

python Test.py 


code chalaye paxi agi tyo banda nagareko bluetoothctl wala terminal ma connect:yes lekhxa 
connected:yes lekhyo vane connection chai vako xa connect vayepaxi transmit pani vakae hola vaneko ho aba baki kura hernu xa.