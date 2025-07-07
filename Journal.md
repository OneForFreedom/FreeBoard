---
title: "FreeBoard"
author: "One For Freedom"
description: "Basically just a 60% keyboard with three rotary encoders."
created_at: "2024-06-29"
---

# June 30th : Started the build!

[I made a schematic today and completed footprints. I also researched parts. I'm using a raspberry pi pico, which is like 5 us dollars, I also found switches which are 110 for 60ish dollars, I know its a bit steep, but I can't afford getting super bad low quality ones after a month of waiting. I also found.. Well, nothing, I was looking for keycaps but realised that you can't get good ones for 10 dollars. I'll have to save the search for keycaps later. I'm gonna have to look for two rotary encoders and 62 diodes.
Peace!]

![FreeBoard Schematic](FreeBoard%20Schematic.png)

**Total time spent: 3h 10m**

# Jul 1 : Finished the schematic!

[Bruh, I rebuilt the schematic, I changed the layout from 14x5 to 7x10 so that I could add an extra rotary encoder - 100% worth it. I decided that I'm gonna 3d print keycaps along with rotary encoder knobs cases and any basic tools ill need. Tomorrow I'll finalise the items I'll need and the prices.]

![Freeboard Second Schematic](FreeBoard%20Schematic%202.png)

**Time spent : 4h**

# Jul 2nd : PCB COMPLETE, ITEM HUNT ALSO COMPLETE!

[LETS GOOO! THE PCB IS DONE!! now I got to do the most taxing job, the case. itll be pain but ill make it through, Honestly i might go for a tilted case ykyk. I'll show you the pcb down below. I also had to painstakinly add holes for clip in stabilizers - I'm too
scared to add screw hole in, so screw that, also since im using an iso layout, i'll have to add a 2.75u wire to the stabiliser, which is impossible to find, so I needed to get them "compatible" ones. I made the keycaps (i love google) and also a plate (idk how'll that go on, if i completely mess it up, then it'll be a plateless project.) Here's an itemised bill: (Prices may fluxuate depending on conversion rates and inflation)]
| Item                    | Pounds (£) | Conversion Rate | Dollars (\$) |
| ----------------------- | ---------- | --------------- | ------------ |
| PCB (Freeboard)         | 25.09      | × 1.36          | 34.52        |
| Raspberry Pi            | 7.70       | × 1.36          | 10.47        |
| Switches                | 24.98      | × 1.36          | 33.97        |
| Rotary Encoders (9.20€) | \~7.93     | × 1.36          | 10.78        |
| Stabilizers + Shipping  | 20.91      | × 1.36          | 28.44        |
| Diodes                  | 6.06       | × 1.36          | 8.24         |
| Royal Mail Shipping     | 5.00       | × 1.36          | 6.80         |
| Micro USB Cable         | 3.00       | × 1.36          | 4.08         |
| Grand Total             |            |                 | ~137.30      |
![FreeBoard PCB](FreeBoard%20PCB.png)

**Time spent 6 Hours**


# Jul 6th : Back to business.

I did one big project, but that got quickly scrapped when I realised It was only a 4 point project, I might continue it after following the discovery of ALiExpress.
I submitted another project which was basically an etchasketch but it was digital. And suprisingly, I did it in under one day! Now enough for that, time for this.

I left off after finishing the pcb. But now I started with the cad. But now I got to go bed, so cya, Bigger update tomorrow.

**Time Spent: 1 Hour**

# Jul 7th : COMPLETION

All softwarical (if thats a word) projects are done! 
Now let me submit this. The cad was done which was relatively easy, but it's big af, cad crashed on me midway saving, but luckily I saved it before it did.
Now lets talk prices, let me run this with my super cool mathmatical skills and I'll get back to you.

# Bill Of Materials (BOM)

| Item              | Quantity | Price (GBP) | Total (GBP) | Link                                                                                       |
|-------------------|----------|-------------|-------------|--------------------------------------------------------------------------------------------|
| Pico Micro        | 1        | £1.90       | £1.90       | [Link](https://www.aliexpress.com/item/1005008513003531.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%202.07%21GBP%201.90%21%21GBP%201.90%21%21%21%40211b804117519184179823635ecba0%2112000045498711555%21ct%21UK%216063356903%21%211%210) |
| Keycaps           | 1        | £7.69       | £7.69       | [Link](https://www.aliexpress.com/item/1005004536761030.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%208.02%21GBP%207.69%21%21GBP%207.69%21%21%21%40211b804117519184179823635ecba0%2112000029514063983%21ct%21UK%216063356903%21%211%210) |
| O-Rings           | 1        | £0.57       | £0.57       | [Link](https://www.aliexpress.com/item/32965363255.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%200.57%21GBP%200.57%21%21GBP%200.57%21%21%21%40211b804117519184179823635ecba0%2112000047834980334%21ct%21UK%216063356903%21%211%210) |
| Keyswitches       | 1        | £21.39      | £21.39      | [Link](https://www.aliexpress.com/item/1005006425450443.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%2021.39%21GBP%2021.39%21%21GBP%2021.39%21%21%21%40211b804117519184179823635ecba0%2112000037120671475%21ct%21UK%216063356903%21%211%210) |
| Cable             | 1        | £0.92       | £0.92       | [Link](https://www.aliexpress.com/item/1005007138392516.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%200.94%21GBP%200.92%21%21GBP%200.91%21%21%21%40211b804117519184179823635ecba0%2112000039538590178%21ct%21UK%216063356903%21%211%210) |
| EC11 Cap          | 1        | £1.06       | £1.06       | [Link](https://www.aliexpress.com/item/1005005983134515.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%201.06%21GBP%201.06%21%21GBP%201.06%21%21%21%40211b804117519184179823635ecba0%2112000035172713582%21ct%21UK%216063356903%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D) |
| EC11              | 1        | £1.89       | £1.89       | [Link](https://www.aliexpress.com/item/1005005983134515.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%201.89%21GBP%201.89%21%21GBP%201.89%21%21%21%40211b804117519184179823635ecba0%2112000035172713579%21ct%21UK%216063356903%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D) |
| Diodes (x3)       | 3        | £0.70       | £2.10       | [Link](https://www.aliexpress.com/item/1005006245109375.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%201.19%21GBP%200.70%21%21GBP%200.69%21%21%21%40211b804117519184179823635ecba0%2112000036448323916%21ct%21UK%216063356903%21%213%210) |
| Switchpads        | 1        | £2.52       | £2.52       | [Link](https://www.aliexpress.com/item/1005006454684461.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%202.52%21GBP%202.52%21%21GBP%202.39%21%21%21%40211b804117519184179823635ecba0%2112000037257481259%21ct%21UK%216063356903%21%211%210) |
| Switch Film       | 1        | £2.00       | £2.00       | [Link](https://www.aliexpress.com/item/1005006584258877.html?spm=a2g0o.cart.0.0.3e1c38daz2FcDN&mp=1&pdp_npi=5%40dis%21GBP%21GBP%202.00%21GBP%202.00%21%21GBP%201.96%21%21%21%40211b804117519184179823635ecba0%2112000037731101685%21ct%21UK%216063356903%21%211%210) |
| PCB               | 1        | £28.65      | £28.65      | [Link](https://cart.jlcpcb.com/)                                                              |
| Royal Mail Shipping | 1       | £5.00       | £5.00       | [Link](https://send.royalmail.com/send/youritem?country=GBR&format&weight=&weightUnit=G)       |

**Grand Total (GBP): £74.69**  
**Grand Total (USD): $101.55**


I'm soo happy !!!

I'll cya UNTIL EVERYTHING ARRIVES!
