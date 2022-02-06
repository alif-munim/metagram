
## Installing

1. Install dependencies

```
npm i && cd client && npm i && cd ..
```

2. Create variables.env file and replace values with yours

```
NODE_ENV=development
DATABASE="Mongodb Connection String"
JWT_KEY="secretkey"
EMAILUSER="example@gmail.com"
EMAILPASS="example"
HOST="your ip eg. http://192.168.0.14:5000"
ENABLE_SEND_EMAIL="true or false" // false if you don't want to set it up
TEST_DATABASE="testing db"
```

3. Go into `client/src/_services/socketService.js` and replace

```
window.location.hostname
```

with your local IP address on port 5000 eg.

```
192.168.0.14:5000
```

4. Run project

```
npm run dev
```

## Contribute

Show your support by ⭐ the project.

## Demo 
https://www.youtube.com/watch?v=ybtiKRVBTjU

## Link To Devpost
https://devpost.com/software/metagram?ref_content=my-projects-tab&ref_feature=my_projects

## Inspiration
We were inspired by the Instagram app, which set out to connect people using photo media. We believe that the next evolution of connectivity is augmented reality, which allows people to share and bring creations into the world around them. This revolutionary technology has immense potential to help restore the financial security of small businesses, which can no longer offer the same in-person shopping experiences they once did before the pandemic.

## What It Does
Metagram is a social network that aims to restore the connection between people and small businesses. Metagram allows users to scan creative works (food, models, furniture), which are then converted to models that can be experienced by others using AR technology.

## How we built it
We built our front-end UI using React.js, Express/Node.js and used MongoDB to store user data. We used Echo3D to host our models and AR capabilities on the mobile phone. In order to create personalized AR models, we hosted COLMAP and OpenCV scripts on Google Cloud to process images and then turn them into 3D models ready for AR.

Challenges we ran into
One of the challenges we ran into was hosting software on Google Cloud, as it needed CUDA to run COLMAP. Since this was our first time using AR technology, we faced some hurdles getting to know Echo3D. However, the documentation was very well written, and the API integrated very nicely with our custom models and web app!

Accomplishments that we're proud of
We are proud of being able to find a method in which we can host COLMAP on Google Cloud and also connect it to the rest of our application. The application is fully functional, and can be accessed by clicking here.

## What We Learned
We learned a great deal about hosting COLMAP on Google Cloud. We were also able to learn how to create an AR and how to use Echo3D as we have never previously used it before, and how to integrate it all into a functional social networking web app!

## Next Steps for Metagram
[ ] Improving the web interface and overall user experience  
[ ] Scan and upload 3D models in a more efficient manner

## Research
Small businesses are the backbone of our economy. They create jobs, improve our communities, fuel innovation, and ultimately help grow our economy! For context, small businesses made up 98% of all Canadian businesses in 2020 and provided nearly 70% of all jobs in Canada [1].

However, the COVID-19 pandemic has devastated small businesses across the country. The Canadian Federation of Independent Business estimates that one in six businesses in Canada will close their doors permanently before the pandemic is over. This would be an economic catastrophe for employers, workers, and Canadians everywhere.

Why is the pandemic affecting these businesses so severely? We live in the age of the internet after all, right? Many retailers believe customers shop similarly online as they do in-store, but the research says otherwise.

The data is clear. According to a 2019 survey of over 1000 respondents, consumers spend significantly more per visit in-store than online [2]. Furthermore, a 2020 survey of over 16,000 shoppers found that 82% of consumers are more inclined to purchase after seeing, holding, or demoing products in-store [3].

It seems that our senses and emotions play an integral role in the shopping experience. This fact is what inspired us to create Metagram, an AR app to help restore small businesses.

## References
[1] https://www150.statcan.gc.ca/n1/pub/45-28-0001/2021001/article/00034-eng.htm  
[2] https://www.forbes.com/sites/gregpetro/2019/03/29/consumers-are-spending-more-per-visit-in-store-than-online-what-does-this-man-for-retailers/?sh=624bafe27543  
[3] https://www.businesswire.com/news/home/20200102005030/en/2020-Shopping-Outlook-82-Percent-of-Consumers-More-Inclined-to-Purchase-After-Seeing-Holding-or-Demoing-Products-In-Store  
