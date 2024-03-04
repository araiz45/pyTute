import asyncio
import requests 

async def function1():
    print("Function 1 start")
    url = "https://source.unsplash.com/random/1920x1080/?food"
    res = requests.get(url)
    open("araiz-image/img1.jpg", "wb").write(res.content)
    print("Function 1 end")

async def function2():
    print("Function 2 start")
    url = "https://source.unsplash.com/random/1920x1080/?car"
    res = requests.get(url)
    open("araiz-image/img2.jpg", "wb").write(res.content)
    print("Function 2 End")


async def function3():
    print("Function 3 start")
    url = "https://source.unsplash.com/random/1920x1080/?aeroplane"
    res = requests.get(url)
    open("araiz-image/img3.jpg", "wb").write(res.content)
    print("Function 3 end")




async def main():
    l = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(l)
    # await asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()


asyncio.run(main())

