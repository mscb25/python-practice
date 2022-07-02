import asyncio

#working with asyncronous programming
#this function sums numbers

async def sumNumbers(num1, num2):

    print("Summing numbers", num1, "+", num2)
    await asyncio.sleep(1)

    print("End Sum", num1, "+", num2)
    return num1 + num2


#creating an event loop

event_loop = asyncio.get_event_loop()

#just sample numbers
num1 = 4
num2 = 2

#running async function and waiting for completion
#this implementation allows for three calculations. before using code, be sure to plug in numbers

result = event_loop.run_until_complete(asyncio.gather(sumNumbers(num1, num2), sumNumbers(num1, num2), sumNumbers(num1, num2))

print("Sum of two numbers:", num1, "+", num2, "=", result)

#closing loop

event_loop.close
