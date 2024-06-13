import string

test_str = '''think I could make a better engine than that.”

“Do you? Well, some’ing’s wanted; hauling coal by horses is very expensive.”

“Ay, it is, and I think an engine could do it better.”

“Mr. Blackett’s second engine burst all to pieces; d’ye mind that?”

“How came that about?”

“Tommy Waters, who put it together, could not make it go, so he got a bit fractious and said she should move. He did some’ing to the safety-valve and she did begin to work, but then she burst all to pieces.”

“Ay, ay, but this one is an improvement.”

“It had need be. Even the third was a perfect plague.”

[10]

“What! you mean Mr. Blackett’s third engine?”

“Ay. It used to draw eight or nine truck loads at about a mile an hour, or a little less; but it often got cranky and stood still.”

“Stood still!”

“Ay; we thought she would never stick to the road, so we had a cogged wheel to work into a rack-work rail laid along the track, and somehow she was always getting off the rack-rail.”

“And now you find that the engine is heavy enough herself to grip the rail.”

“Ay, that was Will Hedley’s notion; he’s a viewer at the colliery. And it is a great improvement. Why, that third engine, I say, was a perfect nuisance. Chaps used to sing out to the driver: ‘How do you get on?’”

“‘Get on,’ sez he, ‘I don’t get on; I on’y get off!’”

“It was always goin’ wrong, and horses was always having to be got out to drag it along.”

“How did Hedley find out that a rack-rail was not needful?”

“Well, he had a framework put upon wheels and worked by windlasses which were geared to the wheels. Men were put to work these windlasses which set the wheels going; and, lo and behold, she moved! The wheels, though smooth, kept to the rails, though they were smooth also, and the framework went along without slipping. ‘Crikey!’ says Hedley, ‘no cogged wheels, no chains, no legs for me! We can do without ’em all. Smooth wheels will grip smooth rails.’ And he proved it too by several experiments.”

“Then Mr. Blackett had this engine built?”

“Ay, and it be, as you say, a great improvement. But that steam blowing off there, after it have done its work, frights the horses on the Wylam Road ter’ble, and makes it a perfect nuisance.”

“Has nothing been done to alter it?”

“Mr. Blackett has given orders to stop the engine when any horses comes along, and the men don’t like that because it loses time. He thinks he is going[11] to let the steam escape gradual like, by blowing it off into a cask first.”

“Umph! very wasteful.”

“Oh, ay; it be wasteful; and many a one about here sez of Mr. Blackett that a fool and his money are soon parted.”

“No,” said the first speaker, shaking his head thoughtfully, “Mr. Blackett is no fool. But I think I could build a better engine than that.”
'''

test_str = test_str.translate(str.maketrans('','', string.punctuation))
print(test_str)
