# The sloped keyboard by koreem ahmed 

## Total time 22-31

## Day 1 (3-4 hours) 8/7/2025
Today I began my search about the keyboard and how to make it and the switch types and all the components of the keyboard. I searched on Ram Electronics and Flux (local stores in Egypt), and I found such a large amount of different components that I can use in my keyboard. I found a lot of microcontrollers, but I chose the Pico due to its high speed and the easy way to flash the code on it. I found that the perfect size for me is 75% keyboards to fit on my desk and be easy to move around. Since I am in a boarding school, every week I will be going to school at the beginning of the week and returning home at the end of the week, so I made a small keyboard that can be carried easily. So I made the layout on the key-layout editor and got the DXF file, which I will use in making the top part of my CAD, and then I continued planning for what I want to do. like having OLED displays or RGBs or rotary Encoders.

<img width="1350" height="538" alt="image" src="https://github.com/user-attachments/assets/5cf65b20-db3c-4c48-a13c-b64d5c4cbc22" />

## Day 2 (2-3 hours) 10/7/2025
I made a deep search of the most compatible libraries for KiCad for the OLED display, which must have 4 pins for (VCC, GND, SDA, SCL), and the Pico to match the exact same model I chose on the Flux, the online local store in Egypt, and the switches to have the perfect size and to have the stabilizers needed. Then I downloaded all of them and started making the schematic, and I am halfway through. In the schematic, I made the key matrix and some of the pico pins, like the 16 columns and 6 rows, for my 75% keyboard. Also, I searched for the best 3D files to represent my work in the right way to be able to put it in the CAD files.

<img width="1573" height="661" alt="image" src="https://github.com/user-attachments/assets/d5b3106d-25fd-4739-bff7-c98421024577" />

## Day 3 (3-4 hours) 12/7/2025
I completed the schematic, which was the RGB lights and the 2 OLED displays and the rest of the Pico pins, and assigned the footprints for them from the libraries that I downloaded. Then I arranged some of the footprints, like the key matrix and routing them, which was a very difficult mission since it is my second time making a PCB. and took the right measurements for real life to make the PCB more accurate and more likely to be made in real life. So I checked by running a DCR on the PCB to check for design errors or electric ones.

<img width="672" height="569" alt="image" src="https://github.com/user-attachments/assets/5a1dab9b-baf1-41a7-a53a-510c1dbb7d56" />

## Day 4 (4-5 hours) 15/7/2025
I arranged all the parts of the PCB, and I saw my keyboard in the PCB and imagined how good it will be, so I ran a DCR, and I didn't find any errors except the ones for overlapping footprints. Arranging the parts and the components and routing them was just a lot of work since my keyboard has 84 keys and 84 LEDs and 2 OLED displays and 1 RP Pico. All these components made the routing more difficult, but thank god I did it faster than I thought it would take. I exported my PCB as a step file to put it in the CAD to test if it will fit in real life or not. Then I searched for the GREB files and how to make them and what they are used for, and I decided to make it the next day.

<img width="1470" height="558" alt="image" src="https://github.com/user-attachments/assets/6c34c026-0e9c-4527-b8e5-8afea82f9253" />
<img width="1897" height="850" alt="image" src="https://github.com/user-attachments/assets/6a278f8b-30e8-4fe6-bde4-176ef7b6a32c" />

## Day 5 (1-2) 16/7/2025
after the long search about how to make a grep file and how to use it properly and how to drill its files and how it works. I tested my Gerber file by putting it on the website of the partner of the Hack Club in making the PCBs, JLCpcb. I tried to upload the file, and it worked, and I found that the LEDs that I will use are so cheap there, so I continued in the shipping steps until I reached the last page, so I went to check the price, and I put it in the BOM to make it more complete. So I made the table as a CSV file to make it easy to read.

<img width="1837" height="784" alt="image" src="https://github.com/user-attachments/assets/c56c7e30-3d0b-430e-810a-269c7c00cb49" />

## Day 6 (3-4) 19/7/2025
I began my 3D designing and made a simple bottom case with a good thickness and a huge triangle in the bottom to make the keyboard sloped with 6.5 deg, which is the best angle for my hand and the one that I found relaxing and charming. So it became one part (the bottom one). I made it fit by calculating the dimensions of the PCB from KiCad and putting it in Onshape while making the top part in the hole, which you might like, so I checked again to ensure they were identical and fit together then.

<img width="933" height="477" alt="image" src="https://github.com/user-attachments/assets/9b1708c1-07f9-4048-b114-be40c8ceb03c" />

## Day 7 (2-3) 20/7/2025
I imported the DXR sketch for the top part and added a square for the OLED display and a hole. I poured all this in, having a good top part that could fit perfectly. The bottom part for the pico was standing on the floor of the second floor. All this made my top part have a lot of work, and I gave it all my creativity. Then exported it and assembled it with the bottom part to check if they were good and fitting together, and they were. As shown in this photo, the two parts are working with each other and fit together. So when I assemble in real life, it will be much easier to do.

<img width="1325" height="646" alt="Screenshot 2025-08-05 160413" src="https://github.com/user-attachments/assets/a5d7613b-551b-4bbb-a856-43406e6866f3" />

## Day 8 (3-4) 23/7/2025
I exported the PCB in STEP to put it in the CAD, and it wasn't good enough, and there were some bad dimensions that were made. So I changed it and searched about the real size and compared it with the store and the CAD, and I found that I must change it. So I changed it, and it was beautiful, and I inserted it in the whole pad assembly and checked on everything to make sure that everything was good and working, and if there were any other problems, then I exported the whole file and changed all the things that wanted to be changed, like the name, size, and font. Then I made the BOM and organized the files in folders.

<img width="1215" height="772" alt="image" src="https://github.com/user-attachments/assets/e276cb9e-f810-4cff-ae3b-f4e74dcecb1e" />

## Day 9 (1-2) 26/7/2025
I put some details in the CAD, like the writing and adding some shapes, curves, and text—all this. and I changed the BOM for the last time, making sure of the prices. on different stores on the internet And took all the photos for the submission and inserted it in the journal file to document what I did. I finished the whole case, making some parts out of it with 5 mm thickness, 2 inside the case and 3 outside it, so it will be so good. and clearly this idea was looking good in the files.

<img width="1021" height="536" alt="image" src="https://github.com/user-attachments/assets/373df4c7-1632-4072-ae8a-d51c65d905f8" />

## Day 10 ( less than 1 hour ) 27/7/2025
I checked on everything and submitted finally my keyboard.

## Day 11 (4 hours) 5/8/2025
i changed alot and submeted for the re-review 😍.
<img width="1851" height="961" alt="image" src="https://github.com/user-attachments/assets/f3520644-f93b-4021-9786-ce2c0277594d" />
