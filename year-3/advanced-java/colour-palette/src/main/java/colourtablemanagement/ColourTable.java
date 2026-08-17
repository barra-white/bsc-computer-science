package colourtablemanagement;

public class ColourTable {
    // variable for colour palette
    private Colour[] colourPalette;

    // constructor
    public ColourTable(int paletteSize) {
        this.colourPalette = new Colour[this.validatePaletteSize(paletteSize)];
    }

    // constructor that throws exception if no size is specified
    public ColourTable() {
        throw new IllegalArgumentException("Must enter a palette size");
    }

    // getter method to return palette size
    public int getPaletteSize() {
        return this.colourPalette.length;
    }

    // get method to get a colour at specified index
    public Colour getColourAtIndex(int index) {
        return this.colourPalette[index];
    }

    // method to add colours to the palette
    public void add(Colour colour) {
        int index;
        for (index = 0; index < this.getPaletteSize(); index++) {
            if (this.contains(colour)) {
                throw new IllegalArgumentException("Colour is already in the palette");
            }
            if (this.getColourAtIndex(index) == null) {
                this.colourPalette[index] = colour;
                return;
            }
        }
        throw new IllegalStateException("There is no space in the colour palette to add another colour");
    }

    // method to check if a colour is already contained in the palette
    public boolean contains(Colour colour) {
        for (int i = 0; i < this.getPaletteSize(); i++) {
            if (this.getColourAtIndex(i) == null) {
                continue;
            }
            if (this.getColourAtIndex(i).equals(colour)) {
                return true;
            }
        }
        return false;
    }

    // method to validate palette size
    public int validatePaletteSize(int size) {
        if (isPowerOf2(size) && size > 1 && size < 1025) {
            return size;
        }
        else {
            throw new IllegalArgumentException("Palette size must be between 2 and 1024, and must be a power of 2");
        }
    }

    // method to check if a value is to the power of 2 (bitwise operation)
    public boolean isPowerOf2(int size) {
        return (size & (size - 1)) == 0;
    }

    // method to count number of empty space in palette
    public int getFreePaletteSpace() {
        int spaceCounter = 0;
        for (Colour col : colourPalette) {
            if (col == null) {
                spaceCounter++;
            }
        }
        return spaceCounter;
    }

    // string representation of the colour palette
    public String toString() {
        StringBuilder palette = new StringBuilder();
        palette.append("Colour Palette {\n\n");
        palette.append("\tTotal Palette Size: ").append(this.getPaletteSize()).append("\n");
        palette.append("\tNo. of Colours in Palette: ").append(this.getPaletteSize() - this.getFreePaletteSpace()).append("\n");
        palette.append("\tFree Palette Space: ").append(this.getFreePaletteSpace()).append("\n");
        palette.append("\tColours:\n");

        for (int i = 0; i < this.getPaletteSize(); i++) {
            if (this.getColourAtIndex(i) != null) {
                String colourString = this.getColourAtIndex(i).toString(); // N.B. regex for tab at beginning of each line adapted from chatGPT
                colourString = colourString.replaceAll("(?m)^", "\t\t"); // add a tab at the beginning of each line
                palette.append(colourString); // append to string representation
            }
        }
        palette.append("}");
        return palette.toString(); // convert StringBuilder() to String + return
    }
}
