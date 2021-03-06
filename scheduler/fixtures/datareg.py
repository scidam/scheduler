#coding: utf-8
data = [
{ 'name' : 'Океанариум',
  'objpk': 3,
  'username': 'ocean',
  'dates': [{'month': '06', 'days': [12, 15, 18, 19, 22, 25, 26, 29]},
            {'month': '07', 'days': [2, 3, 6, 9, 10, 13, 16, 17 ]}
            ],
  'dateonly': True,
  'email': 'zazerkalie2017@ocean.dvo.ru',
  'slug': 'ocean'
},

{ 'name' : 'Ботанический сад-институт ДВО РАН',
  'objpk' : 5,
  'username': 'golovan',
  'dates':[{'month': '06', 'days': [16, 17, 18, 23, 24, 25, 30 ]},
            {'month': '07', 'days': [1, 2, 7, 8, 9, 14, 15, 16]}
            ],
  'dateonly': True,
  'email': 'ecocenter@botsad.ru',
  'slug': 'bsi'

},

{ 'name' : 'Вилла "Курица"',
  'objpk' : 4,
  'username': 'curica',
  'dates':[{'month': '06', 'days': [12, 13, 14, 17, 19, 20, 21, 24, 26, 27, 28]},
            {'month': '07', 'days': [1, 3, 4, 5, 8, 10, 11, 12, 15, 17 ]}
            ],
  'times': "11:00, 11:20, 11:40, 12:00, 12:20, 12:40, 13:00, 13:20, 13:40, 14:00, 14:20, 14:40, 15:00, 15:20, 15:40, 16:00, 16:20, 16:40, 17:00, 17:20, 17:40",
  'dateonly': False,
  'email': 'svetlana.laletina@gmail.com',
  'slug': 'curica'
},

{ 'name' : 'Вилла "Курица"',
  'username': 'curica',
  'objpk' : 4,
  'dates':[{'month': '06', 'days': [15, 22, 29 ]},
            {'month': '07', 'days': [6, 13  ]}
            ],
  'times': "11:00, 11:20, 11:40, 12:00, 12:20, 12:40, 13:00, 13:20, 13:40, 14:00, 14:20, 14:40",
  'dateonly': False,
  'email': 'svetlana.laletina@gmail.com',
  'slug': 'curica'
},

{ 'name' : 'Дом Суханова',
  'username': 'sukhanov',
  'dates':[{'month': '06', 'days': [12, 13, 14, 18, 19, 20, 21, 25, 26, 27, 28]},
            {'month': '07', 'days': [2, 3, 4, 5,  9, 10, 11, 12, 16, 17]}
            ],
  'times': "14:00; 14:15; 14:30; 14:45; 15:00; 15:15; 15:30; 15:45; 16:00; 16:15; 16:30; 16:45; 17:00",
  'dateonly': False,
  'email': 'lidiya_novinskay@mail.ru',
  'slug': 'sukhanov'
},

{ 'name' : 'Дом Суханова',
  'username': 'sukhanov',
  'dates':[{'month': '06', 'days': [15,22,29]},
            {'month': '07', 'days': [6,13]}
            ],
  'times': "10:15; 10:30; 10:45; 11:00; 11:15; 11:30; 11:45; 12:00; 12:15; 12:30; 12:45; 13:00; 13:15; 13:30; 13:45; 14:00; 14:15; 14:30; 14:45; 15:00; 15:15; 15:30; 15:45; 16:00; 16:15; 16:30; 16:45; 17:00",
  'dateonly': False,
  'email': 'lidiya_novinskay@mail.ru',
  'slug': 'sukhanov'

},

{ 'name' : 'Зоомузей ДВФУ',
  'username': 'zoofefu',
  'dates':[{'month': '06', 'days': [13,14, 15, 18, 19, 20, 21, 22, 25, 26, 27, 28, 29]},
            {'month': '07', 'days': [2,3,4,5.6,9,10,11,12,13,16,17]}
            ],
  'times': "11:00; 11:20; 11:40; 12:00; 12:20; 12:40; 13:00; 13:20; 13:40; 14:00; 14:20; 14:40; 15:00; 15:20; 15:40, 16:00",
  'dateonly': False,
  'email': 'rakushki61@mail.ru',
 'slug': 'zoo'
},


{ 'name' : 'Музей ННЦМБ',
  'objpk': 2,
  'username': 'nnc',
  'dates':[{'month': '06', 'days': [14, 15, 18, 19, 21, 22, 25, 26, 28, 29]},
            {'month': '07', 'days': [2, 3, 5, 6, 9, 10, 12, 13 ]}
            ],
  'times': "11:00; 11:15; 11:30; 11:45; 12:00; 12:15; 12:30; 12:45; 13:00; 13:15; 13:30; 13:45; 14:00; 14:15; 14:30; 14:45; 15:00; 15:15; 15:30; 15:45; 16:00",
  'dateonly': False,
  'email': 'seaproject@mail.ru',
 'slug': 'nncmb-dvo-ran'
},

{ 'name' : 'Главный корпус муз. Арсеньева',
  'username': 'arsenev',
  'dates':[{'month': '06', 'days': [14, 15, 16, 19, 21, 22, 23, 26, 28, 29, 30 ]},
            {'month': '07', 'days': [3, 5, 6, 7, 10, 12, 13, 14, 17 ]}
            ],
  'times': "11:00; 11:15; 11:30; 11:45; 12:00; 12:15; 12:30; 12:45; 13:00; 13:15; 13:30; 13:45; 14:00; 14:15; 14:30; 14:45; 15:00; 15:15; 15:30; 15:45; 16:00",
  'dateonly': False,
  'email': 'museum.education@arseniev.org',
 'slug': 'arsenev'
},

{ 'name' : 'Картинная галерея',
  'username': 'cartina',
  'dates':[{'month': '06', 'days': [12,14,15,16,19,21,22, 23,26,28,29,30 ]},
            {'month': '07', 'days': [3,5,6,7,10,12,13,14,17]}
            ],
  'times': "11:00; 11:15; 11:30; 11:45; 12:00; 12:15; 12:30; 12:45; 13:00; 13:15; 13:30; 13:45; 14:00; 14:15; 14:30; 14:45; 15:00; 15:15; 15:30; 15:45; 16:00; 16:15; 16:30; 16:45; 17:00",
  'dateonly': False,
  'email': 'primgallery@mail.ru',
 'slug':'cartina'
},


{ 'name' : 'Геомузей ДВФУ',
  'username': 'geofefu',
  'dates':[{'month': '06', 'days': [14, 15, 18, 19, 21, 22, 25, 26, 28, 29 ]},
            {'month': '07', 'days': [2, 3, 5, 6, 9, 10, 12, 13, 16, 17]}
            ],
  'times': "11:00; 11:15; 11:30; 11:45; 12:00; 12:15; 12:30; 12:45; 13:00; 13:15; 13:30; 13:45; 14:00; 14:15; 15:00; 15:15; 15:30; 15:45; 16:00",
  'dateonly': False,
  'email': 'geolog-mineral@mail.ru',
 'slug': 'geo'
},

{ 'name' : 'Музей города',
  'username': 'citymuseum',
  'dates':[{'month': '6', 'days': [13,14,15,16,20, 21,22,23,27,28,29,30 ]},
            {'month': '07', 'days': [4,5,6,7,11,12,13,14]}
            ],
  'times': "10:30    10:50    11:10    11:30    11:50    12:10    12:30    12:50    13:10    13:30    13:50    14:10    14:30    14:50    15:10    15:30    15:50    16:10    16:30    16:50    17:10    17:30",
  'dateonly': False,
  'email': 'museumcityvlad@gmail.com',
 'slug': 'gorod'
},

{ 'name' : 'ЦСИ "Заря"',
  'username': 'zarya',
  'dates':[{'month': '06', 'days': [12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28, 29 ]},
            {'month': '07', 'days': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]}
            ],
  'times': "12:00, 12:30, 13:00, 13:30, 14:00, 14:30, 15:00, 15:30, 16:00, 16:30, 17:00, 17:30, 18:00",
  'dateonly': False,
  'email': 'info@zaryavladivostok.ru',
 'slug': 'zarya'
},


{ 'name' : 'Дом путешественника',
  'username': 'traveller',
  'dates':[{'month': '06', 'days': [13, 15, 16, 17, 18,  20, 22, 23, 24, 25, 27, 29, 30 ]},
            {'month': '07', 'days': [1, 2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16 ]}
            ],
  'times': "10:30    10:50    11:10    11:30    11:50    12:10    12:30    12:50    13:10    13:30    13:50    14:10    14:30    14:50    15:10    15:30    15:50    16:10    16:30    16:50    17:10    17:30",
  'dateonly': False,
  'email': 'arsenieviVM@yandex.ru',
 'slug' : 'dom'
},
]
