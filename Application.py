import argparse
import collections

import sys

from DeckboxCardEntry import DeckboxCardEntry
from DeckboxEntry import DeckboxEntry
import csv
from collections import namedtuple
try:
    from itertools import imap
except ImportError:  # Python 3
    imap = map


# Count,
# Tradelist Count,
# Name,
# Edition,
# Card Number,
# Condition,
# Language,
# Foil,
# Signed,
# Artist Proof,
# Altered Art,
# Misprint,
# Promo,
# Textless,
# My Price,
# Type,
# Cost,
# Rarity,
# Price,
# Image URL

def parseInt(s):
    try:
        return int(s)
    except ValueError:
        return 0

def main():
    parser = argparse.ArgumentParser(description='Eliminate duplicate entries from deckbox.org card lists')

    parser.add_argument("-i", "--inputFileName", help="Path to the exported file.")
    parser.add_argument("-o", "--outputFileName", help="Path where the result should be stored .")
    args = parser.parse_args()

    outputFileName = args.outputFileName
    inputFileName = args.inputFileName

    print ("reading data from " + str(inputFileName))
    print ("writing result to " + str(outputFileName))

    reader = csv.DictReader(open(inputFileName))
    dictResults = {}

    parseCSV(dictResults, reader)
    writeCSV(dictResults, outputFileName)


def writeCSV(dictResults, outputFileName):
    with open(outputFileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["Count", "Tradelist Count", "Name", "Edition", "Card Number", "Condition", "Language", "Foil", "Signed",
             "Artist Proof", "Altered Art", "Misprint", "Promo", "Textless", "My Price", "Type", "Cost", "Rarity",
             "Price", "Image URL"])

        for key, value in dictResults.items():
            outputRow = [value.count, value.tradelistCount, key.name, key.edition, key.cardNumber, key.condition,
                         key.language, key.foil, key.signed, key.artistProof, key.alteredArt, key.misprint, key.promo,
                         key.textless, key.myPrice, key.type, key.cost, key.rarity, key.price, key.imageUrl]
            if len(outputRow) == 20:
                writer.writerow(outputRow)
            else:
                print("invalid output row")
                print(outputRow)


def parseCSV(dictResults, reader):
    for row in reader:
        try:
            count = parseInt(row["Count"])
            tradelistCount = parseInt(row["Tradelist Count"])
            name = row["Name"]
            edition = row["Edition"]
            cardNumber = row["Card Number"]
            condition = row["Condition"]
            language = row["Language"]
            foil = row["Foil"]
            signed = row["Signed"]
            artistProof = row["Artist Proof"]
            alteredArt = row["Altered Art"]
            misprint = row["Misprint"]
            promo = row["Promo"]
            textless = row["Textless"]
            myPrice = row["My Price"]
            type = row["Type"]
            cost = row["Cost"]
            rarity = row["Rarity"]
            price = row["Price"]
            imageUrl = row["Image URL"]

            entry = DeckboxCardEntry(name, edition, cardNumber, condition, language, foil, signed, artistProof,
                                     alteredArt, misprint, promo, textless, myPrice, type, cost, rarity, price,
                                     imageUrl)

            if entry not in dictResults:
                # print ("creating new entry")
                # print (entry)
                value = DeckboxEntry(count, tradelistCount)
                dictResults[entry] = value
            else:
                value = dictResults[entry]

                # print ("updated entry: ")
                # print (entry)
                # print ("oldValues: count: " + str(value.count) + " , tradeListCount: " + str(value.tradelistCount))

                value.count = parseInt(count) + parseInt(value.count)
                value.tradelistCount = parseInt(tradelistCount) + parseInt(value.tradelistCount)
                dictResults[entry] = value

                # print ("newvalues: count: " + str(value.count) + " , tradeListCount: " + str(value.tradelistCount))


        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("could not parse row: ")
            print(exc_value)
            print(row)


if __name__ == '__main__': main()
