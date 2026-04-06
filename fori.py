#import the random module
import random
# create subjcet
subject=[
    "shiva",
    "dk sigh",
    "ashok"
]
actions=[
    "launches"
    "camcels"
    "dances with"
]
places=[
    "read fort"
    "in mubbal local traia"
    "up"
]
#sart the headline genration loop
while True:
    subject=random.choice(subject)
    actions=random.choice(actions)
    places=random.choice(places)
    headline=f"brking news:{subject} {actions} {places}"
    print("\n"+headline)
    user_input=input("\n do you want anthoer headline?(yes\no)").strip()
    if user_input=="no":
        break
    print("\n thanks for using the fake news headline genator.have a fund")