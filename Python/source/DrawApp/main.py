import drawTool as d


def main():
    
    print("Increment")
    print("Draw stars")
    d.drawStarsIncrement(10, "*")
    print("\n")
    print("")
    
    print("Decrement")
    print("Draw stars")
    d.drawStarsDecrement(5, "*")

    print("\n\n")
    print("Triangle\n")
    d.drawPyramid(7)
    print("\n")
    print("")

    #a.normalForLoop(5, "#")
    #a.normalForLoopTwo(5, "*")

if __name__ == "__main__":
    main()
