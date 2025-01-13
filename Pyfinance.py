#!/usr/bin/env python3
import sys
import yfinance as yf
from PIL import Image
import requests
from io import BytesIO
import PIL.ImageOps as ImageOps


def make_ascii(url, max_width=28, max_height=28, pixel_width=1):
    chars = "$@B%8&WM#*oahkav9 "  # ASCII gradient
    response = requests.get(url)
    img = ImageOps.invert(Image.open(BytesIO(response.content)).convert("L"))  # Convert to grayscale and invert

    # Calculate new dimensions while preserving aspect ratio
    aspect_ratio = img.height / img.width
    new_width = max_width
    new_height = int(max_width * aspect_ratio)

    if new_height > max_height:
        new_height = max_height
        new_width = int(max_height / aspect_ratio)

    img = img.resize((new_width, new_height))  # Resize with updated dimensions

    # Generate ASCII art
    for y in range(0, img.height, pixel_width):  # Apply pixel_width to both dimensions
        row_chars = []
        for x in range(0, img.width, pixel_width):
            final = img.getpixel((x, y))
            index = final * len(chars) // 256  # Map 0–255 to 0–len(chars)-1
            row_chars.append(chars[index])
        print("".join(row_chars))
        
def main():
    # args = sys.argv[1:]
    # if not args:
    #      print("No arguments provided!")
    # else:
    #     print("Arguments received:")
    #     for i,arg in enumerate(args, start=1): #Loop tickers (so far)
    #         print(args)
    #         print("Ticker " + str(i) + ": ")
    #         url = "https://raw.githubusercontent.com/davidepalazzo/ticker-logos/main/ticker_icons/" + sys.argv[i] + ".png" #make_ascii URL
            
    #         make_ascii(url)
            
    #         ticker(arg) #get ticker info
        print(TF("HIMS"))
def ticker(ticker):
    dat = yf.Ticker(ticker)
    #print(dat.calendar) 
    daily_change = dat.info['currentPrice'] - dat.info['open']
    daily_percent_change = (daily_change / dat.info['open']) * 100
    change = False
    print('\n', dat.info['shortName'], '\n',
      "Headquarters:", dat.info['city'], dat.info['state'], '\n',
      "Industry:", dat.info['industry'], '\n',
      "Daily Change: $", f"{daily_change:.3f}","/",f"{daily_percent_change:.3f}%", '\n',
      "Current Price: $", f"{dat.info['currentPrice']:.3f}", '\n',
      "Revenue Growth:", f"{dat.info['revenueGrowth'] * 100:.3f}%", '\n',
      "Current Ratio:", f"{dat.info['currentRatio']:.3f}", '\n',
      "Total Debt: $", f"{dat.info['totalDebt']:.3f}", '\n',
      "Gross Margins:", f"{dat.info['grossMargins'] * 100:.3f}%", '\n',
      "Operating Margins:", f"{dat.info['operatingMargins'] * 100:.3f}%", '\n',
      "Forward PE:", f"{dat.info['forwardPE']:.3f}", '\n',
      "52-Week Change:", f"{dat.info['52WeekChange'] * 100:.3f}%", '\n',
      "Market Capitalization: $", f"{dat.info['marketCap']:.3f}", '\n',
      "Enterprise Value: $", f"{dat.info['enterpriseValue']:.3f}", '\n',
      "Free Cash Flow: $", f"{dat.info['freeCashflow']:.3f}", '\n',
      "Return on Assets (ROA):", f"{dat.info['returnOnAssets'] * 100:.3f}%", '\n',
      "Trailing EPS:", f"{dat.info['trailingEps']:.3f}", '\n',
      "Revenue Per Share: $", dat.info['revenuePerShare'], '\n',
      "Operating Cash Flow: $", dat.info['operatingCashflow'], '\n',
      "Shares Outstanding:", dat.info['sharesOutstanding'], '\n'
)
    if(daily_percent_change>=0):
        change = True
        
def TF(ticker):
    dat = yf.Ticker(ticker)
    daily_change = dat.info['currentPrice'] - dat.info['previousClose']
    change = False
    if(daily_change>=0):
        change = True
    return change
        



if __name__ == "__main__":
    main()
    
    
    
